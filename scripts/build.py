"""Dựng bản đọc đầy đủ từ nguồn Markdown; không gọi dịch vụ ngoài."""
from pathlib import Path
import html
import json
import re
import sys
import unicodedata
from urllib.parse import unquote
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[1]
CHAPTERS=ROOT/'chapters'
WEB=ROOT/'website'
PARTS=[
 ('outline.md','ban-do','Bản đồ nội dung',None),
 ('introduction.md','bat-dau','Lời giới thiệu',None),
 ('chapter-01.md','chuong-1','AI trong học tập: vai trò, cách hoạt động và giới hạn','01'),
 ('chapter-02.md','chuong-2','Điều khiển quá trình làm việc với AI','02'),
 ('chapter-03.md','chuong-3','Học chủ động: dùng AI mà không lạm dụng','03'),
 ('chapter-04.md','chuong-4','Sử dụng AI có trách nhiệm','04'),
 ('chapter-05.md','chuong-5','Lựa chọn AI và model phù hợp','05'),
 ('final-boss.md','final-boss','Dự án tổng kết',None),
 ('prompt-library.md','prompt-library','Thư viện prompt mẫu',None),
 ('glossary.md','glossary','Bảng thuật ngữ',None),
 ('learning-agreement.md','learning-agreement','Thỏa thuận học tập',None),
]
SUBTITLES={
 '01':'Hiểu vai trò của AI: giúp được gì, không giúp được gì, đâu là lạm dụng; nhận diện công cụ và cách một câu trả lời được tạo ra.',
 '02':'Bảy bài thực hành trên ứng dụng ViSinhVien: đọc mã, đặt câu hỏi, sửa lỗi, kiểm thử và nghiệm thu.',
 '03':'Tận dụng AI để học nhanh hơn mà vẫn giữ năng lực: tự dự đoán, tự làm, tự giải thích.',
 '04':'Bảy hồ sơ tình huống về dữ liệu, bảo mật, giấy phép và liêm chính học thuật.',
 '05':'Chọn AI, model và gói dịch vụ theo nhiệm vụ, rủi ro và ngân sách, sau khi đã hiểu vai trò, cách dùng và ranh giới.',
}
md=MarkdownIt('commonmark',{'html':False}).enable('table')
used=set();aliases={};soups={};sources={};nav=[];stats={}

def slug(text):
    s=unicodedata.normalize('NFD',text.lower()).replace('đ','d')
    s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')

def uid(base):
    v=base;i=2
    while v in used:v=f'{base}-{i}';i+=1
    used.add(v);return v

def demote(source):
    fence=None;out=[]
    for line in source.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            mark=match.group(1)
            if fence is None:fence=(mark[0],len(mark))
            elif mark[0]==fence[0] and len(mark)>=fence[1]:fence=None
        elif fence is None and re.match(r'^#{1,5} ',line):line='#'+line
        out.append(line)
    return '\n'.join(out)

BUDGET='''<aside class="widget" aria-labelledby="budget-title"><div class="eyebrow">AI WALLET / Mô phỏng cục bộ</div><h3 id="budget-title">50 request tốn bao nhiêu?</h3><p>Toàn bộ giá và tỷ giá dưới đây là giả định học tập, không phải báo giá hay hóa đơn thực tế. Đổi 50 thành 1000 rồi tính nhẩm hệ số tăng.</p><div class="budget-grid"><label>Số request (yêu cầu gửi dịch vụ)<input id="budget-calls" type="number" min="0" step="1" value="50"></label><label>Token vào / request<input id="budget-input" type="number" min="0" step="1" value="20000"></label><label>Token ra / request<input id="budget-output" type="number" min="0" step="1" value="5000"></label><label>USD / triệu token vào<input id="budget-inrate" type="number" min="0" step="0.01" value="0.30"></label><label>USD / triệu token ra<input id="budget-outrate" type="number" min="0" step="0.01" value="2.50"></label><label>Tỷ giá giả định VND/USD<input id="budget-fx" type="number" min="1" step="1" value="25000"></label></div><div class="budget-result" aria-live="polite"><strong id="budget-usd">0.925 USD</strong><span id="budget-vnd">≈ 23125 VND · chưa phí khác</span></div><p class="error" id="budget-error" hidden>Không nhận ô trống, số âm, số request/token/tỷ giá không nguyên hoặc giá trị quá lớn.</p><p>Chưa tính công cụ, cache, thuế và phí. Budget alert không mặc nhiên là trần chặn chi tiêu.</p></aside>'''
TRACE='''<aside class="widget" aria-labelledby="trace-title"><div class="eyebrow">THINK FIRST / Không phải trình biên dịch</div><h3 id="trace-title">18.000 đồng bị bỏ ở đâu?</h3><p>Chọn cận vòng lặp rồi đi từng lượt. Số tiền ở đây là dữ liệu giả; mô phỏng không thay việc biên dịch code C++.</p><div class="trace-items"><div class="trace-item"><small>i = 0 · CƠM TRƯA</small><b>35.000</b></div><div class="trace-item"><small>i = 1 · XE BUÝT</small><b>7.000</b></div><div class="trace-item"><small>i = 2 · VỞ GHI</small><b>18.000</b></div></div><div class="trace-controls"><label>Cận vòng lặp<select id="trace-mode"><option value="bug">Có lỗi: i &lt; n − 1</option><option value="fixed">Bản sửa: i &lt; n</option></select></label><button id="trace-next" type="button">Bước tiếp</button><button id="trace-reset" type="button">Làm lại</button></div><div id="trace-state" class="trace-state" role="status"></div></aside>'''

def quiz(number,question,options,answer,explanation):
    opts=''.join(f'<label><input type="radio" name="quiz-{number}" value="{i}"><span>{html.escape(s)}</span></label>' for i,s in enumerate(options))
    return f'<form class="widget quiz" data-answer="{answer}" data-explanation="{html.escape(explanation,quote=True)}"><div class="eyebrow">QUICK CHECK / Tự đối chiếu</div><fieldset><legend>{html.escape(question)}</legend>{opts}</fieldset><button type="submit">Đối chiếu lý do</button><p class="quiz-result" role="status" hidden></p></form>'

QUIZZES={
 'chapter-01.md':quiz(1,'Cùng model nhưng hai ứng dụng trả lời khác nhau. Kết luận nào có căn cứ nhất?',['Một ứng dụng chắc chắn nói dối.','Cần đối chiếu context, cấu hình và công cụ truy cập.','Model không có vai trò gì.'],1,'Tên model chưa mô tả toàn bộ lần dùng. Ngữ cảnh, cấu hình và công cụ có thể khác; phải kiểm dữ kiện trước kết luận.'),
 'chapter-05.md':quiz(5,'Gói dịch vụ bật cảnh báo ngân sách (budget alert). Kết luận nào có căn cứ nhất?',['Chắc chắn không bao giờ vượt ngân sách.','Cần kiểm tra cơ chế của đúng dịch vụ: cảnh báo chưa chắc là trần chặn chi tiêu.','Cảnh báo chỉ cần thiết khi dùng gói miễn phí.'],1,'Cảnh báo ngân sách thông báo khi chi tiêu chạm ngưỡng nhưng không mặc nhiên dừng việc sử dụng. Phải đọc cơ chế, phạm vi và độ trễ của dịch vụ cụ thể.'),
 'chapter-03.md':quiz(3,'Vòng lặp trả 0 với danh sách rỗng. Đủ để kết luận đã đúng chưa?',['Đủ vì rỗng là ca khó nhất.','Chưa; một khoản 7000 có thể vẫn bị bỏ.','Không cần test vì AI đã giải thích.'],1,'Ca rỗng không phân biệt hai cận đang xét. Thêm một phần tử là phản ví dụ nhỏ để bắt lỗi bỏ khoản duy nhất.'),
 'chapter-04.md':quiz(4,'Một key thật vừa xuất hiện trong kho được chia sẻ. Hành động ưu tiên?',['Xóa dòng rồi coi như xong.','Thu hồi/rotate theo đúng quyền, rồi phối hợp kiểm usage và dọn bản lưu.','Gửi nguyên key lên nhóm để mọi người kiểm.'],1,'Xóa dòng không vô hiệu hóa key và không xóa clone/cache. Không phát tán thêm bí mật; liên hệ người có thẩm quyền nếu không có quyền thu hồi.'),
}

for filename,part,title,number in PARTS:
    source=(CHAPTERS/filename).read_text(encoding='utf-8');sources[filename]=source
    # Keep standard Markdown's explicit empty anchors without enabling arbitrary HTML.
    explicit_anchors=re.findall(r'^<a id="([a-z][a-z0-9-]*)"></a>\s*\n(#{1,6}) (.+)$',source,re.M)
    render_source=re.sub(r'^<a id="[a-z][a-z0-9-]*"></a>\s*\n','',source,flags=re.M)
    soup=BeautifulSoup(md.render(render_source),'html.parser')
    first=soup.find('h1')
    if first:first.decompose()
    toc=[]
    for h in soup.find_all(re.compile(r'^h[1-6]$')):
        text=h.get_text(' ',strip=True);match=re.match(r'^(\d\.\d+)\b',text)
        ident=uid('muc-'+match.group(1).replace('.','-') if h.name=='h2' and match else part+'-'+slug(text))
        h['id']=ident;aliases[(filename,slug(text))]=ident
        if h.name=='h2':toc.append((ident,text))
    for anchor,level,label in explicit_anchors:
        target=aliases.get((filename,slug(label)))
        if target:aliases[(filename,anchor)]=target
    for table in list(soup.find_all('table')):
        wrapper=soup.new_tag('div',attrs={'class':'table-scroll','tabindex':'0','role':'region','aria-label':'Bảng nội dung, có thể cuộn ngang'})
        table.wrap(wrapper)
        for th in table.find_all('th'):th['scope']='col'
    for pre in list(soup.find_all('pre')):
        code=pre.find('code');language=next((c[9:] for c in code.get('class',[]) if c.startswith('language-')),'text')
        wrapper=soup.new_tag('div',attrs={'class':'code-wrap'});pre.wrap(wrapper)
        bar=soup.new_tag('div',attrs={'class':'code-top'});label=soup.new_tag('span');label.string={'text':'Prompt / Ghi chú','cpp':'C++','javascript':'JavaScript','bash':'Bash','powershell':'PowerShell'}.get(language,language)
        button=soup.new_tag('button',attrs={'type':'button','class':'copy-code','aria-label':'Sao chép khối '+language});button.string='Sao chép';bar.extend([label,button]);wrapper.insert(0,bar)
    for img in list(soup.find_all('img')):
        img['loading']='lazy';img['decoding']='async'
        p=img.parent;fig=soup.new_tag('figure')
        if p.name=='p' and len(p.find_all(True))==1 and not p.get_text(strip=True):p.replace_with(fig);fig.append(img.extract())
        else:img.wrap(fig)
        cap=soup.new_tag('figcaption');cap.string=img.get('alt','Hình minh họa')+' ';a=soup.new_tag('a',href=img['src'],target='_blank',rel='noopener');a.string='Xem hình lớn';cap.append(a);fig.append(cap)
    for heading in list(soup.find_all(['h2','h3','h4'])):
        if heading.parent is None:continue
        text=heading.get_text(' ',strip=True).lower()
        answer=text.startswith(('đáp án','gợi ý đối chiếu','lời giải tham khảo'))
        teacher=text.startswith(('speaker notes','gợi ý cho giảng viên'))
        if not(answer or teacher):continue
        level=int(heading.name[1]);siblings=[]
        for node in list(heading.next_siblings):
            if getattr(node,'name',None) and re.match(r'^h[1-6]$',node.name) and int(node.name[1])<=level:break
            siblings.append(node)
        detail=soup.new_tag('details',attrs={'class':'answer'+(' instructor' if teacher else '')})
        summary=soup.new_tag('summary',attrs={'id':heading['id']});summary.string=heading.get_text(' ',strip=True)+(' · mở sau khi tự thử' if answer else '')
        inside=soup.new_tag('div',attrs={'class':'answer-body'});detail.extend([summary,inside]);heading.replace_with(detail)
        for node in siblings:inside.append(node.extract())
    target=soup.find(id='muc-5-1') if filename=='chapter-05.md' else soup.find(id='muc-2-3') if filename=='chapter-02.md' else None
    if target:target.insert_after(BeautifulSoup(BUDGET if filename=='chapter-05.md' else TRACE,'html.parser'))
    if filename in QUIZZES:soup.append(BeautifulSoup(QUIZZES[filename],'html.parser'))
    soups[filename]=soup
    children=''.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i,t in toc)
    nav.append(f'<li class="toc-group"><a class="chapter-link" href="#{part}">{number+" / " if number else ""}{html.escape(title)}</a><ul>{children}</ul></li>')
    stats[filename]={'words_whitespace':len(source.split()),'sections':len(toc)}

# Chuyển liên kết giữa nguồn chương thành anchor của bản đọc đầy đủ.
part_by_file={f:p for f,p,_,_ in PARTS}
for filename,soup in soups.items():
    for a in soup.find_all('a',href=True):
        href=a['href'];path,_,fragment=href.partition('#');name=Path(unquote(path)).name
        if name in part_by_file:
            anchor=aliases.get((name,unquote(fragment))) or aliases.get((name,slug(unquote(fragment)))) if fragment else None
            if fragment and not anchor:raise ValueError(f'Unresolved source anchor in {filename}: {href}')
            a['href']='#'+(anchor or part_by_file[name])
        elif not path and fragment and not any(fragment==h.get('id') for h in soup.find_all(id=True)):
            if (filename,fragment) in aliases:a['href']='#'+aliases[(filename,fragment)]

sections=[]
for filename,part,title,number in PARTS:
    content=str(soups[filename])
    if number:
        sections.append(f'<section class="chapter" id="{part}"><header class="chapter-heading"><div class="chapter-num" aria-hidden="true">{number}</div><div><div class="eyebrow">CHƯƠNG {number}</div><h2>{html.escape(title)}</h2><p>{SUBTITLES[number]}</p></div></header><figure class="opener"><img src="../assets/chapter-{number}.svg" alt="Hình mở đầu Chương {int(number)}: {html.escape(title)}" loading="lazy"><figcaption>Hình mở đầu chương. Nhân vật và tình huống minh họa là hư cấu. <a href="../assets/chapter-{number}.svg" target="_blank" rel="noopener">Xem hình lớn</a></figcaption></figure><div class="prose">{content}</div><div class="chapter-end"><button type="button" data-complete="{int(number)}" aria-pressed="false">Tôi đã tự kiểm chương này</button><span>Tự ghi nhận, không phải chứng nhận năng lực.</span><a href="#dau-trang">Về đầu</a></div></section>')
    elif filename=='outline.md':sections.append(f'<section class="outline-map" id="{part}"><div class="eyebrow">BẢN ĐỒ NỘI DUNG</div><h2 class="section-title">{html.escape(title)}</h2><div class="prose">{content}</div></section>')
    elif filename=='introduction.md':sections.append(f'<section class="intro" id="{part}"><div class="prose">{content}</div></section>')
    else:sections.append(f'<section class="supplement" id="{part}"><div class="eyebrow">PHỤ LỤC VÀ CÔNG CỤ TỰ HỌC</div><h2 class="section-title">{html.escape(title)}</h2><div class="prose">{content}</div></section>')
css=(WEB/'reader.css').read_text(encoding='utf-8');js=(WEB/'reader.js').read_text(encoding='utf-8')
page='''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="description" content="Cẩm nang tự học về sử dụng AI cho sinh viên Công nghệ thông tin năm thứ nhất và năm thứ hai: năm chương, bảy bài thực hành, bảy hồ sơ tình huống và dự án tổng kết."><title>Học CNTT cùng AI · Cẩm nang sinh viên</title><style>'''+css+'''</style></head><body id="dau-trang"><a class="skip" href="#ban-do">Đến nội dung chính</a><aside class="sidebar" id="reader-toc" aria-label="Mục lục"><a class="brand" href="#dau-trang">HỌC CNTT<br>CÙNG AI<small>HIỂU CÔNG CỤ. GIỮ TƯ DUY.</small></a><label for="toc-search" class="sr-only">Lọc tên mục không dấu</label><input class="nav-search" id="toc-search" type="search" placeholder="Tìm tên mục…" autocomplete="off"><nav><ul class="toc">'''+''.join(nav)+'''</ul></nav><p id="search-empty" hidden>Không tìm thấy tên mục. Dùng Ctrl+F để tìm toàn văn.</p><div class="nav-foot"><p id="study-status" class="study-status"></p><a href="../Cam-nang-AI-Sinh-vien-Redesigned.md">Bản Markdown đầy đủ</a><br><a href="../vi-du/nam-2-web/index.html">Mở ViSinhVien</a><br><a href="../dashboard/index.html">Dashboard sản xuất</a><br><a href="../reports/04_QUALITY_REPORT.md">Báo cáo chất lượng</a></div></aside><button class="shade" id="nav-shade" type="button" aria-label="Đóng mục lục"></button><header class="topbar"><button class="mobile-menu" id="menu-toggle" type="button" aria-expanded="false" aria-controls="reader-toc">Mục lục</button><span class="top-label">TỰ HỌC CÓ HƯỚNG DẪN / KHOA CNTT · TLU</span><div class="tools"><button id="focus-toggle" type="button" aria-pressed="false">Tập trung</button><button id="font-down" type="button" aria-label="Giảm cỡ chữ">A−</button><button id="font-up" type="button" aria-label="Tăng cỡ chữ">A+</button><button id="print-guide" type="button">In / PDF</button></div><div class="scroll-track"><div id="scroll-progress"></div></div></header><main><div class="inner"><section class="hero"><div class="eyebrow">CẨM NANG TỰ HỌC / SINH VIÊN CNTT NĂM 1–2</div><div class="hero-grid"><div><h1>AI có thể viết code.<br><em>Người học cần hiểu<br>vì sao.</em></h1><p class="lede">Sử dụng AI như một công cụ học tập có kiểm soát, thông qua một ứng dụng quản lý chi tiêu nhỏ được xây dựng, kiểm thử và giải thích từng bước.</p><div class="hero-nav"><a href="#ban-do">Bản đồ nội dung</a><a href="#bat-dau">Lời giới thiệu</a><a href="#final-boss">Dự án tổng kết</a></div></div><a class="hero-art-link" href="../assets/cover.svg" target="_blank" rel="noopener" aria-label="Xem ảnh bìa cỡ lớn"><img class="hero-art" src="../assets/cover.svg" alt="Hình bìa: hai nhánh học C++ và Web cùng kiểm tra ba khoản chi giả định có tổng 60000 VND" fetchpriority="high"></a></div><nav class="route-map" aria-label="Năm chương"><a href="#chuong-1"><b>01</b>Hiểu vai trò của AI</a><a href="#chuong-2"><b>02</b>Dùng có kiểm soát</a><a href="#chuong-3"><b>03</b>Học mà không lạm dụng</a><a href="#chuong-4"><b>04</b>Có trách nhiệm</a><a href="#chuong-5"><b>05</b>Chọn công cụ phù hợp</a></nav><p class="edition">Phiên bản 30/10/2026 · Nhân vật và dữ liệu minh họa là hư cấu · Không phải quy định chính thức của Trường · Đọc và thực hành được ngoại tuyến</p></section>'''+''.join(sections)+'''<footer class="footer"><strong>Hiểu công cụ. Làm chủ kiến thức.</strong><p>Sử dụng có trách nhiệm. Kết luận chỉ dừng ở mức bằng chứng cho phép; điều chưa chứng minh được cần một phép thử tiếp theo.</p><p>Nội dung, mô phỏng và tự ghi tiến độ hoạt động cục bộ. Chỉ các liên kết tham khảo cần Internet khi người đọc chủ động mở. Tiến độ tự học do người học tự đánh dấu, không phải đánh giá tự động.</p></footer></div></main><div id="action-status" class="sr-only" role="status" aria-live="polite"></div><script>'''+js+'''</script></body></html>'''
(WEB/'index.html').write_text(page,encoding='utf-8')
combined=['# HỌC CNTT CÙNG AI · CẨM NANG SINH VIÊN\n\nHiểu công cụ · Làm chủ kiến thức · Sử dụng có trách nhiệm\n\nPhiên bản 30/10/2026. Năm chương, dự án tổng kết và các phụ lục.\n']
for f,_,_,_ in PARTS:
    s=demote(sources[f])
    for folder in ('assets','vi-du','chapters','editorial','reports','source'):
        s=s.replace('](../'+folder+'/',']('+folder+'/')
    for target_file in part_by_file:
        s=s.replace(']('+target_file,'](chapters/'+target_file)
    for block in re.findall(r'^```[^\n]*\n(.*?)^```',sources[f],re.M|re.S):assert block in s,(f,'code altered')
    combined.append(s)
(ROOT/'Cam-nang-AI-Sinh-vien-Redesigned.md').write_text('\n\n---\n\n'.join(combined)+'\n',encoding='utf-8')
parsed=BeautifulSoup(page,'html.parser');ids=[x['id'] for x in parsed.find_all(id=True)]
assert len(ids)==len(set(ids)),'Duplicate IDs'
broken=[]
for a in parsed.find_all('a',href=True):
    href=a['href']
    if href.startswith('#'):
        if href[1:] not in ids:broken.append(href)
    elif not href.startswith(('https:','http:','mailto:')):
        if not (WEB/unquote(href.split('#')[0])).exists():broken.append(href)
# QA report is created after preview; until then report as pending, not silently valid.
pending=[x for x in broken if x=='../reports/04_QUALITY_REPORT.md']
broken=[x for x in broken if x not in pending]
assert not broken,broken
for img in parsed.find_all('img'):assert (WEB/img['src']).exists(),img['src']
assert not parsed.find_all('script',src=True)
assert not parsed.find_all('link',rel='stylesheet')
assert '\ufffd' not in page
stats.update({'words_total':sum(len(s.split()) for s in sources.values()),'images':len(parsed.find_all('img')),'tables':len(parsed.find_all('table')),'code_blocks':len(parsed.find_all('pre')),'details':len(parsed.find_all('details')),'broken_links':broken,'pending_report':pending,'html_bytes':(WEB/'index.html').stat().st_size})
(ROOT/'reports/build-results.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False,indent=2))
