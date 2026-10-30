'use strict';
// Chrome headless trong profile tạm; không dùng profile/tài khoản của người dùng.
// Chỉ dùng module chuẩn Node >=22, không cần npm install.
const fs=require('node:fs');
const path=require('node:path');
const os=require('node:os');
const cp=require('node:child_process');
const {pathToFileURL}=require('node:url');
const ROOT=path.resolve(__dirname,'..');
// --site: kiểm bản online trong site/ thay vì bản offline website/.
const SITE_MODE=process.argv.includes('--site');
const BASE=SITE_MODE?path.join(ROOT,'site'):ROOT;
const BOOK=path.join(BASE,SITE_MODE?'index.html':'website/index.html');
const DEMO=path.join(BASE,'vi-du/nam-2-web/index.html');
const ASSETS=path.join(BASE,'assets');
const REPORTS=path.join(ROOT,'reports');
const chrome=[process.env.CHROME_PATH,'C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe','/usr/bin/google-chrome','/usr/bin/chromium'].filter(Boolean).find(x=>fs.existsSync(x));
if(!chrome)throw new Error('Không tìm thấy Chromium/Chrome; đặt CHROME_PATH tới trình duyệt đã cài.');
const profile=fs.mkdtempSync(path.join(os.tmpdir(),'ai-handbook-browser-'));
const results=[], errors=[], requests=[];
const runId=new Date().toISOString();
const log=event=>fs.appendFileSync(path.join(REPORTS,'browser-runs.jsonl'),JSON.stringify({runId,time:new Date().toISOString(),...event})+'\n');
log({event:'start'});
let browser,ws;
function result(name,ok,evidence){const entry={name,ok,evidence};results.push(entry);log({event:'check',...entry});console.log((ok?'PASS ':'FAIL ')+name);}
(async()=>{
 try {
  browser=cp.spawn(chrome,['--headless','--disable-gpu','--disable-background-networking','--no-first-run','--no-default-browser-check','--remote-debugging-port=0','--user-data-dir='+profile,'about:blank'],{stdio:['ignore','ignore','pipe']});
  const endpoint=await new Promise((resolve,reject)=>{let text='';const t=setTimeout(()=>reject(new Error('DevTools startup timeout')),20000);browser.stderr.on('data',buf=>{text+=buf.toString();const m=text.match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m){clearTimeout(t);resolve(m[1]);}});browser.once('error',reject);});
  const discovery=await fetch(endpoint.replace(/^ws:/,'http:').replace(/\/devtools\/browser\/.*/,'/json/version')).then(r=>r.json());
  fs.writeFileSync(path.join(REPORTS,'browser-interface.json'),JSON.stringify(discovery,null,2));
  ws=new WebSocket(endpoint);await new Promise((resolve,reject)=>{ws.addEventListener('open',resolve,{once:true});ws.addEventListener('error',reject,{once:true});});
  let seq=0;const pending=new Map();const events=[];
  ws.addEventListener('message',event=>{const m=JSON.parse(event.data);if(m.id){const p=pending.get(m.id);if(p){pending.delete(m.id);clearTimeout(p.timer);if(m.error)p.reject(new Error(JSON.stringify(m.error)));else p.resolve(m.result);}}else{events.forEach(f=>f(m));if(m.method==='Runtime.exceptionThrown')errors.push(m.params.exceptionDetails);if(m.method==='Network.requestWillBeSent')requests.push(m.params.request.url);}});
  const send=(method,params={},sessionId)=>new Promise((resolve,reject)=>{const id=++seq;const timer=setTimeout(()=>{pending.delete(id);reject(new Error('CDP timeout '+method));},method==='Page.printToPDF'?180000:90000);pending.set(id,{resolve,reject,timer});ws.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})}));});
  const {targetId}=await send('Target.createTarget',{url:'about:blank'});const {sessionId}=await send('Target.attachToTarget',{targetId,flatten:true});
  const page=(method,params={})=>send(method,params,sessionId);
  await page('Page.enable');await page('Runtime.enable');await page('Network.enable');
  const evaluate=async expression=>{const r=await page('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw new Error(JSON.stringify(r.exceptionDetails));return r.result.value;};
  const navigate=async file=>{const wait=new Promise((resolve,reject)=>{const timer=setTimeout(()=>{events.splice(events.indexOf(f),1);reject(new Error('Page load timeout '+file));},30000);const f=m=>{if(m.sessionId===sessionId&&m.method==='Page.loadEventFired'){clearTimeout(timer);events.splice(events.indexOf(f),1);resolve();}};events.push(f);});const navigation=await page('Page.navigate',{url:pathToFileURL(file).href});if(navigation.errorText)throw new Error('Navigation failed: '+navigation.errorText);await wait;await evaluate('Promise.race([Promise.all([document.fonts?.ready,...[...(document.images||[])].map(i=>i.decode().catch(()=>{}))]),new Promise(r=>setTimeout(r,20000))]).then(()=>{document.documentElement.style.scrollBehavior="auto";return true;})');};
  const viewport=(width,height)=>page('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false});
  const screenshot=async name=>{await evaluate('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');const image=await page('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});fs.writeFileSync(path.join(REPORTS,name),Buffer.from(image.data,'base64'));};
  if(process.argv.includes('--preview')){
   await navigate(path.join(ROOT,'dashboard/previews/chapter-02.html'));
   for(const width of [1440,375]){await viewport(width,850);const sizes=await evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})');result('Chapter 2 preview width '+width,sizes.width===width&&sizes.scrollWidth<=width,sizes);await screenshot('chapter2-preview-'+width+'.png');}
   result('Preview content and runtime',errors.length===0&&await evaluate("document.querySelector('h1')?.textContent.includes('CHƯƠNG 2')"),errors);
   fs.writeFileSync(path.join(REPORTS,'preview-browser-results.json'),JSON.stringify({time:new Date().toISOString(),browser:discovery.Browser,results,errors},null,2));
   await send('Browser.close');if(results.some(r=>!r.ok))process.exitCode=1;return;
  }
  if(!SITE_MODE){await viewport(1440,1000);await navigate(path.join(ROOT,'dashboard/index.html'));
  result('Dashboard 14 tasks / 8 phases',await evaluate("document.querySelectorAll('.card').length===14&&document.querySelectorAll('.phase').length===8"),'Read state.js from file://');
  await screenshot('dashboard-final.png');}
  await navigate(BOOK);
  result('Book loaded',await evaluate("document.querySelectorAll('.chapter').length===4&&document.querySelectorAll('[data-complete]').length===4"),'4 full chapters, 4 self-check controls');
  const c3=await evaluate("(()=>{const s=document.getElementById('chuong-3').innerText;const words=['AI TRAP','PREDICT BEFORE ASKING','REVERSE ENGINEERING','MEMORY EXPERIMENT','25-MINUTE NO-AI CHALLENGE','EXPLAIN IT BACK','SKILL UNLOCKED'];return {missing:words.filter(w=>!s.includes(w)),h2:document.querySelectorAll('#chuong-3 h3').length};})()");
  result('Chapter 3 keeps its seven teaching moves',c3.missing.length===0,c3);
  const c4=await evaluate("(()=>{const s=document.getElementById('chuong-4').innerText;const dossiers=[...s.matchAll(/Hồ sơ 0(\\d)/g)].map(m=>m[1]);return {dossiers:[...new Set(dossiers)],hasClinic:s.includes('Phòng khám'),hasRubric:s.includes('Rubric'),hasChecklist:s.includes('Checklist')};})()");
  result('Chapter 4 has dossiers 1–7 plus clinic, rubric, checklist',c4.dossiers.length===7&&c4.hasClinic&&c4.hasRubric&&c4.hasChecklist,c4);
  result('Answers are collapsed until opened',await evaluate("[...document.querySelectorAll('details.answer')].every(d=>!d.open)&&document.querySelectorAll('details.answer').length>=20"),'Answer blocks ship closed; print opens them temporarily');
  // Ảnh dưới màn hình có loading="lazy": ép tải rồi chờ decode để kiểm tệp thật, không đổi hành vi đọc.
  const images=await evaluate("(async()=>{const list=[...document.images];list.forEach(i=>{i.loading='eager';});await Promise.race([Promise.all(list.map(i=>i.decode().catch(()=>{}))),new Promise(r=>setTimeout(r,15000))]);return [list.length,list.filter(i=>!(i.complete&&i.naturalWidth>0)).map(i=>i.getAttribute('src'))];})()");
  result('Images decoded',images[0]===16&&images[1].length===0,images);
  await screenshot('reader-desktop.png');
  const anchors=await evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash)");result('All book anchors exist',anchors.length===0,anchors);
  const budget=await evaluate("(()=>{let e=document.getElementById('budget-calls');e.value='1000';e.dispatchEvent(new Event('input',{bubbles:true}));return [document.getElementById('budget-usd').textContent,document.getElementById('budget-vnd').textContent];})()");result('Budget 1000 calls',budget[0]==='18.500 USD'&&budget[1].includes('462500'),budget);
  result('Reject blank budget',await evaluate("(()=>{let e=document.getElementById('budget-calls');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}));return !document.getElementById('budget-error').hidden;})()"),'No fabricated estimate for empty field');
  await evaluate("document.getElementById('budget-calls').value='50';document.getElementById('budget-calls').dispatchEvent(new Event('input',{bubbles:true}));");
  const trace=await evaluate("(()=>{let b=document.getElementById('trace-next');b.click();b.click();let bad=document.getElementById('trace-state').textContent;let mode=document.getElementById('trace-mode');mode.value='fixed';mode.dispatchEvent(new Event('change'));b.click();b.click();b.click();return [bad,document.getElementById('trace-state').textContent];})()");result('Trace 42000 / 60000',trace[0].includes('42.000')&&trace[1].includes('60.000'),trace);
  await evaluate("document.getElementById('muc-2-3').scrollIntoView();");await screenshot('reader-mission-desktop.png');
  result('TOC non-accented search',await evaluate("(()=>{let e=document.getElementById('toc-search');e.value='tu dien';e.dispatchEvent(new Event('input',{bubbles:true}));let ok=[...document.querySelectorAll('.toc-group')].some(g=>!g.hidden&&g.textContent.includes('Từ điển'));e.value='';e.dispatchEvent(new Event('input',{bubbles:true}));return ok;})()"),'Unicode NFD and đ/d normalization');
  result('Self-check saves local progress',await evaluate("(()=>{document.querySelector('[data-complete=\"1\"]').click();return document.querySelector('[data-complete=\"1\"]').getAttribute('aria-pressed')==='true';})()"),'User-owned self-check, not test score');
  result('Font controls stay within 16–22 px',await evaluate("(()=>{const up=document.getElementById('font-up'),down=document.getElementById('font-down');for(let i=0;i<20;i++)up.click();let upper=document.documentElement.style.getPropertyValue('--font');for(let i=0;i<20;i++)down.click();let lower=document.documentElement.style.getPropertyValue('--font');up.click();up.click();return upper==='22px'&&lower==='16px';})()"),'Measured CSS variable, then restored 18px');
  await navigate(BOOK);
  result('Reader self-check persists after reload',await evaluate("document.querySelector('[data-complete=\"1\"]').getAttribute('aria-pressed')==='true'&&document.documentElement.style.getPropertyValue('--font')==='18px'"),'Same isolated Chrome file:// origin');
  result('Quiz gives explanation',await evaluate("(()=>{let f=document.querySelector('.quiz');f.querySelector('input[value=\"1\"]').checked=true;f.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true}));return f.querySelector('.quiz-result').textContent.startsWith('Đúng hướng');})()"),'Correct choice plus reasoning');
  result('Print opens and restores answers',await evaluate("(()=>{let ds=[...document.querySelectorAll('details')],before=ds.map(d=>d.open);dispatchEvent(new Event('beforeprint'));let open=ds.every(d=>d.open);dispatchEvent(new Event('afterprint'));return open&&ds.every((d,i)=>d.open===before[i]);})()"),'beforeprint/afterprint events');
  for(const [width,height,name] of [[768,1024,'reader-tablet.png'],[375,850,'reader-mobile.png']]){
   await viewport(width,height);await evaluate('scrollTo(0,0)');await screenshot(name);
   const sizes=await evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})');result('No page overflow at '+width,sizes.scrollWidth<=sizes.width,sizes);
   if(width===375){await evaluate("document.getElementById('muc-2-3').scrollIntoView()");await screenshot('reader-mission-mobile.png');await evaluate("document.getElementById('menu-toggle').click()");result('Mobile menu opens',await evaluate("document.body.classList.contains('nav-open')&&document.getElementById('menu-toggle').getAttribute('aria-expanded')==='true'"),'375px actual browser emulation');await evaluate("document.getElementById('nav-shade').click()");}
  }
  await viewport(1440,1000);await evaluate('scrollTo(0,0)');
  if(process.argv.includes('--pdf')){const pdf=await page('Page.printToPDF',{printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false});fs.writeFileSync(path.join(REPORTS,'print-preview.pdf'),Buffer.from(pdf.data,'base64'));result('PDF rendered',true,'reports/print-preview.pdf; requires visual spot check');}
  await navigate(DEMO);
  result('Web starts with three samples',await evaluate("document.getElementById('total').textContent.includes('60.000')&&document.querySelectorAll('#expenses tr').length===3"),'Fresh isolated browser profile');
  const add=async(title,amount)=>evaluate(`(()=>{const f=document.getElementById('expense-form');f.elements.title.value=${JSON.stringify(title)};f.elements.amount.value=${JSON.stringify(amount)};f.requestSubmit();return {total:document.getElementById('total').textContent,message:document.getElementById('message').textContent};})()`);
  let added=await add('Bánh mì','15000');result('Web valid add 75000',added.total.includes('75.000'),added);
  let rejected=await add('Dữ liệu sai','35000abc');result('Web rejects numeric suffix',rejected.total.includes('75.000')&&rejected.message.includes('số nguyên'),rejected);
  await add('<b>Vở</b>','1');result('Web displays literal HTML-like title',await evaluate("document.getElementById('expenses').textContent.includes('<b>Vở</b>')&&!document.querySelector('#expenses b')"),'textContent, not parsed markup');
  await navigate(DEMO);
  result('Web localStorage persists in tested browser',await evaluate("document.getElementById('total').textContent.includes('75.001')"),'Observed on this Chrome file:// profile only; not universal guarantee');
  await evaluate("document.querySelectorAll('#expenses .delete').forEach(b=>b.click())");result('Web delete to empty = 0',await evaluate("document.getElementById('total').textContent==='0 đ'&&!document.getElementById('empty').hidden"),'All fake rows removed in isolated profile');
  await evaluate("localStorage.setItem('visinhvien-demo-v1','{broken')");await navigate(DEMO);
  result('Corrupt storage falls back without overwrite',await evaluate("document.getElementById('storage-notice').textContent.includes('bộ nhớ')&&localStorage.getItem('visinhvien-demo-v1')==='{broken'"),'Broken fixture kept; no real user data used');
  const memoryAdd=await add('Khoản tạm','1');result('Fallback adds a real in-memory row',memoryAdd.total.includes('60.001')&&await evaluate("document.getElementById('expenses').textContent.includes('Khoản tạm')"),memoryAdd);await navigate(DEMO);
  result('Fallback does not promise persistence',await evaluate("document.getElementById('total').textContent.includes('60.000')&&localStorage.getItem('visinhvien-demo-v1')==='{broken'"),'In-memory addition disappears after reload, notice remains');
  await viewport(375,850);await screenshot('demo-mobile.png');const demoSize=await evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})');result('Web demo no mobile page overflow',demoSize.scrollWidth<=demoSize.width,demoSize);
  await viewport(1440,1000);
  const manifest=JSON.parse(fs.readFileSync(path.join(ROOT,'assets/manifest.json'),'utf8'));
  const items=Array.isArray(manifest)?manifest:manifest.visuals||manifest.assets||[];
  for(const asset of items){
   const filename=asset.file||asset.filename||path.basename(asset.path);if(!filename)continue;
   await navigate(path.join(ASSETS,filename));
   const size=await evaluate('({width:document.documentElement.viewBox.baseVal.width,height:document.documentElement.viewBox.baseVal.height})');
   await viewport(size.width,size.height);
   const overflow=await evaluate(`(()=>{const root=document.documentElement,v=root.viewBox.baseVal;return [...document.querySelectorAll('text')].map(t=>{const b=t.getBBox(),m=root.getScreenCTM().inverse().multiply(t.getScreenCTM());const p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));return {text:t.textContent,x:Math.min(...p.map(p=>p.x)),y:Math.min(...p.map(p=>p.y)),right:Math.max(...p.map(p=>p.x)),bottom:Math.max(...p.map(p=>p.y))};}).filter(b=>b.x<v.x-1||b.y<v.y-1||b.right>v.x+v.width+1||b.bottom>v.y+v.height+1);})()`);
   result('SVG transformed text in bounds: '+filename,overflow.length===0,overflow);
   // Chồng chữ phải đo sau khi áp transform của nhóm, không dùng hộp cục bộ trong getBBox.
   const layout=await evaluate(`(()=>{const root=document.documentElement;const box=el=>{const b=el.getBBox();const m=root.getScreenCTM().inverse().multiply(el.getScreenCTM());const p=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>new DOMPoint(x,y).matrixTransform(m));return {x:Math.min(...p.map(q=>q.x)),y:Math.min(...p.map(q=>q.y)),r:Math.max(...p.map(q=>q.x)),b:Math.max(...p.map(q=>q.y))};};const all=[...document.querySelectorAll('text')].map(t=>({s:t.textContent.trim(),...box(t)})).filter(o=>o.s);const overlaps=[];for(let i=0;i<all.length;i++)for(let j=i+1;j<all.length;j++){const a=all[i],c=all[j];const ox=Math.min(a.r,c.r)-Math.max(a.x,c.x);const oy=Math.min(a.b,c.b)-Math.max(a.y,c.y);if(ox>1.5&&oy>1.5)overlaps.push([a.s.slice(0,40),c.s.slice(0,40),+ox.toFixed(1),+oy.toFixed(1)]);}const font=Math.min(...[...document.querySelectorAll('text')].map(t=>parseFloat(getComputedStyle(t).fontSize)));return {texts:all.length,overlaps,minFont:font};})()`);
   result('SVG text does not collide: '+filename,layout.overlaps.length===0,layout.overlaps.slice(0,8));
   result('SVG text at least 18px: '+filename,layout.minFont>=18,layout.minFont);
   await screenshot('visual-'+filename.replace(/\.svg$/,'.png'));
  }
  await navigate(BOOK);
  const outline=await evaluate("(()=>{const s=document.getElementById('ban-do');if(!s)return null;const links=[...s.querySelectorAll('a[href^=\"#\"]')];return {position:[...document.querySelectorAll('main section')].indexOf(s),routes:s.querySelectorAll('table')[0]?.querySelectorAll('tbody tr').length??0,missions:new Set([...s.querySelectorAll('a[href^=\"#muc-2-\"]')].map(a=>a.hash)).size,dossiers:new Set([...s.querySelectorAll('a[href^=\"#muc-4-\"]')].map(a=>a.hash)).size,broken:links.filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.hash),hasContract:s.innerText.includes('500000000000'),hasLimits:s.innerText.includes('chưa kiểm')};})()");
  result('One-page outline is first and complete',!!outline&&outline.position===1&&outline.routes===5&&outline.missions>=7&&outline.dossiers>=7&&outline.broken.length===0&&outline.hasContract&&outline.hasLimits,outline||'missing #ban-do section');
  result('Online build hides internal dashboard link',SITE_MODE?!await evaluate("document.documentElement.innerHTML.includes('Dashboard sản xuất')"):true,SITE_MODE?'site build drops production dashboard':'offline package keeps dashboard');
  result('No runtime exceptions',errors.length===0,errors);
  result('No remote content requests',requests.every(u=>!/^https?:/.test(u)),requests.filter(u=>/^https?:/.test(u)));
  fs.writeFileSync(path.join(REPORTS,SITE_MODE?'site-browser-results.json':'browser-results.json'),JSON.stringify({time:new Date().toISOString(),browser:discovery.Browser,results,errors,externalRequests:requests.filter(u=>/^https?:/.test(u))},null,2));
  await send('Browser.close');
  if(results.some(r=>!r.ok))process.exitCode=1;
 }catch(error){log({event:'error',error:String(error)});fs.writeFileSync(path.join(REPORTS,'browser-error.json'),JSON.stringify({time:new Date().toISOString(),error:String(error),results},null,2));console.error(error);process.exitCode=1;}
 finally{if(ws)ws.close();if(browser&&!browser.killed)browser.kill();try{fs.rmSync(profile,{recursive:true,force:true,maxRetries:3,retryDelay:100});}catch{}}
})();
