# CHƯƠNG 5 · LỰA CHỌN AI VÀ MODEL PHÙ HỢP VỚI NHIỆM VỤ

Bốn chương trước đã đi qua bốn bước: hiểu vai trò của AI, dùng AI có kiểm soát, giữ vững việc tự học và giữ ranh giới về dữ liệu, bản quyền, liêm chính. Chương này là bước thứ năm, bước "Chọn": với nhiệm vụ cụ thể, nên dùng AI nào, model nào, trả tiền hay không và trả bao nhiêu. Việc chọn đặt ở cuối vì chỉ khi đã biết AI nên giữ vai trò gì và kết quả được kiểm bằng cách nào, người học mới có tiêu chí để chọn. Chương không xếp hạng sản phẩm; nguyên tắc vẫn là: AI hỗ trợ, người học quyết định.

Mọi giá, tỷ giá và ngân sách trong chương là *dữ liệu giả định*; thông tin về dịch vụ, ưu đãi và điều khoản ở trạng thái *chưa kiểm chứng* theo mốc 29/10/2026 và cần tra lại khi áp dụng.

**Sau chương này, người học có thể:**

- Phân biệt ba hình thức sử dụng (miễn phí, thuê bao, API trả theo lượng dùng) và tách chi phí input khỏi output khi dự toán.
- Giải thích vì sao cảnh báo ngân sách (budget alert) không phải trần chặn chi tiêu.
- Áp dụng nguyên tắc ưu tiên miễn phí và đọc một chương trình ưu đãi sinh viên qua các câu hỏi về điều kiện, bằng chứng và thời hạn.
- Chọn công cụ theo tác vụ bằng năm lăng kính và viết một quyết định có điều kiện trong 20 phút.

## Tình huống mở đầu

Minh cần hiểu vì sao chương trình cộng ba khoản 35000, 7000 và 18000 của ViSinhVien cho kết quả 42000 thay vì 60000. Lan cần kiểm tra phiên bản Web chạy cục bộ và tìm hiểu một chương trình ưu đãi sinh viên. Cả hai thấy nút nâng cấp gói trên giao diện, nghe nói "dùng API rẻ hơn", và nhận ra chưa trả lời được ba câu hỏi: nên chọn công cụ nào, có cần trả tiền không, và nếu có thì trả bao nhiêu.

Câu hỏi của chương là: dựa trên những điều đã học, Minh và Lan nên chọn gì, vì sao, và kiểm tra lựa chọn đó bằng cách nào.

## 5.1. Chi phí sử dụng AI: hiểu cách tính trước khi gửi yêu cầu (AI Wallet)

Mục này giúp người học biết khoản sẽ phải trả, mức trả và vì sao, trước khi bấm gửi yêu cầu đầu tiên. Bản đọc trên web có mô phỏng chi phí ngay dưới tiêu đề mục; hãy thử đổi số request hoặc đơn giá để xem tổng tiền thay đổi, rồi đọc tiếp để hiểu từng bước tính.

### Ý chính 1 — Ba hình thức sử dụng và những token không nằm trong câu vừa gõ

Trước khi so sánh tiền, cần xác định đang so sánh cái gì. Có ba hình thức sử dụng.

| Hình thức | Cách hiểu ở mức nhập môn | Câu hỏi cần trả lời trước |
| --- | --- | --- |
| Free (miễn phí) | Một phạm vi sử dụng không thu tiền, kèm điều kiện | Model, tính năng, quota và chính sách dữ liệu là gì? |
| Subscription (thuê bao) | Trả phí định kỳ cho quyền lợi của một gói | Gói gồm gì, giới hạn gì, gia hạn khi nào? |
| API pay-as-you-go (trả theo lượng dùng) | Chương trình gọi dịch vụ, phí tính theo bảng giá | Đơn vị tính input và output, phí công cụ, giới hạn chi phí là gì? |

**Quota** (hạn mức) là giới hạn sử dụng có đơn vị và chu kỳ xác định; miễn phí không có nghĩa là vô hạn. Quyền dùng ứng dụng chat và quyền dùng API phải được kiểm tra riêng.

Lan cho rằng input chỉ gồm câu "sửa hàm tổng". Trên thực tế, ứng dụng có thể gửi kèm brief, lịch sử trao đổi, tệp đính kèm và kết quả công cụ (tool output). Một số model còn tính phí **reasoning token**, tức token phát sinh khi suy luận nội bộ. Ở chế độ **agent**, một yêu cầu "sửa cho xong" có thể sinh ra nhiều request. Số token thật chỉ biết được qua báo cáo usage của dịch vụ, không qua việc đếm từ.

### Ý chính 2 — Tách input khỏi output: 50 request và 1000 request

Lan dự toán cho 50 request với các con số cố định dưới đây (*dữ liệu giả định*, không mô tả hóa đơn của nhà cung cấp nào). Một **request** là một yêu cầu gửi đến dịch vụ.

| Đại lượng | Giá trị giả định |
| --- | ---: |
| Input mỗi request | 20000 token |
| Output mỗi request | 5000 token |
| Giá input | 0.30 USD / 1000000 token |
| Giá output | 2.50 USD / 1000000 token |
| Tỷ giá | 25000 VND / USD |

Phép tính đi qua sáu dòng: tổng input (1000000 token), tổng output (250000 token), tiền input (0.30 USD), tiền output (0.625 USD), tổng **0.925 USD**, quy đổi **23125 VND, chưa tính phí**. Cần chia cho một triệu vì đơn giá niêm yết theo triệu token. Kiểm tra chéo theo từng request: một request tốn 0.006 + 0.0125 = 0.0185 USD; nhân với 50 cũng ra 0.925 USD. Hai hướng tính khớp nhau giúp phát hiện lỗi nhầm triệu với nghìn.

Output ít token hơn nhưng tốn nhiều tiền hơn vì đơn giá output cao hơn; không được gộp 1250000 token rồi nhân với một giá chung. Giữ nguyên giả định và tăng lên 1000 request, tức gấp 20 lần, tổng tiền thành 18.50 USD = **462500 VND**, chưa tính phí: con số nhỏ ở 50 request đổi ý nghĩa khi nhân lên.

**Budget alert** (cảnh báo ngân sách) chỉ là thông báo khi mức chi chạm ngưỡng, không phải **hard cap** (trần cứng) chặn việc sử dụng. Email cảnh báo ở mức 80% không chứng minh việc dùng sẽ dừng ở 100%; ngay cả khi có trần, độ trễ và các request đang xử lý vẫn có thể đẩy mức chi vượt ngưỡng. Chưa hiểu cơ chế này thì chưa bật thanh toán.

### Thử ngay (10 phút)

Mục tiêu: tự lập một dự toán và kiểm tra chéo. Lấy giấy, viết sáu dòng tính cho 50 request theo bảng giả định trên, ghi đơn vị ở từng dòng. Tính lại theo từng request rồi nhân với 50. Cuối cùng, đổi một giả định (ví dụ output mỗi request thành 10000 token) và tính lại tổng USD. Ghi lại: hai hướng tính có khớp không, và khoản nào thay đổi nhiều nhất.

### Gợi ý đối chiếu

Đúng hướng khi: mỗi dòng có đơn vị (token, USD, VND); có phép chia cho 1000000; tiền output lớn hơn tiền input dù số token nhỏ hơn; hai hướng tính cho cùng tổng; kết quả có ghi chú "chưa tính phí"; không làm tròn ở bước trung gian.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu ứng dụng gửi kèm toàn bộ lịch sử trao đổi vào mỗi lượt, input của lượt thứ mười lớn gấp bao nhiêu lần lượt thứ nhất?
- **Từ khóa tra cứu:** token pricing, budget alert, hard cap, usage report.
- **Trong Sổ tay thực hành:** [Chi phí sử dụng AI (AI Wallet)](../chapters/chapter-05.md#muc-5-1) — bảng tính đầy đủ cho 50 và 1000 request, thuê bao giả định 20 USD, credit dùng chung và cơ chế kiểm soát chi tiêu.

## 5.2. Ưu tiên phương án miễn phí: chỉ mua khi biết rõ còn thiếu gì (Free First)

Mục này giúp người học quyết định có nên trả tiền hay không, dựa trên nhu cầu thật chứ không dựa trên cảm giác "phải có gói mới học tốt". Phương án 0 VND luôn phải có mặt trong bảng lựa chọn.

### Ý chính 1 — Quyền không mua là một phần của kế hoạch

Để hiểu lỗi 42000, Minh chỉ cần giấy bút, kiến thức về vòng lặp và một trình biên dịch sẵn có; chưa cần agent sửa kho mã. Lan có thể học phiên bản Web chạy cục bộ mà không cần tích hợp AI. Nguyên tắc **ưu tiên miễn phí** (*free first*) là chọn trước phương án không thu phí nhưng đủ dùng, đồng thời vẫn đọc điều kiện dịch vụ.

Khi hết quota, người học chia nhỏ câu hỏi, chờ chu kỳ tiếp theo hoặc hỏi giảng viên và nhóm học. Không lách giới hạn bằng cách tạo nhiều tài khoản, dùng key nhặt được hay thử thanh toán vì tò mò. Khả năng trả tiền không phải thước đo năng lực; ngân sách dành cho AI bằng 0 vẫn hoàn toàn hợp lệ.

Trước khi nâng cấp, cần hoàn thành được một câu ba vế: còn thiếu gì, gói này giải quyết bằng gì, lợi ích đo bằng gì. Chưa điền được thì chưa có lý do để mua.

### Ý chính 2 — Kế hoạch 300000 VND cho 15 tuần và điều kiện phải xét trước giá

Lan lập một kế hoạch với *dữ liệu giả định*: **300000 VND cho một học kỳ 15 tuần**. Đây không phải mức chi khuyến nghị; mục đích là cho thấy một quyết định chi tiêu hằng tháng có thể vượt kế hoạch của cả học kỳ.

| Giai đoạn | Dự trù | Điều kiện để quyết định |
| --- | ---: | --- |
| Tuần 1–5: học nền tảng | 0 VND | Tài liệu và công cụ miễn phí hợp lệ đủ dùng |
| Tuần 6–10: phát sinh nhu cầu rõ ràng | Tối đa 100000 VND | Có lợi ích đo được và đủ điều kiện sử dụng |
| Tuần 11–15: hoàn thiện bài | Tối đa 100000 VND | Đánh giá lại, không gia hạn theo quán tính |
| Dự phòng | 100000 VND | Không phải mục tiêu phải tiêu hết |
| Tổng trần cá nhân | 300000 VND | Kế hoạch trên giấy, không tự chặn hóa đơn |

Thuê bao giả định 20 USD, tức 500000 VND mỗi tháng, đã vượt cả kế hoạch học kỳ. Nếu 1000 request dồn vào một học kỳ, khoản 462500 VND cũng vượt trần. Ngày gia hạn và cách dừng tự động gia hạn phải được tìm hiểu trước khi mua.

Ưu đãi sinh viên cũng cần đọc như một hợp đồng. Hướng dẫn GitHub Education nêu các điều kiện như đang theo học tại cơ sở đủ điều kiện, có tài khoản cá nhân, chứng minh được tình trạng sinh viên và từ 13 tuổi trở lên; điều khoản Gemini API lại yêu cầu người dùng từ 18 tuổi, và với dịch vụ không trả phí, nội dung có thể được dùng để cải thiện sản phẩm (*chưa kiểm chứng*, ghi nhận theo mốc 29/10/2026). Điều kiện tuổi không chuyển từ chương trình này sang chương trình khác; email trường hỗ trợ chứng minh tình trạng sinh viên nhưng không bảo đảm được duyệt. Lan tách một chương trình ưu đãi thành năm câu hỏi: ai đủ điều kiện, cần bằng chứng gì, quyền lợi là gì, kéo dài bao lâu, điều gì xảy ra khi hết ưu đãi. Tuổi, dữ liệu và tài khoản phải được xét trước giá; không mua tài khoản lậu hay dùng chung key.

### Thử ngay (10 phút)

Mục tiêu: ra quyết định cuối tuần thứ năm. Đến lúc đó, Lan chưa thấy chức năng nào cần trả tiền. Hãy điền phiếu dưới đây cho Lan, rồi quyết định giữ khoản dự trù 100000 VND hay mua một gói "để tạo động lực". Ghi lại ba tiêu chí để đánh giá lại ở tuần thứ mười.

```text
Còn thiếu: ______________________________
Gói này giải quyết điều đó bằng: ______________________________
Lợi ích sẽ đo qua: ______________________________
Ngày đánh giá lại: ______________________________
```

### Gợi ý đối chiếu

Đúng hướng khi: vế "còn thiếu" nêu một hạn chế có thật (context, phạm vi, khả năng tự kiểm), không phải cảm giác; tiêu chí đánh giá lại đo được (số lỗi hiểu được, số thao tác tiết kiệm), không đo bằng số câu AI sinh ra; khoản chưa tiêu không bị coi là phần học bị thiếu.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Một gói trả phí ghi "không dùng dữ liệu để huấn luyện". Điều đó có đồng nghĩa với "không lưu" không?
- **Từ khóa tra cứu:** free tier, quota, student developer pack, terms of service, auto-renewal.
- **Trong Sổ tay thực hành:** [Ưu tiên phương án miễn phí (Free First)](../chapters/chapter-05.md#muc-5-2) — bài quyết định cuối tuần thứ năm kèm gợi ý, phần đọc ưu đãi sinh viên và điều khoản về tuổi, dữ liệu, tài khoản.

## 5.3. Đối chiếu công cụ theo tác vụ, không theo danh tiếng (AI Tool Battle)

Mục này giúp người học so sánh công cụ một cách công bằng: chọn theo việc cần làm và bằng chứng có thể kiểm tra, thay vì theo lời đồn về công cụ "mạnh nhất".

### Ý chính 1 — Năm lăng kính và ma trận tác vụ

Minh thích công cụ cho gợi ý ngắn để tự suy nghĩ; Lan ưa công cụ chỉ đúng tệp liên quan. Hai lựa chọn không mâu thuẫn, vì mỗi người ưu tiên một tác vụ khác nhau. Một công cụ dịch tốt không vì thế mà kiểm tra mã tốt.

Năm lăng kính để chọn công cụ là **provenance** (nguồn gốc của thông tin), **test** (cách kiểm tra), **context** (thông tin công cụ cần nhận), **privacy** (điều kiện xử lý dữ liệu) và **cost** (tổng chi phí). Ma trận dưới đây không xếp hạng sản phẩm thật; nó chỉ ra loại bằng chứng mỗi tác vụ cần.

| Tác vụ | Context cần có | Provenance và test | Privacy và cost |
| --- | --- | --- | --- |
| Suy luận logic (lỗi 42000 của Minh) | Mã nguồn, chỉ số, mục tiêu cộng mọi khoản | Bám cận vòng lặp; tự xét ca rỗng, một khoản, ba khoản | Dữ liệu giả; gợi ý ngắn trên phương án miễn phí |
| Viết mã hoặc refactor (Web của Lan) | Brief, hàm liên quan, cấu trúc Expense | Đọc kỹ thay đổi; thử giá trị biên và dữ liệu sai | Không dùng key; xét số bước và chi phí lặp |
| Đọc tài liệu dài | Đoạn được phép chia sẻ | Trích đúng đoạn, tìm mâu thuẫn | Không gửi tài liệu hạn chế; trích đoạn trước khi mua context lớn |
| Dịch và diễn giải | Thông báo lỗi, trình độ người học | Giữ nguyên tên API, số liệu và phủ định | Bỏ thông tin riêng tư; không cần agent |
| Tìm thông tin mới | Câu hỏi đúng sản phẩm, đúng phạm vi | Nguồn chính thức, ngày truy cập | Không gửi giấy tờ; xét phí tìm kiếm |

Công cụ không truy cập web thì không dùng làm nguồn duy nhất cho chính sách hiện hành. Công cụ không chạy được mã vẫn có thể gợi ý, nhưng phải kiểm thử ở nơi khác.

### Ý chính 2 — Benchmark công bằng: cùng đề, cùng dữ liệu, cùng giới hạn

**Benchmark** là phép thử có kiểm soát để so sánh mức độ phù hợp. Sổ tay có ba đề: Đề A giải thích logic C++ cho Minh bằng gợi ý từng bước; Đề B bổ sung xác thực cho hàm tính tổng Web mà không đổi phạm vi sản phẩm; Đề C đọc và kiểm tra một đoạn dữ kiện về ưu đãi sinh viên có mốc thời gian cũ. Mỗi đề chấm theo năm tiêu chí ứng với năm lăng kính, mỗi tiêu chí từ 0 đến 2 điểm.

Phép thử chỉ công bằng khi giữ nguyên brief, mã nguồn, dữ liệu, yêu cầu đầu ra và giới hạn trợ giúp giữa các công cụ; mở phiên mới để giảm ảnh hưởng của lịch sử; ghi tên ứng dụng, nhãn model (hoặc "chưa xác định"), chế độ và ngày thử. Trình tự: gửi đề → giữ nguyên câu trả lời → tự kiểm tra → chấm điểm → ghi giới hạn của kết luận. Một câu trả lời đề nghị đưa key vào mã Web bị loại dù các điểm khác cao. Vài đề thử không chứng minh được công cụ nào "tốt nhất cho mọi người".

### Thử ngay (10 phút)

Mục tiêu: lập phiếu so sánh trên giấy, không cần công cụ thật. Chọn một tác vụ trong ma trận (ví dụ lỗi 42000 của Minh). Hình dung hai công cụ giả định: một "chỉ chat, không chạy mã", một "agent đọc được tệp". Với mỗi công cụ, viết một dòng cho từng lăng kính: cần context gì, kiểm tra bằng gì, nguồn ở đâu, dữ liệu nào không gửi, tốn gì. Ghi lại: công cụ nào phù hợp với tác vụ này, và tác vụ nào thì không nên dùng nó.

### Gợi ý đối chiếu

Đúng hướng khi: phiếu có đủ năm lăng kính cho mỗi công cụ; kết luận gắn với một tác vụ cụ thể, không phải "mạnh hơn nói chung"; có ít nhất một tác vụ ghi "không chọn"; phần chưa thử thật được ghi là "luyện đánh giá trên giấy", không ghi điểm như đã đo.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Nếu hai công cụ cho cùng kết quả đúng ở Đề A nhưng một công cụ viết ngay toàn bộ bài, điểm "dễ học và dễ kiểm tra" nên khác nhau thế nào?
- **Từ khóa tra cứu:** benchmark, rubric, provenance, reproducibility, tool evaluation.
- **Trong Sổ tay thực hành:** [Đối chiếu công cụ theo tác vụ (AI Tool Battle)](../chapters/chapter-05.md#muc-5-3) — ba đề A, B, C đầy đủ, chuẩn đối chiếu, rubric 10 điểm và phiếu ghi nhận benchmark.

## 5.4. Ra quyết định trong 20 phút (Mini Challenge)

Mục này ghép các kỹ năng của cả sách thành một phiếu hoàn chỉnh trong 20 phút: nhận diện công cụ, viết prompt đủ context, tính chi phí và ra quyết định có điều kiện. Chỉ cần giấy, không cần thẻ thanh toán hay tài khoản AI.

### Ý chính — Năm bước, mỗi bước một mục đích

Tình huống giả định: Minh cần hiểu lỗi 42000; Lan kiểm tra phiên bản Web cục bộ và tìm hiểu ưu đãi. Một ứng dụng giả định tên "Trợ lý học ViSinhVien" chỉ công bố chế độ "Tự động", không nêu model hay provider. Chi phí dùng số liệu giả định ở mục 5.1.

1. **Phút 0–4, nhận diện:** điền application, model, provider; thêm producer nếu có căn cứ. Khoanh tròn điểm chưa rõ, ghi "chưa xác định" thay vì đoán model qua giao diện (xem lại [mục 1.2](../chapters/chapter-01.md#muc-1-2)).
2. **Phút 4–8, viết prompt:** đưa vào mục tiêu, đoạn mã, hợp đồng dữ liệu, ba khoản chi và cặp số 60000 với 42000; yêu cầu gợi ý trước khi sửa. Đọc lại dưới góc nhìn của người chưa biết dự án để tìm context còn thiếu.
3. **Phút 8–13, ước tính chi phí:** tách input và output cho 50 request, quy đổi sang VND, rồi xét 1000 request; kiểm tra chéo theo từng request.
4. **Phút 13–17, ra quyết định:** dùng ít nhất ba tiêu chí trong ma trận, nêu phương án không trả tiền, cách kiểm chứng và điều kiện đánh giá lại.
5. **Phút 17–20, đối chiếu:** sửa phiếu nhưng giữ dấu vết lỗi ban đầu; trình bày trong 30 giây: đã biết gì, chưa biết gì, chọn gì, kiểm tra thế nào, chi tối đa bao nhiêu.

Một quyết định tốt trong bài này thường có mức chi bằng 0: Minh tự sửa cận vòng lặp với gợi ý từ một công cụ miễn phí hợp lệ; Lan giữ phiên bản Web cục bộ và ghi "chưa xác minh" cho thông tin ưu đãi. Sở thích cá nhân không thay thế được bằng chứng; cảnh báo ngân sách không thay thế được kế hoạch. Dù chọn công cụ nào, nguyên tắc của cả sách vẫn giữ nguyên: AI hỗ trợ, người học quyết định.

### Thử ngay (10 phút)

Mục tiêu: hoàn thành phần quyết định có điều kiện, tức bước 4 ở trên, với kết quả tính ở mục 5.1 và kế hoạch ở mục 5.2. Điền sáu dòng, mỗi dòng một câu đầy đủ, rồi gạch chân chỗ chưa có bằng chứng.

```text
1. Với Minh, tôi chọn __________ vì __________.
2. Với Lan, tôi chọn __________ vì __________.
3. Ba tiêu chí tôi dựa vào là __________, __________, __________.
4. Phương án không trả tiền của tôi là __________.
5. Mức chi tôi chấp nhận lúc này là __________; tôi sẽ cân nhắc lại khi __________.
6. Nếu điều kiện tuổi chưa rõ hoặc có nguy cơ vượt ngân sách, tôi sẽ __________.
```

### Gợi ý đối chiếu

Đúng hướng khi: dòng 1 và 2 nêu tác vụ cụ thể, không nêu tên sản phẩm vì danh tiếng; ba tiêu chí lấy từ năm lăng kính; dòng 4 là phương án có thật, làm được ngay; dòng 5 có con số và mốc thời gian; dòng 6 là hành động dừng, không phải cách lách.

### Tự tìm hiểu thêm

- **Câu hỏi mở:** Sau một tuần dùng phương án đã chọn, bằng chứng nào cho thấy lựa chọn đó đúng, và bằng chứng nào buộc phải đổi?
- **Từ khóa tra cứu:** decision criteria, conditional decision, cost estimate, model identification.
- **Trong Sổ tay thực hành:** [Bài tập tổng hợp 20 phút (Mini Challenge)](../chapters/chapter-05.md#muc-5-4) — phiếu đầy đủ bốn phần, prompt mẫu cho Minh, bảng phép tính bắt buộc và một phiếu hoàn chỉnh để đối chiếu sau khi tự làm.

## Tóm tắt chương

- Chọn công cụ theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng; thiếu chứng cứ thì ghi "chưa xác định".
- Chi phí phụ thuộc vào lượng dùng và đơn giá của từng loại token: 50 request giả định tốn 0.925 USD, 1000 request tốn 462500 VND, chưa tính phí.
- Budget alert là cảnh báo, không phải trần chặn; chưa hiểu cơ chế thì chưa bật thanh toán.
- Phương án 0 VND luôn có mặt; chỉ mua khi điền được "còn thiếu gì, giải quyết bằng gì, đo bằng gì".
- Benchmark chỉ công bằng khi cùng đề, cùng dữ liệu, cùng giới hạn; chấm bằng bằng chứng, không bằng cảm giác.

**Ba câu để tự kiểm:**

1. Đếm số từ tiếng Việt có đủ để tính hóa đơn theo token không? Vì sao?
2. Email trường có bảo đảm nhận được ưu đãi sinh viên và quyền dùng mọi API không?
3. Một công cụ được nhiều người khen là "mạnh nhất". Điều đó có đủ để chọn nó cho bài vòng lặp C++ của Minh không?

Xuyên suốt năm bước Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn là một nguyên tắc: AI hỗ trợ, người học quyết định.

## Cầu nối sang chương sau

Năm bước đã đủ để từng việc riêng lẻ được làm cẩn thận. [Dự án tổng kết](final-project.md) ghép các bước đó thành một sản phẩm hoàn chỉnh: người học xây dựng, kiểm thử và giải thích, đồng thời lưu bằng chứng cho từng quyết định về công cụ, cách dùng và ranh giới.

## Tài liệu tham khảo

Các nguồn ghi nhận theo mốc truy cập 29/10/2026; nội dung hiện hành cần tra lại trước khi áp dụng. Mọi mức giá, tỷ giá và ngân sách trong chương là dữ liệu giả định.

- [Google — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing): đơn vị giá input, output và phụ phí của một API thật, để đối chiếu cách đọc bảng giá.
- [Google — Gemini API billing](https://ai.google.dev/gemini-api/docs/billing) và [Google Cloud — Budgets](https://cloud.google.com/billing/docs/how-to/budgets): cơ chế cảnh báo ngân sách và kiểm soát mức dùng.
- [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms): điều kiện tuổi, cấp dịch vụ và cách xử lý dữ liệu.
- [GitHub — Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student): điều kiện và bằng chứng tình trạng sinh viên.
- [GitHub Student Developer Pack](https://education.github.com/pack): quyền lợi, thời hạn và giới hạn của ưu đãi.
- [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview): họ model và định danh, dùng khi nhận diện model (mục 5.4).
