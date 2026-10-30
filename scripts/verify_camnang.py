"""Kiểm máy các bất biến của Cẩm nang khởi đầu (cam-nang/). Dùng: python scripts/verify_camnang.py [tệp...]

Kiểm cấu trúc, độ dài, liên kết và nguồn gốc khối mã; không thay review sư phạm.
Thoát mã 1 khi có lỗi. Xem editorial/06_CAM_NANG_SPEC.md mục 6.
"""
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'cam-nang'
SO_TAY = ROOT / 'chapters'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# (sàn, trần) số từ; số mục đánh số; thuật ngữ bắt buộc
PLAN = {
    'introduction.md': ((700, 1000), 0, ['Minh', 'Lan', '60000', 'AI hỗ trợ, người học quyết định', 'Sổ tay']),
    'chapter-01.md': ((3800, 4600), 3, ['Model', 'Provider', 'Application', 'API', 'token', 'context', 'hallucination', '9007199254740991', 'AI hỗ trợ, người học quyết định']),
    'chapter-02.md': ((4200, 5200), 4, ['long long', 'NaN', 'undefined', 'localStorage', 'diff', '42000', '60000', 'Observe', 'C1', 'W1', 'T1', '34']),
    'chapter-03.md': ((3800, 4600), 5, ['AI Trap', 'Think First', 'Explain It Back', 'Memory Experiment', '25', '7000', 'category']),
    'chapter-04.md': ((4400, 5400), 9, ['SQL', 'textContent', 'lockfile', 'MIT', 'GPL', '91/2025', '131/2025', 'GitHub']),
    'chapter-05.md': ((3400, 4200), 4, ['token', 'budget', 'benchmark', '0.925', '462500', '300000', 'AI hỗ trợ, người học quyết định']),
    'final-project.md': ((500, 800), 0, ['Bronze', 'Silver', 'Gold', '60000']),
    'prompt-library.md': ((1800, 2600), 0, ['P01', 'P02', 'P03', 'P04', 'P05', 'P06', 'P07', 'P08', 'P09', 'P10', 'P11']),
    'glossary.md': ((1200, 1800), 0, ['token', 'context', 'hallucination', 'diff']),
}
BANNED_HEADINGS = ('đáp án', 'rubric', 'tiêu chí hoàn thành', 'gợi ý cho giảng viên', 'cấu trúc chương', 'ôn tập: tự trình bày', 'lời giải tham khảo')
BANNED_PHRASES = ['bổ sung biên tập', 'bản nguồn', 'lần biên tập', 'kế thừa từ', 'tái thiết kế', 'source audit']


def blocks(s):
    out = []
    cur = None
    lang = None
    for line in s.splitlines():
        m = re.match(r'^\s*(`{3,}|~{3,})(\S*)', line)
        if m and cur is None:
            cur = []
            lang = m.group(2) or 'text'
        elif m and cur is not None:
            out.append((lang, '\n'.join(cur)))
            cur = None
        elif cur is not None:
            cur.append(line)
    return out


def prose(s):
    keep = []
    fence = False
    for line in s.splitlines():
        if re.match(r'^\s*(`{3,}|~{3,})', line):
            fence = not fence
            continue
        if not fence:
            keep.append(line)
    return '\n'.join(keep)


def sections(s):
    """Tách theo tiêu đề; trả [(level, title, body)]."""
    parts = re.split(r'^(?=#{1,6} )', s, flags=re.M)
    out = []
    for p in parts:
        m = re.match(r'(#{1,6}) (.+)', p)
        if m:
            out.append((len(m.group(1)), m.group(2).strip(), p))
    return out


so_tay_blocks = set()
so_tay_numbered = {}
for f in SO_TAY.glob('*.md'):
    t = f.read_text(encoding='utf-8')
    for lang, body in blocks(t):
        if lang != 'text':
            so_tay_blocks.add(body.strip())
    so_tay_numbered[f.name] = set(re.findall(r'^## (\d\.\d+)\.', t, re.M))


def numbered_anchors(text):
    return {'muc-' + n.replace('.', '-') for n in re.findall(r'^## (\d\.\d+)\.', text, re.M)}


targets = sys.argv[1:] or list(PLAN)
exit_code = 0
for name in targets:
    path = SRC / name
    fails, warns = [], []
    if not path.exists():
        print(f'{name}: THIẾU TỆP')
        exit_code = 1
        continue
    text = path.read_text(encoding='utf-8')
    (lo, hi), n_sections, terms = PLAN[name]
    words = len(text.split())
    if not lo <= words <= hi:
        fails.append(f'Số từ {words} ngoài khoảng {lo}–{hi}')
    if '�' in text:
        fails.append('Có ký tự thay thế Unicode')
    missing = [t for t in terms if t.casefold() not in text.casefold()]
    if missing:
        fails.append(f'Thiếu thuật ngữ bắt buộc: {missing}')

    m = re.match(r'chapter-0(\d)\.md', name)
    if m:
        n = int(m.group(1))
        hs = re.findall(r'^## ' + str(n) + r'\.(\d+)\.', text, re.M)
        if hs != [str(i) for i in range(1, n_sections + 1)]:
            fails.append(f'Đánh số ## {n}.k. phải là 1..{n_sections}, thấy {hs}')
        secs = sections(text)
        for i, (lvl, title, body) in enumerate(secs):
            if lvl == 2 and re.match(str(n) + r'\.\d+\.', title):
                end = next((j for j in range(i + 1, len(secs)) if secs[j][0] <= 2), len(secs))
                subs = [t for l, t, _ in secs[i + 1:end] if l == 3]
                if not any(t.startswith('Thử ngay') for t in subs):
                    fails.append(f'Mục "{title[:50]}" thiếu "### Thử ngay"')
                if not any(t.startswith('Tự tìm hiểu thêm') for t in subs):
                    fails.append(f'Mục "{title[:50]}" thiếu "### Tự tìm hiểu thêm"')
                body_words = sum(len(b.split()) for _, _, b in secs[i:end])
                # Chương 1 và 5 được dùng hai khối "Ý chính"; tình huống 4.1–4.7 là một trang.
                cap = 650 if n == 4 and re.match(r'4\.[1-7]\.', title) else 1300 if n in (1, 5) else 900
                if body_words > cap:
                    warns.append(f'Mục "{title[:50]}" dài {body_words} từ (> {cap})')
            if lvl >= 4:
                fails.append(f'Dùng tiêu đề cấp {lvl}: "{title[:50]}"')
            low = title.lower()
            if any(low.startswith(b) for b in BANNED_HEADINGS):
                fails.append(f'Tiêu đề không được có trong cẩm nang: "{title[:60]}"')
            if low.startswith('gợi ý đối chiếu'):
                end = next((j for j in range(i + 1, len(secs)) if secs[j][0] <= lvl), len(secs))
                gw = sum(len(b.split()) for _, _, b in secs[i:end]) - len(title.split()) - 1
                if gw > 100:
                    fails.append(f'"{title[:40]}" dài {gw} từ (> 100): đang in đáp án thay vì tiêu chí')
        for h in ('## Tóm tắt chương', '## Cầu nối sang chương sau', '## Tài liệu tham khảo', '## Tình huống mở đầu'):
            if h not in text:
                fails.append(f'Thiếu "{h}"')
        if re.search(r'chapter-0' + str(n) + r'\.svg|cover\.svg', text):
            fails.append('Không chèn opener/cover; build tự chèn')

    for lang, body in blocks(text):
        if lang != 'text' and body.strip() not in so_tay_blocks:
            fails.append(f'Khối mã `{lang}` không có nguyên văn trong chapters/: "{body.strip()[:60]}…"')
        if lang == 'text' and len(body.splitlines()) > 14 and name != 'prompt-library.md':
            warns.append(f'Khối text {len(body.splitlines())} dòng (> 12)')

    p = prose(text)
    for link in re.findall(r'\]\(([^)\s]+)\)', p):
        if link.startswith(('http:', 'https:', 'mailto:')):
            continue
        file_part, _, frag = link.partition('#')
        file_part = unquote(file_part)
        if file_part.startswith(('../editorial', '../source', '../reports')):
            fails.append(f'Liên kết tới tệp sản xuất: {link}')
            continue
        target = (SRC / file_part).resolve() if file_part else path
        if not target.exists():
            fails.append(f'Liên kết hỏng: {link}')
            continue
        if frag:
            if not re.fullmatch(r'muc-\d-\d+', frag):
                fails.append(f'Fragment phải dạng muc-n-k: {link}')
            elif frag not in numbered_anchors(target.read_text(encoding='utf-8')):
                fails.append(f'Không có mục {frag} trong {target.name}: {link}')
    for b in BANNED_PHRASES:
        c = len(re.findall(b, p, re.I))
        if c:
            warns.append(f'Cụm dấu vết sản xuất "{b}": {c} lần')
    ban = len(re.findall(r'\bbạn\b', p, re.I))
    if ban > 5:
        warns.append(f'"bạn" {ban} lần (> 5)')
    if re.search(r'\b(mình|tôi)\b', p, re.I):
        warns.append('"mình/tôi" ngoài khối mã')
    bare = re.findall(r'(?<!\()https?://\S+', p)
    if bare:
        warns.append(f'URL trần: {len(bare)}')

    if name == 'glossary.md':
        src_anchors = re.findall(r'<a id="([^"]+)"></a>', (SO_TAY / 'glossary.md').read_text(encoding='utf-8'))
        new_anchors = re.findall(r'<a id="([^"]+)"></a>', text)
        if src_anchors != new_anchors:
            fails.append(f'Anchor thuật ngữ phải giữ y nguyên: {src_anchors} -> {new_anchors}')
    if name == 'prompt-library.md':
        src = [b for l, b in blocks((SO_TAY / 'prompt-library.md').read_text(encoding='utf-8')) if l == 'text']
        new = [b for l, b in blocks(text) if l == 'text']
        if len(new) < 11 or any(b.strip() not in {s.strip() for s in src} for b in new):
            fails.append('Phải giữ đủ 11 khối prompt nguyên văn từ chapters/prompt-library.md')

    print(f'{name}: {words} từ')
    for f in fails:
        print('  FAIL', f)
    for w in warns:
        print('  WARN', w)
    print('  OK' if not fails else '  CÓ LỖI')
    if fails:
        exit_code = 1
sys.exit(exit_code)
