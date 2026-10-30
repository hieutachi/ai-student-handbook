# CHƯƠNG 1 · AI TRONG HỌC TẬP: VAI TRÒ, CÁCH HOẠT ĐỘNG VÀ GIỚI HẠN

Đây là chương mở đầu của cuốn sách. Chương trả lời ba câu hỏi nền tảng trước khi bắt đầu dùng trợ lý AI: AI giúp được gì và không giúp được gì trong việc học, đâu là ranh giới giữa dùng AI để học và dùng AI để né học, và phía sau một câu trả lời của AI thực sự có những thành phần nào.

Cả cuốn sách đi theo một mạch năm bước: **Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn**. Chương 1 là bước *Hiểu*: nắm vai trò, cách hoạt động và giới hạn của AI. Chương 2 là bước *Dùng*: điều khiển quá trình làm việc với AI bằng bằng chứng. Chương 3 là bước *Giữ vững*: tận dụng AI mà vẫn tự học được. Chương 4 là bước *Có trách nhiệm*: giữ ranh giới về dữ liệu, bảo mật, bản quyền và liêm chính. Chương 5 là bước *Chọn*: chọn công cụ, model và gói dịch vụ phù hợp, kể cả chi phí. Việc chọn model và tính chi phí được đặt ở cuối có chủ đích, vì chỉ khi đã hiểu vai trò và ranh giới, người học mới chọn công cụ có cơ sở thay vì chọn theo danh tiếng hay giá.

Toàn bộ chương có thể hoàn thành bằng sách và giấy: không cần đăng ký, cài đặt, tạo key, gọi API hoặc trả tiền. Nhân vật, hội thoại và các thẻ trả lời trong chương là *tình huống hư cấu*; chúng không đại diện cho sản phẩm cụ thể, không phải hội thoại hay benchmark thực, và không đại diện cho khảo sát sinh viên của Trường.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Nêu ba vai trò hợp lý của AI trong học tập, điều AI làm tốt và điều AI làm kém.
2. Phân biệt dùng AI để học với lạm dụng AI để né học, dựa trên các dấu hiệu quan sát được; vận dụng nguyên tắc "AI hỗ trợ, người học quyết định".
3. Phân biệt các vai trò model, provider, application (ứng dụng), producer và user trong một lượt dùng AI; ghi "chưa xác định" khi thiếu bằng chứng thay vì suy đoán.
4. Viết một prompt đủ context, gồm mục tiêu, phần mã liên quan, hợp đồng dữ liệu, kết quả mong đợi và cách kiểm tra; giải thích token và context window ở mức khái niệm.
5. Phân biệt suy luận, thực thi và tra cứu nguồn; nhận diện hiện tượng hallucination và kiểm tra trích dẫn.

Sản phẩm của chương gồm ba thành phần: một bảng tự đánh giá cách dùng AI (đúng, lạm dụng hoặc cần hỏi giảng viên), một bản nhận diện công cụ có ghi rõ phần chưa biết và một prompt đủ context.

## Tình huống mở đầu

Tình huống minh họa xuyên suốt cuốn sách gồm hai sinh viên: Minh, năm nhất, đang học C++; Lan, năm hai, đã học lập trình hướng đối tượng (OOP), cấu trúc dữ liệu và giải thuật (DSA), cơ sở dữ liệu (CSDL) và lập trình Web. Hai người cùng thực hiện **ViSinhVien**, một bài tập quản lý chi tiêu chỉ dùng dữ liệu giả. Minh học mảng và vòng lặp trên phiên bản C++; Lan làm phiên bản Web bằng HTML, JavaScript và `localStorage`. Bài tập không có backend, đăng nhập, kết nối ngân hàng hay dữ liệu tài chính thật. Trợ lý AI chỉ được dùng để hỗ trợ việc học; bản thân ViSinhVien không tích hợp AI.

Minh ghi ba khoản chi giả trên giấy như sau:

| Khoản chi giả | Số tiền nguyên VND |
| --- | ---: |
| Cơm trưa | 35000 |
| Xe buýt | 7000 |
| Vở ghi | 18000 |
| Tổng cần có | 60000 |

Đoạn mã dưới đây chứa một lỗi được đưa vào có chủ đích để người học đọc và đặt câu hỏi. Các số tiền trong đoạn mã được giả định là hợp lệ; chương trình chưa thực hiện việc nhập và xác thực dữ liệu.

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

Minh dán nguyên đoạn mã vào ba ứng dụng AI khác nhau, kèm cùng một câu hỏi:

```text
Tôi mới học vòng lặp C++. Tôi cần cộng tất cả khoản chi GIẢ:
35000, 7000, 18000 phải ra 60000, nhưng chương trình đang cho 42000.
Hãy gợi ý một bước để tôi tự tìm lỗi, chưa viết lại cả chương trình.
```

Ba ứng dụng trả về ba câu trả lời khác nhau. Ứng dụng thứ nhất đặt câu hỏi ngược lại cho người học, ứng dụng thứ hai đưa ra cách sửa với giọng rất chắc chắn, ứng dụng thứ ba đề xuất cách sửa khác và nhắc phải kiểm thử. Các thẻ dưới đây không gắn với sản phẩm nào và không phải báo cáo đã chạy chương trình.

### Thẻ trả lời A

> Khi `n = 3`, chỉ số của khoản Vở ghi là bao nhiêu? Hãy thay chỉ số đó vào điều kiện `i < n - 1` và quyết định xem vòng lặp có cộng khoản này không.

### Thẻ trả lời B

> Vòng lặp thiếu một lượt. Bạn cứ đổi thành `i <= n`; như vậy sẽ cộng đủ và luôn an toàn. Không cần thử thêm vì lỗi này rất đơn giản.

### Thẻ trả lời C

> Điều kiện đang bỏ phần tử cuối. Với yêu cầu cộng mọi khoản, hướng sửa là `i < n`, không phải `i <= n`. Tôi chưa thực thi chương trình; hãy kiểm tra danh sách rỗng, một khoản và ba khoản sau khi tự sửa.

Câu hỏi đặt ra là: nếu cả ba đều là AI, vì sao chúng trả lời khác nhau, và nên dựa vào câu trả lời nào? Một câu trả lời cần được xét đồng thời theo độ đúng, theo mức độ phù hợp với cách giúp người học và theo bằng chứng đi kèm, chứ không theo tốc độ xuất hiện hay độ tự tin của câu chữ. Chẳng hạn, prompt đã yêu cầu rõ **gợi ý một bước**, trong khi thẻ B khẳng định cách sửa được đề xuất **luôn an toàn** mà không nêu căn cứ.

**Yêu cầu trước khi đọc tiếp.** Hãy tự cộng ba khoản, chọn một thẻ để bắt đầu học và ghi lý do lựa chọn. Người chưa học C++ vẫn có thể nhận ra rằng một kết luận về chương trình cần đi kèm cách kiểm tra. Sau khi học xong mục 1.3, hãy chấm lại ba thẻ theo ba câu hỏi: kết luận có đúng không, cách giúp có đúng với yêu cầu không, và có bằng chứng đi kèm không.

## 1.1. Vai trò của AI trong học tập: giúp được gì, không giúp được gì, đâu là lạm dụng

Mục này giúp người học trả lời một câu hỏi trước mọi câu hỏi kỹ thuật: nên để AI làm phần việc nào trong quá trình học, và phần việc nào phải giữ lại cho người học. Câu trả lời được rút ra từ ba thẻ A, B, C ở tình huống mở đầu và từ ba khoản chi 35000, 7000, 18000.

### Ba vai trò hợp lý của AI trong học tập

Học là quá trình thay đổi hiểu biết và kỹ năng của chính người học. Vì vậy, một vai trò của AI chỉ hợp lý khi sau lượt dùng, người học hiểu hoặc làm được nhiều hơn trước. Có ba vai trò đáp ứng điều kiện này.

**Vai trò thứ nhất: gia sư giải thích.** AI có thể giải thích một khái niệm theo nhiều cách, đổi ví dụ khi người học chưa hiểu, hoặc đặt câu hỏi gợi mở thay vì đưa ngay đáp án. Thẻ A là ví dụ điển hình: thẻ này không sửa hộ mà hỏi chỉ số của khoản Vở ghi là bao nhiêu và vòng lặp có cộng khoản đó không. Minh phải tự trả lời, nên người hiểu vòng lặp là Minh chứ không phải AI. Người học có thể chủ động yêu cầu cách giúp này, như prompt trong tình huống mở đầu đã làm khi xin "một bước gợi ý, chưa viết lại cả chương trình".

**Vai trò thứ hai: người phản biện và kiểm tra.** Sau khi tự làm xong, người học có thể nhờ AI tìm chỗ thiếu: ca kiểm thử chưa nghĩ tới, điều kiện biên bị bỏ sót, đoạn giải thích còn mơ hồ. Thẻ C làm đúng việc này khi nhắc kiểm tra danh sách rỗng, một khoản và ba khoản. Thứ tự rất quan trọng: *làm trước, nhờ phản biện sau*. Nếu đảo ngược thứ tự, người học chỉ còn đọc lại điều AI đã nghĩ hộ.

**Vai trò thứ ba: trợ lý cho việc lặp.** Một số việc tốn thời gian nhưng không tạo ra hiểu biết mới: định dạng lại bảng, đổi tên biến đồng loạt, sinh dữ liệu giả để thử, soạn khung tài liệu. AI làm các việc này nhanh, người học tiết kiệm thời gian cho phần cần suy nghĩ. Tiêu chí phân biệt rất đơn giản: nếu bản thân việc đó chính là mục tiêu của bài học (ví dụ bài học đang dạy vòng lặp mà nhờ AI viết vòng lặp), thì đó không còn là "việc lặp" nữa.

Ba vai trò có chung một điểm: AI nằm cạnh người học, không nằm thay chỗ người học.

### AI làm tốt điều gì, làm kém điều gì

Để quyết định giao việc nào cho AI, cần biết hai mặt của công cụ này. Phần dưới đây mô tả xu hướng chung; mức độ cụ thể khác nhau giữa các model và ứng dụng, và mục 1.2 sẽ nói cách phân biệt chúng.

**AI thường làm tốt:**

- **Tốc độ.** Phản hồi xuất hiện sau vài giây, kể cả khi yêu cầu dài. Người học có thể thử nhiều cách hỏi trong thời gian ngắn.
- **Diễn đạt.** AI viết mạch lạc, đổi giọng văn, tóm tắt hoặc giải thích lại cùng một ý theo nhiều mức độ.
- **Gợi ý.** AI nêu được nhiều hướng giải, nhiều ca thử, nhiều cách đặt tên, giúp người học thoát khỏi tình trạng "chưa biết bắt đầu từ đâu".

**AI thường làm kém hoặc không thể làm:**

- **Có thể sai mà vẫn tự tin.** Thẻ B khẳng định `i <= n` "luôn an toàn" và "không cần thử thêm" trong khi cách sửa đó cho phép truy cập ngoài danh sách. Giọng chắc chắn của câu chữ không phải bằng chứng về độ đúng. Hiện tượng này được gọi là hallucination và sẽ được phân tích ở mục 1.3.
- **Thiếu ngữ cảnh.** AI chỉ biết điều đã được gửi vào lượt đó. Nếu quên dán mã, quên nêu phạm vi bài tập, AI sẽ đoán, và có thể đề xuất đăng nhập, máy chủ hay đồng bộ thanh toán cho một bài tập vốn chỉ dùng dữ liệu giả.
- **Không chịu trách nhiệm.** Khi bài nộp có lỗi, khi một kết luận sai được đem ra dùng, người chịu hậu quả là người học. AI không đứng tên trên bài nộp và không giải thích thay trước giảng viên.

Từ hai danh sách trên có thể rút ra một quy tắc phân công: giao cho AI những phần mà **kết quả kiểm tra được nhanh** (ca thử, định dạng, gợi ý hướng đi), và giữ lại cho người học những phần mà **hiểu biết và trách nhiệm không thể chuyển giao** (quyết định cuối, giải thích, kiểm chứng).

### Dùng AI để học và dùng AI để né học

Cùng một công cụ, cùng một bài toán, có thể dẫn tới hai kết quả hoàn toàn khác nhau. Hãy quay lại ví dụ ba khoản chi: 35000 cộng 7000 cộng 18000 phải bằng 60000, còn chương trình cho 42000.

- Minh tự cộng ba khoản trước, thấy kết quả chương trình thiếu đúng 18000, rồi nhờ AI gợi ý một bước. Sau đó Minh tự sửa cận vòng lặp, thử ca rỗng, một khoản, ba khoản và giải thích được vì sao `i < n` đúng còn `i <= n` thì không. Đây là *dùng AI để học*.
- Một cách làm khác: dán đoạn mã, nhận bản sửa hoàn chỉnh, chép vào bài và nộp. Chương trình có thể in đúng 60000. Nhưng khi được hỏi "vì sao vòng lặp dừng ở chỉ số 1", người học không trả lời được. Con số đúng, còn hiểu biết thì không tăng. Đây là *dùng AI để né học*.

Điểm khác biệt không nằm ở việc có dùng AI hay không, mà ở chỗ **ai đã suy nghĩ**. Bảng dưới đây giúp nhận ra dấu hiệu qua hành vi quan sát được.

| Tiêu chí | Dấu hiệu dùng đúng | Dấu hiệu lạm dụng |
| --- | --- | --- |
| Thứ tự | Tự thử hoặc tự dự đoán trước, rồi mới hỏi AI | Hỏi AI ngay khi vừa đọc đề, chưa tự thử |
| Mức trợ giúp | Yêu cầu gợi ý từng bước, câu hỏi dẫn dắt | Yêu cầu bản hoàn chỉnh rồi chép nguyên |
| Kiểm chứng | Tự chạy, tự đối chiếu với 60000 hoặc với test | Tin lời "đã đúng", không chạy, không đối chiếu |
| Giải thích | Nói lại được bằng lời riêng vì sao đúng | Không giải thích được dòng mã vừa nộp |
| Quyền quyết định | Chấp nhận, sửa hoặc bác bỏ từng đề xuất có lý do | Nhận mọi đề xuất, kể cả phần ngoài phạm vi bài |
| Dấu vết học | Còn bản nháp, ghi chú, lỗi đã gặp và cách sửa | Chỉ còn kết quả cuối, không có quá trình |

Ba ví dụ số 35000, 7000 và 18000 cho thấy một phép thử nhanh: sau khi dùng AI, nếu người học tự lần ra được tổng từng bước (35000, rồi 42000, rồi 60000) và chỉ ra bước nào bị bỏ, thì hiểu biết đã thuộc về người học. Nếu không lần ra được, kết quả đúng chỉ là mượn.

Cần nói rõ thêm hai điều. Thứ nhất, một lượt dùng không lạm dụng không có nghĩa là hợp lệ trong mọi bài: mỗi học phần, mỗi bài tập có thể quy định riêng về việc được dùng AI đến mức nào, và quy định đó phải được tôn trọng. Thứ hai, những ranh giới về dữ liệu, bảo mật, bản quyền và liêm chính học thuật được trình bày ở Chương 4; cách giữ để vẫn tự học được trong khi dùng AI được trình bày ở Chương 3. Mục này chỉ đặt nền để người học nhận ra hai hướng đi.

### Nguyên tắc xuyên suốt: AI hỗ trợ, người học quyết định

Từ các phần trên có thể rút ra nguyên tắc mà cả cuốn sách sẽ nhắc lại: **AI hỗ trợ, người học quyết định.**

Nguyên tắc này có ba nghĩa cụ thể. *Người học đặt mục tiêu*: nêu việc cần làm, giới hạn mức trợ giúp, chọn dữ liệu nào được gửi đi. *Người học kiểm chứng*: không dùng kết quả nào chưa có bằng chứng, dù lời giải nghe rất hợp lý. *Người học chịu trách nhiệm*: bài nộp mang tên người học, nên mọi dòng trong đó phải giải thích được. AI có thể đề xuất nhanh và nhiều, nhưng quyết định chấp nhận hay bác bỏ vẫn thuộc về người học.

Nếu nhớ một câu từ chương này, đó nên là câu ấy. Ở Chương 2, nguyên tắc trở thành thao tác: giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. Ở Chương 3, nguyên tắc trở thành thói quen: tự dự đoán, tự làm, tự giải thích. Ở Chương 4, nguyên tắc trở thành ranh giới.

### Bài tập tự đánh giá: dùng đúng, lạm dụng hay cần hỏi giảng viên

Chưa hiểu ngay cách phân loại là điều bình thường; hãy dùng bảng dấu hiệu ở trên làm công cụ đối chiếu. Với mỗi tình huống giả định dưới đây, chọn một trong ba phương án: **dùng đúng**, **lạm dụng** hoặc **cần hỏi giảng viên**, rồi ghi lý do bằng một câu.

| STT | Tình huống giả định | Lựa chọn | Lý do |
| ---: | --- | --- | --- |
| 1 | Minh tự cộng 35000 + 7000 + 18000, thấy chương trình in 42000, rồi nhờ AI gợi ý một bước để tự tìm lỗi. | | |
| 2 | Lan nhờ AI viết trọn phần lưu dữ liệu vào `localStorage`, dán vào bài và nộp mà chưa đọc mã. | | |
| 3 | Minh viết xong hàm tính tổng, rồi nhờ AI nêu thêm các ca kiểm thử còn thiếu; Minh tự dự đoán kết quả từng ca trước khi chạy. | | |
| 4 | Đề bài ghi "sinh viên tự làm", nhưng Minh muốn nhờ AI giải thích một thông báo lỗi khó hiểu của trình biên dịch. | | |
| 5 | AI báo "đã chạy test và tất cả đều đạt"; Lan ghi vào báo cáo như kết quả của chính Lan mà không chạy lại. | | |

### Đáp án tự đánh giá: năm tình huống và lý do

**1. Dùng đúng.** Minh tự làm trước, giới hạn mức trợ giúp ở một bước và còn giữ quyền tự sửa. Cả thứ tự, mức trợ giúp lẫn quyền quyết định đều khớp dấu hiệu dùng đúng.

**2. Lạm dụng.** Phần việc này có thể chính là nội dung bài học, người học chưa đọc và chưa kiểm chứng, nên không giải thích được mã đã nộp. Cách đúng hơn là tự viết bản nháp rồi nhờ AI phản biện, hoặc xin gợi ý từng bước.

**3. Dùng đúng.** AI đóng vai người phản biện sau khi người học đã làm. Việc tự dự đoán kết quả trước khi chạy giữ phần suy nghĩ thuộc về Minh.

**4. Cần hỏi giảng viên.** Quy định "tự làm" có thể loại trừ mọi hỗ trợ của AI hoặc chỉ loại trừ việc làm hộ; câu chữ chưa đủ để kết luận. Việc đúng là hỏi giảng viên và ghi lại câu trả lời, không tự suy diễn theo hướng có lợi cho bản thân.

**5. Lạm dụng.** Lời "đã chạy test" của AI chưa phải bằng chứng. Người học phải tự chạy, hoặc ghi rõ đây là lời khẳng định chưa kiểm chứng. Chỗ sai nằm ở khâu kiểm chứng và trách nhiệm, không nằm ở việc có dùng AI hay không.

Nếu phân loại đúng cả năm tình huống kèm lý do hợp lý, người học đã nắm được tiêu chí của mục này. Nếu lệch một hoặc hai tình huống, nên đọc lại bảng dấu hiệu rồi thử viết lại lý do. Từ mục 1.2 trở đi, chương chuyển từ câu hỏi "nên dùng AI vào việc gì" sang câu hỏi "AI mà chúng ta đang dùng thực chất là gì".

## 1.2. Nhận diện công cụ AI: model, provider và ứng dụng (AI Mystery, AI Map)

### Từ con số 42000 đến câu hỏi "đang dùng công cụ nào?"

Ta có `35000 + 7000 = 42000`; phải cộng thêm `18000` mới được `60000`. **Con số 42000 có thể là một tổng trung gian đúng**, tức tổng của hai khoản đầu. Nó chỉ trở thành sai lệch khi yêu cầu là cộng đủ ba khoản mà chương trình lại kết thúc ở đó. Một con số đứng riêng chưa đủ để chẩn đoán lỗi.

Đoạn mã có `n = 3`, nên các chỉ số hợp lệ là 0, 1 và 2. Điều kiện `i < n - 1`, tức `i < 2`, khiến vòng lặp dừng trước khoản Vở ghi ở chỉ số 2. Phép `static_cast<int>` chuyển kích thước của vector sang số nguyên có dấu để biểu diễn cận; với tối đa 500 khoản, giá trị này nằm gọn trong miền đang dùng.

**Kết quả mong đợi** (suy ra từ mã nguồn, chưa thực thi):

```text
Tong chi tieu: 42000 VND
```

Chuỗi in ra được viết không dấu nhằm giảm lỗi hiển thị trên một số terminal. Việc lần vết (trace) đầy đủ, ca danh sách rỗng, vấn đề kiểu có dấu và không dấu, cũng như tình huống chạy nhầm tệp thực thi cũ được trình bày ở Bài thực hành 03 (mục 2.3) trong **Chương 2 · Điều khiển quá trình làm việc với AI**. Chương này chỉ dừng ở việc nhận diện vấn đề và xác định loại bằng chứng cần có.

### Đáp án mở đầu — Chọn thẻ để học, không chọn giọng văn tự tin

**Nên bắt đầu học với thẻ A**, vì thẻ này giữ đúng yêu cầu gợi ý một bước. Thẻ C phù hợp để đối chiếu sau khi đã tự sửa: thẻ này sửa đúng và nói rõ chưa chạy chương trình, nhưng tiết lộ nhiều hơn mức Minh yêu cầu. Thẻ B cần bị loại, vì điều kiện `i <= n` cho phép chỉ số `n` nằm ngoài danh sách; trong C++, truy cập như vậy dẫn tới hành vi không xác định (undefined behavior).

Cận `i < n` duyệt đúng các chỉ số hợp lệ và dừng trước chỉ số bằng kích thước. Tuy nhiên, sửa cận **chưa bổ sung toàn bộ việc kiểm tra dữ liệu**; Minh vẫn cần tự giải thích và thử các biến thể. Ba thẻ hư cấu này cũng không chứng minh thương hiệu nào tốt hơn thương hiệu nào.

### Model, provider, application và producer: bốn câu hỏi khác nhau

Câu nói "tôi dùng ChatGPT" thường chỉ nêu tên sản phẩm đang mở, chưa xác định model nào xử lý yêu cầu. **Trí tuệ nhân tạo** (tiếng Anh: *artificial intelligence*, AI) là lĩnh vực rộng, bao gồm cả nhận dạng hình ảnh và phát hiện bất thường. Chương này tập trung vào **AI tạo sinh** (*generative AI*), tức các hệ thống tạo ra văn bản hoặc mã. **Mô hình ngôn ngữ lớn** (*large language model*, LLM) thường là thành phần cốt lõi của các trợ lý; tuy nhiên, không phải hệ thống AI nào cũng là chatbot. Khả năng nhận ảnh, âm thanh hay tệp phụ thuộc vào từng model và từng ứng dụng.

**Model** là mô hình tính toán đã được huấn luyện để xử lý đầu vào và tạo đầu ra. Các tên như GPT, Claude hay Gemini có thể chỉ một họ mô hình, chưa phải một phiên bản cụ thể. Tài liệu định danh chính thức đáng tin hơn việc đoán qua văn phong; một lời giải mạch lạc không bảo đảm là lời giải đúng.

**Provider** là bên cung cấp dịch vụ truy cập đến model trên đường truy cập đang xét: tiếp nhận yêu cầu, xác thực và áp dụng các điều kiện sử dụng. Provider có thể trực tiếp vận hành model hoặc đóng vai trò trung gian. **Producer** là bên xây dựng, huấn luyện hoặc phát hành model. Hai vai trò này có thể thuộc cùng một tổ chức nhưng không bắt buộc.

**Application** (ứng dụng) là nơi người dùng thao tác: trang chat, ứng dụng trên điện thoại hoặc máy tính, hay trợ lý lập trình. Ứng dụng tổ chức lịch sử trao đổi, chọn thông tin gửi đi, có thể kết nối với công cụ hoặc chức năng tìm kiếm, và hiển thị các bản sửa. **User** (người dùng) đặt mục tiêu, quyết định dữ liệu nào được phép gửi và kiểm tra phần kết quả được đem ra sử dụng.

| Vai trò | Câu hỏi phải trả lời | Cách ghi nếu thiếu bằng chứng |
| --- | --- | --- |
| Model | Thành phần nào tạo đầu ra? Định danh nào được công bố? | Chỉ biết họ model; chưa xác định phiên bản hoặc model của từng lượt |
| Provider | Ai cung cấp đường truy cập đến model cho ứng dụng? | Chưa xác định provider của đường truy cập |
| Application | Người dùng đang mở và thao tác ở phần mềm nào? | Ghi tên quan sát được, không suy ra model từ tên ứng dụng |
| Producer | Ai phát triển hoặc phát hành model? | Chưa đủ dữ kiện; không gán cho nhóm viết giao diện |
| User | Ai giao việc và kiểm tra trước khi dùng kết quả? | Minh hoặc Lan trong tình huống này |

![Sơ đồ vai trò model, provider, application và user; mũi tên biểu diễn đường truy cập, không phải quyền sở hữu.](../assets/roles.svg)

*Bản đồ vai trò (AI Map). Một tổ chức có thể đảm nhận nhiều vai trò; mỗi ô không nhất thiết tương ứng với một công ty hay một máy chủ riêng. Producer là câu hỏi bổ sung về bên phát triển, không phải một tầng bắt buộc trong mọi request.*

Một ví dụ điển hình là **Claude qua Amazon Bedrock**: Anthropic là bên phát triển Claude, còn AWS cung cấp đường truy cập qua Bedrock trong tình huống đó. Vì vậy, nhãn "hỗ trợ Claude" trên một ứng dụng không tự chứng minh rằng ứng dụng kết nối trực tiếp tới Anthropic. Căn cứ là tài liệu chính thức của Anthropic và AWS, liệt kê ở phần Tài liệu tham khảo cuối chương. *Chưa kiểm chứng:* các thông tin dịch vụ này được ghi nhận theo mốc 29/10/2026, chưa được xác minh độc lập và cần tra lại khi áp dụng.

Tương tự, tên Gemini có thể được nhắc tới ở lớp ứng dụng hoặc ở họ model. Các cụm "mở ứng dụng Gemini", "gọi Gemini API" và "chọn một model thuộc họ Gemini" không đồng nghĩa với nhau. Điều quan trọng không phải là thuộc hết các tên gọi, mà là đặt mỗi tên vào đúng vai trò của nó.

### API và key không phải một bộ não tải về máy

**API** (*application programming interface*) là giao diện để các phần mềm giao tiếp với nhau theo những quy tắc xác định. Khi dùng ứng dụng chat, Minh gõ câu hỏi và gửi đi. Khi dùng API, chương trình chuẩn bị request theo định dạng mà dịch vụ quy định; request có thể chỉ định model cần dùng. API không phải một model mới và cũng không chỉ dùng cho AI.

**API key** là một dạng thông tin xác thực để dịch vụ nhận biết quyền truy cập; một số dịch vụ dùng cơ chế xác thực khác. Có key không có nghĩa là sở hữu model, được dùng mọi phiên bản, có quota vô hạn hoặc được miễn phí. Quyền truy cập và hóa đơn còn phụ thuộc vào tài khoản, dự án và điều kiện dịch vụ.

> **Cảnh báo an toàn — Khóa không phải dữ liệu thực hành.** Không đưa key thật vào chat, ảnh chụp màn hình, nhóm lớp hoặc kho mã công khai. Không nhúng khóa bí mật vào JavaScript chạy phía trình duyệt, vì mã được gửi đến người dùng có thể bị đọc. ViSinhVien không cần key; không tạo bí mật chỉ để hoàn thành bài nhập môn.

Khi gặp key trong một bài hướng dẫn, cần dùng giá trị giữ chỗ (placeholder) thay vì sao chép khóa thật. Nếu nghi ngờ khóa đã bị lộ, trước hết phải thu hồi hoặc vô hiệu hóa khóa qua dịch vụ, sau đó kiểm tra mức sử dụng và xử lý các bản sao. Xóa một dòng khỏi phiên bản mới nhất của tệp không làm các bản sao trước đó biến mất. Quy trình xử lý sự cố đầy đủ được trình bày ở Hồ sơ 01 (mục 4.1) trong **Chương 4 · Sử dụng AI có trách nhiệm**.

### Các đường truy cập AI không phải các bậc thang thứ hạng

![Bản đồ các cách truy cập AI qua ứng dụng chat, trợ lý lập trình, chương trình dùng API hoặc mô hình cục bộ; không xếp hạng thương hiệu.](../assets/ecosystem.svg)

*Bản đồ đường truy cập (AI Map). Đường truy cập được chọn theo nhiệm vụ và điều kiện sử dụng; API hay agent không mặc nhiên là cấp học cao hơn chat.*

Một luồng xử lý giản lược gồm các bước: **người dùng → ứng dụng chuẩn bị thông tin → provider tiếp nhận → model tạo đầu ra → ứng dụng hiển thị → người dùng kiểm tra**. Hệ thống thực tế có thể có thêm trung gian, công cụ và nhiều lượt xử lý. Model chạy cục bộ có thể không cần provider bên ngoài tiếp nhận câu hỏi. Ngược lại, một ứng dụng cài trên máy vẫn có thể gửi dữ liệu lên đám mây.

Ứng dụng đôi khi được gọi là **wrapper**, tức phần mềm bao quanh model hoặc API. Cách nói "chỉ là cái vỏ" bỏ qua giá trị của việc chọn đúng tệp, giữ phạm vi công việc và cho người học duyệt từng thay đổi. Ngược lại, cũng không thể suy ra rằng mọi wrapper đều đọc được dự án, chạy được mã hay tìm kiếm được trên web. Chẳng hạn, khi dùng Qoder, cần phân biệt Qoder IDE, Qoder Desktop và Qoder CLI; các sản phẩm cùng họ tên không chứng tỏ chúng có cùng giao diện, quyền hạn hay quy trình. *Chưa kiểm chứng:* thông tin này dựa trên tài liệu sản phẩm Qoder theo mốc 29/10/2026, chưa được xác minh độc lập và cần tra lại; chi tiết được trình bày ở mục 2.1 của Chương 2.

### Cùng câu hỏi không đồng nghĩa với cùng đầu vào

Ba thẻ hư cấu không cho biết nguyên nhân của sự khác biệt. Trong hệ thống thực, cùng một câu gõ vào có thể được gửi kèm lịch sử, tài liệu, chỉ dẫn hệ thống hoặc công cụ khác nhau. Một ứng dụng có thể được cấu hình để đóng vai gia sư, ứng dụng khác lại ưu tiên sinh mã. Giới hạn độ dài đầu ra, các tham số cấu hình và tính không tất định của quá trình sinh cũng ảnh hưởng đến kết quả.

Minh điều tra theo ba bước: **ghi nhãn ứng dụng, chế độ và model → liệt kê context và công cụ → ghi rõ phần chưa biết**. Nếu giao diện chỉ hiển thị nhãn "Tự động", Minh chỉ được phép ghi "chưa xác định model thực sự xử lý lượt này". Lời tự giới thiệu của chatbot không đủ làm bằng chứng duy nhất. Sang Chương 2, khái niệm "chế độ" sẽ được cụ thể hóa thành chế độ Ask (chỉ đọc và trả lời) và chế độ Agent (được sửa tệp và chạy lệnh); "context" khi đó được gọi là ngữ cảnh.

**Bài tập: nhận diện trên giấy.** Một ứng dụng giả định có tên "Gia sư ViSinhVien" tự mô tả là dùng Gemini API nhưng không công bố model cụ thể. Hãy điền bốn vai trò. Sau đó, thay phần mô tả bằng cụm "hỗ trợ Claude" và xác định thông tin nào không còn biết được.

### Đáp án nhận diện — Giữ chỗ trống đúng chỗ

Application là Gia sư ViSinhVien. Theo mô tả của chính ứng dụng, đường truy cập là Gemini API: nếu ứng dụng gọi trực tiếp thì provider là Google, nhưng ứng dụng cũng có thể đi qua một trung gian, nên cần ghi "provider theo tự mô tả, chưa xác minh". Về model, chỉ biết họ Gemini, chưa biết model cụ thể. Nhóm viết ứng dụng không vì thế mà trở thành bên huấn luyện model. Nếu mô tả chỉ còn "hỗ trợ Claude", cả provider lẫn phiên bản model đều chưa xác định. Khi thiếu bằng chứng, cần giữ nguyên chỗ trống.

## 1.3. Phía sau một câu trả lời: prompt, context và token (Behind the Scene)

### Prompt là lời giao việc; context là thông tin thực sự được nhận

Trong tình huống minh họa, Lan từng yêu cầu: "Làm app ví sinh viên chuyên nghiệp". Câu trả lời giả định nhận được đề xuất thêm đăng nhập, máy chủ và đồng bộ thanh toán. Đề xuất nghe có vẻ đầy đủ nhưng sai phạm vi bài tập. Minh thì viết "sửa vòng lặp này" nhưng quên dán mã. Cả hai trường hợp đều kỳ vọng hệ thống biết những thông tin chưa được gửi.

**Prompt** là yêu cầu hoặc chỉ dẫn đưa cho hệ thống. **Context** (ngữ cảnh) của một lượt là toàn bộ thông tin mà hệ thống thực sự nhận được: prompt, phần lịch sử được chọn, tài liệu, mã nguồn và kết quả của công cụ. Theo cách dùng phổ biến, prompt là một phần của context. Một tài liệu đang mở trên màn hình của người dùng chưa chắc đã nằm trong context của model.

Có thể cải thiện cách đặt câu hỏi theo trình tự sau, mỗi bước có lý do riêng:

1. **Nêu mục tiêu trước triệu chứng.** Mục tiêu "cộng tất cả khoản hợp lệ" cho biết 42000 có phải là kết quả sai hay không; riêng câu "ra 42000" thì chưa đủ.
2. **Đưa phần mã nhỏ nhưng có liên quan.** Với lỗi về cận vòng lặp, cần khai báo dữ liệu, kiểu của biến tổng và vòng lặp; không cần gửi cả ổ đĩa.
3. **Đặt kết quả mong đợi cạnh hiện tượng quan sát.** Ba khoản phải cho 60000, đoạn mã được dự đoán cho 42000; nếu chưa chạy chương trình, phải ghi rõ đó là dự đoán.
4. **Giữ ràng buộc và giới hạn mức trợ giúp.** Số tiền là số nguyên VND, tối đa 500 khoản, cần gợi ý trước; nhờ vậy tránh nhận về một bản viết lại vượt quá nội dung bài học.
5. **Yêu cầu cách kiểm tra.** Đề nghị nêu test và bằng chứng thay vì chỉ yêu cầu "chắc chắn 100%".

Một prompt tốt cần đủ dữ kiện, không nhất thiết phải dài hoặc dùng nhiều lời tôn xưng. Câu "Hãy đóng vai chuyên gia hàng đầu" không thay thế được mã nguồn và kết quả mong đợi. Ngược lại, lược bỏ hợp đồng dữ liệu để tiết kiệm vài token có thể khiến người dùng mất nhiều lượt trao đổi chỉ để sửa một yêu cầu bị hiểu sai.

### Brief chung: giúp hai người học giữ cùng một bài toán

**Brief** là bản mô tả ngắn gọn công việc cần làm. Minh và Lan giữ một bản brief hiện hành và chỉ thay dòng "việc lần này" ở mỗi lượt, thay vì kể lại dự án theo trí nhớ. Mẫu dưới đây có thể dùng độc lập, với điều kiện dán kèm phần mã liên quan:

```text
DỰ ÁN: ViSinhVien, bài tập chỉ dùng dữ liệu GIẢ.
NGƯỜI HỌC: Minh năm 1 học C++; Lan năm 2 học OOP/DSA/CSDL/Web.
MỤC TIÊU: lưu danh sách khoản chi và tính tổng mọi khoản hợp lệ.
DỮ LIỆU CHUNG: mỗi khoản có tên; amount là số nguyên VND.
Nhánh C++ chỉ lưu phần tiền, không lưu tên khoản trong vector.
HỢP ĐỒNG: 0 < amount <= 1000000000; tối đa 500 khoản.
DANH SÁCH RỖNG: hợp lệ, tổng bằng 0; không tạo khoản amount = 0.
MẪU GIẢ: Cơm trưa 35000; Xe buýt 7000; Vở ghi 18000.
KỲ VỌNG: tổng 60000 VND; snippet lỗi bỏ khoản cuối cho 42000.
C++: vector<long long> chỉ mô hình phần tiền; tổng tối đa 500000000000.
WEB: Expense có id, title, amount, category; HTML + JS + localStorage.
PHẠM VI: không backend, đăng nhập, ngân hàng, API AI hoặc dữ liệu thật.
VIỆC LẦN NÀY: đọc snippet đính kèm, tìm nguyên nhân bỏ khoản cuối.
CÁCH GIÚP: gợi ý một bước trước, chưa viết lại chương trình.
NẾU THIẾU: chỉ ra thông tin cần bổ sung, không tự thêm tính năng.
ĐẦU RA: vị trí nghi vấn, giải thích vừa sức, test và kết quả mong đợi.
BẰNG CHỨNG: phân biệt suy luận, kỳ vọng và kết quả đã thực thi.
```

Khi học vòng lặp, Minh chỉ cần mô hình hóa phần tiền bằng `vector<long long>`; tên ba khoản ghi trên giấy giúp hiểu ý nghĩa của dữ liệu. Phiên bản Web của Lan dùng cấu trúc `Expense{id,title,amount,category}`, trong đó `id` phân biệt các khoản giả, `title` là tên hiển thị, `amount` là số tiền và `category` là nhóm chi tiêu. Trường `id` không phải mã sinh viên. Mảng tiền trong C++ không tự trở thành mô hình đầy đủ bốn trường như ở phiên bản Web.

Về góc độ OOP, điểm cần học là phân biệt trách nhiệm lưu dữ liệu, xác thực và tính tổng; không bắt buộc thêm một lớp chỉ để chương trình có dáng "hướng đối tượng". Về DSA, phép duyệt tính tổng một lần có độ phức tạp thời gian O(n), bộ nhớ phụ cho biến tổng là O(1). Về CSDL, Lan có thể phân tích thuộc tính và ràng buộc trên giấy. Việc thay đổi góc nhìn học tập không cho phép tự đưa máy chủ hay cơ sở dữ liệu vào phiên bản Web; ví dụ minh họa SQLite `:memory:` trong `vi-du/minh-hoa-sqlite.py` (mục 4.8.1 của Chương 4) là một bài riêng.

### Hợp đồng dữ liệu: bằng chứng bắt đầu từ trước khi chạy chương trình

**Hợp đồng dữ liệu** quy định đầu vào nào được chấp nhận và đầu ra nào được yêu cầu. Trong bài này, mỗi khoản chi tồn tại phải có `amount` là số nguyên, lớn hơn 0 và không quá 1000000000; danh sách có tối đa 500 khoản. Danh sách rỗng vẫn hợp lệ, vì không có khoản nào vi phạm điều kiện. Tổng bằng 0 không đồng nghĩa với việc có một khoản chi bằng 0.

Từ hợp đồng, có thể tính được tổng lớn nhất:

```text
500 × 1000000000 = 500000000000 VND
```

Trong C++, kiểu dữ liệu được chọn phải chứa được giá trị đó. Kiểu số nguyên có dấu 32 bit thường gặp chỉ đạt khoảng 2,1 tỷ, không đủ chứa 500 tỷ. Vì vậy, đoạn mã dùng `long long` cho số tiền và biến tổng. Không nên suy ra rằng kiểu `int` có cùng kích thước trên mọi hệ thống; lý do lựa chọn kiểu là miền giá trị của dữ liệu, không phải nhãn "tối ưu" do AI gắn vào.

Trong JavaScript, kiểu `Number` biểu diễn chính xác các số nguyên trong miền **số nguyên an toàn** (*safe integers*), từ `-9007199254740991` đến `9007199254740991`. Tổng 500000000000 nằm trong miền này. Vì từng khoản đều là số nguyên và mọi tổng trung gian không vượt trần đang xét, phép cộng của bài là chính xác. Ngoài miền an toàn, việc biểu diễn riêng biệt từng số nguyên không còn được bảo đảm.

Điều này **không** có nghĩa là "dùng Number thì dữ liệu tự hợp lệ". Giá trị `amount` vẫn phải thỏa `Number.isSafeInteger(amount)` như trong `data.js`, đồng thời lớn hơn 0 và không quá 1000000000. Chuỗi `"7000"` không phải là số 7000. Ô nhập trên trang Web có thể trả về chuỗi; dữ liệu trong `localStorage` cũng được lưu dưới dạng chuỗi, nên cần phân tích và kiểm tra cấu trúc khi đọc lại. Chỉ kiểm tra ở giao diện nhập liệu không bảo vệ được mọi dữ liệu đã lưu.

Bảng dưới đây là **kết quả mong đợi theo hợp đồng, chưa phải kết quả đã chạy**:

| Ca kiểm tra | Dữ liệu hoặc thao tác giả | Kết quả mong đợi |
| --- | --- | --- |
| Rỗng | Không có khoản nào | Tổng 0 VND |
| Một khoản | 7000 | Tổng 7000 VND |
| Ba khoản mẫu | 35000, 7000, 18000 | Tổng 60000 VND |
| Chạm trần | 500 khoản, mỗi khoản 1000000000 | Tổng 500000000000 VND |
| Sai giá trị | 0, số âm, 1.5 hoặc lớn hơn 1000000000 | Từ chối khoản sai, không âm thầm làm tròn |
| Vượt số lượng | Thêm khoản thứ 501 | Từ chối thêm, giữ nguyên danh sách hợp lệ trước đó |

Ba ca đầu kiểm tra một phần hành vi tính tổng. Ba ca sau đòi hỏi thêm chức năng xác thực dữ liệu (validation). **Sửa cận vòng lặp không tự giải quyết được việc xác thực.** Nếu đoạn mã chỉ cộng dữ liệu đã hợp lệ, cần nêu rõ giới hạn đó thay vì tuyên bố rằng nó đáp ứng toàn bộ bảng.

### Token và context window: không phải số từ, cũng không phải trí nhớ vô hạn

**Token** là đơn vị dữ liệu mà hệ thống xử lý. Một từ có thể được tách thành nhiều token; dấu câu, khoảng trắng, mã nguồn, ngôn ngữ và bộ tách token (*tokenizer*) đều ảnh hưởng đến số lượng. Không tồn tại quy tắc "một từ tiếng Việt bằng một token". Đếm số từ theo khoảng trắng không cho phép biết chính xác số token; việc quy token thành chi phí được trình bày ở Chương 5 (mục 5.1).

![Các khối dữ liệu minh họa token và vùng context hữu hạn; cách chia khối không phải kết quả của tokenizer thật.](../assets/token-context.svg)

*Phía sau một câu trả lời (Behind the Scene). Các khối chỉ minh họa việc chia và chọn thông tin, không phản ánh số token thật. Context không phải toàn bộ ổ đĩa.*

**Context window** (cửa sổ ngữ cảnh) là giới hạn lượng thông tin được xử lý trong một lần, do từng dịch vụ quy định; thường còn có giới hạn riêng cho đầu ra. Cửa sổ lớn không bảo đảm mọi chi tiết đều được sử dụng chính xác, cũng không cho phép gửi thông tin vô hạn.

Trong tình huống minh họa, Lan dán toàn bộ lịch sử trao đổi, gồm cả yêu cầu backend đã bị loại bỏ và nhiều đoạn log thừa. Kết quả là bản brief hiện hành bị chìm giữa các thông tin không còn hiệu lực. Ngoài ra, một cuộc hội thoại dài có thể bị ứng dụng cắt bớt, tóm tắt hoặc chọn lọc lại; việc "đã nói từ đầu" không bảo đảm thông tin đó còn nguyên trong context.

Cách làm phù hợp là giữ bản brief hiện hành, hàm liên quan, dữ liệu giả và ghi chú về phần đã thay đổi. Model không tự biết tệp vừa được sửa nếu chưa nhận được phiên bản mới. Trợ lý được cấp quyền đọc dự án có thể tự lấy thêm nội dung; khi đó cần kiểm tra quyền và các tệp thực sự được sử dụng, không đoán qua giao diện.

**Bài tập: chọn context.** Với lỗi 42000, hãy chọn trong các thành phần sau: bản brief, hàm tính tổng, ba khoản giả, một bản sao kê ngân hàng thật và một bài giảng không liên quan. Giải thích lý do loại bỏ từng phần bị loại.

### Đáp án chọn context — Đủ để kiểm tra, không đủ để lộ dữ liệu

Chọn bản brief, hàm tính tổng cùng các khai báo cần để hiểu hàm, và ba khoản giả. Loại sao kê vì lý do riêng tư, loại bài giảng không liên quan vì gây nhiễu. Nếu thiếu kiểu dữ liệu hoặc đoạn mã gọi hàm, chỉ bổ sung đúng phần đó, không gửi cả ổ đĩa.

### Training, inference và web search: ba hoạt động không thay thế nhau

**Huấn luyện** (*training*) là quá trình dùng dữ liệu và thuật toán để điều chỉnh tham số của model. **Suy luận** (*inference*), theo nghĩa vận hành được dùng ở đây, là việc dùng model đã có để tạo đầu ra từ đầu vào. Khi Minh gửi ba khoản chi, hệ thống có thể dùng chúng trong context của lượt đó; điều này không tự chứng minh rằng model vừa được huấn luyện lại và sẽ nhớ ba khoản ấy cho mọi người dùng.

Tuy nhiên, "không huấn luyện lại ngay" cũng không đồng nghĩa với "không lưu dữ liệu". Lịch sử chat, bộ nhớ của ứng dụng, log vận hành và việc dùng nội dung để cải thiện dịch vụ là những vấn đề khác nhau. Cần đọc chính sách và kiểm tra cài đặt của đúng sản phẩm đang dùng. Hiểu biết về inference không thay thế được việc kiểm tra quyền riêng tư.

**Tìm kiếm web** (*web search*) là việc truy xuất thông tin qua công cụ kết nối Internet, nếu sản phẩm có công cụ này và lượt trao đổi đó thực sự sử dụng nó. Câu hỏi về một thông tin thay đổi theo ngày không tự kích hoạt tìm kiếm web; câu trả lời có thể chỉ dựa trên kiến thức cũ. Ngược lại, có tìm kiếm cũng chưa bảo đảm nguồn phù hợp hoặc nội dung được tóm tắt đúng.

Với ba khoản tiền, phép cộng và việc kiểm tra mã là căn cứ phù hợp. Với điều kiện sử dụng của một dịch vụ, căn cứ phải là điều khoản chính thức đang còn hiệu lực. Minh không cần tìm kiếm web để cộng ra 60000; Lan không thể dùng một suy luận nghe có vẻ hợp lý để thay cho điều khoản của dịch vụ.

### Hallucination và trích dẫn: chuyển sự tự tin thành câu hỏi kiểm chứng

**Hallucination**, thường gọi là ảo giác AI, là hiện tượng nội dung sai hoặc không có căn cứ được trình bày như thể đúng. Một số ví dụ giả định: "JavaScript tự lưu mọi biến vào localStorage", một hàm C++ không tồn tại, hoặc lời khẳng định "đã chạy test" trong khi hệ thống chỉ đọc văn bản. Tên gọi này không giải thích được mọi nguyên nhân gây lỗi, nhưng nhắc người dùng không coi câu chữ là bằng chứng.

Thay vì yêu cầu "đừng sai", Minh hỏi cụ thể: những chỉ số nào được duyệt, ca một khoản cho kết quả gì, và câu nào chỉ là dự đoán. Lan hỏi: tệp nào ghi dữ liệu vào bộ nhớ lưu trữ, khi nào dữ liệu được đọc lại, và dữ liệu JSON hỏng được xử lý ra sao. Nếu công cụ khẳng định đã chạy chương trình, cần có lệnh, dữ liệu, đầu ra, môi trường thực thi và khả năng đối chiếu. Một vài test đạt vẫn không chứng minh chương trình đúng với mọi đầu vào; test cho phần logic JavaScript cũng không tự kiểm chứng phần DOM hay việc lưu và nạp dữ liệu trên trình duyệt.

Với trích dẫn, cần thực hiện lần lượt: **khoanh vùng nhận định → mở nguồn → tìm đoạn hỗ trợ → kiểm tra phạm vi và ngày → ghi giới hạn**. Một liên kết có thật chưa chắc đã hỗ trợ kết luận. "Đủ điều kiện nộp" khác với "chắc chắn được chấp nhận"; điều khoản của API khác với điều khoản của ứng dụng chat. Ngày truy cập không phải là ngày phát hành. Nếu không tìm được căn cứ, cần ghi **chưa xác minh**, không bù đắp bằng một đoạn giải thích tự tin hơn.

## Câu hỏi tự kiểm tra

Trả lời từng câu bằng một kết luận và một lý do. Không chỉ ghi nhớ chữ "không", mà cần chỉ ra loại bằng chứng còn thiếu.

1. Nhãn "tích hợp Claude" đã đủ để xác định provider và phiên bản model chưa?
2. Cùng một model nhưng một ứng dụng lại đề xuất thêm backend cho ViSinhVien: có thể chắc chắn rằng ứng dụng quảng cáo sai không?
3. Danh sách rỗng có vi phạm điều kiện `amount > 0` không? Có cần tạo một khoản bằng 0 để biểu diễn danh sách rỗng không?
4. Đếm số từ tiếng Việt có đủ để biết chính xác số token của một prompt không?
5. Minh nhờ AI viết trọn vòng lặp tính tổng, chép vào bài rồi nộp. Việc này có phù hợp với nguyên tắc "AI hỗ trợ, người học quyết định" không?
6. Một câu trả lời của AI viết rất chắc chắn có thể dùng ngay mà không cần kiểm tra không?

### Đáp án câu hỏi tự kiểm tra — Sáu kết luận và lý do

**1. Chưa.** Cần định danh model và đường truy cập; producer có thể khác provider, như ví dụ Claude qua Amazon Bedrock. Không đoán qua văn phong của câu trả lời.

**2. Chưa thể kết luận ứng dụng quảng cáo sai.** Cần kiểm tra brief thực sự được gửi, lịch sử, chỉ dẫn, công cụ và cấu hình. Đề xuất backend là sai so với phạm vi đã chốt, nhưng đầu ra khác nhau chưa chứng minh model khác nhau.

**3. Không vi phạm và không cần khoản bằng 0.** Điều kiện số dương chỉ áp dụng cho các khoản tồn tại. Danh sách rỗng có tổng 0; việc tạo một khoản `amount = 0` mới là vi phạm hợp đồng.

**4. Không.** Số token phụ thuộc vào tokenizer và nội dung; lượng dùng thực tế có thể gồm cả lịch sử, mã nguồn và kết quả của công cụ. Cần dùng công cụ đếm phù hợp và số liệu do dịch vụ báo cáo, không dùng số đếm từ.

**5. Không phù hợp.** Người học không đặt giới hạn mức trợ giúp, không tự kiểm chứng và không giải thích được mã đã nộp, tức là quyết định thực chất do AI đưa ra. Cách đúng hơn là tự làm bản nháp, xin gợi ý từng bước và tự giải thích vì sao cận `i < n` đúng.

**6. Không.** Độ tự tin của câu chữ không phải bằng chứng; thẻ B ở tình huống mở đầu tự tin nhưng sai. Cần kiểm bằng phép tính, test hoặc nguồn chính thức, và ghi "chưa xác minh" khi chưa có căn cứ.

## Ôn tập: tự trình bày lại trong 5 phút

Người học có thể trình bày trước nhóm học hoặc tự ghi âm, không cần mở giao diện của bất kỳ dịch vụ nào.

| Thời gian | Nội dung trình bày | Điều cần chứng minh |
| --- | --- | --- |
| 0:00–1:00 | Nêu ba vai trò hợp lý của AI; điều AI làm tốt và làm kém | Phân biệt được hỗ trợ với làm thay |
| 1:00–2:00 | Dùng ví dụ 35000, 7000, 18000 để so sánh dùng AI để học và để né học; đọc nguyên tắc "AI hỗ trợ, người học quyết định" | Chỉ ra được dấu hiệu lạm dụng qua hành vi quan sát được |
| 2:00–3:00 | Vẽ sơ đồ application, provider, model; thêm câu hỏi về producer | Không đồng nhất ứng dụng với model; chấp nhận ghi "chưa biết" |
| 3:00–4:00 | Sửa một prompt thiếu thông tin; nhắc hợp đồng dữ liệu và chỉ số cuối | Không đổi sang cận vượt mảng; nêu đúng context cần gửi |
| 4:00–5:00 | Nêu cách kiểm tra mã, cách xử lý một câu trả lời tự tin nhưng chưa có bằng chứng | Nêu được bằng chứng và những điều chưa xác minh |

Nếu có thêm thời gian, bổ sung một tình huống từ bài tập tự đánh giá ở mục 1.1 và giải thích lý do chọn. Không trình diễn thao tác đăng nhập, thanh toán hoặc giấy tờ cá nhân để làm bài trình bày sinh động hơn.

## Tóm tắt chương

Chương 1 thiết lập nền cho các chương sau: AI có vai trò hợp lý trong học tập, có giới hạn rõ ràng, và hoạt động theo những thành phần mà người học cần nhận diện được. Phiếu bài tập của chương là bằng chứng của một buổi học, không phải chứng nhận năng lực lâu dài.

Ba ý chính của chương:

- **AI hỗ trợ, người học quyết định: AI hợp lý khi đóng vai gia sư, người phản biện hoặc trợ lý cho việc lặp; dùng AI để học khác với dùng AI để né học ở chỗ ai đã suy nghĩ và ai kiểm chứng.**
- **Cần biết ứng dụng đang dùng, đường truy cập và model được công bố; khi thiếu chứng cứ, ghi "chưa xác định".**
- **Cần đưa đúng mục tiêu và context, rồi kiểm tra bằng phép tính, test hoặc nguồn; sự tự tin của câu trả lời không phải bằng chứng.**

## Cầu nối sang chương sau

Hiểu vai trò, giới hạn và cách AI hoạt động mới chỉ là bước đầu; điều còn lại là biến hiểu biết đó thành thao tác cụ thể. **Chương 2 · Điều khiển quá trình làm việc với AI** hướng dẫn giao việc rõ, kiểm bằng bằng chứng và nhận thay đổi có chủ đích, qua các bài thực hành mà Minh và Lan cùng thực hiện.

## Tài liệu tham khảo

Các nguồn dưới đây được ghi nhận theo mốc truy cập 29/10/2026. *Chưa kiểm chứng:* nội dung hiện hành của các nguồn chưa được xác minh độc lập; cần tra lại thông tin về model, đường truy cập và API trước khi áp dụng. Các nguồn về giá, ưu đãi sinh viên và thanh toán được liệt kê ở Chương 5.

| Nội dung đối chiếu | Nguồn chính thức |
| --- | --- |
| Họ model, định danh | [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview) |
| Claude qua provider khác | [AWS — Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) |
| API, xác thực, chỉ định model | [Google — Gemini API docs](https://ai.google.dev/gemini-api/docs) |
| Lớp ứng dụng Gemini | [Google — Gemini overview](https://gemini.google/overview/) |

Các thẻ trả lời hư cấu không phải benchmark; các bảng kết quả mong đợi không phải log thực thi. Mọi kiểm chứng thật phải ghi riêng công cụ, lệnh hoặc nguồn đã dùng, ngày thực hiện và kết quả thu được.
