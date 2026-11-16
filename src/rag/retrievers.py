"""Retrieval methods over the Day 6 pgvector store.

dense   : SEA-LION-E5 query embedding (Day 6 'Retrieval' prompt) + pgvector HNSW cosine.
bm25    : Okapi BM25 (k1=1.5, b=0.75) over Vietnamese syllables + syllable bigrams
          (bigrams approximate Vietnamese multi-syllable words: "thương mại", "điện tử").
hybrid  : Reciprocal Rank Fusion of dense and bm25 rankings (k=60, top 30 each) — rank-based,
          so no score normalisation across incompatible scales is needed.
rerank  : hybrid top-N candidates re-scored by cross-encoder BAAI/bge-reranker-v2-m3.

Every result carries id, text, source_id, source, page, metadata, score, rank, method.
"""
from __future__ import annotations

import math
import os
import re
import time
import unicodedata
from collections import Counter
from functools import lru_cache
from typing import Any

import numpy as np

from .common import db, embedder, load_corpus

RRF_K = 60
FUSION_DEPTH = 30


def _row_to_result(r: dict, score: float, method: str) -> dict:
    md = dict(r.get("metadata") or {})
    md.setdefault("section", r.get("section"))
    md["index"] = r["strategy"]
    return {"id": r["chunk_id"], "text": r["text"], "source_id": r["document_id"], "source": r["source"],
            "page": r["page"], "metadata": md, "score": float(score), "method": method}


def tokenize(text: str) -> list[str]:
    syl = re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())
    return syl + [f"{a}_{b}" for a, b in zip(syl, syl[1:])]


class DenseRetriever:
    name = "dense"

    def __init__(self, strategies: tuple[str, ...]) -> None:
        self.strategies = list(strategies)

    def search(self, query: str, top_k: int, filters: dict | None = None) -> list[dict]:
        qv = np.asarray(embedder().embed_query(query), dtype=np.float32)
        where, params = ["strategy = ANY(%s)"], [self.strategies]
        for key, val in (filters or {}).items():
            if key not in {"page", "section"}:
                raise ValueError(f"filter {key} không được hỗ trợ")
            where.append(f"{key} = ANY(%s)" if isinstance(val, list) else f"{key} = %s")
            params.append(val)
        with db() as conn, conn.cursor() as cur:
            cur.execute("SET hnsw.iterative_scan = relaxed_order")
            cur.execute("SET hnsw.ef_search = 100")
            cur.execute(f"""SELECT strategy, chunk_id, document_id, source, page, section, text, metadata,
                                   1 - (embedding <=> %s) AS score
                            FROM chunks WHERE {' AND '.join(where)}
                            ORDER BY embedding <=> %s LIMIT %s""", [qv, *params, qv, top_k])
            cols = [d.name for d in cur.description]
            rows = [dict(zip(cols, r)) for r in cur.fetchall()]
        return [_row_to_result(r, r["score"], self.name) for r in rows]


class BM25Retriever:
    name = "bm25"

    def __init__(self, strategies: tuple[str, ...], k1: float = 1.5, b: float = 0.75) -> None:
        self.rows = load_corpus(strategies)
        self.k1, self.b = k1, b
        self.tf = [Counter(tokenize(r["text"])) for r in self.rows]
        self.len = [sum(t.values()) for t in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(term for t in self.tf for term in t)
        n = len(self.rows)
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def search(self, query: str, top_k: int, filters: dict | None = None) -> list[dict]:
        q = [t for t in set(tokenize(query)) if t in self.idf]
        scored = []
        for i, (r, tf) in enumerate(zip(self.rows, self.tf)):
            if filters and any((r.get(k) not in v) if isinstance(v, list) else r.get(k) != v
                               for k, v in filters.items()):
                continue
            s = 0.0
            for t in q:
                f = tf.get(t)
                if f:
                    s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
            if s > 0:
                scored.append((s, i))
        scored.sort(key=lambda x: (-x[0], self.rows[x[1]]["chunk_id"]))
        return [_row_to_result(self.rows[i], s, self.name) for s, i in scored[:top_k]]


class HybridRetriever:
    name = "hybrid_rrf"

    def __init__(self, strategies: tuple[str, ...]) -> None:
        self.dense, self.bm25 = DenseRetriever(strategies), BM25Retriever(strategies)

    def search(self, query: str, top_k: int, filters: dict | None = None) -> list[dict]:
        fused: dict[str, dict] = {}
        for ranking in (self.dense.search(query, FUSION_DEPTH, filters), self.bm25.search(query, FUSION_DEPTH, filters)):
            for rank, r in enumerate(ranking, 1):
                e = fused.setdefault(r["id"], {**r, "score": 0.0, "component_ranks": {}})
                e["score"] += 1.0 / (RRF_K + rank)
                e["component_ranks"][r["method"]] = rank
        out = sorted(fused.values(), key=lambda r: (-r["score"], r["id"]))[:top_k]
        for r in out:
            r["method"] = self.name
        return out


@lru_cache(maxsize=1)
def cross_encoder():
    from sentence_transformers import CrossEncoder
    return CrossEncoder(os.getenv("RERANK_MODEL", "BAAI/bge-reranker-v2-m3"), max_length=512)


class RerankRetriever:
    name = "hybrid_rerank"

    def __init__(self, strategies: tuple[str, ...], candidates: int = 20) -> None:
        self.base, self.candidates = HybridRetriever(strategies), candidates

    def search(self, query: str, top_k: int, filters: dict | None = None) -> list[dict]:
        cands = self.base.search(query, self.candidates, filters)
        if not cands:
            return []
        scores = cross_encoder().predict([(query, c["text"]) for c in cands], batch_size=8)
        for c, s in zip(cands, scores):
            c["rrf_score"], c["score"], c["method"] = c["score"], float(s), self.name
        return sorted(cands, key=lambda r: (-r["score"], r["id"]))[:top_k]


METHODS = {"dense": DenseRetriever, "bm25": BM25Retriever, "hybrid": HybridRetriever, "rerank": RerankRetriever}


def build(method: str, index: str) -> Any:
    strategies = tuple(index)  # "B" -> ("B",), "BV" -> ("B", "V")
    return METHODS[method](strategies)


def timed_search(retriever, query: str, top_k: int, filters: dict | None = None) -> tuple[list[dict], float]:
    t0 = time.perf_counter()
    res = retriever.search(query, top_k, filters)
    for rank, r in enumerate(res, 1):
        r["rank"] = rank
    return res, (time.perf_counter() - t0) * 1000
