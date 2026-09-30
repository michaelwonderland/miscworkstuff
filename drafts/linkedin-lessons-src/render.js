const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: process.argv[2], format: 'A4', printBackground: true, preferCSSPageSize: true });
  // overflow check
  const o = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg,i)=>{const ftr=pg.querySelector('.ftr');const kids=[...pg.children].filter(c=>!c.classList.contains('ftr')&&!c.classList.contains('hdr'));const bottom=Math.max(...kids.map(k=>k.getBoundingClientRect().bottom));const lim=ftr?ftr.getBoundingClientRect().top:pg.getBoundingClientRect().bottom;return `p${i+1}: content bottom ${Math.round(bottom-pg.getBoundingClientRect().top)} / limit ${Math.round(lim-pg.getBoundingClientRect().top)} fonts:${document.fonts.check('12px Gelasio')}/${document.fonts.check('12px Carlito')}`}));
  console.log(o.join('\n'));
  for (let i=0;i<10;i++){ const el=(await p.$$(".page"))[i]; await el.screenshot({path: __dirname+`/shot${i+1}.png`}); }
  await b.close();
})();
