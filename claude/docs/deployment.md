# Deployment

## GitHub Pages

- Repository: `git@github.com:FlogFr/www-studio-xci.git`.
- Build: `.github/workflows/pages.yml` (official "Jekyll with GitHub Pages
  dependencies preinstalled" workflow: `actions/jekyll-build-pages`, same gems
  as the `github-pages` gem) runs on every push to `main` and deploys to the
  `github-pages` environment. Settings → Pages → Source must be
  **GitHub Actions**. It can also be re-run by hand (workflow_dispatch).
  "Deploy from a branch" never triggered a build on this repository.
- Custom domain: `CNAME` contains `studio-xci.fr`. In Settings → Pages, set the
  same domain and tick "Enforce HTTPS" once the certificate is issued.
- DNS for the apex `studio-xci.fr`: `A` records to 185.199.108.153,
  185.199.109.153, 185.199.110.153, 185.199.111.153 (and `AAAA`
  2606:50c0:8000::153 … 8003::153); optional `www` `CNAME` to `flogfr.github.io`.
- After the first deploy: submit `https://studio-xci.fr/sitemap.xml` in Google
  Search Console.
- Every push to `main` shows a "Deploy Jekyll site to Pages" run in the
  Actions tab (~1–2 min). "Site not found · GitHub Pages" means no deployment
  succeeded yet: check that run's log, and that the Pages source is
  "GitHub Actions".
- Checking without `gh` (not installed): the public API
  `https://api.github.com/repos/FlogFr/www-studio-xci/actions/runs` lists the
  builds; `dig +short studio-xci.fr A` checks DNS.

## Local preview

Requires Docker only (gems are cached in the `studio-xci-bundle` volume).

```
make serve   # http://localhost:4000, live reload
make build   # production build into _site/
make clean
```

In Claude Code, the `jekyll` entry of `.claude/launch.json` starts the same
server for the browser pane (config changes need a restart).

## Images

`scripts/make-images.sh` regenerates `favicon.ico`, the PNG icons, the logo,
the six universe Open Graph cards and the project cards (`project_card`, e.g.
`og/meredsp206.png` built from the project's icon) in `assets/img/og/` with
ImageMagick. Run it after a change of universe name, tagline or colour. The
fonts default to DejaVu / JetBrains Mono paths; override `FONT_*` when they
live elsewhere (the existing cards use DejaVu Sans Bold for the titles).

### MereDSP206 screenshots

- Android: captures from the phone (900 × 2000), cropped to remove the status
  bar and the system navigation bar (`-crop 900x1808+0+88`), resized to 600 px
  wide WebP (`-quality 82`) → `assets/img/meredsp206/android-*.webp`.
- Linux: build the GTK app (`cargo build --release -p dsp206-gtk`, needs GTK
  4.14 and libadwaita 1.6, e.g. Debian 13 or Ubuntu 26.04 in a container), run
  it under Xvfb with `fonts-adwaita-sans`, `gtk-font-name=Adwaita Sans 11` in
  `~/.config/gtk-4.0/settings.ini` and `ADW_DEBUG_COLOR_SCHEME=prefer-dark`:
  `meredsp206 --demo --page mixer` (or `--page channel --channel out1`). Wait
  ~12 s for the start-up toast to go, grab the 1781 × 900 window with
  `import -window root` + crop, resize to 1600 px wide WebP (`-quality 85`).

### Horn article (charts, plan, renders, STL)

Everything comes from `scripts/pavillon/` (Python; dependencies and commands
in its README). The BEM results are kept in `scripts/pavillon/results/*.npz`
so the charts can be redrawn without re-running the simulation (~1 h on 4
cores for the retained design, 1/6 octave plus the 6.3–10 kHz points).

- Charts and plan: `python3 plots.py` and `python3 plan.py` into
  `assets/img/pavillon/` (WebP, 1600 px); the plan also writes the 1:1 baffle
  template `gabarit-baffle.svg`, copied to `assets/files/pavillon/`.
- STL: `python3 cad.py <design> out/`, then zip the two quadrants (A and B)
  into `assets/files/pavillon/pavillon-80x40-stl.zip`. The assembled STL is
  only used for the renders and is not published.
- Renders: `scripts/pavillon/render/` (three.js 0.170.0 from npm, in the
  pre-installed headless Chromium through Playwright): `python3 export.py`
  writes the STL inputs, `python3 -m http.server 8765` serves the folder,
  `node shoot.js views.json` renders at 2400 × 1650, `python3 finish.py
  ../../../assets/img/pavillon` crops and saves 1600 × 1100 WebP.
