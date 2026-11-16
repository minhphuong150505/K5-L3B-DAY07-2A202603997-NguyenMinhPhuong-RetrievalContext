"""Offline tests for Day 7 evaluation helpers (no DB, no LLM)."""
import importlib.util
import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    # load src/rag/<name>.py without triggering common.load_env() (needs Day 6 + .env)
    pkg = sys.modules.setdefault("src.rag", types.ModuleType("src.rag"))
    common = types.ModuleType("src.rag.common")
    import unicodedata
    common.norm = lambda t: "".join(unicodedata.normalize("NFC", t).casefold().split())
    sys.modules["src.rag.common"] = common
    pkg.common = common
    spec = importlib.util.spec_from_file_location(f"src.rag.{name}", ROOT / "src" / "rag" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


gold = load("gold")
Q_ANY = {"gold": [{"page": 40, "match": ["20,5"]}, {"page": 3, "match": ["20,5 tỷ USD"]}]}
Q_ALL = {"gold_mode": "all", "gold": [{"page": 40, "match": ["20,5"]}, {"page": 37, "match": ["16"]},
                                      {"page": 36, "match": ["16"], "alternative_of": 1}]}


class GoldTest(unittest.TestCase):
    def test_page_and_whitespace_insensitive(self):
        self.assertTrue(gold.supports({"page": 40, "text": "Doanh thu 20, 5 tỷ"}, {"page": 40, "match": ["20,5"]}))
        self.assertFalse(gold.supports({"page": 41, "text": "20,5"}, {"page": 40, "match": ["20,5"]}))

    def test_any_mode(self):
        self.assertTrue(gold.full_hit(Q_ANY, [{"page": 3, "text": "đạt 20,5 tỷ USD"}]))

    def test_all_mode_needs_every_group_and_accepts_alternatives(self):
        c40, c36 = {"page": 40, "text": "20,5"}, {"page": 36, "text": "16"}
        self.assertTrue(gold.any_hit(Q_ALL, [c40]))
        self.assertFalse(gold.full_hit(Q_ALL, [c40]))
        self.assertTrue(gold.full_hit(Q_ALL, [c40, c36]))

    def test_first_hit_rank(self):
        ranked = [{"page": 1, "text": "x"}, {"page": 40, "text": "20,5"}]
        self.assertEqual(gold.first_hit_rank(Q_ANY, ranked), 2)


if __name__ == "__main__":
    unittest.main()
