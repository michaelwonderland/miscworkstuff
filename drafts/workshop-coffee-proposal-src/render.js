const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({viewport:{width:794,height:1123}});
  await p.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg,i)=>{const t=pg.getBoundingClientRect().top;const f=pg.querySelector('.foot');const lim=f?f.getBoundingClientRect().top-t-12:1123;let b=0;pg.querySelectorAll('*').forEach(e=>{if(e.closest('.foot')||e.closest('.glow')||e.closest('svg'))return;const r=e.getBoundingClientRect();if(r.height)b=Math.max(b,r.bottom-t)});return `p${i+1}:${Math.round(b)}/${Math.round(lim)}${b>lim?' OVER':''}`}).join(' ')+` fonts:${document.fonts.check('12px "Instrument Serif"')}/${document.fonts.check('12px "Instrument Sans"')}`);
  console.log(r);
  await p.pdf({ path: process.argv[2], width:'794px', height:'1123px', printBackground: true });
  const pages = await p.$$('.page'); for (let i=0;i<pages.length;i++) await pages[i].screenshot({path: `${__dirname}/s${i+1}.png`});
  await b.close();
})();
