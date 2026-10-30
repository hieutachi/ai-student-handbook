# CHƯƠNG 3 · HỌC CHỦ ĐỘNG: DÙNG AI MÀ KHÔNG LẠM DỤNG

Chương 2 đã trình bày cách làm việc có kiểm soát với AI: chuẩn bị môi trường, giao việc có giới hạn, đọc diff và nghiệm thu bằng kiểm thử. Nhưng một chương trình chạy đúng sau khi được AI hỗ trợ chưa chứng minh người học đã nắm kiến thức mà bài tập nhắm tới. Chương này là bước **Giữ vững** trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn: tận dụng AI mà phần học vẫn ở lại với người học. Nhân vật, hội thoại và số liệu trong chương là *Tình huống hư cấu* và *Dữ liệu giả định*; quyền dùng AI trong bài nộp do từng học phần quy định.

"Lạm dụng" ở đây không có nghĩa dùng AI là xấu. Lạm dụng là giao cho AI đúng phần việc đang cần luyện, chẳng hạn nhờ AI viết vòng lặp trong chính bài học về vòng lặp.

**Sau chương này, người học có thể:**

- Nhận ra kết luận vượt quá bằng chứng trong một câu trả lời tự tin của AI và tìm một phản ví dụ nhỏ để kiểm tra.
- Ghi dự đoán về đầu vào, kỳ vọng và giả thuyết trước khi hỏi AI hoặc chạy chương trình.
- Lần ngược luồng dữ liệu của một ứng dụng nhỏ và giải thích lại bằng lời của chính người học.
- Tự quan sát khả năng nhớ lại, hoàn thành một nhiệm vụ nhỏ không dùng AI và viết kết luận đúng mức bằng chứng.

## Tình huống mở đầu

Sau Chương 2, Minh (năm nhất, học C++) đã sửa cận vòng lặp và chương trình in đúng tổng **60000** cho ba khoản 35000, 7000 và 18000. Khi Lan hỏi kết quả sẽ thế nào nếu danh sách chỉ có một khoản, Minh chưa trả lời được nếu không hỏi lại AI. Lan (năm hai, học Web) gặp điều tương tự: giao diện đã hoạt động, nhưng Lan chưa giải thích được vì sao giá trị đọc từ ô nhập phải qua hai bước chuyển kiểu và kiểm tra. Cả hai đặt một mục tiêu chung cho chương này: **tự giải thích được ít nhất một điều khi không còn nhìn lời giải**. Câu hỏi đặt ra là dùng AI thế nào để mục tiêu đó vẫn đạt được.

## 3.1. Bẫy câu trả lời tự tin (AI Trap)

Mục này giúp người học đánh giá một câu trả lời tự tin của AI bằng căn cứ thay vì bằng cảm giác. Câu hỏi cần đặt ra cho mỗi câu trả lời: "Kết luận này đã được chứng minh cho những đầu vào nào?"

### Ý chính

Một câu trả lời tự tin thường trộn lẫn phần đã chứng minh với phần chỉ suy đoán. Giả sử AI nói với Minh: "Đã đổi cận vòng lặp và thấy 60000, vậy chương trình xử lý mọi đầu vào an toàn." Vế đầu là bằng chứng thật: với ba khoản mẫu, bản sửa in 60000. Vế sau vượt quá bằng chứng: một ca đúng chưa nói gì về danh sách rỗng, khoản âm hay danh sách 501 khoản.

Cách kiểm tra rẻ nhất là một **phản ví dụ nhỏ**: đầu vào ngắn nhất làm cho kết luận sai. Với cận lỗi `i < n - 1`, danh sách chỉ có một khoản 7000 cho `n = 1`; lần kiểm tra đầu tiên là `0 < 0`, sai ngay, vòng lặp không chạy lượt nào và tổng là 0 trong khi kỳ vọng là 7000. Một dòng tính tay đủ bác bỏ chữ "mọi" trong câu trả lời. Ngược lại, danh sách rỗng cho 0 với cả cận đúng lẫn cận sai, nên riêng ca rỗng không phân biệt được hai cận. Chọn phản ví dụ cũng là một việc cần suy nghĩ.

![Lời AI giả lập sai: mảng rỗng ra 0 nên vòng lặp đúng. Phản ví dụ [7000] với i=0, n=1, cận i<n-1 làm 0<0 sai: thực tế 0, kỳ vọng 7000.](../assets/ai-trap.svg)

Để có chỗ bám, cả hai nhánh dùng chung một **hợp đồng dữ liệu**: tiền là số nguyên VND từ 1 đến 1000000000, danh sách tối đa 500 khoản, danh sách rỗng hợp lệ và có tổng 0. Mỗi khoản ở nhánh Web có bốn trường `id`, `title`, `amount`, `category`. Hợp đồng là điều AI không được tự ý đổi cho tiện viết mã. Nếu AI nói "ở Web cứ dùng `Number` cho mọi giá trị là đủ", hợp đồng cho ngay một phản ví dụ: `Number("")` trả về 0, chuyển kiểu được nhưng không phải khoản hợp lệ.

Bẫy cũng xuất hiện khi dựng nhanh bằng cách mô tả mong muốn rồi nhận mã do AI sinh ra qua nhiều lượt trao đổi (vibe coding). Cách làm này hữu ích để thử ý tưởng, nhưng chương trình chạy được không chứng minh người làm hiểu chương trình. Phiên bản có kiểm soát đi chậm hơn: biết vai trò từng tệp, chọn một vấn đề, dự đoán, nhận một thay đổi, kiểm vài ca rồi mới đi tiếp. Người học được phép tra cứu tên API; điều không được bỏ qua là trả lời bốn câu về mỗi đoạn mã: nhận dữ liệu gì, trả về gì, dựa vào điều kiện nào của hợp đồng, và bỏ điều kiện nào thì tạo được ca sai.

### Thử ngay (10 phút)

Mục tiêu: tìm phản ví dụ cho ba kết luận. Chép ba câu sau vào vở (viết sai có chủ đích): (1) "Đổi cận và thấy 60000, vậy mọi đầu vào đều an toàn." (2) "Ở Web cứ dùng `Number` cho mọi giá trị là đủ." (3) "Muốn tổng theo nhóm thì lọc theo `category` trước, khoản thuộc nhóm khác không liên quan." Với mỗi câu, ghi một đầu vào cụ thể cần thử và kết quả dự đoán bằng tay. Chưa viết lại hàm, chưa mở AI. Ghi lại câu nào khó tìm phản ví dụ nhất.

### Gợi ý đối chiếu

Mỗi phản ví dụ phải là một đầu vào cụ thể (giá trị, kiểu, số lượng), không phải nhận xét chung "AI có thể sai". Với câu (1), ca một khoản hoặc khoản âm là dấu hiệu đúng hướng. Với câu (2), nghĩ tới chuỗi rỗng hoặc số âm. Với câu (3), nghĩ tới một khoản ở nhóm khác có tiền sai kiểu: lọc trước sẽ che mất khoản đó.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Vì sao ca rỗng không phân biệt được hai cận nhưng ca một khoản thì được? Với bài đang học, phần nào là "phần đang cần luyện" mà AI không nên làm thay?
- **Từ khóa tra cứu:** counterexample, edge case, data contract, vibe coding.
- **Trong Sổ tay thực hành:** [3.1. Bẫy câu trả lời tự tin](../chapters/chapter-03.md#muc-3-1) — hợp đồng dữ liệu đầy đủ, bảng sáu tình huống phân biệt tận dụng với giao việc học cho AI, phần đối chiếu ba kết luận.

## 3.2. Dự đoán trước khi hỏi (Think First)

Mục này giúp người học hỏi AI hiệu quả hơn bằng cách có sẵn điểm bám: một dự đoán được viết ra trước. Hỏi khi chưa có lời giải là bình thường; hỏi khi chưa có dự đoán mới là điều cần tránh.

### Ý chính

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

### Thử ngay (10 phút)

Mục tiêu: viết phiếu dự đoán và trace bằng tay, chưa chạy, chưa hỏi. Dùng mẫu ba dòng sau cho danh sách chỉ có một khoản 18000:

```text
Đầu vào: ...
Kỳ vọng: ...
Giả thuyết (chưa chạy): ...
```

Sau đó, với đoạn mã lỗi ở trên, lập bảng ba cột: lần kiểm tra, giá trị `i` và điều kiện, `total` sau lượt. Làm cho cả ca một khoản và ca ba khoản mẫu. Ghi lại lượt kiểm tra nào làm vòng lặp dừng sớm.

### Gợi ý đối chiếu

Phiếu đúng hướng khi kỳ vọng được ghi trước khi nhìn mã chạy, và giả thuyết nêu nơi nghi ngờ chứ chưa khẳng định nguyên nhân. Bảng trace đúng hướng khi có cả lần kiểm tra thất bại (lượt mà điều kiện sai) chứ không chỉ các lượt được cộng. Ca một khoản phải cho thấy vòng lặp không chạy lượt nào với cận lỗi.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Vì sao không nên thay cận bằng `size() - 1` dù trông gọn hơn? Khi đã nhớ lời giải, làm sao biết lần này là hiểu hay chỉ là nhớ?
- **Từ khóa tra cứu:** predict-run-investigate, off-by-one error, Socratic prompting.
- **Trong Sổ tay thực hành:** [3.2. Dự đoán trước khi hỏi](../chapters/chapter-03.md#muc-3-2) — phiếu dự đoán năm dòng, hội thoại C++ đầy đủ với bảng trace và bảng kỳ vọng hai cận, bảng dấu vết của phiên 25 phút; [2.3. Gỡ lỗi C++](../chapters/chapter-02.md#muc-2-3) — kiểu kích thước không dấu và việc build.

## 3.3. Lần ngược luồng dữ liệu và giải thích lại (Reverse Engineering, Explain It Back)

Mục này giúp người học kiểm tra bản thân có thật sự hiểu chương trình hay chỉ thấy chương trình chạy. Hai bước đi liền nhau: đọc ngược từ kết quả về nơi dữ liệu được tạo ra, rồi trình bày lại bằng lời của chính người học.

### Ý chính

**Lần ngược** (tiếng Anh: *reverse engineering*) là đọc chương trình từ con số trên màn hình về nơi dữ liệu được tạo. Trong `bai-lam/nam-2-web`, Lan bắt đầu từ tổng hiển thị, lần về hàm `render()`, lời gọi `D.totalExpenses(expenses)`, chỗ gán `expenses`, handler `submit` và `D.parseAmount` trong `app.js`; rồi mở `data.js` để đọc các hàm và `index.html` để xem form. Ở mỗi chặng, điều cần ghi là **kiểu dữ liệu**: `.value` của ô nhập là chuỗi kể cả khi người dùng gõ chữ số; `parseAmount` kiểm tra cách viết rồi mới chuyển thành số; `normalizeExpenses` kiểm tra cả danh sách, gồm `id`, `title`, `amount` và `category`, trước khi gán; `JSON.stringify` tạo chuỗi để ghi vào `localStorage`, và khi đọc lại, JSON hợp lệ chưa chắc đúng schema. Cần mô tả đúng mã hiện có: không bịa ra một hàm tên `handleSubmit` khi mã dùng callback vô danh.

Để thấy vì sao kiểu quan trọng, Lan làm một lab nhỏ trên giấy, không sửa `data.js` đang đúng: ba giá trị `amount` là các chuỗi `"35000"`, `"7000"`, `"18000"`; `total` ban đầu là số 0; mỗi lượt thực hiện `total = total + expense.amount`. Ngay lượt đầu, số 0 cộng chuỗi `"35000"` cho chuỗi `"035000"`; từ đó chương trình không còn cộng số mà nối ký tự. Kết luận của Lan: sửa ở biên nhập liệu (kiểm tra chuỗi, chuyển thành số, kiểm tra giá trị, rồi mới tạo Expense), và hàm tổng vẫn phải từ chối tiền sai vì dữ liệu có thể đến từ đường khác.

**Giải thích lại** (tiếng Anh: *explain it back*) là bước vượt qua câu "em hiểu rồi". Đóng tài liệu, trong khoảng một phút, trình bày đường đi của `"18000"` từ ô nhập đến giá trị số trong danh sách rồi đến chuỗi JSON, chỉ vào tên hàm ở mỗi chặng. Chặng nào bị kẹt chính là nội dung cần ôn tiếp. Minh tham gia với vai trò review chéo cho Lan, không chuyển sang làm dự án Web.

![Vòng sáu bước hai hàng: dự đoán, nhận gợi ý, tự sửa, chạy test, giải thích, biến thể; biến thể quay về dự đoán. AI chỉ hỗ trợ ở bước gợi ý.](../assets/active-learning.svg)

### Thử ngay (10 phút)

Mục tiêu: trace giá trị và kiểu, rồi giải thích lại. Trên giấy, lập bảng bốn cột cho lab ba chuỗi ở trên: lượt, `total` trước và kiểu, `amount` và kiểu, `total` sau và kiểu. Giữ nguyên dấu ngoặc kép khi ghi chuỗi. Sau đó gập bảng lại và nói thành lời, trong một phút, vì sao kết quả không phải 60000 và nên sửa ở chặng nào. Ghi lại chặng đầu tiên bị kẹt.

### Gợi ý đối chiếu

Bảng đúng hướng khi cột kiểu đổi từ number sang string ngay lượt đầu và không đổi lại nữa. Lời giải thích đúng hướng khi nêu được tên hàm hoặc vị trí cho từng chặng (ô nhập, phân tích tiền, kiểm tra danh sách, lưu) thay vì chỉ nói "phải chuyển sang số". Nếu chỉ đề xuất đổi toán tử cộng mà chưa nói tới kiểu của `.value`, chặng đầu còn thiếu.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Khi tải lại trang, dữ liệu đã lưu trong `localStorage` có cần kiểm tra lại không, và vì sao parse thành công chưa đủ? Chỉ dùng `Number` thì chuỗi rỗng và số âm sẽ đi đâu?
- **Từ khóa tra cứu:** typeof, type coercion, input validation, Feynman technique.
- **Trong Sổ tay thực hành:** [3.3. Lần ngược luồng dữ liệu và giải thích lại](../chapters/chapter-03.md#muc-3-3) — bảng bảy chặng, hội thoại Web đầy đủ, hành vi lưu trữ và origin, bảng tám mẫu prompt P01–P08; [3.6. Bài vận dụng](../chapters/chapter-03.md#muc-3-6) — tái dựng phần lõi trong lab, bảng kiểm thử với kỳ vọng ghi trước và biến thể tổng theo `category`; [Thư viện prompt mẫu](../chapters/prompt-library.md).

## 3.4. Tự quan sát trí nhớ và thử thách không dùng AI (Memory Experiment, No-AI Challenge)

Mục này giúp người học biết bản thân còn nhớ gì sau khi học và tự làm được đến đâu khi không có AI. Hai hoạt động không dùng để chấm điểm; chúng tạo bằng chứng để chọn việc luyện tiếp.

### Ý chính

**Tự quan sát trí nhớ** (Memory Experiment) gồm hai nhiệm vụ gần tương đương, không cần AI, khoảng 12–15 phút. Nhiệm vụ A: với `35000, 7000, 18000`, đọc lời giải về cận `i < n` và dãy tổng `0 → 35000 → 42000 → 60000` trong 90 giây rồi gấp lại. Nhiệm vụ B: với `18000, 35000, 7000`, tự viết bảng chỉ số và tổng trong 90 giây, không mở lời giải. Sau mỗi nhiệm vụ, che ghi chép, nghỉ hai phút bằng một việc không liên quan, rồi trả lời bốn câu trên giấy trắng: các chỉ số hợp lệ là gì; tổng sau mỗi lượt là bao nhiêu; điều kiện nào làm vòng lặp dừng; danh sách một khoản và danh sách rỗng cho kết quả ra sao và vì sao. Chỉ sau khi trả lời xong mới đối chiếu.

Điều quan trọng nhất là **kết luận đúng mức bằng chứng**. Một nhận xét phù hợp có dạng: "Ở nhiệm vụ A, nhớ tổng cuối nhưng quên lượt dừng; ở nhiệm vụ B, tự viết được ba tổng trung gian; sẽ luyện điều kiện dừng khi đóng tài liệu." Không được suy ra "AI làm trí nhớ kém đi": không có nhóm so sánh, còn thứ tự làm, độ mệt và việc đã nhìn đáp án đều ảnh hưởng. Kết quả chỉ dùng để chọn hành động học tiếp theo.

**Thử thách 25 phút không dùng AI** (No-AI Challenge) là phiên làm việc độc lập từ đầu đến cuối: đóng hội thoại, không dùng Agent, công cụ sinh mã hay gợi ý. Nhiệm vụ chung: đếm số khoản có tiền **từ 10000 VND trở lên**, với đầu vào đã được xác nhận hợp lệ theo hợp đồng. Minh viết `countLargeAmounts(const std::vector<long long>& amounts)` trả về `int`; Lan viết `countLargeExpenses(expenses)` dùng `expense.amount` ở kiểu số, không đọc DOM hay `localStorage`. Không đổi nhiệm vụ thành tính tổng. Các ca cần chuẩn bị: ba khoản mẫu, danh sách rỗng, một khoản 10000, một khoản 9999, ba khoản mẫu đảo thứ tự. Phân bổ thời gian: 5 phút tính kỳ vọng, 7 phút viết thuật toán bằng lời rồi viết mã hoặc giả mã, 6 phút trace hoặc chạy, 4 phút tự tìm một điểm sai, 3 phút đóng mã và trình bày lại. Chưa xong trong 25 phút là bình thường; điểm nghẽn ghi lại chính là nội dung cần luyện tiếp. Nếu vô tình thấy gợi ý, ghi lại thời điểm và không gọi cả phiên là độc lập.

### Thử ngay (10 phút)

Mục tiêu: làm phiên thu nhỏ của nhiệm vụ B. Lấy giấy và đồng hồ. Trong 90 giây, với `18000, 35000, 7000` và cận `i < n`, tự viết bảng chỉ số và tổng sau mỗi lượt, không mở lời giải. Che bảng, nghỉ hai phút bằng một việc khác. Sau đó trả lời bốn câu hỏi ở trên trên giấy trắng. Cuối cùng, mở bảng và ghi ba điều: ý tự nhớ được, ý sai hoặc cần mở lại, có giải thích được ca một khoản hay không.

### Gợi ý đối chiếu

Đúng hướng khi dãy tổng trung gian của nhiệm vụ B khác nhiệm vụ A nhưng tổng cuối giống nhau, và khi câu trả lời về lượt dừng nêu được lần kiểm tra điều kiện thất bại. Kết luận ghi lại phải là một việc cụ thể cho phiên sau, không phải nhãn "nhớ tốt" hay "nhớ kém".

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Trong bài đếm, vì sao biến đếm kiểu `int` là đủ trong khi tổng tiền phải dùng `long long`? Bốn tiêu chí nào giúp tự đối chiếu một phiên không AI mà không nhìn vào tốc độ?
- **Từ khóa tra cứu:** retrieval practice, testing effect, deliberate practice.
- **Trong Sổ tay thực hành:** [3.4. Tự quan sát khả năng nhớ lại](../chapters/chapter-03.md#muc-3-4) — bảng ghi nhận, lượt hôm sau và phần đối chiếu; [3.5. Thử thách 25 phút không dùng AI](../chapters/chapter-03.md#muc-3-5) — quy tắc đầy đủ, bảng phân bổ thời gian, bốn tiêu chí đối chiếu và lời giải để đọc sau phiên.

## 3.5. Tự đánh giá cuối chương (Skill Unlocked)

Mục này giúp người học nhìn lại đã làm được gì và chọn việc luyện tiếp. Kết quả là ghi nhận tại thời điểm hiện tại, không phải nhãn năng lực lâu dài.

### Ý chính

Với mỗi năng lực, chọn một trong ba mức: **tự làm** (đã đóng chat và không nhìn đáp án), **cần gợi ý**, hoặc **chưa làm**, kèm bằng chứng. Ba nhóm năng lực của chương: *giải thích* (nêu hợp đồng dữ liệu; trace đến 60000 và chỉ ra vì sao cận lỗi dừng ở 42000; phân biệt `35000` với `"35000"`), *sửa* (chỉ thay phần gây lỗi, tách bản vá cận khỏi validation; tự chọn ca một khoản, ca rỗng, ca biên, ca dữ liệu sai) và *vận dụng* (làm hàm max hoặc tổng theo nhóm mà không che khoản sai ngoài nhóm; nêu rõ phần đã nhận hỗ trợ, phần tự làm và phần còn cần hỏi). Chọn một dòng chưa làm được, thu nhỏ ví dụ rồi thử lại.

Các mục trong chương ghép thành một chu trình học chủ động: chọn mục tiêu và đọc hợp đồng → tự thử và dự đoán trước khi hỏi hoặc chạy → xin một gợi ý, tự trả lời, tự sửa một điểm → kiểm chứng bằng test → nếu chưa đúng, ghi điểm nghẽn, thu nhỏ và thử lại; nếu đúng, làm biến thể không AI và ghi chỗ chưa chắc → chọn việc tiếp theo. Cuối mỗi phiên chỉ cần ghi ba dòng: học được, chưa chắc, việc tiếp. Phải gọi tên hành động hoặc kiến thức cụ thể; một ghi chép như "học được nhiều" không giúp phiên sau biết bắt đầu từ đâu.

### Thử ngay (10 phút)

Mục tiêu: viết phiếu ba dòng cho phiên học gần nhất. Phiếu minh họa (hư cấu, không phải kết quả của một sinh viên thật):

```text
Học được: Cận cũ không cho i = 2 đi vào thân vòng lặp.
Chưa chắc: Tôi chưa tự giải thích hết kiểm tra dữ liệu đọc từ JSON.
Việc tiếp: Tự trace ca một khoản và một ca sai ngoài nhóm, chưa mở AI.
```

Viết phiếu của riêng người học. Sau đó chọn một năng lực ở trên đang ở mức "chưa làm" và ghi ví dụ thu nhỏ sẽ thử ở phiên sau.

### Gợi ý đối chiếu

Mỗi dòng của phiếu phải chỉ vào một hành động hoặc một kiến thức kiểm tra được (một ca, một điều kiện, một hàm). Dòng "việc tiếp" nên làm được trong một phiên ngắn mà không cần mở AI.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Bộ test đạt hết đã chứng minh người học hiểu bài chưa? Điều gì còn thiếu?
- **Từ khóa tra cứu:** self-assessment, metacognition, learning log.
- **Trong Sổ tay thực hành:** [3.7. Tự đánh giá năng lực cuối chương](../chapters/chapter-03.md#muc-3-7) — bảng tám năng lực, tám câu vấn đáp và phần đối chiếu; [3.6. Bài vận dụng](../chapters/chapter-03.md#muc-3-6) — bài sửa lỗi hoàn chỉnh với validation, bảng kiểm thử và hai biến thể max, tổng theo nhóm, nơi mức "vận dụng" được kiểm tra đầy đủ.

## Tóm tắt chương

- Một câu trả lời tự tin cần được đánh giá bằng hợp đồng dữ liệu, phản ví dụ và phạm vi kiểm thử; đúng một ca chưa phải đúng mọi ca.
- Ranh giới giữa tận dụng và lạm dụng nằm ở nhiệm vụ đang luyện; trước khi hỏi, xác định phần người học phải tự chứng minh.
- Dự đoán trước khi hỏi hoặc chạy, trace từng lượt, mỗi lượt một câu hỏi: cách giữ quá trình suy nghĩ ở phía người học.
- Lần ngược luồng dữ liệu và giải thích lại bằng lời làm lộ ra chặng còn thiếu, như khác biệt giữa `35000` và `"35000"`.
- Tự quan sát trí nhớ và thử thách không AI chỉ dùng để chọn việc học tiếp, không dùng để kết luận nhân quả.

**Ba câu để tự kiểm:** Vì sao danh sách một khoản là phản ví dụ tốt hơn danh sách rỗng? Lượt đầu tiên của lab chuỗi đổi kiểu ở đâu? Phiếu ba dòng của phiên gần nhất có gọi tên được một ca cụ thể không?

## Cầu nối sang chương sau

Khi đã biết dùng AI mà vẫn học được, bước tiếp theo là biết ranh giới: dữ liệu nào không nên đưa vào AI, mã nào cần bảo mật, nguồn nào có bản quyền, cách giữ liêm chính khi nộp bài. Chương 4 trình bày các ranh giới đó: dùng có trách nhiệm là điều kiện để được tiếp tục dùng.

## Tài liệu tham khảo

- [MDN Web Docs — Window: localStorage property](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [MDN Web Docs — typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)
- [MDN Web Docs — Number.isSafeInteger()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger)
- [cppreference.com — std::vector](https://en.cppreference.com/w/cpp/container/vector)
- Mã ví dụ đi kèm: [loi-bo-sot.cpp](../vi-du/nam-1-cpp/loi-bo-sot.cpp), [data.js](../vi-du/nam-2-web/data.js), [app.js](../vi-du/nam-2-web/app.js).
