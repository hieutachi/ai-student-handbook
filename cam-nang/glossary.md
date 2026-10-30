# BẢNG THUẬT NGỮ

Bảng này giải nghĩa ngắn các thuật ngữ dùng trong cẩm nang, xếp theo bảy nhóm. Mỗi dòng gồm thuật ngữ tiếng Việt, tiếng Anh trong ngoặc và một định nghĩa; dùng để tra cứu, không nhằm học thuộc. Định nghĩa đầy đủ hơn, kèm lưu ý và chỉ dẫn tới từng mục, có trong [Bảng thuật ngữ của Sổ tay thực hành](../chapters/glossary.md).

<a id="ai-access"></a>
## AI: vai trò, các thành phần và quyền truy cập — Chương 1, 2, 5

- **Lạm dụng AI trong học tập** (academic overuse): giao cho AI phần việc cần tự luyện; dấu hiệu là không giải thích được bài làm.
- **Dùng AI có trách nhiệm** (responsible AI use): dùng trong phạm vi được phép, bảo vệ dữ liệu, kiểm chứng đầu ra, khai báo đúng.
- **Mô hình** (model): thành phần đã huấn luyện để tạo đầu ra từ đầu vào; tên mô hình chưa cho biết toàn bộ công cụ.
- **Nhà cung cấp** (provider): bên cấp quyền truy cập mô hình, tính phí, xử lý dữ liệu; có thể khác bên phát triển (producer).
- **Ứng dụng** (application): phần mềm người dùng tương tác trực tiếp, như giao diện chat; có thể gọi nhiều mô hình và công cụ.
- **Giao diện lập trình ứng dụng** (API): quy ước để phần mềm gọi dịch vụ khác; quyền dùng API không đi kèm gói chat.
- **Khóa API** (API key): chuỗi bí mật cấp quyền gọi dịch vụ, có thể phát sinh chi phí; không dán vào prompt hay kho Git.
- **Agent**: AI đọc tệp, sửa mã, chạy công cụ trong phạm vi quyền được cấp; lời dặn trong prompt không thay phân quyền.
- **Miễn phí, thuê bao, hạn mức** (free, subscription, quota): không trả phí; trả phí định kỳ; giới hạn lượng dùng trong một kỳ.
- **Cảnh báo ngân sách, trần chặn** (budget alert, hard cap): cảnh báo chỉ thông báo khi chạm mức; trần chặn mới dừng hẳn chi tiêu.

<a id="ai-process"></a>
## AI: đầu vào, xử lý và độ tin cậy — Chương 1, 3, 5

- **Prompt**: yêu cầu gửi cho AI; prompt tốt nêu mục tiêu, dữ liệu, giới hạn và dạng đầu ra mong muốn.
- **Ngữ cảnh** (context): toàn bộ thông tin mô hình thực nhận khi trả lời; tệp có trên máy chưa chắc nằm trong ngữ cảnh.
- **Cửa sổ ngữ cảnh** (context window): giới hạn lượng thông tin xử lý trong một lượt, đo bằng token; hội thoại dài bị cắt.
- **Token**: đơn vị dữ liệu mô hình dùng để xử lý và tính phí; không tương đương một từ hay một ký tự.
- **Huấn luyện, suy luận** (training, inference): điều chỉnh tham số từ dữ liệu; tạo đầu ra với tham số đã có. Prompt không huấn luyện.
- **Đầu ra bịa đặt** (hallucination): đầu ra không có căn cứ nhưng được nêu tự tin, như hàm, nguồn hay kết quả không tồn tại.
- **Benchmark**: bộ bài kiểm tra cùng cách chấm để đo mô hình; chỉ so sánh được khi cùng nhiệm vụ và cùng tiêu chí.
- **Brief**: bản giao việc ngắn nhưng đủ ràng buộc: mục tiêu, môi trường, hiện tượng, kỳ vọng, điều đã thử (thẻ P09).
- **Hỏi đáp kiểu Socratic** (Socratic questioning): đặt câu hỏi dẫn dắt để người học tự suy nghĩ và tự tìm câu trả lời (thẻ P01).
- **Vibe coding**: làm phần mềm chủ yếu bằng mô tả lời và phản hồi với AI; người làm vẫn phải hiểu và kiểm tra mã.

<a id="environment"></a>
## Môi trường làm việc — Chương 2

- **Môi trường phát triển tích hợp** (IDE): công cụ gộp soạn thảo, chạy, gỡ lỗi và terminal; có AI tích hợp vẫn phải tự kiểm.
- **Terminal, shell, giao diện dòng lệnh** (CLI): cửa sổ nhập lệnh; chương trình thực hiện lệnh (Bash, PowerShell); cách điều khiển bằng lệnh.
- **Thư mục làm việc** (working directory): vị trí gốc để giải đường dẫn tương đối; xem bằng `pwd` hoặc `Get-Location`.
- **Biên dịch, dựng** (compile, build): dịch mã nguồn sang dạng chạy được; build lỗi thì dừng, không dùng tệp thực thi cũ.
- **Mã kết thúc** (exit code): mã chương trình trả về khi kết thúc; `0` thường là thành công nhưng không chứng minh thuật toán đúng.

<a id="code-data"></a>
## Kiểu dữ liệu và tư duy lập trình — Chương 2–3

- **Expense**: mô hình khoản chi trong bản Web, gồm `id`, `title`, `amount`, `category`.
- **`vector<long long>`**: danh sách động của C++ chứa số nguyên `long long`; bản C++ chỉ chứa số tiền, không có tên hay nhóm chi.
- **Tràn giá trị** (overflow): kết quả vượt miền của kiểu; `long long` rộng hơn `int`, giảm nguy cơ tràn khi cộng nhiều khoản.
- **Số nguyên an toàn** (safe integer): số nguyên JavaScript biểu diễn chính xác tới `9007199254740991`; không thay điều kiện tiền từ 1 đến `1e9`.
- **Chỉ số, truy cập ngoài biên** (index, out-of-bounds): vị trí phần tử; truy cập ngoài phạm vi hợp lệ gây hành vi không xác định.
- **Chuỗi, số, chuyển kiểu** (string, number, conversion): hai kiểu khác nhau; ô nhập Web trả chuỗi; chuyển kiểu xong chưa chắc thỏa hợp đồng.
- **`undefined`, `NaN`**: đọc trường không tồn tại cho `undefined`; cộng giá trị đó với số cho `NaN`; gặp `NaN`, đối chiếu tên trường trước.
- **Kiểm tra hợp lệ** (validation): xác minh dữ liệu thỏa hợp đồng; `parseInt` chỉ đọc phần đầu chuỗi nên không thay kiểm tra hợp lệ.
- **Hợp đồng dữ liệu** (data contract): điều kiện dữ liệu phải thỏa; trong sách: số nguyên VND 1 đến 1000000000, tối đa 500 khoản.

<a id="web"></a>
## Web, lưu trữ và ranh giới dữ liệu — Chương 2–4

- **DOM** (Document Object Model): cây đối tượng biểu diễn trang Web để JavaScript đọc và sửa; kiểm thử trong Node.js không xác nhận DOM đúng.
- **`localStorage`**: kho khóa–giá trị dạng chuỗi của trình duyệt; có thể bị chặn hoặc chứa dữ liệu cũ; không phải máy chủ.
- **SQL, truy vấn tham số hóa** (parameterized query): ngôn ngữ dữ liệu quan hệ; truy vấn tham số hóa tách giá trị khỏi câu lệnh.
- **Chèn mã vào lệnh, danh sách cho phép** (injection, allowlist): dữ liệu không đáng tin làm đổi nghĩa câu lệnh; tập giá trị được phép.
- **XSS, `textContent`, `innerHTML`** (cross-site scripting): nội dung không đáng tin bị thực thi trong trang; `textContent` đặt văn bản, `innerHTML` phân tích HTML.

<a id="evidence"></a>
## Kiểm chứng, Git và quyền dùng nguồn — Chương 2–4

- **Trace**: lần theo giá trị, nhánh và vòng lặp qua từng bước trên giấy; là bằng chứng lập luận, không phải nhật ký chạy thật.
- **Ca kiểm thử, ca biên** (test case, edge case): đầu vào kèm điều cần đối chiếu; ca biên ở ranh giới, như danh sách rỗng.
- **Kỳ vọng, quan sát, bằng chứng**: kỳ vọng viết trước khi chạy; quan sát ghi điều thực xảy ra; bằng chứng gắn phiên bản mã.
- **Diff, review**: bản so sánh trước và sau; xem xét thay đổi cùng lý do. Đọc diff không thay chạy kiểm thử.
- **Commit, điểm khôi phục** (checkpoint): commit ghi một mốc trong kho Git; điểm khôi phục là mốc quay lại được chuẩn bị trước.
- **Bản sao kho** (clone), **GitHub**: bản sao kho Git kèm lịch sử; xóa bí mật trên GitHub không xóa trong bản sao của người khác.
- **Gói phụ thuộc, tệp khóa phiên bản** (dependency, lockfile): thư viện dự án cần; lockfile ghi phiên bản đã chọn, chưa bảo đảm đáng tin.
- **Ghi nhận nguồn, quyền sở hữu** (attribution, ownership): ghi nhận hỗ trợ; quyền đối với sản phẩm; khai "AI viết" chưa hết trách nhiệm.
- **Giấy phép** (license), **MIT, GPL**: quyền và điều kiện dùng sản phẩm; MIT yêu cầu giữ thông báo; GPL không cấm dùng thương mại.
- **Dữ liệu giả, khử nhận dạng** (de-identification): dữ liệu tạo mới để luyện; giảm khả năng nhận diện dữ liệu thật; bỏ tên chưa đủ.

<a id="labels"></a>
## Nhãn học tập và hoạt động trong sách

Nhãn tiếng Anh đặt trong ngoặc sau tiêu đề mục và giữ trên hình minh họa; chúng là chỉ dẫn đọc, không phải tên chế độ của công cụ AI.

- **Nhận diện công cụ AI** (AI Map): bốn câu hỏi model, provider, application, producer để biết đang dùng gì (mục 1.2).
- **Cơ chế phía sau** (Behind the Scene): giải thích cơ chế đằng sau một biểu hiện, như prompt, context và token (mục 1.3).
- **Bẫy câu trả lời AI** (AI Trap): câu trả lời sai hoặc thiếu điều kiện được dựng sẵn để người học phản biện (mục 3.1).
- **Dự đoán trước** (Think First): điểm dừng để viết ra dự đoán của bản thân trước khi hỏi AI (mục 3.2).
- **Lần ngược, giải thích lại** (Reverse Engineering, Explain It Back): đi từ con số trên màn hình về nơi tạo ra, rồi tự giải thích.
- **Thí nghiệm ghi nhớ** (Memory Experiment): tự quan sát khả năng nhớ lại; không phải nghiên cứu khoa học hay chẩn đoán (mục 3.4).
- **Phiên tự làm 25 phút không AI** (25-Minute No-AI): phiên tự làm hoàn toàn không dùng AI, khác phiên học có AI (mục 3.4).
- **Tóm tắt chương** (Skill Unlocked): ghi lại năng lực vừa có bằng chứng; không phải chứng chỉ hay kết luận lâu dài (mục 3.5).
- **Chi phí sử dụng AI** (AI Wallet): cách tính chi phí theo token trước khi gửi yêu cầu (mục 5.1).
- **Ưu tiên phương án miễn phí** (Free First): chỉ mua khi biết rõ còn thiếu gì (mục 5.2).
- **Đối chiếu công cụ theo tác vụ** (AI Tool Battle): so sánh công cụ bằng cùng đề, cùng tiêu chí, không theo danh tiếng.
- **Bài thực hành** (Mission): bảy nhiệm vụ 01–07 ở Chương 2 của Sổ tay thực hành, mỗi bài có đầu ra giới hạn.
- **Hồ sơ** (case file): bảy tình huống về dữ liệu, bảo mật, bản quyền và liêm chính ở Chương 4 của Sổ tay thực hành.
- **Dự án tổng kết** (Final Boss): bài tổng hợp cuối sách; Bronze, Silver, Gold chỉ mức độ nhiệm vụ, không phải gói trả tiền.

Để chuyển "phạm vi", "đóng góp" và "bằng chứng" thành việc làm cụ thể, xem [Thỏa thuận học tập](../chapters/learning-agreement.md).
