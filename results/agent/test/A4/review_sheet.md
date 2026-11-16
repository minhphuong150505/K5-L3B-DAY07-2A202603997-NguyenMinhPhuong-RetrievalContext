# Phiếu chấm A4 / test

Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.


## t01 · table · có đáp án
**Câu hỏi:** Ước tính giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023 là bao nhiêu USD?
**Đáp án chuẩn:** 336 USD.  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Ước tính giá trị mua sắm trực tuyến của một người (USD)', cột 2023
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 52.45s):** Ước tính giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023 là 336 USD. [sach-trang-tmdt-2023:p40:V2]
- search_documents: `giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023` → p40, p40, p50, p48, p48

> **[sach-trang-tmdt-2023:p40:V2]** [table] Doanh thu TMĐT B2C Việt Nam năm 2018 – 2023
(Trang 40, nửa dưới; đơn vị: không ghi)
Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người) | 2018: 39,9 | 2019: 44,8 | 2020: 49,3 | 2021: 54,6 | 2022: 57,0 | 2023: 61
Ước tính giá trị mua sắm trực tuyến của một người (USD) | 2018: 202 | 2019: 225 | 2020: 240 | 2021: 251 | 2022: 288 | 2023: 336
Tỷ trọng doanh thu TMĐT B2C so với tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng cả nước | 2018: 4,2% | 2019: 4,9% | 2020: 5,5% | 2021: 7% | 2022: 7,5% | 2023: 8%
Tỷ lệ người dân sử dụng Internet | 2018: 60% | 2019: 66% | 2020: 70% | 2021: 73% | 2022: 73,2% | 2023: 78,6%

## t02 · table · có đáp án
**Câu hỏi:** Số người tiêu dùng mua sắm trực tuyến ước tính của Việt Nam năm 2023 tăng thêm bao nhiêu triệu người so với năm 2018?
**Đáp án chuẩn:** Tăng khoảng 21,1 triệu người (từ 39,9 triệu năm 2018 lên 61 triệu năm 2023).  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người)', cột 2018 và 2023
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 109.51s):** Số người tiêu dùng mua sắm trực tuyến ước tính của Việt Nam năm 2023 là 61 triệu người, tăng 21,1 triệu người so với năm 2018 (39,9 triệu người). [sach-trang-tmdt-2023:p40:V2]
- search_documents: `số người tiêu dùng mua sắm trực tuyến Việt Nam 2023` → p40, p46, p40, p46, p30
- search_documents: `số người tiêu dùng mua sắm trực tuyến Việt Nam 2018` → p40, p40, p44, p49, p49

> **[sach-trang-tmdt-2023:p40:V2]** [table] Doanh thu TMĐT B2C Việt Nam năm 2018 – 2023
(Trang 40, nửa dưới; đơn vị: không ghi)
Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người) | 2018: 39,9 | 2019: 44,8 | 2020: 49,3 | 2021: 54,6 | 2022: 57,0 | 2023: 61
Ước tính giá trị mua sắm trực tuyến của một người (USD) | 2018: 202 | 2019: 225 | 2020: 240 | 2021: 251 | 2022: 288 | 2023: 336
Tỷ trọng doanh thu TMĐT B2C so với tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng cả nước | 2018: 4,2% | 2019: 4,9% | 2020: 5,5% | 2021: 7% | 2022: 7,5% | 2023: 8%
Tỷ lệ người dân sử dụng Internet | 2018: 60% | 2019: 66% | 2020: 70% | 2021: 73% | 2022: 73,2% | 2023: 78,6%

## t03 · table · có đáp án
**Câu hỏi:** Trong danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu, website dsvn.vn thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Tổng công ty Đường sắt Việt Nam.  
**Evidence:** tr.78 — Bảng 4.1, STT 7
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 72.63s):** Website dsvn.vn thuộc Tổng công ty Đường sắt Việt Nam. [sach-trang-tmdt-2023:p78:V1]
- search_documents: `dsvn.vn doanh nghiệp` → p78, p78, p54, p55, p69

> **[sach-trang-tmdt-2023:p78:V1]** [table] 4.1. Danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu
(Trang 78, giữa; đơn vị: không ghi)
STT | Website/ứng dụng: giá trị | Tên doanh nghiệp: giá trị
1 | abay.vn | Công ty TNHH Vé máy bay trực tuyến Abay
2 | AhaMove | Công Ty Cổ Phần Dịch Vụ Tức Thời
3 | amway.com.vn | Công ty TNHH Amway Việt Nam
4 | bachhoaxanh.com | Công ty Cổ phần Thương Mại Bách Hoá Xanh
5 | Con Cưng | Công ty Cổ Phần Con Cưng
6 | dienmayxanh.com | Công ty Cổ phần Thế Giới Di Động
7 | dsvn.vn | Tổng công ty Đường sắt Việt Nam
8 | esale.zing.vn | Công ty Cổ phần VNG
9 | hanoicomputer.vn | Công ty Cổ phần Đầu tư Công nghệ HACOM
10 | iNET.vn | Công ty TNHH Phần mềm INET
11 | Kara

## t04 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT gọi xe, ứng dụng HeyU thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần công nghệ HeyU Việt Nam.  
**Evidence:** tr.84 — Bảng 4.3 Nhóm doanh nghiệp dẫn đầu thị trường dịch vụ TMĐT gọi xe, STT 5
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 91.26s):** Ứng dụng HeyU thuộc Công ty Cổ phần công nghệ HeyU Việt Nam. [sach-trang-tmdt-2023:p084:B00]
- search_documents: `ứng dụng HeyU thuộc doanh nghiệp nào` → p84, p84, p83, p83, p84

> **[sach-trang-tmdt-2023:p084:B00]** 4.3. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT gọi xe 19
19 Taxi, xe ôm
STT Website/ứng dụng Tên doanh nghiệp
1 Be Công ty Cổ phần BE GROUP
2 GoJek Công ty Cổ phần Thương mại Công nghệ Go Viet
3 Grab Công ty TNHH Grab
4 GV Ship Công Ty Cổ Phần GV ASIA
5 HeyU Công ty Cổ phần công nghệ HeyU Việt Nam

## t05 · table · có đáp án
**Câu hỏi:** Theo bảng phụ lục khung pháp lý cơ bản về TMĐT, Luật An ninh mạng được ban hành ngày nào?
**Đáp án chuẩn:** Ngày 12/6/2018.  
**Evidence:** tr.88 — Bảng phụ lục, dòng 'Luật An ninh mạng'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 105.08s):** Luật An ninh mạng được ban hành vào ngày 12 tháng 6 năm 2018. [sach-trang-tmdt-2023:p88:V1]
- search_documents: `Luật An ninh mạng` → p22, p18, p18, p88, p88

> **[sach-trang-tmdt-2023:p88:V1]** [table] PHỤ LỤC: BẢNG CẬP NHẬT KHUNG PHÁP LÝ CƠ BẢN VỀ THƯƠNG MẠI ĐIỆN TỬ
(Trang 88, giữa; đơn vị: không ghi)
Thời gian ban hành | Luật: giá trị | Trạng thái hiệu lực: giá trị
24/11/2023 | Luật viễn thông (sửa đổi) | 1/7/2024
22/6/2023 | Luật Giao dịch điện tử (sửa đổi) | 01/7/2024
20/6/2023 | Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) | 01/7/2024
16/6/2022 | Luật sửa đổi, bổ sung một số điều của Luật Sở hữu trí tuệ | 01/03/2022
11/01/2022 | Luật sửa đổi, bổ sung một số điều của Luật Đầu tư công, Luật Đầu tư theo phương thức đối tác công tư, Luật Đầu thầu, Luật Điện lực, Luật Doanh nghiệp, Luật Thuế tiêu thụ đặc biệt và Luật Thi hành án dân sự | 01/03/2022
18/06/2020 | Luật Đầu tư | Hết

## t06 · table · có đáp án
**Câu hỏi:** Tỷ lệ website/ứng dụng TMĐT bán hàng và website/ứng dụng CCDV TMĐT có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng là bao nhiêu? Loại nào cao hơn?
**Đáp án chuẩn:** Bán hàng 69,8%, CCDV 71,9%; website/ứng dụng CCDV TMĐT cao hơn 2,1 điểm %.  
**Evidence:** tr.75 — Bảng 5.3 Các chính sách, cơ chế hỗ trợ khách hàng, hàng cuối 'Cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 147.42s):** Tỷ lệ website/ứng dụng TMĐT bán hàng có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng là 69,8%, trong khi tỷ lệ này ở website/ứng dụng CCDV TMĐT là 71,9%. Như vậy, tỷ lệ ở website/ứng dụng CCDV TMĐT cao hơn. [sach-trang-tmdt-2023:p075:B00]
- search_documents: `tỷ lệ website/ứng dụng TMĐT bán hàng có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng` → p75, p75, p68, p76, p70
- search_documents: `tỷ lệ website/ứng dụng CCDV TMĐT có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng` → p75, p75, p68, p70, p70

> **[sach-trang-tmdt-2023:p075:B00]** 5.3. Các chính sách, cơ chế hỗ trợ khách hàng
Website, ứng dụng | Website, ứng dụng
TMĐT bán hàng | CCDV TMĐT
Chính sách bảo hành, | 77,3% | 74,1%
bảo trì sản phẩm, dịch vụ
Chính sách đổi trả hàng | 77,1% | 77,5%
và hoàn tiền
Chính sách giải quyết | 81,0% | 85,9%
tranh chấp, khiếu nại
Chính sách bảo vệ | 91,5% | 93,4%
thông tin cá nhân
Cơ chế và quy trình rà soát | 79,0% | 86,5%
và kiểm duyệt thông tin
Cơ chế cho phép
khách hàng kiểm hàng | 69,8% | 71,9%
trước khi nhận hàng

## t07 · image · có đáp án
**Câu hỏi:** Theo sơ đồ quyền của chủ thể dữ liệu trong Nghị định 13/2023/NĐ-CP, có tổng cộng bao nhiêu quyền và quyền cuối cùng (số 11) là gì?
**Đáp án chuẩn:** 11 quyền; quyền số 11 là Quyền tự bảo vệ.  
**Evidence:** tr.21 — Sơ đồ khối '2 Quyền của chủ thể dữ liệu', ô số 11 (cột phải, ô cuối)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 174.89s):** Theo Nghị định 13/2023/NĐ-CP, có tổng cộng 11 quyền của chủ thể dữ liệu. Quyền cuối cùng (số 11) là "Quyền tự bảo vệ". [sach-trang-tmdt-2023:p21:V1]
- search_documents: `sơ đồ quyền của chủ thể dữ liệu Nghị định 13/2023/NĐ-CP` → p21, p21, p23, p20, p22

> **[sach-trang-tmdt-2023:p21:V1]** [diagram] 2 Quyền của chủ thể dữ liệu
(Trang 21, giữa; đơn vị: không ghi)
1. Quyền được biết
2. Quyền đồng ý
3. Quyền truy cập đồng ý
4. Quyền rút lại sự đồng ý
5. Quyền xóa dữ liệu
6. Quyền hạn chế xử lý dữ liệu
7. Quyền cung cấp dữ liệu
8. Quyền phản đối xử lý dữ liệu
9. Quyền khiếu nại, tố cáo, khởi kiện;
10. Quyền yêu cầu bồi thường thiệt hại
11. Quyền tự bảo vệ

## t08 · image · có đáp án
**Câu hỏi:** Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi) gồm những loại dịch vụ nào?
**Đáp án chuẩn:** 3 loại: dịch vụ cấp dấu thời gian; dịch vụ chứng thực thông điệp dữ liệu; dịch vụ chứng thực chữ ký số công cộng.  
**Evidence:** tr.14 — Sơ đồ khối '1 Phân loại dịch vụ tin cậy' (3 ô)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 111.63s):** Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi) gồm ba loại dịch vụ: 1. Dịch vụ cấp dấu thời gian; 2. Dịch vụ chứng thực thông điệp dữ liệu; 3. Dịch vụ chứng thực chữ ký số công cộng. [sach-trang-tmdt-2023:p014:B00] [sach-trang-tmdt-2023:p14:V1]
- search_documents: `Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi)` → p14, p14, p15, p16, p17

> **[sach-trang-tmdt-2023:p014:B00]** 1. Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi)
1
3
2
2. Luật Giao dịch điện tử (sửa đổi)
Ngày 22/6/2023, Quốc hội đã thông qua Luật Giao dịch điện tử (sửa đổi), có hiệu lực thi hành kể từ ngày 01/7/2024.
DỊCH VỤ TIN CẬY
1 Phân loại dịch vụ tin cậy
Dịch vụ cấp dấu thời gian;
Dịch vụ chứng thực thông điệp dữ liệu;
Dịch vụ chứng thực chữ ký số công cộng;

> **[sach-trang-tmdt-2023:p14:V1]** [diagram] 1. Phân loại dịch vụ tin cậy
(Trang 14, giữa; đơn vị: không ghi)
1. Dịch vụ cấp dấu thời gian;
2. Dịch vụ chứng thực thông điệp dữ liệu;
3. Dịch vụ chứng thực chữ ký số công cộng;

## t09 · image · có đáp án
**Câu hỏi:** Theo infographic tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023, bao nhiêu phần trăm doanh nghiệp sử dụng hợp đồng điện tử trong giao dịch?
**Đáp án chuẩn:** 41%.  
**Evidence:** tr.57 — Infographic mục 3, ô thứ 2 (hình E-CONTRACT)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 73.98s):** 41% doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch năm 2023. [sach-trang-tmdt-2023:p57:V2]
- search_documents: `tình hình sử dụng hợp đồng điện tử năm 2023` → p57, p57, p56, p68, p3

> **[sach-trang-tmdt-2023:p57:V2]** [infographic] 3. Tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023
(Trang 57, giữa; đơn vị: %)
80% | doanh nghiệp có sử dụng chữ ký điện tử
41% | doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch
22% | doanh nghiệp có sử dụng dịch vụ chứng thực hợp đồng điện tử

## t10 · image · có đáp án
**Câu hỏi:** Năm 2023, Cổng thông tin quản lý hoạt động TMĐT tiếp nhận bao nhiêu hồ sơ đăng ký và tăng bao nhiêu phần trăm so với năm 2022?
**Đáp án chuẩn:** 9.604 hồ sơ đăng ký, tăng 14,3% so với năm 2022.  
**Evidence:** tr.26 — Infographic khối thứ hai (biểu tượng thư mục), dòng 2
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 254.53s):** Năm 2023, Cổng thông tin quản lý hoạt động TMĐT tiếp nhận 9.604 hồ sơ đăng ký, tăng 14,3% so với năm 2022. [sach-trang-tmdt-2023:p26:V1]
- search_documents: `Cổng thông tin quản lý hoạt động TMĐT hồ sơ đăng ký 2023` → p26, p26, p68, p70, p24
- search_documents: `Cổng thông tin quản lý hoạt động TMĐT tăng trưởng 2022 2023` → p26, p26, p40, p55, p40

> **[sach-trang-tmdt-2023:p26:V1]** [infographic] Số lượng phản ánh, khiếu nại trên Cổng thông tin quản lý hoạt động TMĐT năm 2023
(Trang 26, nửa trên; đơn vị: tài khoản/hồ sơ/website)
76.255 tài khoản doanh nghiệp | tăng 16,4% so với năm 2022
26.250 tài khoản cá nhân | tăng 10,8% so với năm 2022
105.103 hồ sơ thông báo | tăng 12,1% so với năm 2022
9.604 hồ sơ đăng ký | tăng 14,3% so với năm 2022
48.348 website/ứng dụng đã được xác nhận thông báo | tăng 6,7% so với năm 2022
1.218 website/ứng dụng đã được xác nhận đăng ký | tăng 1,1% so với năm 2022

## t11 · image · có đáp án
**Câu hỏi:** Theo infographic phương thức vận chuyển hàng hóa của doanh nghiệp, bao nhiêu phần trăm doanh nghiệp tự vận chuyển và bao nhiêu phần trăm sử dụng dịch vụ của bên thứ ba?
**Đáp án chuẩn:** 67% doanh nghiệp tự vận chuyển; 60% sử dụng dịch vụ của bên thứ ba.  
**Evidence:** tr.64 — Infographic 1. Phương thức vận chuyển hàng hóa (3 thanh)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 55.18s):** 67% doanh nghiệp tự vận chuyển hàng hóa và 60% doanh nghiệp sử dụng dịch vụ của bên thứ ba. [sach-trang-tmdt-2023:p064:B00] [sach-trang-tmdt-2023:p64:V1]
- search_documents: `phương thức vận chuyển hàng hóa của doanh nghiệp` → p64, p64, p64, p64, p74

> **[sach-trang-tmdt-2023:p064:B00]** V. CÁC DỊCH VỤ HỖ TRỢ THƯƠNG MẠI ĐIỆN TỬ
1. Phương thức vận chuyển hàng hóa mà doanh nghiệp đang sử dụng
67% | doanh nghiệp tự vận chuyển
60% | doanh nghiệp sử dụng dịch vụ của bên thứ ba
1% | sử dụng phương thức khác

> **[sach-trang-tmdt-2023:p64:V1]** [bar_chart] 1. Phương thức vận chuyển hàng hóa mà doanh nghiệp đang sử dụng
(Trang 64, nửa trên; đơn vị: %)
doanh nghiệp tự vận chuyển — 2023: 67 | doanh nghiệp sử dụng dịch vụ của bên thứ ba — 2023: 60 | sử dụng phương thức khác — 2023: 1

## t12 · chart · có đáp án
**Câu hỏi:** Năm 2022, khu vực nào có tỷ lệ tăng trưởng doanh thu bán lẻ TMĐT cao nhất thế giới và tỷ lệ đó là bao nhiêu?
**Đáp án chuẩn:** Đông Nam Á, 20,6%.  
**Evidence:** tr.31 — Biểu đồ thanh ngang 2.2, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 133.65s):** Năm 2022, khu vực có tỷ lệ tăng trưởng doanh thu bán lẻ thương mại điện tử cao nhất thế giới là Đông Nam Á với tỷ lệ 20,6%. [sach-trang-tmdt-2023:p31:V1]
- search_documents: `tăng trưởng doanh thu bán lẻ TMĐT 2022` → p31, p31, p40, p40, p32

> **[sach-trang-tmdt-2023:p31:V1]** [bar_chart] 2.2. Tỷ lệ tăng trưởng doanh thu bán lẻ TMĐT toàn cầu, chia theo khu vực năm 2022
(Trang 31, nửa trên; đơn vị: %)
Đông Nam Á — 2022: 20,6% | Châu Mỹ Latin — 2022: 20,4% | Trung Đông và Châu Phi — 2022: 17,0% | Trung & Đông Âu — 2022: 16,1% | Bắc Mỹ — 2022: 15,5% | Châu Á - Thái Bình Dương — 2022: 11,8% | Tây Âu — 2022: 6,1% | Toàn cầu — 2022: 12,2% (dự báo *)

## t13 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay năm 2023 là bao nhiêu và giảm bao nhiêu điểm phần trăm so với năm 2022?
**Đáp án chuẩn:** 50% năm 2023, giảm 13 điểm % so với 63% năm 2022.  
**Evidence:** tr.42 — Biểu đồ cột 1. Phương tiện truy cập Internet, nhóm 'Máy tính để bàn, Máy tính xách tay'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 53.98s):** Tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay năm 2023 là 50%. So với năm 2022, tỷ lệ này giảm 13 điểm phần trăm (63% - 50%). [sach-trang-tmdt-2023:p42:V1]
- search_documents: `tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay 2023 2022` → p42, p42, p42, p45, p42

> **[sach-trang-tmdt-2023:p42:V1]** [bar_chart] 1. Phương tiện truy cập Internet của người dân
(Trang 42, nửa trên; đơn vị: Tỷ lệ (%))
Máy tính để bàn — 2022: 63%; 2023: 50%
Điện thoại di động — 2022: 94%; 2023: 90%
Thiết bị khác (Ipad, Máy tính bảng) — 2022: 14%; 2023: 10%

## t14 · chart · có đáp án
**Câu hỏi:** Sàn giao dịch TMĐT bán buôn bán lẻ nào được người tiêu dùng ưa chuộng thứ ba và với tỷ lệ bao nhiêu?
**Đáp án chuẩn:** TikTok, 34% (sau Shopee 81% và Lazada 42%).  
**Evidence:** tr.46 — Biểu đồ cột 6.1, cột thứ ba
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 55.88s):** Sàn giao dịch TMĐT bán buôn bán lẻ được người tiêu dùng ưa chuộng thứ ba là TikTok với tỷ lệ 34%. [sach-trang-tmdt-2023:p46:V2] [sach-trang-tmdt-2023:p046:B02]
- search_documents: `sàn giao dịch TMĐT bán buôn bán lẻ ưa chuộng thứ ba tỷ lệ` → p46, p46, p46, p46, p47

> **[sach-trang-tmdt-2023:p46:V2]** [bar_chart] 6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng
(Trang 46, giữa; đơn vị: (%))
Shopee — năm: 2023: 81%
Lazada — năm: 2023: 42%
TikTok — năm: 2023: 34%
Tiki — năm: 2023: 20%
Sendo — năm: 2023: 8%
Khác — năm: 2023: 2%

> **[sach-trang-tmdt-2023:p046:B02]** 6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Website TMĐT bán hàng: 34%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Sàn giao dịch TMĐT: 61%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Diễn đàn mạng xã hội: 55%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Các ứng dụng mua hàng trên thiết bị di động: 21%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Hình thức khác: 4%
6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng — S

## t15 · chart · có đáp án
**Câu hỏi:** Bao nhiêu phần trăm doanh nghiệp sở hữu website/ứng dụng di động có chi phí quảng cáo trung bình dưới 10 triệu đồng?
**Đáp án chuẩn:** 63%.  
**Evidence:** tr.61 — Biểu đồ cột 1.2 Ước tính chi phí quảng cáo trung bình, cột 'Dưới 10 triệu đồng'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 78.85s):** 63% doanh nghiệp sở hữu website/ứng dụng di động có chi phí quảng cáo trung bình dưới 10 triệu đồng. [sach-trang-tmdt-2023:p061:B01] [sach-trang-tmdt-2023:p61:V1]
- search_documents: `doanh nghiệp sở hữu website/ứng dụng di động chi phí quảng cáo trung bình dưới 10 triệu đồng` → p61, p61, p61, p85, p60

> **[sach-trang-tmdt-2023:p061:B01]** 2. Tình hình vận hành website, ứng dụng di động TMĐT
2.1. Đánh giá của doanh nghiệp về mức độ hiệu quả của các hình thức bán hàng
Qua ứng dụng di động | 25% | 52% | 23%
Qua website của doanh nghiệp | 23% | 53% | 24%
Qua sàn giao dịch TMĐT | 26% | 51% | 24%
Qua mạng xã hội | 16% | 50% | 34%
(Tỷ lệ doanh nghiệp sở hữu website/ứng dụng di động)
Thấp | Trung bình | Cao
[Tiêu đề trục dọc] (Tỷ lệ doanh nghiệp sở hữu; website/ứng dụng di động)
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1.2. . Ước tính chi phí quảng cáo trung bình của doanh nghiệp — Dưới 10 triệu đồng: 63%
1.2. . Ước tính chi phí quảng cáo trung bình của doanh nghiệp — Từ 10 - 20 triệu đồng: 25%
1.2. . Ước tính ch

> **[sach-trang-tmdt-2023:p61:V1]** [bar_chart] 1.2. . Ước tính chi phí quảng cáo trung bình của doanh nghiệp
(Trang 61, nửa trên; đơn vị: phần trăm)
Dưới 10 triệu đồng: 63%
Từ 10 - 20 triệu đồng: 25%
Từ 20- 50 triệu đồng: 7%
Trên 50 - 100 triệu đồng: 2%
Trên 100 triệu đồng: 3%

## t16 · chart · có đáp án
**Câu hỏi:** Theo biểu đồ quy mô nền kinh tế Internet phân theo quốc gia, quy mô kinh tế Internet của Việt Nam năm 2023 và số liệu dự báo năm 2025 là bao nhiêu?
**Đáp án chuẩn:** 30 tỷ USD năm 2023; dự báo 43 tỷ USD năm 2025.  
**Evidence:** tr.34 — Biểu đồ thanh ngang 2. Quy mô nền kinh tế Internet phân theo quốc gia năm 2023, cặp thanh 'Việt Nam'
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 92.55s):** Quy mô kinh tế Internet của Việt Nam năm 2023 là 30 tỷ USD và dự báo năm 2025 là 43 tỷ USD. [sach-trang-tmdt-2023:p034:B01]
- search_documents: `quy mô nền kinh tế Internet Việt Nam 2023` → p34, p34, p34, p34, p3
- search_documents: `dự báo quy mô nền kinh tế Internet Việt Nam 2025` → p34, p34, p34, p34, p37
- read_page: `page 34` → p34, p34, p34, p34
- read_page: `page 37` → p37, p37, p37, p37, p37, p37, p37

> **[sach-trang-tmdt-2023:p034:B01]** 2. Quy mô nền kinh tế Internet phân theo quốc gia năm 2023
Indonesia | 82
109
Thái Lan | 36 | 49
Việt Nam | 30 | 43
Philippines | 24 | 35
Malaysia | 23 | 30
Singapore | 22 | 29
2023 | 2025* | * Số liệu dự báo
7 | Đơn vị tính: Tỷ USD
Số liệu được tổng hợp từ Báo cáo e-Conomy SEA 2023 – Google, Temasek, Bain & Company

## t17 · multihop · có đáp án
**Câu hỏi:** Doanh thu TMĐT B2C Việt Nam năm 2023 theo biểu đồ chương III chênh lệch bao nhiêu so với doanh thu bán lẻ hàng hóa trực tuyến của Việt Nam năm 2023 theo số liệu e-Conomy SEA ở chương II?
**Đáp án chuẩn:** 20,5 tỷ USD so với 16 tỷ USD, chênh lệch 4,5 tỷ USD.  
**Evidence:** tr.40 — Biểu đồ cột Doanh thu TMĐT B2C Việt Nam 2018–2023, cột 2023; tr.37 — Biểu đồ 8. Việt Nam, cột 'Doanh thu bán lẻ hàng hóa trực tuyến' 2023
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 139.85s):** Doanh thu TMĐT B2C Việt Nam năm 2023 là 20,5 tỷ USD, trong khi doanh thu bán lẻ hàng hóa trực tuyến là 16 tỷ USD. Chênh lệch giữa hai doanh thu này là 4,5 tỷ USD. [sach-trang-tmdt-2023:p040:B00]
- search_documents: `Doanh thu TMĐT B2C Việt Nam năm 2023 chương III` → p40, p40, p40, p30, p46
- search_documents: `doanh thu bán lẻ hàng hóa trực tuyến Việt Nam năm 2023 e-Conomy SEA chương II` → p37, p40, p34, p37, p40
- read_page: `page 40` → p40, p40, p40
- read_page: `page 37` → p37, p37, p37, p37, p37, p37, p37

> **[sach-trang-tmdt-2023:p040:B00]** I. QUY MÔ THỊ TRƯỜNG THƯƠNG MẠI ĐIỆN TỬ BÁN LẺ TẠI VIỆT NAM
8 Doanh thu TMĐT B2C Việt Nam bao gồm doanh thu tất cả hàng hóa, dịch vụ bán qua kênh TMĐT (loại trừ các giao dịch liên quan đến lĩnh vực tài chính, ngân hàng, tín
dụng, bảo hiểm, trò chơi trực tuyến).
9 Số liệu cập nhật đến 6 tháng đầu năm 2023. Nguồn: Bộ Thông tin và Truyền thông
Doanh thu TMĐT B2C Việt Nam năm 2018 – 2023 (tỷ USD)8
2018 2019 2020 2021 2022 2023
Ước tính số lượng người tiêu dùng
mua sắm trực tuyến (triệu người) 39,9 44,8 49,3 54,6 57,0 61
Ước tính giá trị mua sắm trực tuyến
của một người (USD) 202 225 240 251 288 336
Tỷ trọng doanh thu TMĐT B2C so với
tổng mức bán lẻ hàng hóa và doanh
thu dịch vụ tiêu dùng cả nước

## t18 · multihop · có đáp án
**Câu hỏi:** Quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022 là quốc gia nào, và doanh thu TMĐT B2C năm 2022 của quốc gia đó là bao nhiêu?
**Đáp án chuẩn:** Trung Quốc (50,2% thị phần); doanh thu TMĐT B2C năm 2022 là 2.682 tỷ USD.  
**Evidence:** tr.32 — Biểu đồ 2.4 Top 12 quốc gia chiếm thị phần TMĐT lớn nhất, thanh đầu tiên; tr.33 — Biểu đồ 2.6 Trung Quốc, cột 2022
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 60.35s):** Quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022 là Trung Quốc với thị phần 50,2%. Doanh thu TMĐT B2C của Trung Quốc năm 2022 là 3.982 tỷ USD. [sach-trang-tmdt-2023:p32:V1]
- search_documents: `thị phần TMĐT toàn cầu 2022` → p32, p32, p31, p31, p30
- search_documents: `doanh thu TMĐT B2C Trung Quốc 2022` → p32, p33, p32, p30, p31

> **[sach-trang-tmdt-2023:p32:V1]** [bar_chart] 2.4. Top 12 quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022
(Trang 32, nửa trên; đơn vị: %)
Trung Quốc — 2022: 50,2% | Mỹ — 2022: 19,2% | Vương quốc Anh — 2022: 4,4% | Nhật Bản — 2022: 3,0% | Hàn Quốc — 2022: 2,6% | Đức — 2022: 2,1% | Pháp — 2022: 1,7% | Ấn Độ — 2022: 1,5% | Canada — 2022: 1,4% | Nga — 2022: 1,0% | Brazail — 2022: 1,0% | Indonesia — 2022: 1,0% (Tỷ lệ trong tổng doanh thu TMĐT toàn cầu)

## t19 · multihop · có đáp án
**Câu hỏi:** Sàn TMĐT lĩnh vực dịch vụ vận tải nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành ứng dụng này theo danh sách doanh nghiệp dẫn đầu thị trường gọi xe?
**Đáp án chuẩn:** Grab, 70%; do Công ty TNHH Grab vận hành.  
**Evidence:** tr.46 — Biểu đồ cột 6.2 Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải, cột Grab; tr.84 — Bảng 4.3 doanh nghiệp dẫn đầu dịch vụ gọi xe, STT 3; tr.83 — Bảng 4.1, STT 4 (evidence thay thế cho tên doanh nghiệp)
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 54.95s):** Sàn TMĐT lĩnh vực dịch vụ vận tải được người tiêu dùng ưa chuộng nhất là Grab với tỷ lệ 70%. Các doanh nghiệp dẫn đầu thị trường gọi xe bao gồm: 1. Grab (Công ty TNHH Grab), 2. Be (Công ty Cổ phần BE GROUP), 3. GoJek (Công ty Cổ phần Thương mại Công nghệ Go Viet). [sach-trang-tmdt-2023:p46:V3] [sach-trang-tmdt-2023:p84:V1]
- search_documents: `sàn TMĐT lĩnh vực dịch vụ vận tải ưa chuộng nhất tỷ lệ` → p46, p46, p46, p46, p47
- search_documents: `doanh nghiệp dẫn đầu thị trường gọi xe` → p84, p84, p83, p83, p84

> **[sach-trang-tmdt-2023:p46:V3]** [bar_chart] 6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
(Trang 46, nửa dưới; đơn vị: (%))
Grab — năm: 2023: 70%
Be — năm: 2023: 23%
GoJek — năm: 2023: 15%
Khác — năm: 2023: 14%

> **[sach-trang-tmdt-2023:p84:V1]** [table] 4.3. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT gọi xe
(Trang 84, nửa trên; đơn vị: không ghi)
1 | Be | Công ty Cổ phần BE GROUP
2 | GoJek | Công ty Cổ phần Thương mại Công nghệ Go Viet
3 | Grab | Công ty TNHH Grab
4 | GV Ship | Công Ty Cổ Phần GV ASIA
5 | HeyU | Công ty Cổ phần công nghệ HeyU Việt Nam

## t20 · multihop · có đáp án
**Câu hỏi:** TP. Hồ Chí Minh chiếm tỷ lệ đơn hàng thành công bao nhiêu trên website/ứng dụng TMĐT bán hàng và bao nhiêu trên website/ứng dụng cung cấp dịch vụ TMĐT? Chênh lệch bao nhiêu điểm phần trăm?
**Đáp án chuẩn:** 34,6% (TMĐT bán hàng) và 24,1% (CCDV TMĐT); chênh lệch 10,5 điểm %.  
**Evidence:** tr.77 — Biểu đồ 3. Tỷ lệ số lượng đơn hàng thành công của website, ứng dụng TMĐT bán hàng theo tỉnh/thành, mục TP. Hồ Chí Minh; tr.82 — Biểu đồ 3.2 Tỷ lệ số lượng đơn hàng thành công theo địa phương (website CCDV TMĐT), mục TP. Hồ Chí Minh
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 46.42s):** TP. Hồ Chí Minh chiếm tỷ lệ đơn hàng thành công là 34,6% trên website/ứng dụng TMĐT bán hàng và 24,1% trên website/ứng dụng cung cấp dịch vụ TMĐT. Chênh lệch giữa hai tỷ lệ này là 10,5 điểm phần trăm. [sach-trang-tmdt-2023:p77:V1]
- search_documents: `TP. Hồ Chí Minh tỷ lệ đơn hàng thành công website/ứng dụng TMĐT bán hàng` → p77, p77, p81, p82, p82
- search_documents: `TP. Hồ Chí Minh tỷ lệ đơn hàng thành công website/ứng dụng cung cấp dịch vụ TMĐT` → p77, p77, p81, p82, p82

> **[sach-trang-tmdt-2023:p77:V1]** [bar_chart] 3. Tỷ lệ số lượng đơn hàng thành công của website, ứng dụng TMĐT bán hàng tại một số tỉnh/thành phố
(Trang 77, giữa; đơn vị: %)
TP. Hồ Chí Minh — 2023: 34,6%
Hà Nội — 2023: 21,8%
Bình Dương — 2023: 3,7%
Đồng Nai — 2023: 3,2%
Đà Nẵng — 2023: 3,0%
Cần Thơ — 2023: 2,6%
Hải Phòng — 2023: 2,5%
Bà Rịa – Vũng Tàu — 2023: 2,1%
Long An — 2023: 1,7%
Hải Dương — 2023: 1,7%
Bắc Ninh — 2023: 1,6%
Quảng Ninh — 2023: 1,6%
Lâm Đồng — 2023: 1,6%
Nghệ An — 2023: 1,5%
Khánh Hòa — 2023: 1,5%
Vĩnh Phúc — 2023: 1,4%
Hưng Yên — 2023: 1,4%
Thanh Hóa — 2023: 1,4%
Nam Định — 2023: 1,3%
Thái Nguyên — 2023: 1,2%
Các tỉnh/thành phố còn lại — 2023: 8,8%

## t21 · text · có đáp án
**Câu hỏi:** Theo Chỉ thị 18/CT-TTg, giải pháp nào được nêu liên quan đến mã số thuế của cá nhân?
**Đáp án chuẩn:** Thực hiện chuyển đổi sử dụng mã định danh cá nhân làm mã số thuế; tích hợp tài khoản định danh điện tử để kê khai, đăng ký nộp thuế trên ứng dụng VNeID và các nền tảng khác.  
**Evidence:** tr.25 — Mục '2. Một số giải pháp' của Chỉ thị 18/CT-TTg, gạch đầu dòng 4
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 47.72s):** Giải pháp liên quan đến mã số thuế của cá nhân theo Chỉ thị 18/CT-TTg là thực hiện chuyển đổi sử dụng mã định danh cá nhân làm mã số thuế, tích hợp sử dụng tài khoản định danh điện tử để kê khai, đăng ký nộp thuế trên ứng dụng định danh điện tử quốc gia (VneID) và các nền tảng khác do Cơ quan thuế hướng dẫn. [sach-trang-tmdt-2023:p025:B00]
- search_documents: `Chỉ thị 18/CT-TTg mã số thuế cá nhân` → p24, p25, p20, p19, p19

> **[sach-trang-tmdt-2023:p025:B00]** 1. Mục tiêu
Sửa đổi chính sách, pháp luật liên quan đến TMĐT;
Xây dựng cơ sở dữ liệu quản lý thuế đổi với TMĐT, kinh doanh trên nền
tảng số;
Kết nối, chia sẻ dữ liệu giữa các cơ quan liên quan để tăng cường công tác
quản lý thuế đối với hoạt động kinh doanh TMĐT, hoạt động cung cấp sản
phẩm, dịch vụ số xuyên biên giới;
Thực hiện chuyển đổi sử dụng mã định danh cá nhân làm mã số thuế; tích
hợp sử dụng tài khoản định danh điện tử để kê khai, đăng ký nộp thuế trên
ứng dụng định danh điện tử quốc gia (VneID) và các nền tảng khác do Cơ
quan thuế hướng dẫn;
Ứng dụng thẻ Căn cước công dân gắn chịp hoặc dữ liệu dân cư để xác thực
chủ thể của hoạt động TMĐT tham gia giao kết hợp đồng trên Trục phát
t

## t22 · text · có đáp án
**Câu hỏi:** Theo Nghị định 13/2023/NĐ-CP, dữ liệu về vị trí của cá nhân được xác định qua dịch vụ định vị thuộc loại dữ liệu cá nhân nào?
**Đáp án chuẩn:** Dữ liệu cá nhân nhạy cảm.  
**Evidence:** tr.20 — Khối '1 Phân loại dữ liệu cá nhân', cột 'Dữ liệu cá nhân nhạy cảm'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 37.22s):** Dữ liệu về vị trí của cá nhân được xác định qua dịch vụ định vị thuộc loại dữ liệu cá nhân nhạy cảm. [sach-trang-tmdt-2023:p020:B01]
- search_documents: `Nghị định 13/2023/NĐ-CP dữ liệu vị trí cá nhân dịch vụ định vị` → p20, p20, p23, p23, p22

> **[sach-trang-tmdt-2023:p020:B01]** 4. Nghị định số 13/2023/NĐ-CP ngày 17 tháng 4 năm 2023 của Chính phủ
Thông tin về đặc điểm di truyền được thừa hưởng
hoặc có được của cá nhân;
Thông tin về thuộc tính vật lý, đặc điểm sinh học
riêng của cá nhân;
Thông tin về đời sống tình dục, xu hướng tình dục
của cá nhân;
Dữ liệu về tội phạm, hành vi phạm tội được thu
thập, lưu trữ bởi các cơ quan thực thi pháp luật;
Dữ liệu về vị trí của cá nhân được xác định qua
dịch vụ định vị;
Dữ liệu cá nhân khác được pháp luật quy định là
đặc thù và cần có biện pháp bảo mật cần thiết;
Thông tin khách hàng của tổ chức tín dụng, chi
nhánh ngân hàng nước ngoài, tổ chức cung ứng
dịch vụ trung gian thanh toán, các tổ chức được
phép khác, gồm: thông tin đị

## t23 · text · có đáp án
**Câu hỏi:** Sách trắng TMĐT 2023 được xây dựng nhằm đánh giá sơ bộ kết quả thực hiện mục tiêu đặt ra tại quyết định nào của Thủ tướng Chính phủ?
**Đáp án chuẩn:** Quyết định số 645/QĐ-TTg ngày 15/5/2020 phê duyệt Kế hoạch tổng thể phát triển TMĐT quốc gia giai đoạn 2021–2025.  
**Evidence:** tr.3 — Lời giới thiệu, đoạn 3
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 35.48s):** Sách trắng Thương mại điện tử Việt Nam năm 2023 được xây dựng nhằm đánh giá sơ bộ kết quả thực hiện mục tiêu phát triển thương mại điện tử được đặt ra tại Quyết định số 645/QĐ-TTg ngày 15 tháng 5 năm 2020 của Thủ tướng Chính phủ. [sach-trang-tmdt-2023:p003:B01]
- search_documents: `đánh giá sơ bộ kết quả thực hiện mục tiêu quyết định Thủ tướng Chính phủ` → p3, p25, p24, p3, p13

> **[sach-trang-tmdt-2023:p003:B01]** Nhằm tổng kết tình hình, đồng thời, đánh giá sơ bộ kết quả thực hiện một số mục tiêu phát triển thương
mại điện tử được đặt ra tại Quyết định số 645/QĐ-TTg ngày 15 tháng 5 năm 2020 của Thủ tướng Chính phủ phê
duyệt Kế hoạch tổng thể phát triển thương mại điện tử quốc gia giai đoạn 2021 – 2025, Cục Thương mại điện
tử và Kinh tế số - Bộ Công Thương tiếp tục xây dựng và công bố Sách trắng Thương mại điện tử Việt Nam năm
2023 với số liệu được tổng hợp kết quả điều tra của khoảng 20.000 cá nhân người tiêu dùng, gần 7.500 doanh
nghiệp và các dữ liệu tin cậy khác. Sách trắng được kỳ vọng sẽ tiếp tục là một tài liệu quan trọng cho các nhà
kinh doanh, chuyên gia kinh tế và những ai quan tâm đến lĩnh 

## t24 · text · có đáp án
**Câu hỏi:** Theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi), tổ chức thiết lập, vận hành nền tảng số lớn phải đánh giá định kỳ những nội dung nào?
**Đáp án chuẩn:** (1) Hoạt động kiểm duyệt nội dung việc sử dụng hệ thống thuật toán và quảng cáo hướng tới NTD, nhóm NTD cụ thể; (2) việc thực hiện quy định xử lý tài khoản giả, việc sử dụng trí tuệ nhân tạo, các giải pháp tự động toàn bộ hoặc tự động một phần.  
**Evidence:** tr.13 — Khối '4 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số lớn', ô 3 và 4
**auto:** context đủ evidence = True
**Agent (abstain, 1 tool call, 42.32s):** Không đủ bằng chứng để trả lời.
- search_documents: `Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) tổ chức thiết lập vận hành nền tảng số lớn đánh giá định kỳ` → p13, p11, p13, p12, p10
- abstain: Không có thông tin đầy đủ và chính xác về nội dung đánh giá định kỳ theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) trong tài liệu.

## t25 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Doanh thu TMĐT B2C của Việt Nam năm 2024 đạt bao nhiêu tỷ USD?
**Lý do thiếu:** Biểu đồ B2C Việt Nam (tr. 40) dừng ở 2023; số liệu dự báo 2024* chỉ có cho toàn cầu (tr. 30), Trung Quốc và Mỹ (tr. 33); e-Conomy SEA chỉ dự báo năm 2025 (tr. 34–37).
**Agent (abstain, 1 tool call, 22.14s):** Không đủ bằng chứng để trả lời.
- search_documents: `doanh thu TMĐT B2C Việt Nam 2024` → p40, p40, p40, p30, p33
- abstain: Tài liệu không chứa thông tin về doanh thu TMĐT B2C của Việt Nam năm 2024.

## t26 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.3 (tr. 29) chỉ có Philippines, Thái Lan, Malaysia, Indonesia, Singapore, Việt Nam, Ấn Độ, Úc, Trung Quốc, Hàn Quốc và trung bình toàn cầu; 'Nhật Bản' chỉ xuất hiện ở tr. 32 (thị phần) và tr. 63 (xuất khẩu).
**Agent (abstain, 1 tool call, 20.6s):** Không đủ bằng chứng để trả lời.
- search_documents: `thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản` → p42, p28, p42, p42, p29
- abstain: Không có thông tin về thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản trong tài liệu.

## t27 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Shopee chiếm bao nhiêu phần trăm thị phần giá trị giao dịch (GMV) TMĐT tại Việt Nam năm 2023?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ người dùng ưa chuộng Shopee (81%, tr. 46) và danh sách doanh nghiệp dẫn đầu (tr. 83), không có thị phần GMV; 'GMV' không xuất hiện trong toàn văn.
**Agent (answered, 1 tool call, 38.86s):** Shopee chiếm 81% thị phần giá trị giao dịch (GMV) thương mại điện tử tại Việt Nam năm 2023. [sach-trang-tmdt-2023:p46:V2]
- search_documents: `Shopee thị phần giá trị giao dịch TMĐT Việt Nam 2023` → p46, p46, p40, p76, p50

> **[sach-trang-tmdt-2023:p46:V2]** [bar_chart] 6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng
(Trang 46, giữa; đơn vị: (%))
Shopee — năm: 2023: 81%
Lazada — năm: 2023: 42%
TikTok — năm: 2023: 34%
Tiki — năm: 2023: 20%
Sendo — năm: 2023: 8%
Khác — năm: 2023: 2%

## t28 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP là bao nhiêu?
**Lý do thiếu:** Phần Nghị định 13/2023 (tr. 20–24) không nêu mức phạt; từ 'phạt' chỉ xuất hiện trong tên các nghị định xử phạt ở phụ lục (tr. 90–92), không liên quan bảo vệ dữ liệu cá nhân.
**Agent (abstain, 4 tool call, 164.03s):** Không đủ bằng chứng để trả lời.
- search_documents: `mức phạt tiền tối đa hành vi vi phạm quy định bảo vệ dữ liệu cá nhân Nghị định 13/2023/NĐ-CP` → p20, p22, p23, p23, p20
- search_documents: `mức phạt tiền Nghị định 13/2023/NĐ-CP` → p22, p89, p89, p20, p20
- search_documents: `Nghị định 13/2023/NĐ-CP mức phạt tiền` → p89, p89, p22, p20, p20
- read_page: `page 89` → p89, p89, p89
- abstain: Không tìm thấy thông tin về mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP.

## t29 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Bao nhiêu phần trăm doanh nghiệp tham gia xuất khẩu qua TMĐT xuất khẩu sang thị trường Úc?
**Lý do thiếu:** Biểu đồ 2.3.2 (tr. 63) chỉ có Hàn Quốc, Nhật Bản, Trung Quốc, Liên minh châu Âu, Hoa Kỳ và 'Quốc gia khác'; 'Úc' chỉ xuất hiện ở tr. 29–30 (sử dụng Internet).
**Agent (abstain, 1 tool call, 34.68s):** Không đủ bằng chứng để trả lời.
- search_documents: `doanh nghiệp tham gia xuất khẩu qua TMĐT xuất khẩu sang thị trường Úc` → p63, p63, p63, p62, p62
- abstain: Không có thông tin cụ thể về tỷ lệ doanh nghiệp tham gia xuất khẩu qua TMĐT sang thị trường Úc trong tài liệu.

## t30 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ hoàn trả hàng trung bình của các đơn hàng TMĐT tại Việt Nam năm 2023 là bao nhiêu?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ website có chính sách đổi trả (tr. 75) và lý do ưu tiên mua online 'dịch vụ trả hàng' (tr. 44); không có tỷ lệ hoàn trả đơn hàng ('hoàn trả' không xuất hiện).
**Agent (abstain, 1 tool call, 31.81s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ hoàn trả hàng trung bình đơn hàng TMĐT Việt Nam 2023` → p77, p64, p40, p68, p40
- abstain: Không tìm thấy thông tin về tỷ lệ hoàn trả hàng trung bình của các đơn hàng TMĐT tại Việt Nam năm 2023.
