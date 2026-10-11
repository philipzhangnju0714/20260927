// Render figure5_workflow.svg to PNG (4x) and PDF.  Usage: npm install playwright && node render.js
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const svg = fs.readFileSync(path.join(__dirname, 'figure5_workflow.svg'), 'utf8');
  const [, w, h] = svg.match(/width="(\d+)" height="(\d+)"/).map(Number);
  const html = `<!doctype html><html><body style="margin:0;background:#fff">${svg}</body></html>`;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 4 });
  await page.setContent(html); await page.waitForTimeout(200);
  fs.mkdirSync(path.join(__dirname, 'output'), { recursive: true });
  await page.screenshot({ path: path.join(__dirname, 'output/figure5_workflow.png'), clip: { x: 0, y: 0, width: w, height: h } });
  await page.pdf({ path: path.join(__dirname, 'output/figure5_workflow.pdf'), width: w + 'px', height: h + 'px', printBackground: true, pageRanges: '1' });
  await browser.close(); console.log(`saved output/figure5_workflow.png (${w*4}x${h*4}) and .pdf`);
})();
