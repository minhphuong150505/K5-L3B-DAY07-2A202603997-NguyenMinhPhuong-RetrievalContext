"""Shared helpers: env, Day 6 imports, DB access, OpenRouter client with cost tracking."""
from __future__ import annotations

import http.client
import json
import os
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from functools import lru_cache
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"
BENCHMARK = ROOT / "benchmark" / "questions.json"
PDF_PATH = ROOT / "data" / "BCTMDT2023-file-31-1-pdf.pdf"
WORK = ROOT.parent / "work"          # page renders (not committed: copyrighted)
SOURCE_ID = "sach-trang-tmdt-2023"
TEXT_INDEX = "B"                      # Day 6 chosen index: by_paragraph chunks
VISUAL_INDEX = "V"                    # Day 7: vision-extracted tables/charts/diagrams


def load_env() -> None:
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
    starter = os.getenv("DAY6_STARTER")
    if not starter:
        raise SystemExit("DAY6_STARTER chưa đặt (xem .env.example)")
    path = (ROOT / starter).resolve() if not os.path.isabs(starter) else Path(starter)
    if not (path / "src" / "store.py").exists():
        raise SystemExit(f"Không tìm thấy code Day 6 tại {path}")
    # Day 6 code is a package named `src` too; load it under the alias `day6src`.
    if "day6src" not in sys.modules:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "day6src", path / "src" / "__init__.py", submodule_search_locations=[str(path / "src")])
        mod = importlib.util.module_from_spec(spec)
        sys.modules["day6src"] = mod
        spec.loader.exec_module(mod)


load_env()


def norm(text: str) -> str:
    """NFC + casefold + drop all whitespace: robust substring match for gold keys."""
    t = unicodedata.normalize("NFC", text).casefold()
    return "".join(t.split())


def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")


BENCHMARK_TEST2 = ROOT / "benchmark" / "questions_test2.json"


def load_questions(split: str | None = None) -> list[dict]:
    """dev/test from questions.json; test2/test3 (fresh held-out sets, see README_DAY7.md) from their own files."""
    if split in ("test2", "test3"):  # fresh held-out sets, each in its own file
        return read_json(ROOT / "benchmark" / f"questions_{split}.json")
    qs = read_json(BENCHMARK)
    return [q for q in qs if split in (None, "all") or q["split"] == split]


# ---------------------------------------------------------------- Day 6 bits
@lru_cache(maxsize=1)
def embedder():
    from day6src.embeddings import SeaLionEmbedder  # Day 6 code
    return SeaLionEmbedder()


@lru_cache(maxsize=1)
def store():
    from day6src.store import PgVectorStore  # Day 6 code
    return PgVectorStore(os.environ["DATABASE_URL"], dimensions=1024,
                         model_name=os.getenv("EMBEDDING_MODEL", "aisingapore/SEA-LION-E5-Embedding-600M"))


def db():
    return store()._connect()


def load_corpus(strategies: tuple[str, ...]) -> list[dict]:
    """All chunks of the given indexes, straight from pgvector (single source of truth)."""
    with db() as conn, conn.cursor() as cur:
        cur.execute("""SELECT strategy, chunk_id, document_id, source, page, section, text, metadata
                       FROM chunks WHERE strategy = ANY(%s) ORDER BY page, strategy, chunk_id""",
                    (list(strategies),))
        cols = [d.name for d in cur.description]
        rows = [dict(zip(cols, r)) for r in cur.fetchall()]
    if not rows:
        raise SystemExit(f"Không có chunk nào cho index {strategies} trong pgvector")
    return rows


# ---------------------------------------------------------------- LLM client
class LLMError(RuntimeError):
    pass


# Public list prices (USD / 1M tokens) used only to report an "equivalent paid cost"
# when the free tier is used (actual cost 0). Source: ai.google.dev/pricing, checked 2026-11 (OpenRouter list prices for the same models).
PRICE_PER_M = {"gemini-2.5-flash": (0.30, 2.50), "gemini-2.5-flash-lite": (0.10, 0.40),
               "gemini-3-flash-preview": (0.50, 3.00),
               "gemini-3.5-flash": (1.50, 9.00), "gemini-3.1-flash-lite": (0.25, 1.50),
               "gpt-4o-mini": (0.15, 0.60), "gpt-4.1": (2.00, 8.00)}  # openai.com/api/pricing (standard tier)

PROVIDERS = {
    "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions", "GEMINI_API_KEY"),
    "openrouter": ("https://openrouter.ai/api/v1/chat/completions", "OPENROUTER_API_KEY"),
    "openai": ("https://api.openai.com/v1/chat/completions", "OPENAI_API_KEY"),
}


class OpenRouter:
    """OpenAI-compatible chat client (Gemini API or OpenRouter), retries 429/5xx only."""

    def __init__(self, model: str, timeout: int = 180, retries: int = 6, provider: str | None = None) -> None:
        self.provider = provider or os.getenv("LLM_PROVIDER", "gemini")
        self.url, key_name = PROVIDERS[self.provider]
        self.model = model
        self.key = os.environ.get(key_name)
        if not self.key:
            raise SystemExit(f"{key_name} chưa đặt trong .env")
        self.timeout, self.retries = timeout, retries

    def chat(self, messages: list[dict], **params: Any) -> dict:
        body = {"model": self.model, "messages": messages, **params}
        if self.provider == "openrouter":
            body["usage"] = {"include": True}
        data = json.dumps(body).encode()
        last, waited = None, 0.0
        for attempt in range(self.retries):
            req = urllib.request.Request(self.url, data=data, headers={
                "Authorization": f"Bearer {self.key}", "Content-Type": "application/json"})
            t0 = time.perf_counter()
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    out = json.loads(r.read())
            except urllib.error.HTTPError as e:
                detail = e.read().decode(errors="replace")[:400]
                last = f"HTTP {e.code}: {detail}"
                if e.code == 429 or e.code >= 500:
                    delay = min(60, 10 * (attempt + 1))
                    waited += delay
                    time.sleep(delay)
                    continue
                raise LLMError(last) from None
            except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException) as e:
                # transient network errors (timeout, reset, RemoteDisconnected): retry, then report
                last = f"{type(e).__name__}: {e}"
                time.sleep(5 * (attempt + 1))
                continue
            if not out.get("choices"):
                last = json.dumps(out, ensure_ascii=False)[:400]
                time.sleep(5)
                continue
            usage = out.get("usage") or {}
            pt, ct = usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0)
            pin, pout = PRICE_PER_M.get(self.model, (0.0, 0.0))
            out["_meta"] = {"latency_s": round(time.perf_counter() - t0, 3), "prompt_tokens": pt,
                            "completion_tokens": ct,
                            # actual billed: OpenRouter reports it; OpenAI bills tokens x list price; Gemini free tier = 0
                            "cost_usd": (float(usage.get("cost") or 0.0) if self.provider != "openai"
                                         else round((pt * pin + ct * pout) / 1e6, 6)),
                            "equiv_cost_usd": round((pt * pin + ct * pout) / 1e6, 6),
                            "attempts": attempt + 1, "rate_limit_wait_s": waited,
                            "provider": self.provider, "model": self.model}
            return out
        raise LLMError(f"LLM thất bại sau {self.retries} lần: {last}")
