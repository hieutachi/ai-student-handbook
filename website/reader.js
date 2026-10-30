(() => {
'use strict';
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const announce = text => { $('#action-status').textContent = text; };
const normalize = s => s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase();
// Mỗi cuốn (cẩm nang, sổ tay) giữ tiến độ riêng trên cùng origin.
const storageKey = 'ai-handbook-study-v2' + (document.body.dataset.book ? '-' + document.body.dataset.book : '');
let state = {font:18,done:[]};
let persistent = true;
try {
  const saved = JSON.parse(localStorage.getItem(storageKey) || 'null');
  if(saved && typeof saved === 'object') {
    if(Number.isInteger(saved.font) && saved.font>=16 && saved.font<=22) state.font=saved.font;
    if(Array.isArray(saved.done)) state.done=[...new Set(saved.done.filter(x=>['1','2','3','4','5'].includes(x)))];
  }
} catch { persistent=false; }
function save() {
  if(!persistent) return;
  try {localStorage.setItem(storageKey,JSON.stringify(state));}
  catch {persistent=false;studyStatus();}
}
function studyStatus() {
  $('#study-status').textContent=state.done.length+'/5 chương tự đánh dấu đã kiểm'+(persistent?' · lưu trên trình duyệt này':' · bộ nhớ tạm, có thể mất khi tải lại');
}
function applyFont() {document.documentElement.style.setProperty('--font',state.font+'px');}
applyFont(); studyStatus();
$('#font-down').addEventListener('click',()=>{state.font=Math.max(16,state.font-1);applyFont();save();announce('Cỡ chữ '+state.font);});
$('#font-up').addEventListener('click',()=>{state.font=Math.min(22,state.font+1);applyFont();save();announce('Cỡ chữ '+state.font);});
$$('[data-complete]').forEach(button=>{
  const id=button.dataset.complete;
  const update=()=>{const done=state.done.includes(id);button.setAttribute('aria-pressed',String(done));button.textContent=done?'Đã tự kiểm · bấm để bỏ đánh dấu':'Tôi đã tự kiểm chương này';};update();
  button.addEventListener('click',()=>{state.done=state.done.includes(id)?state.done.filter(x=>x!==id):[...state.done,id];update();save();studyStatus();announce('Đã cập nhật ghi chú tự học. Đây không phải chứng nhận năng lực.');});
});
$('#toc-search').addEventListener('input',event=>{
  const query=normalize(event.target.value.trim());let count=0;
  $$('.toc-group').forEach(group=>{
    const heading=group.querySelector('.chapter-link');
    const match=normalize(heading.textContent).includes(query);
    const items=[...group.querySelectorAll('ul li')];let children=0;
    items.forEach(item=>{const visible=!query||match||normalize(item.textContent).includes(query);item.hidden=!visible;if(visible)children++;});
    const visible=!query||match||children>0;group.hidden=!visible;if(visible)count++;
  });
  $('#search-empty').hidden=count>0;
});
function menu(open){const wasOpen=document.body.classList.contains('nav-open');document.body.classList.toggle('nav-open',open);$('#menu-toggle').setAttribute('aria-expanded',String(open));if(open)$('#toc-search').focus();else if(wasOpen&&$('#reader-toc').contains(document.activeElement))$('#menu-toggle').focus();}
$('#menu-toggle').addEventListener('click',()=>menu(!document.body.classList.contains('nav-open')));
$('#nav-shade').addEventListener('click',()=>menu(false));
$$('.toc a').forEach(a=>a.addEventListener('click',()=>menu(false)));
document.addEventListener('keydown',e=>{if(e.key==='Escape')menu(false);});
$('#focus-toggle').addEventListener('click',()=>{const active=document.body.classList.toggle('focus');$('#focus-toggle').setAttribute('aria-pressed',String(active));$('#focus-toggle').textContent=active?'Hiện mục lục':'Tập trung';});
function scroll(){const max=document.documentElement.scrollHeight-innerHeight;$('#scroll-progress').style.width=(max>0?100*scrollY/max:0)+'%';}
window.addEventListener('scroll',scroll,{passive:true});window.addEventListener('resize',scroll);scroll();
const observer=new IntersectionObserver(entries=>{entries.forEach(entry=>{if(entry.isIntersecting){$$('.toc a.active').forEach(a=>a.classList.remove('active'));const a=$$('.toc a').find(a=>a.getAttribute('href')==='#'+entry.target.id);if(a)a.classList.add('active');}});},{rootMargin:'-10% 0px -75% 0px'});
$$('.chapter,.supplement,.prose h2').forEach(e=>observer.observe(e));
async function copy(text){
  if(navigator.clipboard?.writeText){try{await navigator.clipboard.writeText(text);return true;}catch{}}
  const t=document.createElement('textarea');t.value=text;t.style.position='fixed';t.style.left='-9999px';document.body.append(t);t.select();let ok=false;try{ok=document.execCommand('copy');}catch{}t.remove();return ok;
}
$$('.copy-code').forEach(b=>b.addEventListener('click',async()=>{const text=b.closest('.code-wrap').querySelector('code').textContent;const ok=await copy(text);b.textContent=ok?'Đã sao chép':'Chọn mã để chép';announce(ok?'Đã sao chép khối nội dung.':'Trình duyệt chặn sao chép. Hãy chọn nội dung và sao chép thủ công.');setTimeout(()=>b.textContent='Sao chép',1800);}));
let beforePrint=[];
window.addEventListener('beforeprint',()=>{beforePrint=$$('details').map(d=>[d,d.open]);beforePrint.forEach(([d])=>d.open=true);});
window.addEventListener('afterprint',()=>{beforePrint.forEach(([d,open])=>d.open=open);beforePrint=[];});
$('#print-guide').addEventListener('click',()=>window.print());
const budgetIds=['calls','input','output','inrate','outrate','fx'];
function budget(){
  if(!$('#budget-calls'))return;
  const raw=budgetIds.map(x=>$('#budget-'+x).value),v=raw.map(Number);
  const valid=raw.every(x=>x.trim()!=='')&&v.every(x=>Number.isFinite(x)&&x>=0)&&v[5]>0&&[0,1,2,5].every(i=>Number.isSafeInteger(v[i]));
  const usd=valid?v[0]*(v[1]*v[3]+v[2]*v[4])/1e6:NaN,vnd=usd*v[5];
  const ok=valid&&Number.isFinite(usd)&&Number.isFinite(vnd)&&vnd<=Number.MAX_SAFE_INTEGER;
  $('#budget-error').hidden=ok;
  $('#budget-usd').textContent=ok?usd.toFixed(3)+' USD':'—';
  $('#budget-vnd').textContent=ok?'≈ '+String(Math.round(vnd))+' VND · chưa phí khác':'Kiểm tra số nhập; chưa có ước tính hợp lệ.';
}
budgetIds.forEach(x=>$('#budget-'+x)?.addEventListener('input',budget));budget();
let traceIndex=0,traceTotal=0;
function trace(reset=false){
  if(!$('#trace-mode'))return;
  if(reset){traceIndex=0;traceTotal=0;}
  const count=$('#trace-mode').value==='bug'?2:3;
  $$('.trace-item').forEach((e,i)=>{e.classList.toggle('added',i<traceIndex);e.classList.toggle('current',i===traceIndex-1);});
  const ended=traceIndex>=count;
  $('#trace-state').textContent=traceIndex===0?'n = 3 · total = 0. Dự đoán chỉ số nào sẽ được cộng trước khi bấm.':ended?'Dừng tại i = '+traceIndex+' · tổng '+traceTotal.toLocaleString('vi-VN')+' VND. '+(count===2?'Vở ghi chưa được cộng.':'Đã cộng đủ ba khoản; vẫn cần ca biên và dữ liệu sai.'):'Vừa cộng i = '+(traceIndex-1)+' · tổng tạm '+traceTotal.toLocaleString('vi-VN')+' VND. Chưa kết luận đúng/sai chỉ từ tổng trung gian.';
  $('#trace-next').disabled=ended;
}
$('#trace-next')?.addEventListener('click',()=>{const limit=$('#trace-mode').value==='bug'?2:3;if(traceIndex<limit){traceTotal+=[35000,7000,18000][traceIndex];traceIndex++;}trace();});
$('#trace-reset')?.addEventListener('click',()=>trace(true));$('#trace-mode')?.addEventListener('change',()=>trace(true));trace();
$$('.quiz').forEach(quiz=>{
  quiz.addEventListener('submit',event=>{event.preventDefault();const selected=quiz.querySelector('input:checked');const out=quiz.querySelector('.quiz-result');if(!selected){out.hidden=false;out.textContent='Chọn một phương án trước khi đối chiếu.';return;}const correct=selected.value===quiz.dataset.answer;out.textContent=(correct?'Đúng hướng. ':'Chưa đúng. ')+quiz.dataset.explanation;out.hidden=false;});
});
})();
