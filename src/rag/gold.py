"""Gold-evidence matching (used ONLY by evaluation, never by retrieval or the agent).

A chunk supports evidence e  <=>  chunk.page == e.page  and every string in e.match occurs in the
chunk text (NFC, case-folded, whitespace removed). `match` keys are short verbatim fragments of
the original page (numbers, names), chosen so that a chunk transcribing the right table/chart
cell contains them; the full `evidence` text and `region` stay in the benchmark for manual review.

Evidence groups: by default every gold item is an alternative (any one suffices). With
gold_mode == "all" (multi-hop), each item without `alternative_of` is a REQUIRED group and items
with `alternative_of: i` are alternatives for required group i.
"""
from __future__ import annotations

from .common import norm


def supports(chunk: dict, ev: dict) -> bool:
    if chunk.get("page") != ev["page"]:
        return False
    text = norm(chunk.get("text", ""))
    return all(norm(k) in text for k in ev["match"])


def groups(q: dict) -> list[list[dict]]:
    gold = q.get("gold") or []
    if q.get("gold_mode") != "all":
        return [gold]
    req = [[g] for g in gold if "alternative_of" not in g]
    for g in gold:
        if "alternative_of" in g:
            req[g["alternative_of"]].append(g)
    return req


def covered_groups(q: dict, chunks: list[dict]) -> list[bool]:
    return [any(supports(c, ev) for c in chunks for ev in grp) for grp in groups(q)]


def any_hit(q: dict, chunks: list[dict]) -> bool:
    return any(covered_groups(q, chunks))


def full_hit(q: dict, chunks: list[dict]) -> bool:
    return all(covered_groups(q, chunks))


def first_hit_rank(q: dict, ranked: list[dict]) -> int | None:
    for i, c in enumerate(ranked, 1):
        if any_hit(q, [c]):
            return i
    return None


def gold_pages(q: dict) -> set[int]:
    return {g["page"] for g in q.get("gold") or []}
