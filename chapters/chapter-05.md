# CHƯƠNG 5 · LỰA CHỌN AI VÀ MODEL PHÙ HỢP VỚI NHIỆM VỤ

Bốn chương trước đã đi qua bốn bước. Chương 1 giúp hiểu AI đóng vai trò gì trong học tập, giúp được gì và không giúp được gì. Chương 2 hướng dẫn cách điều khiển quá trình làm việc để mọi thay đổi đều có kiểm soát. Chương 3 chỉ ra cách dùng AI mà vẫn tự học được, không lạm dụng. Chương 4 vạch ranh giới về dữ liệu, bảo mật, bản quyền và liêm chính. Đến đây, người học đã có nền để đặt câu hỏi cuối cùng của sách: với nhiệm vụ này, nên chọn AI, model và gói dịch vụ nào?

Việc chọn công cụ được đặt ở cuối vì lý do thực tế. Nếu chọn ngay từ đầu, người học dễ chọn theo danh tiếng hoặc theo giá, khi chưa biết nhu cầu thật của bản thân. Sau bốn bước trước, người học đã biết vai trò mà AI nên giữ, cách kiểm tra kết quả, phần việc phải tự làm và những dữ liệu không được gửi đi. Những hiểu biết đó trở thành tiêu chí để chọn: tác vụ cụ thể, rủi ro, ngân sách và điều kiện sử dụng. Chương này vì vậy không xếp hạng sản phẩm; chương chỉ trình bày cách tính chi phí, cách ưu tiên phương án miễn phí, cách đối chiếu công cụ theo tác vụ và cách ra quyết định có điều kiện. Dù chọn công cụ nào, nguyên tắc vẫn giữ nguyên: AI hỗ trợ, người học quyết định.

Các thông tin về dịch vụ, giá và chính sách trong chương là dữ liệu giả định hoặc chưa kiểm chứng (mốc 29/10/2026), cần tra lại khi áp dụng; các nhân vật là tình huống minh họa, không phải quy định của Trường.

## Mục tiêu học tập

Sau chương này, người học có thể:

- Phân biệt ba hình thức sử dụng (miễn phí, thuê bao, API trả theo lượng dùng) và đọc đúng quyền lợi của từng hình thức.
- Tách chi phí input khỏi output, tính và kiểm tra chéo một dự toán, kèm đơn vị và ghi chú "chưa tính phí".
- Giải thích vì sao budget alert không phải hard cap, và biết cần xác minh điều gì trước khi bật thanh toán.
- Áp dụng nguyên tắc ưu tiên miễn phí và đọc một chương trình ưu đãi sinh viên qua các câu hỏi về điều kiện, bằng chứng, thời hạn.
- Chọn công cụ theo tác vụ bằng năm lăng kính (provenance, test, context, privacy, cost) và chấm đầu ra bằng rubric.
- Hoàn thành một phiếu tích hợp gồm nhận diện, prompt, phép tính và quyết định có điều kiện.

## Tình huống mở đầu

Sau khi đi qua Chương 1–4, Minh và Lan đứng trước một việc cụ thể: Minh cần hiểu vì sao chương trình cộng ba khoản 35000, 7000, 18000 của ViSinhVien cho kết quả 42000 thay vì 60000; Lan cần kiểm tra phiên bản Web và tìm hiểu thông tin ưu đãi sinh viên. Cả hai thấy nút nâng cấp gói, nghe nói API rẻ hơn, và nhận ra rằng họ chưa biết nên chọn công cụ nào, trả tiền hay không, trả bao nhiêu.

Tình huống này dùng dữ liệu giả định. Mọi thông tin về dịch vụ, giá và ưu đãi nhắc tới trong chương đều ở trạng thái *chưa kiểm chứng* theo mốc 29/10/2026, và cần tra lại tại thời điểm áp dụng. Câu hỏi của chương là: dựa trên điều đã học, Minh và Lan nên chọn gì, vì sao, và kiểm tra lựa chọn đó bằng cách nào.

## 5.1. Chi phí sử dụng AI: hiểu cách tính trước khi gửi yêu cầu (AI Wallet)

Mục này giúp người học biết khoản sẽ phải trả, mức trả và vì sao, trước khi bấm gửi yêu cầu đầu tiên.

### Ba hình thức sử dụng, ba cách đọc quyền lợi

Trong tình huống minh họa, Minh thấy nút nâng cấp trên giao diện, còn Lan nghe nói "dùng API rẻ hơn". Trước khi so sánh tiền, cần xác định rõ đối tượng đang được so sánh. Một sản phẩm miễn phí đủ để giúp hiểu vòng lặp có thể là lựa chọn tốt hơn cả hai phương án trả tiền.

| Hình thức | Cách hiểu ở mức nhập môn | Câu hỏi cần trả lời trước khi dùng |
| --- | --- | --- |
| Free (miễn phí) | Một phạm vi sử dụng không thu tiền, kèm điều kiện | Model, tính năng, quota, chính sách dữ liệu và điều kiện tài khoản là gì? |
| Subscription (thuê bao) | Trả phí định kỳ cho quyền lợi của một gói hoặc sản phẩm | Gói bao gồm gì, giới hạn gì, gia hạn khi nào, khoản nào nằm ngoài gói? |
| API pay-as-you-go (trả theo lượng dùng) | Chương trình gọi dịch vụ, phí tính theo lượng dùng và bảng giá | Đơn vị tính input và output, phí công cụ, cách xác thực và giới hạn chi phí là gì? |

**Quota** (hạn mức) là giới hạn sử dụng có đơn vị và chu kỳ xác định: số lượt, tốc độ hoặc lượng dùng; các loại hạn mức này không thể quy đổi lẫn nhau. Miễn phí không có nghĩa là vô hạn; trả tiền cũng không bảo đảm mọi yêu cầu đều được phục vụ không giới hạn.

Quyền sử dụng ứng dụng và quyền sử dụng API phải được kiểm tra riêng. Không thể lấy biên lai thuê bao ứng dụng chat làm bằng chứng đã trả phí cho mọi loại API. Ngược lại, cũng không thể khẳng định "thuê bao không bao giờ kèm API": tài liệu của OpenAI về credit dùng chung giữa ChatGPT và API là một ví dụ ngoại lệ, cần đọc theo từng gói đủ điều kiện. **Credit** là giá trị hoặc lượng dùng được cấp, có thể kèm thời hạn và phạm vi áp dụng. *Chưa kiểm chứng:* thông tin về gói tích hợp này được ghi nhận theo mốc 29/10/2026, chưa được xác minh độc lập và cần tra lại; đây không phải cam kết về quyền lợi hiện hành.

### Bài toán giả định: tách chi phí input khỏi output

Lan muốn dự toán chi phí cho 50 request. **Request** là một yêu cầu gửi đến dịch vụ; một lần bấm nút của người dùng có thể dẫn đến nhiều request phía sau. Trong bài này, kích thước và đơn giá được cố định để luyện phép tính, không mô tả hóa đơn của bất kỳ nhà cung cấp nào.

*Dữ liệu giả định:* toàn bộ giá, tỷ giá và lượng dùng dưới đây là giả định. Không dùng các số liệu này để mua dịch vụ hoặc dự đoán giá thật. Mô hình chưa tính phí riêng của công cụ, cache, lưu trữ hay các cơ chế xử lý đặc thù.

| Đại lượng | Giá trị giả định |
| --- | ---: |
| Input mỗi request | 20000 token |
| Output mỗi request | 5000 token |
| Số request ban đầu | 50 |
| Giá input | 0.30 USD / 1000000 token |
| Giá output | 2.50 USD / 1000000 token |
| Tỷ giá | 25000 VND / USD |

Trước khi xem đáp án, hãy viết sáu dòng tính: tổng input, tổng output, tiền input, tiền output, tổng tiền USD và tổng tiền VND. Ghi đơn vị ở từng dòng. Cần chia cho một triệu vì đơn giá được niêm yết theo triệu token, không phải theo từng token hay theo nghìn token.

```text
Tổng input  = input mỗi request × số request
Tổng output = output mỗi request × số request
Tiền input  = tổng input / 1000000 × giá input
Tiền output = tổng output / 1000000 × giá output
Tổng USD    = tiền input + tiền output
Tổng VND    = tổng USD × tỷ giá giả định
```

### Đáp án bài tính chi phí — 50 request và kiểm tra chéo

| Bước | Phép tính | Kết quả |
| --- | --- | ---: |
| Gom input | 20000 × 50 | 1000000 token |
| Gom output | 5000 × 50 | 250000 token |
| Tính tiền input | 1000000 / 1000000 × 0.30 | 0.30 USD |
| Tính tiền output | 250000 / 1000000 × 2.50 | 0.625 USD |
| Cộng hai khoản | 0.30 + 0.625 | 0.925 USD |
| Quy đổi sau cùng | 0.925 × 25000 | 23125 VND |

Kết quả là **0.925 USD = 23125 VND, chưa tính phí**. Không làm tròn 0.925 thành 0.93 ở bước trung gian rồi gọi con số VND tính sau đó là kết quả chính xác. Thuế, chênh lệch tỷ giá khi thanh toán, phí ngân hàng và các dịch vụ tính phí riêng (nếu có) chưa nằm trong mô hình này.

Kiểm tra lại theo từng request: tiền input là `20000 / 1000000 × 0.30 = 0.006 USD`; tiền output là `5000 / 1000000 × 2.50 = 0.0125 USD`. Một request tốn `0.0185 USD`; nhân với 50 cũng được `0.925 USD`. Hai hướng tính cho cùng kết quả giúp phát hiện lỗi nhầm triệu với nghìn.

Trong bài này, output ít token hơn nhưng lại tốn nhiều tiền hơn vì đơn giá output cao hơn. Không được gộp 1250000 token rồi nhân với một mức giá chung. Chi phí phụ thuộc vào cả lượng dùng và đơn giá của từng loại token, không chỉ vào tổng số token.

### Từ 50 lên 1000 request: con số nhỏ có thể đổi ý nghĩa

Giữ nguyên mọi giả định và tăng số request từ 50 lên 1000, tức tăng **20 lần**, không phải 1000 lần. Tổng input trở thành 20000000 token; tổng output là 5000000 token. Tiền input là 6.00 USD, tiền output là 12.50 USD.

```text
1000 request × 0.0185 USD = 18.50 USD
0.925 USD × 20           = 18.50 USD
18.50 USD × 25000        = 462500 VND, chưa phí
```

Như vậy, với 20000 token input và 5000 token output cho mỗi request, **50 request tốn 0.925 USD = 23125 VND**, còn **1000 request tốn 18.50 USD = 462500 VND**. Phép tính tuyến tính đúng trong trường hợp này vì đơn giá và cơ cấu request được giữ cố định. Dịch vụ thật có thể thay đổi bậc giá, model, chế độ hoặc phí công cụ; khi đó phải lập lại bảng tính.

Để so sánh, một **thuê bao giả định 20 USD/tháng** tương đương **500000 VND/tháng** theo cùng tỷ giá. Tuy vậy, chưa thể kết luận API cho quyền lợi tương đương mà rẻ hơn: quota, tính năng và điều kiện của hai hình thức có thể khác nhau. Nếu Minh vốn không cần mua thuê bao, khoản chi cho API cũng không tự trở thành "tiết kiệm". Phương án 0 VND luôn phải có mặt trong bảng lựa chọn.

### Những token không nằm trong câu vừa gõ

Lan cho rằng input chỉ gồm câu "sửa hàm tổng". Trên thực tế, ứng dụng có thể gửi thêm brief, lịch sử trao đổi, tệp đính kèm và **tool output** (kết quả công cụ, chẳng hạn log của test) vào lượt kế tiếp. Lịch sử đã gửi không mặc nhiên được miễn phí; cache và việc lưu phiên có cách tính riêng.

Một số model ghi nhận và tính phí **reasoning token**, tức token phát sinh trong quá trình suy luận nội bộ. Cách tính loại token này vào usage, vào output hay vào giới hạn phụ thuộc vào từng model và từng provider, và không nằm trong ví dụ trên. Một bản dự toán thật cần dùng công cụ đếm hoặc ước tính phù hợp, sau đó đối chiếu với báo cáo usage khi được phép sử dụng dịch vụ, không dựa vào việc đếm từ.

**Agent** là chế độ trong đó hệ thống có thể tự thực hiện chuỗi bước: đọc mã → sửa → chạy test → đọc lỗi → lặp lại. Một yêu cầu như "sửa cho xong" có thể sinh ra nhiều request. Vì vậy, Lan giới hạn phạm vi ở một hàm, một đề xuất, đầu ra đủ để kiểm tra và một điểm dừng để xem lại. Khi bắt đầu lượt mới, Lan dùng bản brief đã cập nhật, không lược bỏ ràng buộc chỉ để tiết kiệm token.

### Cảnh báo ngân sách không phải là trần chặn chi tiêu

**Budget alert** (cảnh báo ngân sách) là cơ chế thông báo khi mức chi đạt một ngưỡng. **Hard cap** (trần cứng) phải có cơ chế chặn việc sử dụng hoặc chi tiêu theo phạm vi mà dịch vụ định nghĩa. Một email cảnh báo ở mức 80% không chứng minh rằng việc sử dụng sẽ dừng ở mức 100%; con số ghi trong ô "budget" không tự trở thành cầu dao ngắt.

Tài liệu Gemini API billing và Google Cloud Budgets là các nguồn tham chiếu cho cơ chế này. *Chưa kiểm chứng:* nội dung được ghi nhận theo mốc 29/10/2026, chưa được xác minh độc lập và cần tra lại. Không nên mặc định mọi dịch vụ đều có cùng nút điều khiển hay cùng cơ chế. Ngay cả khi trần chi tiêu được hỗ trợ, độ trễ cập nhật, các request đang xử lý và các trường hợp ngoại lệ vẫn có thể khiến mức chi vượt ngưỡng.

Khi chưa hiểu rõ các cơ chế trên thì chưa bật thanh toán. Nếu sau này được phép sử dụng, người dùng cần biết nơi xem usage, quota và các giới hạn thực có, số bước agent được phép chạy, cách dừng dịch vụ và cách xử lý khóa. Câu prompt "đừng tiêu quá" không thay thế được cơ chế kiểm soát của tài khoản. Bài này chỉ tính trên giấy; không bật thanh toán để thử cảnh báo.

## 5.2. Ưu tiên phương án miễn phí: chỉ mua khi biết rõ còn thiếu gì (Free First)

Mục này giúp người học quyết định có nên trả tiền hay không, dựa trên nhu cầu thật chứ không dựa trên cảm giác "phải có gói mới học tốt".

### Quyền không mua là một phần của kế hoạch

Xét thẻ A, Minh nhận thấy chỉ cần giấy bút, kiến thức về vòng lặp và có thể thêm một trình biên dịch sẵn có; chưa cần đến agent sửa kho mã. Lan cũng có thể học phiên bản Web chạy cục bộ mà không cần tích hợp AI. Nguyên tắc **ưu tiên miễn phí** (*free first*) là chọn trước phương án không thu phí nhưng đủ dùng, đồng thời không bỏ qua điều kiện dịch vụ.

Khi hết quota, người học có thể chia nhỏ câu hỏi, chờ chu kỳ tiếp theo, đọc tài liệu hoặc hỏi giảng viên và nhóm học. Không lách giới hạn bằng cách tạo nhiều tài khoản, dùng key nhặt được hay thử thanh toán vì tò mò. Khi chưa có công cụ hợp lệ, có thể luyện tập với các thẻ trả lời hư cấu trong chương.

Trước khi nâng cấp, hãy hoàn thành câu: "Tôi thiếu ______; gói này giải quyết điều đó bằng ______; tôi đo lợi ích qua ______". Nếu chưa điền được, chưa có lý do rõ ràng để mua. Đôi khi chỉ cần trích vài trang tài liệu là đủ, thay vì mua một gói có context lớn.

> **Quyền không mua.** Khả năng trả tiền không phải thước đo năng lực CNTT. Nội dung này không phải chuẩn đầu ra, yêu cầu chi tiêu hay quy định của Trường. Ngân sách dành cho AI bằng 0 vẫn hoàn toàn hợp lệ.

### Kế hoạch 300000 VND cho 15 tuần: trần kế hoạch, không phải trần kỹ thuật

Lan thử lập một kế hoạch với *dữ liệu giả định*: **300000 VND cho một học kỳ 15 tuần**. Đây không phải mức chi khuyến nghị cho mọi sinh viên. Mục đích của bài là cho thấy một quyết định chi tiêu hằng tháng có thể vượt kế hoạch của cả học kỳ.

| Giai đoạn giả định | Dự trù | Điều kiện để quyết định |
| --- | ---: | --- |
| Tuần 1–5: học nền tảng | 0 VND | Tài liệu và công cụ miễn phí hợp lệ đủ dùng |
| Tuần 6–10: phát sinh một nhu cầu rõ ràng | Tối đa 100000 VND | Có lợi ích đo được và đủ điều kiện sử dụng |
| Tuần 11–15: hoàn thiện bài | Tối đa 100000 VND | Đánh giá lại nhu cầu, không gia hạn theo quán tính |
| Dự phòng | 100000 VND | Có thể giữ nguyên, không phải mục tiêu phải tiêu hết |
| Tổng trần cá nhân | 300000 VND | Kế hoạch trên giấy, không tự động chặn hóa đơn |

Thuê bao giả định 500000 VND/tháng đã vượt cả kế hoạch học kỳ. Nếu 1000 request dồn vào cùng một học kỳ, khoản 462500 VND (chưa tính phí) cũng vượt trần 300000 VND. Mức 23125 VND ban đầu không chứng minh rằng Lan cần dùng API, đủ tuổi sử dụng hay có khả năng quản lý khóa.

Trước khi chi tiền, cần ghi rõ nhiệm vụ, phương án miễn phí đã thử, mức trần chi tiêu và ngày đánh giá lại. Ngày gia hạn và cách dừng tự động gia hạn phải được tìm hiểu **trước khi mua**, không giả định rằng mọi dịch vụ đều có nút hủy giống nhau. Sau một tuần sử dụng, đánh giá hiệu quả bằng số lỗi đã hiểu được hoặc số thao tác tiết kiệm được, không bằng số câu AI sinh ra.

**Bài tập: quyết định cuối tuần thứ năm.** Đến cuối tuần thứ năm, Lan chưa thấy chức năng nào cần trả tiền. Lan nên giữ khoản dự trù 100000 VND hay mua một gói để "tạo động lực"? Hãy ghi các tiêu chí đánh giá lại.

### Đáp án kế hoạch — Khoản tiền chưa tiêu không phải phần học bị thiếu

Giữ nguyên khoản dự trù. Đánh giá lại sau khi làm Đề B (mục 5.3), dựa trên ba tiêu chí: context có đủ dùng không, phạm vi có được giữ không, và người học có tự kiểm tra được kết quả không. Chỉ mua khi gói dịch vụ giải quyết một hạn chế có thật, người học đủ điều kiện sử dụng và khoản chi nằm trong ngân sách. Không cần tiêu hết khoản dự phòng.

### Ưu đãi sinh viên: đủ điều kiện nộp hồ sơ không có nghĩa chắc chắn được duyệt

Hướng dẫn của GitHub Education nêu các điều kiện như đang theo học tại cơ sở thuộc diện đủ điều kiện, có tài khoản cá nhân, chứng minh được tình trạng sinh viên và **từ 13 tuổi trở lên**. Tài liệu này cũng ghi nhận quyền lợi GitHub Pro và Copilot Student cho người học đã được xác minh theo điều kiện. *Chưa kiểm chứng:* nội dung được ghi nhận theo mốc 29/10/2026, chưa được xác minh độc lập; tên gói, độ tuổi, quyền lợi và điều kiện phải được tra lại tại thời điểm áp dụng.

Không dựa vào một hướng dẫn cũ để tự đổi tên gói thành "Copilot Pro hiện tại", cũng không chốt mức quota theo trí nhớ. **Completion** là chức năng gợi ý hoàn thành mã; **chat** là hình thức trao đổi hỏi đáp; **agent** có thể tổ chức thực hiện nhiều bước. Quyền lợi ở một hình thức không bảo đảm mọi hình thức sử dụng khác đều không giới hạn. Một chương trình ưu đãi có thể gồm nhiều bên tham gia với điều khoản riêng, và không mặc nhiên cấp API key miễn phí cho mọi dịch vụ.

Để đọc một chương trình ưu đãi, Lan tách thành năm câu hỏi: ai đủ điều kiện; cần bằng chứng gì; quyền lợi cụ thể là gì; quyền lợi kéo dài bao lâu; và điều gì xảy ra khi hết ưu đãi hoặc đến kỳ gia hạn. Email do trường cấp có thể hỗ trợ việc chứng minh tình trạng sinh viên nhưng không phải tấm vé được duyệt tự động. Email TLU không tự bảo đảm hồ sơ sẽ thành công.

Bài tập chỉ yêu cầu đọc thông tin, không yêu cầu nộp hồ sơ hay tải giấy tờ lên. Nếu sau này đăng ký, người học cần dùng quy trình chính thức và chỉ cung cấp giấy tờ cần thiết tại đúng nơi tiếp nhận. Không gửi giấy tờ vào chatbot hoặc nhóm lớp để "nhờ duyệt hộ".

### Tuổi, dữ liệu và tài khoản phải được xét trước giá

Điều kiện tuổi của một chương trình không tự động áp dụng cho chương trình khác. Điều khoản của Gemini API yêu cầu người dùng **từ 18 tuổi trở lên** đối với Gemini API và Google AI Studio. *Chưa kiểm chứng:* thông tin này được ghi nhận theo mốc 29/10/2026, chưa được xác minh độc lập; cần đọc lại điều khoản chính thức trước khi sử dụng. Không thể suy từ mốc 13 tuổi của một chương trình giáo dục rằng người học đủ điều kiện dùng mọi API. Khi chưa đáp ứng hoặc chưa rõ điều kiện, cần chọn bài làm trên giấy, không tìm cách vượt qua giới hạn.

Cũng theo điều khoản Gemini API được ghi nhận ở cùng mốc thời gian, với dịch vụ không trả phí (*unpaid*) thuộc phạm vi áp dụng, nội dung có thể được dùng để cải thiện sản phẩm và có thể được con người xem xét. Với dịch vụ trả phí (*paid*), trong nhiều trường hợp nội dung không được dùng để cải thiện sản phẩm, nhưng vẫn có thể tồn tại các chương trình hoặc cấp dịch vụ (*tier*) có cơ chế đóng góp dữ liệu. *Chưa kiểm chứng:* các chi tiết này chưa được xác minh độc lập và không được trình bày như cam kết hiện hành. Bài học bền vững là phải xem xét đúng sản phẩm, đúng cấp dịch vụ, các lựa chọn về dữ liệu và các ngoại lệ.

Không lấy điều khoản của API để áp nguyên cho ứng dụng chat. Không rút gọn thành các nhận định như "trả phí là riêng tư tuyệt đối", "không dùng để huấn luyện nghĩa là không lưu" hay "mọi provider đều giống nhau". Với ViSinhVien, chỉ sử dụng ba khoản giả; không có lý do gì để đưa sao kê, số tài khoản hay lịch sử chi tiêu thật lên AI. Bản thân `localStorage` cũng không phải kho lưu bí mật hay bản sao lưu đáng tin cậy: dữ liệu có thể mất khi người dùng xóa dữ liệu trình duyệt, không tự đồng bộ giữa các thiết bị và không tạo ra cơ chế đăng nhập.

Nếu sử dụng dịch vụ, người học cần có tài khoản hợp lệ, mật khẩu riêng và bật xác thực nhiều yếu tố khi dịch vụ hỗ trợ. Không mua tài khoản lậu hoặc dùng chung thuê bao hay key theo cách bỏ qua điều khoản và quyền riêng tư. Người bán hoặc người dùng chung có thể đọc lịch sử trao đổi, thu hồi quyền truy cập hoặc làm phát sinh chi phí. Giá rẻ không bù đắp được việc mất quyền kiểm soát; điều kiện sử dụng phải được kiểm tra trước khi so sánh giá.

## 5.3. Đối chiếu công cụ theo tác vụ, không theo danh tiếng (AI Tool Battle)

Mục này giúp người học so sánh công cụ một cách công bằng: chọn theo việc cần làm và bằng chứng có thể kiểm tra, thay vì theo lời đồn về công cụ "mạnh nhất". Hai mục trước đã trả lời "trả bao nhiêu"; mục này trả lời "dùng công cụ nào cho việc nào".

### Ma trận tác vụ: câu hỏi "phù hợp với việc gì?" đứng trước câu hỏi "mạnh nhất?"

Minh thích thẻ A vì được tự suy nghĩ; Lan lại ưa công cụ có thể chỉ đúng tệp liên quan. Hai lựa chọn này không mâu thuẫn, vì mỗi người đang ưu tiên một tác vụ khác nhau. Một công cụ dịch tốt không vì thế mà kiểm tra mã tốt; một công cụ viết mã nhanh không vì thế mà nắm được chính sách mới.

Năm lăng kính để lựa chọn công cụ gồm: **provenance** (nguồn gốc và căn cứ của thông tin), **test** (cách kiểm tra), **context** (thông tin công cụ cần nhận), **privacy** (điều kiện xử lý dữ liệu) và **cost** (tổng chi phí). Bằng chứng phù hợp thay đổi theo tác vụ: với việc debug, đó có thể là dòng mã và test; với điều kiện tuổi sử dụng dịch vụ, đó phải là điều khoản đúng phạm vi.

| Tác vụ | Context cần có | Provenance và test | Privacy và cost |
| --- | --- | --- | --- |
| Suy luận logic | Mã nguồn, chỉ số, mục tiêu cộng mọi khoản của Minh | Bám vào cận vòng lặp; tự xét ca rỗng, một khoản, ba khoản | Dữ liệu giả; gợi ý ngắn trên phương án miễn phí phù hợp |
| Viết mã hoặc refactor | Brief, hàm liên quan, cấu trúc Expense của Lan | Đọc kỹ thay đổi; kiểm tra dữ liệu mẫu, giá trị biên và dữ liệu sai; không thêm backend | Không dùng key; xem xét quyền đọc tệp, số bước và chi phí lặp |
| Đọc tài liệu dài | Đặc tả và đoạn ghi chú được phép chia sẻ | Trích đúng đoạn, tìm mâu thuẫn, so với brief hiện hành | Không gửi tài liệu bị hạn chế; trích đoạn trước khi mua gói context lớn |
| Dịch và diễn giải | Thông báo lỗi hoặc đoạn tài liệu, trình độ người học | Giữ nguyên tên API, số liệu và phủ định; không đổi số nguyên thành số thực | Loại bỏ thông tin riêng tư; không cần agent nhiều bước |
| Tìm thông tin mới | Câu hỏi về ưu đãi hoặc giá, đúng sản phẩm và phạm vi | Nguồn chính thức hiện hành, đoạn hỗ trợ, ngày truy cập | Không gửi giấy tờ; xét phí tìm kiếm nếu có |

Ma trận này không xếp hạng sản phẩm thật. Công cụ không có khả năng truy cập web thì không dùng làm nguồn duy nhất cho chính sách hiện hành. Công cụ không chạy được mã vẫn có thể đưa gợi ý, nhưng cần kiểm thử ở nơi khác. Nên chọn công cụ cho phần việc mà người học kiểm chứng được, thay vì giao toàn bộ chỉ vì công cụ nhận làm.

### Benchmark A–C: chuẩn bị một phép thử đủ công bằng

**Benchmark** là phép thử có kiểm soát để so sánh mức độ phù hợp. Ba đề dưới đây **không kèm điểm sản phẩm điền sẵn**. Nếu không có công cụ được phép sử dụng, người học phân tích trên giấy và ghi rõ đây là bài luyện đánh giá, không phải benchmark thực.

Khi thử, cần giữ nguyên brief, mã nguồn, dữ liệu, yêu cầu đầu ra và giới hạn trợ giúp giữa các công cụ; nên mở một phiên trao đổi mới để giảm ảnh hưởng của lịch sử. Ghi lại tên ứng dụng, nhãn model (hoặc "chưa xác định"), chế độ, ngày thử và các tính năng đang bật. Khác biệt về khả năng truy cập web hay chạy mã phải được ghi riêng, không quy toàn bộ cho model.

Trình tự thực hiện gồm: **gửi đề → giữ nguyên câu trả lời → tự kiểm tra → chấm điểm → ghi câu hỏi bổ sung và giới hạn của kết luận**. Nếu có điều kiện, nên thử lại vì đầu ra có thể thay đổi giữa các lần. Một vài đề thử không chứng minh được công cụ nào "tốt nhất cho mọi người".

### Đề A — Giải thích logic C++ cho Minh

Dán **nguyên đoạn mã ở phần Tình huống mở đầu của Chương 1 và bản brief ở mục 1.3**; dòng chữ "xem ở Chương 1" không tự gửi tài liệu cho ứng dụng.

```text
Với snippet C++ đính kèm, hãy gợi ý một bước trước khi nêu cách sửa.
Sau đó giải thích bằng chỉ số vì sao tổng ba khoản GIẢ bị thiếu.
Nêu kết quả mong đợi sau sửa cho: rỗng; một khoản 7000;
ba khoản 35000, 7000, 18000. Không truy cập quá danh sách.
Phân biệt dự đoán với kết quả đã chạy; chưa viết lại toàn bộ bài.
```

Chấm cả độ đúng lẫn cách giúp người học: một câu trả lời viết ngay toàn bộ bài có thể cho kết quả đúng nhưng sai mức trợ giúp. Mọi lời khẳng định "đã chạy" đều cần bằng chứng.

### Đề B — Refactor phiên bản Web mà không đổi phạm vi sản phẩm

Dùng bản brief và **đoạn mã rút gọn dành cho đề bài** dưới đây; hàm này chỉ cộng đúng khi đầu vào hợp lệ. Đoạn rút gọn chỉ phục vụ bài tập: không suy ra rằng bản demo `data.js` thiếu kiểm tra, và không thay đoạn này vào bản demo.

```javascript
function totalExpenses(expenses) {
  return expenses.reduce((sum, expense) => sum + expense.amount, 0);
}
```

```text
Hãy đề xuất cách bổ sung xác thực cho bản rút gọn đính kèm.
Expense có id, title, amount, category; amount là số nguyên VND,
0 < amount <= 1000000000; danh sách tối đa 500 khoản; rỗng tổng 0.
Giữ HTML + JavaScript + localStorage, không backend hoặc đăng nhập.
Phân biệt kiểm tra khi thêm, khi nạp và trách nhiệm hàm tính tổng.
Nêu cách xử lý JSON hỏng và các test; chưa thêm thư viện hay tính năng.
```

Chấm theo hợp đồng dữ liệu và hành vi, không cộng điểm vì số lớp nhiều hay tên hàm giống mẫu. Chỉ kiểm tra ở form nhập rồi tin mọi dữ liệu đọc lại là chưa đủ.

### Đề C — Đọc và kiểm tra nguồn cho Lan

Cung cấp bản brief và đoạn dữ kiện sau, kèm liên kết để công cụ biết giới hạn của nguồn:

```text
ĐOẠN ĐỐI CHIẾU, THÔNG TIN GHI NHẬN THEO MỐC 29/10/2026:
GitHub Education yêu cầu đáp ứng điều kiện người học, tài khoản cá nhân
và bằng chứng tình trạng sinh viên; tài liệu ghi tuổi tối thiểu 13.
Email trường không tự bảo đảm được duyệt. Chưa xác minh độc lập.
Nguồn: https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student

Hãy tóm tắt cho Minh, phân biệt đủ điều kiện nộp với chắc chắn được duyệt.
Email TLU có tự bảo đảm ưu đãi không? Đoạn này cho phép kết luận gì
về quyền sử dụng một API khác? Nếu không truy xuất web thực,
chỉ phân tích đoạn được cung cấp, không tuyên bố đã kiểm tin mới.
```

Đề C cố ý dùng một mốc thời gian cũ và có giới hạn xác minh. Một câu trả lời tốt không "làm mới" tài liệu bằng cách gắn ngày hiện tại vào. Nếu công cụ thực sự truy xuất web, phải ghi rõ trang đã đọc và nhận định nào được trang đó hỗ trợ; đó là bằng chứng bổ sung, không xóa đi mốc thời gian của đoạn dữ kiện đã cung cấp.

### Đáp án benchmark A–C — Chuẩn đối chiếu, không phải kết quả đo

**Đề A:** điều kiện `i < n - 1` bỏ mất khoản cuối; cần sửa thành `i < n`, không dùng `i <= n`. Ba kết quả mong đợi sau khi sửa là **0, 7000 và 60000**; đây là kết quả suy ra, không phải log thực thi. Ca một khoản làm lộ rõ việc bỏ mất khoản duy nhất, trong khi riêng ca rỗng chưa đủ để phát hiện lỗi. Việc lần vết và thực thi được trình bày ở Bài thực hành 03 (mục 2.3); xác thực dữ liệu là một nhiệm vụ riêng.

**Đề B:** cần kiểm tra cấu trúc danh sách và giới hạn tối đa 500 khoản; từng `amount` phải thỏa `Number.isSafeInteger`, lớn hơn 0 và không quá 1000000000. Việc kiểm tra phải diễn ra cả khi thêm khoản mới và khi nạp lại dữ liệu; dữ liệu JSON hỏng phải được xử lý kèm thông báo, không âm thầm làm mất dữ liệu. Có thể đặt bước xác thực ở biên nhập liệu hoặc ở đầu hàm tính tổng, nhưng hợp đồng phải rõ ràng. Không thêm backend, tài khoản hay thư viện lớn. Test cho phần logic chưa kiểm chứng được phần giao diện và lưu trữ.

**Đề C:** email TLU không bảo đảm hồ sơ được duyệt; điều kiện và bằng chứng nộp hồ sơ khác với kết quả xét duyệt. Đoạn dữ kiện không chứng minh quyền sử dụng mọi API hay nội dung điều khoản hiện hành. Nếu không truy xuất mới, cần giữ nguyên mốc thời gian ban đầu và ghi rõ cần tra lại; không suy điều kiện tuổi sang dịch vụ khác.

### Rubric 10 điểm: chỉ dùng sau khi có bằng chứng

**Rubric** là bảng tiêu chí chấm điểm. Mỗi đề A, B hoặc C được chấm theo năm tiêu chí, mỗi tiêu chí từ 0 đến 2 điểm; tổng tối đa là **10 điểm cho một đề**. Rubric là cách chuyển năm lăng kính ở trên thành tiêu chí đánh giá đầu ra, không phải thuật toán xếp hạng công cụ.

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
| --- | --- | --- | --- |
| Đúng trọng tâm | Sai bài hoặc sai kết luận chính | Đúng một phần, thiếu ý quan trọng | Đúng tác vụ và kết quả chính |
| Giữ ràng buộc và context | Bỏ qua hoặc tự đổi yêu cầu | Giữ phần lớn, cần nhắc lại | Giữ các yêu cầu liên quan, nhận ra dữ kiện còn thiếu |
| Bằng chứng và provenance | Bịa nguồn, bịa việc chạy test hoặc không có căn cứ | Có căn cứ nhưng chưa rõ hoặc chưa đủ | Suy luận, test hoặc nguồn phù hợp; nêu rõ giới hạn |
| Dễ học và dễ kiểm tra | Khó hiểu, không có cách tự kiểm tra | Hiểu được một phần | Vừa sức, giúp người học tự làm bước tiếp theo |
| An toàn và tiết kiệm | Đòi dữ liệu thật hoặc key, hoặc mở rộng tốn kém | Có nhắc nhưng chưa cụ thể | Giữ dữ liệu giả, phạm vi nhỏ, tránh chi phí vô ích |

Một câu trả lời đề nghị đưa key bí mật vào mã Web phải bị loại khỏi phương án triển khai cho đến khi được sửa, dù tổng điểm ở các tiêu chí khác cao. Điểm số không bù được việc vi phạm điều kiện bắt buộc. Nếu chưa kiểm tra nguồn hoặc chưa chạy mã, cần ghi phần đó là chưa kiểm tra, không tự cộng điểm như thể đã có bằng chứng.

### Phiếu ghi nhận benchmark

| Trường ghi nhận | Kết quả ghi nhận |
| --- | --- |
| Thử công cụ thật hay luyện đánh giá trên giấy? | ______________________________ |
| Ứng dụng, model được công bố, provider đã biết, chế độ | ______________________________ |
| Ngày thử, nguồn nhận diện, tính năng đang bật | ______________________________ |
| Brief, mã nguồn và dữ liệu dùng chung | ______________________________ |
| Điểm A /10; B /10; C /10 | ______________________________ |
| Căn cứ cho điểm số và phần chưa kiểm tra | ______________________________ |
| Thời gian, số lượt phải hỏi lại | ______________________________ |
| Chi phí quan sát được hoặc "chưa xác định" | ______________________________ |
| Chọn cho tác vụ nào; không chọn cho tác vụ nào | ______________________________ |

Chỉ chấm điểm khi có bằng chứng; bài phân tích trên giấy không phải kết quả đo của model. Không chia nhỏ phí thuê bao thành giá mỗi request một cách tùy tiện. Với Minh, một câu trả lời đúng, dễ hiểu và miễn phí có giá trị hơn nhiều dòng mã mà người học không giải thích được.

## 5.4. Bài tập tổng hợp: nhận diện, ước tính chi phí và ra quyết định trong 20 phút (Mini Challenge)

Mục này giúp người học ghép các kỹ năng đã học thành một phiếu hoàn chỉnh trong 20 phút. Đây là bài tập tích hợp của cả sách: nhận diện công cụ (mục 1.2), viết prompt với context đủ dùng (mục 1.3 và Chương 2), giữ phần việc tự làm (Chương 3), giữ dữ liệu trong ranh giới an toàn (Chương 4), rồi ước tính chi phí và ra quyết định (Chương 5). Chưa làm được ngay một bước nào là bình thường; hãy xem lại mục tương ứng.

### Chuẩn bị một tờ giấy, không chuẩn bị thẻ thanh toán

Bài tập tổng hợp được làm cá nhân hoặc theo cặp, chỉ cần sách và giấy. Không đăng ký, cài đặt, gọi API, tạo key, tải giấy tờ lên hay dùng dữ liệu chi tiêu thật; không cần tài khoản AI.

**Tình huống giả định.** Minh cần hiểu lỗi 42000; Lan kiểm tra phiên bản Web cục bộ và tìm hiểu thông tin ưu đãi. Một ứng dụng giả định có tên "Trợ lý học ViSinhVien" chỉ công bố chế độ "Tự động", không nêu model của từng lượt và không nêu provider. Phiên bản Web vẫn dùng HTML, JavaScript và `localStorage`, không có backend. Chi phí dùng các số liệu giả định ở mục 5.1.

Sản phẩm cần nộp là một phiếu gồm bốn phần: nhận diện, prompt, phép tính và quyết định có điều kiện. Không cần làm hết benchmark A–C trong bài này; đây là nhiệm vụ kết hợp các kỹ năng, không phải cuộc thi tốc độ.

### Phân bổ 20 phút: mỗi bước có một mục đích

**Phút 0–4: Nhận diện.** Điền application, model và provider; thêm producer nếu biết. Gạch chân các dữ kiện đã có, khoanh tròn những điểm chưa rõ để tránh đoán model qua giao diện. Nếu quan sát một công cụ thật, chỉ đọc những thông tin được phép xem, ghi nguồn và ngày quan sát, không thay đổi cài đặt.

**Phút 4–8: Viết prompt.** Đưa vào mục tiêu, đoạn mã, hợp đồng dữ liệu, ba khoản chi và cặp số 60000/42000; yêu cầu gợi ý trước. Đọc lại prompt dưới góc nhìn của người chưa biết dự án để phát hiện phần context còn thiếu. Nếu gửi ở nơi khác, phải dán đoạn mã thật.

**Phút 8–13: Ước tính chi phí.** Tách input và output cho 50 request, quy đổi từ USD sang VND, rồi xét trường hợp 1000 request. Kiểm tra chéo theo từng request để phát hiện lỗi đơn vị; giữ nguyên các số liệu giả định để tiện đối chiếu.

**Phút 13–17: Ra quyết định.** Dùng ít nhất ba tiêu chí trong ma trận, nêu phương án không trả tiền, cách kiểm chứng và điều kiện đánh giá lại. Sở thích cá nhân không thay thế được bằng chứng.

**Phút 17–20: Đối chiếu.** Sửa phiếu nhưng giữ lại dấu vết của lỗi ban đầu để nhận ra điều vừa học được. Trình bày trong 30 giây: đã biết gì và chưa biết gì, chọn phương án nào, kiểm tra bằng cách nào, mức chi tối đa là bao nhiêu.

### Phiếu bài tập — Điền trước khi xem đáp án

| Ô cần điền | Nội dung điền |
| --- | --- |
| Ứng dụng đang xét | ________________________________________ |
| Model cụ thể hoặc chế độ được công bố | ________________________________________ |
| Provider của đường truy cập | ________________________________________ |
| Producer, nếu có căn cứ | ________________________________________ |
| Nguồn và ngày quan sát, hoặc "tình huống giả định" | ________________________________________ |
| Điều chưa đủ chứng cứ để kết luận | ________________________________________ |
| Mục tiêu và kết quả đúng của ViSinhVien | ________________________________________ |
| Hiện tượng được đề bài cho; test đầu tiên | ________________________________________ |
| Dữ liệu không được gửi | ________________________________________ |

```text
Tôi đang học: _________________________________________________
Mục tiêu và phạm vi: __________________________________________
Dữ liệu GIẢ, hợp đồng và code cần dán: __________________________
Kết quả mong đợi / hiện tượng theo đề: _________________________
Hãy giúp theo cách: ___________________________________________
Tôi sẽ tự kiểm bằng: __________________________________________
Phần chưa chạy hoặc chưa xác minh: _____________________________
```

| Phép tính bắt buộc | Kết quả kèm đơn vị |
| --- | --- |
| 20000 × 50 | ____________________ token input |
| 5000 × 50 | ____________________ token output |
| Tiền input theo đơn giá giả định | ____________________ USD |
| Tiền output theo đơn giá giả định | ____________________ USD |
| Tổng và quy đổi ở 50 request | __________ USD = __________ VND |
| Chi phí một request để kiểm tra chéo | ____________________ USD |
| Tổng ở 1000 request, bằng 20 lần ban đầu | __________ USD = __________ VND |
| Khoản chưa tính trong ví dụ | ________________________________________ |
| So với kế hoạch 300000 VND, chưa tính phí | ________________________________________ |

Hoàn thành quyết định có điều kiện:

```text
Với Minh, tôi chọn __________ vì __________.
Với Lan, tôi chọn __________ vì __________.
Ba tiêu chí tôi dựa vào là __________, __________, __________.
Phương án không trả tiền của tôi là __________.
Tôi chưa mua __________; mức chi tôi chấp nhận lúc này là __________.
Tôi sẽ cân nhắc lại khi __________, sau khi kiểm tra __________.
Nếu điều kiện tuổi chưa phù hợp hoặc chưa rõ, tôi sẽ __________.
Nếu có nguy cơ vượt ngân sách, tôi sẽ __________.
```

### Đáp án bài tập tổng hợp — Một phiếu hoàn chỉnh có điều kiện

**Nhận diện:** ứng dụng là Trợ lý học ViSinhVien, chế độ Tự động; model, provider và producer đều chưa xác định. Nguồn thông tin là tình huống giả định, không phải quan sát dịch vụ thật; vì vậy không tự ghi một ngày truy cập thật.

**Mục tiêu:** cộng mọi khoản hợp lệ; với ba khoản giả, kết quả mong đợi là 60000, còn hiện tượng đề bài cho là 42000. Danh sách rỗng có tổng 0; cần thử ca một khoản 7000 rồi ca ba khoản để phát hiện lỗi bỏ khoản cuối. Không gửi key, giấy tờ, sao kê, thông tin tài khoản hay dữ liệu cá nhân. Nếu chưa chạy chương trình, chỉ ghi kết quả mong đợi, không báo cáo như đã chạy test.

**Prompt mẫu:**

```text
Tôi là Minh năm nhất, mới học vòng lặp C++.
ViSinhVien cộng tất cả khoản hợp lệ: amount nguyên VND,
0 < amount <= 1000000000, tối đa 500 khoản; rỗng tổng 0.
Dữ liệu GIẢ: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000.
Kỳ vọng 60000; tình huống đề cho chương trình kết thúc ở 42000.
Tổng tối đa 500000000000, không đổi sang kiểu không chứa đủ.
Tôi dán snippet lỗi ngay sau yêu cầu này.
Hãy gợi ý một bước bằng chỉ số, chưa viết lại chương trình.
Sau đó nêu test rỗng, một khoản 7000, ba khoản mẫu.
Phân biệt suy luận với chạy thật; thiếu dữ kiện thì chỉ rõ.
```

Khi dùng mẫu này, phải dán kèm đoạn mã ở Tình huống mở đầu của Chương 1; câu "tôi dán snippet" không tự đính kèm mã. Nếu đã thực sự chạy chương trình, có thể thay dòng mô tả hiện tượng bằng lệnh và log của chính người học, không dùng kết quả dự đoán thay cho log.

**Phép tính:** tổng input 1000000 token, tổng output 250000 token; số tiền tương ứng là 0.30 USD và 0.625 USD. Tổng cộng **0.925 USD = 23125 VND, chưa tính phí**. Một request tốn **0.0185 USD**, nhân với 50 cho kết quả khớp. Với 1000 request: input 20000000 token, output 5000000 token; số tiền là 6.00 + 12.50 = **18.50 USD = 462500 VND, chưa tính phí**. Mức chi này vượt kế hoạch giả định 300000 VND; cảnh báo ngân sách không tự bảo đảm chặn được hóa đơn. Thuê bao giả định 20 USD tương đương 500000 VND/tháng, nhưng quyền lợi chưa chắc tương đương với API.

**Với Minh:** dùng giấy, tài liệu hoặc gợi ý từ một công cụ miễn phí hợp lệ; tự sửa cận vòng lặp trên bài làm, kiểm tra các ca rỗng, một khoản và ba khoản ở Bài thực hành 03 (mục 2.3). Ba tiêu chí lựa chọn là context đủ dùng, test kiểm tra được và chi phí bằng 0; dữ liệu giả bảo đảm quyền riêng tư. Minh không cần dùng API.

**Với Lan:** giữ phiên bản Web chạy cục bộ, kiểm tra đầu vào và hàm tính tổng, sau đó kiểm tra riêng phần hiển thị, lưu và nạp dữ liệu. Thông tin ưu đãi cần nguồn chính thức; nếu chưa truy xuất được thì ghi "chưa xác minh" và chưa mua. Lan không tự tích hợp API vào ViSinhVien.

**Điều kiện đánh giá lại:** khi phương án miễn phí không đáp ứng được một nhu cầu rõ ràng, khi đã tra cứu quyền lợi, điều kiện tuổi và chính sách dữ liệu, khi quản lý được chi phí và biết cách dừng gia hạn. Nếu chưa đủ điều kiện hoặc chưa hiểu cơ chế kiểm soát chi tiêu, tiếp tục học trên giấy hoặc với công cụ miễn phí. Mức chi hiện tại có thể là 0 VND.

## Câu hỏi tự kiểm tra

Hãy trả lời từng câu bằng một kết luận và một lý do. Chưa trả lời được ngay là bình thường; khi đó hãy xem lại mục tương ứng. Điều cần chỉ ra là loại bằng chứng còn thiếu, không chỉ nhớ chữ "không".

1. Nhãn "tích hợp Claude" đã đủ để xác định provider và phiên bản model chưa?
2. Đếm số từ tiếng Việt có đủ để tính chính xác hóa đơn theo token không?
3. Email TLU có bảo đảm nhận được ưu đãi sinh viên và quyền dùng mọi API không?
4. Trả phí và bật budget alert đã đủ bảo đảm quyền riêng tư và không vượt ngân sách chưa?
5. Cần dịch một thông báo lỗi và cần tra điều kiện ưu đãi hiện hành. Hai việc này có nên dùng cùng một công cụ theo cùng một cách không?
6. Một công cụ được nhiều người khen là "mạnh nhất". Điều đó có đủ để chọn nó cho bài tập về vòng lặp C++ của Minh không?

### Đáp án câu hỏi tự kiểm tra — Sáu kết luận và lý do

**1. Chưa.** Cần định danh model và đường truy cập; producer có thể khác provider, như ví dụ Claude qua Amazon Bedrock. Không đoán qua văn phong của câu trả lời. (Xem lại mục 1.2.)

**2. Không.** Số token phụ thuộc vào tokenizer và nội dung; usage có thể gồm cả lịch sử, mã nguồn, tool output và các khoản tính riêng. Cần dùng công cụ đếm phù hợp và báo cáo lượng dùng của dịch vụ, không dùng số đếm từ. (Xem mục 1.3 và 5.1.)

**3. Không.** Còn các điều kiện khác, bằng chứng về tình trạng sinh viên và quá trình xét hồ sơ. Điều kiện tuổi và quyền sử dụng từng API phải được tra cứu riêng; thông tin ghi nhận theo mốc thời gian cũ chưa phải xác nhận hiện hành.

**4. Chưa.** Cần kiểm tra chính sách của đúng sản phẩm, đúng cấp dịch vụ và cài đặt. Budget alert không mặc nhiên là hard cap; cần hiểu cơ chế chặn, phạm vi áp dụng, độ trễ và các request đang xử lý.

**5. Không nên mặc định như vậy.** Việc dịch cần giữ nguyên tên API, số liệu và phủ định; việc tra điều kiện ưu đãi cần nguồn chính thức hiện hành và ngày truy cập. Công cụ không truy cập web không thể là nguồn duy nhất cho chính sách mới. Mỗi tác vụ có loại bằng chứng riêng, nên câu hỏi "phù hợp với việc gì?" đứng trước câu hỏi "mạnh nhất?" (mục 5.3).

**6. Chưa đủ.** Danh tiếng không cho biết công cụ có giúp Minh tự suy nghĩ, có kiểm tra được bằng chỉ số và ba ca thử, và có miễn phí hay không. Với Minh, một gợi ý đúng, dễ hiểu và miễn phí có giá trị hơn một lời giải đầy đủ mà người học không giải thích được. Các lựa chọn cần dựa trên tác vụ, rủi ro và ngân sách.

## Ôn tập: tự trình bày lại trong 5 phút

Phần ôn tập này không thay thế bài tập tổng hợp 20 phút ở mục 5.4. Người học có thể trình bày trước nhóm học hoặc tự ghi âm mà không cần mở giao diện của bất kỳ dịch vụ nào. Kịch bản dưới đây chuyển một bài trình bày ngắn thành hình thức tự học.

| Thời gian | Nội dung trình bày | Điều cần chứng minh |
| --- | --- | --- |
| 0:00–1:00 | Nêu tình huống Minh và Lan; phân biệt application, provider và model, kể cả khi ghi "chưa biết" | Không đồng nhất ứng dụng với model |
| 1:00–2:15 | Tính riêng chi phí input và output cho 50 rồi 1000 request | Giữ đơn vị, số liệu giả định và ghi chú "chưa tính phí" |
| 2:15–3:15 | Trình bày nguyên tắc ưu tiên miễn phí; nhắc điều kiện tuổi, ưu đãi, gia hạn, dữ liệu | Không coi email trường hay việc trả tiền là sự bảo đảm |
| 3:15–4:15 | Chọn công cụ cho một tác vụ theo năm lăng kính: provenance, test, context, privacy, cost | Chọn theo nhiệm vụ, không theo danh tiếng |
| 4:15–5:00 | Nêu cách kiểm tra kết quả và hỏi: cảnh báo ngân sách có dừng chi tiêu không | Nêu được bằng chứng và những điều chưa xác minh |

Nếu có thêm 2 phút, bổ sung một quyết định có điều kiện theo mẫu ở mục 5.4. Không trình diễn thao tác đăng nhập, thanh toán hoặc giấy tờ cá nhân để làm bài trình bày sinh động hơn.

## Tóm tắt chương

Phiếu bài tập hoàn chỉnh của chương thể hiện các năng lực: nhận diện công cụ, chọn context, tính chi phí input và output, đối chiếu công cụ theo tác vụ và ra quyết định chi tiêu có điều kiện. Phiếu này là bằng chứng của một buổi học, không phải chứng nhận năng lực lâu dài.

Ba ý chính của chương:

- **Chọn công cụ theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng; khi thiếu chứng cứ về ứng dụng, đường truy cập hay model, ghi "chưa xác định".**
- **Ưu tiên phương án miễn phí đủ dùng; tính lượng dùng, tách input với output và xét điều kiện trước khi trả tiền. Không mua dịch vụ vẫn có thể học nghiêm túc.**
- **Mọi lựa chọn cần kiểm chứng bằng phép tính, test hoặc nguồn chính thức; sự tự tin của câu trả lời và việc đã trả phí đều không phải bằng chứng.**

Mạch năm bước của sách có thể tóm gọn như sau. Chương 1 giúp hiểu vai trò và giới hạn của AI; Chương 2 hướng dẫn dùng AI có kiểm soát; Chương 3 giữ cho người học vẫn tự học được; Chương 4 đặt ranh giới về dữ liệu, bảo mật, bản quyền và liêm chính; Chương 5 giúp chọn công cụ có cơ sở. Xuyên suốt cả năm bước là một nguyên tắc: AI hỗ trợ, người học quyết định.

## Cầu nối sang chương sau

Năm bước đã đủ để từng việc riêng lẻ được làm cẩn thận. Dự án tổng kết ghép các bước đó thành một sản phẩm hoàn chỉnh: người học xây dựng, kiểm thử và giải thích, đồng thời lưu bằng chứng cho từng quyết định về công cụ, cách dùng và ranh giới.

## Tài liệu tham khảo

Các nguồn dưới đây được ghi nhận theo mốc truy cập 29/10/2026. *Chưa kiểm chứng:* nội dung hiện hành của các nguồn chưa được xác minh độc lập; cần tra lại thông tin về model, gói dịch vụ, credit, quota, điều kiện tuổi, chính sách dữ liệu và thanh toán trước khi áp dụng.

| Nội dung đối chiếu | Nguồn chính thức |
| --- | --- |
| Họ model, định danh | [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview) |
| Claude qua provider khác | [AWS — Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) |
| API, xác thực, chỉ định model | [Google — Gemini API docs](https://ai.google.dev/gemini-api/docs) |
| Lớp ứng dụng Gemini | [Google — Gemini overview](https://gemini.google/overview/) |
| Tuổi, điều kiện, bằng chứng sinh viên | [GitHub — Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student) |
| Quyền lợi, thời hạn, giới hạn | [GitHub Student Developer Pack](https://education.github.com/pack) |
| Gói miễn phí và trả phí, đơn vị giá, phụ phí | [Google — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Tuổi, sản phẩm và cấp dịch vụ, xử lý dữ liệu | [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms) |
| Cơ chế kiểm soát mức dùng | [Google — Gemini API billing](https://ai.google.dev/gemini-api/docs/billing) |
| Ngân sách và cảnh báo | [Google Cloud — Budgets](https://cloud.google.com/billing/docs/how-to/budgets) |
| Credit API theo điều kiện gói | [OpenAI — ChatGPT/API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |

Các mức giá **0.30 USD và 2.50 USD mỗi triệu token**, thuê bao **20 USD**, tỷ giá **25000 VND/USD** và ngân sách **300000 VND** trong chương đều là dữ liệu giả định, không lấy từ bảng giá thật. Các thẻ trả lời hư cấu không phải benchmark; các bảng kết quả mong đợi không phải log thực thi. Mọi kiểm chứng thật phải ghi riêng công cụ, lệnh hoặc nguồn đã dùng, ngày thực hiện và kết quả thu được.
