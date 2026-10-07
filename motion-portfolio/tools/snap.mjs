import puppeteer from 'puppeteer-core';
import { mkdir } from 'node:fs/promises';
const [url,outDir,...times]=process.argv.slice(2);
await mkdir(outDir,{recursive:true});
const b=await puppeteer.launch({executablePath:process.env.CHROME||'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',headless:'new',args:['--no-sandbox','--allow-file-access-from-files','--font-render-hinting=none']});
const p=await b.newPage();p.on('pageerror',e=>console.log('PAGEERROR',e.message));p.on('console',m=>{if(m.type()==='error')console.log('CONSOLE',m.text())});
await p.setViewport({width:1080,height:1080,deviceScaleFactor:1});
await p.goto(url,{waitUntil:'load'});
await p.waitForFunction('window.OPENER&&window.OPENER.ready',{timeout:60000});
for(const ts of times){const t=Number(ts);await p.evaluate(async t=>{window.OPENER.seek(t);await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));window.OPENER.seek(t);},t);
 await p.screenshot({path:`${outDir}/t${t.toFixed(2).padStart(5,'0')}.png`});}
await b.close();
