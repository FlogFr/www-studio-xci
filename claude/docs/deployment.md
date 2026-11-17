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

`scripts/make-images.sh` regenerates `favicon.ico`, the PNG icons, the logo and
the six Open Graph cards (`assets/img/og/`) with ImageMagick. Run it after a
change of universe name, tagline or colour.
