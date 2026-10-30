# Thỏa thuận học tập · Được làm gì, tự làm gì, chứng minh bằng gì?

AI có thể giải thích, gợi ý và sinh mã. Bạn quyết định mục tiêu, phạm vi chia sẻ, thay đổi được nhận và bằng chứng cần có.

**Mẫu tự học, không phải quy định hay biểu mẫu chính thức của TLU.** Yêu cầu bài/học phần và giảng viên quyết định việc dùng AI. Khai báo không thay sự cho phép, giấy phép hoặc kiểm chứng.

*Kế thừa thỏa thuận mở đầu và mục 4.1, 4.7 nguồn. Bổ sung biên tập: phiếu trước buổi, sổ đóng góp, bảng kỳ vọng–thực tế. Ô vuông để trống, không xác nhận việc đã làm.*

## 1. Làm rõ quyền trước khi giao việc

| Tình trạng theo yêu cầu bài | Hành động của người học |
|---|---|
| Được phép | Dùng đúng phần cho phép, đúng điều kiện khai báo và lưu bằng chứng. |
| Bị cấm | Không dùng AI tạo/sửa lời giải trong phạm vi bị cấm; chọn tài liệu và hỗ trợ được phép. |
| Có điều kiện | Ghi rõ điều kiện: được giải thích chưa chắc được sinh cả hàm; hỏi khi hành động sắp vượt phạm vi. |
| Chưa rõ | Hỏi giảng viên; trong lúc chờ chỉ tiếp tục phần chắc chắn được phép. Im lặng không là đồng ý. |

Không lấy việc bạn cùng lớp dùng, gói miễn phí hay bài làm chạy được làm căn cứ. Với bài nhóm, thống nhất phạm vi trước khi nhận mã vào bản chung.

**Tin nhắn có thể điều chỉnh rồi gửi:**

> Thưa thầy/cô, với bài [tên bài], em dự định tự viết [phần cụ thể]. Em muốn dùng [công cụ] để [giải thích lỗi/gợi ý ca kiểm thử/sinh nháp phần nào], rồi tự [sửa, chạy và giải thích]. Em chỉ cung cấp dữ liệu giả và đoạn mã cần thiết. Phạm vi này có được phép không ạ? Nếu được, em cần khai báo ở đâu và giữ bằng chứng nào? Trong lúc chờ, em sẽ làm phần [chắc chắn được phép].

Giữ căn cứ và thời điểm trả lời theo yêu cầu môn; không đăng hội thoại riêng của giảng viên lên kho công khai.

## 2. Phiếu trước buổi làm: điền đủ để bắt đầu

Thay nội dung trong ngoặc bằng tình trạng thật. Không biết thì ghi **chưa rõ**, kèm bước hỏi; đừng để ô trống mang nghĩa “đã được duyệt”.

| Mục | Bạn điền |
|---|---|
| Bài, thành viên, vai trò | [Tên bài; ai viết, ai rà soát; cá nhân thì ghi tự rà.] |
| Căn cứ cho phép | [Đề/mục hướng dẫn/phản hồi, ngày; điều được và không được làm.] |
| Mục tiêu buổi này | [Một hành vi quan sát được, ví dụ giải thích vì sao vòng lặp bỏ khoản cuối.] |
| Phần bắt buộc tự làm | [Tự dự đoán, viết/sửa phần nào, chọn ca thử, giải thích và làm biến thể nào.] |
| AI được hỗ trợ | [Giải thích/gợi ý/sinh nháp; tệp, hàm, câu hỏi giới hạn.] |
| Quyền công cụ | [Được đọc/sửa tệp nào; lệnh nào cần duyệt. Không mặc định cho cài gói, commit hay đưa mã lên mạng.] |
| Dữ liệu được đưa vào | [Dữ liệu giả tự tạo; đoạn mã tối thiểu; ảnh đã rà. Không gửi key, mật khẩu, hồ sơ hay chi tiêu thật.] |
| Điểm dừng | [Thiếu quyền/chưa hiểu/lỗi chưa tái hiện: lưu trạng thái, hỏi ai, tiếp tục phần nào.] |

Bỏ tên khỏi dữ liệu thật chưa chắc đã khử nhận dạng. Rà cả ảnh, đường dẫn, chat và lịch sử tệp sẽ chia sẻ. Nếu lộ khóa thật, dừng chia sẻ, thu hồi hoặc nhờ người có quyền vô hiệu khóa; báo đầu mối phù hợp. Xóa dòng hay tự ép đẩy Git không giải quyết mọi bản sao.

## 3. Ghi đóng góp và nguồn ngay khi dùng

Mỗi hỗ trợ đáng kể ghi một dòng. Nếu AI sinh cả hàm, ghi **sinh bản nháp hàm**, không đổi thành “tham khảo ý tưởng”. Người rà soát phải nói đã đọc diff hay chạy thử, không ghi chung “đã xem”.

| Công cụ, ngày, phiên bản nếu biết | Hỗ trợ thực tế, vị trí | Phần người học làm | Quyết định và căn cứ |
|---|---|---|---|
| [Tên; chưa biết phiên bản thì ghi vậy] | [Giải thích/gợi ý/sinh nháp tệp hoặc hàm nào] | [Ai sửa, viết lại, kiểm và giải thích] | [Giữ/bỏ; vì sao; bằng chứng hoặc chưa kiểm] |

Ghi nguồn là **attribution**; quyền sử dụng là câu hỏi về giấy phép/quyền đối với sản phẩm; trách nhiệm là kiểm tra và giải trình theo vai trò. Ba việc không thay nhau.

| Thành phần sử dụng | Nguồn và phiên bản thật | Quyền, điều kiện cần giữ | Quyết định |
|---|---|---|---|
| [Mã/ảnh/tài liệu cụ thể] | [URL hoặc tài liệu, bản đã dùng] | [Giấy phép đã đọc; thông báo cần giữ; chưa rõ thì ghi rõ] | [Dùng có điều kiện/hỏi/loại hoặc tự viết lại] |

Kho công khai không giấy phép không tự cấp quyền sao chép. MIT có điều kiện giữ thông báo; GPL không cấm thương mại nhưng cần đọc nghĩa vụ theo cách dùng và phân phối. “AI tạo” không chứng minh nguồn gốc hay quyền độc quyền. Không rõ quyền thì loại/thay phần đó hoặc hỏi, không chỉ thêm một đường dẫn.

## 4. Bằng chứng: tách kỳ vọng khỏi điều đã thấy

**Mẫu ghi kiểm tra, chưa có kết quả thực thi.** Đầu bảng ghi: [ngày, người kiểm, hệ điều hành, công cụ/phiên bản, bản mã hoặc mốc lưu, lệnh/thao tác]. Với mỗi hàng, điền quan sát thật hoặc **chưa chạy**. Nếu chỉ đọc mã, ghi **rà soát tĩnh**, không ghi đạt kiểm thử.

| Mục kiểm | Đầu vào/thao tác | Kỳ vọng theo hợp đồng | Thực tế và trạng thái bạn điền |
|---|---|---|---|
| Tổng chuẩn | Ba khoản giả `35000`, `7000`, `18000` | `60000` | [Quan sát; đạt/không đạt/chưa chạy; chỗ lưu bằng chứng] |
| Rỗng; một khoản | Danh sách rỗng; riêng khoản `7000` | `0`; `7000` | [Ghi riêng từng lần] |
| Biên tiền | `1`, `1e9`; thử riêng 0, âm, vượt trần | Nhận hai biên; từ chối giá trị sai | [Kết quả từng ca] |
| Số thập phân/chuỗi Web | Nhập số thập phân, chuỗi không hợp lệ; đối chiếu kiểu `amount` | Từ chối; không lén lấy một phần chuỗi | [Quan sát/chưa chạy] |
| Số lượng | 500 khoản hợp lệ; thử khoản thứ 501 | Nhận 500; từ chối 501 | [Quan sát/chưa chạy] |
| Bản ghi Web | Sai `id`, `title`, `category`; thử `category: ['khac']` riêng | `normalizeExpenses` từ chối bản ghi sai | [Không thay bằng test tổng tiền] |
| Hiển thị Web | Fixture tên `<b>Vở</b>` | Hiện nguyên văn trong ô bảng, không thành chữ in đậm | [Quan sát trình duyệt/chưa chạy] |
| Lưu trữ Web | Nạp lại trang; lưu bị chặn hoặc dữ liệu hỏng | Lưu được: giữ dữ liệu; bị chặn/hỏng: thông báo, dùng RAM | [Nêu đúng điều kiện đã thử] |

Giữ fixture riêng, không trộn vào ba khoản chuẩn rồi vẫn gọi tổng là `60000`. C++ dùng `vector<long long>`, không có parser số thập phân: không nhận đã kiểm chức năng không có. Build lỗi thì dừng; tệp chạy cũ không chứng minh mã mới đúng.

**Đối chiếu phiên bản:** [kiểm kê nguồn](../editorial/01_SOURCE_AUDIT.md) ghi bản Web mới có **34 ca JavaScript** sau vá `category`, nguồn cũ có **33 ca**; bản C++ có **9 ca**. Đây không phải kết quả chạy của phiếu này. Khi chạy, ghi số ca thực thi, đầu ra và exit code thật. Test Node.js không chứng minh DOM/lưu trữ đúng; số ca không cộng thành điểm chất lượng.

## 5. Mẫu khai báo dùng cho bản nộp

Chép mẫu rồi điền sự thật, theo hình thức giảng viên yêu cầu. Không cần nộp toàn bộ chat chứa dữ liệu riêng tư.

> **Bài/nhóm, vai trò:** [điền].
>
> **Phạm vi được phép và căn cứ:** [điền; phần đang chờ phải ghi đang chờ].
>
> **Công cụ, thời điểm, phiên bản nếu biết:** [điền; nếu không dùng AI, ghi không dùng].
>
> **Hỗ trợ thực tế:** [giải thích/gợi ý/sinh nháp phần nào, vị trí nào].
>
> **Phần tự làm:** [ai viết, sửa, chọn/bỏ đề xuất và giải thích quyết định].
>
> **Dữ liệu cung cấp:** [dữ liệu giả, mã tối thiểu, quyền đã cấp; sự cố báo riêng, không dán bí mật].
>
> **Nguồn và giấy phép:** [nguồn thật, điều kiện đã thực hiện, phần loại vì chưa rõ quyền].
>
> **Kiểm chứng:** [đã chạy gì, bản nào, quan sát; phần chỉ đọc mã; phần chưa chạy].
>
> **Chưa hiểu/chưa kiểm và bước tiếp:** [vấn đề, ảnh hưởng, người cần hỏi, việc sẽ làm].
>
> **Giới hạn sản phẩm:** [nhánh thực tế]. Web dùng HTML/JavaScript/localStorage, không backend/đăng nhập; SQL là minh họa Python `sqlite3` riêng trong `:memory:`. Chỉ dùng dữ liệu giả.

**Ví dụ cách ghi mức chắc chắn — tình huống biên tập, không phải nhật ký đã chạy:** “Em đã đọc điều kiện kiểm tra `amount`, nhưng chưa chạy vì máy chưa có môi trường cần thiết. Em chưa xác nhận hành vi trình duyệt. Em sẽ xin hướng dẫn môi trường và bổ sung quan sát; không đánh dấu đạt.” Chỉ dùng lời này nếu đúng quá trình của bạn; đừng biến ví dụ thành lời khai.

## 6. Trước khi gửi: ưu tiên và tự đánh giá

**Chặn nộp phần liên quan theo checklist luyện tập:**

- [ ] Đã xử lý dữ liệu/khóa không nên chia sẻ; không đính kèm bí mật làm bằng chứng.
- [ ] Đúng hợp đồng tiền/số lượng; kiểm chứng bắt buộc có quan sát thật; lỗi trọng yếu không bị che bằng giao diện đẹp.
- [ ] Không còn phần chưa rõ quyền hoặc phụ thuộc chưa kiểm chứng trong bản nộp.
- [ ] Khai báo đúng mức hỗ trợ; giải thích được phần trọng yếu mình nhận trách nhiệm.

**Cần hỏi:** phạm vi AI, điều kiện nguồn/dữ liệu, hình thức khai báo hoặc việc ngoài quyền của nhóm. Ghi trạng thái chờ, không xem câu hỏi đã gửi là vấn đề đã giải quyết. Có thể thu hẹp phần chưa rõ nếu vẫn đáp ứng yêu cầu bài và được giảng viên chấp nhận.

**Cải thiện sau:** màu sắc, khoảng cách, tính năng mở rộng; không dùng chúng để trì hoãn xử lý dữ liệu, nguồn và lỗi cốt lõi.

Rubric kế thừa để **tự luyện**, không là thang điểm TLU: mỗi mục 0–2, tối đa 8; điểm tổng không bù lỗi chặn nộp.

| Mục | 0 | 1 | 2 |
|---|---|---|---|
| Học thuật và nguồn | Không rõ | Có ghi nhưng mơ hồ | Phạm vi, đóng góp, nguồn/quyền rõ |
| Dữ liệu và quyền | Dữ liệu/quyền không phù hợp | Đã giảm, chưa rà đủ | Rà đúng bản chia sẻ, quyền vừa đủ |
| Tính đúng và đọc mã | Chưa đối chiếu | Hiểu một phần, thiếu bằng chứng | Đối chiếu hợp đồng và ranh giới ví dụ |
| Kiểm chứng, xử lý | Khẳng định vô căn cứ | Ghi được một phần | Truy lại được bằng chứng và việc còn thiếu |

Trước khi đánh dấu, tự giải thích một luồng không mở AI, nêu một đầu vào bị từ chối và lý do. Vướng đâu ghi đó rồi học lại hoặc hỏi; không cần học thuộc từng dấu câu. Đóng buổi bằng ba dòng: **đã hiểu / chưa chắc / bước tiếp theo**.
