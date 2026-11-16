# Phiếu chấm A0 / test

Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.


## t01 · table · có đáp án
**Câu hỏi:** Ước tính giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023 là bao nhiêu USD?
**Đáp án chuẩn:** 336 USD.  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Ước tính giá trị mua sắm trực tuyến của một người (USD)', cột 2023
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 46.35s):** Giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023 ước tính như sau: 34% người tiêu dùng chi từ 5 triệu - 10 triệu đồng, 21% chi từ 10 triệu - 15 triệu đồng, và 29% chi trên 20 triệu đồng. Nếu quy đổi sang USD (1 triệu đồng ~ 42 USD), thì giá trị trung bình ước tính khoảng 238 USD (5 triệu đồng) đến 357 USD (15 triệu đồng) cho các nhóm chi tiêu này. [sach-trang-tmdt-2023:p048:B01] [sach-trang-tmdt-2023:p050:B02]
- search_documents: `giá trị mua sắm trực tuyến của một người tại Việt Nam năm 2023` → p48, p50, p50

> **[sach-trang-tmdt-2023:p048:B01]** 9. Giá trị hàng hóa mua sắm trực tuyến của một người trong năm
3% | Dưới 2 triệu đồng
4%
9% | Từ 2 triệu - 5 triệu đồng
34% | Từ 5 triệu - 10 triệu đồng
21% | Từ 10 triệu - 15 triệu đồng
Từ 15 triệu - 20 triệu đồng
29%
Trên 20 triệu đồng

> **[sach-trang-tmdt-2023:p050:B02]** 14. Ước tính giá trị mua hàng hóa/dịch vụ qua mạng từ thương nhân nước ngoài trong năm 2023
4%
9% | Dưới 1 triệu đồng
38% | Từ 1 triệu - 3 triệu đồng
21% | Từ 3 triệu - 5 triệu đồng
Từ 5 triệu - 10 triệu đồng
33% | Trên 10 triệu đồng
[Tiêu đề trục dọc] (Tỷ lệ người tiêu dùng mua hàng; của người bán nước ngoài trên; sàn giao dịch TMĐT tại Việt Nam)

## t02 · table · có đáp án
**Câu hỏi:** Số người tiêu dùng mua sắm trực tuyến ước tính của Việt Nam năm 2023 tăng thêm bao nhiêu triệu người so với năm 2018?
**Đáp án chuẩn:** Tăng khoảng 21,1 triệu người (từ 39,9 triệu năm 2018 lên 61 triệu năm 2023).  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người)', cột 2018 và 2023
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 22.89s):** Số người tiêu dùng mua sắm trực tuyến tại Việt Nam năm 2023 ước tính là 61 triệu người, trong khi năm 2018 là 39,9 triệu người. Sự tăng trưởng là 61 - 39,9 = 21,1 triệu người. [sach-trang-tmdt-2023:p040:B00]
- search_documents: `số người tiêu dùng mua sắm trực tuyến Việt Nam 2023 2018` → p40, p37, p50

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

## t03 · table · có đáp án
**Câu hỏi:** Trong danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu, website dsvn.vn thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Tổng công ty Đường sắt Việt Nam.  
**Evidence:** tr.78 — Bảng 4.1, STT 7
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 18.29s):** Website dsvn.vn thuộc Tổng công ty Đường sắt Việt Nam. [sach-trang-tmdt-2023:p078:B01]
- search_documents: `dsvn.vn doanh nghiệp` → p78, p54, p85

> **[sach-trang-tmdt-2023:p078:B01]** 4.1. Danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu
STT | Website/ứng dụng | Tên doanh nghiệp
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
11 | Karavan | Công ty Cổ phần KARAVAN Việt Nam
12 | mygbvs.groz-becker

## t04 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT gọi xe, ứng dụng HeyU thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần công nghệ HeyU Việt Nam.  
**Evidence:** tr.84 — Bảng 4.3 Nhóm doanh nghiệp dẫn đầu thị trường dịch vụ TMĐT gọi xe, STT 5
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 18.51s):** Ứng dụng HeyU thuộc Công ty Cổ phần công nghệ HeyU Việt Nam. [sach-trang-tmdt-2023:p084:B00]
- search_documents: `ứng dụng HeyU thuộc doanh nghiệp nào` → p84, p84, p83

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
**Agent (answered, 1 tool call, 17.01s):** Luật An ninh mạng được ban hành vào ngày 12/6/2018. [sach-trang-tmdt-2023:p088:B01]
- search_documents: `Luật An ninh mạng ban hành ngày nào` → p88, p14, p88

> **[sach-trang-tmdt-2023:p088:B01]** PHỤ LỤC: BẢNG CẬP NHẬT KHUNG PHÁP LÝ CƠ BẢN VỀ THƯƠNG MẠI ĐIỆN TỬ
Thời gian
ban hành Luật Trạng thái hiệu lực
24/11/2023 Luật viễn thông (sửa đổi) 1/7/2024
22/6/2023 Luật Giao dịch điện tử (sửa đổi) 01/7/2024
20/6/2023 Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) 01/7/2024
16/6/2022 Luật sửa đổi, bổ sung một số điều của Luật Sở hữu trí tuệ 01/03/2022
11/01/2022
Luật sửa đổi, bổ sung một số điều của Luật Đầu tư công, Luật Đầu tư
theo phương thức đối tác công tư, Luật Đầu tư, Luật Nhà ở, Luật Đấu
thầu, Luật Điện lực, Luật Doanh nghiệp, Luật Thuế tiêu thụ đặc biệt và
Luật Thi hành án dân sự
01/03/2022
18/06/2020 Luật Đầu tư Hết hiệu lực một phần
17/06/2020 Luật Doanh nghiệp Hết hiệu lực một 

## t06 · table · có đáp án
**Câu hỏi:** Tỷ lệ website/ứng dụng TMĐT bán hàng và website/ứng dụng CCDV TMĐT có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng là bao nhiêu? Loại nào cao hơn?
**Đáp án chuẩn:** Bán hàng 69,8%, CCDV 71,9%; website/ứng dụng CCDV TMĐT cao hơn 2,1 điểm %.  
**Evidence:** tr.75 — Bảng 5.3 Các chính sách, cơ chế hỗ trợ khách hàng, hàng cuối 'Cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 31.81s):** Tỷ lệ website/ứng dụng TMĐT bán hàng có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng là 69,8%, trong khi tỷ lệ này ở website/ứng dụng CCDV TMĐT là 71,9%. Như vậy, tỷ lệ ở CCDV TMĐT cao hơn. [sach-trang-tmdt-2023:p075:B00]
- search_documents: `tỷ lệ website/ứng dụng TMĐT bán hàng có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng` → p75, p70, p59
- search_documents: `tỷ lệ website/ứng dụng CCDV TMĐT có cơ chế cho phép khách hàng kiểm hàng trước khi nhận hàng` → p75, p70, p65

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
**Agent (answered, 1 tool call, 16.1s):** Theo Nghị định 13/2023/NĐ-CP, có tổng cộng 11 quyền của chủ thể dữ liệu. Quyền cuối cùng (số 11) là "Quyền khiếu nại, tố cáo, khởi kiện". [sach-trang-tmdt-2023:p021:B00]
- search_documents: `sơ đồ quyền của chủ thể dữ liệu Nghị định 13/2023/NĐ-CP` → p21, p23, p23

> **[sach-trang-tmdt-2023:p021:B00]** 4. Nghị định số 13/2023/NĐ-CP ngày 17 tháng 4 năm 2023 của Chính phủ
2 Quyền của chủ thể dữ liệu
1
4
9
2
7
5
10
3
8
6
11
Quyền được biết
Quyền đồng ý
Quyền cung cấp dữ liệu
Quyền truy cập đồng ý
Quyền phản đối xử lý dữ liệu
Quyền xóa dữ liệu
Quyền yêu cầu bồi thường thiệt hại
Quyền hạn chế xử lý dữ liệu
Quyền tự bảo vệ
Quyền rút lại sự đồng ý
Quyền khiếu nại, tố cáo, khởi kiện;

## t08 · image · có đáp án
**Câu hỏi:** Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi) gồm những loại dịch vụ nào?
**Đáp án chuẩn:** 3 loại: dịch vụ cấp dấu thời gian; dịch vụ chứng thực thông điệp dữ liệu; dịch vụ chứng thực chữ ký số công cộng.  
**Evidence:** tr.14 — Sơ đồ khối '1 Phân loại dịch vụ tin cậy' (3 ô)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 19.7s):** Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi) gồm ba loại dịch vụ: 
1. Dịch vụ cấp dấu thời gian;
2. Dịch vụ chứng thực thông điệp dữ liệu;
3. Dịch vụ chứng thực chữ ký số công cộng. [sach-trang-tmdt-2023:p014:B00]
- search_documents: `Sơ đồ phân loại dịch vụ tin cậy theo Luật Giao dịch điện tử (sửa đổi)` → p14, p15, p16

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

## t09 · image · có đáp án
**Câu hỏi:** Theo infographic tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023, bao nhiêu phần trăm doanh nghiệp sử dụng hợp đồng điện tử trong giao dịch?
**Đáp án chuẩn:** 41%.  
**Evidence:** tr.57 — Infographic mục 3, ô thứ 2 (hình E-CONTRACT)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 37.74s):** 41% doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch năm 2023. [sach-trang-tmdt-2023:p057:B00]
- search_documents: `tình hình sử dụng hợp đồng điện tử năm 2023` → p57, p26, p3

> **[sach-trang-tmdt-2023:p057:B00]** 2. Nguồn nhân lực cho thương mại điện tử
65% | doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT
3. Tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023
80% | doanh nghiệp có sử dụng chữ ký điện tử
41% | doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch
22% | doanh nghiệp có sử dụng dịch vụ chứng thực hợp đồng điện tử

## t10 · image · có đáp án
**Câu hỏi:** Năm 2023, Cổng thông tin quản lý hoạt động TMĐT tiếp nhận bao nhiêu hồ sơ đăng ký và tăng bao nhiêu phần trăm so với năm 2022?
**Đáp án chuẩn:** 9.604 hồ sơ đăng ký, tăng 14,3% so với năm 2022.  
**Evidence:** tr.26 — Infographic khối thứ hai (biểu tượng thư mục), dòng 2
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 13.43s):** Năm 2023, Cổng thông tin quản lý hoạt động thương mại điện tử tiếp nhận 9.604 hồ sơ đăng ký, tăng 14,3% so với năm 2022. [sach-trang-tmdt-2023:p026:B01]
- search_documents: `Cổng thông tin quản lý hoạt động TMĐT hồ sơ đăng ký 2023 2022` → p26, p19, p26

> **[sach-trang-tmdt-2023:p026:B01]** 9.604 hồ sơ đăng ký
tăng 14,3% so với năm 2022
48.348 website/ứng dụng đã được xác nhận thông báo
tăng 6,7% so với năm 2022
1.218 website/ứng dụng đã được xác nhận đăng ký
tăng 1,1% so với năm 2022
18,0% 12,6%
14,4%
12,6%
17,1%
26,1%
Các loại hành vi khác
Chưa đăng ký, thông báo
website/ứng dụng
Giả mạo thông tin đăng ký
Kinh doanh hàng giả, hàng cấm
Lừa đảo trong thanh toán
Mạo danh website/ứng dụng hoặc
thương nhân, tổ chức khác

## t11 · image · có đáp án
**Câu hỏi:** Theo infographic phương thức vận chuyển hàng hóa của doanh nghiệp, bao nhiêu phần trăm doanh nghiệp tự vận chuyển và bao nhiêu phần trăm sử dụng dịch vụ của bên thứ ba?
**Đáp án chuẩn:** 67% doanh nghiệp tự vận chuyển; 60% sử dụng dịch vụ của bên thứ ba.  
**Evidence:** tr.64 — Infographic 1. Phương thức vận chuyển hàng hóa (3 thanh)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 21.51s):** Theo thông tin từ Sách trắng Thương mại điện tử Việt Nam năm 2023, 67% doanh nghiệp tự vận chuyển hàng hóa, trong khi 60% doanh nghiệp sử dụng dịch vụ của bên thứ ba. [sach-trang-tmdt-2023:p064:B00]
- search_documents: `phương thức vận chuyển hàng hóa của doanh nghiệp tự vận chuyển bên thứ ba` → p64, p74, p64

> **[sach-trang-tmdt-2023:p064:B00]** V. CÁC DỊCH VỤ HỖ TRỢ THƯƠNG MẠI ĐIỆN TỬ
1. Phương thức vận chuyển hàng hóa mà doanh nghiệp đang sử dụng
67% | doanh nghiệp tự vận chuyển
60% | doanh nghiệp sử dụng dịch vụ của bên thứ ba
1% | sử dụng phương thức khác

## t12 · chart · có đáp án
**Câu hỏi:** Năm 2022, khu vực nào có tỷ lệ tăng trưởng doanh thu bán lẻ TMĐT cao nhất thế giới và tỷ lệ đó là bao nhiêu?
**Đáp án chuẩn:** Đông Nam Á, 20,6%.  
**Evidence:** tr.31 — Biểu đồ thanh ngang 2.2, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 19.89s):** Năm 2022, khu vực có tỷ lệ tăng trưởng doanh thu bán lẻ thương mại điện tử cao nhất thế giới là Đông Nam Á với tỷ lệ 20,6%. [sach-trang-tmdt-2023:p031:B00]
- search_documents: `2022 tỷ lệ tăng trưởng doanh thu bán lẻ TMĐT cao nhất thế giới` → p31, p32, p31

> **[sach-trang-tmdt-2023:p031:B00]** 2.2. Tỷ lệ tăng trưởng doanh thu bán lẻ TMĐT toàn cầu, chia theo khu vực năm 2022
Đô | ng N am Á | 20,6%
Ch | âu | Mỹ L | atinh | 20,4%
Tru ng Đ | ông v | à C hâu P | hi | 17,0%
Tru ng & Đô | ng Â u | 16,1%
Bắc | Mỹ | 15,5%
Châu Á - Thá i Bình | Dươ | ng | 11,8%
Tây Â | u | 6,1%
Toàn | cầu | 12,2%
Nguồn: Báo cáo “Global Ecommerce Forecast” - eMarketer 3

## t13 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay năm 2023 là bao nhiêu và giảm bao nhiêu điểm phần trăm so với năm 2022?
**Đáp án chuẩn:** 50% năm 2023, giảm 13 điểm % so với 63% năm 2022.  
**Evidence:** tr.42 — Biểu đồ cột 1. Phương tiện truy cập Internet, nhóm 'Máy tính để bàn, Máy tính xách tay'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 44.6s):** Tỷ lệ người dùng Internet truy cập bằng máy tính để bàn và máy tính xách tay năm 2023 là 50%. So với năm 2022, tỷ lệ này đã giảm 13 điểm phần trăm (từ 63% xuống 50%). [sach-trang-tmdt-2023:p042:B00] [sach-trang-tmdt-2023:p042:B02]
- search_documents: `tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay năm 2023` → p42, p42, p42
- search_documents: `tỷ lệ người dùng Internet truy cập bằng máy tính để bàn/máy tính xách tay năm 2022` → p42, p42, p42

> **[sach-trang-tmdt-2023:p042:B00]** III. TÌNH HÌNH SỬ DỤNG INTERNET
1. Phương tiện truy cập Internet của người dân
94% | 90%
63%
50% | 2022
2023
14%
10%
Máy tính để bàn | Điện thoại di động | Thiết bị khác
Máy tính xách tay | (Ipad, Máy tính bảng)

> **[sach-trang-tmdt-2023:p042:B02]** 2. Thời gian truy cập Internet trung bình mỗi ngày
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1. Phương tiện truy cập Internet của người dân — Máy tính để bàn Máy tính xách tay: 2022: 63%; 2023: 50%
1. Phương tiện truy cập Internet của người dân — Điện thoại di động: 2022: 94%; 2023: 90%
1. Phương tiện truy cập Internet của người dân — Thiết bị khác (Ipad, Máy tính bảng): 2022: 14%; 2023: 10%
2. Thời gian truy cập Internet trung bình mỗi ngày — Dưới 3 tiếng: 2022: 11%; 2023: 23%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 3 - 5 tiếng: 2022: 38%; 2023: 37%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 5 -7 tiếng: 2022: 30%; 2023: 19%
2. Thời gian truy 

## t14 · chart · có đáp án
**Câu hỏi:** Sàn giao dịch TMĐT bán buôn bán lẻ nào được người tiêu dùng ưa chuộng thứ ba và với tỷ lệ bao nhiêu?
**Đáp án chuẩn:** TikTok, 34% (sau Shopee 81% và Lazada 42%).  
**Evidence:** tr.46 — Biểu đồ cột 6.1, cột thứ ba
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 20.21s):** Sàn giao dịch TMĐT bán buôn bán lẻ được người tiêu dùng ưa chuộng thứ ba là TikTok với tỷ lệ 34%. [sach-trang-tmdt-2023:p046:B01]
- search_documents: `sàn giao dịch TMĐT bán buôn bán lẻ ưa chuộng thứ ba tỷ lệ` → p46, p46, p46

> **[sach-trang-tmdt-2023:p046:B01]** 6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng
81%
42%
34%
20%
8% | 2%
Shopee | Lazada | TikTok | Tiki | Sendo | Khác
6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
70%
23%
15% | 14%
Grab | Be | GoJek | Khác
[Tiêu đề trục dọc] (Tỷ lệ người dùng Internet)

## t15 · chart · có đáp án
**Câu hỏi:** Bao nhiêu phần trăm doanh nghiệp sở hữu website/ứng dụng di động có chi phí quảng cáo trung bình dưới 10 triệu đồng?
**Đáp án chuẩn:** 63%.  
**Evidence:** tr.61 — Biểu đồ cột 1.2 Ước tính chi phí quảng cáo trung bình, cột 'Dưới 10 triệu đồng'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 17.59s):** 63% doanh nghiệp sở hữu website/ứng dụng di động có chi phí quảng cáo trung bình dưới 10 triệu đồng. [sach-trang-tmdt-2023:p061:B01] [sach-trang-tmdt-2023:p061:B00]
- search_documents: `doanh nghiệp sở hữu website/ứng dụng di động chi phí quảng cáo trung bình dưới 10 triệu đồng` → p61, p61, p60

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

> **[sach-trang-tmdt-2023:p061:B00]** 1.2. . Ước tính chi phí quảng cáo trung bình của doanh nghiệp
63%
25%
7% | 2% | 3%
Dưới 10 triệu | Từ 10 - 20 | Từ 20- 50 | Trên 50 - 100 | Trên 100
đồng | triệu đồng | triệu đồng | triệu đồng | triệu đồng

## t16 · chart · có đáp án
**Câu hỏi:** Theo biểu đồ quy mô nền kinh tế Internet phân theo quốc gia, quy mô kinh tế Internet của Việt Nam năm 2023 và số liệu dự báo năm 2025 là bao nhiêu?
**Đáp án chuẩn:** 30 tỷ USD năm 2023; dự báo 43 tỷ USD năm 2025.  
**Evidence:** tr.34 — Biểu đồ thanh ngang 2. Quy mô nền kinh tế Internet phân theo quốc gia năm 2023, cặp thanh 'Việt Nam'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 23.49s):** Quy mô kinh tế Internet của Việt Nam năm 2023 là 30 tỷ USD và dự báo năm 2025 là 43 tỷ USD. [sach-trang-tmdt-2023:p034:B01]
- search_documents: `quy mô kinh tế Internet của Việt Nam năm 2023 và dự báo năm 2025` → p34, p34, p3

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
**auto:** context đủ evidence = False
**Agent (answered, 2 tool call, 42.6s):** Doanh thu TMĐT B2C Việt Nam năm 2023 ước tính đạt 20,5 tỷ USD [sach-trang-tmdt-2023:p040:B00]. Doanh thu bán lẻ hàng hóa trực tuyến của Việt Nam năm 2023 là 16,4 tỷ USD [sach-trang-tmdt-2023:p037:B04]. Chênh lệch giữa hai số liệu này là 20,5 tỷ USD - 16,4 tỷ USD = 4,1 tỷ USD.
- search_documents: `doanh thu TMĐT B2C Việt Nam năm 2023 chương III` → p40, p31, p30
- search_documents: `doanh thu bán lẻ hàng hóa trực tuyến Việt Nam năm 2023 e-Conomy SEA chương II` → p35, p37, p37

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

> **[sach-trang-tmdt-2023:p037:B04]** 8. Việt Nam
Việt Nam (đơn vị: Tỷ USD) — 2023 — Tốc độ tăng trưởng doanh thu bán lẻ hàng hóa trực tuyến: 11%
8. Việt Nam (đơn vị: Tỷ USD) — 2025 — Doanh thu bán lẻ hàng hóa trực tuyến: 24
8. Việt Nam (đơn vị: Tỷ USD) — 2025 — Doanh thu vận tải và thực phẩm: 4
8. Việt Nam (đơn vị: Tỷ USD) — 2025 — Doanh thu du lịch trực tuyến: 7
8. Việt Nam (đơn vị: Tỷ USD) — 2025 — Doanh thu nội dung nghe nhìn trực tuyến: 7
8. Việt Nam (đơn vị: Tỷ USD) — 2025 — Tốc độ tăng trưởng doanh thu bán lẻ hàng hóa trực tuyến: 22%

## t18 · multihop · có đáp án
**Câu hỏi:** Quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022 là quốc gia nào, và doanh thu TMĐT B2C năm 2022 của quốc gia đó là bao nhiêu?
**Đáp án chuẩn:** Trung Quốc (50,2% thị phần); doanh thu TMĐT B2C năm 2022 là 2.682 tỷ USD.  
**Evidence:** tr.32 — Biểu đồ 2.4 Top 12 quốc gia chiếm thị phần TMĐT lớn nhất, thanh đầu tiên; tr.33 — Biểu đồ 2.6 Trung Quốc, cột 2022
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 46.4s):** Quốc gia chiếm thị phần thương mại điện tử lớn nhất toàn cầu năm 2022 là Trung Quốc với thị phần 50,2%. Doanh thu thương mại điện tử B2C của Trung Quốc năm 2022 là 3.982 tỷ USD. [sach-trang-tmdt-2023:p032:B00] [sach-trang-tmdt-2023:p033:B00]
- search_documents: `quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022` → p32, p32, p31
- search_documents: `doanh thu TMĐT B2C năm 2022 Trung Quốc` → p33, p30, p40

> **[sach-trang-tmdt-2023:p032:B00]** 2.4. Top 12 quốc gia chiếm thị phần TMĐT lớn nhất toàn cầu năm 2022
Tru ng Quố | c | 50,2%
Mỹ | 19,2%
Vươn | g q uốc | An h | 4,4%
Nhật | Bả n | 3,0%
Hàn | Quố | c | 2,6%
Đức | 2,1%
Pháp | 1,7% | (Tỷ lệ trong tổng doanh thu TMĐT toàn cầu)
Ấn | Độ | 1,5%
Canada | 1,4%
Nga | 1,0%
Brazail | 1,0%
Indonesia | 1,0%
Nguồn: Báo cáo “Global Ecommerce Forecast” - eMarketer

> **[sach-trang-tmdt-2023:p033:B00]** 2.6. Trung Quốc 5
3.982
3.739
3.454
3.198
2.931 | 50,5%
2.682 | 48,6% | 51,8%
2.528 | 45,9% | 47,3%
43,2% | 45,6%
14,0%
9,3% | 9,1% | 8,0% | 8,3%
6,5%
6,1%
2021 | 2022 | 2023 | 2024* | 2025* | 2026* | 2027*
Do | an h th u TMĐ | T | B2C | (tỷ US | D)Tỷ lệ tă ng | trưởng* Số | liệ | u dự b | áo
Tỷ | lệ của T | MĐT | so với | tổ ng doan h th u bán | lẻ

## t19 · multihop · có đáp án
**Câu hỏi:** Sàn TMĐT lĩnh vực dịch vụ vận tải nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành ứng dụng này theo danh sách doanh nghiệp dẫn đầu thị trường gọi xe?
**Đáp án chuẩn:** Grab, 70%; do Công ty TNHH Grab vận hành.  
**Evidence:** tr.46 — Biểu đồ cột 6.2 Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải, cột Grab; tr.84 — Bảng 4.3 doanh nghiệp dẫn đầu dịch vụ gọi xe, STT 3; tr.83 — Bảng 4.1, STT 4 (evidence thay thế cho tên doanh nghiệp)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 20.23s):** Sàn TMĐT lĩnh vực dịch vụ vận tải được người tiêu dùng ưa chuộng nhất là Grab với tỷ lệ 70%. Các doanh nghiệp dẫn đầu thị trường gọi xe bao gồm: 1. Grab (Công ty TNHH Grab), 2. Be (Công ty Cổ phần BE GROUP), 3. GoJek (Công ty Cổ phần Thương mại Công nghệ Go Viet). [sach-trang-tmdt-2023:p046:B03] [sach-trang-tmdt-2023:p084:B00]
- search_documents: `sàn TMĐT dịch vụ vận tải ưa chuộng tỷ lệ doanh nghiệp dẫn đầu thị trường gọi xe` → p46, p84, p46

> **[sach-trang-tmdt-2023:p046:B03]** 6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng — Khác: 2%
6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng — Grab: 70%
6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng — Be: 23%
6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng — GoJek: 15%
6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng — Khác: 14%

> **[sach-trang-tmdt-2023:p084:B00]** 4.3. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT gọi xe 19
19 Taxi, xe ôm
STT Website/ứng dụng Tên doanh nghiệp
1 Be Công ty Cổ phần BE GROUP
2 GoJek Công ty Cổ phần Thương mại Công nghệ Go Viet
3 Grab Công ty TNHH Grab
4 GV Ship Công Ty Cổ Phần GV ASIA
5 HeyU Công ty Cổ phần công nghệ HeyU Việt Nam

## t20 · multihop · có đáp án
**Câu hỏi:** TP. Hồ Chí Minh chiếm tỷ lệ đơn hàng thành công bao nhiêu trên website/ứng dụng TMĐT bán hàng và bao nhiêu trên website/ứng dụng cung cấp dịch vụ TMĐT? Chênh lệch bao nhiêu điểm phần trăm?
**Đáp án chuẩn:** 34,6% (TMĐT bán hàng) và 24,1% (CCDV TMĐT); chênh lệch 10,5 điểm %.  
**Evidence:** tr.77 — Biểu đồ 3. Tỷ lệ số lượng đơn hàng thành công của website, ứng dụng TMĐT bán hàng theo tỉnh/thành, mục TP. Hồ Chí Minh; tr.82 — Biểu đồ 3.2 Tỷ lệ số lượng đơn hàng thành công theo địa phương (website CCDV TMĐT), mục TP. Hồ Chí Minh
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 30.1s):** Tỷ lệ đơn hàng thành công của TP. Hồ Chí Minh trên website/ứng dụng TMĐT bán hàng là 34,6% và trên website/ứng dụng cung cấp dịch vụ TMĐT là 24,1%. Chênh lệch giữa hai tỷ lệ này là 10,5 điểm phần trăm (34,6% - 24,1%). [sach-trang-tmdt-2023:p077:B00] [sach-trang-tmdt-2023:p082:B00]
- search_documents: `TP. Hồ Chí Minh tỷ lệ đơn hàng thành công website/ứng dụng TMĐT bán hàng` → p77, p82, p80
- search_documents: `TP. Hồ Chí Minh tỷ lệ đơn hàng thành công website/ứng dụng cung cấp dịch vụ TMĐT` → p77, p81, p82

> **[sach-trang-tmdt-2023:p077:B00]** 3. Tỷ lệ số lượng đơn hàng thành công của website, ứng dụng TMĐT bán hàng tại một số tỉnh/
thành phố
TP. | Hồ Chí | Minh | 34,6%
Hà Nội | 21,8%
Bìn | h | Dương | 3,7%
Đồng | Nai | 3,2 %
Đà Nẵng | 3,0%
Cần | Thơ | 2,6 | %
Hải Phòng | 2,5%
Bà Rịa – | Vũng | Tàu | 2,1%
Lon | g An | 1,7%
Hải D | ươn | g | 1,7%
Bắc Ninh | 1,6%
Quảng | Ninh 1,6%
Lâm | Đồng | 1,6%
Nghệ | An 1,5%
Khá | nh H | òa | 1,5%
Vĩn | h Phúc | 1,4%
Hư | ng | Yên | 1,4%
Than | h Hóa | 1,4%
Nam | Định | 1,3%
Thái | Nguyên | 1,2%
Các tỉnh/thành | phố còn | lại8,8%

> **[sach-trang-tmdt-2023:p082:B00]** 3.2. Tỷ lệ số lượng đơn hàng thành công theo địa phương
TP . Hồ Chí | Minh | 24,1%
Hà Nội | 12,4%
Đà Nẵng | 5,1 %
Bình | Dư | ơng | 4,7 %
Đồng Nai | 4,1 %
Cần | Thơ | 4,1 %
Bà Rịa - Vũng | Tàu | 4,0 %
Khá | nh Hòa | 3,3 %
Nghệ | An | 3,3%
Lâm | Đồng | 3,2%
Quảng | Ninh | 2,8 %
Lon | g An | 2,8 %
Hải Phòng | 2,8 %
Hải Dư | ơng | 2,5 %
Bắc Ninh | 2,5 %
Thái | Nguyên | 2,3 %
Than | h Hóa | 2,2%
Vĩn | h Phúc | 2,2%
Nam | Định | 2,2 %
Hư | ng Yên | 2,2 %
Các tỉnh/thành phố còn | lại | 7,1 %

## t21 · text · có đáp án
**Câu hỏi:** Theo Chỉ thị 18/CT-TTg, giải pháp nào được nêu liên quan đến mã số thuế của cá nhân?
**Đáp án chuẩn:** Thực hiện chuyển đổi sử dụng mã định danh cá nhân làm mã số thuế; tích hợp tài khoản định danh điện tử để kê khai, đăng ký nộp thuế trên ứng dụng VNeID và các nền tảng khác.  
**Evidence:** tr.25 — Mục '2. Một số giải pháp' của Chỉ thị 18/CT-TTg, gạch đầu dòng 4
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 27.1s):** Giải pháp liên quan đến mã số thuế của cá nhân theo Chỉ thị 18/CT-TTg bao gồm việc thực hiện chuyển đổi sử dụng mã định danh cá nhân làm mã số thuế. Đồng thời, tích hợp sử dụng tài khoản định danh điện tử để kê khai, đăng ký nộp thuế trên ứng dụng định danh điện tử quốc gia (VneID) và các nền tảng khác do Cơ quan thuế hướng dẫn. [sach-trang-tmdt-2023:p025:B00]
- search_documents: `Chỉ thị 18/CT-TTg mã số thuế cá nhân` → p24, p25, p93

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
**Agent (answered, 1 tool call, 21.24s):** Dữ liệu về vị trí của cá nhân được xác định qua dịch vụ định vị thuộc loại dữ liệu cá nhân nhạy cảm theo Nghị định 13/2023/NĐ-CP. [sach-trang-tmdt-2023:p020:B01]
- search_documents: `Nghị định 13/2023/NĐ-CP dữ liệu vị trí cá nhân dịch vụ định vị` → p20, p20, p23

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
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 24.8s):** Sách trắng Thương mại điện tử 2023 được xây dựng nhằm đánh giá sơ bộ kết quả thực hiện mục tiêu đặt ra tại Chỉ thị số 18/CT-TTg ngày 30 tháng 5 năm 2023 của Thủ tướng Chính phủ. [sach-trang-tmdt-2023:p024:B00]
- search_documents: `đánh giá sơ bộ kết quả thực hiện mục tiêu quyết định Thủ tướng Chính phủ` → p24, p56, p24

> **[sach-trang-tmdt-2023:p024:B00]** 5.Chỉ thị số 18/CT-TTg ngày 30 tháng 5 năm 2023 của Thủ tướng Chính phủ
Ngày 30 tháng 5 năm 2023, Thủ tướng Chính phủ đã ban hành Chỉ thị số 18/CT-TTg về việc đẩy mạnh kết
nối, chia sẻ dữ liệu phục vụ phát triển TMĐT chống thất thu thuế, bảo đảm an ninh tiền tệ.
Tăng cường hiệu lực, hiệu quả và tiếp tục đẩy mạnh chuyển đổi số trong công
tác QLNN đối với hoạt động TMĐT, hoạt động kinh doanh trên nền tảng số,
kinh doanh xuyên biên giới, kết nối, chia sẻ dữ liệu giữa các bộ, ngành phục vụ
phát triển TMĐT, chống thất thu thuế, bảo đảm an ninh tiền tệ.

## t24 · text · có đáp án
**Câu hỏi:** Theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi), tổ chức thiết lập, vận hành nền tảng số lớn phải đánh giá định kỳ những nội dung nào?
**Đáp án chuẩn:** (1) Hoạt động kiểm duyệt nội dung việc sử dụng hệ thống thuật toán và quảng cáo hướng tới NTD, nhóm NTD cụ thể; (2) việc thực hiện quy định xử lý tài khoản giả, việc sử dụng trí tuệ nhân tạo, các giải pháp tự động toàn bộ hoặc tự động một phần.  
**Evidence:** tr.13 — Khối '4 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số lớn', ô 3 và 4
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 24.3s):** Theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi), tổ chức thiết lập, vận hành nền tảng số lớn phải đánh giá định kỳ các nội dung sau: 1) Hoạt động kiểm duyệt nội dung việc sử dụng hệ thống thuật toán và quảng cáo hướng tới người tiêu dùng, nhóm người tiêu dùng cụ thể; 2) Việc thực hiện quy định xử lý tài khoản giả, việc sử dụng trí tuệ nhân tạo, các giải pháp tự động toàn bộ hoặc tự động một phần. [sach-trang-tmdt-2023:p013:B00]
- search_documents: `Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) tổ chức thiết lập vận hành nền tảng số lớn đánh giá định kỳ` → p13, p12, p11

> **[sach-trang-tmdt-2023:p013:B00]** 1. Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi)
4 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số lớn với NTD trong giao dịch trên không
gian mạng
1
3
2
4
Có trách nhiệm thực hiện quy định tại khoản 3 Điều 39 Luật này;
Thiết lập kho lưu trữ quảng cáo có sử dụng thuật toán để hướng đến NTD, nhóm NTD cụ thể;
Đánh giá định kỳ hoạt động kiểm duyệt nội dung việc sử dụng hệ thống thuật toán và quảng
cáo hướng tới NTD, nhóm NTD cụ thể;
Đánh giá định kỳ việc thực hiện quy định xử lý tài khoản giả, việc sử dụng trí tuệ nhân
tạo, các giải pháp tự động toàn bộ hoặc tự động một phần;

## t25 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Doanh thu TMĐT B2C của Việt Nam năm 2024 đạt bao nhiêu tỷ USD?
**Lý do thiếu:** Biểu đồ B2C Việt Nam (tr. 40) dừng ở 2023; số liệu dự báo 2024* chỉ có cho toàn cầu (tr. 30), Trung Quốc và Mỹ (tr. 33); e-Conomy SEA chỉ dự báo năm 2025 (tr. 34–37).
**Agent (answered, 1 tool call, 25.63s):** Doanh thu TMĐT B2C của Việt Nam năm 2024 ước đạt 25 tỷ USD. [sach-trang-tmdt-2023:p030:B01]
- search_documents: `doanh thu TMĐT B2C Việt Nam năm 2024` → p40, p30, p33

> **[sach-trang-tmdt-2023:p030:B01]** 2. Quy mô thị trường TMĐT B2C toàn cầu 2
2.1. Toàn cầu | 26,4%
20,6% | 23.9
21.1 | 21.1 | 21.8 | 22.5 | 23.3
19.5 | 16,3%
12,2% | 11,0%
8,2% | 10,0% | 9,2%
3,3% | 3,3% | 3,2% | 3,4% 2,6%
4,9 | 5,5 | 6,2 | 6,8 | 7,4
3,4 | 4,2
-7,5%
2019 | 2020 | 2021 | 2022 | 2023* | 2024* | 2025*
Do | an h th u bán | lẻ q ua | TMĐT | (nghìn tỷ US | D) | Do | an h th u bán | lẻ n goài | TMĐT | (nghìn tỷ US | D)
Tỷ | lệ th ay đ | ổi d oan h th u TMĐT | bán | lẻ | Tỷ | lệ th ay đ | ổi d oan h th u bán | lẻ n goài | TMĐT
Nguồn: Báo cáo “Global Ecommerce Forecast” - eMarketer
2 Doanh thu TMĐT bán lẻ bao gồm hàng hóa và dịch vụ; không bao gồm dịch vụ du lịch, dịch vụ ăn uống, cá cược, dịch vụ chuyển tiền, các loại

## t26 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.3 (tr. 29) chỉ có Philippines, Thái Lan, Malaysia, Indonesia, Singapore, Việt Nam, Ấn Độ, Úc, Trung Quốc, Hàn Quốc và trung bình toàn cầu; 'Nhật Bản' chỉ xuất hiện ở tr. 32 (thị phần) và tr. 63 (xuất khẩu).
**Agent (answered, 1 tool call, 20.28s):** Thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản năm 2023 được phân bố như sau: 23% dưới 3 tiếng, 37% từ 3 - 5 tiếng, 19% từ 5 - 7 tiếng, 13% từ 7 - 9 tiếng, và 8% trên 9 tiếng. [sach-trang-tmdt-2023:p042:B02]
- search_documents: `thời gian truy cập Internet trung bình mỗi ngày của người dùng tại Nhật Bản` → p42, p42, p28

> **[sach-trang-tmdt-2023:p042:B02]** 2. Thời gian truy cập Internet trung bình mỗi ngày
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1. Phương tiện truy cập Internet của người dân — Máy tính để bàn Máy tính xách tay: 2022: 63%; 2023: 50%
1. Phương tiện truy cập Internet của người dân — Điện thoại di động: 2022: 94%; 2023: 90%
1. Phương tiện truy cập Internet của người dân — Thiết bị khác (Ipad, Máy tính bảng): 2022: 14%; 2023: 10%
2. Thời gian truy cập Internet trung bình mỗi ngày — Dưới 3 tiếng: 2022: 11%; 2023: 23%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 3 - 5 tiếng: 2022: 38%; 2023: 37%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 5 -7 tiếng: 2022: 30%; 2023: 19%
2. Thời gian truy 

## t27 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Shopee chiếm bao nhiêu phần trăm thị phần giá trị giao dịch (GMV) TMĐT tại Việt Nam năm 2023?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ người dùng ưa chuộng Shopee (81%, tr. 46) và danh sách doanh nghiệp dẫn đầu (tr. 83), không có thị phần GMV; 'GMV' không xuất hiện trong toàn văn.
**Agent (answered, 1 tool call, 21.29s):** Shopee chiếm 81% thị phần giá trị giao dịch (GMV) trong lĩnh vực bán buôn bán lẻ của thương mại điện tử tại Việt Nam năm 2023. [sach-trang-tmdt-2023:p046:B02]
- search_documents: `Shopee thị phần giá trị giao dịch GMV TMĐT Việt Nam 2023` → p46, p50, p40

> **[sach-trang-tmdt-2023:p046:B02]** 6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Website TMĐT bán hàng: 34%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Sàn giao dịch TMĐT: 61%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Diễn đàn mạng xã hội: 55%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Các ứng dụng mua hàng trên thiết bị di động: 21%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Hình thức khác: 4%
6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng — S

## t28 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP là bao nhiêu?
**Lý do thiếu:** Phần Nghị định 13/2023 (tr. 20–24) không nêu mức phạt; từ 'phạt' chỉ xuất hiện trong tên các nghị định xử phạt ở phụ lục (tr. 90–92), không liên quan bảo vệ dữ liệu cá nhân.
**Agent (abstain, 3 tool call, 62.75s):** Không đủ bằng chứng để trả lời.
- search_documents: `mức phạt tiền tối đa hành vi vi phạm quy định bảo vệ dữ liệu cá nhân Nghị định 13/2023/NĐ-CP` → p23, p22, p20
- search_documents: `Nghị định 13/2023/NĐ-CP mức phạt tiền` → p92, p92, p92
- search_documents: `Nghị định 13/2023/NĐ-CP mức phạt tiền tối đa` → p92, p92, p23
- abstain: Không tìm thấy thông tin về mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân theo Nghị định 13/2023/NĐ-CP.

## t29 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Bao nhiêu phần trăm doanh nghiệp tham gia xuất khẩu qua TMĐT xuất khẩu sang thị trường Úc?
**Lý do thiếu:** Biểu đồ 2.3.2 (tr. 63) chỉ có Hàn Quốc, Nhật Bản, Trung Quốc, Liên minh châu Âu, Hoa Kỳ và 'Quốc gia khác'; 'Úc' chỉ xuất hiện ở tr. 29–30 (sử dụng Internet).
**Agent (abstain, 1 tool call, 85.91s):** Không đủ bằng chứng để trả lời.
- search_documents: `doanh nghiệp tham gia xuất khẩu qua TMĐT sang thị trường Úc` → p63, p63, p62
- abstain: Tài liệu không cung cấp thông tin về tỷ lệ doanh nghiệp xuất khẩu qua TMĐT sang thị trường Úc.

## t30 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ hoàn trả hàng trung bình của các đơn hàng TMĐT tại Việt Nam năm 2023 là bao nhiêu?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ website có chính sách đổi trả (tr. 75) và lý do ưu tiên mua online 'dịch vụ trả hàng' (tr. 44); không có tỷ lệ hoàn trả đơn hàng ('hoàn trả' không xuất hiện).
**Agent (abstain, 1 tool call, 30.34s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ hoàn trả hàng trung bình đơn hàng TMĐT Việt Nam 2023` → p50, p64, p49
- abstain: Tài liệu không chứa thông tin về tỷ lệ hoàn trả hàng trung bình của các đơn hàng TMĐT tại Việt Nam năm 2023.
