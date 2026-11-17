# CLAUDE.md — studio-xci.fr

Source of https://studio-xci.fr/, a Jekyll site built and served by GitHub Pages.
It is Florian Grignon's library / directory of projects, grouped into five
"universes": I Son, II Logiciel, III Motion, IV Web, V Others.

## On every prompt

1. **Read the rules** below (imported) and follow them. They are your standing
   instructions for this repository.
2. **Read the docs** below (imported) before touching anything. They describe the
   project, its architecture, the design system and the content status.
3. **Check the design** in `design/*.png`: compare `md5sum design/*.png` with the
   table in `claude/docs/design.md`. New or changed files must be viewed (see the
   slicing recipe in that doc) and transcribed into `claude/docs/design.md`
   before you build anything from them. Open the PNG of any page you change.
4. **Maintain all three at the end of the prompt**, in English:
   - `claude/rules/*.md` — add or amend a rule whenever the user states a
     preference, corrects you, or a convention is settled.
   - `claude/docs/*.md` — update whatever your change made stale (structure,
     content inventory, open questions, design notes).
   - `design/` — never edit the PNGs; keep `claude/docs/design.md` in sync with them.
   - A new rule or doc file must also be added to the import list below.

## Rules

@claude/rules/workflow.md
@claude/rules/content.md
@claude/rules/seo.md
@claude/rules/code.md

## Docs

@claude/docs/overview.md
@claude/docs/architecture.md
@claude/docs/design.md
@claude/docs/content-status.md
@claude/docs/deployment.md
