# Báo cáo Day 7: Agentic RAG trên Sách trắng TMĐT Việt Nam 2023

Sinh viên: **Nguyễn Minh Phương** · MSSV **2A202603997** · lớp K5-L3B. TODO(SV): kiểm tra lại họ tên/MSSV.
Repo: `K5-L3B-DAY07-2A202603997-NguyenMinhPhuong-RetrievalContext`. Báo cáo sinh bởi `python -m src.rag.build_report`; mọi bảng số liệu đọc trực tiếp từ `results/`.

> Ghi chú minh bạch: code, benchmark và nhãn chấm được soạn với trợ lý AI (Claude Code). Nhãn chấm (`reviews.json`) được soạn bằng cách đối chiếu từng câu trả lời với trang PDF gốc, có ghi lý do; **sinh viên cần tự rà lại toàn bộ nhãn trước khi nộp** (RULES.md). TODO(SV): xác nhận đã rà.

## Dữ liệu và benchmark

- **Nguồn, quyền sử dụng, số trang và số chunk:** *Sách trắng Thương mại điện tử Việt Nam 2023*, Cục Thương mại điện tử và Kinh tế số – Bộ Công Thương (tài liệu công bố công khai). Bản PDF tải từ `https://valoma.vn/wp-content/uploads/2024/05/BCTMDT2023-file-31-1-pdf.pdf`, sha256 `4b7e4a29d5b7f33282f243116d2a2b59f1fb261b8fa76225f7788def2ccb430f`. PDF **không commit** vì chưa rõ quyền tái phân phối; người chấm tải lại theo URL và kiểm hash. 100 trang vật lý, 81 trang nội dung (Day 6). Index **B** (Day 6, by_paragraph): 173 chunk; index **V** (Day 7, vision): 119 chunk trên 66 trang (diagram: 6, infographic: 8, pie_chart: 24, bar_chart: 62, table: 19).
- **Vector store, embedding model, phiên bản và số chiều:** PostgreSQL 16.16 + pgvector 0.8.7 (Docker, `pgvector/pgvector:0.8.7-pg16`), bảng `chunks` của Day 6, HNSW `vector_cosine_ops`, `hnsw.ef_search=100`, `iterative_scan=relaxed_order`. Embedding `aisingapore/SEA-LION-E5-Embedding-600M` (sentence-transformers 5.7.0, CPU), **1024 chiều**, max 512 token, query dùng prompt `Retrieval`, vector chuẩn hóa L2 — giống hệt Day 6 nên query embedding tương thích index. Index V được embed bằng **cùng model**, ghi vào **cùng bảng** (strategy `V`); index B không đổi. Kết nối: `DATABASE_URL` trong `.env` (xem `.env.example`); code Day 6 (`embeddings.py`, `store.py`) được import trực tiếp qua `DAY6_STARTER`. Đã tái lập Day 6: dev Hit@1 9/15, Hit@3 13/15 — khớp báo cáo Day 6.
- **Agent model, cách chạy và phân chia dev/test:** agent `gpt-4o-mini` (OpenAI Chat Completions, tool calling, temperature 0); vision cho index V cũng `gpt-4o-mini` (ảnh trang 144 dpi). Rerank `BAAI/bge-reranker-v2-m3` chạy local. Benchmark `benchmark/questions.json`: **50 câu**, dev 20 (16 có đáp án + 4 thiếu bằng chứng), test 30 (24 + 6); chia trước khi thử nghiệm; câu test không trùng benchmark Day 6. Lệnh chạy: mục "Đường dẫn trace…" bên dưới.
- **Cách xác định câu có/thiếu evidence và tiêu chí chấm:** câu có đáp án được soạn bằng cách đọc ảnh trang gốc; mỗi câu ghi trang, **vùng** (hàng/cột bảng, cột biểu đồ, ô sơ đồ), evidence nguyên văn, chuỗi khớp `match` (đã kiểm: mọi `match` có trong text layer đúng trang), phép tính nếu có. Câu thiếu bằng chứng là câu **gần chủ đề** (sai năm, sai quốc gia, chỉ tiêu không có), kèm cách kiểm tra trong toàn văn (`absence_reason`, đã grep). Retrieval hit = chunk đúng trang **và** chứa mọi chuỗi `match`; câu multi-hop (`gold_mode: all`) chỉ tính "đủ evidence" khi có mọi nhóm bắt buộc. Câu thiếu evidence không vào mẫu số retrieval. Chấm câu trả lời theo BENCHMARK.md (0/1/2) và ADVANCED.md (đạt/không đạt).

## Retrieval và thử nghiệm

Câu hỏi gốc, không filter, cùng corpus/index/nhãn; top-3 luôn được xuất để so sánh Hit@3. Context Evidence Rate = mọi evidence bắt buộc nằm trong context đóng gói theo budget ký tự. Chi phí retrieval = $0 (model local); thời gian đo trên CPU laptop (rerank chậm vì CPU bị chia sẻ với job khác).

| Cấu hình | Phương pháp, top-k, filter, rerank, context budget | Giả thuyết / thay đổi | Split | Hit@1 | Evidence Hit@3 | Context Evidence Rate | Thời gian / chi phí |
|---|---|---|---|---|---|---|---|
| Baseline (Day 6) | `dense:B` · dense, index B, top-3, không filter, budget 4000 ký tự | Dense SEA-LION-E5 trên index B Day 6 — điểm xuất phát | dev | 14/16 (88%) | 16/16 (100%) | 13/16 (81%) | 374 ms/truy vấn (trung vị) · $0 |
| Phương pháp 2 | `bm25:B` · bm25, index B, top-3, không filter, budget 4000 ký tự | Lexical BM25 âm tiết+bigram: khớp số/tên riêng tốt hơn dense? | dev | 14/16 (88%) | 16/16 (100%) | 14/16 (88%) | 1 ms/truy vấn (trung vị) · $0 |
| Phương pháp 3 | `hybrid:B` · hybrid, index B, top-3, không filter, budget 4000 ký tự | RRF dense+BM25: bù điểm yếu của nhau | dev | 15/16 (94%) | 16/16 (100%) | 13/16 (81%) | 587 ms/truy vấn (trung vị) · $0 |
| Phương pháp 4 | `rerank:B` · rerank, index B, top-3, không filter, budget 4000 ký tự | Cross-encoder xếp lại 20 ứng viên hybrid | dev | 16/16 (100%) | 16/16 (100%) | 14/16 (88%) | 37472 ms/truy vấn (trung vị) · $0 |
| Cải thiện 1 | `dense:BV` · dense, index BV, top-3, không filter, budget 4000 ký tự | Thêm index V (bảng/biểu đồ do vision đọc): tăng hit cho câu bảng/biểu đồ | dev | 14/16 (88%) | 16/16 (100%) | 14/16 (88%) | 448 ms/truy vấn (trung vị) · $0 |
| Cải thiện 1b | `hybrid:BV` · hybrid, index BV, top-3, không filter, budget 4000 ký tự | Index V + hybrid | dev | 15/16 (94%) | 16/16 (100%) | 13/16 (81%) | 276 ms/truy vấn (trung vị) · $0 |
| Cải thiện 2 | `rerank:BV` · rerank, index BV, top-3, không filter, budget 4000 ký tự | Index V + rerank | dev | 14/16 (88%) | 16/16 (100%) | 14/16 (88%) | 25442 ms/truy vấn (trung vị) · $0 |
| Cải thiện 2b | `rerank:BV:k=5:budget=6000` · rerank, index BV, top-5, không filter, budget 6000 ký tự | Tăng top-k 3→5, budget 4000→6000: đủ evidence cho multi-hop | dev | 14/16 (88%) | 16/16 (100%) | 15/16 (94%) | 25049 ms/truy vấn (trung vị) · $0 |
| Cấu hình đã chọn (retrieval) | `rerank:BV:k=5:budget=6000` | Chạy sau khi chốt trên dev | test | chưa chạy |  |  |  |
| Baseline | `dense:B` | Day 6 nguyên trạng | test | chưa chạy |  |  |  |

**Nhận xét retrieval (dev):** index B của Day 6 đã khá mạnh vì Day 6 có OCR và ghép nhãn–giá trị biểu đồ, nên mọi phương pháp đạt Evidence Hit@3 16/16 trên dev; khác biệt nằm ở **Hit@1** và **Context Evidence Rate** (câu multi-hop cần đủ 2 trang). Rerank cho Hit@1 cao nhất nhưng chậm (CPU). Tăng top-k lên 5 giúp đủ evidence cho câu multi-hop. Lưu ý: metric khớp chuỗi trên trang có thể tính hit khi chunk đúng trang nhưng câu trả lời vẫn đọc sai ô — vì vậy đánh giá câu trả lời được chấm riêng ở mục sau.

**Hai (nhiều) lỗi dev, nguyên nhân, cách thử và lý do chọn cấu hình** (trace: `results/agent/dev/A0/traces.json`):

1. **d17 — bịa số năm khác (abstention sai).** Hỏi doanh thu B2C 2017 (không có). A0 trả lời "8,06 tỷ USD" — đó là số **2018** trong cùng biểu đồ tr. 40. *Nguyên nhân:* model thấy chunk gần đúng chủ đề và không kiểm năm. *Thử:* A1 (thêm index V, hybrid) → từ chối đúng; A2/A3 thêm luật bắt kiểm năm/đối tượng + trích dẫn nguyên văn → từ chối đúng.
2. **d20 — gán nhầm chỉ tiêu.** Hỏi số người dùng Internet Việt Nam (không có số tuyệt đối). A0 trả lời "43 triệu" — thật ra là **quy mô kinh tế Internet 43 tỷ USD (dự báo 2025)** tr. 34; A1/A2 vẫn trả lời sai ("51,58 triệu", lấy từ số toàn cầu). *Nguyên nhân:* model nhỏ suy diễn/tính từ số liệu khác chỉ tiêu. *Kết quả:* chưa sửa được hoàn toàn — xem giới hạn.
3. **d12 — chọn nhầm cột dự báo.** A0 lấy 24 tỷ (Việt Nam **2025\***) thay vì 16 tỷ (2023) → tỷ lệ sai. Index V chép biểu đồ dạng "nhãn — năm: giá trị" giúp tách năm rõ hơn.
4. **d11 — biểu đồ tròn bị đảo nhãn.** Cả text layer Day 6 lẫn index V (vision) gán 28,8% cho "website bán hàng" (đúng: 71,2%). *Nguyên nhân:* hai lát màu xanh gần nhau, chú giải tách khỏi lát. Kiểm tay 5/5 biểu đồ tròn của index V đều có lỗi ghép (`results/visual/manual_check.md`). Chưa sửa: cần vision mạnh hơn hoặc đọc màu chú giải theo toạ độ.
5. **A2 làm xấu đi (cải thiện thất bại).** Kiểm trích dẫn **nguyên văn tuyệt đối** khiến `gpt-4o-mini` từ chối nhầm nhiều câu đúng (d01, d04, d08, d10, d12…): model diễn đạt lại đoạn trích, gắn đoạn trích vào chunk khác cùng trang, viết `p37` thay vì `p037`, đổi `5.158`→`5,158`. *Thử:* A3 kiểm có dung sai (mọi con số phải khớp, ≥60% từ, chấp nhận đoạn trích nằm ở chunk khác đã tìm và chuyển citation sang chunk đó, sửa ID, cho sửa 2 lần).

**Tiêu chí chọn (công bố trước khi chạy test, `results/selection.json`):** TODO. Cấu hình được chọn: **(chưa chốt)** — (điền sau khi so sánh dev).

## Agent và đánh giá

- **Tool, số lượt gọi, điều kiện dừng, cách chọn context và xử lý lỗi:** tool `search_documents(query)` (retriever theo cấu hình), `read_page(page)` (mọi chunk B+V của một trang — A2/A3), `answer(answer, citations[, evidence])`, `abstain(reason)`. `tool_choice=required`; tối đa 5 (A0), 6 (A1), 8 (A2/A3) lượt LLM; lượt cuối chỉ được answer/abstain; hết lượt ⇒ từ chối (`step_limit`). Context = hợp các chunk đã trả về trong lượt chạy (khử trùng theo `chunk_id`), mỗi kết quả tool cắt theo `result_chars` (4000 ở A0, 7000 ở A1–A3); context gửi kèm `chunk_id | trang | index | loại`. Citation phải là `chunk_id` đã thấy trong lượt chạy, ID lạ bị loại; A2/A3 thêm kiểm trích dẫn (mục trên). Lỗi API/DB ghi vào trace `status: error`, không thay bằng kết quả giả; lỗi tạm thời (429/5xx/timeout) được thử lại có giới hạn. Nội dung tài liệu được khai báo là dữ liệu, không phải chỉ dẫn (system prompt).

| Cấu hình / split | Tool use | Số lượt gọi | Grounded answer 0/1/2 và trung bình /2 | Citation hợp lệ | Câu có citation | Abstention đúng | Từ chối nhầm |
|---|---|---|---|---|---|---|---|
| A0 / dev | 20/20 | 1 lượt: 10, 2 lượt: 8, 3 lượt: 1, 4 lượt: 1 (TB 2.25 lượt LLM) | 3/2/11 · 1.50 | 15/22 | 18/18 | 2/4 | 0/16 |
| A1 / dev | 20/20 | 1 lượt: 12, 2 lượt: 8 (TB 2 lượt LLM) | 3/2/11 · 1.50 | 21/23 | 15/15 | 3/4 | 2/16 |
| A2 / dev | 20/20 | 1 lượt: 12, 2 lượt: 7, 4 lượt: 1 (TB 2.35 lượt LLM) | 8/0/8 · 1.00 | 10/12 | 10/10 | 3/4 | 7/16 |
| A3 / dev | 20/20 | 1 lượt: 12, 2 lượt: 8 (TB 2 lượt LLM) | 1/4/11 · 1.62 | 18/22 | 17/17 | 3/4 | 0/16 |

Nhãn chấm (`reviews.json`) là của người chấm; "tự động" nghĩa là chỉ đếm hành vi từ chối từ trace, chưa chấm tay. Citation hợp lệ = citation có trong context **và** đọc thấy hỗ trợ ý được trích.

**Ví dụ từng câu test (cấu hình (chưa chốt)):**

| Query ID | Loại câu | Tool call và kết quả | Câu trả lời và citation | Nhãn, lý do |
|---|---|---|---|---|

- **Đường dẫn trace, nhãn, lệnh chạy, thời gian và chi phí:**
  - Trace agent: `results/agent/<split>/<A0|A1|A2|A3>/traces.json` (mọi tool call, query, kết quả id/trang/score, context, câu trả lời, citation, token, chi phí, thời gian); tổng hợp `summary.json`; nhãn `reviews.json`; phiếu chấm `review_sheet.md`; metrics từ nhãn `summary_labels.json`.
  - Trace retrieval: `results/retrieval/<split>/*.traces.json`, `summary.json`. Index V: `results/visual/` (extraction.jsonl có output thô + chi phí từng trang, chunks_V.jsonl, manual_check.md).
  - Lệnh: xem `README_DAY7.md`. Chi phí: index V $0.4097 (2,634,475 + 24,275 token); agent theo từng cấu hình ở cột chi phí trong `summary.json` (giá gpt-4o-mini $0,15/$0,60 cho 1M token input/output); embedding/BM25/rerank local $0.
- **Kết quả trước/sau, ví dụ lỗi, đánh đổi và giới hạn:** A1 so với A0 giảm bịa (từ chối đúng 2/4 → 3/4) nhưng bắt đầu từ chối nhầm; A2 giảm bịa thêm nhưng từ chối nhầm rất nhiều (đánh đổi precision/recall); A3 lấy lại độ phủ. Rerank + read_page tăng chất lượng context nhưng tăng thời gian (CPU) và số token (context dài hơn). Giới hạn: biểu đồ tròn (index V), câu "chỉ tiêu gần giống" (d20), metric khớp chuỗi theo trang, một người soạn benchmark, nhãn do trợ lý AI soạn cần SV rà lại. TODO(SV): bổ sung nhận xét cá nhân.

## Thử thách nâng cao (nếu thực hiện)

- **Tài liệu, nguồn, quyền sử dụng, số trang và phiên bản:** như trên — bản PDF ngày 31/01/2024 (metadata InDesign), 100 trang, có văn bản, bảng (tr. 40, 72, 75, 78, 83–85, 88–96), biểu đồ cột/đường/tròn (tr. 28–37, 40–82), sơ đồ khối và infographic (tr. 10–26, 44, 57–58, 64).
- **Cách xử lý text, bảng, ảnh, biểu đồ; phạm vi index và phần chưa xử lý:** text + OCR biểu đồ vector từ Day 6 (index B, pypdf + PyMuPDF + Tesseract). Bổ sung index V: render mỗi trang 144 dpi, `gpt-4o-mini` chép từng khối trực quan thành JSON (loại, tiêu đề, vùng, đơn vị, giá trị) → mỗi khối 1 chunk có `page`, `region`, `page_image` để kiểm chứng. Toàn bộ 100 trang được gửi (0 lỗi); 34 trang không có khối V (bìa, mục lục, trang trống, và các trang sơ đồ dạng ô chữ tr. 10–12, 15, 17–18, 20, 22–25 — nội dung là text thật nên vẫn có trong index B). Ảnh minh họa trang trí bị bỏ qua có chủ đích. Đã kiểm tay index V với ảnh gốc: bảng/cột/infographic đúng; **biểu đồ tròn sai ghép nhãn** (chưa xử lý). 2 chunk dài hơn 512 token bị cắt khi embed (text đầy đủ vẫn lưu và đưa vào context).
- **Cách chia benchmark, schema evidence, model và cấu hình đã chốt trên dev:** schema mở rộng `data/README.md`: `group` (một nhóm chính), `gold[]` với `page`, `region`, `evidence`, `match`, `gold_mode: all` + `alternative_of` cho multi-hop, `calc` cho phép tính, `absence_reason` cho câu thiếu evidence. Test 30 câu: bảng 6, ảnh/sơ đồ 5, biểu đồ 5, multi-hop 4, text 4, thiếu bằng chứng 6. Dev 20 câu phủ đủ nhóm. Cấu hình chốt trên dev: **(chưa chốt)**.

| Nhóm test | Đạt / tổng | Tỷ lệ | Lỗi / nhận xét |
|---|---|---|---|
| Bảng | chưa chấm |  |  |
| Ảnh, sơ đồ | chưa chấm |  |  |
| Biểu đồ | chưa chấm |  |  |
| Multi-hop | chưa chấm |  |  |
| Text | chưa chấm |  |  |
| Thiếu bằng chứng | chưa chấm |  |  |
| **Toàn bộ** | chưa chấm |  |  |

- **Trace, nhãn và evidence từng câu; thời gian, chi phí, lỗi hệ thống:** `results/agent/test/(chưa chốt)/` (traces, reviews có lý do từng câu, summary_labels); evidence từng câu trong `benchmark/questions.json`. Câu lỗi hệ thống/timeout tính không đạt và báo riêng (cột lỗi).
- **Giới hạn, cách tái lập và đường dẫn benchmark:** tái lập theo `README_DAY7.md` (Docker DB Day 6 → `visual_index` → `eval_retrieval` → `agent` → `review` → `build_report`). LLM có tính ngẫu nhiên nhỏ dù temperature 0; vision chỉ chạy một lần (output lưu ở `results/visual/extraction.jsonl` để tái dựng index V mà không gọi lại API: `python -m src.rag.visual_index --skip-extract`). Benchmark: `benchmark/questions.json`.
