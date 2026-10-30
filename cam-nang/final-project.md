# DỰ ÁN TỔNG KẾT: LÀM, KIỂM, GIẢI THÍCH

Năm chương trước đã đi qua năm bước: hiểu, dùng, giữ vững, có trách nhiệm và chọn. Dự án tổng kết ghép cả năm bước thành một sản phẩm nhỏ có bằng chứng. Số liệu trong dự án là *Dữ liệu giả định*; không nhập chi tiêu thật vào bài làm.

## Đề bài

Đối tượng vẫn là ứng dụng ViSinhVien với ba khoản 35000 + 7000 + 18000 = 60000; không cần xây dựng ứng dụng mới. Điều cần luyện không phải là dùng công cụ AI mạnh nhất, mà là trả lời được ba câu hỏi bằng bằng chứng: sản phẩm làm gì và việc gì nằm ngoài phạm vi; căn cứ nào cho thấy sản phẩm đúng; khi không mở cửa sổ chat, người học còn tự giải thích được những gì. Câu "AI bảo là đúng" không phải bằng chứng. Phần nào còn thiếu bằng chứng phải ghi rõ là thiếu, không dùng giao diện đẹp để thay thế.

![Bronze thực hành C++, Silver thực hành Web, Gold nâng quy trình kiểm soát Agent từ một trong hai nhánh: quyền, diff, test, review, khai báo. Không cần trả phí; không có AI có thể mô phỏng thủ công và ghi rõ.](../assets/final-boss.svg)

## Ba cấp độ

Chọn cấp theo năng lực cần luyện; cấp cao hơn không có nghĩa là viết nhiều mã hơn.

**Bronze · C++ cơ bản** theo nhánh của Minh, thời lượng gợi ý 60–90 phút. Sản phẩm là hàm cộng có kiểm tra đầu vào với hai bản vá, bộ kiểm thử và lời giải thích về chỉ số và kiểu dữ liệu; không cần Web hay tài khoản AI trả phí.

**Silver · Web có luồng dữ liệu** theo nhánh của Lan, thời lượng gợi ý 90–120 phút. Sản phẩm là hai lỗi logic được sửa trong bài biệt lập, kèm biên bản kiểm tra luồng form → dữ liệu → DOM và cơ chế lưu trữ trên bản demo đúng; không cần backend hay đăng nhập.

**Gold · Quy trình Agent có kiểm soát** dành cho người đã xong Bronze hoặc Silver, cần thêm 30–45 phút. Sản phẩm là bài của cấp nền cộng với phạm vi quyền, kế hoạch, diff, nhật ký và biên bản nghiệm thu; không có quyền dùng Agent thì diễn tập trên giấy và ghi rõ là mô phỏng.

Thời lượng chỉ để lập kế hoạch, không phải thước đo năng lực.

## Mười yêu cầu của bản nộp

1. Tự diễn đạt yêu cầu chức năng: phép tính tổng làm gì, đầu vào nào bị từ chối, việc gì ngoài phạm vi.
2. Chọn công cụ có lý do, gắn với tác vụ, rủi ro và ngân sách; nếu không dùng AI, ghi rõ.
3. Mô tả cấu trúc dữ liệu: `vector<long long>` ở Bronze; `Expense(id,title,amount,category)` và đường đi của `amount` ở Silver.
4. Triển khai trong phạm vi đã chọn; ghi rõ phần AI gợi ý và phần tự viết.
5. Sửa tối thiểu hai lỗi gốc; mỗi lỗi có hiện tượng, nguyên nhân và phản ví dụ riêng.
6. Đọc diff: mỗi dòng thay đổi giải quyết yêu cầu nào; có tệp, phụ thuộc hay quyền nào tăng thêm không.
7. Chạy kiểm thử với kỳ vọng xác định trước; giữ cả lần chạy thất bại, không chỉ chụp kết quả đạt.
8. Rà soát dữ liệu cá nhân, khóa API, thư viện, giấy phép; không dùng dữ liệu thật.
9. Khai báo đúng mức hỗ trợ của AI theo mẫu trong [Thỏa thuận học tập](../chapters/learning-agreement.md).
10. Giải thích sản phẩm, trả lời một câu hỏi biến thể mà không dùng AI, nêu giới hạn chưa kiểm chứng.

## Bắt đầu từ đâu

Đề đầy đủ nằm trong [Sổ tay thực hành](../chapters/final-boss.md). Ở đó có bộ đề có lỗi chủ đích trong thư mục `vi-du/final-boss/` (`bronze.cpp` với 9 ca kiểm thử, `silver.cjs` và `test_silver.cjs` với 12 ca), hướng dẫn tạo thư mục `bai-lam/final-boss`, lệnh biên dịch và chạy cho từng cấp, quy trình sáu bước cho cấp Gold, bảng nghiệm thu 100 điểm và kịch bản buổi bảo vệ tám phút. Trước khi mở phần đáp án ở đó, hãy ghi dự đoán riêng cho từng ca kiểm thử.

Kết thúc dự án, người học có một sản phẩm nhỏ cùng một chuỗi bằng chứng có thể lặp lại. Khi công cụ AI không còn sẵn dùng, bảng trace, bộ kiểm thử và khả năng tự giải thích vẫn là năng lực của chính người học. AI hỗ trợ, người học quyết định.
