# CHƯƠNG 4 · SỬ DỤNG AI CÓ TRÁCH NHIỆM

Chương 3 đã giúp người học giữ được việc học khi có AI hỗ trợ. Chương này đi tiếp một bước: khi sản phẩm đã chạy đúng, người làm ra nó có thật sự làm chủ nó không. Làm chủ là biết rõ công cụ và nguồn đang dùng, được phép dùng đến đâu, có bằng chứng cho điều đã khẳng định và biết xử lý khi có sai sót. Đây là bước "Có trách nhiệm" trong mạch Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn.

Nhân vật và sự cố trong chương là *tình huống hư cấu*; chương không phải quy định của Trường, không phải tư vấn pháp lý.

**Sau chương này, người học có thể:**

- Xử lý đúng thứ tự khi khóa API bị lộ: thu hồi trước, dọn sau.
- Chọn dữ liệu giả đủ để tái hiện lỗi; nhận ra diff vượt phạm vi và gói thư viện chưa kiểm chứng.
- Phân biệt khai báo với sự cho phép; hiểu giới hạn của "kho công khai", MIT và GPL.
- Giải thích vì sao truy vấn tham số hóa, `textContent` và điều kiện `i < n` là đúng.

## Tình huống mở đầu

Bản Web của ViSinhVien đã hiển thị đúng tổng **60000**, và Minh định nộp ngay. Lan đề nghị trả lời ba câu hỏi trước: một dòng mã từ đâu ra, dữ liệu trong bài là của ai, nhóm đã kiểm tra những gì. Kết quả 60000 chỉ chứng minh phép cộng đúng với ba khoản 35000, 7000, 18000; nó không trả lời được ba câu hỏi đó. Bảy tình huống (4.1–4.7), ba lỗi kỹ thuật (4.8) và danh sách kiểm tra (4.9) lần lượt trả lời. Với mỗi tình huống, hãy chọn một phương án và ghi lý do rồi mới đọc Ý chính.

## 4.1. Tình huống 01 — Khóa API xuất hiện trên GitHub

Tình huống này giúp tránh sai lầm dễ gặp: tưởng xóa dòng chứa khóa là xong. ViSinhVien không cần API key, nhưng trong một bài khác, Minh đặt khóa của một dịch vụ AI trong tệp `config.js` rồi đẩy cả thư mục lên kho GitHub công khai để nhờ Lan xem. Sáng hôm sau, Lan phát hiện dòng `API_KEY = ...`. Minh nên làm gì **đầu tiên**: xóa dòng đó rồi commit lại; tạo khóa mới; thu hồi khóa ở nhà cung cấp; hay viết lại lịch sử Git và ép đẩy?

### Ý chính

Xóa dòng trong tệp **không vô hiệu hóa khóa**: bản cũ vẫn nằm trong lịch sử Git, bản clone của người khác, bộ nhớ đệm hoặc đoạn chat từng dán, và khóa còn hiệu lực đến khi được thu hồi. Tạo khóa mới mà để khóa cũ hoạt động là chưa xong. Viết lại lịch sử kho ảnh hưởng mọi người đang dùng kho mà vẫn không xóa được bản clone; việc này do người quản lý kho quyết định.

![Sáu bước theo đúng thứ tự trong chương: 01 dừng chia sẻ thêm; 02 thu hồi key ở nhà cung cấp, ô lớn bên trái; 03 kiểm tra mức sử dụng; 04 rà bản liên quan; 05 báo đúng đầu mối; 06 giảm bản lưu và chặn tái diễn, không tự viết lại lịch sử kho mã. Nhãn KEY_DEMO_INVALID không phải key thật.](../assets/security.svg)

Sáu bước đúng thứ tự: (1) dừng chia sẻ thêm; (2) thu hồi hoặc xoay vòng khóa, xác nhận trạng thái "đã thu hồi" trong trang quản lý, không gọi thử API bằng khóa cũ; khóa không thuộc tài khoản của Minh thì báo ngay người có quyền; (3) kiểm tra mức sử dụng; (4) rà bản liên quan: commit, tệp cấu hình, ảnh chụp, đoạn chat; (5) báo đúng đầu mối (giảng viên hoặc trưởng nhóm), **không đính kèm khóa**; (6) giảm bản còn lưu, dùng placeholder như `DEMO_KEY_NOT_A_SECRET`, thêm bước rà tệp trước khi đẩy. Nguyên tắc: **thu hồi trước, dọn sau; báo sự cố bằng mô tả, không bằng bí mật.**

### Thử ngay (10 phút)

Hãy gập hình lại, viết từ trí nhớ sáu bước đúng thứ tự. Rồi viết thông báo sự cố năm dòng gửi giảng viên: thời điểm phát hiện, phạm vi đã chia sẻ, trạng thái khóa cũ, đã kiểm tra mức sử dụng chưa, điều cần hướng dẫn. Ghi vào `ghi-chep-04.txt` trong `bai-lam`.

### Gợi ý đối chiếu

Thứ tự đúng hướng nếu "thu hồi" đứng trước mọi bước "dọn". Thông báo đạt nếu người đọc biết phải làm gì tiếp mà không cần thấy khóa.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Khóa thuộc tài khoản nơi thực tập: bước nào thay đổi, bước nào giữ nguyên?
- **Từ khóa tra cứu:** secret rotation, removing sensitive data from a repository.
- **Trong Sổ tay thực hành:** [Hồ sơ 01](../chapters/chapter-04.md#muc-4-1): năm phương án, sáu bước chi tiết, mẫu thông báo.

## 4.2. Tình huống 02 — Dữ liệu cá nhân trong cửa sổ chat

Tình huống này giúp tránh đưa dữ liệu cá nhân vào cửa sổ chat khi không cần. Để nhờ AI tìm lỗi tính tổng, Minh định gửi ảnh chụp bảng chi tiêu thật trong tháng: có tên quán quen, giờ giao dịch, mã sinh viên và góc màn hình còn hiện email. Minh cho rằng đổi tên thành "Sinh viên A" là đủ. Minh nên gửi: ảnh nguyên bản; ảnh đã đổi tên; ảnh che bằng một lớp hình chữ nhật; hay ba khoản giả 35000, 7000, 18000 cùng hàm tính tổng?

### Ý chính

Câu hỏi đầu tiên là **"lỗi này cần tối thiểu dữ liệu gì để tái hiện?"**. Lỗi bỏ sót khoản cuối tái hiện được bằng ba khoản giả: 42000 thay vì 60000. Dữ liệu tạo mới không liên hệ với ai, nên đó là phương án tốt nhất. Đổi tên chưa phải ẩn danh: mã sinh viên, giờ, quán quen và email vẫn đủ để người quen nhận ra. Lớp che trong tệp chỉnh sửa có thể bị gỡ. Giả định "dịch vụ không lưu" không có căn cứ khi chưa đọc điều khoản.

| Nhóm dữ liệu | Cách hiểu | Lựa chọn |
| --- | --- | --- |
| Giả | Tạo mới để thử, không phải hồ sơ thật sửa sơ qua | 35000, 7000, 18000; email giả `demo001@example.invalid` |
| Đã khử nhận dạng | Không còn xác định được một người, kể cả khi ghép dữ liệu khác | Không mặc định là ẩn danh sau khi bỏ tên |
| Cá nhân, bí mật | Gắn với một người, tài khoản hoặc quyền truy cập | Mã sinh viên, chi tiêu thật, mật khẩu, khóa API: không đưa vào ví dụ |

Về pháp luật, chương tham chiếu Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Luật số 131/2025/QH15 sửa đổi Luật Sở hữu trí tuệ (*Chưa kiểm chứng* sau mốc 29/10/2026; không phải ý kiến pháp lý). Nguyên tắc: **dữ liệu giả không phải dữ liệu thật đã đổi tên, mà là dữ liệu được tạo mới.**

### Thử ngay (10 phút)

Hãy chụp màn hình bàn làm việc hiện tại (không gửi ai) và liệt kê mọi thứ trong ảnh có thể giúp nhận ra một người: tên tệp, tab, email, thông báo. Rồi viết bộ dữ liệu giả tối thiểu tái hiện lỗi bỏ sót khoản cuối: ba khoản và một dòng kết quả sai mong đợi. Xóa ảnh sau khi xong.

### Gợi ý đối chiếu

Danh sách đúng hướng nếu có ít nhất một mục ngoài vùng bảng chi tiêu, chẳng hạn thanh tab. Bộ dữ liệu giả đạt nếu không trùng dữ liệu thật và vẫn cho ra 42000 khi hàm bỏ sót khoản cuối.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Dữ liệu đã công khai ở nơi khác có đương nhiên phù hợp để thu gom và gửi cho một dịch vụ AI không?
- **Từ khóa tra cứu:** synthetic data, de-identification, khử nhận dạng.
- **Trong Sổ tay thực hành:** [Hồ sơ 02](../chapters/chapter-04.md#muc-4-2): bốn phương án, bảng phân loại, căn cứ pháp lý.

## 4.3. Tình huống 03 — Agent sửa và xóa ngoài phạm vi

Tình huống này giúp tránh nhận kết quả của Agent chỉ vì màn hình kiểm thử màu xanh. Lan giao cho Agent: "Sửa lỗi tổng tiền trong `bai-lam/nam-2-web`." Agent báo xong. Diff cho thấy hàm tính tổng đã sửa, nhưng `index.html` bị đổi giao diện, hai ca đang thất bại trong `test_data.cjs` bị xóa, và Agent đề nghị cài một gói định dạng mã. Kiểm thử toàn màu xanh. Lan nên: chấp nhận toàn bộ; quay về checkpoint rồi chỉ áp dụng lại phần sửa hàm tính tổng; yêu cầu Agent "khôi phục như cũ"; hay tự gõ lại hai ca theo trí nhớ? (Chi tiết hư cấu; tệp đi kèm vẫn đủ 34 ca.)

### Ý chính

Bốn dấu hiệu vượt phạm vi: diff chạm tệp ngoài mục tiêu; số ca kiểm thử **giảm** đúng bằng số ca đang thất bại; có lệnh cài đặt không được yêu cầu; báo cáo "đã xong" không nêu ca nào bị xóa. Kiểm thử đạt vì ca khó đã biến mất là bằng chứng giả. Nhận toàn bộ thay đổi là nhận trách nhiệm cho cả phần chưa đọc.

Phương án đúng: dừng Agent, quay về checkpoint tạo trước khi giao việc, đọc và hiểu diff của riêng phần sửa hàm tính tổng, áp dụng lại đúng phần đó, chạy đầy đủ bộ kiểm thử gốc. Yêu cầu Agent "khôi phục như cũ" là giao quyền cho chính công cụ vừa vượt phạm vi mà không có bằng chứng.

Câu prompt "chỉ sửa tệp X" là **yêu cầu**, không phải hàng rào kỹ thuật; quyền thực tế nằm ở thiết lập công cụ. Nguyên tắc: **tạo checkpoint trước, đọc diff sau, nhận thay đổi từng phần.** Số ca kiểm thử phải giữ nguyên hoặc tăng; thấy giảm là dừng lại hỏi "ca nào đã biến mất, vì sao?".

### Thử ngay (10 phút)

Hãy viết "hợp đồng giao việc" sáu dòng cho Agent trước khi sửa lỗi tổng tiền: phạm vi (tệp, hàm); không sửa tệp khác, không xóa ca test; không cài gói, không commit, không truy cập mạng; điều phải báo trước khi sửa; điều phải báo sau khi sửa; làm gì khi bị chặn hoặc cần quyền mới.

### Gợi ý đối chiếu

Hợp đồng đạt nếu người khác đọc xong chỉ ra ngay việc xóa hai ca test và đề nghị cài gói vi phạm dòng nào. Chỉ có "sửa lỗi tổng tiền" mà không có dòng "không" là chưa đạt.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu Lan chưa tạo checkpoint, đường quay lại nào còn khả thi mà không phải tin vào lời Agent?
- **Từ khóa tra cứu:** agent permissions, checkpoint, diff review.
- **Trong Sổ tay thực hành:** [Hồ sơ 03](../chapters/chapter-04.md#muc-4-3): bốn phương án, hợp đồng giao việc mẫu; [Bài thực hành 06](../chapters/chapter-02.md#muc-2-6): checkpoint và diff.

## 4.4. Tình huống 04 — Gói thư viện do AI đề xuất

Tình huống này giúp tránh cài gói thư viện chỉ vì AI đề xuất với giọng chắc chắn. Minh hỏi AI cách định dạng số tiền cho dễ đọc. AI trả lời rất tự tin, đưa lệnh cài một gói có tên gần giống một thư viện quen thuộc, kèm câu "chạy lệnh này là xong". Minh chưa từng nghe tên gói này. Minh nên: chạy ngay; hỏi lại AI "gói này có an toàn không"; kiểm tra bài có cần thêm phụ thuộc không rồi đối chiếu trên registry chính thức; hay cài vào thư mục tạm "để thử"?

### Ý chính

Câu hỏi đầu tiên luôn là **"bài có cần thêm phụ thuộc không?"**. Với ứng dụng HTML và JavaScript nhỏ, câu trả lời thường là không: API có sẵn của trình duyệt đã định dạng được số tiền.

Nếu thật sự cần, bằng chứng phải đến từ registry chính thức và kho nguồn. Hỏi lại AI là lập luận vòng tròn: cùng một nguồn vừa đề xuất vừa tự chứng nhận. Tên gần giống thư viện phổ biến nhưng khác vài ký tự là dấu hiệu *typosquatting*, đặt tên để đánh lừa người cài. Gói độc hại có thể chạy script ngay khi cài và đọc tệp cấu hình, khóa; cài "để thử" vẫn là chạy mã. Lockfile cố định phiên bản nhưng không biến gói độc hại thành đáng tin.

Bảng kiểm chứng gồm tám câu hỏi: tên gói trên registry, phiên bản, người duy trì, kho nguồn, giấy phép, script cài đặt, cảnh báo bảo mật, phụ thuộc bắc cầu. Không tự tạo URL để điền cho đủ; một ô trống trung thực có giá trị hơn dòng "đã kiểm" không căn cứ. Nguyên tắc: **không cài gói chỉ để tỏ ra chủ động.**

### Thử ngay (10 phút)

Không cài gì. Hãy lập bảng kiểm chứng tám dòng cho một gói từng thấy ai đó cài. Mỗi dòng ghi **nơi** tìm bằng chứng, không ghi kết luận. Cuối bảng trả lời: bài ViSinhVien có cần gói này không, vì sao.

### Gợi ý đối chiếu

Bảng đúng hướng nếu mọi "nơi tìm bằng chứng" đều là registry, kho nguồn hoặc trang tư vấn bảo mật, không dòng nào ghi "hỏi AI". Câu trả lời cuối đạt nếu nêu được cách định dạng tiền không cần phụ thuộc mới.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Gói đã nằm trong lockfile của dự án nhóm từ trước thì còn cần kiểm chứng không?
- **Từ khóa tra cứu:** typosquatting, software supply chain, lockfile.
- **Trong Sổ tay thực hành:** [Hồ sơ 04](../chapters/chapter-04.md#muc-4-4): bốn phương án, bảng kiểm chứng đầy đủ.

## 4.5. Tình huống 05 — Bài tập hoàn toàn do AI làm

Tình huống này giúp tránh nhầm "được tham khảo" với "được để AI làm thay". Đề ViSinhVien ghi "Được tham khảo tài liệu", không nhắc AI. Minh dán toàn bộ đề vào chat, nhận về đầy đủ `index.html`, `data.js`, `app.js`, sửa vài chỗ, chương trình chạy được, và định khai báo "Có tham khảo ý tưởng từ AI". Minh nên: nộp với khai báo đó; hỏi giảng viên bằng tin nhắn mô tả đúng việc đã làm; xóa hết rồi viết lại theo trí nhớ; hay không khai báo vì "ai cũng dùng"?

### Ý chính

"Tham khảo tài liệu" **không đồng nghĩa** với "được để AI viết hộ". Đề không nói rõ thì tình trạng là *chưa rõ*: hỏi giảng viên trước, không biến giả định thành sự cho phép, không coi im lặng là đồng ý. AI sinh toàn bộ hàm thì khai báo phải ghi đúng như vậy; "có tham khảo ý tưởng" là khai báo thấp hơn thực tế. **Khai báo không thay thế sự cho phép.** Cách đúng là hỏi phạm vi rồi tự làm lại phần cốt lõi trên cơ sở hiểu rõ. Minh không giải thích được vì sao bước kiểm tra `amount` đặt ở đó: dấu hiệu đã mất phần học.

| Tình trạng | Ví dụ | Việc cần làm |
| --- | --- | --- |
| Đã được cho phép | Đề cho dùng AI gợi ý ca kiểm thử | Dùng đúng phần được phép, lưu phần hỗ trợ |
| Đã bị cấm | Bài kiểm tra yêu cầu tự viết | Không nhờ AI tạo hay sửa mã khi làm bài |
| Chưa rõ | Đề cho tham khảo tài liệu, không nói về AI | Hỏi giảng viên trước |
| Có điều kiện | Được giải thích, không được sinh toàn bộ chức năng | Tách câu hỏi giải thích khỏi yêu cầu viết hộ |

Bảng không phải quy định của Trường; bảng giúp đặt câu hỏi đúng. Nguyên tắc: **khai báo là mô tả, không phải xin phép; hỏi phạm vi trước, khai báo sau, đúng việc đã làm.**

### Thử ngay (10 phút)

Hãy viết tin nhắn hỏi giảng viên cho tình huống của Minh, tối đa năm dòng, ngôi "em": phần định tự làm; việc cụ thể muốn dùng AI; điều không định làm; câu hỏi "phạm vi này có được phép không"; hướng làm nếu không được.

### Gợi ý đối chiếu

Tin nhắn đạt nếu giảng viên có thể trả lời "được" hoặc "không" mà không phải hỏi lại "em định dùng AI vào việc gì". Chỉ hỏi "em có được dùng AI không ạ" là chưa đủ cụ thể.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Giảng viên trả lời "được dùng AI để giải thích lỗi": hàm `parseAmount` do AI sinh nháp có thuộc phạm vi đó không?
- **Từ khóa tra cứu:** academic integrity, AI use policy.
- **Trong Sổ tay thực hành:** [Hồ sơ 05](../chapters/chapter-04.md#muc-4-5): tin nhắn mẫu, bảng phân loại đầy đủ; [Thỏa thuận học tập](../chapters/learning-agreement.md): phạm vi dùng AI, phần việc tự làm, bằng chứng cần có.

## 4.6. Tình huống 06 — Đoạn mã không rõ giấy phép

Tình huống này giúp tránh dùng mã của người khác khi chưa rõ quyền. Minh tìm thấy một giao diện đẹp trên GitHub. Vì kho mở được mà không cần đăng nhập, Minh định chép một tệp vào ViSinhVien. Kho **không có tệp LICENSE**. Minh nên: chép và ghi nguồn cuối bài; tự viết bảng khoản chi đơn giản mà Minh hiểu rõ; đổi tên biến và màu sắc để "không ai nhận ra"; hay nhờ AI viết lại giao diện từ ảnh chụp?

### Ý chính

**Công khai không phải là giấy phép.** Kho mở được cho mọi người **không** tự động trao quyền sao chép, phân phối hay tạo tác phẩm phái sinh. Ghi nguồn là yêu cầu học thuật, không thay thế quyền sử dụng. Đổi tên biến hay màu sắc vẫn là sao chép. Nhờ AI "vẽ lại" từ ảnh cũng chưa chắc ổn: nhãn "do AI tạo" không chứng minh nguồn gốc. Phương án đúng trong bài này là tự viết bảng đơn giản mà nhóm hiểu rõ từng phần.

Đọc tên giấy phép cũng chưa đủ. MIT cho quyền dùng rộng nhưng phải giữ thông báo bản quyền và giấy phép khi sao chép. GPL **không** phải "cấm thương mại"; nghĩa vụ tùy phiên bản và cách kết hợp mã, chưa rõ thì hỏi người có chuyên môn. Kho không có giấy phép thì không có cơ sở coi là được tự do sao chép; mã do AI đưa ra cũng cần kiểm tra nguồn và điều khoản công cụ.

Theo Luật Sở hữu trí tuệ Việt Nam, chương trình máy tính được bảo hộ; "sao chép để học" không tự động là ngoại lệ (mốc đối chiếu ở mục 4.2). Điều này không cấm học từ tài liệu; nó nhắc kiểm tra quyền trước khi đưa mã vào bài nộp.

### Thử ngay (10 phút)

Hãy điền "thẻ nguồn" bốn cột cho một thành phần từng định dùng lại: thành phần; nguồn và phiên bản (URL cụ thể, ngày xem); giấy phép và việc phải giữ; quyết định (dùng có điều kiện, hỏi thêm, không dùng). Cột không điền được thì ghi "chưa rõ" thay vì đoán.

### Gợi ý đối chiếu

Thẻ đạt nếu cột "giấy phép" lấy từ tệp LICENSE thật, không từ trí nhớ hay câu trả lời của AI; và nếu cột đó là "chưa rõ" thì cột "quyết định" không thể là "dùng".

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Kho có LICENSE là MIT nhưng thư mục ảnh và phông chữ ghi điều kiện khác: phần nào được dùng theo MIT?
- **Từ khóa tra cứu:** MIT License, GPL, licensing a repository.
- **Trong Sổ tay thực hành:** [Hồ sơ 06](../chapters/chapter-04.md#muc-4-6): bảng giấy phép đầy đủ, thẻ nguồn, tham chiếu điều luật.

## 4.7. Tình huống 07 — Khai báo thiếu và ba tầng trách nhiệm

Tình huống này giúp tránh khai báo chung chung và hiểu ai chịu trách nhiệm ở mỗi tầng. Bài nộp của nhóm ghi: "Có sử dụng AI để tham khảo." Thực tế, AI đã sinh nháp hàm `parseAmount` và gợi ý bảy ca kiểm thử; Lan chép một đoạn CSS từ kho không rõ giấy phép; Minh chỉ đọc mã, không chạy kiểm thử. Giảng viên hỏi "phần này em kiểm chứng thế nào?", cả hai không trả lời được. Nhóm nên: giữ câu khai báo và nộp kèm toàn bộ lịch sử chat; viết lại khai báo đúng việc đã làm, loại đoạn CSS; hay ghi "tự làm 100%"?

### Ý chính

Khai báo tốt phân biệt rõ: AI gợi ý gì, sinh nội dung nào, nhóm thay đổi gì, đã kiểm chứng đến đâu. Đoạn CSS chưa rõ quyền phải **loại khỏi bài** và nêu rõ phần đã loại; ghi nguồn không biến nó thành mã được phép dùng. Mới đọc mã thì ghi "đã rà soát bằng đọc mã; chưa chạy kiểm thử", không ghi "đã xác minh". Gõ lại vài dòng không biến phần được sinh thành phần tự làm.

Mẫu khai báo, chỉ điền thông tin đúng thực tế:

```text
Bài/nhóm: [tên bài; thành viên và vai trò].
Phạm vi được phép: [theo đề hoặc phản hồi giảng viên; chưa rõ thì ghi đang chờ].
Công cụ và thời điểm: [tên, phiên bản nếu biết, ngày dùng].
Hỗ trợ thực tế: [giải thích, gợi ý hay sinh nháp phần nào; tệp, hàm liên quan].
Đóng góp của nhóm: [ai viết lại gì; giữ hoặc bỏ gì, vì sao].
Dữ liệu đã cung cấp: [dữ liệu giả, đoạn mã cần thiết; không dán bí mật].
Nguồn và giấy phép: [nguồn đã dùng, điều kiện phải giữ, phần đã loại].
Kiểm chứng: [đã chạy gì, trên bản nào, kết quả; phần chỉ đọc mã, chưa xác minh].
```

Khi AI viết sai, người nộp có chịu toàn bộ trách nhiệm không? Cần tách ba tầng: **học thuật** (bài đúng yêu cầu môn học; đóng góp và khai báo trung thực); **nghề nghiệp** (sản phẩm được rà soát đúng vai trò, nêu đúng giới hạn); **pháp lý** (dữ liệu, quyền tác giả, quyền truy cập do người có thẩm quyền xem xét). Không có câu "chịu 100% trách nhiệm" cho mọi trường hợp, cũng không đổ hết cho công cụ. Nguyên tắc: **khai báo tốt là bản đồ đóng góp, không phải lời xin lỗi hay lời tự khen.**

### Thử ngay (10 phút)

Hãy điền mẫu trên cho một bài gần nhất có dùng AI. Ở dòng "Kiểm chứng", thay "đã test xong", "an toàn tuyệt đối" bằng câu kiểm chứng được: chạy gì, trên bản nào, bao nhiêu ca đạt, phần nào chưa thử.

### Gợi ý đối chiếu

Khai báo đạt nếu mỗi dòng có một chi tiết cụ thể (tên hàm, số ca, ngày) và không dòng nào chỉ ghi "có tham khảo". Dòng "Kiểm chứng" đạt nếu người khác lặp lại được việc đã chạy và thấy phần còn bỏ trống.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Bài đã nộp rồi mới phát hiện khai báo thiếu: nhóm nên chủ động gửi gì cho giảng viên, và gửi gì thì không nên?
- **Từ khóa tra cứu:** AI disclosure statement, accountability.
- **Trong Sổ tay thực hành:** [Hồ sơ 07](../chapters/chapter-04.md#muc-4-7): bảng ba tầng, mẫu khai báo bổ sung sau khi nộp, ví dụ điền mẫu.

## 4.8. Ba lỗi kỹ thuật ở ranh giới dữ liệu: SQL, XSS và C++

Ba lỗi trong mục này có chung một gốc: người viết mã không nắm rõ **hợp đồng ở ranh giới**, tức các điều kiện mà dữ liệu phải thỏa mãn khi đi qua một lớp của chương trình, và tin vào một lần chạy may mắn.

### Ý chính

**SQL: giá trị là dữ liệu, không phải cấu trúc câu lệnh.** Ví dụ SQL chạy riêng bằng Python `sqlite3` với `:memory:` trong `vi-du/minh-hoa-sqlite.py`; ViSinhVien không có backend. Lan cần tìm khoản tên `Vở O'Reilly`. Khi nối chuỗi `"... WHERE title = '" + title + "'"`, dấu nháy rơi vào cú pháp SQL: câu lệnh sai, và nghiêm trọng hơn, dữ liệu có thể **làm thay đổi ý nghĩa câu lệnh**. Đó là gốc của lỗi chèn mã SQL (*SQL injection*). Cách đúng là truy vấn tham số hóa: `execute('SELECT title, amount FROM expenses WHERE title = ?', (title,))`; dấu `?` giữ chỗ cho giá trị gắn riêng, `(title,)` có dấu phẩy để tạo tuple một phần tử.

**XSS: hiển thị tên khoản chi dưới dạng văn bản.** Minh thử gán tên khoản chi bằng `innerHTML`. Lan kiểm tra bằng đầu vào vô hại `<b>Vở</b>`: nếu chữ Vở hiện in đậm, trình duyệt đang phân tích đầu vào như HTML, dù người dùng chỉ nhập một cái tên. Đây là gốc của lỗi chèn mã kịch bản liên trang (*Cross-Site Scripting*, XSS). Cách đúng cho ô bảng:

```javascript
const td = document.createElement('td');
td.textContent = expense.title;
```

*Kết quả mong đợi*: ô bảng hiện nguyên chuỗi `<b>Vở</b>`, gồm cả dấu ngoặc nhọn. Biện pháp này đúng cho vị trí nhận văn bản thông thường, không tự áp dụng cho URL, thuộc tính sự kiện hay CSS.

**C++: hai lỗi cận khác nhau.** Với `std::vector<long long>` chứa 35000, 7000, 18000, chỉ số hợp lệ từ `0` đến `n - 1`. Viết `i < n - 1` là cận quá hẹp: chương trình chạy ổn định và luôn in 42000, sai nhưng trông hợp lý. Viết `i <= n` là cận quá rộng: lượt cuối đọc `amounts[3]`, chỉ số không tồn tại, dẫn đến **hành vi không xác định** (*undefined behavior*); chương trình không chắc crash, có thể trông như chạy đúng, nên một lần chạy không báo lỗi không chứng minh gì. Điều kiện đúng là `i < n`.

Bài học chung: **nắm rõ hợp đồng ở ranh giới, không tin vào một lần chạy may mắn.**

### Thử ngay (10 phút)

Không cần chạy mã. Hãy viết ba dòng dự đoán: (1) với tên `Vở O'Reilly`, câu SQL nối chuỗi tạo ra chuỗi lệnh nào; (2) với `expense.title` là `<b>Vở</b>`, ô dùng `textContent` và ô dùng `innerHTML` hiện gì; (3) với `i < n - 1` tổng in ra bao nhiêu, với `i <= n` chạm tới chỉ số nào. Rồi mở `vi-du/nam-2-web/app.js`, tìm dòng `cell.textContent` và ghi tên hàm chứa nó.

### Gợi ý đối chiếu

Dự đoán đúng hướng nếu dòng (1) có hai dấu nháy đơn liền nhau bất thường, dòng (2) phân biệt "hiện nguyên chuỗi" với "hiện chữ in đậm", dòng (3) ghi 42000 và chỉ số 3, không ghi "chắc chắn crash".

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Ứng dụng cho người dùng chọn cột để sắp xếp: vì sao dấu `?` không giải quyết được, và danh sách cho phép trông như thế nào?
- **Từ khóa tra cứu:** parameterized query, textContent vs innerHTML, undefined behavior.
- **Trong Sổ tay thực hành:** [Ba lỗi kỹ thuật ở ranh giới dữ liệu](../chapters/chapter-04.md#muc-4-8): cách chạy `vi-du/minh-hoa-sqlite.py`, kết quả mong đợi, trích đoạn C++; [Bài thực hành 03](../chapters/chapter-02.md#muc-2-3): bảng trace cho lỗi bỏ sót 18000.

## 4.9. Danh sách kiểm tra trước khi nộp

Mục này gom cả chương thành một danh sách để rà bài trong mười phút trước khi nộp. Chỉ đánh dấu **sau khi đã thực hiện**, không đánh dấu theo dự định.

### Ý chính

"Chặn nộp" không có nghĩa là hủy cả bài: nhóm có thể loại phần chưa rõ hoặc thu hẹp chức năng.

**Chặn nộp nếu chưa xử lý**

- [ ] Không còn khóa thật hoặc dữ liệu cá nhân không cần thiết trong tệp, ảnh, nội dung sẽ chia sẻ (4.1, 4.2).
- [ ] Ba khoản giả cho tổng 35000 + 7000 + 18000 = 60000; danh sách rỗng có tổng 0; `amount` nguyên dương, không quá `1e9`; tối đa 500 khoản.
- [ ] Tên khoản chi hiển thị bằng `textContent`; đã thử với `<b>Vở</b>` (4.8).
- [ ] Không có mã chưa rõ quyền hoặc gói chưa kiểm chứng (4.4, 4.6).
- [ ] Khai báo AI khớp việc đã làm; không ghi "đã kiểm thử" khi chưa chạy (4.5, 4.7).
- [ ] Diff của lượt Agent gần nhất đã được đọc; số ca kiểm thử không giảm (4.3).

**Hỏi giảng viên khi chưa rõ**

- [ ] Phạm vi dùng AI và hình thức khai báo đã rõ; phần chưa rõ ghi ở trạng thái chờ.
- [ ] Việc ngoài quyền của nhóm (tài khoản tổ chức, lịch sử kho chung) đã chuyển đúng đầu mối.

**Cải thiện sau**

- [ ] Chỉnh giao diện, mở rộng tính năng ghi riêng, không lẫn với yêu cầu an toàn.
- [ ] Nêu rõ bản Web không có backend; SQL là minh họa riêng.

Mỗi dấu kiểm cần bằng chứng ngắn: mục tiêu, đầu vào, kết quả mong đợi, kết quả quan sát, trạng thái, bản mã.

### Thử ngay (10 phút)

Hãy mở bài gần nhất và đi qua đủ mười dòng. Với mỗi dòng, ghi một trong ba trạng thái: đã làm và có bằng chứng; chưa làm; không áp dụng. Ghi thêm một dòng cho mục "chưa làm" quan trọng nhất: việc cụ thể sẽ làm trước khi nộp.

### Gợi ý đối chiếu

Kết quả đúng hướng nếu có ít nhất một dòng "chưa làm" được ghi trung thực; danh sách toàn dấu kiểm sau mười phút thường là đánh dấu theo dự định.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Hai bộ kiểm thử đi kèm (34 ca Web, 9 ca C++) vì sao không được cộng gộp khi báo cáo?
- **Từ khóa tra cứu:** pre-submission checklist, evidence log, exit code.
- **Trong Sổ tay thực hành:** [Thực hành trước khi nộp](../chapters/chapter-04.md#muc-4-9): bài rà soát kho giả định, mẫu ghi bằng chứng, rubric luyện tập, câu hỏi có đáp án.

## Tóm tắt chương

- Khóa bị lộ: thu hồi trước, dọn sau; báo sự cố bằng mô tả, không bằng bí mật.
- Dữ liệu gửi cho AI: dữ liệu giả đủ để tái hiện lỗi; đổi tên chưa phải ẩn danh.
- Agent và gói thư viện: checkpoint trước, đọc diff sau; số ca kiểm thử không giảm; không cài gói chỉ vì AI đề xuất.
- Liêm chính và bản quyền: khai báo là mô tả, không phải xin phép; công khai không phải là giấy phép.
- Ranh giới dữ liệu: truy vấn tham số hóa, `textContent`, điều kiện `i < n`.

**Ba câu để tự kiểm**

1. Minh đã xóa `config.js` và tạo khóa mới. Việc quan trọng nhất còn thiếu là gì?
2. Lan bỏ tên trong bảng chi tiêu thật nhưng giữ mã sinh viên và giờ giao dịch. Đây đã là dữ liệu giả hay ẩn danh chưa?
3. Nhận định "kho công khai không có giấy phép thì được chép, còn GPL cấm thương mại" sai ở đâu?

## Cầu nối sang chương sau

Đến đây, người học đã nắm vai trò của AI, cách dùng có kiểm soát, cách giữ việc học và các ranh giới cần tôn trọng. Chương 5 giúp chọn AI, model và gói dịch vụ phù hợp với nhiệm vụ, mức rủi ro và ngân sách, thay vì dựa vào danh tiếng.

## Tài liệu tham khảo

Mốc đối chiếu 29/10/2026; thông tin pháp luật *chưa kiểm chứng* sau mốc này.

1. Quốc hội. [Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15](https://congbaocdn.chinhphu.vn/CongBaoCP/VanBan/2025/6/45578/57730-1-2025971-97291-2025-qh15.pdf).
2. Văn phòng Quốc hội. [Văn bản hợp nhất số 67/VBHN-VPQH Luật Sở hữu trí tuệ](https://congbaocdn.chinhphu.vn/180507251028987904/2026/4/10/469197-1775632354_v1_1775783230_signed.pdf), thể hiện sửa đổi theo Luật số 131/2025/QH15.
3. OWASP. [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).
4. OWASP. [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
5. GitHub. [Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
6. GitHub. [Licensing a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
