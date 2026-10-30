# BẢN ĐỒ NỘI DUNG

**Tóm lược.** Đây là **Sổ tay thực hành** đi kèm [Cẩm nang khởi đầu](../cam-nang/introduction.md), dành cho sinh viên năm thứ nhất và năm thứ hai ngành Công nghệ thông tin, Trường Đại học Thủy lợi. Cẩm nang nêu ý chính và việc nhỏ để thử; sổ tay này chứa bản đầy đủ của các bài thực hành, hồ sơ tình huống, đáp án và rubric. Mục đích chung là hướng dẫn sử dụng AI khi làm bài tập lập trình mà **không giao phần suy nghĩ cho công cụ**: hiểu vai trò của AI, dùng có kiểm soát, giữ việc học, giữ trách nhiệm, rồi mới chọn công cụ.

**Phạm vi.** Sách không phải quy định chính thức của Trường, không phải đề cương học phần, không phải tài liệu quảng cáo công cụ và không phải bảng giá. Minh và Lan, mọi hội thoại, phiếu khảo sát và con số chi phí trong sách là tình huống hư cấu hoặc dữ liệu giả định phục vụ học tập. Rubric trong sách là rubric luyện tập. Tuyên bố phạm vi đầy đủ được trình bày trong [Lời giới thiệu](introduction.md).

## Năm chương và dự án tổng kết

Sách đi theo năm bước: Hiểu, Dùng, Giữ vững, Có trách nhiệm, Chọn. Việc chọn model và gói dịch vụ nằm ở cuối vì chỉ khi hiểu vai trò, cách dùng và ranh giới của AI, người học mới chọn công cụ có cơ sở. Câu chốt xuyên suốt: AI hỗ trợ, người học quyết định.

| Phần | Kết quả đạt được sau phần này | Gợi ý xếp lịch | Sản phẩm người học tự làm |
|---|---|---|---|
| [Chương 1 · AI trong học tập: vai trò, cách hoạt động và giới hạn](chapter-01.md) | Nêu được lợi ích, giới hạn, cách dùng đúng và lạm dụng; phân biệt model, provider, ứng dụng (application) và nhà sản xuất (producer); hiểu prompt, context và token ảnh hưởng thế nào đến một câu trả lời | 3 mục, khoảng 2 ca 45 phút | Một bảng phân loại việc dùng đúng và lạm dụng, một bản nhận diện công cụ có phần "chưa biết", một prompt đủ ngữ cảnh |
| [Chương 2 · Điều khiển quá trình làm việc với AI](chapter-02.md) | Điều khiển quá trình làm việc qua bảy bài thực hành (**bảy Mission**): đọc môi trường, hỏi đúng, debug C++, debug Web, giao việc cho Agent có giới hạn, đọc diff, nghiệm thu | 7 bài thực hành, khoảng 4 ca 45 phút | ViSinhVien chạy được, hai lỗi đã sửa, bảng kiểm thử, diff |
| [Chương 3 · Học chủ động: dùng AI mà không lạm dụng](chapter-03.md) | Viết dự đoán **trước** khi hỏi; dùng phản ví dụ nhỏ để bác bỏ một kết luận tự tin; giải thích lại mà không cần mở cửa sổ chat | 7 mục, khoảng 3 ca 45 phút | Bảng trace, kết quả tự quan sát, bài giải thích trong 6 phút |
| [Chương 4 · Sử dụng AI có trách nhiệm](chapter-04.md) | Xử lý **bảy hồ sơ** sự cố: khóa API bị lộ, dữ liệu cá nhân, Agent vượt phạm vi, gói thư viện, bài làm hộ, mã không rõ giấy phép, khai báo thiếu | 7 hồ sơ, khoảng 4 ca 45 phút | Biên bản sự cố, phiếu bằng chứng, bản khai báo sử dụng AI |
| [Chương 5 · Lựa chọn AI và model phù hợp với nhiệm vụ](chapter-05.md) | Tính được chi phí cho một việc; ưu tiên phương án miễn phí khi đủ dùng; đối chiếu công cụ theo tác vụ; chọn theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng | 4 mục, khoảng 2 ca 45 phút | Một phép tính chi phí từ giả định, một bảng đối chiếu công cụ, một quyết định có lý do |
| [Dự án tổng kết](final-boss.md) | Ghép năm bước thành một bản nộp có bằng chứng: **làm được, biết là đúng, giải thích được** | Cấp Bronze 60–90 phút; cấp Silver 90–120 phút; cấp Gold thêm 30–45 phút | Mã nguồn trên bản sao, hai bản vá, kiểm thử, diff, khai báo sử dụng AI, buổi bảo vệ 8 phút |

Gợi ý xếp lịch được tính từ đơn vị 20–25 phút cho một mục, như mô tả trong [Lời giới thiệu](introduction.md). Đây **không** phải yêu cầu của học phần và không phải thước đo tốc độ.

## Truy cập nhanh

**Bảy bài thực hành của Chương 2:** [01 · Môi trường làm việc](#muc-2-1) · [02 · Hỏi đúng](#muc-2-2) · [03 · Debug C++](#muc-2-3) · [04 · Debug Web](#muc-2-4) · [05 · Agent có giới hạn](#muc-2-5) · [06 · Đọc diff](#muc-2-6) · [07 · Nghiệm thu](#muc-2-7)

**Bảy hồ sơ sự cố của Chương 4:** [01 · Khóa API trên GitHub](#muc-4-1) · [02 · Dữ liệu cá nhân](#muc-4-2) · [03 · Agent vượt phạm vi](#muc-4-3) · [04 · Gói thư viện](#muc-4-4) · [05 · Bài làm hộ](#muc-4-5) · [06 · Giấy phép](#muc-4-6) · [07 · Khai báo thiếu](#muc-4-7) · [SQL, XSS và C++ (mục 4.8)](#muc-4-8)

**Chọn công cụ và chi phí (Chương 5):** [5.1 · Chi phí](#muc-5-1) · [5.2 · Ưu tiên miễn phí](#muc-5-2) · [5.3 · Đối chiếu công cụ](#muc-5-3) · [5.4 · Bài tập tổng hợp](#muc-5-4)

**Tài liệu đi kèm:** [Thư viện prompt mẫu P01–P11](prompt-library.md) · [Bảng thuật ngữ](glossary.md) · [Thỏa thuận học tập và mẫu khai báo sử dụng AI](learning-agreement.md) · [Ứng dụng minh họa ViSinhVien](../vi-du/nam-2-web/index.html)

## Hợp đồng dữ liệu xuyên suốt

Ba khoản chi giả định **35000 + 7000 + 18000 = 60000**; số tiền là số nguyên VND từ **1 đến 1000000000**; tối đa **500 khoản**; danh sách rỗng có tổng **0**; tổng cực đại là **500000000000**. Cùng một hợp đồng dữ liệu được kiểm tra bằng bốn bộ kiểm thử khác nhau:

| Bộ kiểm thử | Số ca | Trạng thái trong gói tài liệu |
|---|---:|---|
| Ví dụ C++ đúng `vi-du/nam-1-cpp/vi_sinh_vien.cpp --test` | 9 | Đã chạy, đạt |
| Ví dụ dữ liệu Web `vi-du/nam-2-web/test_data.cjs` | 34 | Đã chạy, đạt |
| Đề cấp Bronze `vi-du/final-boss/bronze.cpp` | 9 | **5 ca đạt, 4 ca lỗi chủ đích**; người học cần sửa |
| Đề cấp Silver `vi-du/final-boss/test_silver.cjs` | 12 | **6 ca đạt, 6 ca lỗi chủ đích**; người học cần sửa |

Bốn bộ kiểm thử **không cộng gộp** và không thay thế cho nhau. Tệp `loi-bo-sot.cpp` in ra 42000 và không có chế độ `--test`; đây là học liệu để phân tích lỗi, không phải bài đã được kiểm thử.

## Lộ trình đọc rút gọn trong 60 phút

Đọc trang này, sau đó làm [Bài tập tổng hợp (mục 5.4)](#muc-5-4), xem [Bài thực hành 03 (mục 2.3)](#muc-2-3) và đọc [Hồ sơ 01 (mục 4.1)](#muc-4-1). Các phần còn lại có thể đọc sau mà không ảnh hưởng đến mạch nội dung.

## Dành cho giảng viên

Bảng rubric 100 điểm ở mục 7 của [Dự án tổng kết](final-boss.md) có thể dùng làm thang chấm luyện tập. [Thỏa thuận học tập](learning-agreement.md) có thể dùng làm phiếu nộp đầu kỳ. [Bảy hồ sơ của Chương 4](#muc-4-1) phù hợp làm tình huống thảo luận trong 15 phút. Các câu hỏi biến thể ở mục 8 của Dự án tổng kết có thể dùng cho phần vấn đáp.

## Phạm vi kiểm chứng của bản phát hành

**Đã kiểm tra:** cấu trúc nội dung, ví dụ thực thi và giao diện; xem báo cáo chất lượng trong kho mã.

**Chưa kiểm chứng:** mới thử trên một trình duyệt và một hệ điều hành; bản PDF chưa được soát từng trang; giá, hạn mức (quota) và quyền lợi của các dịch vụ AI chưa được xác minh độc lập; **chưa thử nghiệm với lớp sinh viên thực tế**; lộ trình cấp Gold chưa được vận hành với Agent thật. Các nguồn pháp luật giữ mốc đối chiếu 29/10/2026.

Khi gặp một con số không có trên trang này, người đọc cần tìm nhãn đi kèm: *Tình huống hư cấu*, *Dữ liệu giả định*, *Chưa kiểm chứng* hoặc *Kết quả mong đợi*. Con số không có nhãn nào cần được xem là điều phải hỏi lại.
