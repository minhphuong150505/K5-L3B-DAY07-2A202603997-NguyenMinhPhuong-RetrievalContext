# Hướng dẫn demo Day 7: Agentic RAG trên Sách trắng TMĐT 2023

Thời lượng gợi ý khoảng **7 phút** demo và 3 phút hỏi đáp.

Dùng 2 trang:

| Trang | Mở thế nào | Dùng để |
|---|---|---|
| `Demo/index.html` | mở file trực tiếp hoặc qua Live Server | slide tổng quan: số liệu, bảng so sánh, phân tích lỗi, kịch bản |
| `http://127.0.0.1:8765/` (`Demo/live.html`) | qua server demo | **demo chạy thật**: agent chạy live, pipeline sáng theo từng bước, citation bấm được |

> Mọi số liệu trong `index.html` được sinh tự động từ `results/` bằng `python -m src.rag.build_demo`, không gõ tay. Nếu ai hỏi số ở đâu ra, chỉ vào chân trang: chân trang liệt kê đúng các file nguồn.

---

## 1. Chuẩn bị (trước giờ demo 10–15 phút)

### 1.1 Checklist

- [ ] Laptop cắm sạc, tắt thông báo, phóng to trình duyệt khoảng 125% để cả lớp nhìn rõ.
- [ ] Có mạng: agent gọi OpenAI `gpt-4o-mini`. Nếu không có mạng, dùng chế độ phát lại (mục 4).
- [ ] Docker hệ thống đang chạy, DB Day 6 đã bật (mục 1.2).
- [ ] Server demo đã chạy với `--warm` và trang `http://127.0.0.1:8765/` hiện **"server: đang chạy"** (màu xanh).
- [ ] Đã chạy thử 1 câu để nạp model (lần đầu mất khoảng 20–30 giây).
- [ ] Mở sẵn 3 tab: `index.html`, `http://127.0.0.1:8765/`, và một terminal ở thư mục repo Day 7.
- [ ] Mở sẵn PDF gốc (`data/BCTMDT2023-file-31-1-pdf.pdf`) ở trang 40, để đối chiếu nếu được hỏi.

### 1.2 Lệnh khởi động

```bash
# (1) DB Day 6: PostgreSQL + pgvector
cd ~/Documents/Vin20K/Lab6/K5-L3B-DAY06-*/starter
docker --context default compose -p day6_student_starter up -d --wait

# (2) Server demo: nạp sẵn agent, model embedding, BM25 và reranker
cd ~/Documents/Vin20K/Lab7/K5-L3B-DAY07-*
PY=$(ls -d ~/Documents/Vin20K/Lab6/K5-L3B-DAY06-*/starter/.venv)/bin/python
$PY -m src.rag.demo_server --warm
#   → in ra: "Mở http://127.0.0.1:8765/". Giữ nguyên terminal này trong lúc demo.

# (3) (tuỳ chọn) Sinh lại trang tổng quan sau khi có kết quả mới
$PY -m src.rag.build_demo
```

Kiểm tra nhanh:

```bash
curl -s http://127.0.0.1:8765/api/questions | head -c 100   # phải ra JSON, không phải HTML
```

> **Lỗi `Unexpected token '<', "<!DOCTYPE"` hoặc "Mất kết nối tới server"** nghĩa là server demo (cổng 8765) chưa chạy. Chạy lại bước (2), rồi tải lại trang bằng Ctrl+Shift+R.

---

## 2. Câu hỏi dùng để demo

Chọn trong ô **"Chọn câu từ benchmark"** để không phải gõ.

| Vai trò | Câu | Vì sao chọn |
|---|---|---|
| Câu có bằng chứng (multi-hop) | **t17**: chênh lệch doanh thu B2C 2023 (tr. 40, 20,5 tỷ) so với doanh thu bán lẻ hàng hóa trực tuyến e-Conomy (tr. 37, 16 tỷ) | cần 2 trang và 2 biểu đồ, có phép tính; thấy rõ agent tìm 2 lần |
| Câu thiếu bằng chứng | **t25**: doanh thu TMĐT B2C Việt Nam năm **2024** | tài liệu chỉ có đến 2023: agent phải từ chối, không lấy số năm khác |
| Câu bảng | **t01**: giá trị mua sắm trực tuyến của một người năm 2023 (336 USD, tr. 40) | ngắn, nhanh, citation trỏ thẳng vào bảng |
| Lỗi thật (để phân tích) | **d11** (dev): tỷ lệ website bán hàng (đúng là 71,2%) | biểu đồ tròn bị đọc đảo cả ở index B lẫn V: lỗi thật, có giải thích |
| Câu tự gõ (nếu lớp muốn thử) | ví dụ: "Shopee được bao nhiêu phần trăm người tiêu dùng ưa chuộng?" | 81%, tr. 46: lớp tự kiểm được ngay |

> TODO(SV): sau khi chạy test xong, xem `index.html` mục 7 "Ví dụ thật từ trace". Nếu t17 hoặc t25 bị chấm KHÔNG ĐẠT ở cấu hình đã chốt, đổi sang một câu ĐẠT khác cùng nhóm cho phần demo "đúng", và giữ câu sai cho phần "lỗi". Tuyệt đối không sửa trace.

---

## 3. Kịch bản từng phút

### 0:00 – 0:45 · Vấn đề *(tab `index.html`, mục Tổng quan)*

> "Tài liệu là Sách trắng TMĐT Việt Nam 2023 của Bộ Công Thương, 100 trang, phần lớn số liệu nằm trong **biểu đồ và bảng**. RAG chỉ đọc text thường trả lời sai năm, sai đối tượng, hoặc bịa số khi tài liệu không có. Bài của em xây một agent tự tìm bằng chứng, trả lời có nguồn kiểm chứng được, và biết từ chối."

Chỉ vào các ô KPI: tỷ lệ đạt test, 50 câu benchmark, 173 + 119 chunk, 4 phương pháp retrieval, tổng chi phí.

### 0:45 – 1:45 · Kiến trúc *(mục 2)*

> "Em dùng lại nguyên vector store Day 6: PostgreSQL + pgvector, embedding SEA-LION-E5 1024 chiều chạy local. Index B là text của Day 6. Day 7 em thêm **index V**: cho vision model đọc từng trang và chép bảng/biểu đồ thành text có cấu trúc 'nhãn — năm: giá trị', rồi embed bằng **cùng model** vào **cùng bảng**.
> Có 4 cách tìm: dense, BM25 có bigram tiếng Việt, hybrid RRF, và rerank bằng cross-encoder. Agent là `gpt-4o-mini` có tool `search_documents`, `read_page`, `answer`, `abstain`, và tự quyết tìm mấy lần."

Nhấn mạnh: **agent chỉ nhận câu hỏi; đáp án chuẩn chỉ dùng lúc chấm.**

### 1:45 – 2:30 · Benchmark minh bạch *(mục 3)*

> "50 câu, chia dev/test **trước** khi thử nghiệm: test có 24 câu có đáp án (6 bảng, 5 ảnh/sơ đồ, 5 biểu đồ, 4 multi-hop, 4 text) và 6 câu thiếu bằng chứng. Mỗi câu ghi trang, vùng (hàng/cột bảng, cột biểu đồ), evidence nguyên văn. Em chọn cấu hình chỉ trên dev, ghi tiêu chí vào `results/selection.json`, rồi mới chạy test một lần."

### 2:30 – 3:45 · LIVE: câu có bằng chứng *(tab `http://127.0.0.1:8765/`)*

1. Chọn **t17** trong danh sách, cấu hình để mặc định (cấu hình đã chốt).
2. Bấm **▶ Chạy agent**.
3. Vừa chạy vừa nói, chỉ vào **sơ đồ pipeline** đang sáng lên:
   > "LLM quyết định gọi search; câu hỏi được embed và tìm trong pgvector, BM25 tìm theo từ khóa, RRF trộn hai danh sách, cross-encoder xếp lại. Agent thấy mới có số của trang 40 nên tìm lần nữa cho e-Conomy SEA…"
4. Ở **Dòng thời gian**: chỉ 2 lượt `search_documents`, nhãn **B** (text) và **V** (bảng/biểu đồ), trang, score.
5. Ở **Kết quả**: câu trả lời có phép tính 20,5 − 16 = 4,5 tỷ USD và 2 citation.

### 3:45 – 4:30 · Chứng minh nguồn trong DB

1. Bấm một **citation** (chip màu xanh). Khung **Chunk inspector** bên phải hiện:
   - đúng dòng trong bảng `chunks` của pgvector: `chunk_id`, index, trang, model embedding 1024 chiều, sha256;
   - câu SQL để tự kiểm;
   - **ảnh trang PDF gốc**: chỉ vào cột 2023 = 20,5 trên ảnh.
2. (Nếu còn thời gian) chạy trong terminal:

   ```bash
   $PY -m src.rag.verify --trace results/agent/test/<CẤU_HÌNH_ĐÃ_CHỐT>/traces.json --id t17 --find "20,5"
   ```

   > "Citation hợp lệ chưa đủ. Em đối chiếu nội dung chunk với trang gốc, và script này kiểm chuỗi trong DB và trong text layer của PDF."

### 4:30 – 5:15 · LIVE: câu thiếu bằng chứng + so sánh retriever

1. Chọn **t25** (doanh thu B2C **2024**) → **▶ Chạy agent**.
   > "Tài liệu chỉ có tới 2023. Baseline A0 trên dev từng trả lời 'năm 2017 = 8,06 tỷ', thực ra là số của năm 2018. Cấu hình mới bắt kiểm năm, đối tượng và trích dẫn nguyên văn nên agent từ chối."
2. Bấm **So sánh 4 retriever** để thấy 4 cột dense / BM25 / hybrid / rerank, cùng chunk cùng màu viền: các phương pháp xếp hạng khác nhau.

### 5:15 – 6:00 · Một lỗi thật *(tab `index.html`, mục 6–7)*

> "Đây là lỗi em chưa sửa được: biểu đồ tròn. Vision model đọc ngược nhãn ở 5/5 biểu đồ tròn em kiểm tay; câu d11 vì vậy trả lời 28,8% thay vì 71,2%. Em ghi lại trong `results/visual/manual_check.md`; hướng sửa là dùng model vision mạnh hơn hoặc đọc màu chú giải bằng toạ độ."

Chỉ bảng **Phân tích lỗi trên dev (trước/sau)**: 2+ lỗi, giả thuyết, kết quả sau khi sửa (kể cả lần sửa làm **xấu đi**, A2 từ chối nhầm nhiều, rồi A3 sửa lại).

### 6:00 – 6:40 · Số liệu và đánh đổi *(mục 4–5)*

- Retrieval: Hit@1 / Evidence Hit@3 / Context Evidence Rate theo từng phương pháp.
- Agent: A0 → A1 → A2 → A3 trên dev; test: baseline so với cấu hình đã chốt; tỷ lệ đạt theo nhóm.
- Đánh đổi: nhiều lượt gọi hơn, rerank chậm trên CPU; chi phí API tổng xem ở ô KPI.

### 6:40 – 7:00 · Kết luận

> "Tóm lại: dùng lại Day 6, thêm index trực quan, 4 phương pháp retrieval, agent có kiểm chứng trích dẫn. Mọi câu trả lời đều truy được về một dòng trong pgvector và một trang PDF. Giới hạn chính là biểu đồ tròn và nhãn chấm cần em rà lại."

---

## 4. Phương án dự phòng

| Sự cố | Cách xử lý |
|---|---|
| Mất mạng / OpenAI lỗi / chậm | Tab **"Phát lại trace đã lưu"** → chọn `test` + cấu hình đã chốt + câu → ▶ Phát lại. Đây là trace thật đã ghi, **không gọi API**. Hoặc mở thẳng `http://127.0.0.1:8765/?replay=test/<CẤU_HÌNH>/t17&gold=1` |
| Server demo chưa chạy | chạy lại mục 1.2 bước (2), rồi Ctrl+Shift+R |
| DB không lên | `docker --context default ps`; bật lại bằng lệnh mục 1.2 bước (1). Nếu vẫn lỗi: trình bày bằng `index.html` + phát lại không dùng được inspector; nói rõ là đang dùng trace đã lưu |
| Lần chạy đầu chậm (~30 s) | do nạp model; nói trước "lần đầu nạp model embedding và reranker" |
| Agent trả lời khác lần chạy trước | bình thường với LLM; nói thật và chấm ngay trên màn hình bằng ảnh trang gốc |

> Không bao giờ thay kết quả lỗi bằng kết quả giả. Nếu live sai, đó là ví dụ phân tích lỗi rất tốt.

---

## 5. Chuẩn bị hỏi đáp

| Câu hỏi có thể gặp | Gợi ý trả lời |
|---|---|
| Có đưa đáp án vào agent không? | Không. `agent.py` chỉ nhận câu hỏi; `gold.py`, `eval_retrieval.py` và `review.py` mới đọc đáp án, ở bước chấm. |
| Sao biết citation đúng? | Bấm citation → dòng DB + ảnh trang; `verify.py` kiểm chuỗi trong DB và PDF; nhãn chấm tay có lý do trong `reviews.json`. |
| Có chỉnh trên test không? | Không: chốt trên dev, ghi `results/selection.json` trước khi chạy test (xem lịch sử git). |
| Hybrid cộng điểm thế nào? | RRF theo **rank** (k = 60), không cộng score thô khác thang đo. |
| Sao score lúc 0,99 lúc 124? | Mỗi phương pháp một thang điểm: dense là cosine 0–1; BM25 không có giới hạn trên (khoảng 20–190); RRF ≤ 0,033; rerank là xác suất 0–1. Chỉ so thứ hạng trong cùng một phương pháp, vì vậy hybrid dùng RRF theo rank. |
| Tách từ tiếng Việt? | BM25 dùng âm tiết + bigram âm tiết để xấp xỉ từ ghép ("thương mại", "điện tử"). |
| Chi phí? | Index V khoảng $0,41 cho 100 trang (một lần); agent khoảng $0,0005 mỗi câu; embedding và rerank chạy local, chi phí 0. |
| Vì sao không đạt 100%? | Lỗi biểu đồ tròn, model nhỏ (`gpt-4o-mini`) đôi khi chọn sai năm hoặc từ chối nhầm, và rerank chạy trên CPU nên chậm. |

---

## 6. Sau buổi demo

- Thu hồi (revoke) các API key đã từng gửi qua ảnh chụp: OpenAI, Gemini, OpenRouter.
- Tắt server: Ctrl+C ở terminal chạy server; tắt DB: `docker --context default compose -p day6_student_starter stop`.
