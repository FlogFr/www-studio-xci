# Code rules

- Stay inside what the GitHub Pages Jekyll build supports: Jekyll 3.x, Liquid
  4, kramdown (GFM) and the whitelisted plugins only. No custom Ruby plugins
  and no extra build step: `.github/workflows/pages.yml` only runs the official
  `actions/jekyll-build-pages` and deploys. Change that workflow only when the
  user asks.
- No JavaScript unless a feature cannot work without it. Pages must be fully
  readable with JS off.
- CSS lives in `assets/css/main.css`. Colours, fonts and type treatment come
  from the universe tokens (`[data-universe="…"]` custom properties). Never
  hard-code a universe colour in a component: use `var(--accent)` etc.
- Add a universe-specific rule only for a deliberate identity difference, and
  group it under that universe's section of the CSS file.
- Reusable blocks are includes in `_includes/` fed by front matter
  (`{% include features.html items=page.features %}`); keep the Markdown
  readable by the user.
- Accessibility: semantic landmarks, visible focus, colour contrast ≥ 4.5:1 for
  text, decorative visuals `aria-hidden="true"`, honour `prefers-reduced-motion`.
- Layout must work from 320 px wide, with no horizontal scroll.
- Generated assets (charts, plans, renders, STL) come from scripts under
  `scripts/<project>/` and are never edited by hand: change the script or its
  parameters, rerun it, and commit the script, its inputs/results and the
  outputs together. Charts are static WebP images, never JS on the page.
