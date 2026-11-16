"""Local live-demo server for the RAG visualiser (stdlib only, binds 127.0.0.1).

Run:  python -m src.rag.demo_server [--port 8765]   then open http://127.0.0.1:8765/

Endpoints
  GET /                      -> Demo/live.html
  GET /pages/pNNN.png        -> rendered PDF page (work/pages_hd) for visual verification
  GET /api/questions         -> benchmark questions (question text; gold only for the presenter panel)
  GET /api/ask?q=..&config=A2 -> Server-Sent Events: every agent event live (llm step, search results with
                                 chunk text, quote check, answer/abstain), then the final trace
  GET /api/retrieve?q=..     -> side-by-side rankings: dense, bm25, hybrid RRF, rerank (index BV) + timings
  GET /api/chunk?id=..       -> the chunk row exactly as stored in pgvector (+ SQL to re-check it)
  GET /api/traces?split=test&config=A2 -> saved traces for offline replay
The agent itself never sees gold: /api/ask only passes the typed question.
"""
from __future__ import annotations

import argparse
import json
import threading
import time
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .common import RESULTS, ROOT, WORK, db, load_corpus, load_questions

DEMO_DIR = ROOT.parent / "Demo"
_agents: dict = {}
_retrievers: dict = {}
_lock = threading.Lock()
_corpus: dict[str, dict] = {}


def corpus() -> dict[str, dict]:
    if not _corpus:
        for r in load_corpus(("B", "V")):
            _corpus[r["chunk_id"]] = r
    return _corpus


def agent(cfg: str):
    from .agent import Agent
    if cfg not in _agents:
        _agents[cfg] = Agent(cfg)
    return _agents[cfg]


def retriever(method: str):
    from .retrievers import build
    if method not in _retrievers:
        _retrievers[method] = build(method, "BV")
    return _retrievers[method]


def enrich(ev: dict) -> dict:
    """Attach chunk text/metadata to search results so the UI can show them (UI only)."""
    if ev.get("event") == "search":
        c = corpus()
        ev = {**ev, "results": [{**r, "index": c.get(r["id"], {}).get("strategy"),
                                 "text": c.get(r["id"], {}).get("text", ""),
                                 "visual_type": (c.get(r["id"], {}).get("metadata") or {}).get("visual_type")}
                                for r in ev.get("results", [])]}
    return ev


class Handler(BaseHTTPRequestHandler):
    server_version = "RAGDemo/1.0"

    def log_message(self, fmt, *args):
        print(f"[{time.strftime('%H:%M:%S')}] {self.address_string()} {fmt % args}")

    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False, default=str).encode(), "application/json; charset=utf-8")

    def do_GET(self) -> None:  # noqa: N802
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        try:
            if u.path in ("/", "/live.html"):
                return self._send(200, (DEMO_DIR / "live.html").read_bytes(), "text/html; charset=utf-8")
            if u.path.startswith("/pages/"):
                name = Path(u.path).name
                f = WORK / "pages_hd" / name
                if not (name.startswith("p") and name.endswith(".png") and f.exists()):
                    return self._json({"error": "không có ảnh trang"}, 404)
                return self._send(200, f.read_bytes(), "image/png")
            if u.path == "/api/questions":
                return self._json(load_questions())
            if u.path == "/api/chunk":
                with db() as conn, conn.cursor() as cur:
                    cur.execute("""SELECT strategy, chunk_id, page, section, model_name, text_hash, updated_at,
                                          vector_dims(embedding) AS dims, text, metadata
                                   FROM chunks WHERE chunk_id = %s""", (q.get("id", ""),))
                    row = cur.fetchone()
                    cols = [d.name for d in cur.description]
                if not row:
                    return self._json({"error": "không có chunk này trong pgvector"}, 404)
                d = dict(zip(cols, row))
                d["sql"] = f"SELECT strategy, page, text, metadata FROM chunks WHERE chunk_id = '{d['chunk_id']}';"
                return self._json(d)
            if u.path == "/api/traces":
                p = RESULTS / "agent" / q.get("split", "test") / q.get("config", "A2") / "traces.json"
                return self._json(json.loads(p.read_text(encoding="utf-8")) if p.exists() else [])
            if u.path == "/api/retrieve":
                from .retrievers import timed_search
                text = q.get("q", "").strip()
                out = {}
                with _lock:
                    for m in ("dense", "bm25", "hybrid", "rerank"):
                        res, ms = timed_search(retriever(m), text, 5)
                        out[m] = {"ms": round(ms, 1), "results": [
                            {"rank": r["rank"], "id": r["id"], "page": r["page"], "score": round(r["score"], 4),
                             "index": r["metadata"].get("index"), "text": r["text"][:500],
                             "component_ranks": r.get("component_ranks")} for r in res]}
                return self._json(out)
            if u.path == "/api/ask":
                return self._ask(q.get("q", "").strip(), q.get("config", "A2"))
            return self._json({"error": "not found"}, 404)
        except BrokenPipeError:
            pass
        except Exception as e:  # show the real error in the UI; never fake a result
            traceback.print_exc()
            try:
                self._json({"error": f"{type(e).__name__}: {e}"}, 500)
            except Exception:
                pass

    def _ask(self, question: str, cfg: str) -> None:
        if not question:
            return self._json({"error": "câu hỏi rỗng"}, 400)
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

        def push(kind: str, obj) -> None:
            self.wfile.write(f"event: {kind}\ndata: {json.dumps(obj, ensure_ascii=False, default=str)}\n\n".encode())
            self.wfile.flush()

        with _lock:
            push("status", {"message": f"Nạp cấu hình {cfg} (lần đầu ~20–30 s: model embedding, BM25, reranker)…"})
            a = agent(cfg)
            push("config", {"config": cfg, **a.cfg, "model": a.model})
            try:
                trace = a.run("live", question, on_event=lambda ev: push("step", enrich(ev)))
                push("done", trace)
            except Exception as e:
                push("error", {"error": f"{type(e).__name__}: {e}"})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--warm", action="store_true", help="nạp sẵn agent A2 trước khi mở trang")
    a = ap.parse_args()
    if a.warm:
        print("Đang nạp sẵn A2 + corpus…")
        agent("A2")
        corpus()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    print(f"Mở http://127.0.0.1:{a.port}/   (Ctrl+C để dừng)")
    srv.serve_forever()


if __name__ == "__main__":
    main()
