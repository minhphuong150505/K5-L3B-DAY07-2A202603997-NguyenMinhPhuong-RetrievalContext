# Kiểm chứng thủ công index V (vision gpt-4o-mini) so với ảnh trang gốc

Người kiểm tra mở `work/pages_hd/pNNN.png` (hoặc PDF gốc) và so từng giá trị với chunk V tương ứng.
Đã kiểm 13 chunk trên 8 trang (chọn trang có biểu đồ/bảng/infographic đa dạng). TODO(SV): kiểm thêm và ký xác nhận.

| Chunk | Loại | Kết quả | Ghi chú |
|---|---|---|---|
| p26:V1 | infographic | Đúng 6/6 số | 76.255, 26.250, 105.103, 9.604, 48.348, 1.218 và % tăng khớp ảnh |
| p26:V2 | pie | **Sai ghép nhãn** | Tiêu đề sai ('Các loại hành vi khác' là chú giải, không phải tiêu đề); % gán lệch chú giải |
| p35:V1, V2 | combo (cột + đường) | Đúng | Indonesia 58/62/82, Philippines 15/16/24 khớp |
| p37:V1, V2 | combo | Đúng | Việt Nam 15/16/24, tăng trưởng 37%/11%/22% khớp |
| p40:V1 | combo | Đúng giá trị, sai nhỏ | Gắn nhầm '(*)' dự báo cho 2023 |
| p40:V2 | table | Đúng 24/24 ô | |
| p41:V1 | pie | **Sai** | Ảnh: 26–35 = 33%, 36–45 = 27%; model ghép ngược |
| p41:V2 | pie | **Sai** | Ghép % với nghề nghiệp lệch toàn bộ |
| p46:V1–V3 | bar | Đúng | 6 / 6 / 4 giá trị khớp |
| p64:V1 | infographic | Đúng giá trị | Thiếu ký hiệu % (67, 60, 1) |
| p64:V2 | pie | **Sai** | Ảnh: Dưới 10% = 52%, 10–20% = 33%, 20–40% = 12%, >40% = 3%; model đảo ngược |
| p64:V3 | bar | Đúng 8/8 | |
| p68:V1 | pie | **Sai (đảo)** | Ảnh: bán hàng 71,2%, CCDV 28,8%; model ghi ngược. Tiêu đề cũng sai (lấy tiêu đề mục 1 bên dưới) |

Kết luận: bảng, biểu đồ cột/đường và infographic đọc đúng; **biểu đồ tròn nhiều màu xanh gần nhau thường bị ghép sai nhãn** (5/5 biểu đồ tròn kiểm tra có lỗi ghép).
Ảnh hưởng: câu dev d11 (tr. 68) có chunk V mâu thuẫn với text layer (index B ghi đúng 71,2% cạnh nhãn); đây là một lỗi dev được phân tích trong báo cáo. Không câu test nào dựa vào biểu đồ tròn nhiều phần.
Các trang sơ đồ dạng ô chữ (tr. 10–12, 15, 17–18, 20, 22–25) model không tạo khối V; nội dung là text thật trong PDF nên vẫn có trong index B của Day 6.
