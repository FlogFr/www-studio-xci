# Content status

## Pages

| URL | Status | Missing |
|-----|--------|---------|
| `/` | live | — |
| `/son/` | live | — |
| `/son/meredsp206/` | live, full user guide (v0.1.0) | licence, bug/contact channel, packaged downloads (.deb / Flatpak / Play Store link once published), French-language Android screenshots |
| `/son/sound-system/` | live | photo of the two stacks, anecdote of how/when it was acquired, current crossover frequencies and slopes |
| `/son/pavillon-directivite-constante/` | live, design documented (need, Keele, driver + price, OS-SE profile, BEM simulation, plan, renders, 800 Hz vs 1.2 kHz crossover, level budget and 12″ compatibility, STL, DSP starting points) | prototype photos, measured polars, measured crossover / delay / EQ, ME-12/300 and APA1000 specs, the head cabinet design |
| `/logiciel/` | live | free-software / Linux / infra projects to list |
| `/logiciel/the-art-of-kubernetes/` | live | real cover image (`cover:`), the personal trigger, writing organisation, a quote from the book |
| `/motion/` | live, empty gallery | every render (thumbnail 16:9, video link, software, year) |
| `/web/` | live | sites made for friends and associations (name, URL, for whom, year, stack, screenshot) |
| `/others/` | live | — |
| `/others/shaper/` | live | materials actually used, process details, photos |

`<!-- TODO: … -->` comments in the Markdown mark where each missing fact goes.

## Open questions for Florian

1. MereDSP206: which licence? Where should users report bugs (GitHub issues,
   e-mail)? Has the Android app been tried on the real unit yet (the page only
   says the protocol was tested on Florian's unit)? Link the Play Store page
   once published.
2. "Mere pour Ardour 9" (VST / LV2) appears in the MereDSP206 mockup as a
   related article: is it a real project to document in I Son?
3. IV Web: did you build infratelier.com, theartofkubernetes.com and
   hydrocamp.fr yourself? They are listed as your own sites; remove any you
   did not make.
4. Which friends' / associations' sites can be listed publicly?
5. Free-software / Linux / infrastructure projects for II Logiciel: names and links.
6. Public contact (e-mail, LinkedIn URL) to add to the footer and to the
   Person JSON-LD `sameAs`.
7. Motion: where are the renders hosted (YouTube, PeerTube, Vimeo, files)?
8. Horn: is the B&C DE750TN choice confirmed, and are its M6 holes threaded
   (bolts from the horn side)? Datasheet of the Eminence ME-12/300
   (sensitivity, usable range: can they play cleanly to 2.4 kHz for a 1.2 kHz
   crossover?) and the Ecler APA1000 power at 8 Ω and 4 Ω (the article's
   level budget needs 110 W / 8 Ω for the driver and 600 W / 4 Ω for the
   pair). Settled: 220 × 220 × 220 mm printer bed; the two 12″ can be stacked
   vertically.

## Sources of the facts already published

- Mockups (`design/11`, `12`, `21`) — texts written with Florian: MereDSP206
  story, sound-system composition (Master Sound, Paris, W-bin 415 / RCF
  L15-554K, 2 × Eminence ME-12/300, JBL 2482, 2 × Celestion HF50, rack: DSP 206,
  Crest CPX 2600, 2 × Ecler APA1000, Inter-M M700 spare, `sonorisation.dsp206.rst`),
  book chapters and facts.
- MereDSP206 repository (https://github.com/FlogFr/meredsp206: README,
  `claude/docs/*.md`, GTK and Android source, `strings.xml` for the French UI
  labels) — every feature, range, command, requirement and install step on the
  page. Version 0.1.0 from `Cargo.toml` / `build.gradle.kts`. Requirement
  "GTK 4.14 + libadwaita 1.6" from the `gtk4` / `libadwaita` crate features.
- MereDSP206 screenshots — Android: five captures supplied by Florian (demo
  mode / offline, English UI); Linux: captured from the GTK app's demo mode
  (see deployment.md). Icon: `android/store/icon-512.png` of the repository.
- theartofkubernetes.com — 350 pages, Kindle, Amazon.fr link, free chapter,
  English edition in progress.
- infratelier.com — Infratelier SASU, Nantes, tagline, trainings.
- hydrocamp.fr — « Atelier Amateur de Shape Nantais », boards and accessories, MPCNC.
- Florian's brief — XCI = 91, the five universes, Thomann's agreement, horn
  targets (80° H × 40° V, 800 Hz or 1 kHz).
- Horn article: Keele's rule of thumb (mouth ≈ 25 400 / (angle × f)) and
  Molloy's Q formula are general acoustics knowledge, presented as orders of
  magnitude. Every chart, dimension and STL comes from `scripts/pavillon/`
  (BEM with bempp-cl; results in `scripts/pavillon/results/`). Driver data:
  B&C's DE750TN-8 page (throat, impedance, power, sensitivity, band,
  recommended crossover, voice coil, mounting, size, weight) and retailer
  listings for the compared drivers; prices found in November 2026 (Thomann
  259 €, SonoVente 261 € for the DE750TN; DE950TN 418 € out of stock at
  SonoVente; HF201 ≈ 315 € at Masori; N314T-8 ≈ 239 € at Tout le haut-parleur).
  JBL 2482: JBL spec sheet (10.5 kg magnet structure). The woofer directivity
  (`scripts/pavillon/woofers.py`) is a piston model: 26 cm cones in an
  infinite baffle, two stacked at 33 cm centres. Crossover comparison
  drivers: DE780TN-16 (1.4″, 1.2 kHz minimum, 109 dB, Thomann 192.44 € excl.
  VAT, SonoVente 238 €; 110 W from an 8 Ω listing), DE250-8 (1″, 1.6 kHz,
  108.5 dB, 60 W, Thomann BE 92 €, Muziker 99 €). 12″ candidates: B&C
  12NDL76-8 (100 dB, 50 Hz – 2 kHz, 400 W / 800 W program, Thomann 199 €),
  FaitalPRO 12PR320-8 (97 dB, 45 Hz – 5 kHz, 300 W, Masori 193 € promo /
  229 €, Soundimports 234.95 €). No public datasheet found for the
  ME-12/300.
- Florian's answers (horn): print on a 220 × 220 × 220 mm bed; the two 12″
  can be stacked; the goal is to replace the 2482 + tweeters + passive filter
  by one simpler, high-output, quality top section; asked whether a 1.2 kHz
  crossover would help (documented: it is a DSP setting, recommended as the
  starting point).
