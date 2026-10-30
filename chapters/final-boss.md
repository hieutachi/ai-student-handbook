# DỰ ÁN TỔNG KẾT · XÂY DỰNG, KIỂM THỬ, GIẢI THÍCH

*Build it. Test it. Explain it.*

Năm chương trước đã đi qua năm bước: hiểu vai trò và cách hoạt động của AI (Chương 1), dùng AI có kiểm soát (Chương 2), giữ vững việc học chủ động (Chương 3), sử dụng AI có trách nhiệm (Chương 4) và chọn công cụ phù hợp với nhiệm vụ, rủi ro và ngân sách (Chương 5). Dự án tổng kết ghép cả năm bước thành một sản phẩm nhỏ có bằng chứng kiểm chứng. Dự án không yêu cầu xây dựng một ứng dụng mới vượt quá trình độ sinh viên. Đối tượng thực hành vẫn là ứng dụng mẫu ViSinhVien với dữ liệu giả đã dùng xuyên suốt cuốn sách.

Điều cần luyện ở đây không phải là dùng công cụ AI mạnh nhất, mà là trả lời được ba câu hỏi trọng tâm bằng bằng chứng:

1. Sản phẩm làm gì, và việc gì nằm ngoài phạm vi của nó?
2. Căn cứ nào cho thấy sản phẩm đúng?
3. Khi không mở cửa sổ chat, người học còn tự giải thích được những gì?

Dự án được đặt sau Chương 5 và có ba cấp độ. Cấp Bronze tương ứng với lộ trình C++ của Minh (năm nhất), cấp Silver tương ứng với lộ trình Web của Lan (năm hai), còn cấp Gold bổ sung yêu cầu kiểm soát quy trình giao việc cho Agent. Bản nộp gồm mã nguồn, bảng kiểm thử và lời giải thích. Câu "AI bảo là đúng" không được coi là bằng chứng. Phần nào còn thiếu bằng chứng phải được ghi rõ là thiếu và bổ sung sau, không dùng giao diện đẹp để thay thế.

![Ba lộ trình tổng kết: cấp Bronze tập trung vào C++, cấp Silver theo luồng dữ liệu Web, cấp Gold kiểm soát quy trình làm việc với Agent.](../assets/final-boss.svg)

## 1. Chọn cấp độ theo năng lực cần luyện

Phần này giúp chọn mức độ vừa sức, để dự án luyện đúng điều cần luyện thay vì quá tải.

| Lộ trình | Đối tượng phù hợp | Sản phẩm phải có | Không yêu cầu |
|---|---|---|---|
| Bronze · C++ cơ bản | Sinh viên năm nhất đang học biến, vòng lặp, `vector` | Hàm cộng có kiểm tra đầu vào, hai bản vá, bộ kiểm thử và lời giải thích về chỉ số và kiểu dữ liệu | Web, class Expense, tài khoản AI trả phí |
| Silver · Web có luồng dữ liệu | Sinh viên năm hai đã biết JavaScript và HTML | Sửa hai lỗi logic trong bài biệt lập; kiểm tra lại luồng form → dữ liệu → DOM và cơ chế lưu trữ trên bản demo đúng | Backend, đăng nhập, đồng bộ, ví điện tử |
| Gold · Quy trình Agent có kiểm soát | Người đã hoàn thành cấp Bronze hoặc Silver và muốn luyện kỹ năng giao việc | Toàn bộ sản phẩm của cấp nền, cộng thêm phạm vi quyền, kế hoạch, diff, nhật ký và biên bản nghiệm thu | Thêm framework, thuê máy chủ, mua gói dịch vụ đắt hơn |

Cấp Gold không có nghĩa là viết nhiều mã hơn. Ở cấp này, người học phải chứng minh được rằng Agent không tự mở rộng nhiệm vụ và bản thân người học biết từ chối những thay đổi không có căn cứ. Nếu không có quyền dùng Agent, người học thực hiện bài diễn tập quy trình trên giấy và ghi rõ **mô phỏng, chưa thực thi Agent**; trong trường hợp đó không được nhận là đã đạt phần bằng chứng vận hành Agent thật.

Thời lượng gợi ý: cấp Bronze 60–90 phút; cấp Silver 90–120 phút; cấp Gold cần thêm 30–45 phút cho phần quy trình. Có thể chia thành nhiều phiên làm việc. Thời lượng này chỉ để lập kế hoạch, không phải thước đo tốc độ hay năng lực lâu dài.

## 2. Mười yêu cầu của bản nộp

1. Tự diễn đạt yêu cầu chức năng: phép tính tổng phải làm gì, đầu vào nào bị từ chối, việc gì không thuộc phạm vi.
2. Chọn công cụ có điều kiện và nêu lý do, theo cách đã học ở Chương 5 (mục 5.3 và 5.4): gắn lựa chọn với tác vụ, rủi ro và ngân sách, không theo danh tiếng. Nếu không dùng AI, ghi rõ lựa chọn đó; nếu có dùng, xác nhận rằng phạm vi môn học cho phép.
3. Mô tả cấu trúc dữ liệu: cấp Bronze dùng `vector<long long>`; cấp Silver dùng `Expense(id,title,amount,category)` và mô tả đường đi của trường `amount`.
4. Thực hiện phần triển khai trong phạm vi đã chọn. Ghi rõ phần do AI gợi ý và phần tự viết. Không sửa demo tham khảo để hợp thức hóa đáp án.
5. Sửa tối thiểu hai lỗi gốc trong bộ đề có lỗi chủ đích dưới đây; mỗi lỗi có hiện tượng, nguyên nhân và phản ví dụ riêng.
6. Đọc diff và trả lời: mỗi dòng thay đổi giải quyết yêu cầu nào; có tệp, phụ thuộc hoặc quyền nào tăng thêm hay không.
7. Chạy kiểm thử với kỳ vọng được xác định độc lập; giữ lại cả lần chạy thất bại và lần chạy lại, không chỉ chụp màn hình kết quả đạt cuối cùng.
8. Rà soát dữ liệu cá nhân, khóa API, thư viện, giấy phép và ngữ cảnh hiển thị. Không dùng dữ liệu thật để bài làm "trông thực tế".
9. Khai báo đúng mức độ hỗ trợ của AI theo mẫu trong [Thỏa thuận học tập](learning-agreement.md) và hướng dẫn của môn học.
10. Giải thích sản phẩm, trả lời một câu hỏi biến thể mà không dùng AI và nêu các giới hạn chưa được kiểm chứng.

**Hợp đồng dữ liệu chung.** Dữ liệu giả gồm ba khoản 35000 + 7000 + 18000 = 60000. Mỗi khoản tiền là số nguyên VND từ 1 đến 1000000000; danh sách có tối đa 500 khoản; danh sách rỗng cho tổng bằng 0; tổng cực đại là 500000000000. Kiểu số nguyên trong bài C++ không phải là bộ phân tích (parser) hoàn chỉnh cho mọi chuỗi gõ từ bàn phím. Ví dụ SQLite minh họa riêng không phải là backend và không áp dụng đầy đủ hợp đồng danh sách này.

## 3. Chuẩn bị thư mục bài làm

Mở thư mục gốc **AI-Student-Handbook** trong trình soạn thảo. Dùng trình quản lý tệp để tạo thư mục `bai-lam/final-boss`, sau đó sao chép các tệp cần thiết từ `vi-du/final-boss` vào đó. Không chạy lệnh sao chép khi chưa xác định rõ thư mục đích; ở bước này, thao tác bằng giao diện là đủ. Mọi chỉnh sửa thực hiện trên bản sao, không ghi đè lên ví dụ gốc.

| Tệp đề | Vai trò | Trạng thái ban đầu |
|---|---|---|
| [bronze.cpp](../vi-du/final-boss/bronze.cpp) | Chương trình C++ có hai lỗi gốc và 9 ca kiểm thử | Có lỗi chủ đích, chưa thể đạt toàn bộ kiểm thử |
| [silver.cjs](../vi-du/final-boss/silver.cjs) | Hai hàm JavaScript chứa hai lỗi gốc | Có lỗi chủ đích; không gắn vào demo Web |
| [test_silver.cjs](../vi-du/final-boss/test_silver.cjs) | 12 ca kiểm thử riêng cho đề cấp Silver | Không sửa đáp án kiểm thử để mã vượt qua |

Bộ đề này **khác** với các demo tham khảo `vi-du/nam-1-cpp/vi_sinh_vien.cpp` (9 ca kiểm thử) và `vi-du/nam-2-web/test_data.cjs` (34 ca, trong đó có ca kiểm thử hồi quy cho kiểu của trường `category`). Cần phân biệt rõ ba con số này, không dùng lẫn. Tệp `loi-bo-sot.cpp` trong Bài thực hành 03 (mục 2.3) chỉ có một lỗi cận vòng lặp và không có chế độ `--test`; tệp này không phải là đề của dự án tổng kết.

Tạo tệp ghi chép `ghi-chep.txt` trong thư mục bài làm. Nội dung tối thiểu gồm: điểm xuất phát, phạm vi, hai lỗi đang xét, kết quả kiểm thử mong đợi, các lệnh đã chạy, kết quả thực tế, phần được AI hỗ trợ và những điểm chưa biết. Không lưu khóa API hoặc dữ liệu riêng tư trong tệp ghi chép.

## 4. Cấp Bronze: một vòng lặp, hai quyết định sai

**Bối cảnh.** Người viết chương trình đã biết phải kiểm tra đầu vào, nhưng chương trình vẫn cộng thiếu tiền và từ chối một khoản hợp lệ nằm sát giới hạn. Hai lỗi nằm ở hai quyết định khác nhau; tính đúng tổng mẫu không có nghĩa là lỗi thứ hai đã biến mất.

### Dự đoán trước lần chạy đầu (Think First)

Đọc `bronze.cpp` trong bản sao, chưa mở đáp án. Ghi kết quả mong đợi cho các trường hợp: ba khoản, danh sách rỗng, một khoản 7000, một khoản 1000000000, 500 khoản ở mức tối đa, khoản 0, khoản -1, khoản 1000000001 và danh sách 501 khoản. Với các ca phải bị từ chối, kết quả mong đợi là chương trình từ chối, không phải một giá trị tổng.

Lần theo (trace) riêng vòng lặp cộng, sau đó mới đọc vòng lặp kiểm tra miền giá trị. Không gộp hai vòng thành một nhận định mơ hồ như "đoạn mã xử lý số tiền". Cần trả lời được hai câu hỏi: điều kiện nào quyết định giá trị biên lớn nhất có được chấp nhận hay không, và điều kiện nào quyết định lượt cuối có được cộng hay không.

**Cách đọc bộ chạy kiểm thử.** `check(tên, đầu_vào, tổng_kỳ_vọng, từ_chối)` là một hàm nhỏ dùng để đối chiếu kết quả. Khi đối số cuối là `true`, kiểm thử chờ hàm phát sinh ngoại lệ `std::invalid_argument`; khi đó số `0` ở vị trí trước không phải là tổng cần trả về. Ví dụ, `check("tu choi 0", {0}, 0, true)` yêu cầu **từ chối khoản 0**, chứ không chấp nhận khoản đó rồi cộng ra 0. Nếu bỏ đối số cuối, giá trị mặc định là `false` và kiểm thử chờ một tổng hợp lệ. Lambda là cách khai báo hàm hỗ trợ ngay bên trong `main`. Người học chưa cần tự viết lại bộ chạy này; chỉ cần sửa `totalExpenses` và, khi đã hiểu, thêm một lời gọi `check` theo mẫu.

### Biên dịch và chạy đúng bản sao

Các lệnh sau chạy từ **thư mục gốc AI-Student-Handbook**, không chạy từ bên trong `bai-lam/final-boss`. Cần trình biên dịch `g++` hỗ trợ C++17. Nếu không có trình biên dịch, thực hiện trace trên giấy và ghi rõ là chưa chạy; không tự cài phần mềm lên máy phòng thực hành khi chưa được phép.

Bash trên Linux hoặc Git Bash:

```bash
g++ -std=c++17 -Wall -Wextra "bai-lam/final-boss/bronze.cpp" -o "bai-lam/final-boss/bronze.exe"
```

Kiểm tra mã kết thúc (exit code) ngay sau đó bằng `echo $?`. **Chỉ khi biên dịch thành công** mới chạy:

```bash
"./bai-lam/final-boss/bronze.exe"
echo $?
```

PowerShell:

```powershell
g++ -std=c++17 -Wall -Wextra "bai-lam/final-boss/bronze.cpp" -o "bai-lam/final-boss/bronze.exe"
$LASTEXITCODE
```

Chỉ khi mã kết thúc của lệnh biên dịch là 0:

```powershell
& ".\bai-lam\final-boss\bronze.exe"
$LASTEXITCODE
```

Việc bộ kiểm thử ban đầu có ca FAIL cho thấy đề đang phát huy tác dụng. Không sửa dữ liệu kỳ vọng, không xóa ca kiểm thử và không coi mã kết thúc khác 0 của đề có lỗi là lỗi máy. Sau mỗi bản vá, lưu tệp, biên dịch lại thành công rồi mới chạy lại. Dùng tệp thực thi cũ sau một lần biên dịch lỗi sẽ làm mất giá trị của toàn bộ bằng chứng.

### Kế hoạch sửa theo hai bước

Bước một: chọn một lỗi và dự đoán hành vi nào sẽ thay đổi sau bản vá; một ca kiểm thử vẫn có thể FAIL vì lỗi còn lại che khuất kết quả. Chỉ thay đổi một quyết định, chạy lại và xem cả nguyên nhân thất bại thay vì chỉ đếm số ca PASS. Bước hai: đối chiếu các ca còn lỗi để tìm quyết định sai thứ hai. Cuối cùng, đọc diff và giải thích vì sao không cần thay kiểu dữ liệu, cài thêm thư viện hay viết lại toàn bộ chương trình.

**Mục tiêu sau khi sửa:** cả 9 ca đều đạt. Kết quả này chưa chứng minh mọi đầu vào có thể nghĩ ra đều được xử lý đúng. Người học cần thêm ít nhất một ca kiểm thử tự đề xuất, ví dụ một khoản 1 VND hoặc ba khoản theo thứ tự đảo ngược, và ghi ca bổ sung riêng để không nhầm với số ca gốc của đề.

### Đáp án cấp Bronze

Hai lỗi gốc là cận vòng lặp `i < n - 1` bỏ sót phần tử cuối, và điều kiện `amount >= 1000000000LL` từ chối cả giá trị biên hợp lệ. Bản vá tương ứng là đổi cận thành `i < n` và chỉ từ chối khi `amount > 1000000000LL`. Vẫn giữ điều kiện `amount <= 0` và phần kiểm tra số lượng khoản.

Nếu chỉ sửa vòng lặp cộng, ca tiền tối đa vẫn bị từ chối: kết quả mong đợi là 7 PASS, 2 FAIL. Nếu chỉ sửa miền giá trị tiền, ca một khoản vẫn cộng ra 0 và bộ đếm vẫn là 5 PASS, 4 FAIL. Khi đó hai ca biên đã chuyển từ trạng thái "bị từ chối nhầm" sang "cộng sai", nhưng số ca FAIL không phản ánh sự thay đổi này. Để phân biệt, cần ghi lại mỗi lời gọi phát sinh ngoại lệ hay trả về tổng bao nhiêu; không kết luận bản vá vô dụng chỉ vì bộ đếm không đổi. Đây cũng là lý do không dùng một lần thấy kết quả 60000 để khẳng định toàn bộ chức năng đã đúng.

Với bản đề chưa sửa, có thể suy ra từ mã nguồn kết quả 5 PASS, 4 FAIL; sau hai bản vá là 9 PASS, 0 FAIL. Đây là *kết quả mong đợi* dùng để đối chiếu; người học phải ghi lại kết quả thực tế khi chạy trên máy đang dùng. Bài không yêu cầu xây dựng bộ phân tích dữ liệu nhập từ bàn phím hay kiểm tra chuỗi ký tự như `35000abc` trong C++.

## 5. Cấp Silver: dữ liệu phải đi đúng từ đầu đến cuối

**Bối cảnh.** Một hàm xử lý tiền dùng cách phân tích chuỗi quá dễ dãi, còn hàm cộng lại đọc sai tên trường. Khi thử trên giao diện, hai lỗi có thể che lấp nhau. Vì vậy, như trong lộ trình của Lan, bài làm bắt đầu bằng kiểm thử logic biệt lập rồi mới quay lại kiểm tra giao diện.

### Bài logic có hai lỗi chủ đích

Sao chép cả `silver.cjs` và `test_silver.cjs` vào cùng thư mục `bai-lam/final-boss`. Đọc tệp kiểm thử trước, sau đó lập bảng riêng cho `parseAmount` và `totalExpenses`. Việc ô nhập chỉ cho phép bàn phím số không bảo vệ được dữ liệu lấy từ kho lưu trữ hoặc dữ liệu truyền vào khi gọi hàm trực tiếp.

Chạy từ thư mục gốc của dự án, với Node.js đã có sẵn:

```bash
node "bai-lam/final-boss/test_silver.cjs"
```

Ngay sau đó, kiểm tra mã kết thúc bằng `echo $?` trong Bash hoặc `$LASTEXITCODE` trong PowerShell. Kết quả mong đợi ban đầu là có ca lỗi. Không chạy `npm install`, vì đề chỉ dùng thư viện chuẩn của Node.js. Khi ghi bảng, giữ nguyên kiểu dữ liệu: `"35000"` là chuỗi, `35000` là số.

| Nhóm kiểm thử | Điều cần chứng minh | Ví dụ phản chứng |
|---|---|---|
| Phân tích đúng toàn chuỗi | Không nhận một phần chuỗi rồi bỏ phần hậu tố | `35000abc`, `1.5`, `1e3` đều phải bị từ chối |
| Phân tích đúng miền giá trị | Sau khi chuyển sang số vẫn kiểm tra dương, nguyên và giới hạn | Chuỗi rỗng, 0, giá trị vượt 1e9 |
| Cộng đúng trường | Dữ liệu chứa `amount`, không tự phát sinh trường `value` | Ba khoản phải cho 60000, một khoản cho 7000 |
| Danh sách đúng hợp đồng | Rỗng cho 0, tối đa 500 khoản, không chấp nhận `amount` kiểu chuỗi | 501 khoản, `{amount:'35000'}` |

Sửa từng lỗi một và dự đoán trước nhóm kiểm thử nào sẽ bị ảnh hưởng. Không sửa tệp kiểm thử để bỏ qua lỗi. Sau khi 12 ca có sẵn đều đạt, tự thêm ca `"1000000001"` và ca `" 7000 "`; ghi đúng số ca thực sự đã chạy, không báo rằng bộ kiểm thử vẫn chỉ gồm 12 ca.

### Quay lại luồng Web tham khảo

Bộ đề cấp Silver là bài Node.js riêng, **không tự động trở thành ứng dụng Web**. Nếu chưa chuẩn bị bản sao ở Chương 2, dùng trình quản lý tệp sao chép **toàn bộ thư mục** `vi-du/nam-2-web` sang `bai-lam/nam-2-web`, giữ `index.html`, `data.js` và `app.js` trong cùng thư mục. Sau khi giải được hai hàm, mở `bai-lam/nam-2-web/index.html` để theo dõi luồng form → hàm xử lý sự kiện → `parseAmount` → `normalizeExpenses` → lưu trữ → `render`. Demo Web tham khảo đã có logic đúng; không chép `module.exports` của bài Node.js vào trình duyệt.

Từ ba khoản mẫu có tổng 60000, thêm khoản Bánh mì 15000 và kỳ vọng tổng mới là 75000. Nếu dữ liệu đang lưu khác dữ liệu mẫu, chỉ khôi phục dữ liệu mẫu sau khi xác nhận đó là dữ liệu giả có thể thay thế, hoặc tính kỳ vọng từ tổng thực tế hiện có. Thử nhập chuỗi `35000abc`: tổng không được tăng. Thêm khoản có tên `<b>Vở</b>`: tên phải hiển thị nguyên văn, không được hiểu thành HTML.

Tải lại trang và đọc thông báo về trạng thái lưu trữ. Khi ứng dụng đang dùng phương án dự phòng trên bộ nhớ RAM (fallback), không đòi hỏi dữ liệu còn tồn tại sau khi tải lại; nút khôi phục dữ liệu mẫu không tự bật lại cơ chế lưu bền trong phiên đó. Ghi lại trình duyệt, địa chỉ đang mở và thông báo quan sát được. Khi mở bằng địa chỉ `file://`, hành vi của localStorage phụ thuộc trình duyệt; không kết luận toàn bộ ứng dụng hỏng chỉ vì mở bằng một địa chỉ khác.

**Mục tiêu cấp Silver:** giải thích được hai lỗi logic, có bộ kiểm thử riêng và biên bản thử nghiệm trên Web; chỉ ra được sự khác biệt giữa hàm tính tiền, lược đồ (schema) bốn trường và DOM. Không cần viết backend để "nâng cấp" bài làm.

### Đáp án cấp Silver

Lỗi thứ nhất: `parseInt` có thể chỉ đọc phần đầu của chuỗi và bỏ qua phần còn lại. Cách sửa là kiểm tra toàn bộ chuỗi chỉ gồm chữ số sau khi `trim`, rồi chuyển đổi bằng `Number`; vẫn giữ kiểm tra số nguyên an toàn và miền giá trị tiền. Thêm cơ số 10 (radix) vào `parseInt` không sửa được lỗi chấp nhận hậu tố.

Lỗi thứ hai: hàm reducer cộng `item.value` trong khi dữ liệu chỉ có trường `amount`; cần cộng `item.amount`. Giá trị `undefined` khi đọc một trường không tồn tại khác với `NaN` sinh ra trong phép cộng số. Không xử lý bằng cách đổi `undefined` thành 0, vì cách đó che giấu việc hợp đồng về tên trường đã bị vi phạm.

Kết quả mong đợi của bộ 12 ca: bản đề cho 6 PASS, 6 FAIL; bản đã sửa cho 12 PASS, 0 FAIL. Phần trình duyệt vẫn phải được kiểm tra riêng. Việc kiểm thử logic đạt hết không đủ để kết luận nút thêm, nút xóa, việc dùng `textContent` và cơ chế lưu trữ đều hoạt động đúng.

## 6. Cấp Gold: một Agent, một phạm vi, một lần nghiệm thu

Cấp Gold chỉ nên chọn sau khi đã nắm vững yêu cầu của cấp Bronze hoặc Silver. Người học đóng vai người điều phối và không trao quyền trên toàn bộ máy để đổi lấy tốc độ. Quy trình dưới đây vận dụng Bài thực hành 05 (mục 2.5) và Bài thực hành 06 (mục 2.6).

1. **Khóa phạm vi.** Nêu chính xác bản sao và tên tệp được phép làm việc; cấm cài gói, sửa cấu hình hoặc quyền, xóa tệp, thực hiện commit, push, publish hoặc gọi dịch vụ bên ngoài. Kiểm tra cơ chế phân quyền thật của công cụ, không chỉ dựa vào lời cấm viết trong prompt.
2. **Yêu cầu kế hoạch trước.** Ở bước này Agent chỉ được đọc và đề xuất kiểm thử. Nếu Agent đề xuất chuyển toàn bộ bài sang một framework mới, từ chối và giải thích vì sao đề xuất đó nằm ngoài nhiệm vụ.
3. **Duyệt từng thay đổi.** Dùng thẻ P10 trong [Thư viện prompt mẫu](prompt-library.md), điền đầy đủ các trường. Không cấp phép mơ hồ kiểu "làm mọi thứ cần thiết".
4. **Theo dõi bằng chứng.** Ghi lại tệp nào được đọc hoặc sửa, lệnh nào được thực thi, mã kết thúc của từng lệnh, kể cả các lần thất bại. Báo cáo về ý định của Agent không thay thế kết quả quan sát được.
5. **Đọc diff trước khi chấp nhận.** So sánh với điểm khôi phục (checkpoint) của bản sao; xuất hiện tệp ngoài phạm vi là lý do để dừng. Không khôi phục hàng loạt làm mất các thay đổi hợp lệ của người khác.
6. **Nghiệm thu độc lập.** Người học tự chạy lại kiểm thử, tự giải thích hai lỗi và một ca biến thể. Nếu thiếu công cụ, ghi rõ phần chưa kiểm tra thay vì mượn kết quả chạy ở nơi khác.

| Mốc | Agent được phép làm | Người học phải quyết định | Bằng chứng |
|---|---|---|---|
| Trước khi sửa | Đọc trong phạm vi, đề xuất | Kế hoạch và quyền có phù hợp không? | Kế hoạch đã được xem xét |
| Khi sửa | Chỉ sửa đúng tệp đã duyệt | Có cần dừng vì vượt phạm vi không? | Diff và nhật ký |
| Khi kiểm thử | Chạy các lệnh được cho phép | Kết quả có ứng với đúng phiên bản mã không? | Lệnh, đầu ra, mã kết thúc |
| Khi nghiệm thu | Báo cáo phần đã xong và chưa xong | Đã đủ căn cứ để nghiệm thu chưa? | Kiểm thử tự chạy, vấn đáp |

Trường hợp không có Agent: người học đóng vai người giao việc và nhờ một sinh viên khác phản biện kế hoạch. Bằng chứng thu được có giá trị luyện tập nhưng phải gắn nhãn mô phỏng; phần vận hành công cụ thật để ở trạng thái chưa thực hiện.

## 7. Bảng nghiệm thu và rubric 100 điểm

Rubric này phục vụ mục đích luyện tập, không phải thang điểm chính thức của Trường. Nếu môn học có rubric riêng, sử dụng rubric của môn học. Điểm cao không bù đắp cho các vi phạm như làm lộ khóa API hoặc dữ liệu cá nhân, dùng AI khi không được phép hoặc khai báo sai.

| Tiêu chí | Điểm tối đa | Đạt điểm tối đa khi | Khi thiếu bằng chứng |
|---|---:|---|---|
| Yêu cầu chức năng và phạm vi | 10 | Nêu được hợp đồng, giới hạn và những việc không làm | Mơ hồ: tối đa 4 |
| Chọn công cụ có lý do | 5 | Gắn lựa chọn với tác vụ, chi phí và quyền | Chỉ nói "mạnh nhất": tối đa 1 |
| Cấu trúc dữ liệu | 10 | Nêu đúng kiểu, trường và ranh giới kiểm tra | Nhầm chuỗi với số hoặc nhầm C++ với Web: tối đa 4 |
| Triển khai và phân định đóng góp | 10 | Mã thuộc bản sao, phân định rõ phần AI hỗ trợ và phần tự làm | Sao chép mà không giải thích: tối đa 3 |
| Hai lỗi và nguyên nhân | 15 | Hai bản vá, mỗi bản có phản ví dụ độc lập | Chỉ sửa được một lỗi: tối đa 7 |
| Kiểm tra thay đổi | 10 | Diff có mục đích, không có thay đổi ngoài phạm vi | Không có so sánh trước và sau: tối đa 3 |
| Kiểm thử có kỳ vọng | 15 | Giữ lần chạy sai, biên dịch và kiểm thử bản mới, có ca biên, rỗng và dữ liệu sai | Chỉ có một ca mẫu: tối đa 4 |
| Riêng tư, bảo mật, giấy phép | 10 | Dùng dữ liệu giả, quyền tối thiểu, nguồn rõ ràng | Có lỗi nghiêm trọng chặn nộp: chưa nghiệm thu |
| Khai báo AI trung thực | 5 | Nêu công cụ, việc được hỗ trợ, phần tự làm và phần chưa kiểm | Khai báo sai: chưa nghiệm thu |
| Giải thích và biến thể không AI | 10 | Tự trả lời bằng trace hoặc kiểm thử, nhận biết giới hạn | Chỉ đọc lại lời của AI: tối đa 3 |
| **Tổng** | **100** | Không có điều kiện chặn nộp | Điểm số không thay thế bằng chứng |

Với người làm hoàn toàn không dùng AI, chấm sự phù hợp của lựa chọn và tính trung thực của khai báo; không trừ điểm vì không mua dịch vụ. Với cấp Gold, mức điểm tương ứng phải dựa trên bằng chứng vận hành Agent thật; nếu chỉ mô phỏng, ghi phần đó là chưa đạt.

## 8. Buổi bảo vệ ngắn

Buổi bảo vệ kéo dài khoảng tám phút, theo trình tự sau:

| Thời điểm | Nội dung trình bày |
|---|---|
| Phút 1 | Mô tả đầu vào, đầu ra và một việc ứng dụng không làm. |
| Phút 2–3 | Giải thích lỗi thứ nhất bằng phản ví dụ nhỏ nhất. |
| Phút 4–5 | Giải thích lỗi thứ hai và ca kiểm thử phát hiện ra lỗi đó. |
| Phút 6 | Mở diff, chỉ ra các dòng nằm ngoài thuật toán chính, chẳng hạn phần kiểm tra hợp lệ (validation). |
| Phút 7 | Nêu một phần chưa được kiểm chứng. |
| Phút 8 | Trả lời câu hỏi biến thể do người học khác hoặc giảng viên chọn. |

Một số câu hỏi biến thể có thể dùng: đảo thứ tự các khoản có làm tổng thay đổi không; với 500 khoản ở mức tối đa thì biến tổng cần kiểu dữ liệu nào; vì sao khi lọc theo nhóm vẫn phải kiểm tra toàn bộ danh sách; nếu tắt cơ chế lưu trữ thì chức năng nào còn hoạt động; vì sao thêm 15000 không phải lúc nào cũng cho tổng 75000. Người hỏi không cần gây khó bằng các tính năng chưa học.

### Tóm tắt dự án

Kết thúc dự án, người học có một sản phẩm nhỏ cùng một chuỗi bằng chứng có thể lặp lại. Người học không cần nhớ mọi cú pháp, nhưng phải biết truy mỗi câu hỏi về đúng tệp, đúng dữ liệu và đúng phép thử. Khi công cụ AI không còn sẵn dùng, bảng trace, bộ kiểm thử và khả năng tự giải thích vẫn là năng lực của chính người học.

## Cầu nối

Hoàn thành dự án không phải điểm kết thúc. Bước tiếp theo là mang chuỗi làm, kiểm, giải thích vào các môn học thật: mỗi lần dùng AI, hãy khai báo đúng mức hỗ trợ, giữ bằng chứng và tự trả lời được câu hỏi biến thể. Thư viện prompt mẫu giúp soạn nhanh các thẻ giao việc; Thỏa thuận học tập ghi lại cam kết của người học. AI hỗ trợ, người học quyết định.
