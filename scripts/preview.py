"""Xem trước nội dung đã thực sự biên tập; chưa có ảnh thì ghi rõ đang chờ."""
from pathlib import Path
import sys
from markdown_it import MarkdownIt
from bs4 import BeautifulSoup
from production import load, save
ROOT=Path(__file__).resolve().parents[1]
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
for filename in sys.argv[1:]:
    path=ROOT/'chapters'/filename
    if not path.exists():raise FileNotFoundError(path)
    soup=BeautifulSoup(MarkdownIt('commonmark').enable('table').render(path.read_text(encoding='utf-8')),'html.parser')
    title=soup.h1.get_text(' ',strip=True)
    for img in list(soup.find_all('img')):
        asset=path.parent/img['src']
        if asset.exists():img['src']='../../assets/'+asset.name
        else:
            note=soup.new_tag('p');note['class']='pending';note.string='Hình dự kiến, chưa sản xuất: '+img.get('alt','');img.replace_with(note)
    for a in soup.find_all('a',href=True):
        href=a['href']
        if href.startswith('../'):a['href']='../../'+href[3:]
        elif href.split('#')[0].endswith('.md') and not href.startswith(('https:','http:')):
            a['href']='../../chapters/'+href
    for table in list(soup.find_all('table')):
        wrap=soup.new_tag('div',attrs={'class':'table-scroll'});table.wrap(wrap)
    for pre in list(soup.find_all('pre')):
        wrap=soup.new_tag('div',attrs={'class':'code-wrap'});pre.wrap(wrap)
    css=(ROOT/'website/reader.css').read_text(encoding='utf-8')
    page='<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+css+'main{margin:0}.preview-header{padding:16px 5vw;background:#20342d;color:#fff;font-size:13px}.preview-header a{color:#dce8d0}.preview-main{max-width:1000px;margin:auto;padding:30px 25px}.pending{font-size:13px;color:#58685f;border-left:2px solid #aaa;padding:10px}h1{font-size:44px}</style><body><header class="preview-header"><a href="../index.html">Về dashboard</a> · Bản xem trước nội dung; chưa thay cho kiểm thử bản xuất bản.</header><main class="preview-main prose">'+str(soup)+'</main></body></html>'
    target=ROOT/'dashboard/previews'/(path.stem+'.html');target.write_text(page,encoding='utf-8')
    state=load();previews=state.setdefault('previews',[]);previews[:]=[p for p in previews if p['source']!=filename]
    previews.append({'source':filename,'title':title,'path':'dashboard/previews/'+target.name})
    save(state,'Đã dựng xem trước nội dung thật: '+filename)
