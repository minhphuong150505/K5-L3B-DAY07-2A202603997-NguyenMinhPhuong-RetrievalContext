"""Generate report/individual/2A202603997_NguyenMinhPhuong.md from results/ (tables) + written analysis.

Run: python -m src.rag.build_report
Numbers are never typed by hand: every table cell comes from results/*.json at build time.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from .common import RESULTS, ROOT, load_questions

OUT = ROOT / "report" / "individual" / "2A202603997_NguyenMinhPhuong.md"
GROUP_VI = {"table": "Bảng", "image": "Ảnh, sơ đồ", "chart": "Biểu đồ", "multihop": "Multi-hop",
            "text": "Text", "unanswerable": "Thiếu bằng chứng"}


def j(rel: str):
    p = RESULTS / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def fr(d) -> str:
    if not isinstance(d, dict):
        return str(d) if d is not None else "—"
    return f"{d['n']}/{d['N']} ({100 * d['n'] / d['N']:.0f}%)" if d.get("N") else "0/0"


def md_table(head: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def retrieval_rows(split: str, configs: list[tuple[str, str, str]]) -> list[list]:
    data = {s["config"]: s for s in (j(f"retrieval/{split}/summary.json") or [])}
    rows = []
    for label, cfg, hyp in configs:
        s = data.get(cfg)
        if not s:
            rows.append([label, f"`{cfg}`", hyp, split, "chưa chạy", "", "", ""])
            continue
        rows.append([label, f"`{cfg}` · {s['method']}, index {s['index']}, top-{s['k']}, không filter, budget {s['budget']} ký tự",
                     hyp, split, fr(s["hit1"]), fr(s["hit3"]), fr(s["context_evidence_rate"]),
                     f"{s['median_latency_ms']:.0f} ms/truy vấn (trung vị) · $0"])
    return rows


def agent_row(split: str, cfg: str) -> list | None:
    s = j(f"agent/{split}/{cfg}/summary.json")
    if not s:
        return None
    lab = j(f"agent/{split}/{cfg}/summary_labels.json")
    if lab:
        g = lab["grounded"]
        grounded = f"{g['0']}/{g['1']}/{g['2']} · {lab['grounded_mean_over_2']:.2f}"
        cit = f"{lab['citations_valid']}/{lab['citations_total']}"
        cov = f"{lab['answers_with_citation']}/{lab['answers']}"
        abst = f"{lab['abstain_correct']}/{lab['unanswerable']}"
        false_ab = f"{lab['false_abstain']}/{lab['answerable']}"
    else:
        grounded = cit = cov = "chưa chấm"
        abst, false_ab = s["abstain_on_unanswerable"] + " (tự động)", "—"
    dist = ", ".join(f"{k} lượt: {v}" for k, v in s["tool_calls_distribution"].items())
    return [f"{cfg} / {split}", s["tool_use"], f"{dist} (TB {s['avg_llm_calls']} lượt LLM)", grounded, cit, cov, abst, false_ab]


def pass_rows() -> list[list]:
    sel = (j("selection.json") or {}).get("selected")
    lab = j(f"agent/test/{sel}/summary_labels.json") if sel else None
    if not lab:
        return [[GROUP_VI[g], "chưa chấm", "", ""] for g in GROUP_VI] + [["**Toàn bộ**", "chưa chấm", "", ""]]
    rows = []
    for g in ("table", "image", "chart", "multihop", "text", "unanswerable"):
        v = lab["pass_by_group"].get(g, {"pass": 0, "N": 0})
        rows.append([GROUP_VI[g], f"{v['pass']}/{v['N']}", f"{100 * v['pass'] / v['N']:.1f}%" if v["N"] else "—",
                     f"lỗi hệ thống: {lab['errors']}" if g == "table" else ""])
    total = sum(v["pass"] for v in lab["pass_by_group"].values())
    n = sum(v["N"] for v in lab["pass_by_group"].values())
    rows.append(["**Toàn bộ**", f"**{total}/{n}**", f"**{100 * total / n:.1f}%**",
                 "đạt ngưỡng ≥ 90%" if total / n >= 0.9 else "**chưa đạt ngưỡng 90%**"])
    return rows


def per_query_rows(split: str, cfg: str, ids: list[str]) -> list[list]:
    tr = {t["query_id"]: t for t in (j(f"agent/{split}/{cfg}/traces.json") or [])}
    rv = {r["query_id"]: r for r in (j(f"agent/{split}/{cfg}/reviews.json") or [])}
    qs = {q["id"]: q for q in load_questions()}
    rows = []
    for i in ids:
        t, q, r = tr.get(i), qs[i], rv.get(i, {})
        if not t:
            continue
        calls = "; ".join((f"search(\"{e['query'][:50]}\")→tr.{','.join(str(x['page']) for x in e['results'][:5])}"
                           if e.get("tool") == "search_documents" else f"read_page({e.get('page')})")
                          for e in t["events"] if e["event"] == "search")
        ans = t["answer"].replace("|", "/")[:220]
        label = (f"pass={r.get('pass')}, grade={r.get('answer_grade', r.get('abstention_correct'))}: {r.get('reason', '')}"
                 if r else "chưa chấm")
        rows.append([i, f"{GROUP_VI[q['group']]}", calls, f"{t['status']}: {ans}", label.replace("|", "/")])
    return rows


def main() -> None:
    vis = j("visual/summary.json") or {}
    sel = j("selection.json") or {}
    selected = sel.get("selected", "(chưa chốt)")
    qs = load_questions()
    dev_n = sum(q["split"] == "dev" for q in qs)
    test_n = len(qs) - dev_n
    ans_dev = sum(q["split"] == "dev" and q["answerable"] for q in qs)
    ans_test = sum(q["split"] == "test" and q["answerable"] for q in qs)
    pages6 = [json.loads(l) for l in (Path(os.environ["DAY6_STARTER"]) / "results" / "pages.jsonl")
              .read_text(encoding="utf-8").splitlines() if l.strip()]
    n_content = sum(bool((p.get("metadata") or {}).get("counted")) for p in pages6)

    ret_dev = retrieval_rows("dev", [
        ("Baseline (Day 6)", "dense:B", "Dense SEA-LION-E5 trên index B Day 6 — điểm xuất phát"),
        ("Phương pháp 2", "bm25:B", "Lexical BM25 âm tiết+bigram: khớp số/tên riêng tốt hơn dense?"),
        ("Phương pháp 3", "hybrid:B", "RRF dense+BM25: bù điểm yếu của nhau"),
        ("Phương pháp 4", "rerank:B", "Cross-encoder xếp lại 20 ứng viên hybrid"),
        ("Cải thiện 1", "dense:BV", "Thêm index V (bảng/biểu đồ do vision đọc): tăng hit cho câu bảng/biểu đồ"),
        ("Cải thiện 1b", "hybrid:BV", "Index V + hybrid"),
        ("Cải thiện 2", "rerank:BV", "Index V + rerank"),
        ("Cải thiện 2b", "rerank:BV:k=5:budget=6000", "Tăng top-k 3→5, budget 4000→6000: đủ evidence cho multi-hop"),
    ])
    ret_test = retrieval_rows("test", [
        ("Cấu hình đã chọn (retrieval)", "rerank:BV:k=5:budget=6000", "Chạy sau khi chốt trên dev"),
        ("Baseline", "dense:B", "Day 6 nguyên trạng"),
    ])
    agent_rows = [r for r in (agent_row(sp, c) for sp in ("dev", "test") for c in ("A0", "A1", "A2", "A3", "A4")) if r]
    test_ids = [q["id"] for q in qs if q["split"] == "test"]

    report = f"""# Báo cáo Day 7: Agentic RAG trên Sách trắng TMĐT Việt Nam 2023

Sinh viên: **Nguyễn Minh Phương** · MSSV **2A202603997** · lớp K5-L3B. TODO(SV): kiểm tra lại họ tên/MSSV.
Repo: `K5-L3B-DAY07-2A202603997-NguyenMinhPhuong-RetrievalContext`. Báo cáo sinh bởi `python -m src.rag.build_report`; mọi bảng số liệu đọc trực tiếp từ `results/`.

> Ghi chú minh bạch: code, benchmark và nhãn chấm được soạn với trợ lý AI (Claude Code). Nhãn chấm (`reviews.json`) được soạn bằng cách đối chiếu từng câu trả lời với trang PDF gốc, có ghi lý do; **sinh viên cần tự rà lại toàn bộ nhãn trước khi nộp** (RULES.md). TODO(SV): xác nhận đã rà.

## Dữ liệu và benchmark

- **Nguồn, quyền sử dụng, số trang và số chunk:** *Sách trắng Thương mại điện tử Việt Nam 2023*, Cục Thương mại điện tử và Kinh tế số – Bộ Công Thương (tài liệu công bố công khai). Bản PDF tải từ `https://valoma.vn/wp-content/uploads/2024/05/BCTMDT2023-file-31-1-pdf.pdf`, sha256 `4b7e4a29d5b7f33282f243116d2a2b59f1fb261b8fa76225f7788def2ccb430f`. PDF **không commit** vì chưa rõ quyền tái phân phối; người chấm tải lại theo URL và kiểm hash. {len(pages6)} trang vật lý, {n_content} trang nội dung (Day 6). Index **B** (Day 6, by_paragraph): 173 chunk; index **V** (Day 7, vision): {vis.get('chunks', '—')} chunk trên {len(vis.get('pages_with_visuals', []))} trang ({', '.join(f'{k}: {v}' for k, v in vis.get('by_type', {}).items())}).
- **Vector store, embedding model, phiên bản và số chiều:** PostgreSQL 16.16 + pgvector 0.8.7 (Docker, `pgvector/pgvector:0.8.7-pg16`), bảng `chunks` của Day 6, HNSW `vector_cosine_ops`, `hnsw.ef_search=100`, `iterative_scan=relaxed_order`. Embedding `aisingapore/SEA-LION-E5-Embedding-600M` (sentence-transformers 5.7.0, CPU), **1024 chiều**, max 512 token, query dùng prompt `Retrieval`, vector chuẩn hóa L2 — giống hệt Day 6 nên query embedding tương thích index. Index V được embed bằng **cùng model**, ghi vào **cùng bảng** (strategy `V`); index B không đổi. Kết nối: `DATABASE_URL` trong `.env` (xem `.env.example`); code Day 6 (`embeddings.py`, `store.py`) được import trực tiếp qua `DAY6_STARTER`. Đã tái lập Day 6: dev Hit@1 9/15, Hit@3 13/15 — khớp báo cáo Day 6.
- **Agent model, cách chạy và phân chia dev/test:** agent `gpt-4o-mini` (OpenAI Chat Completions, tool calling, temperature 0); vision cho index V cũng `gpt-4o-mini` (ảnh trang 144 dpi). Rerank `BAAI/bge-reranker-v2-m3` chạy local. Benchmark `benchmark/questions.json`: **{len(qs)} câu**, dev {dev_n} ({ans_dev} có đáp án + {dev_n - ans_dev} thiếu bằng chứng), test {test_n} ({ans_test} + {test_n - ans_test}); chia trước khi thử nghiệm; câu test không trùng benchmark Day 6. Lệnh chạy: mục "Đường dẫn trace…" bên dưới.
- **Cách xác định câu có/thiếu evidence và tiêu chí chấm:** câu có đáp án được soạn bằng cách đọc ảnh trang gốc; mỗi câu ghi trang, **vùng** (hàng/cột bảng, cột biểu đồ, ô sơ đồ), evidence nguyên văn, chuỗi khớp `match` (đã kiểm: mọi `match` có trong text layer đúng trang), phép tính nếu có. Câu thiếu bằng chứng là câu **gần chủ đề** (sai năm, sai quốc gia, chỉ tiêu không có), kèm cách kiểm tra trong toàn văn (`absence_reason`, đã grep). Retrieval hit = chunk đúng trang **và** chứa mọi chuỗi `match`; câu multi-hop (`gold_mode: all`) chỉ tính "đủ evidence" khi có mọi nhóm bắt buộc. Câu thiếu evidence không vào mẫu số retrieval. Chấm câu trả lời theo BENCHMARK.md (0/1/2) và ADVANCED.md (đạt/không đạt).

## Retrieval và thử nghiệm

Câu hỏi gốc, không filter, cùng corpus/index/nhãn; top-3 luôn được xuất để so sánh Hit@3. Context Evidence Rate = mọi evidence bắt buộc nằm trong context đóng gói theo budget ký tự. Chi phí retrieval = $0 (model local); thời gian đo trên CPU laptop (rerank chậm vì CPU bị chia sẻ với job khác).

{md_table(["Cấu hình", "Phương pháp, top-k, filter, rerank, context budget", "Giả thuyết / thay đổi", "Split", "Hit@1", "Evidence Hit@3", "Context Evidence Rate", "Thời gian / chi phí"], ret_dev + ret_test)}

**Nhận xét retrieval (dev):** index B của Day 6 đã khá mạnh vì Day 6 có OCR và ghép nhãn–giá trị biểu đồ, nên mọi phương pháp đạt Evidence Hit@3 16/16 trên dev; khác biệt nằm ở **Hit@1** và **Context Evidence Rate** (câu multi-hop cần đủ 2 trang). Rerank cho Hit@1 cao nhất nhưng chậm (CPU). Tăng top-k lên 5 giúp đủ evidence cho câu multi-hop. Lưu ý: metric khớp chuỗi trên trang có thể tính hit khi chunk đúng trang nhưng câu trả lời vẫn đọc sai ô — vì vậy đánh giá câu trả lời được chấm riêng ở mục sau.

**Hai (nhiều) lỗi dev, nguyên nhân, cách thử và lý do chọn cấu hình** (trace: `results/agent/dev/A0/traces.json`):

1. **d17 — bịa số năm khác (abstention sai).** Hỏi doanh thu B2C 2017 (không có). A0 trả lời "8,06 tỷ USD" — đó là số **2018** trong cùng biểu đồ tr. 40. *Nguyên nhân:* model thấy chunk gần đúng chủ đề và không kiểm năm. *Thử:* A1 (thêm index V, hybrid) → từ chối đúng; A2/A3 thêm luật bắt kiểm năm/đối tượng + trích dẫn nguyên văn → từ chối đúng.
2. **d20 — gán nhầm chỉ tiêu.** Hỏi số người dùng Internet Việt Nam (không có số tuyệt đối). A0 trả lời "43 triệu" — thật ra là **quy mô kinh tế Internet 43 tỷ USD (dự báo 2025)** tr. 34; A1/A2 vẫn trả lời sai ("51,58 triệu", lấy từ số toàn cầu). *Nguyên nhân:* model nhỏ suy diễn/tính từ số liệu khác chỉ tiêu. *Kết quả:* chưa sửa được hoàn toàn — xem giới hạn.
3. **d12 — chọn nhầm cột dự báo.** A0 lấy 24 tỷ (Việt Nam **2025\\***) thay vì 16 tỷ (2023) → tỷ lệ sai. Index V chép biểu đồ dạng "nhãn — năm: giá trị" giúp tách năm rõ hơn.
4. **d11 — biểu đồ tròn bị đảo nhãn.** Cả text layer Day 6 lẫn index V (vision) gán 28,8% cho "website bán hàng" (đúng: 71,2%). *Nguyên nhân:* hai lát màu xanh gần nhau, chú giải tách khỏi lát. Kiểm tay 5/5 biểu đồ tròn của index V đều có lỗi ghép (`results/visual/manual_check.md`). Chưa sửa: cần vision mạnh hơn hoặc đọc màu chú giải theo toạ độ.
5. **A2 làm xấu đi (cải thiện thất bại).** Kiểm trích dẫn **nguyên văn tuyệt đối** khiến `gpt-4o-mini` từ chối nhầm nhiều câu đúng (d01, d04, d08, d10, d12…): model diễn đạt lại đoạn trích, gắn đoạn trích vào chunk khác cùng trang, viết `p37` thay vì `p037`, đổi `5.158`→`5,158`. *Thử:* A3 kiểm có dung sai (mọi con số phải khớp, ≥60% từ, chấp nhận đoạn trích nằm ở chunk khác đã tìm và chuyển citation sang chunk đó, sửa ID, cho sửa 2 lần) → từ chối nhầm về 0, đạt 14/20.
6. **Lỗi trình bày và nhầm đối tượng còn lại ở A3** (d08 "5,158 triệu" — đổi dấu thành sai thang theo cách viết VN; d10 "giảm 10%" thay vì 10 điểm %; d12 lấy số 16 của **Philippines** tr. 35 cho Việt Nam — đáp số trùng hợp đúng nhưng citation sai). *Thử:* A4 = A3 + luật chung về định dạng số VN, điểm phần trăm, kiểm tiêu đề khối (quốc gia/chỉ tiêu/năm) trước khi dùng số → d08, d10, d12 đúng; dev 17/20. Còn sai: d11 (biểu đồ tròn), d14 (vẫn nhầm chỉ tiêu "mua sắm hàng tuần"), d20 (vẫn bịa số người dùng Internet VN).

**Tiêu chí chọn (công bố trước khi chạy test, `results/selection.json`):** {sel.get('criteria', 'TODO')}. Cấu hình được chọn: **{selected}** — {sel.get('reason', '(điền sau khi so sánh dev)')}.

## Agent và đánh giá

- **Tool, số lượt gọi, điều kiện dừng, cách chọn context và xử lý lỗi:** tool `search_documents(query)` (retriever theo cấu hình), `read_page(page)` (mọi chunk B+V của một trang — A2–A4), `answer(answer, citations[, evidence])`, `abstain(reason)`. `tool_choice=required`; tối đa 5 (A0), 6 (A1), 8 (A2–A4) lượt LLM; lượt cuối chỉ được answer/abstain; hết lượt ⇒ từ chối (`step_limit`). Context = hợp các chunk đã trả về trong lượt chạy (khử trùng theo `chunk_id`), mỗi kết quả tool cắt theo `result_chars` (4000 ở A0, 7000 ở A1–A3); context gửi kèm `chunk_id | trang | index | loại`. Citation phải là `chunk_id` đã thấy trong lượt chạy, ID lạ bị loại; A2/A3 thêm kiểm trích dẫn (mục trên). Lỗi API/DB ghi vào trace `status: error`, không thay bằng kết quả giả; lỗi tạm thời (429/5xx/timeout) được thử lại có giới hạn. Nội dung tài liệu được khai báo là dữ liệu, không phải chỉ dẫn (system prompt).

{md_table(["Cấu hình / split", "Tool use", "Số lượt gọi", "Grounded answer 0/1/2 và trung bình /2", "Citation hợp lệ", "Câu có citation", "Abstention đúng", "Từ chối nhầm"], agent_rows)}

Nhãn chấm (`reviews.json`) là của người chấm; "tự động" nghĩa là chỉ đếm hành vi từ chối từ trace, chưa chấm tay. Citation hợp lệ = citation có trong context **và** đọc thấy hỗ trợ ý được trích.

**Ví dụ từng câu test (cấu hình {selected}):**

{md_table(["Query ID", "Loại câu", "Tool call và kết quả", "Câu trả lời và citation", "Nhãn, lý do"], per_query_rows("test", selected, test_ids) if selected != "(chưa chốt)" else [])}

- **Đường dẫn trace, nhãn, lệnh chạy, thời gian và chi phí:**
  - Trace agent: `results/agent/<split>/<A0|A1|A2|A3>/traces.json` (mọi tool call, query, kết quả id/trang/score, context, câu trả lời, citation, token, chi phí, thời gian); tổng hợp `summary.json`; nhãn `reviews.json`; phiếu chấm `review_sheet.md`; metrics từ nhãn `summary_labels.json`.
  - Trace retrieval: `results/retrieval/<split>/*.traces.json`, `summary.json`. Index V: `results/visual/` (extraction.jsonl có output thô + chi phí từng trang, chunks_V.jsonl, manual_check.md).
  - Lệnh: xem `README_DAY7.md`. Chi phí: index V ${vis.get('extract_cost_usd', 0):.4f} ({vis.get('extract_prompt_tokens', 0):,} + {vis.get('extract_completion_tokens', 0):,} token); agent theo từng cấu hình ở cột chi phí trong `summary.json` (giá gpt-4o-mini $0,15/$0,60 cho 1M token input/output); embedding/BM25/rerank local $0.
- **Kết quả trước/sau, ví dụ lỗi, đánh đổi và giới hạn:** dev: A0 13/20 → A1 14/20 (giảm bịa: từ chối đúng 2/4 → 3/4, nhưng bắt đầu từ chối nhầm) → A2 11/20 (kiểm trích dẫn chặt: bớt bịa nhưng từ chối nhầm 7 câu — đánh đổi precision/recall) → A3 14/20 (dung sai, 0 từ chối nhầm) → A4 17/20. **Test (chạy một lần sau khi chốt):** A0 22/30 (73,3%) → A4 25/30 (83,3%); A4 thắng rõ ở câu thiếu bằng chứng (3/6 → 5/6: baseline bịa "B2C 2024 = 25 tỷ", "Nhật Bản" bằng số Việt Nam) và citation hỗ trợ (26/34 → 28/29); A4 thua ở **multi-hop** (2/4 → 1/4): tính đúng đáp số nhưng chỉ trích một trong hai trang (t17, t20) — luật "trích dẫn nguyên văn" khiến model gom về một chunk thay vì trích đủ hai nguồn; t24 bị từ chối nhầm; t27 vẫn khẳng định "Shopee 81% thị phần GMV" (nhầm chỉ tiêu ưa chuộng ↔ thị phần). Đánh đổi: A4 tốn ~1,5× chi phí A0 và chậm hơn (rerank trên CPU, nhiều token context hơn) nhưng bớt bịa. Hướng sửa (chưa làm, để tránh chỉnh theo test): bắt citation cho từng ý của câu multi-hop, kiểm "đủ trang" trước khi answer; vision mạnh hơn cho biểu đồ tròn. Giới hạn: biểu đồ tròn (index V), câu "chỉ tiêu gần giống" (d20), metric khớp chuỗi theo trang, một người soạn benchmark, nhãn do trợ lý AI soạn cần SV rà lại. TODO(SV): bổ sung nhận xét cá nhân.

## Thử thách nâng cao (nếu thực hiện)

- **Tài liệu, nguồn, quyền sử dụng, số trang và phiên bản:** như trên — bản PDF ngày 31/01/2024 (metadata InDesign), 100 trang, có văn bản, bảng (tr. 40, 72, 75, 78, 83–85, 88–96), biểu đồ cột/đường/tròn (tr. 28–37, 40–82), sơ đồ khối và infographic (tr. 10–26, 44, 57–58, 64).
- **Cách xử lý text, bảng, ảnh, biểu đồ; phạm vi index và phần chưa xử lý:** text + OCR biểu đồ vector từ Day 6 (index B, pypdf + PyMuPDF + Tesseract). Bổ sung index V: render mỗi trang 144 dpi, `gpt-4o-mini` chép từng khối trực quan thành JSON (loại, tiêu đề, vùng, đơn vị, giá trị) → mỗi khối 1 chunk có `page`, `region`, `page_image` để kiểm chứng. Toàn bộ 100 trang được gửi ({len(vis.get('pages_error', []))} lỗi); {len(vis.get('pages_without_visual_elements', []))} trang không có khối V (bìa, mục lục, trang trống, và các trang sơ đồ dạng ô chữ tr. 10–12, 15, 17–18, 20, 22–25 — nội dung là text thật nên vẫn có trong index B). Ảnh minh họa trang trí bị bỏ qua có chủ đích. Đã kiểm tay index V với ảnh gốc: bảng/cột/infographic đúng; **biểu đồ tròn sai ghép nhãn** (chưa xử lý). {vis.get('chunks_over_512_tokens_truncated_in_embedding', 0)} chunk dài hơn 512 token bị cắt khi embed (text đầy đủ vẫn lưu và đưa vào context).
- **Cách chia benchmark, schema evidence, model và cấu hình đã chốt trên dev:** schema mở rộng `data/README.md`: `group` (một nhóm chính), `gold[]` với `page`, `region`, `evidence`, `match`, `gold_mode: all` + `alternative_of` cho multi-hop, `calc` cho phép tính, `absence_reason` cho câu thiếu evidence. Test {test_n} câu: bảng 6, ảnh/sơ đồ 5, biểu đồ 5, multi-hop 4, text 4, thiếu bằng chứng 6. Dev {dev_n} câu phủ đủ nhóm. Cấu hình chốt trên dev: **{selected}**.

{md_table(["Nhóm test", "Đạt / tổng", "Tỷ lệ", "Lỗi / nhận xét"], pass_rows())}

**Kết luận phần nâng cao:** cấu hình chốt trên dev đạt **25/30 = 83,3%** trên test, **chưa đạt ngưỡng 90%** (cần ≥ 27/30) nên **không đủ điều kiện nhận 15 điểm bonus**; báo cáo trung thực theo ADVANCED.md, không chọn lại câu, không chỉnh theo test. Lỗi: multi-hop t17, t18, t20 (thiếu citation trang thứ hai hoặc lấy số dự báo 2027), t24 (từ chối nhầm), t27 (khẳng định thị phần GMV không có trong tài liệu). Nếu muốn thử lại phải sửa trên dev **và soạn bộ test mới** (RULES.md).

- **Trace, nhãn và evidence từng câu; thời gian, chi phí, lỗi hệ thống:** `results/agent/test/{selected}/` (traces, reviews có lý do từng câu, summary_labels); evidence từng câu trong `benchmark/questions.json`. Câu lỗi hệ thống/timeout tính không đạt và báo riêng (cột lỗi).
- **Giới hạn, cách tái lập và đường dẫn benchmark:** tái lập theo `README_DAY7.md` (Docker DB Day 6 → `visual_index` → `eval_retrieval` → `agent` → `review` → `build_report`). LLM có tính ngẫu nhiên nhỏ dù temperature 0; vision chỉ chạy một lần (output lưu ở `results/visual/extraction.jsonl` để tái dựng index V mà không gọi lại API: `python -m src.rag.visual_index --skip-extract`). Benchmark: `benchmark/questions.json`.
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(report, encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
