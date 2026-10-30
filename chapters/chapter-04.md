# CHƯƠNG 4 · SỬ DỤNG AI CÓ TRÁCH NHIỆM

Tổng tiền của ViSinhVien đã hiện đúng **60000**. Minh định nộp ngay. Lan hỏi lại: “Nếu thầy hỏi dòng này từ đâu ra, dữ liệu của ai, và em đã kiểm tra những gì, mình trả lời được chưa?” Chương này bắt đầu từ câu hỏi đó.

Làm chủ sản phẩm không có nghĩa là tự gõ từng ký tự hay tuyệt đối không dùng AI. Nó có nghĩa là bạn biết mình đang dùng gì, được phép dùng trong hoàn cảnh nào, có bằng chứng cho điều mình khẳng định và biết xử lý khi phát hiện sai sót. Một bài tập nhỏ là nơi an toàn để tập thói quen ấy, trước khi lỗi của mình ảnh hưởng đến người khác.

**Nhân vật, hồ sơ sự cố và hội thoại trong chương đều HƯ CẤU.** Đây là tài liệu tự học, **không phải quy định của Trường Đại học Thủy lợi** và không phải tư vấn pháp lý. Quyền dùng AI trong bài nộp do từng học phần và giảng viên quyết định.

## Cách dùng phòng xử lý sự cố

Chương được tổ chức như một **phòng xử lý sự cố** gồm bảy hồ sơ và một phòng khám kỹ thuật. Mỗi hồ sơ có cùng sáu phần:

| Phần | Bạn làm gì |
| --- | --- |
| Sự cố | Đọc tình huống hư cấu của Minh hoặc Lan. |
| Dấu hiệu | Gạch chân chi tiết cho thấy có vấn đề. |
| Nguy cơ | Nêu ai hoặc điều gì có thể bị ảnh hưởng. |
| Các lựa chọn | Chọn **một** hành động trước khi đọc tiếp. Viết lý do một dòng. |
| Phân tích từng lựa chọn | Mở sau khi đã chọn. Mỗi phương án đều được phân tích, kể cả phương án sai. |
| Bài học | Một quy tắc ngắn bạn mang sang bài tập thật. |

**Mốc chung của câu chuyện:** ViSinhVien là ứng dụng HTML/JavaScript lưu bằng `localStorage` trong trình duyệt; **không có backend, đăng nhập hay cơ sở dữ liệu máy chủ**. Mỗi khoản chi là `Expense{id,title,amount,category}`. `amount` là số nguyên VND từ 1 đến `1e9`; tối đa 500 khoản; danh sách rỗng có tổng 0. Bộ dữ liệu GIẢ chuẩn: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000, tổng **60000 VND**.

Bạn sẽ gặp thêm SQL chạy bằng Python `sqlite3` với cơ sở dữ liệu `:memory:` ở mục 4.8. Đó là **minh họa riêng**, không phải thành phần của ViSinhVien. Các đoạn mã ngắn phục vụ giải thích; khi thực hành, hãy ghi kết quả mình thực sự quan sát, kể cả kết quả chưa đạt.

**Thứ tự đọc:** hồ sơ 4.1 (khóa bị lộ) được đặt đầu vì sai thứ tự xử lý có hậu quả lớn nhất. Nếu thời gian ít, làm 4.1, 4.2, 4.5 và mục 4.8 trước; các hồ sơ còn lại làm ở buổi sau.

**Chuẩn bị:** một tờ giấy hoặc tệp `ghi-chep-04.txt` trong thư mục `bai-lam`. Không cần cài đặt, đăng nhập, tạo khóa hay truy cập dịch vụ thật nào. Mọi chuỗi bí mật trong chương là placeholder như `DEMO_KEY_NOT_A_SECRET`, không có quyền truy cập.

## 4.1. Hồ sơ 01 — Khóa API xuất hiện trên GitHub

### Sự cố

ViSinhVien **không cần API key**. Nhưng trong một bài khác, Minh thử gọi một dịch vụ AI và để khóa trong tệp `config.js`. Tối thứ Sáu, Minh đẩy cả thư mục lên một kho GitHub công khai để nhờ Lan xem giúp. Sáng hôm sau, Lan nhắn: “Hình như tệp config có dòng `API_KEY = ...`?”

Khi kể lại, chương chỉ dùng placeholder `DEMO_KEY_NOT_A_SECRET`. Trong đời thật, không chụp lại khóa đầy đủ để “làm bằng chứng”.

### Dấu hiệu

- Một chuỗi trông giống khóa nằm trong tệp đã commit.
- Kho ở chế độ công khai từ tối hôm trước; không ai biết chính xác bao nhiêu người đã xem hoặc clone.
- Minh định “xóa dòng đó rồi commit lại là xong”.

### Nguy cơ

Khóa API cấp quyền dùng dịch vụ và có thể phát sinh chi phí dưới tên tài khoản của chủ khóa. Xóa dòng trong tệp **không vô hiệu hóa khóa**: bản cũ vẫn có thể nằm trong lịch sử Git, trong bản clone của người khác, trong cache hoặc trong đoạn chat từng dán. Khóa vẫn còn hiệu lực cho đến khi được thu hồi ở nhà cung cấp.

![Thu hồi trước, dọn sau: sáu bước cùng thứ tự với mục bên dưới, ô lớn là bước 02 thu hồi khóa; nhãn trong hình là nhãn giả, không phải khóa thật.](../assets/security.svg)

### Các lựa chọn

Chọn **một** hành động Minh nên làm **đầu tiên**:

- **A.** Xóa dòng khóa, commit “fix config”, rồi coi như xong.
- **B.** Tạo khóa mới, dán vào tệp, để khóa cũ hoạt động thêm vài ngày cho chắc.
- **C.** Dừng chia sẻ thêm, rồi thu hồi hoặc xoay vòng khóa cũ ở nhà cung cấp (hoặc báo ngay người có quyền nếu khóa không phải của mình).
- **D.** Gửi nguyên khóa vào nhóm chat lớp để mọi người cùng kiểm tra xem có bị dùng chưa.
- **E.** Tự viết lại lịch sử Git và ép đẩy (force push) để “xóa sạch”.

### Đáp án Hồ sơ 01 — Phân tích từng lựa chọn

**A — Chưa đủ.** Commit mới chỉ thay đổi bản hiện tại; khóa cũ vẫn hoạt động và vẫn có trong lịch sử. Đây là sai lầm phổ biến nhất vì màn hình trông “sạch”.

**B — Sai thứ tự.** Tạo khóa mới không làm khóa cũ mất hiệu lực. Để khóa cũ chạy thêm là để cửa mở. Thêm nữa, dán khóa mới vào cùng tệp có thể lặp lại sự cố.

**C — Đúng hướng.** Ưu tiên vô hiệu quyền đã lộ trước khi dọn bản lưu. Hướng dẫn của GitHub cũng khuyến nghị thu hồi hoặc xoay vòng bí mật trước khi xử lý việc loại bỏ dữ liệu khỏi kho [7]. Nếu khóa thuộc nhóm, trường hoặc nơi thực tập, Minh **báo ngay** người có quyền thay vì tự tìm cách truy cập tài khoản người khác.

**D — Làm sự cố lớn hơn.** Gửi khóa vào kênh khác là thêm một nơi lộ. Báo sự cố bằng mô tả, không bằng bí mật.

**E — Không tự làm.** Viết lại lịch sử ảnh hưởng mọi người đang dùng kho và vẫn không bảo đảm các bản clone hoặc cache biến mất. Việc này cần người quản lý kho quyết định và phối hợp. Chương này **không cung cấp lệnh viết lại lịch sử**.

### Sáu bước xử lý có thể làm theo

1. **Dừng chia sẻ thêm.** Không gửi lại tệp, không chụp nguyên khóa để hỏi nhóm. Nếu là kho của chính mình: chuyển kho sang chế độ riêng tư (Private) trong phần cài đặt kho. Nếu không phải kho của mình: nhắn ngay chủ kho, không tự xử lý. Không chuyển khóa sang kênh khác để “cất tạm”.
2. **Thu hồi hoặc xoay vòng khóa ở nhà cung cấp.** Dùng chức năng quản lý khóa chính thức nếu là tài khoản của mình; nếu không, báo người có quyền. **Xác nhận khóa cũ đã bị vô hiệu** — tạo khóa mới nhưng để khóa cũ còn hoạt động là chưa xong. Xác nhận bằng **trạng thái “đã thu hồi/đã xóa” trong trang quản lý khóa**; **không gọi thử API bằng khóa cũ** để kiểm tra.
3. **Kiểm tra mức sử dụng.** Xem lượt gọi, chi phí và mốc thời gian bất thường trong trang quản lý của mình. “Chưa thấy dùng” không chứng minh chưa ai sao chép. Ghi thời điểm phát hiện và phạm vi chia sẻ, không lưu lại bí mật.
4. **Kiểm tra bản liên quan trong phạm vi được phép.** Commit, tệp cấu hình, bản build, ảnh chụp, đoạn chat có liên quan. Không tự truy cập tài khoản hay log của người khác. Khi tìm, tránh tạo log mới chứa khóa.
5. **Báo đúng đầu mối.** Bài học: giảng viên hoặc trưởng nhóm. Tài khoản tổ chức: kênh sự cố của tổ chức. Gửi thời điểm, dịch vụ, trạng thái thu hồi, phạm vi đã biết và điều chưa rõ; **không đính kèm khóa**.
6. **Giảm dữ liệu còn lưu và ngăn tái diễn.** Sau khi khống chế quyền truy cập, phối hợp xử lý các bản chứa bí mật theo quy trình phù hợp. Trong câu chuyện này kho là **kho cá nhân của Minh**: sau khi khóa đã thu hồi, Minh hỏi giảng viên trước khi đụng tới lịch sử kho, và ghi nhận rằng bản clone hoặc cache có thể vẫn còn — đó là lý do bước 2 phải làm trước. Thay minh họa bằng placeholder, bỏ nhu cầu dùng khóa thật trong bài, thêm bước rà tệp trước khi chia sẻ.

### Một thông báo sự cố ngắn, đủ để hành động

```text
Em phát hiện lúc [giờ, ngày] một tệp trong [phạm vi chia sẻ] chứa khóa của [dịch vụ].
Em đã dừng chia sẻ. Khóa cũ: [đã thu hồi / đang chờ người có quyền / chưa xác minh].
Thời gian có thể đã lộ: [phạm vi biết được].
Mức sử dụng: [đã kiểm tra gì, kết quả, hoặc chưa kiểm tra].
Nhờ [đầu mối] hướng dẫn xử lý bản đã chia sẻ. Em không đính kèm khóa.
```

Báo sớm không có nghĩa đã kết luận có tấn công; chưa thấy lạm dụng cũng không phải lý do để giấu. Với dữ liệu hoặc hệ thống thật, người có thẩm quyền đánh giá nghĩa vụ thông báo. Đừng suy ra thời hạn pháp lý từ mẫu này.

### Bài học

**Thu hồi trước, dọn sau. Báo bằng mô tả, không bằng bí mật.** Lan cùng Minh tìm nguyên nhân tệp thừa lọt vào bản chia sẻ, rồi thêm một bước “rà danh sách tệp trước khi đẩy”. Sửa một bước quy trình cụ thể hữu ích hơn lời hứa “lần sau cẩn thận”.

**QUICK CHECK:** Minh đã xóa tệp `config.js` và tạo khóa mới. Còn thiếu việc gì quan trọng nhất? Trả lời một câu rồi đối chiếu với bước 2.

## 4.2. Hồ sơ 02 — Dữ liệu cá nhân đi vào cửa sổ chat

### Sự cố

Để nhờ AI tìm lỗi tính tổng, Minh định gửi **ảnh chụp bảng chi tiêu thật** của mình trong tháng. Ảnh có tên quán ăn quen, giờ giao dịch, mã sinh viên lẫn giữa các dòng, số tài khoản ngân hàng bị che một nửa và góc màn hình còn hiện email sinh viên. Minh nghĩ: “Em đổi tên mình thành ‘Bạn A’ là ẩn danh rồi.”

### Dấu hiệu

- Lỗi cần sửa (bỏ sót khoản cuối) **có thể tái hiện bằng ba khoản giả**; không cần dữ liệu thật.
- Đổi tên nhưng giữ mã sinh viên, giờ, địa điểm và email.
- Ảnh chụp màn hình chứa nhiều thông tin hơn vùng lỗi.

### Nguy cơ

Người biết bối cảnh vẫn có thể nhận ra “Bạn A” từ các trường còn lại. Ảnh có thể lộ email, tab trình duyệt, đường dẫn chứa tên. Một lớp che trong tệp chỉnh sửa có thể bị gỡ. Lịch sử chat có thể giữ đoạn từng dán ngay cả khi bạn đã xóa khỏi mã.

### Phân loại trước khi dán

Quy tắc thực dụng: **chọn dữ liệu ít nhạy cảm nhất nhưng vẫn đủ tái hiện vấn đề.**

| Nhóm dữ liệu | Cách hiểu khi làm bài | Ví dụ và lựa chọn |
| --- | --- | --- |
| Giả/tổng hợp | Tạo mới cho mục đích thử, không lấy hồ sơ thật rồi sửa sơ qua | 35000, 7000, 18000; liên hệ giả `demo001@example.invalid` |
| Đã khử nhận dạng/ẩn danh | Đã xử lý để không còn xác định được người, kể cả khi liên kết với dữ liệu khác | Chỉ gọi là ẩn danh khi đã đánh giá lại khả năng nhận diện; **không mặc định sau khi bỏ tên** |
| Cá nhân, nhạy cảm hoặc bí mật | Liên quan một người, đời sống riêng tư, tài khoản hoặc quyền truy cập | Mã sinh viên, ảnh hồ sơ, lịch chi tiêu thật, mật khẩu, khóa API — không đưa vào ví dụ công khai |

Bảng này là công cụ sàng lọc khi học, không thay thế phân loại pháp lý chi tiết. Khóa API cần bảo vệ vì cấp quyền truy cập, dù bản thân chuỗi khóa không nhận diện một người. Dữ liệu công khai ở nơi khác cũng không đương nhiên phù hợp để gom lại và gửi cho một dịch vụ AI.

### Các lựa chọn

- **A.** Gửi ảnh nguyên bản; dịch vụ AI chắc không lưu đâu.
- **B.** Đổi tên thành “Bạn A”, giữ các cột khác, rồi gửi.
- **C.** Tự tạo ba khoản giả 35000, 7000, 18000 cùng đoạn hàm tính tổng, gửi phần đó.
- **D.** Che bằng một lớp hình chữ nhật trong tệp chỉnh sửa, gửi tệp chỉnh sửa gốc.

### Đáp án Hồ sơ 02 — Phân tích từng lựa chọn

**A — Không có căn cứ.** Cách một dịch vụ lưu, dùng lại hay cho người xem xét nội dung phụ thuộc điều khoản, gói dịch vụ và thiết lập — bạn chưa kiểm tra. Quan trọng hơn: bài không cần dữ liệu thật.

**B — Chưa phải ẩn danh.** Mã sinh viên, giờ, quán quen và email vẫn đủ để người quen nhận ra. Mã hóa tên thành một mã ổn định trong khi vẫn giữ bảng đối chiếu cũng chưa phải ẩn danh hoàn toàn.

**C — Lựa chọn tốt nhất.** Ba khoản giả vẫn đủ tái hiện lỗi bỏ khoản cuối (ra 42000 thay vì 60000). Dữ liệu được tạo mới từ đầu, không còn liên hệ với ai.

**D — Rủi ro kỹ thuật.** Lớp che có thể bị gỡ trong tệp gốc. Nếu thật sự cần ảnh, **xuất ảnh phẳng**, chỉ cắt đúng vùng lỗi rồi mở lại ảnh đầu ra để kiểm tra.

### Hộp pháp lý — đọc để biết mình cần hỏi ai

> **Mốc đối chiếu nguồn: 29/10/2026 (kế thừa từ bản gốc, chưa được kiểm tra lại trong lượt biên tập này).** Bản gốc đối chiếu Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Nghị định 356/2025/NĐ-CP, cùng có hiệu lực từ 01/01/2026 [1][2]; theo Điều 42 Nghị định 356, Nghị định 13/2023/NĐ-CP đã hết hiệu lực. Về sở hữu trí tuệ, bản gốc dùng Văn bản hợp nhất 67/VBHN-VPQH ngày 23/03/2026, thể hiện sửa đổi bởi Luật 131/2025/QH15 có hiệu lực từ 01/04/2026 [3]. Đây là định hướng học tập, **không phải ý kiến pháp lý**. Trước khi áp dụng cho dữ liệu, hợp đồng hay sản phẩm thật, mở văn bản gốc và hỏi người có thẩm quyền.

Luật bảo vệ dữ liệu cá nhân có nội dung về khái niệm và khử nhận dạng, nguyên tắc xử lý theo phạm vi và mục đích, sự đồng ý và xử lý trong hoạt động AI. Nhưng đừng rút gọn thành “mọi xử lý đều phải xin đồng ý”: luật có các trường hợp ngoại lệ tại Điều 19 [1]. Cũng đừng tự suy diễn rằng bài tập của mình chắc chắn thuộc ngoại lệ. **Nếu bài không cần dữ liệu thật, dùng dữ liệu giả là cách giảm vấn đề ngay từ thiết kế.**

### Những chỗ hay quên: ảnh, chat, lịch sử

- **Ảnh:** email ở góc, đường dẫn chứa tên, tab trình duyệt, khóa trong bảng điều khiển.
- **Chat:** đoạn từng dán rồi xóa khỏi mã vẫn có thể còn trong lịch sử hội thoại.
- **Git, bản sao lưu, log, bản xuất dự án:** có thể chứa thông tin ngoài màn hình hiện tại.

Đừng chỉ kiểm tra tệp đang mở. Với ví dụ cần chuỗi bí mật, dùng `DEMO_KEY_NOT_A_SECRET` và ghi rõ đó là placeholder.

### Bài học

**Dữ liệu giả không chỉ là đổi tên — đó là dữ liệu được tạo mới.** Hỏi “lỗi này cần tối thiểu dữ liệu gì để tái hiện?” trước khi hỏi “gửi cho AI thế nào?”.

## 4.3. Hồ sơ 03 — Agent sửa và xóa ngoài phạm vi

### Sự cố

Lan giao cho Agent: “Sửa lỗi tổng tiền trong `bai-lam/nam-2-web`.” Agent báo đã xong. Lan mở diff và thấy: hàm tổng được sửa, nhưng `index.html` đổi giao diện, tệp `test_data.cjs` trong bản sao bị xóa hai ca đang thất bại (việc xóa là hư cấu; tệp kèm cẩm nang vẫn đủ 34 ca), và có đề nghị chạy lệnh cài một gói định dạng mã. Màn hình test giờ toàn màu xanh.

### Dấu hiệu

- Diff chạm vào tệp nằm ngoài mục tiêu.
- Số ca test **giảm** đúng bằng số ca đang thất bại.
- Có lệnh cài đặt không được yêu cầu.
- Báo cáo “đã xong” nhưng không nêu ca nào bị xóa.

### Nguy cơ

Test xanh vì ca khó bị xóa là bằng chứng giả. Thay đổi giao diện không yêu cầu làm khó review. Gói lạ có thể mang rủi ro chuỗi cung ứng (xem Hồ sơ 04). Nhận cả gói thay đổi nghĩa là Lan nhận trách nhiệm cho những gì mình chưa đọc.

Một Agent có thể đọc nhiều tệp, gọi lệnh và gửi nội dung tới dịch vụ, tùy công cụ, chế độ và thiết lập. Đừng mặc định “nằm trên máy em” là “không thể đi vào ngữ cảnh gửi ra ngoài”. Câu prompt “chỉ sửa tệp X” là **yêu cầu**, không phải hàng rào kỹ thuật; quyền thật nằm ở thiết lập và các hộp xác nhận bạn đồng ý.

### Các lựa chọn

- **A.** Chấp nhận toàn bộ vì test đã xanh.
- **B.** Dừng Agent. Quay về checkpoint đã tạo trước khi giao việc (Mission 06, mục 2.6 Chương 2), rồi chỉ áp lại phần sửa hàm tổng sau khi đọc và hiểu diff đó.
- **C.** Bảo Agent “khôi phục lại như cũ” mà không kiểm tra nó khôi phục gì.
- **D.** Giữ thay đổi, chỉ tự gõ lại hai ca test đã bị xóa theo trí nhớ.

### Đáp án Hồ sơ 03 — Phân tích từng lựa chọn

**A — Sai.** Test xanh sau khi xóa ca thất bại không chứng minh hàm đúng. Phần hữu ích không hợp thức hóa phần ngoài phạm vi.

**B — Đúng.** Checkpoint là đường quay lại đã chuẩn bị trước. Sau khi quay về, so sánh với diff, giữ đúng một thay đổi được giao, chạy lại **đủ** bộ test gốc (34 ca cho bản Web tham khảo). Ghi vào nhật ký rằng lượt Agent đầu vượt phạm vi; không xóa lượt đó để câu chuyện trông đẹp.

**C — Khôi phục mù.** Bạn lại giao quyền cho chính công cụ vừa vượt phạm vi mà không có bằng chứng về trạng thái sau đó. Nếu không có checkpoint, hãy dừng, giữ nguyên hiện trạng và đối chiếu từng tệp với bản `vi-du` chỉ đọc.

**D — Nguy hiểm.** Ca test gõ lại theo trí nhớ có thể khác ca gốc. Giao diện thay đổi và đề nghị cài gói vẫn còn đó.

### Hợp đồng giao việc nên có trước khi bấm chạy

```text
Phạm vi: chỉ sửa hàm tính tổng trong bai-lam/nam-2-web/data.js.
Không sửa, xóa hoặc đổi tên tệp khác. Không xóa hoặc sửa ca test.
Không cài gói, đổi cấu hình, commit, đẩy mã hay truy cập mạng.
Trước khi sửa: nêu giả thuyết, dòng dự kiến đổi, ca test sẽ chạy.
Sau khi sửa: báo diff, số ca chạy, số ca đạt/không đạt, phần chưa kiểm.
Nếu bị chặn hoặc cần quyền mới: dừng và hỏi, không tìm đường vòng.
```

### Bài học

**Checkpoint trước, diff sau, nhận từng phần.** Số ca test phải giữ nguyên hoặc tăng; thấy giảm là dừng lại hỏi “ca nào biến mất và vì sao?”.

## 4.4. Hồ sơ 04 — Gói thư viện AI đề xuất

### Sự cố

Minh hỏi cách định dạng tiền cho đẹp. AI trả lời tự tin và đưa một lệnh cài cho gói có tên rất giống một thư viện quen thuộc, kèm câu “chạy lệnh này là xong”. Minh chưa từng nghe tên gói này.

### Dấu hiệu

- Tên gói gần giống thư viện phổ biến nhưng khác một vài ký tự (dấu hiệu **typosquatting**).
- Câu trả lời không dẫn registry chính thức, không nêu người duy trì hay kho nguồn.
- Lệnh cài tải mã từ mạng rồi chạy ngay.
- Bài hiện tại **không cần thêm phụ thuộc** để định dạng tiền; API có sẵn của trình duyệt đã đủ.

### Nguy cơ

Gói không tồn tại, gói bị đặt tên nhầm hoặc gói độc hại có thể chạy script khi cài. Script cài có thể đọc biến môi trường, tệp cấu hình, khóa. Một lockfile giúp cố định phiên bản nhưng **không biến gói độc hại thành đáng tin** [6].

### Các lựa chọn

- **A.** Chạy lệnh ngay; AI đã gợi ý thì chắc ổn.
- **B.** Hỏi AI “gói này có an toàn không?” rồi làm theo câu trả lời.
- **C.** Kiểm tra xem bài có thật sự cần phụ thuộc không. Nếu cần, đối chiếu tên, phiên bản, người duy trì, kho nguồn, giấy phép, dấu hiệu bảo trì và cảnh báo bảo mật trên registry chính thức — **không cài trong bài này**.
- **D.** Cài vào một thư mục tạm “cho biết”, sau đó xóa.

### Đáp án Hồ sơ 04 — Phân tích từng lựa chọn

**A — Sai.** Sự tự tin không phải bằng chứng. Tên gói do mô hình sinh ra có thể không tồn tại hoặc bị nhắm tới để đánh lừa.

**B — Vòng tròn.** Cùng một nguồn vừa đề xuất, vừa tự chứng nhận. Bằng chứng phải đến từ registry và kho nguồn, không phải từ lời khẳng định.

**C — Đúng.** Câu hỏi đầu tiên luôn là “bài có cần thêm phụ thuộc không?”. Với ứng dụng HTML/JS nhỏ, câu trả lời thường là không. Hoạt động của chương chỉ là **lập bảng kiểm chứng, không thực hiện cài gói**. Nếu chưa xác minh được, bỏ đề xuất và dùng giải pháp đang hiểu.

**D — Vẫn là chạy mã.** Cài “cho biết” vẫn thực thi script trên máy bạn. Xóa thư mục sau đó không hoàn tác những gì script đã làm.

### Bảng kiểm chứng để trống — điền khi thật sự cần

| Câu hỏi | Bằng chứng cần có | Đã kiểm? |
| --- | --- | --- |
| Tên gói chính xác? | Trang gói trên registry chính thức của hệ sinh thái | |
| Phiên bản dự định dùng? | Số phiên bản, ngày phát hành | |
| Ai duy trì? | Tài khoản nhà phát hành, lịch sử phát hành | |
| Kho nguồn? | Liên kết kho mã, khớp với registry | |
| Giấy phép? | Tệp giấy phép của gói | |
| Có script cài không? | Nội dung trường script trong manifest | |
| Có cảnh báo bảo mật? | Trang tư vấn bảo mật của hệ sinh thái | |
| Có phụ thuộc bắc cầu lạ? | Danh sách phụ thuộc, lockfile | |

Không bịa URL registry để làm đầy cột. Cột trống trung thực tốt hơn một dòng “đã kiểm” không có căn cứ.

### Bài học

**Không cài chỉ để chứng tỏ chủ động.** Thêm một phụ thuộc là thêm một bên bạn phải tin; hãy chắc mình thật sự cần.

## 4.5. Hồ sơ 05 — Bài tập hoàn toàn do AI làm

### Sự cố

Đề ViSinhVien ghi: “Được tham khảo tài liệu.” Không nhắc gì đến AI. Minh dán cả đề vào chat, nhận về toàn bộ `index.html`, `data.js`, `app.js` và một bài giải thích. Bạn sửa vài chỗ, chạy được, rồi định ghi trong phần khai báo: “Có tham khảo ý tưởng từ AI.”

### Dấu hiệu

- Đề không nói rõ về AI; “tham khảo tài liệu” **không đồng nghĩa** với “AI được viết hộ”.
- Toàn bộ chức năng chính do AI sinh.
- Lời khai nhỏ hơn mức hỗ trợ thực tế.
- Minh không giải thích được vì sao kiểm tra `amount` nằm ở đó.

### Nguy cơ

Đây là vấn đề **học thuật**, và cách xử lý phụ thuộc yêu cầu học phần — chương này không thay quy định của trường. Ba hậu quả có thể xảy ra: mất phần luyện mà môn học nhắm tới; khai báo sai làm mất tính trung thực; không bảo vệ được bài khi bị hỏi.

### Các lựa chọn

- **A.** Nộp nguyên, khai “có tham khảo ý tưởng”.
- **B.** Hỏi giảng viên bằng một tin nhắn mô tả **đúng việc đã làm**, tiếp tục phần chắc chắn được phép trong lúc chờ, không mặc định im lặng là đồng ý.
- **C.** Xóa hết, tự viết lại từ đầu theo trí nhớ của mã AI.
- **D.** Không khai, vì “ai cũng dùng”.

### Đáp án Hồ sơ 05 — Phân tích từng lựa chọn

**A — Khai không khớp.** Nếu AI sinh cả hàm, phải nói là sinh bản nháp của hàm, không đổi thành “chỉ tham khảo ý tưởng”. Khai báo không thay thế sự cho phép.

**B — Đúng hướng.** Mô tả hành động cụ thể để giảng viên trả lời được:

```text
Thưa thầy/cô, với bài ViSinhVien, em dự định tự viết phần thêm khoản chi và tính tổng.
Em muốn dùng AI để giải thích lỗi JavaScript và gợi ý ca kiểm thử cho amount,
sau đó tự sửa và chạy kiểm tra. Em không định gửi dữ liệu thật hoặc nhờ AI làm toàn bộ bài.
Phạm vi này có được phép không ạ? Nếu được, nhóm cần khai báo ở đâu và giữ bằng chứng nào?
Nếu không, em sẽ dùng tài liệu môn học theo hướng dẫn.
```

**C — Trung thực nhưng lãng phí.** Viết lại từ trí nhớ vẫn là làm lại bài của người khác, và bạn có thể đang bỏ phần học. Việc đúng là hỏi phạm vi, rồi **tự làm lại phần cốt lõi có hiểu**.

**D — Tệ nhất.** “Bạn cùng lớp cũng dùng” hay “em chỉ dùng bản miễn phí nên không tính” đều không phải căn cứ học thuật. Không khai là sai lệch về đóng góp.

### Bảng phân loại — để hỏi, không phải để tự cho phép

Bảng này **không phải quy định của TLU**; nó giúp bạn đặt câu hỏi đúng.

| Tình trạng | Ví dụ trong bài ViSinhVien | Việc cần làm |
| --- | --- | --- |
| Đã được cho phép | Đề ghi được dùng AI gợi ý ca kiểm thử, phải khai báo | Dùng đúng phần được phép, lưu lại phần hỗ trợ và tự kiểm tra |
| Đã bị cấm | Bài kiểm tra yêu cầu tự viết, không dùng công cụ sinh mã | Không nhờ AI tạo lời giải hay sửa mã trong thời gian làm bài |
| Chưa rõ | Đề cho tham khảo tài liệu nhưng không nói về AI | Hỏi giảng viên trước; chưa biến giả định thành sự cho phép |
| Có điều kiện | Được hỗ trợ giải thích nhưng không được sinh toàn bộ chức năng | Tách câu hỏi giải thích khỏi yêu cầu viết hộ |

Với bài nhóm, cả nhóm cần biết phạm vi: một thành viên đưa mã AI vào nhánh chung có thể ảnh hưởng bản nộp của mọi người.

### Bài học

**Khai báo là mô tả, không phải xin phép.** Hỏi trước về phạm vi; khai sau đúng với việc đã làm.

## 4.6. Hồ sơ 06 — Đoạn mã không rõ giấy phép

### Sự cố

Minh tìm được một giao diện đẹp trên GitHub. Trang kho mở được không cần đăng nhập, nên bạn định chép một tệp vào ViSinhVien. Kho **không có tệp LICENSE**.

### Dấu hiệu

- Không có giấy phép, hoặc chỉ có tên giấy phép mà chưa đọc điều kiện.
- Có giấy phép cho mã nhưng ảnh và phông chữ đi kèm có điều kiện khác.
- Định “ghi nguồn là đủ”.

### Nguy cơ

Công khai **không** tự trao quyền sao chép, phân phối hay tạo tác phẩm phái sinh [8]. Ghi nguồn là việc học thuật; nó không thay quyền sử dụng. Sản phẩm bị gắn đoạn không rõ quyền có thể phải gỡ bỏ hoặc gây tranh cãi khi công bố.

### Các lựa chọn

- **A.** Chép vì kho công khai và ghi nguồn ở cuối bài.
- **B.** Tự viết lại bảng khoản chi đơn giản mình hiểu; bỏ phần giao diện chưa rõ quyền.
- **C.** Đổi tên biến và màu sắc để “không ai nhận ra”.
- **D.** Nhờ AI viết lại giao diện đó từ ảnh chụp màn hình.

### Đáp án Hồ sơ 06 — Phân tích từng lựa chọn

**A — Không đủ.** Không có giấy phép nghĩa là không có cơ sở để coi là tự do sao chép. Đường dẫn nguồn không tạo ra quyền.

**B — Đúng cho bài này.** Sản phẩm bớt bóng bẩy nhưng nhóm biết nguồn gốc từng phần. Đây là giảm một vấn đề không cần thiết, không phải phòng thủ đến mức không dám học từ ai.

**C — Vẫn là sao chép.** Thay tên biến hay màu sắc không xóa nghĩa vụ và không đổi bản chất việc dùng tác phẩm của người khác.

**D — Chưa chắc sạch.** Đầu ra có thể gần với thiết kế gốc; nhãn “AI tạo” không tự chứng minh nguồn gốc hay quyền sở hữu độc quyền. Kiểm nguồn nếu được dẫn và điều khoản công cụ bạn dùng.

### Đọc tên giấy phép chưa đủ

| Tình huống | Điều cần hiểu | Hành động thực tế |
| --- | --- | --- |
| Mã mang giấy phép MIT | Có quyền sử dụng rộng, nhưng phải giữ thông báo bản quyền và giấy phép theo điều kiện của MIT | Giữ nội dung cần thiết khi sao chép; lưu nguồn và phiên bản |
| Mã mang giấy phép GPL | **Không** phải giấy phép “cấm thương mại”; nghĩa vụ phụ thuộc phiên bản, việc chuyển giao và quan hệ với tác phẩm phái sinh | Đọc đúng GPL áp dụng; hỏi người có chuyên môn nếu chưa xác định được nghĩa vụ |
| Kho không có giấy phép rõ | Không có cơ sở để coi là tự do sao chép | Không đưa vào bản nộp chỉ bằng cách thêm đường dẫn |
| AI đưa một đoạn mã | Nhãn “AI tạo” không tự chứng minh nguồn gốc hay quyền | Kiểm nguồn nếu có, điều khoản công cụ, dấu hiệu sao chép; thay phần chưa rõ quyền |

Với MIT, ghi nguồn học thuật và giữ thông báo giấy phép là hai việc khác nhau. Với GPL, đừng kết luận chỉ từ số dòng đã chép, cũng đừng nói “thấy GPL là không được dùng”. Phải xét văn bản giấy phép cụ thể; chương này không quyết định tính tương thích cho sản phẩm thật.

Về pháp luật Việt Nam, bản gốc dẫn Điều 22 và Điều 25 khoản 3 của văn bản hợp nhất về sở hữu trí tuệ [3]: chương trình máy tính được bảo hộ, và lý do “em sao chép để học” không tự động là ngoại lệ cho mọi trường hợp. Điều này không cấm học từ tài liệu; nó nhắc kiểm tra quyền trước khi mang mã người khác vào bản nộp hoặc sản phẩm phân phối.

### Thẻ nguồn nhỏ — điền ngay khi chọn tài nguyên

| Thành phần định dùng | Nguồn/phiên bản | Giấy phép và việc phải giữ | Quyết định |
| --- | --- | --- | --- |
| Ví dụ: đoạn CSS bố cục | URL cụ thể đã mở, ngày xem | Tên giấy phép, tệp LICENSE, điều kiện giữ thông báo | Dùng có điều kiện / hỏi thêm / không dùng |

Dẫn đúng bản đã dùng, không chỉ trang chủ. Phân biệt **tham khảo ý tưởng thuật toán** với **sao chép cách biểu đạt cụ thể**. Chưa rõ thì khai nguồn và hỏi người chấm, không đổi vài chữ để che dấu vết.

### Bài học

**Công khai không phải giấy phép.** Một sản phẩm đơn giản mình hiểu tốt hơn một giao diện đẹp không rõ nguồn.

## 4.7. Hồ sơ 07 — Khai báo thiếu và ba tầng trách nhiệm

### Sự cố

Bài nộp của nhóm ghi: “Có sử dụng AI để tham khảo.” Nhưng AI đã sinh bản nháp hàm `parseAmount`, gợi ý bảy ca test, và Lan chép một đoạn CSS từ một kho không rõ giấy phép. Minh không chạy test trên máy mình mà chỉ đọc mã. Khi giảng viên hỏi “phần này em kiểm chứng thế nào?”, cả hai nhìn nhau.

### Dấu hiệu

- Một câu khai báo chung chung, không phân biệt gợi ý / sinh nội dung / nhóm sửa gì.
- Không nêu đã chạy gì, trên bản nào.
- Ghi “đã xác minh” trong khi chỉ đọc mã.
- Không nhắc nguồn CSS.

### Nguy cơ

Người chấm không đánh giá được đóng góp thật. Nếu bị hỏi trực tiếp, nhóm không giải thích được — và đó là dấu hiệu mất phần học, không chỉ là lỗi trình bày. Về lâu dài, thói quen khai cao hơn thực tế sẽ theo sang báo cáo thực tập và công việc.

### Các lựa chọn

- **A.** Giữ câu chung chung; nộp kèm toàn bộ lịch sử chat để “đầy đủ”.
- **B.** Viết lại khai báo theo đúng việc đã làm: công cụ, thời điểm, phần được sinh, phần nhóm sửa, đã chạy gì và chưa chạy gì, nguồn CSS. **Loại hoặc thay đoạn CSS chưa rõ quyền** rồi ghi phần đã loại — không giữ lại chỉ vì đã ghi nguồn. Bổ sung phần còn thiếu nếu còn thời gian; nếu không, ghi đúng trạng thái.
- **C.** Ghi “tự làm 100%” vì nhóm đã gõ lại vài dòng.
- **D.** Bỏ phần CSS ra khỏi bài nhưng không nhắc gì trong khai báo.

### Đáp án Hồ sơ 07 — Phân tích từng lựa chọn

**A — Quá tải và rủi ro.** Một câu chung chung không đủ thông tin; dán cả lịch sử chat có thể đưa vào dữ liệu riêng tư không cần thiết. Mô tả đủ để giảng viên đánh giá, theo hình thức giảng viên yêu cầu.

**B — Đúng.** Khai báo tốt phân biệt: AI gợi ý gì, sinh nội dung nào, nhóm thay đổi gì, kiểm chứng đến đâu. Đoạn CSS chưa rõ quyền phải **loại khỏi bài** chứ không chỉ ghi nguồn: thêm dòng nguồn không biến mã không rõ giấy phép thành dùng được. Nếu mới đọc mã mà chưa chạy, ghi “đã rà soát bằng đọc mã; chưa chạy kiểm thử”, không ghi “đã xác minh”. Có thể bổ sung bằng chứng chạy test ngay trên **bản sao của nhóm**: từ thư mục gốc AI-Student-Handbook chạy `node "bai-lam/nam-2-web/test_data.cjs"`, chép nguyên dòng tổng kết cuối và exit code (Bash: `echo $?`; PowerShell: `$LASTEXITCODE`, chạy ngay sau lệnh — xem Chương 2); ghi đúng máy và phiên bản Node đã dùng. Với demo tham khảo chưa sửa, dòng cuối là `34 passed, 0 failed`; bản của nhóm có thể khác nếu đã đổi mã, và khi đó phải ghi đúng con số thực tế.

**C — Sai.** Gõ lại vài dòng không biến phần sinh hàng loạt thành tự làm. Tính trung thực nằm ở độ khớp giữa lời khai và hành động.

**D — Che một phần.** Bỏ đoạn không rõ quyền là tốt, nhưng vẫn cần nói rõ phần đã loại và lý do nếu hình thức khai báo yêu cầu.

Nếu bài **đã nộp** rồi mới phát hiện khai báo thiếu, chủ động gửi một tin ngắn cho giảng viên thay vì chờ bị hỏi:

```text
Thưa thầy/cô, bài [môn, mã bài] nhóm em đã nộp ngày [ngày].
Khai báo AI trong bài còn thiếu: [AI sinh nháp parseAmount, gợi ý 7 ca test].
Bảy ca gợi ý là ca riêng, không nằm trong 34 ca của bộ tham khảo; đừng cộng gộp hai con số.
Nhóm đã [chạy 34 ca / mới đọc mã], và đã [loại đoạn CSS chưa rõ quyền].
Em gửi khai báo sửa lại đính kèm. Nhóm em sẵn sàng giải thích phần đã làm.
```

### Ba tầng trách nhiệm — không đổ lỗi cho công cụ, không nhận bừa mọi lỗi

Minh hỏi: “Nếu AI viết sai thì em chịu hết à?” Cần tách các tầng.

| Tầng | Câu hỏi cần trả lời | Nhóm kiểm soát được | Không nên khẳng định |
| --- | --- | --- | --- |
| Học thuật | Bài có đúng yêu cầu môn; đóng góp và khai báo có trung thực? | Hỏi phạm vi AI, giải thích mã, ghi nguồn, ghi kết quả thật | Mọi dùng AI đều là đạo văn; hoặc khai báo là chắc chắn được chấp nhận |
| Nghề nghiệp | Sản phẩm có được rà soát đúng vai trò và cảnh báo đúng giới hạn? | Kiểm dữ liệu, báo lỗi, yêu cầu người phù hợp duyệt thay đổi | Có AI hỗ trợ thì người làm không còn trách nhiệm; hoặc một người luôn gánh mọi lỗi nhóm |
| Pháp lý | Có vấn đề dữ liệu, quyền tác giả, hợp đồng hay quyền truy cập cần xem xét? | Ngừng hành vi có vấn đề, giữ thông tin cần thiết, báo đầu mối có thẩm quyền | Tự kết luận có tội, mức phạt hay bồi thường từ một ví dụ trong lớp |

Không có một câu “chịu 100% pháp lý” áp dụng cho mọi sinh viên và mọi đầu ra AI. Người nộp bài phải giải thích việc mình làm và mức kiểm tra; kết luận kỷ luật hay pháp lý phụ thuộc quy định, vai trò và tình tiết.

### Chia vai nhưng không tạo khoảng trống

Minh phụ trách nhập và tính tổng; Lan rà soát hiển thị và nguồn; cả hai xem lại bản nộp. **“Lan đã xem” phải rõ là xem gì**: xem diff, đọc hàm, hay chạy ứng dụng. Với `textContent`, bằng chứng là diff và quan sát `<b>Vở</b>` hiện nguyên văn. Với giới hạn 500 khoản, phải thử đúng giới hạn; ảnh tổng 60000 không chứng minh được điều đó.

### Nói mức chắc chắn bằng ngôn ngữ kiểm chứng

| Thay câu này | Bằng câu này |
| --- | --- |
| “An toàn tuyệt đối” | “Đã sửa chỗ hiển thị; ca `<b>Vở</b>` đạt, ca giới hạn 501 khoản chưa chạy” |
| “Không có dữ liệu nhạy cảm” | “Đã rà các tệp X, Y và hai ảnh Z; không thấy email hay khóa thật” |
| “AI bảo là MIT” | “Đã mở tệp LICENSE trong kho, ghi lại tên và phiên bản” |
| “Đã test xong” | “Chạy bộ test trên bản sao bằng Node [phiên bản em dùng]; [số] đạt, [số] không đạt; chưa thử trên trình duyệt khác” |

Nêu giới hạn giúp người đọc đối chiếu, nhưng không được dùng để che việc cốt lõi chưa làm. Phát hiện lỗi thì ghi tác động và cách khắc phục; không sửa lén kết quả cũ.

### Mẫu khai báo AI — điền bằng sự thật

```text
Bài/nhóm: ViSinhVien — [thành viên và vai trò].
Phạm vi được phép: [hướng dẫn của bài hoặc phản hồi giảng viên; nếu chưa rõ, ghi đang chờ].
Công cụ và thời điểm: [tên, phiên bản nếu biết, ngày dùng].
Hỗ trợ thực tế: [giải thích, gợi ý, sinh nháp phần nào; tệp/hàm liên quan].
Đóng góp của nhóm: [ai viết lại gì, lựa chọn nào được giữ hoặc bỏ và lý do].
Dữ liệu đã cung cấp: [bộ dữ liệu giả, đoạn mã cần thiết; không dán bí mật].
Nguồn và giấy phép: [nguồn thật đã dùng, điều kiện cần giữ, phần đã loại vì chưa rõ].
Kiểm chứng: [đã chạy gì, trên bản nào, kết quả; phần chỉ đọc mã; phần chưa xác minh].
Giới hạn: HTML/JavaScript dùng localStorage, không backend/đăng nhập; chỉ phục vụ học tập
với dữ liệu giả. SQL là minh họa Python sqlite3 riêng trong :memory:.
```

Ví dụ đã điền cho đúng tình huống trên — đây là **mẫu, không phải lời khai của bạn**:

```text
Bài/nhóm: ViSinhVien — Minh (nhập, tính tổng), Lan (hiển thị, nguồn).
Phạm vi được phép: theo hướng dẫn học phần; đang chờ xác nhận cho phần sinh mã.
Công cụ và thời điểm: trợ lý AI qua chat, dùng ngày [ngày].
Hỗ trợ thực tế: sinh bản nháp parseAmount trong data.js; gợi ý bảy ca test;
  không sinh phần render hay handler submit.
Đóng góp của nhóm: viết lại parseAmount để từ chối hậu tố; giữ totalExpenses;
  bỏ đoạn CSS nghi không rõ giấy phép.
Dữ liệu đã cung cấp: ba khoản giả 35000, 7000, 18000; không dán dữ liệu thật.
Nguồn và giấy phép: không còn mã ngoài; CSS chưa rõ quyền đã loại khỏi bài.
Kiểm chứng: chạy node bai-lam/nam-2-web/test_data.cjs trên bản sao của nhóm
  (Node [phiên bản]) — [chép nguyên dòng tổng kết, ví dụ 34 passed, 0 failed];
  phần hiển thị mới đọc mã, chưa thử trên trình duyệt khác.
Giới hạn: localStorage, không backend, dữ liệu giả; SQL chỉ là minh họa riêng.
```

### Bài học

**Khai báo tốt là bản đồ đóng góp, không phải câu xin lỗi hay lời khen.** Viết để người khác kiểm lại được, không phải để trông đẹp.

## 4.8. Phòng khám kỹ thuật — SQL, XSS và C++

Ba lỗi dưới đây có cùng một gốc: **biết hợp đồng ở ranh giới, không tin vào một lần chạy may mắn.** Không cần thử chuỗi phá hoại để hiểu bất kỳ lỗi nào.

### 4.8.1. SQL — giá trị là dữ liệu, không phải cấu trúc câu lệnh

**Ranh giới ví dụ:** SQL ở đây chạy riêng bằng Python `sqlite3` với `:memory:`; ViSinhVien không gửi SQL và không có backend. Tệp minh họa là `vi-du/minh-hoa-sqlite.py`. Không nối minh họa này vào sơ đồ kiến trúc ứng dụng Web.

Giả sử bảng minh họa có cột `id`, `title`, `amount`, `category`. Lan muốn tìm một tên thử là `Vở O'Reilly`. Dấu nháy trong tên là dữ liệu bình thường, nhưng cách nối chuỗi sau đưa nó vào cú pháp SQL:

```python
# Mẫu KHÔNG nên dùng; chỉ đọc để nhận diện vấn đề.
query = "SELECT title,amount FROM expenses WHERE title = '" + title + "'"
```

Với tên có dấu nháy, câu lệnh có thể sai cú pháp. Đáng ngại hơn, nối trực tiếp dữ liệu không tin cậy vào câu lệnh có thể cho dữ liệu **làm thay đổi ý nghĩa SQL**. Một tên sách hợp lệ đã đủ chỉ ra chương trình đang trộn hai vai trò: dữ liệu và mã lệnh.

Cách đúng trong ngữ cảnh Python `sqlite3`:

```python
# Rút gọn từ vi-du/minh-hoa-sqlite.py; ở đó biến kết nối tên là connection,
# tạo bằng sqlite3.connect(":memory:").
rows = connection.execute(
    'SELECT title, amount FROM expenses WHERE title = ?',
    (title,)
).fetchall()
```

Dấu `?` là vị trí dành cho giá trị được gắn riêng. `(title,)` là tuple một phần tử; **dấu phẩy tạo tuple**, còn `(title)` chỉ là biểu thức trong ngoặc. Thiếu dấu phẩy là sai cấu trúc đối số. Trình điều khiển tách giá trị khỏi cấu trúc SQL, nên dấu nháy của `Vở O'Reilly` không cần bị thay thế bằng mẹo ghép chuỗi.

OWASP ưu tiên truy vấn tham số hóa cho tình huống này [4]. Tuy vậy, **tham số giá trị không thay thế tùy ý tên bảng, tên cột hay từ khóa sắp xếp**. Nếu chương trình cho chọn cách sắp xếp, hãy ánh xạ lựa chọn sang một tập tên cột định trước — đó là lúc cần danh sách cho phép cho phần cấu trúc.

Chạy minh họa từ thư mục gốc dự án:

```bash
python "vi-du/minh-hoa-sqlite.py"
```

Nếu lệnh `python` không chạy, thử `py` trên Windows hoặc `python3` trên macOS/Linux; trên Windows, gõ `python` khi chưa cài có thể mở Microsoft Store thay vì chạy chương trình. Không có Python thì ghi “chưa chạy, thiếu Python” và đọc tiếp phần giải thích — đây là minh họa khái niệm, không phải điều kiện học xong chương.

Dòng đáng chú ý nhất là `Tra cuu tham so: [("Vở O'Reilly", 12000)]`: dấu nháy đi qua truy vấn như dữ liệu bình thường. Các dòng `PASS reject amount` cho thấy ràng buộc của bảng từ chối số âm, số 0, số thập phân và số vượt `1e9`.

Ghi rõ đây là **fixture SQL riêng**, không thêm nó vào bộ ba khoản chuẩn rồi vẫn tuyên bố tổng 60000. Truy vấn tham số hóa cũng không tự giải quyết phân quyền, rò rỉ log hay mọi lỗi nghiệp vụ.

### 4.8.2. XSS — hiển thị tên khoản chi như văn bản

Minh muốn giao diện linh hoạt nên thử gán tên khoản chi bằng `innerHTML`. Lan đưa đầu vào vô hại `<b>Vở</b>` và hỏi: “Người dùng nhập một cái tên, tại sao ứng dụng lại diễn giải nó thành thẻ?” Nếu giao diện in đậm chữ Vở, trình duyệt đang phân tích đầu vào như HTML. Ví dụ này **không chạy mã độc**, nhưng làm lộ điểm dữ liệu đã bị trao thêm ý nghĩa.

Cách đúng cho một ô bảng cần hiển thị tên dưới dạng văn bản:

```javascript
const td = document.createElement('td');
td.textContent = expense.title;
```

Khi `expense.title` là `<b>Vở</b>`, nội dung mong đợi nhìn thấy là chính chuỗi **`<b>Vở</b>`**, gồm cả dấu ngoặc nhọn, không phải chữ Vở in đậm. `td` là tên biến của đoạn minh họa. Trong `app.js` đi kèm, ô bảng có tên biến `cell`: tìm `cell.textContent = value` trong hàm `render`; `value` lần lượt là tên khoản, nhãn nhóm hoặc số tiền đã định dạng. Không đổi chỗ gán này thành `innerHTML` cho tên khoản chi.

OWASP liệt kê `textContent` là một cách đưa dữ liệu vào nơi nhận văn bản an toàn trong DOM thông thường [5]. Phạm vi “văn bản thông thường” rất quan trọng: cách bảo vệ cho ô bảng **không** tự áp dụng cho URL, thuộc tính sự kiện, CSS hay chuỗi mã JavaScript. Nếu sau này thêm đường dẫn, cần kiểm soát loại URL và ngữ cảnh riêng. Nếu thật sự cần HTML phong phú, đó là yêu cầu mới cần cơ chế làm sạch phù hợp.

Cũng đừng suy luận “dữ liệu nằm trong `localStorage` của em nên tin được”. Người dùng có thể sửa kho lưu trữ, dữ liệu cũ có thể đến từ phiên bản lỗi, máy có thể dùng chung. Hãy kiểm tra lúc nhập, lúc đọc lại và lúc đưa ra giao diện, theo trách nhiệm của từng lớp.

### 4.8.3. C++ — hai lỗi cận khác nhau: bỏ sót và vượt biên

Ở bài năm nhất bằng C++, Minh dùng một `std::vector<long long>` gồm ba số tiền `35000, 7000, 18000`; tổng đúng là **60000**. Với `n` phần tử, chỉ số hợp lệ là `0` đến `n - 1`. Có hai cách viết sai cận, và chúng **không cùng loại lỗi**.

**Lỗi 1 — cận quá hẹp, bỏ sót khoản cuối.** Đây là lỗi có chủ đích trong `vi-du/nam-1-cpp/loi-bo-sot.cpp`:

```cpp
// Trích đoạn rút gọn; chú thích tiếng Việt do chương thêm vào để giải thích.
int n = static_cast<int>(amounts.size());   // n = 3
for (int i = 0; i < n - 1; ++i) {           // CỐ Ý SAI: chỉ chạy i = 0, 1
    total += amounts[i];
}
// Tệp in: Tong chi tieu: 42000 VND — thiếu Vở ghi 18000.
```

Chương trình **không đọc ra ngoài vector**, nên đây không phải hành vi không xác định. Nó chạy ổn định và luôn ra 42000 — một kết quả sai nhưng trông hợp lý, nên dễ lọt nếu không tính tay trước. Sửa bằng `i < n` (trace đầy đủ ở Chương 3, mục 3.2). Kết quả này đã được biên dịch và chạy thật trong lượt kiểm ví dụ của cẩm nang: `Tong chi tieu: 42000 VND`.

**Lỗi 2 — cận quá rộng, vượt biên.** Viết `i <= n` thì lượt cuối đọc `amounts[3]`, một chỉ số không tồn tại. Truy cập ngoài biên bằng `operator[]` dẫn đến **hành vi không xác định**.

“Hành vi không xác định” **không có nghĩa chắc chắn chương trình sẽ crash**. Nó có thể trông như chạy đúng, đọc giá trị lạ hoặc có biểu hiện khác. Một lần chạy không lỗi không chứng minh truy cập đó hợp lệ. Đừng chạy thử truy cập sai rồi dùng việc “máy em vẫn ổn” làm bằng chứng.

Khi đọc vòng lặp duyệt mảng, đối chiếu điều kiện `i < n` — không phải `i < n - 1` (bỏ sót) và không phải `i <= n` (vượt biên). Khi chỉ số đến từ đầu vào, kiểm miền trước khi truy cập. Có thể tìm hiểu `vector::at()` để biết cơ chế báo lỗi ngoài biên của nó, nhưng vẫn phải xử lý đầu vào và lỗi phù hợp.

Bài học chung với JavaScript và SQL: **biết hợp đồng ở ranh giới, không tin vào một lần chạy may mắn.**

## 4.9. Thực hành trước khi nộp: kiểm tra, sửa và đưa bằng chứng

### Bài tập: duyệt một kho ViSinhVien giả định

Bạn rà soát bản nộp của Minh và Lan bằng dữ liệu giả, không truy cập tài khoản thật, không cài gói, không tạo khóa. Các lỗi dưới đây là **phiếu tình huống**, không phải kết luận về kho ví dụ đang có trong gói.

Làm lần lượt: đối chiếu đặc tả → đọc luồng nhập–kiểm tra–lưu–hiển thị → xem nguồn và phạm vi AI → phân loại → sửa → ghi bằng chứng. Nếu chỉ đọc mã, đánh dấu phần chạy thử là **chưa thực hiện**.

| Vấn đề trong kho giả định | Mức xử lý | Cách sửa hoặc quyết định | Bằng chứng cần thu |
| --- | --- | --- | --- |
| Tổng mẫu khác 60000 | Chặn nộp | Rà chuyển đổi số và tính tổng | Đầu vào, tổng trước/sau sửa |
| Nhận 0, số âm, số thập phân hoặc tiền vượt `1e9` | Chặn nộp | Kiểm tra đúng hợp đồng `amount` | Ca bị từ chối; nhận 1 và `1e9` |
| Nhận khoản thứ 501 hoặc tổng rỗng khác 0 | Chặn nộp | Sửa giới hạn và tổng ban đầu | Kết quả thử 500/501 khoản và rỗng |
| Hiện tên bằng `innerHTML` | Chặn nộp | Dùng `cell.textContent` như trong `app.js` | Diff; `<b>Vở</b>` hiện nguyên văn |
| Có dữ liệu thật không cần thiết hoặc khóa thật | Chặn nộp | Dừng chia sẻ; xử lý theo 4.1; dùng dữ liệu giả | Ghi nhận xử lý, không đính kèm bí mật |
| Mã chưa rõ giấy phép | Chặn nộp phần đó | Loại/thay hoặc xác minh quyền | Nguồn, giấy phép hoặc phần thay thế |
| Chưa rõ phạm vi dùng AI | Hỏi giảng viên | Hỏi cụ thể; không mặc định được phép | Phản hồi hoặc trạng thái chờ |
| Khai báo sai mức hỗ trợ AI | Chặn nộp | Khai đúng và theo hướng dẫn môn | Khai báo khớp đóng góp |
| Gói AI đề xuất chưa xác minh | Chặn đưa gói vào bản nộp | Không cài; xác minh hoặc bỏ | Registry, người duy trì, nguồn, giấy phép |
| Màu nút hoặc khoảng cách chưa đẹp | Cải thiện sau | Ưu tiên yêu cầu cốt lõi | Danh sách cải tiến |

Chặn nộp **không** có nghĩa hủy cả bài: có thể loại phần chưa rõ hoặc thu hẹp chức năng nếu vẫn đáp ứng yêu cầu. Hỏi giảng viên không có nghĩa được bỏ qua trong lúc chờ. Màu sắc có thể cải thiện sau; dữ liệu thật trong ảnh thì không.

### Ghi bằng chứng gọn và đối chiếu được

Ghi: **mục tiêu, đầu vào, mong đợi, quan sát, trạng thái, bản mã kiểm tra.** Ví dụ:

```text
Mục tiêu: tổng ba khoản giả.
Đầu vào: 35000, 7000, 18000.
Mong đợi: 60000.
Quan sát: [điền sau khi chạy].
Trạng thái: chưa chạy / đạt / không đạt.
Bản mã: bai-lam/nam-2-web, [ngày hoặc checkpoint đã chạy].
```

Ghi riêng fixture SQL; chỉ giữ vùng ảnh cần thiết.

Hai bộ kiểm thử kèm cẩm nang **không cộng gộp**: `vi-du/nam-2-web/test_data.cjs` có **34 ca** cho phần dữ liệu Web (33 ca gốc cộng một ca hồi quy cho lỗi `category` dạng mảng), còn `vi_sinh_vien.exe --test` của bản C++ (biên dịch từ bản sao `bai-lam/nam-1-cpp/vi_sinh_vien.cpp` theo lệnh ở Chương 2) chỉ in **9 ca**. Bộ đề Final Boss có số ca riêng (Bronze 9, Silver 12), cũng không cộng vào hai bộ này. Số ca không đồng nghĩa đã chạy hay bảo đảm chất lượng. Đối chiếu bộ mình nhận được, ghi cách chạy, số ca thực sự thực thi và kết quả. Chưa có xác nhận thì ghi “chưa xác minh”.

### Rubric bốn mục — tự đánh giá

Mỗi mục 0–2 điểm, tối đa 8. Đây là rubric luyện tập, **không phải thang điểm chính thức của TLU**; điểm tổng không bù được vấn đề chặn nộp.

| Mục | 0 điểm | 1 điểm | 2 điểm |
| --- | --- | --- | --- |
| 1. Trung thực học thuật và nguồn | Không rõ phạm vi, đóng góp hoặc nguồn | Có khai báo nhưng còn mơ hồ | Phạm vi rõ; hỗ trợ, nguồn và quyền được ghi đúng |
| 2. Dữ liệu và quyền truy cập | Dùng dữ liệu thật không cần thiết hoặc quyền quá rộng | Có giảm dữ liệu nhưng chưa rà đủ bản chia sẻ | Dùng dữ liệu giả; rà ảnh/tệp; quyền phù hợp công việc |
| 3. Tính đúng và đọc mã an toàn | Không đối chiếu hợp đồng; nhầm SQL là backend | Biết sửa nhưng bằng chứng còn thiếu | Đối chiếu các giới hạn, hiển thị văn bản và ranh giới ví dụ |
| 4. Kiểm chứng và xử lý vấn đề | Tuyên bố đạt không có căn cứ | Ghi được một phần kết quả và việc còn thiếu | Bằng chứng truy lại được; ưu tiên đúng; báo cáo trung thực |

### Sáu tình huống tự trả lời

**1.** Đề chỉ ghi “tham khảo tài liệu”. Minh khai báo đầy đủ việc AI sinh hàm. Đã chắc được phép chưa?

**2.** Lan bỏ tên trong chi tiêu thật nhưng giữ mã sinh viên, giờ, địa điểm; ảnh còn email. Đã là dữ liệu giả hoặc ẩn danh chưa?

**3.** SQL nối chuỗi bị lỗi với `Vở O'Reilly`. Có nên xóa dấu nháy khỏi tên để sửa?

**4.** `<b>Vở</b>` hiện in đậm; vòng lặp C++ dùng `i <= n` vẫn chạy xong. Đã đạt chưa?

**5.** “Kho công khai không có giấy phép thì được chép, còn GPL cấm thương mại” — đúng không?

**6.** Đã commit khóa thật, Minh xóa tệp, tạo khóa mới rồi định ép đẩy lịch sử. Thiếu gì?

### Đáp án sáu tình huống

**1. Chưa.** Khai báo không thay sự cho phép. Hỏi giảng viên về việc đã làm; không đổi lời khai thành “gợi ý nhẹ”; chưa mặc định phần đó hợp lệ.

**2. Chưa.** Các trường còn lại vẫn có thể nhận diện người. Tạo dữ liệu giả mới, loại ảnh chứa thông tin thật và kiểm tra bản gửi cuối.

**3. Không.** Dùng `execute('SELECT title,amount FROM expenses WHERE title = ?', (title,))`; dấu phẩy tạo tuple một phần tử. Kiểm fixture SQL riêng trong `:memory:`, không thêm backend cho Web.

**4. Chưa.** Tên phải hiện nguyên văn bằng `textContent` trong ô bảng. Riêng phần C++ ở mục 4.8.3: vòng lặp chạm chỉ số `n` (viết `i <= n`) là vượt biên; hành vi không xác định không nhất thiết crash. Sửa theo hợp đồng, không dựa vào may mắn.

**5. Cả hai đều sai.** Công khai không tự cấp quyền. GPL không cấm thương mại; nghĩa vụ phụ thuộc giấy phép và cách chuyển giao, kết hợp mã.

**6.** Dừng chia sẻ; thu hồi và xác nhận khóa cũ đã bị vô hiệu; kiểm tra mức sử dụng trong phạm vi được phép; rà bản liên quan; báo đầu mối và phối hợp giảm bản lưu. Không tự viết lại lịch sử.

### Checklist một trang trước khi gửi

Đánh dấu **sau khi làm**, không đánh dấu theo dự định.

**A. Chặn nộp nếu chưa xử lý**

- [ ] Không còn khóa thật hoặc dữ liệu cá nhân không cần thiết trong tệp, ảnh và nội dung sẽ chia sẻ; sự cố đã phát hiện được báo và xử lý phù hợp.
- [ ] Ba khoản GIẢ đúng 35000 + 7000 + 18000 = 60000; rỗng bằng 0; `amount` nguyên, dương, không quá `1e9`; tối đa 500 khoản.
- [ ] Tên khoản chi hiển thị như văn bản bằng `textContent` (`cell.textContent` trong `app.js`); đã ghi trạng thái kiểm chuỗi `<b>Vở</b>`.
- [ ] Không đưa vào đoạn mã chưa rõ quyền hoặc phụ thuộc chưa kiểm chứng; giữ thông báo giấy phép cần thiết.
- [ ] Khai báo AI đúng việc đã làm; không nhận là tự viết phần được sinh nháp, không ghi đã test khi chưa test.
- [ ] Phần kiểm chứng bắt buộc theo yêu cầu bài đã có kết quả thật; lỗi trọng yếu chưa bị che bằng điểm rubric.

**B. Hỏi giảng viên hoặc người phụ trách khi chưa rõ**

- [ ] Đã làm rõ phạm vi AI, hỗ trợ nhóm và hình thức khai báo; phần chưa rõ được ghi trạng thái chờ.
- [ ] Đã hỏi về nguồn/giấy phép hoặc dữ liệu thật nếu bài bắt buộc dùng mà nhóm chưa xác định được điều kiện.
- [ ] Việc ngoài quyền của nhóm — xử lý tài khoản tổ chức, lịch sử kho chung — được chuyển đúng đầu mối.

**C. Cải thiện sau, không làm sai mô tả hiện tại**

- [ ] Ghi riêng việc chỉnh giao diện và mở rộng tính năng, không lẫn với yêu cầu an toàn cốt lõi.
- [ ] Nêu rõ Web không backend; SQL riêng; không quảng bá `localStorage` là nơi bảo vệ tài chính thực tế.
- [ ] Giữ bằng chứng tối thiểu đủ đối chiếu; tránh tạo thêm ảnh, log hoặc bản sao chứa dữ liệu thừa.

## 4.10. Ranh giới với sản phẩm thật

Kiểm tra trong trình duyệt giúp bài tập nhất quán; nó **không phải** hàng rào đủ cho một hệ thống tài chính. `localStorage` không cung cấp đăng nhập, phân quyền hay bảo vệ dữ liệu tài chính trước mọi người dùng cùng môi trường. ViSinhVien là sản phẩm học tập với dữ liệu giả, **không được quảng bá là ứng dụng tài chính an toàn**.

Nếu làm dịch vụ thật có máy chủ, cần thiết kế xác thực, phân quyền, kiểm tra dữ liệu phía máy chủ và biện pháp vận hành phù hợp. Máy chủ không được tin điều kiện chỉ đặt ở trình duyệt. Đây là ranh giới kiến thức để nhận ra việc mới cần làm, **không phải** yêu cầu nhồi thêm backend vào bài hiện tại.

## 4.11. Tự giảng lại trong 6 phút

Phần này kế thừa speaker notes của nguồn; tham gia tự nguyện.

- **Phút 1.** Kể cảnh Minh định nộp vì tổng đã đúng. Hỏi: “60000 chứng minh được gì, chưa chứng minh được gì?” Chốt: không backend, dữ liệu giả.
- **Phút 2.** Đọc tin nhắn hỏi giảng viên. Nhấn mạnh: phạm vi tùy môn; khai báo không thay giấy phép và không thay sự cho phép.
- **Phút 3.** Dùng hai chuỗi vô hại `Vở O'Reilly` và `<b>Vở</b>` để giải thích tách dữ liệu khỏi cú pháp. Không biểu diễn tấn công, không ngụ ý SQL thuộc Web.
- **Phút 4.** Phân loại một ảnh chứa email và một đoạn mã không giấy phép. Hỏi cách giảm dữ liệu, giảm quyền, giảm phụ thuộc.
- **Phút 5.** Đi qua thứ tự xử lý khóa: dừng chia sẻ → thu hồi/xoay vòng → kiểm tra mức dùng → rà bản liên quan → báo → giảm bản lưu. Nhấn mạnh: xóa tệp không vô hiệu khóa.
- **Phút 6.** Chọn hai dòng “chặn nộp” trong bảng, yêu cầu bằng chứng cụ thể. Kết thúc bằng: “Em biết gì, chưa xác minh gì, bước tiếp theo là gì?”

## 4.12. Tóm tắt và điểm kết năng lực

**Tóm tắt:** Làm chủ ViSinhVien là hiểu đặc tả, biết quyền dùng nguồn và công cụ, kiểm soát dữ liệu đưa đi, kiểm chứng đường đi của đầu vào và khai báo trung thực. `textContent`, truy vấn tham số hóa và kiểm tra giới hạn là biện pháp đúng **trong ngữ cảnh cụ thể**, không phải bùa bảo đảm mọi hệ thống an toàn. Khi có sự cố, ưu tiên khống chế quyền đã lộ và báo đúng người, không chỉ xóa dấu vết nhìn thấy.

**Năng lực mở khóa:** nhận ra một sự cố dữ liệu/quyền/nguồn trong vòng ba phút; chọn hành động ưu tiên đúng; viết được khai báo hỗ trợ AI khớp với việc đã làm; giải thích được vì sao `textContent`, truy vấn tham số hóa và `i < n` đúng trong ngữ cảnh của chúng.

**Chuyển sang Final Boss:** bạn đã có đủ bốn chặng để làm [Build it. Test it. Explain it.](final-boss.md) — nơi hai lỗi chủ đích, diff, test, khai báo và bảo vệ miệng gặp nhau trong một bài nộp.

## Nguồn đối chiếu của chương

Mốc đối chiếu nội dung nguồn: **29/10/2026**, kế thừa từ bản gốc. Các nguồn pháp luật dùng để định hướng và xác định văn bản áp dụng; tình huống thật cần người có thẩm quyền đánh giá. Nội dung các văn bản **chưa được kiểm tra lại** trong lượt biên tập này — hãy mở bản gốc trước khi trích dẫn.

1. [Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf): khái niệm, khử nhận dạng, nguyên tắc, sự đồng ý, ngoại lệ và xử lý dữ liệu trong hoạt động AI.
2. [Nghị định 356/2025/NĐ-CP](https://congbaocdn.chinhphu.vn/180507251028987904/2026/1/17/356signed-1768638052103952849513.pdf): văn bản triển khai tại mốc đối chiếu; Điều 42 về hiệu lực và việc Nghị định 13/2023/NĐ-CP hết hiệu lực.
3. [Văn bản hợp nhất 67/VBHN-VPQH ngày 23/03/2026 về Luật Sở hữu trí tuệ](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469197-1775632354_v1_1775783230_signed.pdf): bảo hộ chương trình máy tính và giới hạn của ngoại lệ liên quan.
4. [OWASP — SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html): truy vấn tham số hóa và danh sách cho phép đối với phần cấu trúc.
5. [OWASP — Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html): nơi nhận dữ liệu an toàn như `textContent` và bảo vệ theo ngữ cảnh.
6. [OWASP — Software Supply Chain Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html): đánh giá phụ thuộc và rủi ro chuỗi cung ứng phần mềm.
7. [GitHub Docs — Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): thu hồi/xoay vòng bí mật trước, giới hạn của việc xóa dữ liệu khỏi lịch sử và các bản sao.
8. [GitHub Docs — Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository): ý nghĩa của giấy phép và giới hạn quyền khi kho chỉ được công khai.

**Nguồn kế thừa:** mục 4.1–4.7 của bản gốc, đối chiếu [bản bảo toàn](../source/Cam-nang-AI-Sinh-vien.original.md), [Source Audit](../editorial/01_SOURCE_AUDIT.md) và [Blueprint](../editorial/02_EDITORIAL_BLUEPRINT.md). Bảy hồ sơ và phòng khám được tái cấu trúc; **không thêm sự kiện, sản phẩm hay mức giá mới**. Các nhận định pháp lý giữ nguyên mức thận trọng của bản gốc và được đánh dấu chưa kiểm tra lại.
