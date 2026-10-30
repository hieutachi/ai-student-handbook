# 04 · BÁO CÁO CHẤT LƯỢNG

Mốc kiểm cuối: **30/10/2026**. Báo cáo này ghi việc đã chạy, bằng chứng nằm ở đâu, phần chưa kiểm. Điểm tự đánh giá nằm ở mục 8 và chỉ có giá trị khi mục 2–7 đọc được bằng chứng tương ứng.

## 1. Kết quả một dòng

Bốn chương và bốn phần phụ trợ được biên tập lại từ nguồn 2532 dòng; bản đọc offline có 4 chương, 16 hình tự tạo, 74 bảng, 85 khối mã. Bốn bộ kiểm tự động đều đạt: **50/50** phép kiểm nội dung, **16/16** phép kiểm ví dụ thực thi, **82/82** phép kiểm bản offline và **80/80** phép kiểm bản online (Chrome headless 156) — gồm 16 SVG, ba kích thước màn hình, PDF và kiểm không có yêu cầu mạng. Lượt bàn giao thứ hai thêm trang **Bản đồ một trang** và **bản online có link gửi được** (mục 10). Review độc lập bằng vai sinh viên đã chạy trên cả bốn chương; mọi điểm lớn và nhỏ được nêu đã sửa hoặc ghi lý do, xem mục 6.

## 2. Nội dung — kiểm máy

Lệnh: `python scripts/check_content.py`. Nhật ký: `reports/content-checks.json` (50 phép kiểm, 50 đạt).

Đã kiểm: đủ 9 tệp chương/phụ trợ; liên kết nội bộ không gãy; UTF-8 không có ký tự thay thế; không phụ thuộc HTML thô ngoài khối mã; cấu trúc mục đánh số liên tục của bốn chương; ngưỡng độ sâu từng chương; sự hiện diện của các chủ đề bắt buộc; nguồn gốc `source/` không đổi byte; đủ 16 hình và cả 16 hình được dùng trong sách; ít nhất 11 thẻ prompt sao chép được; không có chuỗi giống khóa thật chưa gắn nhãn.

Ngưỡng độ sâu là **sàn chống viết tắt**, không phải điểm chất lượng:

| Tệp | Từ (cách trắng) | Mục |
|---|---:|---:|
| outline.md | 967 | 6 |
| introduction.md | 1536 | 7 |
| chapter-01.md | 11129 | 6 |
| chapter-02.md | 12096 | 7 |
| chapter-03.md | 10271 | 7 |
| chapter-04.md | 10843 | 12 |
| final-boss.md | 3479 | 8 |
| prompt-library.md | 2529 | 12 |
| glossary.md | 2952 | 7 |
| learning-agreement.md | 2013 | 6 |

## 3. Kiến trúc theo đề bài

| Yêu cầu | Trạng thái | Bằng chứng |
|---|---|---|
| Ch.1: AI MYSTERY, AI TOOL BATTLE, AI WALLET, AI MAP, MINI CHALLENGE | Đạt | ch.1 mục 1.1–1.6, bảng giá giả định, worksheet 20 phút, QUICK CHECK 6 câu |
| Ch.2: bảy Mission, mỗi Mission đủ chín trường | Đạt | mục 2.1–2.7; mỗi Mission có mục tiêu, bối cảnh, nhiệm vụ, prompt mẫu, các bước, kết quả mong đợi, lỗi thường gặp, câu hỏi kiểm, tiêu chí hoàn thành |
| Ch.3: AI TRAP, PREDICT BEFORE ASKING, REVERSE ENGINEERING, MEMORY EXPERIMENT, 25-MINUTE NO-AI, EXPLAIN IT BACK, SKILL UNLOCKED | Đạt | mục 3.1–3.7; có thêm 3.6 AI CHALLENGE cho bài sửa–kiểm |
| Ch.4: phòng sự cố 7 hồ sơ, mỗi hồ sơ đủ 6 phần; phòng khám SQL/XSS/C++ | Đạt | mục 4.1–4.7; mục 4.8 ba tiểu mục; checklist một trang; rubric 8 điểm |
| Final Boss Bronze/Silver/Gold, hai lỗi chủ đích, test, diff, riêng tư, khai báo, bảo vệ miệng, rubric | Đạt | `chapters/final-boss.md`; `vi-du/final-boss/`; rubric 100 điểm, 10 tiêu chí |
| Thư viện prompt, từ điển, thỏa thuận học tập, tự đánh giá | Đạt | P01–P11; 7 nhóm từ điển; thỏa thuận 6 mục; tự kiểm ở cuối mỗi chương |
| ≥14 nhóm hình, bìa, 4 opener, nhân vật nhất quán | Đạt | 16 SVG: bìa, 4 opener, 11 sơ đồ; `assets/manifest.json` có alt và mục đích |
| Dashboard tiến độ thật, không tự tăng theo giờ | Đạt | `dashboard/index.html` đọc `state.js`; phần trăm = số việc COMPLETED/14, không có bộ đếm thời gian |

## 4. Ví dụ thực thi — kiểm thật

Lệnh: `python scripts/verify_examples.py --wsl Ubuntu-22.04`. Nhật ký từng lần chạy: `reports/test-runs.jsonl`; bản tổng hợp: `reports/example-results.json` (16 phép kiểm, 16 đạt kỳ vọng).

Môi trường: Node v24.21.0, Python 3.14.7, g++ 11.4.0 trong WSL Ubuntu 22.04.

| Bộ | Kết quả | Ghi chú |
|---|---|---|
| `vi-du/nam-2-web/test_data.cjs` | 34 passed, 0 failed | 33 ca kế thừa + 1 ca hồi quy `category` dạng mảng |
| `vi-du/minh-hoa-sqlite.py` | 6 dòng PASS/đạt | fixture `:memory:`, không tạo tệp CSDL |
| `vi-du/nam-1-cpp/vi_sinh_vien.cpp --test` | 9 đạt | demo đúng, không phải đề lỗi |
| `vi-du/nam-1-cpp/loi-bo-sot.cpp` | in `42000`, exit 0 | lỗi cận cố ý, không có bộ test |
| `vi-du/final-boss/bronze.cpp` | 5 passed, 4 failed, exit 1 | đề lỗi chủ đích, đúng kỳ vọng |
| bronze sau vá (bản tạm) | 9 passed, 0 failed | chứng minh hai lỗi độc lập, không chứng minh mọi đầu vào |
| `vi-du/final-boss/test_silver.cjs` | 6 passed, 6 failed, exit 1 | đề lỗi chủ đích |
| silver sau vá (bản tạm) | 12 passed, 0 failed | chạy trên bản sao trong `reports/verification-*`, không sửa nguồn |

Lần thất bại được giữ trong nhật ký. Bản vá chỉ nằm ở bản sao tạm; tệp nguồn trong `vi-du/` vẫn là đề có lỗi.

**Phát hiện lỗi thật trong lúc kiểm:** `normalizeExpenses` chấp nhận `category: ['khac']` vì `Object.hasOwn` ép mảng thành khóa chuỗi. Đã tái hiện test đỏ (exit 1), sửa bản sao Web bằng `typeof item.category === 'string'` và thêm ca hồi quy — do đó bộ Web thành 34 ca. Không sửa lặng lẽ bản ghi cũ.

## 5. Bản đọc, hình và in — kiểm trong trình duyệt thật

Lệnh: `node scripts/browser_check.cjs --pdf`. Nhật ký: `reports/browser-runs.jsonl`; bản tổng hợp: `reports/browser-results.json` (80/80 đạt); ảnh chụp trong `reports/`.

Đã kiểm trên Chrome headless 156, profile tạm, mở bằng `file://`:

- Sách tải đủ 4 chương, 16 ảnh giải mã, mọi anchor trong sách tồn tại; 38 khối đáp án đóng sẵn và in mở tạm rồi trả trạng thái.
- Không tràn ngang ở 1440, 768, 375 px; không có ngoại lệ runtime; **không có yêu cầu mạng ra ngoài**.
- 16 SVG: chữ không chồng, chữ có transform nằm trong khung, cỡ chữ nhỏ nhất ≥18px ở cỡ hiển thị kiểm được.
- Tìm mục lục không dấu (NFD, `đ`→`d`); cỡ chữ 16–22px; menu mobile; tự ghi tiến độ còn sau khi tải lại trong cùng origin `file://`.
- Máy tính chi phí: 1000 request → `18.500 USD` / `≈ 462500 VND` (VND in không phân cách, đúng như văn chương; dấu chấm chỉ dùng cho USD); ô trống bị từ chối, không bịa ước tính.
- Trace vòng lặp: bản lỗi dừng ở 42.000, bản đúng 60.000; câu trạng thái nói rõ chưa kết luận từ tổng trung gian.
- Demo Web: nạp ba mẫu, thêm 15000 → 75.000; từ chối `15k`; `<b>Vở</b>` hiện nguyên văn; xóa hết → 0; lưu trữ hỏng chuyển RAM, không ghi đè dữ liệu hỏng, không hứa bền sau reload.
- PDF in được: `reports/print-preview.pdf`, 159 trang (đếm object `/Type /Page`; con số 157 ghi trước đó là đếm sai của trình duyệt).

## 6. Review độc lập bằng vai sinh viên

Hai agent rà độc lập đọc trọn chương và đối chiếu với mã ví dụ, không viết lại văn.

- **Chương 2:** không tìm thấy blocker; đã sửa 3 điểm — nhập lại tên sau `form.reset` để kiểm đúng parser, tạo checkpoint trước khi vá, đặt chỉ thị include ngoài hàm.
- **Chương 3:** không tìm thấy blocker; đã sửa 10 điểm lớn (chỉ đúng bảng trace cho nhánh A, giải nghĩa P02, mở Console kèm cảnh báo dán, tách bước validation C++, mẫu bộ chạy test, cách tự kiểm EXPLAIN IT BACK, đường dẫn ghi chép, ghi rõ giới hạn 500 khoản chưa kiểm ở `loi-bo-sot`, bỏ nguồn không tồn tại, nhãn mục vận dụng) và 5 điểm nhỏ ở lượt sau (cách dùng `$LASTEXITCODE`, đếm 34 ca theo output thay vì suy từ nguồn, câu chữ ba dòng bảng kiểm thử). Còn lại một NIT: vài bảng 4–6 cột phải cuộn ngang trên điện thoại — đã có vùng cuộn có nhãn.
- **Chương 4:** hai lượt rà. Lượt 1 sửa 11 điểm: lệnh chạy test trỏ về bản sao `bai-lam/` thay vì nhắc "gốc NEW" không tồn tại, mẫu khai báo dùng chỗ trống thay cho con số cứng `34 passed`/`Node 24`, đoạn SQL dùng đúng tên biến `connection` như tệp thật, ghi rõ chú thích C++ do chương thêm, đồng bộ hình `security.svg` theo đúng sáu bước trong văn (bỏ mũi tên chỉ sai bước), ghi chú `python3` đặt cạnh lệnh. Lượt 2: **1 điểm lớn** — "số lẻ" (người đọc dễ hiểu là số *lẻ* như 35001) đổi thành "số thập phân" ở chương 4, và vì cùng lỗi, cả ở phần mở đầu, chương 2 và thỏa thuận học tập; **11 điểm nhỏ** đã sửa (thêm mã sinh viên vào mô tả ảnh cho khớp đáp án, chỉ dẫn `echo $?`/`$LASTEXITCODE`, tách 7 ca AI gợi ý khỏi 34 ca, `py` cho Windows, đường build C++ từ `bai-lam/`, thứ tự sáu bước ở đáp án tình huống 6 và phút 5 tự giảng, dòng "Bản mã" trong phiếu bằng chứng, mục Mission 06 có số mục). NIT về hai tên nhãn giả khác nhau (`KEY_DEMO_INVALID` trong hình, `DEMO_KEY_NOT_A_SECRET` trong văn) giữ nguyên: cả hai đều là nhãn giả có ghi chú.
- **Chương 1 (lượt bổ sung):** không blocker; đã sửa 6 điểm lớn — đáp án nhận diện không còn khẳng định provider từ nhãn tự mô tả, nói rõ nên bắt đầu với Thẻ A, chỉ đúng nơi dùng rubric, bỏ tiêu đề lộ đáp án ở Thẻ B, phần mở đầu nói rõ phải tự tạo `bai-lam/`, máy tính chi phí in VND không dấu chấm để không nhầm 23.125 thành 23 đồng (đổi nhãn "lượt" thành "request"). Điểm nhỏ đã sửa: `Number.isSafeInteger` khớp `data.js`, thêm mốc "cùng học kỳ" cho phép so 462500 VND với trần, tên mục chương 4 đúng, nhãn chưa kiểm chứng cho câu về các sản phẩm Qoder, chỉ rõ tệp SQLite, cầu nối thuật ngữ Ask/Agent sang chương 2, và chú thích `loi-bo-sot.cpp` đổi "quan sat" thành "du kien". Chưa đổi tên "Thẻ A–C" thành "Thẻ 1–3" (gợi ý NIT), vì câu dẫn sang rubric đã nói rõ hai bộ chữ cái khác nhau.

Cả ba review đều dùng cùng mã trong `vi-du/`, nên kết luận số test/giá trị kỳ vọng đối chiếu được, không chỉ dựa vào lời văn.

## 7. Giới hạn — phần chưa kiểm

Ghi rõ để người đọc không suy quá bằng chứng:

1. **Một trình duyệt, một hệ điều hành.** Kiểm giao diện và `localStorage` chỉ trên Chrome 156 / Windows, mở bằng `file://`. Firefox, Safari, Edge và chế độ riêng tư chưa kiểm. MDN ghi hành vi `localStorage` với `file://` không được chuẩn hóa, nên không hứa lưu bền trên mọi máy.
2. **PDF chưa được đọc từng trang.** Đã xác nhận kết xuất 159 trang và mở bằng trình đọc; chưa soát thủ công toàn bộ ngắt trang, chú thích và bảng rộng trong bản in.
3. **Nguồn pháp luật chưa đọc lại toàn văn trong lượt này.** Số hiệu, ngày hiệu lực và liên kết giữ nguyên từ bản gốc, có nhãn "mốc đối chiếu 29/10/2026, chưa kiểm tra lại". Không kết luận ai đương nhiên sở hữu code do AI tạo.
4. **Quyền lợi, giá và quota của sản phẩm AI không được xác minh.** Mọi con số chi phí trong sách là giả định để học phép tính. Claim về credit ChatGPT/API mang nhãn chưa xác minh độc lập.
5. **Số liệu sư phạm là mô phỏng.** Ba phiếu trả lời ở chương 1, hội thoại Minh–Lan, bảy hồ sơ sự cố, phiếu benchmark đều là hư cấu có nhãn; không phải khảo sát, benchmark thật hay chuẩn đầu ra của TLU.
6. **MEMORY EXPERIMENT là tự quan sát.** Không có phép đo chứng minh hai nhiệm vụ tương đương, không kết luận nhân quả về trí nhớ.
7. **Chưa kiểm trên máy sinh viên thật.** Chưa có buổi thử với sinh viên năm 1–2; các review là mô phỏng vai, không thay phản hồi lớp học.
8. **Chưa chạy thử Gold với Agent thật.** Phần Gold là quy trình và mẫu nghiệm thu; sách nói rõ nếu không có quyền dùng Agent thì ghi "mô phỏng, chưa thực thi".

## 8. Tự đánh giá theo đề bài

Chỉ chấm khi có bằng chứng tương ứng; không cộng điểm cho phần "đã viết" mà chưa kiểm.

| Tiêu chí | Điểm | Căn cứ |
|---|---:|---|
| Bám đề bài, đủ thành phần bắt buộc | 19/20 | Mục 3; đủ 4 chương, 7 Mission, 7 hồ sơ, Final Boss ba mức |
| Chất lượng biên tập và độ sâu | 18/20 | Mục 2; 56.848 từ, 74 bảng; cả bốn chương đã qua rà vai sinh viên. Trừ 2 điểm vì lượt rà sau vẫn tìm ra lỗi từ ngữ dùng chung ("số lẻ") — dấu hiệu cần một lượt đọc với sinh viên thật |
| Hệ thống thị giác và hình | 13/15 | Mục 5; 16 SVG tự tạo, không ảnh stock, không chữ Việt do mô hình ảnh vẽ; PDF chưa soát từng trang nên trừ |
| Trải nghiệm đọc và tương tác | 14/15 | Mục 5; tìm không dấu, cỡ chữ, đáp án gập, in, mobile; chỉ kiểm một trình duyệt |
| Dashboard và tính trung thực của tiến độ | 9/10 | Mục 3; phần trăm theo checkpoint thật, không có bộ đếm giả; một đầu việc còn REVIEW nên hiển thị đúng là chưa xong |
| Kiểm chứng kỹ thuật và giữ lần thất bại | 15/15 | Mục 4; 16 phép kiểm, FAIL chủ đích được giữ, lỗi `category` được ghi lại |
| Trung thực về giới hạn | 5/5 | Mục 7; không tuyên bố đã kiểm phần chưa kiểm |

Lượt bàn giao thứ hai không đổi điểm: trang Bản đồ một trang và bản online lấp đúng chỗ yếu về điều hướng, nhưng cũng thêm hai mục chưa có bằng chứng mới (một trình duyệt trên live, tệp `.md` bị tải xuống thay vì hiển thị) — xem mục 10.

**Tổng: 93/100.** Điểm bị trừ đúng ở chỗ chưa có bằng chứng: PDF chưa soát từng trang, chỉ một trình duyệt, chưa thử với lớp thật. Rà chương 4 và chương 1 không tìm thấy blocker; lỗi lớn về từ ngữ đã sửa trên bốn tệp, nên không có lý do hạ điểm thêm.

## 9. Cách tái lập

Đứng tại gốc `AI-Student-Handbook`, cần Python 3 với `markdown-it-py`, `beautifulsoup4`, và Node ≥22 cho bước kiểm trình duyệt:

```bash
python scripts/make_visuals.py
python scripts/build.py
python scripts/check_content.py
python scripts/build_online.py
node scripts/browser_check.cjs --site
python scripts/verify_examples.py --wsl Ubuntu-22.04
node scripts/browser_check.cjs --pdf
python scripts/production.py delivery COMPLETED "Đóng gói sau khi ba bộ kiểm đạt"
python scripts/package.py
```

Chạy lại `build.py` sau mỗi lần sửa `chapters/`; bản `Cam-nang-AI-Sinh-vien-Redesigned.md` và `website/index.html` được sinh từ các tệp chương nên không sửa tay.

## 10. Bản online và trang "Bản đồ một trang" (lượt bàn giao thứ hai)

**Trang đã publish:** `https://ai-student-handbook-8nchu0xfadn.qoder.website` — chế độ **public** theo yêu cầu, mở không cần tài khoản.

**Vì sao có thêm trang này.** Người đọc phản hồi nội dung loãng: 57.815 từ mà không có một trang nào trả lời "sách gồm gì, vào chỗ nào, đã kiểm tới đâu". `chapters/outline.md` (967 từ) nay là mục đầu tiên của sách, gồm: bảng bốn chặng + Final Boss, liên kết thẳng tới bảy Mission và bảy hồ sơ, hợp đồng số liệu, bảng bốn bộ test kèm trạng thái, đường tắt 60 phút, mục dành cho giảng viên, và phần "đã kiểm / chưa kiểm".

**Cách dựng.** `scripts/build_online.py` sinh `site/` từ `website/index.html`: đổi 68 liên kết `../` về đường dẫn gốc, bỏ liên kết dashboard sản xuất, chỉ sao 34 tệp mà trang thực liên kết (1,35 MB). `site/` là đầu ra, không vào ZIP offline.

**Đã kiểm trên chính bản online**, không phải bản đang mở:

- `node scripts/browser_check.cjs --site`: 80/80 đạt, gồm hai phép kiểm mới — "One-page outline is first and complete" (đúng vị trí, 5 dòng chặng, 7 Mission, 7 hồ sơ, không anchor hỏng) và "Online build hides internal dashboard link".
- Trên URL thật bằng trình duyệt: HTTP 200 cho trang chủ và tài nguyên; 16/16 ảnh giải mã (`naturalWidth` 1200); không anchor hỏng; 38 khối đáp án đóng sẵn; máy tính chi phí vẫn ra `18.500 USD` / `462500 VND`; không tràn ngang; đường dẫn không tồn tại trả 404 thật, không phải HTML.
- Ảnh chụp kiểm: `reports/live-outline-desktop.png`.

**Chưa kiểm ở bản online:** chỉ mở trên một trình duyệt tại một thời điểm; chưa kiểm trên Firefox/Safari/Edge và điện thoại thật; chưa đo tốc độ tải từ network của sinh viên; `.md` đi kèm (`source/`, `editorial/`, `reports/`) được máy chủ trả về `application/octet-stream` nên trình duyệt **tải xuống** chứ không hiển thị trong tab — chủ ý giữ liên kết "đối chiếu bản gốc" chạy được, nhưng chưa tối ưu trải nghiệm đọc tệp Markdown trên web.

**Rủi ro còn lại của việc công khai:** trang public nghĩa là bất kỳ ai có link đều đọc được, kể cả máy tìm kiếm. Sách không chứa dữ liệu cá nhân hay khóa thật (đã quét mẫu trên toàn bộ `site/`: chỉ thấy số hợp đồng như `1000000000`, `500000000000` và màu CSS `#10241966`), nhưng bản gốc `source/` và ba tài liệu `editorial/` cũng đang công khai theo lựa chọn giữ nguyên liên kết đối chiếu.

## 11. Lên Git cho đồng nghiệp góp ý (lượt thứ ba)

Repo: `hieutachi/ai-student-handbook`. Đóng góp dự kiến theo kiểu **góp ý**, không phải chạy dịch vụ: sửa `chapters/*.md`, dựng lại, tạo Issue khi chỉ ghi nhận xét.

**Đã kiểm trước khi đẩy:** quét toàn bộ tệp văn bản trong repo theo mẫu khóa API, token GitHub, email thật và số diện thoại — 0 kết quả (đường dẫn tuyệt đối của máy biên tập cũng không xuất hiện trong tệp nào; chỉ ảnh chụp màn hình mới có thể chứa chuỗi đó, và ảnh chỉ chụp vùng trang sách). `.gitignore` loại `site/` (đầu ra), `*.qoder.site` (mô tả publish của máy biên tập), `__pycache__`, bản vá tạm và nhị kiểm.

**Sửa cho người dùng Linux/macOS:** `check_content.py` so SHA-256 của bản nguồn để chứng minh "không ghi đè nguồn gốc". Tệp nguồn lưu CRLF, nên clone trên hệ thống trả LF sẽ làm phép kiểm đỏ oan. Nay script chấp nhận cả hai hash (CRLF `704d10e9…`, LF `efbc9d5e…`) và ghi rõ `line_endings` đang thấy; `.gitattributes` ép LF để mọi máy có cùng một nội dung. Đã mô phỏng clone LF: chấp nhận.

**Chưa kiểm:** chưa clone thử trên máy Linux thật (mới mô phỏng bằng cách đổi dấu xuống dòng trong bộ nhớ); chưa có người góp ý thực tế nên chưa biết quy trình Issue/PR có vừa sức với đồng nghiệp hay không.
