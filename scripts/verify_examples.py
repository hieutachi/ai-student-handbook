"""Kiểm ví dụ và đề lỗi chủ đích, giữ log trước/sau. Không gọi AI/API.
Chạy từ gốc dự án: python scripts/verify_examples.py
Nếu chỉ có compiler WSL: python scripts/verify_examples.py --wsl Ubuntu-22.04
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / 'reports'
LOG = REPORTS / 'test-runs.jsonl'
RESULTS = []


def run(label, command, expected_exit=0, expected_text=None, intentional=False):
    try:
        result = subprocess.run([str(x) for x in command], cwd=ROOT, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=90,
                                env={**os.environ,'PYTHONIOENCODING':'utf-8'})
        ok = result.returncode == expected_exit and (expected_text is None or expected_text in result.stdout)
        rec = {'time':datetime.now(timezone.utc).isoformat(),'label':label,
               'command':[str(x) for x in command],'exit_code':result.returncode,
               'expected_exit':expected_exit,'intentional_failure_fixture':intentional,
               'stdout':result.stdout,'stderr':result.stderr,'ok':ok}
    except (OSError,subprocess.TimeoutExpired) as error:
        rec = {'time':datetime.now(timezone.utc).isoformat(),'label':label,
               'command':[str(x) for x in command],'ok':False,'error':str(error)}
    RESULTS.append(rec)
    with LOG.open('a',encoding='utf-8') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
    print(('PASS ' if rec['ok'] else 'FAIL ')+label)
    if not rec['ok']: print(rec.get('stderr',rec.get('error','')))
    return rec['ok']


def linux_path(path):
    p=Path(path).resolve()
    if p.drive: return '/mnt/'+p.drive[0].lower()+p.as_posix()[2:]
    return str(p)


def cpp(source, output, distro, test=False, text=None, expected_exit=0, intentional=False):
    if distro:
        prefix=['wsl.exe','-d',distro,'--']
        src,out=linux_path(source),linux_path(output)
    else:
        prefix=[];src,out=str(source),str(output)
    built=run('C++ build '+source.name,prefix+['g++','-std=c++17','-Wall','-Wextra',src,'-o',out])
    if built:
        return run('C++ run '+source.name+(' --test' if test else ''),prefix+[out]+(['--test'] if test else []),expected_exit,text,intentional)
    return False


if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'):sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser();parser.add_argument('--wsl',default=None);args=parser.parse_args()
    run('Node version',['node','--version'])
    run('Python version',[sys.executable,'--version'])
    run('JavaScript data regression 34',['node',ROOT/'vi-du/nam-2-web/test_data.cjs'],expected_text='34 passed, 0 failed')
    run('SQLite standalone',[sys.executable,ROOT/'vi-du/minh-hoa-sqlite.py'],expected_text='PASS SQLite demo')
    run('Silver original intentional failures',['node',ROOT/'vi-du/final-boss/test_silver.cjs'],1,'6 passed, 6 failed',True)
    with tempfile.TemporaryDirectory(prefix='verification-',dir=REPORTS) as temp:
        tmp=Path(temp)
        silver=(ROOT/'vi-du/final-boss/silver.cjs').read_text(encoding='utf-8')
        before="  const amount = parseInt(input.trim(), 10);"
        after="  if (!/^[0-9]+$/.test(input.trim())) throw new Error('Chuoi sai');\n  const amount = Number(input.trim());"
        assert before in silver and 'total + item.value' in silver
        (tmp/'silver.cjs').write_text(silver.replace(before,after).replace('total + item.value','total + item.amount'),encoding='utf-8')
        shutil.copy2(ROOT/'vi-du/final-boss/test_silver.cjs',tmp/'test_silver.cjs')
        run('Silver patched temporary copy',['node',tmp/'test_silver.cjs'],expected_text='12 passed, 0 failed')
        if args.wsl or shutil.which('g++'):
            prefix=['wsl.exe','-d',args.wsl,'--'] if args.wsl else []
            run('Compiler version',prefix+['g++','--version'])
            cpp(ROOT/'vi-du/nam-1-cpp/vi_sinh_vien.cpp',tmp/'correct.exe',args.wsl,True,'9 passed, 0 failed')
            run('C++ correct sample',prefix+[linux_path(tmp/'correct.exe') if args.wsl else str(tmp/'correct.exe')],expected_text='60000') if (tmp/'correct.exe').exists() else None
            cpp(ROOT/'vi-du/nam-1-cpp/loi-bo-sot.cpp',tmp/'offbyone.exe',args.wsl,text='42000')
            cpp(ROOT/'vi-du/final-boss/bronze.cpp',tmp/'bronze.exe',args.wsl,text='5 passed, 4 failed',expected_exit=1,intentional=True)
            bronze=(ROOT/'vi-du/final-boss/bronze.cpp').read_text(encoding='utf-8')
            assert 'amount >= 1000000000LL' in bronze and 'i < n - 1' in bronze
            (tmp/'bronze-fixed.cpp').write_text(bronze.replace('amount >= 1000000000LL','amount > 1000000000LL').replace('i < n - 1','i < n'),encoding='utf-8')
            cpp(tmp/'bronze-fixed.cpp',tmp/'bronze-fixed.exe',args.wsl,text='9 passed, 0 failed')
        else:
            RESULTS.append({'label':'C++ compilation','ok':False,'error':'Chưa chạy: không thấy g++; có thể dùng --wsl tên-distro nếu đã cài.'})
    summary={'time':datetime.now(timezone.utc).isoformat(),'all_expected_checks_passed':all(r['ok'] for r in RESULTS),
             'checks':RESULTS,'source_sha256':hashlib.sha256((ROOT/'source/Cam-nang-AI-Sinh-vien.original.md').read_bytes()).hexdigest(),
             'note':'Intentional fixtures are expected to fail before repair. Temporary patched copies and binaries are removed after verification; rerun this script to reproduce.'}
    (REPORTS/'example-results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    sys.exit(0 if summary['all_expected_checks_passed'] else 1)
