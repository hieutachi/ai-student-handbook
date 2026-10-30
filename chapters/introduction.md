# LỜI GIỚI THIỆU

**Học CNTT cùng AI — Cẩm nang tự học và tra cứu dành cho sinh viên năm thứ nhất và năm thứ hai, Khoa Công nghệ thông tin, Trường Đại học Thủy lợi.**

## Mục đích và đối tượng của sách

Các công cụ trí tuệ nhân tạo (AI) hiện có thể giải thích lỗi, đề xuất mã nguồn và gợi ý ca kiểm thử chỉ trong vài giây. Điều đó tạo ra một câu hỏi cho người học lập trình: làm thế nào để tận dụng công cụ mà không giao luôn phần suy nghĩ cho nó. Cuốn sách này trả lời câu hỏi đó bằng các kỹ năng cụ thể: hiểu AI giúp được gì và không giúp được gì, điều khiển quá trình làm việc với AI, tự làm và tự giải thích được kết quả, chịu trách nhiệm về dữ liệu, nguồn và bản nộp, và cuối cùng là chọn công cụ phù hợp.

Đối tượng chính là sinh viên năm thứ nhất và năm thứ hai ngành Công nghệ thông tin. Người học năm thứ nhất cần biết biến, câu lệnh điều kiện và vòng lặp trong C++. Người học năm thứ hai có thể tận dụng thêm kiến thức về Web, lập trình hướng đối tượng, cấu trúc dữ liệu và cơ sở dữ liệu. Giảng viên và cố vấn học tập có thể dùng sách làm tài liệu cho buổi chia sẻ, thảo luận hoặc luyện tập. Không cần mua dịch vụ AI trả phí để bắt đầu học theo sách.

## Câu chuyện xuyên suốt của cuốn sách

Cuốn sách kể một câu chuyện duy nhất: quan hệ giữa người học và AI. Câu chuyện đi qua năm bước, và mỗi chương là một bước.

**Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn**

| Chương | Câu hỏi trung tâm | Thông điệp |
|---|---|---|
| 1 | AI là gì, đóng vai trò gì trong học tập, giúp được gì và không giúp được gì? | AI là người hỗ trợ; người học là người quyết định. |
| 2 | Dùng AI thế nào để việc làm có kiểm soát? | Giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. |
| 3 | Tận dụng AI mà không lạm dụng: làm sao vẫn học được? | Tự dự đoán, tự làm, tự giải thích; AI chỉ đứng cạnh. |
| 4 | Ranh giới nào cần giữ về dữ liệu, bảo mật, bản quyền, liêm chính? | Dùng có trách nhiệm là điều kiện để được tiếp tục dùng. |
| 5 | Khi đã hiểu vai trò, cách dùng và ranh giới: chọn AI, model, gói dịch vụ nào cho nhiệm vụ này? | Chọn theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng. |

Dự án tổng kết ghép năm bước thành một sản phẩm có bằng chứng: làm, kiểm, giải thích.

Vì sao việc chọn model và trả phí nằm ở cuối? Nhiều người bắt đầu bằng câu hỏi "dùng AI nào là tốt nhất?". Câu hỏi đó khó trả lời khi chưa biết AI giúp được gì, cần dùng ra sao và có những ranh giới nào. Khi đã đi qua bốn chương đầu, người học đã rõ cần gì ở công cụ, nên chọn theo nhiệm vụ, rủi ro và ngân sách thay vì theo danh tiếng hay quảng cáo.

Xuyên suốt năm bước chỉ có một ý cần nhớ: **AI hỗ trợ, người học quyết định.**

## Phạm vi và tính chất của nội dung

Phần này nêu tuyên bố phạm vi chung cho toàn bộ cuốn sách. Các chương sau chỉ nhắc lại ngắn gọn khi cần.

- **Nhân vật, hội thoại, tình huống và dữ liệu trong sách đều hư cấu.** Chúng không phải kết quả khảo sát sinh viên Trường Đại học Thủy lợi và không phải bảng giá thực tế của bất kỳ dịch vụ nào.
- **Sách không phải quy định chính thức của Trường Đại học Thủy lợi**, không phải đề cương học phần, không phải tài liệu quảng cáo và không phải tư vấn pháp lý. Việc được dùng AI đến mức nào trong một bài cụ thể do yêu cầu của học phần và giảng viên quyết định.
- **Thông tin về sản phẩm, dịch vụ và văn bản pháp lý có mốc thời gian.** Các thông tin này được đối chiếu tại mốc 29/10/2026 và không bảo đảm còn áp dụng tại thời điểm đọc. Trước khi dựa vào một thông tin như vậy, người đọc cần tra lại nguồn ở cuối chương, kiểm tra ngày cập nhật, đúng tên sản phẩm và điều kiện tài khoản.
- Rubric, thang điểm và mục tiêu trong sách dùng để tự luyện, không thay thế chuẩn đầu ra (CLO) hay thang điểm của học phần.

Để người đọc biết điều gì đã được kiểm chứng, sách dùng thống nhất bốn nhãn: *Tình huống hư cấu* cho nhân vật, hội thoại và thẻ trả lời minh họa; *Dữ liệu giả định* cho số tiền, giá và các kịch bản tính toán; *Chưa kiểm chứng* cho thông tin dịch vụ, chính sách và giá cần tra lại; *Kết quả mong đợi* cho đầu ra suy ra từ mã nguồn nhưng chưa thực thi.

## Tình huống minh họa xuyên suốt

Toàn bộ sách dựa trên một tình huống minh họa chung với hai người học:

- **Minh** là sinh viên năm thứ nhất, đã biết biến và vòng lặp trong C++, nhưng có thói quen hỏi AI ngay khi gặp lỗi.
- **Lan** là sinh viên năm thứ hai, đã học Web, lập trình hướng đối tượng, cấu trúc dữ liệu và cơ sở dữ liệu. Lan dựng được giao diện nhưng còn lúng túng khi một lỗi đi qua nhiều tệp.

Hai người cùng xây dựng **ViSinhVien**, một ứng dụng ghi các khoản chi tiêu nhỏ. Bảng dữ liệu mẫu dưới đây được dùng thống nhất trong mọi chương:

| Khoản chi | Nhóm | Số nguyên lưu trong mã | Hiển thị |
|---|---|---:|---:|
| Cơm trưa | Ăn uống | `35000` | 35.000 đ |
| Xe buýt | Đi lại | `7000` | 7.000 đ |
| Vở ghi | Học tập | `18000` | 18.000 đ |
| **Tổng đối chiếu** | | **`60000`** | **60.000 đ** |

Hai vấn đề mở đầu dẫn dắt nội dung của sách. Phiên bản C++ của Minh cho tổng `42000` thay vì `60000`. Lan cần xác định giá trị tiền đi từ ô nhập đến phần tính tổng như thế nào. Qua các chương, người học lần lượt dự đoán, kiểm tra một thay đổi nhỏ và giải thích vì sao thay đổi đó đúng.

## Hợp đồng dữ liệu chung của ViSinhVien

Mọi ví dụ, bài thực hành và bộ kiểm thử trong sách tuân theo cùng một hợp đồng dữ liệu (quy ước về miền giá trị hợp lệ):

- `amount` là **số nguyên VND từ 1 đến 1.000.000.000 (`1e9`), tính cả hai đầu**.
- Danh sách có tối đa **500 khoản**. Danh sách rỗng là hợp lệ và có tổng bằng **0**.
- Khoản bằng 0, số âm, số thập phân (ví dụ 1.5) hoặc giá trị vượt trần đều bị từ chối.
- Dấu chấm trong “35.000 đ” chỉ dùng khi hiển thị, không thuộc giá trị lưu trữ.

Hai nhánh dùng cùng số tiền mẫu nhưng **khác cấu trúc dữ liệu**:

- Nhánh C++ dùng `std::vector<long long>` chứa `{35000, 7000, 18000}`. Cấu trúc này chỉ chứa số tiền, chưa có tên, nhóm hay mã khoản.
- Nhánh Web dùng danh sách đối tượng `Expense` có **bốn trường**:

```json
{"id": 1, "title": "Cơm trưa", "amount": 35000, "category": "an-uong"}
```

Trong đó, `id` dùng để nhận diện khoản chi, `title` là tên khoản, `amount` là số tiền và `category` là mã nhóm (không phải nhãn hiển thị). Ô nhập trên Web trả về chuỗi, vì vậy việc chuyển đổi kiểu không thay thế được bước kiểm tra hợp lệ. Tương tự, hàm tính tổng không thay thế được bước kiểm tra bản ghi đầy đủ khi đọc và lưu dữ liệu.

Tổng cực đại `500000000000` nằm trong miền số nguyên an toàn của JavaScript và biểu diễn được bằng kiểu `long long` của C++. Đây là quy ước phục vụ học tập, không phải thiết kế dùng chung cho mọi hệ thống tài chính. Khi thay đổi giới hạn hoặc đơn vị tiền, cần xét lại toàn bộ hợp đồng.

Ứng dụng Web chỉ gồm HTML, JavaScript và `localStorage`, **không có backend và không có chức năng đăng nhập**. SQLite xuất hiện trong một minh họa Python riêng, dùng cơ sở dữ liệu `:memory:`, và không phải cơ sở dữ liệu của ứng dụng Web. Không nhập sao kê, chi tiêu thật hay thông tin cá nhân vào bất kỳ ví dụ nào.

## Hai lộ trình đọc

**Lộ trình C++ (theo tình huống của Minh).** Chương 1 giúp hiểu vai trò của AI và nhận diện công cụ đang dùng. Chương 2 hướng dẫn đọc vòng lặp, lập bảng trace và sửa lỗi bỏ sót khoản cuối. Chương 3 yêu cầu tự làm bài biến thể. Chương 4 hướng dẫn chuẩn bị một bản nộp trung thực. Chương 5 giúp Minh chọn công cụ và gói dịch vụ phù hợp với nhiệm vụ và ngân sách. Người học chưa học Web hoặc SQL có thể tạm bỏ qua các phần đó; nhánh C++ không yêu cầu cài thêm công cụ nào khác.

**Lộ trình Web (theo tình huống của Lan).** Sau Chương 1, Chương 2 hướng dẫn lần theo giá trị `amount` từ biểu mẫu, qua bước xử lý, đến hiển thị và lưu trữ. Chương 3 yêu cầu tự giải thích kiểu dữ liệu và làm bài biến thể. Chương 4 rà soát quyền, dữ liệu và nguồn. Chương 5 giúp Lan đối chiếu công cụ theo từng tác vụ Web và ước tính chi phí. Khi Lan cùng xem mã C++ với Minh, đó là hoạt động đọc chéo và không làm thay đổi lộ trình của Minh.

Người học không cần hoàn thành cả hai lộ trình cùng lúc. Một hàm tự giải thích được có giá trị học tập cao hơn một ứng dụng hoàn chỉnh được sao chép mà chưa hiểu.

![Bản đồ bốn năng lực của sách: nhận diện công cụ, điều khiển quá trình, tự làm và chịu trách nhiệm; mỗi năng lực gắn với một loại bằng chứng.](../assets/skill-map.svg)

*Hình. Bản đồ bốn năng lực và bằng chứng tương ứng. Bản đồ dùng để chọn nội dung cần luyện tiếp, không phải chứng nhận năng lực tự động. Bảng ở mục sau trình bày các bằng chứng này dưới dạng văn bản.*

## Mục tiêu học tập và bằng chứng

Các mục tiêu dưới đây là mục tiêu của cẩm nang, **không thay thế chuẩn đầu ra (CLO) hoặc thang điểm của học phần**. Người học nên chọn từng dòng để tự kiểm tra bằng sản phẩm cụ thể, thay vì đánh dấu hoàn thành chỉ vì đã đọc hết chương.

| Mục tiêu | Nội dung tương ứng | Bằng chứng do người học tạo ra |
|---|---|---|
| Nêu được vai trò, lợi ích và giới hạn của AI trong học tập | Chương 1 (mục 1.1) | Bảng phân loại một việc cụ thể thành dùng đúng hoặc lạm dụng, kèm lý do. |
| Phân biệt model, provider và ứng dụng | Chương 1 (mục 1.2) | Bảng nhận diện công cụ, có ghi những điều chưa xác định. |
| Giao việc nhỏ với đủ ngữ cảnh | Chương 1 (mục 1.3) và Chương 2 | Yêu cầu có mục tiêu, dữ liệu, phạm vi và tiêu chí kiểm tra. |
| Đọc lỗi, đọc diff và kiểm thử | Chương 2 | Bảng trace lỗi `42000` so với `60000`; kiểm tra danh sách rỗng và danh sách một phần tử; lần theo `amount`. |
| Học chủ động | Chương 3 | Bài biến thể tự làm khi không mở AI. |
| Giải thích phần việc tự làm | Chương 3 | Câu trả lời cho “vì sao?” và “nếu đổi yêu cầu thì sao?”, kèm ghi chú về chỗ còn vướng. |
| Bảo vệ dữ liệu, rà soát mã và phụ thuộc | Chương 4 | Quyết định về dữ liệu được gửi, điểm hiển thị, truy vấn SQL và gói thư viện được đề xuất. |
| Khai báo, kiểm tra quyền, xử lý sự cố | Chương 4 | Bản khai báo đúng mức hỗ trợ, câu hỏi gửi giảng viên, thứ tự xử lý khi lộ khóa API. |
| Chọn công cụ và gói dịch vụ phù hợp với nhiệm vụ và khả năng chi trả | Chương 5 | Phép tính lại chi phí từ giả định, bảng đối chiếu công cụ theo tác vụ, kèm giới hạn của phép so sánh. |

Các chương tương ứng là: Chương 1 · AI trong học tập: vai trò, cách hoạt động và giới hạn ([chapter-01.md](chapter-01.md)); Chương 2 · Điều khiển quá trình làm việc với AI ([chapter-02.md](chapter-02.md)); Chương 3 · Học chủ động: dùng AI mà không lạm dụng ([chapter-03.md](chapter-03.md)); Chương 4 · Sử dụng AI có trách nhiệm ([chapter-04.md](chapter-04.md)); Chương 5 · Lựa chọn AI và model phù hợp với nhiệm vụ ([chapter-05.md](chapter-05.md)). Dự án tổng kết ([final-boss.md](final-boss.md)) ghép năm bước thành một bản nộp có bằng chứng.

## Hướng dẫn sử dụng sách

### Trước, trong và sau buổi học

**Trước buổi chia sẻ.** Đọc lời giới thiệu và mục 1.1 về vai trò của AI ở Chương 1, chuẩn bị một câu hỏi thực tế. Chưa cần cài phần mềm ở giai đoạn này. Phần chi phí và chọn công cụ nằm ở Chương 5, có thể đọc sau khi đã quen cách dùng.

**Trong buổi.** Viết dự đoán trước khi xem phần chạy mẫu hoặc đáp án. Ghi lại chỗ đã hiểu sai thay vì chỉ chụp màn hình.

**Sau buổi.** Chọn một nhiệm vụ vừa sức, thực hiện trong khoảng 20–25 phút theo trình tự: đọc, dự đoán, thử, đối chiếu và giải thích. Kết thúc bằng ba dòng ghi chú theo mẫu: “Đã hiểu…”, “Chưa chắc…”, “Lần tới sẽ…”. Thời lượng chỉ là gợi ý. Nếu chưa xong, cần lưu lại đầu vào, lỗi gặp phải và bước đang làm; không dùng tốc độ làm thước đo năng lực.

### Bản đọc HTML và đọc ngoại tuyến

Bản HTML có mục lục, ô tìm mục, nút chỉnh cỡ chữ và chức năng in. Các mục **Đáp án** được gập sẵn và chỉ nên mở sau khi đã tự làm. Để đọc ngoại tuyến đầy đủ hình và ví dụ, cần giữ nguyên cả thư mục sách. Các nguồn tham khảo bên ngoài và dịch vụ AI cần kết nối mạng; các mô phỏng trong sách chạy cục bộ và không gọi tới AI. Người học không có tài khoản dịch vụ AI vẫn học được bằng đề bài, bảng trace và các phiếu trả lời minh họa.

### Phân biệt các loại kết quả

Cần phân biệt rõ **hội thoại mô phỏng**, **bảng trace**, **kết quả mong đợi** và **kết quả thực sự chạy**. Các tệp có lỗi chủ đích được giữ nguyên làm đối tượng học; việc sửa lỗi được thực hiện trên bản sao. Tổng trung gian `42000` tự nó chưa chứng minh có lỗi; cần biết vòng lặp đã duyệt đến phần tử nào. Khi chưa có môi trường để chạy, ghi trạng thái **chưa chạy** và không chép kết quả mong đợi thành kết quả quan sát.

### Các tệp ví dụ

Khi thực hiện lệnh ở Chương 2, mở thư mục gốc `AI-Student-Handbook`. Thư mục `vi-du/` được giữ làm bản tham khảo. Người học tự tạo thư mục `bai-lam/` (chưa có sẵn) theo hướng dẫn ở mục 2.1, sau đó sao chép nhánh cần làm sang thư mục này trước khi sửa.

| Tệp | Mục đích và điều kiện sử dụng |
|---|---|
| [C++ có lỗi chủ đích](../vi-du/nam-1-cpp/loi-bo-sot.cpp) | Lập bảng trace cho tổng bị thiếu. Chuẩn C++17, không có chế độ `--test`. Nếu chưa có trình biên dịch, đọc bảng trace trước. |
| [C++ đúng, có kiểm thử](../vi-du/nam-1-cpp/vi_sinh_vien.cpp) | Đối chiếu cách sửa lỗi và các giới hạn. Cần trình biên dịch C++17, ví dụ g++. |
| [Web ViSinhVien](../vi-du/nam-2-web/index.html) | Thử nhập khoản chi giả trên trình duyệt hiện đại. Giữ tệp này cùng thư mục với `data.js` và `app.js`. |
| [Kiểm thử dữ liệu Web](../vi-du/nam-2-web/test_data.cjs) | Kiểm tra phần logic dữ liệu, không chứng minh phần DOM và lưu trữ. Cần Node.js phiên bản hiện đại, không cần `npm install`. |
| [SQLite riêng](../vi-du/minh-hoa-sqlite.py) | Minh họa truy vấn tham số hóa với bộ dữ liệu kiểm thử (fixture) riêng. Cần Python 3 có mô-đun `sqlite3`; đây không phải backend của ứng dụng Web. |

`localStorage` lưu dữ liệu trong trình duyệt, không lưu trên máy chủ. Quyền lưu khi mở tệp cục bộ phụ thuộc vào từng trình duyệt. Khi không lưu được, bản minh họa có thể báo lỗi và chuyển sang bộ nhớ tạm; mọi thay đổi sẽ mất khi kết thúc phiên. Vì vậy không dùng bản minh họa để lưu dữ liệu lâu dài.

## Nguyên tắc học tập khi có AI hỗ trợ

Khi có hướng dẫn mới hơn của học phần hoặc gặp điều chưa rõ, người học cần hỏi người phụ trách. Câu trả lời của AI hay một liên kết tìm được không thay thế cho việc kiểm chứng.

> **Thỏa thuận học tập:** AI có thể giải thích, đưa ra giả thuyết, đề xuất mã nguồn và hỗ trợ kiểm tra. Người học quyết định mục tiêu, phần việc tự làm, phạm vi chia sẻ dữ liệu và bằng chứng cần có. “AI đã làm xong” chưa có nghĩa là “người học đã học xong”.

Các phần tham khảo đi kèm gồm: [Thỏa thuận học tập](learning-agreement.md) với các mẫu biểu để điền, [Bảng thuật ngữ](glossary.md) và [Thư viện prompt mẫu](prompt-library.md).
