# Workflow rules

- Talk to the user in French (their language). Write everything under `claude/`
  and all code comments in English. Site content is in French.
- Start every prompt by reading `claude/rules/`, `claude/docs/` and checking
  `design/` as described in `CLAUDE.md`. End every prompt by updating them.
- Keep rules short and imperative: one bullet per rule, with the reason when it
  is not obvious. Remove rules that turn out to be wrong rather than piling up
  exceptions.
- Docs describe what *is*, not what was done: no changelog, no dates of edits.
  Git history is the changelog.
- Preview with `make serve` (Docker, same gems as GitHub Pages) and check pages
  in the browser before saying a visual change is done. `make build` must pass
  with no Liquid warning.
- Never commit or push unless the user asks. GitHub Pages publishes whatever
  lands on the publishing branch, so a push is a production deploy.
- Never invent facts about the user's projects (dates, versions, licences,
  download links, prices, client names). Missing facts go to the open questions
  in `claude/docs/content-status.md`, and the page omits them.
- The design PNGs are the reference. When the code must diverge from them
  (responsive, accessibility, missing content), note why in `claude/docs/design.md`.
