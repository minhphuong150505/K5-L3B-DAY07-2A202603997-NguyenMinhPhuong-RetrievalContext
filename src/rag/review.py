"""Manual review helpers (evaluation side only — reads gold, never feeds the agent).

  python -m src.rag.review sheet  --split test --config A2     -> results/agent/test/A2/review_sheet.md
  python -m src.rag.review metrics --split test --config A2    -> uses reviews.json (human labels)

reviews.json (one object per query, written by the reviewer after reading the sheet):
  {"query_id": "t01", "answer_grade": 0|1|2 (answerable), "abstention_correct": bool (unanswerable),
   "citation_support": [bool per citation], "pass": bool (ADVANCED.md pass/fail), "reason": "..."}
Outputs summary_labels.json with BENCHMARK.md answer metrics and ADVANCED.md pass rate per group.
"""
from __future__ import annotations

import argparse
import json

from . import gold
from .common import RESULTS, load_questions, read_json, write_json


def sheet(split: str, config: str) -> None:
    base = RESULTS / "agent" / split / config
    traces = {t["query_id"]: t for t in read_json(base / "traces.json")}
    lines = [f"# Phiếu chấm {config} / {split}\n",
             "Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). "
             "Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.\n"]
    for q in load_questions(split):
        t = traces.get(q["id"])
        if not t:
            continue
        lines.append(f"\n## {q['id']} · {q['group']} · {'có đáp án' if q['answerable'] else 'thiếu bằng chứng'}")
        lines.append(f"**Câu hỏi:** {q['question']}")
        if q["answerable"]:
            lines.append(f"**Đáp án chuẩn:** {q['expected_answer']}  ")
            lines.append("**Evidence:** " + "; ".join(f"tr.{g['page']} — {g['region']}" for g in q["gold"]))
            lines.append(f"**auto:** context đủ evidence = {gold.full_hit(q, t['context_chunks'])}")
        else:
            lines.append(f"**Lý do thiếu:** {q['absence_reason']}")
        lines.append(f"**Agent ({t['status']}, {t['n_tool_calls']} tool call, {t['latency_s']}s):** {t['answer']}")
        for e in t["events"]:
            if e["event"] == "search":
                what = e.get("query") or f"page {e.get('page')}"
                lines.append(f"- {e['tool']}: `{what}` → " + ", ".join(f"p{r['page']}" for r in e["results"]))
            elif e["event"] in ("abstain", "invalid_or_missing_citations", "step_limit", "error"):
                lines.append(f"- {e['event']}: {e.get('reason') or e.get('error') or ''}")
        ctx = {c["id"]: c for c in t["context_chunks"]}
        for c in t["citations"]:
            txt = ctx.get(c, {}).get("text", "(không có trong context)")
            lines.append(f"\n> **[{c}]** {txt[:700]}")
    (base / "review_sheet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(base / "review_sheet.md")


def metrics(split: str, config: str) -> dict:
    base = RESULTS / "agent" / split / config
    traces = {t["query_id"]: t for t in read_json(base / "traces.json")}
    reviews = {r["query_id"]: r for r in read_json(base / "reviews.json")}
    qs = load_questions(split)
    out = {"config": config, "split": split, "grounded": {"0": 0, "1": 0, "2": 0}, "citations_valid": 0,
           "citations_total": 0, "answers_with_citation": 0, "answers": 0, "abstain_correct": 0,
           "unanswerable": 0, "false_abstain": 0, "answerable": 0, "errors": 0, "pass_by_group": {}}
    for q in qs:
        t, r = traces[q["id"]], reviews[q["id"]]
        g = out["pass_by_group"].setdefault(q["group"], {"pass": 0, "N": 0})
        g["N"] += 1
        g["pass"] += bool(r.get("pass"))
        if t["status"] == "error":
            out["errors"] += 1
            continue
        out["citations_total"] += len(t["citations"])
        out["citations_valid"] += sum(r.get("citation_support", []))
        if t["status"] == "answered":
            out["answers"] += 1
            out["answers_with_citation"] += bool(t["citations"])
        if q["answerable"]:
            out["answerable"] += 1
            out["grounded"][str(r["answer_grade"])] += 1
            out["false_abstain"] += t["status"] == "abstain"
        else:
            out["unanswerable"] += 1
            out["abstain_correct"] += bool(r["abstention_correct"])
    n = out["answerable"]
    out["grounded_mean_over_2"] = round((out["grounded"]["1"] + 2 * out["grounded"]["2"]) / n, 3) if n else None
    total_pass = sum(v["pass"] for v in out["pass_by_group"].values())
    out["pass_rate"] = f"{total_pass}/{len(qs)} = {100 * total_pass / len(qs):.1f}%"
    write_json(base / "summary_labels.json", out)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("sheet", "metrics"))
    ap.add_argument("--split", required=True)
    ap.add_argument("--config", required=True)
    a = ap.parse_args()
    (sheet if a.cmd == "sheet" else metrics)(a.split, a.config)


if __name__ == "__main__":
    main()
