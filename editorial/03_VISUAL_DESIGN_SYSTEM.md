# 03 · VISUAL DESIGN SYSTEM

## Art direction

Tạp chí công nghệ học thuật, không mô phỏng dashboard SaaS làm cẩm nang. Bìa mang tư duy editorial: chữ lớn, nền giấy sáng, minh họa sinh viên đang cùng đọc một luồng dữ liệu. Trang đọc thoáng và yên tĩnh; sắc đậm tập trung ở đầu chương. Đồ họa vector tự tạo, nhãn SVG/HTML chính xác; không ảnh stock, logo nhãn hàng hay chữ tiếng Việt do mô hình ảnh vẽ.

## Tokens thiết kế

| Vai trò | Giá trị | Cách dùng |
|---|---|---|
| Nền giấy | `#f6f3ea` | Toàn trang đọc |
| Mực | `#20342d` | Chữ chính, tiêu đề |
| Màu phụ | `#58685f` | Chú thích, vẫn bảo đảm dễ đọc |
| Xanh rêu | `#35634b` | Liên kết, điều hướng |
| Xanh nhạt | `#dce8d0` | Phần nhấn nhẹ |
| Cam đất | `#b95132` | Cảnh báo hoặc điểm đang xét, không toàn trang |
| Vàng nhạt | `#f2dfa5` | Dự đoán/ghi chú |
| Đường phân cách | `#d4dbcf` | Bảng, section |
| Display | Georgia, Times New Roman, serif | Tên chương, chữ lớn |
| Body | system-ui, Segoe UI, sans-serif | Tiếng Việt đầy đủ dấu, không tải font |
| Code/meta | ui-monospace, Consolas, monospace | Code, nhãn, số bước |

Cỡ nội dung mặc định 18px, line-height 1.8, độ rộng bài ~76 ký tự. Tiêu đề 40–76px ở desktop, co xuống 32–44px mobile. Grid 8px, khoảng section 48–80px, khoảng đoạn 14–20px. Không dùng đoạn dài 15 dòng liền nếu có thể chia theo một ý.

## Layout và tương tác

Sidebar 270px trên desktop, nội dung rộng tối đa 1060px. Tablet chuyển drawer; mobile một cột. Mọi bảng và code cuộn ngang trong vùng riêng, không tràn viewport. Nút tối thiểu khoảng 40px; focus nhìn thấy; liên kết gạch chân hoặc có phân biệt hình thức, không chỉ màu. Có skip-link.

Mục lục tìm không dấu. Mỗi chương có nút “Đánh dấu đã tự kiểm” tự nguyện; lưu localStorage và fallback bộ nhớ, không coi là chứng nhận năng lực. Tiến độ đọc theo cuộn tách khỏi tiến độ tự kiểm. Cỡ chữ, chế độ tập trung, in. Prompt sao chép có fallback. Quick Check dùng câu hỏi + giải thích, không gửi lên AI. Máy tính chi phí và trace vòng lặp chạy cục bộ, nhãn mô phỏng rõ.

## Nhân vật

Minh: tóc ngắn đen hơi dựng, áo xanh rêu, ba lô hoặc sổ màu vàng; nhận diện bằng nhãn Minh / C++. Lan: tóc đen ngang vai, áo cam đất, máy tính hoặc sổ màu xanh nhạt; nhãn Lan / Web. Cùng tỷ lệ đầu/thân, nét tròn 3–4px, da màu đất ấm. Hình minh họa hư cấu, không dựa ảnh người thật. Biểu cảm tò mò/tập trung, không vẽ người học thành bất lực hay trẻ em.

Cùng hai bộ nhân vật SVG được tái dùng trong cover và opener. Tư thế thay theo nhiệm vụ: so thẻ AI, tìm phần tử bị bỏ, giải thích sơ đồ, rà khóa và quyền. Không thay màu áo hoặc tóc qua chương.

## Danh mục hình bắt buộc và mục đích

| Tệp assets | Mục đích sư phạm |
|---|---|
| cover.svg | Minh–Lan và ba khoản tiền: vấn đề chung của toàn cuốn |
| chapter-01.svg | Ba phiếu đáp cùng một câu hỏi; gợi lý do khác nhau |
| chapter-02.svg | Khoản Vở ghi 18000 bị bỏ; truy dấu để sửa |
| chapter-03.svg | AI gợi ý, sinh viên dự đoán/giải thích; trách nhiệm suy nghĩ |
| chapter-04.svg | Rà dữ liệu, quyền, nguồn, kiểm thử trước chia sẻ |
| ecosystem.svg | Những cách truy cập AI, không bảng xếp hạng thương hiệu |
| roles.svg | Model/provider/application/user; mũi tên truy cập, không chuỗi quyền sở hữu |
| token-context.svg | Chunks chỉ minh họa không là tokenizer thật; vùng ngữ cảnh hữu hạn |
| workspace.svg | IDE chứa editor/terminal, shell thực thi CLI; AI/Agent có quyền giới hạn |
| workflow.svg | Ask → Analyze → Edit → Test → Review, có vòng quay lại khi test sai |
| debugging.svg | Bảng trace i=0,1,2 với cận sai; rỗng không đủ kiểm chứng |
| active-learning.svg | Dự đoán → gợi ý → tự sửa → test → giải thích → biến thể |
| ai-trap.svg | Câu tự tin đối chiếu phản ví dụ một phần tử, không so thương hiệu |
| security.svg | Key lộ: thu hồi trước dọn, không đưa key thật vào minh họa |
| final-boss.svg | Bronze/Silver/Gold theo năng lực, không theo giá công cụ |
| skill-map.svg | Bốn năng lực và bằng chứng, không thanh chứng nhận tự động |

Có 16 hình bao phủ đủ 14 nhóm yêu cầu (cover, 4 opener, nhân vật xuyên suốt và 10 sơ đồ chuyên đề). Tất cả có SVG title/desc, figcaption, chữ không bị cắt; không nhồi tất cả vào một trang đầu.

## Hệ component

Hộp chỉ dùng cho “Trước khi làm”, cảnh báo bắt buộc hoặc câu hỏi tương tác. Các nhãn AI CHALLENGE/THINK FIRST/QUICK CHECK… có cùng typography mono nhỏ; không mỗi loại một màu. Chín trường Mission được thể hiện bằng tiêu đề phụ và văn xuôi, không chín card. Hồ sơ sự cố dùng bảng lựa chọn và đoạn phân tích. Lời giải thu gọn, bản in tự mở. Nguồn tham khảo ở cuối chương và báo cáo xác minh.

## Quy tắc chất lượng

SVG viewBox 1200×720 hoặc 1200×780, chữ tối thiểu 18px trong ảnh. Diagram không có nhiều hơn khoảng 5 bước ngang, nội dung dài chia hai hàng hoặc trình bày bằng HTML. Ảnh có thể mở toàn kích thước để xem chi tiết trên điện thoại. Mọi thông tin quan trọng cũng có trong văn bản, không để chữ nhỏ trong ảnh là cách duy nhất tiếp cận kiến thức.

Kiểm ảnh bằng render thực; desktop/tablet/mobile thực nếu công cụ hỗ trợ. Nếu chỉ kiểm cấu trúc, báo đúng mức đó, không gọi là đã xem giao diện. Tránh animation tự động; tôn trọng prefers-reduced-motion.
