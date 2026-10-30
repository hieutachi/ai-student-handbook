# CHƯƠNG 1 · BƯỚC VÀO THẾ GIỚI AI

Minh mở ba giao diện AI, dán cùng đoạn C++ và hỏi cùng một câu. Nơi thứ nhất hỏi ngược lại. Nơi thứ hai đưa cách sửa rất chắc chắn. Nơi thứ ba sửa khác, nhắc phải kiểm thử. Minh nhìn ba cửa sổ: “Nếu đều là AI, tại sao chúng không nói giống nhau? Mình nên tin cái nào?”.

**Bổ sung biên tập — tình huống mở và ba thẻ trả lời hoàn toàn HƯ CẤU**, không đại diện sản phẩm, không phải hội thoại hay benchmark thực. Minh năm nhất học C++; Lan năm hai học OOP/DSA/CSDL/Web. Hai nhân vật hư cấu không đại diện khảo sát TLU.

Hai bạn làm **ViSinhVien**, bài tập chi tiêu bằng dữ liệu GIẢ. Minh học mảng và vòng lặp; Lan làm Web với HTML, JavaScript, `localStorage`. Không có backend, đăng nhập, ngân hàng hay tài chính thật. Trợ lý AI giúp học; ViSinhVien không tích hợp AI.

Ba khoản GIẢ trên giấy của Minh là:

| Khoản chi GIẢ | Số tiền nguyên VND |
| --- | ---: |
| Cơm trưa | 35000 |
| Xe buýt | 7000 |
| Vở ghi | 18000 |
| Tổng cần có | 60000 |

Đây là **snippet có lỗi chủ đích** để đọc và đặt câu hỏi, không phải yêu cầu làm hỏng demo đúng. Các số tiền trong snippet đã được giả định hợp lệ; chương trình chưa làm nhiệm vụ nhập và xác thực dữ liệu.

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

Minh dán nguyên snippet vào từng giao diện, rồi dùng cùng câu hỏi:

```text
Tôi mới học vòng lặp C++. Tôi cần cộng tất cả khoản chi GIẢ:
35000, 7000, 18000 phải ra 60000, nhưng chương trình đang cho 42000.
Hãy gợi ý một bước để tôi tự tìm lỗi, chưa viết lại cả chương trình.
```

### Thẻ trả lời A — HƯ CẤU, không gắn với sản phẩm

> Khi `n = 3`, chỉ số của khoản Vở ghi là bao nhiêu? Hãy thay chỉ số đó vào điều kiện `i < n - 1` và quyết định xem vòng lặp có cộng khoản này không.

### Thẻ trả lời B — HƯ CẤU, không gắn với sản phẩm

> Vòng lặp thiếu một lượt. Bạn cứ đổi thành `i <= n`; như vậy sẽ cộng đủ và luôn an toàn. Không cần thử thêm vì lỗi này rất đơn giản.

### Thẻ trả lời C — HƯ CẤU, không phải báo cáo đã chạy

> Điều kiện đang bỏ phần tử cuối. Với yêu cầu cộng mọi khoản, hướng sửa là `i < n`, không phải `i <= n`. Tôi chưa thực thi chương trình; hãy kiểm tra danh sách rỗng, một khoản và ba khoản sau khi tự sửa.

Lan chưa chọn “AI thắng cuộc”. Cô lấy bút khoanh yêu cầu **gợi ý một bước**, rồi gạch chân chữ **luôn an toàn** trên thẻ B. Một câu trả lời phải được xét cả độ đúng, cách giúp người học và bằng chứng, chứ không chỉ tốc độ xuất hiện.

Trước khi đọc tiếp, hãy tự cộng ba khoản, chọn một thẻ để bắt đầu học và viết lý do. Nếu chưa biết C++, bạn vẫn có thể nhận ra rằng một kết luận về chương trình cần cách kiểm tra. Sau mục 1.5, hãy chấm lại ba thẻ bằng rubric 10 điểm ở đó (rubric viết cho Đề A–C, nhưng năm tiêu chí dùng được cho thẻ).

**Đầu ra của chương:** một bản nhận diện công cụ có phần “chưa biết”, một prompt đủ context, một phép tính chi phí có đơn vị và một quyết định dùng công cụ có điều kiện. Không cần đăng ký, cài đặt, tạo key, gọi API hoặc trả tiền để hoàn thành.

## 1.1. AI MYSTERY / AI MAP — Giải bí ẩn, đọc bản đồ AI

### Từ 42000 đến câu hỏi “mình đang dùng cái gì?”

`35000 + 7000 = 42000`; thêm `18000` mới được `60000`. **42000 có thể là tổng trung gian đúng** hoặc tổng của hai khoản. Nó chỉ là sai lệch khi yêu cầu cộng đủ ba khoản mà chương trình kết thúc ở đó. Một con số đứng riêng chưa chẩn đoán được lỗi.

Snippet có `n = 3`, chỉ số hợp lệ 0, 1, 2. Cận `i < n - 1`, tức `i < 2`, chặn khoản Vở ghi ở chỉ số 2. `static_cast<int>` chuyển kích thước sang số nguyên có dấu để biểu diễn cận; tối đa 500 khoản vừa trong miền đang dùng.

**Kết quả dự đoán từ snippet**, không phải log thực thi của lần biên tập:

```text
Tong chi tieu: 42000 VND
```

Chuỗi không dấu nhằm giảm lỗi hiển thị ở một số terminal. Trace đầy đủ, ca rỗng, kiểu có dấu/không dấu và executable cũ được học ở **Chương 2 · Trở thành người điều khiển AI, mục 2.3 — Mission 03: Debug C++**. Chương này mới nhận diện vấn đề và loại bằng chứng cần có.

### Đáp án mở đầu — Chọn thẻ để học, không chọn giọng nói tự tin

**Nên bắt đầu học với Thẻ A**, vì nó giữ đúng yêu cầu gợi ý một bước. Thẻ C dùng để đối chiếu sau khi tự sửa: nó sửa đúng, nói rõ chưa chạy nhưng tiết lộ nhiều hơn Minh yêu cầu. Loại Thẻ B: `i <= n` cho phép chỉ số `n` ngoài danh sách; truy cập đó trong C++ dẫn tới hành vi không xác định.

Cận `i < n` duyệt các chỉ số hợp lệ và chặn chỉ số bằng kích thước. Sửa cận **chưa bổ sung toàn bộ kiểm tra dữ liệu**; Minh còn phải giải thích và thử biến thể. Ba thẻ hư cấu không chứng minh thương hiệu nào tốt hơn.

### Model, provider, application và producer: bốn câu hỏi khác nhau

“Mình dùng ChatGPT” thường nêu sản phẩm Minh mở, chưa xác định model. **AI**, trí tuệ nhân tạo, gồm cả nhận diện và phát hiện bất thường. Chương tập trung vào **AI tạo sinh**, tạo văn bản hoặc mã. **LLM**, mô hình ngôn ngữ lớn, thường nằm trong trợ lý; không phải mọi AI đều là chatbot. Khả năng nhận ảnh, âm thanh, tệp tùy model và ứng dụng.

**Model** là mô hình tính toán đã được huấn luyện để xử lý đầu vào và tạo đầu ra. GPT, Claude, Gemini có thể chỉ họ mô hình, chưa phải phiên bản. Tài liệu định danh đáng tin hơn đoán qua văn phong; lời giải mạch lạc không bảo đảm đúng.

**Provider** là bên cung cấp dịch vụ truy cập đến model trong đường đang xét: tiếp nhận, xác thực, áp dụng điều kiện; có thể vận hành trực tiếp hoặc làm trung gian. **Producer** xây dựng, huấn luyện hoặc phát hành model. Hai vai trò có thể cùng tổ chức nhưng không bắt buộc.

**Application** là nơi thao tác: trang chat, ứng dụng điện thoại/máy tính hoặc trợ lý lập trình. Nó tổ chức lịch sử, chọn thông tin, có thể nối công cụ/tìm kiếm và hiển thị bản sửa. **User** đặt mục tiêu, quyết định dữ liệu được phép gửi và kiểm tra phần mình sử dụng.

| Vai trò | Câu hỏi phải trả lời | Cách ghi nếu thiếu bằng chứng |
| --- | --- | --- |
| Model | Thành phần nào tạo đầu ra? Định danh nào được công bố? | Chỉ biết họ model; chưa xác định phiên bản hoặc model từng lượt |
| Provider | Ai cung cấp đường truy cập đến model cho ứng dụng? | Chưa xác định provider của đường truy cập |
| Application | Tôi mở và thao tác ở phần mềm nào? | Ghi tên quan sát được, không suy ra model từ đó |
| Producer | Ai phát triển hoặc phát hành model? | Chưa đủ dữ kiện; không gán cho nhóm viết giao diện |
| User | Ai giao việc và kiểm tra trước khi dùng kết quả? | Minh hoặc Lan trong tình huống này |

![Sơ đồ vai trò model, provider, application và user; mũi tên biểu diễn đường truy cập, không phải quyền sở hữu.](../assets/roles.svg)

*AI MAP — Bản đồ vai trò. Một tổ chức có thể giữ nhiều vai trò; mỗi ô không nhất thiết là một công ty hay máy chủ riêng. Producer là câu hỏi bổ sung về bên phát triển, không phải một tầng bắt buộc trong mọi request.*

Bản nguồn dùng ví dụ **Claude qua Amazon Bedrock**: Anthropic là bên phát triển Claude, AWS cung cấp đường truy cập qua Bedrock trong tình huống đó. Vì vậy, nhãn “hỗ trợ Claude” không tự chứng minh kết nối trực tiếp tới Anthropic. Nguồn chính thức gốc là tài liệu Anthropic và AWS, liệt kê cuối chương. **Mốc bộ nguồn là 29/10/2026; các thông tin dịch vụ chưa được xác minh độc lập trong lần biên tập này, cần tra lại khi áp dụng.**

Tương tự, Gemini có thể được nhắc ở lớp ứng dụng hoặc họ model. “Mở ứng dụng Gemini”, “gọi Gemini API” và “chọn một model thuộc họ Gemini” không đồng nghĩa. Điều quan trọng không phải thuộc hết tên, mà là đặt tên vào đúng vai trò.

### API và key không phải một bộ não tải về máy

**API** là giao diện để các phần mềm giao tiếp theo quy tắc xác định. Trong chat, Minh gõ và gửi. Với API, chương trình chuẩn bị request theo định dạng dịch vụ; request có thể chỉ định model. API không phải model mới và cũng không chỉ dùng cho AI.

**API key** là một dạng thông tin xác thực để dịch vụ nhận biết quyền truy cập; có dịch vụ dùng cơ chế xác thực khác. Có key không có nghĩa sở hữu model, được dùng mọi phiên bản, quota vô hạn hoặc miễn phí. Quyền và hóa đơn còn phụ thuộc tài khoản, dự án và điều kiện dịch vụ.

> **SECURITY ALERT — Khóa không phải dữ liệu thực hành.** Không đưa key thật vào chat, ảnh chụp, nhóm lớp hoặc kho mã công khai. Không nhúng khóa bí mật vào JavaScript phía trình duyệt: mã được gửi đến người dùng có thể bị đọc. ViSinhVien không cần key; đừng tạo bí mật chỉ để hoàn thành bài nhập môn.

Nếu gặp key trong một bài hướng dẫn, hãy dùng placeholder thay vì sao chép khóa thật. Nếu nghi khóa đã lộ, thu hồi hoặc vô hiệu hóa qua dịch vụ trước, rồi kiểm tra mức dùng và xử lý bản sao. Xóa một dòng khỏi tệp mới nhất không làm các bản sao biến mất. Quy trình sự cố đầy đủ nằm ở **Chương 4 · Sử dụng AI có trách nhiệm, mục 4.1 — Hồ sơ 01: Khóa API xuất hiện trên GitHub**.

### Những đường vào AI, không phải những bậc thang danh giá

![Bản đồ các cách truy cập AI qua ứng dụng chat, trợ lý lập trình, chương trình dùng API hoặc mô hình cục bộ; không xếp hạng thương hiệu.](../assets/ecosystem.svg)

*AI MAP — Bản đồ đường truy cập. Chọn đường phù hợp nhiệm vụ và điều kiện, không mặc định API hay agent là cấp học cao hơn chat.*

Một luồng giản lược là **người dùng → ứng dụng chuẩn bị thông tin → provider tiếp nhận → model tạo đầu ra → ứng dụng hiển thị → người dùng kiểm tra**. Hệ thống thực có thể thêm trung gian, công cụ và nhiều lượt. Model chạy cục bộ có thể không cần provider bên ngoài nhận câu hỏi. Ngược lại, ứng dụng cài trên máy vẫn có thể gửi dữ liệu lên đám mây.

Ứng dụng đôi khi được gọi là **wrapper**, phần mềm bao quanh model/API. “Chỉ là cái vỏ” bỏ qua giá trị của việc chọn đúng tệp, giữ phạm vi và cho người học duyệt thay đổi. Nhưng cũng đừng suy mọi wrapper đều đọc được dự án, chạy code hay tìm web. Nếu dùng Qoder, cần phân biệt Qoder IDE, Qoder Desktop và Qoder CLI; tên cùng họ không chứng minh chúng có cùng giao diện, quyền hay quy trình. (Theo tài liệu sản phẩm Qoder; phần này chưa được kiểm chứng độc lập, cần tra lại ở Chương 2, mục 2.1.)

### Cùng câu hỏi không đồng nghĩa cùng đầu vào

Ba thẻ hư cấu không xác định nguyên nhân khác biệt. Trong hệ thống thật, cùng câu gõ có thể kèm lịch sử, tài liệu, chỉ dẫn hoặc công cụ khác. Một nơi làm gia sư, nơi khác ưu tiên sinh mã. Giới hạn đầu ra, cấu hình và tính không tất định cũng ảnh hưởng.

Minh điều tra theo ba bước: **ghi nhãn ứng dụng/chế độ/model → liệt kê context và công cụ → ghi phần chưa biết**. Nhãn “Tự động” chỉ cho phép ghi “chưa xác định model thực sự xử lý lượt này”. Chatbot tự giới thiệu không đủ làm bằng chứng duy nhất. Sang Chương 2, “chế độ” sẽ cụ thể thành Ask (chỉ đọc, trả lời) và Agent (được sửa tệp, chạy lệnh); “context” được gọi là ngữ cảnh.

**Bổ sung biên tập — nhận diện trên giấy.** Ứng dụng GIẢ “Gia sư ViSinhVien” nói dùng Gemini API nhưng không công bố model cụ thể. Điền bốn vai trò; rồi thay mô tả bằng “hỗ trợ Claude”. Điều gì không còn biết được?

### Đáp án nhận diện — Giữ chỗ trống đúng chỗ

Application là Gia sư ViSinhVien; theo mô tả của chính ứng dụng, đường truy cập là Gemini API — nếu đúng là gọi trực tiếp thì provider là Google, nhưng ứng dụng cũng có thể đi qua trung gian, nên ghi “provider theo tự mô tả, chưa xác minh”; biết họ Gemini, chưa biết model cụ thể. Nhóm viết ứng dụng không vì thế là bên huấn luyện model. Nếu chỉ còn “hỗ trợ Claude”, provider và phiên bản đều chưa xác định. Thiếu bằng chứng thì giữ chỗ trống.

## 1.2. BEHIND THE SCENE — Phía sau một câu trả lời

### Prompt là lời giao việc; context là thông tin thực sự nhận được

Lan từng hỏi: “Làm app ví sinh viên chuyên nghiệp”. Câu trả lời HƯ CẤU trong tình huống biên tập đề xuất đăng nhập, máy chủ và đồng bộ thanh toán. Nghe đầy đủ, nhưng sai phạm vi. Minh thì viết “sửa vòng lặp này” mà quên dán code. Cả hai đang mong hệ thống biết những điều chưa gửi.

**Prompt** là yêu cầu hoặc chỉ dẫn đưa cho hệ thống. **Context**, ngữ cảnh của một lượt, gồm thông tin thực sự được nhận: prompt, lịch sử được chọn, tài liệu, code và kết quả công cụ. Theo cách dùng phổ biến, prompt là một phần của context. Tài liệu đang mở trước mắt bạn chưa chắc đã nằm trong context của model.

Hãy sửa cách hỏi theo thứ tự có lý do:

1. **Nêu mục tiêu trước triệu chứng.** “Cộng tất cả khoản hợp lệ” cho biết 42000 có phải sai hay không; riêng “ra 42000” chưa đủ.
2. **Đưa phần nhỏ có liên quan.** Với lỗi cận, cần khai báo dữ liệu, kiểu tổng và vòng lặp; không cần cả ổ đĩa.
3. **Đặt kỳ vọng cạnh hiện tượng.** Ba khoản phải ra 60000, snippet dự đoán ra 42000; nếu chưa chạy, ghi đúng là dự đoán.
4. **Giữ ràng buộc và giới hạn trợ giúp.** Số nguyên VND, tối đa 500 khoản, gợi ý trước; tránh nhận một bản viết lại vượt bài học.
5. **Yêu cầu cách kiểm tra.** Hỏi test và bằng chứng thay vì chỉ yêu cầu “chắc chắn 100%”.

Prompt tốt cần đủ dữ kiện, không cần dài hoặc đầy lời tôn xưng. “Hãy đóng vai chuyên gia hàng đầu” không thay thế code và kết quả mong đợi. Ngược lại, cắt mất hợp đồng để tiết kiệm vài token có thể khiến bạn tốn nhiều lượt sửa sai yêu cầu.

### Brief chung: giúp hai người học giữ cùng một bài

**Brief** là bản mô tả ngắn việc cần làm. Minh và Lan giữ bản hiện hành rồi thay dòng “việc lần này”, thay vì kể lại dự án theo trí nhớ. Đây là mẫu có thể dùng độc lập nếu bạn dán kèm code liên quan:

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

Minh chỉ cần mô hình tiền `vector<long long>` khi học vòng lặp; tên ba khoản trên giấy giúp hiểu ý nghĩa. Bản Web của Lan dùng `Expense{id,title,amount,category}`: `id` phân biệt khoản GIẢ, `title` là tên hiển thị, `amount` là tiền, `category` là nhóm. `id` không phải mã sinh viên. Mảng tiền C++ không tự trở thành mô hình đầy đủ bốn trường của Web.

Liên hệ OOP là phân biệt trách nhiệm dữ liệu, xác thực và tính tổng; không bắt buộc thêm một lớp chỉ để có chữ “hướng đối tượng”. Với DSA, duyệt tổng một lần có thời gian O(n), phần nhớ phụ cho tổng là O(1). Với CSDL, Lan có thể xét thuộc tính và ràng buộc trên giấy. Đổi góc học không cho phép tự đưa máy chủ hay CSDL vào bản Web; minh họa SQLite `:memory:` trong `vi-du/minh-hoa-sqlite.py` (Chương 4, mục 4.8.1) là bài riêng.

### Hợp đồng dữ liệu: bằng chứng bắt đầu trước khi chạy

Một **hợp đồng** nói đầu vào nào được chấp nhận và đầu ra nào được yêu cầu. Ở đây, mỗi khoản tồn tại phải có `amount` nguyên, lớn hơn 0, không quá 1000000000; danh sách có tối đa 500 khoản. Rỗng vẫn hợp lệ vì không có khoản nào vi phạm. Tổng 0 không đồng nghĩa có một khoản chi 0.

Từ hợp đồng, tính được tổng lớn nhất:

```text
500 × 1000000000 = 500000000000 VND
```

C++ cần kiểu chứa được mức đó. Kiểu số nguyên có dấu 32 bit thường gặp chỉ đạt khoảng 2,1 tỷ; không đủ chứa 500 tỷ. Snippet dùng `long long` cho tiền và tổng. Không suy mọi `int` trên mọi hệ thống đều giống nhau; lý do lựa chọn là miền dữ liệu, không phải nhãn “tối ưu” của AI.

Trong JavaScript, `Number` biểu diễn chính xác các số nguyên trong miền **safe integers**, số nguyên an toàn, từ `-9007199254740991` đến `9007199254740991`. Tổng 500000000000 nằm trong miền đó. Từng khoản nguyên và mọi tổng trung gian không vượt trần đang xét nên phù hợp với phép cộng của bài. Vượt miền an toàn thì không còn được bảo đảm biểu diễn riêng từng số nguyên.

Điều này **không** có nghĩa “dùng Number là dữ liệu tự hợp lệ”. `amount` vẫn phải thỏa `Number.isSafeInteger(amount)` như trong `data.js`, lớn hơn 0 và không quá 1000000000. Chuỗi `"7000"` không phải số 7000. Ô nhập Web có thể trả chuỗi; dữ liệu trong `localStorage` cũng được lưu dưới dạng chuỗi, cần phân tích và kiểm tra cấu trúc khi đọc lại. Chỉ kiểm tra ở giao diện không bảo vệ được mọi dữ liệu đã lưu.

Bảng dưới là **kỳ vọng theo hợp đồng, chưa phải kết quả đã chạy**:

| Ca kiểm tra | Dữ liệu hoặc thao tác GIẢ | Kỳ vọng |
| --- | --- | --- |
| Rỗng | Không có khoản nào | Tổng 0 VND |
| Một khoản | 7000 | Tổng 7000 VND |
| Ba khoản mẫu | 35000, 7000, 18000 | Tổng 60000 VND |
| Chạm trần | 500 khoản, mỗi khoản 1000000000 | Tổng 500000000000 VND |
| Sai giá trị | 0, số âm, 1.5 hoặc lớn hơn 1000000000 | Từ chối khoản sai, không âm thầm làm tròn |
| Vượt số lượng | Thêm khoản thứ 501 | Từ chối thêm, giữ danh sách hợp lệ trước đó |

Ba ca đầu kiểm tra một phần hành vi tổng. Ba ca sau yêu cầu cả xác thực dữ liệu. **Đổi cận vòng lặp không tự giải quyết validation.** Nếu snippet chỉ cộng dữ liệu đã hợp lệ, hãy nói giới hạn ấy thay vì tuyên bố nó đáp ứng toàn bộ bảng.

### Token và context window: không phải số từ hay trí nhớ vô hạn

**Token** là đơn vị dữ liệu hệ thống xử lý. Một từ có thể thành nhiều token; dấu câu, khoảng trắng, code, ngôn ngữ và tokenizer đều ảnh hưởng. Không có quy tắc “một từ tiếng Việt bằng một token”. Đếm khoảng trắng của sách không tính được hóa đơn.

![Các khối dữ liệu minh họa token và vùng context hữu hạn; cách chia khối không phải kết quả của tokenizer thật.](../assets/token-context.svg)

*BEHIND THE SCENE — Khối chỉ minh họa chia/chọn thông tin, không tính token thật. Context không phải toàn bộ ổ đĩa.*

**Context window** giới hạn lượng thông tin xử lý trong một lần theo dịch vụ; thường còn có giới hạn đầu ra riêng. Cửa sổ lớn không bảo đảm sử dụng chính xác mọi chi tiết hoặc cho phép gửi vô hạn.

Lan dán lịch sử có cả yêu cầu backend đã bỏ và nhiều log thừa. Brief hiện hành bị chìm. Hội thoại dài còn có thể bị ứng dụng cắt, tóm tắt hoặc chọn lại; “đã nói từ đầu” chưa bảo đảm còn nguyên trong context.

Hãy giữ brief hiện hành, hàm liên quan, dữ liệu GIẢ và ghi phần thay đổi. Model không tự biết tệp vừa sửa nếu chưa nhận bản mới. Trợ lý được quyền đọc dự án có thể lấy thêm nội dung; cần kiểm quyền và tệp thực sự được dùng, không đoán qua giao diện.

**Bổ sung biên tập — chọn context.** Với lỗi 42000, chọn giữa brief, hàm tổng, ba khoản GIẢ, sao kê thật và bài giảng không liên quan. Giải thích một phần phải loại.

### Đáp án chọn context — Đủ để kiểm tra, không đủ để lộ dữ liệu

Chọn brief, hàm cùng khai báo cần hiểu và ba khoản GIẢ. Loại sao kê vì riêng tư, bài giảng vì gây nhiễu. Thiếu kiểu dữ liệu hoặc đoạn gọi hàm thì bổ sung đúng phần đó, không gửi cả ổ đĩa.

### Training, inference và web search: ba việc không thay thế nhau

**Training**, huấn luyện, dùng dữ liệu và thuật toán để điều chỉnh tham số model. **Inference**, suy luận theo nghĩa vận hành ở đây, dùng model đã có để tạo đầu ra từ đầu vào. Minh gửi ba khoản thì hệ thống có thể dùng chúng trong context; điều đó không tự chứng minh model vừa được huấn luyện lại và sẽ nhớ ba khoản ấy cho mọi người dùng.

Nhưng “không huấn luyện lại ngay” cũng không đồng nghĩa “không lưu dữ liệu”. Lịch sử chat, bộ nhớ của ứng dụng, log vận hành và việc dùng nội dung để cải thiện dịch vụ là các vấn đề khác nhau. Cần đọc chính sách và cài đặt đúng sản phẩm. Không dùng hiểu biết về inference để thay cho kiểm tra quyền riêng tư.

**Web search** là truy xuất thông tin qua công cụ kết nối web, nếu sản phẩm có và lượt đó dùng nó. Hỏi “ưu đãi hôm nay là gì?” không tự bật tìm web. Câu trả lời có thể dựa vào kiến thức cũ. Ngược lại, có tìm kiếm cũng chưa bảo đảm nguồn phù hợp hoặc tóm tắt đúng.

Với ba khoản tiền, phép cộng và kiểm tra code là căn cứ phù hợp. Với tuổi được sử dụng dịch vụ, cần điều khoản chính thức còn áp dụng. Minh không cần tìm web để cộng 60000; Lan không được dùng phép suy luận nghe hợp lý để thay cho điều kiện ưu đãi.

### Hallucination và trích dẫn: chuyển sự tự tin thành câu hỏi kiểm chứng

**Hallucination**, thường gọi ảo giác AI, là nội dung sai hoặc không có căn cứ được trình bày như đúng. Ví dụ HƯ CẤU: “JavaScript tự lưu mọi biến vào localStorage”, một hàm C++ không tồn tại, hoặc lời “đã chạy test” khi chỉ đọc văn bản. Tên gọi này không giải thích mọi nguyên nhân lỗi, nhưng nhắc ta không coi câu chữ là bằng chứng.

Thay vì yêu cầu “đừng sai”, Minh hỏi chỉ số nào được duyệt, ca một khoản cho gì, và câu nào là dự đoán. Lan hỏi tệp nào ghi lưu trữ, khi nào đọc lại và JSON hỏng được xử lý ra sao. Nếu công cụ nói đã chạy, cần lệnh, dữ liệu, đầu ra, môi trường và khả năng đối chiếu. Một vài test qua vẫn không chứng minh đúng mọi đầu vào; test logic JavaScript không tự kiểm chứng DOM hay lưu/nạp trên trình duyệt.

Với trích dẫn, làm lần lượt: **khoanh claim → mở nguồn → tìm đoạn hỗ trợ → kiểm phạm vi và ngày → ghi giới hạn**. Liên kết có thật chưa chắc hỗ trợ kết luận. “Đủ điều kiện nộp hồ sơ” khác “chắc chắn được duyệt”; điều khoản API khác điều khoản ứng dụng chat. Ngày truy cập không phải ngày phát hành. Không tìm được căn cứ thì ghi **chưa xác minh**, không bù bằng một đoạn giải thích tự tin hơn.

## 1.3. AI WALLET — Hiểu túi tiền trước khi bấm gửi

### Ba hình thức dùng, ba cách đọc quyền lợi

Minh thấy nút nâng cấp; Lan nghe “API rẻ hơn”. Trước khi so tiền, hai bạn cần biết đang so cái gì. Một sản phẩm miễn phí đủ giúp hiểu vòng lặp có thể là lựa chọn tốt hơn cả hai phương án trả tiền.

| Hình thức | Cách hiểu nhập môn | Câu hỏi trước khi dùng |
| --- | --- | --- |
| Free | Một phạm vi dùng không thu tiền theo điều kiện | Model, tính năng, quota, dữ liệu và điều kiện tài khoản nào? |
| Subscription — thuê bao | Trả định kỳ cho quyền lợi của một gói/sản phẩm | Bao gồm gì, giới hạn gì, gia hạn khi nào, khoản nào ngoài gói? |
| API pay-as-you-go | Chương trình gọi dịch vụ, phí theo lượng dùng và bảng giá | Đơn vị input/output, công cụ, xác thực và giới hạn chi phí nào? |

**Quota** là hạn mức có đơn vị và chu kỳ: số lượt, tốc độ hoặc lượng dùng không thể đọc lẫn nhau. Free không có nghĩa vô hạn; trả tiền cũng không bảo đảm mọi yêu cầu được phục vụ không giới hạn.

Quyền dùng ứng dụng và API phải được kiểm tra riêng. Đừng lấy biên lai thuê bao chat làm bằng chứng đã trả mọi API. Cũng không khẳng định “thuê bao không bao giờ có API”: bản nguồn dẫn tài liệu OpenAI về credit ChatGPT/API như một ngoại lệ cần đọc theo gói đủ điều kiện. **Credit** là giá trị hoặc lượng dùng được cấp, có thể có thời hạn và phạm vi. Claim về gói tích hợp này mang mốc nguồn **29/10/2026, chưa xác minh độc lập ở lần biên tập này; cần tra lại**, không phải lời hứa quyền lợi hiện hành.

### Bài toán GIẢ ĐỊNH: tách input khỏi output

Lan muốn dự toán 50 request. **Request** là một yêu cầu gửi đến dịch vụ; một lần bấm của người dùng có thể dẫn đến nhiều request phía sau. Ta cố định kích thước và đơn giá để học phép tính, không mô tả hóa đơn của một hãng.

**Toàn bộ giá, tỷ giá và lượng dùng dưới đây là GIẢ ĐỊNH.** Không dùng chúng để mua dịch vụ hoặc dự đoán giá thật. Chưa có phí riêng của công cụ, cache, lưu trữ hay cơ chế xử lý đặc thù.

| Đại lượng | Giá trị GIẢ ĐỊNH |
| --- | ---: |
| Input mỗi request | 20000 token |
| Output mỗi request | 5000 token |
| Số request ban đầu | 50 |
| Giá input | 0.30 USD / 1000000 token |
| Giá output | 2.50 USD / 1000000 token |
| Tỷ giá | 25000 VND / USD |

Trước khi xem đáp án, viết sáu dòng: tổng input, tổng output, tiền input, tiền output, tổng USD, tổng VND. Giữ đơn vị ở từng dòng. Phải chia cho một triệu vì đơn giá được niêm yết theo triệu token, không phải theo một token hoặc nghìn token.

```text
Tổng input  = input mỗi request × số request
Tổng output = output mỗi request × số request
Tiền input  = tổng input / 1000000 × giá input
Tiền output = tổng output / 1000000 × giá output
Tổng USD    = tiền input + tiền output
Tổng VND    = tổng USD × tỷ giá giả định
```

### Đáp án AI WALLET — 50 request và kiểm tra chéo

| Bước | Phép tính | Kết quả |
| --- | --- | ---: |
| Gom input | 20000 × 50 | 1000000 token |
| Gom output | 5000 × 50 | 250000 token |
| Tính tiền input | 1000000 / 1000000 × 0.30 | 0.30 USD |
| Tính tiền output | 250000 / 1000000 × 2.50 | 0.625 USD |
| Cộng hai khoản | 0.30 + 0.625 | 0.925 USD |
| Quy đổi sau cùng | 0.925 × 25000 | 23125 VND |

Kết quả là **0.925 USD = 23125 VND, chưa phí**. Không làm tròn 0.925 thành 0.93 ở giữa rồi gọi con số VND sau đó là kết quả chính xác. Thuế, chênh lệch tỷ giá thanh toán, phí ngân hàng và các dịch vụ tính riêng nếu có chưa nằm trong mô hình.

Kiểm tra theo mỗi request: input là `20000 / 1000000 × 0.30 = 0.006 USD`; output là `5000 / 1000000 × 2.50 = 0.0125 USD`. Một request tốn `0.0185 USD`; nhân 50 cũng được `0.925 USD`. Hai hướng tính trùng nhau giúp phát hiện nhầm triệu với nghìn.

Output ít token hơn nhưng đắt hơn ở bài này vì đơn giá output cao hơn. Không gộp 1250000 token rồi nhân một giá chung. Tiền phụ thuộc cả lượng và đơn giá của từng loại, không chỉ tổng số token.

### Từ 50 lên 1000 request: con số nhỏ có thể đổi nghĩa

Giữ nguyên tất cả giả định, tăng số request từ 50 lên 1000, tức tăng **20 lần**, không phải 1000 lần. Tổng input thành 20000000 token; output thành 5000000 token. Tiền input là 6.00 USD, output là 12.50 USD.

```text
1000 request × 0.0185 USD = 18.50 USD
0.925 USD × 20           = 18.50 USD
18.50 USD × 25000        = 462500 VND, chưa phí
```

Như vậy, với `20000/5000` token input/output mỗi request, **×50 cho 0.925 USD = 23125 VND**, còn **×1000 cho 18.50 USD = 462500 VND**. Tính tuyến tính đúng vì ta giữ đơn giá và cơ cấu cố định. Dịch vụ thật có thể đổi bậc giá, model, chế độ hoặc phí công cụ; khi đó phải lập lại bảng.

Để so sánh, một **thuê bao GIẢ ĐỊNH 20 USD/tháng** tương đương **500000 VND/tháng** theo cùng tỷ giá. Chưa thể kết luận API tương đương nhưng rẻ hơn: quota, tính năng và điều kiện có thể khác. Nếu Minh không cần mua thuê bao, chi tiền cho API không tự trở thành “tiết kiệm”. Phương án 0 VND phải có mặt trong bảng lựa chọn.

### Những token không nằm trong câu bạn vừa gõ

Lan tưởng input chỉ là “sửa hàm tổng”. Ứng dụng có thể gửi thêm brief, lịch sử, tệp và **tool output**, kết quả công cụ như log test, vào lượt kế tiếp. Lịch sử đã gửi không mặc định miễn phí; cache và lưu phiên có cách tính riêng.

Một số model ghi nhận/tính phí **reasoning token**, token xử lý suy luận. Cách tính vào usage, output hoặc giới hạn tùy model/provider, không tự nằm trong ví dụ này. Dự toán thật cần bộ đếm/ước tính phù hợp rồi đối chiếu usage khi được phép dùng, không dựa vào đếm từ.

**Agent** có thể đọc mã → sửa → test → đọc lỗi → lặp lại. “Sửa cho xong” có thể sinh nhiều request. Lan giới hạn một hàm, một đề xuất, đầu ra đủ kiểm tra và điểm dừng để xem lại. Khi bắt đầu lượt mới, cô dùng brief cập nhật, không bỏ ràng buộc để tiết kiệm.

### Budget alert không phải hard cap

**Budget alert** thông báo đạt ngưỡng; **hard cap** phải có cơ chế chặn dùng/chi theo phạm vi dịch vụ định nghĩa. Email ở 80% không chứng minh dừng ở 100%; số ghi trong ô “budget” không tự là cầu dao.

Bản nguồn dẫn Gemini API billing và Google Cloud Budgets, **mốc 29/10/2026, chưa xác minh độc lập, cần tra lại**. Không mặc định mọi dịch vụ có cùng nút/cơ chế. Kể cả cap được hỗ trợ, độ trễ, request đang xử lý và ngoại lệ có thể ảnh hưởng mức vượt.

Chưa hiểu thì chưa bật thanh toán. Nếu sau này được phép dùng, cần biết nơi xem usage, quota/giới hạn thực có, số bước agent, cách dừng và xử lý khóa. Prompt “đừng tiêu quá” không thay cơ chế tài khoản. Bài này tính trên giấy, không bật thanh toán để thử cảnh báo.

## 1.4. FREE FIRST — Học trước, chỉ mua khi biết mình thiếu gì

### Quyền không mua là một phần của kế hoạch

Nhìn thẻ A, Minh thấy mình cần giấy, kiến thức vòng lặp và có thể trình biên dịch sẵn có, chưa cần agent sửa kho mã. Lan cũng học được Web cục bộ không tích hợp AI. **Free first** ưu tiên phương án không thu phí đủ dùng, không bỏ qua điều kiện dịch vụ.

Hết quota thì chia nhỏ câu hỏi, chờ chu kỳ sau, đọc tài liệu hoặc nhờ bạn. Không lách giới hạn bằng nhiều tài khoản, dùng key nhặt được hay thử thanh toán vì tò mò. Chưa có công cụ hợp lệ thì luyện bằng thẻ HƯ CẤU.

Trước nâng cấp, điền: “Tôi thiếu ______; gói giải quyết bằng ______; tôi đo lợi ích qua ______”. Chưa điền được thì chưa có lý do rõ để mua. Trích vài trang đôi khi đủ thay việc mua context lớn.

> **Quyền không mua.** Khả năng trả tiền không đo năng lực CNTT. Đây không phải chuẩn đầu ra, yêu cầu chi tiêu hay quy định TLU. Ngân sách AI bằng 0 vẫn hợp lệ.

### 300000 VND cho 15 tuần: trần kế hoạch, không phải cap kỹ thuật

Lan thử một kế hoạch **GIẢ ĐỊNH 300000 VND cho học kỳ 15 tuần**. Đây không phải khuyến nghị mức chi cho mọi sinh viên. Mục đích là thấy một quyết định hàng tháng có thể vượt kế hoạch cả kỳ.

| Giai đoạn GIẢ ĐỊNH | Dự trù | Điều kiện để quyết định |
| --- | ---: | --- |
| Tuần 1–5: học nền tảng | 0 VND | Tài liệu và công cụ miễn phí hợp lệ đủ dùng |
| Tuần 6–10: một nhu cầu rõ | Tối đa 100000 VND | Có lợi ích đo được, đủ điều kiện dùng |
| Tuần 11–15: hoàn thiện bài | Tối đa 100000 VND | Đánh giá lại nhu cầu, không gia hạn theo quán tính |
| Dự phòng | 100000 VND | Có thể giữ nguyên, không phải mục tiêu phải tiêu hết |
| Tổng trần cá nhân | 300000 VND | Kế hoạch trên giấy, không chặn hóa đơn tự động |

Thuê bao giả định 500000 VND/tháng vượt cả kế hoạch; nếu 1000 request dồn trong cùng học kỳ, 462500 VND chưa phí cũng vượt trần 300000 VND. Mức 23125 VND ban đầu chưa chứng minh Lan cần API, đủ tuổi hay quản lý khóa được.

Trước chi, ghi nhiệm vụ, phương án miễn phí đã thử, trần tiền và ngày đánh giá lại. Biết ngày/cách dừng tự gia hạn **trước khi mua**, không giả định nút hủy giống nhau. Sau một tuần, đo lỗi đã hiểu hoặc thao tác tiết kiệm, không đếm câu AI sinh.

**Bổ sung biên tập — cuối tuần thứ năm.** Lan chưa thấy chức năng cần trả tiền. Giữ 100000 VND hay mua để “tạo động lực”? Ghi tiêu chí đánh giá lại.

### Đáp án kế hoạch — Tiền chưa tiêu không phải phần học bị thiếu

Giữ dự trù; đánh giá lại sau khi làm Đề B (mục 1.5) bằng context đủ dùng, giữ phạm vi và khả năng tự kiểm. Chỉ mua nếu giải quyết hạn chế thật, đủ điều kiện, trong ngân sách. Không cần tiêu hết dự phòng.

### Ưu đãi sinh viên: đủ điều kiện nộp không có nghĩa chắc chắn nhận

Bản nguồn dẫn hướng dẫn GitHub Education với các điều kiện như đang theo học thuộc diện đủ điều kiện, có tài khoản cá nhân, chứng minh tình trạng sinh viên và **từ 13 tuổi**. Bản nguồn cũng ghi quyền lợi GitHub Pro và Copilot Student cho người học đã xác minh theo điều kiện. **Đây là nội dung được ghi nhận theo bộ nguồn ngày 29/10/2026, chưa được kiểm chứng độc lập trong lần biên tập này; tên gói, tuổi, quyền lợi và điều kiện phải tra lại.**

Không dùng một hướng dẫn cũ để tự đổi tên thành “Copilot Pro hiện tại”, không chốt quota từ trí nhớ. **Completion** là gợi ý hoàn thành mã; **chat** là trao đổi; **agent** có thể tổ chức nhiều bước. Quyền lợi ở một hình thức không bảo đảm mọi hình thức dùng đều vô hạn. Chương trình ưu đãi có thể gồm nhiều bên với điều khoản riêng, không mặc định cấp API key miễn phí cho mọi dịch vụ.

Để đọc một ưu đãi, Lan tách năm câu hỏi: ai đủ điều kiện; cần bằng chứng nào; quyền lợi cụ thể là gì; kéo dài bao lâu; hết ưu đãi hoặc đến kỳ gia hạn thì điều gì xảy ra. Email trường có thể hỗ trợ chứng minh, không phải vé tự được duyệt. Email TLU không tự bảo đảm hồ sơ thành công.

Bài tập chỉ yêu cầu đọc thông tin, không nộp hồ sơ hoặc tải giấy tờ. Nếu sau này đăng ký, dùng quy trình chính thức và chỉ cung cấp giấy tờ cần thiết ở đúng nơi. Không gửi giấy tờ vào chatbot hoặc nhóm lớp để “nhờ duyệt hộ”.

### Tuổi, dữ liệu và tài khoản phải được xét trước giá

Điều kiện tuổi của một chương trình không áp dụng tự động cho chương trình khác. Bản nguồn ghi điều khoản Gemini API yêu cầu **18 tuổi trở lên** với Gemini API và Google AI Studio. **Claim này mang mốc nguồn 29/10/2026, chưa xác minh độc lập; cần đọc lại điều khoản chính thức trước khi dùng.** Không suy từ mốc 13 của một chương trình giáo dục rằng đủ điều kiện dùng mọi API. Khi chưa đáp ứng hoặc chưa rõ điều kiện, chọn bài trên giấy, không tìm cách vượt giới hạn.

Cũng theo nội dung bản nguồn dẫn điều khoản Gemini API ở mốc đó, dịch vụ unpaid thuộc phạm vi áp dụng có thể dùng nội dung để cải thiện sản phẩm và có người xem xét; paid có nhiều trường hợp không dùng nội dung để cải thiện nhưng có thể tồn tại chương trình/tier đóng góp dữ liệu. **Các chi tiết này chưa xác minh độc lập và không được trình bày như cam kết hiện hành.** Bài học bền vững là phải xem đúng sản phẩm, cấp dịch vụ, lựa chọn dữ liệu và ngoại lệ.

Không lấy điều khoản API gán nguyên cho ứng dụng chat. Không rút thành “trả phí là riêng tư tuyệt đối”, “không training là không lưu” hoặc “mọi provider giống nhau”. Với ViSinhVien, chỉ dùng ba khoản GIẢ; không có lý do đưa sao kê, số tài khoản hoặc lịch sử chi tiêu thật lên AI. `localStorage` cũng không phải kho bí mật hay sao lưu chắc chắn: dữ liệu có thể mất khi xóa dữ liệu trình duyệt, không tự đồng bộ thiết bị hoặc tạo đăng nhập.

Nếu dùng dịch vụ, cần tài khoản hợp lệ, mật khẩu riêng và xác thực nhiều yếu tố khi được hỗ trợ. Không mua tài khoản lậu hoặc chia sẻ thuê bao/key mà bỏ qua điều khoản và quyền riêng tư. Người bán hoặc người dùng chung có thể đọc lịch sử, thu hồi quyền, làm phát sinh phí. Giá rẻ không bù được việc mất kiểm soát; điều kiện sử dụng phải được kiểm tra trước phép so sánh giá.

## 1.5. AI TOOL BATTLE — Đối chiếu công cụ theo việc, không theo danh tiếng

### Ma trận tác vụ: “hợp việc nào?” đứng trước “mạnh nhất?”

Minh thích thẻ A vì được tự suy nghĩ; Lan thích công cụ có thể chỉ đúng tệp liên quan. Không có mâu thuẫn: hai người đang ưu tiên tác vụ khác nhau. Giỏi dịch không tự chứng minh giỏi kiểm tra code; viết mã nhanh không chứng minh biết chính sách mới.

Năm lăng kính để chọn là **provenance** — nguồn gốc/căn cứ; **test** — cách kiểm tra; **context** — thông tin cần nhận; **privacy** — điều kiện dữ liệu; **cost** — tổng chi phí. “Bằng chứng” của debug có thể là dòng code và test; “bằng chứng” của tuổi dùng dịch vụ phải là điều khoản đúng phạm vi.

| Tác vụ | Context cần có | Provenance và test | Privacy và cost |
| --- | --- | --- | --- |
| Suy luận logic | Code, chỉ số, mục tiêu cộng mọi khoản của Minh | Bám cận vòng lặp; tự xét rỗng, một khoản, ba khoản | Dữ liệu GIẢ; gợi ý ngắn trên phương án free phù hợp |
| Code hoặc refactor | Brief, hàm liên quan, cấu trúc Expense của Lan | Đọc thay đổi; kiểm mẫu, biên và dữ liệu sai; không thêm backend | Không key; xem quyền đọc tệp, số bước và phí lặp |
| Đọc tài liệu dài | Đặc tả và đoạn ghi chú được phép | Trích đúng đoạn, tìm mâu thuẫn, so brief hiện hành | Không gửi tài liệu hạn chế; trích đoạn trước khi mua context lớn |
| Dịch và diễn giải | Đoạn lỗi/tài liệu, trình độ người học | Giữ tên API, số liệu và phủ định; không đổi số nguyên thành số thực | Loại thông tin riêng; không cần agent nhiều bước |
| Tìm thông tin mới | Câu hỏi về ưu đãi/giá, đúng sản phẩm và phạm vi | Nguồn chính thức hiện hành, đoạn hỗ trợ, ngày truy cập | Không gửi giấy tờ; xét phí tìm kiếm nếu có |

Ma trận không xếp hạng sản phẩm thật. Không có web thì không dùng làm nguồn duy nhất cho chính sách hiện tại. Không chạy code vẫn có thể gợi ý, nhưng cần kiểm thử ở nơi khác. Chọn công cụ có phần việc mình kiểm chứng được, thay vì giao hết chỉ vì nó nhận làm.

### Benchmark A–C: chuẩn bị một phép thử công bằng vừa đủ

**Benchmark** là phép thử có kiểm soát để so mức phù hợp. Ba đề kế thừa nguồn, **không có điểm sản phẩm điền sẵn**. Không có công cụ được phép dùng thì phân tích trên giấy, ghi là luyện đánh giá, không phải benchmark thực.

Giữ cùng brief, code, dữ liệu, đầu ra và giới hạn trợ giúp; nên mở trao đổi mới để giảm ảnh hưởng lịch sử. Ghi ứng dụng, nhãn model/chưa xác định, chế độ, ngày, tính năng bật. Khác biệt web/chạy code phải được ghi riêng, không quy tất cả cho model.

Làm theo thứ tự **gửi đề → giữ nguyên câu trả lời → tự kiểm → chấm → ghi hỏi bổ sung và giới hạn kết luận**. Có điều kiện thì thử lại vì đầu ra có thể đổi. Vài đề không chứng minh “tốt nhất cho mọi người”.

### Đề A — Giải thích logic C++ cho Minh

Dán **nguyên snippet đầu chương và brief mục 1.2**; chữ “xem đầu chương” không tự gửi tài liệu cho ứng dụng.

```text
Với snippet C++ đính kèm, hãy gợi ý một bước trước khi nêu cách sửa.
Sau đó giải thích bằng chỉ số vì sao tổng ba khoản GIẢ bị thiếu.
Nêu kết quả mong đợi sau sửa cho: rỗng; một khoản 7000;
ba khoản 35000, 7000, 18000. Không truy cập quá danh sách.
Phân biệt dự đoán với kết quả đã chạy; chưa viết lại toàn bộ bài.
```

Chấm cả độ đúng và cách giúp học: viết ngay toàn bài có thể đúng kết quả nhưng sai mức trợ giúp. Lời “đã chạy” cần bằng chứng.

### Đề B — Refactor Web mà không đổi sản phẩm

Dùng brief và **bản rút gọn cho đề bài** dưới đây, chỉ cộng khi đầu vào hợp lệ. Không khẳng định demo `data.js` thiếu kiểm tra; không thay snippet vào demo đúng.

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

Chấm hợp đồng và hành vi, không thưởng số lớp hoặc tên hàm giống mẫu. Kiểm form rồi tin mọi dữ liệu đọc lại là chưa đủ.

### Đề C — Đọc và kiểm tra nguồn cho Lan

Cung cấp brief và đoạn dữ kiện sau, kèm liên kết để người trả lời biết giới hạn nguồn:

```text
ĐOẠN ĐỐI CHIẾU TỪ BẢN NGUỒN, MỐC 29/10/2026:
GitHub Education yêu cầu đáp ứng điều kiện người học, tài khoản cá nhân
và bằng chứng tình trạng sinh viên; bản nguồn ghi tuổi tối thiểu 13.
Email trường không tự bảo đảm được duyệt. Chưa xác minh độc lập lại.
Nguồn: https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student

Hãy tóm tắt cho Minh, phân biệt đủ điều kiện nộp với chắc chắn được duyệt.
Email TLU có tự bảo đảm ưu đãi không? Đoạn này cho phép kết luận gì
về quyền sử dụng một API khác? Nếu không truy xuất web thực,
chỉ phân tích đoạn được cung cấp, không tuyên bố đã kiểm tin mới.
```

Đề C cố ý có mốc cũ và giới hạn xác minh. Một câu trả lời tốt không “làm mới” tài liệu bằng cách gắn ngày hiện tại. Nếu có truy xuất thật, phải ghi trang đã đọc và claim được hỗ trợ; việc đó là bằng chứng bổ sung, không xóa mốc của đoạn được cung cấp.

### Đáp án benchmark A–C — Chuẩn đối chiếu, không phải kết quả đo

**A:** `i < n - 1` bỏ khoản cuối; sửa thành `i < n`, không dùng `i <= n`. Ba kỳ vọng sau sửa là **0, 7000, 60000**, không phải log. Ca một khoản phơi lộ việc bỏ mất khoản duy nhất; rỗng một mình chưa đủ. Trace/thực thi xem mục 2.3; validation là nhiệm vụ riêng.

**B:** kiểm cấu trúc danh sách, tối đa 500 khoản; từng `amount` thỏa `Number.isSafeInteger`, lớn hơn 0, không quá 1000000000. Kiểm khi thêm và nạp lại; xử lý JSON hỏng có thông báo, không âm thầm mất dữ liệu. Có thể xác thực ở biên hoặc đầu hàm tổng nhưng phải rõ hợp đồng. Không thêm backend/tài khoản/thư viện lớn. Test logic chưa kiểm chứng giao diện/lưu trữ.

**C:** email TLU không bảo đảm duyệt; điều kiện và bằng chứng khác kết quả xét hồ sơ. Đoạn nguồn không chứng minh quyền mọi API hay điều khoản hiện tại. Không truy xuất mới thì giữ mốc gốc, ghi cần tra lại; không suy tuổi sang dịch vụ khác.

### Rubric 10 điểm: dùng sau khi có bằng chứng

**Rubric** là bảng tiêu chí chấm. Chấm từng đề A, B hoặc C theo năm tiêu chí, mỗi tiêu chí 0–2; tổng tối đa **10 điểm cho một đề**. Đây là cách chuyển năm lăng kính thành đánh giá đầu ra, không phải thuật toán xếp hạng công cụ.

| Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
| --- | --- | --- | --- |
| Đúng trọng tâm | Sai bài hoặc sai kết luận chính | Đúng một phần, thiếu quan trọng | Đúng tác vụ và kết quả chính |
| Giữ ràng buộc/context | Bỏ hoặc tự đổi yêu cầu | Giữ phần lớn, cần nhắc | Giữ yêu cầu liên quan, nhận ra dữ kiện thiếu |
| Bằng chứng/provenance | Bịa nguồn, bịa chạy test hoặc không căn cứ | Có căn cứ nhưng chưa rõ/đủ | Suy luận, test hoặc nguồn phù hợp; nêu giới hạn |
| Dễ học và kiểm tra | Khó hiểu, không có cách tự kiểm | Hiểu được một phần | Vừa sức, giúp tự làm bước tiếp |
| An toàn và tiết kiệm | Đòi dữ liệu thật/key hoặc mở rộng tốn kém | Có nhắc nhưng chưa cụ thể | Giữ dữ liệu GIẢ, phạm vi nhỏ, tránh chi phí vô ích |

Một đề nghị đưa key bí mật vào Web phải bị loại khỏi phương án triển khai đến khi sửa, dù tổng điểm khác cao. Điểm không bù được vi phạm điều kiện bắt buộc. Nếu chưa kiểm nguồn hoặc chưa chạy code, ghi phần đó là chưa kiểm, không tự cộng điểm như đã có bằng chứng.

### Phiếu benchmark để trống

| Trường ghi nhận | Kết quả của bạn |
| --- | --- |
| Thử công cụ thật hay luyện đánh giá trên giấy? | ______________________________ |
| Ứng dụng, model công bố, provider biết được, chế độ | ______________________________ |
| Ngày thử, nguồn nhận diện, tính năng bật | ______________________________ |
| Brief, code và dữ liệu dùng chung | ______________________________ |
| Điểm A /10; B /10; C /10 | ______________________________ |
| Căn cứ cho điểm và phần chưa kiểm | ______________________________ |
| Thời gian, số lượt hỏi lại | ______________________________ |
| Chi phí quan sát được hoặc “chưa xác định” | ______________________________ |
| Chọn cho tác vụ nào; không chọn cho tác vụ nào | ______________________________ |

Chỉ chấm khi có bằng chứng; bài trên giấy không là kết quả model. Không phân bổ thuê bao thành giá request tùy tiện. Minh ưu tiên đúng, dễ hiểu, miễn phí hơn nhiều mã không giải thích nổi.

## 1.6. MINI CHALLENGE — 20 phút để nhận diện, ước chi và quyết định

### Chuẩn bị một tờ giấy, không chuẩn bị thẻ thanh toán

Lab kế thừa nguồn, làm cá nhân/theo cặp bằng sách và giấy. Không đăng ký, cài đặt, gọi API, tạo key, tải giấy tờ hay dùng chi tiêu thật; không cần tài khoản AI.

**Tình huống GIẢ ĐỊNH:** Minh cần hiểu lỗi 42000; Lan kiểm Web cục bộ và thông tin ưu đãi. Ứng dụng GIẢ “Trợ lý học ViSinhVien” chỉ công bố “Tự động”, không nêu model từng lượt/provider. Web vẫn HTML, JavaScript, `localStorage`, không backend. Dùng chi phí giả định mục 1.3.

Nộp một phiếu gồm nhận diện, prompt, phép tính và quyết định có điều kiện. Không cần làm hết benchmark A–C trong lab; đây là nhiệm vụ ghép kỹ năng, không phải cuộc thi tốc độ.

### Lịch 20 phút: làm từng bước vì một lý do

**Phút 0–4 — Nhận diện.** Điền application/model/provider, thêm producer nếu biết. Gạch dữ kiện, khoanh điều chưa rõ để tránh đoán model từ giao diện. Quan sát công cụ thật thì chỉ đọc thông tin được phép, ghi nguồn/ngày, không đổi cài đặt.

**Phút 4–8 — Viết prompt.** Đưa mục tiêu, code, hợp đồng, ba khoản và cặp 60000/42000; xin gợi ý trước. Đọc như người chưa biết dự án để phát hiện thiếu context. Gửi nơi khác phải dán snippet thật.

**Phút 8–13 — Ước chi.** Tách input/output cho 50 request, đổi USD/VND, rồi xét 1000 request. Kiểm chéo từng request để bắt lỗi đơn vị; giữ nguyên số giả định để đối chiếu.

**Phút 13–17 — Quyết định.** Dùng ít nhất ba tiêu chí ma trận, có phương án không trả tiền, cách kiểm chứng và điều kiện đánh giá lại. Sở thích không thay thế bằng chứng.

**Phút 17–20 — Đối chiếu.** Sửa phiếu nhưng giữ dấu lỗi ban đầu để nhận ra điều vừa học. Nói trong 30 giây: biết/chưa biết gì, chọn gì, kiểm thế nào, chi tối đa bao nhiêu.

### Worksheet — Điền trước khi mở đáp án

| Ô cần điền | Câu trả lời của bạn |
| --- | --- |
| Ứng dụng đang xét | ________________________________________ |
| Model cụ thể hoặc chế độ được công bố | ________________________________________ |
| Provider của đường truy cập | ________________________________________ |
| Producer, nếu có căn cứ | ________________________________________ |
| Nguồn và ngày quan sát, hoặc “tình huống GIẢ ĐỊNH” | ________________________________________ |
| Điều chưa đủ chứng cứ để kết luận | ________________________________________ |
| Mục tiêu và kết quả đúng của ViSinhVien | ________________________________________ |
| Hiện tượng được đề cho; test đầu tiên | ________________________________________ |
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
| So với kế hoạch 300000 VND, chưa phí | ________________________________________ |

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

### Đáp án MINI CHALLENGE — Một phiếu hoàn chỉnh có điều kiện

**Nhận diện:** ứng dụng Trợ lý học ViSinhVien, chế độ Tự động; model/provider/producer chưa xác định. Nguồn là tình huống GIẢ ĐỊNH, không phải quan sát dịch vụ; không tự ghi ngày truy cập thật.

**Mục tiêu:** cộng mọi khoản hợp lệ; ba khoản GIẢ kỳ vọng 60000, lỗi đề cho 42000. Rỗng tổng 0; thử một khoản 7000 rồi ba khoản để kiểm lỗi bỏ cuối. Không gửi key, giấy tờ, sao kê, tài khoản hoặc dữ liệu cá nhân. Chưa chạy thì ghi kỳ vọng, không báo cáo test.

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

Khi dùng mẫu này, phải dán kèm snippet đầu chương; câu “tôi dán” không tự đính kèm code. Nếu đã chạy thật, có thể thay dòng hiện tượng bằng lệnh và log của chính mình, không mượn kết quả dự đoán làm log.

**Phép tính:** tổng input 1000000 token, output 250000 token; tiền tương ứng 0.30 và 0.625 USD. Tổng **0.925 USD = 23125 VND chưa phí**. Một request **0.0185 USD**, nhân 50 khớp. Với 1000 request: input 20000000 token, output 5000000 token; tiền 6.00 + 12.50 = **18.50 USD = 462500 VND chưa phí**. Mức sau vượt kế hoạch giả định 300000 VND; cảnh báo không tự bảo đảm chặn hóa đơn. Thuê bao giả định 20 USD là 500000 VND/tháng nhưng chưa tương đương quyền lợi API.

**Minh:** dùng giấy/tài liệu hoặc gợi ý miễn phí hợp lệ; tự sửa cận trên bài làm, kiểm rỗng/một/ba khoản ở mục 2.3. Chọn theo context đủ dùng, test kiểm được, cost 0; dữ liệu GIẢ giữ privacy. Không cần API.

**Lan:** giữ Web cục bộ, kiểm đầu vào/tổng rồi kiểm riêng hiển thị/lưu/nạp. Ưu đãi cần nguồn chính thức; chưa truy xuất thì ghi chưa xác minh, chưa mua. Không tự tích hợp API.

**Đánh giá lại** khi free chưa đáp ứng nhu cầu rõ, đã tra quyền lợi/tuổi/dữ liệu, quản lý được chi phí và biết cách dừng gia hạn. Chưa đủ điều kiện hoặc chưa hiểu kiểm soát tiền thì tiếp tục trên giấy/miễn phí. Mức chi hiện tại có thể là 0 VND.

### QUICK CHECK — Sáu câu tự kiểm cuối chương

Trả lời từng câu bằng một kết luận và một lý do. Đừng chỉ nhớ chữ “không”; hãy chỉ ra loại bằng chứng còn thiếu.

1. Nhãn “tích hợp Claude” đã đủ xác định provider và phiên bản chưa?
2. Cùng model nhưng một ứng dụng đề xuất backend cho ViSinhVien: có chắc quảng cáo sai không?
3. Danh sách rỗng có vi phạm `amount > 0` không? Có cần tạo một khoản 0 để biểu diễn rỗng không?
4. Đếm số từ tiếng Việt có đủ tính chính xác hóa đơn token không?
5. Email TLU có bảo đảm ưu đãi sinh viên và quyền dùng mọi API không?
6. Trả phí và bật budget alert đã đủ bảo đảm riêng tư, không vượt ngân sách chưa?

### Đáp án QUICK CHECK — Sáu kết luận và lý do

**1. Chưa.** Cần định danh model và đường truy cập; producer có thể khác provider như ví dụ Claude qua Bedrock. Không đoán qua văn phong.

**2. Chưa thể kết luận quảng cáo sai.** Kiểm brief thực sự gửi, lịch sử, chỉ dẫn, công cụ và cấu hình. Backend sai phạm vi đã chốt, nhưng khác đầu ra chưa chứng minh khác model.

**3. Không vi phạm, không cần khoản 0.** Điều kiện dương áp dụng cho khoản tồn tại. Rỗng có tổng 0; tạo `amount = 0` lại vi phạm hợp đồng.

**4. Không.** Token tùy tokenizer/nội dung; usage có thể gồm lịch sử, code, tool output và khoản tính riêng. Cần bộ đếm phù hợp và báo cáo lượng dùng, không dùng wordcount.

**5. Không.** Còn điều kiện, bằng chứng sinh viên và xét hồ sơ. Tuổi/quyền dùng từng API phải tra riêng; mốc nguồn chưa phải xác nhận hiện hành.

**6. Chưa.** Kiểm chính sách đúng sản phẩm/tier/cài đặt. Budget alert không mặc định là hard cap; cần hiểu cơ chế chặn, phạm vi, độ trễ và request đang xử lý.

### Tự giảng lại trong 7 phút — Bản chuyển thể từ Speaker Notes

Phần này không thay lab 20 phút. Bạn có thể nói cho bạn học hoặc tự ghi âm mà không mở giao diện dịch vụ. Đây là cách giữ nội dung trình bày 5–8 phút của bản nguồn trong hình thức tự học.

| Thời gian | Việc trình bày | Điều cần chứng minh |
| --- | --- | --- |
| 0:00–1:00 | Kể Minh, Lan, ba khoản GIẢ; phân biệt 42000 và 60000 | Tự cộng đúng, biết tổng trung gian chưa tự là lỗi |
| 1:00–2:15 | Vẽ application, provider, model; hỏi thêm producer | Không đồng nhất ứng dụng với model, chấp nhận chưa biết |
| 2:15–3:30 | Sửa prompt thiếu; nhắc hợp đồng và chỉ số cuối | Không đổi thành cận vượt mảng; chưa cần kể lại toàn trace |
| 3:30–4:45 | Tính riêng input/output, 50 rồi 1000 request | Giữ đơn vị, số giả định và nhãn chưa phí |
| 4:45–6:00 | Chọn free first; nhắc tuổi, ưu đãi, gia hạn, dữ liệu | Không biến email trường hoặc trả tiền thành bảo đảm |
| 6:00–7:00 | Hỏi kiểm code bằng gì, cảnh báo có dừng không | Nêu được bằng chứng và điều chưa xác minh |

Có 5 phút thì giảm hỏi đáp, không bỏ nhãn giả định; có 8 phút thì thêm một quyết định có điều kiện. Không trình diễn đăng nhập, thanh toán hoặc giấy tờ để làm bài nói sinh động hơn.

### SKILL UNLOCKED — Bạn mang gì sang chương tiếp theo?

Phiếu hoàn thành cần thể hiện: nhận diện vai trò, chọn context, phân biệt suy luận/thực thi/tìm nguồn, tính input/output và quyết định chi tiêu. Đây là bằng chứng một phiên học, không chứng nhận năng lực lâu dài.

Ba câu mang theo:

- **Biết ứng dụng, đường truy cập và model được công bố; thiếu chứng cứ thì ghi chưa xác định.**
- **Đưa đúng mục tiêu/context, kiểm bằng phép tính, test hoặc nguồn; sự tự tin không phải bằng chứng.**
- **Ưu tiên miễn phí đủ dùng; tính lượng dùng và điều kiện trước trả tiền. Không mua vẫn học nghiêm túc.**

Sang **Chương 2 · Trở thành người điều khiển AI**, Minh làm trace/sửa/test ở mục 2.3; Lan theo dữ liệu Web ở mục 2.4. **Chương 3 · Đừng để AI suy nghĩ thay bạn** giữ phần tự làm; **Chương 4 · Sử dụng AI có trách nhiệm** xét quyền, dữ liệu và trách nhiệm.

### Nguồn chính thức và việc còn phải tra lại

**29/10/2026 là mốc truy cập của bộ nguồn được cung cấp**, không phải ngày phát hành hoặc ngày kiểm tra của lần biên tập này. Chưa xác minh độc lập nội dung hiện hành; cần tra lại model, gói, credit, quota, tuổi, dữ liệu và billing trước khi áp dụng. Giữ nguyên 11 liên kết chính thức gốc:

| Nội dung đối chiếu | Nguồn chính thức |
| --- | --- |
| Họ model, định danh | [Anthropic — Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview) |
| Claude qua provider khác | [AWS — Claude in Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) |
| API, xác thực, chỉ định model | [Google — Gemini API docs](https://ai.google.dev/gemini-api/docs) |
| Lớp ứng dụng Gemini | [Google — Gemini overview](https://gemini.google/overview/) |
| Tuổi, điều kiện, bằng chứng sinh viên | [GitHub — Apply to GitHub Education as a student](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student) |
| Quyền lợi, thời hạn, giới hạn | [GitHub Student Developer Pack](https://education.github.com/pack) |
| Free/paid, đơn vị giá, phụ phí | [Google — Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Tuổi, sản phẩm/tier, xử lý dữ liệu | [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms) |
| Cơ chế kiểm soát mức dùng | [Google — Gemini API billing](https://ai.google.dev/gemini-api/docs/billing) |
| Ngân sách và cảnh báo | [Google Cloud — Budgets](https://cloud.google.com/billing/docs/how-to/budgets) |
| Credit API theo điều kiện gói | [OpenAI — ChatGPT/API credits](https://developers.openai.com/api/docs/guides/chatgpt-api-credits) |

Giá **0.30/2.50 USD mỗi triệu token**, thuê bao **20 USD**, tỷ giá **25000 VND/USD**, ngân sách **300000 VND** đều GIẢ ĐỊNH, không lấy từ bảng giá thật. Thẻ hư cấu không phải benchmark; bảng kỳ vọng không phải log. Kiểm chứng thật phải ghi riêng công cụ/lệnh/nguồn, ngày và kết quả.
