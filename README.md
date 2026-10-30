# HỌC CNTT CÙNG AI · Cẩm nang khởi đầu và Sổ tay thực hành

Tài liệu dành cho sinh viên CNTT năm 1–2, gồm **hai cuốn** dựng chung một pipeline:

| Cuốn | Nguồn | Bản đọc | Dành cho |
|---|---|---|---|
| **Cẩm nang khởi đầu** (≈ 27.000 từ) | `cam-nang/` | `website/index.html` | Đọc đầu tiên, 2–3 giờ. Mỗi mục: một ý chính, một việc nhỏ để thử, gợi ý tự tìm hiểu thêm. |
| **Sổ tay thực hành** (≈ 83.000 từ) | `chapters/` | `website/so-tay.html` | Bản đầy đủ: bảy bài thực hành, bảy hồ sơ, benchmark, dự án tổng kết, đáp án và rubric. |

Nhân vật Minh/Lan, dữ liệu và tình huống là hư cấu. Không phải quy định chính thức của Trường Đại học Thủy lợi hoặc ứng dụng tài chính thật. Thiết kế hai cuốn ghi trong `editorial/06_CAM_NANG_SPEC.md`.

**Bản đọc online:** https://ai-student-handbook-8nchu0xfadn.qoder.website (cẩm nang) và `…/so-tay.html` (sổ tay) — mở không cần tài khoản, không cần tải gì.

## Góp ý cho bản này

| Muốn làm gì | Cách nhanh nhất |
|---|---|
| Đọc thử 5 phút | Mở link online ở trên, đọc **Lời giới thiệu** rồi một mục bất kỳ của Chương 1 |
| Ghi nhận xét mà không sửa tệp | Mở một **Issue**, nêu cuốn + chương + mục (ví dụ "Cẩm nang 4.3" hoặc "Sổ tay 4.3, Hồ sơ 03") và điều bạn thấy |
| Sửa trực tiếp câu chữ | Đổi tệp trong `cam-nang/` (cẩm nang) hoặc `chapters/` (sổ tay), rồi chạy `python scripts/build.py` để tạo lại cả hai bản đọc |
| Góp ý về ví dụ code | Sửa trong `vi-du/`, chạy `python scripts/verify_examples.py`; đề Final Boss **cố ý** còn test đỏ |

Hai điều cần giữ khi góp ý: **không đưa dữ liệu thật** (điểm danh sinh viên, MSSV, email thật, ảnh chụp màn hình có tài khoản, API key) vào Issue, pull request hay commit — dùng số giả như `35000, 7000, 18000` và `demo001@example.invalid`; và **giữ nguyên nhãn** HƯ CẤU / GIẢ ĐỊNH / chưa kiểm, vì đó là căn cứ để người sau biết phần nào đã được chứng minh.

## Mở và sử dụng

1. Giải nén toàn bộ gói hoặc `git clone`, giữ nguyên cấu trúc thư mục.
2. Mở [website/index.html](website/index.html) (Cẩm nang khởi đầu) bằng trình duyệt hiện đại. Không cần server, tài khoản AI hoặc Internet để đọc và dùng mô phỏng. [website/so-tay.html](website/so-tay.html) là Sổ tay thực hành; mỗi mục "Tự tìm hiểu thêm" trong cẩm nang trỏ thẳng sang bài tương ứng.
3. Chọn nhánh Minh (C++) hoặc Lan (Web); cả hai cuốn đi theo năm bước Hiểu, Dùng, Giữ vững, Có trách nhiệm, Chọn. Dùng mục lục, ô tìm không dấu, cỡ chữ, gợi ý đối chiếu gập và thư viện prompt.
4. Trước khi sửa ví dụ, tạo bản sao dưới `bai-lam/` theo hướng dẫn chương 2. Không dùng chi tiêu thật, API key, mật khẩu hay dữ liệu cá nhân.
5. Mở [dashboard/index.html](dashboard/index.html) để xem hồ sơ sản xuất và kết quả. Dashboard tự đọc checkpoint cục bộ; nó không chạy Agent khi bạn mở gói.

Bản Markdown ghép [Cam-nang-khoi-dau.md](Cam-nang-khoi-dau.md) và [So-tay-thuc-hanh.md](So-tay-thuc-hanh.md) dùng để xem/chỉnh nội dung. Muốn sửa lâu dài rồi xuất bản lại, chỉnh các tệp dưới `cam-nang/` hoặc `chapters/`, không sửa bản ghép vì lần dựng sau sẽ tạo lại nó.

[Web ViSinhVien](vi-du/nam-2-web/index.html) là demo có dữ liệu giả, không backend/đăng nhập. localStorage tùy trình duyệt và có fallback RAM. Tiến độ tự học trong cẩm nang cũng chỉ lưu cục bộ, không là chứng nhận hoặc tài khoản đồng bộ.

## Kiểm chứng và giới hạn

Đọc [báo cáo chất lượng](reports/04_QUALITY_REPORT.md) để biết nội dung nào đã chạy, được xem bằng trình duyệt nào, và giới hạn còn lại. Nhật ký có cả lần thất bại; đề Final Boss ban đầu cố ý có test không đạt. Không bỏ các dòng FAIL rồi nói tất cả code gốc đều đúng.

- Demo C++ đúng: 9 ca. Demo lỗi `loi-bo-sot.cpp`: cố ý cho 42000, không có `--test`.
- Demo dữ liệu Web bản mới: 34 ca. Nguồn cũ có 33; đã bổ sung ca từ chối `category` dạng mảng sau phát hiện lỗi schema.
- Final Boss Bronze: hai lỗi chủ đích, 9 ca. Silver: hai lỗi chủ đích, 12 ca; độc lập với demo Web.
- SQLite: fixture trong RAM riêng, không phải backend và không có toàn bộ ràng buộc của Web.

## Cấu trúc

| Thư mục | Nội dung |
|---|---|
| `source/` | Bản Markdown gốc giữ nguyên, phục vụ đối chiếu |
| `editorial/` | Kiểm kê đầy đủ, bản đồ tái cấu trúc, hệ thiết kế, quy chuẩn văn phong, thiết kế hai cuốn |
| `cam-nang/` | Cẩm nang khởi đầu: năm chương ngắn, dự án tổng kết một trang, thư viện prompt, bảng thuật ngữ |
| `chapters/` | Sổ tay thực hành: năm chương đầy đủ, dự án tổng kết, mở đầu và các phần phụ trợ |
| `assets/` | Hình SVG tự tạo và manifest mô tả mục đích |
| `website/` | Bản đọc, CSS/JS nguồn; HTML nhúng CSS/JS khi xuất |
| `dashboard/` | Tiến độ sản xuất, nhật ký checkpoint và xem trước |
| `vi-du/` | Ví dụ và đề lỗi có chủ đích |
| `reports/` | Kết quả test, ảnh kiểm giao diện, báo cáo chất lượng |
| `scripts/` | Công cụ dựng, kiểm chứng, dashboard, đóng gói |

## Bản online

Trang đã publish: **https://ai-student-handbook-8nchu0xfadn.qoder.website** (cẩm nang; sổ tay ở `/so-tay.html`) — mở bằng trình duyệt thường, không cần tài khoản, gửi link cho lớp được. Nội dung giống bản offline; khác biệt duy nhất là bỏ liên kết dashboard sản xuất.

Bản online được dựng từ bản offline, không sửa tay:

```bash
python scripts/build.py          # tạo website/index.html (cẩm nang) và website/so-tay.html (sổ tay)
python scripts/build_online.py   # xuất site/ với đường dẫn tuyệt đối và liên kết đã kiểm
node scripts/browser_check.cjs --site   # kiểm chính site/ trong Chrome, không phải bản đang mở
```

`site/` là đầu ra, không phải nguồn: xoá đi dựng lại được, và không vào ZIP offline (trùng nội dung). Muốn cập nhật trang đã publish, sửa `cam-nang/` hoặc `chapters/`, chạy lại ba lệnh trên rồi tạo một lượt prepare + publish mới.

## Dựng lại — chỉ dành cho người biên tập

Repo khai báo `.gitattributes` ép LF cho tệp văn bản: kiểm tra "bản nguồn không đổi" so bằng mã hash byte, nếu Git tự đổi sang CRLF khi clone trên Linux/macOS thì phép kiểm đó báo đỏ dù nội dung y nguyên. `check_content.py` nay chấp nhận cả hai dạng và ghi rõ đang thấy dạng nào.

Đọc sách không cần cài thư viện. Dựng lại cần Python 3 với `markdown-it-py`, `beautifulsoup4` trong môi trường biên tập; script hình dùng thư viện chuẩn. Không có lệnh tải và thực thi script từ mạng.

Đứng tại gốc `AI-Student-Handbook`:

```bash
python scripts/make_visuals.py
python scripts/build.py
python scripts/check_content.py        # bất biến của cả hai cuốn; gọi verify_camnang.py cho cẩm nang
python scripts/verify_camnang.py       # riêng cẩm nang: khoảng số từ có trần, nhịp mục, liên kết chéo, nguồn khối mã
```

Kiểm ví dụ cần Node.js, Python `sqlite3`, C++17. Không cần npm install:

```bash
python scripts/verify_examples.py
```

Trên Windows chỉ có g++ trong WSL đã cài, chọn đúng tên distro sẵn có của bạn, ví dụ:

```bash
python scripts/verify_examples.py --wsl Ubuntu-22.04
```

Kiểm trình duyệt tự động dùng Chrome/Edge cục bộ với profile tạm, Node.js >=22, không dùng phiên đăng nhập của người dùng:

```bash
node scripts/browser_check.cjs
```

Thêm `--pdf` để tạo bản in kiểm tra tại `reports/print-preview.pdf`. Script không tự chứng minh đã xem hết từng trang in; cần đọc báo cáo và xem bố cục thực.

Đóng gói lại:

```bash
python scripts/package.py
```

ZIP tạo ở thư mục cha, chỉ gồm tệp dự án theo danh sách cho phép; không kèm executable, cache, profile trình duyệt hay node_modules. Chạy test và sửa vấn đề trước khi đóng gói, không dùng ZIP cũ thay cho kết quả vừa dựng.

## Tiếp tục từ checkpoint

Dashboard đọc `dashboard/state.json` và `state.js`; `events.jsonl` là nhật ký bổ sung. Khi tiếp tục biên tập, mở các đầu ra hiện có, đọc issue trong task và trạng thái `REVIEW/BLOCKED`. Không xóa lịch sử để làm dự án trông như chưa từng gặp lỗi. Chỉ thay trạng thái khi công việc thực sự thay đổi; phần trăm tính từ số đầu việc hoàn tất, không phải đồng hồ hay ước lượng thời gian.
