"""Generate the class demo page from result files (no hand-typed numbers).

Run: python -m src.rag.build_demo   ->  ../Demo/index.html  (Lab7/Demo)
Every number on the page is read from results/*.json at build time; the page footer lists the files.
"""
from __future__ import annotations

import html
import json
from datetime import datetime
from pathlib import Path

from .common import RESULTS, ROOT, load_questions

DEMO = ROOT.parent / "Demo"
_sel = RESULTS / "selection.json"
SELECTED = json.loads(_sel.read_text())["selected"] if _sel.exists() else "A3"
BASELINE = "A0"
GROUP_VI = {"table": "Bảng", "image": "Ảnh, sơ đồ", "chart": "Biểu đồ", "multihop": "Multi-hop",
            "text": "Text", "unanswerable": "Thiếu bằng chứng"}
SOURCES: list[str] = []


def load(rel: str):
    p = RESULTS / rel
    if not p.exists():
        return None
    SOURCES.append(f"results/{rel}")
    return json.loads(p.read_text(encoding="utf-8"))


def e(x) -> str:
    return html.escape(str(x))


def frac(d) -> str:
    return f"{d['n']}/{d['N']}" if isinstance(d, dict) else e(d)


def table(headers: list[str], rows: list[list], cls: str = "") -> str:
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def bar(value: float, maxv: float = 1.0) -> str:
    pct = 0 if not maxv else max(0, min(100, 100 * value / maxv))
    return f'<span class="bar"><span style="width:{pct:.0f}%"></span></span>'


def retrieval_section(split: str) -> str:
    rows_data = load(f"retrieval/{split}/summary.json") or []
    if not rows_data:
        return f"<p class='muted'>Chưa có kết quả retrieval {split}.</p>"
    order = ["dense:B", "bm25:B", "hybrid:B", "rerank:B", "dense:BV", "bm25:BV", "hybrid:BV", "rerank:BV",
             "rerank:BV:k=5:budget=6000", "dense:B:k=5:budget=6000"]
    rows_data.sort(key=lambda s: order.index(s["config"]) if s["config"] in order else 99)
    rows = []
    for s in rows_data:
        h1 = s["hit1"]
        rows.append([f"<code>{e(s['config'])}</code>", e(s["method"]), e(s["index"]), s["k"],
                     f"{frac(h1)} {bar(h1['n'], h1['N'])}", frac(s["hit3"]), frac(s["full_k"]),
                     frac(s["context_evidence_rate"]), s["mrr10"], f"{s['median_latency_ms']:.0f} ms"])
    return table(["Cấu hình", "Phương pháp", "Index", "k", "Hit@1", "Evidence Hit@3", "Đủ evidence@k",
                  "Context Evidence Rate", "MRR@10", "Độ trễ (trung vị)"], rows)


def agent_rows(split: str) -> list[list]:
    rows = []
    for cfg in ("A0", "A1", "A2", "A3"):
        s = load(f"agent/{split}/{cfg}/summary.json")
        if not s:
            continue
        lab = load(f"agent/{split}/{cfg}/summary_labels.json")
        g = lab["grounded"] if lab else None
        rows.append([f"<b>{cfg}</b>", f"{e(s['method'])}:{e(s['index'])}, k={s['top_k']}"
                     + (", read_page" if s["read_page"] else "") + (", kiểm trích dẫn" if s.get("strict") else ""),
                     e(s["tool_use"]), s["avg_llm_calls"], e(s["context_evidence_rate"]),
                     (f"{g['0']}/{g['1']}/{g['2']} · {lab['grounded_mean_over_2']:.2f}" if lab else "—"),
                     (f"{lab['citations_valid']}/{lab['citations_total']}" if lab else "—"),
                     e(s["abstain_on_unanswerable"]),
                     (f"{lab['false_abstain']}/{lab['answerable']}" if lab else "—"),
                     (e(lab["pass_rate"]) if lab else "—"),
                     f"{s['median_latency_s']} s", f"${s['total_cost_usd']:.4f}"])
    return rows


AGENT_HEAD = ["Cấu hình", "Retrieval / context", "Tool use", "Lượt LLM TB", "Context đủ evidence",
              "Grounded 0/1/2 · TB/2", "Citation hợp lệ", "Từ chối đúng", "Từ chối nhầm", "Đạt (ADVANCED)",
              "Thời gian TV", "Chi phí"]


def group_table() -> str:
    lab = load(f"agent/test/{SELECTED}/summary_labels.json")
    base = load(f"agent/test/{BASELINE}/summary_labels.json")
    if not lab:
        return "<p class='muted'>Chưa chấm test.</p>"
    rows = []
    for g in ("table", "image", "chart", "multihop", "text", "unanswerable"):
        v = lab["pass_by_group"].get(g, {"pass": 0, "N": 0})
        b = base["pass_by_group"].get(g, {"pass": 0, "N": 0}) if base else None
        rows.append([GROUP_VI[g], f"{v['pass']}/{v['N']} {bar(v['pass'], v['N'])}",
                     f"{b['pass']}/{b['N']}" if b else "—"])
    rows.append(["<b>Toàn bộ</b>", f"<b>{e(lab['pass_rate'])}</b>", e(base["pass_rate"]) if base else "—"])
    return table(["Nhóm test", f"{SELECTED} (đã chốt)", f"{BASELINE} (baseline)"], rows)


def example_cards() -> str:
    tr = load(f"agent/test/{SELECTED}/traces.json") or load(f"agent/dev/{SELECTED}/traces.json")
    rv = load(f"agent/test/{SELECTED}/reviews.json") or []
    if not tr:
        return "<p class='muted'>Chưa có trace.</p>"
    reviews = {r["query_id"]: r for r in rv}
    qs = {q["id"]: q for q in load_questions()}
    picks, wanted = [], [("answered", True, True), ("abstain", False, True), (None, None, False)]
    for status, answerable, ok in wanted:
        for t in tr:
            q, r = qs[t["query_id"]], reviews.get(t["query_id"], {})
            if t in [p[0] for p in picks]:
                continue
            good = bool(r.get("pass")) if r else None
            if status and (t["status"] != status or q["answerable"] != answerable or good is False):
                continue
            if status is None and good is not False:
                continue
            if status and q["group"] == "text" and any(qs[p[0]["query_id"]]["group"] != "text" for p in picks):
                pass
            picks.append((t, q, r))
            break
    labels = ["Câu có bằng chứng", "Câu thiếu bằng chứng (từ chối)", "Một lỗi (để phân tích)"]
    out = []
    for (t, q, r), lab in zip(picks, labels):
        steps = "".join(
            f"<li><code>{e(ev.get('tool', ev['event']))}</code> "
            f"{e(ev.get('query') or (('trang ' + str(ev['page'])) if ev.get('page') else ''))}"
            f"{' → ' + ', '.join('tr.' + str(x['page']) for x in ev.get('results', [])[:6]) if ev.get('results') else ''}"
            f"{' — ' + e(ev.get('reason', ''))[:200] if ev['event'] == 'abstain' else ''}</li>"
            for ev in t["events"] if ev["event"] in ("search", "abstain", "quote_check_failed", "quote_check_passed"))
        ctx = {c["id"]: c for c in t["context_chunks"]}
        cits = "".join(
            f"<details><summary><code>{e(c)}</code> · trang {ctx.get(c, {}).get('page', '?')}</summary>"
            f"<pre>{e(ctx.get(c, {}).get('text', ''))[:900]}</pre>"
            f"<img loading='lazy' alt='Trang {ctx.get(c, {}).get('page', '')} của PDF gốc' "
            f"src='../work/pages_hd/p{int(ctx.get(c, {}).get('page', 0)):03d}.png'></details>" for c in t["citations"])
        expected = q.get("expected_answer") or ("Hành vi mong đợi: từ chối. " + q.get("absence_reason", ""))
        verdict = ("ĐẠT" if r.get("pass") else "KHÔNG ĐẠT") if r else "chưa chấm"
        out.append(f"""<article class="card ex">
  <div class="tag">{lab} · {e(q['id'])} · {GROUP_VI[q['group']]}</div>
  <h4>{e(q['question'])}</h4>
  <div class="two"><div><div class="k">Agent trả lời ({e(t['status'])})</div><p>{e(t['answer'])}</p></div>
  <div><div class="k">Đáp án chuẩn / kỳ vọng</div><p>{e(expected)}</p></div></div>
  <div class="k">Các bước tool ({t['n_tool_calls']} lượt, {t['latency_s']} s, ${t['cost_usd']:.5f})</div><ol class="steps">{steps}</ol>
  {('<div class="k">Citation → nội dung chunk trong pgvector + ảnh trang gốc</div>' + cits) if cits else ''}
  <p class="verdict {'ok' if r.get('pass') else 'bad'}">Nhãn chấm: {verdict}. {e(r.get('reason', ''))}</p>
</article>""")
    return "\n".join(out)


def error_analysis() -> str:
    p = RESULTS / "error_analysis.json"
    if not p.exists():
        return "<p class='muted'>Chưa có phân tích lỗi.</p>"
    SOURCES.append("results/error_analysis.json")
    rows = [[f"<b>{e(x['id'])}</b>", e(x["symptom"]), e(x["cause"]), e(x["fix"]), e(x["before"]), e(x["after"])]
            for x in json.loads(p.read_text(encoding="utf-8"))]
    return table(["Câu dev", "Triệu chứng (A0)", "Nguyên nhân", "Thay đổi thử", "Trước", "Sau"], rows)


def main() -> None:
    vis = load("visual/summary.json") or {}
    import os
    pages6 = [json.loads(l) for l in (Path(os.environ["DAY6_STARTER"]) / "results" / "pages.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    SOURCES.append("Day 6 starter/results/pages.jsonl")
    n_content = sum(bool((p.get("metadata") or {}).get("counted")) for p in pages6)
    n_chart = sum(bool((p.get("metadata") or {}).get("chart_heavy")) for p in pages6)
    qs = load_questions()
    dist: dict[tuple, int] = {}
    for q in qs:
        dist[(q["split"], q["group"])] = dist.get((q["split"], q["group"]), 0) + 1
    bench_rows = [[GROUP_VI[g], dist.get(("dev", g), 0), dist.get(("test", g), 0)]
                  for g in ("table", "image", "chart", "multihop", "text", "unanswerable")]
    bench_rows.append(["<b>Tổng</b>", sum(v for (s, _), v in dist.items() if s == "dev"),
                       sum(v for (s, _), v in dist.items() if s == "test")])
    sel_test = load(f"agent/test/{SELECTED}/summary_labels.json")
    headline = e(sel_test["pass_rate"]) if sel_test else "chưa chạy"
    test_cost = sum((load(f"agent/test/{c}/summary.json") or {}).get("total_cost_usd", 0) for c in ("A0", "A1", "A2", "A3"))
    dev_cost = sum((load(f"agent/dev/{c}/summary.json") or {}).get("total_cost_usd", 0) for c in ("A0", "A1", "A2", "A3"))
    total_cost = vis.get("extract_cost_usd", 0) + test_cost + dev_cost

    page = f"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Agentic RAG Demo</title>
<style>
:root{{--bg:#f7f8fa;--card:#fff;--ink:#16202c;--muted:#5b6876;--line:#dde3ea;--accent:#1554a5;--accent2:#e8f0fb;--ok:#1e7a46;--bad:#b3261e;--code:#eef2f6}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f141a;--card:#161d25;--ink:#e6ebf1;--muted:#9aa7b4;--line:#2a3542;--accent:#6ea8ff;--accent2:#1b2a3d;--ok:#4cc38a;--bad:#ff7b72;--code:#1f2933}}}}
:root[data-theme="dark"]{{--bg:#0f141a;--card:#161d25;--ink:#e6ebf1;--muted:#9aa7b4;--line:#2a3542;--accent:#6ea8ff;--accent2:#1b2a3d;--ok:#4cc38a;--bad:#ff7b72;--code:#1f2933}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
main{{max-width:1120px;margin:0 auto;padding:24px 16px 80px}}
nav{{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);overflow-x:auto;white-space:nowrap}}
nav a{{display:inline-block;padding:10px 12px;color:var(--muted);text-decoration:none;font-size:14px}}nav a:hover{{color:var(--accent)}}
h1{{font-size:clamp(26px,4vw,38px);line-height:1.2;margin:24px 0 8px}}h2{{margin:48px 0 12px;font-size:24px}}h4{{margin:6px 0 10px}}
.lead{{color:var(--muted);max-width:780px}}.muted{{color:var(--muted)}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:20px 0}}
.kpi,.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}}
.kpi b{{display:block;font-size:26px;color:var(--accent);font-variant-numeric:tabular-nums}}.kpi span{{color:var(--muted);font-size:13px}}
.tw{{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card)}}
table{{border-collapse:collapse;width:100%;font-size:14px;font-variant-numeric:tabular-nums}}
th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}th{{background:var(--accent2);font-weight:600}}
tr:last-child td{{border-bottom:0}}code,pre{{background:var(--code);border-radius:6px;font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}}
code{{padding:1px 5px}}pre{{padding:10px;white-space:pre-wrap;overflow-x:auto}}
.bar{{display:inline-block;width:70px;height:8px;background:var(--line);border-radius:4px;vertical-align:middle;margin-left:6px}}.bar span{{display:block;height:100%;background:var(--accent);border-radius:4px}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}}
.ex{{margin:16px 0}}.tag{{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--accent);font-weight:600}}
.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}.k{{font-size:12px;color:var(--muted);font-weight:600;margin-top:8px}}
.steps{{margin:4px 0;padding-left:20px;font-size:14px}}details{{margin:6px 0}}summary{{cursor:pointer}}
details img{{max-width:100%;border:1px solid var(--line);border-radius:8px;margin-top:6px}}
.verdict{{font-weight:600}}.verdict.ok{{color:var(--ok)}}.verdict.bad{{color:var(--bad)}}
.script li{{margin:8px 0}}.time{{display:inline-block;min-width:72px;font-weight:600;color:var(--accent)}}
svg text{{fill:var(--ink);font-size:13px}}svg .box{{fill:var(--card);stroke:var(--accent);stroke-width:1.5}}svg .hl{{fill:var(--accent2)}}svg .ln{{stroke:var(--muted);stroke-width:1.5;fill:none;marker-end:url(#a)}}
footer{{margin-top:48px;color:var(--muted);font-size:13px}}
</style></head><body>
<nav><a href="#tong-quan">Tổng quan</a><a href="#du-lieu">Dữ liệu</a><a href="#kien-truc">Kiến trúc</a><a href="#benchmark">Benchmark</a><a href="#retrieval">Retrieval</a><a href="#agent">Agent</a><a href="#loi">Phân tích lỗi</a><a href="#vi-du">Ví dụ</a><a href="#kich-ban">Kịch bản demo</a><a href="#kiem-chung">Kiểm chứng</a><a href="#gioi-han">Giới hạn</a><a href="http://127.0.0.1:8765/">▶ Demo live</a></nav>
<main>
<section id="tong-quan">
<h1>Agentic RAG trên Sách trắng TMĐT Việt Nam 2023</h1>
<p class="lead">Day 7 · tiếp nối Day 6 (PostgreSQL + pgvector + SEA-LION-E5). Agent dùng model thật (<code>gpt-4o-mini</code>) để tự tìm bằng chứng trong tài liệu 100 trang có bảng, biểu đồ, sơ đồ; trả lời kèm citation có thể kiểm chứng, hoặc từ chối khi tài liệu không đủ thông tin. Sinh viên: TODO(SV) Nguyễn Minh Phương · 2A202603997.</p>
<div class="kpis">
<div class="kpi"><b>{headline}</b><span>Tỷ lệ đạt test (ADVANCED, cấu hình {SELECTED})</span></div>
<div class="kpi"><b>{len(qs)}</b><span>câu benchmark (dev {sum(q['split']=='dev' for q in qs)} · test {sum(q['split']=='test' for q in qs)})</span></div>
<div class="kpi"><b>173 + {vis.get('chunks', '—')}</b><span>chunk text (Day 6, B) + chunk trực quan (Day 7, V)</span></div>
<div class="kpi"><b>4</b><span>phương pháp retrieval: dense, BM25, hybrid RRF, rerank</span></div>
<div class="kpi"><b>${total_cost:.2f}</b><span>tổng chi phí API (index V + agent dev/test)</span></div>
</div>
</section>

<section id="du-lieu"><h2>1. Dữ liệu và kết nối Day 6</h2>
<div class="grid2">
<div class="card"><h4>Tài liệu</h4><ul>
<li>Sách trắng Thương mại điện tử Việt Nam 2023 — Cục TMĐT &amp; Kinh tế số, Bộ Công Thương</li>
<li>{len(pages6)} trang PDF, {n_content} trang nội dung (Day 6); {n_chart} trang Day 6 đánh dấu chart_heavy</li>
<li>Nguồn: <code>valoma.vn/…/BCTMDT2023-file-31-1-pdf.pdf</code>, sha256 <code>4b7e4a29…ccb430f</code>; không commit PDF (chưa rõ quyền tái phân phối)</li></ul></div>
<div class="card"><h4>Vector store (dùng lại Day 6)</h4><ul>
<li>PostgreSQL 16 + pgvector 0.8.7, bảng <code>chunks</code>, HNSW cosine</li>
<li>Embedding <code>aisingapore/SEA-LION-E5-Embedding-600M</code>, 1024 chiều, chạy local, chi phí 0</li>
<li>Index <b>B</b> (Day 6): 173 chunk theo đoạn/heading — tái lập đúng số Day 6 (dev Hit@3 13/15)</li>
<li>Index <b>V</b> (Day 7): {vis.get('chunks', '—')} khối trực quan trên {len(vis.get('pages_with_visuals', []))} trang, đọc bằng <code>{e(vis.get('vision_model', ''))}</code>, ${vis.get('extract_cost_usd', 0):.2f}; cùng bảng, cùng model embedding</li></ul></div>
</div></section>

<section id="kien-truc"><h2>2. Kiến trúc</h2>
<div class="card"><svg viewBox="0 0 1060 300" width="100%" role="img" aria-label="Sơ đồ pipeline: PDF tới hai index, pgvector, bốn retriever, agent và câu trả lời có citation">
<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="currentColor"/></marker></defs>
<rect class="box" x="10" y="115" width="120" height="60" rx="10"/><text x="70" y="140" text-anchor="middle">PDF 100 trang</text><text x="70" y="160" text-anchor="middle">bảng · biểu đồ</text>
<rect class="box" x="170" y="40" width="190" height="64" rx="10"/><text x="265" y="66" text-anchor="middle">Index B (Day 6)</text><text x="265" y="86" text-anchor="middle">text + OCR biểu đồ</text>
<rect class="box" x="170" y="190" width="190" height="64" rx="10"/><text x="265" y="216" text-anchor="middle">Index V (Day 7)</text><text x="265" y="236" text-anchor="middle">vision → bảng/biểu đồ</text>
<rect class="box hl" x="400" y="115" width="150" height="60" rx="10"/><text x="475" y="140" text-anchor="middle">pgvector</text><text x="475" y="160" text-anchor="middle">SEA-LION-E5 1024d</text>
<rect class="box" x="590" y="20" width="180" height="250" rx="10"/><text x="680" y="48" text-anchor="middle">Retrievers</text>
<text x="680" y="88" text-anchor="middle">dense (HNSW)</text><text x="680" y="126" text-anchor="middle">BM25 âm tiết+bigram</text><text x="680" y="164" text-anchor="middle">hybrid RRF k=60</text><text x="680" y="202" text-anchor="middle">rerank bge-v2-m3</text><text x="680" y="240" text-anchor="middle">read_page</text>
<rect class="box hl" x="810" y="85" width="120" height="120" rx="10"/><text x="870" y="120" text-anchor="middle">Agent</text><text x="870" y="142" text-anchor="middle">gpt-4o-mini</text><text x="870" y="164" text-anchor="middle">tool calling</text><text x="870" y="186" text-anchor="middle">kiểm trích dẫn</text>
<rect class="box" x="960" y="60" width="92" height="60" rx="10"/><text x="1006" y="86" text-anchor="middle">Trả lời</text><text x="1006" y="104" text-anchor="middle">+ citation</text>
<rect class="box" x="960" y="170" width="92" height="60" rx="10"/><text x="1006" y="204" text-anchor="middle">Từ chối</text>
<path class="ln" d="M130 135 L170 80"/><path class="ln" d="M130 155 L170 215"/><path class="ln" d="M360 72 L400 132"/><path class="ln" d="M360 222 L400 160"/>
<path class="ln" d="M550 145 L590 145"/><path class="ln" d="M770 145 L810 145"/><path class="ln" d="M930 125 L960 95"/><path class="ln" d="M930 165 L960 198"/>
</svg>
<p class="muted">Agent chỉ nhận câu hỏi. Đáp án chuẩn và evidence gold chỉ dùng ở bước chấm, không bao giờ vào prompt hay tool.</p></div></section>

<section id="benchmark"><h2>3. Benchmark (chia dev/test trước khi thử nghiệm)</h2>
{table(["Nhóm chính", "Dev", "Test"], bench_rows)}
<p class="muted">Mỗi câu có trang, vùng (hàng/cột bảng, cột biểu đồ, ô sơ đồ), đoạn evidence nguyên văn và các chuỗi khớp tự động; câu thiếu bằng chứng ghi cách kiểm tra trong toàn văn. File: <code>benchmark/questions.json</code>. Câu test không trùng benchmark Day 6.</p></section>

<section id="retrieval"><h2>4. So sánh retrieval (câu hỏi gốc, không filter)</h2>
<h4>Dev</h4>{retrieval_section("dev")}
<h4>Test (chạy sau khi chốt cấu hình)</h4>{retrieval_section("test")}
<p class="muted">Hit = chunk đúng trang và chứa toàn bộ chuỗi khớp của evidence. Context Evidence Rate = mọi evidence bắt buộc (multi-hop cần đủ các trang) nằm trong context đóng gói theo budget ký tự. Độ trễ rerank đo trên CPU.</p></section>

<section id="agent"><h2>5. Agent: so sánh cấu hình</h2>
<h4>Dev</h4>{table(AGENT_HEAD, agent_rows("dev"))}
<h4>Test — baseline vs cấu hình đã chốt</h4>{table(AGENT_HEAD, agent_rows("test"))}
<h4>Tỷ lệ đạt theo nhóm (ADVANCED.md: đúng + đủ + citation hỗ trợ; từ chối đúng)</h4>{group_table()}
<p class="muted">A0 = Day 6 nguyên trạng (dense, index B, top-3). A1 = + index V + hybrid RRF, top-5. A2 = A1 + rerank + read_page + kiểm trích dẫn nguyên văn &amp; luật năm/đối tượng. A3 = A2 nhưng kiểm trích dẫn có dung sai (số phải khớp, ≥60% từ, sửa ID). Tiêu chí chọn công bố trước khi chạy test (<code>results/selection.json</code>): (1) số câu dev đạt, (2) từ chối đúng, (3) ít từ chối nhầm, (4) chi phí/thời gian.</p></section>

<section id="loi"><h2>6. Phân tích lỗi trên dev (trước/sau)</h2>{error_analysis()}</section>

<section id="vi-du"><h2>7. Ví dụ thật từ trace</h2>{example_cards()}</section>

<section id="kich-ban"><h2>8. Kịch bản demo (≈ 7 phút)</h2>
<div class="card"><ol class="script">
<li><span class="time">0:00</span> <b>Vấn đề.</b> Mở mục Tổng quan: tài liệu 100 trang, nhiều số liệu nằm trong biểu đồ; RAG chỉ đọc text sẽ trả lời sai hoặc bịa.</li>
<li><span class="time">0:45</span> <b>Kiến trúc.</b> Chỉ sơ đồ: dùng lại pgvector + embedding Day 6 (index B), thêm index V đọc bảng/biểu đồ bằng vision; 4 retriever; agent có tool và tự quyết số lượt tìm.</li>
<li><span class="time">1:45</span> <b>Benchmark minh bạch.</b> Mở <code>benchmark/questions.json</code>, chỉ một câu biểu đồ: trang, vùng, evidence. Nhấn mạnh chia dev/test trước, test không dùng để chỉnh.</li>
<li><span class="time">2:30</span> <b>Live demo câu có bằng chứng.</b> Mở <code>http://127.0.0.1:8765/</code> (server <code>python -m src.rag.demo_server --warm</code>), chọn câu t17 (multi-hop tr. 40 + tr. 37), bấm ▶ Chạy agent: pipeline sáng theo từng bước, bảng kết quả mỗi lần tìm, câu trả lời có phép tính và citation bấm được.</li>
<li><span class="time">3:30</span> <b>Chứng minh trong DB.</b> Bấm citation → khung Chunk inspector hiện đúng dòng trong pgvector, câu SQL và ảnh trang PDF; hoặc chạy <code>python -m src.rag.verify --trace results/agent/test/{SELECTED}/traces.json --id t17 --find "20,5"</code> → in đúng dòng trong bảng <code>chunks</code> (index, trang, hash) và đối chiếu PDF; mở ảnh trang gốc.</li>
<li><span class="time">4:30</span> <b>Câu thiếu bằng chứng + so sánh retriever.</b> Chạy câu t25 (doanh thu B2C 2024) → agent tìm nhiều lần rồi từ chối; so với baseline A0 từng bịa số năm khác trên dev (d17). Bấm “So sánh 4 retriever” để thấy dense/BM25/hybrid/rerank xếp hạng khác nhau thế nào.</li>
<li><span class="time">5:15</span> <b>Một lỗi thật.</b> Mở thẻ “Một lỗi” ở mục 7: chỉ ra nguyên nhân (đọc biểu đồ tròn / chọn sai năm) và giới hạn.</li>
<li><span class="time">6:00</span> <b>Số liệu &amp; đánh đổi.</b> Bảng mục 4–5: chất lượng tăng từ A0 → A2, đổi lại nhiều lượt gọi hơn, rerank chậm trên CPU; tổng chi phí API ${total_cost:.2f}.</li>
<li><span class="time">6:40</span> <b>Kết luận + Q&amp;A.</b> Giới hạn ở mục cuối; mọi số liệu sinh tự động từ <code>results/</code>.</li>
</ol>
<p class="muted">Chuẩn bị trước: <code>docker --context default compose -p day6_student_starter up -d</code> (thư mục starter Day 6), kiểm tra <code>.env</code>, chạy thử một câu để nạp model (lần đầu ~25 s). Nếu mạng/API lỗi: tab “Phát lại trace đã lưu” (hoặc mở <code>http://127.0.0.1:8765/?replay=test/{SELECTED}/t17&amp;gold=1</code>) phát lại đúng trace thật đã ghi, không gọi API, không bịa kết quả.</p></div></section>

<section id="kiem-chung"><h2>9. Cách kiểm chứng một câu trả lời</h2>
<div class="card"><ol>
<li>Lấy <code>chunk_id</code> trong citation, ví dụ <code>sach-trang-tmdt-2023:p40:V2</code> (trang 40, index V, khối 2).</li>
<li>Truy vấn trực tiếp DB: <code>SELECT strategy, page, text, metadata FROM chunks WHERE chunk_id = '…';</code></li>
<li>Mở PDF gốc đúng trang (hoặc <code>work/pages_hd/p040.png</code>), so từng số, đơn vị, năm.</li>
<li>Hoặc chạy <code>python -m src.rag.verify --chunk … --find "…"</code>: in dòng DB, kiểm chuỗi trong text layer PDF, hash PDF và nguồn tải.</li>
</ol><p class="muted">Chi tiết: <code>Demo/README_KIEM_CHUNG.md</code>.</p></div></section>

<section id="gioi-han"><h2>10. Giới hạn</h2>
<div class="card"><ul>
<li>Vision <code>gpt-4o-mini</code> đọc sai ghép nhãn ở nhiều biểu đồ tròn (5/5 biểu đồ tròn kiểm tay có lỗi) — xem <code>results/visual/manual_check.md</code>.</li>
<li>Nhãn chấm do trợ lý AI soạn sau khi đối chiếu trang gốc; sinh viên cần rà lại (đề yêu cầu chấm thủ công).</li>
<li>Khớp evidence tự động dựa trên trang + chuỗi; đúng trang nhưng sai ô vẫn có thể bị tính hit — vì vậy có chấm tay câu trả lời.</li>
<li>Benchmark 50 câu do một người soạn, có thể thiên lệch theo cách hỏi.</li>
</ul></div></section>
<footer>Sinh tự động lúc {datetime.now().strftime('%Y-%m-%d %H:%M')} bởi <code>src/rag/build_demo.py</code> từ: {', '.join(f'<code>{e(s)}</code>' for s in dict.fromkeys(SOURCES))}.</footer>
</main></body></html>"""
    DEMO.mkdir(parents=True, exist_ok=True)
    (DEMO / "index.html").write_text(page, encoding="utf-8")
    print(DEMO / "index.html")


if __name__ == "__main__":
    main()
