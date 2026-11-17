# Deployment

## GitHub Pages

- Repository: `git@github.com:FlogFr/www-studio-xci.git`.
- Build: GitHub Pages "Deploy from a branch" with the native Jekyll build — no
  workflow file needed. Settings → Pages → Source: the publishing branch
  (`main` or `gh-pages`, folder `/`).
- Custom domain: `CNAME` contains `studio-xci.fr`. In Settings → Pages, set the
  same domain and tick "Enforce HTTPS" once the certificate is issued.
- DNS for the apex `studio-xci.fr`: `A` records to 185.199.108.153,
  185.199.109.153, 185.199.110.153, 185.199.111.153 (and `AAAA`
  2606:50c0:8000::153 … 8003::153); optional `www` `CNAME` to `flogfr.github.io`.
- After the first deploy: submit `https://studio-xci.fr/sitemap.xml` in Google
  Search Console.

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
