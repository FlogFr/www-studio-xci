// Renders the views listed in a JSON file with three.js in headless Chromium.
//   python3 export.py                      # STL inputs into stl/
//   python3 -m http.server 8765 &          # from this folder
//   node shoot.js views.json               # PNG files named in views.json
// Playwright must be installed globally (require('playwright')).
const { chromium } = require("playwright");
const fs = require("fs");

(async () => {
  const views = JSON.parse(fs.readFileSync(process.argv[2] || "views.json", "utf8"));
  const browser = await chromium.launch({ args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"] });
  for (const view of views) {
    const page = await browser.newPage({ viewport: { width: view.w, height: view.h } });
    page.on("pageerror", (e) => console.log("pageerror:", e.message));
    await page.goto("http://localhost:8765/index.html#" + encodeURIComponent(JSON.stringify(view)));
    await page.waitForFunction(() => document.title === "done", null, { timeout: 300000 });
    await page.locator("canvas").screenshot({ path: view.out });
    console.log("wrote", view.out);
    await page.close();
  }
  await browser.close();
})();
