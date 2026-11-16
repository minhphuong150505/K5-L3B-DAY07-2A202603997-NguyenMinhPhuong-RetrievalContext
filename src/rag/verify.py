"""Prove a cited answer: show the cited chunk exactly as stored in pgvector + the original PDF page.

Usage:
  python -m src.rag.verify --chunk "sach-trang-tmdt-2023:p40:V2"          # one chunk
  python -m src.rag.verify --trace results/agent/test/A2/traces.json --id t17   # all citations of an answer
  python -m src.rag.verify --chunk ... --find "20,5"                       # also locate a string on the PDF page

For each citation it prints: DB row (strategy/index, page, metadata, text), whether the text is
also present in the PDF text layer of that page (pypdf), the page image path to compare visually,
and the external source URL + sha256 of the PDF so anyone can re-check the original.
"""
from __future__ import annotations

import argparse
import hashlib
import json

from .common import PDF_PATH, ROOT, db, norm

SOURCE_URL = "https://valoma.vn/wp-content/uploads/2024/05/BCTMDT2023-file-31-1-pdf.pdf"


def pdf_page_text(page: int) -> str:
    from pypdf import PdfReader
    return PdfReader(str(PDF_PATH)).pages[page - 1].extract_text() or ""


def show(chunk_id: str, find: list[str]) -> None:
    with db() as conn, conn.cursor() as cur:
        cur.execute("""SELECT strategy, chunk_id, page, section, text, metadata, model_name, text_hash, updated_at,
                              vector_dims(embedding) FROM chunks WHERE chunk_id = %s""", (chunk_id,))
        row = cur.fetchone()
    if not row:
        print(f"!! {chunk_id}: KHÔNG có trong pgvector")
        return
    strategy, cid, page, section, text, md, model, h, upd, dims = row
    print("=" * 100)
    print(f"chunk_id : {cid}\nindex    : {strategy} ({'Day 6 text, by_paragraph' if strategy == 'B' else 'Day 7 visual extraction' if strategy == 'V' else strategy})")
    print(f"trang PDF: {page}   section: {section}   embedding: {model} ({dims} chiều)   sha256(text): {h[:16]}…   cập nhật: {upd}")
    if md.get("page_image"):
        print(f"ảnh trang để đối chiếu: {ROOT.parent / md['page_image']}   vùng: {md.get('region')}   loại: {md.get('visual_type')}")
    print("-" * 40 + " TEXT TRONG DB " + "-" * 40)
    print(text)
    layer = pdf_page_text(page)
    print("-" * 40 + f" ĐỐI CHIẾU PDF trang {page} " + "-" * 30)
    for s in find:
        print(f"  '{s}' trong chunk DB: {norm(s) in norm(text)} | trong text layer PDF: {norm(s) in norm(layer)}")
    lines = [l for l in text.splitlines()[1:] if len(l.strip()) > 12][:6]
    for l in lines:
        frag = l.strip()[:40]
        print(f"  dòng chunk '{frag}…' xuất hiện trong text layer PDF: {norm(frag) in norm(layer)}")
    print("  (chunk V do vision model đọc từ ảnh: nếu text layer không có, mở ảnh trang ở trên để so)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chunk", action="append", default=[])
    ap.add_argument("--trace")
    ap.add_argument("--id")
    ap.add_argument("--find", action="append", default=[])
    a = ap.parse_args()
    print(f"Nguồn gốc: {SOURCE_URL}\nFile local: {PDF_PATH}  sha256={hashlib.sha256(PDF_PATH.read_bytes()).hexdigest()}")
    ids = list(a.chunk)
    if a.trace:
        t = next(t for t in json.loads(open(a.trace, encoding='utf-8').read()) if t["query_id"] == a.id)
        print(f"\nCâu {t['query_id']}: {t['question']}\nTrả lời ({t['status']}): {t['answer']}")
        ids += t["citations"]
    for c in ids:
        show(c, a.find)


if __name__ == "__main__":
    main()
