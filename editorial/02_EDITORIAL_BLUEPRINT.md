# 02 · EDITORIAL BLUEPRINT

## Concept đã chọn

Modern Technology Editorial × Mission Handbook. Câu chuyện bốn chặng: nhận diện công cụ → điều khiển quá trình → giữ năng lực tự làm → chịu trách nhiệm. Không làm quảng cáo và không biến người học thành người phải mua dịch vụ.

Đối tượng thiết kế: Minh năm nhất cần hướng dẫn thao tác có lý do; Lan năm hai cần theo dấu dữ liệu nhiều tệp. Đây là giả định biên tập, không phải khảo sát sinh viên TLU.

Bản mới ở thư mục riêng; bản nguồn bất biến. Kiến thức kế thừa được viết lại, chuyển vị trí nếu cần. Hoạt động mới ghi “Bổ sung biên tập”; mọi hội thoại AI/phiếu trả lời hư cấu ghi rõ. Trạng thái code: demo đúng, snippet có lỗi chủ đích, bài làm tự tạo, đầu ra kỳ vọng và kết quả kiểm thử là năm thứ khác nhau.

## Kiến trúc xuất bản

- `chapters/introduction.md`: hook, hai lộ trình, hợp đồng dữ liệu, cách dùng bản đọc.
- `chapter-01.md` … `chapter-04.md`: bốn chương biên tập đầy đủ.
- `prompt-library.md`: tám prompt học tập gốc + brief, debug, Agent và kiểm chứng; thẻ độc lập sao chép được.
- `glossary.md`: thuật ngữ gốc và thuật ngữ bổ sung, ví dụ ngắn.
- `learning-agreement.md`: phạm vi, phần tự làm, dữ liệu, nguồn và khai báo; mẫu không thay quy định môn học.
- `final-boss.md`: đề bài ba mức, hai lỗi minh bạch mỗi nhánh, test, rubric và bảo vệ.
- `website/index.html`: cẩm nang đầy đủ, không cần server hay mạng; CSS/JS nhúng, ảnh SVG ngoài trong `assets/`.
- `dashboard/index.html`: tiến độ sản xuất đọc checkpoint có thật; không đồng nhất với tự đánh dấu đã học.
- `reports/04_QUALITY_REPORT.md`: bằng chứng, kết quả, điểm tự đánh giá và giới hạn.

## Cấu trúc chương mới và bản đồ nguồn

### Chương 1 · Bước vào thế giới AI

Mở với Minh hỏi cùng một câu về vòng lặp ở ba giao diện, ba phiếu đáp hư cấu. Câu hỏi dẫn: khác đáp án do model, context hay ứng dụng?

| Mục mới | Nội dung/hoạt động | Nguồn |
|---|---|---|
| 1.1 AI MYSTERY / AI MAP | Vai trò model/provider/application/producer/user; API/key; nhận diện điều chưa rõ | 1.1 |
| 1.2 BEHIND THE SCENE | Prompt/token/context; ví dụ brief; cửa sổ ngữ cảnh; training/inference/search; hallucination | 1.2 |
| 1.3 AI WALLET | Phép tính giả định chi phí; input/output; agent nhiều lượt; hard cap | 1.3 |
| 1.4 Free first | Ngân sách, quyền không mua, gia hạn/điều kiện tuổi và ưu đãi chưa xác minh | 1.4 |
| 1.5 AI TOOL BATTLE | Ma trận tác vụ, benchmark A–C, năm tiêu chí và rubric 10 điểm; phiếu trống | 1.5 |
| 1.6 MINI CHALLENGE | Lab 20 phút, worksheet, quyết định có điều kiện, sáu câu, nguồn | 1.6 |

Không giữ trace chi tiết hai lần: chương 1 nêu vấn đề; chương 2 giải đầy đủ. Không xóa kiến thức safe integer hay bảng kỳ vọng mà chuyển vào chỗ đúng.

### Chương 2 · Trở thành người điều khiển AI

Bảy Mission, mục 2.1–2.7. Mỗi Mission có: mục tiêu, bối cảnh, nhiệm vụ, prompt mẫu, hướng dẫn, kỳ vọng, lỗi thường gặp, câu hỏi, tiêu chí hoàn thành. Không dùng chín hộp màu; ưu tiên văn xuôi, checklist/bảng khi cần.

| Mission | Nội dung | Nguồn |
|---|---|---|
| 01 / 2.1 Môi trường | Editor/IDE/terminal/shell/CLI, cwd, bản sao, bảng lệnh Bash/PowerShell | 2.1, 2.2, 2.6 |
| 02 / 2.2 Hỏi đúng | Ask chỉ đọc, context, dẫn vị trí, prompt không thay quyền | 2.3, 1.2 |
| 03 / 2.3 Debug C++ | Trace, cận, unsigned, reference/copy, `;`, build cũ; tách vá cận và validation | 2.4 |
| 04 / 2.4 Debug Web | OOP/DSA, Expense, O(n)/O(1), ba tệp, string/parse, undefined/NaN, storage | 2.5 |
| 05 / 2.5 Giao Agent | Observe/Plan/Act/Test/Review, phân quyền, phạm vi và đúng dòng sản phẩm | 2.2, 2.3, 2.7 |
| 06 / 2.6 Đọc diff | Bốn câu hỏi, checkpoint, khôi phục có chọn lọc, không đè bài khác | 2.7 |
| 07 / 2.7 Nghiệm thu | Build/run/exit code, 9 C++/34 JS bản mới (33 JS nguồn gốc); C1–C9, W1–W10, T1–T8, rubric | 2.6, 2.8 |

Quy ước chung: mở gốc `AI-Student-Handbook`. Thư mục `vi-du/` là tham khảo; người học tạo `bai-lam/nam-1-cpp` hoặc `bai-lam/nam-2-web` bằng trình quản lý tệp và sao chép nhánh tương ứng. Nếu khối lệnh đứng trong nhánh phải ghi thật rõ; ưu tiên mọi lệnh từ gốc dùng đường dẫn đầy đủ tương đối. Không dùng tên `-ban-sao` lẫn lộn nữa. `loi-bo-sot.cpp` có dữ liệu cố định, không có `--test`; `vi_sinh_vien.cpp` đúng có 9 test. Sửa vòng lặp không đủ validation: báo thành bước mở rộng riêng.

### Chương 3 · Đừng để AI suy nghĩ thay bạn

| Mục | Hoạt động | Nguồn |
|---|---|---|
| 3.1 AI TRAP | Sáu tình huống sử dụng/vùng xám, phản biện câu trả lời tự tin, vibe coding có kiểm soát | 3.1–3.2 + mới |
| 3.2 THINK FIRST | Dự đoán trước hỏi, hội thoại C++, phiên 25 phút có AI, xử lý khi lộ đáp án | 3.3, 3.5 |
| 3.3 REVERSE / EXPLAIN IT BACK | Luồng Web, kiểu dữ liệu, giải thích code, tám chức năng prompt được dẫn tới thư viện | 3.4–3.5 |
| 3.4 MEMORY EXPERIMENT | Hai nhiệm vụ tương đương để tự quan sát nhớ lại, không kết luận nhân quả | Bổ sung |
| 3.5 25-MINUTE NO-AI | Nhiệm vụ độc lập không AI, chấm theo bằng chứng, chưa xong vẫn ghi điểm nghẽn | Bổ sung |
| 3.6 AI CHALLENGE | Hai nhánh thực hành, bảng test, đáp án validation, max, tổng nhóm kiểm toàn bộ dữ liệu | 3.6 |
| 3.7 SKILL UNLOCKED | Ba mức tự đánh giá, tám vấn đáp, phiếu ba dòng, không phán năng lực lâu dài | 3.7 |

Khi cần trạng thái Web 42000, phải nói demo khởi đầu 60000: trên bản sao, xóa riêng Vở ghi rồi thêm lại; hoặc dùng mảng lab riêng. Không bảo sửa demo đang đúng. `MEMORY EXPERIMENT` không được nói AI làm suy giảm trí nhớ hay đưa phần trăm bịa.

### Chương 4 · Sử dụng AI có trách nhiệm

Bảy hồ sơ và một phòng khám kỹ thuật. Mỗi hồ sơ đủ sáu thành phần: sự cố, dấu hiệu, nguy cơ, các lựa chọn, phân tích từng lựa chọn, bài học. Chọn ít nhất hai lựa chọn có phân tích không chỉ đáp án.

| Mục | Hồ sơ | Nguồn |
|---|---|---|
| 4.1 | Key trên GitHub: revoke/rotate trước dọn, sáu bước, thông báo | 4.6 |
| 4.2 | Dữ liệu cá nhân đi vào AI: tái nhận diện, ảnh/chat/Git, pháp lý theo phạm vi | 4.2 |
| 4.3 | Agent sửa/xóa quá phạm vi: dừng, checkpoint, diff, không khôi phục mù | 4.2 + 2.7 |
| 4.4 | Dependency lạ: registry, lockfile, kiểm tra không cài, không ống lệnh từ mạng | 4.3 |
| 4.5 | Bài tập hoàn toàn do AI: phạm vi/khai báo/được phép, tin nhắn hỏi giảng viên | 4.1 |
| 4.6 | Mã chưa rõ giấy phép: MIT/GPL/no-license/mã AI, thẻ nguồn | 4.4 |
| 4.7 | Khai báo thiếu: ba tầng trách nhiệm, mẫu, review, rubric 8 và checklist | 4.1, 4.5, 4.7 |
| 4.8 | Phòng khám SQL/XSS/C++: parameter/tuple/allowlist, fixture; cell.textContent; UB; test | 4.3, 4.7 |

Không bịa quy định TLU hoặc nói sinh viên gánh 100% pháp lý. Văn bản pháp luật chưa kiểm chứng nội dung/hiệu lực phải ghi chưa xác minh, không chỉ gắn link rồi khẳng định.

## Phần bổ trợ và dự án cuối

Tám prompt gốc có số P01–P08, thêm P09 brief, P10 điều khiển Agent, P11 kiểm chứng nguồn; mỗi prompt mang tối thiểu dữ liệu/giới hạn/cách trả lời/phần chưa làm. Glossary giải thích thuật ngữ kỹ thuật lẫn editorial labels bằng tiếng Việt.

Final Boss yêu cầu xác định yêu cầu, chọn công cụ hoặc phương án không truy cập AI, cấu trúc dữ liệu, hỗ trợ triển khai trong phạm vi cho phép, sửa hai lỗi, diff, test, rà dữ liệu/giấy phép, khai báo, bảo vệ. Bronze C++, Silver Web, Gold quy trình Agent nâng từ Bronze/Silver, không tăng tính năng vô cớ. Phải có hai lỗi chủ đích cho người học tự sửa trên bản sao; không làm hỏng demo tham khảo. Không có AI thì làm được Bronze/Silver với phiếu đáp mô phỏng, Gold thực hành quy trình thủ công được ghi đúng là mô phỏng.

## Nhịp sư phạm thống nhất

Tình huống → tự dự đoán → khái niệm đúng lúc → thử nhiệm vụ → đối chiếu → giải thích → biến thể. Lời giải dùng tiêu đề `### Đáp án ...` để trình xuất bản gập được; đáp án gập không phải cơ chế chống gian lận. Mỗi chương có tóm tắt năng lực và đầu ra cụ thể.

Nhãn dùng nhất quán: AI CHALLENGE (thực hành), AI TRAP (lời sai), THINK FIRST (dự đoán), REAL-WORLD CASE (tình huống gần thực tế, vẫn giả lập), BEHIND THE SCENE (giải thích), AI VS HUMAN (so phần hỗ trợ và phần tự làm, không đánh giá sản phẩm), QUICK CHECK, PRO TIP, SECURITY ALERT, SKILL UNLOCKED. Không lạm dụng mỗi nhãn thành hộp.

## Quy trình kiểm soát

Mỗi chương được agent biên tập đọc trọn nguồn chương, viết lại và tự rà; người phụ trách đọc kết quả, kiểm đủ chủ đề/bảng/code trước khi giao chương tiếp theo. Song song chỉ các công việc độc lập (xác minh nguồn, xây hệ thống công cụ), không viết bốn chương cùng lúc. Giữ nhật ký thất bại. Kiểm chứng thật trước khi đánh dấu COMPLETED; không tự chấm ≥90 để hợp thức hóa việc chưa kiểm.
