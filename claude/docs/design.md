# Design

## Reference files (`design/`)

Exported mockups at 2× (2880 px wide = 1440 px layout). Renamed from the
export's broken (mojibake) names; `design/studio-xci.fr-png.zip` is the same
set and is git-ignored.

| File | md5 | Status | Page |
|------|-----|--------|------|
| `00-accueil-hub.png` | `203076044fad91ca5deb966b8742a851` | **blank** (fully transparent) | `/` |
| `01-planche-identite.png` | `0d53f91b65d15de5c00a816121539767` | **blank** | identity board |
| `10-son-liste.png` | `1fc06c4d41061547c2fc00c349fdc13a` | **blank** | `/son/` |
| `11-son-article-meredsp206.png` | `aa305e47e92c5f0dfc3803a2bc102e0f` | ok | `/son/meredsp206/` |
| `12-son-article-sound-system.png` | `56b9c4b19bbb9c7a13354cc17b36aa5f` | ok | `/son/sound-system/` |
| `20-logiciel-liste.png` | `115c97131c6b0249d3ac1560bc24dba8` | **blank** | `/logiciel/` |
| `21-logiciel-article-the-art-of-kubernetes.png` | `93ea7a27f797e957b919f105ad472590` | ok | `/logiciel/the-art-of-kubernetes/` |
| `30-motion-liste.png` | `29a8c4031459d296eab09a37b186e9cc` | **blank** | `/motion/` |
| `40-web-references.png` | `11ef8e8787fd6af3593b7e9a278058a2` | **blank** | `/web/` |
| `50-others.png` | `69ed96214e160008054eeb3c0186e93c` | **blank** | `/others/` |

The seven blank files were exported empty: those pages were designed in code,
extending the identities of the three article mockups. Re-exported files must
be viewed and this table updated. The horn article
(`/son/pavillon-directivite-constante/`) has no mockup: it reuses the I Son
article components, with a render as hero image.

### Viewing a mockup

They are too tall to read in one image. Slice them into the scratchpad:

```
convert design/<file>.png -resize 50% -crop 1440x1100 +repage <scratch>/slice_%02d.png
```

Check a file is not blank: `convert <file> -resize 10% -alpha extract -format "%[fx:maxima]" info:`
(0 = fully transparent).

## Shared chrome (from the mockups)

- Header 76 px, bottom rule: `XCI` square mark (38 px) · `← studio` (mono,
  muted) · universe label `I — SON` in the accent. Right side: page CTA
  (MereDSP206 "Télécharger"), `← tous les articles` on articles, the I–V
  switcher elsewhere.
- Footer: `← I · Son` back link, the five universes, `studio-xci.fr`.
- Layout: 1280 px content, 80 px gutters at 1440 (16 px min on mobile).
  Article = 280 px aside (TOC with 2 px accent top rule + facts box) and a
  760 px text column. Sections numbered `01`, `02`… in the accent colour.
- "À lire ensuite": two surface cards (mono kicker + display title).

## Universe identities

Every value below is a custom property in `assets/css/main.css` §8.

| | Background / surface | Ink / muted | Accent / 2nd | Display · Body · Mono | Type treatment |
|---|---|---|---|---|---|
| Studio (hub) | `#f3f1ec` / `#e8e5de` | `#121212` / `#67635b` | `#121212` / `#c2410c` | Inter 800 · Inter · JetBrains Mono | tight negative tracking |
| I Son | `#121212` / `#1c1c1c` | `#ededed` / `#a4a4a4` | `#ffb000` / `#3ddc84` | Barlow Condensed 800 · Barlow · JetBrains Mono | UPPERCASE condensed |
| II Logiciel | `#ffffff` / `#f3f5f9` | `#0f172a` / `#64748b` | `#2448c9` / `#0f172a` | IBM Plex Sans 700 · IBM Plex Serif · IBM Plex Mono | sentence case, serif body, mono numbers |
| III Motion | `#0d0b14` / `#17131f` | `#f4f0ff` / `#9c93b5` | `#ff4d8d` / `#7b61ff` | Syne 800 · DM Sans · DM Mono | gradient numerals, "SC 01" tags |
| IV Web | `#f5efe4` / `#ebe3d4` | `#1b1a17` / `#6b655b` | `#c2410c` / `#2f5d50` | Fraunces 600 · Inter · JetBrains Mono | italic serif numerals, browser-frame cards |
| V Others | `#e6eeec` / `#d7e4e1` | `#0b2a2f` / `#4c6669` | `#0a6e65` / `#e8552a` | Space Grotesk 700 · Space Grotesk · Space Mono | graph-paper background, outlined numerals |

I Son and II Logiciel come straight from the mockups (sampled colours). Hub,
III, IV and V are code-side designs, pending real mockups.

## Components seen in the mockups

- MereDSP206: split hero with a DSP console (IN A/B amber meters, OUT 1–6
  green meters, GAIN/X-OVER/EQ/DELAY/LIMIT tabs) → `visual-dsp.html`; 2×2
  feature grid; a Linux capture (wide) beside an Android capture (rounded
  phone frame) → `shots.html`; Linux (amber, filled) / Android (green outline)
  install cards + terminal block; disclaimer note.
- Sound system: wide hero photo (replaced by an SVG schematic until a photo
  exists → `visual-stacks.html`); stats box 2/4/3/6; spec tables with accent
  header rule; rack grid; signal-chain figure; amber callout linking MereDSP206.
- The Art Of Kubernetes: split hero with the book cover (typographic stand-in
  `visual-book.html` until `cover:` is set); "Fiche du livre" facts; numbered
  chapter list; quote; blue + outline buttons; dark navy "Aller plus loin" callout.

## Components designed in code

- Screenshots (`shots.html`): phone captures in a 6 px `--surface-2` bezel
  with 26 px radius; desktop captures with a 1 px `--line` border and 10 px
  radius; mono caption. A single phone can float right (250 px, max 38 %)
  beside the text; `h2` clears the float. Rows: phones 150–230 px wide; a
  desktop + phone row is 3.2 fr / 1 fr.
- App icon above the kicker (88 px, 22 % radius, 1 px `--line` ring).
- `<kbd>` keys: mono, `--surface` fill, 2 px bottom border.
- Install cards can carry a `note` line under the formats.
- Tables are real table boxes (header and body columns aligned, full width);
  under 720 px they become horizontally scrollable blocks.
- Figures (`shots.html`, `kind: figure`): charts, renders and drawings in a
  1 px `--line` frame, mono caption; two figures share a row (one column under
  720 px). A render or photo can be the hero (`hero_visual: image`).
- Charts (horn article) are WebP images drawn by `scripts/pavillon/` in the
  I · Son colours: `#1c1c1c` surface, Barlow labels, JetBrains Mono numbers.
  Data series take the first three slots of the validated dark categorical
  palette (`#3987e5` blue, `#d95926` orange, `#199e70` aqua; the brand amber
  and green fail its lightness band), the site amber marks annotations (the
  800 Hz line), polar maps use a single amber ramp with the −6 dB contour in
  ink. Every chart has its numbers in a table next to it. When a chart mixes
  two sources (horn vs 12″), colour stays the plane (blue horizontal, orange
  vertical) and the line style is the source: solid = simulated / retained,
  dashed = model or compared design.
- Technical drawings follow first-angle projection (ISO E, the French
  convention): front view, side section on its right, top section below.
- 3D renders (three.js, offline): printed parts in light grey, the second
  part type in amber, the driver as a dark schematic cylinder.

## Deliberate differences from the mockups

- Placeholders (`[DATE]`, `[CAPTURE]`, `[LICENCE]`…) are not rendered; the
  missing facts are tracked in `content-status.md`.
- The MereDSP206 related card "Mere pour Ardour 9" is replaced by the horn
  project until that project is confirmed.
- MereDSP206 grew from the mockup's six sections into a full user guide
  (connection, one section per screen, settings table, Linux shortcuts and
  CLI, troubleshooting): same components, more of them. The hero keeps the
  stylised DSP console; real screenshots illustrate the body. The app icon
  sits above the kicker (not in the mockup). The mockup's "Licence" fact is
  omitted until the licence is known.
- Below 1080 px the aside stacks above the text; below 720 px every grid goes
  single column.
