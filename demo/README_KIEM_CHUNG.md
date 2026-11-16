# Cách chứng minh câu trả lời RAG là đúng

Mục tiêu: với mỗi câu agent trả lời, người xem tự kiểm được ba điều:

1. Citation có thật: chunk tồn tại trong vector store Day 6 (PostgreSQL + pgvector).
2. Chunk đúng nguồn: đúng tài liệu, đúng trang, và nội dung khớp bản gốc.
3. Chunk hỗ trợ câu trả lời: số liệu, đơn vị, năm và đối tượng trong chunk khớp với từng ý của câu trả lời.

Một citation hợp lệ về ID mới chứng minh điều 1. Điều 2 và 3 phải đọc đối chiếu bằng mắt. Phần dưới hướng dẫn làm cả ba.

---

## 0. Chuẩn bị (1 lần)

```bash
# DB Day 6 (pgvector) — chạy trong thư mục starter của repo Day 6
cd ~/Documents/Vin20K/Lab6/K5-L3B-DAY06-*/starter
docker --context default compose -p day6_student_starter up -d --wait

# Python dùng chung venv Day 6; chạy lệnh từ thư mục repo Day 7
cd ~/Documents/Vin20K/Lab7/K5-L3B-DAY07-*
PY=~/Documents/Vin20K/Lab6/K5-L3B-DAY06-*/starter/.venv/bin/python
```

Nguồn gốc tài liệu, để người khác tự tải và so:
- Sách trắng Thương mại điện tử Việt Nam 2023, Cục TMĐT và Kinh tế số, Bộ Công Thương.
- URL: `https://valoma.vn/wp-content/uploads/2024/05/BCTMDT2023-file-31-1-pdf.pdf`
- sha256: `4b7e4a29d5b7f33282f243116d2a2b59f1fb261b8fa76225f7788def2ccb430f`

```bash
sha256sum data/BCTMDT2023-file-31-1-pdf.pdf   # phải ra đúng hash trên
```

---

## 1. Đọc `chunk_id` trong citation

Định dạng: `<document_id>:p<trang>:<index><số>`

| Ví dụ | Ý nghĩa |
|---|---|
| `sach-trang-tmdt-2023:p040:B00` | trang 40, **index B** (Day 6: text PDF + OCR biểu đồ, chunk theo đoạn), chunk số 0 |
| `sach-trang-tmdt-2023:p40:V2` | trang 40, **index V** (Day 7: vision model chép bảng/biểu đồ), khối trực quan số 2 |

Số trang là trang vật lý của PDF (trang 1 là bìa), trùng với số in ở góc mỗi trang.

---

## 2. Kiểm tra trực tiếp trong DB (SQL)

```bash
docker --context default exec -it day6_student_starter-postgres-1 psql -U day6 -d day6_lab
```

```sql
-- Tổng quan các index trong cùng bảng chunks
SELECT strategy, count(*), min(page), max(page) FROM chunks GROUP BY 1 ORDER BY 1;
--  A | 232 | 3 | 96     (Day 6, fixed-size, không dùng ở Day 7)
--  B | 173 | 3 | 96     (Day 6, by_paragraph: index text dùng ở Day 7)
--  V | 119 | 8 | 95     (Day 7, bảng/biểu đồ/sơ đồ do vision model chép)

-- Xem đúng chunk được trích dẫn
SELECT strategy, chunk_id, page, section, model_name, text_hash, updated_at, text, metadata
FROM chunks WHERE chunk_id = 'sach-trang-tmdt-2023:p40:V2';

-- Mọi chunk của một trang, để xem ngữ cảnh lân cận
SELECT strategy, chunk_id, left(text, 200) FROM chunks WHERE page = 40 ORDER BY strategy, chunk_id;

-- Chứng minh vector thật (1024 chiều, cùng model với query), không phải vector giả
SELECT chunk_id, vector_dims(embedding), model_name FROM chunks WHERE chunk_id = 'sach-trang-tmdt-2023:p40:V2';

-- Tái hiện retrieval: chunk gần nhất với chính chunk này (cosine)
SELECT chunk_id, page, 1 - (embedding <=> (SELECT embedding FROM chunks WHERE chunk_id='sach-trang-tmdt-2023:p40:V2')) AS cosine
FROM chunks WHERE strategy IN ('B','V') ORDER BY 3 DESC LIMIT 5;
```

Với chunk V, `metadata` còn ghi `page_image` (ảnh trang để so), `region` (vị trí trên trang), `visual_type` và `extractor` (model đã đọc ảnh).

---

## 3. Kiểm tra tự động bằng script `verify`

```bash
# Kiểm mọi citation của một câu trả lời đã lưu trong trace
$PY -m src.rag.verify --trace results/agent/test/A2/traces.json --id t17 --find "20,5" --find "16"

# Hoặc kiểm một chunk bất kỳ
$PY -m src.rag.verify --chunk "sach-trang-tmdt-2023:p40:V2" --find "336"
```

Với mỗi citation, script in ra:
- dòng tương ứng trong pgvector: index, trang, model embedding, số chiều, hash;
- chuỗi cần tìm có nằm trong chunk ở DB không, và có nằm trong text layer của đúng trang PDF (đọc bằng pypdf) không;
- đường dẫn ảnh trang để so bằng mắt;
- hash và URL nguồn của PDF.

Cách đọc kết quả:
- **Chunk B:** text được trích từ chính PDF, nên các dòng của chunk sẽ báo `xuất hiện trong text layer PDF: True`.
- **Chunk V:** do vision model đọc từ ảnh, nên có thể không trùng nguyên văn với text layer, vì biểu đồ được vẽ bằng vector. Khi đó phải mở ảnh trang (`work/pages_hd/pNNN.png`) để so từng số. **Không coi chunk V là đúng chỉ vì model đã sinh ra nó.** Biên bản kiểm tay nằm ở `results/visual/manual_check.md` (ví dụ: biểu đồ tròn hay bị ghép sai nhãn).

---

## 4. Kiểm bằng mắt với bản gốc

1. Mở PDF gốc, hoặc `../work/pages_hd/p040.png`, đến đúng trang trong `chunk_id`.
2. Tìm vùng ghi trong `metadata.region` hoặc trong cột "Evidence" của benchmark (`benchmark/questions.json`, trường `gold[].region`).
3. So từng ý của câu trả lời: con số, đơn vị (tỷ USD, %, triệu người), năm (không lấy cột dự báo `*`), đối tượng (quốc gia, loại website), và phép tính nếu có.
4. Ghi nhãn vào `results/agent/<split>/<config>/reviews.json` (xem mục 5).

---

## 5. Nhãn chấm và cách tái tạo số liệu

| File | Nội dung |
|---|---|
| `benchmark/questions.json` | câu hỏi, đáp án, trang, vùng, evidence nguyên văn, chuỗi khớp, lý do thiếu bằng chứng |
| `results/agent/<split>/<cfg>/traces.json` | toàn bộ tool call, query, kết quả (id, trang, score), context, câu trả lời, citation, token, chi phí, thời gian |
| `results/agent/<split>/<cfg>/review_sheet.md` | phiếu chấm: câu hỏi, đáp án chuẩn, câu trả lời, nội dung từng citation |
| `results/agent/<split>/<cfg>/reviews.json` | nhãn: `answer_grade` 0/1/2, `citation_support`, `abstention_correct`, `pass`, `reason` |
| `results/agent/<split>/<cfg>/summary_labels.json` | metrics tổng hợp từ nhãn: grounded, citation hợp lệ, từ chối, tỷ lệ đạt theo nhóm |
| `results/retrieval/<split>/summary.json` | Hit@1, Evidence Hit@3, Context Evidence Rate, MRR theo từng phương pháp |

```bash
$PY -m src.rag.review sheet   --split test --config A2   # sinh phiếu chấm
$PY -m src.rag.review metrics --split test --config A2   # tổng hợp từ nhãn
$PY -m src.rag.build_demo                                # sinh lại Demo/index.html từ results/
```

> Lưu ý trung thực: nhãn trong `reviews.json` do trợ lý AI soạn sau khi đối chiếu trang gốc, có ghi lý do. Sinh viên cần tự rà lại từng nhãn trước khi nộp (TODO(SV)). LLM không tự chấm thay người.

---

## 6. Vì sao kết quả không bị "rò đáp án"

- `src/rag/agent.py` chỉ truyền **câu hỏi** vào model. Đáp án chuẩn, trang gold và evidence chỉ được đọc trong `gold.py`, `eval_retrieval.py` và `review.py`, tức là ở bước chấm.
- Cấu hình được chốt trên dev (`results/agent/dev/*`) **trước** khi chạy test. Có thể kiểm tra bằng thời gian ghi file và lịch sử git.
- Lỗi API hoặc DB được ghi vào trace với `status: "error"`, không thay bằng kết quả giả.
