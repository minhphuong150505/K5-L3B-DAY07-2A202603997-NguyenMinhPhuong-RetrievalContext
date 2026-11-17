"""Retrieval + context benchmark (no LLM). Original query only, no filter, same corpus/index.

Run: python -m src.rag.eval_retrieval --split dev --configs dense:B bm25:B hybrid:B dense:BV ...
Config syntax: <method>:<index>[:k=<top_k>][:budget=<chars>]   (defaults k=3, budget=4000)

Metrics per config (answerable questions only; denominator N = answerable in split):
  Hit@1            evidence (any required group) in rank 1
  Evidence Hit@3   evidence in top-3 (always top-3, even if k differs)
  Full@k           ALL required evidence groups in top-k (matters for multi-hop)
  Context Evidence Rate  ALL required groups inside the packed context (budget chars)
  MRR@10, Page Hit@3 (gold page in top-3), latency
Outputs: results/retrieval/<split>/<config>.traces.json and summary.json
"""
from __future__ import annotations

import argparse
import statistics
import time

from . import gold
from .common import RESULTS, load_questions, write_json
from .retrievers import build, timed_search


def pack(results: list[dict], budget: int) -> tuple[str, list[str]]:
    """Greedy by rank, dedupe by id, keep source + page header, skip chunks that do not fit."""
    blocks, ids, used = [], [], 0
    for r in results:
        if r["id"] in ids:
            continue
        block = f"[{r['id']} | trang {r['page']}]\n{r['text']}"
        if used + len(block) + 2 > budget:
            continue
        blocks.append(block)
        ids.append(r["id"])
        used += len(block) + 2
    return "\n\n".join(blocks), ids


def parse(cfg: str) -> dict:
    parts = cfg.split(":")
    out = {"name": cfg, "method": parts[0], "index": parts[1], "k": 3, "budget": 4000}
    for p in parts[2:]:
        k, v = p.split("=")
        out[k] = int(v)
    return out


def run(cfg: dict, questions: list[dict]) -> tuple[dict, list[dict]]:
    t0 = time.perf_counter()
    retriever = build(cfg["method"], cfg["index"])
    setup_s = time.perf_counter() - t0
    depth = max(cfg["k"], 10)
    traces = []
    for q in questions:
        try:
            ranked, ms = timed_search(retriever, q["question"], depth)
            err = None
        except Exception as e:  # report, never fake
            ranked, ms, err = [], 0.0, f"{type(e).__name__}: {e}"
        topk = ranked[:cfg["k"]]
        context, ids = pack(topk, cfg["budget"])
        in_ctx = [r for r in topk if r["id"] in ids]
        t = {"query_id": q["id"], "split": q["split"], "group": q["group"], "answerable": q["answerable"],
             "question": q["question"], "config": cfg["name"], "error": err, "latency_ms": round(ms, 1),
             "results": [{k: r.get(k) for k in ("rank", "id", "page", "score", "method", "component_ranks")}
                         | {"index": r["metadata"].get("index"), "text": r["text"][:400]} for r in ranked],
             "context_ids": ids, "context_chars": len(context)}
        if q["answerable"]:
            fr = gold.first_hit_rank(q, ranked[:10])
            t.update({"gold_pages": sorted(gold.gold_pages(q)), "first_hit_rank": fr,
                      "hit1": gold.any_hit(q, ranked[:1]), "hit3": gold.any_hit(q, ranked[:3]),
                      "full_k": gold.full_hit(q, topk), "context_full": gold.full_hit(q, in_ctx),
                      "page_hit3": bool(gold.gold_pages(q) & {r["page"] for r in ranked[:3]}),
                      "rr": 1 / fr if fr else 0.0})
        traces.append(t)
    ans = [t for t in traces if t["answerable"]]
    n = len(ans)

    def frac(key):
        k = sum(bool(t[key]) for t in ans)
        return {"n": k, "N": n, "rate": round(k / n, 3) if n else None}

    summary = {"config": cfg["name"], **{k: cfg[k] for k in ("method", "index", "k", "budget")},
               "split": questions[0]["split"] if questions else None, "answerable_N": n,
               "hit1": frac("hit1"), "hit3": frac("hit3"), "full_k": frac("full_k"),
               "context_evidence_rate": frac("context_full"), "page_hit3": frac("page_hit3"),
               "mrr10": round(sum(t["rr"] for t in ans) / n, 3) if n else None,
               "errors": sum(t["error"] is not None for t in traces),
               "median_latency_ms": round(statistics.median(t["latency_ms"] for t in traces), 1),
               "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces)),
               "setup_s": round(setup_s, 1), "cost_usd": 0.0,
               "by_group": {g: {"hit3": sum(t["hit3"] for t in ans if t["group"] == g),
                                "context": sum(t["context_full"] for t in ans if t["group"] == g),
                                "N": sum(t["group"] == g for t in ans)}
                            for g in sorted({t["group"] for t in ans})},
               "misses_at3": [t["query_id"] for t in ans if not t["hit3"]]}
    return summary, traces


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test", "test2", "test3"))
    ap.add_argument("--configs", nargs="+", required=True)
    args = ap.parse_args()
    qs = load_questions(args.split)
    out = RESULTS / "retrieval" / args.split
    summaries = []
    old = out / "summary.json"
    if old.exists():
        import json
        summaries = [s for s in json.loads(old.read_text()) if s["config"] not in args.configs]
    for c in args.configs:
        s, tr = run(parse(c), qs)
        write_json(out / f"{c.replace(':', '_').replace('=', '')}.traces.json", tr)
        summaries.append(s)
        print(f"{c:28s} Hit@1 {s['hit1']['n']}/{s['hit1']['N']}  Hit@3 {s['hit3']['n']}/{s['hit3']['N']}  "
              f"Full@k {s['full_k']['n']}  Ctx {s['context_evidence_rate']['n']}  MRR {s['mrr10']}  "
              f"{s['median_latency_ms']}ms  miss {s['misses_at3']}")
    write_json(old, summaries)


if __name__ == "__main__":
    main()
