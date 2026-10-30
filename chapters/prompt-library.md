# THƯ VIỆN PROMPT MẪU

Thư viện gồm mười một thẻ prompt mẫu, đánh mã từ P01 đến P11. Mỗi thẻ là một văn bản có thể sao chép; thẻ được thiết kế để AI hỗ trợ việc học, không làm thay phần việc người học cần luyện (xem mục 1.1 về vai trò của AI). Các thẻ P01–P08 phục vụ học chủ động và được giới thiệu trong bảng ở mục 3.3 của Chương 3. Các thẻ P09–P11 phục vụ việc chuẩn bị ngữ cảnh trước khi hỏi, giao việc có giới hạn cho Agent và kiểm chứng nguồn, gắn với nội dung của Chương 1 (mục 1.3), Chương 2, Chương 4 và Chương 5.

## Cách sử dụng thư viện

Mỗi lần chỉ cần chọn **một thẻ hợp với đúng điểm nghẽn** đang gặp; không gửi toàn bộ thư viện. Khi không có quyền truy cập AI, các câu hỏi trong thẻ vẫn có thể dùng để trao đổi với một sinh viên khác hoặc với giảng viên.

Prompt là một lời yêu cầu, không phải cơ chế bảo vệ quyền của hệ thống. Chỉ dùng thẻ khi phạm vi môn học cho phép và chỉ gửi dữ liệu giả. Trước khi gửi, cần đọc lại toàn bộ nội dung và thay các phần trong ngoặc vuông bằng dữ liệu của bài tập được phép chia sẻ. Không để AI tự đoán tên tệp hoặc kết quả chạy chương trình.

Các thẻ dùng chung dữ liệu giả của ứng dụng mẫu ViSinhVien (35000, 7000, 18000; tổng 60000) và hợp đồng dữ liệu: tiền là số nguyên VND từ 1 đến 1000000000, tối đa 500 khoản, danh sách rỗng có tổng bằng 0. Câu xưng "tôi" trong thẻ là lời của người học gửi cho AI. Phần thuyết minh quanh mỗi thẻ có cùng một khung: khi nào nên dùng, khi nào không nên dùng, cần chuẩn bị gì và cách kiểm tra kết quả sau lượt hỏi.

| Mã | Chức năng | Liên quan |
|---|---|---|
| P01 | Hỏi đáp kiểu Socratic, một câu mỗi lượt | Chương 3, Bài thực hành 03 (mục 2.3) |
| P02 | Gợi ý theo ba tầng | Chương 3 |
| P03 | Trace cả giá trị lẫn kiểu dữ liệu | Chương 3, Bài thực hành 04 (mục 2.4) |
| P04 | Review đúng một thay đổi | Chương 3, Bài thực hành 06 (mục 2.6) |
| P05 | Thiết kế kiểm thử trước khi viết mã | Chương 3, Bài thực hành 07 (mục 2.7) |
| P06 | Đọc tài liệu tiếng Anh có đối chiếu | Chương 3 |
| P07 | Vấn đáp ôn tập | Chương 3 |
| P08 | Đóng chat rồi làm bài biến thể | Chương 3 |
| P09 | Chuẩn bị ngữ cảnh (brief) trước khi hỏi | Mục 1.3 (prompt, context), Bài thực hành 02 (mục 2.2) |
| P10 | Hợp đồng giao việc cho Agent | Bài thực hành 05 (mục 2.5), Hồ sơ 03 (mục 4.3) |
| P11 | Kiểm chứng nguồn | Mục 1.3 (hallucination, trích dẫn), Chương 4, mục 5.3 (benchmark và thông tin giá) |

## P01 · Hỏi đáp kiểu Socratic: bắt đầu từ câu hỏi

**Khi dùng.** Người học đã biết chương trình cho kết quả sai nhưng chưa chỉ ra được lỗi nằm ở đâu. Tình huống minh họa: Minh biết chương trình C++ in ra 42000 nhưng chưa xác định được lượt lặp nào bị bỏ.

**Không nên dùng khi** cần kết quả nhanh cho một việc đã hiểu rõ, hoặc khi chưa tự tính được tổng đúng để đối chiếu.

**Chuẩn bị.** Ghi ra giấy các chỉ số hợp lệ của danh sách và tổng tính tay.

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

**Cách kiểm tra kết quả.** Sau câu hỏi đầu tiên, người học phải viết ra được một điều mà trước đó chưa viết được. Nếu AI đặt năm câu hỏi cùng lúc, chỉ chọn một câu để trả lời và yêu cầu AI chờ. Nếu đáp án bị lộ, việc đọc đáp án chỉ được tính là ôn tập, không còn là bằng chứng tự giải.

## P02 · Gợi ý theo ba tầng

**Khi dùng.** Người học chưa biết cần nhìn vào đâu nhưng vẫn muốn tự sửa lỗi.

**Không nên dùng khi** muốn xin cả ba tầng gợi ý cùng lúc; khi đó thẻ mất tác dụng.

**Chuẩn bị.** Một dòng mô tả điều đã thử, chẳng hạn "em đã in tổng sau từng lượt".

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

**Cách kiểm tra kết quả.** Lỗi thường gặp là xin cả ba tầng một lúc rồi đọc hết. Nhịp làm việc hữu ích là: một gợi ý, một thao tác, một nhận xét; không phải một prompt dài đổi lấy một đáp án hoàn chỉnh. Kết quả đạt yêu cầu là bảng trace do người học tự điền và một thay đổi người học tự giải thích được.

## P03 · Trace cả giá trị lẫn kiểu dữ liệu

**Khi dùng.** Người học thấy một chuỗi số dài bất thường và muốn biết chuỗi đó hình thành ở bước nào. Tình huống minh họa: Lan mô phỏng lỗi cộng chuỗi trong JavaScript. Đây là lỗi được dựng riêng cho bài luyện, không mô tả bản demo Web đúng đi kèm sách.

**Không nên dùng khi** muốn AI điền sẵn bảng trace; mục đích của thẻ là người học tự điền.

**Chuẩn bị.** Biết giá trị khởi tạo của biến tổng và kiểu dữ liệu của từng khoản tiền.

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

**Cách kiểm tra kết quả.** Khi ghi chuỗi, phải giữ dấu ngoặc kép. `"35000"` và `35000` trông gần giống nhau nhưng phép cộng có thể xử lý khác nhau. Ghi kèm kiểu dữ liệu cho mỗi kết quả là cách tránh đoán theo hình dáng của giá trị. Kết quả đạt yêu cầu là người học chỉ ra được lượt đầu tiên làm đổi kiểu và vị trí cần kiểm tra đầu vào.

## P04 · Review đúng một thay đổi

**Khi dùng.** Người học đã có một bản vá nhỏ và muốn kiểm tra lập luận đằng sau bản vá mà không để AI viết lại toàn bộ chương trình.

**Không nên dùng khi** bản vá chưa được viết, hoặc khi thay đổi gồm nhiều phần chưa tách riêng.

**Chuẩn bị.** Dòng mã trước và sau khi sửa, cùng các ca kiểm thử dự định dùng.

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

**Câu hỏi tự kiểm tra.** Nếu bản review kết luận "đã sửa cận nên chương trình an toàn với mọi đầu vào", cần phản biện bằng ca kiểm thử nào? Gợi ý để tự suy nghĩ: điều kiện về số lượng khoản và miền giá trị tiền chưa xuất hiện trong diff này.

## P05 · Thiết kế kiểm thử trước khi viết mã

**Khi dùng.** Người học chuẩn bị viết hàm tính tổng và chưa muốn nhận thuật toán có sẵn.

**Không nên dùng khi** để AI tính hộ mọi kết quả kỳ vọng; khi đó bộ kiểm thử mất tính độc lập.

**Chuẩn bị.** Hợp đồng dữ liệu của hàm và các nhóm ca kiểm thử cần có: ca thường, ca biên và ca dữ liệu sai.

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

**Cách kiểm tra kết quả.** Một bộ kiểm thử không có kỳ vọng được xác định độc lập dễ xác nhận nhầm chính lỗi của chương trình. Mọi đầu ra do AI sinh ra cũng cần được đối chiếu bằng tính tay hoặc lập luận.

## P06 · Đọc tài liệu tiếng Anh có đối chiếu

**Khi dùng.** Người học vướng một số từ kỹ thuật khi đọc tài liệu tiếng Anh.

**Không nên dùng khi** muốn AI đoán nội dung của một trang tài liệu mà người học chưa đọc.

**Chuẩn bị.** Câu hoặc đoạn văn cần hiểu, kèm ngữ cảnh sử dụng trong bài.

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

**Cách kiểm tra kết quả.** Với một trang tài liệu thật, cần bổ sung URL và đoạn văn đã đọc được. Nếu AI không truy cập được trang, yêu cầu AI nói rõ điều đó; một bản dịch trôi chảy, tự tin không chứng minh rằng AI đã đọc đúng nguồn. Kết quả đạt yêu cầu là người học tự diễn giải được câu văn và phân biệt được chuyển kiểu với kiểm tra hợp lệ.

## P07 · Vấn đáp ôn tập, không đoán điểm môn học

**Khi dùng.** Người học đã hoàn thành một nội dung và muốn tự kiểm tra mức độ hiểu bằng hình thức vấn đáp.

**Không nên dùng khi** muốn AI dự đoán điểm, đánh giá năng lực tổng quát hoặc suy ra quy định của học phần.

**Chuẩn bị.** Tóm tắt những lỗi và khái niệm đã học, kèm dữ liệu giả liên quan.

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

**Phân vai giữa AI và người học (AI vs Human).** Đây là sự phân công, không phải cuộc thi hơn thua: AI hỗ trợ, người học quyết định. AI đặt câu hỏi và phản hồi. Người học phải nêu ví dụ, tự chạy chương trình khi cần và giải thích vì sao bằng chứng đã đủ hoặc chưa đủ. Một câu hỏi mà người học đã đọc đáp án chỉ được tính là ôn tập.

## P08 · Đóng chat rồi làm bài biến thể

**Khi dùng.** Người học muốn tự kiểm tra khả năng vận dụng trên một bài tương tự mà chưa nhận lời giải.

**Không nên dùng khi** muốn thay thế phiên tự học 25 phút không dùng AI ở mục 3.5; thẻ này chỉ tạo một lượt tự thử ngắn.

**Chuẩn bị.** Giấy nháp hoặc vùng soạn thảo không có gợi ý của AI, và đồng hồ bấm giờ.

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

**Cách kiểm tra kết quả.** Bốn phút là một lượt tự thử ngắn, khác với bài 25 phút không dùng AI ở mục 3.5. Không cần hoàn tất mọi thứ trong một lượt; điều cần thiết là ghi trung thực những gì đã tự làm được.

## P09 · Chuẩn bị ngữ cảnh (brief) trước khi hỏi

**Khi dùng.** Người học cần hỏi AI về một lỗi hoặc một nhiệm vụ cụ thể và muốn cung cấp đủ ngữ cảnh ngay từ đầu.

**Không nên dùng khi** chưa quan sát được hiện tượng nào; khi đó cần chạy thử hoặc trace trước rồi mới điền thẻ.

**Chuẩn bị.** Thông tin về môi trường (shell, thư mục hiện tại, tệp liên quan), hiện tượng quan sát được, kỳ vọng tự tính và điều đã thử.

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

**Cách kiểm tra kết quả.** Nếu chưa biết thông tin về môi trường, ghi "chưa xác định" và hỏi cách xác định; không điền một phiên bản bất kỳ chỉ để biểu mẫu trông đầy đủ. Câu trả lời đạt yêu cầu phải tách được giả thuyết với điều đã kiểm chứng và đề xuất một phép thử nhỏ để phân biệt các giả thuyết.

## P10 · Hợp đồng giao việc cho Agent

**Khi dùng.** Người học giao cho Agent một thay đổi đã được thống nhất, trong một bản sao bài làm và với danh sách tệp cụ thể.

**Không nên dùng khi** chưa kiểm tra cơ chế phân quyền thật của công cụ, hoặc khi phạm vi thay đổi chưa được xác định rõ.

**Chuẩn bị.** Mô tả thay đổi cần làm, đường dẫn bản sao, danh sách tệp được phép sửa và điểm khôi phục (checkpoint) trước khi giao việc.

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

**Cách kiểm tra kết quả.** Trước khi dùng thẻ, kiểm tra quyền thật trong công cụ. Câu "không xóa file" trong prompt không thay thế được cơ chế giới hạn truy cập hệ thống tệp hoặc cơ chế phê duyệt hành động. Sau khi Agent hoàn thành, người học đọc diff, tự chạy lại kiểm thử và tự giải thích thay đổi trước khi chấp nhận kết quả.

## P11 · Kiểm chứng nguồn

**Khi dùng.** Người học cần kiểm chứng một nhận định (claim) về sản phẩm, giá, chính sách hoặc quy định trước khi sử dụng hay trích dẫn.

**Không nên dùng khi** muốn suy ra quyền lợi của tài khoản cá nhân hoặc quy định của môn học từ thông tin chung; những nội dung này cần tra tại nguồn chính thức tương ứng.

**Chuẩn bị.** Nhận định cụ thể cần kiểm chứng (sản phẩm, phiên bản, quốc gia nếu liên quan) và các nguồn đã có.

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

**Cách kiểm tra kết quả.** Câu trả lời đạt yêu cầu phải ghi URL, ngày đọc và phạm vi áp dụng của từng nguồn, đồng thời tách rõ nội dung quan sát trực tiếp, phần suy luận và phần chưa truy cập được. Người học cần tự mở lại ít nhất một nguồn chính thức để đối chiếu trước khi sử dụng kết quả.

## Ghi nhận sau khi dùng thẻ

Sau mỗi lần dùng thẻ, ghi một câu theo mẫu: "Tôi dùng P__ để tháo gỡ __; bằng chứng sau lượt hỏi là __." Nếu ô cuối cùng chỉ ghi được "AI đã trả lời", cần quay lại và chọn một phép thử hoặc một lời giải thích do chính người học thực hiện.
