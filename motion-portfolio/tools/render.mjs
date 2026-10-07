// frame-by-frame render: seek the timeline, wait two rAFs, capture; frames piped straight into ffmpeg
import puppeteer from 'puppeteer-core';
import { spawn } from 'node:child_process';
const [url, out, fpsArg, fromArg, toArg] = process.argv.slice(2);
const FPS = Number(fpsArg || 60);
const b = await puppeteer.launch({executablePath:process.env.CHROME||'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',headless:'new',args:['--no-sandbox','--allow-file-access-from-files','--font-render-hinting=none']});
const p = await b.newPage(); p.on('pageerror', e => console.log('PAGEERROR', e.message));
await p.setViewport({width:1080,height:1080,deviceScaleFactor:1});
await p.goto(url,{waitUntil:'load'});
await p.waitForFunction('window.OPENER&&window.OPENER.ready',{timeout:60000});
const DUR = await p.evaluate(() => window.OPENER.DURATION);
const f0 = Math.round(Number(fromArg || 0) * FPS), f1 = Math.round(Number(toArg || DUR) * FPS);
const ff = spawn('ffmpeg', ['-hide_banner','-loglevel','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','png','-i','-','-c:v','libx264','-preset','slow','-crf','15','-pix_fmt','yuv420p','-tune','film', out], {stdio:['pipe','inherit','inherit']});
const t0 = Date.now();
for (let i = f0; i < f1; i++) {
  await p.evaluate(async t => { window.OPENER.seek(t); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); window.OPENER.seek(t); }, i / FPS);
  const buf = await p.screenshot({type:'png'});
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % (FPS * 5) === 0) console.log(`${(i / FPS).toFixed(1)}s  ${((i - f0 + 1) / ((Date.now() - t0) / 1000)).toFixed(1)} fps`);
}
ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('done', out);
