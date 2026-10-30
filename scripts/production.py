"""Checkpoint cho dashboard. Chỉ đổi trạng thái khi công việc thực tế thay đổi."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / 'dashboard' / 'state.json'
TASKS = [
 ('audit',0,'Đọc đủ nguồn và kiểm kê chủ đề'),
 ('dashboard',0,'Dashboard và bản nguồn bất biến'),
 ('blueprint',1,'Bản đồ nội dung cũ → mới'),
 ('design',2,'Hệ thống thị giác và nhân vật'),
 ('chapter1',3,'Chương 1 · Bước vào thế giới AI'),
 ('chapter2',3,'Chương 2 · Trở thành người điều khiển AI'),
 ('chapter3',3,'Chương 3 · Đừng để AI suy nghĩ thay bạn'),
 ('chapter4',3,'Chương 4 · Sử dụng AI có trách nhiệm'),
 ('supplements',3,'Prompt, từ điển, thỏa thuận và Final Boss'),
 ('visuals',4,'Cover, opener và các sơ đồ học tập'),
 ('website',5,'Trình đọc offline và tương tác'),
 ('contentqa',6,'Rà soát nội dung và trải nghiệm sinh viên'),
 ('technicalqa',6,'Ví dụ, liên kết, ảnh và trình duyệt'),
 ('delivery',7,'Báo cáo, gói tải và bàn giao'),
]

def now():
    return datetime.now(timezone.utc).isoformat()

def load():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding='utf-8'))
    return {'title':'HỌC CNTT CÙNG AI','started':now(),'updated':now(), 'tasks':[{'id':i,'phase':p,'title':t,'status':'BACKLOG','output':'','issue':''} for i,p,t in TASKS], 'events':[], 'gallery':[], 'checks':[]}

def save(state, message):
    state['updated']=now()
    event={'time':state['updated'],'message':message}
    state['events'].append(event)
    state['percent']=round(100*sum(t['status']=='COMPLETED' for t in state['tasks'])/len(state['tasks']))
    payload=json.dumps(state,ensure_ascii=False,indent=2)
    STATE.write_text(payload,encoding='utf-8')
    (ROOT/'dashboard'/'state.js').write_text('window.STUDIO_DATA = '+payload+';\n',encoding='utf-8')
    with (ROOT/'dashboard'/'events.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps(event,ensure_ascii=False)+'\n')
    print(f"{state['percent']}% | {message}")

if __name__=='__main__':
    if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser()
    parser.add_argument('task',choices=[t[0] for t in TASKS]+['event'])
    parser.add_argument('status',choices=['BACKLOG','IN PROGRESS','REVIEW','COMPLETED','BLOCKED'])
    parser.add_argument('message')
    parser.add_argument('--output',default=None)
    parser.add_argument('--issue',default=None)
    args=parser.parse_args(); state=load()
    if args.task!='event':
        task=next(t for t in state['tasks'] if t['id']==args.task)
        task['status']=args.status
        if args.output is not None: task['output']=args.output
        if args.issue is not None: task['issue']=args.issue
    save(state,args.message)
