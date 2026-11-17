# Phiếu chấm A4 / test2

Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.


## u01 · table · có đáp án
**Câu hỏi:** Theo bảng số liệu thị trường TMĐT bán lẻ, tỷ lệ người dân Việt Nam sử dụng Internet năm 2020 là bao nhiêu?
**Đáp án chuẩn:** 70%.  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Tỷ lệ người dân sử dụng Internet', cột 2020
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 85.61s):** Tỷ lệ người dân Việt Nam sử dụng Internet năm 2020 là 70%. [sach-trang-tmdt-2023:p40:V2]
- search_documents: `tỷ lệ người dân Việt Nam sử dụng Internet năm 2020` → p28, p40, p42, p42, p40

> **[sach-trang-tmdt-2023:p40:V2]** [table] Doanh thu TMĐT B2C Việt Nam năm 2018 – 2023
(Trang 40, nửa dưới; đơn vị: không ghi)
Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người) | 2018: 39,9 | 2019: 44,8 | 2020: 49,3 | 2021: 54,6 | 2022: 57,0 | 2023: 61
Ước tính giá trị mua sắm trực tuyến của một người (USD) | 2018: 202 | 2019: 225 | 2020: 240 | 2021: 251 | 2022: 288 | 2023: 336
Tỷ trọng doanh thu TMĐT B2C so với tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng cả nước | 2018: 4,2% | 2019: 4,9% | 2020: 5,5% | 2021: 7% | 2022: 7,5% | 2023: 8%
Tỷ lệ người dân sử dụng Internet | 2018: 60% | 2019: 66% | 2020: 70% | 2021: 73% | 2022: 73,2% | 2023: 78,6%

## u02 · table · có đáp án
**Câu hỏi:** Trong danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu, website thegioididong.com thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần Thế Giới Di Động.  
**Evidence:** tr.78 — Bảng 4.1, STT 16
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 83.04s):** Website thegioididong.com thuộc Công ty Cổ phần Thế Giới Di Động. [sach-trang-tmdt-2023:p078:B01]
- search_documents: `thegioididong.com doanh nghiệp` → p78, p78, p61, p54, p54

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

## u03 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ, Voso thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL.  
**Evidence:** tr.83 — Bảng 4.2, STT 10
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 89.94s):** Voso thuộc Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL. [sach-trang-tmdt-2023:p83:V2]
- search_documents: `Voso doanh nghiệp cung cấp dịch vụ TMĐT bán buôn bán lẻ` → p83, p83, p83, p83, p79

> **[sach-trang-tmdt-2023:p83:V2]** [table] 4.2. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ
(Trang 83, nửa dưới; đơn vị: không ghi)
1 | Lazada | Công ty TNHH Recess
2 | samsung.com.vn | Công Ty TNHH Điện Tử Samsung Vina
3 | Selly | Công ty TNHH Selly
4 | Sendo | Công ty Cổ Phần Công Nghệ Sen Đỏ
5 | Shopee | Công ty TNHH Shopee
6 | thuocsi.vn | Công ty TNHH Buymed
7 | Tiki | Công ty TNHH TI KI
8 | TIKTOK | TIKTOK PTE. LTD.
9 | VinShop | Công ty cổ phần One Mount Distribution
10 | Voso | Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL

## u04 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT du lịch trực tuyến, Tripi Partner thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần du lịch Việt Nam Vntravel.  
**Evidence:** tr.85 — Bảng 4.5, STT 3
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 57.74s):** Tripi Partner thuộc Công ty Cổ phần du lịch Việt Nam Vntravel. [sach-trang-tmdt-2023:p085:B00]
- search_documents: `Tripi Partner doanh nghiệp nào` → p85, p85, p47, p47, p47

> **[sach-trang-tmdt-2023:p085:B00]** 4.4. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn
STT Website/ứng dụng Tên doanh nghiệp
1 Traveloka Công ty TNHH Traveloka Việt Nam
2 Gotadi Công ty Cổ phần Công nghệ du lịch Gotadi
3 Tripi Partner Công ty Cổ phần du lịch Việt Nam Vntravel
4 Travellink.vn Công ty Cổ phần Công nghệ và Truyền thông VNLINK
5 Onedanang.vn Công ty TNHH Truyền Thông và Công nghệ One Office

## u05 · table · có đáp án
**Câu hỏi:** Tỷ lệ website/ứng dụng TMĐT bán hàng và website/ứng dụng CCDV TMĐT có chính sách giải quyết tranh chấp, khiếu nại là bao nhiêu?
**Đáp án chuẩn:** Bán hàng 81,0%; CCDV 85,9%.  
**Evidence:** tr.75 — Bảng 5.3, hàng 'Chính sách giải quyết tranh chấp, khiếu nại'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 151.58s):** Tỷ lệ website/ứng dụng TMĐT bán hàng có chính sách giải quyết tranh chấp, khiếu nại là 81,0%, trong khi tỷ lệ của website/ứng dụng CCDV TMĐT là 85,9%. [sach-trang-tmdt-2023:p75:V1]
- search_documents: `tỷ lệ website/ứng dụng TMĐT bán hàng có chính sách giải quyết tranh chấp, khiếu nại` → p75, p75, p68, p76, p70
- search_documents: `tỷ lệ website/ứng dụng CCDV TMĐT có chính sách giải quyết tranh chấp, khiếu nại` → p75, p75, p26, p68, p79

> **[sach-trang-tmdt-2023:p75:V1]** [table] 5.3. Các chính sách, cơ chế hỗ trợ khách hàng
(Trang 75, giữa; đơn vị: %)
Chính sách bảo hành, bảo trì sản phẩm, dịch vụ | Website, ứng dụng TMĐT bán hàng: 77,3% | Website, ứng dụng CCDV TMĐT: 74,1%
Chính sách đổi trả hàng và hoàn tiền | Website, ứng dụng TMĐT bán hàng: 77,1% | Website, ứng dụng CCDV TMĐT: 77,5%
Chính sách giải quyết tranh chấp, khiếu nại | Website, ứng dụng TMĐT bán hàng: 81,0% | Website, ứng dụng CCDV TMĐT: 85,9%
Chính sách bảo vệ thông tin cá nhân | Website, ứng dụng TMĐT bán hàng: 91,5% | Website, ứng dụng CCDV TMĐT: 93,4%
Cơ chế và quy trình rà soát và kiểm duyệt thông tin | Website, ứng dụng TMĐT bán hàng: 79,0% | Website, ứng dụng CCDV TMĐT: 86,5%
Cơ chế cho p

## u06 · table · có đáp án
**Câu hỏi:** Trên website, ứng dụng TMĐT bán hàng, tỷ lệ đơn hàng được thanh toán bằng tiền mặt (COD) là bao nhiêu?
**Đáp án chuẩn:** 50,6%.  
**Evidence:** tr.72 — Bảng 4.1 Tỷ lệ đơn hàng được thanh toán qua các hình thức, hàng 'Website, ứng dụng TMĐT bán hàng', cột 'Tiền mặt (COD)'
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 134.19s):** Tỷ lệ đơn hàng được thanh toán bằng tiền mặt (COD) trên website, ứng dụng thương mại điện tử bán hàng là 50,6% trong năm 2023. [sach-trang-tmdt-2023:p072:B00] [sach-trang-tmdt-2023:p72:V1]
- search_documents: `tỷ lệ đơn hàng thanh toán bằng tiền mặt COD` → p72, p72, p64, p73, p47

> **[sach-trang-tmdt-2023:p072:B00]** 4. Thanh toán
4.1. Tỷ lệ đơn hàng được thanh toán qua các hình thức
Ti ền | Th ẻ | Th ẻ | Hìn | h
mặt | Ví điện | th an h | Mob | il e | th ức
(C OD | ) | tử | toán nộ | i toán | Mon | ey | kh ác
địa | quốc | tế
Website, ứng dụng | 50,6 | % | 2,8% | 3,1% | 2,8% | 1,4%
TMĐT bán hàng
Website, ứng dụng
CCDV TMĐT | 46,3 | % | 31,7 | % | 7,5% | 3,6% | 0,7%

> **[sach-trang-tmdt-2023:p72:V1]** [table] 4.1. Tỷ lệ đơn hàng được thanh toán qua các hình thức
(Trang 72, giữa; đơn vị: %)
Tiền mặt (COD) | cột1: 50,6 | cột2: 46,3
Internet banking | cột1: 34,1 | cột2: 31,7
Ví điện tử | cột1: 2,8 | cột2: 7,5
Thẻ thanh toán nội địa | cột1: 3,1 | cột2: 4,6
Thẻ thanh toán quốc tế | cột1: 2,8 | cột2: 3,6
Mobile Money | cột1: 1,4 | cột2: 0,7
Hình thức khác | cột1: 5,2 | cột2: 5,6

## u07 · image · có đáp án
**Câu hỏi:** Theo sơ đồ quyền của chủ thể dữ liệu trong Nghị định 13/2023/NĐ-CP, quyền số 7 là quyền gì?
**Đáp án chuẩn:** Quyền cung cấp dữ liệu.  
**Evidence:** tr.21 — Sơ đồ khối '2 Quyền của chủ thể dữ liệu', ô số 7 (cột phải, ô đầu)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 140.13s):** Quyền số 7 trong Nghị định 13/2023/NĐ-CP là "Quyền yêu cầu bồi thường thiệt hại". [sach-trang-tmdt-2023:p021:B00]
- search_documents: `quyền số 7 Nghị định 13/2023/NĐ-CP` → p21, p20, p23, p23, p89

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

## u08 · image · có đáp án
**Câu hỏi:** Theo sơ đồ điều kiện kinh doanh dịch vụ tin cậy, điều kiện thứ nhất là gì?
**Đáp án chuẩn:** Là doanh nghiệp được thành lập và hoạt động hợp pháp trên lãnh thổ Việt Nam.  
**Evidence:** tr.15 — Sơ đồ khối mục 2 'Điều kiện kinh doanh dịch vụ tin cậy', ô số 1
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 71.85s):** Điều kiện thứ nhất trong sơ đồ điều kiện kinh doanh dịch vụ tin cậy là "Là doanh nghiệp được thành lập và hoạt động hợp pháp trên lãnh thổ Việt Nam". [sach-trang-tmdt-2023:p015:B00]
- search_documents: `sơ đồ điều kiện kinh doanh dịch vụ tin cậy` → p15, p16, p16, p14, p14

> **[sach-trang-tmdt-2023:p015:B00]** 2. Luật Giao dịch điện tử (sửa đổi)
1
1
3
3
5
2
2
4
4
2
3
Điều kiện kinh doanh dịch vụ tin cậy
Trách nhiệm của tổ chức cung cấp dịch vụ tin cậy
Là doanh nghiệp được thành lập và hoạt động hợp pháp trên lãnh thổ Việt Nam;
Công bố công khai quy trình đăng ký sử dụng dịch vụ, các biểu mẫu và chi phí liên quan;
Đáp ứng điều kiện tài chính, nhân lực quản lý và kỹ thuật phù hợp với từng loại hình
dịch vụ tin cậy;
Bảo đảm kênh tiếp nhận thông tin và cung cấp dịch vụ liên tục 24 giờ trong ngày và
07 ngày trong tuần;
Có phương án kỹ thuật phục vụ hoạt động cung cấp dịch vụ phù hợp với từng loại dịch
vụ tin cậy;
Bảo đảm trang thiết bị trong hệ thống thông tin được cấp mã quản lý, sẵn sàng kết nối
kỹ t

## u09 · image · có đáp án
**Câu hỏi:** Theo infographic về nguồn nhân lực cho TMĐT, bao nhiêu phần trăm doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT?
**Đáp án chuẩn:** 65%.  
**Evidence:** tr.57 — Infographic mục 2. Nguồn nhân lực cho TMĐT (ô '65%')
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 58.72s):** 65% doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT. [sach-trang-tmdt-2023:p57:V1]
- search_documents: `nguồn nhân lực cho TMĐT phần trăm doanh nghiệp ưu tiên tuyển dụng nhân sự đào tạo CNTT và TMĐT` → p57, p57, p55, p56, p56

> **[sach-trang-tmdt-2023:p57:V1]** [infographic] 2. Nguồn nhân lực cho thương mại điện tử
(Trang 57, nửa trên; đơn vị: %)
65% | doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT

## u10 · image · có đáp án
**Câu hỏi:** Năm 2023 có bao nhiêu website/ứng dụng đã được xác nhận đăng ký trên Cổng thông tin quản lý hoạt động TMĐT và tăng bao nhiêu phần trăm so với năm 2022?
**Đáp án chuẩn:** 1.218 website/ứng dụng, tăng 1,1%.  
**Evidence:** tr.26 — Infographic khối thứ ba (biểu tượng huy hiệu), dòng 2
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 124.82s):** Năm 2023, có 1.218 website/ứng dụng đã được xác nhận đăng ký trên Cổng thông tin quản lý hoạt động TMĐT, tăng 1,1% so với năm 2022. [sach-trang-tmdt-2023:p26:V1]
- search_documents: `website ứng dụng đăng ký Cổng thông tin quản lý hoạt động TMĐT 2023` → p70, p26, p68, p69, p76
- search_documents: `tăng phần trăm website ứng dụng đăng ký Cổng thông tin quản lý hoạt động TMĐT 2023 so với 2022` → p26, p70, p68, p69, p76
- read_page: `page 26` → p26, p26, p26, p26
- read_page: `page 70` → p70, p70, p70, p70

> **[sach-trang-tmdt-2023:p26:V1]** [infographic] Số lượng phản ánh, khiếu nại trên Cổng thông tin quản lý hoạt động TMĐT năm 2023
(Trang 26, nửa trên; đơn vị: tài khoản/hồ sơ/website)
76.255 tài khoản doanh nghiệp | tăng 16,4% so với năm 2022
26.250 tài khoản cá nhân | tăng 10,8% so với năm 2022
105.103 hồ sơ thông báo | tăng 12,1% so với năm 2022
9.604 hồ sơ đăng ký | tăng 14,3% so với năm 2022
48.348 website/ứng dụng đã được xác nhận thông báo | tăng 6,7% so với năm 2022
1.218 website/ứng dụng đã được xác nhận đăng ký | tăng 1,1% so với năm 2022

## u11 · image · có đáp án
**Câu hỏi:** Theo infographic hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu, bao nhiêu phần trăm người dùng sử dụng dịch vụ so sánh giá trực tuyến?
**Đáp án chuẩn:** 23,5%.  
**Evidence:** tr.29 — Infographic 1.4 (nửa dưới trang), dòng thứ 3
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 70.15s):** 23,5% người dùng Internet toàn cầu sử dụng dịch vụ so sánh giá trực tuyến. [sach-trang-tmdt-2023:p29:V2]
- search_documents: `hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu dịch vụ so sánh giá trực tuyến` → p29, p29, p30, p30, p44

> **[sach-trang-tmdt-2023:p29:V2]** [infographic] 1.4. Hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu
(Trang 29, nửa dưới; đơn vị: %)
57,6% | người dùng Internet có mua hàng hóa hoặc dịch vụ trực tuyến
14,2% | người dùng Internet mua hàng đã qua sử dụng
23,5% | người dùng Internet sử dụng dịch vụ so sánh giá trực tuyến
18,4% | người dùng Internet sử dụng dịch vụ mua ngay trả sau

## u12 · chart · có đáp án
**Câu hỏi:** Quốc gia nào có tỷ lệ TMĐT bán lẻ (doanh thu TMĐT B2C so với tổng doanh thu bán lẻ) lớn nhất toàn cầu năm 2022 và tỷ lệ là bao nhiêu?
**Đáp án chuẩn:** Trung Quốc, 46,3%.  
**Evidence:** tr.32 — Biểu đồ thanh ngang 2.5 Top 10 quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất 2022, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 64.15s):** Quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất toàn cầu năm 2022 là Trung Quốc với tỷ lệ 46,3%. [sach-trang-tmdt-2023:p32:V2]
- search_documents: `tỷ lệ TMĐT bán lẻ toàn cầu 2022` → p32, p31, p32, p31, p30

> **[sach-trang-tmdt-2023:p32:V2]** [bar_chart] 2.5. Top 10 quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất toàn cầu năm 2022
(Trang 32, nửa dưới; đơn vị: %)
Trung Quốc — 2022: 46,3% | Vương quốc Anh — 2022: 36,3% | Hàn Quốc — 2022: 32,2% | Đan Mạch — 2022: 20,2% | Indonesia — 2022: 20,2% | Na Uy — 2022: 19,4% | Mỹ — 2022: 16,1% | Phần Lan — 2022: 14,6% | Thụy Điển — 2022: 14,1% | Canada — 2022: 13,6% (Doanh thu TMĐT B2C so với Tổng doanh thu bán lẻ)

## u13 · chart · có đáp án
**Câu hỏi:** Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến là gì và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Mua hàng tại cửa hàng thuận tiện hơn, 40%.  
**Evidence:** tr.52 — Biểu đồ thanh ngang 4. Lý do chưa mua sắm trực tuyến, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 57.75s):** Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến là "Mua hàng tại cửa hàng thuận tiện hơn", chiếm 40%. [sach-trang-tmdt-2023:p052:B01]
- search_documents: `Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến` → p52, p52, p44, p51, p44

> **[sach-trang-tmdt-2023:p052:B01]** 4. Lý do chưa mua sắm trực tuyến
Mua hàng tại cửa hàng thuận tiện hơn | 40%
Sợ lộ thông tin cá nhân | 29%
Khó kiểm định chất lượng hàng hóa | 29%
Không tin tưởng đơn vị bán hàng | 24%
Hàng hóa, dịch vụ không phong phú | 18%
Không có các loại thẻ thanh toán | 15%
Chưa có kinh nghiệm mua bán trên mạng | 15%
Không có nhu cầu mua bán | 14%
Cách thức đặt hàng trực tuyến quá rắc rối | 13%
Không có đủ thông tin để ra quyết định | 11%
(Tỷ lệ người tiêu dùng chưa mua sắm trực tuyến)

## u14 · chart · có đáp án
**Câu hỏi:** Cách thức tìm kiếm thông tin phổ biến nhất của người tiêu dùng khi mua hàng trực tuyến là gì và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Bạn bè, người thân giới thiệu trực tiếp, 53%.  
**Evidence:** tr.44 — Biểu đồ thanh ngang 3. Cách thức tìm kiếm thông tin khi mua hàng trực tuyến, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 57.34s):** Cách thức tìm kiếm thông tin phổ biến nhất của người tiêu dùng khi mua hàng trực tuyến là "Bạn bè, người thân giới thiệu trực tiếp" với tỷ lệ 53%. Các cách thức khác bao gồm "Xem bình luận, đánh giá trên mạng" (52%) và "Qua quảng cáo trực tuyến" (52%). [sach-trang-tmdt-2023:p44:V3]
- search_documents: `cách thức tìm kiếm thông tin phổ biến nhất của người tiêu dùng khi mua hàng trực tuyến` → p44, p44, p51, p52, p52

> **[sach-trang-tmdt-2023:p44:V3]** [bar_chart] 3. Cách thức tìm kiếm thông tin khi mua hàng trực tuyến
(Trang 44, nửa dưới; đơn vị: %)
Bạn bè, người thân giới thiệu trực tiếp — 2023: 53% | Xem bình luận, đánh giá trên mạng — 2023: 52% | Qua quảng cáo trực tuyến — 2023: 52% | Xem quảng cáo truyền thống — 2023: 38% | Website/ứng dụng đã thông báo/đăng ký với Bộ Công Thương — 2023: 15% | Khác — 2023: 2% (Tỷ lệ người tiêu dùng trực tuyến)

## u15 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài thay đổi thế nào từ năm 2021 đến năm 2023?
**Đáp án chuẩn:** Giảm dần: 43% (2021), 35% (2022), 28% (2023); giảm 15 điểm phần trăm.  
**Evidence:** tr.49 — Biểu đồ cột 11. Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài (3 cột 2021–2023)
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 114.83s):** Tỷ lệ người tiêu dùng mua hàng qua các website thương mại điện tử nước ngoài đã giảm từ 43% năm 2021 xuống 35% năm 2022 và tiếp tục giảm xuống 28% năm 2023. Cụ thể:  
- Năm 2021: 43%  
- Năm 2022: 35%  
- Năm 2023: 28%  
Ngoài ra, tỷ lệ mua hàng trực tiếp trên website quốc tế cũng giảm từ 56% năm 2021 xuống 50% năm 2023, trong khi tỷ lệ mua qua website Việt Nam và qua người bán trung gian trên mạng xã hội cũng có xu hướng giảm trong cùng thời gian này. [sach-trang-tmdt-2023:p049:B00] [sach-trang-tmdt-2023:p49:V1]
- search_documents: `tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài 2021 2023` → p49, p49, p49, p49, p50
- search_documents: `thay đổi tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài 2021 2023` → p49, p49, p49, p49, p49

> **[sach-trang-tmdt-2023:p049:B00]** 11. Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài
43% | 2021
35% | 2022
28%
2023
Người tiêu dùng mua hàng qua các các website nước ngoài
11.1. Các hình thức mua hàng từ website TMĐT nước ngoài
56% | 59%
50% | 47% | 50%
41% | 41% | 44%
37% | 2021
2022
2023
Trực tiếp trên | Thông qua | Thông qua người bán
website quốc tế | website Việt Nam | trung gian trên mạng
mua hộ hàng quốc tế | xã hội

> **[sach-trang-tmdt-2023:p49:V1]** [bar_chart] 11. Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài
(Trang 49, nửa trên; đơn vị: %)
2021: 43% | 2022: 35% | 2023: 28%

## u16 · chart · có đáp án
**Câu hỏi:** Phương thức thanh toán nào được doanh nghiệp sử dụng phổ biến thứ hai và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Chuyển khoản Internet banking, 87% (sau thanh toán tiền mặt 88%).  
**Evidence:** tr.64 — Biểu đồ thanh ngang 3. Phương thức thanh toán mà doanh nghiệp đang sử dụng, thanh thứ hai
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 49.13s):** Phương thức thanh toán phổ biến thứ hai được doanh nghiệp sử dụng là "Chuyển khoản Internet banking" với tỷ lệ 87%. [sach-trang-tmdt-2023:p64:V3]
- search_documents: `phương thức thanh toán phổ biến thứ hai` → p47, p47, p64, p47, p72

> **[sach-trang-tmdt-2023:p64:V3]** [table] 3. Phương thức thanh toán mà doanh nghiệp đang sử dụng
(Trang 64, nửa dưới; đơn vị: %)
Thanh toán tiền mặt | 88% | | Chuyển khoản Internet banking | 87% | | Ví điện tử | 22% | | Thẻ thanh toán nội địa | 15% | | Thẻ thanh toán quốc tế | 12% | | Tài khoản mobile, SMS | 9% | | Thanh toán qua mobile money | 6% | | Phương thức khác | 1% |

## u17 · multihop · có đáp án
**Câu hỏi:** Năm 2023, bao nhiêu phần trăm người dùng truy cập Internet bằng điện thoại di động, và bao nhiêu phần trăm sử dụng điện thoại di động để đặt hàng trực tuyến?
**Đáp án chuẩn:** 90% người dùng truy cập Internet bằng điện thoại di động (tr. 42); 91% dùng điện thoại di động để đặt hàng trực tuyến (tr. 45).  
**Evidence:** tr.42 — Biểu đồ cột 1. Phương tiện truy cập Internet, nhóm 'Điện thoại di động', cột 2023; tr.45 — Biểu đồ cột 4. Phương tiện điện tử thường được sử dụng để đặt hàng trực tuyến, nhóm 'Điện thoại di động', cột 2023
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 108.16s):** Năm 2023, 90% người dùng truy cập Internet bằng điện thoại di động và 91% sử dụng điện thoại di động để đặt hàng trực tuyến. [sach-trang-tmdt-2023:p42:V1] [sach-trang-tmdt-2023:p45:V1]
- search_documents: `2023 phần trăm người dùng truy cập Internet bằng điện thoại di động` → p42, p45, p42, p42, p43
- search_documents: `2023 phần trăm sử dụng điện thoại di động để đặt hàng trực tuyến` → p45, p45, p46, p46, p68
- read_page: `page 42` → p42, p42, p42, p42, p42
- read_page: `page 45` → p45, p45, p45, p45

> **[sach-trang-tmdt-2023:p42:V1]** [bar_chart] 1. Phương tiện truy cập Internet của người dân
(Trang 42, nửa trên; đơn vị: Tỷ lệ (%))
Máy tính để bàn — 2022: 63%; 2023: 50%
Điện thoại di động — 2022: 94%; 2023: 90%
Thiết bị khác (Ipad, Máy tính bảng) — 2022: 14%; 2023: 10%

> **[sach-trang-tmdt-2023:p45:V1]** [bar_chart] 4. Phương tiện điện tử thường được sử dụng để đặt hàng trực tuyến
(Trang 45, nửa trên; đơn vị: Tỷ lệ người dùng Internet)
Điện thoại di động — 2022: 91% | Điện thoại di động — 2023: 91% | Máy tính để bàn — 2022: 46% | Máy tính để bàn — 2023: 46% | Máy tính xách tay — 2022: 18% | Máy tính xách tay — 2023: 13% | Thiết bị khác (Ipad, Máy tính bảng) — 2022: 5% | Thiết bị khác (Ipad, Máy tính bảng) — 2023: 5%

## u18 · multihop · có đáp án
**Câu hỏi:** Sàn giao dịch TMĐT bán buôn bán lẻ nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành sàn này theo danh sách doanh nghiệp dẫn đầu thị trường?
**Đáp án chuẩn:** Shopee, 81%; do Công ty TNHH Shopee vận hành.  
**Evidence:** tr.46 — Biểu đồ cột 6.1, cột Shopee; tr.83 — Bảng 4.1 STT 6 / bảng 4.2 STT 5
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 40.74s):** Sàn giao dịch TMĐT bán buôn bán lẻ được người tiêu dùng ưa chuộng nhất là Shopee với tỷ lệ 81%. Doanh nghiệp vận hành sàn này là Công ty TNHH Shopee. [sach-trang-tmdt-2023:p46:V2]
- search_documents: `sàn giao dịch TMĐT bán buôn bán lẻ ưa chuộng nhất tỷ lệ doanh nghiệp dẫn đầu thị trường` → p83, p46, p83, p83, p46

> **[sach-trang-tmdt-2023:p46:V2]** [bar_chart] 6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng
(Trang 46, giữa; đơn vị: (%))
Shopee — năm: 2023: 81%
Lazada — năm: 2023: 42%
TikTok — năm: 2023: 34%
Tiki — năm: 2023: 20%
Sendo — năm: 2023: 8%
Khác — năm: 2023: 2%

## u19 · multihop · có đáp án
**Câu hỏi:** Doanh thu bán lẻ TMĐT của khu vực Bắc Mỹ năm 2022 là bao nhiêu, và Mỹ chiếm bao nhiêu phần trăm thị phần TMĐT toàn cầu năm 2022?
**Đáp án chuẩn:** Bắc Mỹ 1.144,99 tỷ USD; Mỹ chiếm 19,2% thị phần TMĐT toàn cầu.  
**Evidence:** tr.31 — Biểu đồ thanh ngang 2.3 Doanh thu bán lẻ TMĐT toàn cầu theo khu vực 2022, thanh 'Bắc Mỹ'; tr.32 — Biểu đồ thanh ngang 2.4 Top 12 quốc gia chiếm thị phần TMĐT lớn nhất 2022, thanh 'Mỹ'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 86.63s):** Doanh thu bán lẻ TMĐT của khu vực Bắc Mỹ năm 2022 là 1.144,99 tỷ USD. Mỹ chiếm 19,2% thị phần TMĐT toàn cầu năm 2022. [sach-trang-tmdt-2023:p31:V2]
- search_documents: `Doanh thu bán lẻ TMĐT Bắc Mỹ 2022` → p31, p31, p31, p31, p30
- search_documents: `Mỹ thị phần TMĐT toàn cầu 2022` → p32, p31, p31, p32, p31

> **[sach-trang-tmdt-2023:p31:V2]** [table] 2.3. Doanh thu bán lẻ TMĐT toàn cầu, chia theo khu vực năm 2022
(Trang 31, nửa dưới; đơn vị: tỷ USD)
Châu Á - Thái Bình Dương | 3.323,19 |  | Bắc Mỹ | 1.144,99 |  | Tây Âu | 694,59 |  | Châu Mỹ Latin | 167,81 |  | Trung & Đông Âu | 141,90 |  | Đông Nam Á | 89,67 |  | Trung Đông và Châu Phi | 69,39 |

## u20 · multihop · có đáp án
**Câu hỏi:** Sàn TMĐT giao đồ ăn nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành sàn này theo danh sách doanh nghiệp dẫn đầu thị trường giao đồ ăn?
**Đáp án chuẩn:** ShopeeFood/Foody, 51%; do Công ty Cổ phần Foody vận hành.  
**Evidence:** tr.47 — Biểu đồ cột 6.3, cột 'ShopeeFood, Foody'; tr.84 — Bảng 4.4 Nhóm doanh nghiệp dẫn đầu dịch vụ giao đồ ăn, STT 4; tr.83 — Bảng 4.1, STT 7 (evidence thay thế cho tên doanh nghiệp)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 35.92s):** Sàn TMĐT giao đồ ăn được người tiêu dùng ưa chuộng nhất là ShopeeFood và Foody với tỷ lệ 51%. Doanh nghiệp vận hành sàn này là Công ty Cổ phần Foody. [sach-trang-tmdt-2023:p47:V1]
- search_documents: `sàn TMĐT giao đồ ăn ưa chuộng nhất tỷ lệ doanh nghiệp dẫn đầu thị trường` → p47, p84, p84, p85, p47

> **[sach-trang-tmdt-2023:p47:V1]** [bar_chart] 6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng
(Trang 47, nửa trên; đơn vị: Tỷ lệ người dùng Internet)
ShopeeFood, Foody — năm: 51%
Grab — năm: 50%
Baemin — năm: 15%
Be — năm: 7%
Khác — năm: 13%

## u21 · text · có đáp án
**Câu hỏi:** Theo Lời giới thiệu, tốc độ tăng trưởng TMĐT của Việt Nam được xếp vào nhóm bao nhiêu quốc gia dẫn đầu thế giới, theo nguồn nào?
**Đáp án chuẩn:** Nhóm 10 quốc gia có tốc độ tăng trưởng TMĐT hàng đầu thế giới, tính đến tháng 12/2023 theo Statista.  
**Evidence:** tr.3 — Lời giới thiệu, đoạn 2
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 40.78s):** Tốc độ tăng trưởng thương mại điện tử của Việt Nam được xếp vào nhóm 10 quốc gia có tốc độ tăng trưởng thương mại điện tử hàng đầu thế giới (tính đến tháng 12/2023 theo Statista). [sach-trang-tmdt-2023:p003:B00]
- search_documents: `tốc độ tăng trưởng TMĐT của Việt Nam nhóm quốc gia dẫn đầu thế giới Lời giới thiệu` → p3, p40, p32, p37, p32

> **[sach-trang-tmdt-2023:p003:B00]** LỜI GIỚI THIỆU
Kinh tế Việt Nam 2023 duy trì xu hướng phục hồi, tiếp tục là điểm sáng của kinh tế toàn cầu (theo Cổng
Thông tin điện tử Chính phủ). Kinh tế vĩ mô cơ bản ổn định; lạm phát thấp hơn mục tiêu Quốc hội đề ra; nợ
công, nợ Chính phủ, nợ nước ngoài, bội chi ngân sách nhà nước được kiểm soát; tăng trưởng được thúc đẩy;
các cân đối lớn của nền kinh tế được bảo đảm. Tăng trưởng GDP cả năm khoảng 5% thuộc nhóm các nước tăng
trưởng cao trong khu vực và thế giới.
Trong bức tranh tổng thể về kinh tế Việt Nam, thương mại điện tử tiếp tục khẳng định vị trí là một trong
những lĩnh vực tiên phong của nền kinh tế số. Năm 2023, quy mô thị trường thương mại điện tử bán lẻ Việt
Nam đạt 20,5 tỷ USD

## u22 · text · có đáp án
**Câu hỏi:** Theo Nghị định 13/2023/NĐ-CP, thông tin về tài khoản số của cá nhân thuộc loại dữ liệu cá nhân nào?
**Đáp án chuẩn:** Dữ liệu cá nhân cơ bản.  
**Evidence:** tr.20 — Khối '1 Phân loại dữ liệu cá nhân', cột 'Dữ liệu cá nhân cơ bản'
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 36.15s):** Thông tin về tài khoản số của cá nhân thuộc loại dữ liệu cá nhân cơ bản theo Nghị định 13/2023/NĐ-CP. [sach-trang-tmdt-2023:p020:B00]
- search_documents: `Nghị định 13/2023/NĐ-CP tài khoản số cá nhân dữ liệu cá nhân` → p20, p23, p20, p22, p23

> **[sach-trang-tmdt-2023:p020:B00]** 4. Nghị định số 13/2023/NĐ-CP ngày 17 tháng 4 năm 2023 của Chính phủ
Nghị định 13/2023/NĐ-CP quy định về bảo vệ dữ liệu cá nhân và trách nhiệm bảo vệ dữ liệu cá nhân của
cơ quan, tổ chức, cá nhân có liên quan.
1 Phân loại dữ liệu cá nhân
Dữ liệu cá nhân cơ bản Dữ liệu cá nhân nhạy cảm
Họ, chữ đệm và tên khai sinh, tên gọi khác (nếu có);
Ngày, tháng, năm sinh; ngày, tháng, năm chết hoặc
mất tích;
Giới tính;
Quốc tịch;
Hình ảnh của cá nhân;
Tình trạng hôn nhân;
Thông tin về mối quan hệ gia đình (cha mẹ, con cái);
Thông tin về tài khoản số của cá nhân; dữ liệu cá
nhân phản ánh hoạt động, lịch sử hoạt động trên
không gian mạng;
Các thông tin khác gắn liền với một con người cụ
thể hoặc giúp xác đ

## u23 · text · có đáp án
**Câu hỏi:** Theo Chỉ thị 18/CT-TTg, thẻ Căn cước công dân gắn chíp hoặc dữ liệu dân cư được ứng dụng để xác thực chủ thể hoạt động TMĐT khi giao kết hợp đồng trên nền tảng nào?
**Đáp án chuẩn:** Trên Trục phát triển hợp đồng điện tử Việt Nam.  
**Evidence:** tr.25 — Mục '2. Một số giải pháp' của Chỉ thị 18/CT-TTg, gạch đầu dòng 5
**auto:** context đủ evidence = True
**Agent (abstain, 1 tool call, 27.47s):** Không đủ bằng chứng để trả lời.
- search_documents: `Chỉ thị 18/CT-TTg thẻ Căn cước công dân gắn chíp dữ liệu dân cư xác thực chủ thể hoạt động TMĐT` → p25, p24, p16, p16, p12
- abstain: Không tìm thấy thông tin chính xác về ứng dụng xác thực chủ thể hoạt động thương mại điện tử trong tài liệu.

## u24 · text · có đáp án
**Câu hỏi:** Theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi), tổ chức vận hành nền tảng số trung gian phải cung cấp thông tin về tổ chức, cá nhân kinh doanh trên nền tảng trong trường hợp nào?
**Đáp án chuẩn:** Khi người tiêu dùng giao dịch với tổ chức, cá nhân kinh doanh đó có yêu cầu.  
**Evidence:** tr.11 — Khối '3 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian', ô số 4
**auto:** context đủ evidence = True
**Agent (abstain, 1 tool call, 51.38s):** Không đủ bằng chứng để trả lời.
- search_documents: `Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) tổ chức vận hành nền tảng số trung gian cung cấp thông tin` → p12, p11, p11, p10, p13
- abstain: Không có thông tin đầy đủ và chính xác về yêu cầu cung cấp thông tin của tổ chức vận hành nền tảng số trung gian trong tài liệu.

## u25 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Mỹ là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.5 (tr. 30) chỉ có Thái Lan, Hàn Quốc, Indonesia, Ấn Độ, Trung Quốc, Malaysia, Singapore, Philippines, Việt Nam, Úc và trung bình toàn cầu; 'Mỹ' chỉ xuất hiện ở tr. 31–33 (doanh thu, thị phần).
**Agent (abstain, 1 tool call, 13.45s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần Mỹ` → p29, p29, p30, p30, p44
- abstain: Tài liệu không chứa thông tin về tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Mỹ.

## u26 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Quy mô nền kinh tế Internet của Campuchia năm 2023 là bao nhiêu tỷ USD?
**Lý do thiếu:** Biểu đồ 2 (tr. 34) chỉ có Indonesia, Thái Lan, Việt Nam, Philippines, Malaysia, Singapore; 'Campuchia' không xuất hiện trong toàn văn.
**Agent (abstain, 1 tool call, 21.54s):** Không đủ bằng chứng để trả lời.
- search_documents: `quy mô nền kinh tế Internet Campuchia 2023` → p34, p34, p34, p34, p30
- abstain: Không có thông tin về quy mô nền kinh tế Internet của Campuchia năm 2023 trong tài liệu.

## u27 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Bao nhiêu phần trăm người tiêu dùng ưa chuộng Tiki trong lĩnh vực dịch vụ giao đồ ăn?
**Lý do thiếu:** Biểu đồ 6.3 (tr. 47) chỉ có ShopeeFood/Foody, Grab, Baemin, Be, Khác; Tiki chỉ có ở biểu đồ bán buôn bán lẻ (tr. 46, 20%) và bảng doanh nghiệp (tr. 83).
**Agent (abstain, 1 tool call, 17.71s):** Không đủ bằng chứng để trả lời.
- search_documents: `Tiki dịch vụ giao đồ ăn phần trăm người tiêu dùng ưa chuộng` → p47, p47, p47, p46, p46
- abstain: Tài liệu không chứa thông tin về tỷ lệ phần trăm người tiêu dùng ưa chuộng Tiki trong lĩnh vực dịch vụ giao đồ ăn.

## u28 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Năm 2023, các website TMĐT bán hàng tại Việt Nam xử lý tổng cộng bao nhiêu triệu đơn hàng thành công?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ % đơn hàng thành công theo tỉnh/thành (tr. 77, 82) và theo người bán (tr. 80); không có số đơn hàng tuyệt đối ('triệu đơn' không xuất hiện).
**Agent (answered, 3 tool call, 49.07s):** Năm 2023, các website thương mại điện tử bán hàng tại Việt Nam xử lý tổng cộng 61 triệu đơn hàng thành công. [sach-trang-tmdt-2023:p40:V2]
- search_documents: `2023 tổng số đơn hàng thành công Việt Nam` → p77, p82, p40, p77, p82
- search_documents: `2023 tổng số đơn hàng TMĐT Việt Nam` → p77, p40, p3, p40, p40
- read_page: `page 40` → p40, p40, p40

> **[sach-trang-tmdt-2023:p40:V2]** [table] Doanh thu TMĐT B2C Việt Nam năm 2018 – 2023
(Trang 40, nửa dưới; đơn vị: không ghi)
Ước tính số lượng người tiêu dùng mua sắm trực tuyến (triệu người) | 2018: 39,9 | 2019: 44,8 | 2020: 49,3 | 2021: 54,6 | 2022: 57,0 | 2023: 61
Ước tính giá trị mua sắm trực tuyến của một người (USD) | 2018: 202 | 2019: 225 | 2020: 240 | 2021: 251 | 2022: 288 | 2023: 336
Tỷ trọng doanh thu TMĐT B2C so với tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng cả nước | 2018: 4,2% | 2019: 4,9% | 2020: 5,5% | 2021: 7% | 2022: 7,5% | 2023: 8%
Tỷ lệ người dân sử dụng Internet | 2018: 60% | 2019: 66% | 2020: 70% | 2021: 73% | 2022: 73,2% | 2023: 78,6%

## u29 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho năm 2023 là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.1 (tr. 55) chỉ có phần mềm quản lý nhân sự, chuỗi cung ứng, chăm sóc khách hàng, quản trị doanh nghiệp; 'quản lý kho' không xuất hiện.
**Agent (abstain, 1 tool call, 15.56s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho 2023` → p55, p55, p65, p56, p65
- abstain: Không tìm thấy thông tin cụ thể về tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho năm 2023.

## u30 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Mức lương trung bình của nhân sự làm thương mại điện tử tại Việt Nam năm 2023 là bao nhiêu?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ doanh nghiệp ưu tiên tuyển nhân sự đào tạo CNTT/TMĐT (tr. 57); 'lương' không xuất hiện trong toàn văn.
**Agent (abstain, 3 tool call, 43.28s):** Không đủ bằng chứng để trả lời.
- search_documents: `mức lương trung bình nhân sự thương mại điện tử Việt Nam 2023` → p3, p50, p57, p3, p50
- search_documents: `lương nhân sự thương mại điện tử Việt Nam 2023` → p3, p57, p50, p40, p40
- search_documents: `lương nhân sự thương mại điện tử` → p57, p57, p50, p91, p93
- abstain: Không tìm thấy thông tin về mức lương trung bình của nhân sự làm thương mại điện tử tại Việt Nam năm 2023.
