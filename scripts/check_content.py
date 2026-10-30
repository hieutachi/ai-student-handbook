"""Kiểm máy các bất biến; không thay review sư phạm hay kiểm chứng nguồn."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import subprocess
import sys
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
ROOT=Path(__file__).resolve().parents[1]
md=MarkdownIt('commonmark',{'html':False}).enable('table')
results=[]

def check(name,ok,evidence):
    results.append({'name':name,'ok':bool(ok),'evidence':evidence})

files=['outline.md','introduction.md','chapter-01.md','chapter-02.md','chapter-03.md','chapter-04.md','chapter-05.md','prompt-library.md','glossary.md','final-boss.md','learning-agreement.md']
texts={f:(ROOT/'chapters'/f).read_text(encoding='utf-8') for f in files}

def outside_fences(source):
    """Bỏ khối mã: HTML trong ví dụ minh họa không phải phụ thuộc trình xuất bản."""
    kept=[];fence=None
    for line in source.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            mark=match.group(1)
            if fence is None:fence=(mark[0],len(mark))
            elif mark[0]==fence[0] and len(mark)>=fence[1]:fence=None
            kept.append('')
        else:kept.append('' if fence else line)
    return '\n'.join(kept)

for f,s in texts.items():
    parsed=BeautifulSoup(md.render(s),'html.parser')
    broken=[]
    for node in parsed.find_all(['a','img']):
        value=node.get('href') or node.get('src') or ''
        target=value.split('#')[0]
        if not target or target.startswith(('http:','https:','mailto:')):continue
        if not (ROOT/'chapters'/unquote(target)).exists():broken.append(value)
    check('Local source links '+f,not broken,broken)
    check('UTF-8 '+f,'\ufffd' not in s,'No Unicode replacement character')
    check('No raw HTML dependency '+f,not re.search(r'^<(?:script|iframe|div|details)\b',outside_fences(s),re.M),'Plain Markdown with fenced code')

for n,minimum,sections in [(1,6000,3),(2,8500,7),(3,7500,7),(4,7500,12),(5,6000,4)]:
    f=f'chapter-0{n}.md';s=texts[f];hs=re.findall(r'^## '+str(n)+r'\.(\d+)\.',s,re.M)
    check(f'Ch{n} complete numbered structure',hs==[str(i) for i in range(1,sections+1)],hs)
    check(f'Ch{n} depth floor (not quality score)',len(s.split())>=minimum,{'whitespace_words':len(s.split()),'minimum':minimum})

required={
 'chapter-01.md':['Model','Provider','Application','API','token','context','hallucination','9007199254740991','AI hỗ trợ, người học quyết định'],
 'chapter-05.md':['benchmark','0.925','462500','300000','budget','AI hỗ trợ, người học quyết định'],
 'chapter-02.md':['C1','C9','W1','W10','T1','T8','34','long long','NaN','undefined','localStorage','PowerShell','diff'],
 'chapter-03.md':['AI TRAP','MEMORY EXPERIMENT','NO-AI','EXPLAIN IT BACK','25','7000','category'],
 'chapter-04.md':['SQL','textContent','registry','lockfile','MIT','GPL','91/2025','131/2025','GitHub'],
 'prompt-library.md':['P01','P02','P03','P04','P05','P06','P07','P08','P09','P10','P11'],
 'final-boss.md':['BRONZE','SILVER','GOLD','100','hai lỗi','60000','500000000000'],
 'outline.md':['bảy Mission','bảy hồ sơ','P01','Bronze','Silver','Gold','60000','500000000000','chưa kiểm','hư cấu'],
}
for f,terms in required.items():
    missing=[t for t in terms if t.casefold() not in texts[f].casefold()]
    check('Topic presence '+f,not missing,{'missing':missing,'note':'Presence only; human review checks meaning.'})
orig=ROOT/'source/Cam-nang-AI-Sinh-vien.original.md'
raw=orig.read_bytes()
CRLF,LF=bytes([13,10]),bytes([10])
# Ban goc luu CRLF. Git tra LF khi clone tren Linux/macOS, nen ca hai dang deu hop le
# voi dieu kien "noi dung khong doi"; byte chi khac o ky tu xuong dong.
digest={'crlf':hashlib.sha256(raw).hexdigest(),'lf':hashlib.sha256(raw.replace(CRLF,LF)).hexdigest()}
form='crlf' if CRLF in raw else 'lf'
check('Original source unchanged',digest['crlf']=='704d10e9603d0b494196795b9b45ae701dfc1caadeab54bcc3d76c4c7ae53772' or digest['lf']=='efbc9d5ed7587fe453c8a45a0b7bc877be0c3783bed5eff1076de15185570468',{'line_endings':form,'sha256':digest[form],'note':'Content snapshot; CRLF and LF forms of the same text are both accepted'})
expected=['cover','chapter-01','chapter-02','chapter-03','chapter-04','chapter-05','ecosystem','roles','token-context','workspace','workflow','debugging','active-learning','ai-trap','security','final-boss','skill-map']
check('All seventeen illustrations',all((ROOT/'assets'/(x+'.svg')).exists() for x in expected),expected)
# Hai bản đọc: cẩm nang (index.html) và sổ tay (so-tay.html) dùng chung kho hình.
paths=set()
for page in ('index.html','so-tay.html'):
    soup=BeautifulSoup((ROOT/'website'/page).read_text(encoding='utf-8'),'html.parser')
    paths|={Path(i['src']).stem for i in soup.find_all('img',src=True)}
check('All illustrations used across both books',all(x in paths for x in expected),sorted(paths))
# Cẩm nang khởi đầu: cấu trúc, độ dài có trần, liên kết chéo và nguồn gốc khối mã (scripts/verify_camnang.py).
cam=subprocess.run([sys.executable,str(ROOT/'scripts/verify_camnang.py')],capture_output=True,text=True,encoding='utf-8')
check('Cam nang khoi dau invariants',cam.returncode==0,[l for l in cam.stdout.splitlines() if 'FAIL' in l or 'THIẾU' in l] or 'verify_camnang.py OK')
cam_words=sum(len((ROOT/'cam-nang'/f).read_text(encoding='utf-8').split()) for f in ['introduction.md','chapter-01.md','chapter-02.md','chapter-03.md','chapter-04.md','chapter-05.md','final-project.md','prompt-library.md','glossary.md'] if (ROOT/'cam-nang'/f).exists())
check('Cam nang total length ceiling (not quality score)',22000<=cam_words<=30000,{'whitespace_words':cam_words,'range':'22000–30000'})
check('At least eleven copyable prompt cards',len(BeautifulSoup(md.render(texts['prompt-library.md']),'html.parser').find_all('pre'))>=11,'P01–P11')
check('No unmarked real secret literals',not re.search(r'sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}','\n'.join(texts.values())),'Pattern scan only, not proof of all possible personal data')
report={'checks':results,'all_passed':all(r['ok'] for r in results),'limitation':'Mechanical coverage and structural checks, not factual proof or pedagogical certification.'}
(ROOT/'reports/content-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
for r in results:print(('PASS ' if r['ok'] else 'FAIL ')+r['name']+((' '+str(r['evidence'])) if not r['ok'] else ''))
sys.exit(0 if report['all_passed'] else 1)
