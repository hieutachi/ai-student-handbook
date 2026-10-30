# Glossary · Tra từ để đọc tiếp được

Tìm từ đang vướng, đọc nghĩa rồi trở lại nhiệm vụ; không cần học thuộc bảng.

**Kế thừa:** đủ 16 mục từ mở đầu nguồn. **Bổ sung biên tập:** thuật ngữ xuyên sách, cặp dễ nhầm và nhãn hoạt động. Giải thích này không thay giáo trình.

**Tra theo nhóm:** [AI và quyền truy cập](#ai-access) · [Cách AI xử lý](#ai-process) · [Môi trường](#environment) · [Mã và dữ liệu](#code-data) · [Web](#web) · [Kiểm chứng, Git, nguồn](#evidence) · [Nhãn học tập](#labels).

<a id="ai-access"></a>
## AI: thành phần nào đang làm gì? — Chương 1–2

| Thuật ngữ | Nghĩa và điều cần phân biệt |
|---|---|
| **Model — mô hình** | Thành phần đã được huấn luyện để tạo đầu ra từ đầu vào. Tên model không cho biết toàn bộ công cụ hay ngữ cảnh đang dùng. |
| **Provider — nhà cung cấp** | Bên cung cấp quyền truy cập model, tính phí và xử lý dữ liệu theo dịch vụ; có thể khác bên phát triển model. |
| **Application — ứng dụng** | Phần mềm bạn tương tác, như giao diện chat. Có thể gọi nhiều model, bổ sung tệp và công cụ khi trả lời. |
| **Producer/developer — bên phát triển model** | Bên xây dựng model. Vai trò có thể trùng provider nhưng không tự đồng nhất hai bên. |
| **API — giao diện lập trình ứng dụng** | Quy ước để phần mềm gọi chức năng của phần mềm/dịch vụ khác. Quyền dùng API không mặc nhiên nằm trong thuê bao chat. |
| **API key — khóa API** | Bí mật cấp quyền gọi dịch vụ, có thể phát sinh chi phí. Không dán vào prompt, Git hoặc ảnh; ViSinhVien không cần key. |
| **Ask** | Chế độ hỏi đáp chỉ đọc trong Qoder IDE được sách hướng dẫn. Vẫn kiểm dữ liệu đưa vào ngữ cảnh; không suy quyền sang sản phẩm khác. |
| **Agent** | AI phối hợp đọc tệp, đề xuất/sửa mã hoặc chạy công cụ theo quyền. Prompt “đừng sửa” không thay cơ chế cấp quyền và duyệt hành động. |
| **Qoder IDE / Desktop / CLI** | Các dòng sản phẩm/giao diện khác nhau; đối chiếu tài liệu đúng sản phẩm, không áp tên nút hay chế độ của IDE sang Desktop/CLI. |
| **Free / subscription / quota / hard cap** | Dùng miễn phí, thuê bao, hạn mức và trần chặn sử dụng/chi tiêu. Cảnh báo ngân sách chưa chắc chặn chi tiêu; phải kiểm điều kiện. |

<a id="ai-process"></a>
## AI: đầu vào, xử lý và độ tin cậy — Chương 1, 3

| Thuật ngữ | Nghĩa và ví dụ |
|---|---|
| **Prompt** | Yêu cầu gửi AI; nên nêu mục tiêu, dữ liệu, giới hạn và dạng đầu ra, không chỉ “sửa giúp em”. |
| **Context — ngữ cảnh** | Thông tin model nhận khi trả lời: yêu cầu, lịch sử, mã, tài liệu, kết quả công cụ. Tệp trên máy chưa chắc nằm trong context. |
| **Context window — cửa sổ ngữ cảnh** | Giới hạn thông tin xử lý một lượt, thường đo bằng token. Hội thoại dài có thể bị rút gọn hoặc bỏ phần, không được nhớ nguyên vẹn. |
| **Token** | Đơn vị dữ liệu do bộ tách của model tạo để xử lý, thường dùng tính phí vào/ra. Không bằng một từ hay ký tự. |
| **Inference — suy luận khi sử dụng** | Model tạo đầu ra với tham số hiện có. Thuật ngữ “suy luận” không bảo đảm lập luận đúng. |
| **Training — huấn luyện** | Điều chỉnh tham số model từ dữ liệu. Gửi prompt không đồng nghĩa huấn luyện lại ngay; chính sách lưu/dùng dữ liệu là câu hỏi riêng. |
| **Search / retrieval — tìm kiếm, truy xuất** | Lấy tài liệu từ web hoặc kho dữ liệu để hỗ trợ trả lời, khác huấn luyện. Kết quả vẫn cần đối chiếu. |
| **Grounding — neo vào bằng chứng** | Ràng câu trả lời với mã, dữ liệu, nguồn được cung cấp/truy xuất. Không loại hết lỗi; nguồn phải thực sự hỗ trợ nhận định. |
| **Hallucination — đầu ra bịa hoặc không có căn cứ** | Hàm, nguồn hay kết quả không tồn tại vẫn có thể được nêu tự tin. Kiểm API/tệp/nguồn thật thay vì tin giọng điệu. |
| **Benchmark** | Bộ bài và cách chấm đo khả năng trong điều kiện xác định. So sánh cần cùng nhiệm vụ/tiêu chí; điểm cao không bảo đảm hợp bài của bạn. |
| **Brief / Socratic / vibe coding** | Brief: giao việc ngắn, đủ ràng buộc. Socratic: hỏi dẫn dắt người học tự nghĩ. Vibe coding: triển khai qua mô tả và phản hồi, vẫn phải hiểu/kiểm mã. |

<a id="environment"></a>
## Môi trường làm việc — Chương 2

| Thuật ngữ | Nghĩa và ví dụ |
|---|---|
| **Editor — trình soạn thảo** | Công cụ đọc/sửa mã nguồn; không nhất thiết tự biên dịch, chạy hay kiểm thử. |
| **IDE — môi trường phát triển tích hợp** | Kết hợp editor với công cụ chạy, gỡ lỗi, terminal. Tích hợp AI không bảo đảm thao tác đúng. |
| **Terminal** | Cửa sổ tương tác bằng chữ để nhập lệnh, xem đầu ra; không phải chương trình diễn giải lệnh. |
| **Shell** | Chương trình đọc/thực hiện lệnh, như Bash hoặc PowerShell; phải chọn cú pháp đúng shell. |
| **CLI — giao diện dòng lệnh** | Điều khiển công cụ bằng lệnh và đối số thay vì nút bấm, qua shell trong terminal. Ba khái niệm không đồng nghĩa. |
| **Thư mục làm việc — working directory, cwd** | Vị trí dùng giải đường dẫn tương đối. Xem bằng `pwd` trong Bash, `Get-Location` trong PowerShell. |
| **Đường dẫn tương đối / tuyệt đối** | Tương đối phụ thuộc vị trí đang xét; tuyệt đối tính từ gốc hệ thống. Link Markdown và lệnh terminal có thể có gốc khác nhau. |
| **Biên dịch — compile; build** | Compile dịch mã C++ sang dạng đích; build gồm cả các bước như liên kết. Build lỗi thì dừng, không lấy tệp cũ chứng minh mã mới đúng. |
| **Executable / runtime** | Tệp chạy được / môi trường thực thi. C++ tạo executable; Node.js chạy JavaScript nhưng không có sẵn DOM trình duyệt. |
| **stdout / stderr / exit code** | Luồng đầu ra thường / luồng lỗi / mã kết thúc. Exit code `0` thường báo thành công, khác `0` báo lỗi; không tự chứng minh thuật toán đúng. |

<a id="code-data"></a>
## Kiểu dữ liệu và tư duy lập trình — Chương 2–3

| Thuật ngữ | Nghĩa trong sách và ví dụ |
|---|---|
| **Expense** | Mô hình khoản chi Web với `id`, `title`, `amount`, `category`. Đối tượng có trường dữ liệu không tự đồng nghĩa đã thiết kế một hệ thống OOP đầy đủ. |
| **`vector<long long>`** | Danh sách động của C++ chứa số nguyên kiểu `long long`; bản năm nhất chỉ chứa tiền. Không gán thêm tên/nhóm vào mô hình này khi mô tả mã hiện có. |
| **OOP — lập trình hướng đối tượng** | Tổ chức chương trình quanh đối tượng, trạng thái và hành vi với trách nhiệm rõ. Có một object JavaScript chưa chứng minh đã áp dụng mọi nguyên lý OOP. |
| **DSA — cấu trúc dữ liệu và giải thuật** | Chọn cách tổ chức dữ liệu và các bước xử lý. Trong bài tổng, danh sách cùng phép duyệt là điểm nối với kiến thức DSA. |
| **Complexity — độ phức tạp** | Mô tả tài nguyên tăng theo kích thước đầu vào. Duyệt `n` khoản có thời gian `O(n)`; một biến cộng dồn dùng bộ nhớ phụ `O(1)`, không tính danh sách đầu vào. |
| **Safe integer — số nguyên an toàn** | Với JavaScript `Number`, miền từ `-9007199254740991` đến `9007199254740991` bảo đảm phân biệt chính xác từng số nguyên. `Number.isSafeInteger` không thay điều kiện tiền phải dương và không quá `1e9`. |
| **Unsigned — kiểu không dấu; tràn giá trị** | Kiểu nguyên không âm trong C++ tính theo modulo: `0 - 1` trên kiểu unsigned vòng về giá trị lớn. Tràn số nguyên có dấu lại là hành vi không xác định. |
| **Index / out-of-bounds / UB** | Index là chỉ số; ngoài phạm vi hợp lệ là out-of-bounds. Truy cập ngoài biên bằng `vector::operator[]` gây undefined behavior (UB), có thể không crash; “chạy được” không chứng minh hợp lệ. |
| **Reference / copy / `const`** | Reference tham chiếu đối tượng sẵn có; copy tạo bản sao. `const std::vector<long long>&` cho hàm đọc qua tham chiếu không sửa vector qua tham chiếu ấy, tránh sao chép toàn danh sách. |
| **String / number / conversion** | Chuỗi và số là hai kiểu khác nhau. Ô nhập trả chuỗi; chuyển kiểu chưa chứng minh hợp đồng hợp lệ. `parseInt` có thể chỉ đọc đầu chuỗi, nên không dùng thay validation. |
| **`undefined` / `NaN`** | Đọc trường không có như `item.value` có thể nhận `undefined`; đem cộng có thể thành `NaN`, giá trị biểu thị kết quả số không hợp lệ. Đối chiếu tên `amount` trước. |
| **Validation / schema / normalization** | Validation kiểm điều kiện; schema mô tả cấu trúc; normalization đưa dữ liệu về dạng thống nhất. Web kiểm đủ bản ghi bằng `normalizeExpenses`; `totalExpenses` chỉ kiểm tiền và số lượng. |

<a id="web"></a>
## Web, lưu trữ và ranh giới dữ liệu — Chương 2–4

| Thuật ngữ | Nghĩa trong sách và ví dụ |
|---|---|
| **DOM — Document Object Model** | Cây đối tượng biểu diễn tài liệu Web để JavaScript đọc/sửa. Test hàm tính tổng trong Node.js không xác nhận trang đã cập nhật DOM đúng. |
| **Event handler — hàm xử lý sự kiện** | Hàm chạy khi có sự kiện, như gửi biểu mẫu. Hàm vô danh vẫn có trách nhiệm và vị trí trong luồng; theo dữ liệu thay vì chỉ tìm tên hàm. |
| **JSON** | Định dạng văn bản trao đổi dữ liệu với cú pháp xác định. Phân tích JSON thành công không chứng minh `amount` hay các trường còn lại đúng hợp đồng. |
| **Origin** | Với địa chỉ Web thông thường, là bộ giao thức, tên máy chủ và cổng. Trình duyệt dùng origin để tách nhiều quyền/dữ liệu; không coi mọi tệp `file://` có hành vi giống nhau. |
| **`localStorage`** | Kho khóa–giá trị chuỗi của trình duyệt theo origin. Có thể bị chặn hoặc chứa dữ liệu cũ/sai; không là cơ sở dữ liệu máy chủ, đăng nhập hay kho tài chính bảo mật. |
| **Fallback / RAM** | Fallback là phương án thay thế khi cách chính thất bại. Demo dùng bộ nhớ tạm khi không lưu được; thay đổi không được bảo đảm còn sau khi kết thúc phiên. |
| **Backend / SQLite / `:memory:`** | Backend xử lý phía máy chủ; Web của sách không có phần này. SQLite là hệ quản trị cơ sở dữ liệu nhúng; `:memory:` tạo cơ sở dữ liệu trong bộ nhớ cho minh họa Python riêng. |
| **SQL / truy vấn tham số hóa / tuple** | SQL là ngôn ngữ làm việc với dữ liệu quan hệ. Truy vấn tham số hóa tách giá trị khỏi cấu trúc lệnh; `(title,)` là tuple một phần tử Python, dấu phẩy tạo tuple. |
| **Injection / allowlist** | Injection xảy ra khi dữ liệu không tin cậy làm đổi ý nghĩa lệnh. Allowlist là danh sách cho phép; dùng khi chọn cấu trúc như tên cột, không chèn chuỗi tùy ý. |
| **XSS / `textContent` / `innerHTML`** | XSS liên quan nội dung không tin cậy dẫn tới thực thi script trong trang. `textContent` đặt văn bản ở ô bảng; `innerHTML` phân tích HTML. Không suy biện pháp cho văn bản sang URL hoặc mã JavaScript. |

<a id="evidence"></a>
## Kiểm chứng, Git và quyền dùng nguồn — Chương 2–4

| Thuật ngữ | Nghĩa trong sách và điều cần nhớ |
|---|---|
| **Trace / mô phỏng** | Trace lần theo giá trị, nhánh và vòng lặp từng bước. Mô phỏng là tình huống được dựng để giải thích. Cả hai không tự trở thành nhật ký chạy phần mềm thật. |
| **Test case / fixture / regression test** | Ca kiểm thử gồm đầu vào và điều cần đối chiếu. Fixture là dữ liệu giả chuẩn bị riêng. Regression test kiểm lỗi đã sửa không tái xuất hiện, như `category` là mảng. |
| **Kỳ vọng / quan sát / bằng chứng** | Kỳ vọng viết trước khi chạy; quan sát ghi điều thực sự xảy ra; bằng chứng gắn với bản mã, môi trường và cách kiểm. “Chưa chạy” khác “không đạt”. |
| **Diff / review** | Diff so trước–sau, chỉ dòng thêm, bớt, đổi. Review là xem xét thay đổi và lý do; đọc diff không tương đương chạy test, nhưng giúp phát hiện sửa vượt phạm vi. |
| **Commit / checkpoint** | Commit ghi một mốc trạng thái trong kho Git. Checkpoint là mốc quay lại đã chuẩn bị, có thể là commit hoặc bản sao; cả hai không chứng nhận mã đúng. |
| **Clone** | Tạo bản sao kho Git, thường có cả lịch sử liên quan. Xóa bí mật ở kho chính không khiến bí mật trong clone của người khác tự biến mất. |
| **Force push — ép đẩy** | Cập nhật nhánh từ xa cưỡng bức, có thể thay thế lịch sử người khác đang dựa vào. Không tự dùng để dọn key; thu hồi key và phối hợp người quản lý kho trước. |
| **Dependency / registry / lockfile** | Dependency là thư viện/gói phụ thuộc; registry là kho phân phối gói, công khai hoặc riêng. Lockfile ghi lựa chọn phiên bản cụ thể để tái lập cài đặt, không bảo đảm gói đáng tin. |
| **Attribution / ownership / trách nhiệm** | Lần lượt là ghi nhận nguồn/hỗ trợ, quyền đối với sản phẩm và nghĩa vụ kiểm tra/giải trình theo vai trò. Ghi nguồn hay khai “AI viết” không tự giải quyết hai phần còn lại. |
| **License — giấy phép; MIT / GPL** | Giấy phép nêu quyền và điều kiện sử dụng. MIT yêu cầu giữ thông báo theo điều kiện; GPL không cấm thương mại. Kho công khai không giấy phép không đồng nghĩa tự do sao chép. |
| **Dữ liệu giả / khử nhận dạng** | Dữ liệu giả được tạo mới cho bài; khử nhận dạng xử lý dữ liệu có thật. Chỉ bỏ tên chưa chắc ngăn tái nhận diện qua giờ, địa điểm hoặc mã khác. |
| **Revoke / rotate / log** | Revoke thu hồi khóa; rotate thay khóa theo quy trình, cần xác nhận khóa cũ vô hiệu. Log là nhật ký hoạt động; chỉ xem trong quyền được phép, không đưa bí mật vào bằng chứng. |

<a id="labels"></a>
## Nhãn học tập: nhìn nhãn để biết mình cần làm gì

**Mười nhãn editorial dùng xuyên sách** là chỉ dẫn đọc, không phải tên chế độ AI:

| Nhãn | Cách dùng |
|---|---|
| **AI CHALLENGE** | Bài thực hành: tạo sản phẩm nhỏ và bằng chứng, không chỉ đọc đáp án. |
| **AI TRAP** | Lời đáp sai hoặc thiếu điều kiện được dựng để bạn phản biện; không quy kết một thương hiệu. |
| **THINK FIRST** | Dừng và viết dự đoán của mình trước khi hỏi hoặc xem lời giải. |
| **REAL-WORLD CASE** | Tình huống gần thực tế nhưng vẫn giả lập nếu không ghi nguồn sự kiện thật. |
| **BEHIND THE SCENE** | Giải thích cơ chế phía sau biểu hiện, giúp hiểu vì sao thao tác có tác dụng. |
| **AI VS HUMAN** | Phân biệt phần AI hỗ trợ và phần người học tự chứng minh; không xếp hạng người với sản phẩm. |
| **QUICK CHECK** | Tự kiểm nhanh một điểm hiểu; trả lời đúng chưa chứng minh thành thạo toàn chương. |
| **PRO TIP** | Mẹo thao tác có điều kiện áp dụng, không phải cách bỏ qua kiểm chứng. |
| **SECURITY ALERT** | Dừng để kiểm dữ liệu, quyền hoặc hành động có thể gây hại trước khi tiếp tục. |
| **SKILL UNLOCKED** | Ghi năng lực vừa có bằng chứng; không là chứng chỉ hoặc kết luận năng lực lâu dài. |

**Mission / MINI CHALLENGE** là nhiệm vụ có đầu ra giới hạn. **Final Boss** là bài tổng hợp; Bronze, Silver, Gold chỉ mức nhiệm vụ, không phải gói trả tiền. **Memory Experiment** là tự quan sát việc nhớ lại, không nghiên cứu hay chẩn đoán. **25-MINUTE NO-AI** là phiên không AI, khác phiên học có AI cùng thời lượng.

**CLO — Course Learning Outcome:** chuẩn đầu ra do đề cương học phần công bố. Mục tiêu sách, điểm tự đánh giá và dấu “đã tự kiểm” không thay CLO hay cách chấm của giảng viên.

Quay lại [mở đầu](introduction.md) hoặc dùng [thỏa thuận học tập](learning-agreement.md) để chuyển các từ “phạm vi”, “đóng góp” và “bằng chứng” thành việc cụ thể.
