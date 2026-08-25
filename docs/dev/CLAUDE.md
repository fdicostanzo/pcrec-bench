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
  R2 (2026-08-25): the merged record schema, 22 findings, all carried
  by the schema v1.1 lane.

- `feedback_pcrecdev1_2026-08-25.md` — the pcrec manager session's
  feedback on the first production sample (what is missing to act on an
  outlier; what it distrusts; five ranked sub-bench areas), for Frank.
- `feedback_pcrecdev1_2026-08-25-repin.md` — its reading of the re-pin
  report as it reads (actionability, the facts it had to interpret, a
  prediction list with verdicts), the first input to [B13].
- `inbox_from_pcrec.md` — the DURABLE CHANNEL IN (pcrec D78 / BD5):
  written and committed ONLY by the pcrec manager session (`[inbox]`
  commits); rulings, priorities, re-pin targets, requests. This session
  reads it at wake, moves each new item into plan.md and appends one
  `ack: <date> — <where>` line under it — the only thing it writes here.
- `outbox_to_pcrec.md` — the DURABLE CHANNEL OUT: written ONLY by this
  session (findings about pcrec, requests for pcrec changes, questions
  that must outlive the session); the pcrec manager reads it at wake.
  Items `O-n`, never deleted.
- `upstream_findings.md` — findings about OTHER engines with the record
  that shows them (U1 2026-08-25: pcre2-jit's 60 s timeout on the
  factored email pattern over 1 MB of `a`). Findings about pcrec go to
  the pcrec manager for pcrec's known_issues.md, never here.

- `known_issues.md` — bugs in pcrec-bench's OWN harness/adapters/
  reporter (`KB-n`); KB-1 the runtime_options bare-flag pairing.
