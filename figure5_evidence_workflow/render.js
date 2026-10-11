// Render the figure to PNG (3x, ~2880 px wide) and vector PDF.
// Usage: npm install playwright && node render.js
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs'); const { pathToFileURL } = require('url');
const WIDTH = 960, SCALE = 3, OUT = path.join(__dirname, 'output');
const FILE = process.argv[2] || 'figure5_evidence_workflow.html';
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: WIDTH, height: 800 }, deviceScaleFactor: SCALE });
  await page.goto(pathToFileURL(path.join(__dirname, FILE)).href);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const h = await page.evaluate(() => Math.ceil(document.body.getBoundingClientRect().height));
  await page.setViewportSize({ width: WIDTH, height: h });
  const stem = path.basename(FILE, '.html');
  await page.screenshot({ path: path.join(OUT, stem + '.png'), fullPage: true });
  await page.pdf({ path: path.join(OUT, stem + '.pdf'), width: WIDTH + 'px', height: (h + 2) + 'px',
                   printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  console.log(`saved output/${stem}.png (${WIDTH * SCALE}x${h * SCALE}) and .pdf`);
  await browser.close();
})();
