# CHƯƠNG 3 · ĐỪNG ĐỂ AI SUY NGHĨ THAY BẠN

Minh đóng cửa sổ chat, nhìn lại vòng lặp vừa sửa. Tổng đã thành **60000**, nhưng khi Lan hỏi “Nếu chỉ có một khoản thì sao?”, Minh lại muốn mở chat. Lan cũng có chuyện tương tự: giao diện Web hoạt động, nhưng cô chưa giải thích được vì sao giá trị đọc từ ô nhập phải qua hai bước chuyển kiểu và kiểm tra. Hai bạn thống nhất một cuộc hẹn khác: không mang đến câu trả lời dài nhất, mà mang đến **một điều tự giải thích được khi không còn nhìn lời giải**.

**Nhân vật, tình huống và hội thoại trong chương đều HƯ CẤU.** Minh học C++ năm nhất; Lan học Web/OOP/DSA/CSDL năm hai. Đây không phải khảo sát, chuẩn đầu ra hoặc quy định chính thức của TLU. Quyền dùng AI trong bài nộp tùy từng học phần.

Chương này luyện dự đoán, tự sửa, kiểm chứng và vận dụng. Chọn một nhánh thực hành sâu, đọc nhánh kia để đối chiếu; không cần làm hết trong một buổi.

**Quy ước:** gọi gốc `AI-Student-Handbook` là **NEW**. Mở NEW, dùng bản sao `bai-lam/nam-1-cpp` và `bai-lam/nam-2-web` đã tạo ở Chương 2; `vi-du` chỉ tham khảo. Nếu thiếu bản sao, làm mục 2.1 của [Chương 2](chapter-02.md). Ghi trong vở hoặc `bai-lam/nam-1-cpp/ghi-chep-02.txt` (tệp đã tạo ở Chương 2). Không cài đặt, đổi cấu hình, đăng nhập, gọi API hay truy cập mạng. Không có AI thì dùng hội thoại hư cấu làm phiếu gợi ý, ghi đúng là học bằng phiếu.

## 3.1. AI TRAP — Câu trả lời tự tin có giữ lại phần học của bạn?

### Một hợp đồng nhỏ để không tranh luận bằng cảm giác

ViSinhVien dùng dữ liệu **hoàn toàn giả** sau. Bảng này là điểm tựa để tính tay, không phải lịch sử chi tiêu thật.

| id | title | amount | category |
| --- | --- | ---: | --- |
| 1 | Cơm trưa | 35000 | `an-uong` |
| 2 | Xe buýt | 7000 | `di-lai` |
| 3 | Vở ghi | 18000 | `hoc-tap` |

“Hợp đồng” là điều kiện đầu vào và kết quả phải bảo đảm, không phải điều AI được tự thay cho tiện viết code.

| Phần hợp đồng | Quy định của bài |
| --- | --- |
| Tiền | `amount` là số nguyên VND từ 1 đến 1000000000, không lưu chuỗi có dấu phân cách. |
| Danh sách | Tối đa 500 khoản; rỗng hợp lệ, tổng bằng 0. |
| Tổng | Mẫu có tổng 60000; cực đại là `500 × 1000000000 = 500000000000`. |
| C++ năm nhất | Chỉ dùng `vector<long long>` chứa tiền; không yêu cầu class `Expense`. |
| Web năm hai | Mỗi `Expense` có `id`, `title`, `amount`, `category`. |
| `id` Web | Số nguyên an toàn, dương, không trùng trong danh sách. |
| `title` Web | Chuỗi; sau `trim()` dài 1–80 **đơn vị UTF-16**, theo `.length` của JavaScript. |
| `category` Web | **Chuỗi** thuộc `an-uong`, `di-lai`, `hoc-tap`, `khac`; mảng `['khac']` không hợp lệ. |

Trong C++, `long long` đủ chứa tổng cực đại, còn số nguyên có dấu 32 bit thì không. Trong JavaScript, 500000000000 nằm trong miền số nguyên an toàn của `Number`, giới hạn trên là 9007199254740991. “Biểu diễn được” vẫn khác “được phép”: số âm biểu diễn được nhưng vi phạm hợp đồng tiền. Độ dài UTF-16 cũng không luôn bằng số ký tự nhìn thấy; một số ký hiệu được tính bằng hai đơn vị.

Bản Web là HTML/JavaScript với `localStorage`, không backend, đăng nhập thật hoặc SQLite tích hợp. Bài SQL/SQLite dùng cùng dữ liệu là bài CSDL riêng. Demo Web hiện **đúng**: nếu chưa có dữ liệu lưu, nó bắt đầu bằng ba khoản, tổng **60000**. Đừng chẩn đoán một lỗi do cẩm nang cố ý dựng trong mảng lab thành lỗi của demo.

### Bẫy: đúng một kết quả rồi kết luận đúng tất cả

**Bổ sung biên tập — phiếu trả lời AI HƯ CẤU, cố ý sai:**

> “Đã đổi cận vòng lặp và thấy 60000, vậy chương trình xử lý mọi đầu vào an toàn. Ở Web cứ dùng `Number` cho mọi giá trị là đủ. Muốn tổng theo nhóm thì lọc trước, dữ liệu nhóm khác không liên quan.”

Chưa cần viết lại hàm. Gạch chân ba kết luận, rồi với mỗi kết luận nêu một đầu vào cần thử. Nếu chỉ trả lời “AI có thể sai”, bạn mới nhắc lại khẩu hiệu, chưa có phản biện kỹ thuật.

### Đáp án AI TRAP — Ba kết luận vượt quá bằng chứng

Đổi cận chỉ sửa việc bỏ cuối; `{0}` hoặc 501 khoản vẫn cần validation riêng. `Number("")` cho 0, chuyển được nhưng không hợp lệ. Lọc trước có thể che khoản sai: tiền chuỗi ở `di-lai` phải khiến yêu cầu tổng `hoc-tap` bị từ chối. Hãy tách yêu cầu, tìm phản ví dụ và xác định phạm vi test thay vì tranh luận về giọng văn AI.

### Sáu tình huống: ranh giới nằm ở nhiệm vụ đang luyện

“Tận dụng” giữ phần học cần thiết ở phía bạn; “giao việc học cho AI” để AI nghĩ thay phần đang cần luyện. Không chỉ nhìn code do AI gợi ý rồi kết luận về tính liêm chính.

| Tình huống | Tận dụng để học | Dấu hiệu giao việc học cho AI | Vùng xám phải kiểm tra |
| --- | --- | --- | --- |
| 1. Minh gặp lỗi biên dịch | Gửi lỗi và đoạn tối thiểu, tự giải thích nguyên nhân sau gợi ý. | Dán cả bài, thay bằng lời giải không đọc. | Bản vá rất nhỏ vẫn có thể bị cấm trong bài đánh giá không cho AI. |
| 2. Minh học vòng lặp | Xin câu hỏi về chỉ số, tự trace ba khoản. | Xin vòng lặp hoàn chỉnh rồi học thuộc. | Được xem mẫu không đồng nghĩa được nộp thuật toán do AI xây. |
| 3. Lan đọc tiếng Anh | Giải nghĩa thuật ngữ, đối chiếu câu gốc. | Chỉ đọc tóm tắt rồi nhận đã đọc tài liệu. | Dịch hỗ trợ khác với viết hộ phần phân tích được chấm. |
| 4. Lan thiết kế test | Tự tính kỳ vọng, nhờ tìm loại ca còn thiếu. | Nhận cả hàm lẫn kỳ vọng test từ một câu trả lời. | Môn có thể cho sinh test nhưng yêu cầu khai báo. |
| 5. Hai bạn làm giao diện | Sinh khung không phải trọng tâm rồi tự nối dữ liệu. | Không biết nút Lưu gọi gì nhưng nhận đã làm chủ Web. | Nếu đang học HTML, khung sinh sẵn có thể bỏ qua mục tiêu chính. |
| 6. Chuẩn bị bài nhóm | Thống nhất hỗ trợ, mỗi người giải thích phần mình. | AI hoàn thành phần chưa làm nhưng báo tự làm hoàn toàn. | Quy tắc nhóm, ghi nhận hỗ trợ và cách đánh giá có thể khác nhau. |

Trước khi mở chat, viết: “Bài đang luyện __; AI chỉ hỗ trợ __; tôi tự chứng minh __.” Minh chọn điều kiện dừng, Lan chọn đường đi của kiểu dữ liệu. Nếu quyền sử dụng chưa rõ, đọc hướng dẫn học phần và hỏi giảng viên trước khi dùng cho bài nộp. Khai báo không tự biến một cách dùng bị cấm thành được phép.

### Vibe coding có kiểm soát: dựng nhanh, nhận chậm

Ở đây, **vibe coding** là mô tả mong muốn bằng ngôn ngữ tự nhiên, nhận code và điều chỉnh qua nhiều lượt. Dựng nhanh có ích để thử ý tưởng; chạy được không tự chứng minh người làm hiểu chương trình.

Lan có thể nhận hàng trăm dòng rồi liên tục nhắn “sửa hết”. Cách có kiểm soát ngược lại: biết `index.html` chứa giao diện, `data.js` xử lý dữ liệu, `app.js` nối sự kiện và lưu trữ; chọn một vấn đề, dự đoán, nhận một thay đổi, kiểm vài ca rồi mới đi tiếp. Không thêm framework, dịch vụ hay đăng nhập để giải quyết lỗi chuỗi tiền.

Hiểu không phải thuộc mọi API. Bạn được tra tên phương thức nhưng phải trả lời bốn câu:

1. Đoạn code nhận dữ liệu gì, kiểu nào, từ đâu?
2. Nó trả về hoặc thay đổi điều gì?
3. Nó dựa vào điều kiện nào của hợp đồng?
4. Nếu bỏ một điều kiện, tôi tạo được ca nào khiến nó sai?

Với `localStorage.setItem`, Lan cần biết nó lưu chuỗi, có thể thất bại, và không được báo lưu bền khi chỉ cập nhật bộ nhớ. Với `vector`, Minh cần biết ba phần tử có chỉ số 0, 1, 2. Quên tên API thì tra; không biết vì sao thiếu phần tử cuối thì trace.

![Bẫy AI: từ câu trả lời tự tin, quay về dự đoán, phản ví dụ và bằng chứng do người học kiểm tra.](../assets/ai-trap.svg)

## 3.2. THINK FIRST / PREDICT BEFORE ASKING — Viết dự đoán trước câu hỏi

### Một phiếu ngắn trước khi nhấn Gửi

Chưa có lời giải vẫn được hỏi. Viết “cộng từ khoản đầu đến khoản cuối” rồi thử một khoản để tạo chỗ bám cho gợi ý.

| Điều cần ghi | Minh điền trước khi hỏi | Nếu chưa biết |
| --- | --- | --- |
| Đầu vào | `35000, 7000, 18000`, số nguyên | Chép đúng dữ liệu và kiểu đang có. |
| Kỳ vọng | 60000, do cộng đủ ba khoản | Tính tay ca một khoản trước. |
| Hiện tượng | Dự đoán cận lỗi cho 42000; chưa chạy | Ghi “chưa chạy”, không mượn log của sách. |
| Giả thuyết | Có thể chưa cộng Vở ghi | Ghi nơi nghi ngờ, chưa khẳng định nguyên nhân. |
| Điều xin hỗ trợ | Một câu hỏi về chỉ số | Không xin đồng thời giải thích, sửa cả bài và sinh test. |

Chương 2 đã giải cận và build; lần này luyện **giữ từng bước suy nghĩ**. Nếu nhớ lời giải, hãy tự giải thích ca mới.

### Hội thoại C++: người học phải đi qua lượt dừng

Đây là **mã lỗi chủ đích** từ `loi-bo-sot.cpp`. `amounts` là `std::vector<long long>{35000, 7000, 18000}`, `total` là `long long` khởi tạo 0.

```cpp
int n = static_cast<int>(amounts.size());
for (int i = 0; i < n - 1; ++i) { // CỐ Ý SAI
    total += amounts[i];
}
```

Trước khi mở đối chiếu, tự ghi `n`, các chỉ số hợp lệ và từng lần kiểm tra điều kiện, kể cả lần sai khiến vòng lặp dừng. `size()` là số lượng, không phải chỉ số cuối. Với ba khoản mẫu, `int n` không có rủi ro. `loi-bo-sot.cpp` **chưa** kiểm giới hạn 500; bản có kiểm số lượng trước khi ép sang `int` nằm ở mục 3.6. Không suy ra mọi phép ép kích thước về `int` đều an toàn.

### Đáp án hội thoại C++ — HƯ CẤU, không phải log thực thi

**Minh:** Em tính tay 60000. Với cận đang đọc, em dự đoán 42000. Em nghi thiếu Vở ghi nhưng chưa biết phải sửa thế nào.

**Người hướng dẫn:** Chưa sửa. Ba phần tử có chỉ số nào?

**Minh:** 1, 2, 3… Em nhầm: vector bắt đầu ở 0, vậy là 0, 1, 2.

**Người hướng dẫn:** Khi ấy `n` và điều kiện lượt đầu bằng gì?

**Minh:** `n = 3`, nên `n - 1 = 2`. Lượt đầu `0 < 2` đúng, tổng thành 35000.

**Người hướng dẫn:** Em tự đi tiếp, cả lượt không được chạy.

**Minh:** `i = 1`, `1 < 2` đúng, tổng thành 42000. Đến `i = 2`, `2 < 2` sai. Chưa đọc 18000 mà đã dừng. Phép cộng không sai; thiếu một số hạng.

| Lần kiểm tra | i | Điều kiện lỗi | Khoản được cộng | total sau kiểm tra |
| --- | ---: | --- | --- | ---: |
| 1 | 0 | `0 < 2`: đúng | Cơm trưa 35000 | 35000 |
| 2 | 1 | `1 < 2`: đúng | Xe buýt 7000 | 42000 |
| 3 | 2 | `2 < 2`: sai | Không có | 42000 |

**Người hướng dẫn:** Em muốn đọc chỉ số nào và không được đọc chỉ số nào?

**Minh:** Đọc 0, 1, 2; không đọc 3. Em đề xuất `i < n`. Khi `i = 2`, cộng thêm 18000 thành 60000; tăng lên 3 thì dừng.

**Người hướng dẫn:** Một khoản Vở ghi và danh sách rỗng có giúp kiểm đề xuất không?

**Minh:** Một khoản: cũ kiểm `0 < 0`, bỏ luôn khoản duy nhất; mới kiểm `0 < 1`, cộng 18000. Rỗng: mới kiểm `0 < 0`, tổng giữ 0. Cũ với `int n = 0` cũng không lặp, nên riêng ca rỗng không phân biệt được hai cận.

| Đầu vào | Kỳ vọng cận lỗi | Kỳ vọng cận đúng |
| --- | ---: | ---: |
| Ba khoản mẫu | 42000 | 60000 |
| Chỉ 18000 | 0 | 18000 |
| Rỗng | 0 | 0 |

Đây là **trace thủ công và đầu ra kỳ vọng**, không phải bằng chứng đã biên dịch. Sửa cận không tự thêm kiểm tra tiền hoặc số lượng. Cũng không thay bằng `size() - 1` cho “gọn”: kích thước thuộc kiểu không dấu, trừ 1 khi rỗng có thể tạo giá trị rất lớn; xem giải thích ở mục 2.3.

Nếu dùng AI làm người hỏi, yêu cầu chờ câu trả lời, không để nó tự nhận là giảng viên của bạn. Giá trị của hội thoại nằm ở câu Minh tự nói về chỉ số 2, không phải số lượt trao đổi.

### Phiên 25 phút CÓ AI hỗ trợ: sáu bước, sáu dấu vết

Đây là phiên học **có giai đoạn được hỏi AI**, khác hoàn toàn thử thách không AI ở mục 3.5. Chọn một mục tiêu: Minh sửa cận; Lan giải thích tiền chuỗi trong lab. Chỉ dùng phương tiện đã được phép; nếu không truy cập AI, thay lượt hỏi bằng phiếu gợi ý hoặc bạn học và ghi rõ cách làm.

| Thời gian | Việc phải làm | Dấu vết cần giữ |
| --- | --- | --- |
| 0–4 phút: tự thử | Đọc đề, phác một cách, dù còn thiếu. | Code tự viết hoặc mô tả thuật toán. |
| 4–7 phút: dự đoán | Tính tay; ghi chỉ số hoặc kiểu từng chặng. | Kỳ vọng viết **trước** chạy và trước hỏi. |
| 7–11 phút: xin gợi ý | Một câu mỗi lượt, tự trả lời rồi mới hỏi tiếp. | Câu gợi ý và câu trả lời của bạn. |
| 11–16 phút: tự sửa | Chỉ sửa nguyên nhân đã giải thích được. | Dòng đổi cùng lý do. |
| 16–21 phút: kiểm chứng | Ca thường, biên và sai theo phạm vi việc sửa. | Kỳ vọng, thực tế, kết luận; ghi validation còn thiếu nếu có. |
| 21–25 phút: biến thể không AI | Đóng chat, đổi dữ liệu hoặc câu hỏi. | Bài tự làm và chỗ chưa chắc. |

Minh dự đoán `0 → 35000 → 42000 → 60000`; Lan vẽ “ô nhập → đối tượng → danh sách → tổng”. Chưa viết được code vẫn bắt đầu bằng hai dấu vết này. Khi mới sửa cận, test tiền sai chưa bị từ chối là phần validation còn thiếu.

Thử tối đa ba lượt gợi ý cho một nút thắt, theo quy ước phiên học. Mỗi lượt phải dẫn đến một hành động tự làm: điền trace, sửa dòng hoặc nghĩ test. Vẫn vướng thì thu xuống một khoản.

### Khi đáp án lộ, hoặc hết giờ mà chưa xong

Nếu AI viết luôn điều kiện đúng, ghi “đã xem lời giải phần cận”, đóng lại, tự giải thích rồi thử ca mới. Câu đã lộ chỉ tính là ôn tập. Thẻ P02 (bảng thẻ P01–P08 ở cuối mục 3.3 và trong [Thư viện prompt](prompt-library.md)) có thể xin bảng trống, nhưng không bảo đảm AI tuân thủ.

Nếu mệt, ghi cụ thể “đã biết chỉ số cuối, chưa biết lập điều kiện” rồi dừng. Thời lượng không chẩn đoán khả năng tập trung hay năng lực ngành học. Phiên sau thu nhỏ nhiệm vụ; khi hỏi người hướng dẫn, mang đầu vào, kỳ vọng, thực tế và điều đã thử.

## 3.3. REVERSE ENGINEERING / EXPLAIN IT BACK — Lần ngược rồi giải thích lại

Mục này cố ý ghép hai bước vì chúng đi liền nhau: phần đầu là **REVERSE ENGINEERING** (lần ngược luồng dữ liệu), phần “Giải thích lại” bên dưới là **EXPLAIN IT BACK**. Mục 3.7 cuối chương là **SKILL UNLOCKED**.

### Từ một con số trên màn hình về nơi dữ liệu được tạo

**Reverse engineering** ở đây là đọc ngược chương trình để hiểu luồng. **Explain it back** là giải thích bằng lời của bạn, kèm vị trí code và ví dụ.

Trong `bai-lam/nam-2-web`, Lan lần từ tổng hiển thị về `render()`, `D.totalExpenses(expenses)`, chỗ gán `expenses`, handler `submit` vô danh và `D.parseAmount` trong `app.js`. Sau đó mở `data.js` đọc hàm, `index.html` kiểm form và thứ tự script. Không bịa `handleSubmit` khi mã dùng callback vô danh.

| Chặng cần lần | Vị trí/vai trò | Kiểu và điều phải giải thích |
| --- | --- | --- |
| Ô nhập | `index.html`, đọc trong `app.js` | `.value` là chuỗi, dù người dùng gõ chữ số. |
| Phân tích tiền | `parseAmount` trong `data.js` | Kiểm cách viết, chuyển thành số, kiểm miền tiền. |
| Danh sách ứng viên | Handler `submit` trong `app.js` | Ghép khoản mới; `normalizeExpenses` kiểm cả danh sách trước khi gán. |
| Tính tổng | `totalExpenses` trong `data.js` | Kiểm tiền/số lượng, trả số; không xác thực toàn schema. |
| Lưu | `save()` trong `app.js` | `JSON.stringify` tạo chuỗi để ghi vào `localStorage`; ghi có thể lỗi. |
| Hiển thị | `render()` trong `app.js` | Định dạng để nhìn, không biến tiền lưu thành chuỗi có dấu chấm. |
| Đọc lại | Khối khởi tạo trong `app.js` | `JSON.parse` rồi `normalizeExpenses`; JSON hợp lệ chưa chắc đúng schema. |

Trong handler, vế phải `D.normalizeExpenses([...expenses, khoản_mới])` phải thành công trước khi gán lại `expenses`. Dữ liệu sai bị ném lỗi và bắt ở giao diện, nên không được thêm vào danh sách. Dữ liệu hợp lệ được cập nhật trong bộ nhớ, sau đó mới gọi `save()` và `render()`: lưu thất bại không hoàn tác khoản vừa thêm trong RAM, nhưng phải báo không lưu bền.

### Lab kiểu dữ liệu: không làm hỏng demo đúng

Giữ nguyên `data.js` đang đúng. Trên giấy hoặc vùng nháp, giả lập ba `amount` là chuỗi `"35000"`, `"7000"`, `"18000"`, biến `total` ban đầu là số 0. Mỗi lượt thực hiện `total = total + expense.amount`. Đây là **lab lỗi chủ đích**, không phải mô tả trạng thái dữ liệu mẫu của ứng dụng.

Chưa mở đáp án: lập bảng lượt, `total` trước và kiểu, `amount` và kiểu, `total` sau và kiểu. Giữ dấu ngoặc kép; bỏ chúng làm mất phần quan trọng nhất của bài.

### Đáp án hội thoại Web — HƯ CẤU, giải thích bằng giá trị và kiểu

**Lan:** Trong lab, em dự đoán kết quả là chuỗi dài chứ không phải tiền. Em định thay toán tử cộng.

**Người hướng dẫn:** Trước khi đổi toán tử, em biết kiểu của `.value` chưa?

**Lan:** Em từng nghĩ gõ số thì nhận số. Nhưng giá trị của ô nhập là chuỗi. Em phải kiểm `typeof` nếu muốn quan sát trên Console, không đoán bằng hình dáng.

**Người hướng dẫn:** Vậy lượt đầu, bên trái và bên phải là gì?

**Lan:** Số 0 cộng chuỗi `"35000"` thành chuỗi `"035000"`. Tổng đã đổi kiểu ngay lượt đầu.

**Người hướng dẫn:** Em làm hai lượt tiếp và ghi cả kiểu.

| Lượt | total trước và kiểu | amount và kiểu | total sau và kiểu |
| --- | --- | --- | --- |
| 1 | `0`, number | `"35000"`, string | `"035000"`, string |
| 2 | `"035000"`, string | `"7000"`, string | `"0350007000"`, string |
| 3 | `"0350007000"`, string | `"18000"`, string | `"035000700018000"`, string |

**Lan:** Sau lượt đầu không còn cộng số. Em đang nối ký tự liên tiếp.

**Người hướng dẫn:** Nên sửa ở đâu để phía sau không phải đoán kiểu?

**Lan:** Ở biên nhập liệu: kiểm chuỗi, chuyển số, kiểm giá trị rồi mới tạo `Expense`. Hàm tổng vẫn phải từ chối tiền sai vì dữ liệu có thể đến từ đường khác.

**Người hướng dẫn:** Chỉ dùng `Number` đủ không? Xét chuỗi rỗng và số âm.

**Lan:** Không. `Number("")` cho 0; `Number("-7000")` cho số âm. Cả hai không là khoản hợp lệ. Em cho phép khoảng trắng ngoài cùng, rồi chỉ nhận chữ số; từ chối chấm, phẩy, chữ và ký hiệu mũ.

**Người hướng dẫn:** Khi tải lại trang, dữ liệu đã lưu có cần kiểm nữa?

**Lan:** Có. `localStorage` giữ chuỗi JSON. Parse được chỉ chứng minh cú pháp JSON; vẫn phải kiểm danh sách, tiền, id, title, category. Lỗi đọc không được âm thầm đổi dữ liệu cũ thành danh sách rỗng rồi ghi đè.

Các kết quả trên là **kỳ vọng từ trace**. Khi tiền đã là số, trace đúng là `0 → 35000 → 42000 → 60000`. `42000` ở giữa là tổng trung gian đúng; `42000` cuối vòng lặp C++ lỗi là kết quả sai. Cùng con số, khác thời điểm và yêu cầu.

### EXPLAIN IT BACK — Giải thích lại: vượt qua câu “em hiểu rồi”

Đóng phần hội thoại. Trong khoảng một phút, kể đường đi của `"18000"` từ ô nhập đến số trong danh sách rồi chuỗi JSON. Chỉ vào tên hàm khi nói. Nếu kẹt, đánh dấu chặng bị thiếu trước khi mở lại tài liệu. **Tự kiểm:** mở lại bảng “Chặng cần lần” ở đầu mục này và đánh dấu từng chặng bạn đã nói được; thiếu chặng nào thì đó là việc ôn tiếp theo. Minh chỉ tham gia phần này như **review chéo với Lan**, không ngầm chuyển sang làm dự án Web năm hai.

Dùng thêm câu tiếng Anh **do cẩm nang tự soạn, không phải trích dẫn chính thức**: “The value of a text input is a string. Convert and validate it before storing an expense amount.” Giải nghĩa `value` là giá trị, `string` là chuỗi, `convert` là chuyển kiểu, `validate` là kiểm tra hợp lệ. Sau đó tự diễn giải cả câu và chọn một trường hợp chuyển được nhưng không hợp lệ. Với tài liệu thật, phải giữ đoạn gốc và nguồn để đối chiếu; bản dịch không thay việc đọc điều kiện áp dụng.

Về lưu trữ, bản demo khởi tạo mẫu trước. Không có bản lưu thì giữ ba khoản 60000; có bản lưu hợp lệ thì dùng bản đó, kể cả `[]` với tổng 0. Nếu đọc/parse/normalize thất bại, `persistent = false`, dùng mẫu trong bộ nhớ và thông báo không ghi đè dữ liệu cũ. Nếu ghi thất bại, `save()` cũng chuyển sang bộ nhớ tạm, các thay đổi sau trong phiên không thử ghi tiếp. Nút khôi phục mẫu không tự bật lại quyền lưu.

`file://` có hành vi lưu trữ phụ thuộc trình duyệt. Kiểm reload ở cùng file và cùng trình duyệt; nếu dùng HTTP có sẵn, cần cùng origin, tức cùng giao thức, host và cổng. Khác địa chỉ có thể là vùng lưu khác. Không dựng server hoặc backend chỉ để hoàn thành bài đọc này.

### Tám chức năng prompt gốc: chọn đúng một điểm nghẽn

Tám chức năng dưới đây kế thừa mục 3.4 bản nguồn; thẻ đầy đủ, có ngữ cảnh và cách xử lý lộ đáp án, nằm trong [Thư viện prompt](prompt-library.md). Chương giữ cách chọn và bằng chứng học, không bắt bạn chép lại tám khối dài.

| Thẻ | Chức năng và khi dùng | Bạn phải chuẩn bị/làm | Nếu đáp án lộ |
| --- | --- | --- | --- |
| [P01](prompt-library.md) | Socratic, một câu mỗi lượt; chưa biết vì sao bỏ khoản cuối. | Tự nêu chỉ số, trace, giải thích dòng sửa. | Ghi đã xem; đóng lại và trace ca một khoản mới. |
| [P02](prompt-library.md) | Ba tầng gợi ý: vùng cần xem → quan hệ chỉ số/kích thước → bảng trống. | Sau mỗi tầng báo điều vừa thử, không xin cả ba cùng lúc. | Tự so ca rỗng **và** một khoản; rỗng riêng lẻ chưa phân biệt cận. |
| [P03](prompt-library.md) | Trace giá trị và kiểu ở lab tiền chuỗi. | Điền từng hàng, chỉ lượt đầu đổi kiểu. | Che bảng, tự trace một chuỗi khác. |
| [P04](prompt-library.md) | Review đúng một thay đổi nhỏ. | Chứng minh cận, chọn test, nói validation nào chưa làm. | Không thay cả file; tự so hai cận với `n = 1`. |
| [P05](prompt-library.md) | Test trước code. | Tự đề xuất ca thường, biên, sai và tính kỳ vọng. | Đóng lời giải, tính ca 500 khoản tối đa. |
| [P06](prompt-library.md) | Giải thích tiếng Anh có đối chiếu. | Diễn giải câu gốc, phân biệt chuyển kiểu/kiểm hợp lệ. | Tự phân tích `"35000abc"` bằng lời. |
| [P07](prompt-library.md) | Vấn đáp như người hướng dẫn. | Trả lời bằng ví dụ về chỉ số, kiểu, test, lưu trữ. | Bỏ câu đã lộ khỏi đánh giá độc lập, chuyển câu mới. |
| [P08](prompt-library.md) | Giao biến thể rồi đóng chat. | Tự làm max C++ hoặc tổng nhóm Web; nêu chỗ chưa chứng minh. | Chuyển sang bài đảo thứ tự, chưa xem kết quả. |

Một thẻ không làm thay nhiệm vụ chuẩn bị. P05 không hữu ích nếu bạn để AI tính luôn mọi kỳ vọng; P07 không phải công cụ đoán điểm học phần. Bốn phút tự thử trong P08 chỉ là lượt ngắn, không thay thử thách 25 phút ở mục 3.5.

## 3.4. MEMORY EXPERIMENT — Tự quan sát điều còn nhớ, không kết luận nhân quả

### Hai nhiệm vụ gần tương đương, một mục tiêu quan sát

**Bổ sung biên tập.** Hoạt động tự quan sát nhớ lại, không nghiên cứu tác động AI lên trí nhớ. Hai nhiệm vụ cùng số khoản, phép cộng, giới hạn chỉ số; chưa có phép đo chứng minh độ khó tương đương.

Chuẩn bị giấy, đồng hồ, 12–15 phút; không cần AI. Dùng cận đúng đã học, đổi thứ tự dữ liệu:

- **A:** `35000, 7000, 18000`. Đọc câu trả lời của Minh về cận `i < n` và bảng “Đầu vào / Kỳ vọng cận đúng” ở mục 3.2 (tổng `0 → 35000 → 42000 → 60000`) trong khoảng 90 giây, rồi gấp phần đó lại. Ghi rõ A đã được đọc lời giải.
- **B:** `18000, 35000, 7000`. Trong khoảng 90 giây, tự viết bảng chỉ số/tổng mà không mở lời giải. Không chạy trước để lấy kết quả.

Tung đồng xu hoặc chọn thứ tự B trước A nếu thuận tiện; ghi thứ tự thật. Không coi việc đổi thứ tự đã loại bỏ ảnh hưởng luyện tập. Nếu chưa hiểu vòng lặp, làm cả hai với trợ giúp và ghi đúng mức hỗ trợ; lúc này chỉ quan sát nhớ lại, không so “có AI” với “không AI”.

### Quy trình: tách lúc học khỏi lúc nhớ lại

Sau từng nhiệm vụ, che code và ghi chép, nghỉ khoảng hai phút bằng một việc không liên quan đến bài. Sau đó trả lời cùng bốn câu trên giấy trắng: chỉ số hợp lệ là gì; tổng sau mỗi lượt là gì; điều kiện nào làm dừng; với một khoản và rỗng sẽ ra sao, vì sao? Không mở kết quả trong khi trả lời. Cuối cùng mới đối chiếu và đánh dấu phần cần nhìn lại.

Nếu máy hoặc hoàn cảnh không cho nghỉ đúng thời lượng, ghi thời gian thực tế. Ngày hôm sau có thể trả lời lại bốn câu trước khi đọc chương; đây là lượt tự kiểm bổ sung, không bắt buộc để “đạt”. Không chép câu vừa đọc rồi gọi đó là nhớ lại độc lập.

| Nhiệm vụ | Thứ tự/thời gian thật | Hỗ trợ đã xem | Tự nhớ được ý nào | Ý sai hoặc cần mở lại | Giải thích được ca mới? |
| --- | --- | --- | --- | --- | --- |
| A | … | Bảng đã có lời giải | … | … | … |
| B | … | Tự lập bảng; ghi thêm nếu có | … | … | … |
| Lượt hôm sau, nếu làm | … | Chưa xem lại/đã xem lại | … | … | … |

### Đáp án đối chiếu MEMORY EXPERIMENT

A có tổng lần lượt 35000, 42000, 60000; B có 18000, 53000, 60000. Cả hai đọc chỉ số 0, 1, 2 và dừng trước 3 với cận `i < n`. Một khoản hợp lệ có tổng bằng chính khoản ấy; rỗng giữ 0. Dãy tổng trung gian khác nhau nhưng tổng cuối không đổi.

Đối chiếu từng ý: nhớ 60000 chưa chứng minh nhớ quá trình cộng; nhớ tên `long long` chưa chứng minh hiểu giới hạn tổng.

### Viết kết luận đúng mức bằng chứng

Nhận xét **HƯ CẤU** phù hợp: “A tôi nhớ tổng cuối nhưng quên lượt dừng; B tôi tự viết được ba tổng trung gian. Tôi sẽ luyện điều kiện dừng khi đóng tài liệu.” Không suy “AI làm tôi nhớ kém”.

Kiến thức sẵn có, thứ tự, độ quen, mệt mỏi, thời gian, việc nhìn đáp án và cách tự chấm đều có thể ảnh hưởng. Không kiểm soát chúng và thiếu nhóm so sánh, bạn không suy nhân quả, tạo phần trăm hay gắn nhãn trí nhớ tốt/xấu. Chỉ chọn **hành động học tiếp**: nhớ lại, giải thích thành lời hoặc đổi dữ liệu.

## 3.5. 25-MINUTE NO-AI CHALLENGE — Tự làm trọn một nhiệm vụ nhỏ

### Luật phiên này: không AI từ đầu đến cuối

**Bổ sung biên tập.** Đây là 25 phút độc lập, không phải 21 phút có AI rồi bốn phút đóng chat. Đóng hội thoại, không dùng Agent, sinh code, giải thích AI hoặc gợi ý AI trong cả phiên. Dùng vùng soạn thảo không hiện gợi ý AI đang có sẵn hoặc làm trên giấy; không đổi cấu hình công cụ để thi hành bài. Được đọc đề, hợp đồng, ghi chú cú pháp tự viết; không mở đáp án dưới đây hay nhờ người khác làm hộ.

Nếu vô tình nhìn thấy gợi ý, ghi thời điểm và phần đã thấy; tiếp tục luyện nhưng không gọi cả phiên là độc lập. Điều cần bảo vệ là chất lượng bằng chứng, không phải một dấu tích đẹp.

**Nhiệm vụ chung:** đếm số khoản có tiền **từ 10000 VND trở lên**. Danh sách đầu vào của riêng bài đếm này **đã được xác nhận hợp lệ** theo hợp đồng. Bạn chưa phải viết parser hoặc validation mới; hãy ghi rõ tiền đề đó trong lời giải.

- Minh viết `countLargeAmounts(const std::vector<long long>& amounts)`, trả số lượng bằng `int`.
- Lan viết `countLargeExpenses(expenses)`, dùng `expense.amount` là số, trả số lượng bằng `number`. Không đọc DOM hoặc `localStorage` trong hàm.

Chọn một nhánh. Không đổi nhiệm vụ thành tính tổng hoặc tìm số tiền lớn nhất. Chuẩn bị ca ba khoản mẫu, rỗng, một khoản 10000, một khoản 9999, và đảo thứ tự ba khoản. Với Web, các đối tượng đầy đủ và id không trùng; với C++, chỉ cần vector tiền.

### Chia thời gian để còn chỗ kiểm chứng

| Khoảng phút | Việc tự làm | Sản phẩm nhỏ |
| --- | --- | --- |
| 0–5 | Diễn giải “từ 10000 trở lên”; tính kỳ vọng các ca. | Bảng trước chạy, có cả biên bằng 10000. |
| 5–12 | Viết thuật toán bằng lời rồi code hoặc giả mã. | Một biến đếm, cách duyệt, điều kiện xét khoản. |
| 12–18 | Trace từng khoản; nếu có môi trường sẵn thì chạy bản nháp. | Kết quả thực hoặc nhãn trace, không trộn hai loại. |
| 18–22 | Tự tìm và sửa một điểm sai/thiếu; nếu đã đúng, giải thích vì sao. | Dòng đổi và lý do hoặc lập luận bảo vệ code. |
| 22–25 | Đóng cả code, nói lại cách làm và ghi điểm nghẽn. | Giải thích ngắn, trạng thái cuối phiên. |

Không cần thêm tệp: viết trong vở hoặc vùng nháp của ghi chép hiện có. Nếu thử C++ trong bản sao, giữ lại mã trước thay đổi để đối chiếu, không ghi đè bản tham khảo. Không có compiler/runtime thì hoàn thành giả mã và trace, đánh dấu phần thực thi chưa làm.

### Đối chiếu theo bằng chứng, không theo tốc độ

Ghi có/chưa có cho bốn điểm: phân biệt đếm/cộng tiền; kỳ vọng độc lập; trace hoặc lần chạy được mô tả đúng; giải thích biên 10000 và rỗng. Giữ bản tự làm trước khi mở đáp án. Chưa xong thì ghi điểm nghẽn cụ thể, chẳng hạn “em tăng tiền thay vì tăng số lượng”, để chọn việc phiên sau.

### Đáp án thử thách không AI — Đếm, không cộng tiền

Kỳ vọng: ba khoản mẫu có **2** khoản đạt; rỗng **0**; `[10000]` cho **1**; `[9999]` cho **0**; đảo thứ tự vẫn **2**. Lượt cộng tiền 18000 không có nghĩa tăng biến đếm thêm 18000; mỗi khoản thỏa điều kiện chỉ tăng 1.

Các lõi sau là lời giải đọc sau phiên, giả định đầu vào đã hợp lệ; không thay thế validation ở mục 3.6.

```cpp
int countLargeAmounts(const std::vector<long long>& amounts) {
    int count = 0;
    for (long long amount : amounts) {
        if (amount >= 10000) ++count;
    }
    return count;
}
```

```javascript
function countLargeExpenses(expenses) {
  let count = 0;
  for (const expense of expenses) {
    if (expense.amount >= 10000) count += 1;
  }
  return count;
}
```

Mỗi hàm duyệt một lần, thời gian O(n), bộ nhớ phụ O(1), không thay đổi đầu vào. Biến đếm C++ tối đa 500 nên `int` phù hợp; điều này không mâu thuẫn với việc **tổng tiền** phải dùng `long long`. Sau khi xem đáp án, sửa lại bản nháp là ôn tập có đối chiếu, không sửa lịch sử thành “tự làm đúng ngay”.

## 3.6. AI CHALLENGE — Sửa ít, xác thực đủ, thử biến thể

*Mục vận dụng: ghép các bước 3.1–3.5 vào một bài sửa thật trước khi điểm lại năng lực ở 3.7.*

### Chuẩn bị: một nhánh, một bản sao, ba loại bằng chứng

Chọn Minh hoặc Lan, nộp code/nháp, bảng kỳ vọng–thực tế và giải thích. P04/P05/P08 là hỗ trợ tùy chọn. Mở NEW, dùng bản sao `bai-lam`: C++ sửa `loi-bo-sot.cpp`, giữ `vi_sinh_vien.cpp` đối chiếu; Web giữ bốn tệp cùng thư mục, **tái dựng lõi ở lab riêng**, không chữa demo đúng.

Trace là lập luận; test logic kiểm hàm; thao tác trình duyệt kiểm sự kiện, hiển thị, lưu trữ. Không dùng một loại để nhận đã hoàn tất cả ba.

### Nhánh Minh: từ bản vá cận đến hợp đồng đầy đủ

**Bước 1 — Vá đúng một nguyên nhân.** Trong bản sao `loi-bo-sot.cpp`, dự đoán ba khoản, một khoản 18000, rỗng trước sửa. Trace rồi đổi cận. Giữ ghi nhận: đây là bản vá duyệt trên đầu vào hợp lệ, chưa bổ sung validation.

**Bước 2 — Bổ sung validation thành việc riêng.** Tách hàm `totalExpenses` phía trên `main`, vẫn dùng `vector<long long>`. Kiểm số lượng trước khi chuyển `size()` sang `int`; kiểm từng tiền trước khi cộng. Danh sách sai phải ném `std::invalid_argument`, không bỏ qua khoản sai hoặc trả 0. Thêm `<stdexcept>` cho ngoại lệ, giữ `<vector>` và `<iostream>`. **Nếu bước này quá lớn:** làm hai lượt nhỏ — lượt 1 chỉ thêm kiểm số lượng (quá 500 thì ném lỗi), build và thử; lượt 2 mới thêm kiểm từng tiền. Bản hoàn chỉnh để đối chiếu nằm ở mục “Đáp án” cuối 3.6; chỉ mở sau khi đã tự thử.

**Bước 3 — Gọi hàm và kiểm cả nhánh lỗi.** Trong `main`, gọi hàm với vector đang thử. Đặt lời gọi trong `try`, bắt `std::invalid_argument` để báo lỗi và trả mã khác 0. Trọng tâm là tiền đã ở kiểu `long long`; chưa yêu cầu hệ thống nhập bàn phím phát hiện mọi chuỗi sai. Khi mở rộng nhập sau này, phải kiểm cả việc đọc/chuyển đổi thành công trước khi đưa vào vector.

**Bước 4 — Chạy đúng bản vừa sửa.** `loi-bo-sot.cpp` không có `--test`. Thay vector dữ liệu trong bản sao để thử từng ca rồi build lại, hoặc tự viết bộ gọi test khi đã hiểu (xem hàm `runTests()` trong `vi_sinh_vien.cpp` làm mẫu); không gắn `--test` và tưởng chương trình sẽ tự kiểm. Dùng `std::vector<long long>(500, 1000000000LL)` để tạo ca cực đại, không gõ 500 số.

Từ **gốc NEW**, khi máy đã có `g++`, chọn đúng shell. Bash/Git Bash dùng nối `&&` để chỉ chạy khi build thành công:

```bash
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/loi-bo-sot.cpp" -o "bai-lam/nam-1-cpp/loi-bo-sot.exe" && "./bai-lam/nam-1-cpp/loi-bo-sot.exe"
```

PowerShell dùng kiểm mã build:

```powershell
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/loi-bo-sot.cpp" -o "bai-lam/nam-1-cpp/loi-bo-sot.exe"
if ($LASTEXITCODE -eq 0) { & ".\bai-lam\nam-1-cpp\loi-bo-sot.exe" }
```

Chạy dòng thứ hai ngay sau dòng build: `$LASTEXITCODE` chỉ phản ánh lệnh vừa chạy trước nó. Đọc output và mã thoát theo mục 2.7; nếu build lỗi thì dừng, không chạy executable cũ. Dùng IDE thì Build thành công rồi Run đúng đích. Thiếu compiler thì trace, ghi chưa thực thi, không tự cài trên máy chung.

### Nhánh Lan: tái dựng lõi, không chữa một demo đang đúng

**Bước 1 — Chọn trạng thái xuất phát rõ ràng.** Nếu chưa có dữ liệu lưu, demo mở với ba khoản 60000. Muốn luyện thêm Vở ghi từ tổng 42000, trên **bản sao với dữ liệu giả có thể thay**, xóa riêng Vở ghi bằng nút Xóa của dòng đó rồi thêm lại. Xóa có thể được lưu; không dùng thao tác này với dữ liệu cần giữ. Không xóa cả kho trình duyệt để đạt trạng thái bài.

Phương án không đụng lưu trữ: dùng mảng lab riêng gồm hai đối tượng Cơm trưa và Xe buýt. Mảng này có tổng 42000; thêm `{id: 3, title: 'Vở ghi', amount: 18000, category: 'hoc-tap'}` thì kỳ vọng 60000. Thêm Vở ghi vào đủ ba mẫu sẽ cho **78000**, không phải 60000. Nếu đang có dữ liệu cũ khác, tính theo dữ liệu thật đang hiển thị hoặc chuyển sang mảng lab; đừng giả định tổng ban đầu.

**Bước 2 — Test trước lõi.** Sau trim chỉ nhận chữ số, rồi kiểm số nguyên an toàn trong 1..1e9. Viết cách xử lý trước khi mở đáp án. Tách `parseAmount` khỏi `totalExpenses`; hàm tổng không chữa tiền chuỗi để che lỗi nguồn dữ liệu.

**Bước 3 — Hai tầng kiểm tra.** `{amount: 7000}` đủ cho riêng `totalExpenses`, vì hàm chỉ kiểm mảng, số lượng và tiền. Đối tượng ấy thiếu `id/title/category` nên không đủ cho `normalizeExpenses`. Normalize kiểm schema, trả danh sách mới, không chữa tiền chuỗi.

**Bước 4 — Đọc chỗ nối.** Tìm `D.parseAmount` rồi gán qua `D.normalizeExpenses` trong `app.js`, không thay handler đúng bằng lab. Nhập sai phải giữ danh sách, tổng và dữ liệu lưu. Nhập hợp lệ có thể thêm trong RAM khi ghi thất bại, nhưng phải báo bộ nhớ tạm.

**Bước 5 — Kiểm trình duyệt.** Mở `bai-lam/nam-2-web/index.html`, thêm lại Vở ghi từ hai khoản, thử đầu vào sai, đọc thông báo thêm/lưu rồi reload cùng địa chỉ. Nếu dùng RAM, không kỳ vọng thay đổi còn sau reload.

Bản đầy đủ bọc logic trong hàm tự gọi, công bố `globalThis.ViData`; `app.js` lấy bằng `const D = globalThis.ViData`. Trong Node, API gán `module.exports`, bộ test dùng `require('./data.js')`. HTML nạp **script thông thường** theo thứ tự:

```html
<script src="data.js"></script>
<script src="app.js"></script>
```

Không thêm `type="module"`, `import`, server hoặc thư viện. `test_data.cjs` là chương trình kiểm logic riêng, không gắn vào trang. Nếu đã có Node.js, chạy từ **gốc NEW**:

```bash
node "bai-lam/nam-2-web/test_data.cjs"
```

Lệnh này dùng được trong Bash hoặc PowerShell; cách đọc mã thoát tùy shell như Chương 2. **Bộ Web hiện có 34 ca** (đếm theo số dòng `PASS` và dòng tổng kết cuối), gồm bộ ca kế thừa và một ca hồi quy cho `category` dạng mảng. Kỳ vọng bản đúng là `34 passed, 0 failed`; đó chưa phải kết quả máy bạn. Bản C++ tham khảo `vi_sinh_vien.cpp` có **9 ca**, chạy bằng `--test` sau build; không lẫn bộ này với bản bài làm `loi-bo-sot.cpp` không có bộ test. Test tham khảo xanh cũng không chứng minh hàm lab tự viết đúng.

### Bảng kiểm thử: ghi kỳ vọng trước, thực tế sau

Bảng giữ các ca cốt lõi của nguồn, thêm ranh giới schema. Cột thực tế để người học điền; “chưa chạy” khác “đã chạy đạt”. Với ca sai, kỳ vọng là **từ chối**, không phải tổng 0. Trong hàm, từ chối là phát sinh lỗi; ở giao diện, bắt lỗi và không nhận thay đổi sai.

| Ca | Kỳ vọng | Vì sao cần | Thực tế/trạng thái |
| --- | --- | --- | --- |
| Ba khoản mẫu | 60000 | Cộng đủ ba số hạng. | … |
| Chỉ một khoản Vở ghi 18000 | 18000 | Phát hiện bỏ phần tử cuối. | … |
| Rỗng | 0 | Tổng của danh sách hợp lệ không có khoản. | … |
| Đảo thứ tự ba khoản | 60000 | Tổng không phụ thuộc thứ tự. | … |
| Một khoản 1; một khoản 1000000000 | Lần lượt: 1; 1000000000 | Hai biên đều được nhận. | … |
| 500 khoản, mỗi khoản 1000000000 | 500000000000 | Kiểm số lượng và kiểu tổng. | … |
| 501 khoản, tiền đều hợp lệ | Từ chối | Không chỉ kiểm từng tiền. | … |
| Có khoản 0, âm hoặc 1000000001 | Từ chối từng ca | Không bỏ qua khoản sai. | … |
| JS có `amount: "35000"` hoặc `1.5` | Từ chối | Không là tiền số nguyên hợp lệ. | … |
| Chuỗi nhập `" 35000 "` | Số 35000 | Cho phép khoảng trắng ngoài cùng. | … |
| Nhập `""`, `" "`, `"35.000"`, `"35000abc"` | Từ chối từng ca | Kiểm toàn chuỗi, không đọc một phần. | … |
| Nhập `"0"`, `"1000000001"`, `"1e3"` | Từ chối từng ca | Cách viết đúng chưa đủ; ký hiệu mũ không được nhận. | … |
| Schema có id trùng, 0 hoặc không an toàn | Từ chối từng ca | Danh tính khoản phải hợp lệ, duy nhất. | … |
| Title toàn khoảng trắng hoặc 81 đơn vị UTF-16 | Từ chối từng ca | Kiểm sau trim, giới hạn 80. | … |
| Title `" Vở ghi "` | Chuẩn hóa thành `"Vở ghi"` | Không làm biến đổi tiền. | … |
| Category `"khac"` / `['khac']` / `"toString"` | Nhận / từ chối / từ chối | Kiểm kiểu chuỗi và khóa riêng trong danh mục. | … |

Nếu tạo 500 đối tượng để thử **normalize**, dùng id riêng cho từng khoản; nhân bản cùng một id 500 lần sẽ kiểm lỗi trùng id chứ chưa kiểm được biên số lượng hợp lệ. Nếu chỉ thử **totalExpenses**, các đối tượng có tiền là đủ theo phạm vi hàm.

### Đáp án validation C++ — Lõi đầy đủ, không phải chỉ một dòng cận

Lõi sau kế thừa `vi-du/nam-1-cpp/vi_sinh_vien.cpp`. Đặt hàm trên `main` trong bản bài làm, không chép đè bản tham khảo có `runTests()` và nhánh `--test`.

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
```

`const ...&` nhận tham chiếu chỉ đọc, không sao chép vector. Khi rỗng, không vào thân vòng lặp, tổng giữ 0. Kiểm số lượng trước phép ép kích thước; kiểm tiền trước cộng; không có nhánh “gặp sai thì bỏ qua”. Thời gian O(n), bộ nhớ phụ O(1).

Mẫu `main` cho bản bài làm, có bắt lỗi, được bổ sung để thử các ca sai. Chỉ thay vector khi thử dữ liệu khác; các dòng tên khoản dưới đây mô tả riêng bộ mẫu, nên cần đổi/bỏ chúng nếu đổi dữ liệu, tránh nhãn in không khớp.

```cpp
int main() {
    const std::vector<long long> amounts = {35000, 7000, 18000};
    try {
        const long long total = totalExpenses(amounts);
        std::cout << "Com trua: 35000 VND\nXe buyt: 7000 VND\nVo ghi: 18000 VND\n";
        std::cout << "Tong chi tieu: " << total << " VND\n";
        return 0;
    } catch (const std::invalid_argument& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
```

**Đầu ra kỳ vọng** với bộ mẫu là ba dòng tiền và `Tong chi tieu: 60000 VND`; không phải log đã chạy. Khi thử ca sai, nhánh bắt lỗi trả 1, không in tổng hợp lệ bằng 0. Hàm này nhận tiền đã có kiểu số nguyên; nó không thể phát hiện một lỗi parser đã biến đầu vào sai thành số hợp lệ từ trước.

### Đáp án validation Web — Tách parse, tổng và schema trong lab

Lõi `validAmount`, `parseAmount`, `totalExpenses`, `normalizeExpenses` dưới đây kế thừa `vi-du/nam-2-web/data.js` của NEW, có kiểm **kiểu chuỗi category**. Vỏ `chapter3Lab` là **bổ sung biên tập** để thử độc lập; không thay `globalThis.ViData`, không truy cập DOM/lưu trữ và không chép đè `data.js`.

Nếu muốn thử, mở `bai-lam/nam-2-web/index.html`, nhấn F12 rồi chọn thẻ **Console** (cách mở ở mục 2.4, Chương 2). Lần đầu dán mã, Chrome/Edge có thể chặn và yêu cầu tự gõ một cụm cho phép dán; đọc kỹ cảnh báo, chỉ dán khối trong cẩm nang này, không dán mã lạ. Đọc rồi nhập khối lab một lần; `var chapter3Lab` cho phép tạo lại lab sau khi sửa. Có thể chỉ đọc/trace nếu chưa quen Console. Khối này tự đủ phần logic, không cần gói ngoài.

```javascript
var chapter3Lab = (function () {
  'use strict';
  const MAX_AMOUNT = 1000000000;
  const MAX_ITEMS = 500;
  const categories = Object.freeze({
    'an-uong': 'Ăn uống', 'di-lai': 'Đi lại',
    'hoc-tap': 'Học tập', 'khac': 'Khác'
  });

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
    if (!Array.isArray(expenses) || expenses.length > MAX_ITEMS) {
      throw new Error('Danh sách tối đa 500 khoản.');
    }
    let total = 0;
    for (const expense of expenses) {
      if (!expense || !validAmount(expense.amount)) {
        throw new Error('amount phải là số nguyên VND hợp lệ.');
      }
      total += expense.amount;
    }
    return total;
  }

  function normalizeExpenses(input) {
    if (!Array.isArray(input) || input.length > MAX_ITEMS) {
      throw new Error('Dữ liệu lưu không đúng định dạng.');
    }
    const ids = new Set();
    return input.map(item => {
      if (!item || !Number.isSafeInteger(item.id) || item.id < 1 || ids.has(item.id) ||
          typeof item.title !== 'string' || !item.title.trim() || item.title.trim().length > 80 ||
          typeof item.category !== 'string' || !Object.hasOwn(categories, item.category) ||
          !validAmount(item.amount)) {
        throw new Error('Một khoản lưu sẵn không hợp lệ.');
      }
      ids.add(item.id);
      return { id: item.id, title: item.title.trim(), amount: item.amount, category: item.category };
    });
  }

  return { parseAmount, totalExpenses, normalizeExpenses, categories };
})();
```

`/^[0-9]+$/` kiểm toàn chuỗi sau trim, không nhận dấu chấm, phẩy, chữ hoặc mũ. `parseInt("35000abc", 10)` có thể đọc được tiền tố 35000, nên chỉ thêm radix không sửa được lỗi nhận hậu tố. `Number.isInteger` kiểm số nguyên; ở đây dùng `Number.isSafeInteger` rồi giới hạn riêng miền tiền. `"0007"` hợp lệ và cho số 7; `"0"` chỉ đúng cách viết nhưng sai miền.

`Object.hasOwn` kiểm khóa riêng, nhưng không thay kiểm kiểu: `['khac']` có thể bị ép thành tên khóa `"khac"`. Vì vậy phải giữ `typeof item.category !== 'string'`. `Set` lưu id đã gặp để phát hiện trùng. Normalize trả đối tượng mới với title đã trim, không sửa đối tượng đầu vào. Nó dùng thêm O(n) bộ nhớ cho danh sách mới và tập id; không gọi mọi phần của quá trình này là O(1).

Ví dụ thử sau khi mở bản Web và tạo lab; các chú thích là **kỳ vọng**, không phải thông báo kiểm thử đã chạy:

```javascript
chapter3Lab.totalExpenses(globalThis.ViData.sampleExpenses()); // kỳ vọng 60000
chapter3Lab.parseAmount(' 35000 ');                            // kỳ vọng số 35000
chapter3Lab.totalExpenses([]);                                // kỳ vọng 0
```

Thử từng ca sai riêng và chờ lỗi: `chapter3Lab.parseAmount('35000abc')`, hoặc `chapter3Lab.totalExpenses([{amount: '35000'}])`. Lỗi mong đợi không phải “Console hỏng”; đó là hàm đang từ chối dữ liệu. Để kiểm không thay đổi đầu vào, chụp giá trị JSON trước/sau lời gọi rồi đối chiếu, không chỉ nhìn tổng.

### Biến thể: đóng chat trước khi mở lời giải

**Minh:** viết `maxExpense` nhận cùng vector tiền, rỗng trả 0, vẫn từ chối mọi tiền sai và quá 500 khoản. Tự dự đoán ba khoản, một khoản và rỗng. Đừng chỉ đổi tên hàm tổng; biến đang giữ **một khoản lớn nhất**, không phải tổng đã cộng.

**Lan:** viết `totalByCategory`, nhận danh sách Expense và mã nhóm. Mã nhóm phải là chuỗi trong danh mục. Kiểm **toàn bộ danh sách** trước khi chọn nhóm, gồm schema, tiền và số lượng; bất kỳ khoản sai nào cũng làm lời gọi bị từ chối, kể cả khoản thuộc nhóm khác. Không giả định đầu vào đã được normalize ở nơi nào đó nếu chữ ký hàm chưa nêu tiền đề ấy.

| Biến thể/ca | Kỳ vọng cần tự đối chiếu |
| --- | --- |
| Max ba mẫu / chỉ Vở ghi / rỗng | 35000 / 18000 / 0 |
| Max có 0, số âm, quá 1e9 hoặc 501 khoản | Từ chối, dù đã gặp một giá trị lớn hợp lệ trước đó. |
| Tổng `hoc-tap` / `khac` trên ba mẫu | 18000 / 0 |
| Tổng nhóm trên rỗng, mã nhóm hợp lệ | 0 |
| Chọn `hoc-tap`, khoản `di-lai` có amount chuỗi hoặc 1.5 | Từ chối, không trả 18000. |
| Chọn `hoc-tap`, khoản ngoài nhóm có id trùng, title rỗng hoặc category mảng | Từ chối từng ca schema. |
| 501 khoản, không khoản nào thuộc nhóm chọn | Từ chối, không trả 0. |
| Mã nhóm yêu cầu là `['khac']` hoặc `toString` | Từ chối mã nhóm. |

### Đáp án biến thể max C++ — Kiểm hết rồi mới kết luận

Đặt hàm sau `totalExpenses` trong bản bài làm; nó dùng lại validation của hàm tổng. Cách này duyệt hai lượt nhưng dễ đọc ở năm nhất, vẫn O(n) thời gian và O(1) bộ nhớ phụ.

```cpp
long long maxExpense(const std::vector<long long>& amounts) {
    totalExpenses(amounts); // Kiểm toàn bộ tiền và số lượng; có thể ném lỗi.
    long long best = 0;
    for (long long amount : amounts) {
        if (amount > best) best = amount;
    }
    return best;
}
```

Mốc 0 phù hợp vì mọi khoản hợp lệ đều dương; rỗng giữ 0 mà không cần truy cập phần tử đầu. Với mẫu, `best` thành 35000 và giữ nguyên khi gặp 7000, 18000. Không được trả sớm khi gặp 1000000000 trước khi kiểm các khoản còn lại: danh sách có thể chứa khoản sai phía sau. Gọi hàm tổng ở đầu là cách tái sử dụng kiểm tra, không có nghĩa tổng chính là max. Khi thêm test, đổi lời gọi sang `maxExpense`, đừng chạy lại hàm tổng rồi nhận là đã test max.

### Đáp án tổng theo category — Xác thực trước, chọn nhóm sau

Hàm lab sau dùng `chapter3Lab` đã tạo ở đáp án Web. Đây là **hàm bổ sung**, chưa có trong API demo; không nói bộ 34 test hiện có đã kiểm nó.

```javascript
function totalByCategory(expenses, category) {
  if (typeof category !== 'string' || !Object.hasOwn(chapter3Lab.categories, category)) {
    throw new Error('Mã nhóm không hợp lệ.');
  }
  const checked = chapter3Lab.normalizeExpenses(expenses);
  const selected = checked.filter(expense => expense.category === category);
  return chapter3Lab.totalExpenses(selected);
}
```

Nếu mã nhóm sai, lời gọi bị từ chối ngay. Khi mã hợp lệ, normalize kiểm toàn danh sách trước lọc: không có kết quả nhóm nào được trả từ danh sách chứa khoản sai. `totalExpenses(selected)` cộng sau khi schema đã được bảo vệ. Nếu nơi gọi đã có bảo đảm schema rõ ràng, có thể kiểm toàn bộ tiền/số lượng bằng `totalExpenses(expenses)` trước khi lọc; nhưng **chỉ lời gọi đó không đủ chứng minh schema** cho hàm nhận dữ liệu bất kỳ.

Ví dụ phản chứng với bộ mẫu: đổi riêng tiền Xe buýt thành `"7000"`, vẫn hỏi `hoc-tap`. Hàm phải ném lỗi, dù Vở ghi hoàn toàn đúng. Đổi Xe buýt thành id 1 trùng Cơm trưa cũng phải lỗi. Lọc `hoc-tap` trước normalize sẽ làm biến mất các bằng chứng sai đó và trả 18000 trái hợp đồng.

Với dữ liệu hợp lệ, `hoc-tap` cho 18000, `khac` cho 0. Số 0 này nghĩa không có khoản thuộc nhóm, không phải “gặp lỗi nên trả 0”. Cách normalize rồi filter tạo danh sách mới, nên toàn hàm O(n) thời gian, O(n) bộ nhớ phụ. Có thể tối ưu sau, nhưng chưa đánh đổi thứ tự kiểm tra để tiết kiệm một lượt duyệt nhỏ.

## 3.7. SKILL UNLOCKED — Năng lực ở lại khi cửa sổ chat đóng

### Ba mức tự đánh giá, không phải nhãn năng lực lâu dài

Chọn **tự làm / cần gợi ý / chưa làm**, kèm bằng chứng. “Tự làm” nghĩa đã đóng chat, không nhìn đáp án. Đây là ghi nhận hiện tại, không phán năng lực lâu dài.

| Năng lực | Việc cần làm được | Mức và bằng chứng của bạn |
| --- | --- | --- |
| Giải thích | Nêu hợp đồng tiền, số lượng, tổng rỗng, tổng cực đại. | … |
| Giải thích | Trace đến 60000 và chỉ vì sao cận lỗi dừng ở 42000. | … |
| Giải thích | Phân biệt `35000` với `"35000"`, hậu quả của phép `+`. | … |
| Sửa | Chỉ thay phần gây lỗi, tách vá cận khỏi validation. | … |
| Sửa | Tự chọn ca một khoản, rỗng, biên lớn và dữ liệu sai. | … |
| Sửa | Phân biệt từ chối với tổng hợp lệ bằng 0. | … |
| Vận dụng | Làm max hoặc tổng nhóm và không che khoản sai ngoài nhóm. | … |
| Vận dụng | Nêu phần đã nhận hỗ trợ, tự làm và còn cần hỏi. | … |

Chọn một dòng chưa làm được, thu nhỏ ví dụ rồi thử lại. Bài đếm 3.5 là bước vận dụng nhỏ, chưa thay validation ở 3.6.

### Tám câu vấn đáp: hỏi từng câu rồi chờ

Nhờ bạn học hoặc dùng P07; hỏi rồi chờ, cho phép giấy và ví dụ. Không suy điểm học phần.

| Câu hỏi | Gợi ý để tự lập luận |
| --- | --- |
| 1. Vì sao đúng 60000 nhưng cận lỗi ra 42000? | Viết ba số hạng và tìm phép cộng chưa xảy ra. |
| 2. Ba phần tử có chỉ số cuối nào; dừng khi nào? | Phân biệt số lượng với chỉ số bắt đầu từ 0. |
| 3. Vì sao cần `long long` dù ba khoản đều nhỏ? | Nhân số khoản tối đa với tiền tối đa. |
| 4. Rỗng trả 0 có mâu thuẫn tiền phải dương? | Tổng danh sách và tiền của một khoản là hai đối tượng. |
| 5. Vì sao `0 + "35000"` không là tổng hợp lệ? | Nêu kiểu hai toán hạng và kết quả. |
| 6. Chuyển chuỗi thành số đã đủ chưa? | Xét rỗng, `"0"`, số âm, quá giới hạn và hậu tố chữ. |
| 7. `localStorage` có nghĩa có tài khoản hoặc CSDL máy chủ? | Chỉ nơi dữ liệu nằm, phạm vi origin và trạng thái RAM. |
| 8. Test xanh đã chứng minh bạn hiểu chưa? | Tự giải thích một ca, sửa một lỗi và làm biến thể mới. |

### Đáp án vấn đáp — Những ý cần có, không phải văn mẫu để học thuộc

1. Thiếu Vở ghi 18000 vì chỉ số 2 chưa vào thân vòng lặp; 35000 + 7000 là 42000.
2. Chỉ số cuối là 2 khi `n = 3`; cận đúng cho 0, 1, 2 và chặn 3 trước truy cập.
3. Tổng tối đa 500000000000 vượt số nguyên có dấu 32 bit; cần xét hợp đồng, không chỉ mẫu nhỏ.
4. Rỗng không chứa khoản 0 nào; nó không có khoản để cộng, nên tổng 0 hợp lệ.
5. Phép `+` với số 0 và chuỗi tạo `"035000"`, kiểu string, không phải tiền number.
6. Cần kiểm cách viết và miền giá trị; chuyển được chưa đủ, còn hàm tổng phải từ chối tiền chuỗi.
7. Dữ liệu ở trình duyệt, không đồng bộ/tài khoản/backend; đọc hoặc ghi lỗi có thể chuyển sang RAM. SQLite là bài riêng.
8. Test chỉ kiểm những ca đã chọn trên mã đã gọi; hiểu cần lời giải thích và vận dụng không nhìn đáp án.

Nếu câu trả lời còn mơ hồ, hỏi thêm một ví dụ thay vì phán “chưa hiểu gì”. “Em chưa biết xử lý JSON sai mà không ghi đè bản cũ” là điểm nghẽn cụ thể để luyện tiếp.

### Chu trình và phiếu ba dòng

![Chu trình học chủ động: mục tiêu, tự thử, dự đoán, một gợi ý, tự sửa, kiểm chứng, biến thể không AI và ghi chỗ chưa chắc.](../assets/active-learning.svg)

```text
Chọn mục tiêu + đọc hợp đồng
          ↓
Tự thử → Dự đoán trước hỏi/chạy
          ↓
Xin một gợi ý → Tự trả lời → Tự sửa một điểm
          ↓
Kiểm chứng bằng test
    ├─ Chưa đúng → Ghi điểm nghẽn → Thu nhỏ và thử lại
    └─ Đúng → Biến thể không AI → Ghi chỗ chưa chắc
                                      ↓
                              Chọn việc tiếp theo
```

Cuối phiên chỉ cần ba dòng. Ví dụ sau là **phiếu HƯ CẤU**, không phải kết quả học của một sinh viên thật:

```text
Học được: Cận cũ không cho i = 2 đi vào thân vòng lặp.
Chưa chắc: Tôi chưa tự giải thích hết kiểm tra dữ liệu đọc từ JSON.
Việc tiếp: Tự trace ca một khoản và một ca sai ngoài nhóm, chưa mở AI.
```

Gọi tên hành động hoặc kiến thức cụ thể; “học được nhiều” không giúp phiên sau biết bắt đầu đâu. Đầu ra cuối chương là một bài làm nhỏ, bảng kiểm có trạng thái thật và lời giải thích của chính bạn. Nếu muốn ghép thêm diff, hai lỗi chủ đích và khai báo hỗ trợ, chuyển sang [Final Boss](final-boss.md) sau khi học đủ các phần liên quan; bộ đề đó khác bài cận đơn và demo Web đúng ở đây.

### Gợi ý cho người hướng dẫn: trình bày trong bảy phút

Phần này kế thừa speaker notes của nguồn; tham gia tự nguyện, không kiểm tra bất ngờ. Phút 0–1 giới thiệu dữ liệu và mời tính tay; phút 1–2 hỏi phần luyện nào bị mất nếu AI viết luôn vòng lặp; phút 2–3:15 cho tự ghi chỉ số trước khi hiện trace Minh. Phút 3:15–4:30 đặt số cạnh chuỗi, dự đoán lượt cộng đầu; phút 4:30–5:30 làm mẫu hỏi một câu rồi chờ. Phút 5:30–6:30 cho phác biến thể độc lập; phút cuối điền phiếu ba dòng. Bảy phút chỉ là dẫn nhập, không thay hai hoạt động 25 phút hoặc dùng làm phép đo tốc độ.

### Nguồn kế thừa và điểm kết năng lực

Kế thừa chương 3 (mục 3.1–3.7) của [bản bảo toàn](../source/Cam-nang-AI-Sinh-vien.original.md), [Blueprint](../editorial/02_EDITORIAL_BLUEPRINT.md), [Source Audit](../editorial/01_SOURCE_AUDIT.md), P01–P08 trong [Thư viện prompt](prompt-library.md) và mã [data.js](../vi-du/nam-2-web/data.js), [app.js](../vi-du/nam-2-web/app.js), [C++](../vi-du/nam-1-cpp/vi_sinh_vien.cpp). Hoạt động và vỏ lab mới có nhãn bổ sung biên tập tại chỗ.

**Năng lực mở khóa:** tự dự đoán, sửa và kiểm chứng; giải thích được 60000, 42000 và chuỗi nối sai. Khi đóng chat, bạn còn cách tự làm lại, bằng chứng kiểm được và một việc tiếp theo cụ thể.
