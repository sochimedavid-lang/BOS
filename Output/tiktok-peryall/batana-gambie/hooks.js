const { chromium } = require('playwright');
const css = `@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&display=swap');
*{margin:0;padding:0;box-sizing:border-box} html,body{background:transparent} body{width:1080px;height:1920px;position:relative;font-family:Montserrat,sans-serif}
.s1{position:absolute;top:300px;width:100%;text-align:center}.s1 span{display:inline-block;background:#000;color:#fff;font-weight:900;font-size:76px;line-height:1.05;padding:10px 26px;margin:4px 0}.y{color:#ffd400}
.s3{position:absolute;top:320px;left:0;right:0;text-align:center}.s3 span{display:inline-block;background:#ffe500;color:#000;font-weight:900;font-size:78px;line-height:1.1;padding:12px 30px;transform:rotate(-3deg);box-shadow:10px 10px 0 #000;margin:10px 0}.s3 .r{background:#fff;transform:rotate(2deg)}
.s4{position:absolute;top:300px;left:90px;width:820px;background:#fff;border-radius:34px;padding:34px 40px;box-shadow:0 20px 50px rgba(0,0,0,.35)}.s4 .h{display:flex;align-items:center;gap:20px;color:#888;font-weight:700;font-size:36px}.s4 .av{width:76px;height:76px;border-radius:50%;background:linear-gradient(135deg,#f6a,#a6f)}.s4 .q{margin-top:20px;color:#111;font-weight:800;font-size:58px;line-height:1.2}.s4:after{content:"";position:absolute;left:80px;bottom:-30px;border:30px solid transparent;border-top-color:#fff;border-bottom:0}
.s6{position:absolute;top:190px;left:0;right:0;text-align:center;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.82) 18%,rgba(0,0,0,.82) 82%,rgba(0,0,0,0));padding:60px 0 70px}.s6 .a{display:inline-block;background:#e0001b;color:#fff;font-weight:900;font-size:58px;padding:14px 34px;border-radius:12px;letter-spacing:2px}.s6 .m{margin-top:26px;color:#fff;font-weight:900;font-size:96px;line-height:1.02}.s6 .m b{color:#ff3b4e}`;
const s1=(a,b)=>`<div class="s1"><span>${a}</span><br><span>${b}</span></div>`;
const s3=(a,b)=>`<div class="s3"><span>${a}</span><br><span class="r">${b}</span></div>`;
const s4=q=>`<div class="s4"><div class="h"><div class="av"></div>Reply to a comment</div><div class="q">${q}</div></div>`;
const s6=(a,m)=>`<div class="s6"><div class="a">${a}</div><div class="m">${m}</div></div>`;
const H={
 '01':s4("Will it work if I’m already going bald? 😟"),
 '02':s1('FROM RECEDING HAIRLINE','TO A <b class="y">FULL HAIRLINE</b>'),
 '03':s1('FROM BALD SPOT','TO A <b class="y">FULL HEAD</b>'),
 '04':s3('SHE HAD NO IDEA','IT WAS THIS BAD 😳'),
 '05':s4("Does this oil really work for men’s hairline? 🤔"),
 '06':s6('⚠️ MEN IN GAMBIA','DON’T SHAVE<br>YOUR HEAD <b>YET</b>'),
 '07':s6('⚠️ STOP SCROLLING','IF YOUR EDGES<br>ARE <b>THINNING</b>'),
 '08':s1('SHE SHAVED IT ALL OFF…','<b class="y">THEN TRIED THIS OIL</b>'),
 '09':s3('HIS HAIRLINE WAS','THIS FAR BACK 😳'),
 '10':s4("Can it fix a hairline this far back? 😩"),
};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 for(const [k,h] of Object.entries(H)){await p.setContent(`<html><head><style>${css}</style></head><body>${h}</body></html>`);await p.waitForTimeout(900);await p.screenshot({path:`../prod/hook_${k}.png`,omitBackground:true});}
 await p.goto('file://'+process.cwd()+'/b_bold.html');await p.waitForTimeout(1200);await p.screenshot({path:'../prod/card.png'});
 await b.close();})();
