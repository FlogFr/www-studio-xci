# SEO rules

- Every page has `title` (≤ 50 chars, main keyword first: jekyll-seo-tag appends
  " | Studio XCI", and Google shows ~60) and `description`
  (140–160 chars, unique, says what the reader gets). `jekyll-seo-tag` turns
  them into `<title>`, meta description, canonical, Open Graph and Twitter tags.
- One `<h1>` per page. Headings follow the outline (`h2` sections, `h3` inside).
- URLs: `/<universe>/<slug>/`, lowercase ASCII, hyphens, no dates. Never rename
  a published URL; if you must, add a `redirect_from` (jekyll-redirect-from).
- Structured data: articles get a JSON-LD type through `schema:` front matter
  (`SoftwareApplication`, `Book`, `CreativeWork`…), see `_includes/schema.html`.
  Every page gets a `BreadcrumbList`. Keep JSON-LD facts identical to the
  visible text.
- Images: meaningful `alt` in French, explicit `width`/`height`,
  `loading="lazy"` below the fold, WebP or optimised JPEG/PNG under ~300 KB.
  Each universe has a default social image in `assets/img/og/`.
- Screenshots: real captures only (demo mode is fine), WebP at about twice the
  displayed width (600 px phones, 1600 px desktop windows), phone status and
  navigation bars cropped out, in `assets/img/<project>/`, through
  `shots.html`.
- Link between projects whenever it is natural (`related:` front matter and in
  the text). Cross-list a project in a second universe with `also_in:`.
- Keep the site fast: one CSS file, no JS framework, fonts with
  `display=swap` and only the weights in use.
- External links to the user's other sites (infratelier.com,
  theartofkubernetes.com, hydrocamp.fr) are normal `<a>` links (no `nofollow`).
