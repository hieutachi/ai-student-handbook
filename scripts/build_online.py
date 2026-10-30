"""Dựng bản Online: một thư mục tĩnh tự chứa, mọi liên kết trỏ về gốc site.

Bản offline giữ nguyên dashboard và cấu trúc thư mục dự án. Bản online bỏ liên kết
dashboard nội bộ, đổi mọi đường dẫn ../ thành đường dẫn tương đối từ gốc site, và
chỉ sao những tệp mà trang thực sự liên kết. Không gọi dịch vụ mạng.
"""
from pathlib import Path
import json
import re
import shutil
import sys
from urllib.parse import unquote
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
HTML = ROOT / 'website' / 'index.html'

# Những nhánh được publish. reports/ chỉ lấy tệp .md; ảnh chụp và nhật ký ở lại máy.
COPY_DIRS = ['assets', 'vi-du', 'editorial', 'source']
COPY_FILES = ['Cam-nang-AI-Sinh-vien-Redesigned.md']
COPY_SELECTIVE = {'reports': ['04_QUALITY_REPORT.md']}
EXCLUDE_SUFFIX = {'.png', '.pdf', '.jsonl', '.exe', '.out'}


def copy_tree(name):
    src, dst = ROOT / name, SITE / name
    written = []
    for path in sorted(src.rglob('*')):
        if path.is_dir():
            continue
        if path.suffix.lower() in EXCLUDE_SUFFIX or '__pycache__' in path.parts:
            continue
        target = dst / path.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        written.append(target.relative_to(SITE).as_posix())
    return written


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    copied = []
    for name in COPY_DIRS:
        copied += copy_tree(name)
    for name, files in COPY_SELECTIVE.items():
        for filename in files:
            src = ROOT / name / filename
            if not src.exists():
                raise SystemExit(f'Thiếu tệp bắt buộc: {src}')
            (SITE / name).mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, SITE / name / filename)
            copied.append(f'{name}/{filename}')
    for filename in COPY_FILES:
        shutil.copy2(ROOT / filename, SITE / filename)
        copied.append(filename)

    page = HTML.read_text(encoding='utf-8')
    # Dashboard là công cụ sản xuất nội bộ: ẩn khỏi trang chủ, không phải nội dung sinh viên cần.
    page = re.sub(r'<a href="\.\./dashboard/index\.html">Dashboard sản xuất</a>(<br>)?', '', page)
    before = len(re.findall(r'(?:src|href)="\.\./', page))
    page = page.replace('src="../', 'src="').replace('href="../', 'href="')
    after = len(re.findall(r'(?:src|href)="\.\./', page))
    if after:
        raise SystemExit(f'Còn {after} đường dẫn ../ sau khi viết lại')

    # Trang demo nằm sâu trong site/vi-du/...: đường dẫn về sách phải theo vị trí mới.
    for demo in sorted((SITE / 'vi-du').rglob('*.html')):
        text = demo.read_text(encoding='utf-8')
        demo.write_text(text.replace('../../website/index.html', '../../index.html'), encoding='utf-8')

    (SITE / 'index.html').write_text(page, encoding='utf-8')

    # Kiểm bằng BeautifulSoup: mã HTML trong khối <pre> chỉ là văn bản, không phải liên kết.
    soup = BeautifulSoup((SITE / 'index.html').read_text(encoding='utf-8'), 'html.parser')
    for tag in soup.find_all('pre'):
        tag.decompose()
    missing = []
    for value in {a.get('href') for a in soup.find_all('a', href=True)} | {i.get('src') for i in soup.find_all('img', src=True)}:
        if not value or value.startswith(('http:', 'https:', 'mailto:', 'data:', '#')):
            continue
        if not (SITE / unquote(value.split('#')[0])).exists():
            missing.append(value)
    for demo in sorted((SITE / 'vi-du').rglob('*.html')):
        dsoup = BeautifulSoup(demo.read_text(encoding='utf-8'), 'html.parser')
        for tag in dsoup.find_all('pre'):
            tag.decompose()
        for value in {a.get('href') for a in dsoup.find_all('a', href=True)} | {i.get('src') for i in dsoup.find_all('img', src=True)} | {s.get('src') for s in dsoup.find_all('script', src=True)}:
            if not value or value.startswith(('http:', 'https:', 'mailto:', 'data:', '#')):
                continue
            if not (demo.parent / unquote(value.split('#')[0])).resolve().exists():
                missing.append(f'{demo.relative_to(SITE).as_posix()} -> {value}')
    if missing:
        raise SystemExit(f'Liên kết hỏng trong bản online: {sorted(missing)}')

    svg = len(list((SITE / 'assets').glob('*.svg')))
    if svg != 17:
        raise SystemExit(f'Sau khi sao chỉ còn {svg}/17 hình SVG')

    total = sum(f.stat().st_size for f in SITE.rglob('*') if f.is_file())
    summary = {
        'site_directory': SITE.relative_to(ROOT).as_posix(),
        'entry': 'site/index.html',
        'rewritten_parent_links': before,
        'remaining_parent_links': after,
        'files_copied': len(copied) + 1,
        'svg_images': svg,
        'total_bytes': total,
        'excluded_from_online': ['dashboard/', 'scripts/', 'chapters/ (nguồn biên tập)',
                                 'reports/*.png|pdf|jsonl', 'website/ (nguồn CSS/JS)'],
        'broken_links': missing,
    }
    (ROOT / 'reports' / 'online-build.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
