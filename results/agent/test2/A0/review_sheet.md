# Phiếu chấm A0 / test2

Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.


## u01 · table · có đáp án
**Câu hỏi:** Theo bảng số liệu thị trường TMĐT bán lẻ, tỷ lệ người dân Việt Nam sử dụng Internet năm 2020 là bao nhiêu?
**Đáp án chuẩn:** 70%.  
**Evidence:** tr.40 — Bảng dưới biểu đồ B2C, hàng 'Tỷ lệ người dân sử dụng Internet', cột 2020
**auto:** context đủ evidence = False
**Agent (abstain, 1 tool call, 25.27s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ người dân Việt Nam sử dụng Internet năm 2020` → p42, p42, p42
- abstain: Tài liệu không cung cấp thông tin về tỷ lệ người dân Việt Nam sử dụng Internet năm 2020.

## u02 · table · có đáp án
**Câu hỏi:** Trong danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu, website thegioididong.com thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần Thế Giới Di Động.  
**Evidence:** tr.78 — Bảng 4.1, STT 16
**auto:** context đủ evidence = False
**Agent (abstain, 4 tool call, 61.74s):** Không đủ bằng chứng để trả lời.
- search_documents: `thegioididong.com doanh nghiệp` → p84, p85, p79
- search_documents: `thegioididong.com doanh nghiệp` → p84, p85, p79
- search_documents: `doanh nghiệp thegioididong.com` → p85, p84, p83
- search_documents: `thegioididong.com` → p84, p85, p47
- abstain: Không tìm thấy thông tin về doanh nghiệp sở hữu website thegioididong.com trong tài liệu.

## u03 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ, Voso thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL.  
**Evidence:** tr.83 — Bảng 4.2, STT 10
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 7.19s):** Voso thuộc Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL. [sach-trang-tmdt-2023:p083:B01]
- search_documents: `Voso thuộc doanh nghiệp nào` → p84, p84, p83

> **[sach-trang-tmdt-2023:p083:B01]** 4.2. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ
STT Website/ứng dụng Tên doanh nghiệp
1 Lazada Công ty TNHH Recess
2 samsung.com.vn Công Ty TNHH Điện Tử Samsung Vina
3 Selly Công ty TNHH Selly
4 Sendo Công ty Cổ Phần Công Nghệ Sen Đỏ
5 Shopee Công ty TNHH Shopee
6 thuocsi.vn Công ty TNHH Buymed
7 Tiki Công ty TNHH TI KI
8 TIKTOK TIKTOK PTE. LTD.
9 VinShop Công ty cổ phần One Mount Distribution
10 Voso Công ty TNHH MTV Thương mại Điện tử Bưu Chính VIETTEL

## u04 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT du lịch trực tuyến, Tripi Partner thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần du lịch Việt Nam Vntravel.  
**Evidence:** tr.85 — Bảng 4.5, STT 3
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 19.58s):** Tripi Partner thuộc Công ty Cổ phần du lịch Việt Nam Vntravel. [sach-trang-tmdt-2023:p085:B00]
- search_documents: `Tripi Partner doanh nghiệp nào` → p85, p84, p83

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
**Agent (answered, 2 tool call, 30.21s):** Tỷ lệ website/ứng dụng TMĐT bán hàng có chính sách giải quyết tranh chấp, khiếu nại là 81,0%. Tỷ lệ website/ứng dụng CCDV TMĐT có chính sách giải quyết tranh chấp, khiếu nại là 85,9%. [sach-trang-tmdt-2023:p075:B00]
- search_documents: `tỷ lệ website/ứng dụng TMĐT bán hàng có chính sách giải quyết tranh chấp, khiếu nại` → p75, p26, p73
- search_documents: `tỷ lệ website/ứng dụng CCDV TMĐT có chính sách giải quyết tranh chấp, khiếu nại` → p75, p26, p73

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

## u06 · table · có đáp án
**Câu hỏi:** Trên website, ứng dụng TMĐT bán hàng, tỷ lệ đơn hàng được thanh toán bằng tiền mặt (COD) là bao nhiêu?
**Đáp án chuẩn:** 50,6%.  
**Evidence:** tr.72 — Bảng 4.1 Tỷ lệ đơn hàng được thanh toán qua các hình thức, hàng 'Website, ứng dụng TMĐT bán hàng', cột 'Tiền mặt (COD)'
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 26.7s):** Tỷ lệ đơn hàng được thanh toán bằng tiền mặt (COD) trên website, ứng dụng thương mại điện tử bán hàng là 50,6%. [sach-trang-tmdt-2023:p072:B00]
- search_documents: `tỷ lệ đơn hàng thanh toán bằng tiền mặt COD` → p72, p64, p47

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

## u07 · image · có đáp án
**Câu hỏi:** Theo sơ đồ quyền của chủ thể dữ liệu trong Nghị định 13/2023/NĐ-CP, quyền số 7 là quyền gì?
**Đáp án chuẩn:** Quyền cung cấp dữ liệu.  
**Evidence:** tr.21 — Sơ đồ khối '2 Quyền của chủ thể dữ liệu', ô số 7 (cột phải, ô đầu)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 13.59s):** Quyền số 7 trong Nghị định 13/2023/NĐ-CP là "Quyền yêu cầu bồi thường thiệt hại". [sach-trang-tmdt-2023:p021:B00]
- search_documents: `quyền số 7 Nghị định 13/2023/NĐ-CP` → p21, p20, p22

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
**Agent (answered, 1 tool call, 16.14s):** Điều kiện thứ nhất trong sơ đồ điều kiện kinh doanh dịch vụ tin cậy là: Doanh nghiệp được thành lập và hoạt động hợp pháp trên lãnh thổ Việt Nam. [sach-trang-tmdt-2023:p015:B00]
- search_documents: `sơ đồ điều kiện kinh doanh dịch vụ tin cậy` → p15, p16, p14

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
**Agent (answered, 1 tool call, 18.95s):** 65% doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT. [sach-trang-tmdt-2023:p057:B00]
- search_documents: `nguồn nhân lực cho TMĐT phần trăm doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT` → p57, p55, p56

> **[sach-trang-tmdt-2023:p057:B00]** 2. Nguồn nhân lực cho thương mại điện tử
65% | doanh nghiệp ưu tiên tuyển dụng nhân sự được đào tạo về CNTT và TMĐT
3. Tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023
80% | doanh nghiệp có sử dụng chữ ký điện tử
41% | doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch
22% | doanh nghiệp có sử dụng dịch vụ chứng thực hợp đồng điện tử

## u10 · image · có đáp án
**Câu hỏi:** Năm 2023 có bao nhiêu website/ứng dụng đã được xác nhận đăng ký trên Cổng thông tin quản lý hoạt động TMĐT và tăng bao nhiêu phần trăm so với năm 2022?
**Đáp án chuẩn:** 1.218 website/ứng dụng, tăng 1,1%.  
**Evidence:** tr.26 — Infographic khối thứ ba (biểu tượng huy hiệu), dòng 2
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 26.26s):** Năm 2023, có 1.218 website/ứng dụng đã được xác nhận đăng ký trên Cổng thông tin quản lý hoạt động TMĐT, tăng 1,1% so với năm 2022. (Năm 2022 có 1.204 website/ứng dụng được xác nhận đăng ký) [sach-trang-tmdt-2023:p026:B01].
- search_documents: `số lượng website ứng dụng đăng ký trên Cổng thông tin quản lý hoạt động TMĐT năm 2023` → p26, p26, p78
- search_documents: `tăng trưởng phần trăm số lượng website ứng dụng đăng ký năm 2023 so với 2022` → p26, p65, p71

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

## u11 · image · có đáp án
**Câu hỏi:** Theo infographic hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu, bao nhiêu phần trăm người dùng sử dụng dịch vụ so sánh giá trực tuyến?
**Đáp án chuẩn:** 23,5%.  
**Evidence:** tr.29 — Infographic 1.4 (nửa dưới trang), dòng thứ 3
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 11.62s):** 23,5% người dùng Internet toàn cầu sử dụng dịch vụ so sánh giá trực tuyến. [sach-trang-tmdt-2023:p029:B01]
- search_documents: `hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu dịch vụ so sánh giá trực tuyến` → p29, p48, p30

> **[sach-trang-tmdt-2023:p029:B01]** 1.4. Hoạt động mua sắm trực tuyến hàng tuần của người dùng Internet toàn cầu
57,6% | người dùng Internet có mua hàng hóa hoặc dịch vụ trực tuyến
người dùng Internet mua hàng đã qua sử dụng | 14,2%
23,5% | người dùng Internet sử dụng dịch vụ so sánh giá trực tuyến
người dùng Internet sử dụng dịch vụ mua ngay trả sau | 18,4%

## u12 · chart · có đáp án
**Câu hỏi:** Quốc gia nào có tỷ lệ TMĐT bán lẻ (doanh thu TMĐT B2C so với tổng doanh thu bán lẻ) lớn nhất toàn cầu năm 2022 và tỷ lệ là bao nhiêu?
**Đáp án chuẩn:** Trung Quốc, 46,3%.  
**Evidence:** tr.32 — Biểu đồ thanh ngang 2.5 Top 10 quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất 2022, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 10.94s):** Quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất toàn cầu năm 2022 là Trung Quốc với tỷ lệ 46,3%. [sach-trang-tmdt-2023:p032:B01]
- search_documents: `tỷ lệ TMĐT bán lẻ toàn cầu năm 2022` → p31, p31, p32

> **[sach-trang-tmdt-2023:p032:B01]** 2.5. Top 10 quốc gia có tỷ lệ TMĐT bán lẻ lớn nhất toàn cầu năm 2022
Tru ng Quố | c | 46,3%
Vươ | ngq | uốc | An h | 36,3%
Hàn Q | uố c | 32,2%
Đan M | ạc h | 20,2%
Indonesia | 20,2%
Na Uy | 19,4%
Mỹ | 16,1% | ( Doanh thu TMĐT B2C so với Tổng doanh thu bán lẻ )
Phần | L an | 14,6%
Thụy Đi | ển | 14,1%
Canada | 13,6%
Nguồn: Báo cáo “Global Ecommerce Forecast” - eMarketer

## u13 · chart · có đáp án
**Câu hỏi:** Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến là gì và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Mua hàng tại cửa hàng thuận tiện hơn, 40%.  
**Evidence:** tr.52 — Biểu đồ thanh ngang 4. Lý do chưa mua sắm trực tuyến, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 14.25s):** Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến là "Mua hàng tại cửa hàng thuận tiện hơn", chiếm 40%. [sach-trang-tmdt-2023:p052:B01]
- search_documents: `Lý do hàng đầu khiến người tiêu dùng chưa mua sắm trực tuyến` → p52, p52, p44

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
**Agent (answered, 1 tool call, 11.56s):** Cách thức tìm kiếm thông tin phổ biến nhất của người tiêu dùng khi mua hàng trực tuyến là thông qua bạn bè, người thân giới thiệu trực tiếp, chiếm 53%. Các cách thức khác bao gồm xem bình luận, đánh giá trên mạng (52%) và qua quảng cáo trực tuyến (52%). [sach-trang-tmdt-2023:p044:B01]
- search_documents: `cách thức tìm kiếm thông tin phổ biến nhất của người tiêu dùng khi mua hàng trực tuyến` → p44, p51, p29

> **[sach-trang-tmdt-2023:p044:B01]** 2. Tỷ lệ người dùng Internet tham gia mua sắm trực tuyến
78%
3. Cách thức tìm kiếm thông tin khi mua hàng trực tuyến
Bạn bè, người thân giới thiệu trực tiếp | 53%
Xem bình luận, đánh giá trên mạng | 52%
(Mạng xã hội /sàn TMĐT)
Qua quảng cáo trực tuyến | 52%
(mạng xã hội/công cụ tìm kiếm/email quảng cáo)
Xem quảng cáo truyền thống | 38%
(tivi /báo điện tử /báo giấy)
Website/ứng dụng đã thông báo/đăng ký với | 15%
Bộ Công Thương
Khác | 2% | (Tỷ lệ người tiêu dùng trực tuyến)

## u15 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài thay đổi thế nào từ năm 2021 đến năm 2023?
**Đáp án chuẩn:** Giảm dần: 43% (2021), 35% (2022), 28% (2023); giảm 15 điểm phần trăm.  
**Evidence:** tr.49 — Biểu đồ cột 11. Tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài (3 cột 2021–2023)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 21.96s):** Tỷ lệ người tiêu dùng mua hàng qua các website thương mại điện tử nước ngoài đã giảm từ 43% vào năm 2021 xuống 35% vào năm 2022 và tiếp tục giảm xuống còn 28% vào năm 2023. [sach-trang-tmdt-2023:p049:B00]
- search_documents: `tỷ lệ người tiêu dùng mua hàng qua các website TMĐT nước ngoài 2021 2023` → p49, p49, p50

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

## u16 · chart · có đáp án
**Câu hỏi:** Phương thức thanh toán nào được doanh nghiệp sử dụng phổ biến thứ hai và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Chuyển khoản Internet banking, 87% (sau thanh toán tiền mặt 88%).  
**Evidence:** tr.64 — Biểu đồ thanh ngang 3. Phương thức thanh toán mà doanh nghiệp đang sử dụng, thanh thứ hai
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 15.74s):** Phương thức thanh toán phổ biến thứ hai được doanh nghiệp sử dụng là "Chuyển Khoản", chiếm 60%. [sach-trang-tmdt-2023:p047:B03]
- search_documents: `phương thức thanh toán phổ biến thứ hai` → p47, p47, p47

> **[sach-trang-tmdt-2023:p047:B03]** 7. Hình thức thanh toán phổ biến
Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng — Tripi Partner: 9%
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng — AirBnB: 8%
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng — Khác: 16%
7. Hình thức thanh toán phổ biến — Tiền mặt khi nhận hàng: 76%
7. Hình thức thanh toán phổ biến — Chuyển Khoản: 60%
7. Hình thức thanh toán phổ biến — Thẻ ATM nội địa: 20%
7. Hình thức thanh toán phổ biến — Thẻ tín dụng thẻ ghi nợ: 14%
7. Hình thức thanh toán phổ biến — Ví điện tử: 21%
7. Hình thức thanh toán phổ biến — Mobile Money: 6%
7. Hình thức thanh toán phổ biến — Trả góp (mua trước 

## u17 · multihop · có đáp án
**Câu hỏi:** Năm 2023, bao nhiêu phần trăm người dùng truy cập Internet bằng điện thoại di động, và bao nhiêu phần trăm sử dụng điện thoại di động để đặt hàng trực tuyến?
**Đáp án chuẩn:** 90% người dùng truy cập Internet bằng điện thoại di động (tr. 42); 91% dùng điện thoại di động để đặt hàng trực tuyến (tr. 45).  
**Evidence:** tr.42 — Biểu đồ cột 1. Phương tiện truy cập Internet, nhóm 'Điện thoại di động', cột 2023; tr.45 — Biểu đồ cột 4. Phương tiện điện tử thường được sử dụng để đặt hàng trực tuyến, nhóm 'Điện thoại di động', cột 2023
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 24.71s):** Năm 2023, 90% người dùng truy cập Internet bằng điện thoại di động và 91% sử dụng điện thoại di động để đặt hàng trực tuyến. [sach-trang-tmdt-2023:p042:B02] [sach-trang-tmdt-2023:p045:B00]
- search_documents: `2023 phần trăm người dùng truy cập Internet bằng điện thoại di động` → p42, p42, p42
- search_documents: `2023 phần trăm sử dụng điện thoại di động để đặt hàng trực tuyến` → p45, p59, p46

> **[sach-trang-tmdt-2023:p042:B02]** 2. Thời gian truy cập Internet trung bình mỗi ngày
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1. Phương tiện truy cập Internet của người dân — Máy tính để bàn Máy tính xách tay: 2022: 63%; 2023: 50%
1. Phương tiện truy cập Internet của người dân — Điện thoại di động: 2022: 94%; 2023: 90%
1. Phương tiện truy cập Internet của người dân — Thiết bị khác (Ipad, Máy tính bảng): 2022: 14%; 2023: 10%
2. Thời gian truy cập Internet trung bình mỗi ngày — Dưới 3 tiếng: 2022: 11%; 2023: 23%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 3 - 5 tiếng: 2022: 38%; 2023: 37%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 5 -7 tiếng: 2022: 30%; 2023: 19%
2. Thời gian truy 

> **[sach-trang-tmdt-2023:p045:B00]** 4. Phương tiện điện tử thường được sử dụng để đặt hàng trực tuyến
91% | 91%
2022
2023
46%
18% | 13%
5%
Điện thoại di động | TMá | y tính | để | bà nh iết | bị k | há c
Máy | tính | xách tay | (I pa d, Máy | tính bảng)

## u18 · multihop · có đáp án
**Câu hỏi:** Sàn giao dịch TMĐT bán buôn bán lẻ nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành sàn này theo danh sách doanh nghiệp dẫn đầu thị trường?
**Đáp án chuẩn:** Shopee, 81%; do Công ty TNHH Shopee vận hành.  
**Evidence:** tr.46 — Biểu đồ cột 6.1, cột Shopee; tr.83 — Bảng 4.1 STT 6 / bảng 4.2 STT 5
**auto:** context đủ evidence = False
**Agent (answered, 1 tool call, 22.79s):** Sàn giao dịch TMĐT bán buôn bán lẻ được người tiêu dùng ưa chuộng nhất là Shopee, với tỷ lệ 81%. Các doanh nghiệp vận hành sàn này là Shopee, Lazada (42%), TikTok (34%), Tiki (20%), và Sendo (8%). [sach-trang-tmdt-2023:p046:B01] [sach-trang-tmdt-2023:p046:B02]
- search_documents: `sàn giao dịch TMĐT bán buôn bán lẻ ưa chuộng nhất tỷ lệ doanh nghiệp dẫn đầu thị trường` → p46, p46, p46

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

> **[sach-trang-tmdt-2023:p046:B02]** 6.2. Sàn giao dịch TMĐT lĩnh vực dịch vụ vận tải người tiêu dùng ưa chuộng
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Website TMĐT bán hàng: 34%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Sàn giao dịch TMĐT: 61%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Diễn đàn mạng xã hội: 55%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Các ứng dụng mua hàng trên thiết bị di động: 21%
6. Các kênh mua sắm trực tuyến người tiêu dùng ưa chuộng năm 2023 — Hình thức khác: 4%
6.1. Sàn giao dịch TMĐT lĩnh vực bán buôn bán lẻ người tiêu dùng ưa chuộng — S

## u19 · multihop · có đáp án
**Câu hỏi:** Doanh thu bán lẻ TMĐT của khu vực Bắc Mỹ năm 2022 là bao nhiêu, và Mỹ chiếm bao nhiêu phần trăm thị phần TMĐT toàn cầu năm 2022?
**Đáp án chuẩn:** Bắc Mỹ 1.144,99 tỷ USD; Mỹ chiếm 19,2% thị phần TMĐT toàn cầu.  
**Evidence:** tr.31 — Biểu đồ thanh ngang 2.3 Doanh thu bán lẻ TMĐT toàn cầu theo khu vực 2022, thanh 'Bắc Mỹ'; tr.32 — Biểu đồ thanh ngang 2.4 Top 12 quốc gia chiếm thị phần TMĐT lớn nhất 2022, thanh 'Mỹ'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 26.15s):** Doanh thu bán lẻ TMĐT của khu vực Bắc Mỹ năm 2022 là 1.144,99 tỷ USD. Mỹ chiếm 19,2% thị phần TMĐT toàn cầu năm 2022. [sach-trang-tmdt-2023:p031:B01] [sach-trang-tmdt-2023:p032:B00]
- search_documents: `doanh thu bán lẻ TMĐT Bắc Mỹ năm 2022` → p31, p31, p30
- search_documents: `Mỹ thị phần TMĐT toàn cầu năm 2022` → p32, p31, p33

> **[sach-trang-tmdt-2023:p031:B01]** 2.3. Doanh thu bán lẻ TMĐT toàn cầu, chia theo khu vực năm 2022
Châ | u Á - Thái | B ìn h Dươn | g | 3.323,19
Bắc | Mỹ | 1.144,99
Tây Â | u | 694,59
Ch | âu | Mỹ L | ati | nh | 167,81
Tru ng & Đô | ng Â u | 141,90
Đô | ng N am Á | 89,67
Tru ng Đô | ng và | Ch | âu | P hi 69,39 | Đơn vị tính: tỷ USD
Nguồn: Báo cáo “Global Ecommerce Forecast” - eMarketer4
3 Khu vực Đông Nam Á là một thành phần trong khu vực Châu Á – Thái Bình Dương và số liệu của khu vực Đông Nam Á cũng được tính trong số liệu của khu vực Châu
Á – Thái Bình Dương.
4 Khu vực Đông Nam Á là một thành phần trong khu vực Châu Á – Thái Bình Dương và số liệu của khu vực Đông Nam Á cũng được tính trong số liệu của khu vực Châu
Á – Thá

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

## u20 · multihop · có đáp án
**Câu hỏi:** Sàn TMĐT giao đồ ăn nào được người tiêu dùng ưa chuộng nhất, với tỷ lệ bao nhiêu, và doanh nghiệp nào vận hành sàn này theo danh sách doanh nghiệp dẫn đầu thị trường giao đồ ăn?
**Đáp án chuẩn:** ShopeeFood/Foody, 51%; do Công ty Cổ phần Foody vận hành.  
**Evidence:** tr.47 — Biểu đồ cột 6.3, cột 'ShopeeFood, Foody'; tr.84 — Bảng 4.4 Nhóm doanh nghiệp dẫn đầu dịch vụ giao đồ ăn, STT 4; tr.83 — Bảng 4.1, STT 7 (evidence thay thế cho tên doanh nghiệp)
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 23.33s):** Sàn TMĐT giao đồ ăn được người tiêu dùng ưa chuộng nhất là ShopeeFood với tỷ lệ 51%. Doanh nghiệp vận hành sàn này là Công ty Cổ phần Foody. Theo sau là Grab với tỷ lệ 50%, thuộc Công ty TNHH Grab. [sach-trang-tmdt-2023:p047:B00] [sach-trang-tmdt-2023:p084:B01]
- search_documents: `sàn TMĐT giao đồ ăn ưa chuộng nhất tỷ lệ doanh nghiệp dẫn đầu thị trường` → p47, p47, p84

> **[sach-trang-tmdt-2023:p047:B00]** 6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng
51% | 50%
15% | 13%
7%
ShopeeFood, | Grab | Baemin | Be | Khác
Foody
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng
50%
26% | 24%
14% | 9% | 8% | 16%
Traveloka | Agoda | Gotadi | Tripi Partner | AirBnB | KhácBooking.com

> **[sach-trang-tmdt-2023:p084:B01]** 4.4. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn
STT Website/ứng dụng Tên doanh nghiệp
1 Baemin Công ty TNHH Woowa Brothers Việt Nam
2 Be Công ty Cổ phần BE GROUP
3 Grab Công ty TNHH Grab
4 ShopeeFood, Foody Công ty Cổ phần Foody
5 Utop Công ty Cổ phần Công nghệ UTOP

## u21 · text · có đáp án
**Câu hỏi:** Theo Lời giới thiệu, tốc độ tăng trưởng TMĐT của Việt Nam được xếp vào nhóm bao nhiêu quốc gia dẫn đầu thế giới, theo nguồn nào?
**Đáp án chuẩn:** Nhóm 10 quốc gia có tốc độ tăng trưởng TMĐT hàng đầu thế giới, tính đến tháng 12/2023 theo Statista.  
**Evidence:** tr.3 — Lời giới thiệu, đoạn 2
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 21.89s):** Tốc độ tăng trưởng thương mại điện tử của Việt Nam được xếp vào nhóm 10 quốc gia có tốc độ tăng trưởng thương mại điện tử hàng đầu thế giới, theo nguồn Statista tính đến tháng 12/2023. [sach-trang-tmdt-2023:p003:B00]
- search_documents: `tốc độ tăng trưởng TMĐT Việt Nam nhóm quốc gia dẫn đầu thế giới Lời giới thiệu` → p3, p37, p32

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
**Agent (answered, 1 tool call, 19.38s):** Thông tin về tài khoản số của cá nhân thuộc loại dữ liệu cá nhân cơ bản theo Nghị định 13/2023/NĐ-CP. [sach-trang-tmdt-2023:p020:B00]
- search_documents: `Nghị định 13/2023/NĐ-CP tài khoản số cá nhân dữ liệu cá nhân` → p20, p20, p23

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
**Agent (answered, 1 tool call, 12.82s):** Thẻ Căn cước công dân gắn chíp hoặc dữ liệu dân cư được ứng dụng để xác thực chủ thể hoạt động thương mại điện tử khi giao kết hợp đồng trên Trục phát triển hợp đồng điện tử Việt Nam. [sach-trang-tmdt-2023:p025:B00]
- search_documents: `Chỉ thị 18/CT-TTg thẻ Căn cước công dân gắn chíp dữ liệu dân cư xác thực TMĐT` → p24, p25, p96

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

## u24 · text · có đáp án
**Câu hỏi:** Theo Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi), tổ chức vận hành nền tảng số trung gian phải cung cấp thông tin về tổ chức, cá nhân kinh doanh trên nền tảng trong trường hợp nào?
**Đáp án chuẩn:** Khi người tiêu dùng giao dịch với tổ chức, cá nhân kinh doanh đó có yêu cầu.  
**Evidence:** tr.11 — Khối '3 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian', ô số 4
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 16.71s):** Tổ chức vận hành nền tảng số trung gian phải cung cấp thông tin về tổ chức, cá nhân kinh doanh trên nền tảng khi người tiêu dùng (NTD) giao dịch với tổ chức, cá nhân kinh doanh đó có yêu cầu. [sach-trang-tmdt-2023:p011:B01]
- search_documents: `Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) thông tin tổ chức cá nhân kinh doanh nền tảng số trung gian` → p12, p11, p11

> **[sach-trang-tmdt-2023:p011:B01]** 1. Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi)
Hiển thị đầy đủ, minh bạch thông tin sản phẩm, hàng hóa, dịch vụ do tổ
chức, cá nhân kinh doanh bán, cung cấp, bao gồm các nội dung bắt buộc thể
hiện trên nhãn hàng hóa theo quy định của pháp luật về nhãn hàng hóa, trừ
các thông tin có tính chất riêng biệt theo sản phẩm, bao gồm: ngày, tháng,
năm sản xuất; thời hạn sử dụng; số lô sản xuất; số khung, số máy; tiêu chuẩn
kết quả cần đạt được trong cung cấp sản phẩm, hàng hóa, dịch vụ;
Cung cấp thông tin về tổ chức, cá nhân kinh doanh hoạt động trên nền tảng
số trung gian khi NTD giao dịch với tổ chức, cá nhân kinh doanh đó có yêu cầu;

## u25 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Mỹ là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.5 (tr. 30) chỉ có Thái Lan, Hàn Quốc, Indonesia, Ấn Độ, Trung Quốc, Malaysia, Singapore, Philippines, Việt Nam, Úc và trung bình toàn cầu; 'Mỹ' chỉ xuất hiện ở tr. 31–33 (doanh thu, thị phần).
**Agent (abstain, 1 tool call, 28.1s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Mỹ` → p29, p30, p48
- abstain: Tài liệu không cung cấp thông tin về tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Mỹ.

## u26 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Quy mô nền kinh tế Internet của Campuchia năm 2023 là bao nhiêu tỷ USD?
**Lý do thiếu:** Biểu đồ 2 (tr. 34) chỉ có Indonesia, Thái Lan, Việt Nam, Philippines, Malaysia, Singapore; 'Campuchia' không xuất hiện trong toàn văn.
**Agent (abstain, 1 tool call, 21.5s):** Không đủ bằng chứng để trả lời.
- search_documents: `quy mô nền kinh tế Internet Campuchia 2023` → p34, p34, p3
- abstain: Tài liệu không chứa thông tin về quy mô nền kinh tế Internet của Campuchia năm 2023.

## u27 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Bao nhiêu phần trăm người tiêu dùng ưa chuộng Tiki trong lĩnh vực dịch vụ giao đồ ăn?
**Lý do thiếu:** Biểu đồ 6.3 (tr. 47) chỉ có ShopeeFood/Foody, Grab, Baemin, Be, Khác; Tiki chỉ có ở biểu đồ bán buôn bán lẻ (tr. 46, 20%) và bảng doanh nghiệp (tr. 83).
**Agent (answered, 1 tool call, 20.36s):** Trong lĩnh vực dịch vụ giao đồ ăn, Tiki không nằm trong danh sách các sàn giao dịch được ưa chuộng. Các sàn giao dịch phổ biến nhất là ShopeeFood (51%), Grab (50%), Baemin (15%), Be (7%) và các sàn khác (13%). [sach-trang-tmdt-2023:p047:B00] [sach-trang-tmdt-2023:p047:B02]
- search_documents: `Tiki dịch vụ giao đồ ăn phần trăm người tiêu dùng ưa chuộng` → p46, p47, p47

> **[sach-trang-tmdt-2023:p047:B00]** 6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng
51% | 50%
15% | 13%
7%
ShopeeFood, | Grab | Baemin | Be | Khác
Foody
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng
50%
26% | 24%
14% | 9% | 8% | 16%
Traveloka | Agoda | Gotadi | Tripi Partner | AirBnB | KhácBooking.com

> **[sach-trang-tmdt-2023:p047:B02]** 7. Hình thức thanh toán phổ biến
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng — ShopeeFood, Foody: 51%
6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng — Grab: 50%
6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng — Baemin: 15%
6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng — Be: 7%
6.3. Sàn giao dịch TMĐT lĩnh vực dịch vụ giao đồ ăn người tiêu dùng ưa chuộng — Khác: 13%
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tuyến người tiêu dùng ưa chuộng — Traveloka: 50%
6.4. Sàn giao dịch TMĐT lĩnh vực du lịch trực tu

## u28 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Năm 2023, các website TMĐT bán hàng tại Việt Nam xử lý tổng cộng bao nhiêu triệu đơn hàng thành công?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ % đơn hàng thành công theo tỉnh/thành (tr. 77, 82) và theo người bán (tr. 80); không có số đơn hàng tuyệt đối ('triệu đơn' không xuất hiện).
**Agent (abstain, 4 tool call, 71.67s):** Không đủ bằng chứng để trả lời.
- search_documents: `2023 tổng số đơn hàng thành công website TMĐT Việt Nam` → p80, p26, p78
- search_documents: `2023 tổng số đơn hàng TMĐT Việt Nam` → p40, p3, p26
- search_documents: `2023 số lượng đơn hàng TMĐT Việt Nam` → p40, p26, p37
- search_documents: `2023 tổng số đơn hàng TMĐT Việt Nam` → p40, p3, p26
- abstain: Tài liệu không chứa thông tin về tổng số đơn hàng thành công của các website TMĐT tại Việt Nam trong năm 2023.

## u29 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho năm 2023 là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.1 (tr. 55) chỉ có phần mềm quản lý nhân sự, chuỗi cung ứng, chăm sóc khách hàng, quản trị doanh nghiệp; 'quản lý kho' không xuất hiện.
**Agent (answered, 1 tool call, 18.86s):** Tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho năm 2023 không được nêu cụ thể trong tài liệu. Tuy nhiên, có thông tin về tỷ lệ doanh nghiệp sử dụng các phần mềm khác như quản lý nhân sự (47%), quản lý chuỗi cung ứng (28%), quản lý chăm sóc khách hàng (29%), và quản trị doanh nghiệp (20%). [sach-trang-tmdt-2023:p055:B00]
- search_documents: `tỷ lệ doanh nghiệp sử dụng phần mềm quản lý kho năm 2023` → p55, p57, p56

> **[sach-trang-tmdt-2023:p055:B00]** 3. Quy mô của doanh nghiệp tham gia khảo sát
12%
Doanh nghiệp vừ a và nhỏ
Doanh nghiệp lớn
88%
II. MỨC ĐỘ SẴN SÀNG ỨNG DỤNG TMĐT CỦA DOANH NGHIỆP
1. Hạ tầng công nghệ thông tin
1.1. Các phần mềm phổ biến được doanh nghiệp sử dụng
57%
47%
31% | 33%28%29%
2022
22% | 20% | 2023
Quản lý nhân sự | Quản lý chuỗi | Quản lý chăm sóc | Quản trị
cung ứng | khách hàng | doanh nghiệp
[Tiêu đề trục dọc] (Tỷ lệ doanh nghiệp tham gia khảo sát)
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1.1. Các phần mềm phổ biến được doanh nghiệp sử dụng — Quản lý nhân sự: 2022: 57%; 2023: 47%
1.1. Các phần mềm phổ biến được doanh nghiệp sử dụng — Quản lý chuỗi cung ứng: 2022: 31%; 2023: 28%
1.1. Các phầ

## u30 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Mức lương trung bình của nhân sự làm thương mại điện tử tại Việt Nam năm 2023 là bao nhiêu?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ doanh nghiệp ưu tiên tuyển nhân sự đào tạo CNTT/TMĐT (tr. 57); 'lương' không xuất hiện trong toàn văn.
**Agent (abstain, 2 tool call, 39.19s):** Không đủ bằng chứng để trả lời.
- search_documents: `mức lương trung bình nhân sự thương mại điện tử Việt Nam 2023` → p57, p3, p50
- search_documents: `lương nhân sự thương mại điện tử Việt Nam 2023` → p57, p3, p50
- abstain: Tài liệu không chứa thông tin về mức lương trung bình của nhân sự làm thương mại điện tử tại Việt Nam năm 2023.
