# Day 7: Agentic RAG · cách chạy và tái lập

Bài làm của Nguyễn Minh Phương (2A202603997). Đề bài gốc ở [README.md](README.md). Báo cáo ở [report/individual/2A202603997_NguyenMinhPhuong.md](report/individual/2A202603997_NguyenMinhPhuong.md). Demo ở [demo/](demo/), xem [HUONG_DAN_DEMO.md](demo/HUONG_DAN_DEMO.md).

## Thành phần

| Thành phần | Lựa chọn |
|---|---|
| Tài liệu | Sách trắng TMĐT Việt Nam 2023 (100 trang), tải theo URL và kiểm sha256 ở mục 2 |
| Vector store | **Dùng lại Day 6**: PostgreSQL 16 + pgvector 0.8.7, bảng `chunks`, HNSW cosine |
| Embedding | `aisingapore/SEA-LION-E5-Embedding-600M`, 1024 chiều, local (code Day 6) |
| Index | `B` = chunk text Day 6 (173); `V` = bảng/biểu đồ/sơ đồ do vision model chép (Day 7) |
| Retrieval | dense, BM25 (âm tiết + bigram), hybrid RRF (k = 60), rerank `BAAI/bge-reranker-v2-m3` |
| Agent | `gpt-4o-mini` tool calling: `search_documents`, `read_page`, `answer`, `abstain`; cấu hình A0–A3 trong `src/rag/agent.py` |
| Benchmark | `benchmark/questions.json`: 50 câu, dev 20 / test 30 |

```text
src/rag/
  common.py          env, kết nối Day 6 (embedder + store), client LLM có ghi token/chi phí
  visual_index.py    index V: render trang → vision → chunk → embed → pgvector
  retrievers.py      dense / bm25 / hybrid / rerank
  gold.py            khớp evidence (chỉ dùng khi chấm)
  eval_retrieval.py  Hit@1, Evidence Hit@3, Context Evidence Rate, MRR
  agent.py           agent + chạy benchmark, lưu trace
  review.py          phiếu chấm tay + tổng hợp metrics từ nhãn
  verify.py          chứng minh citation: dòng DB + PDF gốc
  demo_server.py     server demo live (127.0.0.1)
  build_demo.py, build_report.py   sinh trang demo và báo cáo từ results/
```

## 1. Cài đặt

Cần repo Day 6 đã cài (venv có torch, sentence-transformers, psycopg, pgvector, PyMuPDF, pypdf) và Docker.

```bash
# DB Day 6
cd <repo Day 6>/starter && docker compose -p day6_student_starter up -d --wait
# Nếu volume DB trống: chạy lại pipeline Day 6 để có index B
python -c "from src.run import main; main()"      # ~13 phút CPU, tái lập đúng số Day 6

# Day 7
cd <repo Day 7>
cp .env.example .env          # điền OPENAI_API_KEY; DAY6_STARTER trỏ tới thư mục starter Day 6
PY=<repo Day 6>/starter/.venv/bin/python
python3 -m unittest discover -s tests -v   # test offline (không cần DB/LLM)
```

## 2. Dữ liệu

```bash
curl -L -o data/BCTMDT2023-file-31-1-pdf.pdf "https://valoma.vn/wp-content/uploads/2024/05/BCTMDT2023-file-31-1-pdf.pdf"
sha256sum data/BCTMDT2023-file-31-1-pdf.pdf
# 4b7e4a29d5b7f33282f243116d2a2b59f1fb261b8fa76225f7788def2ccb430f
```

PDF và ảnh trang không được commit (chưa rõ quyền tái phân phối).

## 3. Chạy

```bash
# Index V (khoảng $0,41, chạy 1 lần). Đã có output thô thì dựng lại không gọi API:
$PY -m src.rag.visual_index --pages 1-100 --workers 8
$PY -m src.rag.visual_index --skip-extract

# Retrieval: câu hỏi gốc, không filter
$PY -m src.rag.eval_retrieval --split dev  --configs dense:B bm25:B hybrid:B rerank:B dense:BV bm25:BV hybrid:BV rerank:BV rerank:BV:k=5:budget=6000
$PY -m src.rag.eval_retrieval --split test --configs dense:B rerank:BV:k=5:budget=6000   # chỉ sau khi chốt

# Agent: dev để chọn cấu hình
for c in A0 A1 A2 A3; do $PY -m src.rag.agent --split dev --config $c; done
# Ghi results/selection.json (cấu hình + tiêu chí) TRƯỚC khi chạy test
$PY -m src.rag.agent --split test --config A0
$PY -m src.rag.agent --split test --config <đã chọn>

# Chấm: đọc phiếu, ghi reviews.json, tổng hợp
$PY -m src.rag.review sheet   --split test --config <cfg>
$PY -m src.rag.review metrics --split test --config <cfg>

# Báo cáo + demo (sinh từ results/)
$PY -m src.rag.build_report
$PY -m src.rag.build_demo
$PY -m src.rag.demo_server --warm        # http://127.0.0.1:8765/
```

## 4. Kiểm chứng một câu trả lời

```bash
$PY -m src.rag.verify --trace results/agent/test/<cfg>/traces.json --id t17 --find "20,5"
```

Xem thêm [demo/README_KIEM_CHUNG.md](demo/README_KIEM_CHUNG.md): SQL trực tiếp vào pgvector và cách đối chiếu với PDF gốc.

## 5. Quy tắc đã tuân thủ

- Đáp án và evidence gold không vào agent hay retrieval. Chỉ `gold.py`, `eval_retrieval.py` và `review.py` đọc chúng, ở bước chấm.
- Chọn cấu hình trên dev, ghi tiêu chí vào `results/selection.json` trước khi chạy test.
- Lỗi API/DB được ghi vào trace, không thay bằng kết quả giả.
- `.env`, API key, PDF và ảnh trang không được commit.
