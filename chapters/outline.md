# BẢN ĐỒ MỘT TRANG · Đọc trước khi vào chi tiết

**Một câu.** Cẩm nang tự học cho sinh viên năm 1–2 Công nghệ thông tin, Đại học Thủy lợi: dùng AI để làm bài tập lập trình mà **không giao phần suy nghĩ cho công cụ**.

**Không phải là** quy định chính thức của trường, giáo trình học phần, quảng cáo công cụ hay bảng giá. Minh và Lan, mọi hội thoại, phiếu khảo sát và mọi con số chi phí là **hư cấu hoặc giả định** để học. Rubric trong sách là rubric luyện tập.

## Bốn chặng và dự án tổng kết

| Chặng | Sau chặng này, bạn làm được gì | Gợi ý xếp lịch | Sản phẩm tự làm |
|---|---|---|---|
| [01 · Bước vào thế giới AI](#chuong-1) | Phân biệt model / provider / application / producer; tính được chi phí một việc; chọn công cụ theo việc, không theo danh tiếng | 6 mục ≈ 3 ca 45 phút | Một bản nhận diện có phần "chưa biết", một prompt đủ ngữ cảnh, một phép tính chi phí |
| [02 · Trở thành người điều khiển AI](#chuong-2) | Điều khiển quá trình qua **bảy Mission**: đọc môi trường, hỏi đúng, debug C++, debug Web, giao Agent có giới hạn, đọc diff, nghiệm thu | 7 Mission ≈ 4 ca 45 phút | ViSinhVien chạy được, hai lỗi đã sửa, bảng test, diff |
| [03 · Đừng để AI suy nghĩ thay bạn](#chuong-3) | Viết dự đoán **trước** khi hỏi; dùng phản ví dụ nhỏ bác bỏ kết luận tự tin; giải thích lại không cần mở chat | 7 mục ≈ 3 ca 45 phút | Bảng trace, kết quả tự quan sát, bài giải thích 6 phút |
| [04 · Sử dụng AI có trách nhiệm](#chuong-4) | Xử lý **bảy hồ sơ sự cố**: key bị lộ, dữ liệu cá nhân, Agent vượt phạm vi, gói thư viện, bài làm hộ, mã không rõ giấy phép, khai báo thiếu | 7 hồ sơ ≈ 4 ca 45 phút | Biên bản sự cố, phiếu bằng chứng, bản khai báo AI |
| [FINAL BOSS](#final-boss) | Ghép bốn chặng thành một bản nộp có bằng chứng: **làm được — biết là đúng — giải thích được** | Bronze 60–90; Silver 90–120; Gold +30–45 phút | Code bản sao, hai bản vá, test, diff, khai báo AI, bảo vệ 8 phút |

Gợi ý xếp lịch chỉ là phép tính từ đơn vị 20–25 phút cho một mục ở [phần Mở đầu](#bat-dau). Đây **không** phải yêu cầu của học phần và không phải thước đo tốc độ.

## Vào thẳng chỗ cần

**Bảy Mission — Chương 2:** [01 môi trường](#muc-2-1) · [02 hỏi đúng](#muc-2-2) · [03 debug C++](#muc-2-3) · [04 debug Web](#muc-2-4) · [05 Agent có giới hạn](#muc-2-5) · [06 đọc diff](#muc-2-6) · [07 nghiệm thu](#muc-2-7)

**Bảy hồ sơ sự cố — Chương 4:** [01 key trên GitHub](#muc-4-1) · [02 dữ liệu cá nhân](#muc-4-2) · [03 Agent vượt phạm vi](#muc-4-3) · [04 gói thư viện](#muc-4-4) · [05 bài làm hộ](#muc-4-5) · [06 giấy phép](#muc-4-6) · [07 khai báo thiếu](#muc-4-7) · [phòng khám SQL/XSS/C++](#muc-4-8)

**Bộ công cụ:** [11 mẫu prompt P01–P11](#prompt-library) · [từ điển tra nhanh](#glossary) · [thỏa thuận học tập và mẫu khai báo AI](#learning-agreement) · [demo ViSinhVien](../vi-du/nam-2-web/index.html)

## Một hợp đồng số liệu chạy xuyên suốt

Ba khoản giả **35000 + 7000 + 18000 = 60000**; tiền nguyên VND từ **1 đến 1000000000**; tối đa **500 khoản**; danh sách rỗng trả **0**; tổng cực đại **500000000000**. Cùng một hợp đồng, bốn cách kiểm khác nhau:

| Bộ kiểm | Số ca | Trạng thái trong gói |
|---|---:|---|
| Demo C++ đúng `vi-du/nam-1-cpp/vi_sinh_vien.cpp --test` | 9 | đã chạy, đạt |
| Demo dữ liệu Web `vi-du/nam-2-web/test_data.cjs` | 34 | đã chạy, đạt |
| Đề Bronze `vi-du/final-boss/bronze.cpp` | 9 | **5 đạt, 4 lỗi chủ đích** — bạn phải sửa |
| Đề Silver `vi-du/final-boss/test_silver.cjs` | 12 | **6 đạt, 6 lỗi chủ đích** — bạn phải sửa |

Bốn bộ **không cộng gộp** và không thay nhau. `loi-bo-sot.cpp` in ra 42000 và không có `--test`; đó là đồ dùng học, không phải bài đã kiểm.

## Nếu bạn chỉ có 60 phút

Đọc trang này → làm [1.6 MINI CHALLENGE](#muc-1-6) → xem [Mission 03](#muc-2-3) → đọc [Hồ sơ 01](#muc-4-1). Bỏ qua được phần còn lại mà không hỏng mạch.

## Nếu bạn là giảng viên

Dùng [bảng rubric 100 điểm của Final Boss](#final-boss-7-bang-nghiem-thu-va-rubric-100-diem) làm thang chấm luyện tập, [thỏa thuận học tập](#learning-agreement) làm phiếu nộp đầu kỳ, và [bảy hồ sơ Chương 4](#muc-4-1) làm tình huống thảo luận 15 phút. Câu hỏi biến thể ở [mục 8 Final Boss](#final-boss-8-buoi-bao-ve-ngan) dùng được cho vấn đáp.

## Đã kiểm chứng tới đâu — và phần nào chưa

**Đã chạy trên máy biên tập:** 46 phép kiểm cấu trúc nội dung; 16 phép kiểm ví dụ thực thi (Node 24, Python 3.14, g++ 11.4 trong WSL); 80 phép kiểm trong trình duyệt Chrome 156, gồm 16 hình SVG, ba cỡ màn hình, bản in PDF 159 trang và xác nhận **không gửi yêu cầu ra mạng**. Nhật ký giữ cả lần thất bại — xem [báo cáo chất lượng](../reports/04_QUALITY_REPORT.md).

**Chưa kiểm:** chỉ một trình duyệt trên một hệ điều hành; PDF chưa soát từng trang; giá, quota và quyền lợi của các dịch vụ AI chưa xác minh độc lập; **chưa thử với lớp sinh viên thật**; lộ trình Gold chưa vận hành Agent thật. Nguồn pháp luật giữ mốc đối chiếu 29/10/2026.

Gặp một con số không có ở trang này, hãy tìm nhãn **HƯ CẤU**, **GIẢ ĐỊNH** hoặc **chưa kiểm** cạnh nó. Không có nhãn nào thì coi là điều cần hỏi lại.
