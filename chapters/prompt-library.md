# THƯ VIỆN PROMPT · HỎI ÍT HƠN, HIỂU RÕ HƠN

Tám thẻ P01–P08 kế thừa chức năng học tập của mục 3.4 bản nguồn; P09–P11 là bổ sung biên tập cho việc chuẩn bị ngữ cảnh, giao Agent và kiểm chứng nguồn. Chọn **một thẻ cho đúng điểm nghẽn**, không gửi cả thư viện. Bạn có thể dùng câu hỏi với bạn học hoặc giảng viên nếu không có quyền truy cập AI.

Prompt là lời yêu cầu, không phải cơ chế bảo vệ quyền hệ thống. Chỉ dùng khi phạm vi môn học cho phép, chỉ gửi dữ liệu giả. Trước khi bấm gửi, đọc lại tất cả nội dung và thay phần có ngoặc vuông bằng dữ liệu của bài tập được phép chia sẻ; đừng để AI tự đoán tệp hoặc kết quả chạy.

## P01 · Socratic: bắt đầu từ câu hỏi

**Dùng khi:** Minh biết chương trình ra 42000 nhưng chưa chỉ ra lượt bị bỏ. **Bạn chuẩn bị:** viết chỉ số hợp lệ và tổng tính tay lên giấy.

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

**THINK FIRST:** Sau câu hỏi đầu, bạn phải viết được điều gì mà trước đó chưa viết được? Nếu AI hỏi năm câu cùng lúc, chọn một câu để trả lời và yêu cầu chờ. Nếu đáp án lộ, việc đọc nó là ôn tập, không còn là bằng chứng tự giải.

## P02 · Ba tầng gợi ý

**Dùng khi:** chưa biết nhìn vào đâu nhưng vẫn muốn tự sửa. **Bạn chuẩn bị:** một dòng mô tả điều đã thử, chẳng hạn “em đã in tổng sau từng lượt”.

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

**Lỗi thường gặp:** xin cả ba tầng một lúc rồi đọc hết. Nhịp hữu ích là một gợi ý → một thao tác → một nhận xét, không phải một prompt dài → một đáp án hoàn chỉnh.

## P03 · Trace cả giá trị lẫn kiểu

**Dùng khi:** Lan thấy một chuỗi số dài và muốn biết nó hình thành ở đâu. Đây là lỗi mô phỏng riêng, không mô tả demo Web đúng đi kèm.

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

Giữ dấu ngoặc kép khi ghi chuỗi. `"35000"` và `35000` nhìn gần giống nhưng phép cộng có thể xử lý khác. Ghi mỗi kết quả cùng kiểu là cách chống đoán bằng hình dáng.

## P04 · Review đúng một thay đổi

**Dùng khi:** đã có bản vá nhỏ và muốn kiểm tra lập luận, không muốn AI viết lại cả chương trình.

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

**QUICK CHECK:** Nếu review nói “đã sửa cận nên an toàn mọi đầu vào”, bạn sẽ phản biện bằng ca nào? Gợi ý để tự nghĩ: số lượng và miền tiền chưa xuất hiện trong diff này.

## P05 · Test trước code

**Dùng khi:** chuẩn bị viết hàm tính tổng, chưa muốn được cho thuật toán.

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

Một bộ test không có kỳ vọng độc lập dễ xác nhận nhầm chính lỗi của chương trình. Đầu ra AI sinh ra cũng cần đối chiếu bằng tính tay hoặc lập luận.

## P06 · Đọc tiếng Anh có đối chiếu

**Dùng khi:** vướng từ kỹ thuật, không phải yêu cầu AI đoán nội dung một trang chưa đọc.

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

Với trang thật, thêm URL và đoạn đã đọc được. Nếu AI không truy cập được trang, yêu cầu nói rõ; bản dịch tự tin không chứng minh nó đã đọc đúng nguồn.

## P07 · Vấn đáp, không đoán điểm môn học

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

**AI VS HUMAN — phân vai, không thi hơn thua:** AI đặt câu hỏi và phản hồi. Bạn phải nêu ví dụ, tự chạy nếu cần, giải thích tại sao bằng chứng đủ hoặc chưa đủ. Một câu bạn đã đọc đáp án chỉ tính là ôn tập.

## P08 · Đóng chat rồi làm biến thể

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

Bốn phút là một lượt tự thử ngắn, khác bài 25 phút không AI ở chương 3. Không cần hoàn tất mọi thứ trong một lượt; cần trung thực điều tự làm được.

## P09 · Brief trước khi hỏi — bổ sung biên tập

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

Nếu chưa biết môi trường, ghi “chưa xác định” và hỏi cách xác định; đừng điền một phiên bản cho đẹp biểu mẫu.

## P10 · Hợp đồng giao việc cho Agent — bổ sung biên tập

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

Trước khi dùng thẻ, kiểm tra quyền thật trong công cụ. Chỉ câu “không xóa file” trong prompt không thay thế cơ chế giới hạn filesystem hoặc phê duyệt hành động.

## P11 · Kiểm chứng nguồn — bổ sung biên tập

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

## Trước khi rời thư viện

Ghi một câu: “Tôi dùng P__ để tháo gỡ __; bằng chứng sau lượt hỏi là __.” Nếu ô cuối chỉ có “AI đã trả lời”, quay lại và chọn một phép thử hoặc lời giải thích do chính bạn thực hiện.
