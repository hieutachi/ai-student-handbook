# CHƯƠNG 2 · ĐIỀU KHIỂN QUÁ TRÌNH LÀM VIỆC VỚI AI

Chương 1 đã làm rõ vai trò của AI trong học tập và cho thấy một câu trả lời được tạo ra từ prompt, context và token, nên không thể chấp nhận nó chỉ vì được trình bày tự tin. Chương 2 là bước **Dùng** trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn: dùng AI như một công cụ có kiểm soát. Ba câu hỏi xuyên suốt là việc gì cần làm, công cụ được phép làm đến đâu, và bằng chứng nào đủ để chấp nhận kết quả. Minh, Lan, các hội thoại và ba khoản chi trong chương là *tình huống hư cấu* với *dữ liệu giả định*; kết quả chạy chương trình nêu trong chương là *kết quả mong đợi* suy ra từ mã.

**Sau chương này, người học có thể:**

- Mở đúng thư mục làm việc, biết shell đang dùng và hỏi AI ở chế độ chỉ đọc trước khi cho phép sửa.
- Lập bảng trace để chỉ ra lượt lặp bị bỏ sót và giải thích vì sao tổng là 42000 thay vì 60000.
- Lần theo một giá trị từ ô nhập trên Web đến hàm tính tổng và nơi lưu; phân biệt chuỗi, số, `undefined` và `NaN`.
- Giao việc cho Agent trong phạm vi hẹp, đọc diff trước khi chấp nhận và nghiệm thu bằng bằng chứng thay vì bằng lời hứa.

## Tình huống mở đầu

Chương trình C++ của Minh in ra **42000**, trong khi ba khoản chi Cơm trưa 35000, Xe buýt 7000 và Vở ghi 18000 cộng trên giấy được **60000**. Lan có bản Web của cùng ứng dụng ViSinhVien với tổng đúng, nhưng khi thử nhập `35000abc`, Lan cần biết chương trình từ chối giá trị này ở đâu. Cùng lúc, một trợ lý AI đề nghị cài thêm thư viện để "xử lý tiền chuyên nghiệp". Ba việc này cần ba mức quyền và ba loại bằng chứng khác nhau.

Hợp đồng dữ liệu chung cho cả hai nhánh: mỗi khoản là số nguyên từ 1 đến 1000000000, tối đa 500 khoản, danh sách rỗng có tổng 0. Người học chọn một nhánh (C++ của Minh hoặc Web của Lan) để làm sâu, nhưng vẫn cần giải thích được lỗi trọng tâm của nhánh còn lại. Không nhập thông tin sinh viên thật hay bất kỳ bí mật nào vào mã nguồn hoặc hội thoại với AI.

## 2.1. Chuẩn bị môi trường và hỏi trước khi cho phép sửa

Mục này giúp người học biết đang đứng ở đâu, dùng công cụ nào, rồi đặt một câu hỏi mà AI chỉ được đọc và giải thích. Hai việc nhỏ ấy ngăn phần lớn lỗi "sửa nhầm tệp" trước khi chúng kịp xảy ra.

### Ý chính

Minh gọi chung vùng soạn mã, khung hội thoại và cửa sổ lệnh là "AI". Cần tách chúng ra. **Editor** là nơi soạn tệp. **IDE** gom editor, cây tệp, tìm kiếm và terminal vào một cửa sổ. **Terminal** chỉ hiển thị văn bản; **shell** (Bash hoặc PowerShell) là chương trình diễn giải lệnh chạy bên trong terminal; **CLI** là chương trình được gọi, như `g++` hoặc `node`. **Agent** là AI được gắn công cụ: nó có thể đọc, sửa tệp và chạy lệnh tùy theo sản phẩm, chế độ và quyền được cấp. Khi gõ `g++ --version` mà shell báo không tìm thấy lệnh, vấn đề nằm ở môi trường, chưa phải ở vòng lặp C++. Việc đã cài IDE cũng không chứng minh máy đã có compiler.

![Khung IDE chứa cây tệp, editor và terminal. Trong terminal, shell nhận python --version và gọi CLI Python. AI hoặc Agent ở ngoài ranh giới quyền đọc, sửa, chạy lệnh.](../assets/workspace.svg)

Hai thứ cần đọc được ngay là **thư mục hiện hành** (current working directory, viết tắt cwd) và **tên shell**. Trong chương, cwd luôn là thư mục gốc `AI-Student-Handbook`; bài làm nằm trong `bai-lam/`, còn `vi-du/` chỉ để đối chiếu, không sửa. Bash xem cwd bằng `pwd`, PowerShell bằng `Get-Location`. Cùng một máy Windows có thể mở cả hai shell, nên hệ điều hành không quyết định cú pháp; shell đang mở mới quyết định. Terminal mở từ trước có thể đang đứng ở nơi khác thư mục IDE đang mở, vì vậy cần kiểm tra vị trí trước khi chạy bất kỳ lệnh nào.

Khi đã biết vị trí, hãy hỏi trước khi cho phép sửa. Trong Qoder IDE, chế độ **Ask** đọc hiểu và gợi ý đoạn mã nhưng không tự sửa tệp; chế độ **Agent** mới được sửa và chạy lệnh theo quyền. Dùng `@` để đưa đúng tệp cần đọc vào ngữ cảnh: Minh bắt đầu với `loi-bo-sot.cpp`, Lan với `app.js` và `data.js`. Ngữ cảnh nhỏ không có nghĩa là cắt bỏ khai báo kiểu hay dữ liệu đầu vào. Một câu hỏi tốt tách bốn thành phần: đầu vào, điều mong muốn, điều quan sát được và đoạn mã liên quan. Câu "quan sát thấy 42000 với ba khoản" là dữ kiện; câu "chắc chắn compiler cộng sai" là một giả thuyết yếu. Chưa chạy chương trình thì ghi "dự đoán từ mã" thay cho "quan sát".

Câu trả lời của AI chỉ là đề xuất cho tới khi người học mở lại từng vị trí nó dẫn ra. Lan hỏi về luồng submit của bản Web; nếu AI bịa ra hàm `handleSubmit`, cần sửa mô tả thành "handler vô danh gắn vào sự kiện submit", không sửa mã cho khớp với câu trả lời. Một đoạn mã xuất hiện trong hội thoại cũng chưa có nghĩa là tệp đã thay đổi. Prompt không thay cho hàng rào quyền: chế độ, cấu hình và bước phê duyệt mới quyết định công cụ được phép làm gì. Chế độ chỉ đọc cũng không biện minh cho việc đưa dữ liệu nhạy cảm vào ngữ cảnh; chương chỉ dùng ba khoản chi giả định. Nếu giao diện khác với mô tả, cần kiểm tra sản phẩm và phiên bản thay vì chọn một chế độ có quyền rộng hơn.

### Thử ngay (10 phút)

Mục tiêu: có thư mục bài làm và một câu hỏi chỉ đọc. Việc cụ thể: tạo `bai-lam/` với hai thư mục con `nam-1-cpp` và `nam-2-web`; sao chép **nội dung** một nhánh từ `vi-du/` sang (tránh tầng lồng `nam-1-cpp/nam-1-cpp`); tạo `ghi-chep-02.txt` trong nhánh đang học. Mở terminal, ghi vào tệp đó tên shell và cwd. Sau cùng viết một câu hỏi cho AI theo bốn thành phần ở trên, mở đầu bằng "Chỉ giải thích, chưa sửa, chưa chạy lệnh". Chưa cần gửi; chỉ cần viết ra.

### Gợi ý đối chiếu

Cây thư mục có đúng ba tầng `AI-Student-Handbook/bai-lam/nam-1-cpp`? Tệp ghi chép nêu tên shell, cwd và không mang đuôi `.txt.txt`? Câu hỏi có đủ đầu vào, điều mong muốn, điều quan sát (hoặc dự đoán) và đoạn mã, và nói rõ AI chưa được sửa gì?

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Giải thích toán tử `+=` và tìm hàm mà `app.js` gọi trong `data.js` có cần cùng một mức quyền không? Nếu AI chỉ đọc `data.js` rồi kết luận "nút Thêm đã gắn đúng sự kiện", kết luận đó đã đủ bằng chứng chưa?
- **Từ khóa tra cứu:** current working directory, shell và terminal, Ask mode, read-only prompt.
- **Trong Sổ tay thực hành:** [Bài thực hành 01](../chapters/chapter-02.md#muc-2-1) có bảng lệnh Bash và PowerShell, cấu trúc thư mục đầy đủ và prompt mẫu; [Bài thực hành 02](../chapters/chapter-02.md#muc-2-2) có hai prompt chỉ đọc cho nhánh C++ và Web cùng đáp án câu hỏi kiểm tra.

## 2.2. Gỡ lỗi bằng bảng trace: khoản 18000 bị bỏ sót

Mục này giúp người học tự tìm nguyên nhân của con số 42000 bằng cách đóng vai máy tính trên giấy, rồi mới nhờ AI kiểm lại. Hãy dùng mô phỏng trace ngay dưới tiêu đề này để xem từng lượt lặp trước khi đọc tiếp; mỗi lượt trong mô phỏng tương ứng với một dòng của bảng ở phần "Thử ngay".

### Ý chính

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

![Trace n=3, total=0, cận i<n-1: i=0 cộng 35000; i=1 cộng 7000 thành 42000; i=2 không thỏa 2<2, bỏ 18000. Kỳ vọng 60000; sửa cận i<n, validation là bước riêng.](../assets/debugging.svg)

Bản vá đúng là `i < n`, không phải `i <= n` (truy cập chỉ số `n` nằm ngoài vector là hành vi không xác định) và cũng không phải cộng bù `amounts[n - 1]` sau vòng lặp (che nguyên nhân, lại hỏng với danh sách rỗng). Ca danh sách rỗng trả 0 ở cả hai phiên bản nên không phân biệt được chúng; ca một khoản `[7000]` thì có: bản sai trả 0, bản đúng trả 7000. Sửa cận xong, tổng ra 60000 nhưng validation vẫn chưa có: `-1` vừa với `long long` mà không phải khoản chi hợp lệ. Đó là một trách nhiệm riêng, không tự xuất hiện khi đổi cận. Khi có compiler, nhớ rằng thông báo lỗi đầu tiên mới là nơi cần đọc, và sau mỗi lần sửa phải lưu tệp rồi biên dịch lại: nếu lần build thất bại mà executable cũ vẫn còn, chạy tệp đó có thể in 60000 dù mã vừa sửa chưa hợp lệ.

### Thử ngay (10 phút)

Mục tiêu: tự tạo bằng chứng trước khi hỏi AI. Trên giấy hoặc trong `ghi-chep-02.txt`, kẻ bảng bốn cột: `i`, điều kiện, khoản được cộng, tổng sau bước. Điền ba lượt cho `n = 3` với điều kiện lỗi `i < n - 1`, kể cả lượt làm vòng lặp dừng. Sau đó lập thêm hai bảng ngắn cho danh sách rỗng và danh sách chỉ có `7000`. Ghi lại ca nào phân biệt được bản sai với bản đúng. Nếu muốn, dán bảng vào một câu hỏi chỉ đọc để AI kiểm tra bảng, không phải để AI lập hộ.

### Gợi ý đối chiếu

Bảng ba khoản có đúng một lượt với điều kiện sai làm dừng vòng lặp? Tổng sau lượt cuối được cộng là 42000? Bảng rỗng cho 0 ở cả hai phiên bản, còn bảng `[7000]` cho hai kết quả khác nhau? Bản vá đề xuất chỉ đổi phần cận trong điều kiện, không thêm phép cộng bù?

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu khai báo `long long& alias = total;` rồi thực hiện `alias += 35000`, biến `total` có thay đổi không, và một bản sao `copied` thì sao? Khi compiler báo `expected ',' or ';' before 'for'` và chỉ vào dòng `for`, nguyên nhân thật nằm ở đâu?
- **Từ khóa tra cứu:** off-by-one error, unsigned wraparound, undefined behavior, reference và copy.
- **Trong Sổ tay thực hành:** [Bài thực hành 03](../chapters/chapter-02.md#muc-2-3) có bảng trace đầy đủ cho cả hai phiên bản, bài trace tham chiếu, cách đọc lỗi thiếu dấu chấm phẩy và hướng dẫn tách validation.

## 2.3. Lần theo dữ liệu trên Web: chuỗi trông giống số chưa phải số

Mục này giúp người học theo dõi một giá trị từ ô nhập đến nơi lưu trên bản Web của Lan, để nhận ra chỗ dữ liệu đổi kiểu hoặc bị từ chối. Bản Web đang chạy đúng; bài học ở đây là hiểu cơ chế, không phải tìm chỗ hỏng.

### Ý chính

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

### Thử ngay (10 phút)

Mục tiêu: dự đoán rồi mới chạy. Trước khi mở Console, viết ra ba dòng dự đoán cho đoạn mã trên: giá trị `wrong`, kết quả `Number.isNaN(wrong)` và giá trị `correct`. Sau đó mở `index.html` trong trình duyệt, ghi lại tổng ban đầu, dán đoạn mã vào Console và so với dự đoán. Tiếp theo, trên form, nhập tên giả hợp lệ, chọn nhóm, số tiền `35000abc` và gửi; ghi lại thông báo, tổng và số khoản sau thao tác. Không có trình duyệt thì chỉ làm phần dự đoán và ghi "chưa chạy".

### Gợi ý đối chiếu

Dự đoán nêu đúng hai giá trị `undefined` và `NaN` ở đúng chỗ, không coi chúng là một? Tổng sau khi gửi `35000abc` bằng tổng trước thao tác? Phần ghi chép tách rõ "kiểm hàm trực tiếp trong Console" với "kiểm qua form", vì đó là hai bằng chứng khác nhau?

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nút Khôi phục mẫu có bật lại khả năng lưu khi `persistent` đã là false không? Vì sao `category: ['khac']` từng lọt qua một cách kiểm tra, và ca kiểm thử nào giữ cho lỗi ấy không quay lại?
- **Từ khóa tra cứu:** input.value string, NaN và undefined, Number.isSafeInteger, localStorage file://.
- **Trong Sổ tay thực hành:** [Bài thực hành 04](../chapters/chapter-02.md#muc-2-4) có bảng luồng dữ liệu bảy chặng, hai đoạn Console dùng API thật của trang, giải thích ca hồi quy category mảng và cơ chế dự phòng khi lưu.

## 2.4. Giao việc có giới hạn, đọc diff và nghiệm thu

Mục này giúp người học chuyển từ "hỏi" sang "giao việc" mà không mất quyền kiểm soát: viết hợp đồng giao việc, đọc từng dòng thay đổi trước khi chấp nhận, và kết luận đúng phạm vi đã kiểm tra.

### Ý chính

Một lượt làm việc có kiểm soát đi qua năm bước **Observe → Plan → Act → Test → Review**: quan sát mã, dữ liệu và lỗi; nêu giả thuyết, tệp dự kiến đổi và phép thử; thực hiện thay đổi đã được phép; kiểm bằng ca thường và ca biên; rồi rà soát diff và bằng chứng để quyết định nhận hay từ chối. Với tình huống 42000: Observe đọc vector và `i < n - 1`; Plan dự đoán ca rỗng, một khoản, ba khoản; Act đổi thành `i < n` đúng tệp bài làm; Test biên dịch rồi chạy đúng executable; Review so yêu cầu, diff và kết quả. Chỉ chuyển từ Ask sang Agent khi đã mô tả được lỗi, biết tệp nào sẽ đổi và đã có dự đoán. Test sai thì quay lại Observe với dữ kiện mới, không đổi mã ngẫu nhiên cho tới khi màn hình báo đạt.

![Ask sang Analyze, Edit, Test, Review. Test sai quay lại Analyze; đổi yêu cầu hoặc phát hiện thiếu sau review quay lại Ask.](../assets/workflow.svg)

Hợp đồng giao việc nêu rõ tệp duy nhất được sửa, mục tiêu hẹp, điểm dừng ("chỉ Observe và Plan; chưa sửa") và những việc cấm: không cài dependency, không đổi cấu hình hay quyền, không chạm `vi-du`. Khi Agent đề nghị cài một gói "xử lý tiền chuyên nghiệp", câu hỏi của Lan là đúng: API hiện có thiếu ở điểm nào? Bản Web thuần chỉ dùng API trình duyệt, bộ test dùng `node:assert/strict` có sẵn trong Node.js; không bài nào cần `npm install`. Chưa kiểm tra tên gói, nhà phát hành, kho mã, phiên bản và giấy phép thì ghi "dependency chưa xác minh"; không cài thử để xem, cũng không gọi gói là độc hại chỉ vì lạ.

**Diff** là danh sách dòng bị bỏ và dòng được thêm giữa hai trạng thái của tệp. Trước khi sửa, tạo checkpoint bằng cách sao chép tệp bài làm vào `bai-lam/checkpoints/moc-01-truoc-can/`; đó là đường quay lại. Mỗi diff đọc theo bốn câu hỏi: tệp nào thay đổi, dòng nào thay đổi, thay đổi liên quan đến lỗi ra sao, và hợp đồng dữ liệu có bị ảnh hưởng không. Một diff sửa đúng cận nhưng đồng thời xóa phép kiểm `category` và bật tự chạy lệnh thì tổng 60000 vẫn đúng mà hành vi đã yếu đi. Chấp nhận (accept) chỉ là nhận thay đổi, không phải chứng nhận đúng; nhật ký giữ cả lượt thất bại, vì chính lượt thất bại sinh ra ca kiểm thử hồi quy.

Nghiệm thu dựa trên ba loại bằng chứng. Thứ nhất là **lệnh**: build với `g++`, chạy đúng executable, đọc stdout, stderr và exit code ngay sau lệnh; compiler lỗi thì dừng, vì executable cũ vẫn có thể in 60000. Thứ hai là **ca biên**: Sổ tay có ba bảng C1–C9 cho C++, W1–W10 cho `parseAmount` và T1–T8 cho `totalExpenses`, cùng bộ `test_data.cjs` với kết quả mong đợi 34 passed, 0 failed; bảng và cách đọc kết quả được trình bày ở [Bài thực hành 07](../chapters/chapter-02.md#muc-2-7). Thứ ba là **lời giải thích**: test của bản đúng đạt không chứng minh tệp lỗi vừa sửa đã chạy; test Node.js đạt không chứng minh `localStorage` lưu được. Báo cáo một phút gồm bốn ý: lỗi, chỗ sửa, bằng chứng, phần chưa kiểm.

### Thử ngay (10 phút)

Mục tiêu: viết hợp đồng giao việc và đọc một diff. Viết sáu dòng vào `ghi-chep-02.txt`: tệp duy nhất được sửa; mục tiêu (ba khoản ra 60000); điểm dừng trước Act; ba việc cấm; bằng chứng yêu cầu sau khi sửa; câu "nếu bị chặn thì dừng và báo". Sau đó tạo checkpoint, tự sửa `i < n - 1` thành `i < n` trong bài làm (nếu chưa sửa ở mục 2.2) và so hai tệp theo bốn câu hỏi. Ghi phần đã chạy thật và phần chưa chạy.

### Gợi ý đối chiếu

Hợp đồng có tên tệp cụ thể, có điểm dừng và có câu từ chối dependency? Diff chỉ đổi một dòng trong đúng tệp bài làm, còn `vi-du` không thay đổi? Phần "chưa kiểm" có ghi rõ validation chưa làm và các ca C7–C9 chưa thể đạt với bản vá cận?

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nên nhận bản vá cùng với thay đổi Auto-Run và dependency, hay tách riêng từng việc? Khi `test_data.cjs` báo đạt, kết luận nào được phép và kết luận nào chưa?
- **Từ khóa tra cứu:** diff, checkpoint, regression test, exit code, dependency review.
- **Trong Sổ tay thực hành:** [Bài thực hành 05](../chapters/chapter-02.md#muc-2-5) có hợp đồng giao việc mẫu và cách kiểm dependency; [Bài thực hành 06](../chapters/chapter-02.md#muc-2-6) có diff minh họa và mẫu nhật ký mười dòng; [Bài thực hành 07](../chapters/chapter-02.md#muc-2-7) có lệnh build cho Bash và PowerShell, ba bảng ca biên, bốn bước nghiệm thu trên trình duyệt và bảng tự đánh giá.

## Tóm tắt chương

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

## Cầu nối sang chương sau

Chương này đã cho thấy cách dùng AI có kiểm soát: giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. Nhưng một công cụ chạy tốt rất dễ khiến người dùng ngừng tự nghĩ. Chương 3 bàn cách tận dụng AI mà không lạm dụng, để mỗi lần dùng đều giúp người học hiểu thêm.

## Tài liệu tham khảo

Thông tin về sản phẩm Qoder được đối chiếu với tài liệu chính thức tại mốc 30/10/2026; giao diện và quyền có thể thay đổi theo phiên bản.

- [Qoder IDE: Ask](https://docs.qoder.com/user-guide/chat/ask.md) và [Agent](https://docs.qoder.com/user-guide/chat/agent.md): hai chế độ chat và cách review thay đổi.
- [Qoder IDE: Terminal](https://docs.qoder.com/user-guide/editor/terminal.md): mở terminal và chính sách chạy lệnh của IDE.
- [MDN: parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) và [Number.isSafeInteger](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger): đọc một phần chuỗi và miền số nguyên an toàn.
- [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage): giới hạn lưu trữ khi mở trang qua `file://`.
- Mã ví dụ kèm sách, chỉ để đọc và đối chiếu: [`loi-bo-sot.cpp`](../vi-du/nam-1-cpp/loi-bo-sot.cpp), [`vi_sinh_vien.cpp`](../vi-du/nam-1-cpp/vi_sinh_vien.cpp), [`data.js`](../vi-du/nam-2-web/data.js), [`test_data.cjs`](../vi-du/nam-2-web/test_data.cjs).
