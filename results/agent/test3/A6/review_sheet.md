# Phiếu chấm A6 / test3

Đối chiếu từng câu trả lời với đáp án chuẩn và ảnh trang gốc (work/pages_hd/pNNN.png). Cột 'auto' chỉ là gợi ý (gold match trong context), không thay chấm tay.


## v01 · table · có đáp án
**Câu hỏi:** Trong danh sách website TMĐT bán hàng có chức năng đặt hàng trực tuyến dẫn đầu về doanh thu, website bachhoaxanh.com thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần Thương Mại Bách Hoá Xanh.  
**Evidence:** tr.78 — Bảng 4.1, STT 4
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 94.4s):** Website bachhoaxanh.com thuộc Công ty Cổ phần Thương Mại Bách Hoá Xanh. [sach-trang-tmdt-2023:p78:V1]
- search_documents: `bachhoaxanh.com doanh nghiệp` → p78, p78, p58, p55, p54

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

## v02 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ, website samsung.com.vn thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty TNHH Điện Tử Samsung Vina.  
**Evidence:** tr.83 — Bảng 4.2, STT 2
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 114.47s):** Website samsung.com.vn thuộc Công Ty TNHH Điện Tử Samsung Vina trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT bán buôn bán lẻ năm 2023. [sach-trang-tmdt-2023:p083:B01] [sach-trang-tmdt-2023:p83:V2]
- search_documents: `samsung.com.vn thuộc doanh nghiệp nào` → p83, p83, p83, p78, p78
- read_page: `page 83` → p83, p83, p83, p83

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

## v03 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn, ứng dụng Utop thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần Công nghệ UTOP.  
**Evidence:** tr.84 — Bảng 4.4, STT 5
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 83.89s):** Ứng dụng Utop thuộc Công ty Cổ phần Công nghệ UTOP trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn năm 2023. [sach-trang-tmdt-2023:p084:B01] [sach-trang-tmdt-2023:p84:V2]
- search_documents: `Utop thuộc doanh nghiệp nào` → p84, p84, p83, p83, p84
- read_page: `page 84` → p84, p84, p84, p84

> **[sach-trang-tmdt-2023:p084:B01]** 4.4. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn
STT Website/ứng dụng Tên doanh nghiệp
1 Baemin Công ty TNHH Woowa Brothers Việt Nam
2 Be Công ty Cổ phần BE GROUP
3 Grab Công ty TNHH Grab
4 ShopeeFood, Foody Công ty Cổ phần Foody
5 Utop Công ty Cổ phần Công nghệ UTOP

> **[sach-trang-tmdt-2023:p84:V2]** [table] 4.4. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT giao đồ ăn
(Trang 84, nửa dưới; đơn vị: không ghi)
1 | Baemin | Công ty TNHH Woowa Brothers Việt Nam
2 | Be | Công ty Cổ phần BE GROUP
3 | Grab | Công ty TNHH Grab
4 | ShopeeFood, Foody | Công ty Cổ phần Foody
5 | Utop | Công ty Cổ phần Công nghệ UTOP

## v04 · table · có đáp án
**Câu hỏi:** Trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT du lịch trực tuyến, Travellink.vn thuộc doanh nghiệp nào?
**Đáp án chuẩn:** Công ty Cổ phần Công nghệ và Truyền thông VNLINK.  
**Evidence:** tr.85 — Bảng 4.5, STT 4
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 101.38s):** Travellink.vn thuộc Công ty Cổ phần Công nghệ và Truyền thông VNLINK trong nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT du lịch trực tuyến năm 2023. [sach-trang-tmdt-2023:p85:V1]
- search_documents: `Travellink.vn thuộc doanh nghiệp nào` → p85, p85, p83, p83, p83
- read_page: `page 85` → p85, p85, p85, p85

> **[sach-trang-tmdt-2023:p85:V1]** [table] 4.5. Nhóm doanh nghiệp dẫn đầu thị trường cung cấp dịch vụ TMĐT du lịch trực tuyến
(Trang 85, nửa trên; đơn vị: không ghi)
STT | Website/ứng dụng: giá trị | Tên doanh nghiệp: giá trị
1 | Traveloka | Công ty TNHH Traveloka Việt Nam
2 | Gotadi | Công ty Cổ phần Công nghệ du lịch Gotadi
3 | Tripi Partner | Công ty Cổ phần du lịch Việt Nam Vntravel
4 | Travellink.vn | Công ty Cổ phần Công nghệ và Truyền thông VNLINK
5 | Onedanang.vn | Công ty TNHH Truyền Thông và Công nghệ One Office

## v05 · table · có đáp án
**Câu hỏi:** Tỷ lệ website/ứng dụng TMĐT bán hàng và website/ứng dụng CCDV TMĐT có chính sách đổi trả hàng và hoàn tiền là bao nhiêu?
**Đáp án chuẩn:** Bán hàng 77,1%; CCDV 77,5%.  
**Evidence:** tr.75 — Bảng 5.3, hàng 'Chính sách đổi trả hàng và hoàn tiền'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 159.2s):** Năm 2023, tỷ lệ website/ứng dụng TMĐT bán hàng có chính sách đổi trả hàng và hoàn tiền là 77,1%. Tỷ lệ này ở website/ứng dụng CCDV TMĐT là 77,5%. [sach-trang-tmdt-2023:p75:V1]
- search_documents: `tỷ lệ website TMĐT bán hàng có chính sách đổi trả hàng và hoàn tiền` → p75, p75, p68, p76, p70
- search_documents: `tỷ lệ website CCDV TMĐT có chính sách đổi trả hàng và hoàn tiền` → p75, p75, p68, p72, p70

> **[sach-trang-tmdt-2023:p75:V1]** [table] 5.3. Các chính sách, cơ chế hỗ trợ khách hàng
(Trang 75, giữa; đơn vị: %)
Chính sách bảo hành, bảo trì sản phẩm, dịch vụ | Website, ứng dụng TMĐT bán hàng: 77,3% | Website, ứng dụng CCDV TMĐT: 74,1%
Chính sách đổi trả hàng và hoàn tiền | Website, ứng dụng TMĐT bán hàng: 77,1% | Website, ứng dụng CCDV TMĐT: 77,5%
Chính sách giải quyết tranh chấp, khiếu nại | Website, ứng dụng TMĐT bán hàng: 81,0% | Website, ứng dụng CCDV TMĐT: 85,9%
Chính sách bảo vệ thông tin cá nhân | Website, ứng dụng TMĐT bán hàng: 91,5% | Website, ứng dụng CCDV TMĐT: 93,4%
Cơ chế và quy trình rà soát và kiểm duyệt thông tin | Website, ứng dụng TMĐT bán hàng: 79,0% | Website, ứng dụng CCDV TMĐT: 86,5%
Cơ chế cho p

## v06 · table · có đáp án
**Câu hỏi:** Theo bảng phụ lục khung pháp lý cơ bản về TMĐT, Luật Doanh nghiệp được ban hành ngày nào và trạng thái hiệu lực ra sao?
**Đáp án chuẩn:** Ban hành ngày 17/06/2020; hết hiệu lực một phần.  
**Evidence:** tr.88 — Bảng phụ lục, dòng 'Luật Doanh nghiệp' (17/06/2020)
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 109.63s):** Theo bảng phụ lục khung pháp lý cơ bản về thương mại điện tử, Luật Doanh nghiệp được ban hành ngày 17/06/2020 và trạng thái hiệu lực là "Hết hiệu lực một phần". [sach-trang-tmdt-2023:p88:V1]
- search_documents: `bảng phụ lục khung pháp lý cơ bản về TMĐT` → p95, p88, p93, p95, p89
- read_page: `page 88` → p88, p88, p88, p88

> **[sach-trang-tmdt-2023:p88:V1]** [table] PHỤ LỤC: BẢNG CẬP NHẬT KHUNG PHÁP LÝ CƠ BẢN VỀ THƯƠNG MẠI ĐIỆN TỬ
(Trang 88, giữa; đơn vị: không ghi)
Thời gian ban hành | Luật: giá trị | Trạng thái hiệu lực: giá trị
24/11/2023 | Luật viễn thông (sửa đổi) | 1/7/2024
22/6/2023 | Luật Giao dịch điện tử (sửa đổi) | 01/7/2024
20/6/2023 | Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi) | 01/7/2024
16/6/2022 | Luật sửa đổi, bổ sung một số điều của Luật Sở hữu trí tuệ | 01/03/2022
11/01/2022 | Luật sửa đổi, bổ sung một số điều của Luật Đầu tư công, Luật Đầu tư theo phương thức đối tác công tư, Luật Đầu thầu, Luật Điện lực, Luật Doanh nghiệp, Luật Thuế tiêu thụ đặc biệt và Luật Thi hành án dân sự | 01/03/2022
18/06/2020 | Luật Đầu tư | Hết

## v07 · image · có đáp án
**Câu hỏi:** Theo sơ đồ quyền của chủ thể dữ liệu trong Nghị định 13/2023/NĐ-CP, quyền số 4 là quyền gì?
**Đáp án chuẩn:** Quyền rút lại sự đồng ý.  
**Evidence:** tr.21 — Sơ đồ khối '2 Quyền của chủ thể dữ liệu', ô số 4 (cột trái)
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 163.98s):** Theo sơ đồ quyền của chủ thể dữ liệu trong Nghị định 13/2023/NĐ-CP, quyền số 4 là "Quyền rút lại sự đồng ý". [sach-trang-tmdt-2023:p21:V1]
- search_documents: `sơ đồ quyền của chủ thể dữ liệu Nghị định 13/2023/NĐ-CP` → p21, p21, p23, p20, p22
- read_page: `page 21` → p21, p21

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

## v08 · image · có đáp án
**Câu hỏi:** Theo sơ đồ trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian với người tiêu dùng (mục 3), trách nhiệm thứ hai là gì?
**Đáp án chuẩn:** Chỉ định, công bố công khai đầu mối liên hệ, người đại diện được ủy quyền phối hợp với cơ quan quản lý nhà nước có thẩm quyền trong việc giải quyết các vấn đề liên quan đến bảo vệ quyền lợi người tiêu dùng.  
**Evidence:** tr.11 — Sơ đồ khối mục 3, ô số 2
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 169.98s):** Trách nhiệm thứ hai của tổ chức thiết lập, vận hành nền tảng số trung gian với người tiêu dùng là: "Xây dựng, công bố công khai quy chế hoạt động của nền tảng số trung gian cho NTD, trong đó phân định rõ trách nhiệm của các bên tham gia giao dịch." [sach-trang-tmdt-2023:p011:B00]
- search_documents: `trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian với người tiêu dùng` → p11, p13, p10, p13, p12
- read_page: `page 11` → p11, p11
- search_documents: `sơ đồ trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian` → p13, p11, p13, p18, p10
- read_page: `page 11` → p11, p11

> **[sach-trang-tmdt-2023:p011:B00]** 1. Luật Bảo vệ quyền lợi người tiêu dùng (sửa đổi)
3 Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số trung gian với NTD trong giao dịch
trên không gian mạng
1
3
5
2
4
6
Có trách nhiệm thực hiện quy định tại Điều 37 và Điều 38, Mục 2 Chương III
trong trường hợp cung cấp dịch vụ liên tục;
Xây dựng, công bố công khai quy chế hoạt động của nền tảng số trung gian
cho NTD, trong đó phân định rõ trách nhiệm của các bên tham gia giao dịch;
Chỉ định, công bố công khai đầu mối liên hệ, người đại diện được ủy quyền
phối hợp với CQQLNN có thẩm quyền trong việc giải quyết các vấn đề liên
quan đến BVQLNTD;
Cho phép NTD phản hồi, đánh giá về tổ chức, cá nhân kinh doanh, sản phẩm,
hàng hóa, dịch vụ 

## v09 · image · có đáp án
**Câu hỏi:** Theo infographic tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023, bao nhiêu phần trăm doanh nghiệp có sử dụng chữ ký điện tử?
**Đáp án chuẩn:** 80%.  
**Evidence:** tr.57 — Infographic mục 3, ô thứ nhất (hình chữ ký)
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 62.97s):** Theo infographic về tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023, có 80% doanh nghiệp có sử dụng chữ ký điện tử. [sach-trang-tmdt-2023:p57:V2]
- search_documents: `infographic tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023` → p57, p57, p56, p56, p3
- read_page: `page 57` → p57, p57, p57

> **[sach-trang-tmdt-2023:p57:V2]** [infographic] 3. Tình hình sử dụng chữ ký số, hợp đồng và hóa đơn điện tử năm 2023
(Trang 57, giữa; đơn vị: %)
80% | doanh nghiệp có sử dụng chữ ký điện tử
41% | doanh nghiệp có sử dụng hợp đồng điện tử trong giao dịch
22% | doanh nghiệp có sử dụng dịch vụ chứng thực hợp đồng điện tử

## v10 · image · có đáp án
**Câu hỏi:** Theo infographic về website của doanh nghiệp, bao nhiêu phần trăm website của doanh nghiệp có tính năng tương tác trực tuyến với khách hàng?
**Đáp án chuẩn:** 66%.  
**Evidence:** tr.58 — Infographic 1.3 Website tương tác trực tuyến với khách hàng (ô '66%')
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 57.23s):** Theo infographic về website của doanh nghiệp, 66% website của doanh nghiệp có tính năng tương tác trực tuyến với khách hàng trong năm 2023. [sach-trang-tmdt-2023:p058:B02] [sach-trang-tmdt-2023:p58:V3]
- search_documents: `infographic website doanh nghiệp tính năng tương tác trực tuyến` → p58, p58, p73, p58, p58
- read_page: `page 58` → p58, p58, p58, p58, p58, p58

> **[sach-trang-tmdt-2023:p058:B02]** 1.3. Website tương tác trực tuyến với khách hàng
66% | website của doanh nghiệp có tính năng tương tác trực tuyến13 với khách hàng
Hình thức phản hồi trực tuyến với khách hàng
66% | 61%
44%
2%
Qua | nhân sự | phụQua | thông tinQua | chat bot | Hình | thứ | c khác
trách | tư ơng tác liên hệ khách | tự động
trực tiếp | hàng | để lại
13 Facebook Messenger, Zalo, Viber, Whatsapp,...
[Tiêu đề trục dọc] hợp tính năng tương tác trực; tiếp với khách hàng trên website); (Tỷ lệ doanh nghiệp có tích

> **[sach-trang-tmdt-2023:p58:V3]** [bar_chart] 1.3. Website tương tác trực tuyến với khách hàng
(Trang 58, nửa dưới; đơn vị: %)
website có tính năng tương tác trực tuyến với khách hàng — 2023: 66%; Qua nhân sự phụ trách tương tác trực tiếp — 2023: 66%; Qua thông tin liên hệ khách hàng để lại — 2023: 61%; Qua chat bot tự động — 2023: 44%; Hình thức khác — 2023: 2%

## v11 · image · có đáp án
**Câu hỏi:** Năm 2023, Cổng thông tin quản lý hoạt động TMĐT tiếp nhận bao nhiêu hồ sơ thông báo và tăng bao nhiêu phần trăm so với năm 2022?
**Đáp án chuẩn:** 105.103 hồ sơ thông báo, tăng 12,1%.  
**Evidence:** tr.26 — Infographic khối thứ hai (biểu tượng thư mục), dòng 1
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 106.56s):** Năm 2023, Cổng thông tin quản lý hoạt động TMĐT tiếp nhận 105.103 hồ sơ thông báo, tăng 12,1% so với năm 2022. [sach-trang-tmdt-2023:p026:B00]
- search_documents: `Cổng thông tin quản lý hoạt động TMĐT hồ sơ thông báo 2023` → p26, p26, p68, p55, p24
- read_page: `page 26` → p26, p26, p26, p26

> **[sach-trang-tmdt-2023:p026:B00]** II. THÔNG TIN QUẢN LÝ HOẠT ĐỘNG THƯƠNG MẠI ĐIỆN TỬ
Số lượng phản ánh, khiếu nại trên
Cổng thông tin quản lý hoạt động TMĐT năm 2023
76.255 tài khoản doanh nghiệp
tăng 16,4% so với năm 2022
26.250 tài khoản cá nhân
tăng 10,8% so với năm 2022
105.103 hồ sơ thông báo
tăng 12,1% so với năm 2022

## v12 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Việt Nam là bao nhiêu, và cao hay thấp hơn mức trung bình toàn cầu?
**Đáp án chuẩn:** 60,7%, cao hơn trung bình toàn cầu 57,6% (3,1 điểm phần trăm).  
**Evidence:** tr.30 — Biểu đồ thanh ngang 1.5, thanh 'Việt Nam' và 'Trung bình toàn cầu'
**auto:** context đủ evidence = True
**Agent (answered, 3 tool call, 69.59s):** Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Việt Nam năm 2023 là 60,7%. Mức này cao hơn mức trung bình toàn cầu là 57,6% (cao hơn 3,1 điểm phần trăm) . [sach-trang-tmdt-2023:p030:B00]
- search_documents: `tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần Việt Nam` → p30, p29, p29, p30, p40
- read_page: `page 30` → p30, p30, p30
- read_page: `page 29` → p29, p29, p29, p29

> **[sach-trang-tmdt-2023:p030:B00]** 1.5. Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại một số quốc gia
Thái L | an | 66,8%
Hàn | Q uốc | 65,6%
Indonesia | 62,6%
Ấn | Độ | 62,3%
Tru ng Quốc | 61,9%
Malaysia | 61,3%
Singapore | 61,0%
Philippines | 61,0%
Việt N am | 60,7%
Úc | 53,4%
Tru ng bình to àn | c ầu | 57,6%

## v13 · chart · có đáp án
**Câu hỏi:** Năm 2023, nhóm thời gian truy cập Internet trung bình mỗi ngày nào chiếm tỷ lệ người dùng cao nhất?
**Đáp án chuẩn:** Từ 3 – 5 tiếng, 37%.  
**Evidence:** tr.42 — Biểu đồ cột 2. Thời gian truy cập Internet trung bình mỗi ngày, cột 2023 nhóm 'Từ 3 - 5 tiếng'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 78.27s):** Năm 2023, nhóm thời gian truy cập Internet trung bình mỗi ngày chiếm tỷ lệ người dùng cao nhất là "Từ 3 - 5 tiếng" với 37%. [sach-trang-tmdt-2023:p042:B02]
- search_documents: `thời gian truy cập Internet trung bình mỗi ngày 2023` → p42, p42, p29, p42, p28
- read_page: `page 42` → p42, p42, p42, p42, p42

> **[sach-trang-tmdt-2023:p042:B02]** 2. Thời gian truy cập Internet trung bình mỗi ngày
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
1. Phương tiện truy cập Internet của người dân — Máy tính để bàn Máy tính xách tay: 2022: 63%; 2023: 50%
1. Phương tiện truy cập Internet của người dân — Điện thoại di động: 2022: 94%; 2023: 90%
1. Phương tiện truy cập Internet của người dân — Thiết bị khác (Ipad, Máy tính bảng): 2022: 14%; 2023: 10%
2. Thời gian truy cập Internet trung bình mỗi ngày — Dưới 3 tiếng: 2022: 11%; 2023: 23%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 3 - 5 tiếng: 2022: 38%; 2023: 37%
2. Thời gian truy cập Internet trung bình mỗi ngày — Từ 5 -7 tiếng: 2022: 30%; 2023: 19%
2. Thời gian truy 

## v14 · chart · có đáp án
**Câu hỏi:** Tỷ lệ người tiêu dùng trực tuyến đánh giá 'Hài lòng' năm 2023 là bao nhiêu và thay đổi thế nào so với năm 2022?
**Đáp án chuẩn:** 42% năm 2023, giảm 11 điểm phần trăm so với 53% năm 2022.  
**Evidence:** tr.51 — Biểu đồ cột 1. Mức độ hài lòng, nhóm 'Hài lòng'
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 57.34s):** Tỷ lệ người tiêu dùng trực tuyến đánh giá 'Hài lòng' năm 2023 là 42%. So với năm 2022 (53%), tỷ lệ này đã giảm 11 điểm phần trăm (53% - 42% = 11 điểm phần trăm). [sach-trang-tmdt-2023:p051:B00]
- search_documents: `tỷ lệ người tiêu dùng trực tuyến đánh giá hài lòng năm 2023` → p51, p51, p51, p46, p46
- read_page: `page 51` → p51, p51, p51, p51

> **[sach-trang-tmdt-2023:p051:B00]** V. ĐÁNH GIÁ MỨC ĐỘ HÀI LÒNG VỀ HOẠT ĐỘNG MUA SẮM TRỰC TUYẾN
1. Mức độ hài lòng của người tiêu dùng trực tuyến
53%
47%
42%
32%
2022
2023
14%
8%
1% | 3%
Rất hài lòng | Hài lòng | Bình thường | Không hài lòng

## v15 · chart · có đáp án
**Câu hỏi:** Quốc gia/khu vực nào là thị trường xuất khẩu qua TMĐT phổ biến nhất của doanh nghiệp và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Hàn Quốc, 45%.  
**Evidence:** tr.63 — Biểu đồ cột 2.3.2 Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT, cột đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 47.59s):** Thị trường xuất khẩu qua thương mại điện tử phổ biến nhất của doanh nghiệp Việt Nam là Hàn Quốc, chiếm 45%. [sach-trang-tmdt-2023:p063:B01]
- search_documents: `thị trường xuất khẩu qua thương mại điện tử phổ biến nhất` → p63, p63, p63, p62, p62
- read_page: `page 63` → p63, p63, p63, p63, p63

> **[sach-trang-tmdt-2023:p063:B01]** 2.3.4. Doanh nghiệp đánh giá mức độ hiệu quả ứng dụng TMĐT trong hoạt động xuất khẩu
17% | 9%
Không hiệu quả
23% | Tương đối hiệu quả
50% | Hiệu quả
Rất hiệu quả
[Tiêu đề trục dọc] (Tỷ lệ doanh nghiệp tham gia; xuất khẩu qua TMĐT)
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Hàn Quốc: 45%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Nhật Bản: 40%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Trung Quốc: 38%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Liên minh Châu Âu: 15%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Hoa Kỳ: 14%
2.3.2. Quốc gia/khu vực doanh nghiệp x

## v16 · chart · có đáp án
**Câu hỏi:** Nhóm hàng hóa, dịch vụ cụ thể nào được mua, sử dụng nhiều nhất trên website, ứng dụng TMĐT bán hàng và chiếm bao nhiêu phần trăm?
**Đáp án chuẩn:** Thực phẩm, thực phẩm chức năng, làm đẹp, sức khỏe: 20,4% (không tính nhóm 'Sản phẩm, dịch vụ khác' 29,0%).  
**Evidence:** tr.76 — Biểu đồ thanh ngang 1. Hàng hóa, dịch vụ được mua nhiều nhất, thanh đầu tiên
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 64.2s):** Nhóm hàng hóa, dịch vụ được mua, sử dụng nhiều nhất trên website, ứng dụng TMĐT bán hàng năm 2023 là "Thực phẩm, thực phẩm chức năng, làm đẹp, sức khỏe" với tỷ lệ 20,4%. [sach-trang-tmdt-2023:p076:B01] [sach-trang-tmdt-2023:p76:V1]
- search_documents: `nhóm hàng hóa dịch vụ được mua nhiều nhất trên website ứng dụng TMĐT bán hàng` → p76, p76, p76, p45, p45
- read_page: `page 76` → p76, p76, p76, p76, p76

> **[sach-trang-tmdt-2023:p076:B01]** 1. Hàng hóa, dịch vụ được mua, sử dụng nhiều nhất trên website, ứng dụng TMĐT bán hàng
Thự | c phẩm | , thự | c phẩm | chứ | c năng, làm đẹp, sức khỏe | 20,4%
Đồ điện | tử | 18,0%
Nhà | cửa – đờ | i sốn | g | 12,5%
Thời trang – phụ kiện, đồ chơi – mẹ và bé | 9,5%
Dịch vụ nội dung số & giá trị gia tăng; tên miền, hosting,phần mềm,
thiết kế website; quảng cáo, quảng cáo trực tuyến, tổ chức sự kiện. | 9,1%
Ô tô – xe máy – xe đạp & phụ kiện, thể thao – dã ngoại – du lịch | 5,4%
Dịch vụ y tế, chăm sóc sức khỏe, làm đẹp | 4,8%
Dịch vụ đào tạo, đào tạo trực tuyến; tư vấn hồ sơ, pháp lý, thuế, tài chính, | 3,5%
quản lý, v.v..; môi giới việc làm, tư vấn du học; tư vấn, thiết kế xây dựng, kiến trúc
Sá

> **[sach-trang-tmdt-2023:p76:V1]** [bar_chart] 1. Hàng hóa, dịch vụ được mua, sử dụng nhiều nhất trên website, ứng dụng TMĐT bán hàng
(Trang 76, nửa trên; đơn vị: %)
Thực phẩm, thực phẩm chức năng, làm đẹp, sức khỏe — 2023: 20,4%
Đồ điện tử — 2023: 18,0%
Nhà cửa – đồ sống — 2023: 12,5%
Thời trang – phụ kiện, đồ chơi – mẹ và bé — 2023: 9,5%
Dịch vụ nội dung số & giá trị gia tăng; tên miền, hosting, phần mềm, thiết kế website; quảng cáo, quảng cáo trực tuyến, tổ chức sự kiện. — 2023: 9,1%
Ô tô – xe máy – xe đạp & phụ kiện, thể thao – dã ngoại – du lịch — 2023: 5,4%
Dịch vụ y tế, chăm sóc sức khỏe, làm đẹp — 2023: 4,8%
Dịch vụ đào tạo, đào tạo trực tuyến; tư vấn hồ sơ, pháp lý, thuế, tài chính, quản lý, v.v..; môi giới việc làm,

## v17 · multihop · có đáp án
**Câu hỏi:** Bao nhiêu phần trăm doanh nghiệp có sử dụng website/ứng dụng TMĐT cho mục đích xuất nhập khẩu, và trong số doanh nghiệp xuất khẩu qua TMĐT, bao nhiêu phần trăm xuất khẩu sang Nhật Bản?
**Đáp án chuẩn:** 13% doanh nghiệp dùng website/ứng dụng TMĐT cho xuất nhập khẩu (tr. 62); 40% doanh nghiệp xuất khẩu qua TMĐT sang Nhật Bản (tr. 63).  
**Evidence:** tr.62 — Mục 2.3 Hoạt động xuất nhập khẩu thông qua TMĐT (ô '13%'); tr.63 — Biểu đồ cột 2.3.2 Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT, cột Nhật Bản
**auto:** context đủ evidence = True
**Agent (answered, 3 tool call, 99.01s):** Năm 2023, có 13% doanh nghiệp sử dụng website/ứng dụng thương mại điện tử cho mục đích xuất nhập khẩu. Trong số doanh nghiệp xuất khẩu qua thương mại điện tử, 40% xuất khẩu sang Nhật Bản. [sach-trang-tmdt-2023:p62:V2] [sach-trang-tmdt-2023:p063:B01]
- search_documents: `doanh nghiệp sử dụng website ứng dụng TMĐT cho xuất nhập khẩu` → p62, p62, p62, p62, p63
- search_documents: `doanh nghiệp xuất khẩu qua TMĐT sang Nhật Bản` → p63, p63, p63, p62, p83
- read_page: `page 63` → p63, p63, p63, p63, p63

> **[sach-trang-tmdt-2023:p62:V2]** [infographic] 2.3. Hoạt động xuất nhập khẩu thông qua TMĐT
(Trang 62, giữa; đơn vị: %)
13% doanh nghiệp có sử dụng website/ứng dụng TMĐT phục vụ cho mục đích xuất nhập khẩu

> **[sach-trang-tmdt-2023:p063:B01]** 2.3.4. Doanh nghiệp đánh giá mức độ hiệu quả ứng dụng TMĐT trong hoạt động xuất khẩu
17% | 9%
Không hiệu quả
23% | Tương đối hiệu quả
50% | Hiệu quả
Rất hiệu quả
[Tiêu đề trục dọc] (Tỷ lệ doanh nghiệp tham gia; xuất khẩu qua TMĐT)
[Biểu đồ cột đứng – nhãn và giá trị ghép tự động theo toạ độ]
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Hàn Quốc: 45%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Nhật Bản: 40%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Trung Quốc: 38%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Liên minh Châu Âu: 15%
2.3.2. Quốc gia/khu vực doanh nghiệp xuất khẩu qua TMĐT — Hoa Kỳ: 14%
2.3.2. Quốc gia/khu vực doanh nghiệp x

## v18 · multihop · có đáp án
**Câu hỏi:** Theo số liệu eMarketer, doanh thu bán lẻ TMĐT khu vực Đông Nam Á năm 2022 là bao nhiêu; còn theo e-Conomy SEA, doanh thu bán lẻ hàng hóa trực tuyến của Đông Nam Á năm 2022 là bao nhiêu?
**Đáp án chuẩn:** eMarketer: 89,67 tỷ USD; e-Conomy SEA: 130 tỷ USD.  
**Evidence:** tr.31 — Biểu đồ thanh ngang 2.3 (nguồn eMarketer), thanh 'Đông Nam Á'; tr.34 — Biểu đồ 1. Quy mô nền kinh tế Internet phân theo lĩnh vực (e-Conomy SEA), cột 'Doanh thu bán lẻ hàng hóa trực tuyến' 2022
**auto:** context đủ evidence = True
**Agent (answered, 3 tool call, 126.02s):** Theo số liệu eMarketer, doanh thu bán lẻ thương mại điện tử khu vực Đông Nam Á năm 2022 là 89,67 tỷ USD . Theo e-Conomy SEA, doanh thu bán lẻ hàng hóa trực tuyến của Đông Nam Á năm 2022 là 130 tỷ USD . [sach-trang-tmdt-2023:p031:B01] [sach-trang-tmdt-2023:p34:V1]
- search_documents: `eMarketer doanh thu bán lẻ thương mại điện tử Đông Nam Á 2022` → p31, p31, p31, p31, p34
- search_documents: `e-Conomy SEA doanh thu bán lẻ hàng hóa trực tuyến Đông Nam Á 2022` → p34, p35, p31, p31, p37
- read_page: `page 34` → p34, p34, p34, p34

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

> **[sach-trang-tmdt-2023:p34:V1]** [bar_chart] 1. Quy mô nền kinh tế Internet phân theo lĩnh vực
(Trang 34, nửa trên; đơn vị: Tỷ USD)
Doanh thu bán lẻ hàng hóa trực tuyến — 2022: 130
Doanh thu bán lẻ hàng hóa trực tuyến — 2023: 139
Doanh thu bán lẻ hàng hóa trực tuyến — 2025*: 186
Doanh thu vận tải và giao đồ ăn — 2022: 18
Doanh thu vận tải và giao đồ ăn — 2023: 23
Doanh thu vận tải và giao đồ ăn — 2025*: 34
Doanh thu du lịch trực tuyến — 2022: 30
Doanh thu du lịch trực tuyến — 2023: 24
Doanh thu du lịch trực tuyến — 2025*: 26
Doanh thu nội dung nghe nhìn trực tuyến — 2022: 24
Doanh thu nội dung nghe nhìn trực tuyến — 2023: 26
Doanh thu nội dung nghe nhìn trực tuyến — 2025*: 31
Tốc độ tăng trưởng doanh thu bán lẻ hàng hóa trự

## v19 · multihop · có đáp án
**Câu hỏi:** Hà Nội chiếm bao nhiêu phần trăm số lượng đơn hàng thành công của website/ứng dụng TMĐT bán hàng, và bao nhiêu phần trăm số người bán trên website/ứng dụng cung cấp dịch vụ TMĐT?
**Đáp án chuẩn:** 21,8% đơn hàng thành công (website bán hàng); 21,5% người bán (website CCDV).  
**Evidence:** tr.77 — Biểu đồ 3. Tỷ lệ số lượng đơn hàng thành công của website TMĐT bán hàng theo tỉnh/thành, mục Hà Nội; tr.81 — Biểu đồ 3.1 Tỷ lệ người bán theo địa phương (website CCDV), mục Hà Nội
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 133.72s):** Năm 2023, Hà Nội chiếm 21,8% số lượng đơn hàng thành công của website/ứng dụng thương mại điện tử bán hàng . Hà Nội cũng chiếm 21,5% số người bán trên website/ứng dụng cung cấp dịch vụ thương mại điện tử . [sach-trang-tmdt-2023:p077:B00] [sach-trang-tmdt-2023:p081:B00]
- search_documents: `Hà Nội tỷ lệ đơn hàng thành công website TMĐT bán hàng` → p77, p77, p81, p82, p82
- search_documents: `Hà Nội tỷ lệ người bán website cung cấp dịch vụ TMĐT` → p81, p77, p77, p79, p79

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

> **[sach-trang-tmdt-2023:p081:B00]** 3. Tình hình hoạt động của website/ứng dụng cung cấp dịch vụ TMĐT theo địa phương
3.1. Tỷ lệ người bán theo địa phương
TP. | Hồ Chí | Minh | 37,3 %
Hà Nội | 21,5%
Đà Nẵng | 4,2 | %
Bình | Dư | ơng | 3,9%
Cần | Thơ | 2,9 %
Đồng Nai | 2,4 %
Hải Phòng | 1,9 %
Lâm | Đồng | 1,8 %
Nghệ An | 1,8 %
Khá | nh H | òa 1,7%
Bà Rịa - Vũng | Tàu | 1,6%
Lon | g An | 1,5%
Hải Dư | ơng1,2 %
Hư | ng Yên | 1,0%
Vĩn | h Phúc | 1,0 %
Quảng | Ninh1,0%
Than | h Hóa | 1,0%
Nam | Định | 1,0%
Bắc Ninh | 0,9%
Thái | Nguyên | 0,6 %
Các tỉnh/thành phố còn | lại | 10,0 %

## v20 · multihop · có đáp án
**Câu hỏi:** Lazada được bao nhiêu phần trăm người tiêu dùng ưa chuộng trong lĩnh vực bán buôn bán lẻ, và doanh nghiệp nào vận hành Lazada theo danh sách doanh nghiệp dẫn đầu thị trường?
**Đáp án chuẩn:** 42%; Công ty TNHH Recess.  
**Evidence:** tr.46 — Biểu đồ cột 6.1, cột Lazada; tr.83 — Bảng 4.1 STT 5 / bảng 4.2 STT 1
**auto:** context đủ evidence = True
**Agent (answered, 4 tool call, 144.16s):** Năm 2023, Lazada được 42% người tiêu dùng ưa chuộng trong lĩnh vực bán buôn bán lẻ. Doanh nghiệp vận hành Lazada theo danh sách doanh nghiệp dẫn đầu thị trường là Công ty TNHH Recess. [sach-trang-tmdt-2023:p046:B01] [sach-trang-tmdt-2023:p083:B01]
- search_documents: `Lazada ưa chuộng bán buôn bán lẻ` → p46, p46, p46, p83, p46
- search_documents: `doanh nghiệp vận hành Lazada` → p83, p83, p83, p83, p85
- read_page: `page 83` → p83, p83, p83, p83
- read_page: `page 46` → p46, p46, p46, p46, p46, p46, p46

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

## v21 · text · có đáp án
**Câu hỏi:** Theo Lời giới thiệu của Sách trắng, tăng trưởng GDP cả năm 2023 của Việt Nam khoảng bao nhiêu?
**Đáp án chuẩn:** Khoảng 5%.  
**Evidence:** tr.3 — Lời giới thiệu, đoạn 1
**auto:** context đủ evidence = True
**Agent (answered, 1 tool call, 70.13s):** Theo Lời giới thiệu của Sách trắng Thương mại điện tử Việt Nam năm 2023, tăng trưởng GDP cả năm 2023 của Việt Nam khoảng 5%. [sach-trang-tmdt-2023:p003:B00]
- search_documents: `Lời giới thiệu tăng trưởng GDP 2023` → p3, p33, p37, p33, p37

> **[sach-trang-tmdt-2023:p003:B00]** LỜI GIỚI THIỆU
Kinh tế Việt Nam 2023 duy trì xu hướng phục hồi, tiếp tục là điểm sáng của kinh tế toàn cầu (theo Cổng
Thông tin điện tử Chính phủ). Kinh tế vĩ mô cơ bản ổn định; lạm phát thấp hơn mục tiêu Quốc hội đề ra; nợ
công, nợ Chính phủ, nợ nước ngoài, bội chi ngân sách nhà nước được kiểm soát; tăng trưởng được thúc đẩy;
các cân đối lớn của nền kinh tế được bảo đảm. Tăng trưởng GDP cả năm khoảng 5% thuộc nhóm các nước tăng
trưởng cao trong khu vực và thế giới.
Trong bức tranh tổng thể về kinh tế Việt Nam, thương mại điện tử tiếp tục khẳng định vị trí là một trong
những lĩnh vực tiên phong của nền kinh tế số. Năm 2023, quy mô thị trường thương mại điện tử bán lẻ Việt
Nam đạt 20,5 tỷ USD

## v22 · text · có đáp án
**Câu hỏi:** Nghị định số 91/2022/NĐ-CP sửa đổi, bổ sung một số điều của nghị định nào?
**Đáp án chuẩn:** Nghị định số 126/2020/NĐ-CP ngày 19/10/2020 quy định chi tiết một số điều của Luật Quản lý thuế.  
**Evidence:** tr.19 — Mục 3, đoạn mở đầu
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 118.49s):** Nghị định số 91/2022/NĐ-CP sửa đổi, bổ sung một số điều của Nghị định số 126/2020/NĐ-CP ngày 19 tháng 10 năm 2020 của Chính phủ quy định chi tiết một số điều của Luật Quản lý thuế. [sach-trang-tmdt-2023:p019:B00]
- search_documents: `Nghị định số 91/2022/NĐ-CP sửa đổi nghị định nào` → p19, p89, p89, p93, p93
- read_page: `page 19` → p19, p19, p19

> **[sach-trang-tmdt-2023:p019:B00]** 3. Nghị định số 91/2022/NĐ-CP ngày 30 tháng 10 năm 2022 của Chính phủ
Nghị định số 91/2022/NĐ-CP sửa đổi, bổ sung một số điều của Nghị định số 126/2020/NĐ-CP ngày 19 tháng 10
năm 2020 của Chính phủ quy định chi tiết một số điều của Luật Quản lý thuế. Theo đó, Nghị định bổ sung quy
định về trách nhiệm của chủ sở hữu sàn giao dịch thương mại điện tử.
Việc cung cấp thông tin được thực hiện định kỳ hàng quý chậm nhất vào ngày cuối cùng
của tháng đầu quý sau, bằng phương thức điện tử, qua Cổng thông tin điện tử của Tổng
cục Thuế theo định dạng dữ liệu do Tổng cục Thuế công bố.

## v23 · text · có đáp án
**Câu hỏi:** Theo Nghị định 13/2023/NĐ-CP, nếu thông báo vi phạm quy định bảo vệ dữ liệu cá nhân cho Bộ Công an sau thời hạn quy định thì phải làm gì?
**Đáp án chuẩn:** Thời hạn là chậm nhất 72 giờ; nếu thông báo sau 72 giờ thì phải kèm theo lý do thông báo chậm, muộn.  
**Evidence:** tr.22 — Khối '4 Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân', ý 2
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 110.65s):** Theo Nghị định 13/2023/NĐ-CP, nếu thông báo vi phạm quy định bảo vệ dữ liệu cá nhân cho Bộ Công an sau thời hạn 72 giờ thì phải kèm theo lý do thông báo chậm, muộn. [sach-trang-tmdt-2023:p022:B00]
- search_documents: `Nghị định 13/2023/NĐ-CP thông báo vi phạm quy định bảo vệ dữ liệu cá nhân cho Bộ Công an sau thời hạn` → p22, p23, p23, p20, p20
- read_page: `page 22` → p22

> **[sach-trang-tmdt-2023:p022:B00]** 4. Nghị định số 13/2023/NĐ-CP ngày 17 tháng 4 năm 2023 của Chính phủ
3
4
Trường hợp xử lý dữ liệu cá nhân không cần sự đồng ý của chủ thể dữ liệu
Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân
Trường hợp khẩn cấp, cần xử lý ngay dữ liệu cá nhân có liên
quan để bảo vệ tính mạng, sức khỏe của chủ thể dữ liệu hoặc
người khác;
Việc công khai dữ liệu cá nhân theo quy định của luật.
Việc xử lý dữ liệu của cơ quan nhà nước có thẩm quyền trong
trường hợp tình trạng khẩn cấp về quốc phòng, an ninh quốc
gia, trật tự an toàn xã hội, thảm họa lớn, dịch bệnh nguy hiểm,...
Để thực hiện nghĩa vụ theo hợp đồng của chủ thể dữ liệu với cơ
quan, tổ chức, cá nhân có liên quan theo quy định của luật;
Phục 

## v24 · text · có đáp án
**Câu hỏi:** Theo Nghị định 13/2023/NĐ-CP, trong trường hợp chuyển dữ liệu cá nhân ra nước ngoài, bên chuyển dữ liệu phải gửi hồ sơ tới Bộ Công an như thế nào?
**Đáp án chuẩn:** Gửi 01 bản chính hồ sơ tới Bộ Công an trong thời gian 60 ngày kể từ ngày tiến hành xử lý dữ liệu cá nhân.  
**Evidence:** tr.24 — Khối '6 Đánh giá tác động xử lý dữ liệu cá nhân', ý 4
**auto:** context đủ evidence = True
**Agent (answered, 2 tool call, 57.82s):** Theo Nghị định 13/2023/NĐ-CP, trong trường hợp chuyển dữ liệu cá nhân ra nước ngoài, bên chuyển dữ liệu phải gửi 01 bản chính hồ sơ đánh giá tác động xử lý dữ liệu cá nhân tới Bộ Công an trong thời gian 60 ngày kể từ ngày tiến hành xử lý dữ liệu cá nhân . [sach-trang-tmdt-2023:p024:B01]
- search_documents: `chuyển dữ liệu cá nhân ra nước ngoài Nghị định 13/2023/NĐ-CP gửi hồ sơ Bộ Công an` → p24, p23, p22, p23, p20
- read_page: `page 24` → p24, p24

> **[sach-trang-tmdt-2023:p024:B01]** 1. Mục tiêu
6 Đánh giá tác động xử lý dữ liệu cá nhân
Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá
nhân lập và lưu giữ Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân
của mình kể từ thời điểm bắt đầu xử lý dữ liệu cá nhân.
Bên Xử lý dữ liệu cá nhân tiến hành lập và lưu giữ Hồ sơ đánh giá tác
động xử lý dữ liệu cá nhân trong trường hợp thực hiện hợp đồng
với Bên Kiểm soát dữ liệu cá nhân.
Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải luôn có sẵn để
phục vụ hoạt động kiểm tra, đánh giá của Bộ Công an và gửi Bộ
Công an 01 bản chính trong thời gian 60 ngày kể từ ngày tiến hành
xử lý dữ liệu cá nhân.
Trường hợp chuyển dữ liệu cá nhân ra nước ngoài, bên chuyển dữ
liệu ra nướ

## v25 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Đức là bao nhiêu?
**Lý do thiếu:** Biểu đồ 1.5 (tr. 30) không có Đức; 'Đức' chỉ xuất hiện ở tr. 32 (thị phần TMĐT 2,1%) và tr. 11 (chữ 'đức' trong 'đạo đức').
**Agent (abstain, 7 tool call, 91.96s):** Không đủ bằng chứng để trả lời.
- search_documents: `tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Đức` → p29, p29, p30, p44, p30
- search_documents: `Đức tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần` → p29, p29, p30, p44, p30
- read_page: `page 30` → p30, p30, p30
- search_documents: `Đức` → p32, p32, p32, p63, p32
- read_page: `page 29` → p29, p29, p29, p29
- read_page: `page 31` → p31, p31, p31, p31
- read_page: `page 28` → p28, p28, p28, p28
- abstain: Tài liệu không có số liệu về tỷ lệ người dùng Internet mua sắm trực tuyến hàng tuần tại Đức. Chỉ có số liệu trung bình toàn cầu và một số quốc gia châu Á, không có Đức.

## v26 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Theo dự báo trong Sách trắng, doanh thu TMĐT B2C của Mỹ năm 2028 là bao nhiêu?
**Lý do thiếu:** Biểu đồ 2.7 Mỹ (tr. 33) chỉ dự báo đến 2027* (1.720 tỷ USD); '2028' không xuất hiện trong toàn văn.
**Agent (abstain, 7 tool call, 100.64s):** Không đủ bằng chứng để trả lời.
- search_documents: `doanh thu TMĐT B2C của Mỹ năm 2028` → p30, p40, p32, p31, p31
- search_documents: `dự báo doanh thu TMĐT B2C Mỹ năm 2028` → p30, p33, p40, p31, p32
- read_page: `page 33` → p33, p33, p33, p33
- search_documents: `doanh thu TMĐT B2C Mỹ năm 2028` → p30, p40, p31, p31, p32
- read_page: `page 34` → p34, p34, p34, p34
- read_page: `page 35` → p35, p35, p35, p35, p35, p35, p35
- read_page: `page 36` → p36, p36, p36, p36, p36, p36, p36
- abstain: Sách trắng Thương mại điện tử Việt Nam 2023 không có số liệu dự báo doanh thu TMĐT B2C của Mỹ năm 2028. Số liệu dự báo chỉ đến năm 2027.

## v27 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Bao nhiêu phần trăm người tiêu dùng ưa chuộng Shopee trong lĩnh vực du lịch trực tuyến?
**Lý do thiếu:** Biểu đồ 6.4 (tr. 47) du lịch trực tuyến chỉ có Traveloka, Agoda, Booking.com, Gotadi, Tripi Partner, AirBnB, Khác; Shopee chỉ có ở mảng bán buôn bán lẻ (tr. 46).
**Agent (abstain, 4 tool call, 226.39s):** Không đủ bằng chứng để trả lời.
- search_documents: `Shopee du lịch trực tuyến` → p47, p47, p47, p47, p85
- search_documents: `Shopee du lịch trực tuyến` → p47, p47, p47, p47, p85
- read_page: `page 47` → p47, p47, p47, p47, p47, p47, p47
- search_documents: `Shopee du lịch trực tuyến` → p47, p47, p47, p47, p85
- abstain: Không có số liệu về tỷ lệ người tiêu dùng ưa chuộng Shopee trong lĩnh vực du lịch trực tuyến. Các số liệu chỉ có cho Traveloka, Agoda, Booking.com, Gotadi, Tripi Partner, AirBnB và nhóm 'Khác', không có Shopee.

## v28 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Quy mô thị trường TMĐT bán lẻ của Lào năm 2023 là bao nhiêu?
**Lý do thiếu:** Các biểu đồ Đông Nam Á (tr. 34–37) chỉ có Indonesia, Thái Lan, Việt Nam, Philippines, Malaysia, Singapore; 'Lào' không xuất hiện trong toàn văn.
**Agent (abstain, 7 tool call, 158.65s):** Không đủ bằng chứng để trả lời.
- search_documents: `quy mô thị trường thương mại điện tử bán lẻ Lào 2023` → p3, p40, p30, p34, p34
- search_documents: `quy mô thị trường thương mại điện tử bán lẻ Lào` → p30, p3, p83, p40, p83
- search_documents: `Lào` → p32, p32, p35, p35, p36
- search_documents: `Lào Đông Nam Á` → p34, p35, p36, p36, p35
- search_documents: `quy mô thị trường thương mại điện tử bán lẻ Lào năm 2023` → p3, p40, p30, p46, p57
- read_page: `page 34` → p34, p34, p34, p34
- read_page: `page 35` → p35, p35, p35, p35, p35, p35, p35
- abstain: Không tìm thấy số liệu về quy mô thị trường thương mại điện tử bán lẻ của Lào năm 2023 trong Sách trắng Thương mại điện tử Việt Nam 2023. Tài liệu chỉ có số liệu của các nước lớn Đông Nam Á như Indonesia, Thái Lan, Việt Nam, Philippines, Malaysia, Singapore.

## v29 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Chi phí giao hàng chặng cuối trung bình cho mỗi đơn hàng TMĐT là bao nhiêu đồng?
**Lý do thiếu:** Tài liệu chỉ có tỷ lệ chi phí hoàn tất đơn hàng và giao hàng chặng cuối so với doanh thu theo nhóm % (tr. 64), không có chi phí tuyệt đối mỗi đơn.
**Agent (abstain, 7 tool call, 117.11s):** Không đủ bằng chứng để trả lời.
- search_documents: `chi phí giao hàng chặng cuối trung bình` → p64, p64, p50, p61, p61
- search_documents: `chi phí giao hàng chặng cuối trung bình cho mỗi đơn hàng` → p64, p64, p50, p61, p61
- search_documents: `chi phí giao hàng chặng cuối trung bình đồng` → p64, p64, p61, p50, p61
- search_documents: `chi phí giao hàng chặng cuối trung bình mỗi đơn hàng` → p64, p64, p50, p61, p61
- read_page: `page 64` → p64, p64, p64, p64, p64
- search_documents: `chi phí giao hàng chặng cuối trung bình đồng 2023` → p64, p64, p50, p82, p50
- search_documents: `chi phí giao hàng chặng cuối trung bình mỗi đơn hàng đồng` → p64, p64, p50, p61, p61
- abstain: Tài liệu chỉ cung cấp tỷ lệ chi phí giao hàng chặng cuối so với doanh thu TMĐT (theo phần trăm), không có số liệu chi phí giao hàng chặng cuối trung bình cho mỗi đơn hàng tính theo đồng.

## v30 · unanswerable · thiếu bằng chứng
**Câu hỏi:** Có bao nhiêu doanh nghiệp tại Hà Nội tham gia khảo sát ứng dụng TMĐT năm 2023?
**Lý do thiếu:** Tr. 54 chỉ nêu tổng 5.531 doanh nghiệp khảo sát và phân loại theo loại hình, lĩnh vực, quy mô; không có số doanh nghiệp theo tỉnh/thành.
**Agent (abstain, 7 tool call, 105.14s):** Không đủ bằng chứng để trả lời.
- search_documents: `số doanh nghiệp Hà Nội tham gia khảo sát 2023` → p55, p54, p55, p59, p54
- search_documents: `số doanh nghiệp Hà Nội tham gia khảo sát` → p54, p55, p54, p55, p59
- read_page: `page 54` → p54, p54, p54
- search_documents: `doanh nghiệp Hà Nội tham gia khảo sát` → p54, p55, p54, p55, p59
- read_page: `page 55` → p55, p55, p55
- search_documents: `doanh nghiệp theo địa phương tham gia khảo sát` → p54, p54, p55, p55, p82
- search_documents: `doanh nghiệp tham gia khảo sát theo địa phương` → p54, p54, p55, p55, p59
- abstain: Không tìm thấy số lượng doanh nghiệp tại Hà Nội tham gia khảo sát ứng dụng TMĐT năm 2023 trong tài liệu. Tài liệu chỉ có tổng số doanh nghiệp khảo sát toàn quốc, không có số liệu riêng cho Hà Nội.
