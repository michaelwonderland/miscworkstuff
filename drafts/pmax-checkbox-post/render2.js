const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/' + (process.argv[2]||'index.html') + '', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log(await p.evaluate(() => `fonts:${document.fonts.check('12px "Instrument Serif"')}/${document.fonts.check('12px Geist')}`));
  await p.locator('.canvas').screenshot({ path: __dirname + '/' + (process.argv[3]||'pmax-checkbox.png') + '' });
  await b.close();
})();
