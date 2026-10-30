# HỌC CNTT CÙNG AI · CẨM NANG KHỞI ĐẦU

Hiểu công cụ · Làm chủ kiến thức · Sử dụng có trách nhiệm

Phiên bản 30/10/2026. Năm chương ngắn, dự án tổng kết một trang, thư viện prompt và bảng thuật ngữ. Bản đầy đủ nằm trong Sổ tay thực hành.


---

## LỜI GIỚI THIỆU

**Học CNTT cùng AI — Cẩm nang khởi đầu dành cho sinh viên năm thứ nhất và năm thứ hai, Khoa Công nghệ thông tin, Trường Đại học Thủy lợi.**

### Cuốn sách này dành cho ai

Các công cụ trí tuệ nhân tạo (AI) có thể giải thích lỗi, đề xuất mã nguồn và gợi ý ca kiểm thử trong vài giây. Câu hỏi cho người học lập trình là: làm sao tận dụng công cụ mà không giao luôn phần suy nghĩ cho nó. Cẩm nang này trả lời bằng những kỹ năng cụ thể, mỗi kỹ năng kèm một việc nhỏ để thử.

Đối tượng chính là sinh viên năm thứ nhất và năm thứ hai ngành Công nghệ thông tin: chỉ cần biết biến, câu lệnh điều kiện và vòng lặp trong C++; kiến thức Web và cơ sở dữ liệu là lợi thế thêm. Không cần mua dịch vụ AI trả phí để bắt đầu.

### Năm bước của một câu chuyện

Cẩm nang kể một câu chuyện duy nhất, quan hệ giữa người học và AI, qua năm bước; mỗi chương là một bước.

**Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn**

| Chương | Câu hỏi trung tâm | Thông điệp |
|---|---|---|
| 1 | AI là gì, đóng vai trò gì trong học tập, giúp được gì và không giúp được gì? | AI là người hỗ trợ; người học là người quyết định. |
| 2 | Dùng AI thế nào để việc làm có kiểm soát? | Giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. |
| 3 | Tận dụng AI mà không lạm dụng: làm sao vẫn học được? | Tự dự đoán, tự làm, tự giải thích; AI chỉ đứng cạnh. |
| 4 | Ranh giới nào cần giữ về dữ liệu, bảo mật, bản quyền, liêm chính? | Dùng có trách nhiệm là điều kiện để được tiếp tục dùng. |
| 5 | Khi đã hiểu vai trò, cách dùng và ranh giới: chọn AI, model, gói dịch vụ nào cho nhiệm vụ này? | Chọn theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng. |

Dự án tổng kết ghép năm bước thành một sản phẩm có bằng chứng: làm, kiểm, giải thích. Việc chọn model và trả phí nằm ở cuối vì chỉ khi đã hiểu vai trò, cách dùng và ranh giới, người học mới chọn có cơ sở. Một ý cần nhớ xuyên suốt: **AI hỗ trợ, người học quyết định.**

### Hai người học và ba khoản chi

Sách dựa trên một tình huống minh họa chung:

- **Minh**, năm thứ nhất, đã biết biến và vòng lặp trong C++, nhưng có thói quen hỏi AI ngay khi gặp lỗi.
- **Lan**, năm thứ hai, đã học Web và cơ sở dữ liệu, dựng được giao diện nhưng còn lúng túng khi một lỗi đi qua nhiều tệp.

Hai người cùng xây dựng **ViSinhVien**, ứng dụng ghi các khoản chi tiêu nhỏ, với bảng dữ liệu mẫu dùng trong mọi chương:

| Khoản chi | Nhóm | Số nguyên lưu trong mã | Hiển thị |
|---|---|---:|---:|
| Cơm trưa | Ăn uống | `35000` | 35.000 đ |
| Xe buýt | Đi lại | `7000` | 7.000 đ |
| Vở ghi | Học tập | `18000` | 18.000 đ |
| **Tổng đối chiếu** | | **`60000`** | **60.000 đ** |

Hai vấn đề mở đầu dẫn dắt cả cuốn sách: phiên bản C++ của Minh cho tổng `42000` thay vì `60000`; Lan cần xác định giá trị tiền đi từ ô nhập đến phần tính tổng như thế nào. Qua các chương, chúng ta lần lượt dự đoán, kiểm tra và giải thích. Người học chọn nhánh Minh (C++) hoặc nhánh Lan (Web) tùy kiến thức đã có.

### Phạm vi của nội dung

Nhân vật, hội thoại, tình huống và dữ liệu trong sách đều hư cấu, không phải kết quả khảo sát sinh viên hay bảng giá thực tế của dịch vụ nào. Sách không phải quy định chính thức của Trường Đại học Thủy lợi, không phải đề cương học phần hay tư vấn pháp lý; mức độ được dùng AI trong một bài cụ thể do giảng viên quyết định. Thông tin về sản phẩm, dịch vụ và văn bản pháp lý đối chiếu tại mốc 29/10/2026, cần tra lại trước khi dùng.

Sách dùng thống nhất bốn nhãn: *Tình huống hư cấu* cho nhân vật, hội thoại và thẻ trả lời minh họa; *Dữ liệu giả định* cho số tiền, giá và kịch bản tính toán; *Chưa kiểm chứng* cho thông tin dịch vụ, chính sách cần tra lại; *Kết quả mong đợi* cho đầu ra suy ra từ mã nguồn, chưa thực thi.

### Cách dùng hai cuốn

Hai cuốn dùng chung một câu chuyện và một bộ ví dụ.

Hãy đọc **Cẩm nang khởi đầu** (cuốn đang mở) trước. Mỗi mục nêu một ý chính, cho một việc nhỏ "Thử ngay" làm được trong mười phút không cần tài khoản AI, rồi để lại câu hỏi mở. Cẩm nang không in đáp án; "Gợi ý đối chiếu" chỉ nêu tiêu chí để tự biết đã đúng hướng.

**Sổ tay thực hành** là nơi đi sâu. Khi muốn làm bài đầy đủ, xem đáp án hay bảng kiểm thử, hãy mở [Sổ tay thực hành](chapters/introduction.md). Mỗi mục trong cẩm nang kết thúc bằng phần "Tự tìm hiểu thêm" trỏ tới mục tương ứng của Sổ tay.

Đi kèm là ba phần tham khảo: [Thư viện prompt mẫu](cam-nang/prompt-library.md) với các thẻ giao việc, [Bảng thuật ngữ](cam-nang/glossary.md) và [Thỏa thuận học tập](chapters/learning-agreement.md) với mẫu khai báo mức hỗ trợ của AI. Khi gặp điều chưa rõ, hãy hỏi giảng viên; câu trả lời của AI không thay thế cho việc kiểm chứng.

---

## CHƯƠNG 1 · AI TRONG HỌC TẬP: VAI TRÒ, CÁCH HOẠT ĐỘNG VÀ GIỚI HẠN

Lời giới thiệu đã nêu mạch năm bước **Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn**, giới thiệu Minh, Lan và bài tập ViSinhVien với ba khoản chi giả. Chương này là bước *Hiểu*: trước khi gõ câu hỏi đầu tiên, người học cần biết AI giúp được gì, không giúp được gì, "AI" đang mở trên màn hình gồm những thành phần nào, và phía sau một câu trả lời có gì. Toàn bộ chương làm được bằng giấy và bút.

Nhân vật, hội thoại và ba thẻ trả lời trong chương là *tình huống hư cấu*; thông tin về dịch vụ AI được ghi theo mốc 29/10/2026 và *chưa kiểm chứng* độc lập.

**Sau chương này, người học có thể:**

- Nêu ba vai trò hợp lý của AI trong học tập; phân biệt dùng AI để học với dùng AI để né học.
- Gọi đúng tên model, provider, application, producer trong một lượt dùng AI; ghi "chưa xác định" khi thiếu bằng chứng.
- Viết một prompt đủ context cho một lỗi nhỏ; giải thích token và context window ở mức khái niệm.
- Chuyển một câu trả lời tự tin của AI thành câu hỏi kiểm chứng.

### Tình huống mở đầu

Minh, sinh viên năm nhất đang học C++, ghi ba khoản chi giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000. Tổng phải là 60000 VND. Chương trình tính tổng của Minh lại in ra 42000; vòng lặp dùng điều kiện `i < n - 1` với `n = 3`.

Minh dán đoạn mã vào ba ứng dụng AI khác nhau, kèm cùng một yêu cầu: "Hãy gợi ý một bước để tự tìm lỗi, chưa viết lại cả chương trình." Ba câu trả lời, rút gọn, như sau.

> **Thẻ A.** Khi `n = 3`, chỉ số của khoản Vở ghi là bao nhiêu? Hãy thay chỉ số đó vào điều kiện `i < n - 1` và tự quyết định xem vòng lặp có cộng khoản này không.

> **Thẻ B.** Vòng lặp thiếu một lượt. Cứ đổi thành `i <= n`; như vậy sẽ cộng đủ và luôn an toàn. Không cần thử thêm vì lỗi này rất đơn giản.

> **Thẻ C.** Điều kiện đang bỏ phần tử cuối. Hướng sửa là `i < n`, không phải `i <= n`. Chương trình chưa được chạy thử; hãy kiểm tra danh sách rỗng, một khoản và ba khoản sau khi tự sửa.

Cả ba đều là AI. Vì sao chúng trả lời khác nhau, và Minh nên bắt đầu học từ thẻ nào? Hãy ghi lựa chọn và lý do trước khi đọc tiếp; cuối mục 1.3, chúng ta chấm lại ba thẻ.

### 1.1. Vai trò của AI trong học tập: giúp được gì, không giúp được gì, đâu là lạm dụng

Mục này trả lời câu hỏi đứng trước mọi câu hỏi kỹ thuật: nên để AI làm phần việc nào trong quá trình học, và phần việc nào phải giữ lại cho người học. Câu trả lời được rút ra từ ba thẻ A, B, C và ba khoản chi 35000, 7000, 18000.

#### Ý chính 1 — Ba vai trò hợp lý và hai mặt của công cụ

Học là quá trình thay đổi hiểu biết và kỹ năng của chính người học. Vì vậy, một vai trò của AI chỉ hợp lý khi sau lượt dùng, người học hiểu hoặc làm được nhiều hơn trước. Có ba vai trò đáp ứng điều kiện đó.

**Gia sư giải thích.** AI giải thích một khái niệm theo nhiều cách, đổi ví dụ khi người học chưa hiểu, hoặc đặt câu hỏi gợi mở thay vì đưa ngay đáp án. Thẻ A làm đúng việc này: không sửa hộ mà hỏi chỉ số của khoản Vở ghi. Minh phải tự trả lời, nên người hiểu vòng lặp là Minh.

**Người phản biện.** Sau khi tự làm xong, người học nhờ AI tìm chỗ thiếu: ca kiểm thử chưa nghĩ tới, điều kiện biên bị bỏ sót. Thẻ C làm việc này khi nhắc kiểm tra danh sách rỗng, một khoản và ba khoản. Thứ tự rất quan trọng: *làm trước, nhờ phản biện sau*.

**Trợ lý cho việc lặp.** Định dạng lại bảng, đổi tên biến đồng loạt, sinh dữ liệu giả: những việc tốn thời gian nhưng không tạo ra hiểu biết mới. Nếu việc đó chính là mục tiêu của bài học (bài đang dạy vòng lặp mà nhờ AI viết vòng lặp), thì nó không còn là "việc lặp".

Ba vai trò có chung một điểm: AI nằm cạnh người học, không nằm thay chỗ người học.

| AI thường làm tốt | AI thường làm kém hoặc không thể làm |
| --- | --- |
| **Tốc độ**: phản hồi sau vài giây, thử được nhiều cách hỏi | **Sai mà vẫn tự tin**: thẻ B khẳng định `i <= n` "luôn an toàn" trong khi cách sửa đó truy cập ngoài danh sách |
| **Diễn đạt**: giải thích lại cùng một ý ở nhiều mức | **Thiếu ngữ cảnh**: chỉ biết điều đã được gửi; quên dán mã thì AI đoán |
| **Gợi ý**: nêu nhiều hướng giải, nhiều ca thử | **Không chịu trách nhiệm**: bài nộp mang tên người học |

Quy tắc phân công rút ra từ bảng: giao cho AI phần mà **kết quả kiểm tra được nhanh** (ca thử, định dạng, gợi ý hướng đi); giữ lại cho người học phần mà **hiểu biết và trách nhiệm không thể chuyển giao** (quyết định cuối, giải thích, kiểm chứng).

#### Ý chính 2 — Dùng AI để học và dùng AI để né học

Cùng một công cụ, cùng một bài toán, có thể dẫn tới hai kết quả khác hẳn nhau. Minh tự cộng ba khoản trước, thấy chương trình thiếu đúng 18000, rồi nhờ AI gợi ý một bước. Sau đó Minh tự sửa cận vòng lặp, thử ca rỗng, một khoản, ba khoản, và giải thích được vì sao `i < n` đúng còn `i <= n` thì không. Đây là *dùng AI để học*. Cách làm khác: dán mã, nhận bản sửa hoàn chỉnh, chép vào bài và nộp. Chương trình in đúng 60000, nhưng khi được hỏi "vì sao vòng lặp dừng ở chỉ số 1", người học không trả lời được. Đây là *dùng AI để né học*.

Điểm khác biệt không nằm ở việc có dùng AI hay không, mà ở chỗ **ai đã suy nghĩ**:

| Tiêu chí | Dấu hiệu dùng đúng | Dấu hiệu lạm dụng |
| --- | --- | --- |
| Thứ tự | Tự thử hoặc tự dự đoán trước, rồi mới hỏi | Hỏi ngay khi vừa đọc đề |
| Mức trợ giúp | Xin gợi ý từng bước | Xin bản hoàn chỉnh rồi chép nguyên |
| Kiểm chứng | Tự chạy, tự đối chiếu với 60000 | Tin lời "đã đúng", không chạy |
| Giải thích | Nói lại được bằng lời riêng | Không giải thích được dòng mã vừa nộp |

Một phép thử nhanh: sau khi dùng AI, nếu người học tự lần ra được tổng từng bước (35000, rồi 42000, rồi 60000) và chỉ ra bước nào bị bỏ, thì hiểu biết đã thuộc về người học. Nếu không, kết quả đúng chỉ là mượn. Ngoài ra, mỗi học phần có thể quy định riêng về mức được dùng AI.

Từ đây rút ra nguyên tắc mà cả cuốn sách sẽ nhắc lại: **AI hỗ trợ, người học quyết định.** Người học *đặt mục tiêu* (nêu việc cần làm, giới hạn mức trợ giúp, chọn dữ liệu được gửi), *kiểm chứng* (không dùng kết quả chưa có bằng chứng) và *chịu trách nhiệm* (mọi dòng trong bài nộp phải giải thích được). Trong hình dưới đây, người dùng đứng ở cả hai đầu của một lượt hỏi: giao việc đi và kiểm tra kết quả về; các ô còn lại được gọi tên ở mục 1.2.

![Bốn vai trò xếp Model, Provider, Application, User. Request đi ngược từ User tới Model; response xuôi từ Model tới User. Mũi tên không biểu thị quan hệ sở hữu.](assets/roles.svg)

#### Thử ngay (10 phút)

Mục tiêu: tự áp bảng dấu hiệu vào ba tình huống giả định. Với mỗi tình huống, ghi một trong ba lựa chọn **dùng đúng**, **lạm dụng** hoặc **cần hỏi giảng viên**, kèm một câu lý do.

1. Lan nhờ AI viết trọn phần lưu dữ liệu vào `localStorage`, dán vào bài và nộp mà chưa đọc mã.
2. Đề bài ghi "sinh viên tự làm", nhưng Minh muốn nhờ AI giải thích một thông báo lỗi khó hiểu của trình biên dịch.
3. AI báo "đã chạy test và tất cả đều đạt"; Lan ghi vào báo cáo như kết quả của chính Lan mà không chạy lại.

Ghi lại ba lựa chọn, ba lý do và tiêu chí nào trong bảng đã quyết định.

#### Gợi ý đối chiếu

Lý do hợp lý phải gọi tên được ít nhất một tiêu chí: thứ tự, mức trợ giúp, kiểm chứng, giải thích hay quyền quyết định. Khi câu chữ của đề bài chưa đủ rõ, lựa chọn đúng không phải là suy diễn theo hướng có lợi. Lời "đã chạy test" của AI chưa phải bằng chứng. Nếu cả ba lý do đều chỉ nói "vì có dùng AI", cần đọc lại bảng dấu hiệu.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Trong học phần đang học, việc nào là "mục tiêu của bài" nên phải tự làm, việc nào là "việc lặp" có thể giao cho AI? Giảng viên có đồng ý với cách chia đó không?
- **Từ khóa tra cứu:** AI literacy, academic integrity, productive struggle.
- **Trong Sổ tay thực hành:** [Mục 1.1](chapters/chapter-01.md#muc-1-1) có đủ năm tình huống tự đánh giá kèm lời giải, bảng dấu hiệu sáu tiêu chí và ba nghĩa của nguyên tắc.

### 1.2. Nhận diện công cụ AI: model, provider và ứng dụng (AI Map)

Câu "đang dùng ChatGPT" chỉ nêu tên sản phẩm đang mở, chưa nói model nào xử lý yêu cầu. Mục này giúp người học gọi đúng tên từng thành phần của một lượt dùng AI, và dám ghi "chưa xác định" khi thiếu bằng chứng.

#### Ý chính 1 — Bốn câu hỏi: model, provider, application và producer

Hãy nhìn lại con số 42000. Ta có 35000 + 7000 = 42000; phải cộng thêm 18000 mới được 60000. Vậy 42000 là tổng trung gian đúng của hai khoản đầu; nó chỉ thành sai lệch khi yêu cầu là cộng đủ ba khoản. Với `n = 3`, các chỉ số hợp lệ là 0, 1 và 2; điều kiện `i < n - 1`, tức `i < 2`, khiến vòng lặp dừng trước khoản Vở ghi. Thẻ A giữ đúng yêu cầu gợi ý một bước nên là nơi bắt đầu học. Thẻ C sửa đúng và nói rõ chưa chạy, phù hợp để đối chiếu sau khi tự sửa. Thẻ B phải bị loại: `i <= n` cho phép chỉ số `n` nằm ngoài danh sách, trong C++ là hành vi không xác định.

Ba thẻ không cho biết "AI nào tốt hơn", vì chưa biết phía sau mỗi thẻ là gì. Cần tách bốn câu hỏi.

**Model** là mô hình tính toán đã được huấn luyện để xử lý đầu vào và tạo đầu ra. Các tên như GPT, Claude hay Gemini có thể chỉ một họ mô hình, chưa phải một phiên bản cụ thể. **Provider** là bên cung cấp đường truy cập đến model: tiếp nhận yêu cầu, xác thực và áp điều kiện sử dụng; provider có thể tự vận hành model hoặc chỉ là trung gian. **Producer** là bên xây dựng, huấn luyện hoặc phát hành model; producer và provider có thể là một tổ chức, nhưng không bắt buộc. **Application** (ứng dụng) là nơi người dùng thao tác: trang chat, ứng dụng trên điện thoại, trợ lý lập trình; ứng dụng chọn thông tin gửi đi, giữ lịch sử và hiển thị bản sửa. **User** (người dùng) đặt mục tiêu và kiểm tra kết quả.

| Vai trò | Câu hỏi phải trả lời | Cách ghi nếu thiếu bằng chứng |
| --- | --- | --- |
| Model | Thành phần nào tạo đầu ra? Định danh nào được công bố? | "Chỉ biết họ model, chưa xác định phiên bản" |
| Provider | Ai cung cấp đường truy cập cho ứng dụng? | "Chưa xác định provider" |
| Application | Đang thao tác ở phần mềm nào? | Ghi tên quan sát được, không suy ra model từ tên ứng dụng |
| Producer | Ai phát triển hoặc phát hành model? | "Chưa đủ dữ kiện"; không gán cho nhóm viết giao diện |

Một ví dụ điển hình là Claude qua Amazon Bedrock: Anthropic phát triển Claude, còn AWS cung cấp đường truy cập qua Bedrock. Vì vậy, nhãn "hỗ trợ Claude" trên một ứng dụng không tự chứng minh ứng dụng kết nối trực tiếp tới Anthropic. Tương tự, "mở ứng dụng Gemini", "gọi Gemini API" và "chọn một model thuộc họ Gemini" là ba việc khác nhau.

#### Ý chính 2 — API, key và các đường truy cập

**API** (*application programming interface*) là giao diện để các phần mềm giao tiếp với nhau theo quy tắc xác định. Khi dùng ứng dụng chat, Minh gõ câu hỏi và gửi đi; khi dùng API, một chương trình chuẩn bị request theo định dạng dịch vụ quy định và có thể chỉ định model. API không phải một model mới, cũng không phải "bộ não tải về máy". **API key** là thông tin xác thực để dịch vụ nhận biết quyền truy cập. Có key không có nghĩa là sở hữu model, có quota vô hạn hay được miễn phí.

Một lưu ý an toàn: không đưa key thật vào chat, ảnh chụp màn hình, nhóm lớp hay kho mã công khai; không nhúng key vào JavaScript phía trình duyệt. ViSinhVien không cần key. Nếu nghi key đã lộ, việc đầu tiên là thu hồi key ở dịch vụ, không phải xóa dòng khỏi tệp; quy trình đầy đủ ở [Hồ sơ 01 của Sổ tay](chapters/chapter-04.md#muc-4-1).

![Chat web, API và trợ lý IDE đi qua cổng dịch vụ tới model từ xa; một nhánh riêng chạy model trên máy. Không có thứ hạng thương hiệu.](assets/ecosystem.svg)

Các đường truy cập trong hình không phải bậc thang thứ hạng: API hay agent không mặc nhiên "cao cấp" hơn chat. Luồng giản lược là **người dùng → ứng dụng chuẩn bị thông tin → provider tiếp nhận → model tạo đầu ra → ứng dụng hiển thị → người dùng kiểm tra**. Một ứng dụng cài trên máy vẫn có thể gửi dữ liệu lên đám mây.

Hệ quả quan trọng: **cùng câu hỏi không đồng nghĩa với cùng đầu vào**. Cùng một câu Minh gõ có thể được gửi kèm lịch sử, tài liệu, chỉ dẫn hệ thống hoặc công cụ khác nhau; một ứng dụng được cấu hình đóng vai gia sư, ứng dụng khác ưu tiên sinh mã. Vì thế ba thẻ khác nhau chưa chứng minh ba model khác nhau. Khi điều tra, Minh làm ba bước: **ghi nhãn ứng dụng, chế độ và model → liệt kê context và công cụ → ghi rõ phần chưa biết**. Nếu giao diện chỉ hiện nhãn "Tự động", chỉ được ghi "chưa xác định model xử lý lượt này".

#### Thử ngay (10 phút)

Mục tiêu: điền bản đồ vai trò cho một ứng dụng giả định, chỉ bằng giấy. Ứng dụng "Gia sư ViSinhVien" tự mô tả là "dùng Gemini API" nhưng không công bố model cụ thể.

1. Kẻ bốn dòng: Model, Provider, Application, Producer. Điền từng dòng; chỗ nào chưa có bằng chứng, ghi đúng cụm "chưa xác định" kèm lý do.
2. Thay phần mô tả bằng "hỗ trợ Claude". Điền lại và gạch chân những dòng vừa thay đổi.

Ghi lại hai bản đồ và một câu: thông tin nào mất đi khi mô tả đổi từ "Gemini API" sang "hỗ trợ Claude"?

#### Gợi ý đối chiếu

Dòng Application phải là tên quan sát được, không phải tên model. Dòng Provider ở bản đồ thứ nhất chỉ được ghi theo tự mô tả, chưa xác minh, vì ứng dụng có thể đi qua trung gian. Dòng Model chỉ biết họ, chưa biết phiên bản. Nhóm viết ứng dụng không phải Producer. Ở bản đồ thứ hai, số ô "chưa xác định" phải nhiều hơn.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Với ứng dụng AI đang dùng nhiều nhất, có tìm được tài liệu chính thức ghi rõ model và provider không? Nếu chỉ có nhãn "Tự động", điều đó ảnh hưởng gì khi phải khai báo việc dùng AI trong bài nộp?
- **Từ khóa tra cứu:** model card, model provider, API key, inference endpoint.
- **Trong Sổ tay thực hành:** [Mục 1.2](chapters/chapter-01.md#muc-1-2) có phân tích đầy đủ ba thẻ, lời giải bài nhận diện và ví dụ phân biệt các sản phẩm cùng họ tên; chế độ Ask và Agent được cụ thể hóa ở [Bài thực hành 01](chapters/chapter-02.md#muc-2-1).

### 1.3. Phía sau một câu trả lời: prompt, context và token (Behind the Scene)

Lan từng yêu cầu "Làm app ví sinh viên chuyên nghiệp" và nhận về đề xuất thêm đăng nhập, máy chủ, đồng bộ thanh toán, sai hẳn phạm vi bài tập. Minh viết "sửa vòng lặp này" nhưng quên dán mã. Mục này giải thích vì sao hai câu hỏi đó thất bại, và một câu trả lời được tạo ra từ gì.

#### Ý chính 1 — Prompt là lời giao việc, context là thông tin thực sự được nhận

**Prompt** là yêu cầu hoặc chỉ dẫn đưa cho hệ thống. **Context** (ngữ cảnh) của một lượt là toàn bộ thông tin hệ thống thực sự nhận được: prompt, phần lịch sử được chọn, tài liệu, mã nguồn và kết quả của công cụ. Prompt là một phần của context. Một tài liệu đang mở trên màn hình chưa chắc đã nằm trong context của model.

Một prompt đủ dữ kiện có năm thành phần:

1. **Mục tiêu trước triệu chứng.** "Cộng tất cả khoản hợp lệ" cho biết 42000 có phải kết quả sai hay không; riêng câu "ra 42000" thì chưa đủ.
2. **Phần mã nhỏ nhưng liên quan.** Với lỗi cận vòng lặp, cần khai báo dữ liệu, kiểu của biến tổng và vòng lặp.
3. **Kết quả mong đợi cạnh hiện tượng quan sát.** Ba khoản phải cho 60000, chương trình cho 42000; nếu chưa chạy, ghi rõ đó là dự đoán.
4. **Ràng buộc và mức trợ giúp.** Số tiền là số nguyên VND, tối đa 500 khoản, cần gợi ý trước.
5. **Cách kiểm tra.** Đề nghị nêu test và bằng chứng, thay vì yêu cầu "chắc chắn 100%".

Câu "Hãy đóng vai chuyên gia hàng đầu" không thay thế được mã nguồn và kết quả mong đợi. Ràng buộc quan trọng nhất của ViSinhVien là **hợp đồng dữ liệu**: mỗi khoản có `amount` là số nguyên, lớn hơn 0 và không quá 1000000000; tối đa 500 khoản; danh sách rỗng hợp lệ, tổng bằng 0. Tổng lớn nhất 500 × 1000000000 = 500000000000 VND vượt xa miền của kiểu số nguyên 32 bit (khoảng 2,1 tỷ), nên bản C++ dùng `long long`. Trong JavaScript, kiểu `Number` biểu diễn chính xác các số nguyên tới 9007199254740991, nên tổng này vẫn chính xác; nhưng chuỗi `"7000"` không phải số 7000, và ô nhập trên trang Web trả về chuỗi. Sửa cận vòng lặp không tự giải quyết việc xác thực dữ liệu. Minh và Lan giữ một bản brief chung ghi hợp đồng này và chỉ thay dòng "việc lần này" ở mỗi lượt.

#### Ý chính 2 — Token, context window và ba hoạt động không thay thế nhau

**Token** là đơn vị dữ liệu mà hệ thống xử lý. Một từ có thể được tách thành nhiều token; dấu câu, mã nguồn, ngôn ngữ và bộ tách token (*tokenizer*) đều ảnh hưởng tới số lượng. Không có quy tắc "một từ tiếng Việt bằng một token", nên đếm từ không cho biết số token; quy token thành chi phí là việc của Chương 5.

![Năm lát cắt giả định minh họa token, không phải tokenizer thật. Cửa sổ hữu hạn có chỉ dẫn, dữ liệu, hội thoại và phần dành cho đầu ra; nội dung ngoài cửa sổ không tự được nhớ.](assets/token-context.svg)

**Context window** (cửa sổ ngữ cảnh) là giới hạn lượng thông tin được xử lý trong một lần, do từng dịch vụ quy định. Cửa sổ lớn không bảo đảm mọi chi tiết đều được dùng chính xác. Lan từng dán toàn bộ lịch sử trao đổi, gồm cả yêu cầu backend đã bị loại; bản brief hiện hành bị chìm giữa thông tin hết hiệu lực. Một hội thoại dài còn có thể bị ứng dụng cắt bớt hoặc tóm tắt, nên "đã nói từ đầu" không bảo đảm thông tin còn trong context. Cách làm phù hợp: giữ brief hiện hành, hàm liên quan, dữ liệu giả và ghi chú phần đã thay đổi.

Ba hoạt động sau thường bị gộp làm một. **Huấn luyện** (*training*) là điều chỉnh tham số của model bằng dữ liệu; **suy luận** (*inference*) là dùng model đã có để tạo đầu ra từ đầu vào; **tìm kiếm web** (*web search*) là truy xuất thông tin qua công cụ nối Internet, nếu sản phẩm có và lượt đó thực sự dùng. Khi Minh gửi ba khoản chi, hệ thống dùng chúng trong context của lượt đó; điều này không chứng minh model vừa được huấn luyện lại, nhưng cũng không đồng nghĩa "không lưu dữ liệu", vì lịch sử chat và log là chuyện riêng của từng sản phẩm. Một câu hỏi về thông tin thay đổi theo ngày không tự kích hoạt tìm kiếm web.

**Hallucination**, thường gọi là ảo giác AI, là hiện tượng nội dung sai hoặc không có căn cứ được trình bày như thể đúng: "JavaScript tự lưu mọi biến vào localStorage", hay lời "đã chạy test" trong khi hệ thống chỉ đọc văn bản. Cách ứng phó không phải yêu cầu "đừng sai", mà chuyển sự tự tin thành câu hỏi kiểm chứng. Minh hỏi: những chỉ số nào được duyệt, ca một khoản cho kết quả gì, câu nào chỉ là dự đoán. Nếu công cụ khẳng định đã chạy, cần có lệnh, dữ liệu, đầu ra và môi trường thực thi. Với trích dẫn: **khoanh vùng nhận định → mở nguồn → tìm đoạn hỗ trợ → kiểm tra phạm vi và ngày → ghi giới hạn**; không tìm được căn cứ thì ghi "chưa xác minh". Giờ hãy chấm lại ba thẻ ở đầu chương theo ba câu: kết luận có đúng không, cách giúp có đúng yêu cầu không, có bằng chứng đi kèm không.

#### Thử ngay (10 phút)

Mục tiêu: viết lại câu "sửa vòng lặp này" của Minh thành một prompt đủ năm thành phần, và chọn đúng context.

1. Trong năm thứ sau, chọn những gì sẽ gửi kèm: bản brief, hàm tính tổng, ba khoản giả, một bản sao kê ngân hàng thật, một bài giảng không liên quan. Ghi lý do loại từng phần bị loại.
2. Viết prompt không quá tám dòng theo khung:

```text
MỤC TIÊU: …
MÃ LIÊN QUAN: (dán phần nhỏ nhất đủ hiểu)
KỲ VỌNG: … · QUAN SÁT: … (ghi rõ nếu chưa chạy)
RÀNG BUỘC: … · MỨC TRỢ GIÚP: …
CÁCH KIỂM TRA: …
```

Ghi lại: danh sách context đã chọn và prompt hoàn chỉnh.

#### Gợi ý đối chiếu

Context đủ để kiểm tra nhưng không lộ dữ liệu: có brief, hàm và ba khoản giả; không có sao kê thật, không có tài liệu gây nhiễu. Prompt phải nêu 60000 cạnh 42000, nói rõ tổng là số nguyên VND, xin gợi ý một bước và yêu cầu test. Prompt chỉ có "sửa giúp" và lời tôn xưng vẫn thiếu dữ kiện dù dài.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Ứng dụng đang dùng có cho biết lượt vừa rồi dùng bao nhiêu token và có dùng tìm kiếm web hay không? Nếu không, kết luận nào về "AI đã biết gì" là chưa có căn cứ?
- **Từ khóa tra cứu:** tokenizer, context window, inference, hallucination, retrieval.
- **Trong Sổ tay thực hành:** [Mục 1.3](chapters/chapter-01.md#muc-1-3) có bản brief đầy đủ của ViSinhVien, bảng sáu ca kiểm tra theo hợp đồng dữ liệu và lời giải bài chọn context; chi phí tính từ token ở [Mục 5.1](chapters/chapter-05.md#muc-5-1).

### Tóm tắt chương

- AI hợp lý khi đóng vai gia sư giải thích, người phản biện hoặc trợ lý cho việc lặp; giao cho AI phần kiểm tra được nhanh, giữ lại phần hiểu biết và trách nhiệm.
- Dùng để học khác dùng để né học ở chỗ ai đã suy nghĩ: **AI hỗ trợ, người học quyết định.**
- Một lượt dùng AI có model, provider, application, producer và user; thiếu bằng chứng thì ghi "chưa xác định".
- API và key là đường truy cập, không phải bộ não tải về; cùng câu hỏi không đồng nghĩa cùng đầu vào.
- Prompt là lời giao việc, context là thông tin thực nhận; token và context window hữu hạn.
- Sự tự tin của câu trả lời không phải bằng chứng; hãy chuyển nó thành câu hỏi kiểm chứng.

**Ba câu để tự kiểm.** Nhãn "tích hợp Claude" đã đủ để xác định provider và phiên bản model chưa? Danh sách rỗng có vi phạm điều kiện `amount > 0` không, và có cần tạo một khoản bằng 0 để biểu diễn nó không? Đếm số từ tiếng Việt có đủ để biết số token của một prompt không?

### Cầu nối sang chương sau

Hiểu vai trò, giới hạn và cách AI hoạt động mới là bước đầu; điều còn lại là biến hiểu biết đó thành thao tác. Chương 2 · Điều khiển quá trình làm việc với AI hướng dẫn giao việc rõ, kiểm bằng bằng chứng và nhận thay đổi có chủ đích, bắt đầu từ chính khoản 18000 bị bỏ sót.

### Tài liệu tham khảo

Thông tin về model, đường truy cập và API cần tra lại tại thời điểm áp dụng; nguồn về giá và ưu đãi sinh viên ở Chương 5.

- [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview): họ model và định danh phiên bản.
- [AWS — Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/): ví dụ producer và provider khác nhau.
- [Google — Gemini API docs](https://ai.google.dev/gemini-api/docs): API, xác thực và cách chỉ định model.
- [Google — Gemini overview](https://gemini.google/overview/): lớp ứng dụng mang tên Gemini.

---

## CHƯƠNG 2 · ĐIỀU KHIỂN QUÁ TRÌNH LÀM VIỆC VỚI AI

Chương 1 đã làm rõ vai trò của AI trong học tập và cho thấy một câu trả lời được tạo ra từ prompt, context và token, nên không thể chấp nhận nó chỉ vì được trình bày tự tin. Chương 2 là bước **Dùng** trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn: dùng AI như một công cụ có kiểm soát. Ba câu hỏi xuyên suốt là việc gì cần làm, công cụ được phép làm đến đâu, và bằng chứng nào đủ để chấp nhận kết quả. Minh, Lan, các hội thoại và ba khoản chi trong chương là *tình huống hư cấu* với *dữ liệu giả định*; kết quả chạy chương trình nêu trong chương là *kết quả mong đợi* suy ra từ mã.

**Sau chương này, người học có thể:**

- Mở đúng thư mục làm việc, biết shell đang dùng và hỏi AI ở chế độ chỉ đọc trước khi cho phép sửa.
- Lập bảng trace để chỉ ra lượt lặp bị bỏ sót và giải thích vì sao tổng là 42000 thay vì 60000.
- Lần theo một giá trị từ ô nhập trên Web đến hàm tính tổng và nơi lưu; phân biệt chuỗi, số, `undefined` và `NaN`.
- Giao việc cho Agent trong phạm vi hẹp, đọc diff trước khi chấp nhận và nghiệm thu bằng bằng chứng thay vì bằng lời hứa.

### Tình huống mở đầu

Chương trình C++ của Minh in ra **42000**, trong khi ba khoản chi Cơm trưa 35000, Xe buýt 7000 và Vở ghi 18000 cộng trên giấy được **60000**. Lan có bản Web của cùng ứng dụng ViSinhVien với tổng đúng, nhưng khi thử nhập `35000abc`, Lan cần biết chương trình từ chối giá trị này ở đâu. Cùng lúc, một trợ lý AI đề nghị cài thêm thư viện để "xử lý tiền chuyên nghiệp". Ba việc này cần ba mức quyền và ba loại bằng chứng khác nhau.

Hợp đồng dữ liệu chung cho cả hai nhánh: mỗi khoản là số nguyên từ 1 đến 1000000000, tối đa 500 khoản, danh sách rỗng có tổng 0. Người học chọn một nhánh (C++ của Minh hoặc Web của Lan) để làm sâu, nhưng vẫn cần giải thích được lỗi trọng tâm của nhánh còn lại. Không nhập thông tin sinh viên thật hay bất kỳ bí mật nào vào mã nguồn hoặc hội thoại với AI.

### 2.1. Chuẩn bị môi trường và hỏi trước khi cho phép sửa

Mục này giúp người học biết đang đứng ở đâu, dùng công cụ nào, rồi đặt một câu hỏi mà AI chỉ được đọc và giải thích. Hai việc nhỏ ấy ngăn phần lớn lỗi "sửa nhầm tệp" trước khi chúng kịp xảy ra.

#### Ý chính

Minh gọi chung vùng soạn mã, khung hội thoại và cửa sổ lệnh là "AI". Cần tách chúng ra. **Editor** là nơi soạn tệp. **IDE** gom editor, cây tệp, tìm kiếm và terminal vào một cửa sổ. **Terminal** chỉ hiển thị văn bản; **shell** (Bash hoặc PowerShell) là chương trình diễn giải lệnh chạy bên trong terminal; **CLI** là chương trình được gọi, như `g++` hoặc `node`. **Agent** là AI được gắn công cụ: nó có thể đọc, sửa tệp và chạy lệnh tùy theo sản phẩm, chế độ và quyền được cấp. Khi gõ `g++ --version` mà shell báo không tìm thấy lệnh, vấn đề nằm ở môi trường, chưa phải ở vòng lặp C++. Việc đã cài IDE cũng không chứng minh máy đã có compiler.

![Khung IDE chứa cây tệp, editor và terminal. Trong terminal, shell nhận python --version và gọi CLI Python. AI hoặc Agent ở ngoài ranh giới quyền đọc, sửa, chạy lệnh.](assets/workspace.svg)

Hai thứ cần đọc được ngay là **thư mục hiện hành** (current working directory, viết tắt cwd) và **tên shell**. Trong chương, cwd luôn là thư mục gốc `AI-Student-Handbook`; bài làm nằm trong `bai-lam/`, còn `vi-du/` chỉ để đối chiếu, không sửa. Bash xem cwd bằng `pwd`, PowerShell bằng `Get-Location`. Cùng một máy Windows có thể mở cả hai shell, nên hệ điều hành không quyết định cú pháp; shell đang mở mới quyết định. Terminal mở từ trước có thể đang đứng ở nơi khác thư mục IDE đang mở, vì vậy cần kiểm tra vị trí trước khi chạy bất kỳ lệnh nào.

Khi đã biết vị trí, hãy hỏi trước khi cho phép sửa. Trong Qoder IDE, chế độ **Ask** đọc hiểu và gợi ý đoạn mã nhưng không tự sửa tệp; chế độ **Agent** mới được sửa và chạy lệnh theo quyền. Dùng `@` để đưa đúng tệp cần đọc vào ngữ cảnh: Minh bắt đầu với `loi-bo-sot.cpp`, Lan với `app.js` và `data.js`. Ngữ cảnh nhỏ không có nghĩa là cắt bỏ khai báo kiểu hay dữ liệu đầu vào. Một câu hỏi tốt tách bốn thành phần: đầu vào, điều mong muốn, điều quan sát được và đoạn mã liên quan. Câu "quan sát thấy 42000 với ba khoản" là dữ kiện; câu "chắc chắn compiler cộng sai" là một giả thuyết yếu. Chưa chạy chương trình thì ghi "dự đoán từ mã" thay cho "quan sát".

Câu trả lời của AI chỉ là đề xuất cho tới khi người học mở lại từng vị trí nó dẫn ra. Lan hỏi về luồng submit của bản Web; nếu AI bịa ra hàm `handleSubmit`, cần sửa mô tả thành "handler vô danh gắn vào sự kiện submit", không sửa mã cho khớp với câu trả lời. Một đoạn mã xuất hiện trong hội thoại cũng chưa có nghĩa là tệp đã thay đổi. Prompt không thay cho hàng rào quyền: chế độ, cấu hình và bước phê duyệt mới quyết định công cụ được phép làm gì. Chế độ chỉ đọc cũng không biện minh cho việc đưa dữ liệu nhạy cảm vào ngữ cảnh; chương chỉ dùng ba khoản chi giả định. Nếu giao diện khác với mô tả, cần kiểm tra sản phẩm và phiên bản thay vì chọn một chế độ có quyền rộng hơn.

#### Thử ngay (10 phút)

Mục tiêu: có thư mục bài làm và một câu hỏi chỉ đọc. Việc cụ thể: tạo `bai-lam/` với hai thư mục con `nam-1-cpp` và `nam-2-web`; sao chép **nội dung** một nhánh từ `vi-du/` sang (tránh tầng lồng `nam-1-cpp/nam-1-cpp`); tạo `ghi-chep-02.txt` trong nhánh đang học. Mở terminal, ghi vào tệp đó tên shell và cwd. Sau cùng viết một câu hỏi cho AI theo bốn thành phần ở trên, mở đầu bằng "Chỉ giải thích, chưa sửa, chưa chạy lệnh". Chưa cần gửi; chỉ cần viết ra.

#### Gợi ý đối chiếu

Cây thư mục có đúng ba tầng `AI-Student-Handbook/bai-lam/nam-1-cpp`? Tệp ghi chép nêu tên shell, cwd và không mang đuôi `.txt.txt`? Câu hỏi có đủ đầu vào, điều mong muốn, điều quan sát (hoặc dự đoán) và đoạn mã, và nói rõ AI chưa được sửa gì?

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Giải thích toán tử `+=` và tìm hàm mà `app.js` gọi trong `data.js` có cần cùng một mức quyền không? Nếu AI chỉ đọc `data.js` rồi kết luận "nút Thêm đã gắn đúng sự kiện", kết luận đó đã đủ bằng chứng chưa?
- **Từ khóa tra cứu:** current working directory, shell và terminal, Ask mode, read-only prompt.
- **Trong Sổ tay thực hành:** [Bài thực hành 01](chapters/chapter-02.md#muc-2-1) có bảng lệnh Bash và PowerShell, cấu trúc thư mục đầy đủ và prompt mẫu; [Bài thực hành 02](chapters/chapter-02.md#muc-2-2) có hai prompt chỉ đọc cho nhánh C++ và Web cùng đáp án câu hỏi kiểm tra.

### 2.2. Gỡ lỗi bằng bảng trace: khoản 18000 bị bỏ sót

Mục này giúp người học tự tìm nguyên nhân của con số 42000 bằng cách đóng vai máy tính trên giấy, rồi mới nhờ AI kiểm lại. Hãy dùng mô phỏng trace ngay dưới tiêu đề này để xem từng lượt lặp trước khi đọc tiếp; mỗi lượt trong mô phỏng tương ứng với một dòng của bảng ở phần "Thử ngay".

#### Ý chính

Demo lỗi `loi-bo-sot.cpp` duyệt danh sách với điều kiện `i < n - 1`. Với ba khoản, `n = 3`, điều kiện trở thành `i < 2`: lượt `i = 0` cộng 35000, lượt `i = 1` cộng 7000 thành 42000, lượt `i = 2` kiểm tra `2 < 2` cho kết quả sai nên vòng lặp dừng, và khoản Vở ghi 18000 không bao giờ được cộng. Lượt dừng ấy chính là bằng chứng: nếu chỉ ghi các lượt có điều kiện đúng, người học dễ bỏ qua đúng điểm gây lỗi.

**Trace** là bảng ghi lại giá trị các biến sau từng lượt lặp, do người học suy luận thủ công; nó không phải nhật ký do máy ghi. Bảng trace làm được cả khi chưa có compiler, khi đó gắn nhãn "trace thủ công". Chưa quen thì bắt đầu với danh sách một phần tử, vì bảng chỉ có vài dòng. Hàm đúng trong bản mẫu có dạng dưới đây, đã lược phần kiểm tra dữ liệu để tập trung vào phép duyệt:

```cpp
long long totalExpenses(const std::vector<long long>& amounts) {
    int n = static_cast<int>(amounts.size());
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        total += amounts[i];
    }
    return total;
}
```

Vì sao `long long`? Kiểu dữ liệu giống kích cỡ chiếc hộp đựng số. Mỗi khoản tối đa 1000000000 và danh sách tối đa 500 khoản, nên tổng có thể lên tới 500000000000; kiểu `int` 32 bit không đủ chứa, vì vậy cả phần tử lẫn biến tổng đều dùng `long long`. Tham số `const std::vector<long long>&` nhận danh sách theo tham chiếu để không sao chép, còn `const` ngăn hàm sửa danh sách. `size()` trả về số không dấu; chuyển sang `int n` ở đây chấp nhận được vì số lượng đã bị chặn ở 500, nhưng không nên máy móc đổi điều kiện thành `i < amounts.size() - 1`, vì với danh sách rỗng phép trừ không dấu tràn vòng thành một số rất lớn.

![Trace n=3, total=0, cận i<n-1: i=0 cộng 35000; i=1 cộng 7000 thành 42000; i=2 không thỏa 2<2, bỏ 18000. Kỳ vọng 60000; sửa cận i<n, validation là bước riêng.](assets/debugging.svg)

Bản vá đúng là `i < n`, không phải `i <= n` (truy cập chỉ số `n` nằm ngoài vector là hành vi không xác định) và cũng không phải cộng bù `amounts[n - 1]` sau vòng lặp (che nguyên nhân, lại hỏng với danh sách rỗng). Ca danh sách rỗng trả 0 ở cả hai phiên bản nên không phân biệt được chúng; ca một khoản `[7000]` thì có: bản sai trả 0, bản đúng trả 7000. Sửa cận xong, tổng ra 60000 nhưng validation vẫn chưa có: `-1` vừa với `long long` mà không phải khoản chi hợp lệ. Đó là một trách nhiệm riêng, không tự xuất hiện khi đổi cận. Khi có compiler, nhớ rằng thông báo lỗi đầu tiên mới là nơi cần đọc, và sau mỗi lần sửa phải lưu tệp rồi biên dịch lại: nếu lần build thất bại mà executable cũ vẫn còn, chạy tệp đó có thể in 60000 dù mã vừa sửa chưa hợp lệ.

#### Thử ngay (10 phút)

Mục tiêu: tự tạo bằng chứng trước khi hỏi AI. Trên giấy hoặc trong `ghi-chep-02.txt`, kẻ bảng bốn cột: `i`, điều kiện, khoản được cộng, tổng sau bước. Điền ba lượt cho `n = 3` với điều kiện lỗi `i < n - 1`, kể cả lượt làm vòng lặp dừng. Sau đó lập thêm hai bảng ngắn cho danh sách rỗng và danh sách chỉ có `7000`. Ghi lại ca nào phân biệt được bản sai với bản đúng. Nếu muốn, dán bảng vào một câu hỏi chỉ đọc để AI kiểm tra bảng, không phải để AI lập hộ.

#### Gợi ý đối chiếu

Bảng ba khoản có đúng một lượt với điều kiện sai làm dừng vòng lặp? Tổng sau lượt cuối được cộng là 42000? Bảng rỗng cho 0 ở cả hai phiên bản, còn bảng `[7000]` cho hai kết quả khác nhau? Bản vá đề xuất chỉ đổi phần cận trong điều kiện, không thêm phép cộng bù?

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu khai báo `long long& alias = total;` rồi thực hiện `alias += 35000`, biến `total` có thay đổi không, và một bản sao `copied` thì sao? Khi compiler báo `expected ',' or ';' before 'for'` và chỉ vào dòng `for`, nguyên nhân thật nằm ở đâu?
- **Từ khóa tra cứu:** off-by-one error, unsigned wraparound, undefined behavior, reference và copy.
- **Trong Sổ tay thực hành:** [Bài thực hành 03](chapters/chapter-02.md#muc-2-3) có bảng trace đầy đủ cho cả hai phiên bản, bài trace tham chiếu, cách đọc lỗi thiếu dấu chấm phẩy và hướng dẫn tách validation.

### 2.3. Lần theo dữ liệu trên Web: chuỗi trông giống số chưa phải số

Mục này giúp người học theo dõi một giá trị từ ô nhập đến nơi lưu trên bản Web của Lan, để nhận ra chỗ dữ liệu đổi kiểu hoặc bị từ chối. Bản Web đang chạy đúng; bài học ở đây là hiểu cơ chế, không phải tìm chỗ hỏng.

#### Ý chính

Khi chưa có dữ liệu lưu, trang nạp sẵn ba khoản mẫu với tổng 60000, nên không nhập trùng ba khoản này rồi coi tổng 120000 là lỗi. Mỗi khoản là một đối tượng `Expense` bốn trường `id`, `title`, `amount`, `category`; số tiền là số, không đặt trong dấu nháy. Giá trị đi qua các chặng: ô nhập `amount` trong `index.html` → handler vô danh gắn vào sự kiện `submit` trong `app.js` → `D.parseAmount` → tạo khoản mới và `normalizeExpenses` → `totalExpenses` trong `data.js` → `render()` và `save()`. Minh tham gia với vai trò review chéo bài của Lan.

Chặng đầu tiên là nơi nhiều người nhầm: `input.value` luôn trả về **chuỗi**, kể cả với ô `type="number"`; demo dùng `type="text"` với `inputmode="numeric"`, thuộc tính này chỉ gợi ý bàn phím, không kiểm tra dữ liệu. Nối `'35000' + '7000'` cho `350007000`, không phải 42000. `parseInt('35000abc', 10)` trả về 35000 vì chỉ đọc phần đầu chuỗi. `parseAmount` vì thế yêu cầu toàn bộ chuỗi sau `trim()` khớp `/^[0-9]+$/`, rồi mới gọi `Number`, kiểm tra `Number.isSafeInteger` và miền từ 1 đến 1000000000. Nhập `35000abc` qua form phải thấy thông báo từ chối, còn tổng và số khoản giữ nguyên.

Chặng thứ hai dễ nhầm là tên trường. Đoạn dưới đây cố ý ánh xạ sai trường; nó chạy riêng trong Console của trình duyệt (phím F12), không phải trong terminal, và không thêm khoản nào vào ứng dụng:

```javascript
{
  const items = [{ amount: 35000 }, { amount: 7000 }, { amount: 18000 }];
  const wrong = items.reduce((sum, x) => sum + x.value, 0);
  console.log(wrong);
  console.log(Number.isNaN(wrong));
  const correct = items.reduce((sum, x) => sum + x.amount, 0);
  console.log(correct);
}
```

Truy cập một thuộc tính không tồn tại cho `undefined`; cộng số với `undefined` cho `NaN` (Not-a-Number). Hai giá trị này khác nhau: `undefined` nghĩa là "không có gì ở đó", `NaN` nghĩa là "kết quả không phải số". `typeof NaN` vẫn là `"number"`, nên cần `Number.isNaN` để nhận diện. Ba biểu hiện 42000, 350007000 và NaN gợi ba giả thuyết khác nhau: bỏ sót phần tử, nối chuỗi, và cộng một giá trị không dùng được như số; màn hình chưa đủ để chẩn đoán, cần xem đầu vào, kiểu và mã.

Mỗi hàm có một trách nhiệm. `totalExpenses` chỉ kiểm tra đầu vào là mảng, có tối đa 500 phần tử và từng `amount` hợp lệ; `normalizeExpenses` mới kiểm tra schema đủ bốn trường và trả về danh sách mới đã chuẩn hóa. Bộ `test_data.cjs` chạy qua Node.js trong terminal: nó kiểm logic của `data.js`, không mở trình duyệt, nên không chứng minh gì về handler, DOM hay lưu trữ.

Chặng cuối là lưu. `app.js` đọc khóa `visinhvien-demo-v1` trong `localStorage`; nếu đọc hoặc ghi thất bại (bị chặn khi mở qua `file://`, hết dung lượng), ứng dụng chuyển sang giữ dữ liệu trong RAM và hiển thị cảnh báo. Mở được trang không có nghĩa là lưu bền vững: tải lại trang có thể mất thay đổi, và dữ liệu không đồng bộ giữa các máy hay gắn với tài khoản nào.

#### Thử ngay (10 phút)

Mục tiêu: dự đoán rồi mới chạy. Trước khi mở Console, viết ra ba dòng dự đoán cho đoạn mã trên: giá trị `wrong`, kết quả `Number.isNaN(wrong)` và giá trị `correct`. Sau đó mở `index.html` trong trình duyệt, ghi lại tổng ban đầu, dán đoạn mã vào Console và so với dự đoán. Tiếp theo, trên form, nhập tên giả hợp lệ, chọn nhóm, số tiền `35000abc` và gửi; ghi lại thông báo, tổng và số khoản sau thao tác. Không có trình duyệt thì chỉ làm phần dự đoán và ghi "chưa chạy".

#### Gợi ý đối chiếu

Dự đoán nêu đúng hai giá trị `undefined` và `NaN` ở đúng chỗ, không coi chúng là một? Tổng sau khi gửi `35000abc` bằng tổng trước thao tác? Phần ghi chép tách rõ "kiểm hàm trực tiếp trong Console" với "kiểm qua form", vì đó là hai bằng chứng khác nhau?

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nút Khôi phục mẫu có bật lại khả năng lưu khi `persistent` đã là false không? Vì sao `category: ['khac']` từng lọt qua một cách kiểm tra, và ca kiểm thử nào giữ cho lỗi ấy không quay lại?
- **Từ khóa tra cứu:** input.value string, NaN và undefined, Number.isSafeInteger, localStorage file://.
- **Trong Sổ tay thực hành:** [Bài thực hành 04](chapters/chapter-02.md#muc-2-4) có bảng luồng dữ liệu bảy chặng, hai đoạn Console dùng API thật của trang, giải thích ca hồi quy category mảng và cơ chế dự phòng khi lưu.

### 2.4. Giao việc có giới hạn, đọc diff và nghiệm thu

Mục này giúp người học chuyển từ "hỏi" sang "giao việc" mà không mất quyền kiểm soát: viết hợp đồng giao việc, đọc từng dòng thay đổi trước khi chấp nhận, và kết luận đúng phạm vi đã kiểm tra.

#### Ý chính

Một lượt làm việc có kiểm soát đi qua năm bước **Observe → Plan → Act → Test → Review**: quan sát mã, dữ liệu và lỗi; nêu giả thuyết, tệp dự kiến đổi và phép thử; thực hiện thay đổi đã được phép; kiểm bằng ca thường và ca biên; rồi rà soát diff và bằng chứng để quyết định nhận hay từ chối. Với tình huống 42000: Observe đọc vector và `i < n - 1`; Plan dự đoán ca rỗng, một khoản, ba khoản; Act đổi thành `i < n` đúng tệp bài làm; Test biên dịch rồi chạy đúng executable; Review so yêu cầu, diff và kết quả. Chỉ chuyển từ Ask sang Agent khi đã mô tả được lỗi, biết tệp nào sẽ đổi và đã có dự đoán. Test sai thì quay lại Observe với dữ kiện mới, không đổi mã ngẫu nhiên cho tới khi màn hình báo đạt.

![Ask sang Analyze, Edit, Test, Review. Test sai quay lại Analyze; đổi yêu cầu hoặc phát hiện thiếu sau review quay lại Ask.](assets/workflow.svg)

Hợp đồng giao việc nêu rõ tệp duy nhất được sửa, mục tiêu hẹp, điểm dừng ("chỉ Observe và Plan; chưa sửa") và những việc cấm: không cài dependency, không đổi cấu hình hay quyền, không chạm `vi-du`. Khi Agent đề nghị cài một gói "xử lý tiền chuyên nghiệp", câu hỏi của Lan là đúng: API hiện có thiếu ở điểm nào? Bản Web thuần chỉ dùng API trình duyệt, bộ test dùng `node:assert/strict` có sẵn trong Node.js; không bài nào cần `npm install`. Chưa kiểm tra tên gói, nhà phát hành, kho mã, phiên bản và giấy phép thì ghi "dependency chưa xác minh"; không cài thử để xem, cũng không gọi gói là độc hại chỉ vì lạ.

**Diff** là danh sách dòng bị bỏ và dòng được thêm giữa hai trạng thái của tệp. Trước khi sửa, tạo checkpoint bằng cách sao chép tệp bài làm vào `bai-lam/checkpoints/moc-01-truoc-can/`; đó là đường quay lại. Mỗi diff đọc theo bốn câu hỏi: tệp nào thay đổi, dòng nào thay đổi, thay đổi liên quan đến lỗi ra sao, và hợp đồng dữ liệu có bị ảnh hưởng không. Một diff sửa đúng cận nhưng đồng thời xóa phép kiểm `category` và bật tự chạy lệnh thì tổng 60000 vẫn đúng mà hành vi đã yếu đi. Chấp nhận (accept) chỉ là nhận thay đổi, không phải chứng nhận đúng; nhật ký giữ cả lượt thất bại, vì chính lượt thất bại sinh ra ca kiểm thử hồi quy.

Nghiệm thu dựa trên ba loại bằng chứng. Thứ nhất là **lệnh**: build với `g++`, chạy đúng executable, đọc stdout, stderr và exit code ngay sau lệnh; compiler lỗi thì dừng, vì executable cũ vẫn có thể in 60000. Thứ hai là **ca biên**: Sổ tay có ba bảng C1–C9 cho C++, W1–W10 cho `parseAmount` và T1–T8 cho `totalExpenses`, cùng bộ `test_data.cjs` với kết quả mong đợi 34 passed, 0 failed; bảng và cách đọc kết quả được trình bày ở [Bài thực hành 07](chapters/chapter-02.md#muc-2-7). Thứ ba là **lời giải thích**: test của bản đúng đạt không chứng minh tệp lỗi vừa sửa đã chạy; test Node.js đạt không chứng minh `localStorage` lưu được. Báo cáo một phút gồm bốn ý: lỗi, chỗ sửa, bằng chứng, phần chưa kiểm.

#### Thử ngay (10 phút)

Mục tiêu: viết hợp đồng giao việc và đọc một diff. Viết sáu dòng vào `ghi-chep-02.txt`: tệp duy nhất được sửa; mục tiêu (ba khoản ra 60000); điểm dừng trước Act; ba việc cấm; bằng chứng yêu cầu sau khi sửa; câu "nếu bị chặn thì dừng và báo". Sau đó tạo checkpoint, tự sửa `i < n - 1` thành `i < n` trong bài làm (nếu chưa sửa ở mục 2.2) và so hai tệp theo bốn câu hỏi. Ghi phần đã chạy thật và phần chưa chạy.

#### Gợi ý đối chiếu

Hợp đồng có tên tệp cụ thể, có điểm dừng và có câu từ chối dependency? Diff chỉ đổi một dòng trong đúng tệp bài làm, còn `vi-du` không thay đổi? Phần "chưa kiểm" có ghi rõ validation chưa làm và các ca C7–C9 chưa thể đạt với bản vá cận?

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nên nhận bản vá cùng với thay đổi Auto-Run và dependency, hay tách riêng từng việc? Khi `test_data.cjs` báo đạt, kết luận nào được phép và kết luận nào chưa?
- **Từ khóa tra cứu:** diff, checkpoint, regression test, exit code, dependency review.
- **Trong Sổ tay thực hành:** [Bài thực hành 05](chapters/chapter-02.md#muc-2-5) có hợp đồng giao việc mẫu và cách kiểm dependency; [Bài thực hành 06](chapters/chapter-02.md#muc-2-6) có diff minh họa và mẫu nhật ký mười dòng; [Bài thực hành 07](chapters/chapter-02.md#muc-2-7) có lệnh build cho Bash và PowerShell, ba bảng ca biên, bốn bước nghiệm thu trên trình duyệt và bảng tự đánh giá.

### Tóm tắt chương

- Biết cwd, shell và công cụ thật có trên máy trước khi giao việc; hỏi ở chế độ chỉ đọc trước khi cho phép sửa.
- Lỗi 42000 nằm ở cận `i < n - 1`; ca một khoản phân biệt được bản sai và bản đúng, ca rỗng thì không; validation là trách nhiệm riêng.
- Giá trị từ ô nhập là chuỗi; `parseAmount` kiểm cú pháp và miền, `normalizeExpenses` kiểm schema; `undefined` không phải `NaN`; lưu cục bộ có thể rơi vào dự phòng trong RAM.
- Agent chỉ làm trong phạm vi được giao; đọc diff theo bốn câu hỏi; checkpoint và nhật ký giữ cả lượt thất bại.
- Mỗi kết luận gắn với một phép kiểm cụ thể: test nào, chạy trên mã nào, phần nào chưa kiểm.
- Ba nguyên tắc mang sang các chương sau: chưa chạy thì nói chưa chạy; không có quyền thì dừng; không có lý do thì không mở rộng hệ thống.

**Ba câu để tự kiểm**

1. Danh sách rỗng trả về 0 có chứng minh vòng lặp đúng không?
2. Khi thiếu `x.value`, tổng là `undefined` hay `NaN`, và vì sao hai giá trị này khác nhau?
3. Khi AI báo "đã sửa", cần những gì trước khi nộp bài?

### Cầu nối sang chương sau

Chương này đã cho thấy cách dùng AI có kiểm soát: giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. Nhưng một công cụ chạy tốt rất dễ khiến người dùng ngừng tự nghĩ. Chương 3 bàn cách tận dụng AI mà không lạm dụng, để mỗi lần dùng đều giúp người học hiểu thêm.

### Tài liệu tham khảo

Thông tin về sản phẩm Qoder được đối chiếu với tài liệu chính thức tại mốc 30/10/2026; giao diện và quyền có thể thay đổi theo phiên bản.

- [Qoder IDE: Ask](https://docs.qoder.com/user-guide/chat/ask.md) và [Agent](https://docs.qoder.com/user-guide/chat/agent.md): hai chế độ chat và cách review thay đổi.
- [Qoder IDE: Terminal](https://docs.qoder.com/user-guide/editor/terminal.md): mở terminal và chính sách chạy lệnh của IDE.
- [MDN: parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) và [Number.isSafeInteger](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger): đọc một phần chuỗi và miền số nguyên an toàn.
- [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage): giới hạn lưu trữ khi mở trang qua `file://`.
- Mã ví dụ kèm sách, chỉ để đọc và đối chiếu: [`loi-bo-sot.cpp`](vi-du/nam-1-cpp/loi-bo-sot.cpp), [`vi_sinh_vien.cpp`](vi-du/nam-1-cpp/vi_sinh_vien.cpp), [`data.js`](vi-du/nam-2-web/data.js), [`test_data.cjs`](vi-du/nam-2-web/test_data.cjs).

---

## CHƯƠNG 3 · HỌC CHỦ ĐỘNG: DÙNG AI MÀ KHÔNG LẠM DỤNG

Chương 2 đã trình bày cách làm việc có kiểm soát với AI: chuẩn bị môi trường, giao việc có giới hạn, đọc diff và nghiệm thu bằng kiểm thử. Nhưng một chương trình chạy đúng sau khi được AI hỗ trợ chưa chứng minh người học đã nắm kiến thức mà bài tập nhắm tới. Chương này là bước **Giữ vững** trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn: tận dụng AI mà phần học vẫn ở lại với người học. Nhân vật, hội thoại và số liệu trong chương là *Tình huống hư cấu* và *Dữ liệu giả định*; quyền dùng AI trong bài nộp do từng học phần quy định.

"Lạm dụng" ở đây không có nghĩa dùng AI là xấu. Lạm dụng là giao cho AI đúng phần việc đang cần luyện, chẳng hạn nhờ AI viết vòng lặp trong chính bài học về vòng lặp.

**Sau chương này, người học có thể:**

- Nhận ra kết luận vượt quá bằng chứng trong một câu trả lời tự tin của AI và tìm một phản ví dụ nhỏ để kiểm tra.
- Ghi dự đoán về đầu vào, kỳ vọng và giả thuyết trước khi hỏi AI hoặc chạy chương trình.
- Lần ngược luồng dữ liệu của một ứng dụng nhỏ và giải thích lại bằng lời của chính người học.
- Tự quan sát khả năng nhớ lại, hoàn thành một nhiệm vụ nhỏ không dùng AI và viết kết luận đúng mức bằng chứng.

### Tình huống mở đầu

Sau Chương 2, Minh (năm nhất, học C++) đã sửa cận vòng lặp và chương trình in đúng tổng **60000** cho ba khoản 35000, 7000 và 18000. Khi Lan hỏi kết quả sẽ thế nào nếu danh sách chỉ có một khoản, Minh chưa trả lời được nếu không hỏi lại AI. Lan (năm hai, học Web) gặp điều tương tự: giao diện đã hoạt động, nhưng Lan chưa giải thích được vì sao giá trị đọc từ ô nhập phải qua hai bước chuyển kiểu và kiểm tra. Cả hai đặt một mục tiêu chung cho chương này: **tự giải thích được ít nhất một điều khi không còn nhìn lời giải**. Câu hỏi đặt ra là dùng AI thế nào để mục tiêu đó vẫn đạt được.

### 3.1. Bẫy câu trả lời tự tin (AI Trap)

Mục này giúp người học đánh giá một câu trả lời tự tin của AI bằng căn cứ thay vì bằng cảm giác. Câu hỏi cần đặt ra cho mỗi câu trả lời: "Kết luận này đã được chứng minh cho những đầu vào nào?"

#### Ý chính

Một câu trả lời tự tin thường trộn lẫn phần đã chứng minh với phần chỉ suy đoán. Giả sử AI nói với Minh: "Đã đổi cận vòng lặp và thấy 60000, vậy chương trình xử lý mọi đầu vào an toàn." Vế đầu là bằng chứng thật: với ba khoản mẫu, bản sửa in 60000. Vế sau vượt quá bằng chứng: một ca đúng chưa nói gì về danh sách rỗng, khoản âm hay danh sách 501 khoản.

Cách kiểm tra rẻ nhất là một **phản ví dụ nhỏ**: đầu vào ngắn nhất làm cho kết luận sai. Với cận lỗi `i < n - 1`, danh sách chỉ có một khoản 7000 cho `n = 1`; lần kiểm tra đầu tiên là `0 < 0`, sai ngay, vòng lặp không chạy lượt nào và tổng là 0 trong khi kỳ vọng là 7000. Một dòng tính tay đủ bác bỏ chữ "mọi" trong câu trả lời. Ngược lại, danh sách rỗng cho 0 với cả cận đúng lẫn cận sai, nên riêng ca rỗng không phân biệt được hai cận. Chọn phản ví dụ cũng là một việc cần suy nghĩ.

![Lời AI giả lập sai: mảng rỗng ra 0 nên vòng lặp đúng. Phản ví dụ [7000] với i=0, n=1, cận i<n-1 làm 0<0 sai: thực tế 0, kỳ vọng 7000.](assets/ai-trap.svg)

Để có chỗ bám, cả hai nhánh dùng chung một **hợp đồng dữ liệu**: tiền là số nguyên VND từ 1 đến 1000000000, danh sách tối đa 500 khoản, danh sách rỗng hợp lệ và có tổng 0. Mỗi khoản ở nhánh Web có bốn trường `id`, `title`, `amount`, `category`. Hợp đồng là điều AI không được tự ý đổi cho tiện viết mã. Nếu AI nói "ở Web cứ dùng `Number` cho mọi giá trị là đủ", hợp đồng cho ngay một phản ví dụ: `Number("")` trả về 0, chuyển kiểu được nhưng không phải khoản hợp lệ.

Bẫy cũng xuất hiện khi dựng nhanh bằng cách mô tả mong muốn rồi nhận mã do AI sinh ra qua nhiều lượt trao đổi (vibe coding). Cách làm này hữu ích để thử ý tưởng, nhưng chương trình chạy được không chứng minh người làm hiểu chương trình. Phiên bản có kiểm soát đi chậm hơn: biết vai trò từng tệp, chọn một vấn đề, dự đoán, nhận một thay đổi, kiểm vài ca rồi mới đi tiếp. Người học được phép tra cứu tên API; điều không được bỏ qua là trả lời bốn câu về mỗi đoạn mã: nhận dữ liệu gì, trả về gì, dựa vào điều kiện nào của hợp đồng, và bỏ điều kiện nào thì tạo được ca sai.

#### Thử ngay (10 phút)

Mục tiêu: tìm phản ví dụ cho ba kết luận. Chép ba câu sau vào vở (viết sai có chủ đích): (1) "Đổi cận và thấy 60000, vậy mọi đầu vào đều an toàn." (2) "Ở Web cứ dùng `Number` cho mọi giá trị là đủ." (3) "Muốn tổng theo nhóm thì lọc theo `category` trước, khoản thuộc nhóm khác không liên quan." Với mỗi câu, ghi một đầu vào cụ thể cần thử và kết quả dự đoán bằng tay. Chưa viết lại hàm, chưa mở AI. Ghi lại câu nào khó tìm phản ví dụ nhất.

#### Gợi ý đối chiếu

Mỗi phản ví dụ phải là một đầu vào cụ thể (giá trị, kiểu, số lượng), không phải nhận xét chung "AI có thể sai". Với câu (1), ca một khoản hoặc khoản âm là dấu hiệu đúng hướng. Với câu (2), nghĩ tới chuỗi rỗng hoặc số âm. Với câu (3), nghĩ tới một khoản ở nhóm khác có tiền sai kiểu: lọc trước sẽ che mất khoản đó.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Vì sao ca rỗng không phân biệt được hai cận nhưng ca một khoản thì được? Với bài đang học, phần nào là "phần đang cần luyện" mà AI không nên làm thay?
- **Từ khóa tra cứu:** counterexample, edge case, data contract, vibe coding.
- **Trong Sổ tay thực hành:** [3.1. Bẫy câu trả lời tự tin](chapters/chapter-03.md#muc-3-1) — hợp đồng dữ liệu đầy đủ, bảng sáu tình huống phân biệt tận dụng với giao việc học cho AI, phần đối chiếu ba kết luận.

### 3.2. Dự đoán trước khi hỏi (Think First)

Mục này giúp người học hỏi AI hiệu quả hơn bằng cách có sẵn điểm bám: một dự đoán được viết ra trước. Hỏi khi chưa có lời giải là bình thường; hỏi khi chưa có dự đoán mới là điều cần tránh.

#### Ý chính

Một gợi ý của AI chỉ phát huy tác dụng khi có chỗ để bám vào. Trước khi gửi câu hỏi, Minh ghi ba dòng: đầu vào (`35000, 7000, 18000`, số nguyên), kỳ vọng (60000, vì cộng đủ ba khoản) và giả thuyết (có thể chưa cộng khoản Vở ghi; chưa chạy). Có ba dòng đó, câu hỏi gửi đi hẹp lại thành "một câu về chỉ số" thay vì "sửa giúp cả bài". Nếu chưa biết kỳ vọng, hãy tính tay ca một khoản trước.

Đoạn mã lỗi có chủ đích trong `loi-bo-sot.cpp`, với `amounts` là `std::vector<long long>{35000, 7000, 18000}` và `total` khởi tạo bằng 0:

```cpp
int n = static_cast<int>(amounts.size());
for (int i = 0; i < n - 1; ++i) { // CỐ Ý SAI
    total += amounts[i];
}
```

Giá trị của bài không nằm ở việc đoán ra `i < n`, mà ở việc Minh tự đi qua từng lượt: `n = 3`, lượt đầu kiểm tra `0 < 2`, tổng 35000; lượt hai `1 < 2`, tổng 42000; lượt ba `2 < 2` sai, vòng lặp dừng khi chưa đọc 18000. Phép cộng không sai; chỉ thiếu một số hạng. Lưu ý `size()` trả về số lượng phần tử, không phải chỉ số cuối. Nếu dùng AI đóng vai người hỏi, cần yêu cầu AI chờ câu trả lời và mỗi lượt chỉ hỏi một câu.

Thói quen này được gói thành **phiên học 25 phút có AI hỗ trợ**, khác với thử thách không dùng AI ở mục 3.4:

1. 0–4 phút: tự thử, phác thảo một cách làm dù còn thiếu.
2. 4–7 phút: dự đoán, tính tay, ghi kỳ vọng trước khi chạy và trước khi hỏi.
3. 7–11 phút: xin gợi ý, mỗi lượt một câu, tự trả lời rồi mới hỏi tiếp.
4. 11–16 phút: tự sửa, chỉ sửa nguyên nhân đã giải thích được.
5. 16–21 phút: kiểm chứng bằng ca thường, ca biên và ca sai.
6. 21–25 phút: đóng chat, làm một biến thể không AI.

Mỗi nút thắt được xin tối đa ba lượt gợi ý; mỗi lượt phải dẫn tới một hành động tự làm. Nếu AI viết luôn điều kiện đúng, ghi "đã xem lời giải phần cận", đóng lại, tự giải thích rồi thử một ca mới; phần đã lộ chỉ được tính là ôn tập. Nếu mệt hoặc hết giờ, ghi cụ thể trạng thái ("đã biết chỉ số cuối, chưa biết lập điều kiện") rồi dừng. Thời lượng làm bài không đo năng lực theo đuổi ngành học.

#### Thử ngay (10 phút)

Mục tiêu: viết phiếu dự đoán và trace bằng tay, chưa chạy, chưa hỏi. Dùng mẫu ba dòng sau cho danh sách chỉ có một khoản 18000:

```text
Đầu vào: ...
Kỳ vọng: ...
Giả thuyết (chưa chạy): ...
```

Sau đó, với đoạn mã lỗi ở trên, lập bảng ba cột: lần kiểm tra, giá trị `i` và điều kiện, `total` sau lượt. Làm cho cả ca một khoản và ca ba khoản mẫu. Ghi lại lượt kiểm tra nào làm vòng lặp dừng sớm.

#### Gợi ý đối chiếu

Phiếu đúng hướng khi kỳ vọng được ghi trước khi nhìn mã chạy, và giả thuyết nêu nơi nghi ngờ chứ chưa khẳng định nguyên nhân. Bảng trace đúng hướng khi có cả lần kiểm tra thất bại (lượt mà điều kiện sai) chứ không chỉ các lượt được cộng. Ca một khoản phải cho thấy vòng lặp không chạy lượt nào với cận lỗi.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Vì sao không nên thay cận bằng `size() - 1` dù trông gọn hơn? Khi đã nhớ lời giải, làm sao biết lần này là hiểu hay chỉ là nhớ?
- **Từ khóa tra cứu:** predict-run-investigate, off-by-one error, Socratic prompting.
- **Trong Sổ tay thực hành:** [3.2. Dự đoán trước khi hỏi](chapters/chapter-03.md#muc-3-2) — phiếu dự đoán năm dòng, hội thoại C++ đầy đủ với bảng trace và bảng kỳ vọng hai cận, bảng dấu vết của phiên 25 phút; [2.3. Gỡ lỗi C++](chapters/chapter-02.md#muc-2-3) — kiểu kích thước không dấu và việc build.

### 3.3. Lần ngược luồng dữ liệu và giải thích lại (Reverse Engineering, Explain It Back)

Mục này giúp người học kiểm tra bản thân có thật sự hiểu chương trình hay chỉ thấy chương trình chạy. Hai bước đi liền nhau: đọc ngược từ kết quả về nơi dữ liệu được tạo ra, rồi trình bày lại bằng lời của chính người học.

#### Ý chính

**Lần ngược** (tiếng Anh: *reverse engineering*) là đọc chương trình từ con số trên màn hình về nơi dữ liệu được tạo. Trong `bai-lam/nam-2-web`, Lan bắt đầu từ tổng hiển thị, lần về hàm `render()`, lời gọi `D.totalExpenses(expenses)`, chỗ gán `expenses`, handler `submit` và `D.parseAmount` trong `app.js`; rồi mở `data.js` để đọc các hàm và `index.html` để xem form. Ở mỗi chặng, điều cần ghi là **kiểu dữ liệu**: `.value` của ô nhập là chuỗi kể cả khi người dùng gõ chữ số; `parseAmount` kiểm tra cách viết rồi mới chuyển thành số; `normalizeExpenses` kiểm tra cả danh sách, gồm `id`, `title`, `amount` và `category`, trước khi gán; `JSON.stringify` tạo chuỗi để ghi vào `localStorage`, và khi đọc lại, JSON hợp lệ chưa chắc đúng schema. Cần mô tả đúng mã hiện có: không bịa ra một hàm tên `handleSubmit` khi mã dùng callback vô danh.

Để thấy vì sao kiểu quan trọng, Lan làm một lab nhỏ trên giấy, không sửa `data.js` đang đúng: ba giá trị `amount` là các chuỗi `"35000"`, `"7000"`, `"18000"`; `total` ban đầu là số 0; mỗi lượt thực hiện `total = total + expense.amount`. Ngay lượt đầu, số 0 cộng chuỗi `"35000"` cho chuỗi `"035000"`; từ đó chương trình không còn cộng số mà nối ký tự. Kết luận của Lan: sửa ở biên nhập liệu (kiểm tra chuỗi, chuyển thành số, kiểm tra giá trị, rồi mới tạo Expense), và hàm tổng vẫn phải từ chối tiền sai vì dữ liệu có thể đến từ đường khác.

**Giải thích lại** (tiếng Anh: *explain it back*) là bước vượt qua câu "em hiểu rồi". Đóng tài liệu, trong khoảng một phút, trình bày đường đi của `"18000"` từ ô nhập đến giá trị số trong danh sách rồi đến chuỗi JSON, chỉ vào tên hàm ở mỗi chặng. Chặng nào bị kẹt chính là nội dung cần ôn tiếp. Minh tham gia với vai trò review chéo cho Lan, không chuyển sang làm dự án Web.

![Vòng sáu bước hai hàng: dự đoán, nhận gợi ý, tự sửa, chạy test, giải thích, biến thể; biến thể quay về dự đoán. AI chỉ hỗ trợ ở bước gợi ý.](assets/active-learning.svg)

#### Thử ngay (10 phút)

Mục tiêu: trace giá trị và kiểu, rồi giải thích lại. Trên giấy, lập bảng bốn cột cho lab ba chuỗi ở trên: lượt, `total` trước và kiểu, `amount` và kiểu, `total` sau và kiểu. Giữ nguyên dấu ngoặc kép khi ghi chuỗi. Sau đó gập bảng lại và nói thành lời, trong một phút, vì sao kết quả không phải 60000 và nên sửa ở chặng nào. Ghi lại chặng đầu tiên bị kẹt.

#### Gợi ý đối chiếu

Bảng đúng hướng khi cột kiểu đổi từ number sang string ngay lượt đầu và không đổi lại nữa. Lời giải thích đúng hướng khi nêu được tên hàm hoặc vị trí cho từng chặng (ô nhập, phân tích tiền, kiểm tra danh sách, lưu) thay vì chỉ nói "phải chuyển sang số". Nếu chỉ đề xuất đổi toán tử cộng mà chưa nói tới kiểu của `.value`, chặng đầu còn thiếu.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Khi tải lại trang, dữ liệu đã lưu trong `localStorage` có cần kiểm tra lại không, và vì sao parse thành công chưa đủ? Chỉ dùng `Number` thì chuỗi rỗng và số âm sẽ đi đâu?
- **Từ khóa tra cứu:** typeof, type coercion, input validation, Feynman technique.
- **Trong Sổ tay thực hành:** [3.3. Lần ngược luồng dữ liệu và giải thích lại](chapters/chapter-03.md#muc-3-3) — bảng bảy chặng, hội thoại Web đầy đủ, hành vi lưu trữ và origin, bảng tám mẫu prompt P01–P08; [3.6. Bài vận dụng](chapters/chapter-03.md#muc-3-6) — tái dựng phần lõi trong lab, bảng kiểm thử với kỳ vọng ghi trước và biến thể tổng theo `category`; [Thư viện prompt mẫu](chapters/prompt-library.md).

### 3.4. Tự quan sát trí nhớ và thử thách không dùng AI (Memory Experiment, No-AI Challenge)

Mục này giúp người học biết bản thân còn nhớ gì sau khi học và tự làm được đến đâu khi không có AI. Hai hoạt động không dùng để chấm điểm; chúng tạo bằng chứng để chọn việc luyện tiếp.

#### Ý chính

**Tự quan sát trí nhớ** (Memory Experiment) gồm hai nhiệm vụ gần tương đương, không cần AI, khoảng 12–15 phút. Nhiệm vụ A: với `35000, 7000, 18000`, đọc lời giải về cận `i < n` và dãy tổng `0 → 35000 → 42000 → 60000` trong 90 giây rồi gấp lại. Nhiệm vụ B: với `18000, 35000, 7000`, tự viết bảng chỉ số và tổng trong 90 giây, không mở lời giải. Sau mỗi nhiệm vụ, che ghi chép, nghỉ hai phút bằng một việc không liên quan, rồi trả lời bốn câu trên giấy trắng: các chỉ số hợp lệ là gì; tổng sau mỗi lượt là bao nhiêu; điều kiện nào làm vòng lặp dừng; danh sách một khoản và danh sách rỗng cho kết quả ra sao và vì sao. Chỉ sau khi trả lời xong mới đối chiếu.

Điều quan trọng nhất là **kết luận đúng mức bằng chứng**. Một nhận xét phù hợp có dạng: "Ở nhiệm vụ A, nhớ tổng cuối nhưng quên lượt dừng; ở nhiệm vụ B, tự viết được ba tổng trung gian; sẽ luyện điều kiện dừng khi đóng tài liệu." Không được suy ra "AI làm trí nhớ kém đi": không có nhóm so sánh, còn thứ tự làm, độ mệt và việc đã nhìn đáp án đều ảnh hưởng. Kết quả chỉ dùng để chọn hành động học tiếp theo.

**Thử thách 25 phút không dùng AI** (No-AI Challenge) là phiên làm việc độc lập từ đầu đến cuối: đóng hội thoại, không dùng Agent, công cụ sinh mã hay gợi ý. Nhiệm vụ chung: đếm số khoản có tiền **từ 10000 VND trở lên**, với đầu vào đã được xác nhận hợp lệ theo hợp đồng. Minh viết `countLargeAmounts(const std::vector<long long>& amounts)` trả về `int`; Lan viết `countLargeExpenses(expenses)` dùng `expense.amount` ở kiểu số, không đọc DOM hay `localStorage`. Không đổi nhiệm vụ thành tính tổng. Các ca cần chuẩn bị: ba khoản mẫu, danh sách rỗng, một khoản 10000, một khoản 9999, ba khoản mẫu đảo thứ tự. Phân bổ thời gian: 5 phút tính kỳ vọng, 7 phút viết thuật toán bằng lời rồi viết mã hoặc giả mã, 6 phút trace hoặc chạy, 4 phút tự tìm một điểm sai, 3 phút đóng mã và trình bày lại. Chưa xong trong 25 phút là bình thường; điểm nghẽn ghi lại chính là nội dung cần luyện tiếp. Nếu vô tình thấy gợi ý, ghi lại thời điểm và không gọi cả phiên là độc lập.

#### Thử ngay (10 phút)

Mục tiêu: làm phiên thu nhỏ của nhiệm vụ B. Lấy giấy và đồng hồ. Trong 90 giây, với `18000, 35000, 7000` và cận `i < n`, tự viết bảng chỉ số và tổng sau mỗi lượt, không mở lời giải. Che bảng, nghỉ hai phút bằng một việc khác. Sau đó trả lời bốn câu hỏi ở trên trên giấy trắng. Cuối cùng, mở bảng và ghi ba điều: ý tự nhớ được, ý sai hoặc cần mở lại, có giải thích được ca một khoản hay không.

#### Gợi ý đối chiếu

Đúng hướng khi dãy tổng trung gian của nhiệm vụ B khác nhiệm vụ A nhưng tổng cuối giống nhau, và khi câu trả lời về lượt dừng nêu được lần kiểm tra điều kiện thất bại. Kết luận ghi lại phải là một việc cụ thể cho phiên sau, không phải nhãn "nhớ tốt" hay "nhớ kém".

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Trong bài đếm, vì sao biến đếm kiểu `int` là đủ trong khi tổng tiền phải dùng `long long`? Bốn tiêu chí nào giúp tự đối chiếu một phiên không AI mà không nhìn vào tốc độ?
- **Từ khóa tra cứu:** retrieval practice, testing effect, deliberate practice.
- **Trong Sổ tay thực hành:** [3.4. Tự quan sát khả năng nhớ lại](chapters/chapter-03.md#muc-3-4) — bảng ghi nhận, lượt hôm sau và phần đối chiếu; [3.5. Thử thách 25 phút không dùng AI](chapters/chapter-03.md#muc-3-5) — quy tắc đầy đủ, bảng phân bổ thời gian, bốn tiêu chí đối chiếu và lời giải để đọc sau phiên.

### 3.5. Tự đánh giá cuối chương (Skill Unlocked)

Mục này giúp người học nhìn lại đã làm được gì và chọn việc luyện tiếp. Kết quả là ghi nhận tại thời điểm hiện tại, không phải nhãn năng lực lâu dài.

#### Ý chính

Với mỗi năng lực, chọn một trong ba mức: **tự làm** (đã đóng chat và không nhìn đáp án), **cần gợi ý**, hoặc **chưa làm**, kèm bằng chứng. Ba nhóm năng lực của chương: *giải thích* (nêu hợp đồng dữ liệu; trace đến 60000 và chỉ ra vì sao cận lỗi dừng ở 42000; phân biệt `35000` với `"35000"`), *sửa* (chỉ thay phần gây lỗi, tách bản vá cận khỏi validation; tự chọn ca một khoản, ca rỗng, ca biên, ca dữ liệu sai) và *vận dụng* (làm hàm max hoặc tổng theo nhóm mà không che khoản sai ngoài nhóm; nêu rõ phần đã nhận hỗ trợ, phần tự làm và phần còn cần hỏi). Chọn một dòng chưa làm được, thu nhỏ ví dụ rồi thử lại.

Các mục trong chương ghép thành một chu trình học chủ động: chọn mục tiêu và đọc hợp đồng → tự thử và dự đoán trước khi hỏi hoặc chạy → xin một gợi ý, tự trả lời, tự sửa một điểm → kiểm chứng bằng test → nếu chưa đúng, ghi điểm nghẽn, thu nhỏ và thử lại; nếu đúng, làm biến thể không AI và ghi chỗ chưa chắc → chọn việc tiếp theo. Cuối mỗi phiên chỉ cần ghi ba dòng: học được, chưa chắc, việc tiếp. Phải gọi tên hành động hoặc kiến thức cụ thể; một ghi chép như "học được nhiều" không giúp phiên sau biết bắt đầu từ đâu.

#### Thử ngay (10 phút)

Mục tiêu: viết phiếu ba dòng cho phiên học gần nhất. Phiếu minh họa (hư cấu, không phải kết quả của một sinh viên thật):

```text
Học được: Cận cũ không cho i = 2 đi vào thân vòng lặp.
Chưa chắc: Tôi chưa tự giải thích hết kiểm tra dữ liệu đọc từ JSON.
Việc tiếp: Tự trace ca một khoản và một ca sai ngoài nhóm, chưa mở AI.
```

Viết phiếu của riêng người học. Sau đó chọn một năng lực ở trên đang ở mức "chưa làm" và ghi ví dụ thu nhỏ sẽ thử ở phiên sau.

#### Gợi ý đối chiếu

Mỗi dòng của phiếu phải chỉ vào một hành động hoặc một kiến thức kiểm tra được (một ca, một điều kiện, một hàm). Dòng "việc tiếp" nên làm được trong một phiên ngắn mà không cần mở AI.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Bộ test đạt hết đã chứng minh người học hiểu bài chưa? Điều gì còn thiếu?
- **Từ khóa tra cứu:** self-assessment, metacognition, learning log.
- **Trong Sổ tay thực hành:** [3.7. Tự đánh giá năng lực cuối chương](chapters/chapter-03.md#muc-3-7) — bảng tám năng lực, tám câu vấn đáp và phần đối chiếu; [3.6. Bài vận dụng](chapters/chapter-03.md#muc-3-6) — bài sửa lỗi hoàn chỉnh với validation, bảng kiểm thử và hai biến thể max, tổng theo nhóm, nơi mức "vận dụng" được kiểm tra đầy đủ.

### Tóm tắt chương

- Một câu trả lời tự tin cần được đánh giá bằng hợp đồng dữ liệu, phản ví dụ và phạm vi kiểm thử; đúng một ca chưa phải đúng mọi ca.
- Ranh giới giữa tận dụng và lạm dụng nằm ở nhiệm vụ đang luyện; trước khi hỏi, xác định phần người học phải tự chứng minh.
- Dự đoán trước khi hỏi hoặc chạy, trace từng lượt, mỗi lượt một câu hỏi: cách giữ quá trình suy nghĩ ở phía người học.
- Lần ngược luồng dữ liệu và giải thích lại bằng lời làm lộ ra chặng còn thiếu, như khác biệt giữa `35000` và `"35000"`.
- Tự quan sát trí nhớ và thử thách không AI chỉ dùng để chọn việc học tiếp, không dùng để kết luận nhân quả.

**Ba câu để tự kiểm:** Vì sao danh sách một khoản là phản ví dụ tốt hơn danh sách rỗng? Lượt đầu tiên của lab chuỗi đổi kiểu ở đâu? Phiếu ba dòng của phiên gần nhất có gọi tên được một ca cụ thể không?

### Cầu nối sang chương sau

Khi đã biết dùng AI mà vẫn học được, bước tiếp theo là biết ranh giới: dữ liệu nào không nên đưa vào AI, mã nào cần bảo mật, nguồn nào có bản quyền, cách giữ liêm chính khi nộp bài. Chương 4 trình bày các ranh giới đó: dùng có trách nhiệm là điều kiện để được tiếp tục dùng.

### Tài liệu tham khảo

- [MDN Web Docs — Window: localStorage property](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [MDN Web Docs — typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [MDN Web Docs — Number.isSafeInteger()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger)
- [cppreference.com — std::vector](https://en.cppreference.com/w/cpp/container/vector)
- Mã ví dụ đi kèm: [loi-bo-sot.cpp](vi-du/nam-1-cpp/loi-bo-sot.cpp), [data.js](vi-du/nam-2-web/data.js), [app.js](vi-du/nam-2-web/app.js).

---

## CHƯƠNG 4 · SỬ DỤNG AI CÓ TRÁCH NHIỆM

Chương 3 đã giúp người học giữ được việc học khi có AI hỗ trợ. Chương này đi tiếp một bước: khi sản phẩm đã chạy đúng, người làm ra nó có thật sự làm chủ nó không. Làm chủ là biết rõ công cụ và nguồn đang dùng, được phép dùng đến đâu, có bằng chứng cho điều đã khẳng định và biết xử lý khi có sai sót. Đây là bước "Có trách nhiệm" trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn.

Nhân vật và sự cố trong chương là *tình huống hư cấu*; chương không phải quy định của Trường, không phải tư vấn pháp lý.

**Sau chương này, người học có thể:**

- Xử lý đúng thứ tự khi khóa API bị lộ: thu hồi trước, dọn sau.
- Chọn dữ liệu giả đủ để tái hiện lỗi; nhận ra diff vượt phạm vi và gói thư viện chưa kiểm chứng.
- Phân biệt khai báo với sự cho phép; hiểu giới hạn của "kho công khai", MIT và GPL.
- Giải thích vì sao truy vấn tham số hóa, `textContent` và điều kiện `i < n` là đúng.

### Tình huống mở đầu

Bản Web của ViSinhVien đã hiển thị đúng tổng **60000**, và Minh định nộp ngay. Lan đề nghị trả lời ba câu hỏi trước: một dòng mã từ đâu ra, dữ liệu trong bài là của ai, nhóm đã kiểm tra những gì. Kết quả 60000 chỉ chứng minh phép cộng đúng với ba khoản 35000, 7000, 18000; nó không trả lời được ba câu hỏi đó. Bảy tình huống (4.1–4.7), ba lỗi kỹ thuật (4.8) và danh sách kiểm tra (4.9) lần lượt trả lời. Với mỗi tình huống, hãy chọn một phương án và ghi lý do rồi mới đọc Ý chính.

### 4.1. Tình huống 01 — Khóa API xuất hiện trên GitHub

Tình huống này giúp tránh sai lầm dễ gặp: tưởng xóa dòng chứa khóa là xong. ViSinhVien không cần API key, nhưng trong một bài khác, Minh đặt khóa của một dịch vụ AI trong tệp `config.js` rồi đẩy cả thư mục lên kho GitHub công khai để nhờ Lan xem. Sáng hôm sau, Lan phát hiện dòng `API_KEY = ...`. Minh nên làm gì **đầu tiên**: xóa dòng đó rồi commit lại; tạo khóa mới; thu hồi khóa ở nhà cung cấp; hay viết lại lịch sử Git và ép đẩy?

#### Ý chính

Xóa dòng trong tệp **không vô hiệu hóa khóa**: bản cũ vẫn nằm trong lịch sử Git, bản clone của người khác, bộ nhớ đệm hoặc đoạn chat từng dán, và khóa còn hiệu lực đến khi được thu hồi. Tạo khóa mới mà để khóa cũ hoạt động là chưa xong. Viết lại lịch sử kho ảnh hưởng mọi người đang dùng kho mà vẫn không xóa được bản clone; việc này do người quản lý kho quyết định.

![Sáu bước theo đúng thứ tự trong chương: 01 dừng chia sẻ thêm; 02 thu hồi key ở nhà cung cấp, ô lớn bên trái; 03 kiểm tra mức sử dụng; 04 rà bản liên quan; 05 báo đúng đầu mối; 06 giảm bản lưu và chặn tái diễn, không tự viết lại lịch sử kho mã. Nhãn KEY_DEMO_INVALID không phải key thật.](assets/security.svg)

Sáu bước đúng thứ tự: (1) dừng chia sẻ thêm; (2) thu hồi hoặc xoay vòng khóa, xác nhận trạng thái "đã thu hồi" trong trang quản lý, không gọi thử API bằng khóa cũ; khóa không thuộc tài khoản của Minh thì báo ngay người có quyền; (3) kiểm tra mức sử dụng; (4) rà bản liên quan: commit, tệp cấu hình, ảnh chụp, đoạn chat; (5) báo đúng đầu mối (giảng viên hoặc trưởng nhóm), **không đính kèm khóa**; (6) giảm bản còn lưu, dùng placeholder như `DEMO_KEY_NOT_A_SECRET`, thêm bước rà tệp trước khi đẩy. Nguyên tắc: **thu hồi trước, dọn sau; báo sự cố bằng mô tả, không bằng bí mật.**

#### Thử ngay (10 phút)

Hãy gập hình lại, viết từ trí nhớ sáu bước đúng thứ tự. Rồi viết thông báo sự cố năm dòng gửi giảng viên: thời điểm phát hiện, phạm vi đã chia sẻ, trạng thái khóa cũ, đã kiểm tra mức sử dụng chưa, điều cần hướng dẫn. Ghi vào `ghi-chep-04.txt` trong `bai-lam`.

#### Gợi ý đối chiếu

Thứ tự đúng hướng nếu "thu hồi" đứng trước mọi bước "dọn". Thông báo đạt nếu người đọc biết phải làm gì tiếp mà không cần thấy khóa.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Khóa thuộc tài khoản nơi thực tập: bước nào thay đổi, bước nào giữ nguyên?
- **Từ khóa tra cứu:** secret rotation, removing sensitive data from a repository.
- **Trong Sổ tay thực hành:** [Hồ sơ 01](chapters/chapter-04.md#muc-4-1): năm phương án, sáu bước chi tiết, mẫu thông báo.

### 4.2. Tình huống 02 — Dữ liệu cá nhân trong cửa sổ chat

Tình huống này giúp tránh đưa dữ liệu cá nhân vào cửa sổ chat khi không cần. Để nhờ AI tìm lỗi tính tổng, Minh định gửi ảnh chụp bảng chi tiêu thật trong tháng: có tên quán quen, giờ giao dịch, mã sinh viên và góc màn hình còn hiện email. Minh cho rằng đổi tên thành "Sinh viên A" là đủ. Minh nên gửi: ảnh nguyên bản; ảnh đã đổi tên; ảnh che bằng một lớp hình chữ nhật; hay ba khoản giả 35000, 7000, 18000 cùng hàm tính tổng?

#### Ý chính

Câu hỏi đầu tiên là **"lỗi này cần tối thiểu dữ liệu gì để tái hiện?"**. Lỗi bỏ sót khoản cuối tái hiện được bằng ba khoản giả: 42000 thay vì 60000. Dữ liệu tạo mới không liên hệ với ai, nên đó là phương án tốt nhất. Đổi tên chưa phải ẩn danh: mã sinh viên, giờ, quán quen và email vẫn đủ để người quen nhận ra. Lớp che trong tệp chỉnh sửa có thể bị gỡ. Giả định "dịch vụ không lưu" không có căn cứ khi chưa đọc điều khoản.

| Nhóm dữ liệu | Cách hiểu | Lựa chọn |
| --- | --- | --- |
| Giả | Tạo mới để thử, không phải hồ sơ thật sửa sơ qua | 35000, 7000, 18000; email giả `demo001@example.invalid` |
| Đã khử nhận dạng | Không còn xác định được một người, kể cả khi ghép dữ liệu khác | Không mặc định là ẩn danh sau khi bỏ tên |
| Cá nhân, bí mật | Gắn với một người, tài khoản hoặc quyền truy cập | Mã sinh viên, chi tiêu thật, mật khẩu, khóa API: không đưa vào ví dụ |

Về pháp luật, chương tham chiếu Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Luật số 131/2025/QH15 sửa đổi Luật Sở hữu trí tuệ (*Chưa kiểm chứng* sau mốc 29/10/2026; không phải ý kiến pháp lý). Nguyên tắc: **dữ liệu giả không phải dữ liệu thật đã đổi tên, mà là dữ liệu được tạo mới.**

#### Thử ngay (10 phút)

Hãy chụp màn hình bàn làm việc hiện tại (không gửi ai) và liệt kê mọi thứ trong ảnh có thể giúp nhận ra một người: tên tệp, tab, email, thông báo. Rồi viết bộ dữ liệu giả tối thiểu tái hiện lỗi bỏ sót khoản cuối: ba khoản và một dòng kết quả sai mong đợi. Xóa ảnh sau khi xong.

#### Gợi ý đối chiếu

Danh sách đúng hướng nếu có ít nhất một mục ngoài vùng bảng chi tiêu, chẳng hạn thanh tab. Bộ dữ liệu giả đạt nếu không trùng dữ liệu thật và vẫn cho ra 42000 khi hàm bỏ sót khoản cuối.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Dữ liệu đã công khai ở nơi khác có đương nhiên phù hợp để thu gom và gửi cho một dịch vụ AI không?
- **Từ khóa tra cứu:** synthetic data, de-identification, khử nhận dạng.
- **Trong Sổ tay thực hành:** [Hồ sơ 02](chapters/chapter-04.md#muc-4-2): bốn phương án, bảng phân loại, căn cứ pháp lý.

### 4.3. Tình huống 03 — Agent sửa và xóa ngoài phạm vi

Tình huống này giúp tránh nhận kết quả của Agent chỉ vì màn hình kiểm thử màu xanh. Lan giao cho Agent: "Sửa lỗi tổng tiền trong `bai-lam/nam-2-web`." Agent báo xong. Diff cho thấy hàm tính tổng đã sửa, nhưng `index.html` bị đổi giao diện, hai ca đang thất bại trong `test_data.cjs` bị xóa, và Agent đề nghị cài một gói định dạng mã. Kiểm thử toàn màu xanh. Lan nên: chấp nhận toàn bộ; quay về checkpoint rồi chỉ áp dụng lại phần sửa hàm tính tổng; yêu cầu Agent "khôi phục như cũ"; hay tự gõ lại hai ca theo trí nhớ? (Chi tiết hư cấu; tệp đi kèm vẫn đủ 34 ca.)

#### Ý chính

Bốn dấu hiệu vượt phạm vi: diff chạm tệp ngoài mục tiêu; số ca kiểm thử **giảm** đúng bằng số ca đang thất bại; có lệnh cài đặt không được yêu cầu; báo cáo "đã xong" không nêu ca nào bị xóa. Kiểm thử đạt vì ca khó đã biến mất là bằng chứng giả. Nhận toàn bộ thay đổi là nhận trách nhiệm cho cả phần chưa đọc.

Phương án đúng: dừng Agent, quay về checkpoint tạo trước khi giao việc, đọc và hiểu diff của riêng phần sửa hàm tính tổng, áp dụng lại đúng phần đó, chạy đầy đủ bộ kiểm thử gốc. Yêu cầu Agent "khôi phục như cũ" là giao quyền cho chính công cụ vừa vượt phạm vi mà không có bằng chứng.

Câu prompt "chỉ sửa tệp X" là **yêu cầu**, không phải hàng rào kỹ thuật; quyền thực tế nằm ở thiết lập công cụ. Nguyên tắc: **tạo checkpoint trước, đọc diff sau, nhận thay đổi từng phần.** Số ca kiểm thử phải giữ nguyên hoặc tăng; thấy giảm là dừng lại hỏi "ca nào đã biến mất, vì sao?".

#### Thử ngay (10 phút)

Hãy viết "hợp đồng giao việc" sáu dòng cho Agent trước khi sửa lỗi tổng tiền: phạm vi (tệp, hàm); không sửa tệp khác, không xóa ca test; không cài gói, không commit, không truy cập mạng; điều phải báo trước khi sửa; điều phải báo sau khi sửa; làm gì khi bị chặn hoặc cần quyền mới.

#### Gợi ý đối chiếu

Hợp đồng đạt nếu người khác đọc xong chỉ ra ngay việc xóa hai ca test và đề nghị cài gói vi phạm dòng nào. Chỉ có "sửa lỗi tổng tiền" mà không có dòng "không" là chưa đạt.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu Lan chưa tạo checkpoint, đường quay lại nào còn khả thi mà không phải tin vào lời Agent?
- **Từ khóa tra cứu:** agent permissions, checkpoint, diff review.
- **Trong Sổ tay thực hành:** [Hồ sơ 03](chapters/chapter-04.md#muc-4-3): bốn phương án, hợp đồng giao việc mẫu; [Bài thực hành 06](chapters/chapter-02.md#muc-2-6): checkpoint và diff.

### 4.4. Tình huống 04 — Gói thư viện do AI đề xuất

Tình huống này giúp tránh cài gói thư viện chỉ vì AI đề xuất với giọng chắc chắn. Minh hỏi AI cách định dạng số tiền cho dễ đọc. AI trả lời rất tự tin, đưa lệnh cài một gói có tên gần giống một thư viện quen thuộc, kèm câu "chạy lệnh này là xong". Minh chưa từng nghe tên gói này. Minh nên: chạy ngay; hỏi lại AI "gói này có an toàn không"; kiểm tra bài có cần thêm phụ thuộc không rồi đối chiếu trên registry chính thức; hay cài vào thư mục tạm "để thử"?

#### Ý chính

Câu hỏi đầu tiên luôn là **"bài có cần thêm phụ thuộc không?"**. Với ứng dụng HTML và JavaScript nhỏ, câu trả lời thường là không: API có sẵn của trình duyệt đã định dạng được số tiền.

Nếu thật sự cần, bằng chứng phải đến từ registry chính thức và kho nguồn. Hỏi lại AI là lập luận vòng tròn: cùng một nguồn vừa đề xuất vừa tự chứng nhận. Tên gần giống thư viện phổ biến nhưng khác vài ký tự là dấu hiệu *typosquatting*, đặt tên để đánh lừa người cài. Gói độc hại có thể chạy script ngay khi cài và đọc tệp cấu hình, khóa; cài "để thử" vẫn là chạy mã. Lockfile cố định phiên bản nhưng không biến gói độc hại thành đáng tin.

Bảng kiểm chứng gồm tám câu hỏi: tên gói trên registry, phiên bản, người duy trì, kho nguồn, giấy phép, script cài đặt, cảnh báo bảo mật, phụ thuộc bắc cầu. Không tự tạo URL để điền cho đủ; một ô trống trung thực có giá trị hơn dòng "đã kiểm" không căn cứ. Nguyên tắc: **không cài gói chỉ để tỏ ra chủ động.**

#### Thử ngay (10 phút)

Không cài gì. Hãy lập bảng kiểm chứng tám dòng cho một gói từng thấy ai đó cài. Mỗi dòng ghi **nơi** tìm bằng chứng, không ghi kết luận. Cuối bảng trả lời: bài ViSinhVien có cần gói này không, vì sao.

#### Gợi ý đối chiếu

Bảng đúng hướng nếu mọi "nơi tìm bằng chứng" đều là registry, kho nguồn hoặc trang tư vấn bảo mật, không dòng nào ghi "hỏi AI". Câu trả lời cuối đạt nếu nêu được cách định dạng tiền không cần phụ thuộc mới.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Gói đã nằm trong lockfile của dự án nhóm từ trước thì còn cần kiểm chứng không?
- **Từ khóa tra cứu:** typosquatting, software supply chain, lockfile.
- **Trong Sổ tay thực hành:** [Hồ sơ 04](chapters/chapter-04.md#muc-4-4): bốn phương án, bảng kiểm chứng đầy đủ.

### 4.5. Tình huống 05 — Bài tập hoàn toàn do AI làm

Tình huống này giúp tránh nhầm "được tham khảo" với "được để AI làm thay". Đề ViSinhVien ghi "Được tham khảo tài liệu", không nhắc AI. Minh dán toàn bộ đề vào chat, nhận về đầy đủ `index.html`, `data.js`, `app.js`, sửa vài chỗ, chương trình chạy được, và định khai báo "Có tham khảo ý tưởng từ AI". Minh nên: nộp với khai báo đó; hỏi giảng viên bằng tin nhắn mô tả đúng việc đã làm; xóa hết rồi viết lại theo trí nhớ; hay không khai báo vì "ai cũng dùng"?

#### Ý chính

"Tham khảo tài liệu" **không đồng nghĩa** với "được để AI viết hộ". Đề không nói rõ thì tình trạng là *chưa rõ*: hỏi giảng viên trước, không biến giả định thành sự cho phép, không coi im lặng là đồng ý. AI sinh toàn bộ hàm thì khai báo phải ghi đúng như vậy; "có tham khảo ý tưởng" là khai báo thấp hơn thực tế. **Khai báo không thay thế sự cho phép.** Cách đúng là hỏi phạm vi rồi tự làm lại phần cốt lõi trên cơ sở hiểu rõ. Minh không giải thích được vì sao bước kiểm tra `amount` đặt ở đó: dấu hiệu đã mất phần học.

| Tình trạng | Ví dụ | Việc cần làm |
| --- | --- | --- |
| Đã được cho phép | Đề cho dùng AI gợi ý ca kiểm thử | Dùng đúng phần được phép, lưu phần hỗ trợ |
| Đã bị cấm | Bài kiểm tra yêu cầu tự viết | Không nhờ AI tạo hay sửa mã khi làm bài |
| Chưa rõ | Đề cho tham khảo tài liệu, không nói về AI | Hỏi giảng viên trước |
| Có điều kiện | Được giải thích, không được sinh toàn bộ chức năng | Tách câu hỏi giải thích khỏi yêu cầu viết hộ |

Bảng không phải quy định của Trường; bảng giúp đặt câu hỏi đúng. Nguyên tắc: **khai báo là mô tả, không phải xin phép; hỏi phạm vi trước, khai báo sau, đúng việc đã làm.**

#### Thử ngay (10 phút)

Hãy viết tin nhắn hỏi giảng viên cho tình huống của Minh, tối đa năm dòng, ngôi "em": phần định tự làm; việc cụ thể muốn dùng AI; điều không định làm; câu hỏi "phạm vi này có được phép không"; hướng làm nếu không được.

#### Gợi ý đối chiếu

Tin nhắn đạt nếu giảng viên có thể trả lời "được" hoặc "không" mà không phải hỏi lại "em định dùng AI vào việc gì". Chỉ hỏi "em có được dùng AI không ạ" là chưa đủ cụ thể.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Giảng viên trả lời "được dùng AI để giải thích lỗi": hàm `parseAmount` do AI sinh nháp có thuộc phạm vi đó không?
- **Từ khóa tra cứu:** academic integrity, AI use policy.
- **Trong Sổ tay thực hành:** [Hồ sơ 05](chapters/chapter-04.md#muc-4-5): tin nhắn mẫu, bảng phân loại đầy đủ; [Thỏa thuận học tập](chapters/learning-agreement.md): phạm vi dùng AI, phần việc tự làm, bằng chứng cần có.

### 4.6. Tình huống 06 — Đoạn mã không rõ giấy phép

Tình huống này giúp tránh dùng mã của người khác khi chưa rõ quyền. Minh tìm thấy một giao diện đẹp trên GitHub. Vì kho mở được mà không cần đăng nhập, Minh định chép một tệp vào ViSinhVien. Kho **không có tệp LICENSE**. Minh nên: chép và ghi nguồn cuối bài; tự viết bảng khoản chi đơn giản mà Minh hiểu rõ; đổi tên biến và màu sắc để "không ai nhận ra"; hay nhờ AI viết lại giao diện từ ảnh chụp?

#### Ý chính

**Công khai không phải là giấy phép.** Kho mở được cho mọi người **không** tự động trao quyền sao chép, phân phối hay tạo tác phẩm phái sinh. Ghi nguồn là yêu cầu học thuật, không thay thế quyền sử dụng. Đổi tên biến hay màu sắc vẫn là sao chép. Nhờ AI "vẽ lại" từ ảnh cũng chưa chắc ổn: nhãn "do AI tạo" không chứng minh nguồn gốc. Phương án đúng trong bài này là tự viết bảng đơn giản mà nhóm hiểu rõ từng phần.

Đọc tên giấy phép cũng chưa đủ. MIT cho quyền dùng rộng nhưng phải giữ thông báo bản quyền và giấy phép khi sao chép. GPL **không** phải "cấm thương mại"; nghĩa vụ tùy phiên bản và cách kết hợp mã, chưa rõ thì hỏi người có chuyên môn. Kho không có giấy phép thì không có cơ sở coi là được tự do sao chép; mã do AI đưa ra cũng cần kiểm tra nguồn và điều khoản công cụ.

Theo Luật Sở hữu trí tuệ Việt Nam, chương trình máy tính được bảo hộ; "sao chép để học" không tự động là ngoại lệ (mốc đối chiếu ở mục 4.2). Điều này không cấm học từ tài liệu; nó nhắc kiểm tra quyền trước khi đưa mã vào bài nộp.

#### Thử ngay (10 phút)

Hãy điền "thẻ nguồn" bốn cột cho một thành phần từng định dùng lại: thành phần; nguồn và phiên bản (URL cụ thể, ngày xem); giấy phép và việc phải giữ; quyết định (dùng có điều kiện, hỏi thêm, không dùng). Cột không điền được thì ghi "chưa rõ" thay vì đoán.

#### Gợi ý đối chiếu

Thẻ đạt nếu cột "giấy phép" lấy từ tệp LICENSE thật, không từ trí nhớ hay câu trả lời của AI; và nếu cột đó là "chưa rõ" thì cột "quyết định" không thể là "dùng".

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Kho có LICENSE là MIT nhưng thư mục ảnh và phông chữ ghi điều kiện khác: phần nào được dùng theo MIT?
- **Từ khóa tra cứu:** MIT License, GPL, licensing a repository.
- **Trong Sổ tay thực hành:** [Hồ sơ 06](chapters/chapter-04.md#muc-4-6): bảng giấy phép đầy đủ, thẻ nguồn, tham chiếu điều luật.

### 4.7. Tình huống 07 — Khai báo thiếu và ba tầng trách nhiệm

Tình huống này giúp tránh khai báo chung chung và hiểu ai chịu trách nhiệm ở mỗi tầng. Bài nộp của nhóm ghi: "Có sử dụng AI để tham khảo." Thực tế, AI đã sinh nháp hàm `parseAmount` và gợi ý bảy ca kiểm thử; Lan chép một đoạn CSS từ kho không rõ giấy phép; Minh chỉ đọc mã, không chạy kiểm thử. Giảng viên hỏi "phần này em kiểm chứng thế nào?", cả hai không trả lời được. Nhóm nên: giữ câu khai báo và nộp kèm toàn bộ lịch sử chat; viết lại khai báo đúng việc đã làm, loại đoạn CSS; hay ghi "tự làm 100%"?

#### Ý chính

Khai báo tốt phân biệt rõ: AI gợi ý gì, sinh nội dung nào, nhóm thay đổi gì, đã kiểm chứng đến đâu. Đoạn CSS chưa rõ quyền phải **loại khỏi bài** và nêu rõ phần đã loại; ghi nguồn không biến nó thành mã được phép dùng. Mới đọc mã thì ghi "đã rà soát bằng đọc mã; chưa chạy kiểm thử", không ghi "đã xác minh". Gõ lại vài dòng không biến phần được sinh thành phần tự làm.

Mẫu khai báo, chỉ điền thông tin đúng thực tế:

```text
Bài/nhóm: [tên bài; thành viên và vai trò].
Phạm vi được phép: [theo đề hoặc phản hồi giảng viên; chưa rõ thì ghi đang chờ].
Công cụ và thời điểm: [tên, phiên bản nếu biết, ngày dùng].
Hỗ trợ thực tế: [giải thích, gợi ý hay sinh nháp phần nào; tệp, hàm liên quan].
Đóng góp của nhóm: [ai viết lại gì; giữ hoặc bỏ gì, vì sao].
Dữ liệu đã cung cấp: [dữ liệu giả, đoạn mã cần thiết; không dán bí mật].
Nguồn và giấy phép: [nguồn đã dùng, điều kiện phải giữ, phần đã loại].
Kiểm chứng: [đã chạy gì, trên bản nào, kết quả; phần chỉ đọc mã, chưa xác minh].
```

Khi AI viết sai, người nộp có chịu toàn bộ trách nhiệm không? Cần tách ba tầng: **học thuật** (bài đúng yêu cầu môn học; đóng góp và khai báo trung thực); **nghề nghiệp** (sản phẩm được rà soát đúng vai trò, nêu đúng giới hạn); **pháp lý** (dữ liệu, quyền tác giả, quyền truy cập do người có thẩm quyền xem xét). Không có câu "chịu 100% trách nhiệm" cho mọi trường hợp, cũng không đổ hết cho công cụ. Nguyên tắc: **khai báo tốt là bản đồ đóng góp, không phải lời xin lỗi hay lời tự khen.**

#### Thử ngay (10 phút)

Hãy điền mẫu trên cho một bài gần nhất có dùng AI. Ở dòng "Kiểm chứng", thay "đã test xong", "an toàn tuyệt đối" bằng câu kiểm chứng được: chạy gì, trên bản nào, bao nhiêu ca đạt, phần nào chưa thử.

#### Gợi ý đối chiếu

Khai báo đạt nếu mỗi dòng có một chi tiết cụ thể (tên hàm, số ca, ngày) và không dòng nào chỉ ghi "có tham khảo". Dòng "Kiểm chứng" đạt nếu người khác lặp lại được việc đã chạy và thấy phần còn bỏ trống.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Bài đã nộp rồi mới phát hiện khai báo thiếu: nhóm nên chủ động gửi gì cho giảng viên, và gửi gì thì không nên?
- **Từ khóa tra cứu:** AI disclosure statement, accountability.
- **Trong Sổ tay thực hành:** [Hồ sơ 07](chapters/chapter-04.md#muc-4-7): bảng ba tầng, mẫu khai báo bổ sung sau khi nộp, ví dụ điền mẫu.

### 4.8. Ba lỗi kỹ thuật ở ranh giới dữ liệu: SQL, XSS và C++

Ba lỗi trong mục này có chung một gốc: người viết mã không nắm rõ **hợp đồng ở ranh giới**, tức các điều kiện mà dữ liệu phải thỏa mãn khi đi qua một lớp của chương trình, và tin vào một lần chạy may mắn.

#### Ý chính

**SQL: giá trị là dữ liệu, không phải cấu trúc câu lệnh.** Ví dụ SQL chạy riêng bằng Python `sqlite3` với `:memory:` trong `vi-du/minh-hoa-sqlite.py`; ViSinhVien không có backend. Lan cần tìm khoản tên `Vở O'Reilly`. Khi nối chuỗi `"... WHERE title = '" + title + "'"`, dấu nháy rơi vào cú pháp SQL: câu lệnh sai, và nghiêm trọng hơn, dữ liệu có thể **làm thay đổi ý nghĩa câu lệnh**. Đó là gốc của lỗi chèn mã SQL (*SQL injection*). Cách đúng là truy vấn tham số hóa: `execute('SELECT title, amount FROM expenses WHERE title = ?', (title,))`; dấu `?` giữ chỗ cho giá trị gắn riêng, `(title,)` có dấu phẩy để tạo tuple một phần tử.

**XSS: hiển thị tên khoản chi dưới dạng văn bản.** Minh thử gán tên khoản chi bằng `innerHTML`. Lan kiểm tra bằng đầu vào vô hại `<b>Vở</b>`: nếu chữ Vở hiện in đậm, trình duyệt đang phân tích đầu vào như HTML, dù người dùng chỉ nhập một cái tên. Đây là gốc của lỗi chèn mã kịch bản liên trang (*Cross-Site Scripting*, XSS). Cách đúng cho ô bảng:

```javascript
const td = document.createElement('td');
td.textContent = expense.title;
```

*Kết quả mong đợi*: ô bảng hiện nguyên chuỗi `<b>Vở</b>`, gồm cả dấu ngoặc nhọn. Biện pháp này đúng cho vị trí nhận văn bản thông thường, không tự áp dụng cho URL, thuộc tính sự kiện hay CSS.

**C++: hai lỗi cận khác nhau.** Với `std::vector<long long>` chứa 35000, 7000, 18000, chỉ số hợp lệ từ `0` đến `n - 1`. Viết `i < n - 1` là cận quá hẹp: chương trình chạy ổn định và luôn in 42000, sai nhưng trông hợp lý. Viết `i <= n` là cận quá rộng: lượt cuối đọc `amounts[3]`, chỉ số không tồn tại, dẫn đến **hành vi không xác định** (*undefined behavior*); chương trình không chắc crash, có thể trông như chạy đúng, nên một lần chạy không báo lỗi không chứng minh gì. Điều kiện đúng là `i < n`.

Bài học chung: **nắm rõ hợp đồng ở ranh giới, không tin vào một lần chạy may mắn.**

#### Thử ngay (10 phút)

Không cần chạy mã. Hãy viết ba dòng dự đoán: (1) với tên `Vở O'Reilly`, câu SQL nối chuỗi tạo ra chuỗi lệnh nào; (2) với `expense.title` là `<b>Vở</b>`, ô dùng `textContent` và ô dùng `innerHTML` hiện gì; (3) với `i < n - 1` tổng in ra bao nhiêu, với `i <= n` chạm tới chỉ số nào. Rồi mở `vi-du/nam-2-web/app.js`, tìm dòng `cell.textContent` và ghi tên hàm chứa nó.

#### Gợi ý đối chiếu

Dự đoán đúng hướng nếu dòng (1) có hai dấu nháy đơn liền nhau bất thường, dòng (2) phân biệt "hiện nguyên chuỗi" với "hiện chữ in đậm", dòng (3) ghi 42000 và chỉ số 3, không ghi "chắc chắn crash".

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Ứng dụng cho người dùng chọn cột để sắp xếp: vì sao dấu `?` không giải quyết được, và danh sách cho phép trông như thế nào?
- **Từ khóa tra cứu:** parameterized query, textContent vs innerHTML, undefined behavior.
- **Trong Sổ tay thực hành:** [Ba lỗi kỹ thuật ở ranh giới dữ liệu](chapters/chapter-04.md#muc-4-8): cách chạy `vi-du/minh-hoa-sqlite.py`, kết quả mong đợi, trích đoạn C++; [Bài thực hành 03](chapters/chapter-02.md#muc-2-3): bảng trace cho lỗi bỏ sót 18000.

### 4.9. Danh sách kiểm tra trước khi nộp

Mục này gom cả chương thành một danh sách để rà bài trong mười phút trước khi nộp. Chỉ đánh dấu **sau khi đã thực hiện**, không đánh dấu theo dự định.

#### Ý chính

"Chặn nộp" không có nghĩa là hủy cả bài: nhóm có thể loại phần chưa rõ hoặc thu hẹp chức năng.

**Chặn nộp nếu chưa xử lý**

- [ ] Không còn khóa thật hoặc dữ liệu cá nhân không cần thiết trong tệp, ảnh, nội dung sẽ chia sẻ (4.1, 4.2).
- [ ] Ba khoản giả cho tổng 35000 + 7000 + 18000 = 60000; danh sách rỗng có tổng 0; `amount` nguyên dương, không quá `1e9`; tối đa 500 khoản.
- [ ] Tên khoản chi hiển thị bằng `textContent`; đã thử với `<b>Vở</b>` (4.8).
- [ ] Không có mã chưa rõ quyền hoặc gói chưa kiểm chứng (4.4, 4.6).
- [ ] Khai báo AI khớp việc đã làm; không ghi "đã kiểm thử" khi chưa chạy (4.5, 4.7).
- [ ] Diff của lượt Agent gần nhất đã được đọc; số ca kiểm thử không giảm (4.3).

**Hỏi giảng viên khi chưa rõ**

- [ ] Phạm vi dùng AI và hình thức khai báo đã rõ; phần chưa rõ ghi ở trạng thái chờ.
- [ ] Việc ngoài quyền của nhóm (tài khoản tổ chức, lịch sử kho chung) đã chuyển đúng đầu mối.

**Cải thiện sau**

- [ ] Chỉnh giao diện, mở rộng tính năng ghi riêng, không lẫn với yêu cầu an toàn.
- [ ] Nêu rõ bản Web không có backend; SQL là minh họa riêng.

Mỗi dấu kiểm cần bằng chứng ngắn: mục tiêu, đầu vào, kết quả mong đợi, kết quả quan sát, trạng thái, bản mã.

#### Thử ngay (10 phút)

Hãy mở bài gần nhất và đi qua đủ mười dòng. Với mỗi dòng, ghi một trong ba trạng thái: đã làm và có bằng chứng; chưa làm; không áp dụng. Ghi thêm một dòng cho mục "chưa làm" quan trọng nhất: việc cụ thể sẽ làm trước khi nộp.

#### Gợi ý đối chiếu

Kết quả đúng hướng nếu có ít nhất một dòng "chưa làm" được ghi trung thực; danh sách toàn dấu kiểm sau mười phút thường là đánh dấu theo dự định.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Hai bộ kiểm thử đi kèm (34 ca Web, 9 ca C++) vì sao không được cộng gộp khi báo cáo?
- **Từ khóa tra cứu:** pre-submission checklist, evidence log, exit code.
- **Trong Sổ tay thực hành:** [Thực hành trước khi nộp](chapters/chapter-04.md#muc-4-9): bài rà soát kho giả định, mẫu ghi bằng chứng, rubric luyện tập, câu hỏi có đáp án.

### Tóm tắt chương

- Khóa bị lộ: thu hồi trước, dọn sau; báo sự cố bằng mô tả, không bằng bí mật.
- Dữ liệu gửi cho AI: dữ liệu giả đủ để tái hiện lỗi; đổi tên chưa phải ẩn danh.
- Agent và gói thư viện: checkpoint trước, đọc diff sau; số ca kiểm thử không giảm; không cài gói chỉ vì AI đề xuất.
- Liêm chính và bản quyền: khai báo là mô tả, không phải xin phép; công khai không phải là giấy phép.
- Ranh giới dữ liệu: truy vấn tham số hóa, `textContent`, điều kiện `i < n`.

**Ba câu để tự kiểm**

1. Minh đã xóa `config.js` và tạo khóa mới. Việc quan trọng nhất còn thiếu là gì?
2. Lan bỏ tên trong bảng chi tiêu thật nhưng giữ mã sinh viên và giờ giao dịch. Đây đã là dữ liệu giả hay ẩn danh chưa?
3. Nhận định "kho công khai không có giấy phép thì được chép, còn GPL cấm thương mại" sai ở đâu?

### Cầu nối sang chương sau

Đến đây, người học đã nắm vai trò của AI, cách dùng có kiểm soát, cách giữ việc học và các ranh giới cần tôn trọng. Chương 5 giúp chọn AI, model và gói dịch vụ phù hợp với nhiệm vụ, mức rủi ro và ngân sách, thay vì dựa vào danh tiếng.

### Tài liệu tham khảo

Mốc đối chiếu 29/10/2026; thông tin pháp luật *chưa kiểm chứng* sau mốc này.

1. Quốc hội. [Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf).
2. Văn phòng Quốc hội. [Văn bản hợp nhất số 67/VBHN-VPQH Luật Sở hữu trí tuệ](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469197-1775632354_v1_1775783230_signed.pdf), thể hiện sửa đổi theo Luật số 131/2025/QH15.
3. OWASP. [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
4. OWASP. [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
5. GitHub. [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
6. GitHub. [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).

---

## CHƯƠNG 5 · LỰA CHỌN AI VÀ MODEL PHÙ HỢP VỚI NHIỆM VỤ

Bốn chương trước đã đi qua bốn bước: hiểu vai trò của AI, dùng AI có kiểm soát, giữ vững việc tự học và giữ ranh giới về dữ liệu, bản quyền, liêm chính. Chương này là bước thứ năm, bước "Chọn": với nhiệm vụ cụ thể, nên dùng AI nào, model nào, trả tiền hay không và trả bao nhiêu. Việc chọn đặt ở cuối vì chỉ khi đã biết AI nên giữ vai trò gì và kết quả được kiểm bằng cách nào, người học mới có tiêu chí để chọn. Chương không xếp hạng sản phẩm; nguyên tắc vẫn là: AI hỗ trợ, người học quyết định.

Mọi giá, tỷ giá và ngân sách trong chương là *dữ liệu giả định*; thông tin về dịch vụ, ưu đãi và điều khoản ở trạng thái *chưa kiểm chứng* theo mốc 29/10/2026 và cần tra lại khi áp dụng.

**Sau chương này, người học có thể:**

- Phân biệt ba hình thức sử dụng (miễn phí, thuê bao, API trả theo lượng dùng) và tách chi phí input khỏi output khi dự toán.
- Giải thích vì sao cảnh báo ngân sách (budget alert) không phải trần chặn chi tiêu.
- Áp dụng nguyên tắc ưu tiên miễn phí và đọc một chương trình ưu đãi sinh viên qua các câu hỏi về điều kiện, bằng chứng và thời hạn.
- Chọn công cụ theo tác vụ bằng năm lăng kính và viết một quyết định có điều kiện trong 20 phút.

### Tình huống mở đầu

Minh cần hiểu vì sao chương trình cộng ba khoản 35000, 7000 và 18000 của ViSinhVien cho kết quả 42000 thay vì 60000. Lan cần kiểm tra phiên bản Web chạy cục bộ và tìm hiểu một chương trình ưu đãi sinh viên. Cả hai thấy nút nâng cấp gói trên giao diện, nghe nói "dùng API rẻ hơn", và nhận ra chưa trả lời được ba câu hỏi: nên chọn công cụ nào, có cần trả tiền không, và nếu có thì trả bao nhiêu.

Câu hỏi của chương là: dựa trên những điều đã học, Minh và Lan nên chọn gì, vì sao, và kiểm tra lựa chọn đó bằng cách nào.

### 5.1. Chi phí sử dụng AI: hiểu cách tính trước khi gửi yêu cầu (AI Wallet)

Mục này giúp người học biết khoản sẽ phải trả, mức trả và vì sao, trước khi bấm gửi yêu cầu đầu tiên. Bản đọc trên web có mô phỏng chi phí ngay dưới tiêu đề mục; hãy thử đổi số request hoặc đơn giá để xem tổng tiền thay đổi, rồi đọc tiếp để hiểu từng bước tính.

#### Ý chính 1 — Ba hình thức sử dụng và những token không nằm trong câu vừa gõ

Trước khi so sánh tiền, cần xác định đang so sánh cái gì. Có ba hình thức sử dụng.

| Hình thức | Cách hiểu ở mức nhập môn | Câu hỏi cần trả lời trước |
| --- | --- | --- |
| Free (miễn phí) | Một phạm vi sử dụng không thu tiền, kèm điều kiện | Model, tính năng, quota và chính sách dữ liệu là gì? |
| Subscription (thuê bao) | Trả phí định kỳ cho quyền lợi của một gói | Gói gồm gì, giới hạn gì, gia hạn khi nào? |
| API pay-as-you-go (trả theo lượng dùng) | Chương trình gọi dịch vụ, phí tính theo bảng giá | Đơn vị tính input và output, phí công cụ, giới hạn chi phí là gì? |

**Quota** (hạn mức) là giới hạn sử dụng có đơn vị và chu kỳ xác định; miễn phí không có nghĩa là vô hạn. Quyền dùng ứng dụng chat và quyền dùng API phải được kiểm tra riêng.

Lan cho rằng input chỉ gồm câu "sửa hàm tổng". Trên thực tế, ứng dụng có thể gửi kèm brief, lịch sử trao đổi, tệp đính kèm và kết quả công cụ (tool output). Một số model còn tính phí **reasoning token**, tức token phát sinh khi suy luận nội bộ. Ở chế độ **agent**, một yêu cầu "sửa cho xong" có thể sinh ra nhiều request. Số token thật chỉ biết được qua báo cáo usage của dịch vụ, không qua việc đếm từ.

#### Ý chính 2 — Tách input khỏi output: 50 request và 1000 request

Lan dự toán cho 50 request với các con số cố định dưới đây (*dữ liệu giả định*, không mô tả hóa đơn của nhà cung cấp nào). Một **request** là một yêu cầu gửi đến dịch vụ.

| Đại lượng | Giá trị giả định |
| --- | ---: |
| Input mỗi request | 20000 token |
| Output mỗi request | 5000 token |
| Giá input | 0.30 USD / 1000000 token |
| Giá output | 2.50 USD / 1000000 token |
| Tỷ giá | 25000 VND / USD |

Phép tính đi qua sáu dòng: tổng input (1000000 token), tổng output (250000 token), tiền input (0.30 USD), tiền output (0.625 USD), tổng **0.925 USD**, quy đổi **23125 VND, chưa tính phí**. Cần chia cho một triệu vì đơn giá niêm yết theo triệu token. Kiểm tra chéo theo từng request: một request tốn 0.006 + 0.0125 = 0.0185 USD; nhân với 50 cũng ra 0.925 USD. Hai hướng tính khớp nhau giúp phát hiện lỗi nhầm triệu với nghìn.

Output ít token hơn nhưng tốn nhiều tiền hơn vì đơn giá output cao hơn; không được gộp 1250000 token rồi nhân với một giá chung. Giữ nguyên giả định và tăng lên 1000 request, tức gấp 20 lần, tổng tiền thành 18.50 USD = **462500 VND**, chưa tính phí: con số nhỏ ở 50 request đổi ý nghĩa khi nhân lên.

**Budget alert** (cảnh báo ngân sách) chỉ là thông báo khi mức chi chạm ngưỡng, không phải **hard cap** (trần cứng) chặn việc sử dụng. Email cảnh báo ở mức 80% không chứng minh việc dùng sẽ dừng ở 100%; ngay cả khi có trần, độ trễ và các request đang xử lý vẫn có thể đẩy mức chi vượt ngưỡng. Chưa hiểu cơ chế này thì chưa bật thanh toán.

#### Thử ngay (10 phút)

Mục tiêu: tự lập một dự toán và kiểm tra chéo. Lấy giấy, viết sáu dòng tính cho 50 request theo bảng giả định trên, ghi đơn vị ở từng dòng. Tính lại theo từng request rồi nhân với 50. Cuối cùng, đổi một giả định (ví dụ output mỗi request thành 10000 token) và tính lại tổng USD. Ghi lại: hai hướng tính có khớp không, và khoản nào thay đổi nhiều nhất.

#### Gợi ý đối chiếu

Đúng hướng khi: mỗi dòng có đơn vị (token, USD, VND); có phép chia cho 1000000; tiền output lớn hơn tiền input dù số token nhỏ hơn; hai hướng tính cho cùng tổng; kết quả có ghi chú "chưa tính phí"; không làm tròn ở bước trung gian.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu ứng dụng gửi kèm toàn bộ lịch sử trao đổi vào mỗi lượt, input của lượt thứ mười lớn gấp bao nhiêu lần lượt thứ nhất?
- **Từ khóa tra cứu:** token pricing, budget alert, hard cap, usage report.
- **Trong Sổ tay thực hành:** [Chi phí sử dụng AI (AI Wallet)](chapters/chapter-05.md#muc-5-1) — bảng tính đầy đủ cho 50 và 1000 request, thuê bao giả định 20 USD, credit dùng chung và cơ chế kiểm soát chi tiêu.

### 5.2. Ưu tiên phương án miễn phí: chỉ mua khi biết rõ còn thiếu gì (Free First)

Mục này giúp người học quyết định có nên trả tiền hay không, dựa trên nhu cầu thật chứ không dựa trên cảm giác "phải có gói mới học tốt". Phương án 0 VND luôn phải có mặt trong bảng lựa chọn.

#### Ý chính 1 — Quyền không mua là một phần của kế hoạch

Để hiểu lỗi 42000, Minh chỉ cần giấy bút, kiến thức về vòng lặp và một trình biên dịch sẵn có; chưa cần agent sửa kho mã. Lan có thể học phiên bản Web chạy cục bộ mà không cần tích hợp AI. Nguyên tắc **ưu tiên miễn phí** (*free first*) là chọn trước phương án không thu phí nhưng đủ dùng, đồng thời vẫn đọc điều kiện dịch vụ.

Khi hết quota, người học chia nhỏ câu hỏi, chờ chu kỳ tiếp theo hoặc hỏi giảng viên và nhóm học. Không lách giới hạn bằng cách tạo nhiều tài khoản, dùng key nhặt được hay thử thanh toán vì tò mò. Khả năng trả tiền không phải thước đo năng lực; ngân sách dành cho AI bằng 0 vẫn hoàn toàn hợp lệ.

Trước khi nâng cấp, cần hoàn thành được một câu ba vế: còn thiếu gì, gói này giải quyết bằng gì, lợi ích đo bằng gì. Chưa điền được thì chưa có lý do để mua.

#### Ý chính 2 — Kế hoạch 300000 VND cho 15 tuần và điều kiện phải xét trước giá

Lan lập một kế hoạch với *dữ liệu giả định*: **300000 VND cho một học kỳ 15 tuần**. Đây không phải mức chi khuyến nghị; mục đích là cho thấy một quyết định chi tiêu hằng tháng có thể vượt kế hoạch của cả học kỳ.

| Giai đoạn | Dự trù | Điều kiện để quyết định |
| --- | ---: | --- |
| Tuần 1–5: học nền tảng | 0 VND | Tài liệu và công cụ miễn phí hợp lệ đủ dùng |
| Tuần 6–10: phát sinh nhu cầu rõ ràng | Tối đa 100000 VND | Có lợi ích đo được và đủ điều kiện sử dụng |
| Tuần 11–15: hoàn thiện bài | Tối đa 100000 VND | Đánh giá lại, không gia hạn theo quán tính |
| Dự phòng | 100000 VND | Không phải mục tiêu phải tiêu hết |
| Tổng trần cá nhân | 300000 VND | Kế hoạch trên giấy, không tự chặn hóa đơn |

Thuê bao giả định 20 USD, tức 500000 VND mỗi tháng, đã vượt cả kế hoạch học kỳ. Nếu 1000 request dồn vào một học kỳ, khoản 462500 VND cũng vượt trần. Ngày gia hạn và cách dừng tự động gia hạn phải được tìm hiểu trước khi mua.

Ưu đãi sinh viên cũng cần đọc như một hợp đồng. Hướng dẫn GitHub Education nêu các điều kiện như đang theo học tại cơ sở đủ điều kiện, có tài khoản cá nhân, chứng minh được tình trạng sinh viên và từ 13 tuổi trở lên; điều khoản Gemini API lại yêu cầu người dùng từ 18 tuổi, và với dịch vụ không trả phí, nội dung có thể được dùng để cải thiện sản phẩm (*chưa kiểm chứng*, ghi nhận theo mốc 29/10/2026). Điều kiện tuổi không chuyển từ chương trình này sang chương trình khác; email trường hỗ trợ chứng minh tình trạng sinh viên nhưng không bảo đảm được duyệt. Lan tách một chương trình ưu đãi thành năm câu hỏi: ai đủ điều kiện, cần bằng chứng gì, quyền lợi là gì, kéo dài bao lâu, điều gì xảy ra khi hết ưu đãi. Tuổi, dữ liệu và tài khoản phải được xét trước giá; không mua tài khoản lậu hay dùng chung key.

#### Thử ngay (10 phút)

Mục tiêu: ra quyết định cuối tuần thứ năm. Đến lúc đó, Lan chưa thấy chức năng nào cần trả tiền. Hãy điền phiếu dưới đây cho Lan, rồi quyết định giữ khoản dự trù 100000 VND hay mua một gói "để tạo động lực". Ghi lại ba tiêu chí để đánh giá lại ở tuần thứ mười.

```text
Còn thiếu: ______________________________
Gói này giải quyết điều đó bằng: ______________________________
Lợi ích sẽ đo qua: ______________________________
Ngày đánh giá lại: ______________________________
```

#### Gợi ý đối chiếu

Đúng hướng khi: vế "còn thiếu" nêu một hạn chế có thật (context, phạm vi, khả năng tự kiểm), không phải cảm giác; tiêu chí đánh giá lại đo được (số lỗi hiểu được, số thao tác tiết kiệm), không đo bằng số câu AI sinh ra; khoản chưa tiêu không bị coi là phần học bị thiếu.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Một gói trả phí ghi "không dùng dữ liệu để huấn luyện". Điều đó có đồng nghĩa với "không lưu" không?
- **Từ khóa tra cứu:** free tier, quota, student developer pack, terms of service, auto-renewal.
- **Trong Sổ tay thực hành:** [Ưu tiên phương án miễn phí (Free First)](chapters/chapter-05.md#muc-5-2) — bài quyết định cuối tuần thứ năm kèm gợi ý, phần đọc ưu đãi sinh viên và điều khoản về tuổi, dữ liệu, tài khoản.

### 5.3. Đối chiếu công cụ theo tác vụ, không theo danh tiếng (AI Tool Battle)

Mục này giúp người học so sánh công cụ một cách công bằng: chọn theo việc cần làm và bằng chứng có thể kiểm tra, thay vì theo lời đồn về công cụ "mạnh nhất".

#### Ý chính 1 — Năm lăng kính và ma trận tác vụ

Minh thích công cụ cho gợi ý ngắn để tự suy nghĩ; Lan ưa công cụ chỉ đúng tệp liên quan. Hai lựa chọn không mâu thuẫn, vì mỗi người ưu tiên một tác vụ khác nhau. Một công cụ dịch tốt không vì thế mà kiểm tra mã tốt.

Năm lăng kính để chọn công cụ là **provenance** (nguồn gốc của thông tin), **test** (cách kiểm tra), **context** (thông tin công cụ cần nhận), **privacy** (điều kiện xử lý dữ liệu) và **cost** (tổng chi phí). Ma trận dưới đây không xếp hạng sản phẩm thật; nó chỉ ra loại bằng chứng mỗi tác vụ cần.

| Tác vụ | Context cần có | Provenance và test | Privacy và cost |
| --- | --- | --- | --- |
| Suy luận logic (lỗi 42000 của Minh) | Mã nguồn, chỉ số, mục tiêu cộng mọi khoản | Bám cận vòng lặp; tự xét ca rỗng, một khoản, ba khoản | Dữ liệu giả; gợi ý ngắn trên phương án miễn phí |
| Viết mã hoặc refactor (Web của Lan) | Brief, hàm liên quan, cấu trúc Expense | Đọc kỹ thay đổi; thử giá trị biên và dữ liệu sai | Không dùng key; xét số bước và chi phí lặp |
| Đọc tài liệu dài | Đoạn được phép chia sẻ | Trích đúng đoạn, tìm mâu thuẫn | Không gửi tài liệu hạn chế; trích đoạn trước khi mua context lớn |
| Dịch và diễn giải | Thông báo lỗi, trình độ người học | Giữ nguyên tên API, số liệu và phủ định | Bỏ thông tin riêng tư; không cần agent |
| Tìm thông tin mới | Câu hỏi đúng sản phẩm, đúng phạm vi | Nguồn chính thức, ngày truy cập | Không gửi giấy tờ; xét phí tìm kiếm |

Công cụ không truy cập web thì không dùng làm nguồn duy nhất cho chính sách hiện hành. Công cụ không chạy được mã vẫn có thể gợi ý, nhưng phải kiểm thử ở nơi khác.

#### Ý chính 2 — Benchmark công bằng: cùng đề, cùng dữ liệu, cùng giới hạn

**Benchmark** là phép thử có kiểm soát để so sánh mức độ phù hợp. Sổ tay có ba đề: Đề A giải thích logic C++ cho Minh bằng gợi ý từng bước; Đề B bổ sung xác thực cho hàm tính tổng Web mà không đổi phạm vi sản phẩm; Đề C đọc và kiểm tra một đoạn dữ kiện về ưu đãi sinh viên có mốc thời gian cũ. Mỗi đề chấm theo năm tiêu chí ứng với năm lăng kính, mỗi tiêu chí từ 0 đến 2 điểm.

Phép thử chỉ công bằng khi giữ nguyên brief, mã nguồn, dữ liệu, yêu cầu đầu ra và giới hạn trợ giúp giữa các công cụ; mở phiên mới để giảm ảnh hưởng của lịch sử; ghi tên ứng dụng, nhãn model (hoặc "chưa xác định"), chế độ và ngày thử. Trình tự: gửi đề → giữ nguyên câu trả lời → tự kiểm tra → chấm điểm → ghi giới hạn của kết luận. Một câu trả lời đề nghị đưa key vào mã Web bị loại dù các điểm khác cao. Vài đề thử không chứng minh được công cụ nào "tốt nhất cho mọi người".

#### Thử ngay (10 phút)

Mục tiêu: lập phiếu so sánh trên giấy, không cần công cụ thật. Chọn một tác vụ trong ma trận (ví dụ lỗi 42000 của Minh). Hình dung hai công cụ giả định: một "chỉ chat, không chạy mã", một "agent đọc được tệp". Với mỗi công cụ, viết một dòng cho từng lăng kính: cần context gì, kiểm tra bằng gì, nguồn ở đâu, dữ liệu nào không gửi, tốn gì. Ghi lại: công cụ nào phù hợp với tác vụ này, và tác vụ nào thì không nên dùng nó.

#### Gợi ý đối chiếu

Đúng hướng khi: phiếu có đủ năm lăng kính cho mỗi công cụ; kết luận gắn với một tác vụ cụ thể, không phải "mạnh hơn nói chung"; có ít nhất một tác vụ ghi "không chọn"; phần chưa thử thật được ghi là "luyện đánh giá trên giấy", không ghi điểm như đã đo.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu hai công cụ cho cùng kết quả đúng ở Đề A nhưng một công cụ viết ngay toàn bộ bài, điểm "dễ học và dễ kiểm tra" nên khác nhau thế nào?
- **Từ khóa tra cứu:** benchmark, rubric, provenance, reproducibility, tool evaluation.
- **Trong Sổ tay thực hành:** [Đối chiếu công cụ theo tác vụ (AI Tool Battle)](chapters/chapter-05.md#muc-5-3) — ba đề A, B, C đầy đủ, chuẩn đối chiếu, rubric 10 điểm và phiếu ghi nhận benchmark.

### 5.4. Ra quyết định trong 20 phút (Mini Challenge)

Mục này ghép các kỹ năng của cả sách thành một phiếu hoàn chỉnh trong 20 phút: nhận diện công cụ, viết prompt đủ context, tính chi phí và ra quyết định có điều kiện. Chỉ cần giấy, không cần thẻ thanh toán hay tài khoản AI.

#### Ý chính — Năm bước, mỗi bước một mục đích

Tình huống giả định: Minh cần hiểu lỗi 42000; Lan kiểm tra phiên bản Web cục bộ và tìm hiểu ưu đãi. Một ứng dụng giả định tên "Trợ lý học ViSinhVien" chỉ công bố chế độ "Tự động", không nêu model hay provider. Chi phí dùng số liệu giả định ở mục 5.1.

1. **Phút 0–4, nhận diện:** điền application, model, provider; thêm producer nếu có căn cứ. Khoanh tròn điểm chưa rõ, ghi "chưa xác định" thay vì đoán model qua giao diện (xem lại [mục 1.2](chapters/chapter-01.md#muc-1-2)).
2. **Phút 4–8, viết prompt:** đưa vào mục tiêu, đoạn mã, hợp đồng dữ liệu, ba khoản chi và cặp số 60000 với 42000; yêu cầu gợi ý trước khi sửa. Đọc lại dưới góc nhìn của người chưa biết dự án để tìm context còn thiếu.
3. **Phút 8–13, ước tính chi phí:** tách input và output cho 50 request, quy đổi sang VND, rồi xét 1000 request; kiểm tra chéo theo từng request.
4. **Phút 13–17, ra quyết định:** dùng ít nhất ba tiêu chí trong ma trận, nêu phương án không trả tiền, cách kiểm chứng và điều kiện đánh giá lại.
5. **Phút 17–20, đối chiếu:** sửa phiếu nhưng giữ dấu vết lỗi ban đầu; trình bày trong 30 giây: đã biết gì, chưa biết gì, chọn gì, kiểm tra thế nào, chi tối đa bao nhiêu.

Một quyết định tốt trong bài này thường có mức chi bằng 0: Minh tự sửa cận vòng lặp với gợi ý từ một công cụ miễn phí hợp lệ; Lan giữ phiên bản Web cục bộ và ghi "chưa xác minh" cho thông tin ưu đãi. Sở thích cá nhân không thay thế được bằng chứng; cảnh báo ngân sách không thay thế được kế hoạch. Dù chọn công cụ nào, nguyên tắc của cả sách vẫn giữ nguyên: AI hỗ trợ, người học quyết định.

#### Thử ngay (10 phút)

Mục tiêu: hoàn thành phần quyết định có điều kiện, tức bước 4 ở trên, với kết quả tính ở mục 5.1 và kế hoạch ở mục 5.2. Điền sáu dòng, mỗi dòng một câu đầy đủ, rồi gạch chân chỗ chưa có bằng chứng.

```text
1. Với Minh, tôi chọn __________ vì __________.
2. Với Lan, tôi chọn __________ vì __________.
3. Ba tiêu chí tôi dựa vào là __________, __________, __________.
4. Phương án không trả tiền của tôi là __________.
5. Mức chi tôi chấp nhận lúc này là __________; tôi sẽ cân nhắc lại khi __________.
6. Nếu điều kiện tuổi chưa rõ hoặc có nguy cơ vượt ngân sách, tôi sẽ __________.
```

#### Gợi ý đối chiếu

Đúng hướng khi: dòng 1 và 2 nêu tác vụ cụ thể, không nêu tên sản phẩm vì danh tiếng; ba tiêu chí lấy từ năm lăng kính; dòng 4 là phương án có thật, làm được ngay; dòng 5 có con số và mốc thời gian; dòng 6 là hành động dừng, không phải cách lách.

#### Tự tìm hiểu thêm

- **Câu hỏi mở:** Sau một tuần dùng phương án đã chọn, bằng chứng nào cho thấy lựa chọn đó đúng, và bằng chứng nào buộc phải đổi?
- **Từ khóa tra cứu:** decision criteria, conditional decision, cost estimate, model identification.
- **Trong Sổ tay thực hành:** [Bài tập tổng hợp 20 phút (Mini Challenge)](chapters/chapter-05.md#muc-5-4) — phiếu đầy đủ bốn phần, prompt mẫu cho Minh, bảng phép tính bắt buộc và một phiếu hoàn chỉnh để đối chiếu sau khi tự làm.

### Tóm tắt chương

- Chọn công cụ theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng; thiếu chứng cứ thì ghi "chưa xác định".
- Chi phí phụ thuộc vào lượng dùng và đơn giá của từng loại token: 50 request giả định tốn 0.925 USD, 1000 request tốn 462500 VND, chưa tính phí.
- Budget alert là cảnh báo, không phải trần chặn; chưa hiểu cơ chế thì chưa bật thanh toán.
- Phương án 0 VND luôn có mặt; chỉ mua khi điền được "còn thiếu gì, giải quyết bằng gì, đo bằng gì".
- Benchmark chỉ công bằng khi cùng đề, cùng dữ liệu, cùng giới hạn; chấm bằng bằng chứng, không bằng cảm giác.

**Ba câu để tự kiểm:**

1. Đếm số từ tiếng Việt có đủ để tính hóa đơn theo token không? Vì sao?
2. Email trường có bảo đảm nhận được ưu đãi sinh viên và quyền dùng mọi API không?
3. Một công cụ được nhiều người khen là "mạnh nhất". Điều đó có đủ để chọn nó cho bài vòng lặp C++ của Minh không?

Xuyên suốt năm bước Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn là một nguyên tắc: AI hỗ trợ, người học quyết định.

### Cầu nối sang chương sau

Năm bước đã đủ để từng việc riêng lẻ được làm cẩn thận. [Dự án tổng kết](cam-nang/final-project.md) ghép các bước đó thành một sản phẩm hoàn chỉnh: người học xây dựng, kiểm thử và giải thích, đồng thời lưu bằng chứng cho từng quyết định về công cụ, cách dùng và ranh giới.

### Tài liệu tham khảo

Các nguồn ghi nhận theo mốc truy cập 29/10/2026; nội dung hiện hành cần tra lại trước khi áp dụng. Mọi mức giá, tỷ giá và ngân sách trong chương là dữ liệu giả định.

- [Google — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing): đơn vị giá input, output và phụ phí của một API thật, để đối chiếu cách đọc bảng giá.
- [Google — Gemini API billing](https://ai.google.dev/gemini-api/docs/billing) và [Google Cloud — Budgets](https://cloud.google.com/billing/docs/how-to/budgets): cơ chế cảnh báo ngân sách và kiểm soát mức dùng.
- [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms): điều kiện tuổi, cấp dịch vụ và cách xử lý dữ liệu.
- [GitHub — Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student): điều kiện và bằng chứng tình trạng sinh viên.
- [GitHub Student Developer Pack](https://education.github.com/pack): quyền lợi, thời hạn và giới hạn của ưu đãi.
- [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview): họ model và định danh, dùng khi nhận diện model (mục 5.4).

---

## DỰ ÁN TỔNG KẾT: LÀM, KIỂM, GIẢI THÍCH

Năm chương trước đã đi qua năm bước: hiểu, dùng, giữ vững, có trách nhiệm và chọn. Dự án tổng kết ghép cả năm bước thành một sản phẩm nhỏ có bằng chứng. Số liệu trong dự án là *Dữ liệu giả định*; không nhập chi tiêu thật vào bài làm.

### Đề bài

Đối tượng vẫn là ứng dụng ViSinhVien với ba khoản 35000 + 7000 + 18000 = 60000; không cần xây dựng ứng dụng mới. Điều cần luyện không phải là dùng công cụ AI mạnh nhất, mà là trả lời được ba câu hỏi bằng bằng chứng: sản phẩm làm gì và việc gì nằm ngoài phạm vi; căn cứ nào cho thấy sản phẩm đúng; khi không mở cửa sổ chat, người học còn tự giải thích được những gì. Câu "AI bảo là đúng" không phải bằng chứng. Phần nào còn thiếu bằng chứng phải ghi rõ là thiếu, không dùng giao diện đẹp để thay thế.

![Bronze thực hành C++, Silver thực hành Web, Gold nâng quy trình kiểm soát Agent từ một trong hai nhánh: quyền, diff, test, review, khai báo. Không cần trả phí; không có AI có thể mô phỏng thủ công và ghi rõ.](assets/final-boss.svg)

### Ba cấp độ

Chọn cấp theo năng lực cần luyện; cấp cao hơn không có nghĩa là viết nhiều mã hơn.

**Bronze · C++ cơ bản** theo nhánh của Minh, thời lượng gợi ý 60–90 phút. Sản phẩm là hàm cộng có kiểm tra đầu vào với hai bản vá, bộ kiểm thử và lời giải thích về chỉ số và kiểu dữ liệu; không cần Web hay tài khoản AI trả phí.

**Silver · Web có luồng dữ liệu** theo nhánh của Lan, thời lượng gợi ý 90–120 phút. Sản phẩm là hai lỗi logic được sửa trong bài biệt lập, kèm biên bản kiểm tra luồng form → dữ liệu → DOM và cơ chế lưu trữ trên bản demo đúng; không cần backend hay đăng nhập.

**Gold · Quy trình Agent có kiểm soát** dành cho người đã xong Bronze hoặc Silver, cần thêm 30–45 phút. Sản phẩm là bài của cấp nền cộng với phạm vi quyền, kế hoạch, diff, nhật ký và biên bản nghiệm thu; không có quyền dùng Agent thì diễn tập trên giấy và ghi rõ là mô phỏng.

Thời lượng chỉ để lập kế hoạch, không phải thước đo năng lực.

### Mười yêu cầu của bản nộp

1. Tự diễn đạt yêu cầu chức năng: phép tính tổng làm gì, đầu vào nào bị từ chối, việc gì ngoài phạm vi.
2. Chọn công cụ có lý do, gắn với tác vụ, rủi ro và ngân sách; nếu không dùng AI, ghi rõ.
3. Mô tả cấu trúc dữ liệu: `vector<long long>` ở Bronze; `Expense(id,title,amount,category)` và đường đi của `amount` ở Silver.
4. Triển khai trong phạm vi đã chọn; ghi rõ phần AI gợi ý và phần tự viết.
5. Sửa tối thiểu hai lỗi gốc; mỗi lỗi có hiện tượng, nguyên nhân và phản ví dụ riêng.
6. Đọc diff: mỗi dòng thay đổi giải quyết yêu cầu nào; có tệp, phụ thuộc hay quyền nào tăng thêm không.
7. Chạy kiểm thử với kỳ vọng xác định trước; giữ cả lần chạy thất bại, không chỉ chụp kết quả đạt.
8. Rà soát dữ liệu cá nhân, khóa API, thư viện, giấy phép; không dùng dữ liệu thật.
9. Khai báo đúng mức hỗ trợ của AI theo mẫu trong [Thỏa thuận học tập](chapters/learning-agreement.md).
10. Giải thích sản phẩm, trả lời một câu hỏi biến thể mà không dùng AI, nêu giới hạn chưa kiểm chứng.

### Bắt đầu từ đâu

Đề đầy đủ nằm trong [Sổ tay thực hành](chapters/final-boss.md). Ở đó có bộ đề có lỗi chủ đích trong thư mục `vi-du/final-boss/` (`bronze.cpp` với 9 ca kiểm thử, `silver.cjs` và `test_silver.cjs` với 12 ca), hướng dẫn tạo thư mục `bai-lam/final-boss`, lệnh biên dịch và chạy cho từng cấp, quy trình sáu bước cho cấp Gold, bảng nghiệm thu 100 điểm và kịch bản buổi bảo vệ tám phút. Trước khi mở phần đáp án ở đó, hãy ghi dự đoán riêng cho từng ca kiểm thử.

Kết thúc dự án, người học có một sản phẩm nhỏ cùng một chuỗi bằng chứng có thể lặp lại. Khi công cụ AI không còn sẵn dùng, bảng trace, bộ kiểm thử và khả năng tự giải thích vẫn là năng lực của chính người học. AI hỗ trợ, người học quyết định.

---

## THƯ VIỆN PROMPT MẪU

Mười một thẻ prompt, mã P01–P11, để sao chép khi gặp đúng điểm nghẽn: P01–P08 phục vụ học chủ động (Chương 3); P09–P11 giúp chuẩn bị ngữ cảnh, giao việc cho Agent và kiểm chứng nguồn. Mỗi lần chỉ chọn một thẻ. Trước khi gửi, hãy đọc lại toàn bộ, thay phần trong ngoặc vuông bằng dữ liệu giả được phép chia sẻ (35000, 7000, 18000; tổng 60000). Prompt là lời yêu cầu, không phải cơ chế bảo vệ của hệ thống. Thuyết minh đầy đủ từng thẻ: [Sổ tay thực hành](chapters/prompt-library.md).

### P01 · Hỏi đáp kiểu Socratic: bắt đầu từ câu hỏi

Dùng khi chương trình cho kết quả sai (Minh nhận 42000 thay vì 60000) mà chưa biết lỗi ở đâu.

```text
Tôi là Minh, năm nhất học C++. Bản C++ ViSinhVien chỉ dùng
vector<long long> amounts, không cần class Expense bốn trường.
Dữ liệu hoàn toàn giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000.
Tổng đúng 60000; vòng lặp i < n - 1 đang cho 42000, n là int.
Hợp đồng: tiền nguyên VND từ 1 đến 1000000000; tối đa 500 khoản;
danh sách rỗng hợp lệ và tổng bằng 0.
Hãy hỏi kiểu Socratic, một câu mỗi lượt, chờ tôi trả lời.
Bắt đầu từ các chỉ số hợp lệ của ba phần tử. Không viết vòng lặp
đúng và chưa nêu điều kiện cần thay. Chỉ nhận xét lập luận tôi gửi.
Bằng chứng cuối buổi: tôi tự trace, nêu lượt bị bỏ và lý do sửa.
Nếu lỡ lộ lời giải, dừng và giao ca một khoản 7000 để tôi tự trace;
không giải hộ ca mới. Không nhận đã chạy code nếu chưa thực thi.
```

Sau khi dùng, tự làm: viết ra một điều mới sau mỗi câu hỏi; AI hỏi nhiều câu thì chỉ trả lời một.

### P02 · Gợi ý theo ba tầng

Dùng khi chưa biết cần nhìn vào đâu nhưng vẫn muốn tự sửa.

```text
Tôi tự viết vòng lặp C++ cộng vector<long long> amounts trong
ViSinhVien. Ba khoản giả theo thứ tự: 35000, 7000, 18000 VND.
Mong đợi 60000, đang nhận 42000. Mỗi khoản nguyên từ 1 đến 1e9,
tối đa 500 khoản, rỗng tổng 0. Vòng lặp hiện dùng i < n - 1;
n và i là int, tổng là long long.
Chuẩn bị ba mức gợi ý: mức 1 chỉ vùng cần xem; mức 2 hỏi quan hệ
chỉ số cuối và số phần tử; mức 3 cho bảng trace còn ô trống.
Bây giờ CHỈ đưa mức 1. Chỉ nâng mức khi tôi yêu cầu sau khi báo
điều đã thử. Không viết code sửa hoặc điều kiện đúng.
Kết quả cần có là bảng tôi tự điền và một thay đổi tôi giải thích.
Nếu lộ lời giải, báo rõ rồi giao ca rỗng và danh sách một khoản 12000
để tôi tự so hai cận, không kèm kết quả. Ca rỗng riêng lẻ không đủ
phân biệt hai cận. Không chỉnh file hay chạy lệnh ở nhiệm vụ này.
```

Sau khi dùng, tự làm: ghi điều đã thử trước khi xin nâng mức; tự điền bảng trace, tự giải thích thay đổi.

### P03 · Trace cả giá trị lẫn kiểu dữ liệu

Dùng khi thấy một chuỗi số dài bất thường (Lan mô phỏng lỗi cộng chuỗi JavaScript).

```text
Tôi là Lan, năm hai học Web. ViSinhVien dùng HTML/JS/localStorage,
không backend. Bộ mẫu giả chuẩn có tiền số: 35000, 7000, 18000;
tổng 60000. Bây giờ tôi mô phỏng lỗi bằng amount chuỗi "35000",
"7000", "18000", với total bắt đầu là số 0.
Mỗi lượt thực hiện total = total + expense.amount.
Hãy tạo bảng TRỐNG với cột: lượt, kiểu total trước, kiểu amount,
phép toán, giá trị total sau, kiểu total sau. Chờ tôi điền từng hàng.
Không điền hộ và không viết hàm chuyển kiểu. Hợp đồng đích là
amount số nguyên VND từ 1 đến 1e9; tối đa 500 khoản, rỗng trả 0.
Hãy nhận xét chỗ tôi nhầm kiểu; mục tiêu là tôi chỉ ra lượt đầu
đổi kiểu và ranh giới cần kiểm tra đầu vào.
Nếu lỡ điền bảng, dừng; để tôi tự trace một chuỗi "7000" từ total=0.
Không nói rằng chạy thử đã thành công nếu chỉ suy luận.
```

Sau khi dùng, tự làm: điền từng hàng, giữ dấu ngoặc kép cho chuỗi; chỉ ra lượt đầu tiên đổi kiểu.

### P04 · Review đúng một thay đổi

Dùng khi đã có một bản vá duy nhất (`i < n - 1` thành `i < n`) và muốn kiểm lập luận.

```text
Tôi là Minh. Bản C++ ViSinhVien dùng vector<long long> amounts;
int n là số khoản, int i là chỉ số, long long total là tổng.
Dữ liệu giả 35000, 7000, 18000; tổng đúng 60000, cận cũ cho 42000.
Thay đổi duy nhất của tôi: i < n - 1 thành i < n.
Hợp đồng dữ liệu: nguyên VND từ 1 đến 1e9, tối đa 500; rỗng tổng 0.
Chỉ review thay đổi cận này, hỏi tôi chứng minh phạm vi chỉ số và
chọn test. Không viết lại hàm, không thêm validation hay tính năng.
Phân biệt rõ: sửa cận KHÔNG tự chứng minh chương trình từ chối
đầu vào sai; phần validation là việc riêng chưa được review ở đây.
Chờ tôi giải thích ba khoản, một khoản 7000, rỗng và vì sao dùng
long long. Nếu đưa lời giải đầy đủ, dừng rồi giao n=1 để tôi tự so
hai điều kiện. Không thay file và không nhận đã chạy kiểm thử.
```

Sau khi dùng, tự làm: chứng minh phạm vi chỉ số với ba khoản, một khoản 7000 và danh sách rỗng; sửa cận chưa chứng minh phần kiểm tra đầu vào.

### P05 · Thiết kế kiểm thử trước khi viết mã

Dùng khi chuẩn bị viết hàm tính tổng và muốn có bộ kiểm thử độc lập trước.

```text
Tôi là Lan. Chưa viết hàm totalExpenses cho bản Web ViSinhVien.
Expense gồm id, title, amount, category. Hợp đồng phần tính tiền:
amount phải là số nguyên VND từ 1 đến 1000000000; tối đa 500
khoản; rỗng trả 0; amount dạng chuỗi phải bị từ chối ở hàm tính tổng.
Dữ liệu giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000; tổng 60000.
Hãy yêu cầu tôi đề xuất lần lượt ca thường, biên và dữ liệu sai.
Không viết hàm, không viết test tự động, không tính hộ kỳ vọng.
Sau mỗi ca, hỏi lý do hoặc chỉ ra LOẠI ca còn thiếu, chưa cho đáp án.
Bảng do tôi điền cần có đầu vào, kỳ vọng, lý do và trạng thái chưa chạy.
Nếu lộ code/đáp án, dừng và để tôi tự tính ca 500 khoản mỗi khoản 1e9.
Không gộp kiểm thử parseAmount với kiểm thử form/DOM/localStorage.
```

Sau khi dùng, tự làm: tính mọi kỳ vọng bằng tay; bảng ghi đầu vào, kỳ vọng, lý do và trạng thái.

### P06 · Đọc tài liệu tiếng Anh có đối chiếu

Dùng khi vướng vài từ kỹ thuật trong một câu tiếng Anh đã đọc.

```text
Tôi là Lan, làm Web ViSinhVien bằng HTML/JS/localStorage, không backend.
Câu sau do cẩm nang tự soạn để luyện đọc, KHÔNG là trích dẫn chính thức:
"The value of a text input is a string. Convert and validate it before
storing an expense amount."
Ví dụ giả: ô nhập Cơm trưa chứa "35000"; Expense.amount cần là số nguyên
VND từ 1 đến 1e9, tối đa 500 khoản trong danh sách, rỗng tổng 0.
Giải thích value, string, convert, validate trong ngữ cảnh rồi hỏi tôi
diễn giải câu trên bằng tiếng Việt và nêu một đầu vào sai.
Không viết hàm, không bịa nguồn, không nhận đã mở tài liệu chính thức.
Tôi cần chứng minh mình phân biệt chuyển kiểu và kiểm tra hợp lệ.
Nếu lộ code, dừng rồi hỏi tôi phân tích "35000abc" bằng lời,
không nêu sẵn kết luận.
```

Sau khi dùng, tự làm: diễn giải câu bằng tiếng Việt và nêu một đầu vào sai; tài liệu thật cần kèm URL.

### P07 · Vấn đáp ôn tập, không đoán điểm môn học

Dùng khi đã học xong một nội dung và muốn tự kiểm mức hiểu qua vấn đáp.

```text
Tôi đã học hai lỗi ViSinhVien: cận vòng lặp C++ bỏ cuối cho 42000
thay vì 60000 và amount chuỗi trong JS làm phép + nối ký tự.
Dữ liệu giả: 35000, 7000, 18000 VND. C++ dùng vector<long long>;
Web dùng Expense(id,title,amount,category). Tiền nguyên từ 1 đến 1e9,
tối đa 500 khoản, rỗng tổng 0. Web dùng localStorage, không backend.
Vấn đáp một câu mỗi lượt: chỉ số, kiểu dữ liệu, test, rồi lưu trữ Web.
Chờ tôi trả lời; hỏi thêm nếu mơ hồ. Không trả lời thay, không phán
năng lực tổng quát và không đoán điểm hay quy định của học phần.
Cuối phiên ghi điều tôi đã chứng minh bằng ví dụ và chỗ cần luyện.
Nếu lộ đáp án, bỏ câu đó khỏi đánh giá độc lập, giao câu biến thể
mới không kèm gợi ý trong lượt đầu. Không nhận đã kiểm thử code.
```

Sau khi dùng, tự làm: nêu ví dụ, tự chạy chương trình khi cần; câu đã lộ đáp án chỉ tính là ôn tập.

### P08 · Đóng chat rồi làm bài biến thể

Dùng khi muốn tự kiểm khả năng vận dụng trên một bài tương tự, chưa nhận lời giải.

```text
Tôi muốn tự kiểm tra mà chưa nhận lời giải. ViSinhVien có ba khoản
giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000. Tiền nguyên VND
1..1e9, tối đa 500 khoản, rỗng tổng 0. C++ dùng vector<long long>;
Web dùng Expense(id,title,amount,category). Hợp đồng Web: id là số
nguyên an toàn, dương, không trùng; title là chuỗi sau trim dài 1–80
đơn vị UTF-16; category là chuỗi thuộc an-uong, di-lai, hoc-tap, khac.
Giao hai nhiệm vụ ngắn: C++ tìm tiền lớn nhất, quy ước rỗng trả 0;
JS tính tổng theo category nhưng phải xác thực TOÀN BỘ danh sách
trước khi lọc, không che khoản sai nằm ở nhóm khác.
Không cho thuật toán, code, kết quả mẫu hoặc gợi ý ngay.
Tôi đóng chat, thử 4 phút rồi gửi bài và dự đoán. Nếu chưa xong,
chỉ giúp xác định điểm nghẽn; không coi thời gian là thước đo năng lực.
Đối chiếu lập luận, ca thường, rỗng và dữ liệu sai tôi trình bày.
Nếu lộ đáp án, đổi sang tính bất biến khi đảo thứ tự, chưa nói kết quả.
```

Sau khi dùng, tự làm: đóng chat, thử bốn phút, ghi trung thực phần đã làm; lượt này không thay phiên 25 phút không AI.

### P09 · Chuẩn bị ngữ cảnh (brief) trước khi hỏi

Dùng khi cần hỏi về một lỗi cụ thể và đã quan sát được hiện tượng.

```text
Mục tiêu: [một việc cụ thể trong ViSinhVien]. Tôi học [C++/Web].
Môi trường và vị trí: [tên shell, thư mục hiện tại, file liên quan].
Dữ liệu GIẢ chuẩn 35000, 7000, 18000 VND; tổng 60000.
Hợp đồng: tiền nguyên 1..1e9, tối đa 500, rỗng tổng 0.
Hiện tượng quan sát: [đầu ra đã nhìn thấy, hoặc ghi chưa chạy].
Kỳ vọng tôi tự tính: [giá trị và cách tính].
Điều đã thử: [một thao tác và kết quả, không suy đoán].
Đoạn code liên quan: [chỉ phần cần thiết, không bí mật/dữ liệu thật].
Chỉ phân tích nguyên nhân và hỏi tối đa một câu còn thiếu trước;
chưa sửa file, chưa cài gì, chưa chạy lệnh. Nói rõ giả thuyết nào
cần kiểm chứng và đề xuất một phép thử nhỏ để phân biệt chúng.
```

Sau khi dùng, tự làm: ô chưa biết thì ghi "chưa xác định"; kiểm xem AI có tách giả thuyết khỏi điều đã kiểm chứng.

### P10 · Hợp đồng giao việc cho Agent

Dùng khi giao cho Agent một thay đổi đã thống nhất trong bản sao `bai-lam/`.

```text
Bài tập ViSinhVien với dữ liệu giả 35000,7000,18000 VND.
Tiền nguyên 1..1e9, tối đa 500 khoản, rỗng tổng 0.
Đích: [một thay đổi đã thống nhất]. Chỉ làm trong bản sao
bai-lam/[nhánh], chỉ được sửa [danh sách file cụ thể].
Bước đầu chỉ đọc, nêu kế hoạch và test dự kiến; chờ tôi đồng ý
trước khi sửa. Không thay config/quyền, không cài gói, không gọi API,
không đăng nhập, không commit/push/publish, không xóa file.
Nếu cần vượt phạm vi, dừng và nêu việc cần quyết định, không tự làm.
Sau sửa cho diff, lệnh thực sự chạy, exit code và output; phân biệt
trace với test đã chạy. Giữ cả lần thất bại, không dùng executable cũ
sau lỗi build. Việc thiếu công cụ phải ghi chưa kiểm chứng.
Tôi sẽ đọc diff, kiểm test và tự giải thích trước khi nhận kết quả.
```

Sau khi dùng, tự làm: kiểm quyền thật của công cụ trước khi gửi; sau đó đọc diff, chạy lại kiểm thử, giải thích thay đổi.

### P11 · Kiểm chứng nguồn

Dùng khi cần kiểm chứng một nhận định về sản phẩm, giá hoặc chính sách trước khi trích dẫn.

```text
Tôi cần kiểm chứng claim sau cho cẩm nang sinh viên CNTT:
[claim cụ thể; ghi rõ sản phẩm, phiên bản, quốc gia nếu liên quan].
Nguồn đang có: [URL và đoạn đã đọc được, hoặc chưa có].
Ưu tiên tài liệu chính thức. Phân biệt nội dung quan sát trực tiếp,
suy luận và phần chưa truy cập được. Ghi URL, ngày đọc, phạm vi áp dụng.
Không dùng một trang giá để suy ra quyền lợi hiện tại của tài khoản tôi.
Không suy quy định môn học TLU từ lời khuyên chung trên mạng.
Không đăng nhập, không đăng ký/mua, không gọi API trả phí hay gửi dữ liệu.
Nếu không đọc được nguồn, nêu rõ hạn chế và câu hỏi cần kiểm tiếp;
không bịa trích dẫn, giá, điều khoản hoặc kết quả kiểm chứng.
```

Sau khi dùng, tự làm: mở lại ít nhất một nguồn chính thức; kiểm xem AI có ghi URL, ngày đọc, phạm vi áp dụng.

---

## BẢNG THUẬT NGỮ

Bảng này giải nghĩa ngắn các thuật ngữ dùng trong cẩm nang, xếp theo bảy nhóm. Mỗi dòng gồm thuật ngữ tiếng Việt, tiếng Anh trong ngoặc và một định nghĩa; dùng để tra cứu, không nhằm học thuộc. Định nghĩa đầy đủ hơn, kèm lưu ý và chỉ dẫn tới từng mục, có trong [Bảng thuật ngữ của Sổ tay thực hành](chapters/glossary.md).

<a id="ai-access"></a>
### AI: vai trò, các thành phần và quyền truy cập — Chương 1, 2, 5

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
### AI: đầu vào, xử lý và độ tin cậy — Chương 1, 3, 5

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
### Môi trường làm việc — Chương 2

- **Môi trường phát triển tích hợp** (IDE): công cụ gộp soạn thảo, chạy, gỡ lỗi và terminal; có AI tích hợp vẫn phải tự kiểm.
- **Terminal, shell, giao diện dòng lệnh** (CLI): cửa sổ nhập lệnh; chương trình thực hiện lệnh (Bash, PowerShell); cách điều khiển bằng lệnh.
- **Thư mục làm việc** (working directory): vị trí gốc để giải đường dẫn tương đối; xem bằng `pwd` hoặc `Get-Location`.
- **Biên dịch, dựng** (compile, build): dịch mã nguồn sang dạng chạy được; build lỗi thì dừng, không dùng tệp thực thi cũ.
- **Mã kết thúc** (exit code): mã chương trình trả về khi kết thúc; `0` thường là thành công nhưng không chứng minh thuật toán đúng.

<a id="code-data"></a>
### Kiểu dữ liệu và tư duy lập trình — Chương 2–3

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
### Web, lưu trữ và ranh giới dữ liệu — Chương 2–4

- **DOM** (Document Object Model): cây đối tượng biểu diễn trang Web để JavaScript đọc và sửa; kiểm thử trong Node.js không xác nhận DOM đúng.
- **`localStorage`**: kho khóa–giá trị dạng chuỗi của trình duyệt; có thể bị chặn hoặc chứa dữ liệu cũ; không phải máy chủ.
- **SQL, truy vấn tham số hóa** (parameterized query): ngôn ngữ dữ liệu quan hệ; truy vấn tham số hóa tách giá trị khỏi câu lệnh.
- **Chèn mã vào lệnh, danh sách cho phép** (injection, allowlist): dữ liệu không đáng tin làm đổi nghĩa câu lệnh; tập giá trị được phép.
- **XSS, `textContent`, `innerHTML`** (cross-site scripting): nội dung không đáng tin bị thực thi trong trang; `textContent` đặt văn bản, `innerHTML` phân tích HTML.

<a id="evidence"></a>
### Kiểm chứng, Git và quyền dùng nguồn — Chương 2–4

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
### Nhãn học tập và hoạt động trong sách

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

Để chuyển "phạm vi", "đóng góp" và "bằng chứng" thành việc làm cụ thể, xem [Thỏa thuận học tập](chapters/learning-agreement.md).
