# BẢNG THUẬT NGỮ

Bảng thuật ngữ tập hợp các khái niệm được dùng xuyên suốt cuốn sách, sắp xếp theo bảy nhóm chủ đề. Mỗi mục từ gồm thuật ngữ tiếng Việt kèm thuật ngữ tiếng Anh trong ngoặc đơn, định nghĩa ngắn gọn, lưu ý hoặc ví dụ khi cần, và chỉ dẫn tới chương, mục có nội dung liên quan. Các thuật ngữ đã thông dụng trong ngành như API, token, prompt, diff, commit được giữ nguyên dạng tiếng Anh.

Bảng dùng để tra cứu khi gặp từ chưa rõ trong lúc đọc hoặc làm bài, không nhằm học thuộc. Các định nghĩa phục vụ việc đọc sách và không thay thế giáo trình của các học phần chuyên ngành.

**Tra theo nhóm:** [AI và quyền truy cập](#ai-access) · [Cách AI xử lý](#ai-process) · [Môi trường](#environment) · [Mã và dữ liệu](#code-data) · [Web](#web) · [Kiểm chứng, Git, nguồn](#evidence) · [Nhãn học tập](#labels).

<a id="ai-access"></a>
## AI: vai trò, các thành phần và quyền truy cập — Chương 1, 2, 5

- **Lạm dụng AI trong học tập** (*academic overuse*) — giao cho AI chính phần việc mà người học cần tự luyện, chẳng hạn tự dự đoán, tự viết hay tự giải thích, khiến kết quả có vẻ tốt nhưng năng lực của người học không tăng. Dấu hiệu nhận biết: không còn giải thích được bài làm khi đóng cửa sổ chat. Xem thêm: mục 1.1; Chương 3.
- **Dùng AI có trách nhiệm** (*responsible AI use*) — dùng AI trong phạm vi môn học cho phép, bảo vệ dữ liệu cá nhân và khóa bí mật, kiểm chứng đầu ra, tôn trọng bản quyền và khai báo đúng mức hỗ trợ đã nhận. Đây là điều kiện để được tiếp tục dùng AI trong học tập. Xem thêm: mục 1.1; Chương 4.
- **Mô hình** (*model*) — thành phần đã được huấn luyện để tạo đầu ra từ đầu vào. Tên mô hình không cho biết toàn bộ công cụ hay ngữ cảnh đang được sử dụng. Xem thêm: mục 1.2.
- **Nhà cung cấp** (*provider*) — bên cung cấp quyền truy cập mô hình, tính phí và xử lý dữ liệu theo điều khoản dịch vụ; nhà cung cấp có thể khác với bên phát triển mô hình. Xem thêm: mục 1.2, 5.1.
- **Ứng dụng** (*application*) — phần mềm người dùng tương tác trực tiếp, chẳng hạn giao diện chat. Một ứng dụng có thể gọi nhiều mô hình, bổ sung tệp và công cụ khi trả lời. Xem thêm: mục 1.2.
- **Bên phát triển mô hình** (*producer*, *developer*) — bên xây dựng mô hình. Vai trò này có thể trùng với nhà cung cấp, nhưng không mặc nhiên đồng nhất hai bên. Xem thêm: mục 1.2.
- **Giao diện lập trình ứng dụng** (*API — Application Programming Interface*) — quy ước để phần mềm gọi chức năng của một phần mềm hoặc dịch vụ khác. Quyền dùng API không mặc nhiên đi kèm gói thuê bao chat. Xem thêm: mục 1.2, 5.1.
- **Khóa API** (*API key*) — chuỗi bí mật cấp quyền gọi dịch vụ, có thể phát sinh chi phí. Không dán khóa API vào prompt, kho Git hoặc ảnh chụp màn hình; ứng dụng ViSinhVien không cần khóa API. Xem thêm: Hồ sơ 01 (mục 4.1).
- **Ask** — chế độ hỏi đáp chỉ đọc trong Qoder IDE, công cụ được sách dùng làm ví dụ hướng dẫn. Khi dùng chế độ này vẫn phải kiểm soát dữ liệu đưa vào ngữ cảnh; không suy diễn quyền của chế độ Ask sang sản phẩm khác. Xem thêm: Bài thực hành 02 (mục 2.2).
- **Agent** — dạng AI phối hợp đọc tệp, đề xuất hoặc sửa mã và chạy công cụ trong phạm vi quyền được cấp. Lời dặn "đừng sửa" trong prompt không thay thế cơ chế cấp quyền và phê duyệt hành động. Xem thêm: Bài thực hành 05 (mục 2.5), Hồ sơ 03 (mục 4.3).
- **Qoder IDE, Qoder Desktop, Qoder CLI** — các dòng sản phẩm với giao diện khác nhau. Cần đối chiếu tài liệu của đúng sản phẩm đang dùng; không áp tên nút hay chế độ của IDE sang Desktop hoặc CLI. Xem thêm: Bài thực hành 01 (mục 2.1), Bài thực hành 02 (mục 2.2).
- **Miễn phí, thuê bao, hạn mức, trần chặn** (*free*, *subscription*, *quota*, *hard cap*) — lần lượt là hình thức sử dụng không trả phí, hình thức trả phí định kỳ, giới hạn lượng sử dụng, và mức trần chặn việc sử dụng hoặc chi tiêu. Cảnh báo ngân sách chưa chắc đã chặn chi tiêu; cần kiểm tra điều kiện cụ thể của dịch vụ. Xem thêm: mục 5.1, 5.2.

<a id="ai-process"></a>
## AI: đầu vào, xử lý và độ tin cậy — Chương 1, 3, 5

- **Prompt** — yêu cầu gửi cho AI. Một prompt tốt nêu mục tiêu, dữ liệu, giới hạn và dạng đầu ra mong muốn, thay vì chỉ "sửa giúp em". Xem thêm: [Thư viện prompt mẫu](prompt-library.md).
- **Ngữ cảnh** (*context*) — toàn bộ thông tin mô hình nhận được khi trả lời, gồm yêu cầu, lịch sử hội thoại, mã nguồn, tài liệu và kết quả của công cụ. Tệp có trên máy chưa chắc đã nằm trong ngữ cảnh. Xem thêm: mục 1.3.
- **Cửa sổ ngữ cảnh** (*context window*) — giới hạn lượng thông tin được xử lý trong một lượt, thường đo bằng token. Hội thoại dài có thể bị rút gọn hoặc lược bỏ một phần, không được ghi nhớ nguyên vẹn. Xem thêm: mục 1.3.
- **Token** — đơn vị dữ liệu do bộ tách của mô hình tạo ra để xử lý, thường được dùng làm cơ sở tính phí đầu vào và đầu ra. Một token không tương đương một từ hay một ký tự. Xem thêm: mục 1.3, 5.1.
- **Suy luận khi sử dụng** (*inference*) — quá trình mô hình tạo đầu ra với bộ tham số hiện có. Tên gọi "suy luận" không bảo đảm rằng lập luận của mô hình là đúng. Xem thêm: mục 1.3.
- **Huấn luyện** (*training*) — quá trình điều chỉnh tham số của mô hình từ dữ liệu. Gửi prompt không đồng nghĩa với việc mô hình được huấn luyện lại ngay; chính sách lưu trữ và sử dụng dữ liệu là một vấn đề riêng. Xem thêm: mục 1.3, 5.2.
- **Tìm kiếm, truy xuất** (*search*, *retrieval*) — việc lấy tài liệu từ web hoặc từ kho dữ liệu để hỗ trợ câu trả lời; khác với huấn luyện. Kết quả truy xuất vẫn cần được đối chiếu. Xem thêm: mục 1.3.
- **Neo vào bằng chứng** (*grounding*) — việc ràng buộc câu trả lời với mã, dữ liệu hoặc nguồn được cung cấp hay truy xuất. Grounding không loại bỏ hết lỗi; nguồn được dẫn phải thực sự hỗ trợ nhận định. Xem thêm: mục 1.3.
- **Đầu ra bịa đặt** (*hallucination*) — đầu ra không có căn cứ, chẳng hạn một hàm, nguồn hay kết quả không tồn tại nhưng vẫn được nêu một cách tự tin. Cần kiểm tra API, tệp và nguồn thật thay vì tin vào giọng điệu của câu trả lời. Xem thêm: mục 1.3; mục 3.1.
- **Benchmark** — bộ bài kiểm tra cùng cách chấm, dùng để đo khả năng của mô hình trong điều kiện xác định. So sánh chỉ có ý nghĩa khi cùng nhiệm vụ và cùng tiêu chí; điểm benchmark cao không bảo đảm phù hợp với bài toán cụ thể của người học. Xem thêm: mục 5.3.
- **Brief** — bản giao việc ngắn gọn nhưng đủ ràng buộc. Xem thêm: thẻ P09 trong [Thư viện prompt mẫu](prompt-library.md).
- **Hỏi đáp kiểu Socratic** (*Socratic questioning*) — cách đặt câu hỏi dẫn dắt để người học tự suy nghĩ và tự tìm ra câu trả lời. Xem thêm: mục 3.3; thẻ P01.
- **Vibe coding** — cách triển khai phần mềm chủ yếu thông qua mô tả bằng lời và phản hồi qua lại với AI; người làm vẫn phải hiểu và kiểm tra mã được tạo ra. Xem thêm: mục 3.1.

<a id="environment"></a>
## Môi trường làm việc — Chương 2

- **Trình soạn thảo** (*editor*) — công cụ đọc và sửa mã nguồn; không nhất thiết có chức năng biên dịch, chạy hay kiểm thử. Xem thêm: Bài thực hành 01 (mục 2.1).
- **Môi trường phát triển tích hợp** (*IDE — Integrated Development Environment*) — công cụ kết hợp trình soạn thảo với các chức năng chạy chương trình, gỡ lỗi và terminal. Việc tích hợp AI vào IDE không bảo đảm thao tác đúng. Xem thêm: mục 2.1.
- **Terminal** — cửa sổ tương tác bằng văn bản để nhập lệnh và xem đầu ra; bản thân terminal không phải chương trình diễn giải lệnh. Xem thêm: mục 2.1.
- **Shell** — chương trình đọc và thực hiện lệnh, chẳng hạn Bash hoặc PowerShell. Cần dùng đúng cú pháp của shell đang chạy. Xem thêm: mục 2.1.
- **Giao diện dòng lệnh** (*CLI — Command-Line Interface*) — cách điều khiển công cụ bằng lệnh và đối số thay vì nút bấm, thông qua shell trong terminal. Terminal, shell và CLI là ba khái niệm không đồng nghĩa. Xem thêm: mục 2.1.
- **Thư mục làm việc** (*working directory*, *cwd*) — vị trí được dùng làm gốc để giải các đường dẫn tương đối. Có thể xem thư mục làm việc bằng `pwd` trong Bash hoặc `Get-Location` trong PowerShell. Xem thêm: mục 2.1, 2.7.
- **Đường dẫn tương đối, đường dẫn tuyệt đối** (*relative path*, *absolute path*) — đường dẫn tương đối phụ thuộc vào vị trí đang xét; đường dẫn tuyệt đối tính từ gốc của hệ thống tệp. Liên kết trong Markdown và lệnh trong terminal có thể dùng các gốc khác nhau. Xem thêm: mục 2.1.
- **Biên dịch** (*compile*), **dựng** (*build*) — biên dịch là dịch mã nguồn C++ sang dạng đích; build bao gồm cả các bước khác như liên kết. Khi build lỗi phải dừng lại, không dùng tệp thực thi cũ để chứng minh mã mới đúng. Xem thêm: Bài thực hành 03 (mục 2.3), Bài thực hành 07 (mục 2.7).
- **Tệp thực thi** (*executable*), **môi trường thực thi** (*runtime*) — tệp thực thi là tệp có thể chạy được; môi trường thực thi là môi trường nơi chương trình chạy. Chương trình C++ được biên dịch thành tệp thực thi; Node.js chạy JavaScript nhưng không có sẵn DOM của trình duyệt. Xem thêm: mục 2.1, 2.7.
- **stdout, stderr, mã kết thúc** (*exit code*) — lần lượt là luồng đầu ra thông thường, luồng báo lỗi và mã trả về khi chương trình kết thúc. Mã kết thúc `0` thường báo thành công, mã khác `0` báo lỗi; mã kết thúc không tự chứng minh thuật toán đúng. Xem thêm: mục 2.6, 2.7.

<a id="code-data"></a>
## Kiểu dữ liệu và tư duy lập trình — Chương 2–3

- **Expense** — mô hình khoản chi trong bản Web, gồm các trường `id`, `title`, `amount`, `category`. Một đối tượng có các trường dữ liệu không đồng nghĩa với việc đã thiết kế một hệ thống hướng đối tượng đầy đủ. Xem thêm: Bài thực hành 04 (mục 2.4).
- **`vector<long long>`** — danh sách động của C++ chứa các số nguyên kiểu `long long`; trong bản C++ dành cho năm nhất, danh sách chỉ chứa số tiền. Khi mô tả mã hiện có, không gán thêm tên hay nhóm chi tiêu vào mô hình này. Xem thêm: Bài thực hành 03 (mục 2.3).
- **Lập trình hướng đối tượng** (*OOP — Object-Oriented Programming*) — cách tổ chức chương trình xoay quanh các đối tượng, trạng thái và hành vi, với trách nhiệm được phân định rõ. Việc có một object JavaScript chưa chứng minh rằng mọi nguyên lý OOP đã được áp dụng.
- **Cấu trúc dữ liệu và giải thuật** (*DSA — Data Structures and Algorithms*) — lĩnh vực nghiên cứu cách tổ chức dữ liệu và các bước xử lý. Trong bài tính tổng, danh sách cùng phép duyệt là điểm nối với kiến thức DSA.
- **Độ phức tạp** (*complexity*) — mô tả mức tăng tài nguyên theo kích thước đầu vào. Duyệt `n` khoản có độ phức tạp thời gian `O(n)`; một biến cộng dồn dùng bộ nhớ phụ `O(1)`, không tính danh sách đầu vào. Xem thêm: mục 3.5, 3.6.
- **Số nguyên an toàn** (*safe integer*) — với kiểu `Number` của JavaScript, các số nguyên trong miền từ `-9007199254740991` đến `9007199254740991` được bảo đảm biểu diễn chính xác và phân biệt được với nhau. `Number.isSafeInteger` không thay thế điều kiện tiền phải dương và không vượt quá `1e9`. Xem thêm: mục 2.4.
- **Kiểu không dấu, tràn giá trị** (*unsigned*, *overflow*) — kiểu nguyên không dấu trong C++ chỉ biểu diễn giá trị không âm và tính theo modulo: `0 - 1` trên kiểu unsigned quay vòng về một giá trị lớn. Ngược lại, tràn số nguyên có dấu là hành vi không xác định. Xem thêm: mục 2.3.
- **Chỉ số, truy cập ngoài biên, hành vi không xác định** (*index*, *out-of-bounds*, *undefined behavior — UB*) — chỉ số xác định vị trí của phần tử; truy cập ra ngoài phạm vi chỉ số hợp lệ gọi là truy cập ngoài biên. Truy cập ngoài biên bằng `vector::operator[]` gây hành vi không xác định (UB) và có thể không làm chương trình dừng đột ngột; vì vậy việc chương trình "chạy được" không chứng minh mã hợp lệ. Xem thêm: mục 2.3, 4.8.
- **Tham chiếu, bản sao, `const`** (*reference*, *copy*) — tham chiếu trỏ tới một đối tượng có sẵn; bản sao tạo ra một đối tượng mới. Tham số `const std::vector<long long>&` cho phép hàm đọc dữ liệu qua tham chiếu mà không sửa vector qua tham chiếu đó, đồng thời tránh sao chép toàn bộ danh sách. Xem thêm: mục 2.3.
- **Chuỗi, số, chuyển kiểu** (*string*, *number*, *conversion*) — chuỗi và số là hai kiểu dữ liệu khác nhau. Ô nhập trên trang Web trả về chuỗi; chuyển kiểu thành công chưa chứng minh giá trị thỏa hợp đồng dữ liệu. `parseInt` có thể chỉ đọc phần đầu của chuỗi, nên không dùng thay cho kiểm tra hợp lệ. Xem thêm: mục 2.4; [Dự án tổng kết](final-boss.md).
- **`undefined`, `NaN`** — đọc một trường không tồn tại như `item.value` có thể nhận giá trị `undefined`; đem giá trị đó cộng với số có thể cho `NaN`, tức giá trị biểu thị kết quả số không hợp lệ. Khi gặp `NaN`, cần đối chiếu tên trường `amount` trước tiên. Xem thêm: mục 2.4.
- **Kiểm tra hợp lệ, lược đồ, chuẩn hóa** (*validation*, *schema*, *normalization*) — kiểm tra hợp lệ xác minh dữ liệu thỏa các điều kiện; lược đồ mô tả cấu trúc của dữ liệu; chuẩn hóa đưa dữ liệu về một dạng thống nhất. Bản Web kiểm tra đầy đủ từng bản ghi bằng `normalizeExpenses`, còn `totalExpenses` chỉ kiểm tra số tiền và số lượng khoản. Xem thêm: mục 2.4.

<a id="web"></a>
## Web, lưu trữ và ranh giới dữ liệu — Chương 2–4

- **DOM** (*Document Object Model*) — cây đối tượng biểu diễn tài liệu Web để JavaScript đọc và sửa. Kiểm thử hàm tính tổng trong Node.js không xác nhận rằng trang Web đã cập nhật DOM đúng. Xem thêm: Bài thực hành 04 (mục 2.4).
- **Hàm xử lý sự kiện** (*event handler*) — hàm được gọi khi xảy ra một sự kiện, chẳng hạn khi gửi biểu mẫu. Một hàm vô danh vẫn có trách nhiệm và vị trí riêng trong luồng xử lý; cần lần theo dữ liệu thay vì chỉ tìm tên hàm. Xem thêm: mục 2.4.
- **JSON** (*JavaScript Object Notation*) — định dạng văn bản để trao đổi dữ liệu, có cú pháp xác định. Phân tích JSON thành công không chứng minh `amount` hay các trường còn lại đúng hợp đồng. Xem thêm: mục 2.4.
- **Origin** — với địa chỉ Web thông thường, origin là bộ gồm giao thức, tên máy chủ và cổng. Trình duyệt dùng origin để tách biệt nhiều loại quyền và dữ liệu; không nên coi mọi tệp mở bằng `file://` đều có hành vi giống nhau. Xem thêm: Chương 3.
- **`localStorage`** — kho lưu trữ dạng khóa–giá trị (kiểu chuỗi) của trình duyệt, tách riêng theo origin. Kho này có thể bị chặn hoặc chứa dữ liệu cũ, dữ liệu sai; nó không phải cơ sở dữ liệu máy chủ, cơ chế đăng nhập hay kho lưu trữ tài chính bảo mật. Xem thêm: mục 2.4.
- **Phương án dự phòng** (*fallback*), **RAM** — fallback là phương án thay thế khi cách xử lý chính thất bại. Bản demo dùng bộ nhớ tạm (RAM) khi không lưu được dữ liệu; khi đó các thay đổi không được bảo đảm còn lại sau khi kết thúc phiên. Xem thêm: mục 2.4, 2.7.
- **Backend, SQLite, `:memory:`** — backend là phần xử lý phía máy chủ; ứng dụng Web trong sách không có phần này. SQLite là hệ quản trị cơ sở dữ liệu nhúng; `:memory:` tạo cơ sở dữ liệu nằm trong bộ nhớ, dùng cho một ví dụ minh họa riêng bằng Python. Xem thêm: mục 4.8.
- **SQL, truy vấn tham số hóa, tuple** (*parameterized query*) — SQL là ngôn ngữ làm việc với dữ liệu quan hệ. Truy vấn tham số hóa tách giá trị khỏi cấu trúc câu lệnh. Trong Python, `(title,)` là tuple một phần tử; chính dấu phẩy tạo nên tuple. Xem thêm: mục 4.8.
- **Chèn mã độc vào lệnh, danh sách cho phép** (*injection*, *allowlist*) — injection xảy ra khi dữ liệu không đáng tin làm thay đổi ý nghĩa của câu lệnh. Allowlist là danh sách các giá trị được phép, dùng khi cần chọn thành phần cấu trúc như tên cột thay vì chèn chuỗi tùy ý. Xem thêm: mục 4.8.
- **XSS, `textContent`, `innerHTML`** (*cross-site scripting*) — XSS là loại lỗ hổng trong đó nội dung không đáng tin dẫn tới việc thực thi script trong trang. `textContent` đặt nội dung dưới dạng văn bản vào ô bảng; `innerHTML` phân tích nội dung như mã HTML. Không suy diễn biện pháp bảo vệ dành cho văn bản sang trường hợp URL hoặc mã JavaScript. Xem thêm: mục 4.8.

<a id="evidence"></a>
## Kiểm chứng, Git và quyền dùng nguồn — Chương 2–4

- **Trace, mô phỏng** — trace là lần theo giá trị, nhánh và vòng lặp qua từng bước; mô phỏng là tình huống được dựng để giải thích. Cả hai đều không tự trở thành nhật ký chạy phần mềm thật. Xem thêm: Bài thực hành 03 (mục 2.3); Chương 3.
- **Ca kiểm thử, fixture, kiểm thử hồi quy** (*test case*, *fixture*, *regression test*) — ca kiểm thử gồm đầu vào và điều cần đối chiếu; fixture là dữ liệu giả được chuẩn bị riêng cho kiểm thử; kiểm thử hồi quy xác nhận một lỗi đã sửa không tái xuất hiện, ví dụ ca trường `category` là mảng. Xem thêm: mục 2.4, 2.7.
- **Kỳ vọng, quan sát, bằng chứng** — kỳ vọng được viết trước khi chạy; quan sát ghi lại điều thực sự xảy ra; bằng chứng gắn với một phiên bản mã, một môi trường và một cách kiểm tra cụ thể. Trạng thái "chưa chạy" khác với "không đạt". Xem thêm: Bài thực hành 07 (mục 2.7).
- **Diff, review** — diff là bản so sánh trước và sau, chỉ ra các dòng được thêm, bớt hoặc thay đổi. Review là việc xem xét thay đổi cùng lý do của nó. Đọc diff không tương đương với chạy kiểm thử, nhưng giúp phát hiện các sửa đổi vượt phạm vi. Xem thêm: Bài thực hành 06 (mục 2.6).
- **Commit, điểm khôi phục** (*checkpoint*) — commit ghi lại một mốc trạng thái trong kho Git. Điểm khôi phục là mốc có thể quay lại đã được chuẩn bị trước, có thể là một commit hoặc một bản sao thư mục. Cả hai đều không chứng nhận mã đúng. Xem thêm: mục 2.6.
- **Bản sao kho** (*clone*) — bản sao của một kho Git, thường kèm theo cả phần lịch sử liên quan. Xóa bí mật khỏi kho chính không làm bí mật trong bản sao của người khác tự biến mất. Xem thêm: Hồ sơ 01 (mục 4.1).
- **Ép đẩy** (*force push*) — thao tác cập nhật cưỡng bức một nhánh trên kho từ xa, có thể thay thế phần lịch sử mà người khác đang dựa vào. Không tự ý dùng force push để dọn khóa bị lộ; cần thu hồi khóa và phối hợp với người quản lý kho trước. Xem thêm: Hồ sơ 01 (mục 4.1).
- **Gói phụ thuộc, kho phân phối gói, tệp khóa phiên bản** (*dependency*, *registry*, *lockfile*) — dependency là thư viện hoặc gói mà dự án phụ thuộc vào; registry là kho phân phối gói, có thể công khai hoặc riêng; lockfile ghi lại phiên bản cụ thể đã chọn để tái lập việc cài đặt, nhưng không bảo đảm gói đó đáng tin cậy. Xem thêm: Hồ sơ 04 (mục 4.4).
- **Ghi nhận nguồn, quyền sở hữu, trách nhiệm** (*attribution*, *ownership*) — lần lượt là việc ghi nhận nguồn hoặc sự hỗ trợ đã nhận, quyền đối với sản phẩm, và nghĩa vụ kiểm tra, giải trình theo vai trò. Việc ghi nguồn hay khai "AI viết" không tự giải quyết hai vấn đề còn lại. Xem thêm: Hồ sơ 07 (mục 4.7).
- **Giấy phép** (*license*); **MIT, GPL** — giấy phép nêu quyền và điều kiện sử dụng một sản phẩm. Giấy phép MIT yêu cầu giữ thông báo theo điều kiện của giấy phép; giấy phép GPL không cấm sử dụng thương mại. Một kho mã công khai nhưng không có giấy phép không đồng nghĩa với việc được tự do sao chép. Xem thêm: Hồ sơ 06 (mục 4.6).
- **Dữ liệu giả, khử nhận dạng** (*de-identification*) — dữ liệu giả được tạo mới cho bài tập; khử nhận dạng là việc xử lý dữ liệu có thật để giảm khả năng nhận diện cá nhân. Chỉ bỏ tên chưa chắc ngăn được việc tái nhận diện qua thời gian, địa điểm hoặc các mã định danh khác. Xem thêm: Hồ sơ 02 (mục 4.2).
- **Thu hồi khóa, thay khóa, nhật ký** (*revoke*, *rotate*, *log*) — revoke là thu hồi khóa; rotate là thay khóa theo quy trình, cần xác nhận khóa cũ đã bị vô hiệu. Log là nhật ký hoạt động; chỉ xem log trong phạm vi được phép và không đưa bí mật vào bằng chứng. Xem thêm: Hồ sơ 01 (mục 4.1).

<a id="labels"></a>
## Nhãn học tập và hoạt động trong sách

Sách dùng một số nhãn để báo trước loại hoạt động người đọc sắp thực hiện. Tiêu đề mục dùng tên tiếng Việt; nhãn tiếng Anh đặt trong ngoặc đơn và được giữ trên hình minh họa. Các nhãn này là chỉ dẫn đọc, không phải tên chế độ của công cụ AI.

- **Thử thách thực hành** (*AI Challenge*) — bài thực hành yêu cầu tạo một sản phẩm nhỏ kèm bằng chứng, không chỉ đọc đáp án.
- **Bẫy câu trả lời AI** (*AI Trap*) — câu trả lời sai hoặc thiếu điều kiện được dựng sẵn để người học phản biện; không nhằm quy kết một thương hiệu cụ thể. Xem thêm: mục 3.1.
- **Dự đoán trước** (*Think First*) — điểm dừng để người học viết ra dự đoán của bản thân trước khi hỏi AI hoặc xem lời giải. Xem thêm: mục 3.2.
- **Tình huống thực tế** (*Real-World Case*) — tình huống gần với thực tế nhưng vẫn là giả lập nếu không ghi nguồn sự kiện thật.
- **Cơ chế phía sau** (*Behind the Scene*) — phần giải thích cơ chế đằng sau một biểu hiện, giúp hiểu vì sao một thao tác có tác dụng. Xem thêm: mục 1.3.
- **Phân vai AI và người học** (*AI vs Human*) — phần phân biệt việc do AI hỗ trợ với việc người học phải tự chứng minh; không nhằm xếp hạng con người với sản phẩm phần mềm.
- **Câu hỏi tự kiểm tra** (*Quick Check*) — câu hỏi kiểm tra nhanh một điểm kiến thức; trả lời đúng chưa chứng minh đã thành thạo toàn chương.
- **Mẹo thực hành** (*Pro Tip*) — mẹo thao tác kèm điều kiện áp dụng, không phải cách bỏ qua bước kiểm chứng.
- **Cảnh báo an toàn** (*Security Alert*) — điểm dừng để kiểm tra dữ liệu, quyền hoặc hành động có thể gây hại trước khi tiếp tục.
- **Tóm tắt chương** (*Skill Unlocked*) — phần ghi lại năng lực vừa có bằng chứng; không phải chứng chỉ hay kết luận về năng lực lâu dài.
- **Bài thực hành** (*Mission*), **Bài tập tổng hợp** (*Mini Challenge*) — các nhiệm vụ có đầu ra giới hạn. Xem thêm: Chương 2; mục 5.4.
- **Dự án tổng kết** (*Final Boss*) — bài tổng hợp ở cuối sách. Ba cấp Bronze, Silver, Gold chỉ mức độ của nhiệm vụ, không phải các gói dịch vụ trả tiền. Xem thêm: [Dự án tổng kết](final-boss.md).
- **Thí nghiệm ghi nhớ** (*Memory Experiment*) — hoạt động tự quan sát khả năng nhớ lại; không phải nghiên cứu khoa học hay chẩn đoán. Xem thêm: mục 3.4.
- **Phiên tự làm 25 phút không AI** (*25-Minute No-AI*) — phiên tự làm hoàn toàn không dùng AI, khác với phiên học có AI hỗ trợ cùng thời lượng. Xem thêm: mục 3.5.
- **Chuẩn đầu ra học phần** (*CLO — Course Learning Outcome*) — chuẩn đầu ra do đề cương học phần công bố. Mục tiêu của sách, điểm tự đánh giá và dấu "đã tự kiểm" không thay thế CLO hay cách chấm của giảng viên. Xem thêm: [Lời giới thiệu](introduction.md).

Để chuyển các khái niệm "phạm vi", "đóng góp" và "bằng chứng" thành việc làm cụ thể, xem [Thỏa thuận học tập](learning-agreement.md).
