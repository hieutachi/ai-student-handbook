# 01 · SOURCE AUDIT

Ngày kiểm kê: 30/10/2026. Trạng thái: đã đọc toàn văn, chưa coi kiểm kê là kiểm chứng kỹ thuật hay pháp lý.

## Phạm vi và bằng chứng đọc

Nguồn bảo toàn: `source/Cam-nang-AI-Sinh-vien.original.md`, 2.532 dòng, SHA-256 `704d10e9603d0b494196795b9b45ae701dfc1caadeab54bcc3d76c4c7ae53772`.

Biên tập viên đọc toàn bộ theo các khoảng liên tục 1–350, 351–700, 701–1050, 1051–1400, 1401–1750, 1751–2100, 2101–2450, 2451–2532; đọc toàn bộ 716 dòng bản yêu cầu mới. Người phụ trách đối chiếu trực tiếp code C++ và JavaScript đi kèm. Việc kiểm chứng tài liệu chính thức và thực thi tách sang bước riêng, không suy ra từ lời khẳng định trong bản nguồn.

## Bất biến học thuật và dữ liệu

- Minh năm nhất, C++; Lan năm hai, Web/OOP/DSA/CSDL. Đây là nhân vật hư cấu, không phải khảo sát TLU.
- Ba khoản giả: Cơm trưa 35000, Xe buýt 7000, Vở ghi 18000; tổng 60000. Lỗi bỏ phần tử cuối cho 42000; tổng trung gian 42000 chưa tự chứng minh có lỗi.
- `amount` nguyên VND, 1–1000000000; tối đa 500 khoản; rỗng trả 0; tổng cực đại 500000000000. C++ `vector<long long>` chỉ mô hình tiền, Web `Expense` có bốn trường.
- Web thuần HTML/JS/localStorage, không backend/đăng nhập. SQLite `:memory:` là minh họa riêng.
- Mô phỏng ≠ trace ≠ kỳ vọng ≠ kết quả đã chạy. JS kiểm thử logic ≠ kiểm chứng DOM/lưu trữ.
- Qoder IDE ≠ Qoder Desktop ≠ Qoder CLI. Không bịa giá, quota, benchmark, ưu đãi, quy định TLU hoặc kết luận pháp lý về một vụ việc.

## Content inventory đầy đủ

| Nguồn / dòng | Nội dung phải bảo tồn | Đánh giá biên tập | Đích mới |
|---|---|---|---|
| Mở đầu 1–147 | Câu chuyện, dữ liệu, hai nhánh, mục tiêu–bằng chứng, hướng dẫn đọc, ví dụ, từ mới, thỏa thuận | Nhiều giải thích trước tình huống; tách tra cứu khỏi mở đầu | Mở đầu, Glossary, Learning Agreement |
| 1.1 / 162–294 | Model/provider/application/producer, API/key, bảng nhận diện, đường truy cập, khác đầu ra | Có chiều sâu; chuyển trace dài sang nhiệm vụ C++ | AI MYSTERY, AI MAP |
| 1.2 / 295–398 | Prompt/context/token, brief, context window, training/inference/search, hallucination, trích dẫn, safe integer | Nhiều khái niệm nối dài; cần ví dụ nhìn được | 1.2, Prompt Library, 3.1 |
| 1.3 / 399–509 | Free/subscription/API; 0.925 USD/23125 VND, ×20 = 18.50 USD/462500 VND; input/output; agent nhiều request; hard cap | Phép tính đáng giữ; chỉ dẫn chỗ nhập và tự đối chiếu | AI WALLET |
| 1.4 / 510–561 | Free first, không mua, ngân sách 300000 giả định, gia hạn, ưu đãi, tuổi, dữ liệu | Cảnh báo trùng chương 4; dùng liên kết thay lặp nguyên văn | 1.4 |
| 1.5 / 562–619 | Ma trận tác vụ, năm tiêu chí, benchmark A–C, rubric 10 điểm, phiếu trống | Nên là hoạt động so sánh, không bảng xếp hạng | AI TOOL BATTLE |
| 1.6 / 620–746 | Lab 20 phút, worksheet, quyết định có điều kiện, đáp án, sáu câu, nguồn | Đáp án lặp phép tính; phân lớp gợi ý/đối chiếu | MINI CHALLENGE |
| 2.1 / 809–851 | Editor/IDE/chat/agent và chọn công cụ đủ dùng | Sơ đồ tiến hóa gây hiểu nhầm; dùng bản đồ vai trò | Mission 01 |
| 2.2 / 852–909 | Terminal/shell/CLI, Observe–Plan–Act–Test, bằng chứng, prompt quan sát | Nhấn prompt không thay cơ chế quyền | Mission 01, 05 |
| 2.3 / 910–965 | Chỉ đọc, context nhỏ, dẫn vị trí, Agent, View Changes, Auto-Run, đúng sản phẩm | Giảm khẳng định UI không được quan sát | Mission 02, 05 |
| 2.4 / 966–1097 | Trace, ca rỗng/một phần tử, unsigned, reference/copy, lỗi `;`, executable cũ | Phần sâu bắt buộc giữ, che đáp án sau dự đoán | Mission 03 |
| 2.5 / 1098–1227 | Expense/OOP/DSA, O(n)/O(1), ba tệp, anonymous handler, chuỗi, parse, undefined/NaN, fallback | Demo đúng phải tách khỏi lỗi giả lập | Mission 04 |
| 2.6 / 1228–1334 | Bash/PowerShell, cwd, build/run, stdout/stderr/exit code, `--test`, Node/DOM, CLI tùy chọn | Bảng lệnh tra cứu, dừng nếu build lỗi | Mission 01, 07 |
| 2.7 / 1335–1384 | Hợp đồng giao việc, phạm vi, không cài/commit/publish, diff, accept, checkpoint, giữ lần lỗi | Thêm quyết định trước diff vượt phạm vi | Mission 05, 06 |
| 2.8 / 1385–1502 | C1–C9, W1–W10, T1–T8, hai nhánh, rubric, câu hỏi | Không gộp kỳ vọng với đã chạy | Mission 07, Final Boss |
| 3.1 / 1513–1549 | Sáu tình huống, mục tiêu, phần AI làm, phần tự chứng minh | Giữ sắc thái vùng xám, không dán nhãn người học | 3.1, Learning Agreement |
| 3.2 / 1550–1576 | Vibe coding có kiểm soát, bốn câu hỏi, đổi nhỏ | Thuật ngữ theo cách dùng của sách | 3.1, 3.3 |
| 3.3 / 1577–1609 | Phiên 25 phút có AI, khi mệt/chưa xong/lộ đáp án | Không nhầm với thử thách hoàn toàn không AI | 3.2 và 3.5 |
| 3.4 / 1610–1768 | Tám prompt: Socratic, ba gợi ý, trace, review, test-first, tiếng Anh, vấn đáp, tự kiểm | Thẻ đầy đủ context, sao chép độc lập | Prompt Library |
| 3.5 / 1769–1860 | Hai hội thoại, trace, biến đổi kiểu và chuỗi kết quả | Chất liệu tốt; giữ nhãn hư cấu và từng kiểu dữ liệu | 3.2, 3.3 |
| 3.6 / 1861–2011 | Bài sửa, bảng test, lời giải xác thực C++/JS, module, max, tổng nhóm, kiểm toàn danh sách | Tách bản vá cận khỏi mở rộng validation | 3.6 |
| 3.7 / 2012–2104 | Ba mức tự đánh giá, tám vấn đáp, sơ đồ, phiếu ba dòng | Không suy năng lực lâu dài từ một phiên | 3.7, Skill Map |
| 4.1 / 2119–2161 | Phạm vi AI, tin nhắn hỏi, khai báo, attribution/quyền/trách nhiệm | Không coi khai báo là được phép | Hồ sơ 05, 07 |
| 4.2 / 2162–2204 | Giả/khử nhận dạng/bảo vệ, tái nhận diện, quyền Agent, ảnh/chat/Git, placeholder | Hộp luật phải có nguồn và mức chắc chắn | Hồ sơ 02, 03 |
| 4.3 / 2205–2292 | SQL parameter/tuple/allowlist, fixture, XSS/textContent, C++ UB, dependencies/registry/lockfile | Tách phòng khám kỹ thuật, không cắt ngữ cảnh | Hồ sơ 04, phòng khám 4.8 |
| 4.4 / 2293–2329 | MIT/GPL/no license/mã AI, thẻ nguồn, nghĩa vụ | Bổ sung nguồn giấy phép gốc nếu dùng | Hồ sơ 06 |
| 4.5 / 2330–2351 | Trách nhiệm học thuật/nghề nghiệp/pháp lý, phân vai review, mức chắc chắn | Tránh khẩu hiệu pháp lý 100% | 4.7, Final Boss |
| 4.6 / 2352–2378 | Sáu bước key leak, thu hồi trước dọn, usage/log, thẩm quyền, mẫu báo | Hồ sơ đã mạnh; bổ sung phân tích lựa chọn | Hồ sơ 01 |
| 4.7 / 2379–2518 | Vấn đề/xử lý/bằng chứng, rubric 8, sáu tình huống, khai báo, checklist A/B/C | Nghiệm thu là bước thực hành, không danh sách cảnh báo | 4.7–4.8, Final Boss, Learning Agreement |
| Kết 2524–2532 | Ba câu hỏi và giới hạn demo/TLU/môi trường chạy | Môi trường thực chuyển báo cáo QA | Kết, báo cáo chất lượng |

## Sửa lỗi cụ thể, không chỉ làm đẹp

1. Dòng 783 tạo `-ban-sao` nhưng 922 và 1243–1259 dùng tên gốc. Bản mới dùng duy nhất quy ước mở thư mục gốc `AI-Student-Handbook`; bài làm riêng dưới `bai-lam/`, ví dụ gốc chỉ để đối chiếu. Mỗi khối lệnh ghi rõ thư mục và shell.
2. Dòng 1232 tham chiếu hướng dẫn mở bảng lệnh chưa tồn tại: bỏ tham chiếu, không bịa phím tắt.
3. Dòng 1416 nói demo đúng nhưng 1897–1904 yêu cầu sửa: tách lab đọc hiểu demo đúng và lab snippet lỗi chủ đích.
4. Dòng 1897 bắt đầu hai khoản mà chưa nói chuẩn bị: Web nạp ba khoản; nếu cần 42000 trung gian, xóa Vở ghi trên bản sao rồi thêm lại hoặc dùng dữ liệu lab riêng, có cảnh báo tác động.
5. Sửa cận vòng lặp và thêm validation là hai yêu cầu: nhiệm vụ đầu đổi cận; nhiệm vụ sau viết kiểm tra miền/số lượng, không hứa một dòng giải quyết cả hai.
6. Khối build/run phải dừng nếu compile lỗi; tệp cũ không chứng minh code mới chạy được.
7. Khi Minh đọc luồng Web phải ghi review chéo với Lan, không ngầm đổi persona.

## Nội dung mới cần ghi nhãn

- Tình huống mở ba AI và các phiếu trả lời là mô phỏng, không benchmark thật.
- Bảy Mission với đủ chín trường học tập; bảy hồ sơ sự cố có lựa chọn và phân tích.
- AI TRAP; Memory Experiment (tự quan sát, không nghiên cứu hay chẩn đoán); 25 phút không AI tách khỏi phiên có AI.
- Final Boss Bronze/Silver/Gold: sửa hai lỗi chủ đích, kiểm diff/test, riêng tư, khai báo, giải thích; Gold không là gói trả tiền.
- Cover, bốn opener, nhân vật nhất quán và sơ đồ; dashboard tiến độ sản xuất khác tiến độ tự học.

## Claim cần xác minh riêng

Số test, API hàm, file:// và fallback; tên chế độ IDE/Desktop/CLI; tính phí API khác subscription; quyền lợi sinh viên/tuổi/quota; điều khoản luật Việt Nam và hiệu lực tại mốc đọc; MIT/GPL. Giữ link gốc để tra, dùng nhãn chưa xác minh khi chưa đọc được nguồn chính thức. Không cập nhật âm thầm theo trí nhớ.

## Kết luận giai đoạn 0

Nguồn đủ chiều sâu để tái thiết kế. Chiến lược là giữ nội dung chuyên môn trong lớp đọc sâu và hoạt động có kiểm chứng, gom lặp vào thư viện tra cứu, sửa bảy điểm thao tác sai/thiếu; không rút thành landing page hay bản giới thiệu công cụ.

## Cập nhật kiểm chứng kỹ thuật 30/10/2026

Đã đọc đầy đủ 7 tệp ví dụ. Phát hiện `normalizeExpenses` chấp nhận `category: ['khac']` do ép kiểu khóa trong `Object.hasOwn`; đã tái hiện test thất bại (exit 1), chỉ sửa bản sao ở dự án mới bằng kiểm tra `typeof item.category === 'string'` và thêm regression test. Bản mới **34 passed, 0 failed**, bản nguồn **33 ca** giữ nguyên. Nhật ký cả trước/sau ở `reports/test-runs.jsonl`. Không ghi bản mới còn 33 ca.

`totalExpenses` Web chỉ kiểm phần tiền và số lượng, không kiểm đầy đủ bốn trường; cần `normalizeExpenses` ở ranh giới lưu/đọc. SQLite là fixture riêng: không giới hạn 500 bản ghi, type affinity có thể đổi chuỗi số thành INTEGER. Không nói validation SQLite giống hệt JS. localStorage thất bại làm demo chuyển RAM, nút khôi phục mẫu không tự phục hồi quyền lưu trong phiên.

Nguồn chính thức đã được người rà kỹ thuật đọc:

- [Qoder IDE Ask/Agent](https://docs.qoder.com/user-guide/chat/overview.md), [Desktop Coding/General](https://docs.qoder.com/qoder/new-task.md), [CLI modes](https://docs.qoder.com/cli/working-modes.md). General không phải Ask chỉ đọc; không chuyển hướng dẫn UI giữa sản phẩm.
- [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage): `file://` chưa xác định thống nhất; [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent): văn bản tại ô bảng; [parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt): đọc một phần chuỗi; [safe integer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/isSafeInteger): ±9007199254740991.
- [SQLite affinity](https://www.sqlite.org/datatype3.html): kiểu lưu sau chuyển đổi không chứng minh kiểu đầu vào ban đầu.
- [GitHub về secret lộ](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository): revoke/rotate trước dọn, clone/cache không tự biến mất.
- [Công báo Luật 91/2025/QH15](https://congbao.chinhphu.vn/van-ban/luat-so-91-2025-qh15-45578.htm): hiệu lực 01/01/2026; [Luật 131/2025/QH15](https://congbao.chinhphu.vn/van-ban/luat-so-131-2025-qh15-468691.htm): hiệu lực 01/04/2026. [Cục bản quyền](https://cov.gov.vn/tin-tuc/gioi-thieu-luat-sua-doi-bo-sung-mot-so-dieu-cua-luat-so-huu-tri-tue-nam-2025-noi-dung-quyen-tac-gia-quyen-lien-quan-168841.html) giải thích phần đối tượng tạo ra có AI; chưa rà đủ văn bản hướng dẫn và vụ việc cụ thể nên không kết luận ai đương nhiên sở hữu toàn bộ code AI.
- OpenAI billing ChatGPT/API: chỉ đối chiếu được đoạn trích chỉ mục chính thức; truy cập toàn văn Help Center trả 403. Không nhận đã kiểm toàn văn, không suy giá/quota/quyền lợi tài khoản từ đó.

Bản sao Web đã sửa link quay về `website/index.html#chuong-2`; phải kiểm lại sau khi dựng website. C++ trong lượt rà chuyên gia mới kiểm tĩnh, sẽ compile/run thật ở QA. Bố cục/DOM chưa được chuyên gia này xác nhận.
