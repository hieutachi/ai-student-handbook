# LỜI GIỚI THIỆU

**Học CNTT cùng AI — Cẩm nang khởi đầu dành cho sinh viên năm thứ nhất và năm thứ hai, Khoa Công nghệ thông tin, Trường Đại học Thủy lợi.**

## Cuốn sách này dành cho ai

Các công cụ trí tuệ nhân tạo (AI) có thể giải thích lỗi, đề xuất mã nguồn và gợi ý ca kiểm thử trong vài giây. Câu hỏi cho người học lập trình là: làm sao tận dụng công cụ mà không giao luôn phần suy nghĩ cho nó. Cẩm nang này trả lời bằng những kỹ năng cụ thể, mỗi kỹ năng kèm một việc nhỏ để thử.

Đối tượng chính là sinh viên năm thứ nhất và năm thứ hai ngành Công nghệ thông tin: chỉ cần biết biến, câu lệnh điều kiện và vòng lặp trong C++; kiến thức Web và cơ sở dữ liệu là lợi thế thêm. Không cần mua dịch vụ AI trả phí để bắt đầu.

## Năm bước của một câu chuyện

Cẩm nang kể một câu chuyện duy nhất, quan hệ giữa người học và AI, qua năm bước; mỗi chương là một bước.

**Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn**

| Chương | Câu hỏi trung tâm | Thông điệp |
|---|---|---|
| 1 | AI là gì, đóng vai trò gì trong học tập, giúp được gì và không giúp được gì? | AI là người hỗ trợ; người học là người quyết định. |
| 2 | Dùng AI thế nào để việc làm có kiểm soát? | Giao việc rõ, kiểm bằng bằng chứng, nhận thay đổi có chủ đích. |
| 3 | Tận dụng AI mà không lạm dụng: làm sao vẫn học được? | Tự dự đoán, tự làm, tự giải thích; AI chỉ đứng cạnh. |
| 4 | Ranh giới nào cần giữ về dữ liệu, bảo mật, bản quyền, liêm chính? | Dùng có trách nhiệm là điều kiện để được tiếp tục dùng. |
| 5 | Khi đã hiểu vai trò, cách dùng và ranh giới: chọn AI, model, gói dịch vụ nào cho nhiệm vụ này? | Chọn theo nhiệm vụ, rủi ro và ngân sách, không theo danh tiếng. |

Dự án tổng kết ghép năm bước thành một sản phẩm có bằng chứng: làm, kiểm, giải thích. Việc chọn model và trả phí nằm ở cuối vì chỉ khi đã hiểu vai trò, cách dùng và ranh giới, người học mới chọn có cơ sở. Một ý cần nhớ xuyên suốt: **AI hỗ trợ, người học quyết định.**

## Hai người học và ba khoản chi

Sách dựa trên một tình huống minh họa chung:

- **Minh**, năm thứ nhất, đã biết biến và vòng lặp trong C++, nhưng có thói quen hỏi AI ngay khi gặp lỗi.
- **Lan**, năm thứ hai, đã học Web và cơ sở dữ liệu, dựng được giao diện nhưng còn lúng túng khi một lỗi đi qua nhiều tệp.

Hai người cùng xây dựng **ViSinhVien**, ứng dụng ghi các khoản chi tiêu nhỏ, với bảng dữ liệu mẫu dùng trong mọi chương:

| Khoản chi | Nhóm | Số nguyên lưu trong mã | Hiển thị |
|---|---|---:|---:|
| Cơm trưa | Ăn uống | `35000` | 35.000 đ |
| Xe buýt | Đi lại | `7000` | 7.000 đ |
| Vở ghi | Học tập | `18000` | 18.000 đ |
| **Tổng đối chiếu** | | **`60000`** | **60.000 đ** |

Hai vấn đề mở đầu dẫn dắt cả cuốn sách: phiên bản C++ của Minh cho tổng `42000` thay vì `60000`; Lan cần xác định giá trị tiền đi từ ô nhập đến phần tính tổng như thế nào. Qua các chương, chúng ta lần lượt dự đoán, kiểm tra và giải thích. Người học chọn nhánh Minh (C++) hoặc nhánh Lan (Web) tùy kiến thức đã có.

## Phạm vi của nội dung

Nhân vật, hội thoại, tình huống và dữ liệu trong sách đều hư cấu, không phải kết quả khảo sát sinh viên hay bảng giá thực tế của dịch vụ nào. Sách không phải quy định chính thức của Trường Đại học Thủy lợi, không phải đề cương học phần hay tư vấn pháp lý; mức độ được dùng AI trong một bài cụ thể do giảng viên quyết định. Thông tin về sản phẩm, dịch vụ và văn bản pháp lý đối chiếu tại mốc 29/10/2026, cần tra lại trước khi dùng.

Sách dùng thống nhất bốn nhãn: *Tình huống hư cấu* cho nhân vật, hội thoại và thẻ trả lời minh họa; *Dữ liệu giả định* cho số tiền, giá và kịch bản tính toán; *Chưa kiểm chứng* cho thông tin dịch vụ, chính sách cần tra lại; *Kết quả mong đợi* cho đầu ra suy ra từ mã nguồn, chưa thực thi.

## Cách dùng hai cuốn

Hai cuốn dùng chung một câu chuyện và một bộ ví dụ.

Hãy đọc **Cẩm nang khởi đầu** (cuốn đang mở) trước. Mỗi mục nêu một ý chính, cho một việc nhỏ "Thử ngay" làm được trong mười phút không cần tài khoản AI, rồi để lại câu hỏi mở. Cẩm nang không in đáp án; "Gợi ý đối chiếu" chỉ nêu tiêu chí để tự biết đã đúng hướng.

**Sổ tay thực hành** là nơi đi sâu. Khi muốn làm bài đầy đủ, xem đáp án hay bảng kiểm thử, hãy mở [Sổ tay thực hành](../chapters/introduction.md). Mỗi mục trong cẩm nang kết thúc bằng phần "Tự tìm hiểu thêm" trỏ tới mục tương ứng của Sổ tay.

Đi kèm là ba phần tham khảo: [Thư viện prompt mẫu](prompt-library.md) với các thẻ giao việc, [Bảng thuật ngữ](glossary.md) và [Thỏa thuận học tập](../chapters/learning-agreement.md) với mẫu khai báo mức hỗ trợ của AI. Khi gặp điều chưa rõ, hãy hỏi giảng viên; câu trả lời của AI không thay thế cho việc kiểm chứng.
