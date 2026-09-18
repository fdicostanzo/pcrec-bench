# Lane `r7consol` — consolidate the R7 panel on `predicate_audit_v1.md`

Branch `lane/r7consol`, worktree `worktrees/r7consol` off `master` at
`8a0ec37`. Read-only against `~/pcrec`; no code, no catalogue, no store,
no report change — docs only, per the brief.

## Charter vs. committed

| brief item | committed |
|---|---|
| Read the three critic files + the target note | done; the three critic files were untracked in `master` at lane start and were imported into this lane and committed (`fb5d3ce`) so the deliverable's inputs are reproducible from the branch alone |
| Apply the 13 ACCEPT-AND-APPLY dispositions to `predicate_audit_v1.md`, each citing its finding id | done, `3af97af`; grep-verified all 13 ids (`r7ver-1..8` minus 7/9, `r7pop-1/2/3/5`, `r7code-1/2`) appear in the revised note |
| Record r7ver-9 and r7code-3 as CLEAN, consolidation-table row only | done — no edit to the note for either; both recorded in the consolidated review's disposition table and "CLEAN dispositions" section |
| Escalate anything impossible to apply as stated, with a reason | none needed — every disposition applied cleanly as given; the deliverable states this explicitly |
| Deliverable 1: `docs/dev/reviews/2026-09-18-r7-predicate-audit.md` — by-id table, completeness check RUN, overall verdict | done — the completeness check is the actual `grep -oE` output pasted in, not a hand-built list (17/17: 5 popsem + 9 versioning + 3 code, matching the brief's own count) |
| Deliverable 2: `predicate_audit_v1.md` bumped to v1.1, every accepted edit applied in place, each citing its finding id | done — header bumped, a v1.1 changelog paragraph added, and every edit inline cites its id (`r7ver-N`/`r7pop-N`/`r7code-N`) |
| Deliverable 3: `make check-interpret` green | done — 149/149, unaffected as expected for a docs-only change |
| Deliverable 4: lane report | this file |
| Do not merge | not merged; branch left for the manager |

## What "applying" the dispositions actually meant

The 13 accepted dispositions were not independent one-line edits — several
interlocked, and applying them required tracing the actual code the
critics cited (not just trusting their prose) to state the corrected fix
shapes precisely:

- **r7ver-1 + r7ver-2 + r7ver-4** together required rebuilding §6 from a
  two-cost prose grouping into a fix-by-fix table with five cost columns
  (catalogue bump, `INTERPRET_VERSION`, sidecars, fixtures, goldens), a
  new Group 1B for F7 alone, and F7b split into a code half and a
  catalogue half with different costs.
- **r7ver-3** required a new §6.05 subsection stating `INTERPRET_VERSION`'s
  bump rule by the `REPORTER_VERSION` analogy the versioning critic cited,
  then folding a bump requirement into eight named fixes' cost lines
  (F3, F7, F7b-code, F11, F15, F16, F19, F27) — exactly the set r7ver-3
  named, not a broader set I inferred.
- **r7pop-1** required redoing the hand computation the critic ran
  (`321 → 66` values, `nums[len//2]` landing in the zero block both
  before and after) rather than just asserting the critic's conclusion,
  since the point of the finding is that the ORIGINAL claim was uncited.
- **r7code-1**'s rewrite of F27 is the largest single edit: the corrected
  join (OD-B15's dedup key, not the R-STATUS-1 join) had to be stated
  precisely enough that an implementer could build it without re-deriving
  it from the critic's file, including the `check_stated_utc` signature
  change the original fix shape never mentioned.
- **r7ver-7 and r7pop-4** were folded into F27's section (per the
  manager's explicit instruction) rather than filed as separate findings,
  since both are stated risks for the SAME ruling (F27's re-anchor), not
  independent defects.

## What is NOT claimed

This lane does not claim the corrected fix shapes are final or
implementation-ready in every particular — F9's fixture-pair/golden-file
exposure and F3/F4's possible golden movement are stated as UNMEASURED
open questions in §6's cost table (r7ver-4's own ask), not resolved,
because resolving them would require running `acceptance_10.py` against
hypothetical rule changes that don't exist yet — out of scope for a
docs-only consolidation lane with no code changes permitted. The
recommended order in §6 is re-derived to say so explicitly rather than
silently keep the v1 draft's cheap-then-expensive framing.

## Validation

`make check-interpret`: 149 passed, 0 failed (`docs/design/CLAUDE.md` and
`docs/dev/reviews/CLAUDE.md` are not read by any check; the target note
and the reviews directory are outside `check-interpret`'s scope entirely
— confirmed green as a smoke check per the brief's ask, not because the
change could plausibly break it).

No heavy runs. No store, schema, catalogue, or `pcrecbench/` file
touched. Commits: `fb5d3ce` (import the three critic files),
`3af97af` (the consolidation itself).
