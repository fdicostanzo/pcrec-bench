# docs/dev/ — development-process documents

Documents that track execution against the charter, not the product.
Append-only where noted; the restart/status-recovery record for this
project. Shape mirrors ~/pcrec/docs/dev/ (see that CLAUDE.md for the
fuller rationale); ids here carry a `B` prefix (`[B1]` plan rows, `BD1`
decisions) so cross-references between the two repos are never ambiguous.

## Files

- `plan.md` — the ACTIVE milestone/step tracker. Machine-greppable step
  states (`STATE:not-started|started|completed|blocked|deferred`); format
  and grep recipes at the top of the file. Expand a milestone into substeps
  only when work on it begins. Completed rows move to `plan_completed.md`.
- `plan_completed.md` — archive of completed plan rows, grouped by
  completion date, text preserved verbatim.
- `dev_journal.md` — append-only dated journal, newest at bottom. Append an
  entry after every significant work session AND at every stage boundary
  during autonomous runs (journal defensively — the narrative is the only
  thing a crash loses). Primary restart/status-recovery record.
- `decisions.md` — ADR-lite decision log (BD1, BD2, ...): decision, why,
  revisit-when. Add an entry whenever a choice would surprise a future
  reader. pcrec's decisions are cited as `pcrec D52` etc.
- `pcrec_references.md` — the MAP of everything in ~/pcrec that this
  project builds on or must stay consistent with (rulings, plan rows,
  measurement harnesses, discipline docs), with paths and ids. Read-only
  pointers; the pcrec documents themselves are the truth.
- `wake.md` — GITIGNORED hand-off brief for the next manager session,
  rewritten from scratch at every session end or significant pause. On any
  disagreement the committed docs win.

- `reviews/` — D6-style critic-panel records, `YYYY-MM-DD-rN-<topic>.md`,
  each with the findings table, dispositions, and what is owed to Frank.
  R1 (2026-08-24): the requirements note, 29 findings, 27 fixed in v2.

Created when their first row lands (not before): `known_issues.md`
(bugs in pcrec-bench's own harness/adapters/comparator), and
`upstream_findings.md` (findings about OTHER engines, in the archived-
transcript style of pcrec's docs/dev/upstream_issues.md and D35 —
findings about pcrec itself go to pcrec's known_issues.md via the pcrec
manager, never filed here).
