"""Đóng gói đúng tệp dự án; không đưa cache/profile/nhị phân vào bản giao."""
from pathlib import Path
import hashlib
import json
import zipfile
import sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'AI-Student-Handbook.zip'
EXCLUDED={'__pycache__','.git','node_modules'}
# site/ la dau ra cua ban online (tai tao bang scripts/build_online.py); khong nhan doi trong gói offline.
SKIP_TOP={'site'}
SUFFIXES={'.md','.html','.css','.js','.cjs','.py','.cpp','.svg','.json','.jsonl','.png','.pdf'}
files=[]
for p in sorted(ROOT.rglob('*')):
    rel=p.relative_to(ROOT)
    if rel.parts and rel.parts[0] in SKIP_TOP:continue
    if not p.is_file() or any(x in EXCLUDED or x.startswith(('verification-','browser-check-')) for x in rel.parts):continue
    if p.suffix.lower() not in SUFFIXES:continue
    if rel.as_posix()=='reports/package-manifest.json':continue
    files.append(p)
manifest={'files':[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(ROOT/'reports/package-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
files.append(ROOT/'reports/package-manifest.json')
with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files:z.write(p,Path(ROOT.name)/p.relative_to(ROOT))
with zipfile.ZipFile(OUT) as z:
    assert z.testzip() is None
    for p in files:assert z.read((Path(ROOT.name)/p.relative_to(ROOT)).as_posix())==p.read_bytes()
if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
print(json.dumps({'archive':str(OUT),'entries':len(files),'bytes':OUT.stat().st_size,'crc_and_bytes':'verified'},ensure_ascii=False,indent=2))
