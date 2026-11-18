# Content rules

- Language: French, first person ("je"), plain and concrete — the voice of the
  design mockups. No marketing superlatives, no emoji in body text.
- Each universe speaks to a different audience; write for it:
  - I Son — DJs, sound engineers, DSP 206 owners. MereDSP206 is promoted to the
    general public: lead with what it does and how to get it.
  - II Logiciel — tech peers and recruiters: precise, factual.
  - III Motion — portfolio: show the result first, the making-of after.
  - IV Web — professional references (LinkedIn, friends, associations): client,
    need, what was delivered, link.
  - V Others — personal projects and notes (shaping, composites…).
- No visible placeholders on the live site (`[DATE]`, `[LICENCE]`, "lorem").
  Leave the element out and log the missing fact in
  `claude/docs/content-status.md`. An HTML comment `<!-- TODO: … -->` in the
  Markdown is fine.
- Brands: always keep the MereDSP206 disclaimer ("projet indépendant, non
  affilié à Thomann ; t.racks est une marque de Thomann"). Thomann agreed to
  public distribution; say so, nothing more.
- French typography: « guillemets », capital accents (É, À), "×" for
  multiplication, "–" for ranges (800 Hz – 1 kHz), units with a space (12 m, 300 W).
- One article = one project. Use `##` headings with an explicit id
  (`## Titre {#slug}`): they feed the numbered table of contents.
- Software pages (MereDSP206) are user documentation: what it does, install,
  connect, then one section per screen with its screenshot, a settings
  reference table, troubleshooting. Take every feature, range and command
  from the project's repository (README, docs, code), never from memory.
- Name UI elements in italics. When the screenshots are in English, give the
  French label first and the English one in parentheses: *Console* (*Mixer*).
- Prices: name the shop, the price and the month it was read, link the
  listing, and say prices move. Never quote a price without a source.
- Figures computed for an article (charts, simulation results, drawings, 3D
  files) state their method and limits next to them, and every number in the
  text matches the published files.
