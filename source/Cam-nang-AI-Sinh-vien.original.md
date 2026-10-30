# HỌC CNTT CÙNG AI

## Hiểu công cụ · Làm chủ kiến thức · Sử dụng có trách nhiệm

**Cẩm nang tự học và tra cứu dành cho sinh viên năm 1–2 Khoa Công nghệ thông tin, Trường Đại học Thủy lợi.**

*Mốc đối chiếu tài liệu sản phẩm và nguồn pháp lý: 29/10/2026. Đây là tài liệu hướng dẫn học tập, không phải quy định chính thức của trường, tài liệu quảng cáo hay tư vấn pháp lý cho một vụ việc cụ thể.*

> **Bạn không cần giỏi lập trình mới bắt đầu được. Nhưng sau mỗi lần nhờ AI, bạn cần hiểu thêm một điều và tự làm được thêm một việc.**

### Câu chuyện của cuốn cẩm nang

Minh học năm nhất. Bạn biết khai báo biến, viết vài vòng lặp C++ nhưng thường thấy thông báo lỗi là muốn chụp màn hình hỏi AI ngay. Lan học năm hai, đã làm quen với cấu trúc dữ liệu, OOP, cơ sở dữ liệu và Web. Bạn có thể nhờ AI tạo giao diện khá đẹp, nhưng khi một chức năng đi qua ba tệp thì chưa biết nên tìm lỗi từ đâu.

Hai bạn cùng làm **ViSinhVien**, một ứng dụng ghi lại các khoản chi tiêu nhỏ. Đây là câu chuyện hư cấu để học; các nhân vật và dữ liệu không đại diện cho sinh viên thật hay kết quả khảo sát tại TLU.

Ta bắt đầu bằng ba khoản rất quen:

| Khoản chi giả | Nhóm | Số tiền lưu trong code | Cách hiển thị |
| --- | --- | ---: | ---: |
| Cơm trưa | Ăn uống | `35000` | 35.000 đ |
| Xe buýt | Đi lại | `7000` | 7.000 đ |
| Vở ghi | Học tập | `18000` | 18.000 đ |
| **Tổng đúng** | | **`60000`** | **60.000 đ** |

Các mức tiền chỉ phục vụ bài tập, **không phải bảng giá thực tế**. Điểm quan trọng là cùng một bộ dữ liệu sẽ đi qua bốn chương, giúp bạn tập trung vào cách suy nghĩ thay vì phải làm quen bài toán mới liên tục.

```text
Một nhu cầu gần gũi: “Hôm nay mình đã chi bao nhiêu?”
                       │
        Chương 1: chọn công cụ và cách dùng vừa túi tiền
                       │
        Chương 2: làm bản C++, rồi theo luồng Web nhiều tệp
                       │
        Chương 3: tự giải thích, sửa và làm bài biến thể
                       │
        Chương 4: kiểm tra quyền dùng, dữ liệu và an toàn
                       │
   Kết quả: một bài học có bằng chứng, không chỉ một màn hình đẹp
```

### Cùng một dự án, hai mức độ

**Đường đi năm nhất:** Bạn làm phần C++ trước. Mục tiêu ban đầu chỉ là đọc dữ liệu mẫu, tính tổng và hiểu vì sao bỏ sót một phần tử lại làm kết quả từ 60.000 thành 42.000. Chưa cần học Web, SQL hay mua API.

**Đường đi năm hai:** Bạn dùng lại ba khoản đó trong một danh sách các đối tượng `Expense`, rồi đọc luồng từ biểu mẫu đến xử lý dữ liệu và hiển thị trên Web. Những vấn đề mới xuất hiện: dữ liệu trong ô nhập là chuỗi, tên trường ở các tệp phải khớp nhau, dữ liệu lưu có thể sai và nội dung người dùng nhập không nên được thực thi như HTML.

**Không cần hoàn thành cả hai đường đi ngay lần đọc đầu.** Những phần nối sang môn chưa học có thể đánh dấu để quay lại. Hiểu chắc một hàm nhỏ có giá trị hơn việc chép toàn bộ một dự án vượt quá khả năng giải thích của mình.

### Những điều đã thống nhất trong bài toán

Trong các ví dụ, số tiền được lưu bằng **số nguyên VND**, không dùng số thập phân để biểu diễn đồng tiền trong phạm vi bài tập. Một khoản chi phải từ 1 đến 1.000.000.000 VND; danh sách có tối đa 500 khoản. Danh sách rỗng hợp lệ và có tổng bằng 0. Khoản chi bằng 0, số âm hoặc vượt giới hạn bị từ chối.

Giới hạn này là **quy ước của bản học tập**, không phải chuẩn cho mọi hệ thống tài chính. Một phần mềm thật còn phải giải quyết nhiều bài toán khác: hoàn tiền, đa tiền tệ, làm tròn, phân quyền, sao lưu, đồng bộ và kiểm toán.

Dữ liệu một khoản chi ở mức Web có dạng:

```json
{
  "id": 1,
  "title": "Cơm trưa",
  "amount": 35000,
  "category": "an-uong"
}
```

`id` là mã nhận diện một khoản; `title` là nội dung; `amount` là số tiền; `category` là nhóm chi. Tên nhóm trong dữ liệu là mã đơn giản như `an-uong`, còn giao diện hiển thị “Ăn uống”. Trong phần tính tổng, điều quan trọng nhất là **mọi nơi cùng dùng trường `amount` và cùng hiểu nó là số nguyên VND**.

### Bạn sẽ làm được gì sau cuốn này?

Đây là mục tiêu của cẩm nang, **không phải hệ thống CLO chính thức của một học phần**.

| Mục tiêu | Học ở đâu? | Bạn chứng minh bằng gì? |
| --- | --- | --- |
| Phân biệt model, provider và ứng dụng | Chương 1 | Điền bảng nhận diện một công cụ và ghi rõ điều chưa xác định. |
| Ước lượng chi phí, chọn cách dùng hợp lý | Chương 1 | Tính lại bài toán token bằng số liệu giả định và giải thích giới hạn của phép so sánh. |
| Cung cấp ngữ cảnh và giao việc trong phạm vi nhỏ | Chương 1–2 | Viết một yêu cầu có mục tiêu, dữ liệu, giới hạn và tiêu chí kiểm tra. |
| Đọc lỗi, đọc thay đổi và kiểm thử kết quả | Chương 2 | Chỉ ra lỗi 42.000/60.000, test rỗng/một phần tử và theo dấu trường `amount`. |
| Học chủ động, không chỉ chép lời giải | Chương 3 | Làm được một bài biến thể khi không mở AI. |
| Giải thích và bảo vệ phần mình thực hiện | Chương 3 | Trả lời được câu hỏi “vì sao?”, “nếu đổi yêu cầu thì sao?”. |
| Bảo vệ dữ liệu, kiểm tra mã và phụ thuộc | Chương 4 | Sửa đúng một tình huống dữ liệu không nên đưa lên AI, một ví dụ hiển thị và một truy vấn SQL. |
| Khai báo hỗ trợ, kiểm tra quyền sử dụng và xử lý sự cố | Chương 4 | Viết bản khai báo trung thực, đánh dấu mục còn phải hỏi giảng viên, mô tả bước xử lý khi key bị lộ. |

### Cách đọc để không bị ngợp

**Trước buổi chia sẻ:** Đọc câu chuyện này, mục 1.1 và bảng nhận diện công cụ. Chọn một câu hỏi thật của mình để mang đến, chẳng hạn: “Em không biết code sai vì kiến thức hay vì cách hỏi AI”. Không cần cài thêm phần mềm chỉ để đọc trước.

**Trong buổi chia sẻ:** Dùng mục lục để theo đúng phần đang trình bày. Trước khi giảng viên chạy một ví dụ, tự dự đoán kết quả. Khi kết quả khác dự đoán, ghi lại chỗ mình hiểu sai; không chỉ chụp ảnh đáp án.

**Sau buổi chia sẻ:** Mỗi lần chọn một nhiệm vụ nhỏ và làm trong khoảng 20–25 phút. Đọc yêu cầu, dự đoán, thử, đối chiếu, rồi viết ba dòng: “Mình đã hiểu… / Mình chưa chắc… / Lần tới mình sẽ…”. Thời lượng là gợi ý tổ chức việc học, không phải tiêu chuẩn đánh giá tốc độ.

Nếu đọc bản HTML, bạn có thể dùng mục lục bên trái, lọc tên mục, tăng cỡ chữ, mở các lời giải khi cần và dùng nút In để lưu PDF từ trình duyệt. Các hình mô phỏng là công cụ học tại chỗ, không gọi AI hay gửi dữ liệu lên mạng. Bản HTML tự chứa phần nội dung và giao diện; chỉ các đường dẫn nguồn tham khảo cần Internet khi bạn bấm mở.

### Dấu hiệu nhận biết các loại nội dung

**Tình huống và hội thoại minh họa:** Được biên soạn để giải thích cách suy nghĩ, không phải bản ghi một sản phẩm đã trả lời đúng như vậy. Không nên lấy một hội thoại minh họa làm bằng chứng năng lực của công cụ.

**Dự kiến đầu ra:** Cho biết điều bạn cần kiểm tra khi chạy ví dụ. Các tệp mẫu đi kèm đã được kiểm tra riêng; điều đó không bảo đảm môi trường trên máy bạn giống môi trường biên soạn.

**Bài có lỗi chủ đích:** Được giữ lại để học cách phát hiện và sửa lỗi. Bản sai không bị xóa hay lặng lẽ thay bằng bản đúng. Ghi lại kết quả sai là một phần của việc học và kiểm thử.

**Thông tin sản phẩm và pháp lý:** Có nguồn để tra lại. Tên nút, quyền lợi gói, giá, điều kiện sinh viên và quy định pháp luật có thể thay đổi. Nếu tài liệu môn học hoặc thông báo chính thức mới hơn khác với ví dụ trong sách, cần kiểm tra và hỏi người phụ trách thay vì tự suy đoán.

### Mở ví dụ nào trước?

| Tệp trong bộ tài liệu | Dùng để làm gì? | Điều kiện |
| --- | --- | --- |
| [Bản Web ViSinhVien](vi-du/nam-2-web/index.html) | Thử thêm khoản giả, xem tổng, kiểm tra dữ liệu nhập và hiển thị văn bản. | Trình duyệt hiện đại; giữ `index.html`, `data.js`, `app.js` trong cùng thư mục. Không cần Internet hay tài khoản AI. |
| [C++ có lỗi chủ đích](vi-du/nam-1-cpp/loi-bo-sot.cpp) | Quan sát tổng 42.000 thay vì 60.000. | Trình biên dịch C++17 như g++; nếu chưa có, đọc trace trong Chương 2 trước. |
| [C++ đúng và có kiểm thử](vi-du/nam-1-cpp/vi_sinh_vien.cpp) | Đối chiếu bản sửa và các test giới hạn. | C++17; hướng dẫn lệnh ở Chương 2. |
| [Kiểm thử dữ liệu Web](vi-du/nam-2-web/test_data.cjs) | Chạy test hàm xử lý dữ liệu, không mở trình duyệt. | Node.js hiện đại; không cần `npm install`. |
| [Minh họa SQLite riêng](vi-du/minh-hoa-sqlite.py) | Xem truy vấn có tham số và kiểm tra dữ liệu bằng CSDL trong bộ nhớ. | Python 3 có mô-đun `sqlite3`; không phải backend của bản Web. |

**Lưu ý về dữ liệu Web:** `localStorage` là nơi lưu dữ liệu trong trình duyệt, không phải cơ sở dữ liệu máy chủ. Nếu trình duyệt chặn lưu khi mở tệp cục bộ hoặc dữ liệu cũ không hợp lệ, bản demo báo rõ và dùng bộ nhớ tạm. Không nhập dữ liệu cần giữ lâu dài, sao kê thật hay thông tin cá nhân vào bản học tập này.

Bạn không cần trả tiền cho AI để chạy các tệp ví dụ. Những phần hỏi Qoder hoặc công cụ AI cần quyền truy cập dịch vụ tương ứng, và điều kiện của tài khoản có thể khác nhau. Nếu chưa có quyền dùng, bạn vẫn có thể học bằng đề bài, trace và đáp án minh họa trong sách.

### Hộp từ mới: tra nhanh trước khi đọc tiếp

Cẩm nang cố gắng giải thích từ mới ngay tại chỗ dùng. Bảng dưới gom lại những từ dễ gây nghẽn nhất cho người đọc năm nhất, kèm chỗ nó xuất hiện để bạn quay lại đọc đầy đủ. Đây là cách nói gọn để hiểu bài, không phải định nghĩa chuẩn trong giáo trình chuyên ngành.

| Từ | Hiểu gọn | Gặp ở đâu |
| --- | --- | --- |
| model, provider, ứng dụng | Model là phần sinh ra câu trả lời; provider là nơi cung cấp quyền gọi model; ứng dụng là thứ bạn bấm trên máy. | 1.1 |
| token | Đơn vị văn bản mà dịch vụ AI tách dữ liệu ra để xử lý và để đếm lượng vào – ra; không bằng một từ hay một chữ cái. | 1.2 |
| số nguyên an toàn | Khoảng số nguyên JavaScript còn tính chính xác từng đơn vị, tới 9007199254740991; vượt mốc đó phép cộng có thể lệch lặng lẽ. | 1.2, 2.5 |
| terminal, shell, CLI | Terminal là ô nhập lệnh bằng chữ; shell là chương trình đọc lệnh đó; CLI là cách dùng công cụ qua lệnh thay vì bấm nút. | 2.2 |
| thư mục làm việc | Vị trí hiện tại của terminal; nó quyết định đường dẫn tương đối trong lệnh chạy đúng hay sai. Xem bằng `pwd`, PowerShell là `Get-Location`. | Đầu chương 2, 2.6 |
| biên dịch (compile) | Bước dịch mã C++ thành tệp chạy được. Sửa mã mà chưa biên dịch lại thì tệp đang chạy vẫn là bản cũ. | 2.4 |
| kiểu không dấu, tràn giá trị | Kiểu số chỉ chứa giá trị không âm; lấy `0 - 1` trên kiểu đó không ra `-1` mà vòng về một số rất lớn. | 2.4 |
| diff | Bảng so sánh trước – sau của một tệp, cho thấy đúng những dòng được thêm, bớt hay đổi. | 2.4, 2.7 |
| exit code | Con số chương trình trả về khi kết thúc; `0` thường là chạy xong không báo lỗi, khác `0` là có lỗi. | 2.6 |
| DOM | Cây các thành phần của trang Web mà JavaScript đọc và sửa được. | 2.6, 4.3 |
| origin | Bộ ba giao thức, tên miền và cổng của một địa chỉ Web; trình duyệt dựa vào đó để tách dữ liệu lưu trữ giữa các trang. | 3.6 |
| fixture | Dữ liệu giả dựng riêng cho một phép kiểm tra, không trộn vào bộ dữ liệu mẫu chính. | 4.3 |
| registry | Kho công khai liệt kê các gói thư viện và phiên bản của chúng. | 4.3 |
| lockfile | Tệp ghi cố định phiên bản gói đã chọn, giúp lần cài sau giống lần trước. | 4.3 |
| commit, clone, ép đẩy | Commit là một lần ghi mốc thay đổi; clone là bản sao kho mã; ép đẩy là ghi đè lịch sử trên kho chung — việc cẩm nang này không hướng dẫn tự làm. | 4.6 |
| CLO | Chuẩn đầu ra của một học phần, do đề cương môn công bố. Mục tiêu trong cẩm nang không thay thế CLO. | Mở đầu, đầu mỗi chương |

Nếu một từ chưa có trong bảng và cũng chưa được giải thích tại chỗ, hãy ghi vào vở rồi hỏi lại trong buổi chia sẻ. Đoán nghĩa rồi dùng tiếp là cách dễ nhất để hiểu sai cả mục.

> **Thỏa thuận học tập**
>
> AI có thể giúp giải thích, tạo giả thuyết, đề xuất code và kiểm tra. Bạn giữ quyền quyết định mục tiêu, phạm vi, điều gì được phép chia sẻ và khi nào bằng chứng đã đủ. Đừng nhầm “AI đã làm xong” với “mình đã học xong”.


---

## CHƯƠNG 1. BẢN ĐỒ AI VÀ TÚI TIỀN SINH VIÊN

Minh là sinh viên năm nhất CNTT, vừa học mảng và vòng lặp C++. Minh có thể chép một chương trình chạy được, nhưng vẫn lúng túng khi giải thích vì sao vòng lặp dừng. Lan học năm hai, đang nối kiến thức lập trình hướng đối tượng (OOP), cấu trúc dữ liệu và giải thuật (DSA), cơ sở dữ liệu (CSDL) với Web. Hai bạn cùng làm **ViSinhVien**, một bài tập quản lý chi tiêu bằng dữ liệu giả.

Chúng ta sẽ theo hai bạn từ câu hỏi “mình đang dùng AI gì?” đến quyết định “việc này có cần trả tiền không?”. Mục tiêu không phải nhớ tên các hãng. Sau chương, bạn cần mô tả đúng công cụ, đưa đủ thông tin cho AI, kiểm tra một lời giải và ước tính chi phí trước khi dùng dịch vụ có tính tiền.

> **Quy ước xuyên suốt chương**
>
> Dữ liệu mẫu là **Cơm trưa: 35000 VND; Xe buýt: 7000 VND; Vở ghi: 18000 VND**. Tổng đúng là **60000 VND**; lỗi bỏ khoản cuối cho **42000 VND**. Mỗi `amount` là số nguyên VND, lớn hơn 0 và không quá 1000000000; danh sách tối đa 500 khoản. Danh sách rỗng có tổng bằng 0.
>
> Minh làm bản C++; Lan phát triển bài tập Web bằng HTML và JavaScript, lưu trong `localStorage`. Không có backend, đăng nhập, kết nối ngân hàng hay tài chính thật. Các câu trả lời AI minh họa trong chương do tác giả biên soạn, không phải kết quả đo sản phẩm. Không cần đăng ký, cài đặt, tạo khóa hay gọi API thật để học chương này.

### 1.1. Model, provider và ứng dụng: đọc đúng bản đồ trước khi chọn đường

#### 1.1.1. Một câu nói có thể đang chỉ ba thứ khác nhau

Minh nói: “Mình dùng ChatGPT sửa ViSinhVien.” Lan hỏi: “Model nào?”. Minh trả lời: “Thì ChatGPT!”. Minh mới nêu tên sản phẩm, chưa xác định mô hình xử lý lượt hỏi.

**AI**, trí tuệ nhân tạo, là lĩnh vực rộng, gồm cả nhận diện vật thể hay phát hiện bất thường. Chương tập trung vào **AI tạo sinh**, những hệ thống tạo nội dung như văn bản, mã nguồn. **LLM**, mô hình ngôn ngữ lớn, thường gặp trong trợ lý học tập. Không phải mọi AI đều là chatbot; khả năng nhận ảnh, âm thanh hoặc tệp tùy model.

**Model là mô hình tính toán đã được huấn luyện để xử lý đầu vào và tạo đầu ra**. Minh đưa đề, C++ và câu hỏi để nhận gợi ý vòng lặp. Gợi ý mạch lạc không bảo đảm chương trình đúng yêu cầu; vẫn cần kiểm chứng.

Các tên GPT, Claude, Gemini có thể chỉ **họ mô hình**, gồm nhiều phiên bản hoặc biến thể. Biết họ chưa chắc biết model cụ thể. Tài liệu [Anthropic về các mô hình Claude](https://docs.anthropic.com/en/docs/about-claude/models/overview), theo nguồn đối chiếu truy cập ngày **29/10/2026**, phân biệt các model và định danh của chúng. Chúng ta dùng nguồn để hiểu cách nhận diện, không chốt một danh sách phiên bản “mới nhất” cho cả học kỳ.

#### 1.1.2. Provider là đường truy cập, không nhất thiết là bên tạo model

**Provider**, trong chương này, là bên cung cấp dịch vụ truy cập đến một hay nhiều model. Dịch vụ tiếp nhận yêu cầu, xác thực quyền dùng và áp dụng điều kiện sử dụng. Provider có thể trực tiếp vận hành mô hình hoặc làm trung gian kết nối đến bên vận hành khác. Câu hỏi cần đặt là: “Trong đường truy cập đang xét, ai cung cấp dịch vụ cho ứng dụng?”.

Câu đó khác với “Ai phát triển model?”. Bên phát triển, đôi khi gọi là **producer**, xây dựng, huấn luyện hoặc phát hành mô hình. Một tổ chức có thể đồng thời phát triển model và cung cấp dịch vụ, nhưng hai vai trò không buộc phải trùng nhau.

Ví dụ, Anthropic phát triển Claude; Claude cũng được cung cấp qua Amazon Bedrock. Nếu một trợ lý lập trình giả định của Lan dùng Claude qua Bedrock, Anthropic là bên phát triển model, còn AWS cung cấp đường truy cập qua dịch vụ Bedrock trong tình huống này. Quan hệ đó được minh họa tại [AWS: Claude trong Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), nguồn truy cập ngày **29/10/2026**. Vì vậy, nhãn “có Claude” chưa chứng minh ứng dụng kết nối trực tiếp đến Anthropic.

##### API và khóa truy cập nằm ở đâu?

**API** là giao diện để các phần mềm giao tiếp theo quy tắc xác định. Khi chat, Minh gõ rồi bấm gửi. Khi dùng API, chương trình gửi yêu cầu theo định dạng dịch vụ quy định. API không phải một model mới. [Tài liệu Gemini API](https://ai.google.dev/gemini-api/docs), nguồn truy cập ngày **29/10/2026**, minh họa việc chương trình chỉ định model rồi gửi nội dung cần xử lý.

**API key** là một dạng thông tin xác thực; không phải “bộ não AI riêng” tải về máy. Một số dịch vụ dùng cách xác thực khác. Có key cũng không đồng nghĩa có quyền dùng mọi model, quota vô hạn hoặc miễn phí. Quyền và cách tính tiền phụ thuộc dịch vụ cùng cấu hình tài khoản.

> **Dừng trước khi chia sẻ khóa**
>
> Không đưa API key thật vào chat, nhóm lớp, ảnh chụp màn hình hay kho mã công khai. Đặc biệt, không nhúng khóa bí mật vào JavaScript phía trình duyệt của ViSinhVien: người dùng có thể đọc mã đó. Bài tập này không cần khóa và không tích hợp API.

#### 1.1.3. Ứng dụng là nơi bạn thao tác và nơi tổ chức công việc

**Ứng dụng**, hay application, là phần mềm người dùng trực tiếp tương tác: trang chat, ứng dụng điện thoại, phần mềm máy tính hoặc trợ lý trong môi trường lập trình. Ứng dụng cung cấp ô nhập, lịch sử, nút đính kèm; có thể chọn thông tin gửi đi, kết nối tìm kiếm hoặc hiển thị bản sửa mã để người dùng duyệt.

Google dùng tên Gemini cho cả trải nghiệm ứng dụng và họ mô hình. [Trang tổng quan ứng dụng Gemini](https://gemini.google/overview/), nguồn truy cập ngày **29/10/2026**, giúp phân biệt giao diện người dùng với các mô hình nền tảng. “Tôi mở Gemini trên điện thoại”, “tôi gọi Gemini API” và “model thuộc họ Gemini” là ba phát biểu ở những lớp khác nhau, không nên dùng thay thế tùy tiện.

Một ứng dụng đôi khi được gọi là **wrapper**, phần mềm bao quanh model hoặc API. Tuy nhiên, kết luận “chỉ là cái vỏ nên không có giá trị” bỏ qua công việc tổ chức thông tin và quy trình. Với Minh, một trợ lý chỉ hỏi gợi mở có thể hữu ích hơn trợ lý lập tức viết hộ toàn bộ bài. Với Lan, công cụ chọn đúng tệp và cho xem phần thay đổi có thể giảm lỗi sửa lan sang chức năng khác.

Đừng suy ngược rằng mọi ứng dụng AI đều đọc tệp, chạy code hoặc lên mạng. Chức năng phụ thuộc sản phẩm, cấu hình, môi trường và quyền được cấp. Một giao diện đẹp không chứng minh nó kiểm thử được; một ứng dụng cài trên máy vẫn có thể gửi dữ liệu lên đám mây.

| Vai trò | Câu hỏi nhận diện | Trong tình huống trợ lý giúp sửa ViSinhVien |
| --- | --- | --- |
| Model | Thành phần nào sinh lời gợi ý? | Model được cấu hình để xử lý yêu cầu; có thể chưa xác định. |
| Provider | Ai cung cấp đường truy cập đến model? | Dịch vụ trực tiếp hoặc trung gian được ứng dụng sử dụng. |
| Ứng dụng | Minh hoặc Lan mở và thao tác ở đâu? | Trang chat hoặc trợ lý lập trình đang dùng. |
| Bên phát triển model | Ai xây dựng hoặc phát hành mô hình? | Có thể khác provider; đây là câu hỏi bổ sung, không phải ứng dụng. |

**Ba vai trò model, provider, application không phải ba công ty.** Một công ty có thể đảm nhận nhiều vai trò; một ứng dụng có thể kết hợp nhiều dịch vụ. ViSinhVien hiện là bài tập không tích hợp AI: trợ lý giúp viết nó là ứng dụng AI, còn ViSinhVien không tự trở thành ứng dụng AI chỉ vì mã được AI gợi ý.

Có thể nhớ gần đúng: model như động cơ, ứng dụng như chiếc xe có bộ điều khiển, provider như bên cung cấp dịch vụ vận hành. Nhưng API không phải “xăng”, provider không đơn thuần là “trạm xăng”; một hệ thống có thể dùng nhiều model. Phép so sánh chỉ để nhớ vai trò, không thay thế sơ đồ kỹ thuật.

#### 1.1.4. Theo một lỗi 42000 VND qua các lớp

Minh đã có ba khoản mẫu, nhưng chương trình bỏ khoản cuối. Đoạn dưới đây **chính là tệp `vi-du/nam-1-cpp/loi-bo-sot.cpp`** đi kèm cẩm nang, rút bớt dòng chú thích; các số tiền đã được giả định hợp lệ. Nó chưa chứa phần nhập và kiểm tra dữ liệu của sản phẩm.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<long long> amounts = {35000, 7000, 18000};
    long long total = 0;
    int n = static_cast<int>(amounts.size());
    for (int i = 0; i < n - 1; ++i) {
        total += amounts[i];
    }
    std::cout << "Tong chi tieu: " << total << " VND\n";
    return 0;
}
```

**Kết quả quan sát khi chạy bản đã biên dịch:**

```text
Tong chi tieu: 42000 VND
```

Chuỗi in ra không có dấu tiếng Việt để tránh lỗi hiển thị trên một số terminal. `static_cast<int>` chỉ là cách nói “đổi kích thước danh sách sang số nguyên có dấu để so sánh cho rõ ràng”; bạn chưa cần hiểu sâu phần này để theo bài.

Minh gửi yêu cầu: “Tôi cần cộng tất cả khoản chi. Ba khoản 35000, 7000, 18000 phải ra 60000 nhưng đang ra 42000. Hãy gợi ý một bước, chưa viết lại code.” Luồng vai trò giản lược như sau:

```text
Minh: mục tiêu + mã + kết quả sai
                 |
                 v
Ứng dụng: chọn và chuẩn bị thông tin
                 |
                 v
Provider: tiếp nhận yêu cầu hợp lệ
                 |
                 v
Model: tạo gợi ý từ thông tin nhận được
                 |
                 v
Ứng dụng hiển thị -> Minh kiểm tra lại
```

Mỗi ô không nhất thiết là một máy chủ riêng. Hệ thống thực tế có thể thêm dịch vụ trung gian, công cụ hoặc nhiều lượt xử lý. Với model chạy cục bộ, có thể không có provider bên ngoài nhận câu hỏi; không nên áp sơ đồ đám mây cho mọi trường hợp.

Một gợi ý minh họa là: “Khi `i = 2`, điều kiện `i < n - 1` có đúng không?”. Ở đây `n` bằng 3. Minh lập bảng thay vì chỉ tin lời AI:

| `i` được xét | Điều kiện `i < n - 1` tức `i < 2` | Hành động | Tổng sau bước |
| --- | --- | --- | --- |
| 0 | `0 < 2`, đúng | Cộng 35000 | 35000 |
| 1 | `1 < 2`, đúng | Cộng 7000 | 42000 |
| 2 | `2 < 2`, sai | Dừng, không cộng 18000 | 42000 |

Mảng có ba phần tử dùng chỉ số 0, 1, 2. Sửa điều kiện thành `i < n` sẽ cho cả ba chỉ số đi qua, còn `i = 3` bị chặn. Không sửa máy móc thành `i <= n`: khi ấy có nguy cơ truy cập chỉ số bằng kích thước, nằm ngoài mảng. Cách sửa này được dùng lại nguyên văn ở mục 2.8.1 và trong tệp đúng `vi_sinh_vien.cpp`.

Với danh sách rỗng, `n` bằng 0 nên vòng lặp không chạy lượt nào; tổng khởi tạo 0 giữ nguyên. Dùng `long long` cho tổng giúp chứa mức lớn nhất 500 × 1000000000 = 500000000000 VND, vượt phạm vi số nguyên có dấu 32 bit thường gặp — tức kiểu `int` thông dụng chỉ chứa khoảng ±2,1 tỷ, không đủ cho con số trên. Phân tích này xuất phát từ yêu cầu dữ liệu, không từ lời khẳng định “code tối ưu” của AI.

#### 1.1.5. Cùng model vẫn có thể trả lời khác

Lan đưa đúng câu hỏi của Minh vào một trợ lý trong trình soạn mã. Trợ lý đó gợi ý giữ dữ liệu trong trình duyệt; trang chat khác lại đề xuất máy chủ. Chưa thể kết luận bên nào dùng model giả. Cần xem **thông tin thực sự được gửi**, không chỉ câu vừa gõ.

Ứng dụng thứ nhất có thể nhận thêm brief “HTML, JavaScript, localStorage, không backend”. Ứng dụng thứ hai chỉ thấy “làm ứng dụng quản lý chi tiêu”. Cùng model, hai đầu vào khác nhau có thể dẫn đến hai hướng giải khác nhau. Lịch sử, tài liệu được chọn và đoạn code đính kèm đều có ảnh hưởng.

Chỉ dẫn của ứng dụng cũng khác: một nơi đóng vai gia sư, một nơi ưu tiên tạo mã hoàn chỉnh. Công cụ có thể khác: một nơi thực thi được kiểm thử, nơi khác chỉ sinh văn bản. Cuối cùng, giới hạn đầu ra, chế độ xử lý và tính không tất định của quá trình sinh có thể làm hai lượt trả lời khác nhau ngay cả khi đầu vào gần giống.

> **Hai loại bằng chứng không giống nhau**
>
> “Tôi nghĩ code đúng” là nhận định. “Tôi chạy lệnh này, với dữ liệu này, nhận kết quả này” là thông tin về kiểm thử, còn cần kiểm tra tính xác thực và độ bao phủ. Một vài test qua không chứng minh chương trình đúng với mọi đầu vào.

#### 1.1.6. Nhận diện có giới hạn là một kỹ năng

Nếu giao diện chỉ ghi “Tự động”, hãy ghi **“chưa xác định model thực sự xử lý lượt này”**. Nếu chỉ thấy tên họ model, ghi tên họ và phần chưa biết. Đừng suy model từ văn phong hoặc hỏi chatbot tự giới thiệu rồi coi đó là bằng chứng duy nhất. Hệ thống có thể định tuyến nhiều thành phần cho tìm kiếm, đọc tệp và sinh câu trả lời.

Thử tình huống trên giấy: ứng dụng giả định “Gia sư ViSinhVien” do một nhóm xây dựng, tài liệu nói dùng Gemini API với model được chỉ định trong cấu hình, nhưng không công bố định danh. Đáp án: ứng dụng là Gia sư ViSinhVien; họ model là Gemini; model cụ thể chưa xác định; provider của đường truy cập đã nêu là Google qua Gemini API. Nhóm viết ứng dụng không vì vậy trở thành bên huấn luyện model.

Nếu đổi thành Claude qua Bedrock, bên phát triển là Anthropic, provider đường truy cập là AWS qua Bedrock. Nếu đề chỉ nói “hỗ trợ Claude”, chưa đủ xác định provider hoặc phiên bản. Đó không phải làm bài thiếu; đó là không bịa dữ kiện.

Trước khi chuyển mục, Minh tự chốt: model không tự thấy mọi tệp trên máy, ứng dụng cài cục bộ không bảo đảm dữ liệu ở cục bộ, model giỏi không bảo đảm người dùng học tốt. Minh chỉ thực sự hiểu lỗi khi tự giải thích được khoản 18000 bị bỏ ở bước nào và kiểm tra được một danh sách khác.

### 1.2. Prompt, token và context: đưa đúng bài thay vì bắt AI đoán

#### 1.2.1. Prompt là yêu cầu; context là thông tin model thực sự nhận

**Prompt** là yêu cầu hoặc chỉ dẫn đưa cho hệ thống. **Context**, ngữ cảnh, là thông tin nhận được để xử lý một lượt: prompt, lịch sử đã chọn, tài liệu, mã và kết quả công cụ. Theo cách dùng phổ biến, prompt là một phần của context.

Minh chỉ viết “Sửa vòng lặp này”. AI có thể đoán khoản cuối cố tình bị bỏ vì đang chờ xác nhận, hoặc viết lại bằng kỹ thuật Minh chưa học. Lan hỏi “Làm app ví sinh viên chuyên nghiệp” thì có thể nhận đề xuất đăng nhập, backend, thanh toán. Đáp án trôi chảy vẫn sai bài khi mục tiêu chưa rõ.

> **Yêu cầu thiếu và hậu quả minh họa**
>
> Prompt: “ViSinhVien tính sai, sửa cho chuẩn.”
>
> Câu trả lời có thể gặp: “Hãy làm tròn về hai chữ số thập phân và đồng bộ dữ liệu lên máy chủ.”
>
> Sai hướng vì bài dùng số nguyên VND, không có backend. Chưa có code, dữ liệu và kết quả mong đợi để xác định lỗi. Nghe chuyên nghiệp không bù được việc thiếu đề.

Prompt tốt cần đủ thông tin, không nhất thiết dài. Đoạn vòng lặp, mục tiêu 60000 và lỗi 42000 hữu ích hơn lời “hãy đóng vai chuyên gia hàng đầu”.

#### 1.2.2. Mẫu brief đủ dùng cho cả Minh và Lan

**Brief** là bản mô tả ngắn về việc cần làm. Minh và Lan thống nhất bản dưới đây làm nguồn yêu cầu chung. Khi chuyển sang tác vụ mới, hai bạn giữ phần ràng buộc và thay phần việc cần hỗ trợ, thay vì kể lại dự án theo trí nhớ.

```text
DỰ ÁN: ViSinhVien, bài tập với dữ liệu giả.
NGƯỜI HỌC: Minh năm 1 đang học C++; Lan năm 2 học OOP/DSA/CSDL/Web.
MỤC TIÊU: lưu danh sách khoản chi và tính tổng tất cả khoản hợp lệ.
DỮ LIỆU: mỗi khoản có tên và amount là số nguyên VND.
RÀNG BUỘC: 0 < amount <= 1000000000; tối đa 500 khoản.
TRƯỜNG HỢP RỖNG: tổng bằng 0.
VÍ DỤ: Cơm trưa 35000; Xe buýt 7000; Vở ghi 18000.
KẾT QUẢ ĐÚNG: 60000 VND; lỗi đang quan sát là 42000 VND.
C++: không dùng kiểu tổng có thể tràn ở 500000000000.
WEB: HTML + JavaScript + localStorage; không backend, không đăng nhập.
PHẠM VI: không dữ liệu tài chính thật, không kết nối ngân hàng hoặc API AI.
VIỆC LẦN NÀY: tìm lỗi bỏ khoản cuối trong code tôi đính kèm.
CÁCH GIÚP: gợi ý một bước trước; nếu thiếu dữ kiện thì hỏi, không tự thêm tính năng.
ĐẦU RA: chỉ vị trí nghi vấn, giải thích cho người mới, đề xuất test và kết quả mong đợi.
BẰNG CHỨNG: phân biệt suy luận với kết quả đã thực thi; không nói đã chạy nếu chưa chạy.
```

Brief không bảo đảm AI luôn đúng. “Việc lần này” giới hạn tác vụ; “cách giúp” giữ Minh tự học; “bằng chứng” làm rõ phần đã kiểm chứng.

Lan học OOP thì hỏi cách tách trách nhiệm xác thực và tính tổng; học DSA thì xét duyệt tối đa 500 phần tử. Với CSDL, cô tập xác định thuộc tính, ràng buộc trên giấy, không đưa hệ quản trị CSDL vào Web. Đổi góc học không đồng nghĩa mở rộng sản phẩm.

#### 1.2.3. Token: đơn vị xử lý và tính dùng, không phải số từ tiếng Việt

**Token** là đơn vị mà hệ thống tách dữ liệu thành để xử lý. Một từ có thể tương ứng một hoặc nhiều token; dấu câu, khoảng trắng, mã nguồn, ngôn ngữ và bộ tách token đều ảnh hưởng. Không dùng quy tắc cố định như “một từ tiếng Việt luôn bằng một token” hoặc một hệ số duy nhất áp cho mọi model.

Số từ của chương sách có thể đếm bằng cách tách khoảng trắng. Số đó không phải hóa đơn token. Muốn dự toán dịch vụ cụ thể, xem bộ đếm hoặc công cụ ước tính phù hợp của provider, rồi đối chiếu báo cáo usage thực tế nếu sau này được phép dùng. Nội dung ảnh, âm thanh hoặc cơ chế đặc thù có thể có cách tính khác; chương chỉ dùng ví dụ văn bản giả định.

**Context window**, cửa sổ ngữ cảnh, là giới hạn lượng thông tin model có thể xử lý trong một lần theo quy định của dịch vụ. Nhiều hệ thống còn có giới hạn đầu ra riêng. Không hiểu “cửa sổ lớn” thành quyền gửi mọi thứ vô hạn, hoặc bảo đảm từng chi tiết trong tài liệu dài đều được dùng chính xác.

Lan dán cả lịch sử dự án, bài giảng cũ, lỗi đã sửa và những phương án bị bỏ. Lúc đó brief ngắn quan trọng có thể bị chìm. Khi hội thoại dài, ứng dụng có thể cắt bớt, tóm tắt hoặc chọn một phần lịch sử; không nên mặc định mọi câu từ đầu buổi còn nguyên trong context. Cách sửa là giữ bản yêu cầu hiện hành ngắn và nhắc lại những ràng buộc quyết định.

```text
Ổ đĩa của Lan                       Context của một lượt
+--------------------------+        +--------------------------+
| Nhiều dự án, ảnh, dữ liệu |        | Brief ViSinhVien          |
| Tệp riêng tư             |  chọn  | Hàm tính tổng liên quan   |
| Mã ViSinhVien            | -----> | Ba khoản giả + test rỗng  |
| Tài liệu môn học         |        | Lỗi hiện tại              |
+--------------------------+        +--------------------------+
Không mặc định gửi tất cả.          Chỉ phần cần và được phép.
```

Context không phải cả ổ đĩa. Model không tự biết tệp đã sửa sau lượt trước nếu ứng dụng không gửi bản mới. Ngược lại, một trợ lý có quyền đọc dự án có thể lấy thêm nội dung tùy cách hoạt động. Cần kiểm tra phạm vi quyền, tệp đính kèm và thông tin sản phẩm, thay vì đoán từ giao diện.

#### 1.2.4. Huấn luyện, suy luận và tìm web không phải một việc

**Training**, huấn luyện, là quá trình dùng dữ liệu và thuật toán để điều chỉnh tham số mô hình. **Inference**, suy luận ở đây, là quá trình dùng mô hình đã có để tạo đầu ra từ đầu vào. Khi Minh gửi ba khoản chi, hệ thống có thể dùng chúng trong context để trả lời; điều đó không tự chứng minh model đã được huấn luyện lại và sẽ nhớ ba khoản ấy cho mọi người dùng về sau.

Tuy nhiên, “không huấn luyện lại ngay khi bấm gửi” không đồng nghĩa “dữ liệu không được lưu hoặc không bao giờ được dùng cải thiện dịch vụ”. Lưu lịch sử, tính năng bộ nhớ của ứng dụng, nhật ký vận hành và việc dùng dữ liệu cho cải thiện là những vấn đề riêng. Chính sách sản phẩm và cài đặt quyết định; sẽ cần đọc kỹ ở mục 1.4.

**Web search** là tìm kiếm thông tin qua công cụ kết nối web, nếu ứng dụng có chức năng và lượt làm việc sử dụng nó. Model không mặc nhiên lên mạng chỉ vì bạn hỏi một câu về hôm nay. Câu trả lời về học bổng hoặc quyền lợi sinh viên có thể dựa trên kiến thức cũ nếu không có truy xuất nguồn mới.

Với lỗi cộng tiền, không cần tìm web để biết 35000 + 7000 + 18000. Với điều kiện ưu đãi sinh viên, lại cần nguồn chính thức còn hiệu lực. Hai việc cần hai cách kiểm chứng khác nhau: phép tính và test cho code; tài liệu có nguồn, phạm vi và ngày truy cập cho chính sách.

#### 1.2.5. Hallucination: lời có vẻ đúng nhưng thiếu cơ sở

**Hallucination**, thường gọi là ảo giác AI, là nội dung sai hoặc không có căn cứ nhưng được trình bày như đúng. Trong ViSinhVien, đó có thể là khẳng định JavaScript tự lưu mọi biến vào `localStorage`, bịa ra một hàm C++ không tồn tại, hoặc nói đã chạy chương trình khi chỉ đọc văn bản.

Đừng chữa bằng câu “hãy chắc chắn 100%”. Hãy đổi yêu cầu thành thứ kiểm tra được. Với sửa vòng lặp, yêu cầu liệt kê chỉ số được duyệt và dự đoán kết quả ở danh sách rỗng, một khoản, ba khoản. Với Web, hỏi “tệp nào đọc dữ liệu đã lưu, lúc nào ghi lại, khi dữ liệu hỏng thì báo gì?”. Những câu đó buộc lời giải gắn vào hành vi cụ thể.

Đây là **bảng đầu ra mong đợi**, không phải báo cáo đã chạy thử:

| Tình huống | Đầu vào hoặc trạng thái | Kết quả cần có |
| --- | --- | --- |
| Không có khoản chi | Danh sách rỗng | Tổng 0 VND |
| Một khoản | 7000 | Tổng 7000 VND |
| Dữ liệu xuyên suốt | 35000, 7000, 18000 | Tổng 60000 VND |
| Sát giới hạn | 500 khoản, mỗi khoản 1000000000 | Tổng 500000000000 VND |
| Số tiền không hợp lệ | 0, số âm, 1.5 hoặc lớn hơn 1000000000 | Từ chối khoản không hợp lệ, không âm thầm làm tròn |
| Vượt số lượng | Thêm khoản thứ 501 | Từ chối thêm; giữ danh sách hợp lệ trước đó |

Lan dùng `Number` của JavaScript có thể biểu diễn chính xác các số nguyên trong phạm vi tổng đang xét, vì 500000000000 nhỏ hơn giới hạn số nguyên an toàn 9007199254740991 — đây là mốc mà JavaScript còn bảo đảm mỗi số nguyên được lưu đúng từng đơn vị, vượt mốc đó phép cộng có thể lệch. Nhưng vẫn phải kiểm tra `amount` là số nguyên đúng phạm vi; một ô nhập trên Web không tự bảo đảm mọi dữ liệu đã lưu hợp lệ. `localStorage` lưu chuỗi, nên việc đọc lại cần phân tích và kiểm tra cấu trúc dữ liệu.

#### 1.2.6. Có trích dẫn vẫn phải kiểm tra trích dẫn

Một liên kết có thật chưa chắc hỗ trợ kết luận. Nếu AI nói “sinh viên được miễn phí toàn bộ dịch vụ”, Minh cần: khoanh phát biểu; mở nguồn tìm đoạn chứng minh; đối chiếu phạm vi ứng dụng/API và điều kiện. Ngày truy cập không phải ngày phát hành chính sách.

Nguồn nói “đủ điều kiện nộp hồ sơ” không có nghĩa “email trường tự được duyệt”. Không tìm được căn cứ thì ghi chưa xác minh.

**Tự kiểm tra:** Gửi cả ổ đĩa để đủ context? Không. Gõ prompt là huấn luyện lại ngay? Không. Câu “đã chạy” tự đủ bằng chứng? Không. Prompt dài không thay thế ba kiểm tra đó.

### 1.3. Free, thuê bao và API pay-as-you-go: tính tiền trước khi bấm nhiều lần

#### 1.3.1. Ba cách sử dụng, ba câu hỏi về quyền lợi

Minh thấy nút miễn phí, Lan nghe về thuê bao, bạn khác bảo “API rẻ hơn”. Đừng chọn chỉ từ nhãn: hãy hỏi được dùng gì, giới hạn ra sao và phần nào phát sinh tiền.

| Cách dùng | Cách hiểu nhập môn | Cần kiểm tra trước |
| --- | --- | --- |
| Free | Có phạm vi sử dụng không thu tiền theo điều kiện dịch vụ | Model, tính năng, giới hạn dùng, dữ liệu và điều kiện tài khoản |
| Subscription, thuê bao | Trả khoản định kỳ cho quyền lợi của một sản phẩm hoặc gói | Quota, tính năng, thời hạn, gia hạn, giới hạn và các khoản ngoài gói |
| API pay-as-you-go | Chương trình gọi dịch vụ; tiền phụ thuộc mức dùng và bảng giá | Đơn vị tính, input/output, công cụ, hạn mức, xác thực và kiểm soát chi phí |

Free không có nghĩa vô hạn, và trả tiền không có nghĩa mọi yêu cầu đều được phục vụ không giới hạn. Một gói có thể giới hạn lượt, tốc độ, loại tính năng hoặc lượng dùng. **Quota** là hạn mức theo một đơn vị và khoảng thời gian xác định; cần đọc cả đơn vị, không chỉ con số.

Quyền sử dụng ứng dụng và quyền sử dụng API cần được phân biệt. Không lấy biên lai thuê bao chat làm bằng chứng API của mọi dịch vụ đã được thanh toán. Tuy vậy, cũng không viết “thuê bao không bao giờ gồm API”: một số gói đủ điều kiện có credit API tích hợp. [Hướng dẫn về credit ChatGPT/API](https://developers.openai.com/api/docs/guides/chatgpt-api-credits), theo nguồn nghiên cứu truy cập ngày **29/10/2026**, cho thấy cần kiểm tra quyền lợi cụ thể. **Credit** là khoản giá trị hoặc lượng dùng được cấp theo điều kiện, có thể có hạn dùng và phạm vi áp dụng.

Với một dịch vụ khác, [bảng giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing), nguồn truy cập ngày **29/10/2026**, là nơi đọc mức free/paid theo model và điều kiện. Chương không lấy tên hay giá thực trên trang làm số liệu bài toán. Khi đọc, phải nhìn đơn vị, đầu vào, đầu ra, loại xử lý và ghi chú; đừng chỉ chụp ô giá thấp nhất.

#### 1.3.2. Bài toán ngân sách hoàn toàn giả định

Lan muốn biết 50 lượt nhờ phân tích ViSinhVien có thể được tính thế nào. Ta dựng bảng giá **hoàn toàn giả định**, không gắn với model hoặc provider thật. Tỷ giá cũng là giả định phục vụ bài tập, không phải tỷ giá thanh toán. Giả sử mỗi request có cùng lượng token, không có khoản tính riêng khác.

| Đại lượng | Giá trị giả định |
| --- | ---: |
| Input mỗi request | 20000 token |
| Output mỗi request | 5000 token |
| Số request | 50 |
| Giá input | 0.30 USD / 1000000 token |
| Giá output | 2.50 USD / 1000000 token |
| Tỷ giá quy đổi | 25000 VND / USD |

**Request** là một yêu cầu gửi đến dịch vụ. Trong bảng, 50 request được giả định là 50 lần xử lý theo lượng đã cho. Một lần người dùng bấm nút trong ứng dụng thực tế chưa chắc chỉ tương ứng một request; phần agent phía sau có thể gọi nhiều lần.

Công thức không khó, nhưng phải đặt đúng đơn vị:

```text
Tổng input  = input mỗi request  × số request
Tổng output = output mỗi request × số request

Tiền input  = tổng input  / 1000000 × giá input
Tiền output = tổng output / 1000000 × giá output
Tổng USD    = tiền input + tiền output
Tổng VND    = tổng USD × tỷ giá giả định
```

Làm từng dòng, chưa làm tròn ở giữa:

| Phần tính | Phép tính | Kết quả |
| --- | --- | ---: |
| Tổng input | 20000 × 50 | 1000000 token |
| Tổng output | 5000 × 50 | 250000 token |
| Tiền input | 1000000 / 1000000 × 0.30 | 0.30 USD |
| Tiền output | 250000 / 1000000 × 2.50 | 0.625 USD |
| Tổng | 0.30 + 0.625 | 0.925 USD |
| Quy đổi | 0.925 × 25000 | 23125 VND |

**Kết luận đúng: 0.925 USD = 23125 VND, chưa phí.** Các khoản như thuế, chênh lệch tỷ giá thanh toán, phí ngân hàng, công cụ hoặc lưu trữ nếu dịch vụ áp dụng chưa nằm trong mô hình. Không làm tròn 0.925 thành 0.93 trước rồi dùng kết quả đó để khẳng định con số chính xác của bài.

Minh kiểm tra theo từng request: input tốn 0.006 USD, output tốn 0.0125 USD, tổng 0.0185 USD. Nhân 50 được 0.925 USD, trùng phép tính theo tổng token. Đây là cách kiểm tra chéo đơn giản: tính theo hai hướng để bắt lỗi nhầm triệu với nghìn.

> **Tại sao output ít hơn mà tốn nhiều hơn?**
>
> Output chỉ bằng một phần tư input, nhưng giá giả định mỗi triệu token output lớn hơn. Tiền không tỉ lệ riêng với số token nếu đơn giá hai loại khác nhau. Gộp 1250000 token rồi nhân một giá chung sẽ sai bài.

#### 1.3.3. Nếu lượng dùng tăng 20 lần thì sao?

Giữ nguyên cơ cấu input/output và đơn giá giả định, tăng toàn bộ lượng dùng 20 lần. Có thể hình dung từ 50 lên 1000 request cùng kích thước. Khi đó tổng input là 20000000 token, output là 5000000 token. Tiền tương ứng là 6.00 USD và 12.50 USD.

```text
Tổng mới = 0.925 × 20 = 18.50 USD
Quy đổi  = 18.50 × 25000 = 462500 VND, chưa phí
```

Bài cố định đơn giá để xét lượng dùng. Giá thực không nhất thiết luôn tuyến tính; đổi model, bậc giá, chế độ hoặc công cụ thì phải tính lại.

Một **thuê bao hoàn toàn giả định 20 USD/tháng** tương ứng **500000 VND/tháng** theo cùng tỷ giá. Không suy API tương đương nhưng rẻ hơn: quota, tính năng, công cụ và điều kiện hai sản phẩm có thể khác. Tiền gần nhau không có nghĩa quyền lợi giống nhau.

Nếu Minh chỉ cần vài gợi ý miễn phí, không cần mua API để “tiết kiệm” so với thuê bao vốn không cần mua. Luôn đưa phương án không chi tiền vào so sánh.

#### 1.3.4. Những phần lượng dùng dễ bị quên

Lan nghĩ input chỉ là câu “Sửa hàm tính tổng”. Thực tế, ứng dụng có thể gửi lại brief, mã, lịch sử và kết quả công cụ trong mỗi lượt. Dù có cơ chế lưu phiên hoặc cache, cách tính lượng dùng vẫn phụ thuộc dịch vụ; không mặc định lịch sử đã gửi một lần thì mọi lần sau miễn phí.

**Tool output**, kết quả công cụ, như nhật ký chạy test dài hoặc nội dung tệp tìm được, có thể trở thành input của lượt tiếp theo. Một số model có lượng xử lý suy luận được ghi nhận hoặc tính phí theo cơ chế riêng. Việc reasoning token nằm ở đâu trong báo cáo, có tính vào output hay giới hạn nào, tùy provider và model. Bảng giả định không tự bao phủ mọi loại tính phí đó.

Một **agent** có thể tổ chức nhiều bước: đọc mã, đề xuất sửa, chạy test, đọc lỗi rồi sửa tiếp. Quy trình hữu ích nhưng có nguy cơ lặp. Nếu mỗi lần đều đính kèm context lớn, một yêu cầu “sửa cho xong” có thể sinh nhiều request mà người học không đếm bằng số lần bấm gửi.

```text
Yêu cầu của Lan
      |
      v
Đọc mã -> đề xuất sửa -> kiểm thử -> đọc lỗi
             ^                         |
             +------ lặp nếu chưa xong -+

Mỗi bước có thể phát sinh lần gọi hoặc dữ liệu tính phí.
Cần giới hạn phạm vi, số bước và có điểm dừng để người học xem lại.
```

Để dự toán hợp lý, Lan yêu cầu phạm vi chỉ một hàm, đầu ra ngắn đủ kiểm tra, và dừng sau một bản đề xuất. Khi không cần lịch sử dài, cô bắt đầu lượt mới bằng brief đã cập nhật. Không cắt bớt ràng buộc quan trọng chỉ để tiết kiệm vài token: sửa sai yêu cầu thường làm tốn thêm lượt.

#### 1.3.5. Cảnh báo ngân sách không phải cầu dao tự ngắt

Một email báo đạt 80% ngân sách là thông báo, không tự chứng minh dịch vụ dừng ở 100%. [Tài liệu billing Gemini API](https://ai.google.dev/gemini-api/docs/billing) và [Google Cloud Budgets](https://cloud.google.com/billing/docs/how-to/budgets), theo nguồn truy cập ngày **29/10/2026**, cần được đọc để phân biệt theo dõi ngân sách, cảnh báo và các cơ chế giới hạn chi tiêu được hỗ trợ.

Một số cơ chế cap hoặc giới hạn có thể được cung cấp tùy dịch vụ. Tuy nhiên, độ trễ ghi nhận, yêu cầu đang xử lý hoặc điều kiện áp dụng có thể khiến mức dùng vượt con số mong đợi. Không gọi một ngưỡng cảnh báo là **hard cap**, hạn mức cứng, và không hứa mọi cấu hình cap là ngân sách cứng tuyệt đối an toàn.

Với người mới, biện pháp quan trọng đầu tiên là chưa bật thanh toán khi chưa hiểu. Nếu sau này đủ điều kiện sử dụng, cần biết cách xem usage, giảm quota phù hợp, giới hạn số bước, dừng quy trình và xử lý khóa lộ. Chương này chỉ tập tính trên giấy, không hướng dẫn mở tài khoản thanh toán.

**Câu hỏi chốt mục:** Một agent dùng gấp 20 lần lượng token có còn là bài toán 23125 VND không? Không; theo đúng giả định phải là 462500 VND chưa phí. Bật cảnh báo 100000 VND có tự bảo đảm không vượt không? Không. Mua thuê bao chat có chứng minh mọi API đều miễn phí không? Không; phải xem quyền lợi, kể cả credit tích hợp nếu có.

### 1.4. Free first: học có kế hoạch, không mua trước khi biết thiếu gì

#### 1.4.1. Bắt đầu từ việc học, không bắt đầu từ màn hình nâng cấp

Minh cần hiểu vòng lặp, chưa cần agent sửa cả kho mã. Hãy tính tay, đọc bài học, dùng trình biên dịch sẵn có rồi hỏi công cụ miễn phí phù hợp nếu cần. Lan cũng xây được Web cục bộ không tích hợp AI.

**Free first** là ưu tiên phương án không thu phí đáp ứng việc học, không phải bất chấp điều kiện. Hết quota thì chia nhỏ câu hỏi, chờ chu kỳ sau, đọc tài liệu hoặc nhờ bạn. Không tạo nhiều tài khoản để lách giới hạn, dùng key nhặt được hay thử thanh toán vì tò mò.

Trước nâng cấp, nêu hạn chế cụ thể và kiểm tra gói có giải quyết không. Nếu chỉ cần một phần tài liệu, trích đoạn liên quan có thể thay thế việc mua khả năng đọc dài hơn.

> **Quyền không mua**
>
> Không mua công cụ là một quyết định hợp lệ. Không nên đánh đồng khả năng trả tiền với năng lực học CNTT. Các đề xuất trong chương là hướng dẫn tự học, không phải chuẩn đầu ra, quy định chi tiêu hay yêu cầu chính thức của TLU.

#### 1.4.2. Dự trù cho cả học kỳ, không chỉ một tối làm bài

Lan đặt một ngân sách học tập giả định **300000 VND cho học kỳ 15 tuần**, chỉ để minh họa cách lập kế hoạch. Đây không phải mức khuyến nghị cho mọi sinh viên. Nếu không có khoản dành cho AI, ngân sách có thể bằng 0; vẫn làm được các thực hành của chương.

| Khoản trong kế hoạch giả định của Lan | Dự trù | Điều kiện quyết định |
| --- | ---: | --- |
| Tuần 1–5: học nền tảng, thử cách hỏi | 0 VND | Dùng tài liệu và phương án miễn phí phù hợp |
| Tuần 6–10: một nhu cầu đã xác định | Tối đa 100000 VND | Chỉ xét chi khi có lợi ích đo được và đủ điều kiện |
| Tuần 11–15: hoàn thiện bài | Tối đa 100000 VND | Kiểm tra lại nhu cầu, không gia hạn theo quán tính |
| Dự phòng, có thể không dùng | 100000 VND | Không coi tiền dự phòng là mục tiêu phải tiêu hết |
| Tổng trần kế hoạch cá nhân | 300000 VND | Đây là kế hoạch trên giấy, không phải cap kỹ thuật |

So với kế hoạch này, thuê bao giả định 500000 VND/tháng ở mục 1.3 đã vượt cả ngân sách học kỳ. Không cần cố chứng minh mình “nên đầu tư” bằng mọi giá. Còn con số 23125 VND của API chỉ là một bài toán lượng dùng; nó chưa chứng minh Lan đủ tuổi, có thể quản lý khóa hoặc cần API.

Trước mỗi lần trả tiền, ghi việc cần làm, phương án miễn phí đã thử, số tiền tối đa và thời điểm đánh giá lại. Nếu gói tự gia hạn, phải biết ngày gia hạn và cách dừng trước khi mua; không coi quên hủy là chi phí tất yếu của việc học. Sau một tuần, đánh giá bằng số lỗi hiểu được hoặc thời gian thao tác tiết kiệm, không bằng số câu trả lời AI đã tạo.

#### 1.4.3. Ưu đãi sinh viên: xác minh điều kiện, không tin lời truyền miệng

Email trường có thể hỗ trợ chứng minh tình trạng học tập, nhưng không phải vé tự động được duyệt. [Hướng dẫn đăng ký GitHub Education cho sinh viên](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student), nguồn nghiên cứu truy cập ngày **29/10/2026**, nêu các điều kiện như đang theo học thuộc diện đủ điều kiện, từ 13 tuổi, có tài khoản cá nhân và chứng minh tình trạng sinh viên hiện tại. Có email TLU không tự bảo đảm hồ sơ được chấp thuận.

[GitHub Student Developer Pack](https://education.github.com/pack), nguồn truy cập ngày **29/10/2026**, liệt kê quyền lợi gồm GitHub Pro cho sinh viên và Copilot Student cho người học đã xác minh theo điều kiện áp dụng. Không đổi tên quyền lợi thành “Copilot Pro hiện tại” theo một hướng dẫn cũ. Các khả năng completion, chat, agent hoặc credit có giới hạn và điều kiện; chương không chốt quota.

Completion là gợi ý hoàn thành mã khi viết; chat là trao đổi; agent có thể thực hiện quy trình nhiều bước. Có một quyền lợi không có nghĩa mọi hình thức dùng đều vô hạn. Gói sinh viên cũng không mặc định cấp API key miễn phí cho mọi dịch vụ AI. Mỗi nhà cung cấp trong một chương trình ưu đãi có thể có điều khoản riêng.

Trong bài thực hành, chỉ đọc hoặc đối chiếu thông tin được cung cấp; không yêu cầu nộp hồ sơ, chụp giấy tờ hay đăng ký. Nếu sau này tự đăng ký, dùng trang chính thức và chỉ cung cấp giấy tờ cần thiết qua quy trình chính thức, không gửi vào chatbot hoặc nhóm lớp để “nhờ duyệt hộ”.

#### 1.4.4. Tuổi, dữ liệu và tài khoản là điều kiện trước giá

Điều kiện tuổi của một chương trình không áp dụng tự động cho dịch vụ khác. [Điều khoản Gemini API](https://ai.google.dev/gemini-api/terms), theo nguồn truy cập ngày **29/10/2026**, yêu cầu **18 tuổi trở lên** với Gemini API và Google AI Studio. Việc đủ điều kiện GitHub Education từ 13 tuổi không cho phép suy ra đủ điều kiện dùng Gemini API. Người chưa đủ tuổi theo điều khoản dịch vụ không dùng API đó; bài tập trên giấy là phương án phù hợp.

Cùng nguồn điều khoản này phân biệt cách xử lý dữ liệu theo loại dịch vụ. Với dịch vụ unpaid thuộc phạm vi áp dụng, nội dung có thể được dùng cải thiện sản phẩm và có người xem xét; không gửi dữ liệu nhạy cảm, bí mật hoặc thông tin cá nhân. Với paid, nhiều trường hợp không dùng nội dung để cải thiện, nhưng có chương trình hoặc tier đóng góp dữ liệu. Vì thế, không rút gọn thành “trả phí là riêng tư tuyệt đối”.

Cần kiểm tra đúng sản phẩm, cấp dịch vụ, lựa chọn dữ liệu và điều khoản đang áp dụng. Không lấy điều khoản API gán nguyên cho ứng dụng chat, hoặc suy mọi provider xử lý dữ liệu giống nhau. Với ViSinhVien, quyết định an toàn và đủ học là chỉ dùng ba khoản giả; không có lý do gửi sao kê, số tài khoản hay lịch sử chi tiêu thật.

Dùng tài khoản cá nhân hợp lệ, mật khẩu riêng và xác thực nhiều yếu tố khi dịch vụ hỗ trợ. Không mua tài khoản lậu, không dùng chung tài khoản thuê bao hoặc key để chia tiền mà bỏ qua điều khoản và quyền riêng tư. Người bán có thể đọc lịch sử, thu hồi quyền hoặc lấy thông tin; giá rẻ không bù được việc mất kiểm soát.

Nếu nghi khóa bị lộ, ưu tiên thu hồi hoặc vô hiệu hóa qua dịch vụ, kiểm tra mức dùng và tạo lại khi thực sự cần. Xóa khóa khỏi đoạn chat hoặc tệp mới nhất không bảo đảm những bản sao cũ biến mất. Bài tập không cần tạo khóa, nên cách tránh sự cố đơn giản nhất là không tạo bí mật không cần thiết.

### 1.5. Chọn theo tác vụ: ma trận công việc thay cho bảng xếp hạng

#### 1.5.1. Hỏi “hợp việc nào?” trước “mạnh nhất là ai?”

Giỏi dịch chưa chắc giỏi kiểm tra code; viết mã nhanh chưa chắc tìm được chính sách mới. Minh cần hiểu logic, Lan cần giữ đúng phạm vi dự án. Hãy chọn theo **tác vụ**, không theo danh tiếng chung.

Các tiêu chí đối chiếu là **provenance** (nguồn gốc, căn cứ), **test** (cách kiểm tra), **context** (thông tin cần nhận), **privacy** (điều kiện dữ liệu), **cost** (tổng chi phí). Căn cứ của sửa mã có thể là dòng code; căn cứ của tin chính sách phải là nguồn phù hợp. Ma trận này không xếp hạng sản phẩm thật.

| Tác vụ | Nhu cầu và context cần có | Provenance và test | Privacy và cost cần cân nhắc |
| --- | --- | --- | --- |
| Suy luận logic | Minh cần hiểu vì sao vòng lặp bỏ khoản cuối; đưa code, chỉ số, mục tiêu | Giải thích bám điều kiện; lập bảng duyệt, kiểm tra rỗng và một khoản | Dữ liệu giả; ưu tiên câu hỏi ngắn trên phương án free phù hợp |
| Code hoặc refactor | Lan tách kiểm tra dữ liệu và tính tổng; giữ HTML + JS + localStorage | Chỉ rõ thay đổi, không thêm backend; test mẫu, biên, dữ liệu sai | Không gửi key; xem quyền đọc tệp, số bước và chi phí lặp |
| Đọc tài liệu dài | Rút ràng buộc từ đặc tả ViSinhVien và ghi chú môn học liên quan | Trích đúng đoạn, chỉ chỗ mâu thuẫn; so với brief đã chốt | Chỉ tài liệu được phép; không mua context lớn nếu trích đoạn đủ |
| Dịch và diễn giải | Dịch lỗi hoặc tài liệu về lưu dữ liệu cho người mới | Giữ tên API và phủ định; kiểm tra không đổi số nguyên thành số thực | Tránh nội dung riêng tư; không cần quy trình agent nhiều bước |
| Tìm thông tin mới | Kiểm tra điều kiện ưu đãi hoặc cách đọc bảng giá | Cần truy xuất nguồn hiện hành, liên kết đúng đoạn, ngày truy cập | Không gửi giấy tờ; tính cả công cụ tìm kiếm nếu dịch vụ thu phí |

Không có tìm web thì không làm nguồn duy nhất về chính sách hiện tại. Không chạy được code thì vẫn có thể gợi ý, nhưng phải kiểm thử riêng. Giao việc trong phạm vi kiểm chứng được.

#### 1.5.2. Tự benchmark bằng ba đề nhỏ, cùng context

**Benchmark** là thử có kiểm soát để so mức phù hợp. Dùng ba đề có đáp án kiểm tra được, không chấm bằng cảm giác. Chuẩn bị trên giấy; chỉ thử bằng công cụ sẵn có được phép dùng, không mở tài khoản mới.

Giữ cùng brief, mã, dữ liệu, yêu cầu đầu ra và giới hạn trợ giúp. Nên bắt đầu cuộc trao đổi mới; ghi công cụ, chế độ, ngày và tính năng bật. Nếu một bên có web hoặc chạy code, ghi khác biệt, không quy mọi chênh lệch cho model.

**Đề A — Logic C++:** đưa chương trình lỗi ở mục 1.1, yêu cầu “gợi ý một bước rồi giải thích bằng chỉ số; nêu kết quả cho danh sách rỗng, một khoản 7000 và ba khoản mẫu”. Đáp án đối chiếu phải nhận ra bỏ phần tử cuối, tránh sửa thành truy cập quá mảng, và cho các tổng 0, 7000, 60000. Ba ca này trùng với ba ca đầu trong `vi_sinh_vien.cpp --test`, nên bạn kiểm chứng được. Đề này đo khả năng giải thích đúng, không chỉ viết code ngắn.

**Đề B — Refactor Web:** đưa brief và hàm cộng hợp lệ sau đây, yêu cầu đề xuất cách bổ sung kiểm tra dữ liệu mà không đổi phạm vi sản phẩm. Đoạn này là **bản rút gọn** của `totalExpenses` trong `vi-du/nam-2-web/data.js`, bỏ phần kiểm tra để làm đề bài; bản thật có thêm kiểm tra số lượng và giá trị:

```javascript
function totalExpenses(expenses) {
  return expenses.reduce((sum, expense) => sum + expense.amount, 0);
}
```

Đáp án tốt phân biệt nhiệm vụ cộng với nhiệm vụ xác thực. Dữ liệu trước khi được chấp nhận phải là danh sách tối đa 500 khoản; `amount` thỏa `Number.isInteger(amount)`, lớn hơn 0 và không quá 1000000000. Dữ liệu đọc từ `localStorage` cũng cần được kiểm tra; JSON hỏng cần xử lý có thông báo, không giả vờ là dữ liệu đúng. Không cần thêm máy chủ, tài khoản hoặc thư viện lớn để đạt yêu cầu.

Không bắt mọi đáp án phải có cùng kiến trúc. Có thể xác thực khi thêm và khi nạp, rồi hàm tổng nhận dữ liệu đã hợp lệ; cũng có thể đặt kiểm tra rõ ràng ở đầu hàm. Điều cần kiểm là hợp đồng dữ liệu và hành vi, không phải số lớp hay tên hàm giống bản mẫu.

**Đề C — Đọc và kiểm tra nguồn:** cung cấp brief và đoạn đối chiếu điều kiện GitHub Education tại mục 1.4.3, gồm liên kết, ngày truy cập. Yêu cầu tóm tắt cho Minh, phân biệt “đủ điều kiện nộp hồ sơ” với “chắc chắn được duyệt”, trả lời “email TLU có tự bảo đảm không?”. Đáp án là không; cần đáp ứng điều kiện và chứng minh tình trạng sinh viên. Không có công cụ tìm web thì chỉ phân tích đoạn được cung cấp, không tuyên bố đã kiểm tra tin mới.

#### 1.5.3. Rubric chung: đúng bài quan trọng hơn văn hay

**Rubric** là bảng tiêu chí chấm. Dùng mỗi tiêu chí 0–2 điểm, tổng tối đa 10 điểm cho một đề. Điểm này do người thử điền sau khi kiểm tra; chương không bịa kết quả của model nào.

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
| --- | --- | --- | --- |
| Đúng trọng tâm | Giải sai bài hoặc sai kết luận chính | Đúng một phần, còn thiếu quan trọng | Giải đúng tác vụ và kết quả chính |
| Giữ ràng buộc/context | Bỏ hoặc thay yêu cầu | Giữ phần lớn, cần nhắc thêm | Giữ yêu cầu liên quan, nhận ra dữ kiện thiếu |
| Bằng chứng/provenance | Khẳng định không căn cứ, bịa nguồn hoặc bịa chạy test | Có căn cứ nhưng chưa đủ rõ | Có suy luận, test hoặc nguồn phù hợp; nói rõ giới hạn |
| Dễ học và kiểm tra | Chép không hiểu, không có cách kiểm | Hiểu được một phần | Giải thích vừa sức, giúp tự làm bước tiếp |
| An toàn và tiết kiệm | Yêu cầu dữ liệu thật, khóa hoặc mở rộng tốn kém không cần | Có nhắc nhưng chưa cụ thể | Giữ dữ liệu giả, phạm vi nhỏ, không kéo chi phí vô ích |

Ghi thêm thời gian, số lượt phải hỏi lại, chi phí quan sát được hoặc “chưa xác định”. Đừng quy toàn bộ thuê bao thành giá một câu nếu chưa có mô hình phân bổ rõ. Nếu có điều kiện, thử lại một lần vì đầu ra có thể thay đổi; vẫn không dùng vài đề nhỏ để tuyên bố công cụ tốt nhất cho mọi người.

Một đáp án đạt nhiều điểm nhưng đề nghị đưa API key vào Web phải bị loại khỏi phương án triển khai cho đến khi sửa vấn đề an toàn. Rubric hỗ trợ suy nghĩ, không thay thế điều kiện bắt buộc. Với Minh, phương án đủ đúng, dễ hiểu, miễn phí có thể thắng phương án sinh nhiều mã hơn nhưng Minh không giải thích nổi.

**Phiếu ghi kết quả để trống:** Công cụ/chế độ: ______. Ngày thử: ______. Context dùng chung: ______. Điểm A/B/C: ______. Phần chưa kiểm chứng: ______. Số lượt và chi phí: ______. Chọn cho tác vụ nào, không chọn cho tác vụ nào: ______. Không điền điểm trước khi có thử nghiệm hoặc bằng chứng.

### 1.6. Thực hành 20 phút: nhận diện, ước chi và chọn giải pháp

#### 1.6.1. Chuẩn bị một tờ giấy, không chuẩn bị thẻ thanh toán

Làm cá nhân hoặc theo cặp, chỉ cần chương sách và chỗ ghi. Không đăng ký, cài đặt, gọi API, tạo key, tải giấy tờ hay dùng chi tiêu thật.

**Tình huống:** Minh muốn hiểu lỗi 42000 VND trong C++; Lan muốn kiểm tra Web cục bộ và thông tin ưu đãi sinh viên. Ứng dụng giả định “Trợ lý học ViSinhVien” công bố chế độ “Tự động”, không nêu model từng lượt hoặc provider. Web vẫn dùng HTML, JavaScript và `localStorage`. Dùng bảng giá giả định mục 1.3 để tính trên giấy.

Sản phẩm thực hành là phiếu ghi điều đã biết/chưa biết, phép tính có đơn vị, phương án chọn và cách kiểm tra. Không chấm theo việc sở hữu gói trả phí.

#### 1.6.2. Lịch 20 phút có điểm dừng

**Phút 0–4: nhận diện.** Điền ba vai trò; gạch chân dữ kiện, khoanh điều chưa biết. Nếu quan sát công cụ sẵn có, chỉ đọc thông tin công khai, ghi nguồn và ngày; không thay cài đặt hoặc đoán model.

**Phút 4–8: sửa cách hỏi.** Viết prompt ngắn cho Minh: mục tiêu, ba khoản, tổng đúng/sai, code, ràng buộc và yêu cầu gợi ý trước. Có thể dùng brief nhưng phải bảo đảm người nhận thực sự nhận được brief.

**Phút 8–13: ước chi.** Tính input/output cho 50 request, tiền USD/VND và mức dùng gấp 20. Kiểm tra chéo bằng cách tính từng request. Không thay số giả định bằng giá thật.

**Phút 13–17: chọn giải pháp.** Đối chiếu ít nhất ba tiêu chí mục 1.5. Nêu một phương án không trả tiền, một cách kiểm thử và điều kiện để cân nhắc lại.

**Phút 17–20: đối chiếu.** Xem đáp án, sửa phiếu rồi nói trong 30 giây: “Tôi biết gì, chưa biết gì, chọn gì, kiểm tra thế nào và chi tối đa bao nhiêu?”.

#### 1.6.3. Worksheet: điền trước khi xem đáp án

| Ô cần điền | Câu trả lời của bạn |
| --- | --- |
| Ứng dụng đang xét | ________________________________________ |
| Model cụ thể hoặc chế độ được công bố | ________________________________________ |
| Provider của đường truy cập | ________________________________________ |
| Nguồn và ngày quan sát | ________________________________________ |
| Điều chưa đủ chứng cứ để kết luận | ________________________________________ |
| Mục tiêu và kết quả đúng của ViSinhVien | ________________________________________ |
| Lỗi quan sát được và test đầu tiên | ________________________________________ |
| Dữ liệu không được gửi | ________________________________________ |

Viết prompt của bạn vào khoảng trống dưới đây. Hãy đọc lại bằng góc nhìn một người chưa biết dự án: họ có thể phân biệt lỗi với hành vi đúng hay chưa?

```text
Tôi đang học: _________________________________________________
Mục tiêu và phạm vi: __________________________________________
Dữ liệu, ràng buộc, code liên quan: _____________________________
Kết quả mong đợi / đang thấy: __________________________________
Hãy giúp theo cách: ___________________________________________
Tôi sẽ kiểm tra bằng: _________________________________________
```

| Phép tính bắt buộc | Kết quả kèm đơn vị |
| --- | --- |
| 20000 × 50 | ____________________ token input |
| 5000 × 50 | ____________________ token output |
| Tiền input theo giá giả định | ____________________ USD |
| Tiền output theo giá giả định | ____________________ USD |
| Tổng và quy đổi | ____________________ USD = ____________________ VND |
| Tổng khi lượng dùng tăng 20 lần | ____________________ USD = ____________________ VND |
| Khoản chưa được tính trong ví dụ | ________________________________________ |

Cuối cùng, hoàn thành một quyết định có điều kiện: “Với Minh, tôi chọn ______ vì ______. Với Lan, tôi chọn ______ vì ______. Tôi chưa mua ______. Tôi sẽ cân nhắc lại khi ______, sau khi kiểm tra ______. Nếu có nguy cơ vượt ngân sách hoặc điều kiện tuổi không phù hợp, tôi sẽ ______.”

#### 1.6.4. Đáp án đối chiếu và cách giải thích

**Nhận diện:** ứng dụng là Trợ lý học ViSinhVien, chế độ Tự động; model từng lượt và provider chưa xác định. Không đoán provider từ công ty phát hành ứng dụng. Nguồn là tình huống giả định; chỉ ghi ngày quan sát thực nếu có quan sát công cụ.

**Prompt mẫu:** “Tôi là Minh năm nhất, mới học vòng lặp C++. ViSinhVien cộng mọi khoản hợp lệ: `amount` nguyên VND, 0 < amount <= 1000000000, tối đa 500 khoản; rỗng cho tổng 0. Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000 phải ra 60000, nhưng code đính kèm ở mục 1.1 ra 42000. Hãy gợi ý một bước bằng cách xét chỉ số, chưa viết lại chương trình. Sau đó nêu test rỗng, một khoản và ba khoản; phân biệt suy luận với chạy thật.”

Khi thực sự gửi ở nơi khác, phải đính kèm code, không chỉ nói “code ở mục 1.1” nếu hệ thống không nhận chương sách. Đây là ví dụ nhỏ của việc kiểm tra context: con người thấy tài liệu không có nghĩa model thấy tài liệu.

**Phép tính:** input 1000000 token, output 250000 token; tiền tương ứng 0.30 và 0.625 USD; tổng **0.925 USD = 23125 VND chưa phí**. Mỗi request là 0.0185 USD, nhân 50 cho cùng kết quả. Khi toàn bộ lượng dùng tăng 20 lần theo cùng giá và cơ cấu, tổng **18.50 USD = 462500 VND chưa phí**. Thuê bao giả định 20 USD tương ứng 500000 VND nhưng không mặc nhiên tương đương về quota và tính năng.

**Minh:** lập bảng chỉ số, nhận gợi ý miễn phí nếu cần, tự sửa `i < n` rồi kiểm tra rỗng, một khoản, ba khoản; không cần API. **Lan:** giữ brief, sửa từng phần, kiểm tra dữ liệu vào, tổng và lưu/nạp; đối chiếu ưu đãi tại nguồn chính thức.

`localStorage` không phải kho bí mật hoặc sao lưu chắc chắn: xóa dữ liệu trình duyệt có thể làm mất dữ liệu; không tự đồng bộ thiết bị hay tạo đăng nhập. Web dùng dữ liệu giả, không backend là đúng phạm vi bài, không phải mẫu hệ thống tài chính thật.

#### 1.6.5. Câu hỏi kiểm tra cuối chương

**Câu 1.** “Tích hợp Claude” đủ xác định provider và phiên bản chưa? **Đáp án:** chưa; cần định danh và đường truy cập. Claude qua Bedrock cho thấy producer có thể khác provider.

**Câu 2.** Cùng model, một công cụ lại đề xuất backend: có chắc quảng cáo sai? **Đáp án:** chưa; kiểm tra context, chỉ dẫn, công cụ và cấu hình.

**Câu 3.** Rỗng có vi phạm `amount > 0` không? **Đáp án:** không; điều kiện áp dụng cho khoản tồn tại. Rỗng có tổng 0, không cần tạo khoản tiền 0.

**Câu 4.** Số từ tiếng Việt đủ suy chính xác hóa đơn token? **Đáp án:** không; còn phụ thuộc bộ tách, nội dung và cách tính dịch vụ.

**Câu 5.** Email TLU bảo đảm ưu đãi và quyền dùng mọi API? **Đáp án:** không; xác minh sinh viên và điều kiện tuổi từng dịch vụ là hai việc riêng.

**Câu 6.** Trả phí, bật cảnh báo là đủ bảo đảm riêng tư và không vượt tiền? **Đáp án:** không; phải kiểm tra chính sách dữ liệu, cơ chế giới hạn và độ trễ.

#### 1.6.6. Speaker Notes: trình bày trong 5–8 phút

Kịch bản **7 phút**, không thay thế thực hành 20 phút. Dùng bảng hoặc sơ đồ ASCII, không trình diễn đăng nhập hay thanh toán.

**0:00–1:00 — Mở chuyện.** Giới thiệu Minh, Lan và ba khoản mẫu. Hỏi tổng đúng, rồi đưa 42000. Đợi lớp tìm khoản thiếu 18000 để hình thành mốc kiểm tra độc lập.

**1:00–2:15 — Vẽ vai trò.** Vẽ ứng dụng, provider, model. Hỏi “mở ChatGPT đã biết model chưa?”. Dùng Claude qua Bedrock để tách producer/provider; Gemini để phân biệt ứng dụng/model. Chấp nhận “chưa xác định”.

**2:15–3:30 — Sửa prompt.** Đọc “sửa app cho chuẩn”, hỏi thiếu gì. Bổ sung mục tiêu, code, 60000/42000, dữ liệu nguyên và Web cục bộ. Cho lớp xét `i = 2`; nhắc không sửa thành `<= size`.

**3:30–4:45 — Tính tiền.** Nhân riêng 1 triệu input và 250000 output với giá giả định. Chốt 0.925 USD = 23125 VND; gấp 20 là 18.50 USD = 462500 VND, chưa phí. Nhắc giá, tỷ giá đều giả định.

**4:45–6:00 — Chọn an toàn.** Hỏi Minh có cần mua để hiểu vòng lặp không. Nhắc free first, email trường không tự duyệt, tuổi API theo điều khoản, không tài khoản lậu hoặc khóa trong JavaScript.

**6:00–7:00 — Kiểm tra.** Hỏi “kiểm chứng code bằng gì?” và “cảnh báo có tự dừng không?”. Đọc ba câu chốt. Có 5 phút thì rút hỏi đáp; có 8 phút thì thêm một quyết định của sinh viên.

#### 1.6.7. Ba câu chốt mang sang chương sau

> **Biết mình đang dùng ứng dụng nào, qua đường truy cập nào và model nào được công bố; không biết thì ghi chưa xác định.**
>
> **Đưa đúng mục tiêu và context, rồi kiểm tra đầu ra bằng phép tính, test hoặc nguồn phù hợp; văn phong tự tin không phải bằng chứng.**
>
> **Ưu tiên phương án miễn phí đủ dùng, tính cả lượng dùng và điều kiện dịch vụ trước khi trả tiền; không cần mua công cụ để chứng minh mình học nghiêm túc.**

#### 1.6.8. Nguồn và mốc đối chiếu

Các liên kết được đặt ngay ở đoạn sử dụng trong chương. Danh sách dưới đây giúp tìm lại nguồn; mốc **29/10/2026 là ngày truy cập của bộ nguồn nghiên cứu được cung cấp để biên soạn**, không phải ngày phát hành tài liệu và không phải cam kết điều khoản còn nguyên sau mốc đó. Khi áp dụng thực tế, đọc lại trang chính thức. Giá và tỷ giá trong bài toán mục 1.3 hoàn toàn giả định, không lấy từ các bảng giá này.

| Nhóm nội dung | Nguồn chính thức để đối chiếu |
| --- | --- |
| Họ model và định danh Claude | [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview) |
| Claude qua provider khác | [AWS — Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) |
| Gọi dịch vụ và chỉ định model | [Google — Gemini API docs](https://ai.google.dev/gemini-api/docs) |
| Ứng dụng Gemini và trải nghiệm người dùng | [Google — Gemini overview](https://gemini.google/overview/) |
| Điều kiện hồ sơ sinh viên | [GitHub — Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student) |
| Quyền lợi sinh viên được xác minh | [GitHub Student Developer Pack](https://education.github.com/pack) |
| Cách đọc free/paid và giá theo model | [Google — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Tuổi và điều kiện xử lý dữ liệu | [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms) |
| Thanh toán, cơ chế kiểm soát mức dùng | [Google — Gemini API billing](https://ai.google.dev/gemini-api/docs/billing) |
| Ngân sách và cảnh báo | [Google Cloud — Budgets](https://cloud.google.com/billing/docs/how-to/budgets) |
| Ngoại lệ credit API tích hợp theo điều kiện | [OpenAI — ChatGPT/API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |


---

## CHƯƠNG 2. TỪ CHAT ĐẾN CỘNG TÁC: AGENT, IDE VÀ CLI

Minh năm nhất còn yếu C++; Lan năm hai đang học OOP, DSA, CSDL và Web nhưng lúng túng khi lỗi chạy qua nhiều file. Hai bạn cùng xây **ViSinhVien**, ứng dụng ghi chi tiêu nhỏ: Minh luyện C++, Lan làm Web. Đây là hai phiên bản học tập, chưa kết nối với nhau.

Dữ liệu hoàn toàn giả: **Cơm trưa: 35000; Xe buýt: 7000; Vở ghi: 18000**, đơn vị VND. Tổng đúng **60000**; bỏ khoản cuối còn **42000**. Không nhập tên, mã sinh viên, số tài khoản hoặc thông tin thật của sinh viên vào bài tập hay hội thoại AI.

Mục tiêu không phải khiến AI viết thật nhiều, mà biết công cụ được phép làm gì và bằng chứng nào cho thấy chương trình đúng.

#### Chuẩn bị và thời lượng

Dành khoảng **180 phút**, chia hai buổi 90 phút: chuẩn bị 15 phút; 2.1–2.2: 20 phút; 2.3: 20 phút; 2.4: 35 phút; 2.5: 35 phút; 2.6–2.7: 20 phút; 2.8: 35 phút. Người chưa quen terminal có thể cần thêm thời gian.

Chuẩn bị Qoder IDE đã mở được và đăng nhập theo yêu cầu của sản phẩm; một trình duyệt; thư mục bài học có các demo bên dưới. Nhánh C++ cần `g++` **đã có sẵn** nếu muốn biên dịch. Nhánh Web cần Node.js đã có sẵn để chạy test dòng lệnh; mở trang Web không đòi Node.js. Thiếu công cụ thì vẫn đọc, dự đoán và trace được, nhưng phải ghi phần chạy máy là “chưa thực hiện”.

```text
vi-du/
  nam-1-cpp/
    vi_sinh_vien.cpp
    loi-bo-sot.cpp
  nam-2-web/
    index.html
    data.js
    app.js
    test_data.cjs
```

Các file demo được cung cấp cùng tài liệu; chương này không yêu cầu tạo lại chúng. Trước khi sửa, tạo bản sao thư mục nhánh bài học bằng trình quản lý tệp. Làm trên bản sao và giữ bản gốc để so sánh. Nếu dùng máy phòng thực hành, chỉ thao tác trong thư mục được giảng viên cho phép.

#### Trước khi gõ lệnh đầu tiên

Mục này dành cho người chưa từng mở terminal. Làm xong năm việc dưới đây rồi hãy đọc tiếp; chưa cần hiểu lệnh làm gì.

**1. Tạo bản sao để làm bài.** Mở trình quản lý tệp (Windows: File Explorer), vào thư mục `vi-du`, nhấn chuột phải thư mục `nam-1-cpp` → Copy, rồi Paste ngay trong `vi-du` và đổi tên bản vừa dán thành `nam-1-cpp-ban-sao`. Làm tương tự với `nam-2-web` khi học nhánh Web. Từ đây, mọi lần sửa là sửa trong bản sao.

**2. Tạo tệp ghi chép.** Trong Qoder IDE, mở thư mục bản sao, rồi dùng chức năng tạo tệp mới của IDE (thường là biểu tượng “New File” ở khung danh sách tệp, hoặc menu File → New File) và đặt tên đúng là `ghi-chep-02.txt`. Cách khác: trong File Explorer, nhấn chuột phải chỗ trống → New → Text Document rồi đổi tên. Tệp này không có sẵn trong bộ ví dụ; bạn tự tạo và tự ghi.

**3. Mở terminal trong IDE.** Qoder IDE có terminal tích hợp; nếu chưa biết mở ở đâu, dùng menu của IDE hoặc đối chiếu tài liệu chính thức <https://docs.qoder.com/user-guide/editor/terminal.md>. Cẩm nang không khẳng định tổ hợp phím cụ thể vì bố cục có thể khác theo phiên bản và hệ điều hành. Bạn cũng có thể dùng terminal của hệ điều hành rồi tự chuyển vào đúng thư mục theo mục 2.6.1.

**4. Mở Console của trình duyệt** (phần này cần cho nhánh Web, dùng khi xem thông báo lỗi JavaScript). Mở `index.html` trong Chrome hoặc Edge, nhấn **F12**, rồi chọn tab **Console**. Nếu F12 không có tác dụng, thử `Ctrl + Shift + I` (macOS: `Cmd + Option + I`), hoặc menu ba chấm → More tools → Developer tools. Đóng bằng F12 lần nữa.

**5. Biết mình đang đứng ở thư mục nào.** Cẩm nang luôn ghi rõ lệnh chạy ở đâu. Toàn chương này chạy lệnh **bên trong thư mục của nhánh**, ví dụ `vi-du/nam-1-cpp-ban-sao`; mục 3.6 có cách chạy từ thư mục gốc dự án nên đường dẫn trong lệnh dài hơn. Hai cách cho cùng kết quả, nhưng không được trộn nửa cách này với nửa cách kia. Kiểm tra vị trí bằng `pwd` (PowerShell: `Get-Location`) trước mọi lệnh.

**Nếu máy chưa có `g++` hoặc `node`:** bạn vẫn học được chương này. Hãy đọc mã, lập bảng trace bằng tay, trả lời các ca kiểm thử trên giấy và ghi vào `ghi-chep-02.txt` dòng “phần chạy máy: chưa thực hiện vì thiếu công cụ”. Việc cài trình biên dịch hoặc Node.js phụ thuộc quy định máy phòng thực hành, nên hãy hỏi giảng viên hoặc người quản lý phòng máy trước khi cài; cẩm nang không hướng dẫn cài để tránh làm sai cấu hình máy chung. Bảng trace làm đúng vẫn được tính là bài làm hợp lệ.

#### Mục tiêu đo được của buổi học

Đây là mục tiêu thực hành, **không phải CLO chính thức** của học phần. Kết thúc buổi học, người học có thể:

- Phân biệt IDE, terminal, shell, CLI và Agent bằng một câu cho mỗi thuật ngữ.
- Mở đúng thư mục, dùng Ask đặt một câu hỏi chỉ đọc với ngữ cảnh một hoặc hai file.
- Lập bảng trace ba khoản tiền, chỉ ra vì sao điều kiện sai cho kết quả 42000.
- Giải thích được tham chiếu C++ đơn giản và một lỗi biên dịch thiếu dấu chấm phẩy.
- Theo dấu dữ liệu Web từ ô nhập qua `app.js` đến `data.js`, phân biệt chuỗi với số.
- Chạy được ít nhất một nhánh kiểm thử nếu đủ công cụ; ghi lệnh, kết quả và exit code.
- Đọc diff trước khi nhận thay đổi; nhận diện việc ngoài phạm vi và không tự động cho phép.

Mọi đoạn hội thoại AI sau đây là **tình huống minh họa giả định**, không phải nhật ký đã chạy Qoder trong tài khoản người đọc. Output gắn nhãn “dự kiến” là đích đối chiếu, không phải chứng nhận demo đã được thực thi. Tên nút và vị trí giao diện có thể khác theo phiên bản.

### 2.1. Từ trình soạn thảo đến người cộng tác: thêm khả năng, không bỏ nền tảng

#### 2.1.1. Bốn cách làm việc quanh cùng một bài toán

Minh cần nơi gõ mã, tìm lỗi, chạy chương trình, hỏi khái niệm rồi giao việc có giới hạn cho AI. Sơ đồ mô tả sự mở rộng cách làm việc, **không phải bảng xếp hạng hay lộ trình thay thế**:

```text
Editor → IDE → Web chat → Agent
 gõ mã   tích hợp   hỏi đáp   cộng tác có công cụ
```

Mũi tên nghĩa là thêm cách hỗ trợ. Editor vẫn hữu ích; Web chat vẫn phù hợp câu hỏi nhỏ; Agent không thay thế hiểu biết lập trình. IDE có thể tích hợp chat và Agent, nên các nhãn không hoàn toàn tách biệt.

| Cách làm | Việc phù hợp | Người học vẫn phải làm |
|---|---|---|
| Editor | Viết, sửa nội dung file | Lưu đúng file và nơi |
| IDE | Mở dự án, tìm mã, dùng terminal | Kiểm tra công cụ thực sự có trên máy |
| Web chat | Hỏi nguyên nhân lỗi vòng lặp | Cung cấp ngữ cảnh, kiểm chứng lời giải |
| Agent | Tìm file, đề xuất sửa, kiểm thử theo quyền | Giới hạn phạm vi, xem diff và bằng chứng |

Web chat thông thường chỉ thấy nội dung được cung cấp, trừ khi có kết nối hoặc quyền bổ sung. Đừng mặc định nó biết toàn dự án. Agent được cấp công cụ cũng không có nghĩa mọi kết luận của nó đúng.

#### 2.1.2. Cùng câu hỏi, khác lượng ngữ cảnh

“Tại sao tổng của em sai?” thiếu dữ liệu và kết quả để đối chiếu. Minh nên hỏi:

```text
Tôi đang học C++ năm nhất. Với ba khoản giả 35000, 7000,
18000, tổng cần là 60000 nhưng tôi quan sát được 42000.
Hãy đọc vòng lặp tôi cung cấp, giải thích từng lượt bằng bảng.
Chưa viết lại chương trình. Nếu thiếu ngữ cảnh, hãy nêu rõ.
```

Câu hỏi tốt có đầu vào, kết quả mong đợi, kết quả quan sát và mã cần xem. Tách điều quan sát khỏi điều phỏng đoán. Lan có thể hỏi Web chat về kiểu của `.value`; khi theo dấu nhiều file, IDE thuận tiện hơn nhờ ngữ cảnh, không phải vì đáp án chắc chắn đúng.

#### 2.1.3. Bài làm nhanh: chọn công cụ đủ dùng

Trong ba phút, chọn công cụ cho hai việc: giải thích `+=`; tìm hàm mà `app.js` gọi trong `data.js`. Ghi lựa chọn và lý do vào `ghi-chep-02.txt` trong bản sao bài học.

Đáp án gợi ý: hỏi đoạn ngắn cho việc đầu; dùng Ask đọc hai file cho việc sau. Chưa cần Agent sửa mã. Kết quả cần có là hai quyết định có lý do.

**Speaker Notes:** Hỏi lớp: “AI nói tổng đúng nhưng màn hình hiện 42000, em kiểm tra bằng chứng nào?”. Chọn cách làm quan sát được, không nhất thiết chọn công cụ mạnh nhất.

### 2.2. IDE, terminal, shell, CLI và vòng lặp Agent

#### 2.2.1. Năm thuật ngữ thường bị trộn lẫn

**IDE** là môi trường phát triển tích hợp: mở dự án, đọc/sửa mã, dùng tiện ích phát triển. Có Qoder IDE không bảo đảm có compiler `g++` hay runtime Node.js.

**Terminal** là cửa sổ nhận và hiển thị văn bản, nằm trong IDE hoặc là ứng dụng riêng.

**Shell** là chương trình diễn giải lệnh. PowerShell và Bash khác nhau; máy Windows có thể dùng PowerShell hoặc Git Bash. Biết hệ điều hành chưa đủ để chọn cú pháp.

**CLI**, giao diện dòng lệnh, cho phép tương tác bằng lệnh và tham số. `g++`, `node` và Qoder CLI là các ví dụ. Terminal hiển thị; shell hiểu cú pháp; chương trình CLI thực hiện việc được gọi.

**Agent** là trợ lý AI kết hợp suy luận với công cụ. Tùy sản phẩm, chế độ và quyền, nó có thể tìm, đọc, sửa file hoặc chạy terminal; không có quyền tuyệt đối trên máy.

Ví dụ, Minh gõ `g++ --version`: Bash tìm chương trình, `g++` in phiên bản, terminal hiển thị. Nếu không tìm thấy lệnh, cần kiểm tra công cụ hoặc đường dẫn, chưa phải sửa vòng lặp C++.

#### 2.2.2. Vòng lặp observe → plan → act → test

```text
Observe: quan sát dữ liệu, mã và thông báo lỗi
   ↓
Plan: nêu giả thuyết, phạm vi sửa và cách kiểm tra
   ↓
Act: thực hiện thay đổi được phép
   ↓
Test: chạy phép kiểm tra, đọc kết quả
   └── nếu chưa đạt: trở lại quan sát, không tuyên bố hoàn thành
```

Các bước là mô hình tư duy, không bảo đảm giao diện luôn hiển thị đúng bốn nhãn. Agent có thể lặp lại nhiều lần. Con người nên yêu cầu đầu ra ngắn ở mỗi bước để biết nó đang dựa vào bằng chứng nào.

| Bước | Việc với lỗi 42000 | Bằng chứng cần giữ |
|---|---|---|
| Observe | Đọc dữ liệu và điều kiện `i < n - 1` | Đoạn mã, kết quả trước sửa |
| Plan | Giả thuyết bỏ khoản cuối; chỉ sửa cận vòng lặp | Dự đoán ca 0, 1, 3 khoản |
| Act | Đổi điều kiện sang `i < n` trong phạm vi cho phép | Diff nhỏ, không kèm sửa giao diện |
| Test | Chạy lại ca thường và ca biên | Lệnh, output, exit code hoặc lý do chưa chạy |

Test thất bại là thông tin mới. Ví dụ, sửa vòng lặp khiến tổng đúng nhưng test khoản âm vẫn thất bại: phần tính tổng đã tiến bộ, phần kiểm tra đầu vào chưa đạt. Không được xóa ca khó, bỏ qua lượt chạy lỗi hoặc đổi giá trị mong đợi thành kết quả sai để làm báo cáo đẹp.

#### 2.2.3. Phân biệt lời hứa với bằng chứng

“Tôi sẽ chạy test” là kế hoạch, chưa phải kết quả. Cần lệnh, thư mục, log và mã thoát. Thiếu công cụ hoặc bị chặn thì báo “chưa kiểm thử”, không nói “chắc sẽ qua”.

Prompt sao chép:

```text
Hãy làm theo Observe → Plan → Act → Test.
Trước mắt chỉ Observe và Plan, không sửa file hoặc chạy lệnh.
Tách rõ: điều đọc được từ mã; giả thuyết; điều chưa kiểm chứng.
Đề xuất một thay đổi nhỏ và các ca kiểm tra trước khi thực hiện.
Không coi việc tôi nhờ hỗ trợ là quyền truy cập toàn máy.
```

Prompt **không thay thế quyền công cụ**. Quyền phụ thuộc cài đặt, môi trường, cơ chế phê duyệt; vẫn phải kiểm tra chính sách chạy lệnh.

**Speaker Notes:** Cho sinh viên đóng vai Agent chỉ được đọc một mảnh giấy. Có khả năng lấy cả tập bài không đồng nghĩa được phép lấy.

### 2.3. Khởi đầu với Qoder IDE bằng chế độ chỉ đọc

#### 2.3.1. Chọn đúng sản phẩm trước khi tìm nút

Demo chính dùng **Qoder IDE**, theo tài liệu đối chiếu ngày **29/10/2026**. Giao diện có thể khác phiên bản; kiểm tra tài liệu thay vì thử hành động có quyền rộng hơn.

> **Phân biệt sản phẩm:** Qoder Desktop độc lập với Qoder IDE, có Coding/General. Không áp hướng dẫn Ask/Agent hay UI của IDE sang Desktop. Qoder CLI là sản phẩm dòng lệnh, chỉ là tùy chọn ở 2.6; không bắt buộc cài cả ba.

Chương không hứa quota, gói miễn phí hay giá. Điều kiện tài khoản có thể thay đổi; trace bằng tay không cần mua dịch vụ.

#### 2.3.2. Mở thư mục nhỏ, nhận diện file trước

1. Khởi động Qoder IDE và dùng **Open** để mở bản sao nhánh bài học. Minh chọn thư mục `nam-1-cpp`; Lan chọn `nam-2-web`. Không mở toàn bộ ổ đĩa hoặc thư mục cá nhân chỉ để tiện tìm file.
2. Nhìn cây thư mục. Minh phải thấy hai file C++; Lan phải thấy bốn file Web. Nếu khác, dừng lại xác định nơi đã mở.
3. Mở file định đọc bằng cách chọn tên file. Kiểm tra phần nội dung có thuộc ViSinhVien hay không.
4. Nhấn **Ctrl+L** để mở Chat theo tài liệu Qoder IDE. Trên thanh công cụ chat, chọn **Ask**, chưa chọn Agent.
5. Dùng `@` để chọn file hoặc folder làm ngữ cảnh. Nếu chỉ cần một đoạn, chọn đoạn mã và dùng **Add to Chat**. Giữ ngữ cảnh nhỏ trước; bổ sung khi có lý do.

Ask là chế độ chỉ đọc để hiểu kho mã và gợi ý snippet, không tự viết lại file. Tuy vậy, thông tin bạn đưa vào hội thoại vẫn cần tuân thủ quy định dữ liệu của lớp. “Chỉ đọc” không có nghĩa được phép đưa dữ liệu cá nhân hoặc bí mật vào ngữ cảnh.

#### 2.3.3. Câu hỏi đầu tiên cho từng năm học

Minh thêm `loi-bo-sot.cpp` vào ngữ cảnh rồi gửi:

```text
Tôi là sinh viên năm nhất C++ còn yếu vòng lặp.
Chỉ đọc loi-bo-sot.cpp; không sửa và không chạy lệnh.
Tìm nơi tính tổng. Với 35000, 7000, 18000, hãy lập bảng
cột i, điều kiện, số được cộng, tổng sau bước.
Giải thích vì sao kết quả có thể là 42000 thay vì 60000.
Chỉ ra giả định về n và kiểu dữ liệu trước khi kết luận.
```

Lan thêm `app.js` và `data.js`, chỉ bổ sung `index.html` khi cần xem form:

```text
Tôi là sinh viên năm hai, đang học OOP/DSA và Web.
Chỉ đọc các file được đính kèm, không sửa hoặc chạy lệnh.
Hãy mô tả đường đi: ô nhập → xử lý form → kiểm tra amount
→ tạo Expense → tính tổng → hiển thị/lưu cục bộ.
Với mỗi bước, nêu tên file và hàm thực sự tìm thấy.
Nếu chưa thấy mã liên quan, nói thiếu ngữ cảnh; đừng bịa tên hàm.
```

Đáp án đạt yêu cầu phải dẫn tới vị trí có thể mở lại trong file. Nếu AI chỉ nói chung “hãy kiểm tra biến”, hỏi tiếp một vị trí cụ thể. Nếu AI dùng tên hàm không tồn tại, ghi nhận đó là điều cần kiểm chứng; đừng đổi tên mã để làm nó khớp câu trả lời.

#### 2.3.4. Khi nào chuyển sang Agent?

Chỉ chuyển khi đã mô tả được lỗi bằng một câu, có dự đoán trước sửa và biết file nào được phép đổi. Trong Qoder IDE, Agent có thể tìm/đọc/sửa nhiều file, lập kế hoạch và chạy terminal theo quyền. Khả năng nhiều file hữu ích nhưng không phải lý do để mở rộng một lỗi một dòng thành viết lại cả dự án.

Với thay đổi được đề xuất, dùng **View Changes** để xem và quyết định accept/reject. Không mặc định mọi phiên bản hiển thị giống nhau, cũng không khẳng định máy sinh viên đang bật xác nhận cho mọi lệnh. Trước khi nhờ chạy terminal, vào **Qoder IDE Settings → Chat → Auto-Run → Terminal** để xem chính sách hiện hành; không tự đổi cấu hình hoặc nới quyền để vượt một yêu cầu bị chặn.

Bài làm năm phút: gửi prompt chỉ đọc, mở vị trí AI chỉ ra. Lưu vào `ghi-chep-02.txt`: file đã đọc, điều xác minh được, điều chưa biết. Cần căn cứ trong mã, chưa cần bản sửa.

**Speaker Notes:** Xác nhận đúng sản phẩm. Hội thoại là giả định; nếu giao diện khác, kiểm tra phiên bản trước khi kết luận sinh viên làm sai.

### 2.4. Minh năm nhất: debug C++, trace và đọc lỗi biên dịch

#### 2.4.1. Hợp đồng dữ liệu trước thuật toán

Mỗi khoản có mô hình `Expense{id,title,amount,category}`. Bản C++ trong bài tập tập trung thuật toán nên có thể lấy riêng cột `amount` thành `vector<long long>`. Việc lấy riêng cột không có nghĩa các trường còn lại biến mất khỏi mô hình chung.

Quy tắc: `amount` là số nguyên **lớn hơn 0 và không quá 1000000000**; tối đa **500 khoản**; danh sách rỗng có tổng **0**. Giới hạn 1000000000 áp dụng cho từng khoản, không phải tổng. Tổng lớn nhất là `500 × 1000000000 = 500000000000`, nên dùng `long long` cho tiền và biến tổng thay vì dựa vào `int` thường chỉ có miền giá trị 32 bit.

Dưới đây là lõi minh họa, **trích đúng tên hàm `totalExpenses` của `vi-du/nam-1-cpp/vi_sinh_vien.cpp`** nhưng đã lược bỏ phần kiểm tra đầu vào để tập trung vào vòng lặp. Nó giả định danh sách đã qua bước kiểm tra số lượng và giá trị:

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

Giải thích từng dòng:

1. Hàm trả về `long long`. `const std::vector<long long>&` nhận danh sách bằng tham chiếu để không sao chép cả vector; `const` ngăn sửa danh sách qua tham số này.
2. `size()` cho số phần tử; đổi sang `int` phù hợp ở đây vì đã giới hạn tối đa 500. Không coi phép đổi kiểu này luôn an toàn với mọi vector khổng lồ.
3. Khởi tạo tổng bằng 0 trước khi cộng; danh sách rỗng cũng có đáp án xác định.
4. `i` bắt đầu từ 0, chạy khi nhỏ hơn `n`, tăng một sau mỗi lượt. Chỉ số hợp lệ là 0 đến `n - 1`.
5. `+=` nghĩa là lấy tổng cũ cộng giá trị tại chỉ số `i`, rồi lưu lại vào tổng.
6. Dấu `}` kết thúc thân vòng lặp; dòng sau chỉ chạy khi vòng lặp dừng.
7. `return` chuyển tổng về nơi gọi hàm.
8. Dấu `}` cuối kết thúc hàm.

Hàm lõi trên chưa tự kiểm tra đầu vào. Một chương trình hoàn chỉnh phải chặn khoản không hợp lệ và số lượng vượt giới hạn trước khi gọi, hoặc đặt kiểm tra tương đương trong hàm xử lý. Không dùng việc kiểu dữ liệu chứa được số âm làm lý do cho phép chi tiêu âm.

#### 2.4.2. Nhìn thấy phần tử bị bỏ qua

Trong `loi-bo-sot.cpp`, lỗi cần tìm là cận lặp sai:

```cpp
for (int i = 0; i < n - 1; ++i) {
    total += amounts[i];
}
```

Dòng đầu chỉ cho `i` chạy khi nhỏ hơn `n - 1`, nên dừng trước chỉ số cuối. Dòng thứ hai cộng đúng phần tử được truy cập nhưng không thể bù phần tử chưa được duyệt. Dòng thứ ba chỉ đóng vòng lặp, không tự cộng thêm gì.

Với `n = 3`, vector tiền là `[35000, 7000, 18000]`. Hãy che cột tổng và tự điền trước khi xem đáp án:

| Phiên bản | i | Điều kiện | Khoản được cộng | Tổng sau bước |
|---|---:|---|---:|---:|
| Sai | 0 | `0 < 2`: đúng | 35000 | 35000 |
| Sai | 1 | `1 < 2`: đúng | 7000 | 42000 |
| Sai | 2 | `2 < 2`: sai, dừng | Không cộng | 42000 |
| Đúng | 0 | `0 < 3`: đúng | 35000 | 35000 |
| Đúng | 1 | `1 < 3`: đúng | 7000 | 42000 |
| Đúng | 2 | `2 < 3`: đúng | 18000 | 60000 |
| Đúng | 3 | `3 < 3`: sai, dừng | Không cộng | 60000 |

Output số học dự kiến với ba khoản:

```text
Lõi sai:   42000
Lõi đúng:  60000
```

Đây là nhãn giải thích trong sách, không cam kết chương trình in nguyên văn “Lõi sai”. Hãy đối chiếu giá trị số, dữ liệu đầu vào và tên executable thực sự đã chạy.

**Ca `n = 0`:** trong ví dụ này `n` là `int`. Điều kiện đúng là `0 < 0`, sai ngay; tổng giữ 0. Điều kiện lỗi là `0 < -1`, cũng sai ngay; tổng vẫn 0. Vì vậy test rỗng **không phát hiện** lỗi bỏ phần tử cuối. Vòng lặp không truy cập phần tử nào; đừng giải thích rằng nó đọc `amounts[-1]`.

**Ca `n = 1`:** điều kiện sai thành `0 < 0`, không chạy; tổng sai là 0. Điều kiện đúng `0 < 1` chạy một lượt và trả đúng khoản duy nhất. Ca một phần tử rất mạnh để phát hiện lỗi này.

Không thay `n` bằng `amounts.size()` rồi trừ 1 một cách máy móc. `size()` thường trả **kiểu không dấu**, tức kiểu chỉ chứa số không âm; với danh sách rỗng, phép trừ `0 - 1` ở kiểu đó không cho `-1` mà vòng về một số rất lớn, nên vòng lặp chạy sai hoàn toàn. Đó là **tràn vòng giá trị**. Chương dùng `int n` với giới hạn nhỏ để người mới tập trung hiểu cận vòng lặp.

#### 2.4.3. Tham chiếu đơn giản: hai tên, một biến

Trước khi học con trỏ phức tạp, Minh đọc ví dụ độc lập sau:

```cpp
long long total = 0;
long long& alias = total;
long long copied = total;
alias += 35000;
std::cout << total << ' ' << copied << '\n';
```

Dòng 1 tạo biến tổng bằng 0. Dòng 2 tạo tham chiếu `alias`, tức một tên khác của chính `total`; dấu `&` ở khai báo này không phải yêu cầu nhập địa chỉ. Dòng 3 tạo biến mới `copied` bằng giá trị hiện tại của `total`. Dòng 4 tăng biến được tham chiếu lên 35000. Dòng 5 in hai giá trị cách nhau một dấu cách.

Output dự kiến:

```text
35000 0
```

| Sau dòng | total | alias nhìn thấy | copied |
|---|---:|---:|---:|
| 1 | 0 | Chưa khai báo | Chưa khai báo |
| 2 | 0 | 0, cùng biến total | Chưa khai báo |
| 3 | 0 | 0 | 0 |
| 4 | 35000 | 35000 | 0 |

Không sửa demo chỉ để chèn đoạn này. Có thể trace trên giấy và lưu bảng trong ghi chép. Mục tiêu là phân biệt tham chiếu với bản sao, chưa phải học quản lý bộ nhớ động.

#### 2.4.4. Đọc lỗi compiler thay vì hỏi “sửa hết giúp em”

Giả sử Minh viết đoạn sau; đây là lỗi minh họa, không yêu cầu cố tình làm hỏng demo:

```cpp
long long total = 0
for (int i = 0; i < n; ++i) {
    total += amounts[i];
}
```

Dòng đầu thiếu `;`. Compiler có thể báo thông điệp dạng `expected ',' or ';' before 'for'`, kèm file, dòng và cột. Câu chữ cụ thể tùy phiên bản. Nó trỏ tới `for` vì đến đó mới thấy không thể tiếp tục phân tích; nguyên nhân có thể nằm ở dòng ngay trước.

Đọc theo thứ tự: đúng tên file chưa; lỗi đầu tiên ở đâu; dòng trước có kết thúc đầy đủ không; tên biến đã khai báo chưa. Sửa lỗi đầu tiên rồi biên dịch lại. Nhiều thông báo sau có thể là hệ quả dây chuyền, không phải nhiều lỗi độc lập.

```text
Tôi mới học C++. Đây là lệnh biên dịch và thông báo lỗi đầu tiên.
Hãy giải thích từng phần: file, dòng, cột, nội dung thông báo.
Chỉ ra dòng cần kiểm tra và một sửa đổi nhỏ nhất.
Chưa viết lại thuật toán; không tuyên bố chạy được nếu chưa chạy.
```

#### 2.4.5. Thực hành ngắn và nơi lưu

Mở bản sao `loi-bo-sot.cpp`, tìm đúng vòng lặp, ghi dự đoán 42000 trước khi sửa. Dùng Ask để đối chiếu trace. Khi đã hiểu, chỉ đổi cận sai thành `i < n`; lưu file bằng lệnh Save của IDE. Biên dịch và chạy theo 2.6 nếu có `g++`. Ghi kết quả trước/sau, bảng `n = 0, 1, 3` vào `ghi-chep-02.txt` trong bản sao `nam-1-cpp`.

Kết quả cần có: diff nhỏ, giải thích được vì sao sửa, tổng dự kiến sau sửa là 60000. Không thay cả file lỗi bằng file đúng, vì như vậy khó chứng minh mình xác định được nguyên nhân.

**Speaker Notes:** Cho sinh viên tự trace `n = 1` trước ca ba khoản. Hỏi vì sao rỗng vẫn qua dù chương trình sai. Nếu chưa có compiler, đánh dấu hoạt động là “trace thủ công”; tuyệt đối không biến dự đoán trên bảng thành báo cáo đã chạy máy.

### 2.5. Lan năm hai: theo dấu dữ liệu qua form, app.js và data.js

#### 2.5.1. Mô hình Expense nối các môn, không mở rộng hệ thống

Lan dùng đối tượng có hình dạng `Expense{id,title,amount,category}`. `id` phân biệt khoản; `title` là tên hiển thị; `amount` là số tiền nguyên VND; `category` là nhóm chi tiêu. Dữ liệu giả minh họa:

```js
const expenses = [
  { id: 1, title: 'Cơm trưa', amount: 35000, category: 'an-uong' },
  { id: 2, title: 'Xe buýt', amount: 7000, category: 'di-lai' },
  { id: 3, title: 'Vở ghi', amount: 18000, category: 'hoc-tap' }
];
```

Dòng đầu khai báo mảng. Ba dòng tiếp theo tạo ba đối tượng cùng cấu trúc; số tiền không có dấu nháy vì đang là số. Dòng cuối đóng mảng và kết thúc khai báo. Các `id` ở đây là mã số của khoản chi giả, không phải mã sinh viên. `category` lưu mã như `hoc-tap`; bảng ánh xạ trong `data.js` chuyển mã này thành nhãn “Học tập” để hiển thị.

Liên hệ OOP: `Expense` là mô hình dữ liệu của một thực thể chi tiêu; kiểm tra đầu vào giúp giữ bất biến của mô hình. JavaScript không bắt buộc viết `class Expense` chỉ để biểu diễn mô hình này. Liên hệ DSA: tổng duyệt qua danh sách một lần, thời gian O(n), biến tổng thêm O(1) bộ nhớ. Không cần thuật toán khó để giải thích lỗi ánh xạ sai trường.

CSDL/SQL chỉ là điểm nối môn để học tiếp ở **Chương 4**. Bản Web hiện tại không có server, không đăng nhập, không kết nối CSDL thật. Không tự thêm API, tài khoản hay dịch vụ lưu trữ trực tuyến để “hoàn thiện” bài này.

#### 2.5.2. Mở trang và xác định đường đi của giá trị

Giữ `index.html`, `data.js`, `app.js`, `test_data.cjs` trong cùng thư mục `nam-2-web`. Mở trực tiếp `index.html` bằng trình duyệt, chẳng hạn từ trình quản lý tệp. Không cần khởi động server cho demo này. Nếu trang không hoạt động, kiểm tra các file JS còn ở đúng vị trí và xem Console; không lập tức đổi sang một kiến trúc khác.

`data.js` công bố API qua `globalThis.ViData` để trình duyệt dùng và `module.exports` để Node.js dùng. Trong trang, mã cần API dữ liệu phải chạy sau khi API đã được nạp. Trong Node.js, file kiểm thử dùng cơ chế xuất tương ứng. Đây là hai môi trường cùng dùng logic dữ liệu, không phải hai bản logic cần chép riêng.

| Chặng | Nơi cần đọc | Câu hỏi kiểm tra |
|---|---|---|
| Ô nhập tiền | `index.html` | Ô nào chứa giá trị? Tên/id thực tế là gì? |
| Nhận sự kiện form | `app.js` | Handler lấy `.value` từ phần tử nào? |
| Chuyển và kiểm tra | `data.js`, `parseAmount(input)` | Chuỗi có đúng dạng, miền giá trị không? |
| Tạo khoản | `app.js` | Thuộc tính nhận số tiền tên `amount` hay tên khác? |
| Tính tổng | `data.js`, `totalExpenses(expenses)` | Đọc đúng `amount` và kiểm tra hợp lệ chưa? |
| Hiển thị/lưu | `app.js` | Giá trị được render và lưu cục bộ thế nào? |

Các id của form và cách gắn sự kiện phải đọc từ demo thực tế, không suy đoán theo bảng. Trong `app.js` đi kèm, phần xử lý gửi form được gắn bằng `form.addEventListener('submit', event => { ... })`, tức là **hàm xử lý không có tên**; khi ghi chép, bạn ghi “hàm vô danh gắn vào sự kiện submit của form” thay vì cố tìm một cái tên. Khi hỏi AI, yêu cầu nó nêu file và dòng tìm thấy. Nếu nó chỉ đọc `data.js`, nó chưa đủ bằng chứng để kết luận form gắn sự kiện đúng.

#### 2.5.3. `.value` là chuỗi: nhìn giống số chưa phải số

Với ô nhập HTML đang dùng, `input.value` luôn trả chuỗi, kể cả khi ô có `type="number"`. Xem ví dụ độc lập trong Console:

```js
const first = '35000';
const second = '7000';
console.log(first + second);
console.log(typeof first);
```

Dòng 1 và 2 tạo hai chuỗi. Dòng 3 dùng `+` với chuỗi nên nối ký tự. Dòng 4 hỏi kiểu của biến đầu. Output dự kiến:

```text
350007000
string
```

Đây không phải tổng 42000. Đổi kiểu tùy tiện bằng `Number` cũng chưa đủ: chuỗi rỗng hoặc ký hiệu số mũ có thể được diễn giải theo cách ngoài hợp đồng nhập của bài.

`parseAmount(input)` nhận **chuỗi chỉ gồm chữ số sau `trim()`**; kết quả phải là số nguyên an toàn, lớn hơn 0 và không quá `1e9`. `trim()` bỏ khoảng trắng đầu/cuối, không xóa khoảng trắng ở giữa. Kiểm tra dạng chuỗi trước, rồi kiểm tra giá trị số. Không dùng `parseInt` như một bộ kiểm tra đầy đủ vì nó có thể đọc phần đầu rồi bỏ phần ký tự không hợp lệ phía sau.

Ví dụ dùng API đã có, sau khi mở trang và xác nhận `data.js` đã nạp:

```js
const raw = ' 35000 ';
const amount = globalThis.ViData.parseAmount(raw);
console.log(amount);
console.log(typeof amount);
```

Dòng 1 mô phỏng `.value`. Dòng 2 gọi hàm kiểm tra/chuyển đổi của demo, không chỉ đổi tên biến. Dòng 3 in giá trị; dòng 4 kiểm tra kiểu. Output dự kiến là `35000` rồi `number`. Các dòng Console này chỉ tạo giá trị minh họa, không tự thêm khoản vào giao diện hoặc lưu khoản.

#### 2.5.4. Lỗi biệt lập: đọc `value` thay vì `amount`

Đoạn lỗi sau **được cô lập để học**, không khẳng định `app.js` hoặc `data.js` được phát hành đang chứa nó. Không chèn nó vào demo đúng:

```js
const items = [{ amount: 35000 }, { amount: 7000 }, { amount: 18000 }];
const wrong = items.reduce((sum, x) => sum + x.value, 0);
console.log(wrong);
console.log(Number.isNaN(wrong));
```

Dòng 1 tạo ba đối tượng chỉ có trường `amount`; đây là mẫu tối giản để cô lập lỗi, chưa phải danh sách Expense đầy đủ. Dòng 2 cộng trường `value` không tồn tại. Dòng 3 in kết quả. Dòng 4 kiểm tra đúng cách xem giá trị có phải `NaN` không.

Output dự kiến:

```text
NaN
true
```

`NaN` viết tắt của **Not-a-Number**. Giá trị thuộc tính bị thiếu `x.value` là `undefined`; phép cộng số với giá trị đó dẫn tới `NaN`. **NaN không phải undefined**. Một điều dễ nhầm khác: `typeof NaN` là `"number"`; chỉ kiểm tra `typeof` chưa đủ để xác nhận số tiền hợp lệ.

| Lượt | amount của x | x.value | sum trước | Phép cộng | sum sau |
|---|---:|---|---|---|---|
| 1 | 35000 | `undefined` | 0 | `0 + undefined` | `NaN` |
| 2 | 7000 | `undefined` | `NaN` | `NaN + undefined` | `NaN` |
| 3 | 18000 | `undefined` | `NaN` | `NaN + undefined` | `NaN` |

Sửa đúng trường trong **đoạn biệt lập**:

```js
const correct = items.reduce((sum, x) => sum + x.amount, 0);
console.log(correct);
```

Dòng đầu bắt đầu từ 0 rồi cộng trường `amount` từng đối tượng. Dòng sau in tổng dự kiến `60000`. Cách này minh họa ánh xạ đúng trường, nhưng bản thân `reduce` chưa kiểm tra miền giá trị hay số lượng. Logic ứng dụng vẫn dùng `totalExpenses(expenses)` và các kiểm tra theo hợp đồng.

#### 2.5.5. Phân biệt lỗi ánh xạ, lỗi kiểu và lỗi duyệt

Ba kết quả sai kể ba câu chuyện khác nhau: **42000** gợi ý có thể thiếu khoản cuối; **350007000** gợi ý nối hai chuỗi; **NaN** gợi ý phép tính đã nhận dữ liệu không dùng được như số. Đây là dấu hiệu để đặt giả thuyết, chưa phải kết luận chỉ từ con số.

```text
Chỉ đọc index.html, app.js và data.js trong nam-2-web.
Tôi muốn kiểm tra mapping tiền từ ô nhập tới Expense.amount.
Hãy chỉ ra nơi lấy chuỗi, gọi parseAmount và tính tổng.
Phân biệt ba khả năng: nối chuỗi, đọc nhầm x.value, bỏ khoản cuối.
Đừng chèn lỗi minh họa vào demo đúng, đừng thêm server hay CSDL.
Đề xuất cách tái hiện nhỏ trước khi đề nghị sửa file.
```

Bài làm năm phút: vẽ sơ đồ mũi tên qua ba file; bên mỗi mũi tên ghi kiểu dữ liệu. Tối thiểu phải có “chuỗi từ `.value`” và “số nguyên hợp lệ trong `Expense.amount`”. Lưu sơ đồ dạng chữ và bảng trace vào `ghi-chep-02.txt` trong bản sao `nam-2-web`. Kết quả đạt là giải thích được **điểm chuyển kiểu**, không chỉ chỉ tay vào nút Thêm.

#### 2.5.6. Lưu cục bộ có giới hạn

Bản Web lưu bằng `localStorage` trong trình duyệt. Đây không phải server hay CSDL thật, không tự đồng bộ giữa máy hoặc tài khoản. Với file mở trực tiếp, cách trình duyệt xử lý lưu trữ có thể khác nhau. Nếu trình duyệt chặn lưu, app phải chuyển sang bộ nhớ và cảnh báo; dữ liệu trong bộ nhớ có thể mất khi tải lại hoặc đóng trang.

Hãy ghi lại bạn có thấy cảnh báo không. Nếu đã thấy cảnh báo fallback mà tải lại bị mất khoản, đừng báo “đã kiểm thử lưu bền vững thành công”. Cũng không tắt bảo vệ trình duyệt hoặc cấp quyền rộng để ép bài chạy. Nếu không tái hiện được tình huống bị chặn, ghi “chưa kiểm chứng fallback trên máy này”.

**Speaker Notes:** Dừng ở lần cộng đầu tiên của bảng NaN; hỏi chính xác cái gì là `undefined`, cái gì là `NaN`. Nối với OOP bằng bất biến của Expense, không kéo lớp sang triển khai cơ sở dữ liệu. Đảm bảo sinh viên biết dữ liệu đang nằm ở máy nào và tồn tại bao lâu.

### 2.6. CLI: thao tác nhỏ, đọc stdout và exit code

#### 2.6.1. Biết shell và thư mục trước khi gõ

Trong Qoder IDE, mở bảng lệnh — tức ô tìm lệnh của IDE, mở theo cách đã nêu ở mục “Trước khi gõ lệnh đầu tiên” — và tìm **Terminal: Create New Terminal**. Nếu không tìm thấy bảng lệnh, dùng menu của IDE để mở terminal tích hợp. Sau khi terminal xuất hiện, xác định shell đang dùng từ tên phiên hoặc cấu hình hiển thị. Không suy ra shell chỉ từ hệ điều hành. Kiểm tra thư mục hiện hành trước mọi lệnh biên dịch hay test.

| Nhu cầu | Bash, gồm Git Bash | PowerShell |
|---|---|---|
| Xem thư mục hiện hành | `pwd` | `Get-Location` |
| Liệt kê mục trong thư mục | `ls` | `Get-ChildItem` |
| Đổi sang thư mục đã xác định | `cd "đường/dẫn"` | `Set-Location "đường\dẫn"` |
| Xem mã thoát lệnh ngoài vừa chạy | `echo $?` | `$LASTEXITCODE` |

Trong bảng, đường dẫn là chỗ phải thay bằng vị trí bản sao của bạn, không phải chữ để gõ nguyên xi. Đặt đường dẫn có dấu cách trong dấu nháy kép. PowerShell có thể hỗ trợ vài tên gọi tắt quen thuộc, nhưng chương dùng tên rõ ràng để tránh trộn shell.

Nếu mở IDE ở thư mục gốc bài học, ví dụ sau vào nhánh C++; chỉ chạy khi kiểm tra thấy `vi-du` tại vị trí hiện hành:

```bash
cd "vi-du/nam-1-cpp"
pwd
ls
```

Ba dòng lần lượt đổi thư mục, xác nhận vị trí và liệt kê file. Với PowerShell, dùng:

```powershell
Set-Location "vi-du\nam-1-cpp"
Get-Location
Get-ChildItem
```

Nếu đã mở trực tiếp `nam-1-cpp`, **không chạy lại bước đổi thư mục này**. Chỉ xác nhận vị trí và nhìn thấy đúng file. Đây là lỗi rất thường gặp khi người học chép toàn bộ một khối lệnh mà không kiểm tra điểm bắt đầu.

#### 2.6.2. Biên dịch C++ nếu đã có g++

Chạy `g++ --version`. Nếu không tìm thấy, dừng nhánh chạy C++; không yêu cầu Agent tự cài compiler. Qoder không được giả định có compiler đi kèm hay tự động cài giúp. Tham khảo trang chính thức GCC tại <https://gcc.gnu.org/>; với Windows có thể tham khảo hướng dẫn chính thức MSYS2 tại <https://www.msys2.org/> cùng yêu cầu của phòng máy. Không tải rồi thực thi mã từ xa bằng lệnh ghép đường ống.

Thực hiện **từng dòng**, không dán chạy cả khối; biên dịch lỗi thì dừng trước dòng chạy chương trình. Trong Bash/Unix hoặc Git Bash, tại thư mục C++:

```bash
g++ -std=c++17 -Wall -Wextra vi_sinh_vien.cpp -o vi_sinh_vien
echo $?
./vi_sinh_vien
echo $?
```

Dòng 1 gọi compiler, chọn C++17, bật cảnh báo và đặt tên đầu ra. Dòng 2 đọc mã thoát biên dịch ngay sau lệnh. **Chỉ chạy dòng 3 nếu biên dịch thành công**; nó chạy chương trình vừa tạo trong thư mục hiện hành. Dòng 4 đọc mã thoát của lượt chạy, không phải của compiler nữa.

Trong PowerShell, dùng tên `.exe` rõ ràng:

```powershell
g++ -std=c++17 -Wall -Wextra vi_sinh_vien.cpp -o vi_sinh_vien.exe
$LASTEXITCODE
.\vi_sinh_vien.exe
$LASTEXITCODE
```

Ý nghĩa từng dòng tương ứng bản Bash, nhưng cú pháp chạy executable là `.\vi_sinh_vien.exe`. Với demo lỗi, thay tên nguồn bằng `loi-bo-sot.cpp` và đặt tên executable riêng `loi-bo-sot` hoặc `loi-bo-sot.exe`; tránh nhầm chương trình đúng với chương trình lỗi.

**Tệp C++ đi kèm dùng dữ liệu cố định**, không chờ bạn nhập `n` hay số tiền từ bàn phím. Bản đúng in:

```text
Com trua: 35000 VND
Xe buyt: 7000 VND
Vo ghi: 18000 VND
Tong chi tieu: 60000 VND
```

Các nhãn không dấu giúp ví dụ dễ hiển thị trên terminal; không ảnh hưởng phép tính. Bản lỗi riêng in `Tong chi tieu: 42000 VND`. Muốn kiểm tra các ca rỗng, một khoản, giới hạn và dữ liệu sai trong bản đúng, thêm tham số `--test` sau tên chương trình:

```bash
./vi_sinh_vien --test
```

Trong PowerShell, dùng `.\vi_sinh_vien.exe --test`. `--test` là tham số do chương trình mẫu này tự xử lý, không phải tính năng có sẵn của mọi chương trình C++. Kết quả đạt của bản kèm có dòng cuối `9 passed, 0 failed`; kiểm tra cả các dòng `PASS` trước đó và exit code. Khi thử sửa bài, một ca không đạt phải được giữ lại để tìm nguyên nhân, không xóa khỏi bộ test.

Compiler thành công thường không in gì nếu không có cảnh báo. Im lặng không có nghĩa chưa chạy. Ngược lại, sau biên dịch thất bại có thể còn executable cũ; chạy nó rồi thấy đúng không chứng minh mã vừa sửa đúng.

#### 2.6.3. Chạy test dữ liệu Web bằng Node.js

Tại đúng thư mục `nam-2-web`, kiểm tra `node --version`, rồi chạy:

```text
node test_data.cjs
```

Lệnh này chạy file test có sẵn; không mở trình duyệt và không khởi động server. Sau lệnh, dùng `echo $?` trong Bash hoặc `$LASTEXITCODE` trong PowerShell để ghi mã thoát. Nếu thiếu Node.js, tham khảo <https://nodejs.org/> và quy định cài đặt của máy; ghi phần test là chưa chạy cho đến khi có môi trường phù hợp.

**stdout** là luồng kết quả thông thường; **stderr** thường chứa chẩn đoán lỗi. Terminal có thể hiển thị cả hai xen kẽ. Đừng chỉ đọc dòng cuối hoặc thấy một chữ “pass” rồi bỏ qua lỗi ở trên. Thông thường mã thoát 0 chỉ thành công, khác 0 chỉ thất bại; với test, còn phải đọc xem những ca nào thực sự đã chạy.

| Quan sát | Kết luận được phép | Bước tiếp theo |
|---|---|---|
| Exit 0, tất cả ca được báo đạt | Bộ test đã chạy qua các ca đó | Ghi log, tiếp tục kiểm tra giao diện |
| Exit khác 0, có assertion lỗi | Ít nhất một phép kiểm tra không đạt | Giữ log, tìm input và expected/actual |
| Không tìm thấy `node` | Chưa chạy được bộ test | Ghi thiếu runtime, không đánh dấu đạt |
| Không tìm thấy file test | Sai vị trí hoặc thiếu file | Kiểm tra thư mục, không tự tạo test thay thế |

Test `data.js` qua Node.js không chứng minh form, DOM hoặc localStorage trên trình duyệt hoạt động. Phải làm cả lượt thử giao diện ở 2.8. Ghi lệnh và exit code ngay; chạy lệnh khác trước có thể làm mất mã thoát cần báo cáo.

#### 2.6.4. Qoder CLI là phần tùy chọn

Chỉ thử khi **Qoder CLI đã được cài và đăng nhập** theo tài liệu hiện hành. CLI tách với IDE; có IDE không chứng minh lệnh CLI đã có. Kiểm tra bằng `qoder --version`, rồi gõ lệnh `qoder` tại thư mục bài học đã xác nhận để mở phiên tương tác. Trong phiên đó, `/help` xem trợ giúp, `/usage` xem thông tin sử dụng, `/quit` thoát. Không gõ các lệnh dấu `/` này vào PowerShell/Bash bên ngoài phiên rồi chờ chúng có cùng tác dụng.

Không cần khởi tạo tệp hướng dẫn Agent, thay cấu hình hay cài thêm CLI để đạt mục tiêu chương. Nếu chỉ có IDE, hoàn thành bài bằng IDE và terminal hiện có là đủ.

**Speaker Notes:** Yêu cầu sinh viên đọc lớn tên shell trước khi chạy. Khi có lượt test thất bại, giữ nó trên màn hình để lớp học cách đọc bằng chứng. Không che lỗi rồi chỉ trình chiếu lượt xanh cuối cùng.

### 2.7. Cộng tác an toàn: phạm vi nhỏ, diff rõ, checkpoint có thật

#### 2.7.1. Viết “hợp đồng công việc” trước khi giao sửa

Agent có thể tác động nhiều file, nên yêu cầu phải giới hạn được cả mục đích lẫn vị trí. Với lỗi của Minh, sửa toàn bộ giao diện Web là ngoài phạm vi. Với lỗi parse của Lan, thêm tài khoản và server là ngoài phạm vi. “Làm tốt nhất có thể” không thay được mô tả cụ thể.

```text
Phạm vi: bản sao thư mục bài học đã mở, không đọc ngoài thư mục.
Mục tiêu: sửa lỗi được tái hiện bằng ca kiểm tra tôi cung cấp.
Trước khi sửa: nêu file, nguyên nhân dự kiến và diff nhỏ nhất.
Chỉ sửa file đã được tôi đồng ý; giữ nguyên các phần không liên quan.
Không cài gói, không đổi cấu hình/quyền, không dùng dữ liệu thật.
Không tự commit, publish, triển khai hoặc đồng bộ ra dịch vụ ngoài.
Nếu hành động bị chặn, báo lại; không tìm đường vòng để vượt chặn.
Sau sửa: nêu test đã chạy, kết quả thất bại và phần chưa kiểm chứng.
```

Đây là prompt giao việc, không bảo đảm kỹ thuật rằng công cụ bị khóa đúng từng folder. Kết hợp nó với việc chỉ mở thư mục cần dùng, ngữ cảnh nhỏ và quyền hiện có. Không cấp quyền toàn máy để giải quyết một bài tập hai file.

#### 2.7.2. Đọc diff theo bốn câu hỏi

Mở **View Changes** để xem diff, tức phần khác nhau trước/sau. Đọc nội dung dòng bỏ/thêm, không chỉ nhìn màu.

Hỏi: file nào đổi; dòng nào đổi; liên quan lỗi thế nào; có ảnh hưởng hợp đồng dữ liệu không? Sửa `i < n - 1` thành `i < n` giải thích được bằng trace. Thêm hàng trăm dòng hoặc đổi API cần kiểm tra phạm vi.

Accept là nhận thay đổi, **không chứng nhận đúng**. Reject là không nhận đề xuất, không thay bản sao dự phòng. Luôn biết bản nào đang được chạy.

#### 2.7.3. Checkpoint và nhật ký bằng chứng

Người mới tạo bản copy trước sửa bằng trình quản lý tệp, đặt tên như `nam-1-cpp-truoc-sua`, giữ nguyên bản gốc. Người đã biết Git có thể dùng checkpoint quen thuộc theo hướng dẫn lớp; chương không yêu cầu tự tạo commit.

Nếu sửa không ổn, dừng, so sánh bản copy rồi phục hồi phần cần thiết. Không xóa hàng loạt hoặc ghi đè việc của bạn cùng nhóm. Biết checkpoint chụp thời điểm nào.

Mẫu ghi vào `ghi-chep-02.txt`:

```text
Phạm vi được mở:
Checkpoint trước sửa:
Lỗi quan sát và input:
File/dòng thay đổi, lý do:
Lệnh hoặc thao tác kiểm tra:
Kết quả thực tế, exit code nếu có:
Lượt thất bại đã gặp:
Phần chưa chạy hoặc chưa xác minh:
```

Giữ cả lần thất bại và lần sửa thành công giúp phân biệt “đã tìm được nguyên nhân” với “vô tình thấy kết quả đúng”. Nếu log chứa thông tin cá nhân do môi trường máy, che hoặc loại phần đó trước khi chia sẻ; dữ liệu bài tập vẫn phải hoàn toàn giả.

**Speaker Notes:** Đưa một diff giả định sửa đúng vòng lặp nhưng thêm đổi cấu hình. Hỏi lớp có chấp nhận cả gói không. Đáp án mong đợi là tách phần ngoài phạm vi, không đổi quyền để khiến Agent làm nhanh hơn.

### 2.8. Thực hành hai nhánh, đáp án ca biên và tự đánh giá

#### 2.8.1. Bài thực hành Minh: từ 42000 đến 60000

**Thời lượng:** 15–20 phút nếu có môi trường C++. **Đầu ra:** bản sửa và ghi chép, không chỉ executable.

1. Mở bản sao `nam-1-cpp`, kiểm tra file, vị trí terminal và checkpoint.
2. Dùng Ask đọc `loi-bo-sot.cpp`. Ghi dự đoán với ba khoản giả vào `ghi-chep-02.txt`.
3. Trace `n = 1, 3`; chỉ rõ lượt bỏ Vở ghi.
4. Có compiler thì biên dịch bản lỗi ra executable riêng, chạy và lưu output; thiếu thì ghi “dự đoán, chưa chạy”.
5. Chỉ sửa điều kiện vòng lặp; xem diff nếu nhờ Agent. Save `loi-bo-sot.cpp` trong **bản sao**.
6. Biên dịch lại thành công rồi mới chạy; không dùng executable cũ sau lỗi biên dịch.
7. Kiểm tra bảng dưới. Chú ý: `loi-bo-sot.cpp` **không có tham số `--test`** và dữ liệu nằm cố định trong dòng `std::vector<long long> amounts = {35000, 7000, 18000};`. Muốn thử ca khác, sửa đúng dòng đó trong bản sao, ví dụ `= {}` cho ca C1 hoặc `= {7000}` cho ca C2, rồi biên dịch lại. Các ca còn lại có thể làm bằng trace; ghi rõ ca nào đã chạy, ca nào chỉ trace.
8. Lưu `ghi-chep-02.txt` cùng bản sao: trace, lệnh, kết quả, exit code, phần chưa kiểm chứng. Giữ `vi_sinh_vien.cpp` gốc để đối chiếu; chín ca trong bảng dưới trùng ý với `vi_sinh_vien --test`.

| Ca | Input tiền | Đáp án đúng | Lõi sai `i < n - 1` | Ý nghĩa |
|---|---|---:|---:|---|
| C1 | Rỗng, `n = 0` | 0 | 0 | Qua ca này chưa đủ |
| C2 | `[7000]` | 7000 | 0 | Bắt lỗi bỏ khoản duy nhất; trùng ca `mot khoan` trong `--test` |
| C3 | `[35000,7000,18000]` | 60000 | 42000 | Ca xuyên suốt chương |
| C4 | `[1]` | 1 | 0 | Biên nhỏ nhất hợp lệ |
| C5 | `[1000000000]` | 1000000000 | 0 | Biên lớn nhất mỗi khoản |
| C6 | 500 khoản, mỗi khoản 1000000000 | 500000000000 | 499000000000 | Giới hạn số lượng và kiểu tổng |
| C7 | Một khoản 0 hoặc -1 | Từ chối | Không dùng lõi để hợp thức hóa | Kiểm tra đầu vào |
| C8 | Một khoản 1000000001 | Từ chối | Không có tổng hợp lệ | Vượt giới hạn mỗi khoản |
| C9 | 501 khoản hợp lệ | Từ chối | Không có tổng hợp lệ | Vượt giới hạn số lượng |

C7–C9 kiểm tra chương trình xử lý dữ liệu, không chỉ hàm cộng đã giả định đầu vào hợp lệ. Nếu chỉ trace lõi, phải ghi rõ chưa xác minh bước từ chối. Đáp án sửa lỗi cận là `for (int i = 0; i < n; ++i)`; không phải cộng riêng `amounts[n - 1]`, vì cách vá đó cần xử lý rỗng và che mất nguyên nhân.

#### 2.8.2. Bài thực hành Lan: dữ liệu đúng trước giao diện đẹp

**Thời lượng:** 15–20 phút. **Đầu ra:** sơ đồ, kết quả test nếu đủ công cụ, biên bản thử trình duyệt. Không cần sửa demo đã đúng.

1. Mở bản sao `nam-2-web`, xác nhận bốn file cùng thư mục; mở trực tiếp `index.html`.
2. Ghi trạng thái ban đầu. Lần mở đầu tiên, `app.js` nạp sẵn ba khoản mẫu nên bảng đã có 60000; **đừng nhập thêm ba khoản nữa** rồi tưởng tổng 120000 là lỗi. Nếu trước đó bạn đã xóa hết, hãy nhập lại ba khoản giả.
3. Dùng Ask đọc form, `app.js`, `data.js`; vẽ sơ đồ với tên phần tử thực tế và ghi rõ sự kiện nào gắn vào đâu (xem 2.5.2 về hàm vô danh).
4. Chạy hoặc trace lỗi biệt lập `x.value` ở 2.5; ghi nguyên nhân NaN. Không chèn lỗi vào demo.
5. Thử bảng W; giá trị sai không được thêm hoặc làm đổi tổng. Chỉ dùng dữ liệu giả.
6. Có Node.js thì chạy `node test_data.cjs`, ghi exit code và ca thực sự được kiểm tra; thiếu thì ghi chưa chạy.
7. Xác nhận tổng ba khoản là 60000 VND; phân biệt dấu định dạng hiển thị với ký tự nhập.
8. Ghi cảnh báo lưu trữ, thử tải lại. Fallback bộ nhớ có thể mất dữ liệu; không nhận đã lưu bền vững.
9. Lưu `ghi-chep-02.txt` trong bản sao `nam-2-web`. Nếu sửa lỗi thật, Save đúng file được duyệt, giữ diff; nếu đã đúng, ghi “không thay mã”.

| Ca parseAmount | Chuỗi đưa vào | Đáp án theo hợp đồng |
|---|---|---|
| W1 | `"35000"` | Số 35000 |
| W2 | `" 7000 "` | Số 7000 sau trim |
| W3 | `"1"` | Chấp nhận, biên dưới |
| W4 | `"1000000000"` | Chấp nhận, biên trên |
| W5 | `"0007"` | Số 7; vẫn là chuỗi chữ số hợp lệ |
| W6 | `""`, `"   "` | Từ chối vì rỗng sau trim |
| W7 | `"0"`, `"-1"`, `"+1"` | Từ chối: giá trị 0 hoặc có dấu |
| W8 | `"1.5"`, `"35.000"`, `"35,000"` | Từ chối: không chỉ gồm chữ số |
| W9 | `"1e3"`, `"12abc"`, `"35 000"` | Từ chối: sai dạng chuỗi |
| W10 | `"1000000001"`, `"9007199254740992"` | Từ chối: vượt miền cho phép |

Một số kiểu ô nhập có thể ngăn hoặc biến đổi ký tự trước khi gọi hàm. Vì thế cần phân biệt kiểm tra trực tiếp `parseAmount` với thử qua form. “Không gõ được chữ vào ô” chưa chứng minh hàm dữ liệu tự kiểm tra đầy đủ.

| Ca totalExpenses | Danh sách/amount | Đáp án |
|---|---|---|
| T1 | Danh sách rỗng | 0 |
| T2 | Ba Expense giả của chương | 60000 |
| T3 | Một khoản amount là số 1 | 1 |
| T4 | 500 khoản amount đều là số 1000000000 | 500000000000 |
| T5 | 501 khoản hợp lệ | Từ chối vì quá số lượng |
| T6 | amount là chuỗi `"35000"` | Từ chối; hàm tổng không nhận chuỗi thay số |
| T7 | amount là 0, -1, 1.5 hoặc 1000000001 | Từ chối giá trị không hợp lệ |
| T8 | amount thiếu, `undefined`, `NaN` hoặc `Infinity` | Từ chối, không cho tổng NaN lọt ra |

“Từ chối” nghĩa là API/ứng dụng báo không hợp lệ theo cơ chế đã triển khai và không ghi nhận khoản sai; không áp đặt một câu thông báo nguyên văn. Đọc `test_data.cjs` để biết cách bộ test bắt trường hợp lỗi. Không tự sửa test thành chấp nhận input sai cho dễ đạt.

#### 2.8.3. Câu hỏi kiểm tra và đáp án ngắn

**Câu 1:** Rỗng ra 0 có chứng minh vòng lặp đúng không? **Đáp án:** Không. Cả bản sai và đúng đều không chạy với `n = 0` kiểu `int`; cần thêm ca một phần tử.

**Câu 2:** `input.value` của ô số là số nguyên đúng không? **Đáp án:** Không, nó là chuỗi. Phải qua `parseAmount` và kiểm tra hợp đồng trước khi đặt vào `Expense.amount`.

**Câu 3:** `x.value` không có thì kết quả tổng là `undefined`? **Đáp án:** Thuộc tính thiếu là `undefined`; phép cộng trong ví dụ tạo NaN, tức Not-a-Number. Hai giá trị không đồng nhất.

**Câu 4:** Node test qua có chứng minh localStorage lưu được không? **Đáp án:** Không. Cần kiểm tra trong trình duyệt; môi trường file trực tiếp có thể chặn lưu và kích hoạt fallback bộ nhớ.

**Câu 5:** AI nói “đã sửa” thì có được nộp ngay? **Đáp án:** Chưa. Cần xem diff, biết file đã lưu, chạy hoặc ghi rõ chưa chạy các phép kiểm tra, giữ bằng chứng thất bại nếu có.

#### 2.8.4. Rubric tự đánh giá

Tự chấm mỗi tiêu chí 0–2 điểm. Đây là rubric tự học, không thay thang điểm chính thức của môn. Có thể chọn một nhánh để thực hiện sâu nhưng vẫn giải thích được các lỗi chính của nhánh còn lại.

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| Hiểu công cụ | Trộn IDE, shell, CLI | Phân biệt được một phần | Gọi đúng vai trò và đúng shell |
| Giới hạn Agent | Cho sửa tùy ý | Có giới hạn nhưng thiếu kiểm tra | Ask trước, phạm vi nhỏ, xem diff |
| Giải thích lỗi | Chỉ chép đáp án | Nêu nguyên nhân, thiếu trace | Trace đúng, giải thích cả ca biên |
| Bằng chứng kiểm thử | Chỉ nói “chạy rồi” | Có output, thiếu ngữ cảnh | Có input, lệnh/thao tác, kết quả và trạng thái |
| An toàn và trung thực | Dữ liệu thật hoặc bịa đã chạy | Có ghi thiếu sót nhưng chưa đủ | Dữ liệu giả, checkpoint, phần chưa chạy rõ ràng |

Từ 8–10 điểm: có thể chuyển tiếp và vẫn giữ thói quen kiểm chứng. Từ 5–7: làm lại tiêu chí thấp nhất trước khi tăng độ khó. Dưới 5: quay lại thao tác mở đúng thư mục và trace một phần tử. Thiếu compiler không phải lý do bịa log; ghi trung thực phần chưa chạy tốt hơn nhận đạt không có căn cứ.

#### 2.8.5. Tóm tắt chương

Editor, IDE, Web chat và Agent bổ sung nhau. Qoder IDE là công cụ chính của demo; Ask giúp bắt đầu chỉ đọc; Agent chỉ thực hiện trong phạm vi và quyền cho phép. Terminal hiển thị, shell diễn giải, CLI thực hiện lệnh; luôn kiểm tra vị trí và loại shell.

Minh biết dùng trace để sửa cận vòng lặp, không vá bằng cộng bù khoản cuối. Lan biết `.value` là chuỗi, `amount` là trường tiền và NaN không phải undefined. Hai bạn thống nhất tiền nguyên dương tối đa 1e9 mỗi khoản, tối đa 500 khoản, rỗng tổng 0; ba khoản giả luôn có tổng đúng 60000.

Thói quen mang sang chương sau là: **quan sát → dự đoán → thay đổi nhỏ → kiểm tra → ghi bằng chứng**. Không có lượt chạy thì nói chưa chạy. Không có quyền thì dừng, không vượt chặn. Không có lý do rõ ràng thì không mở rộng hệ thống.

**Speaker Notes:** Kết thúc bằng phần trình bày một phút mỗi nhóm: lỗi gì, sửa ở đâu, bằng chứng nào, còn gì chưa kiểm chứng. Khen cách báo cáo trung thực, không chỉ khen màn hình hiện tổng đúng. Nhắc điểm nối CSDL/SQL để dành Chương 4.

#### Nguồn chính thức dùng cho thao tác Qoder

Các thông tin sản phẩm bên trên dựa trên tài liệu đã đối chiếu ngày 29/10/2026; không phải xác nhận giao diện hoặc chính sách hiện có trên máy người học.

- Qoder IDE, mở dự án, Ctrl+L và Ask/Agent: <https://docs.qoder.com/quick-start.md>.
- Ask chỉ đọc và gợi ý mã: <https://docs.qoder.com/user-guide/chat/ask.md>.
- Agent, công cụ, View Changes và accept/reject: <https://docs.qoder.com/user-guide/chat/agent.md>.
- Ngữ cảnh `@`, file/folder và Add to Chat: <https://docs.qoder.com/user-guide/chat/context.md>.
- Terminal và vị trí xem chính sách Auto-Run: <https://docs.qoder.com/user-guide/editor/terminal.md>.
- Qoder CLI, điều kiện sử dụng và lệnh hiện hành: <https://docs.qoder.com/cli/quickstart.md>.
- Qoder Desktop độc lập, Coding/General: <https://docs.qoder.com/qoder/overview.md>.


---

## CHƯƠNG 3. HỌC CÙNG AI, KHÔNG GIAO VIỆC HỌC CHO AI

Minh học năm nhất, vừa làm quen C++. Lan học năm hai, đang học lập trình hướng đối tượng (OOP), cấu trúc dữ liệu và giải thuật (DSA), cơ sở dữ liệu (CSDL) và Web. Hai bạn cùng xây **ViSinhVien**, một dự án quản lý chi tiêu nhỏ. Minh làm chương trình dòng lệnh tính tổng; Lan làm giao diện Web. Cả hai có thể nhờ AI, nhưng phải giữ lại công việc quan trọng nhất: tự hiểu bài toán, đưa ra dự đoán, sửa sai và chứng minh kết quả.

Chương này không yêu cầu bạn đã code tốt. Mục tiêu của cẩm nang là giúp bạn biết bắt đầu khi chưa hiểu, hỏi mà không mất cơ hội suy nghĩ, và tự làm lại một việc tương tự. Đây không phải chuẩn đầu ra hay quy định chính thức của trường. Việc được dùng AI đến đâu trong bài tập, kiểm tra và bài nộp phải theo quy định của từng học phần.

### 3.1. Tận dụng AI hay lạm dụng AI: nhìn vào việc mình còn phải làm

#### Bộ dữ liệu và hợp đồng chung của ViSinhVien

Mọi khoản chi dưới đây đều là **dữ liệu giả**, không phải lịch sử chi tiêu của sinh viên thật. Hai bạn thống nhất dùng cùng một bộ mẫu xuyên suốt:

| id | title | amount | category |
|---|---|---:|---|
| 1 | Cơm trưa | 35000 | `an-uong` |
| 2 | Xe buýt | 7000 | `di-lai` |
| 3 | Vở ghi | 18000 | `hoc-tap` |

Một đối tượng `Expense` có bốn trường `id`, `title`, `amount`, `category`. `amount` là **số nguyên VND**, mỗi khoản phải lớn hơn 0 và không quá `1000000000` (`1e9`). Danh sách có tối đa 500 khoản; danh sách rỗng có tổng bằng 0. Tổng mẫu là `35000 + 7000 + 18000 = 60000`. Vòng lặp bỏ phần tử cuối chỉ cho `42000`.

Đó là “hợp đồng” của bài: điều kiện đầu vào và kết quả chương trình phải bảo đảm. Trong C++, tổng dùng `long long`, vì tổng lớn nhất là `500000000000`, vượt khả năng biểu diễn của số nguyên có dấu 32 bit. Trong JavaScript, giới hạn này nằm trong miền số nguyên biểu diễn chính xác của `Number`. Không dùng chuỗi có dấu phân cách như `"35.000"` để lưu tiền; định dạng hiển thị là việc riêng.

Bản năm nhất là CLI C++; bản năm hai gồm HTML và JavaScript nhiều file, lưu bằng `localStorage` trong trình duyệt. Bản Web **không có backend, đăng nhập thật hay SQLite tích hợp**. Lan có thể học SQL/SQLite bằng một bài CSDL riêng dùng cùng dữ liệu giả; đó không phải nơi ứng dụng Web này lưu dữ liệu.

#### Sáu tình huống có ranh giới và vùng xám

“Tận dụng” là dùng AI để hỗ trợ trong khi bạn vẫn thực hiện phần học cần thiết. “Lạm dụng” ở đây là để AI thay thế phần suy nghĩ mà bài đang yêu cầu bạn luyện. Không thể chỉ nhìn thấy một đoạn code do AI gợi ý rồi kết luận ngay về tính liêm chính; cần xét nhiệm vụ, cách sử dụng và quy định học phần.

| Tình huống | Tận dụng để học | Dấu hiệu giao việc học cho AI | Vùng xám cần kiểm tra |
|---|---|---|---|
| 1. Minh không hiểu lỗi biên dịch | Đưa lỗi và đoạn code tối thiểu, tự diễn giải lại nguyên nhân sau gợi ý. | Dán cả bài, thay toàn bộ bằng bản AI viết mà không đọc. | Một bản vá nhỏ vẫn có thể không được phép trong bài đánh giá cấm AI. |
| 2. Minh học vòng lặp | Xin câu hỏi về chỉ số, tự trace ba khoản. | Xin luôn lời giải và học thuộc đoạn lặp. | Được xem ví dụ mẫu nhưng bài nộp có thể yêu cầu tự xây thuật toán. |
| 3. Lan đọc tài liệu tiếng Anh | Xin giải nghĩa thuật ngữ rồi đối chiếu đoạn gốc. | Tin bản tóm tắt, bỏ qua điều kiện và tự nhận đã đọc tài liệu. | Dịch hỗ trợ thường khác với để AI viết toàn bộ phần phân tích được chấm điểm. |
| 4. Lan viết kiểm thử | Tự dự đoán trước, nhờ AI tìm trường hợp còn thiếu. | Chấp nhận cả hàm và test từ cùng một câu trả lời mà không kiểm tra kỳ vọng. | Học phần có thể cho tạo test bằng AI nhưng yêu cầu khai báo cách dùng. |
| 5. Hai bạn làm giao diện | Nhờ tạo khung HTML không phải trọng tâm, rồi tự nối luồng dữ liệu. | Không biết nút Lưu gọi hàm nào, vẫn coi là đã làm chủ Web. | Nếu mục tiêu đang là học HTML, tạo sẵn khung có thể bỏ qua chính kỹ năng cần luyện. |
| 6. Chuẩn bị bài nộp nhóm | Thống nhất phần được hỗ trợ, mỗi người giải thích phần mình phụ trách. | Dùng AI hoàn thành phần chưa làm rồi ghi nhận như tự làm hoàn toàn. | Quy định nhóm, yêu cầu ghi nhận hỗ trợ và hình thức đánh giá có thể khác nhau. |

Trước mỗi việc, hỏi: “Bài đang luyện gì? AI làm phần nào? Mình phải tự chứng minh điều gì?” Nếu chưa rõ quyền sử dụng, đọc hướng dẫn và hỏi giảng viên trước khi dùng cho bài nộp. Không lấy lời AI làm căn cứ. Khi cần ghi nhận hỗ trợ, nêu đúng phạm vi: “AI gợi ý kiểm tra điều kiện dừng; tôi tự sửa và kiểm thử”.

#### Một quyết định nhỏ trước khi mở khung chat

Minh chọn luyện điều kiện dừng: được tra cách in nhưng không xin vòng lặp hoàn chỉnh. Lan chọn luyện kiểu dữ liệu: được tra cú pháp nhưng phải tự chỉ ra lúc chuỗi trở thành số. Một mục tiêu cụ thể giúp đặt giới hạn cho AI.

### 3.2. Vibe coding có kiểm soát: chạy được là khởi đầu, chưa phải kết thúc

#### Hai cách cùng tạo ra một màn hình

Ở đây, “vibe coding” chỉ cách mô tả mong muốn bằng ngôn ngữ tự nhiên, để AI đề xuất code rồi chỉnh qua nhiều lượt. Dựng thử nhanh không tự chứng minh người làm hiểu chương trình.

Lan có thể yêu cầu cả giao diện, nhận hàng trăm dòng rồi bấm chạy. Khi sai, bạn lại gửi “sửa hết giúp tôi”: thay đổi rộng dần nhưng vẫn không biết dữ liệu đi đâu. Cách có kiểm soát bắt đầu bằng phân công: `index.html` chứa giao diện, `data.js` xử lý dữ liệu, `app.js` nối sự kiện và lưu trữ. Lan chỉ làm phần kiểm tra tiền trước: một thay đổi, một dự đoán, vài test; xong mới sang việc tiếp.

#### Hiểu code không có nghĩa là học thuộc mọi API

Bạn có thể quên tên phương thức hoặc cần tra cú pháp. Điều cần nắm là **đầu vào, đầu ra, luồng đi và điều kiện đúng**. Với `localStorage.setItem`, Lan không nhất thiết thuộc lòng toàn bộ tài liệu, nhưng cần giải thích được: giá trị lưu là chuỗi; phải chuyển dữ liệu sang JSON; khi đọc phải phân tích JSON và kiểm tra lại; thao tác có thể lỗi nên giao diện không được báo đã lưu khi thực tế chưa lưu được.

Tương tự, Minh có thể tra cách khai báo `vector`, nhưng phải biết danh sách ba phần tử có chỉ số 0, 1, 2. Nếu không nhớ một tên API, bạn tra rồi tiếp tục. Nếu không biết vì sao phần tử số 2 chưa được cộng, bạn cần dừng để trace, không chỉ tìm tên hàm khác.

Dùng bốn câu hỏi để kiểm tra một đoạn code mới:

1. Nó nhận dữ liệu gì, ở kiểu nào, từ đâu?
2. Nó thay đổi hoặc trả về điều gì?
3. Nó dựa vào điều kiện nào của hợp đồng?
4. Tôi tạo được một ca khiến nó sai nếu bỏ một điều kiện không?

#### Chốt kiểm soát trước khi nhận thay đổi

Minh chỉ sửa điều kiện vòng lặp, không nhận đề xuất thêm menu, con trỏ hay tách lớp cùng lúc. Lan từ chối thư viện, dịch vụ ngoài, đăng nhập và SQLite nằm ngoài phạm vi. Cả hai có thể yêu cầu: “Giữ cấu trúc, chỉ giải thích vấn đề đang xét.”

Sau thay đổi, chỉ vào dòng liên quan, dự đoán rồi chạy. Nếu chưa giải thích được toàn bộ file, làm chủ hàm vừa sửa trước; không cần giả vờ hiểu hoặc xóa mọi tiến bộ đã có.

### 3.3. Một phiên 25 phút: tự thử, dự đoán, hỏi ít và kiểm chứng

#### Chuẩn bị mục tiêu vừa sức

Phiên 25 phút dưới đây là giới hạn cho một hoạt động học, không phải công cụ chẩn đoán khả năng, sự tập trung hay sức khỏe. Bạn có thể điều chỉnh thời lượng theo điều kiện cá nhân. Hết giờ mà chưa xong không có nghĩa là không phù hợp với ngành; hãy thu nhỏ nhiệm vụ và ghi lại điểm đang vướng.

Chọn **một** mục tiêu: Minh tìm vì sao tổng là `42000`; Lan tìm vì sao cộng tiền lại thành chuỗi. Mở đúng file liên quan, đặt bộ dữ liệu giả bên cạnh, tắt các yêu cầu mở rộng. Chưa cần tài khoản trả phí; nếu không dùng được AI, phần gợi ý trong chương có thể thay vai trò người hỏi.

#### Sáu bước với dấu vết học tập

| Thời gian | Việc bạn làm | Dấu vết cần giữ |
|---|---|---|
| Phút 0–4: tự thử | Đọc đề, làm một cách dù chưa hoàn chỉnh. | Một đoạn code hoặc mô tả thuật toán tự viết. |
| Phút 4–7: dự đoán | Tính tay kết quả, ghi nơi nghi ngờ. | `60000`, các chỉ số cần đi qua, hoặc kiểu dữ liệu dự kiến. |
| Phút 7–11: xin gợi ý | Chỉ gửi phần liên quan, xin một câu hỏi mỗi lượt. | Câu hỏi của AI và câu trả lời do bạn nghĩ. |
| Phút 11–16: tự sửa | Sửa một nguyên nhân đã giải thích được. | Dòng thay đổi và lý do, không chỉ bản code mới. |
| Phút 16–21: kiểm chứng | Chạy ca thường, biên và đầu vào sai. | Kỳ vọng, thực tế, kết luận cho từng ca. |
| Phút 21–25: biến thể không AI | Đóng chat, làm bài gần giống nhưng có thay đổi. | Bài tự làm và chỗ chưa chắc. |

**Tự thử** có thể bắt đầu bằng lời: Minh viết “cộng từ khoản đầu đến khoản cuối”; Lan vẽ “ô nhập → đối tượng → danh sách → tổng”. Phác thảo chưa đúng vẫn giúp câu hỏi bám vào suy nghĩ thật.

**Dự đoán** trước khi Chạy: Minh ghi `0 → 35000 → 42000 → 60000`; Lan ghi kiểu dữ liệu tại từng chặng. Chép kết quả sau khi chạy không thay thế bước này.

**Xin gợi ý** tối đa ba lượt cho một nút thắt trong phiên này, theo quy ước thực hành. Vẫn vướng thì giảm bài xuống một khoản hoặc trace bằng giấy, không đổi prompt liên tục để tìm lời giải.

**Tự sửa** cần lý do: “Cho vòng lặp tới chỉ số 2 vì đó là phần tử hợp lệ cuối.” Chỉ sửa một điểm. **Kiểm chứng** phải so sánh giá trị; “không có lỗi” chưa chứng minh tổng đúng.

#### Khi AI trả lời quá nhiều hoặc bạn đang mệt

Nếu AI lộ đáp án, không thể làm như mình chưa thấy. Dừng đọc, ghi “đã xem lời giải ở phần điều kiện dừng”, rồi đóng chat. Tự giải thích lại bằng trace, sau đó làm biến thể mới không nhìn đáp án. Đây là cách tiếp tục học trung thực, không phải hình phạt.

Nếu chưa tự làm được biến thể, đánh dấu “cần luyện tiếp”, không kéo dài vô hạn để đạt một dấu tích đẹp. Phiên sau bắt đầu từ điểm nhỏ hơn, chẳng hạn chỉ xác định các chỉ số hợp lệ. Khi cần hỏi bạn học hoặc giảng viên, mang theo đầu vào, kỳ vọng, thực tế và điều đã thử; xem Chương 2/4 để nối với các hoạt động liên quan của cẩm nang.

### 3.4. Tám prompt có thể sao chép, nhưng bạn vẫn phải trả lời

#### Cách dùng bộ prompt

Mỗi khối dưới đây đã có dữ liệu và yêu cầu cụ thể. Chọn một khối phù hợp, không gửi cả tám cùng lúc. Các prompt không bảo đảm AI luôn tuân thủ; phần xử lý lộ đáp án là việc **bạn chủ động làm**. Chỉ dùng dữ liệu giả, không thêm thông tin cá nhân, bài kiểm tra đang bị cấm hỗ trợ hoặc nội dung không được phép chia sẻ.

#### Prompt 1 — Hỏi kiểu Socratic: dẫn bằng câu hỏi

```text
Tôi là Minh, năm 1, học C++. ViSinhVien có các Expense
(id, title, amount, category), tiền là số nguyên VND, mỗi khoản
>0 và <=1e9, tối đa 500 khoản; rỗng có tổng 0.
Dữ liệu giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000.
Tôi cần hiểu vì sao vòng lặp bỏ khoản cuối cho 42000 thay vì 60000.
Hãy hỏi kiểu Socratic, một câu mỗi lượt, chờ tôi trả lời trước
khi hỏi tiếp. Bắt đầu từ chỉ số hợp lệ của ba phần tử.
Không viết vòng lặp đúng, không nói ngay điều kiện cần thay.
Bằng chứng cuối buổi: tôi tự nêu các chỉ số, trace tổng và
viết lý do sửa bằng lời của mình; bạn chỉ nhận xét chỗ thiếu.
Nếu bạn lỡ lộ đáp án, dừng giải thích và chuyển sang câu hỏi
mới với danh sách chỉ có Vở ghi 18000, không giải hộ.
```

Viết trước khi gửi. Nếu lộ đáp án, đóng phần đó, tự làm ca một khoản.

#### Prompt 2 — Ba mức gợi ý, không nhảy thẳng tới lời giải

```text
Tôi tự viết vòng lặp C++ cộng ViSinhVien nhưng đang bị 42000.
Ba khoản giả theo thứ tự: Cơm trưa=35000, Xe buýt=7000,
Vở ghi=18000; đúng phải là 60000. Hợp đồng: amount nguyên
VND, >0, <=1e9; tối đa 500 khoản; rỗng tổng 0.
Hãy chuẩn bị ba mức gợi ý: mức 1 chỉ vùng cần xem;
mức 2 hỏi quan hệ giữa chỉ số cuối và kích thước;
mức 3 cho bảng trace còn ô trống, không cho điều kiện sửa.
Chỉ đưa mức 1 bây giờ. Chỉ nâng mức khi tôi yêu cầu và đã
trình bày điều vừa thử. Không viết code thay tôi.
Bằng chứng mong đợi: tôi điền bảng và tự đề xuất một thay đổi.
Nếu lỡ đưa lời giải, báo rõ, dừng và giao một ca rỗng để tôi
phân tích độc lập, không kèm đáp án.
```

Sau mỗi mức, thử một hành động. Nếu lộ lời giải, ghi nhận rồi tự phân tích ca rỗng.

#### Prompt 3 — Trace giá trị và kiểu dữ liệu

```text
Tôi là Lan, học Web năm 2. Ứng dụng dùng HTML+JS và
localStorage, không backend. Bộ mẫu giả: Cơm trưa 35000,
Xe buýt 7000, Vở ghi 18000; tổng hợp lệ 60000.
Tôi đang mô phỏng lỗi bằng amount là các chuỗi "35000",
"7000", "18000" và biến total bắt đầu là số 0.
Mỗi lượt tôi làm total = total + expense.amount.
Hãy cho bảng trống: lượt, kiểu total trước, kiểu amount,
phép toán, total sau. Chờ tôi điền từng hàng rồi nhận xét.
Không điền hộ toàn bảng, không viết hàm chuyển kiểu.
Hợp đồng đích: amount là số nguyên VND >0 <=1e9,
tối đa 500 khoản, rỗng tổng 0.
Bằng chứng: tôi chỉ ra lượt đầu đổi kiểu và nơi cần kiểm tra
đầu vào. Nếu bạn lộ đáp án, dừng; cho tôi tự trace chỉ "18000".
```

Giữ dấu ngoặc kép của chuỗi. Nếu AI điền hộ, che bảng, trace lại một khoản và nêu kiểu.

#### Prompt 4 — Review một thay đổi nhỏ

```text
Tôi là Minh. Dữ liệu giả ViSinhVien: 35000, 7000, 18000 VND,
tổng 60000; vòng lặp trước bỏ khoản cuối nên ra 42000.
Tôi đã đổi điều kiện từ i < n - 1
sang i < n, với int n là số khoản, int i và long long total.
Hợp đồng đầu vào: Expense có id,title,amount,category;
amount nguyên >0 <=1e9, tối đa 500 khoản; rỗng tổng 0.
Hãy review đúng thay đổi này: hỏi tôi chứng minh giới hạn
chỉ số và chọn test. Không viết lại hàm, không thêm tính năng.
Bằng chứng: tôi giải thích ca ba khoản, một khoản, rỗng
và vì sao cần long long. Chỉ kết luận sau khi tôi trả lời.
Nếu bạn viết lời giải đầy đủ, dừng và yêu cầu tôi tự so sánh
hai điều kiện với kích thước 1, không cung cấp bảng điền sẵn.
```

Nếu AI viết cả hàm, đừng thay file; tự kiểm tra hai điều kiện với kích thước 1.

#### Prompt 5 — Thiết kế test trước khi viết code

```text
Tôi là Lan. Chưa viết hàm tính tổng ViSinhVien.
Expense có id,title,amount,category; amount phải là số nguyên
VND >0 <=1e9, tối đa 500 khoản; rỗng trả 0.
Bộ giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000,
tổng 60000. Hàm phải từ chối amount chuỗi và danh sách quá dài.
Hãy yêu cầu tôi đề xuất lần lượt ca thường, biên, dữ liệu sai.
Không viết code hàm hoặc test tự động; không tính hộ kỳ vọng.
Sau mỗi ca tôi nêu, chỉ hỏi lý do hoặc chỉ ra loại ca còn thiếu.
Bằng chứng: bảng do tôi điền gồm đầu vào, kỳ vọng, lý do,
bao gồm giới hạn 500 khoản. Nếu bạn lộ code hay đáp án,
dừng; yêu cầu tôi tự tính ca 500 khoản đều bằng 1e9.
```

Tự tính kỳ vọng từng test. Nếu lộ lời giải, tính lại ca giới hạn lớn khi đóng chat.

#### Prompt 6 — Giải thích tài liệu tiếng Anh có đối chiếu

```text
Tôi là Lan, làm Web ViSinhVien lưu localStorage, không backend.
Đây là câu tiếng Anh do cẩm nang tự soạn để luyện đọc,
không phải trích nguyên văn tài liệu chính thức:
"The value of a text input is a string. Convert and validate
it before storing an expense amount."
Ví dụ giả: ô nhập chứa "35000" cho Cơm trưa;
Expense.amount phải là số nguyên VND >0 <=1e9.
Hãy giải nghĩa value, string, convert, validate trong ngữ cảnh,
rồi hỏi tôi diễn giải câu trên bằng tiếng Việt và nêu một ca sai.
Không viết hàm xử lý, không bịa nguồn hay nhận là đã tra tài liệu.
Bằng chứng: tôi phân biệt chuyển kiểu với kiểm tra hợp lệ.
Nếu bạn lộ code, dừng và hỏi tôi phân tích đầu vào "35000abc"
bằng lời, không cho kết luận sẵn.
```

Với tài liệu thật, giữ nguồn để đối chiếu. Nếu lộ code, đóng nó, tự phân tích chuỗi có chữ.

#### Prompt 7 — Vấn đáp như người hướng dẫn

```text
Tôi đã học hai lỗi ViSinhVien: vòng lặp bỏ cuối ra 42000
thay vì 60000, và amount chuỗi làm phép + nối ký tự.
Bộ giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000 VND.
Hợp đồng: Expense có id,title,amount,category; amount nguyên
>0 <=1e9, tối đa 500 khoản; rỗng tổng 0.
Hãy vấn đáp từng câu: một câu về chỉ số, một câu về kiểu,
một câu về test, một câu về localStorage của bản Web.
Chờ câu trả lời, hỏi tiếp nếu tôi mơ hồ; không trả lời thay,
không đánh giá năng lực tổng quát hay đoán điểm học phần.
Bằng chứng: tôi trả lời bằng ví dụ, được ghi rõ chỗ cần luyện.
Nếu bạn lộ đáp án, bỏ câu ấy khỏi đánh giá và hỏi một câu
biến thể mới không kèm gợi ý trong lượt đầu.
```

Trả lời bằng ví dụ. Câu đã thấy đáp án chỉ dùng ôn, không làm bằng chứng tự làm.

#### Prompt 8 — Tự kiểm tra sau khi đóng chat

```text
Tôi muốn tự kiểm tra, không nhận lời giải. ViSinhVien dùng
ba khoản giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000.
Contract: amount nguyên VND >0 <=1e9, tối đa 500; rỗng tổng 0.
Hãy giao hai nhiệm vụ ngắn: C++ tìm khoản tiền lớn nhất,
quy ước rỗng trả 0; JS lọc theo category rồi tính tổng,
nhưng vẫn phải kiểm tra toàn bộ danh sách đầu vào.
Không cung cấp thuật toán, code, kết quả mẫu hay gợi ý ngay.
Tôi sẽ đóng chat, làm 4 phút, rồi gửi bài và dự đoán.
Bằng chứng: bạn đối chiếu lập luận, ca thường, ca rỗng,
và chỉ ra đúng phần chưa chứng minh. Không chấm điểm học phần.
Nếu bạn lộ đáp án, đổi nhiệm vụ sang kiểm tra tính bất biến
của tổng khi đảo thứ tự; không nói trước kết quả.
```

Chưa xong thì giữ bản để tiếp tục. Nếu lộ đáp án, đóng chat, tự làm nhiệm vụ thay thế.

### 3.5. Hai cuộc hội thoại minh họa: sinh viên nghĩ trước, thầy gợi ý sau

#### Ca năm nhất: Minh tìm khoản chi bị bỏ quên

**Đây là hội thoại giả định do cẩm nang xây dựng, không phải log thật.** Vai “Thầy” có thể do người hướng dẫn đảm nhận; khi dùng AI, yêu cầu AI chỉ đóng vai người hỏi, không tự nhận là giảng viên của bạn.

Minh đang xem đoạn **cố ý có lỗi để luyện debug** trích từ `loi-bo-sot.cpp`. `amounts` là `vector<long long>` chứa ba số tiền, `total` bắt đầu bằng 0:

```cpp
int n = static_cast<int>(amounts.size());
// CỐ Ý SAI: điều kiện này bỏ phần tử cuối.
for (int i = 0; i < n - 1; ++i) {
    total += amounts[i];
}
```

`amounts.size()` cho số phần tử. Ở bài này đã giới hạn tối đa 500 khoản, nên chuyển kích thước sang `int` để học chỉ số là phù hợp; không áp dụng tùy tiện cách chuyển này cho danh sách lớn không có giới hạn.

**Minh:** Em tính tay được 60000, máy in 42000. Em đoán máy chưa cộng Vở ghi, nhưng chưa biết vì sao.

**Thầy:** Chưa sửa vội. Ba phần tử có các chỉ số nào?

**Minh:** Em nghĩ 1, 2, 3... Khoan, `vector` bắt đầu từ 0, vậy là 0, 1, 2.

**Thầy:** Bây giờ `n` bằng mấy và điều kiện ở lượt đầu là gì?

**Minh:** `n = 3`, vậy `n - 1 = 2`. Với `i = 0`, `0 < 2` đúng; cộng Cơm trưa được 35000.

**Thầy:** Em tự làm lượt tiếp theo, chưa nhìn kết quả chạy.

**Minh:** `i = 1`, `1 < 2` đúng; cộng Xe buýt thành 42000. Nhưng khi `i = 2`, `2 < 2` sai. Chưa cộng Vở ghi mà đã dừng. Vậy phép cộng không sai; em bỏ một số hạng.

Bảng Minh tự hoàn thành sau khi trả lời:

| Lần kiểm tra | i | Điều kiện lỗi | Khoản được cộng | total sau kiểm tra |
|---|---:|---|---|---:|
| 1 | 0 | `0 < 2`: đúng | Cơm trưa 35000 | 35000 |
| 2 | 1 | `1 < 2`: đúng | Xe buýt 7000 | 42000 |
| 3 | 2 | `2 < 2`: sai | Không có | 42000 |

**Thầy:** Em muốn chạy với các chỉ số nào, và không được đọc chỉ số nào?

**Minh:** Muốn chạy 0, 1, 2 và dừng trước 3. Em đề xuất `i < n`. Lúc `i = 2`, `2 < 3` đúng, cộng 18000 được 60000. Tăng lên 3 thì dừng, không đọc quá cuối.

**Thầy:** Nếu chỉ có Vở ghi, điều kiện cũ và mới khác nhau thế nào?

**Minh:** Điều kiện cũ là `0 < 0`, sai ngay nên tổng 0. Mới là `0 < 1`, cộng được 18000. Với danh sách rỗng, điều kiện mới `0 < 0` sai, tổng giữ 0.

Minh sửa một điều kiện rồi chạy ba ca. Bằng chứng học được là giải thích được **tại sao** thiếu khoản cuối và tự làm được ca một khoản, không chỉ có ảnh màn hình ghi 60000.

#### Ca năm hai: Lan phân biệt số tiền với chuỗi ký tự

**Đây cũng là hội thoại giả định.** Lan đã nhập ba khoản nhưng lưu `amount` trực tiếp từ `.value` của ô nhập. Trong ca lỗi này, dữ liệu đang là các chuỗi `"35000"`, `"7000"`, `"18000"`; chúng **vi phạm hợp đồng**, dù nhìn trên màn hình giống số.

**Lan:** Em cộng từ số 0, kết quả lại là `"035000700018000"`. Em định đổi `+` thành một hàm cộng khác.

**Thầy:** Trước khi đổi phép toán, em biết kiểu của giá trị ở ô nhập chưa?

**Lan:** Em thấy bàn phím nhập số nên nghĩ là số. Để em kiểm tra `typeof amountInput.value` trong Console... Kết quả là `"string"`.

**Thầy:** Với mô phỏng `total = total + expense.amount`, hãy dự đoán lượt đầu.

**Lan:** Bên trái là số 0, bên phải là chuỗi `"35000"`. Có chuỗi nên phép `+` nối lại thành `"035000"`, không phải số 35000.

**Thầy:** Sau lượt đầu, biến tổng còn là số không? Em tự hoàn thành hai lượt tiếp.

**Lan:** Không. Nó là chuỗi, rồi nối thêm `"7000"` thành `"0350007000"`, cuối cùng nối `"18000"` thành `"035000700018000"`.

| Lượt | total trước và kiểu | amount và kiểu | total sau và kiểu |
|---|---|---|---|
| 1 | `0`, number | `"35000"`, string | `"035000"`, string |
| 2 | `"035000"`, string | `"7000"`, string | `"0350007000"`, string |
| 3 | `"0350007000"`, string | `"18000"`, string | `"035000700018000"`, string |

**Thầy:** Theo hợp đồng, em muốn sửa ở đâu để mỗi hàm phía sau không phải đoán kiểu?

**Lan:** Ở biên nhập liệu: đọc chuỗi, kiểm tra cách viết, chuyển thành số, kiểm tra miền giá trị rồi mới tạo `Expense`. Hàm tính tổng vẫn từ chối dữ liệu sai nếu có đường khác đưa vào.

**Thầy:** Chỉ gọi `Number` đã đủ chưa? Em nghĩ về chuỗi rỗng và số âm.

**Lan:** Chưa. `Number("")` cho 0 nhưng khoản tiền phải dương. `Number("-7000")` cho số âm, cũng không hợp lệ. Em cần phân biệt chuyển được thành số với được phép là một khoản chi.

**Thầy:** Em đặt quy tắc nhập thế nào để người dùng không hiểu nhầm `35.000`?

**Lan:** Ô nhập sẽ hướng dẫn “nhập số nguyên VND, ví dụ 35000”. Em cho phép khoảng trắng ngoài cùng rồi bỏ đi; phần còn lại chỉ có chữ số. Từ chối dấu chấm, dấu phẩy, chữ và ký hiệu mũ. Đây là quy tắc của bài thực hành, không phải mọi ứng dụng tiền đều phải như vậy.

**Thầy:** Sau khi lưu rồi tải lại trang, còn cần kiểm tra không?

**Lan:** Có. `localStorage` giữ chuỗi JSON. Sau `JSON.parse`, em kiểm tra danh sách và `amount` lần nữa; dữ liệu cũ có thể vẫn chứa chuỗi. Nếu lỗi, phải thông báo, không âm thầm ghi đè dữ liệu cũ bằng danh sách rỗng.

Lan viết test trước khi sửa. Khi cả ba `amount` đã là số, trace đúng là `0 → 35000 → 42000 → 60000`. Bạn hiểu rằng 42000 ở đây chỉ là **tổng trung gian đúng**, còn ở ca Minh nó là **kết quả cuối sai**. Cùng một con số phải được đọc trong đúng thời điểm của chương trình.

### 3.6. Buổi thực hành: sửa ít, chứng minh rõ, lưu đúng chỗ

#### Mục tiêu, chuẩn bị và sản phẩm

Chọn một nhánh. **Mục tiêu:** tìm nguyên nhân, tự sửa, kiểm chứng, làm biến thể không AI. **Chuẩn bị:** bộ dữ liệu giả, trình soạn thảo, giấy ghi chú; Minh cần trình biên dịch C++, Lan cần trình duyệt hiện đại. Bản Web đi kèm dùng script thông thường, mở trực tiếp `index.html` với các tệp cùng thư mục, không cần máy chủ file tĩnh. Không mua tài khoản hay dịch vụ; AI là tùy chọn.

**Sản phẩm:** code, bảng kỳ vọng/thực tế và lời giải thích. **Đích lưu** trong bộ ví dụ:

- Năm nhất: bản sao của `vi-du/nam-1-cpp/loi-bo-sot.cpp` — đây là tệp có lỗi cần sửa. Giữ `vi-du/nam-1-cpp/vi_sinh_vien.cpp` nguyên trạng để đối chiếu đáp án, như quy ước ở mục 2.4.5.
- Năm hai: `vi-du/nam-2-web/index.html`, `vi-du/nam-2-web/data.js`, `vi-du/nam-2-web/app.js` và `vi-du/nam-2-web/test_data.cjs`.

Các đoạn dưới là lõi bài tập, không phải Web hoàn chỉnh. Bảng kiểm thử và phiếu cuối buổi ghi trong vở, không cần ảnh minh chứng.

#### Nhánh Minh: đề gốc và các bước làm

**Đề gốc:** sửa vòng lặp ở ca 3.5 để tính đúng tổng; bảo đảm rỗng trả 0, từ chối danh sách quá 500 khoản và khoản tiền ngoài miền hợp lệ. Bản C++ năm nhất chỉ dùng `vector<long long> amounts` chứa các số tiền, không yêu cầu `Expense` đủ bốn trường. Trọng tâm là số tiền và số lượng, chưa phải hệ thống kiểm tra mọi lỗi nhập bàn phím. Mô hình `Expense` bốn trường dùng ở bản Web; phần giải thích OOP nằm ở Chương 2, không cần tạo thêm file OOP cho bài này.

1. **Tự dự đoán:** viết tổng mẫu 60000, một khoản Vở ghi 18000, rỗng 0. Với vòng lặp lỗi, dự đoán tương ứng 42000, 0, 0.
2. **Khoanh nguyên nhân:** trace chỉ số như ca hội thoại. Chưa đọc đáp án phía dưới nếu đang tự thử.
3. **Tự sửa:** thay điều kiện theo lập luận của mình. Chọn kiểu tổng dựa trên giới hạn lớn nhất, không dựa vào ba khoản nhỏ.
4. **Kiểm chứng:** dùng bảng chung bên dưới, ghi cả kỳ vọng lẫn kết quả. Đầu vào sai phải bị từ chối chứ không được âm thầm bỏ qua khoản sai. `loi-bo-sot.cpp` dùng dữ liệu cố định và không có `--test`, nên muốn thử ca rỗng hoặc một khoản thì sửa dòng `std::vector<long long> amounts = {35000, 7000, 18000};` trong bản sao rồi biên dịch lại.
5. **Lưu và chạy lại:** lưu đúng file C++; biên dịch lại bản vừa sửa rồi chạy. Chạy một tệp thực thi cũ không chứng minh code mới đúng.

Nếu máy đã có `g++`, có thể chạy **từ thư mục gốc dự án** bằng **Bash trên Linux hoặc Git Bash trên Windows**; vì đứng ở gốc nên đường dẫn trong lệnh phải viết đầy đủ. Hai dòng đầu dùng bản đúng để xem đáp án mong đợi; dòng cuối chạy bộ kiểm thử 9 ca có sẵn:

```bash
g++ -std=c++17 "vi-du/nam-1-cpp/vi_sinh_vien.cpp" -o "vi-du/nam-1-cpp/vi_sinh_vien.exe"
"./vi-du/nam-1-cpp/vi_sinh_vien.exe"
"./vi-du/nam-1-cpp/vi_sinh_vien.exe" --test
```

Khi chạy bản bài làm của mình, thay đường dẫn nguồn bằng bản sao `loi-bo-sot.cpp` và đặt tên tệp thực thi khác, ví dụ `loi-bo-sot.exe`, để không lẫn với bản đúng. Mục 2.6.2 chạy cùng những lệnh này nhưng đứng **trong** thư mục `nam-1-cpp`, nên đường dẫn ngắn hơn; chọn một cách và kiểm tra vị trí bằng `pwd` trước khi gõ.
Cách chạy trên các nền tảng khác, gồm cú pháp **PowerShell**, xem Chương 2; không chép nguyên cú pháp Bash sang PowerShell. Nếu dùng IDE, dùng lệnh Build rồi Run tương ứng. Nếu thiếu trình biên dịch, tiếp tục trace trên giấy và dùng môi trường học tập sẵn có sau; đó là vấn đề chuẩn bị công cụ, chưa phải lỗi thuật toán.

#### Nhánh Lan: đề gốc và các bước làm

**Đề gốc:** ngăn tiền dạng chuỗi đi vào danh sách. Khi danh sách đang có Cơm trưa và Xe buýt, nhập Vở ghi với `"18000"` phải tạo `amount` số 18000, tổng thành 60000. Nhập sai phải hiện thông báo và giữ nguyên danh sách, tổng, dữ liệu đã lưu.

1. **Dự đoán luồng:** ghi kiểu ở từng chặng: ô nhập là chuỗi; qua kiểm tra thành số; vào `Expense`; qua tính tổng; chuyển cả danh sách thành JSON để lưu.
2. **Thiết kế test trước:** điền bảng, đặc biệt `""`, `"35000abc"`, `"35.000"`, `"0"`, `"1000000001"`. Chốt quy tắc chỉ nhận chữ số sau khi bỏ khoảng trắng ngoài cùng.
3. **Sửa lõi trong `data.js`:** tách hàm phân tích tiền khỏi hàm tổng. Hàm tổng không tự “chữa” chuỗi thành số, vì như vậy lỗi nguồn dữ liệu có thể bị che giấu.
4. **Nối trong `app.js`:** đọc ô nhập, tạo danh sách ứng viên và kiểm tra bằng `normalizeExpenses` trước khi cập nhật `expenses`. Dữ liệu sai phải bị từ chối, không được thêm vào danh sách. Với dữ liệu hợp lệ, bản demo cập nhật trong bộ nhớ rồi gọi `save()` và hiển thị lại. Nếu lưu trữ bị chặn hoặc hết dung lượng, ứng dụng vẫn cho thêm trong bộ nhớ nhưng phải báo rõ không lưu bền; “đã thêm” không có nghĩa là “đã lưu”.
5. **Kiểm tra trên trình duyệt:** thêm Vở ghi, kiểm tra tổng và thông báo lưu trữ, tải lại trang rồi đối chiếu. Khi đang dùng bộ nhớ tạm, không kỳ vọng thay đổi còn sau khi tải lại. Mở lại cùng file bằng cùng trình duyệt; với `file://`, khả năng lưu phụ thuộc trình duyệt. Nếu chạy qua HTTP, dùng cùng origin; khác giao thức, host hoặc cổng có thể là vùng lưu trữ khác. Không kết luận mất dữ liệu chỉ vì mở một địa chỉ khác.
6. **Lưu đúng vai trò:** `index.html` có ô nhập và nơi báo lỗi; `data.js` chứa logic; `app.js` xử lý DOM và lưu trữ. `test_data.cjs` là bộ kiểm thử logic chạy riêng bằng Node.js khi bộ demo đã được chuẩn bị, không phải script gắn vào trang.

Bản này lưu cục bộ trong trình duyệt, không đồng bộ đa thiết bị và không có tài khoản thật. Khi đọc dữ liệu cũ, cần bắt lỗi JSON, kiểm tra cấu trúc danh sách và các số tiền. Nếu không đọc được hoặc dữ liệu không hợp lệ, bản demo đặt `persistent = false`, dùng dữ liệu mẫu trong bộ nhớ và thông báo không ghi đè dữ liệu cũ. Nếu ghi thất bại, `save()` cũng đặt `persistent = false` và báo đang dùng bộ nhớ tạm; những lần thay đổi tiếp theo không thử ghi nữa trong phiên đó. Danh sách vẫn có thể thay đổi trong bộ nhớ, nhưng lỗi lưu trữ không được biến thành thông báo “đã lưu”.

#### Bảng kết quả phải đối chiếu

| Ca | Kỳ vọng | Lý do |
|---|---:|---|
| Ba khoản mẫu hợp lệ | 60000 | Cộng đủ cả ba khoản. |
| Chỉ Vở ghi 18000 | 18000 | Bắt được lỗi bỏ phần tử cuối. |
| Danh sách rỗng | 0 | Không có khoản để cộng. |
| Đảo thứ tự ba khoản | 60000 | Tổng không phụ thuộc thứ tự. |
| 500 khoản, mỗi khoản 1000000000 | 500000000000 | Kiểm tra giới hạn số lượng và kiểu tổng. |
| 501 khoản hợp lệ về tiền | Từ chối | Vượt giới hạn danh sách. |
| Một khoản 0, âm hoặc 1000000001 | Từ chối | Vi phạm miền tiền. |
| JS có `amount: "35000"` hoặc `1.5` | Từ chối | Không phải số nguyên hợp lệ theo hợp đồng. |
| Chuỗi nhập `" 35000 "` | Số 35000 | Cho phép khoảng trắng ngoài cùng. |
| Chuỗi nhập rỗng, `"35.000"`, `"35000abc"` | Từ chối | Không phù hợp quy tắc nhập đã chọn. |

“Từ chối” trong hàm là phát sinh lỗi; trong giao diện là bắt lỗi, báo rõ và không lưu thay đổi sai. Dòng test bị từ chối không có “tổng kỳ vọng” bằng 0; 0 chỉ là tổng của danh sách rỗng hợp lệ. Bảng này không kiểm tra mọi lỗi giao diện, nhưng đủ để đánh giá mục tiêu buổi học.

#### Đáp án tham khảo có lý giải: chỉ mở sau lượt tự làm

Lõi C++ dưới đây trích từ `vi-du/nam-1-cpp/vi_sinh_vien.cpp`, rút gọn phần `main` để đọc. Hàm `totalExpenses` kiểm tra miền tiền và số lượng; `main` dùng dữ liệu giả cố định, chưa triển khai nhập bàn phím. **Không chép đoạn này đè lên cả file:** bản đi kèm còn có `runTests()` và nhánh xử lý `--test`, được lược khỏi đoạn đọc này:

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>

long long totalExpenses(const std::vector<long long>& amounts) {
    if (amounts.size() > 500) {
        throw std::invalid_argument("Toi da 500 khoan chi");
    }
    long long total = 0;
    int n = static_cast<int>(amounts.size());
    for (int i = 0; i < n; ++i) {
        if (amounts[i] <= 0 || amounts[i] > 1000000000LL) {
            throw std::invalid_argument("Moi khoan: 1 den 1000000000 VND");
        }
        total += amounts[i];
    }
    return total;
}

int main() {
    const std::vector<long long> amounts = {35000, 7000, 18000};
    std::cout << "Com trua: 35000 VND\nXe buyt: 7000 VND\nVo ghi: 18000 VND\n";
    std::cout << "Tong chi tieu: " << totalExpenses(amounts) << " VND\n";
    return 0;
}
```

Điều kiện `i < n` xét đủ chỉ số hợp lệ; rỗng thì không lặp, tổng giữ 0. Giới hạn 500 khoản được kiểm tra trước khi chuyển kích thước sang `int`; `long long` đủ cho tổng tối đa. Khi thêm nhập bàn phím, phải kiểm tra đọc số thành công và giá trị trong miền cho phép trước khi đưa vào `amounts`; hàm này không phát hiện được mọi lỗi chuyển đổi trước đó.

Lõi JavaScript dưới đây trích từ `vi-du/nam-2-web/data.js`, chỉ giữ các hằng số và hàm liên quan đến tiền, không truy cập DOM hay `localStorage`. Đây là **đoạn rút gọn để đọc**, khai báo `function` thông thường, không có `export`; không dùng nó thay toàn bộ `data.js` hay `app.js`:

```javascript
const MAX_AMOUNT = 1000000000;
const MAX_ITEMS = 500;

function validAmount(amount) {
  return Number.isSafeInteger(amount) && amount > 0 && amount <= MAX_AMOUNT;
}

function parseAmount(input) {
  if (typeof input !== 'string' || !/^[0-9]+$/.test(input.trim())) {
    throw new Error('Nhập số nguyên VND, không có dấu chấm, phẩy hay chữ.');
  }
  const amount = Number(input.trim());
  if (!validAmount(amount)) throw new Error('Số tiền phải từ 1 đến 1.000.000.000 VND.');
  return amount;
}

function totalExpenses(expenses) {
  if (!Array.isArray(expenses) || expenses.length > MAX_ITEMS) throw new Error('Danh sách tối đa 500 khoản.');
  let total = 0;
  for (const expense of expenses) {
    if (!expense || !validAmount(expense.amount)) throw new Error('amount phải là số nguyên VND hợp lệ.');
    total += expense.amount;
  }
  return total;
}
```

`parseAmount` kiểm tra cách viết rồi kiểm tra giá trị. Vì vậy `"35000abc"` không bị chấp nhận một phần như có thể xảy ra nếu chỉ dùng `parseInt`. `Number` chuyển chuỗi thành số, không tự bảo đảm hợp đồng: `Number("")` vẫn cho 0. `Number.isInteger` kiểm tra số nguyên; bản demo dùng `Number.isSafeInteger` để kiểm tra thêm miền số nguyên an toàn, rồi giới hạn riêng `> 0` và `<= 1e9`. Chuỗi rỗng, có chữ, dấu phân cách hay ký hiệu mũ bị từ chối; `"0"` và `"1000000001"` dù chỉ có chữ số vẫn sai miền tiền.

`totalExpenses` chỉ nhận `amount` đã là số nguyên hợp lệ, giúp phát hiện cả dữ liệu sai đọc từ lưu trữ; không tự chuyển chuỗi thành số và không bỏ qua khoản sai. Hai hàm tập trung vào hợp đồng tiền và số lượng; `normalizeExpenses` trong bản đầy đủ kiểm tra thêm `id`, `title`, `category` khi nhận danh sách ứng viên hoặc đọc dữ liệu lưu.

Bản `data.js` đầy đủ bọc các hàm trong một hàm tự gọi và công bố API qua `globalThis.ViData` cho trình duyệt; `app.js` lấy API này bằng `const D = globalThis.ViData`. Trong Node.js, cùng API được gán cho `module.exports`, nên `test_data.cjs` dùng `const D = require('./data.js');` để kiểm thử logic, không cần DOM hay trình duyệt. HTML nạp `data.js` trước `app.js` bằng **script thông thường**, không dùng `import` hay `type="module"`:

```html
<script src="data.js"></script>
<script src="app.js"></script>
```

Giữ các file cùng thư mục và mở trực tiếp `index.html` được, không cần máy chủ file tĩnh. Các đoạn đọc ở trên không thay thế phần nối DOM, xử lý lỗi và lưu trữ sẵn có trong `app.js`.

#### Biến thể đóng chat và tự làm

**Minh:** viết hàm tìm số tiền lớn nhất, đầu vào theo cùng hợp đồng, rỗng trả 0. Tự dự đoán với ba khoản, một khoản và rỗng trước khi viết. Không sao chép vòng lặp tính tổng rồi chỉ đổi tên hàm.

**Đáp án có lý giải:** với dữ liệu hợp lệ, khởi tạo giá trị lớn nhất bằng 0; duyệt mỗi khoản, chỉ thay giá trị lớn nhất khi gặp tiền lớn hơn. Ba khoản cho 35000; chỉ Vở ghi cho 18000; rỗng cho 0. Mốc 0 phù hợp vì mọi khoản hợp lệ đều dương. Vẫn phải từ chối tiền sai và quá 500 khoản; có thể gọi hàm kiểm tra hiện có trước khi tìm lớn nhất.

**Lan:** tính tổng theo `category`, nhưng từ chối nếu bất kỳ khoản nào của toàn danh sách sai, kể cả khoản không thuộc nhóm đang chọn. Dùng mã `'hoc-tap'` (hiển thị “Học tập”), rồi mã `'khac'` (hiển thị “Khác”, chưa có khoản nào trong bộ mẫu).

**Đáp án có lý giải:** kiểm tra toàn bộ danh sách trước, sau đó chỉ cộng khoản có `category` đúng bằng mã nhóm chọn. Với các trường còn lại đã được `normalizeExpenses` kiểm tra, có thể gọi `totalExpenses(expenses)` để kiểm tra tiền và số lượng của toàn danh sách rồi mới lọc và cộng. `'hoc-tap'` cho 18000; `'khac'` cho 0 với bộ mẫu. Nếu có `amount` là chuỗi, số không nguyên, không dương, vượt `1e9`, hoặc danh sách quá 500 khoản, phải từ chối dù khoản sai nằm ngoài nhóm chọn; không coi dữ liệu sai là tổng 0. Nếu chỉ lọc rồi kiểm tra, khoản sai ngoài nhóm bị bỏ qua, trái yêu cầu biến thể. Đây là lý do thứ tự xử lý quan trọng, không chỉ kết quả với dữ liệu đẹp.

### 3.7. Tự đánh giá bằng việc làm được, không bằng số lần hỏi AI

#### Checklist giải thích, sửa và vận dụng

Dùng ba mức cho từng dòng: **tự làm**, **cần gợi ý**, **chưa làm**. Chỉ ghi “tự làm” khi đã đóng chat và không nhìn đáp án. Bạn đang ghi nhận một kỹ năng tại thời điểm này, không tự gắn nhãn khả năng lâu dài.

- [ ] **Giải thích:** nêu được hợp đồng tiền, giới hạn danh sách và tổng rỗng.
- [ ] **Giải thích:** trace được đường đi từ 0 tới 60000 và chỉ ra vì sao lỗi vòng lặp dừng ở 42000.
- [ ] **Giải thích:** phân biệt `35000` với `"35000"`, mô tả hậu quả trong phép `+` của JavaScript.
- [ ] **Sửa:** thay đúng phần gây lỗi và nói được vì sao không cần viết lại mọi file.
- [ ] **Sửa:** tự chọn test một khoản, rỗng, giới hạn lớn và đầu vào sai.
- [ ] **Sửa:** phân biệt lỗi bị từ chối với tổng hợp lệ bằng 0.
- [ ] **Vận dụng:** làm được biến thể lớn nhất hoặc tổng theo nhóm mà không mở chat.
- [ ] **Vận dụng:** chỉ rõ phần đã nhận hỗ trợ, phần đã tự làm và phần cần hỏi người hướng dẫn.

Chưa hoàn thành thì chọn một dòng, luyện trên ví dụ nhỏ rồi đánh dấu lại. Khi nhờ bạn học vấn đáp, đề nghị họ chờ bạn nghĩ thay vì đọc đáp án.

#### Tám câu vấn đáp kèm gợi ý, không thay câu trả lời của bạn

| Câu hỏi | Gợi ý để tự lập luận |
|---|---|
| 1. Vì sao đúng 60000 nhưng lỗi lại ra 42000? | Viết ba lần cộng, tìm khoản nào chưa được thực hiện. |
| 2. Ba phần tử có chỉ số cuối là gì; khi nào phải dừng? | Phân biệt số lượng phần tử với chỉ số bắt đầu từ 0. |
| 3. Vì sao dùng `long long` dù ba khoản đều nhỏ? | Tự nhân số khoản tối đa với tiền tối đa mỗi khoản. |
| 4. Rỗng trả 0 có mâu thuẫn với khoản tiền phải lớn hơn 0 không? | Tổng của danh sách và giá trị của một khoản là hai đối tượng khác nhau. |
| 5. Vì sao `0 + "35000"` không phải tổng tiền hợp lệ? | Nêu kiểu hai toán hạng và kiểu kết quả trước khi nói giá trị. |
| 6. Chuyển chuỗi sang số đã đủ chưa? | Xét chuỗi rỗng, `"0"`, số âm và tiền vượt giới hạn. |
| 7. Lưu được bằng `localStorage` có nghĩa là có tài khoản hoặc CSDL máy chủ không? | Chỉ ra nơi dữ liệu đang nằm và phạm vi origin; tách bài SQL riêng. |
| 8. Một bộ test đều xanh đã chứng minh bạn hiểu chưa? | Thử tự giải thích một ca, tự sửa một lỗi và làm một biến thể không AI. |

Có thể trả lời bằng lời nói hoặc viết vài dòng. Khi chưa chắc, nêu đúng điểm chưa chắc: “Em chưa biết khi dữ liệu JSON lỗi thì giao diện nên giữ trạng thái nào.” Câu hỏi cụ thể đó hữu ích hơn việc tự kết luận “em không biết Web”.

#### Sơ đồ chu trình và phiếu ba dòng

```text
[Chọn một mục tiêu + đọc hợp đồng]
                 |
                 v
             [Tự thử]
                 |
                 v
      [Dự đoán trước khi chạy]
                 |
                 v
 [Xin một gợi ý -> tự trả lời câu hỏi]
                 |
                 v
          [Tự sửa một điểm]
                 |
                 v
       [Kiểm chứng bằng test]
          |              |
       chưa đúng        đúng
          |              v
          |    [Biến thể không AI]
          |              |
          +--> [Ghi chỗ chưa chắc]
                         |
                         v
              [Chọn việc tiếp theo]
```

Cuối phiên, điền đúng ba dòng, chẳng hạn:

```text
Học được: Điều kiện cũ không cho i = 2 đi vào thân vòng lặp.
Chưa chắc: Tôi còn lúng túng khi kiểm tra dữ liệu đọc lại từ JSON.
Việc tiếp: Tự làm ca một khoản và trace kiểu dữ liệu, chưa mở AI.
```

Phiếu không cần văn hay. Mỗi dòng nên gọi tên một hành động hoặc một điểm kiến thức; tránh “học được nhiều” vì phiên sau bạn không biết bắt đầu từ đâu.

#### Speaker Notes riêng — gợi ý trình bày trong 7 phút

Dành cho người hướng dẫn. Mời tham gia tự nguyện, không kiểm tra bất ngờ trước lớp.

**0:00–1:00 — Đặt mục tiêu.** Giới thiệu Minh, Lan và dữ liệu giả. Mời tính tổng ba khoản. Chốt: không thi tốc độ; ta luyện giữ quyền suy nghĩ khi có AI.

**1:00–2:00 — Nêu ranh giới.** Hỏi: “Nếu AI viết luôn vòng lặp, Minh mất phần luyện nào?” Nhắc quyền dùng AI trong bài nộp theo học phần.

**2:00–3:15 — Trace Minh.** Hiện điều kiện lỗi, dành 20 giây tự ghi chỉ số. Với `n = 3`, cộng ở chỉ số 0 và 1; đến `i = 2` thì `2 < 2` sai nên dừng. Mời giải thích khoản 18000 bị bỏ trước khi hiện cách sửa.

**3:15–4:30 — Trace Lan.** Đặt cạnh nhau `35000` và `"35000"`, mời dự đoán lượt cộng đầu. Chốt: kiểm tra ở biên nhập và khi đọc lại lưu trữ.

**4:30–5:30 — Làm mẫu hỏi.** Dùng prompt Socratic, hỏi một câu rồi chờ. Nếu trả lời chưa đúng, trở lại bảng trace, không đọc luôn lời giải. Minh họa cách dừng khi AI nói quá mức.

**5:30–6:30 — Tự làm.** Cho một phút phác thảo biến thể độc lập. Đây là khởi động, không đánh giá tốc độ hay khả năng cá nhân.

**6:30–7:00 — Chốt.** Điền phiếu ba dòng. Nhắc: giải thích, sửa, vận dụng; màn hình chạy đúng chưa đủ.

#### Ba câu tóm tắt

AI hỗ trợ học tốt hơn khi bạn giữ việc dự đoán, tự sửa và kiểm chứng trong tay mình. Với ViSinhVien, hiểu vì sao có 60000, 42000 hoặc một chuỗi nối sai quan trọng hơn việc chép được một đoạn code chạy. Sau mỗi phiên, hãy đóng chat, làm một biến thể và ghi rõ điều học được, điều chưa chắc, việc tiếp theo.


---

## CHƯƠNG 4. LÀM CHỦ SẢN PHẨM, GIỮ AN TOÀN VÀ CHỊU TRÁCH NHIỆM

Minh, sinh viên năm nhất CNTT TLU, đã sửa được phép tính tổng trong bản C++. Lan, sinh viên năm hai, đã đưa cùng dữ liệu lên bản Web, tách phần kiểm tra khỏi phần hiển thị. Cả hai cùng học từ dự án **ViSinhVien**. Khi tổng tiền hiện đúng, Minh nghĩ phần mình đã đủ để nộp. Lan hỏi: “Nếu thầy hỏi dòng này từ đâu, dữ liệu của ai và em đã kiểm tra gì, mình trả lời được chưa?” Chương này bắt đầu từ câu hỏi ấy.

Làm chủ sản phẩm không có nghĩa là tự viết từng ký tự hoặc tuyệt đối không dùng AI. Nó có nghĩa là biết mình đang dùng gì, được phép dùng trong hoàn cảnh nào, có bằng chứng cho điều mình khẳng định và biết xử lý khi phát hiện sai sót. Một bài tập nhỏ là nơi tốt để tập thói quen đó, trước khi lỗi của mình ảnh hưởng đến người khác.

**Mốc chung của câu chuyện:** ViSinhVien là ứng dụng Web HTML và JavaScript, lưu dữ liệu bằng `localStorage` trong trình duyệt; không có backend, đăng nhập hay cơ sở dữ liệu máy chủ. Mỗi khoản chi có cấu trúc `Expense{id,title,amount,category}`. `amount` là số nguyên VND, lớn hơn 0 và không vượt quá `1e9`; danh sách tối đa 500 khoản; danh sách rỗng có tổng bằng 0. Bộ dữ liệu GIẢ dùng để đối chiếu gồm Cơm trưa 35000, Xe buýt 7000 và Vở ghi 18000, tổng **60000 VND**. Không dùng lịch sử chi tiêu thật của sinh viên để làm ví dụ.

Bạn sẽ gặp thêm SQL bằng Python `sqlite3` với cơ sở dữ liệu `:memory:`. Đó là minh họa riêng, không phải thành phần của ViSinhVien. Các đoạn mã ngắn dưới đây phục vụ giải thích; chúng không chứng nhận rằng mã nguồn kèm cẩm nang đã chạy kiểm thử thành công. Khi thực hành, hãy ghi kết quả mình thực sự quan sát, kể cả kết quả chưa đạt.

### 4.1. Dùng AI trong học tập: hỏi đúng phạm vi, khai báo đúng việc

#### Được phép, không được phép và chưa rõ

Minh nghĩ: “AI chỉ giúp sửa lỗi, chắc môn nào cũng cho.” Lan nhắc rằng một công cụ giống nhau có thể được chấp nhận trong đồ án nhưng không được dùng trong bài kiểm tra cá nhân. Điểm quyết định là yêu cầu cụ thể của môn, bài và thời điểm làm bài, không phải nhận xét chung rằng AI tốt hay xấu.

Bảng dưới là cách phân loại để hỏi và hành động, **không phải quy định của TLU**:

| Tình trạng | Ví dụ trong bài ViSinhVien | Việc cần làm |
|---|---|---|
| Đã được cho phép | Đề ghi được dùng AI gợi ý ca kiểm thử, phải khai báo | Dùng đúng phần được phép, lưu lại phần hỗ trợ và tự kiểm tra |
| Đã bị cấm | Bài kiểm tra yêu cầu tự viết, không dùng công cụ sinh mã | Không nhờ AI tạo lời giải hay sửa mã trong thời gian làm bài |
| Chưa rõ | Đề cho tham khảo tài liệu nhưng không nói về AI | Hỏi giảng viên trước; chưa biến giả định thành sự cho phép |
| Có điều kiện | Được hỗ trợ giải thích nhưng không được sinh toàn bộ chức năng | Tách câu hỏi giải thích khỏi yêu cầu viết hộ; xin làm rõ nếu cần |

“Bạn cùng lớp cũng dùng” không phải căn cứ. “Em chỉ dùng bản miễn phí” cũng không giải quyết câu hỏi học thuật. Với bài nhóm, cả nhóm cần biết phạm vi được phép: một thành viên đưa mã AI vào nhánh chung có thể ảnh hưởng đến bản nộp của mọi người.

#### Một tin nhắn hỏi giảng viên có thể gửi được

Minh không hỏi chung chung “Có được dùng AI không?”. Bạn mô tả hành động dự kiến:

> Thưa thầy/cô, với bài ViSinhVien, em dự định tự viết phần thêm khoản chi và tính tổng. Em muốn dùng AI để giải thích lỗi JavaScript và gợi ý ca kiểm thử cho `amount`, sau đó tự sửa và chạy kiểm tra. Em không định gửi dữ liệu thật hoặc nhờ AI làm toàn bộ bài. Phạm vi này có được phép không ạ? Nếu được, nhóm cần khai báo ở đâu và giữ bằng chứng nào? Nếu không, em sẽ dùng tài liệu môn học theo hướng dẫn.

Câu hỏi này giúp thầy cô trả lời theo công việc cụ thể. Nếu chưa nhận được phản hồi, Minh tiếp tục phần chắc chắn được phép, thay vì coi im lặng là đồng ý. Khi có trả lời, nhóm giữ thông tin cần thiết về phạm vi và thời điểm, không phát tán ảnh chụp hội thoại riêng vào kho công khai.

#### Khai báo hỗ trợ phải khớp với quá trình thật

Khai báo tốt không phải một câu trang trí “Có sử dụng AI”. Người đọc cần phân biệt AI gợi ý điều gì, sinh nội dung nào, nhóm thay đổi gì và kiểm chứng đến đâu. Ngược lại, không cần đổ toàn bộ lịch sử chat chứa thông tin riêng tư vào bài nộp. Hãy mô tả đủ để giảng viên đánh giá, theo hình thức giảng viên yêu cầu.

Mẫu minh họa sau **chỉ dùng nếu đúng với việc đã làm**:

> Nhóm dùng [tên công cụ, phiên bản nếu biết] ngày [ngày thực tế] để hỏi cách kiểm tra số nguyên dương và gợi ý trường hợp biên cho `amount`. AI đề xuất kiểm tra số âm, số thập phân và giới hạn trên. Minh viết lại điều kiện theo đặc tả `0 < amount <= 1e9`; Lan rà soát chỗ gọi kiểm tra trước khi lưu. Phần hiển thị tên khoản chi được nhóm đối chiếu với hướng dẫn OWASP về `textContent`. Trạng thái kiểm tra: [đã chạy gì, kết quả gì hoặc chưa chạy]. Nhóm không gửi dữ liệu chi tiêu thật. Những phần còn chưa hiểu: [ghi thật, hoặc ghi không có sau khi rà soát].

Nếu AI đã sinh cả hàm, phải nói là sinh bản nháp của hàm, không đổi thành “chỉ tham khảo ý tưởng”. Nếu mới đọc mã mà chưa chạy, ghi “đã rà soát bằng đọc mã; chưa chạy kiểm thử”, không ghi “đã xác minh”. Tính trung thực nằm ở độ khớp giữa lời khai và hành động, không nằm ở độ đẹp của mẫu.

#### Ghi nguồn không thay cho quyền sử dụng

Lan phân biệt ba câu hỏi. **Attribution**: mình ghi nhận nguồn và sự hỗ trợ thế nào? **Ownership/quyền đối với sản phẩm**: mình có những quyền gì với phần mã, tài liệu, hình ảnh? **Trách nhiệm**: ai kiểm tra và đứng tên cho bản nộp? Ba câu hỏi liên quan nhưng không thay thế nhau.

Ghi “nguồn: một kho GitHub” không tự tạo quyền sao chép đoạn mã không có giấy phép. Khai báo “AI viết” không chuyển trách nhiệm kiểm tra sang công cụ. Ngược lại, việc dùng AI trong phạm vi được phép, khai báo đúng và tự kiểm chứng không tự động là đạo văn. Cần đánh giá hành vi theo yêu cầu học thuật cụ thể, nguồn đã dùng và cách trình bày đóng góp.

Trước khi nộp, Minh tự giải thích một luồng: người dùng nhập số tiền, dữ liệu được kiểm tra, khoản chi được thêm, tổng được tính rồi lưu. Đến dòng không giải thích được, Minh đánh dấu để học lại. Lan yêu cầu bạn nêu một đầu vào bị từ chối và lý do. Đây là kiểm tra năng lực làm chủ, không phải yêu cầu học thuộc từng dấu chấm phẩy. Nếu chưa hiểu phần trọng yếu, lựa chọn tốt là thu hẹp bài về phần hiểu được và hỏi hỗ trợ, thay vì che giấu bằng một bản trình bày trơn tru.

### 4.2. Dữ liệu và quyền của Agent: chỉ đưa thứ cần thiết

#### Phân loại trước khi dán vào cửa sổ chat

Để nhờ AI tìm lỗi tính tổng, Minh định gửi ảnh chụp bảng chi tiêu cá nhân. Lan dừng lại: lỗi có thể tái hiện bằng ba khoản GIẢ, không cần biết Minh ăn ở đâu, lúc nào hoặc chuyển tiền cho ai. Quy tắc thực dụng là chọn dữ liệu ít nhạy cảm nhất nhưng vẫn đủ tái hiện vấn đề.

| Nhóm dữ liệu | Cách hiểu để làm bài | Ví dụ và lựa chọn |
|---|---|---|
| Giả/tổng hợp | Tạo mới cho mục đích thử, không lấy hồ sơ thật rồi sửa sơ qua | Ba khoản mẫu 35000, 7000, 18000; liên hệ giả `demo001@example.invalid` |
| Đã khử nhận dạng/ẩn danh | Đã xử lý để không còn xác định được người từ dữ liệu và khả năng liên kết có liên quan | Chỉ gọi là ẩn danh khi đã đánh giá lại khả năng nhận diện; không mặc định sau khi bỏ tên |
| Cá nhân, nhạy cảm hoặc bí mật cần bảo vệ | Có thể liên quan một người, đời sống riêng tư, tài khoản hoặc quyền truy cập | Mã sinh viên, ảnh hồ sơ, lịch chi tiêu thật, mật khẩu, khóa API; không đưa vào ví dụ công khai |

Bảng này là cách sàng lọc khi học, không thay thế phân loại pháp lý chi tiết. Khóa API cần bảo vệ vì cấp quyền truy cập, kể cả khi bản thân chuỗi khóa không phải thông tin nhận diện một cá nhân. Dữ liệu công khai ở nơi khác cũng không đương nhiên phù hợp để gom lại và gửi cho một dịch vụ AI.

**Dữ liệu giả không chỉ là đổi tên.** Nếu Minh thay tên bằng “Bạn A” nhưng giữ mã sinh viên, giờ giao dịch và cửa hàng quen thuộc, người biết bối cảnh vẫn có thể nhận ra bạn đó. Mã hóa tên thành một mã ổn định trong khi giữ bảng đối chiếu cũng chưa phải đã ẩn danh hoàn toàn. Với bài năm nhất, phương án dễ kiểm soát hơn là tự tạo dữ liệu mới từ đầu, bỏ lịch sử thật ra khỏi luồng thực hành.

#### Đọc một hộp pháp lý, rồi quay lại quyết định cụ thể

> **Mốc áp dụng: 29/10/2026.** Phần pháp lý trong chương đối chiếu Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Nghị định 356/2025/NĐ-CP, cùng có hiệu lực từ 01/01/2026 [1][2]. Theo Điều 42 của Nghị định 356, Nghị định 13/2023/NĐ-CP đã hết hiệu lực; không dẫn nghị định cũ như văn bản đang hiện hành. Về sở hữu trí tuệ, dùng Văn bản hợp nhất 67/VBHN-VPQH ngày 23/03/2026, thể hiện sửa đổi bởi Luật 131/2025/QH15 có hiệu lực từ 01/04/2026 [3]. Đây là định hướng học tập, không phải ý kiến pháp lý cho vụ việc cụ thể. Hãy hỏi giảng viên hoặc đầu mối có thẩm quyền khi áp dụng cho dữ liệu, hợp đồng hay sản phẩm thật.

Luật bảo vệ dữ liệu cá nhân có nội dung về khái niệm và khử nhận dạng, nguyên tắc xử lý theo phạm vi, mục đích, sự đồng ý và xử lý trong hoạt động AI. Nhưng không nên rút thành câu “mọi xử lý đều phải xin đồng ý”: luật có các trường hợp ngoại lệ tại Điều 19 [1]. Với sinh viên, đừng tự suy diễn rằng bài tập của mình chắc chắn thuộc ngoại lệ. Nếu bài không cần dữ liệu thật, dùng dữ liệu giả là cách giảm vấn đề ngay từ thiết kế.

#### Quyền đọc của Agent là một quyết định thật

Một Agent có thể tìm trong nhiều tệp thay vì chỉ trả lời đoạn văn bạn dán. Phạm vi đọc, khả năng gọi lệnh và việc truyền nội dung đến dịch vụ phụ thuộc công cụ, chế độ và thiết lập đang dùng. Đừng mặc định “nằm trên máy em” đồng nghĩa với “không thể được đưa vào ngữ cảnh gửi ra ngoài”. Hãy kiểm tra mô tả quyền và yêu cầu xác nhận hiện ra.

Lan chia việc xin trợ giúp thành bốn bước:

1. Viết rõ vấn đề: tổng của ba khoản giả không bằng 60000, hay tên có dấu hiển thị sai?
2. Chọn phần nhỏ nhất: hàm tính tổng và dữ liệu giả, không chọn cả thư mục cá nhân.
3. Đọc quyền được yêu cầu: xem tệp nào cần đọc, lệnh nào cần chạy, có cần ghi hay truy cập mạng không.
4. Nếu quyền vượt mục tiêu, không chấp nhận chỉ để hết thông báo; thu hẹp yêu cầu hoặc hỏi người phụ trách.

Đọc một hàm thường không cần quyền ghi toàn kho. Giải thích lỗi JavaScript không cần xem thư mục tải xuống, hồ sơ lớp hoặc tệp chứa bí mật. Cài gói, đẩy mã lên mạng và sửa lịch sử Git là những hành động khác với đọc mã; không gộp chúng vào một sự đồng ý mơ hồ “cứ làm mọi thứ”.

Một prompt phù hợp là: “Chỉ phân tích đoạn hàm và ba khoản giả bên dưới. Không cần đọc tệp khác, chạy lệnh hay thay đổi mã. Hãy chỉ ra giả thuyết lỗi và ca kiểm tra.” Nếu công cụ vẫn yêu cầu quyền rộng, Minh phải đánh giá yêu cầu thật, không cho rằng câu prompt tự tạo ra hàng rào kỹ thuật.

#### Những chỗ hay quên: ảnh, chat, lịch sử

Ảnh chụp màn hình có thể lộ email ở góc, đường dẫn chứa tên, tab trình duyệt hoặc khóa trong bảng điều khiển. Trước khi gửi, cắt đúng vùng lỗi và kiểm tra ảnh đầu ra. Một lớp che có thể bị gỡ trong tệp chỉnh sửa; đừng gửi bản còn giữ lớp chứa dữ liệu gốc.

Lịch sử chat có thể chứa đoạn từng dán rồi đã xóa khỏi mã. Git có thể giữ phiên bản trước. Tệp sao lưu, log và bản xuất dự án có thể chứa thông tin ngoài màn hình hiện tại. Đừng kiểm tra mỗi tệp đang mở. Với ví dụ cần chuỗi minh họa bí mật, dùng `DEMO_KEY_NOT_A_SECRET` và ghi rõ đó là placeholder không có quyền truy cập. Nếu phát hiện khóa thật, chuyển sang quy trình sự cố ở mục 4.6, không chụp khóa vào báo cáo để “làm bằng chứng”.

### 4.3. Đọc mã với câu hỏi “đầu vào này đi đâu?”

#### Giữ đặc tả nhỏ nhưng nhất quán

Minh từng dùng `parseInt` rồi coi kết quả là hợp lệ. Lan yêu cầu xét cả chuỗi ban đầu: chuyển đổi kiểu không tự chứng minh dữ liệu đáp ứng đặc tả. Một hàm chuyển đổi có thể chấp nhận phần đầu của chuỗi trong khi người nhập đã gõ nội dung không hợp lệ. Trước hết cần xác định cách nhận và chuyển đầu vào; sau đó kiểm tra giá trị thu được theo hợp đồng của chương.

Với ViSinhVien, các điều kiện cần đối chiếu gồm số tiền là số nguyên hữu hạn, lớn hơn 0, không quá `1e9`; không thêm khoản thứ 501; danh sách rỗng có tổng 0. Những dữ liệu như 0, số âm, số thập phân, giá trị vượt trần và giá trị không phải số phải có kết quả rõ ràng. Đừng chỉ kiểm tra ba khoản hợp lệ rồi kết luận mọi trường hợp đã an toàn.

Tổng lớn nhất theo giới hạn hiện tại là `500 × 1e9 = 500000000000`, vẫn trong khoảng số nguyên an toàn của JavaScript. Điều này giúp giải thích lựa chọn dùng số nguyên VND cho bài tập, không cho phép bỏ kiểm tra từng khoản. Nếu sau này đổi đơn vị tiền, thêm tỷ giá hoặc tăng giới hạn, phải xem lại giả định số học.

Trong bộ ví dụ kèm cẩm nang, `vi-du/nam-2-web/data.js` là nơi đối chiếu phần kiểm tra đầu vào; `vi-du/nam-2-web/app.js` là nơi đối chiếu hiển thị. Đọc cả đường đi của dữ liệu, không chỉ tìm thấy một hàm tên “validate” rồi kết luận mọi lối nhập đều đã gọi nó. Dữ liệu lấy lại từ `localStorage` cũng cần được xem là đầu vào có thể hỏng hoặc bị sửa.

#### SQL: giá trị là dữ liệu, không phải cấu trúc câu lệnh

**Ranh giới ví dụ:** SQL ở đây chạy riêng bằng Python `sqlite3` với `:memory:`; ViSinhVien không gửi SQL và không có backend. Tệp minh họa riêng là `vi-du/minh-hoa-sqlite.py`. Không nối minh họa này vào sơ đồ kiến trúc của ứng dụng Web.

Giả sử bảng minh họa có các cột `id`, `title`, `amount`, `category`. Lan muốn tìm một tên khoản chi thử riêng là `Vở O'Reilly`. Dấu nháy trong tên là dữ liệu bình thường, nhưng cách nối chuỗi sau làm nó đi vào cú pháp SQL:

```python
# Mẫu không nên dùng; chỉ đọc để nhận diện vấn đề.
query = "SELECT title,amount FROM expenses WHERE title = '" + title + "'"
```

Với tên có dấu nháy, câu lệnh ghép có thể sai cú pháp. Đáng ngại hơn, nối trực tiếp dữ liệu không tin cậy vào câu lệnh có thể cho phép dữ liệu làm thay đổi ý nghĩa SQL. Không cần thử chuỗi phá hoại để hiểu lỗi này. Một tên sách hợp lệ đã đủ chỉ ra rằng chương trình đang trộn hai vai trò: dữ liệu và mã lệnh.

Cách truy vấn giá trị đúng trong ngữ cảnh Python `sqlite3` này là:

```python
# conn là kết nối sqlite3 tới ":memory:" trong minh họa riêng.
rows = conn.execute(
    'SELECT title,amount FROM expenses WHERE title = ?',
    (title,)
).fetchall()
```

Dấu `?` là vị trí dành cho giá trị được gắn riêng. `(title,)` là tuple một phần tử của Python; **dấu phẩy tạo tuple**, còn `(title)` chỉ là biểu thức được đặt trong ngoặc. Khi dùng tuple, thiếu dấu phẩy không còn cung cấp đúng cấu trúc đối số như dự định. Trình điều khiển xử lý giá trị tách khỏi cấu trúc SQL, nên dấu nháy của `Vở O'Reilly` không cần được người học tự thay thế bằng mẹo ghép chuỗi.

OWASP ưu tiên truy vấn tham số hóa cho tình huống này [4]. Tuy vậy, tham số giá trị không thay thế tùy ý tên bảng, tên cột hoặc từ khóa sắp xếp. Nếu chương trình cho chọn cách sắp xếp, hãy ánh xạ lựa chọn sang một tập tên cột đã định trước, không chèn nguyên văn chuỗi bất kỳ. Đó là lúc cần danh sách cho phép cho phần cấu trúc.

Để kiểm tra, nhóm chuẩn bị một bản ghi thử riêng mang tên `Vở O'Reilly`, truy vấn bằng tham số rồi đối chiếu kết quả mong đợi. Tệp `vi-du/minh-hoa-sqlite.py` đã làm sẵn việc đó: nếu máy có Python 3, đứng ở thư mục gốc dự án và chạy một dòng sau, rồi ghi lại đúng dòng kết quả nhìn thấy.

```bash
python "vi-du/minh-hoa-sqlite.py"
```

Dòng đáng chú ý nhất trong kết quả là `Tra cuu tham so: [("Vở O'Reilly", 12000)]`: dấu nháy đơn đi qua truy vấn như dữ liệu bình thường, không ai phải ghép chuỗi để “né” nó. Các dòng `PASS reject amount` cho thấy ràng buộc của bảng từ chối số âm, số 0, số thập phân và số vượt `1e9`.

Trên một số máy Linux hoặc macOS, lệnh là `python3` thay vì `python`; nếu cả hai đều không có, ghi “chưa chạy, thiếu Python” và đọc tiếp phần giải thích — đây là minh họa khái niệm, không phải điều kiện để học xong chương. Ghi rõ đây là fixture SQL riêng, không thêm nó vào bộ ba khoản chuẩn rồi vẫn tuyên bố tổng 60000. Truy vấn tham số hóa cũng không tự giải quyết phân quyền, rò rỉ log hoặc mọi lỗi nghiệp vụ.

#### XSS: hiển thị tên khoản chi như văn bản

Minh muốn giao diện linh hoạt nên thử gán tên khoản chi bằng `innerHTML`. Lan đưa đầu vào vô hại `<b>Vở</b>` và hỏi: “Người dùng nhập một cái tên, tại sao ứng dụng lại diễn giải nó thành thẻ?” Nếu giao diện in đậm chữ Vở, ta thấy trình duyệt đang phân tích đầu vào như HTML. Ví dụ này không chạy mã độc, nhưng làm lộ điểm dữ liệu đã bị trao thêm ý nghĩa.

Với một ô bảng cần hiển thị tên dưới dạng văn bản thông thường, dùng:

```javascript
const td = document.createElement('td');
td.textContent = expense.title;
```

Khi `expense.title` là `<b>Vở</b>`, nội dung mong đợi nhìn thấy là chính chuỗi **`<b>Vở</b>`**, gồm cả dấu ngoặc nhọn, không phải chỉ chữ Vở được in đậm. `td` là tên biến của đoạn minh họa. Trong `app.js` đi kèm, ô bảng có tên biến `cell`: hãy tìm `cell.textContent = value` trong hàm `render`; `value` lần lượt là tên khoản, nhãn nhóm hoặc số tiền đã định dạng. Không đổi chỗ gán này thành `innerHTML` cho tên khoản chi.

OWASP liệt kê `textContent` là một cách đưa dữ liệu vào nơi nhận văn bản an toàn trong DOM thông thường [5]. Phạm vi “văn bản thông thường” rất quan trọng. Cách bảo vệ cho nội dung ô bảng không tự áp dụng cho một URL, thuộc tính sự kiện, CSS hay chuỗi mã JavaScript. Nếu sau này thêm đường dẫn, cần kiểm soát loại URL và ngữ cảnh riêng. Nếu thật sự cần HTML phong phú, đó là yêu cầu mới cần cơ chế làm sạch phù hợp, không phải lý do dùng `innerHTML` cho mọi tên khoản chi.

Cũng đừng suy luận rằng “dữ liệu nằm trong `localStorage` của em nên tin được”. Người dùng có thể sửa kho lưu trữ, dữ liệu cũ có thể đến từ phiên bản lỗi và máy có thể dùng chung. Hãy kiểm tra cả lúc nhập, lúc đọc lại dữ liệu và lúc đưa dữ liệu ra giao diện theo trách nhiệm của từng lớp.

#### C++: vượt chỉ số không phải phép thử vận may

Ở bài năm nhất bằng C++, Minh có thể dùng một mảng gồm ba số tiền. Với `n` phần tử, chỉ số hợp lệ là từ 0 đến `n - 1`. Truy cập mảng ngoài biên, hoặc dùng `operator[]` của `std::vector` với chỉ số không hợp lệ, dẫn đến hành vi không xác định. `index >= n` là ngoài biên; nếu chỉ số có dấu thì cũng phải xét chỉ số âm.

“Hành vi không xác định” không có nghĩa là chắc chắn chương trình sẽ crash. Nó có thể trông như chạy đúng, đọc giá trị lạ hoặc có biểu hiện khác. Một lần chạy không lỗi không chứng minh truy cập đó hợp lệ. Đừng chạy thử truy cập sai rồi dùng việc “máy em vẫn ổn” làm bằng chứng.

Khi đọc vòng lặp duyệt mảng, đối chiếu điều kiện `i < n`, không phải `i <= n`. Khi chỉ số đến từ đầu vào, kiểm tra miền trước khi truy cập. Có thể tìm hiểu `vector::at()` để biết cơ chế báo lỗi ngoài biên của nó, nhưng vẫn phải xử lý đầu vào và lỗi phù hợp. Bài học chung với JavaScript và SQL là: biết hợp đồng ở ranh giới, không tin vào một lần chạy may mắn.

#### Gói thư viện AI đề xuất: kiểm chứng trước khi cân nhắc cài

AI có thể nêu tên một gói không tồn tại, nhầm tên hoặc dẫn đến gói có tên gần giống thư viện quen thuộc. Minh không chạy lệnh cài chỉ vì câu trả lời có vẻ tự tin. Với ứng dụng HTML và JavaScript nhỏ hiện tại, hãy hỏi trước: chức năng này có cần thêm phụ thuộc không?

Nếu thật sự cần, Lan kiểm tra tên và phiên bản trên registry chính thức của hệ sinh thái, đối chiếu đường dẫn từ tài liệu chính thức, người duy trì, kho mã nguồn, giấy phép và dấu hiệu bảo trì. Xem cả nội dung liên quan đến quá trình cài đặt, thay đổi phiên bản và cảnh báo bảo mật. Tên nổi tiếng hoặc số lượt tải cao không phải bảo đảm tuyệt đối. Một lockfile giúp cố định lựa chọn phiên bản, nhưng không biến gói độc hại thành đáng tin [6].

Hoạt động của chương chỉ là lập bảng kiểm chứng, **không thực hiện cài gói**. Nếu chưa xác minh được, bỏ đề xuất phụ thuộc và dùng giải pháp đang hiểu, hoặc hỏi giảng viên. Không bịa một URL registry để làm đầy cột bằng chứng.

#### Ranh giới với sản phẩm thật

Kiểm tra trong trình duyệt giúp bài tập nhất quán; nó không phải hàng rào đủ cho hệ thống tài chính. `localStorage` không cung cấp cơ chế đăng nhập, phân quyền hay bảo vệ dữ liệu tài chính trước mọi người dùng cùng môi trường. ViSinhVien là sản phẩm học tập với dữ liệu giả, không được quảng bá là ứng dụng tài chính an toàn.

Nếu làm dịch vụ thật có máy chủ, cần thiết kế xác thực, phân quyền, kiểm tra dữ liệu phía máy chủ và các biện pháp vận hành phù hợp. Máy chủ không được tin điều kiện chỉ đặt ở trình duyệt. Đây là ranh giới kiến thức để nhận ra việc mới cần làm, không phải yêu cầu nhồi thêm backend vào bài hiện tại.

### 4.4. Mã nguồn mở, giấy phép và quyền đối với mã AI

#### Kho công khai không đồng nghĩa được dùng tùy ý

Minh tìm được một giao diện đẹp trên GitHub. Trang kho mở được không cần đăng nhập, nên bạn định chép một tệp vào ViSinhVien. Lan yêu cầu mở phần giấy phép trước. GitHub cũng lưu ý rằng việc công khai kho không tự trao toàn bộ quyền sao chép, phân phối hay tạo tác phẩm phái sinh [8].

Nếu không thấy giấy phép, đừng tự gắn nhãn “miễn phí”. Cần tìm thông tin quyền ở vị trí liên quan, kể cả tệp riêng và tài sản ảnh. Một kho có giấy phép cho mã chưa chắc có cùng giấy phép cho mọi hình ảnh hoặc phông chữ kèm theo. Nếu vẫn chưa rõ, tránh dùng đoạn không rõ quyền, tìm nguồn khác có điều kiện rõ ràng hoặc tự viết từ yêu cầu chức năng.

#### Đọc điều kiện của MIT và GPL, không chỉ đọc tên

| Tình huống | Điều cần hiểu | Hành động thực tế |
|---|---|---|
| Mã mang giấy phép MIT | Có quyền sử dụng rộng, nhưng phải giữ thông báo bản quyền và thông báo giấy phép theo điều kiện của MIT | Giữ nội dung cần thiết khi sao chép, lưu nguồn và phiên bản; không xóa đầu tệp chỉ vì thấy dài |
| Mã mang giấy phép GPL | Không phải giấy phép “cấm thương mại”; nghĩa vụ phụ thuộc phiên bản giấy phép, việc chuyển giao/phân phối và quan hệ với tác phẩm phái sinh | Đọc đúng GPL áp dụng, xem cách đưa mã vào sản phẩm; hỏi người có chuyên môn nếu chưa xác định được nghĩa vụ |
| Kho không có giấy phép rõ | Không có cơ sở để coi là tự do sao chép | Không đưa vào bản nộp chỉ bằng cách thêm đường dẫn nguồn |
| AI đưa một đoạn mã | Nhãn “AI tạo” không tự chứng minh nguồn gốc hay quyền sở hữu độc quyền | Kiểm tra nguồn nếu được dẫn, điều khoản công cụ và dấu hiệu sao chép; thay phần chưa rõ quyền |

Với MIT, ghi nguồn học thuật và giữ thông báo giấy phép là hai công việc khác nhau; làm một việc không luôn đủ cho việc còn lại. Với GPL, đừng kết luận chỉ từ số dòng đã chép, hoặc cho rằng thay tên biến sẽ xóa nghĩa vụ. Cũng không nên nói cứ nhìn thấy GPL là không được dùng. Phải xét trường hợp và văn bản giấy phép cụ thể; chương này không quyết định tính tương thích cho một sản phẩm thật.

#### Một thẻ nguồn nhỏ giúp tránh quên

Ghi nguồn ngay khi chọn tài nguyên, vào phần khai báo của bài:

| Thành phần định dùng | Nguồn/phiên bản | Giấy phép và việc phải giữ | Quyết định |
|---|---|---|---|
| Đoạn xử lý hoặc giao diện cụ thể | URL thật, phiên bản nếu có | Ghi giấy phép đã kiểm tra | Dùng có điều kiện / hỏi thêm / không dùng |

Dẫn đúng bản đã dùng, không chỉ trang chủ. Phân biệt tham khảo ý tưởng thuật toán với sao chép cách biểu đạt cụ thể. Chưa rõ thì khai nguồn và hỏi người chấm, không đổi vài chữ để che dấu vết.

#### Học tập không phải ngoại lệ sao chép mọi chương trình

Pháp luật sở hữu trí tuệ Việt Nam bảo hộ chương trình máy tính ở dạng mã nguồn hoặc mã máy theo Điều 22. Không thể dựa đơn giản vào lý do “em sao chép để học” để khẳng định được tự do sao chép chương trình máy tính; Điều 25 khoản 3 đặt giới hạn liên quan đến việc áp dụng ngoại lệ [3]. Điều này không cấm học từ tài liệu, cũng không làm mọi bài tập cần tư vấn pháp lý. Nó nhắc mình kiểm tra quyền trước khi mang mã của người khác vào bản nộp hoặc sản phẩm phân phối.

Đối với mã AI tạo, quyền còn có thể liên quan đến điều khoản dịch vụ, đóng góp của con người, nguồn mà đầu ra trùng hoặc dựa vào và pháp luật áp dụng. Đừng cam kết “AI viết nên chắc chắn thuộc sở hữu của em” hay “không ai có quyền với mã này”. Khi chưa rõ, lựa chọn phù hợp cho bài ViSinhVien là tránh đoạn không rõ nguồn/quyền, dùng chức năng đơn giản tự hiểu và triển khai được, rồi ghi nhận hỗ trợ thật sự.

Minh cuối cùng không dùng giao diện chưa rõ giấy phép. Bạn tự viết bảng khoản chi đơn giản, còn Lan giúp kiểm tra cách hiển thị văn bản. Sản phẩm bớt bóng bẩy nhưng nhóm biết nguồn gốc của từng phần. Đó là giảm một vấn đề không cần thiết, không phải phòng thủ đến mức không dám học từ ai.

### 4.5. Chịu trách nhiệm: không đổ lỗi cho công cụ, không nhận bừa mọi lỗi

Minh hỏi: “Nếu AI viết sai thì em chịu hết à?” Câu trả lời cần tách các tầng trách nhiệm. Người nộp bài phải giải thích việc mình làm và mức kiểm tra; nhưng kết luận kỷ luật, trách nhiệm nghề nghiệp hay pháp lý còn phụ thuộc quy định, vai trò và tình tiết. Không có một câu “chịu 100% pháp lý” áp dụng cho mọi sinh viên và mọi đầu ra AI.

| Tầng trách nhiệm | Câu hỏi cần trả lời | Việc Minh và Lan kiểm soát được | Không nên khẳng định |
|---|---|---|---|
| Học thuật | Bài có đúng yêu cầu môn, đóng góp và khai báo có trung thực không? | Hỏi phạm vi AI, giải thích mã, ghi nguồn, ghi kết quả thật | Mọi dùng AI đều là đạo văn; hoặc khai báo là chắc chắn được chấp nhận |
| Nghề nghiệp | Sản phẩm có được rà soát đúng vai trò và cảnh báo đúng giới hạn không? | Kiểm tra dữ liệu, báo lỗi, yêu cầu người phù hợp duyệt thay đổi | Có AI hỗ trợ thì người làm không còn trách nhiệm; hoặc một người luôn gánh mọi lỗi nhóm |
| Pháp lý | Có vấn đề dữ liệu, quyền tác giả, hợp đồng hoặc quyền truy cập nào cần xem xét không? | Ngừng hành vi có vấn đề, giữ thông tin cần thiết, báo đầu mối có thẩm quyền | Tự kết luận có tội, mức phạt hoặc trách nhiệm bồi thường từ một ví dụ trong lớp |

#### Chia vai nhưng không tạo khoảng trống

Minh phụ trách nhập và tính tổng; Lan rà soát hiển thị và nguồn; cả hai xem lại bản nộp. “Lan đã xem” phải rõ là xem diff, đọc hàm hay chạy ứng dụng, tránh hiểu nhầm tất cả đã được duyệt.

Người viết giải thích thay đổi, người xem nêu bằng chứng. Với `textContent`, đó có thể là diff và quan sát `<b>Vở</b>` hiện nguyên văn. Với giới hạn 500 khoản, cần thử đúng giới hạn; ảnh tổng 60000 không chứng minh được. Không cần hai người ký mọi dấu cách, nhưng phải rõ trách nhiệm với hành vi trọng yếu.

#### Nói mức chắc chắn bằng ngôn ngữ kiểm chứng

Thay “an toàn tuyệt đối”, ghi điểm hiển thị đã sửa và ca đã/chưa kiểm tra. Thay “không có dữ liệu nhạy cảm”, liệt kê phạm vi tệp, ảnh đã rà soát. Thay “AI bảo MIT”, dẫn giấy phép đã mở.

Nêu giới hạn giúp người đọc đối chiếu, nhưng không được dùng để che việc cốt lõi chưa hoàn tất. Phát hiện lỗi thì ghi tác động, cách khắc phục; không sửa lén kết quả cũ. Khi bàn giao chưa rõ, cùng làm rõ thay vì đổ lỗi. Hãy nói: “Đây là điều em biết, điều chưa xác minh và bước tiếp theo.”

### 4.6. Nếu lộ khóa API: bình tĩnh xử lý theo thứ tự

#### Tình huống giả định không làm thay đổi kiến trúc ứng dụng

ViSinhVien không cần API key. Giả sử Minh vô tình chia sẻ khóa của dịch vụ khác trong thư mục bài tập. Khi trình bày tình huống, chỉ dùng placeholder `DEMO_KEY_NOT_A_SECRET`.

Với khóa thật, xóa dòng trong tệp chưa đủ: khóa có thể còn hiệu lực, bản cũ còn trong lịch sử Git, clone, cache hoặc chat [7]. Ưu tiên vô hiệu quyền đã lộ trước khi dọn bản lưu.

#### Sáu bước xử lý có thể làm theo

1. **Dừng chia sẻ thêm.** Không gửi lại tệp hoặc chụp nguyên khóa để hỏi nhóm. Tạm dừng việc công khai bản có bí mật trong phạm vi mình có quyền xử lý. Không chuyển khóa sang một kênh chat khác để “cất tạm”.
2. **Thu hồi hoặc xoay vòng khóa ở nhà cung cấp.** Nếu là tài khoản của mình, dùng chức năng quản lý khóa chính thức. Nếu thuộc nhóm, trường hoặc nơi thực tập, báo ngay người có quyền để họ thực hiện. Xác nhận khóa cũ đã bị vô hiệu; tạo khóa mới nhưng để khóa cũ còn hoạt động chưa giải quyết xong.
3. **Kiểm tra mức sử dụng ở nhà cung cấp.** Xem lượt gọi, chi phí, tài nguyên và mốc thời gian có dấu hiệu bất thường. “Chưa thấy dùng” không chứng minh chưa ai sao chép. Giữ thông tin cần thiết về thời điểm phát hiện và phạm vi chia sẻ, không lưu lại nguyên bí mật.
4. **Kiểm tra log và bản liên quan trong phạm vi được phép.** Xem commit, tệp cấu hình, sản phẩm build, ảnh và lịch sử chia sẻ có liên quan. Không tự truy cập tài khoản hay log của người khác. Tránh làm log mới chứa khóa khi tìm kiếm hoặc sao chép bằng chứng.
5. **Báo đúng đầu mối.** Với bài học, báo giảng viên hoặc người phụ trách nhóm; với tài khoản tổ chức, theo kênh sự cố của tổ chức. Gửi thời điểm, dịch vụ, trạng thái thu hồi, phạm vi đã biết và việc còn chưa rõ; không gửi khóa đầy đủ.
6. **Giảm dữ liệu còn lưu và ngăn tái diễn.** Sau khi khống chế quyền truy cập, phối hợp xử lý bản chứa bí mật theo quy trình phù hợp. Thay minh họa bằng placeholder, kiểm tra phạm vi Agent, bỏ nhu cầu dùng khóa thật trong bài và cập nhật checklist.

GitHub khuyến nghị thu hồi hoặc xoay vòng bí mật trước khi xử lý việc loại bỏ dữ liệu khỏi kho [7]. Với kho nhóm, không tự ý viết lại lịch sử hay ép đẩy để “xóa sạch”. Những việc đó ảnh hưởng người khác và không bảo đảm mọi clone hoặc cache biến mất. Hãy để người quản lý kho phối hợp phương án; chương này không cung cấp lệnh viết lại lịch sử.

#### Một thông báo sự cố ngắn, đủ hành động

> Em phát hiện lúc [giờ, ngày] một tệp trong [phạm vi chia sẻ] chứa khóa của [dịch vụ]. Em đã dừng chia sẻ. Khóa cũ: [đã thu hồi/đang chờ/chưa xác minh]. Thời gian có thể đã lộ: [phạm vi biết được]. Usage/log: [đã kiểm tra gì, kết quả hoặc chưa kiểm tra]. Nhờ [đầu mối] hướng dẫn xử lý bản đã chia sẻ. Em không đính kèm khóa.

Báo sớm không phải kết luận đã có tấn công; chưa thấy lạm dụng cũng không phải lý do giấu sự cố. Với dữ liệu hoặc hệ thống thật, người có thẩm quyền phải đánh giá nghĩa vụ thông báo và lưu bằng chứng. Không suy ra thời hạn pháp lý từ mẫu này.

Lan cùng Minh tìm nguyên nhân tệp thừa lọt vào bản chia sẻ, rồi thêm bước rà đúng thành phần bản nộp. Sửa quy trình cụ thể hữu ích hơn lời hứa “lần sau cẩn thận”.

### 4.7. Thực hành trước khi nộp: kiểm tra, sửa và đưa bằng chứng

#### Bài tập: duyệt một kho ViSinhVien giả định

Bạn rà soát bản nộp của Minh và Lan bằng dữ liệu giả, không truy cập tài khoản thật, cài gói hay tạo khóa. Các lỗi dưới đây là **phiếu tình huống, không phải kết luận về kho ví dụ hiện có**.

Làm lần lượt: đối chiếu đặc tả; đọc luồng nhập–kiểm tra–lưu–hiển thị; xem nguồn và phạm vi AI; phân loại; sửa; ghi bằng chứng. Nếu chỉ đọc mã, đánh dấu phần chạy thử là chưa thực hiện.

#### Bảng vấn đề – cách sửa – bằng chứng

| Vấn đề trong kho giả định | Mức xử lý | Cách sửa hoặc quyết định | Bằng chứng cần thu |
|---|---|---|---|
| Tổng mẫu khác 60000 | Chặn nộp | Rà chuyển đổi số và tính tổng | Đầu vào, tổng trước/sau sửa |
| Nhận 0, số âm, số lẻ hoặc tiền vượt `1e9` | Chặn nộp | Kiểm tra đúng hợp đồng `amount` | Ca bị từ chối; nhận 1 và `1e9` |
| Nhận khoản thứ 501 hoặc tổng rỗng khác 0 | Chặn nộp | Sửa giới hạn và tổng ban đầu | Kết quả thử 500/501 khoản và rỗng |
| Hiện tên bằng `innerHTML` | Chặn nộp | Dùng `cell.textContent` như trong `app.js` | Diff; `<b>Vở</b>` hiện nguyên văn |
| Có dữ liệu thật không cần thiết hoặc khóa thật | Chặn nộp | Dừng chia sẻ; xử lý khóa theo 4.6; dùng dữ liệu giả | Ghi nhận xử lý, không đính kèm bí mật |
| Mã chưa rõ giấy phép | Chặn nộp phần đó | Loại/thay hoặc xác minh quyền | Nguồn, giấy phép hoặc phần thay thế |
| Chưa rõ phạm vi dùng AI | Hỏi giảng viên | Hỏi cụ thể; không mặc định được phép | Phản hồi hoặc trạng thái chờ |
| Khai báo sai mức hỗ trợ AI | Chặn nộp | Khai đúng và theo hướng dẫn môn | Khai báo khớp đóng góp |
| Gói AI đề xuất chưa xác minh | Chặn đưa gói vào bản nộp | Không cài; xác minh hoặc bỏ | Registry, người duy trì, nguồn, giấy phép |
| Màu nút hoặc khoảng cách chưa đẹp | Cải thiện sau | Ưu tiên yêu cầu cốt lõi | Danh sách cải tiến |

Chặn nộp không có nghĩa hủy cả bài: có thể loại phần chưa rõ hoặc thu hẹp chức năng nếu vẫn đáp ứng yêu cầu. Hỏi giảng viên không có nghĩa được bỏ qua trong lúc chờ. Màu sắc có thể cải thiện sau, dữ liệu thật trong ảnh thì không.

#### Ghi bằng chứng gọn và có thể đối chiếu

Ghi mục tiêu, đầu vào, mong đợi, quan sát, trạng thái và bản mã kiểm tra. Ví dụ: “Tổng mẫu; ba khoản giả; mong đợi 60000; quan sát [điền sau khi chạy]; chưa chạy/đạt/không đạt”. Ghi riêng fixture SQL; chỉ giữ vùng ảnh cần thiết.

Bộ kiểm thử đi kèm cẩm nang có hai phần riêng, đừng cộng gộp hay nhắc sai số: `vi-du/nam-2-web/test_data.cjs` được định hướng gồm **33 ca** cho phần dữ liệu Web, còn `vi_sinh_vien.exe --test` của bản C++ chỉ in **9 ca**. Con số ca không đồng nghĩa đã chạy hay bảo đảm chất lượng. Đối chiếu bộ mình nhận được, ghi cách chạy, số ca thực sự thực thi và kết quả. Chưa có xác nhận thì ghi “chưa xác minh”. Đọc giấy phép, hỏi phạm vi AI và rà ảnh vẫn là việc của người làm.

#### Rubric bốn mục để tự đánh giá

Mỗi mục 0–2 điểm, tổng tối đa 8. Đây là rubric luyện tập, không phải thang điểm chính thức của TLU; điểm tổng không bù được vấn đề chặn nộp.

| Mục | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| 1. Trung thực học thuật và nguồn | Không rõ phạm vi, đóng góp hoặc nguồn | Có khai báo nhưng còn mơ hồ | Phạm vi rõ; hỗ trợ, nguồn và quyền được ghi đúng |
| 2. Dữ liệu và quyền truy cập | Dùng dữ liệu thật không cần thiết hoặc quyền quá rộng | Có giảm dữ liệu nhưng chưa rà đủ bản chia sẻ | Dùng dữ liệu giả; rà ảnh/tệp; quyền phù hợp công việc |
| 3. Tính đúng và đọc mã an toàn | Không đối chiếu hợp đồng, nhầm SQL là backend | Biết sửa nhưng bằng chứng còn thiếu | Đối chiếu các giới hạn, hiển thị văn bản và ranh giới ví dụ |
| 4. Kiểm chứng và xử lý vấn đề | Tuyên bố đạt không có căn cứ | Ghi được một phần kết quả và việc còn thiếu | Bằng chứng truy lại được; ưu tiên đúng; báo cáo trung thực |

#### Sáu tình huống tự trả lời, kèm đáp án

**Tình huống 1.** Đề chỉ ghi “tham khảo tài liệu”. Minh khai báo đầy đủ việc AI sinh hàm. Đã chắc được phép chưa?

**Đáp án:** Chưa. Khai báo không thay sự cho phép. Hỏi giảng viên về việc đã làm, không đổi lời khai thành “gợi ý nhẹ”; chưa mặc định phần đó hợp lệ.

**Tình huống 2.** Lan bỏ tên trong chi tiêu thật nhưng giữ mã sinh viên, giờ, địa điểm; ảnh còn email. Đã là dữ liệu giả hoặc ẩn danh chưa?

**Đáp án:** Chưa. Các trường còn lại vẫn có thể nhận diện người. Tạo dữ liệu giả mới, loại ảnh chứa thông tin thật và kiểm tra bản gửi cuối.

**Tình huống 3.** SQL nối chuỗi bị lỗi với `Vở O'Reilly`. Có nên xóa dấu nháy khỏi tên để sửa?

**Đáp án:** Không thay truy vấn tham số hóa bằng cách đó. Dùng `execute('SELECT title,amount FROM expenses WHERE title = ?', (title,))`; dấu phẩy tạo tuple một phần tử. Kiểm tra fixture SQL riêng trong `:memory:`, không thêm backend cho Web.

**Tình huống 4.** `<b>Vở</b>` hiện in đậm; vòng lặp C++ dùng `i <= n` vẫn chạy xong. Đã đạt chưa?

**Đáp án:** Chưa. Tên phải hiện nguyên văn bằng `textContent` trong ô bảng. Vòng lặp chạm chỉ số `n` có thể vượt biên; hành vi không xác định không nhất thiết crash. Sửa hợp đồng, không dựa vào may mắn.

**Tình huống 5.** Kho công khai không có giấy phép thì được chép, còn GPL cấm thương mại: đúng không?

**Đáp án:** Cả hai đều sai. Công khai không tự cấp quyền. GPL không cấm thương mại; nghĩa vụ phụ thuộc giấy phép và cách chuyển giao, kết hợp mã. Tránh đoạn chưa rõ quyền; lời AI không thay giấy phép.

**Tình huống 6.** Đã commit khóa thật, Minh xóa tệp, tạo khóa mới rồi định ép đẩy lịch sử. Thiếu gì?

**Đáp án:** Xác nhận khóa cũ bị vô hiệu; dừng chia sẻ, kiểm tra usage/log được phép, báo đầu mối và phối hợp giảm bản lưu. Không tự ý viết lại lịch sử. Khóa mới và xóa tệp không tự xử lý khóa cũ hoặc mọi bản sao.

#### Mẫu khai báo AI dùng cho bản nộp

Điền bằng sự thật, bỏ mục không áp dụng; không biến mẫu thành lời khẳng định đã thực hiện:

> **Bài/nhóm:** ViSinhVien — [thành viên và vai trò].
>
> **Phạm vi được phép:** [hướng dẫn của bài hoặc phản hồi giảng viên; nếu chưa rõ, ghi đang chờ].
>
> **Công cụ và thời điểm:** [tên, phiên bản nếu biết, ngày dùng].
>
> **Hỗ trợ thực tế:** [giải thích, gợi ý, sinh nháp phần nào; tệp/hàm liên quan].
>
> **Đóng góp của nhóm:** [ai viết lại gì, lựa chọn nào được giữ hoặc bỏ và lý do].
>
> **Dữ liệu đã cung cấp:** [bộ dữ liệu giả, đoạn mã cần thiết; nếu có sự cố, báo theo kênh phù hợp, không dán bí mật].
>
> **Nguồn và giấy phép:** [nguồn thật đã dùng, điều kiện cần giữ, phần đã loại vì chưa rõ].
>
> **Kiểm chứng:** [đã chạy gì, trên bản nào, kết quả; phần chỉ đọc mã; phần chưa xác minh].
>
> **Giới hạn:** Ứng dụng HTML và JavaScript dùng `localStorage`, không backend/đăng nhập; chỉ phục vụ học tập với dữ liệu giả. SQL là minh họa Python `sqlite3` riêng trong `:memory:`.

#### Checklist một trang trước khi gửi

Dùng danh sách ngắn này cho bản nộp cuối; đánh dấu sau khi làm, không đánh dấu theo dự định. Bố cục in có thể cần chỉnh theo khổ giấy.

**A. Chặn nộp nếu chưa xử lý**

- [ ] Không còn khóa thật hoặc dữ liệu cá nhân không cần thiết trong phạm vi tệp, ảnh và nội dung sẽ chia sẻ; sự cố đã phát hiện được báo và xử lý phù hợp.
- [ ] Bộ ba khoản GIẢ đúng 35000 + 7000 + 18000 = 60000; rỗng bằng 0; `amount` nguyên, dương, không quá `1e9`; tối đa 500 khoản.
- [ ] Tên khoản chi được hiển thị như văn bản bằng `textContent`, trong `app.js` là `cell.textContent`; đã ghi trạng thái kiểm tra chuỗi `<b>Vở</b>`.
- [ ] Không đưa vào đoạn mã chưa rõ quyền hoặc phụ thuộc chưa kiểm chứng; giữ thông báo giấy phép cần thiết.
- [ ] Khai báo AI đúng việc đã làm; không nhận là tự viết phần được sinh nháp, không ghi đã test khi chưa test.
- [ ] Phần kiểm chứng bắt buộc theo yêu cầu bài đã có kết quả thật; lỗi trọng yếu còn lại chưa bị che bằng điểm rubric.

**B. Hỏi giảng viên hoặc người phụ trách khi chưa rõ**

- [ ] Đã làm rõ phạm vi AI, hỗ trợ nhóm và hình thức khai báo; phần chưa rõ được ghi trạng thái chờ, không mặc định được phép.
- [ ] Đã hỏi về nguồn/giấy phép hoặc dữ liệu thật nếu bài bắt buộc dùng mà nhóm chưa xác định được điều kiện.
- [ ] Việc ngoài quyền của nhóm, như xử lý tài khoản tổ chức hay lịch sử kho chung, được chuyển đúng đầu mối.

**C. Cải thiện sau, không làm sai mô tả hiện tại**

- [ ] Ghi riêng việc chỉnh giao diện và mở rộng tính năng, không lẫn với yêu cầu an toàn cốt lõi.
- [ ] Nêu rõ Web không backend; SQL riêng; không quảng bá `localStorage` là nơi bảo vệ tài chính thực tế.
- [ ] Giữ bằng chứng tối thiểu đủ đối chiếu, tránh tạo thêm ảnh, log hoặc bản sao chứa dữ liệu thừa.

#### Tóm tắt và Speaker Notes

**Tóm tắt cho người học:** Làm chủ ViSinhVien là hiểu đặc tả, biết quyền dùng nguồn và công cụ, kiểm soát dữ liệu đưa đi, kiểm chứng đường đi của đầu vào và khai báo trung thực. `textContent`, truy vấn tham số hóa và kiểm tra giới hạn là biện pháp đúng trong ngữ cảnh cụ thể, không phải bùa bảo đảm mọi hệ thống an toàn. Khi có sự cố, ưu tiên khống chế quyền đã lộ và báo đúng người, không chỉ xóa dấu vết nhìn thấy.

**Speaker Notes — gợi ý trình bày 6 phút:**

- **Phút 1:** Kể cảnh Minh định nộp vì tổng đã đúng. Hỏi lớp: “60000 chứng minh được điều gì, chưa chứng minh được điều gì?” Chốt kiến trúc không backend và dữ liệu giả.
- **Phút 2:** Đọc tin nhắn hỏi giảng viên. Nhấn mạnh phạm vi tùy môn; khai báo không thay giấy phép và không thay sự cho phép.
- **Phút 3:** Dùng hai chuỗi vô hại `Vở O'Reilly` và `<b>Vở</b>` để giải thích tách dữ liệu khỏi cú pháp. Không biểu diễn tấn công và không ngụ ý SQL thuộc Web.
- **Phút 4:** Cho lớp phân loại một ảnh chứa email và một đoạn mã không giấy phép. Hỏi cách giảm dữ liệu, giảm quyền, giảm phụ thuộc.
- **Phút 5:** Đi qua thứ tự xử lý khóa: dừng chia sẻ, thu hồi/xoay vòng, kiểm tra, báo, giảm bản lưu. Nhấn mạnh xóa tệp không vô hiệu khóa.
- **Phút 6:** Chọn hai dòng chặn nộp trong bảng, yêu cầu bằng chứng cụ thể. Kết thúc bằng câu: “Em biết gì, chưa xác minh gì, bước tiếp theo là gì?”

#### Nguồn đối chiếu của chương

Mốc đối chiếu nội dung nguồn: **29/10/2026**. Các nguồn pháp luật dùng để định hướng và xác định văn bản áp dụng; tình huống thật cần người có thẩm quyền đánh giá. Các hướng dẫn kỹ thuật cần được đọc trong đúng ngữ cảnh công nghệ.

1. [Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf): khái niệm, khử nhận dạng, nguyên tắc, sự đồng ý, ngoại lệ và xử lý dữ liệu trong hoạt động AI.
2. [Nghị định 356/2025/NĐ-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/17/356signed-1768638052103952849513.pdf): văn bản triển khai hiện hành tại mốc đối chiếu; Điều 42 về hiệu lực và việc Nghị định 13/2023/NĐ-CP hết hiệu lực.
3. [Văn bản hợp nhất 67/VBHN-VPQH ngày 23/03/2026 về Luật Sở hữu trí tuệ](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469197-1775632354_v1_1775783230_signed.pdf): bảo hộ chương trình máy tính và giới hạn của ngoại lệ liên quan.
4. [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html): truy vấn tham số hóa và danh sách cho phép đối với phần cấu trúc cần kiểm soát.
5. [OWASP — Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html): nơi nhận dữ liệu an toàn như `textContent` trong ngữ cảnh phù hợp và bảo vệ theo ngữ cảnh.
6. [OWASP — Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html): đánh giá phụ thuộc và rủi ro chuỗi cung ứng phần mềm.
7. [GitHub Docs — Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): thu hồi/xoay vòng bí mật trước, giới hạn của việc xóa dữ liệu khỏi lịch sử và các bản sao.
8. [GitHub Docs — Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository): ý nghĩa của giấy phép và giới hạn quyền khi kho chỉ được công khai.


---


## Trước khi khép lại

Mở lại một bài tập của mình, chọn đúng một hàm và tự trả lời: đầu vào là gì, kết quả mong đợi là gì, mình đã kiểm tra thế nào? Nếu ba câu ấy còn mơ hồ, hãy quay lại ví dụ nhỏ trước khi yêu cầu AI làm thêm tính năng.

### Phạm vi đã kiểm tra của bộ ví dụ

Bản C++ mẫu được biên dịch bằng g++ 11.4.0 trong Ubuntu 22.04 qua WSL; bản đúng có 9 test, bản lỗi chủ đích cho 42.000 như dự đoán. Bộ logic JavaScript có 33 test chạy bằng Node.js 24.21.0. Minh họa Python/SQLite chỉ dùng CSDL trong bộ nhớ. Đây là kiểm tra của các tệp đi kèm, không phải bằng chứng mọi đoạn mã minh họa hoặc mọi môi trường máy sinh viên đã được kiểm thử.

Bản đọc HTML hoạt động ngoại tuyến; bản demo Web không gọi dịch vụ AI hoặc gửi dữ liệu ra mạng. Các mô phỏng trong sách là JavaScript phục vụ học, không thực thi C++ và không gọi API tính tiền thật. Dữ liệu và hội thoại minh họa đều được ghi rõ là giả định. Chưa có quy định sử dụng AI nội bộ TLU được cung cấp để xác minh, vì vậy luôn đối chiếu yêu cầu thực tế của học phần.
