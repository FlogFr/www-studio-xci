# Content status

## Pages

| URL | Status | Missing |
|-----|--------|---------|
| `/` | live | — |
| `/son/` | live | — |
| `/son/meredsp206/` | live, full user guide (v0.1.0) | licence, bug/contact channel, packaged downloads (.deb / Flatpak / Play Store link once published), French-language Android screenshots |
| `/son/sound-system/` | live | photo of the two stacks, anecdote of how/when it was acquired, current crossover frequencies and slopes |
| `/son/pavillon-directivite-constante/` | live, design documented (need, Keele, driver + price, OS-SE profile, BEM simulation, plan, renders, STL, DSP starting points) | prototype photos, measured polars, measured crossover / delay / EQ, the head cabinet design |
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
8. Horn: which 3D printer (bed size) will print it? The parts are sized for a
   220 × 220 mm bed. Are the two 12″ of the future heads stacked vertically
   (the article's vertical-coverage argument assumes so)? Is the B&C DE750TN
   choice confirmed, and are its M6 holes threaded (bolts from the horn side)?

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
  JBL 2482: JBL spec sheet (10.5 kg magnet structure). The two-woofer vertical
  beamwidth is a two-point-source estimate (12″ centres 33 cm apart).
