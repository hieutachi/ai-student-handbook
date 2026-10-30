# 06 · THIẾT KẾ "CẨM NANG KHỞI ĐẦU" (hai cuốn)

Từ phiên bản này, tài liệu gồm **hai cuốn** dựng chung một pipeline:

| Cuốn | Nguồn | Đầu ra | Vai trò |
|---|---|---|---|
| **Cẩm nang khởi đầu** | `cam-nang/*.md` | `website/index.html`, `Cam-nang-khoi-dau.md` | Phần đọc đầu tiên. ≈ 25–29k từ, đọc trọn trong 2–3 giờ. Mỗi mục kết thúc bằng "Tự tìm hiểu thêm" trỏ sang Sổ tay. |
| **Sổ tay thực hành** | `chapters/*.md` | `website/so-tay.html`, `So-tay-thuc-hanh.md` | Nội dung đầy đủ đã kiểm chứng: bảy bài thực hành, bảy hồ sơ, benchmark, dự án tổng kết, đáp án, rubric, thỏa thuận học tập. |

Cẩm nang **không phải bản tóm tắt** của Sổ tay. Nó là điểm xuất phát: nêu ý chính, cho một việc nhỏ để thử, rồi để câu hỏi mở và chỉ đường. Sổ tay là nơi người học tìm tiếp khi muốn đi sâu.

## 1. Nguyên tắc biên soạn cẩm nang

1. **Một mục, một ý.** Người đọc phải trả lời được "mục này giúp tôi làm gì?" sau 60 từ đầu.
2. **Để câu hỏi mở.** Không in đáp án đầy đủ. Chỉ có "Gợi ý đối chiếu" ≤ 80 từ nêu tiêu chí tự biết đã đúng hướng.
3. **Ví dụ trước khái niệm.** Dùng Minh, Lan và ba khoản 35000 + 7000 + 18000 = 60000 làm ví dụ lồng trong đoạn văn; không tách thành tiểu mục "Tình huống" riêng ở từng mục.
4. **Không có lớp kiểm định.** Không rubric, không "Tiêu chí hoàn thành", không "Gợi ý cho giảng viên", không "Cấu trúc chương và cách sử dụng", không "Ôn tập tự trình bày lại", không bảng ca kiểm thử C1–C9 / W1–W10 / T1–T8 (chỉ nhắc tên và trỏ sang Sổ tay).
5. **Mã nguồn chỉ khi không thể thiếu.** Tối đa 2 khối mã (không phải `text`) mỗi mục, và phải **sao nguyên văn** từ `chapters/` (kiểm máy đối chiếu). Khối `text` (prompt mẫu) được viết mới nhưng ≤ 12 dòng.
6. **Mạch năm bước và câu chốt giữ nguyên:** Hiểu → Dùng → Giữ vững → Có trách nhiệm → Chọn; "AI hỗ trợ, người học quyết định" xuất hiện nguyên văn ở Chương 1 và Chương 5, và trong Lời giới thiệu.
7. **Văn phong:** theo `05_STYLE_GUIDE.md` mục 1 (thân thiện nhưng chuẩn mực). Được dùng "bạn" tối đa 5 lần mỗi chương; "chúng ta" khi cùng làm; không "mình/tôi" ngoài văn bản mẫu. Câu ngắn. Không dấu vết sản xuất, không liên kết `editorial/`, `source/`.
8. **Nhãn bằng chứng** giữ bốn nhãn chuẩn (*Tình huống hư cấu*, *Dữ liệu giả định*, *Chưa kiểm chứng*, *Kết quả mong đợi*) nhưng mỗi chương chỉ nhắc tối đa một câu ở đầu; tuyên bố phạm vi đầy đủ chỉ ở Lời giới thiệu.

## 2. Nhịp chuẩn của một mục (`## n.k.`)

```
## n.k. Tiêu đề tiếng Việt (nhãn tiếng Anh trong ngoặc nếu khớp hình/giao diện)

Một đoạn ≤ 60 từ: mục này trả lời câu hỏi gì, vì sao người học cần nó lúc này.

### Ý chính
Từ 2 đến 4 đoạn ngắn hoặc một bảng nhỏ, tổng ≤ 350 từ. Ví dụ Minh/Lan lồng trong đoạn.
(Chương 1 và Chương 5 được dùng 2 khối "Ý chính" khi mục có hai ý tách bạch; đặt tên
"### Ý chính 1 — …", "### Ý chính 2 — …".)

### Thử ngay (10 phút)
Một việc nhỏ, làm được mà không cần tài khoản AI, ≤ 120 từ. Có mục tiêu, có việc cụ thể, có thứ cần ghi lại.

### Gợi ý đối chiếu
≤ 80 từ. Tiêu chí tự kiểm, không phải lời giải. (Bản đọc tự gập mục này.)

### Tự tìm hiểu thêm
- **Câu hỏi mở:** một hoặc hai câu người học tự trả lời sau khi đọc Sổ tay hoặc thử thêm.
- **Từ khóa tra cứu:** 2–4 từ khóa tiếng Anh/Việt.
- **Trong Sổ tay thực hành:** [Tên mục](../chapters/<tệp>.md#muc-n-k) — một dòng nói ở đó có gì (bài đầy đủ, đáp án, bảng kiểm thử…).
```

Độ dài một mục: 550–800 từ (Chương 4: 400–600 cho mỗi tình huống). Mục "Thử ngay" và "Tự tìm hiểu thêm" là **bắt buộc** ở mọi mục đánh số.

## 3. Khung một chương

```
# CHƯƠNG n · TIÊU ĐỀ VIẾT HOA

Đoạn nối ≤ 100 từ: "Chương trước đã … Chương này …" và vị trí trong mạch năm bước.
Một câu nhắc nhãn bằng chứng nếu chương có số liệu giả định.

**Sau chương này, người học có thể:** 3–4 gạch đầu dòng.

![alt](../assets/<opener không cần; build tự chèn chapter-0n.svg>)   ← KHÔNG chèn opener trong Markdown.

## Tình huống mở đầu
≤ 150 từ, ngôi thứ ba, nêu dữ kiện và câu hỏi. Có thể chèn một hình minh họa ở đây hoặc trong mục đầu.

## n.1. …
## n.2. …
(…)

## Tóm tắt chương
4–6 gạch đầu dòng, ≤ 120 từ, rồi **Ba câu để tự kiểm** (không đáp án).

## Cầu nối sang chương sau
≤ 60 từ.

## Tài liệu tham khảo
3–6 nguồn chính thức, dạng liên kết Markdown, mỗi dòng ≤ 25 từ. Không URL trần.
```

Đánh số `## n.k.` phải liên tục từ 1. Không dùng `####`. Tiêu đề bắt đầu bằng "Gợi ý đối chiếu" được bản đọc tự gập; không dùng "Đáp án" trong cẩm nang.

## 4. Kế hoạch từng tệp (nguồn → cẩm nang)

Số từ đếm theo `len(text.split())`.

### `introduction.md` — 700–1.000 từ
Nguồn: `chapters/introduction.md`. Giữ: mục đích và đối tượng (ngắn), bảng năm bước, Minh/Lan và bảng ba khoản chi, một đoạn tuyên bố phạm vi gồm bốn nhãn, một đoạn "Cách dùng hai cuốn" (cẩm nang đọc trước; Sổ tay khi muốn đi sâu; liên kết `../chapters/introduction.md`). Bỏ: hợp đồng dữ liệu đầy đủ, bảng mục tiêu–bằng chứng, bảng tệp ví dụ, hai lộ trình (chỉ một câu: chọn nhánh Minh hoặc Lan), hướng dẫn trước/trong/sau buổi học. Không chèn `skill-map.svg`.

### `chapter-01.md` — 3.800–4.600 từ · "AI TRONG HỌC TẬP: VAI TRÒ, CÁCH HOẠT ĐỘNG VÀ GIỚI HẠN"
Nguồn: `chapters/chapter-01.md`.
- 1.1. Vai trò của AI trong học tập: giúp được gì, không giúp được gì, đâu là lạm dụng. Ý chính 1: ba vai trò hợp lý (giải thích, giả thuyết, kiểm tra) và điều AI làm tốt/kém. Ý chính 2: dùng để học và dùng để né học; nguyên tắc "AI hỗ trợ, người học quyết định" (nguyên văn). Thử ngay: phân loại 3 tình huống (lấy từ bài tự đánh giá, không in đáp án). Hình: `roles.svg`.
- 1.2. Nhận diện công cụ AI: model, provider và ứng dụng (AI Map). Ý chính: bốn câu hỏi model/provider/application/producer; API và key không phải bộ não tải về; cùng câu hỏi không đồng nghĩa cùng đầu vào. Giữ ví dụ 42000 và ba thẻ trả lời A/B/C ở dạng rút gọn (mỗi thẻ ≤ 40 từ). Hình: `ecosystem.svg`.
- 1.3. Phía sau một câu trả lời: prompt, context và token (Behind the Scene). Ý chính: prompt là lời giao việc, context là thông tin thực nhận; token và context window; training/inference/web search; hallucination thành câu hỏi kiểm chứng. Giữ số `9007199254740991` trong một câu. Hình: `token-context.svg`.
Thuật ngữ bắt buộc: Model, Provider, Application, API, token, context, hallucination.

### `chapter-02.md` — 4.200–5.200 từ · "ĐIỀU KHIỂN QUÁ TRÌNH LÀM VIỆC VỚI AI"
Nguồn: `chapters/chapter-02.md` (bảy bài thực hành). Cẩm nang gom thành **bốn mục**:
- 2.1. Chuẩn bị môi trường và hỏi trước khi cho phép sửa (gộp Bài 01–02). Thử ngay: tạo `bai-lam/`, sao chép một nhánh, viết một câu hỏi "chỉ giải thích, chưa sửa". Hình: `workspace.svg`.
- 2.2. Gỡ lỗi bằng bảng trace: khoản 18000 bị bỏ sót (Bài 03). **Bản đọc chèn mô phỏng trace ngay sau tiêu đề mục này.** Ý chính: cận vòng lặp `i < n - 1`, vì sao `long long`; trace là bằng chứng. Thử ngay: điền bảng trace ba lượt. Hình: `debugging.svg`. Được sao 1 khối C++ nguyên văn.
- 2.3. Lần theo dữ liệu trên Web: chuỗi trông giống số chưa phải số (Bài 04). Ý chính: ô nhập trả chuỗi, `NaN` và `undefined` khác nhau, `localStorage` không phải lưu bền vững. Được sao 1 khối JavaScript nguyên văn.
- 2.4. Giao việc có giới hạn, đọc diff và nghiệm thu (gộp Bài 05–07). Ý chính: Observe → Plan → Act → Test → Review; kiểm dependency thay vì cài; diff là đường quay lại; ba loại bằng chứng khi nghiệm thu (lệnh, ca biên, lời giải thích); chỉ **nhắc tên** các bảng C1–C9, W1–W10, T1–T8 và 34 ca kiểm thử, trỏ sang Sổ tay. Hình: `workflow.svg`.
Thuật ngữ bắt buộc: long long, NaN, undefined, localStorage, diff, 42000, 60000, Observe.

### `chapter-03.md` — 3.800–4.600 từ · "HỌC CHỦ ĐỘNG: DÙNG AI MÀ KHÔNG LẠM DỤNG"
Nguồn: `chapters/chapter-03.md`. **Năm mục**:
- 3.1. Bẫy câu trả lời tự tin (AI Trap): đúng một ca chưa phải đúng mọi ca; phản ví dụ nhỏ (danh sách một phần tử, 7000); vibe coding có kiểm soát. Hình: `ai-trap.svg`.
- 3.2. Dự đoán trước khi hỏi (Think First): phiếu dự đoán ba dòng; phiên 25 phút có AI (chỉ liệt kê sáu bước, mỗi bước một dòng).
- 3.3. Lần ngược luồng dữ liệu và giải thích lại (Reverse Engineering, Explain It Back): từ con số trên màn hình về nơi tạo ra; vượt qua "em hiểu rồi". Hình: `active-learning.svg`.
- 3.4. Tự quan sát trí nhớ và thử thách không dùng AI (Memory Experiment, No-AI Challenge): gộp hai mục nguồn; giữ ý "kết luận đúng mức bằng chứng".
- 3.5. Tự đánh giá cuối chương (Skill Unlocked): ba mức tự đánh giá, chu trình học chủ động và phiếu ba dòng. Mục này ngắn (≈ 400 từ) và "Thử ngay" là viết phiếu ba dòng.
Bỏ hẳn 3.6 (bài vận dụng dài) trong cẩm nang; trỏ sang Sổ tay ở 3.3 và 3.5.
Thuật ngữ bắt buộc: AI Trap, Think First, Explain It Back, Memory Experiment, 25, 7000, category.

### `chapter-04.md` — 4.400–5.400 từ · "SỬ DỤNG AI CÓ TRÁCH NHIỆM"
Nguồn: `chapters/chapter-04.md`. **Chín mục**:
- 4.1–4.7: bảy tình huống, **mỗi tình huống một trang (400–600 từ)** theo nhịp: đoạn mở (tình huống + câu hỏi phải quyết định, ≤ 120 từ) → Ý chính (nguyên tắc và vì sao, ≤ 250 từ, có thể 1 bảng nhỏ) → Thử ngay → Gợi ý đối chiếu → Tự tìm hiểu thêm (trỏ sang hồ sơ đầy đủ `#muc-4-k`). Tiêu đề: "4.k. Tình huống 0k — …" (giữ tên bảy hồ sơ nguồn). 4.7 giữ **mẫu khai báo AI** dạng khối `text` ≤ 10 dòng. 4.2 giữ tên hai văn bản 91/2025 và 131/2025 (một câu, nhãn *Chưa kiểm chứng*). Hình `security.svg` ở 4.1.
- 4.8. Ba lỗi kỹ thuật ở ranh giới dữ liệu: SQL, XSS và C++ (≈ 650 từ): mỗi lỗi một đoạn + một dòng nguyên tắc; giữ `textContent`, truy vấn tham số hóa; được sao 1 khối mã nguyên văn.
- 4.9. Danh sách kiểm tra trước khi nộp (≈ 400 từ): 8–10 dòng kiểm; "Thử ngay" là áp danh sách vào một bài gần nhất.
Thuật ngữ bắt buộc: SQL, textContent, lockfile, MIT, GPL, 91/2025, 131/2025, GitHub.

### `chapter-05.md` — 3.400–4.200 từ · "LỰA CHỌN AI VÀ MODEL PHÙ HỢP VỚI NHIỆM VỤ"
Nguồn: `chapters/chapter-05.md`. **Bốn mục**:
- 5.1. Chi phí sử dụng AI: hiểu cách tính trước khi gửi yêu cầu (AI Wallet). **Bản đọc chèn mô phỏng chi phí ngay sau tiêu đề mục.** Giữ ví dụ 50 request = 0.925 USD và nhắc 1000 request = 462500 VND (một câu); những token không nằm trong câu vừa gõ; cảnh báo ngân sách (budget alert) không phải trần chặn.
- 5.2. Ưu tiên phương án miễn phí: chỉ mua khi biết rõ còn thiếu gì (Free First). Giữ kế hoạch 300000 VND/15 tuần dưới dạng một bảng nhỏ; ưu đãi sinh viên và điều kiện tuổi/dữ liệu (một đoạn, nhãn *Chưa kiểm chứng*).
- 5.3. Đối chiếu công cụ theo tác vụ, không theo danh tiếng (AI Tool Battle). Ma trận tác vụ rút gọn (≤ 6 dòng); nguyên tắc benchmark công bằng (chỉ nêu ba đề A/B/C bằng một dòng mỗi đề, không in đề đầy đủ, trỏ sang Sổ tay `#muc-5-3`).
- 5.4. Ra quyết định trong 20 phút: phiếu 6 dòng để điền (khối `text`), không in phiếu đáp án; trỏ sang Sổ tay `#muc-5-4`. Kết bằng câu "AI hỗ trợ, người học quyết định" nguyên văn.
Thuật ngữ bắt buộc: token, budget, benchmark, 0.925, 462500, 300000.

### `final-project.md` — 500–800 từ · "DỰ ÁN TỔNG KẾT: LÀM, KIỂM, GIẢI THÍCH"
Nguồn: `chapters/final-boss.md`. Một trang: đề bài một đoạn; ba cấp Bronze/Silver/Gold mỗi cấp hai câu (thời lượng, sản phẩm); mười yêu cầu của bản nộp rút thành danh sách 10 dòng ngắn; đoạn "Bắt đầu từ đâu" trỏ sang `../chapters/final-boss.md` (đề đầy đủ, tệp `vi-du/final-boss/`, rubric 100 điểm, buổi bảo vệ). Hình: `final-boss.svg`. Không có mục đánh số, không "Thử ngay".

### `prompt-library.md` — 1.800–2.400 từ
Nguồn: `chapters/prompt-library.md`. Giữ **đủ 11 khối prompt P01–P11 nguyên văn** (khối `text`). Mỗi thẻ: tiêu đề `## P0k · …`, một câu "dùng khi", khối prompt, một câu "điều cần tự làm sau khi dùng". Mở đầu ≤ 120 từ. Bỏ phần "Ghi nhận sau khi dùng thẻ" dài.

### `glossary.md` — 1.200–1.800 từ
Nguồn: `chapters/glossary.md`. Giữ bảy nhóm `## …` và **bảy anchor `<a id="…"></a>`** y nguyên nguồn (xem nguồn để chép đúng). Mỗi thuật ngữ một dòng ≤ 25 từ; chỉ giữ thuật ngữ xuất hiện trong cẩm nang hoặc trong tên các mục Sổ tay được trỏ tới.

## 5. Liên kết

- Trong cẩm nang: `[…](chapter-02.md#muc-2-2)` (cùng cuốn) hoặc `[…](../chapters/chapter-02.md#muc-2-3)` (sang Sổ tay). **Chỉ dùng fragment dạng `#muc-n-k`** hoặc không có fragment (`../chapters/final-boss.md`, `../chapters/learning-agreement.md`, `../chapters/prompt-library.md`). Không dùng slug tiêu đề.
- Hình: `../assets/<tên>.svg`; alt lấy từ `assets/manifest.json`. Không chèn `chapter-0n.svg` và `cover.svg` (build tự chèn).
- Ví dụ: `../vi-du/...` như nguồn.
- Không liên kết tới `editorial/`, `source/`, `reports/`.

## 6. Kiểm máy (`scripts/verify_camnang.py`, `scripts/check_content.py`)

- Khoảng số từ của từng tệp theo mục 4 (có **trần**, không chỉ sàn).
- `## n.k.` liên tục; mỗi mục đánh số có `### Thử ngay` và `### Tự tìm hiểu thêm`; mọi "Gợi ý đối chiếu" ≤ 100 từ; không có tiêu đề "Đáp án", "Rubric", "Tiêu chí hoàn thành", "Gợi ý cho giảng viên".
- Mọi khối mã không phải `text` phải tồn tại nguyên văn trong `chapters/`.
- Mọi liên kết nội bộ phải trỏ tới tệp có thật và (nếu có fragment) tới `## n.k.` có thật trong tệp đích.
- Thuật ngữ bắt buộc theo mục 4; câu chốt nguyên văn ở introduction, chapter-01, chapter-05.
- "bạn" ≤ 5 lần/chương ngoài khối mã; không cụm dấu vết sản xuất.
