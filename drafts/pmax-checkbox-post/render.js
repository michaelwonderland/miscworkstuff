const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await p.goto('file://' + __dirname + '/index.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log(await p.evaluate(() => `fonts:${document.fonts.check('12px "Instrument Serif"')}/${document.fonts.check('12px "Instrument Sans"')}`));
  await p.locator('.canvas').screenshot({ path: __dirname + '/pmax-checkbox.png' });
  await b.close();
})();
