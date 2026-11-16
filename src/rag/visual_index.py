"""Build index V: vision-model transcription of tables, charts, diagrams and infographics.

Run: python -m src.rag.visual_index [--pages 1-100] [--workers 6] [--skip-extract]

1. Render each PDF page (PyMuPDF, 144 dpi) to work/pages_hd/pNNN.png.
2. Send page image + the Day 6 text layer (hint only) to VISION_MODEL; ask for one JSON
   element per visual block (type, title, region, unit, full transcription of values).
3. Each element -> one chunk `sach-trang-tmdt-2023:pNN:V<k>` with page, region and image path
   for verification; embedded with the SAME Day 6 model and stored in the SAME pgvector table
   (strategy 'V'). Text index B from Day 6 is untouched.
Outputs: results/visual/extraction.jsonl (raw model output + cost), results/visual/summary.json
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .common import (PDF_PATH, RESULTS, SOURCE_ID, VISUAL_INDEX, WORK, OpenRouter, embedder,
                     read_json, store, write_json)

OUT = RESULTS / "visual"
PAGES_DIR = WORK / "pages_hd"
DPI = 144

PROMPT = """Bạn là công cụ trích xuất dữ liệu từ ảnh một trang của "Sách trắng Thương mại điện tử Việt Nam 2023" (trang {page}).
Nhiệm vụ: chép lại CHÍNH XÁC mọi khối nội dung trực quan có thông tin trên trang: bảng, biểu đồ (cột, thanh, tròn, đường),
sơ đồ khối/danh sách đánh số trong ô, infographic (ô số liệu lớn kèm mô tả).
Quy tắc:
- Mỗi khối là một phần tử. Ghi tiêu đề đúng như trên trang (kể cả số mục, ví dụ "6.1. ...").
- Biểu đồ: liệt kê TỪNG nhãn với TỪNG giá trị theo dạng "Nhãn — năm/chuỗi: giá trị", kèm đơn vị, chú giải, tiêu đề trục; ghi rõ cột nào là dự báo (*).
- Bảng: chép từng hàng dạng "tên hàng | cột1: giá trị | cột2: giá trị". Giữ nguyên cách viết số tiếng Việt (dấu phẩy thập phân, dấu chấm hàng nghìn).
- Biểu đồ tròn: ghép đúng phần trăm với chú giải dựa vào màu; nếu không chắc, ghi "(ghép màu không chắc chắn)".
- Sơ đồ khối: chép từng ô theo số thứ tự.
- Không suy diễn, không thêm số liệu không có trên ảnh. Bỏ qua ảnh minh họa trang trí, chỉ ghi chúng vào "decorative".
- Text layer dưới đây chỉ để tham khảo chính tả; khi mâu thuẫn, tin vào ảnh.
Trả về JSON: {{"elements":[{{"type":"table|bar_chart|line_chart|pie_chart|combo_chart|diagram|infographic","title":"...","region":"vị trí trên trang, ví dụ 'nửa trên', 'giữa', 'nửa dưới'","unit":"...","content":"..."}}],"decorative":["mô tả ngắn ảnh trang trí"]}}
Nếu trang không có khối trực quan nào, trả {{"elements":[],"decorative":[...]}}.

Text layer (tham khảo):
<<<
{text}
>>>"""


def render_pages(pages: list[int]) -> None:
    import fitz
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    for p in pages:
        out = PAGES_DIR / f"p{p:03d}.png"
        if not out.exists():
            doc[p - 1].get_pixmap(dpi=DPI).save(out)


def day6_pages() -> dict[int, dict]:
    path = Path(os.environ["DAY6_STARTER"]) / "results" / "pages.jsonl"
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    return {r["page"]: r for r in rows}


def extract_page(llm: OpenRouter, page: int, text: str) -> dict:
    img = base64.b64encode((PAGES_DIR / f"p{page:03d}.png").read_bytes()).decode()
    messages = [{"role": "user", "content": [
        {"type": "text", "text": PROMPT.format(page=page, text=text[:6000] or "(trống)")},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}}]}]
    t0 = time.perf_counter()
    try:
        out = llm.chat(messages, temperature=0, response_format={"type": "json_object"})
        raw = out["choices"][0]["message"]["content"]
        parsed = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
        return {"page": page, "status": "ok", "elements": parsed.get("elements", []),
                "decorative": parsed.get("decorative", []), **out["_meta"]}
    except Exception as e:  # recorded, never replaced by fake output
        return {"page": page, "status": "error", "error": f"{type(e).__name__}: {e}",
                "elements": [], "latency_s": round(time.perf_counter() - t0, 2), "cost_usd": 0.0}


def to_chunks(rec: dict, meta6: dict) -> list:
    from day6src.models import Chunk
    chunks = []
    for k, el in enumerate(rec["elements"], 1):
        content = str(el.get("content", "")).strip()
        if not content:
            continue
        title = str(el.get("title", "")).strip()
        header = f"[{el.get('type', 'visual')}] {title}\n(Trang {rec['page']}, {el.get('region', '')}; đơn vị: {el.get('unit') or 'không ghi'})"
        md = {"section": (meta6.get("metadata") or {}).get("section"), "year": 2023, "language": "vi",
              "chart_heavy": True, "visual_type": el.get("type"), "title": title,
              "region": el.get("region"), "unit": el.get("unit"),
              "page_image": f"work/pages_hd/p{rec['page']:03d}.png",
              "extractor": rec.get("model"), "index": VISUAL_INDEX}
        chunks.append(Chunk(chunk_id=f"{SOURCE_ID}:p{rec['page']}:V{k}", document_id=SOURCE_ID,
                            source=f"data/{PDF_PATH.name}", page=rec["page"],
                            text=f"{header}\n{content}", metadata=md))
    return chunks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", default="1-100")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--skip-extract", action="store_true", help="chỉ embed lại từ extraction.jsonl")
    args = ap.parse_args()
    a, b = (int(x) for x in args.pages.split("-"))
    pages = list(range(a, b + 1))
    meta = day6_pages()
    raw_path = OUT / "extraction.jsonl"
    model = os.environ.get("VISION_MODEL", "gpt-4o-mini")

    if not args.skip_extract:
        render_pages(pages)
        llm = OpenRouter(model, timeout=180)
        # resume: keep pages already extracted OK by the same model; write each page as it finishes
        OUT.mkdir(parents=True, exist_ok=True)
        done = {}
        if raw_path.exists():
            for l in raw_path.read_text(encoding="utf-8").splitlines():
                r = json.loads(l)
                if r["status"] == "ok" and r.get("model") == model:
                    done[r["page"]] = r
        todo = [p for p in pages if p not in done]
        t0 = time.perf_counter()
        lock = threading.Lock()

        def work(p):
            r = extract_page(llm, p, meta.get(p, {}).get("text", ""))
            r["model"] = model
            with lock:
                done[p] = r
                with raw_path.open("w", encoding="utf-8") as f:
                    for k in sorted(done):
                        f.write(json.dumps(done[k], ensure_ascii=False) + "\n")
                print(f"  p{p}: {r['status']} {len(r['elements'])} khối {r.get('error', '')[:120]}", flush=True)
            return r

        with ThreadPoolExecutor(args.workers) as ex:
            recs = list(ex.map(work, todo))
        print(f"extract: {len(recs)} trang, {time.perf_counter() - t0:.0f}s, "
              f"${sum(r['cost_usd'] for r in recs):.4f} (tương đương trả phí ${sum(r.get('equiv_cost_usd', 0) for r in recs):.4f}), lỗi {sum(r['status'] != 'ok' for r in recs)}")

    recs = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    chunks = [c for r in recs if r["status"] == "ok" for c in to_chunks(r, meta.get(r["page"], {}))]
    emb, st = embedder(), store()
    st.create_schema()
    too_long = sum(emb.count_tokens(c.text) > emb.max_seq_length for c in chunks)
    t0 = time.perf_counter()
    vectors = emb.embed_documents([c.text for c in chunks])
    embed_s = time.perf_counter() - t0
    st.upsert(VISUAL_INDEX, chunks, vectors)
    removed = st.prune(VISUAL_INDEX, [SOURCE_ID], [c.chunk_id for c in chunks])
    types: dict[str, int] = {}
    for c in chunks:
        types[c.metadata["visual_type"]] = types.get(c.metadata["visual_type"], 0) + 1
    summary = {
        "vision_model": model, "dpi": DPI, "pages_requested": len(pages),
        "pages_sent": len(recs), "pages_error": [r["page"] for r in recs if r["status"] != "ok"],
        "pages_with_visuals": sorted({c.page for c in chunks}),
        "pages_without_visual_elements": [r["page"] for r in recs if r["status"] == "ok" and not r["elements"]],
        "chunks": len(chunks), "by_type": types, "chunks_over_512_tokens_truncated_in_embedding": too_long,
        "extract_cost_usd": round(sum(r.get("cost_usd", 0) for r in recs), 4),
        "extract_equiv_paid_cost_usd": round(sum(r.get("equiv_cost_usd", 0) for r in recs), 4),
        "extract_seconds_total_latency": round(sum(r.get("latency_s", 0) for r in recs), 1),
        "rate_limit_wait_s": round(sum(r.get("rate_limit_wait_s", 0) for r in recs), 1),
        "extract_prompt_tokens": sum(r.get("prompt_tokens", 0) for r in recs),
        "extract_completion_tokens": sum(r.get("completion_tokens", 0) for r in recs),
        "embed_seconds": round(embed_s, 1), "pruned_old_chunks": removed,
        "db_rows_V": st.count(VISUAL_INDEX),
    }
    write_json(OUT / "summary.json", summary)
    with (OUT / "chunks_V.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps({"chunk_id": c.chunk_id, "page": c.page, "text": c.text, "metadata": c.metadata},
                               ensure_ascii=False) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
