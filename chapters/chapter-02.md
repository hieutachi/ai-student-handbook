# CHƯƠNG 2 · ĐIỀU KHIỂN QUÁ TRÌNH LÀM VIỆC VỚI AI

Chương 1 đã làm rõ vai trò của AI trong học tập: AI hỗ trợ, người học quyết định. Chương cũng giúp nhận diện công cụ qua ba lớp model, provider và ứng dụng, và cho thấy một câu trả lời được tạo ra từ prompt, context và token. Vì vậy, một câu trả lời không nên được chấp nhận chỉ vì nó được trình bày tự tin. Việc so sánh chi phí và chọn công cụ được để lại cho Chương 5 (mục 5.1 đến 5.4), khi người học đã biết dùng và biết giữ ranh giới.

Chương 2 chuyển sang bước tiếp theo: dùng AI như một công cụ có kiểm soát. Thay cho câu hỏi "AI nào giỏi nhất?", chương đặt ra ba câu hỏi xuyên suốt: **việc gì cần làm, công cụ được phép làm đến đâu, và bằng chứng nào đủ để chấp nhận kết quả?** Nói ngắn gọn, giao việc rõ, kiểm bằng bằng chứng và chỉ nhận thay đổi khi có chủ đích.

Chương được tổ chức thành bảy bài thực hành (Mission 01–07), đi từ việc chuẩn bị môi trường đến việc nghiệm thu kết quả. Thời lượng dự kiến là hai buổi, mỗi buổi 90 phút, chưa kể thời gian đọc sâu và làm lại; con số này chỉ để tham khảo, không phải chuẩn tốc độ hay chuẩn đầu ra học phần (CLO) chính thức. Người học chọn một nhánh để thực hành sâu nhưng vẫn cần giải thích được lỗi trọng tâm của nhánh còn lại. Một số khái niệm như trace, kiểu dữ liệu hay diff có thể còn mới; chưa hiểu ngay là bình thường, vì mỗi khái niệm đều được giải thích bằng ví dụ nhỏ ngay tại chỗ.

Hai nhân vật Minh, Lan cùng mọi hội thoại trong chương là *tình huống hư cấu*; chúng không phải nhật ký sử dụng tài khoản Qoder, kết quả benchmark hay khảo sát tại Trường Đại học Thủy lợi.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Phân biệt vai trò của editor, IDE, terminal, shell, CLI và Agent; xác định đúng thư mục làm việc và shell đang sử dụng.
2. Đặt câu hỏi ở chế độ chỉ đọc với ngữ cảnh nhỏ và vị trí mã có thể kiểm lại.
3. Lập bảng trace để tìm nguyên nhân lỗi cận vòng lặp trong C++, đồng thời giải thích các khái niệm liên quan: kiểu `long long`, giá trị không dấu của `size()`, tham chiếu và thông báo lỗi biên dịch.
4. Lần theo luồng dữ liệu của một ứng dụng Web từ ô nhập đến hàm tính tổng và nơi lưu trữ; phân biệt chuỗi, số, `undefined` và `NaN`.
5. Viết hợp đồng giao việc cho Agent với phạm vi, điểm dừng và yêu cầu bằng chứng; từ chối dependency hoặc thay đổi quyền nằm ngoài phạm vi.
6. Đọc diff theo bốn câu hỏi, tạo checkpoint và giữ nhật ký làm việc, kể cả các lượt thất bại.
7. Nghiệm thu bằng lệnh build và test, bảng ca biên và quan sát trên trình duyệt; báo cáo đúng phạm vi đã kiểm tra và chưa kiểm tra.

## Tình huống mở đầu

Chương trình C++ của Minh in ra **42000**, trong khi ba khoản chi cộng trên giấy được **60000**. Lan có bản Web của ứng dụng ViSinhVien: bảng hiển thị đủ ba khoản và tổng đúng, nhưng khi thử nhập `35000abc`, Lan cần biết chương trình thực sự từ chối giá trị này ở đâu. Cùng lúc đó, một trợ lý AI đề nghị cài thêm thư viện để "xử lý tiền chuyên nghiệp". Ba việc này đòi hỏi ba mức quyền và ba loại bằng chứng khác nhau.

Minh là sinh viên năm nhất học C++. Lan là sinh viên năm hai, học lập trình hướng đối tượng (OOP), cấu trúc dữ liệu và giải thuật (DSA), lập trình Web và cơ sở dữ liệu. Hai phiên bản ViSinhVien phục vụ mục đích học tập và chưa được kết nối với nhau. Không nhập thông tin sinh viên thật, tài khoản, sao kê ngân hàng hay bất kỳ bí mật nào vào mã nguồn hoặc hội thoại với AI.

Dữ liệu xuyên suốt chương (*dữ liệu giả định*) gồm ba khoản: Cơm trưa **35000**, Xe buýt **7000**, Vở ghi **18000**, đơn vị là đồng (VND), kiểu số nguyên. Giá trị `42000` đúng nếu chỉ tính hai khoản đầu, nhưng sai nếu là tổng cuối cùng của cả ba khoản. Hợp đồng dữ liệu quy định mỗi khoản hợp lệ nằm trong khoảng **1–1000000000**, danh sách có tối đa **500 khoản**, danh sách rỗng có tổng **0**; do đó tổng lớn nhất có thể đạt **500000000000**.

Trong suốt chương cần phân biệt năm đối tượng: **demo đúng** (bản ví dụ chạy đúng), **mã lỗi chủ đích** (bản được cố ý cài lỗi để học), **bài làm** của người học, **kết quả kỳ vọng** suy ra từ mã và **kết quả đã chạy** trên máy. Bảng trace là suy luận thủ công, không phải nhật ký do máy ghi lại. Khi thiếu công cụ, người học vẫn có thể đọc mã, dự đoán và ghi rõ phần chưa thực hiện; không cần mua dịch vụ hay tự cài đặt phần mềm trên máy dùng chung.

## 2.1. Bài thực hành 01 (Mission 01) — Làm chủ môi trường trước khi giao việc

Bài này giúp người học biết vị trí làm việc hiện tại và đang dùng công cụ nào trước khi nhờ AI làm bất cứ việc gì.

### Mục tiêu

Mở đúng thư mục gốc của dự án và phân biệt vai trò của editor, IDE, terminal, shell, CLI và Agent.

### Bối cảnh

Minh gọi chung vùng soạn mã, khung hội thoại và cửa sổ lệnh là "AI". Nhầm lẫn vai trò như vậy dễ dẫn đến lưu nhầm phiên bản tệp hoặc dùng sai cú pháp của shell.

### Các thành phần của môi trường làm việc

Editor (trình soạn thảo) dùng để soạn thảo tệp. IDE (môi trường phát triển tích hợp) kết hợp việc mở dự án, tìm kiếm mã và các tiện ích phát triển khác. Web chat thường chỉ biết phần ngữ cảnh được người dùng cung cấp, trừ khi có kết nối bổ sung. Agent kết hợp mô hình AI với công cụ; nó có thể đọc, sửa tệp và chạy lệnh **tùy theo sản phẩm, chế độ và quyền được cấp**.

Các cách làm này bổ sung cho nhau; chúng không tạo thành một bảng xếp hạng hay một lộ trình thay thế lần lượt. Công cụ mạnh hơn không tự tạo ra kết luận đúng hơn.

| Cách làm | Việc phù hợp trong ViSinhVien | Trách nhiệm không chuyển cho AI |
| --- | --- | --- |
| Editor | Đọc và sửa cận vòng lặp | Lưu đúng tệp, hiểu dòng vừa sửa |
| IDE | Mở dự án, tìm hàm, dùng terminal | Biết đang mở thư mục nào và có công cụ gì |
| Web chat | Hỏi nghĩa của `+=` hoặc một lỗi nhỏ | Cung cấp đoạn mã đủ ngữ cảnh, kiểm chứng lời giải thích |
| Agent | Tìm vị trí, đề xuất thay đổi, kiểm thử theo quyền | Giới hạn phạm vi, xem diff, đọc bằng chứng |

**Terminal** là cửa sổ nhận và hiển thị văn bản. **Shell** là chương trình diễn giải lệnh chạy bên trong terminal, chẳng hạn Bash hoặc PowerShell. **CLI** (giao diện dòng lệnh) là giao diện của chương trình được gọi, ví dụ `g++`, `node` hoặc Qoder CLI. Khi gõ `g++ --version`, shell tìm chương trình `g++`, chương trình in ra phiên bản, còn terminal hiển thị kết quả. Nếu shell không tìm thấy lệnh, vấn đề trước mắt nằm ở môi trường hoặc đường dẫn, chưa phải ở vòng lặp C++.

![Bản đồ môi trường: IDE chứa vùng soạn thảo và terminal; shell diễn giải lệnh gọi CLI; Agent hoạt động theo quyền được cấp.](../assets/workspace.svg)

Việc đã cài Qoder IDE không chứng minh máy đã có compiler `g++`, runtime Node.js hoặc Qoder CLI. Việc dùng Windows cũng không xác định shell: trên cùng một máy có thể mở cả PowerShell lẫn Git Bash. Cần đọc tên phiên terminal hoặc cấu hình đang hiển thị, thay vì thử trộn cú pháp cho đến khi một lệnh tình cờ chạy được.

### Các bước thực hiện

Nhiệm vụ của bài là chuẩn bị thư mục bài làm trong khi giữ nguyên các ví dụ gốc.

1. Mở thư mục gốc **`AI-Student-Handbook`** trong Qoder IDE; không mở toàn bộ ổ đĩa hoặc riêng một nhánh con.
2. Dùng File Explorer hoặc trình quản lý tệp, tạo thư mục `bai-lam` với hai thư mục con `nam-1-cpp` và `nam-2-web`.
3. Sao chép **nội dung** của từng nhánh tương ứng từ `vi-du` sang `bai-lam`; tránh tạo thêm tầng lồng như `nam-1-cpp/nam-1-cpp`. Giữ nguyên `vi-du` để đối chiếu.
4. Dùng chức năng New File của IDE hoặc trình quản lý tệp để tạo `ghi-chep-02.txt` trong nhánh đang học. Đây là tệp người học tự tạo, không có sẵn; cần kiểm tra phần mở rộng để tránh tên tệp dạng `.txt.txt`.

Cấu trúc thư mục sau khi chuẩn bị:

```text
AI-Student-Handbook/              ← thư mục mở trong IDE và cwd của các lệnh
  vi-du/                         ← tham khảo, không sửa
    nam-1-cpp/
    nam-2-web/
  bai-lam/
    nam-1-cpp/
      loi-bo-sot.cpp
      vi_sinh_vien.cpp
      ghi-chep-02.txt             ← người học tự tạo
    nam-2-web/
      index.html
      data.js
      app.js
      test_data.cjs
      ghi-chep-02.txt             ← người học tự tạo
```

Mở terminal qua menu của IDE, hoặc tìm lệnh **Terminal: Create New Terminal** nếu phiên bản có mục đó; không đoán phím tắt. Nếu bố cục giao diện khác, tra cứu [tài liệu terminal](https://docs.qoder.com/user-guide/editor/terminal.md).

**Thư mục hiện hành** (current working directory, viết tắt *cwd*) là thư mục mà shell đang đứng khi thực thi lệnh. Mọi lệnh thực hành trong chương dùng cwd là thư mục gốc `AI-Student-Handbook`, với đường dẫn dạng `bai-lam/...`. Terminal mở từ trước có thể không chuyển theo thư mục đang mở trong IDE, vì vậy cần kiểm tra vị trí trước khi build hoặc chạy test.

| Nhu cầu | Bash, gồm Git Bash | PowerShell |
| --- | --- | --- |
| Xem cwd | `pwd` | `Get-Location` |
| Liệt kê mục ở cwd | `ls` | `Get-ChildItem` |
| Chuyển đến gốc đã xác định nếu đang ở sai nơi | `cd "đường/dẫn/AI-Student-Handbook"` | `Set-Location "đường\dẫn\AI-Student-Handbook"` |
| Đọc mã thoát lệnh ngoài vừa chạy | `echo $?` | `$LASTEXITCODE` |

Dòng đổi thư mục trong bảng là mẫu để **thay bằng đường dẫn thật**, không gõ nguyên chữ "đường/dẫn". Đường dẫn có dấu cách phải được đặt trong dấu nháy kép. Nếu cwd đã đúng thì không cần đổi. Không chạy lần lượt cả hai cột; chỉ dùng cột khớp với shell đang mở. Từ đây trở đi, chương không yêu cầu chuyển vào nhánh con, nên người học cũng không phải nhớ khi nào cần `cd` trở ra.

### Prompt mẫu

Prompt dưới đây yêu cầu AI giải thích dựa trên thông tin được cung cấp, không cài đặt và không giả định công cụ có sẵn:

```text
Tôi mở gốc AI-Student-Handbook trong Qoder IDE và mới học terminal.
Chỉ giải thích dựa trên thông tin tôi cung cấp; không sửa hay chạy lệnh.
Giúp tôi phân biệt IDE, terminal, shell, CLI và Agent.
Bài làm ở bai-lam/nam-1-cpp và bai-lam/nam-2-web; vi-du chỉ để đọc.
Hãy hỏi tôi kiểm tra tên shell và cwd trước khi đưa lệnh phù hợp.
Không giả định có g++, Node.js hay Qoder CLI; không hướng dẫn tự cài.
```

**Kết quả mong đợi.** Hai nhánh được sao chép đúng; tệp ghi chép nêu tên shell và cwd, đồng thời giải thích được thành phần nào làm gì khi gọi `node --version`. Thao tác này không cần AI thực thi. Nếu không dùng AI, người học tự trả lời các câu trong prompt như một phiếu học tập và ghi rõ đó là thực hành thủ công.

**Lỗi thường gặp.** Thường là sửa tệp trong `vi-du`, sao chép tạo thư mục lồng, dùng terminal cũ đang đứng ở nơi khác, hoặc cho rằng IDE có sẵn compiler. Cách xử lý đầu tiên là xem cây thư mục và cwd, không nhờ Agent "tìm mọi nơi trên máy". Nếu thiếu công cụ thì ghi nhận là thiếu; việc cài đặt phải theo quyền hạn và quy định của phòng thực hành.

### Câu hỏi kiểm tra

Giả sử cần giải thích toán tử `+=` và cần tìm hàm mà `app.js` gọi trong `data.js`. Hai việc này có cần cùng một mức quyền không? Nếu trên Windows đang mở Git Bash, cần dùng cột nào trong bảng lệnh? Ghi câu trả lời trước khi mở phần đáp án.

### Đáp án Bài thực hành 01

Một đoạn chat ngắn đủ để giải thích `+=`; chế độ Ask kèm hai tệp thuận tiện cho việc lần theo lời gọi hàm. Cả hai việc đều chưa cần quyền sửa tệp. Khi Windows đang chạy Git Bash thì dùng cột Bash, vì shell, không phải hệ điều hành, quyết định cú pháp lệnh. Tóm lại: editor lưu nội dung, IDE tổ chức công việc, terminal hiển thị, shell diễn giải lệnh, CLI là chương trình được gọi, còn Agent sử dụng công cụ trong giới hạn được cấp.

### Tiêu chí hoàn thành

Người học chỉ ra đúng thư mục gốc, thư mục tham khảo, thư mục bài làm và tệp ghi chép; đọc được cwd và tên shell; giải thích được rằng thiếu `g++` là vấn đề của môi trường, khác với lỗi trong mã C++. Sản phẩm nộp gồm sơ đồ vị trí các thư mục và phần ghi nhận, không chỉ là ảnh chụp giao diện.

## 2.2. Bài thực hành 02 (Mission 02) — Đặt câu hỏi đúng trước khi cho phép sửa

Bài này giúp người học hỏi AI ở chế độ chỉ đọc, để có câu trả lời kiểm lại được mà chưa phải trao quyền sửa tệp.

### Mục tiêu

Đặt câu hỏi ở chế độ chỉ đọc, với ngữ cảnh nhỏ và vị trí mã có thể kiểm lại.

### Bối cảnh

Minh hỏi "Tại sao tổng sai?" khi chưa gửi mã nguồn và dữ liệu. Lan muốn suy ra handler (hàm xử lý sự kiện) chỉ từ hàm tính tổng. Một câu trả lời dài không bù được phần ngữ cảnh còn thiếu; cần thu nhỏ câu hỏi để nhìn thấy bằng chứng.

### Chế độ làm việc của các sản phẩm Qoder

Theo tài liệu chính thức của Qoder tại mốc **30/10/2026**, **Qoder IDE** có hai chế độ Ask và Agent; chế độ Ask đọc hiểu và gợi ý đoạn mã (snippet) nhưng không tự sửa tệp. Qoder Desktop có hai chế độ Coding và General; **General vẫn là chế độ agent, không phải chế độ Ask chỉ đọc**. Qoder CLI là một sản phẩm dòng lệnh riêng. Không chuyển giả định về giao diện hay quyền hạn giữa ba sản phẩm này.

Các thao tác Open, Ctrl+L, `@` và Add to Chat mô tả dưới đây dựa trên tài liệu của IDE, chưa được kiểm chứng trên máy của từng người học. Nếu giao diện khác, cần kiểm tra sản phẩm và phiên bản thay vì chọn một chế độ có quyền rộng hơn. Chương không đưa ra cam kết nào về giá, hạn mức sử dụng (quota) hay điều kiện tài khoản.

### Các bước thực hiện

Nhiệm vụ của Minh là tìm cận của vòng lặp và dự đoán lượt bị bỏ qua. Nhiệm vụ của Lan là lần theo giá trị từ chuỗi nhập vào đến trường `amount`.

1. Giữ thư mục gốc `AI-Student-Handbook` đang mở và chọn tệp trong `bai-lam`.
2. Mở khung Chat theo tài liệu IDE (bằng Ctrl+L nếu phù hợp với phiên bản), rồi chọn **Ask** trên thanh công cụ chat. Chưa giao việc sửa và chưa yêu cầu chạy lệnh trong terminal.
3. Dùng `@` để chọn tệp hoặc thư mục làm ngữ cảnh. Khi chỉ cần một đoạn, bôi chọn đoạn đó rồi dùng **Add to Chat** nếu có. Minh bắt đầu với `bai-lam/nam-1-cpp/loi-bo-sot.cpp`. Lan bắt đầu với `bai-lam/nam-2-web/app.js` và `data.js`, thêm `index.html` khi cần xác minh form.

Ngữ cảnh nhỏ không có nghĩa là cắt bỏ khai báo kiểu hoặc dữ liệu đầu vào quan trọng.

Một câu hỏi tốt tách riêng bốn thành phần: đầu vào, điều mong muốn, điều quan sát được và đoạn mã liên quan. Câu "tôi quan sát thấy 42000 với ba khoản" khác hẳn câu "chắc chắn compiler cộng sai": câu đầu là dữ kiện cần đối chiếu, còn câu sau đã nhảy đến một giả thuyết yếu. Nếu chưa chạy chương trình, cần thay "quan sát" bằng "dự đoán từ mã"; không dùng kết quả minh họa trong sách thay cho kết quả tự thu được.

### Prompt mẫu

Prompt cho nhánh C++ (Minh):

```text
Tôi học C++ năm nhất. Chỉ đọc bai-lam/nam-1-cpp/loi-bo-sot.cpp.
Không sửa tệp, không chạy lệnh. Dữ liệu giả: 35000, 7000, 18000.
Tổng yêu cầu là 60000; tình huống bài học có tổng sai 42000.
Tìm vòng lặp thực tế, nêu kiểu của n và lập bảng i, điều kiện,
khoản được cộng, tổng sau bước. Chưa viết lại cả chương trình.
Tách điều đọc được, giả thuyết và điều chưa chạy kiểm chứng.
Dẫn vị trí mã để tôi tự mở lại; thiếu ngữ cảnh thì nói rõ.
```

Prompt cho nhánh Web (Lan):

```text
Tôi học Web/OOP/DSA năm hai. Chỉ đọc các tệp được đính kèm trong
bai-lam/nam-2-web; không sửa hoặc chạy lệnh.
Lần theo ô nhập → submit → parseAmount → Expense.amount → tổng → lưu/hiện.
Ở mỗi bước ghi tên tệp, tên hàm thật hoặc mô tả handler vô danh,
vị trí tìm thấy và kiểu dữ liệu. Nếu cần index.html, hãy nói cần nó.
Không bịa hàm handleSubmit; không thêm server, CSDL hay dependency.
Phân biệt mã đọc được với trạng thái trình duyệt chưa quan sát.
```

Sau khi nhận câu trả lời, cần mở lại từng vị trí mà AI dẫn ra và kiểm tra tên hàm, khai báo và nơi gọi. Nếu AI bịa ra hàm `handleSubmit`, sửa mô tả thành **handler submit vô danh**; không sửa mã cho khớp với câu trả lời. Khi chưa xem `index.html` thì chưa đủ bằng chứng về phần tử giao diện hoặc thứ tự nạp script.

Prompt không thay thế hàng rào quyền: chế độ, cấu hình và bước phê duyệt mới quyết định công cụ được phép làm gì. Chế độ Ask chỉ đọc cũng không biện minh cho việc đưa dữ liệu nhạy cảm vào ngữ cảnh.

**Kết quả mong đợi.** Minh mở được vòng lặp ở dòng 9 của demo lỗi; Lan tìm được lời gọi `D.parseAmount` trong `app.js`. Số dòng có thể thay đổi giữa các phiên bản, vì vậy cần ghi tên tệp, đoạn mã và điều đã tự kiểm lại.

**Lỗi thường gặp.** Thường là gửi quá nhiều ngữ cảnh hoặc làm mất thông tin về kiểu và cận, nhầm lẫn giữa các sản phẩm, và coi câu "sẽ kiểm thử" là kết quả kiểm thử. Cách khắc phục là thu nhỏ câu hỏi và yêu cầu bằng chứng, không đổi sang công cụ khác để tìm một câu trả lời vừa ý.

### Câu hỏi kiểm tra

AI chỉ đọc `data.js` rồi kết luận "nút Thêm đã gắn đúng sự kiện". Có thể chấp nhận kết luận đó không? Nếu AI gửi một đoạn mã trong chế độ Ask, có thể nói tệp đã thay đổi hay chưa?

### Đáp án Bài thực hành 02

Chưa thể xác nhận việc gắn sự kiện khi chưa xem mã gắn handler trong `app.js` và phần tử liên quan trong `index.html`. Đoạn mã trong hội thoại chỉ là đề xuất; nó không đồng nghĩa với việc tệp đã được sửa hoặc đã được lưu. Cách xử lý đúng là bổ sung đúng ngữ cảnh rồi tự mở lại vị trí mã; không cần cấp quyền Agent chỉ để giải quyết tình trạng thiếu bằng chứng này.

### Tiêu chí hoàn thành

Người học có một prompt chỉ đọc, các vị trí mã đã tự kiểm tra và danh sách những điều chưa biết; phân biệt đúng các sản phẩm; chỉ dùng dữ liệu giả. Ở bài này chưa cần bản vá, nhưng phải mô tả được lỗi.

## 2.3. Bài thực hành 03 (Mission 03) — Gỡ lỗi C++: tìm khoản 18000 bị bỏ sót

Bài này giúp người học tự tìm ra nguyên nhân một lỗi vòng lặp bằng bảng trace, rồi mới nhờ AI kiểm lại.

### Mục tiêu

Lập bảng trace cho danh sách có 0, 1 và 3 phần tử; hiểu vai trò của cận vòng lặp, kiểu dữ liệu, tham chiếu và thông báo của compiler. Mỗi dòng sửa phải đi kèm một lời giải thích.

### Bối cảnh

[Demo lỗi `loi-bo-sot.cpp`](../vi-du/nam-1-cpp/loi-bo-sot.cpp) dùng điều kiện `i < n - 1`, dữ liệu cố định trong `main`, không có hàm tính tổng riêng và không hỗ trợ tham số **`--test`**.

Nhiệm vụ được chia làm hai giai đoạn. Giai đoạn 1 chỉ sửa cận vòng lặp trên dữ liệu hợp lệ; việc kiểm tra tính hợp lệ (validation) của số tiền và số lượng là phần mở rộng riêng. Không thay toàn bộ tệp bằng [bản đúng](../vi-du/nam-1-cpp/vi_sinh_vien.cpp): bài làm cần một diff nhỏ và bảng trace để chứng minh người học đã hiểu nguyên nhân.

### Hợp đồng dữ liệu trước thuật toán: vì sao dùng `long long`

Mô hình chung của một khoản chi là `Expense{id,title,amount,category}`. Nhánh C++ hiện chỉ lấy cột tiền dưới dạng `std::vector<long long>` để luyện thuật toán, còn nhánh Web giữ đối tượng đủ bốn trường. Vì vậy không nên nói chương trình C++ này đã triển khai lớp Expense hoặc lưu đủ tên và nhóm. Hai cách biểu diễn phục vụ hai mục tiêu học tập khác nhau nhưng tuân theo cùng một hợp đồng về tiền.

Kiểu dữ liệu có thể hiểu như kích cỡ của chiếc hộp đựng số: hộp nhỏ thì số lớn không vừa. Phần này chỉ cần nắm ý đó, các chi tiết kỹ thuật đi kèm sẽ rõ dần khi làm bài. Mỗi khoản là số dương, tối đa 1000000000; 500 khoản lớn nhất cho tổng 500000000000. Kiểu `int` thường có miền 32 bit, không đủ chứa tổng đó, nên cả phần tử lẫn biến tổng đều dùng `long long`. Cần phân biệt giới hạn của **mỗi khoản** với giới hạn của **toàn bộ tổng**. Một giá trị vừa với kiểu số cũng chưa chắc hợp lệ về nghiệp vụ: `-1` biểu diễn được trong `long long` nhưng không phải là khoản chi được chấp nhận trong bài này.

Đoạn lõi dưới đây dùng đúng tên và chữ ký hàm của bản đúng, **đã lược bỏ phần validation để tập trung vào phép duyệt**. Đây là trích đoạn để đọc hiểu, không phải toàn bộ tệp để thay vào bài làm; đoạn mã giả định số lượng và số tiền đều đã hợp lệ.

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

Hàm trả về giá trị kiểu `long long`. Tham số `const std::vector<long long>&` nhận vector theo tham chiếu để không sao chép cả danh sách, còn từ khóa `const` ngăn việc sửa danh sách qua tham số này. `size()` trả về số phần tử; việc chuyển sang `int` phù hợp ở đây vì số lượng đã được giới hạn ở 500, không phải là mẫu chuyển kiểu an toàn cho mọi vector có kích thước lớn. Biến `total` được khởi tạo bằng 0, nên khi không có lượt cộng nào, kết quả vẫn xác định.

Vòng lặp bắt đầu với `i = 0`, tiếp tục khi `i < n`, rồi tăng `i`. Chỉ số hợp lệ nằm trong khoảng từ 0 đến `n - 1`; điều kiện lặp phải chặn **trước khi** chỉ số bằng `n` được sử dụng. Phép `+=` lấy tổng cũ cộng với phần tử đang xét rồi ghi lại vào biến. Dấu `}` đóng vòng lặp, không tự cộng phần tử cuối. Câu lệnh `return total` chuyển kết quả về nơi gọi; đó không phải lệnh in ra terminal.

### Các bước thực hiện

Nguyên tắc của bài là dự đoán trước khi xem đáp án. **Trace** là cách đóng vai máy tính: đi từng lượt của vòng lặp và ghi lại giá trị các biến trên giấy. Chưa quen thì hãy bắt đầu với danh sách một phần tử, vì bảng chỉ có vài dòng.

1. Mở `bai-lam/nam-1-cpp/loi-bo-sot.cpp`, giữ nguyên vector `{35000, 7000, 18000}` trong giai đoạn 1.
2. Đọc dòng `int n = static_cast<int>(amounts.size());`, rồi chép điều kiện lặp có lỗi vào tệp ghi chép. Đoạn dưới đây là **đoạn mã lỗi có chủ đích, trích từ demo lỗi**; không chèn đoạn này vào bản đúng.

```cpp
for (int i = 0; i < n - 1; ++i) {
    total += amounts[i];
}
```

3. Lập bảng với các cột `i`, điều kiện, khoản được cộng và tổng sau bước. Với ba khoản, ghi cả lượt kiểm tra điều kiện cho kết quả sai làm vòng lặp dừng; nếu chỉ ghi các lượt có điều kiện đúng, người học rất dễ bỏ qua chính điểm gây lỗi.
4. Lập thêm bảng cho danh sách rỗng và danh sách chỉ có `7000`.

Phần này làm được cả khi chưa biên dịch; khi đó gắn nhãn "trace thủ công" cho bảng.

### Prompt mẫu

Prompt sau giữ phần suy luận ở phía người học: AI chỉ kiểm tra bảng trace mà người học đã tự lập.

```text
Chỉ đọc bai-lam/nam-1-cpp/loi-bo-sot.cpp, chưa sửa hoặc chạy lệnh.
Tôi dự đoán ba khoản 35000, 7000, 18000 bị bỏ khoản cuối.
Hãy kiểm tra bảng trace của tôi cho n = 0, n = 1 với [7000], n = 3.
Giải thích vai trò int n và nguy cơ nếu đổi sang size() - 1.
Chỉ gợi ý cận nhỏ nhất cần sửa, không cộng bù phần tử cuối.
Tách lỗi duyệt với kiểm tra tiền/số lượng còn thiếu trong demo lỗi.
```

![Trace C++: cận sai dừng trước khoản Vở ghi; ca rỗng cùng trả 0 nên cần thêm ca một khoản.](../assets/debugging.svg)

### Đáp án bảng trace: lượt dừng cũng là bằng chứng

Với `n = 3`, điều kiện lỗi trở thành `i < 2`. Vòng lặp cộng đúng hai khoản được truy cập nhưng không bao giờ cộng phần tử ở chỉ số 2. Bảng dưới đây gồm cả phiên bản sai và phiên bản đã sửa để đối chiếu từng bước, không chỉ so sánh tổng cuối.

| Phiên bản | i | Điều kiện | Khoản được cộng | Tổng sau bước |
| --- | ---: | --- | ---: | ---: |
| Sai | 0 | `0 < 2`: đúng | 35000 | 35000 |
| Sai | 1 | `1 < 2`: đúng | 7000 | 42000 |
| Sai | 2 | `2 < 2`: sai, dừng | Không cộng | 42000 |
| Đúng | 0 | `0 < 3`: đúng | 35000 | 35000 |
| Đúng | 1 | `1 < 3`: đúng | 7000 | 42000 |
| Đúng | 2 | `2 < 3`: đúng | 18000 | 60000 |
| Đúng | 3 | `3 < 3`: sai, dừng | Không cộng | 60000 |

Với `n = 0` kiểu `int`, cận sai kiểm tra `0 < -1`, cận đúng kiểm tra `0 < 0`; cả hai điều kiện đều sai ngay từ đầu nên tổng giữ nguyên 0. Hai vòng lặp này không truy cập `amounts[-1]`. Như vậy ca danh sách rỗng **không phân biệt được** hai phiên bản. Với `n = 1`, cận sai kiểm tra `0 < 0` nên trả về 0; cận đúng kiểm tra `0 < 1`, cộng 7000 rồi dừng. Danh sách một phần tử là một phản ví dụ rất nhỏ nhưng có sức phân biệt cao.

Bản vá đúng là `i < n`, không phải `i <= n`. Điều kiện `<=` cho phép truy cập chỉ số `n`, vốn nằm ngoài vector; trong C++, đó là hành vi không xác định (undefined behavior), và không có gì bảo đảm chương trình sẽ báo lỗi rõ ràng. Cộng riêng `amounts[n - 1]` sau vòng lặp cũng chỉ che giấu nguyên nhân và buộc phải xử lý riêng trường hợp danh sách rỗng.

### Đọc sâu: `size()` không dấu và tham chiếu khác bản sao

Không nên máy móc đổi điều kiện thành `i < amounts.size() - 1`. Hàm `size()` trả về kiểu kích thước không dấu; với danh sách rỗng, phép trừ không tạo ra `-1` như khi dùng `int n`. Giá trị bị **tràn vòng không dấu** (unsigned wrap) quay về một số rất lớn theo quy tắc số học không dấu, khiến điều kiện lặp và phép truy cập có thể sai nghiêm trọng. Bản thân phép tràn vòng không phải là truy cập ngoài giới hạn; chính phép truy cập xảy ra sau đó mới dẫn đến hành vi không xác định. Bài dùng `int n` trong miền tối đa 500 để người mới học tập trung vào cận vòng lặp, không nhằm khuyến khích ép kiểu tùy tiện.

Tham chiếu trong chữ ký hàm cũng cần được hiểu, không chỉ được chép lại. Hãy trace đoạn mã **độc lập** dưới đây. Nếu muốn tự chạy thử trong một tệp riêng, đặt `#include <iostream>` ở đầu tệp, ngoài mọi hàm, và đặt năm dòng dưới đây trong thân hàm `int main()`. Không chèn đoạn này vào demo chỉ để xem kết quả.

```cpp
long long total = 0;
long long& alias = total;
long long copied = total;
alias += 35000;
std::cout << total << ' ' << copied << '\n';
```

Dòng 2 tạo một tên khác cho chính biến `total`; dấu `&` trong khai báo này đánh dấu kiểu tham chiếu, không phải phép lấy địa chỉ. Dòng 3 tạo một biến mới, nhận giá trị của `total` tại thời điểm sao chép. Thay đổi thực hiện qua `alias` tác động lên `total` nhưng không cập nhật `copied`. Tham chiếu `const` trong hàm tính tổng dựa trên cùng ý tưởng tránh sao chép, nhưng không cho phép thay đổi danh sách qua tham số đó.

### Đáp án bài trace tham chiếu: hai tên và một bản sao giá trị

| Sau dòng | total | alias nhìn thấy | copied |
| --- | ---: | --- | --- |
| 1 | 0 | Chưa khai báo | Chưa khai báo |
| 2 | 0 | 0, cùng biến total | Chưa khai báo |
| 3 | 0 | 0 | 0 |
| 4 | 35000 | 35000 | 0 |

Kết quả mong đợi (suy ra từ mã, chưa phải kết quả chạy của người đọc) là `35000 0`. Giải thích được vì sao biến sao chép vẫn giữ giá trị 0 quan trọng hơn việc thuộc lòng định nghĩa tham chiếu.

### Lỗi biên dịch: thiếu dấu chấm phẩy và chương trình cũ

Đoạn sau là **đoạn mã lỗi cú pháp độc lập**, không phải lỗi có trong demo phát hành. Các tên `n` và `amounts` được giả định đã khai báo; dòng khởi tạo thiếu dấu chấm phẩy:

```cpp
long long total = 0
for (int i = 0; i < n; ++i) {
    total += amounts[i];
}
```

Compiler có thể báo lỗi dạng `expected ',' or ';' before 'for'`, với câu chữ cụ thể tùy phiên bản. Vị trí được chỉ vào `for` là nơi bộ phân tích cú pháp không thể tiếp tục, trong khi nguyên nhân nằm ở dòng ngay trước đó. Cần đọc tên tệp, số dòng, số cột và **thông báo lỗi đầu tiên**, rồi xem dòng phía trước đã kết thúc đầy đủ hay chưa. Các lỗi phía sau có thể chỉ là lỗi dây chuyền; không cần yêu cầu AI viết lại cả thuật toán.

Prompt mẫu khi hỏi AI về một lỗi biên dịch:

```text
Tôi gửi lệnh biên dịch, cwd và thông báo lỗi đầu tiên của C++.
Chỉ giải thích file, dòng, cột và phần mã cần kiểm tra.
Đề xuất sửa đổi nhỏ nhất; xem cả dòng trước vị trí compiler chỉ ra.
Không sửa thuật toán ngoài phạm vi, không nói chạy được khi chưa chạy.
```

Sau khi thêm `;`, phải lưu tệp và biên dịch lại. Nếu lần build thất bại nhưng vẫn còn executable từ lần build trước, việc chạy tệp đó có thể vẫn in ra 60000. Kết quả ấy chỉ cho biết bản cũ chạy được, không chứng minh mã vừa sửa là hợp lệ. Hướng dẫn build ở Bài thực hành 07 yêu cầu đọc mã thoát (exit code) của compiler trước khi chạy executable; không dán liền cả khối lệnh rồi chọn dòng output đẹp nhất.

### Hoàn tất bản vá và tách riêng validation

**Trước khi đổi cận**, tạo checkpoint bằng một bản sao tệp theo hướng dẫn ở Bài thực hành 06, ghi rõ đây là mốc trước khi sửa. Nếu đã lỡ sửa trước, giữ bản hiện tại và ghi đúng thời điểm; không dựng lại một lịch sử thao tác chưa từng diễn ra.

**Kết quả mong đợi.** Diff chỉ đổi `i < n - 1` thành `i < n`, vector ba khoản được giữ nguyên, bảng trace cho tổng 60000. Nếu có compiler, chạy theo hướng dẫn ở Bài thực hành 07; nếu không, ghi "chưa chạy, đã trace". Việc thử với một vector khác là một lượt riêng sau bản vá, và mỗi lượt đều phải biên dịch lại.

Bản đúng chặn danh sách có quá 500 khoản trước khi ép kiểu, kiểm tra số tiền `<= 0` hoặc `> 1000000000LL` và ném ngoại lệ `std::invalid_argument` nếu dữ liệu sai. Demo lỗi sau khi sửa cận **chưa có phần validation này**, nên không được ghi nhận là đạt các ca C7–C9. Chín test của bản đúng cũng không chạy trên mã demo lỗi vừa sửa.

**Lỗi thường gặp.** Thường là dùng `<=`, cộng bù phần tử cuối, thay cả tệp, cho rằng ca rỗng đạt là đủ, nhầm tham chiếu với bản sao, và chạy executable cũ. Cần giữ bảng trace, diff và trạng thái build để gắn kết luận với đúng phiên bản mã.

### Câu hỏi kiểm tra

Danh sách rỗng trả về 0 có chứng minh cận vòng lặp đúng không? Đổi cận đúng có làm khoản `-1` tự động bị từ chối không? Vì sao `i <= n` không phải là cách "chạy thêm một lượt cho đủ"?

### Đáp án Bài thực hành 03

Không. Với `int n = 0`, cả hai phiên bản đều không thực hiện lượt lặp nào. Đổi cận không bổ sung validation, vì vậy cần tách riêng việc kiểm tra miền dữ liệu. Điều kiện `i <= n` cho phép truy cập chỉ số nằm ngoài danh sách. Ca `[7000]` giúp phát hiện lỗi bỏ phần tử cuối, còn ca dữ liệu sai kiểm tra một trách nhiệm khác.

### Tiêu chí hoàn thành

Người học có đủ ba bảng trace; giải thích được hiện tượng tràn vòng không dấu, sự khác nhau giữa tham chiếu và bản sao, lỗi thiếu `;`; bản vá chỉ thay đổi cận vòng lặp. Nhật ký tách rõ phần đã chạy, phần dự đoán và phần validation chưa làm. Người học trình bày được khoản Vở ghi bị chặn ở đâu, đã sửa gì và còn thiếu bằng chứng nào.

## 2.4. Bài thực hành 04 (Mission 04) — Gỡ lỗi Web: lần theo dữ liệu thay vì đoán tên hàm

Bài này giúp người học theo dõi một giá trị từ ô nhập đến nơi lưu, để nhận ra chỗ dữ liệu đổi kiểu hoặc bị từ chối.

### Mục tiêu

Lần theo dữ liệu qua HTML, handler, API, nơi lưu trữ và kiểu dữ liệu ở từng chặng.

### Bối cảnh

Bản Web phát hành đang chạy đúng: khi chưa có dữ liệu lưu, ứng dụng nạp sẵn ba khoản mẫu với tổng **60000**. Vì vậy không nhập trùng ba khoản này rồi coi tổng 120000 là lỗi. Dù là demo đúng, đây vẫn là một bài học gỡ lỗi: mục tiêu là hiểu cơ chế xử lý, không phải tìm chỗ hỏng.

Lan thử nhập `35000abc`, kiểm tra cơ chế từ chối và thực hiện một bài thử lỗi cô lập (fault lab) riêng. Minh tham gia với vai trò **review chéo bài của Lan**, không ngầm đổi vai. Bài không thêm server, chức năng đăng nhập hay cơ sở dữ liệu; điểm nối với SQL được trình bày ở Chương 4.

### Các bước thực hiện

1. Giữ bốn tệp Web cùng nhau trong `bai-lam/nam-2-web`.
2. Mở trực tiếp `index.html` từ trình quản lý tệp bằng Chrome, Edge hoặc một trình duyệt phù hợp. Hai thẻ script ở cuối trang lần lượt nạp `data.js` rồi `app.js`, **không dùng module**, nên demo mở được qua `file://` mà không cần server. Nếu trang báo lỗi, kiểm tra vị trí tệp và Console trước, không vội thay đổi kiến trúc.
3. Mở Developer Tools bằng phím F12 rồi chọn thẻ Console. Nếu không được, dùng `Ctrl+Shift+I` trên Windows và Linux, `Cmd+Option+I` trên macOS, hoặc menu More tools → Developer tools; tên menu có thể khác nhau giữa các trình duyệt.

Console của trình duyệt không phải terminal Bash hay PowerShell trong IDE: các lệnh JavaScript dưới đây chạy trong Console, còn lệnh `node` chạy trong terminal.

### Mô hình dữ liệu và luồng xử lý

`Expense` có bốn trường: `id` là định danh của khoản chi giả, `title` là tên hiển thị, `amount` là số tiền và `category` là mã nhóm. [Hàm `sampleExpenses`](../vi-du/nam-2-web/data.js) trả về ba đối tượng sau:

```javascript
const expenses = [
  { id: 1, title: 'Cơm trưa', amount: 35000, category: 'an-uong' },
  { id: 2, title: 'Xe buýt', amount: 7000, category: 'di-lai' },
  { id: 3, title: 'Vở ghi', amount: 18000, category: 'hoc-tap' }
];
```

Đây là trích đoạn để đọc hiểu mô hình, không dán vào để thay biến nội bộ của ứng dụng. Số tiền không đặt trong dấu nháy; `id` không phải mã sinh viên. Đối tượng `categories` ánh xạ `hoc-tap` thành "Học tập". Mối liên hệ với lập trình hướng đối tượng nằm ở việc biểu diễn thực thể và giữ bất biến dữ liệu, không ở yêu cầu phải viết `class Expense` thì mới được coi là có mô hình.

Về cấu trúc dữ liệu và giải thuật, `totalExpenses` duyệt danh sách một lần nên có độ phức tạp thời gian **O(n)**; biến tổng và phần phụ trợ của chính hàm tổng dùng **O(1)** bộ nhớ thêm, không tính mảng đầu vào. Không gán O(1) cho cả ứng dụng: `normalizeExpenses` tạo mảng mới và một `Set` chứa các id, còn hàm render tạo các phần tử DOM. Thuật toán tính tổng đơn giản vẫn đòi hỏi đúng trường và đúng kiểu ở đầu vào.

| Chặng dữ liệu | Vị trí hoặc API thực tế | Kiểu và câu hỏi cần kiểm |
| --- | --- | --- |
| Ô nhập | `index.html`: form `expense-form`, input `id/name="amount"` | `type="text"`, `inputmode="numeric"`; giá trị đọc là chuỗi |
| Nhận submit | `app.js`: `form.addEventListener('submit', event => ...)` | Handler vô danh, `event` là đối tượng sự kiện |
| Chặn gửi mặc định | `app.js`: `event.preventDefault()` | Không để hành vi submit mặc định điều hướng trang |
| Parse tiền | `D.parseAmount(form.elements.amount.value)` | Chuỗi qua kiểm tra thành số hợp lệ, hoặc ném lỗi |
| Tạo khoản | `app.js`: `{ id, title, amount, category }` | Chọn id chưa dùng, đưa vào `D.normalizeExpenses` |
| Tính tổng | `data.js`: `totalExpenses(expenses)` | Kiểm mảng, số lượng và phần tiền |
| Hiển thị, lưu | `app.js`: `render()`, `save()` | `textContent`, định dạng số, localStorage hoặc bộ nhớ |

`data.js` công bố API qua `globalThis.ViData` cho trình duyệt và qua `module.exports` cho Node.js. `app.js` đặt tên ngắn `D` cho API đó. `test_data.cjs` dùng `require('./data.js')` và không giữ một bản sao logic riêng. Do đó thứ tự nạp script rất quan trọng: khi `app.js` lấy `globalThis.ViData`, API phải đã được nạp.

Handler submit không có tên, nên cần mô tả là "hàm vô danh gắn vào sự kiện submit của form", không bịa ra tên `handleSubmit`. Hàm này lần lượt kiểm tra số lượng và title, parse số tiền, lấy category, dùng `Set` để chọn id nhỏ nhất còn trống, gọi normalize trên danh sách mới rồi mới gán lại `expenses`. Nếu có lỗi xảy ra trước phép gán, khối `catch` hiển thị thông báo và danh sách cũ không bị thêm khoản sai. Đây là lý do phải lần theo đúng thứ tự thực thi, thay vì chỉ thấy một khối `try/catch` rồi kết luận chung chung là "đã an toàn".

### Prompt mẫu

Prompt sau yêu cầu AI lần theo giá trị `35000abc` qua các chặng xử lý:

```text
Chỉ đọc bai-lam/nam-2-web/index.html, app.js, data.js; không sửa/chạy.
Demo đúng đã có ba khoản mẫu 60000 khi chưa có dữ liệu lưu.
Nếu nhập title giả hợp lệ, amount là 35000abc và gửi form,
hãy lần theo phần tử thật, handler vô danh, parseAmount và catch.
Chỉ ra nơi từ chối, kiểu dữ liệu và vì sao tổng không được đổi.
Phân biệt totalExpenses kiểm phần tiền với normalizeExpenses kiểm schema.
Không thêm server/dependency, không chèn fault lab vào demo đúng.
```

### Phân tích: chuỗi trông giống số chưa phải là số

`input.value` trả về chuỗi, kể cả với nhiều ô nhập `type="number"`; demo thực tế dùng `type="text"`, không phải ô số. Thuộc tính `inputmode="numeric"` chỉ gợi ý loại bàn phím, không thay thế bộ kiểm tra dữ liệu. Đoạn thử nghiệm sau chạy độc lập trong Console và không thêm khoản nào vào ứng dụng. Cặp ngoặc `{ ... }` giữ các biến minh họa trong một phạm vi riêng để có thể chạy lại nhiều lần.

```javascript
{
  const first = '35000';
  const second = '7000';
  console.log(first + second);
  console.log(typeof first);
}
```

Kết quả mong đợi là `350007000` rồi `string`: toán tử `+` nối hai chuỗi chứ không cộng tiền. Chỉ gọi `Number` cũng chưa đáp ứng hợp đồng, vì chuỗi rỗng hoặc chuỗi dạng số mũ có thể được chuyển thành giá trị số dù nằm ngoài cú pháp nhập cho phép. `parseInt('35000abc', 10)` trả về 35000 do chỉ đọc phần đầu chuỗi; hàm này không xác nhận toàn bộ chuỗi là một số tiền hợp lệ.

API `parseAmount(input)` trước hết yêu cầu `typeof input === 'string'`. Sau `trim()`, biểu thức chính quy **`/^[0-9]+$/`** buộc toàn bộ chuỗi chỉ gồm chữ số và có ít nhất một chữ số: `^` neo đầu chuỗi, `$` neo cuối chuỗi, `[0-9]` khớp một chữ số, còn `+` yêu cầu có ít nhất một ký tự như vậy. `trim()` chỉ bỏ khoảng trắng ở hai đầu, không xóa khoảng trắng ở giữa như trong `35 000`. Chỉ sau khi kiểm tra dạng chuỗi, hàm mới gọi `Number`, rồi kiểm tra `Number.isSafeInteger` và miền giá trị dương tới `MAX_AMOUNT`.

JavaScript có miền số nguyên an toàn từ -9007199254740991 đến 9007199254740991; tổng cực đại 500000000000 của bài nằm trong miền đó. Tuy nhiên, điều kiện `typeof value === 'number'` chưa đủ, vì số thập phân, `NaN` và `Infinity` cũng cần bị loại. Hợp đồng đầy đủ của phép parse là sự kết hợp giữa cú pháp chuỗi, tính nguyên an toàn và miền giá trị nghiệp vụ.

Đoạn Console dưới đây dùng **API thật mà trang đã nạp** và vẫn không thay đổi danh sách:

```javascript
{
  const D = globalThis.ViData;
  const amount = D.parseAmount(' 35000 ');
  console.log(amount, typeof amount);
  try {
    D.parseAmount('35000abc');
    console.log('Không đạt: đầu vào sai đã lọt qua');
  } catch (error) {
    console.log('Đã từ chối:', error.message);
  }
}
```

Kết quả mong đợi là `35000 number` và một thông báo từ chối. Sau đó thử qua form với title giả hợp lệ, category hợp lệ và số tiền `35000abc`: phải xuất hiện thông báo lỗi, còn số khoản và tổng giữ nguyên. Cần ghi lại tổng **trước** thao tác để không nhầm với dữ liệu đã lưu từ trước. Kiểm tra hàm trực tiếp và kiểm tra qua form là hai bằng chứng khác nhau; một ô nhập ngăn gõ chữ cũng chưa chứng minh API tự kiểm tra đầy đủ.

### Bài thử lỗi cô lập (fault lab): thiếu trường value, tổng thành NaN

Đoạn sau **cố ý chứa lỗi ánh xạ trường**; đây không phải lỗi có trong `data.js` và cũng không phải yêu cầu sửa demo Web. Dữ liệu được rút gọn chỉ còn trường tiền, không phải Expense đầy đủ. Hãy tự dự đoán giá trị của `x.value` và của biến tổng trước khi chạy trong Console.

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

### Đáp án bài thử lỗi cô lập: undefined không phải NaN

| Lượt | amount của x | x.value | sum trước | Phép cộng | sum sau |
| --- | ---: | --- | --- | --- | --- |
| 1 | 35000 | `undefined` | 0 | `0 + undefined` | `NaN` |
| 2 | 7000 | `undefined` | `NaN` | `NaN + undefined` | `NaN` |
| 3 | 18000 | `undefined` | `NaN` | `NaN + undefined` | `NaN` |

Truy cập một thuộc tính không tồn tại trả về `undefined`; phép cộng với giá trị đó cho kết quả `NaN` (viết tắt của Not-a-Number). Kết quả mong đợi là `NaN`, `true`, `60000`. `typeof NaN` vẫn là `"number"`; cần dùng `Number.isNaN` để nhận diện NaN và không coi `undefined` với `NaN` là một khái niệm. Đổi sang `x.amount` sửa được lỗi ánh xạ trong bài thử, nhưng phép `reduce` đó vẫn chưa kiểm tra số lượng hay miền giá trị tiền; ứng dụng thật vẫn phải dùng API có kiểm tra.

Ba biểu hiện 42000, 350007000 và NaN gợi ý ba giả thuyết khác nhau: bỏ sót phần tử, nối chuỗi, và nhận một trường hoặc giá trị không dùng được như số. Đó chưa phải là chẩn đoán có thể rút ra chỉ từ màn hình; cần xem đầu vào, kiểu dữ liệu, mã nguồn và trạng thái dữ liệu để chọn phép thử phân biệt được các giả thuyết.

### Ranh giới schema và ca kiểm thử hồi quy

`totalExpenses` kiểm tra đầu vào là mảng, có tối đa 500 phần tử và từng `amount` hợp lệ. Hàm này **không kiểm tra đủ bốn trường** của Expense; vì vậy `[{ amount: 7000 }]` vẫn đủ để kiểm tra riêng hàm tổng. `normalizeExpenses` mới là nơi kiểm tra schema: id là số nguyên an toàn dương và không trùng; title là chuỗi không rỗng sau khi `trim`, dài tối đa 80 ký tự; category là chuỗi thuộc tập giá trị cho phép; số tiền hợp lệ. Hàm trả về một danh sách đối tượng mới đã được chuẩn hóa.

Ranh giới này minh họa một lỗi điển hình. Nếu chỉ kiểm tra bằng `Object.hasOwn(categories, item.category)`, giá trị `category: ['khac']` sẽ lọt qua, vì mảng bị chuyển thành khóa chuỗi `khac` khi tra cứu thuộc tính. `data.js` chặn trường hợp này bằng điều kiện **`typeof item.category !== 'string'`** trong nhánh từ chối, và `test_data.cjs` có một regression test riêng cho category là mảng. Demo hiện tại đã có điều kiện này, nên người học không cần sửa lại.

**Hồi quy** (regression) là tình trạng một hành vi đã được sửa đúng bị phá hỏng trở lại khi mã nguồn thay đổi. **Ca kiểm thử hồi quy** (regression test) giữ lại chính phản ví dụ cụ thể đã làm lộ lỗi, chứ không chỉ thêm một ca thuận lợi với category là chuỗi. Quy trình nghề nghiệp khi phát hiện lỗi gồm ba bước: viết ca kiểm thử tái hiện lỗi và xác nhận ca đó thất bại (bộ test kết thúc với exit code 1) trước khi vá; vá mã và xác nhận ca đó chuyển sang đạt; giữ ca đó lâu dài trong bộ kiểm thử. Bộ `test_data.cjs` hiện tại gồm 34 ca, trong đó có ca category mảng, và kết quả mong đợi là **34 passed, 0 failed**. Khi dùng con số này trong báo cáo, cần ghi rõ đó là kết quả mong đợi nêu trong sách hay là kết quả người học vừa tự chạy lại trên bản hiện tại.

### Lưu cục bộ: khả năng mở trang khác với lưu bền vững

`app.js` khởi tạo danh sách bằng `D.sampleExpenses()`, sau đó thử đọc khóa `visinhvien-demo-v1` trong localStorage. Nếu có dữ liệu, ứng dụng gọi `JSON.parse` và `normalizeExpenses` để kiểm tra trước khi dùng. Nếu việc đọc hoặc chuẩn hóa thất bại, ứng dụng giữ dữ liệu mẫu trong bộ nhớ, đặt `persistent = false`, hiển thị cảnh báo và không ghi đè dữ liệu cũ. Nếu việc ghi thất bại do bị chặn hoặc hết dung lượng, ứng dụng cũng chuyển sang lưu tạm trong bộ nhớ.

Việc mở được trang qua `file://` mà không cần server **không có nghĩa là localStorage được bảo đảm trên mọi trình duyệt**. Hành vi lưu khi mở tệp trực tiếp khác nhau tùy trình duyệt và chính sách bảo mật. Dữ liệu không đồng bộ giữa các máy và không gắn với tài khoản hay cơ sở dữ liệu máy chủ. Cơ chế dự phòng lưu trong bộ nhớ (RAM) cho phép tiếp tục thao tác, nhưng tải lại trang có thể làm mất thay đổi. Nút Khôi phục mẫu thay dữ liệu bằng ba khoản mẫu sau khi người dùng xác nhận; nút này không bật lại khả năng lưu khi `persistent` đã là false trong phiên làm việc.

Để quan sát hợp lệ, cần ghi lại việc có xuất hiện cảnh báo hay không, thêm một khoản giả rồi tải lại trang và đối chiếu. Nếu cần tái tạo trạng thái 42000, xóa riêng khoản Vở ghi trên **bài làm** rồi thêm lại 18000 với nhóm Học tập, hoặc dùng một mảng thử nghiệm riêng. Không diễn giải việc chủ động xóa một khoản là lỗi bỏ sót phần tử. Nút Khôi phục mẫu thay toàn bộ danh sách, nên chỉ dùng khi chắc chắn dữ liệu giả hiện tại có thể bỏ đi.

**Kết quả mong đợi.** Sơ đồ luồng dữ liệu ghi rõ kiểu ở từng chặng; thao tác thử `35000abc` không làm thay đổi tổng; báo cáo về lưu trữ đúng với mức đã quan sát.

**Lỗi thường gặp.** Thường là nhập trùng dữ liệu mẫu, bịa tên handler, lạm dụng `parseInt`, nhầm `NaN` với `undefined`, và nhầm môi trường Node.js với trình duyệt. Nếu không tái hiện được cơ chế dự phòng, ghi là chưa kiểm tra; không tắt cơ chế bảo vệ để thử.

### Câu hỏi kiểm tra

Thuộc tính `inputmode` có thay thế được biểu thức chính quy không? Hàm tổng có kiểm tra đủ schema không? Nút Khôi phục mẫu có phục hồi quyền lưu đã bị chặn không? Xác định bên nào chịu trách nhiệm kiểm tra từng điều.

### Đáp án Bài thực hành 04

Cả ba câu đều có câu trả lời là không. `inputmode` không thay thế validation; hàm tổng chỉ kiểm tra phần tiền và số lượng, còn `normalizeExpenses` mới kiểm tra schema. Nút Khôi phục mẫu thay dữ liệu bằng bộ mẫu nhưng không đảo cờ `persistent` đã là false. Việc kiểm tra DOM và lưu trữ phải thực hiện trên trình duyệt, tách biệt với việc kiểm tra logic bằng Node.js.

### Tiêu chí hoàn thành

Người học chỉ ra đúng luồng xử lý và API; giải thích được các chuyển đổi chuỗi → số, `undefined` → `NaN` và ca hồi quy category. Nhật ký ghi lại trạng thái trước và sau, cơ chế từ chối và tình trạng lưu trữ. Vì đây là demo đúng, sản phẩm nộp là bằng chứng phân tích kèm ghi chú **"không thay đổi mã"**.

## 2.5. Bài thực hành 05 (Mission 05) — Giao cho Agent một công việc có giới hạn

Bài này giúp người học viết một bản giao việc đủ rõ để Agent chỉ làm đúng phần được phép.

### Mục tiêu

Giao việc cho Agent với phạm vi và yêu cầu bằng chứng rõ ràng. Quyền càng mạnh thì hợp đồng giao việc càng phải rõ.

### Bối cảnh

Agent đề nghị sửa cận vòng lặp, đồng thời định dạng lại toàn bộ dự án và cài một thư viện xử lý tiền. Lan đặt câu hỏi vì sao API đang có lại chưa đủ. Nguyên tắc ở đây là phần đề xuất hữu ích không hợp thức hóa phần nằm ngoài phạm vi.

Nhiệm vụ là viết hợp đồng cho một bản vá, thực hiện bước quan sát (Observe) và lập kế hoạch (Plan) trước bước hành động (Act). Nếu đã tự sửa ở Bài thực hành 03, dùng diff và checkpoint để **mô phỏng** việc giao việc; không làm hỏng lại bài và không ghi nhận như thể Agent đã thực thi.

### Quy trình Observe → Plan → Act → Test → Review

**Observe** (quan sát) là thu thập mã, dữ liệu, thông báo lỗi và trạng thái môi trường. **Plan** (lập kế hoạch) là nêu giả thuyết, các tệp dự kiến thay đổi, phép thử và những điều chưa biết. **Act** (hành động) là thực hiện thay đổi đã được cho phép. **Test** (kiểm thử) là kiểm tra giả thuyết bằng ca thông thường, ca biên và việc đọc kết quả. Sau cùng, người học **Review** (rà soát) diff và bằng chứng để quyết định có nhận thay đổi hay không. Các bước này là một mô hình tư duy; giao diện công cụ không nhất thiết hiển thị đúng năm nhãn như vậy.

![Luồng cộng tác: Ask để hiểu, phân tích và sửa có giới hạn, kiểm thử rồi review; nếu test sai phải quay lại quan sát.](../assets/workflow.svg)

| Bước | Việc với tình huống 42000 | Bằng chứng cần giữ |
| --- | --- | --- |
| Observe | Đọc vector và `i < n - 1`, xác định `int n` | Tệp, đoạn mã, output thật hoặc trace có nhãn |
| Plan | Giả thuyết bỏ khoản cuối; chỉ sửa cận | Dự đoán cho ca rỗng, một khoản, ba khoản |
| Act | Đổi thành `i < n` ở đúng bài làm | Diff nhỏ và trạng thái đã lưu |
| Test | Biên dịch rồi chạy đúng executable; thử ca phân biệt | Cwd, shell, lệnh, output, exit code hoặc lý do chưa chạy |
| Review | So yêu cầu, diff và kết quả | Quyết định nhận hoặc từ chối, phần còn chưa kiểm |

Một phép thử thất bại không phải là lý do để bỏ ca khó. Nếu tổng đã đúng nhưng khoản âm chưa bị chặn, cần ghi rằng bản vá cận đạt mục tiêu hẹp, còn validation chưa được triển khai. Không sửa giá trị kỳ vọng (expected) cho khớp với kết quả thực tế (actual) sai, không xóa assertion và không che giấu lượt thất bại. Mỗi lần quay lại bước Observe phải dựa trên dữ kiện mới, không thay đổi mã một cách ngẫu nhiên cho tới khi màn hình báo đạt.

### Prompt mẫu

Prompt sau đóng vai trò hợp đồng giao việc trước khi chuyển sang chế độ Agent:

```text
Workspace mở ở gốc AI-Student-Handbook. Dữ liệu hoàn toàn giả.
Chỉ được sửa bai-lam/nam-1-cpp/loi-bo-sot.cpp nếu bản vá chưa có.
Mục tiêu giai đoạn 1: sửa cận để ba khoản 35000, 7000, 18000 ra 60000.
Trước mắt chỉ Observe và Plan; chưa sửa, chưa chạy lệnh.
Nêu nguyên nhân, đúng dòng dự kiến đổi và dự đoán ca 0, 1, 3 khoản.
Giữ vector mẫu; không thêm validation trong bản vá cận này.
Không sửa vi-du, Web hoặc bài người khác; không đọc ngoài phạm vi cần thiết.
Không cài dependency, đổi cấu hình/quyền, tạo key, commit, publish hay triển khai.
Nếu bị chặn, dừng và báo; không thử đường vòng để vượt chặn.
Sau khi tôi đồng ý bước tiếp theo, báo diff, test thật, lượt fail và phần chưa kiểm.
Không coi prompt này là cơ chế khóa quyền kỹ thuật.
```

Chỉ chuyển từ Ask sang Agent khi đã mô tả được lỗi, biết tệp nào sẽ thay đổi và đã có dự đoán. Trong IDE, xem chính sách **Settings → Chat → Auto-Run → Terminal** theo tài liệu; không mặc định rằng mọi lệnh đều chờ xác nhận và không tự thay đổi cài đặt này.

Khi bị chặn hoặc quyền hạn không rõ ràng thì dừng lại; không nới quyền hay chuyển sang công cụ khác để vượt qua hàng rào. Đường dẫn Settings nêu trên không áp dụng cho Qoder Desktop và Qoder CLI. Quyền, tài khoản và công cụ hiện có trên máy người học là thông tin *chưa kiểm chứng*.

### Kiểm tra dependency thay vì cài đặt

**Dependency** (thành phần phụ thuộc) là thành phần phần mềm mà dự án cần để hoạt động. Bản Web thuần này chỉ dùng API của trình duyệt, còn bộ test dùng `node:assert/strict`, một mô-đun có sẵn của Node.js; các bài trong chương không cần `npm install`. Việc dùng `require` không tự nhiên có nghĩa là đang dùng gói của bên thứ ba. Cần đọc đường dẫn và tên mô-đun trước khi kết luận dự án thiếu dependency.

Trong tình huống minh họa, Agent đưa ra tên một gói lạ và đề nghị chạy lệnh cài đặt. Quyết định phù hợp là yêu cầu nêu lý do cần gói, chỉ ra chức năng hiện có chưa đáp ứng ở điểm nào và đưa ra phương án không thêm gói. Nếu một nhiệm vụ khác thực sự cần dependency, phải kiểm tra đúng registry, tên gói, nhà phát hành, kho mã nguồn, phiên bản, giấy phép, các phụ thuộc bắc cầu, script chạy khi cài, cùng thay đổi trong manifest và lockfile. Việc gói có trang giới thiệu hoặc có nhiều lượt tải không đủ để chứng minh gói đó an toàn.

Khi chưa kiểm tra, ghi là "dependency chưa xác minh"; không gọi gói đó là độc hại chỉ vì lạ, cũng không cài thử để xem có gì. Không dùng lệnh tải mã từ mạng rồi chuyển thẳng cho shell thực thi. Việc kiểm tra dependency chi tiết được mở rộng ở Chương 4; ở bài này, lựa chọn đúng là giữ bài làm không phát sinh thành phần không cần thiết. Chủ động không thể hiện ở việc cài thêm gói.

**Kết quả mong đợi.** Kế hoạch có điểm dừng, phạm vi quyền và phép thử.

**Lỗi thường gặp.** Thường là giao việc kiểu "làm tốt nhất có thể", để Agent sửa cả dự án, nhầm prompt với cơ chế cô lập (sandbox), và coi lời hứa của AI là nhật ký thực thi. Thiếu compiler không phải là lý do để tự cài đặt.

### Câu hỏi kiểm tra

Nên nhận bản vá cùng với thay đổi Auto-Run và dependency, hay tách riêng từng việc? Có nên xóa ca khoản âm đang thất bại để hoàn thành giai đoạn 1 không? Phần đề xuất hữu ích có hợp thức hóa phần thừa không?

### Đáp án Bài thực hành 05

Cần tách bản vá cận khỏi thay đổi quyền và dependency, vì hai việc sau nằm ngoài phạm vi. Giữ ca khoản âm và ghi rằng đó là phép kiểm validation chưa được triển khai trong demo lỗi; không xóa ca này và không báo toàn chương đã đạt. Có thể ghi nhận hoàn thành mục tiêu hẹp khi có bằng chứng rõ, nhưng không nhận mục tiêu rộng hơn khi chưa thực hiện.

### Tiêu chí hoàn thành

Người học viết được hợp đồng giao việc, chỉ ra điểm phải dừng trước bước Act, phân biệt chế độ Ask và Agent trong IDE với Qoder Desktop và Qoder CLI, và từ chối phần cài đặt không cần thiết. Nhật ký ghi rõ thao tác nào được thực hiện thật, thao tác nào là mô phỏng, phép thử nào chưa thực hiện. Năng lực kiểm soát thể hiện ở những quyết định có lý do, không ở số lần nhấn chấp nhận.

## 2.6. Bài thực hành 06 (Mission 06) — Đọc diff và giữ đường quay lại

Bài này giúp người học quyết định nhận hay từ chối một thay đổi dựa trên nội dung thật của nó, và luôn có đường quay lại.

### Mục tiêu

Rà soát thay đổi bằng bốn câu hỏi và giữ checkpoint để có thể quay lại trạng thái trước.

### Bối cảnh

Một diff sửa đúng cận vòng lặp nhưng đồng thời bỏ phần kiểm tra category và thêm cấu hình tự động chạy lệnh. Tổng 60000 đúng không làm lộ ra mọi hậu quả của thay đổi. Trạng thái "đã sửa" vì thế chưa đồng nghĩa với "chấp nhận".

Nhiệm vụ là tách bản vá hợp lệ khỏi phần vượt phạm vi. **Diff** là bản thể hiện khác biệt giữa trạng thái trước và sau của tệp; khi đọc diff cần đọc nội dung các dòng được thêm và bị xóa, không chỉ nhìn màu sắc hoặc số dòng. Chỉ một dòng bỏ phép kiểm tra cũng có thể gây hồi quy.

### Các bước thực hiện

**Tạo checkpoint trước khi sửa.** Dùng trình quản lý tệp tạo checkpoint trong `bai-lam/checkpoints/`: đặt một thư mục mốc có tên rõ nghĩa như `moc-01-truoc-can`, rồi sao chép các tệp bài làm cần giữ vào đó. Nếu đã sửa cận, bản chụp hiện tại là bản **sau khi sửa**; cần đặt tên tương ứng, không ghi nhận nó là bản trước khi sửa. Ghi thời điểm và nội dung của mốc vào nhật ký. Checkpoint là một bản chụp riêng: **không đổi tên hai nhánh bài làm**, không thay đổi cwd và không biến thư mục checkpoint thành nơi chạy lệnh chính.

Bản gốc trong `vi-du` giúp đối chiếu ban đầu, còn checkpoint giữ phần việc người học đã làm trước lượt sửa; hai thứ không thay thế nhau. Người đã học Git có thể dùng quy trình checkpoint được lớp hướng dẫn, nhưng chương không yêu cầu tự tạo commit. Không tự tạo commit hoặc đẩy mã lên dịch vụ bên ngoài chỉ để lưu một bản vá học tập.

**Xem thay đổi.** Diff nghe có vẻ kỹ thuật nhưng thực chất là danh sách "dòng nào bị bỏ, dòng nào được thêm"; chỉ cần đọc chậm từng dòng là đủ. Trong Qoder IDE, dùng **View Changes** (tùy phiên bản) để xem đề xuất và quyết định chấp nhận (accept) hoặc từ chối (reject). Nếu tự sửa bằng tay, so sánh tệp trước và sau bằng công cụ so sánh của IDE hoặc đặt cạnh checkpoint để đọc. Dù dùng cách nào, luôn trả lời bốn câu hỏi:

1. **Tệp nào thay đổi?** Tệp đó có nằm trong bài làm và trong phạm vi đã đồng ý không?
2. **Dòng nào thay đổi?** Nội dung bị xóa và nội dung được thêm là gì, thay vì chỉ xem màu nào nhiều hơn?
3. **Thay đổi liên quan đến lỗi như thế nào?** Bảng trace hoặc phép thử nào giải thích thay đổi này?
4. **Thay đổi có ảnh hưởng đến hợp đồng dữ liệu không?** Kiểu, miền giá trị, số lượng, schema hay hành vi từ chối có thay đổi không?

Diff dưới đây **minh họa một thay đổi đúng phạm vi**, chỉ mô tả dòng điều kiện lặp; đây không phải lệnh để chạy:

```diff
-    for (int i = 0; i < n - 1; ++i) {
+    for (int i = 0; i < n; ++i) {
```

Tệp thay đổi phải là `bai-lam/nam-1-cpp/loi-bo-sot.cpp`. Lý do thay đổi là chỉ số cuối cần được duyệt, còn chỉ số `n` phải bị chặn. Hợp đồng tiền không đổi; validation vẫn là phần mở rộng. Nếu diff còn sửa `vi_sinh_vien.cpp`, mã Web, test, quyền hoặc dependency, cần yêu cầu tách riêng và giải trình trước khi chấp nhận. Không "chấp nhận tất cả rồi tính sau" khi chưa biết cách hoàn nguyên từng phần.

### Prompt mẫu

Prompt sau yêu cầu AI chỉ rà soát, không tự sửa thêm:

```text
Chỉ review diff và checkpoint tôi cung cấp; không sửa hoặc chạy lệnh.
Phạm vi được giao: cận vòng lặp trong bai-lam/nam-1-cpp/loi-bo-sot.cpp.
Trả lời bốn câu: file nào, dòng nào, liên quan lỗi ra sao,
ảnh hưởng hợp đồng dữ liệu thế nào.
Đánh dấu riêng thay đổi dependency, test, cấu hình/quyền và tệp ngoài phạm vi.
Không coi accept là chứng nhận đúng; nêu test hồi quy cần giữ.
Nếu bản sửa không ổn, đề xuất phục hồi có chọn lọc, không ghi đè bài khác.
```

Chấp nhận (accept) chỉ là nhận thay đổi, không phải chứng nhận tính đúng. Từ chối (reject) không phải là bản sao dự phòng và không bảo đảm hoàn nguyên mọi thao tác đã chạy bên ngoài đề xuất. Người học cần biết tệp nào đang được lưu trên đĩa, checkpoint được chụp lúc nào và executable nào sẽ được chạy. Nếu bài nhóm có thay đổi khác diễn ra cùng lúc, cần trao đổi với người phụ trách phần đó theo quy trình của nhóm thay vì ghi đè cả thư mục.

### Nhật ký thất bại: giữ nguyên lịch sử để có thể truy vết

Khi một bản sửa không ổn, trình tự xử lý là dừng lại, giữ bằng chứng, so sánh với checkpoint, khôi phục có chọn lọc rồi kiểm tra lại. Không xóa hàng loạt và không ghi đè bài của người khác. Cần lưu ý rằng khôi phục mã nguồn không tự khôi phục quyền của trình duyệt, dữ liệu localStorage hay trạng thái của các tiến trình.

Trong thực hành nghề nghiệp, nhật ký làm việc phải phản ánh đúng những gì đã xảy ra, kể cả các lượt thất bại. Một lịch sử chỉ gồm các lượt thành công tạo ấn tượng gọn gàng nhưng làm mất thông tin cần thiết để chẩn đoán, để viết ca kiểm thử hồi quy và để người khác kiểm chứng lại. Mẫu nhật ký dưới đây được ghi vào `bai-lam/nam-1-cpp/ghi-chep-02.txt` hoặc tệp ghi chép của nhánh Web:

```text
Phạm vi được mở và tệp được phép đổi:
Cwd, shell, công cụ/phiên bản nếu đã kiểm:
Checkpoint trước sửa, thời điểm và nội dung:
Input; expected; actual trước sửa (hoặc trace, chưa chạy):
File/dòng đổi, lý do theo bốn câu hỏi:
Lệnh hoặc thao tác kiểm tra; executable/tệp test thực tế:
Stdout, stderr liên quan; exit code nếu có:
Lượt thất bại: input, expected, actual, bước xử lý tiếp:
Kết quả sau sửa và quyết định nhận/từ chối:
Phần chưa chạy/chưa xác minh; nguồn AI hỗ trợ và phần tự làm:
```

Cần giữ lỗi đầu tiên, đầu vào, giá trị kỳ vọng và giá trị thực tế; không nhất thiết phải lưu toàn bộ log. Che thông tin cá nhân và bí mật trước khi chia sẻ, nhưng không làm sai lệch dữ kiện cần cho chẩn đoán.

Ca category mảng ở Bài thực hành 04 minh họa giá trị của nguyên tắc này: ca kiểm thử ra đời từ một lượt thất bại thật và tiếp tục bảo vệ hành vi đúng sau khi đã vá. Nếu một diff xóa điều kiện `typeof` hoặc xóa regression test đó, schema có thể yếu đi trở lại trong khi tổng mẫu vẫn là 60000. Việc rà soát vì thế phải bảo vệ cả những hành vi đã đúng.

**Kết quả mong đợi.** Quyết định chấp nhận hoặc từ chối có lý do; đường quay lại rõ ràng.

**Lỗi thường gặp.** Thường là coi View Changes là checkpoint, nhận cả diff vì có một dòng đúng, xóa test khó, và chỉ giữ các lượt thành công. Mỗi quyết định phải gắn với phạm vi và phép thử cụ thể.

### Câu hỏi kiểm tra

Một diff sửa đúng cận vòng lặp nhưng xóa regression test cho `category` là mảng, trong khi các test còn lại đều đạt. Có thể ghi nhận "không có hồi quy" không? Checkpoint tạo từ hôm qua có chắc giữ được phần vừa viết sáng nay không? Khi nào phải dừng việc nhận thay đổi?

### Đáp án Bài thực hành 06

Không thể ghi nhận "không có hồi quy" khi phản ví dụ bảo vệ hành vi đúng đã bị xóa mà không có lý do hợp lệ; đây là lúc phải dừng việc nhận thay đổi. Cần yêu cầu giữ lại test và loại bỏ phần thay đổi ngoài phạm vi. Checkpoint chỉ giữ trạng thái tại thời điểm chụp; cần biết thời điểm đó và so sánh với phần việc mới hơn, không khôi phục toàn bộ thư mục một cách mù quáng.

### Tiêu chí hoàn thành

Người học có checkpoint được xác định rõ, câu trả lời cho bốn câu hỏi về diff, nhật ký giữ cả lượt thất bại nếu có, và quyết định chấp nhận hoặc từ chối không vượt phạm vi. Nếu chưa có lượt thất bại thật, ghi "chưa phát sinh", không bịa ra một lịch sử sửa lỗi. Người học giải thích được cách quay lại trạng thái trước mà không làm mất bài của người khác.

## 2.7. Bài thực hành 07 (Mission 07) — Nghiệm thu bằng lệnh, ca biên và lời giải thích

Bài này giúp người học kết luận đúng phạm vi: điều gì đã được kiểm tra, bằng cách nào, và điều gì còn chưa.

### Mục tiêu

Lập báo cáo nghiệm thu nêu rõ giới hạn của những gì đã kiểm tra.

### Bối cảnh

Minh đã có bản vá cận vòng lặp, Lan có demo đúng; tuy vậy, chưa thể khẳng định mọi thứ đã được kiểm tra. Nhiệm vụ cuối chương gồm: build và chạy chương trình nếu đủ công cụ, đối chiếu với các bảng ca kiểm thử C, W, T, thử trên trình duyệt, tự chấm điểm và nêu rõ phần chưa kiểm tra. Mục tiêu không phải là làm cho mọi phép thử báo đạt bằng mọi giá.

### Các bước thực hiện: kiểm tra môi trường và đọc ba loại bằng chứng

Mọi lệnh dưới đây chạy ở **thư mục gốc `AI-Student-Handbook`**, không chuyển cwd vào nhánh con. Kiểm tra bằng `pwd` trong Bash hoặc `Get-Location` trong PowerShell và xác nhận nhìn thấy thư mục `bai-lam` trước khi tiếp tục. Kiểm tra `g++ --version` hoặc `node --version` tùy theo nhánh. Nếu không tìm thấy công cụ, dừng phần chạy tương ứng và ghi "chưa thực hiện vì thiếu công cụ"; có thể tham khảo [GCC](https://gcc.gnu.org/), [MSYS2](https://www.msys2.org/) hoặc [Node.js](https://nodejs.org/) theo quy định của máy, không yêu cầu Agent tự cài.

**Stdout** là luồng kết quả thông thường; **stderr** thường chứa thông tin chẩn đoán lỗi. Terminal có thể hiển thị hai luồng xen kẽ nhau, nên ảnh chụp màn hình không phải lúc nào cũng phân biệt được nguồn của từng dòng. **Exit code** (mã thoát) là trạng thái mà tiến trình trả về khi kết thúc: theo quy ước, 0 là thành công, giá trị khác 0 là thất bại. Tuy vậy vẫn phải đọc kết quả đã in ra, vì một chương trình có lỗi thuật toán vẫn có thể trả về 0 khi chương trình không tự kiểm tra kết quả.

| Bằng chứng | Bash, gồm Git Bash | PowerShell | Cách đọc |
| --- | --- | --- | --- |
| Stdout | Đọc output của lệnh | Đọc output của lệnh | Tổng hoặc dòng PASS, không tự chứng minh đủ ca |
| Stderr | Đọc chẩn đoán của lệnh | Đọc chẩn đoán của lệnh | Compiler error hoặc FAIL; không bỏ qua vì có stdout đẹp |
| Exit code lệnh ngoài | `echo $?` ngay sau lệnh | `$LASTEXITCODE` ngay sau lệnh | Ghi riêng mã của compiler, chương trình, test |
| Cwd | `pwd` | `Get-Location` | Phải là gốc chứa `bai-lam` |

Trong Bash, một lệnh chen vào giữa có thể thay đổi `$?`; trong PowerShell, `$LASTEXITCODE` là mã thoát của chương trình ngoài chạy gần nhất, không phải kết quả của mọi cmdlet. Vì vậy cần đọc và ghi mã thoát ngay sau lệnh cần kiểm tra. Thông báo "không tìm thấy lệnh" hay "không tìm thấy tệp" có nghĩa là phép thử chưa chạy được, không phải phép thử đã trả về kết quả đạt.

### Build và chạy C++: hai executable, hai mục đích

Để tránh nhầm tên giữa các shell, chương đặt tên tệp đầu ra có phần mở rộng `.exe` trong cả hai cột. Trên Bash của hệ Unix, đây vẫn có thể là tên của một tệp thực thi; định dạng thực tế do compiler và nền tảng quyết định, không do phần mở rộng. Tùy chọn `-std=c++17` chọn chuẩn ngôn ngữ, `-Wall -Wextra` bật cảnh báo, còn `-o` chỉ đường dẫn của tệp đầu ra.

**Bash, cwd là thư mục gốc. Chạy từng dòng; nếu mã thoát của bước biên dịch khác 0, dừng trước dòng chạy chương trình:**

```bash
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/loi-bo-sot.cpp" -o "bai-lam/nam-1-cpp/loi-bo-sot.exe"
echo $?
./bai-lam/nam-1-cpp/loi-bo-sot.exe
echo $?
```

**PowerShell, cwd là thư mục gốc. Áp dụng cùng quy tắc dừng khi biên dịch lỗi:**

```powershell
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/loi-bo-sot.cpp" -o "bai-lam/nam-1-cpp/loi-bo-sot.exe"
$LASTEXITCODE
.\bai-lam\nam-1-cpp\loi-bo-sot.exe
$LASTEXITCODE
```

Kết quả mong đợi (suy ra từ mã nguồn) trước khi sửa là `Tong chi tieu: 42000 VND`, sau bản vá cận là `Tong chi tieu: 60000 VND`. Không thêm `--test`: demo lỗi không xử lý tham số này và cũng không chờ nhập tiền từ bàn phím. Nếu đã sửa mã trước lượt chạy đầu tiên, không ghi một output "trước khi sửa" do tự dựng ra; dùng bảng trace có nhãn để đối chiếu.

Bản đúng có bộ test riêng. **Bash, cwd vẫn là thư mục gốc; chỉ chạy executable sau khi compiler trả về 0:**

```bash
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/vi_sinh_vien.cpp" -o "bai-lam/nam-1-cpp/vi_sinh_vien.exe"
echo $?
./bai-lam/nam-1-cpp/vi_sinh_vien.exe
echo $?
./bai-lam/nam-1-cpp/vi_sinh_vien.exe --test
echo $?
```

**PowerShell, cwd vẫn là thư mục gốc; kiểm tra từng mã thoát:**

```powershell
g++ -std=c++17 -Wall -Wextra "bai-lam/nam-1-cpp/vi_sinh_vien.cpp" -o "bai-lam/nam-1-cpp/vi_sinh_vien.exe"
$LASTEXITCODE
.\bai-lam\nam-1-cpp\vi_sinh_vien.exe
$LASTEXITCODE
.\bai-lam\nam-1-cpp\vi_sinh_vien.exe --test
$LASTEXITCODE
```

Khi chạy ở chế độ thường, bản đúng có output mong đợi như dưới đây; chữ không dấu giúp hiển thị ổn định trên terminal và không ảnh hưởng đến phép tính:

```text
Com trua: 35000 VND
Xe buyt: 7000 VND
Vo ghi: 18000 VND
Tong chi tieu: 60000 VND
```

Ở chế độ test, kết quả mong đợi kết thúc bằng dòng **`9 passed, 0 failed`** với exit code 0. `--test` là tham số do chính hàm `main` của bản đúng xử lý, không phải chức năng có sẵn của C++. Compiler biên dịch thành công có thể không in gì; sự im lặng đó không có nghĩa là chưa chạy. Khi compiler thất bại thì phải dừng, vì executable cũ còn tồn tại có thể gây nhầm lẫn.

### Bảng C1–C9: kiểm tra cả phép cộng và trách nhiệm từ chối

Hãy che cột đáp án để tự dự đoán trước. Bảng là một ma trận học tập; cột "lõi sai" dùng `int n` và chỉ xét phép duyệt. Với dữ liệu nằm ngoài hợp đồng, không dùng một tổng số học tình cờ để hợp thức hóa đầu vào.

| Ca | Input tiền | Đáp án đúng | Lõi sai `i < n - 1` | Ý nghĩa |
| --- | --- | ---: | --- | --- |
| C1 | Rỗng, `n = 0` | 0 | 0 | Qua ca này chưa đủ |
| C2 | `[7000]` | 7000 | 0 | Bắt lỗi bỏ khoản duy nhất |
| C3 | `[35000,7000,18000]` | 60000 | 42000 | Ca xuyên suốt chương |
| C4 | `[1]` | 1 | 0 | Biên nhỏ nhất hợp lệ |
| C5 | `[1000000000]` | 1000000000 | 0 | Biên lớn nhất mỗi khoản |
| C6 | 500 khoản, mỗi khoản 1000000000 | 500000000000 | 499000000000 | Giới hạn số lượng và kiểu tổng |
| C7 | Một khoản 0 hoặc -1 | Từ chối | Không dùng lõi để hợp thức hóa | Kiểm tra đầu vào |
| C8 | Một khoản 1000000001 | Từ chối | Không có tổng hợp lệ | Vượt giới hạn mỗi khoản |
| C9 | 501 khoản hợp lệ | Từ chối | Không có tổng hợp lệ | Vượt giới hạn số lượng |

Chín hàng C **không tương ứng một-một** với chín lượt `check` trong bản đúng. Bộ kiểm thử tự động hiện có gồm: ba khoản; danh sách rỗng; một khoản 7000; một khoản 1; 500 khoản lớn; từ chối 0, **-1000** và 1000000001; từ chối 501 khoản. C5 không có ca đơn lẻ riêng, dù biên trên có xuất hiện trong ca 500 khoản; giá trị âm của C7 trong bảng là -1, còn test dùng -1000. Vì vậy không ghi mọi ô là đã chạy nguyên văn chỉ dựa vào con số 9.

Muốn thử C1 và C2 trên demo lỗi sau khi hoàn tất bản vá, thay **riêng dòng khai báo vector** trong bài làm thành `{}` hoặc `{7000}`, lưu và biên dịch lại ở mỗi lượt; ghi rõ đó là thay dữ liệu thử, không phải mở rộng bản vá. Khôi phục `{35000, 7000, 18000}` khi kết thúc. Các ca còn lại có thể trace thủ công nếu chưa có bộ khung kiểm thử (harness); C7–C9 thuộc phần validation nên không thể ghi nhận đạt với phần lõi chỉ làm phép cộng. Việc test của bản đúng đạt cũng không chứng minh tệp lỗi vừa sửa đã được chạy.

### Chạy Node.js và phạm vi của 34 ca kiểm thử

**Bash, cwd là thư mục gốc:**

```bash
node --version
node "bai-lam/nam-2-web/test_data.cjs"
echo $?
```

**PowerShell, cwd là thư mục gốc:**

```powershell
node --version
node "bai-lam/nam-2-web/test_data.cjs"
$LASTEXITCODE
```

Nếu lệnh kiểm tra phiên bản thất bại, dừng trước lệnh test. [Bộ `test_data.cjs`](../vi-du/nam-2-web/test_data.cjs) hiện tại có kết quả mong đợi **`34 passed, 0 failed`** với exit code 0, gồm 33 ca kiểm tra hợp đồng dữ liệu và một ca hồi quy cho category là mảng. Bộ test bắt ngoại lệ bằng `assert.throws`: một ca từ chối đúng sẽ được báo PASS, không phải cứ có lỗi được ném ra là cả bộ thất bại.

Bộ test kiểm tra logic của `data.js` qua Node.js: không mở trình duyệt, không khởi động server và không chứng minh hoạt động của handler, DOM hay localStorage. Bộ test cũng không chạy mọi chuỗi trong bảng W hay mọi biến thể trong bảng T. Các bảng nhóm nhiều giá trị để người học mở rộng việc kiểm tra; cần đọc tên ca và đầu vào thực tế trước khi ghi nhận mức độ bao phủ.

| Quan sát | Kết luận được phép | Bước tiếp theo |
| --- | --- | --- |
| Exit 0, tất cả ca được báo đạt | Các ca thực sự chạy đã qua | Lưu log, kiểm tiếp giao diện |
| Exit khác 0, có assertion lỗi | Có phép kiểm không đạt | Giữ input, expected, actual và lỗi |
| Không tìm thấy `node` | Chưa chạy được bộ test | Ghi thiếu runtime, không đánh dấu đạt |
| Không tìm thấy tệp test | Sai cwd, sai đường dẫn hoặc thiếu tệp | Kiểm cây tệp, không tự tạo test thay thế |

### Bảng W1–W10: kiểm tra toàn bộ chuỗi, không chỉ phần đầu

Dùng `globalThis.ViData.parseAmount` trong Console để kiểm tra hàm trực tiếp, và dùng form để kiểm tra luồng ứng dụng; kết quả của hai cách cần được ghi riêng. Mỗi chuỗi bị từ chối phải được bắt lỗi hoặc quan sát thấy thông báo phù hợp; không đòi hỏi câu thông báo lỗi giống hệt nhau giữa mọi môi trường.

| Ca parseAmount | Chuỗi đưa vào | Đáp án theo hợp đồng |
| --- | --- | --- |
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

Chuỗi `35000abc` dùng xuyên suốt chương thuộc cùng nhóm lỗi dạng chuỗi với W9 nhưng không thay thế các ca trong bảng. Bộ kiểm thử tự động dùng thêm một số phản ví dụ khác như `15k`, `15.000`, `15,000`, `3.5`, và kiểm tra cả đầu vào không phải chuỗi như số 35000 hoặc `null`. Ô nhập ở một số ứng dụng khác có thể biến đổi ký tự trước khi gọi hàm; việc không gõ được chữ vào ô nhập chưa chứng minh API tự chặn đầy đủ.

### Bảng T1–T8: hàm tổng chỉ nhận số tiền đã đúng kiểu

Các đầu vào rút gọn chỉ có trường `amount` dùng để cô lập trách nhiệm của `totalExpenses`; chúng không được coi là đủ schema để lưu. Muốn kiểm tra ranh giới lưu và đọc dữ liệu, cần đối tượng đủ trường và hàm `normalizeExpenses`.

| Ca totalExpenses | Danh sách hoặc amount | Đáp án |
| --- | --- | --- |
| T1 | Danh sách rỗng | 0 |
| T2 | Ba Expense giả của chương | 60000 |
| T3 | Một khoản amount là số 1 | 1 |
| T4 | 500 khoản amount đều là số 1000000000 | 500000000000 |
| T5 | 501 khoản hợp lệ | Từ chối vì quá số lượng |
| T6 | amount là chuỗi `"35000"` | Từ chối; hàm tổng không nhận chuỗi thay số |
| T7 | amount là 0, -1, 1.5 hoặc 1000000001 | Từ chối giá trị không hợp lệ |
| T8 | amount thiếu, `undefined`, `NaN` hoặc `Infinity` | Từ chối, không cho tổng NaN lọt ra |

"Từ chối" nghĩa là API ném lỗi hoặc ứng dụng báo dữ liệu không hợp lệ theo cơ chế đã triển khai, và khoản sai không được ghi nhận. Khi thử trực tiếp, dùng `try/catch` để phân biệt việc từ chối có chủ đích với lỗi do gọi sai tên API. Không sửa test để cho chuỗi tiền đi qua hàm tổng chỉ vì form ban đầu cũng đọc chuỗi: bước parse chính là ranh giới chuyển kiểu đứng trước hàm tổng.

### Nghiệm thu trên trình duyệt: lượt hợp lệ, lượt bị từ chối và lượt tải lại

Trước hết, ghi lại tổng và số khoản ban đầu. Nếu chưa có dữ liệu lưu, trang hiển thị ba khoản mẫu với tổng 60000; nếu khác, ghi lại trạng thái hiện có, hoặc khôi phục dữ liệu mẫu sau khi xác nhận có thể bỏ dữ liệu giả hiện tại. Sau đó thực hiện lần lượt:

1. **Thêm một khoản hợp lệ.** Thêm khoản Bánh mì 15000: từ trạng thái mẫu, tổng thành 75000; từ trạng thái khác, tổng tăng đúng 15000.
2. **Thử dữ liệu bị từ chối.** Form vừa được đặt lại sau lượt trước, vì vậy cần **nhập lại tên giả hợp lệ và chọn nhóm**, rồi thử số tiền `35000abc`. Phải thấy thông báo từ chối số tiền, còn tổng và số khoản giữ nguyên. Nếu bỏ trống tên và bị thuộc tính `required` chặn trước thì chưa kiểm tra được `parseAmount`.
3. **Kiểm tra cách hiển thị tên.** Nhập title giả `<b>Vở</b>`, **amount `1`, nhóm Học tập**, rồi gửi form thành công. Quan sát hàng vừa thêm: tên phải hiện nguyên văn, không in đậm, và tổng tăng 1 VND. Hàm `render()` dùng `cell.textContent`; việc test giữ nguyên chuỗi không chứng minh cách DOM hiển thị, nên cần quan sát bảng thật. Không dùng dữ liệu thật hay script độc hại.
4. **Tải lại trang.** Ghi lại cảnh báo nếu có, tải lại trang và đối chiếu. Cơ chế dự phòng lưu trong RAM có thể làm mất thay đổi; khi đó không báo là đã lưu bền vững. Nếu chưa tái hiện được tình huống bị chặn lưu hoặc dữ liệu hỏng, ghi là chưa kiểm tra; không thay đổi cơ chế bảo vệ hoặc xóa dữ liệu của trang khác.

### Qoder CLI (tùy chọn, không phải điều kiện hoàn thành)

Chỉ thử phần này khi Qoder CLI đã được cài và đăng nhập. Từ cwd là thư mục gốc, lệnh `qoder --version` kiểm tra phiên bản, còn `qoder` mở một phiên làm việc. **Bên trong phiên CLI**, `/help` hiển thị trợ giúp, `/usage` cho biết mức sử dụng và `/quit` để thoát; không gõ các lệnh này vào Bash hoặc PowerShell bên ngoài.

Không cần cài CLI, tạo tệp hướng dẫn cho Agent hay thay đổi cấu hình để hoàn thành bài. CLI có quyền và chế độ làm việc riêng, không suy ra từ IDE hay Desktop. Nếu không dùng, ghi "không thực hiện phần tùy chọn".

### Prompt mẫu

Prompt sau yêu cầu AI rà soát bằng chứng và lập báo cáo có giới hạn:

```text
Review bằng chứng tôi cung cấp, không tự nhận đã chạy thay tôi.
Cwd quy ước là gốc AI-Student-Handbook; bài làm ở bai-lam.
Tách: trace, build C++, chạy demo lỗi đã sửa, 9 test bản đúng,
34 test dữ liệu Web, thử form/DOM và thử localStorage.
So với bảng C1–C9, W1–W10, T1–T8; nêu input nào chưa được chạy nguyên xi.
Kiểm hồi quy category mảng nhưng không sửa demo Web đang đúng.
Giữ các lần fail, không đổi expected để hợp thức hóa actual.
Kết luận đạt ở phạm vi nào, còn gì chưa xác minh và bước nhỏ tiếp theo.
```

**Kết quả mong đợi.** Hồ sơ nghiệm thu gồm bài làm, diff, bảng trace, các lệnh hoặc thao tác đã thực hiện và kết quả tương ứng.

**Lỗi thường gặp.** Thường là nhầm test của bản đúng với test của bản vá, nhầm Node.js với trình duyệt, nhầm exit code 0 với thuật toán đúng, và nhầm trace với chạy thật. Mỗi kết luận cần gắn với một phép kiểm tra cụ thể.

### Câu hỏi kiểm tra

Năm câu sau tổng hợp các ý chính của cả bảy bài thực hành; cần tự trả lời trước khi xem đáp án.

1. Danh sách rỗng trả về 0 có chứng minh vòng lặp đúng không?
2. `input.value` của ô nhập số có phải là số nguyên không?
3. Khi thiếu `x.value`, tổng trong bài thử lỗi cô lập là `undefined` hay `NaN`?
4. Bộ test Node.js đạt có chứng minh localStorage lưu được dữ liệu không?
5. Khi AI báo "đã sửa", có thể nộp bài ngay không?

### Đáp án Bài thực hành 07

1. Không. Với `int n = 0`, cả bản sai và bản đúng đều không thực hiện lượt lặp nào; cần thêm ca một khoản.
2. Không. `.value` là chuỗi; chuỗi phải qua bước parse và kiểm tra hợp đồng rồi mới được đặt vào `Expense.amount`.
3. Truy cập thuộc tính thiếu cho `undefined`; phép cộng trong bài thử tạo ra `NaN`. Hai giá trị này không đồng nhất.
4. Không. Cần thử trên trình duyệt; khi mở qua `file://`, việc lưu có thể bị chặn và ứng dụng chuyển sang lưu tạm trong RAM.
5. Chưa. Phải xem diff, biết tệp đã được lưu, chạy kiểm tra hoặc ghi rõ là chưa chạy, và giữ bằng chứng của các lượt thất bại nếu có.

### Bảng tự đánh giá (rubric)

Mỗi tiêu chí được chấm từ 0 đến 2 điểm, tổng tối đa 10 điểm. Việc chấm dựa trên sản phẩm đầu ra, không dựa trên sự tự tin. Đây là rubric phục vụ tự học, không thay thế thang điểm chính thức của học phần. Người học có thể thực hành sâu một nhánh, nhưng phải giải thích được các lỗi trọng tâm của nhánh còn lại và ghi đúng giới hạn của môi trường.

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
| --- | --- | --- | --- |
| Hiểu công cụ | Trộn lẫn IDE, shell, CLI | Phân biệt được một phần | Gọi đúng vai trò và đúng shell |
| Giới hạn Agent | Cho sửa tùy ý | Có giới hạn nhưng thiếu kiểm tra | Ask trước, phạm vi nhỏ, xem diff |
| Giải thích lỗi | Chỉ chép đáp án | Nêu nguyên nhân, thiếu trace | Trace đúng, giải thích cả ca biên |
| Bằng chứng kiểm thử | Chỉ nói "chạy rồi" | Có output, thiếu ngữ cảnh | Có input, lệnh hoặc thao tác, kết quả và trạng thái |
| An toàn và trung thực | Dùng dữ liệu thật hoặc bịa là đã chạy | Có ghi thiếu sót nhưng chưa đủ | Dữ liệu giả, có checkpoint, ghi rõ phần chưa chạy |

Từ 8 đến 10 điểm: chuyển sang chương tiếp theo và duy trì thói quen kiểm chứng. Từ 5 đến 7 điểm: làm lại tiêu chí có điểm thấp nhất. Dưới 5 điểm: quay lại bước mở đúng thư mục gốc và trace danh sách một phần tử. Không suy ra năng lực dài hạn từ một phiên học, và không bịa log khi thiếu compiler.

### Tiêu chí hoàn thành

Người học nêu được test nào chạy trên mã nào, đối chiếu đủ ba bảng C, W, T, giữ nhật ký và tự chấm điểm có căn cứ. Báo cáo một phút gồm bốn ý: lỗi, vị trí sửa hoặc lý do không sửa, bằng chứng, và phần chưa kiểm tra.

## Tóm tắt chương

- **Môi trường trước công cụ.** Cần biết thư mục đang mở, shell đang dùng và công cụ nào thực sự có trên máy trước khi giao việc cho AI.
- **Hỏi chỉ đọc trước khi cho phép sửa.** Một câu hỏi tốt tách đầu vào, điều mong muốn, điều quan sát được và đoạn mã liên quan; câu trả lời phải dẫn được vị trí để tự kiểm lại.
- **Trace trước bản vá.** Lỗi 42000 nằm ở cận `i < n - 1`; ca một phần tử phân biệt được bản sai và bản đúng, còn ca rỗng thì không. Validation là trách nhiệm riêng, không tự có khi sửa cận.
- **Lần theo dữ liệu thay vì đoán.** Giá trị từ ô nhập là chuỗi; `parseAmount` kiểm tra cú pháp và miền giá trị, `totalExpenses` kiểm tra phần tiền, `normalizeExpenses` kiểm tra schema; lưu cục bộ có thể rơi vào cơ chế dự phòng trong RAM.
- **Hợp đồng, diff và checkpoint.** Agent chỉ làm việc trong phạm vi được giao; mỗi diff được đọc theo bốn câu hỏi; checkpoint và nhật ký giữ cả lượt thất bại cùng ca kiểm thử hồi quy.
- **Nghiệm thu có giới hạn.** Mỗi kết luận gắn với một phép kiểm tra cụ thể: test nào, chạy trên mã nào, trong môi trường nào, và phần nào chưa kiểm tra.

Qua bảy bài thực hành, Minh giải thích được lượt dừng của vòng lặp, sự khác nhau giữa tham chiếu và bản sao, và rủi ro của executable cũ. Lan lần theo được chuỗi nhập qua bước parse, schema, hàm tổng và lưu trữ, đồng thời biết giữ ca kiểm thử hồi quy. Cả hai đều có quyền từ chối dependency hoặc thay đổi quyền nằm ngoài phạm vi.

Quy trình mang sang các chương sau là: **quan sát → dự đoán → thay đổi nhỏ → kiểm tra → review → ghi bằng chứng**. Ba nguyên tắc đi kèm: chưa chạy thì nói chưa chạy; không có quyền thì dừng; không có lý do thì không mở rộng hệ thống. Nhắc lại thông điệp xuyên suốt: AI hỗ trợ, người học quyết định.

## Cầu nối sang chương sau

Chương này đã cho thấy cách dùng AI có kiểm soát: giao việc rõ, kiểm bằng bằng chứng và nhận thay đổi có chủ đích. Tuy vậy, vẫn còn nguy cơ giao hết việc suy nghĩ cho AI, vì một công cụ chạy tốt rất dễ khiến người dùng ngừng tự làm. Chương 3 sẽ học cách tận dụng AI mà không lạm dụng, để mỗi lần dùng đều giúp người học hiểu thêm.

## Tài liệu tham khảo

Thông tin về các sản phẩm Qoder trong chương được đối chiếu với tài liệu chính thức tại mốc **30/10/2026**. Giao diện, chế độ, quyền và điều kiện tài khoản có thể thay đổi theo phiên bản, vì vậy người đọc cần tra lại các tài liệu dưới đây tại thời điểm áp dụng. Tại mốc đối chiếu, bộ kiểm thử Node.js của mã ví dụ cho kết quả 34 passed, 0 failed, exit code 0; các output C++ trong chương là kết quả mong đợi suy ra từ mã nguồn, chưa thực thi. Giao diện Qoder, quyền Auto-Run, cách hiển thị DOM và cơ chế lưu cũng như dự phòng trên từng trình duyệt cụ thể chưa được kiểm chứng; các giới hạn này không được ghi thành "đã đạt" chỉ vì bộ test dữ liệu hợp lệ.

**Tài liệu chính thức của Qoder**

- [Qoder IDE quick start](https://docs.qoder.com/quick-start.md), [Chat overview](https://docs.qoder.com/user-guide/chat/overview.md), [Ask](https://docs.qoder.com/user-guide/chat/ask.md), [Agent](https://docs.qoder.com/user-guide/chat/agent.md): vai trò của các chế độ và cách review thay đổi.
- [Context](https://docs.qoder.com/user-guide/chat/context.md), [Terminal](https://docs.qoder.com/user-guide/editor/terminal.md): cách chọn ngữ cảnh, sử dụng terminal và chính sách chạy lệnh của IDE.
- [Qoder Desktop overview](https://docs.qoder.com/qoder/overview.md), [Desktop new task](https://docs.qoder.com/qoder/new-task.md): hai chế độ Coding và General; General không đồng nhất với chế độ Ask chỉ đọc.
- [Qoder CLI quickstart](https://docs.qoder.com/cli/quickstart.md), [CLI working modes](https://docs.qoder.com/cli/working-modes.md): sản phẩm CLI, điều kiện sử dụng và các chế độ làm việc riêng.

**Tài liệu JavaScript và Web API (MDN)**

- [MDN parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt), [Number.isSafeInteger](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger): cách đọc một phần chuỗi và miền số nguyên an toàn.
- [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent): giới hạn khi mở trang qua `file://` và cách hiển thị văn bản.

**Mã nguồn ví dụ kèm sách**

Các liên kết sau chỉ dùng để đọc và đối chiếu; mọi thay đổi được thực hiện trong thư mục `bai-lam`.

- C++: [demo lỗi `loi-bo-sot.cpp`](../vi-du/nam-1-cpp/loi-bo-sot.cpp), [bản đúng kèm 9 test `vi_sinh_vien.cpp`](../vi-du/nam-1-cpp/vi_sinh_vien.cpp).
- Web: [`index.html`](../vi-du/nam-2-web/index.html), [`app.js`](../vi-du/nam-2-web/app.js), [`data.js`](../vi-du/nam-2-web/data.js), [bộ 34 test `test_data.cjs`](../vi-du/nam-2-web/test_data.cjs).
