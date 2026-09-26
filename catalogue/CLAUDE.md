# catalogue/ — the interpreter's RULE CATALOGUE and its checks

The versioned catalogue `pcrecbench interpret` reads ([B13];
`docs/design/interpreter_v1.md` is the design note, at v1.4). It sits at
the repository ROOT beside `schema/` deliberately: it is a FORMAT with a
version, a validator and a fixture corpus, read by two consumers (the
`interpret` subcommand and `make check-interpret`), not an
implementation detail of one module.

**This directory is where this project's opinions about reading a report
are deliberately CONCENTRATED** (interpreter_v1.md §0): stated once, in
one versioned file, each with its threshold's source, diffable,
reviewable and bumpable — instead of being re-improvised in prose every
time a report is read. It is not a place where opinions are impossible;
it is the place they are visible.

## Files

| file | role |
|---|---|
| `rules.toml` | THE CATALOGUE: `catalogue_version` **3.8** since [B90] (2026-09-25, MINOR: the `[[pin_order]]` append of `ce658cb7`, abi 33 -- no rule moved); **3.7** since [B79] (2026-09-25, MINOR: R-DELTA-5, the CLASS-AWARE D119 verdict over reporter v22's `d119` rows -- a cross-pin cell outside max(IQR, null band), aggregated by capture class first so no bullet pools a capturing and a non-capturing cell -- and R-STATUS-15, the standing I-101 cross-class query firing with the reporter's own clearance sentence; 35 rules, R-STATUS 15, R-DELTA 5; `docs/design/null_band_v1.md` §6). Before it (**3.0**, [B56], 2026-09-19 — MAJOR under the Q2-reframed §3.3: F3/F11's shared-code population fixes (R-DELTA-4's coverage reads the prediction SELECTOR's own glob, not the rows a clause happened to match; R-BUCKET-SPAN's partner search widens to `excluded` rows) and Q4's six-duplicate-rank-row collapse for the four failure quantities all move facts/verdicts on unchanged inputs; R-ARM-2 (F9, additive) and the Q1 did-not-fire REASON channel (F1/F2, additive) ride the same bump; F27 re-anchors `check_stated_utc` to the report's own included population, code only; see `docs/design/predicate_audit_v1.md` and `docs/design/interpreter_v1.md` §3.3/§6.5), the `[[pin_order]]` table, and 32 `[[rule]]` blocks in 7 classes (R-STATUS 13, R-DELTA 4, R-RANK 1, R-ARM **2**, R-FLOOR 3, R-PRED 4, R-BUCKET 5). Every rule carries `id`, `title`, `class`, `since`, `grain`, `aggregate`, `inputs`, `predicate`, `threshold`, `threshold_src`, `slots`, `arith`, `template`, `no_fire`, `links`, `example`, and optionally `extremal`, (catalogue 1.1) `legend` and (catalogue 3.0) `no_fire_reasons` — a CLOSED, slot-free set of per-instance reasons a did-not-fire token may carry in place of the rule's static `no_fire` sentence (§8(6)-reviewed, same discipline as `no_fire`; a rule function returns `(token, reason)` where `reason` must be one of its own declared set); a rule that aggregates and carries a numeric slot MUST declare `extremal` (checked at render time, `check_extremal` — there is no implicit "first numeric slot" default). |
| `check_interpret.py` | `make check-interpret`'s six sections ([B79]: the rule count is 35; the header-parse check admits `interpret.CONDITIONAL_HEADER_KEYS` -- `null_band`, present only on a cross-pin v22 render -- as absent) (interpreter_v1.md §8; 190 checks at catalogue 3.0, [B72smalls]'s Q6 load checks added 35). Never loads the record store. |
| `acceptance_10.py` | §10's ACCEPTANCE TEST, run: every numbered MUST / MUST-NOT on Reports A, B, C and D with its actual firing (25/25 at catalogue 3.0). Not part of `make check`; run at a catalogue change. |
| `refresh_golden.py` | Regenerates `golden/*.facts.tsv`. Run ONLY in a commit entitled to move a golden fact (§8(2)'s table). |
| `fixtures/fixtures.toml` | The one authored fixture DECLARATION: 75 fixtures at catalogue 3.7 ([B79] added 4 on `report_e` -- the v22 capability after-b1885a83 TSV, the first cross-pin render carrying `d119` rows: R-DELTA-5's `router-prefix-order` regress + its all-`within` control, R-STATUS-15's `codegrammar-flat` query hits + a ratio=1.000000 control; 71 before it; 67 at [B56], which added 2: R-ARM-2's control/sabotage pair, `report_d` — the pin 35e1ab1 loglines witness), each a real reporter-produced slice plus at most one declared mutation. A fixture may also declare `subject_grain`/`mutate_subject_grain` (a second real slice, resolved against `decl["subject_grain_<key>"]` — a second BASE, not a mutation) and `predictions_source` (draw `predictions_select` from a declared file other than the default `predictions` key). |
| `fixtures/gen.py` | The generator (`--check` re-derives and diffs), and the synthetic §10 Report D null control. |
| `fixtures/<name>/` | `source.toml` (the declaration, materialised) + the GENERATED `report.tsv` / `index.tsv` / `predictions.tsv` / (since [B47]) `subject_grain.tsv`. |
| `fixtures/predictions-inexpressible.tsv` | The two §6.4 clauses that MUST fail at load (P9's span, P12's answer-equality). A fixture, never a committed prediction. |
| `fixtures/predictions-subject-grain.tsv` | [B47]: two fixture-only clauses (SG1 `grain=subject`, AG1 ruling (α)'s default-widening), never a committed prediction — same precedent as `predictions-inexpressible.tsv`. |
| `fixtures/predictions-utc-before.tsv` / `-utc-after.tsv` | [B56], F27: a `stated_utc` legitimately before / illegitimately after the syntax report's own re-anchored population — checked DIRECTLY in `check_interpret.py` section 1 (a load-time raise is not a firing `expect`/`expect_not` can assert on), same precedent as `predictions-inexpressible.tsv`. |
| `fixtures/predictions-compile-scope.tsv` | [B72smalls], `interpret_subject_grain_v1.md` §6 Q6 (i), RATIFIED: a clean control (a `compile:` quantity's selector names no `subject_or_na`/`regime_or_na`) plus two sabotage rows (one naming each key) — the exact defect shape `capability-0.1-first.tsv`'s P2.a/P2.b carry (Cause B, §1.2). Checked directly in `check_interpret.py` section 1, same precedent as `predictions-inexpressible.tsv`; `load_predictions` stops at its FIRST bad row, so `_tmp_predictions_file` isolates one clause at a time. |
| `fixtures/predictions-testee-glob.tsv` | [B72smalls], `interpret_subject_grain_v1.md` §6 Q6 (ii), RATIFIED: a clean control (`testee=` matches real measured `syntax@0.1` pcrec testees in the frozen `golden/index@2026-09-09.tsv` snapshot), a sabotage row (the P4.a defect shape, `pcrec_*-auto-*` — a hyphen where every real testee_id has an underscore), and a VACUOUS control (the same sabotaged glob against an unmeasured `(subbench, version)`, which must NOT raise). Exercises `check_testee_globs` (store-free: reads `index.rows` only, never a record), checked directly in `check_interpret.py` section 1. |
| `golden/index@<date>.tsv` | The FROZEN `store/index.tsv` snapshot the golden comparison reads. |
| `golden/<report>.facts.tsv` | The pinned facts for §10's acceptance reports. |

## Three rules that are not obvious from the files

**The catalogue is a contract, not a rule engine.** `predicate` is PROSE,
for the reader; the executable predicate is a python function in
`pcrecbench/interpret.py` named exactly the rule id lowercased with `-`
→ `_` (`R-DELTA-1` → `r_delta_1`). `make check-interpret` section 1
asserts every `[[rule]]` has a function and every function a `[[rule]]`,
and every rule function is handed a view that RAISES on any column
outside that rule's declared `inputs`. A DSL would be a second language
to get wrong (§11 Q7).

**No rule introduces a threshold of its own.** Every `threshold` is
either a token or number `report.py`/`reduce.py` already computed and
printed (`timer-floor`, `faster ×N`, `selection changed`, `disagree`,
a header integer), a comparison of two measured quantities from the same
report, or a boundary that is DEFINITIONAL and says so (`≥ 1.0`,
"crosses 1.0"). The one rule that computes rather than reads, R-ARM-1,
COPIES `_cross_pin_verdict`'s arithmetic and declares it in `arith`.

**A diff that touches prose needs a human.** `template`, `no_fire`,
`legend` (catalogue 1.1) and `links` are the only unmechanised prose
surface in the system, so `check-interpret` section 6 flags any diff
that touches one and requires a reviewer's approval line in the commit
message naming the rule ids reviewed (§8(6)) — read against `HEAD~1
.. HEAD` of whatever commit is checked out, so it is the MERGE commit
the approval line belongs on: a lane's own WIP commits are not the
review, and `make check-interpret` legitimately fails section 6 in a
lane's own worktree until the manager's merge commit carries the line.
Registering a `[[signature]]` for R-BUCKET-KB is a MAJOR version bump;
catalogue 1.1 still registers none, and says so.

## Versioning

`catalogue_version` is MAJOR.MINOR, the record schema's own discipline
(§3.3). **AMENDED 2026-09-19** (Frank, `docs/design/predicate_audit_v1.md`
§7 Q2): the unit of compatibility is whether emitted FACTS/VERDICTS are
comparable across the boundary, not whether a catalogue field's text
moved. MAJOR: a fact or verdict moves on UNCHANGED inputs — a predicate
or threshold changes, a rule is removed, `inputs` read a different
column, a SHARED HELPER's population changes what several rules can see
(the 2.0 bump's own shape), or a signature is registered. MINOR:
additive — a rule added, a template's wording, a link, a `legend` line,
an `example`, a `[[pin_order]]` append at a re-pin, an appended column.
A field-text edit is an INSTANCE of MINOR, never its definition — a
wording change that happens to move a verdict is MAJOR regardless of
its size. A retired rule keeps its block with
`retired_in` and its id is never reused.

**Every bump regenerates every committed sidecar in the same commit** —
`check-interpret` section 3 re-renders each `reports/*.interpretation.md`
from its own stamped inputs and requires byte equality, so a stale
sidecar is a `make check` failure rather than something a reader has to
notice.

**Both [B72smalls] (2026-09-22) stopgaps are RETIRED ([B93], 2026-09-25/26,
Frank's ruling + the manager's P4 follow-up ruling;
`docs/dev/lanes/b93pred_report.md`).** Q6 (i)'s load check correctly
refused `docs/dev/predictions/capability-0.1-first.tsv` at load (P2.a/
P2.b's already-diagnosed Cause-B defect) — stamped `predictions` on FOUR
committed sidecars (`2026-09-17-capability-0.1-...-first-a770139e`,
`2026-09-18-...-after-cf0962e3`, `2026-09-18-...-ext-first-cf0962e3`,
`2026-09-19-...-ext-second-cf0962e3`), so `interpret()` refused to run
for any of them, and this section's own `section_1`/`section_3` carried
a NAMED, provisional exception (`_KNOWN_HISTORICAL_LOAD_DEFECTS`,
`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_RULING`) filed for a ruling
rather than silently absorbed. Frank ruled candidate (b) of that
filing: fixing an ALREADY-DIAGNOSED, ALREADY-WRITTEN-UP authoring
defect that moves no predicted value is NOT the revision the
predictions-immutability rule was meant to forbid — `docs/dev/
predictions/CLAUDE.md`'s new "Revising an already-scored file" section
states the resulting standing rule, and P2.a/P2.b are fixed in the
committed file itself under it.

Retiring that stopgap surfaced a SECOND, separate Cause-C defect
(P4.a/P4.b's testee-glob typo, Q6 (ii)) that Cause B's earlier-raising
crash had been masking — filed, not fixed, the same day, pending a
ruling (a second, differently-named stopgap,
`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`, kept `make
check-interpret` green while it was open). **The manager ruled the
SAME DAY**: both P4 clauses' notes state their meaning unambiguously
(cross-pattern `ratio_to` comparisons, exactly P2's own shape), so the
glob and both reducers are fixed too, each hand-verified against the
report TSV / underlying records before being trusted (`docs/dev/
predictions/CLAUDE.md`'s file entry has the full table). ALL THREE
named exceptions this file's history has carried
(`_KNOWN_HISTORICAL_LOAD_DEFECTS`, `_SIDECARS_BLOCKED_ON_CAPABILITY_
FIRST_RULING`, `_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_P4_CAUSE_C`) are
GONE from `check_interpret.py` — Q6 (i)/Q6 (ii) now pass on every
committed predictions file with no exception, exactly as they would
for a file that never carried either defect, and the four sidecars are
regenerated for real (`make check-interpret`: 203 passed, 0 FAILED).
One residual, NOT part of this fix: P4.b's own `subject_or_na`/
`regime_or_na` selector keys need `grain=subject` to ever be reachable
at set grain (Cause A, a third, separate structural fact) — outside
the manager's three-part ruling, so P4.b stays `not evaluable`
(correctly, safely, no crash) on every report; hand-derived from the
underlying records and cross-checked against the committed
subject-grain TSV anyway, for the record (`docs/dev/predictions/
CLAUDE.md`).

## Running

    python3 -m pcrecbench interpret reports/<name>.tsv            # facts TSV
    python3 -m pcrecbench interpret --render reports/<name>.tsv   # the sidecar
    make check-interpret
    python3 catalogue/acceptance_10.py

The committed `reports/<name>.interpretation.md` sidecars ([B13.4]) are
never produced by hand: run `/pcrec-bench-interpret <report>`
(`.claude/skills/pcrec-bench-interpret/SKILL.md`), which locates a
matching predictions file, runs `interpret --render`, checks its own
determinism, and commits the result beside its report.

At a RE-PIN, append the new pin to `[[pin_order]]` (a MINOR bump): a pin
absent from the table makes R-BUCKET-SPAN exit 2 naming the missing slug
(§11 Q10, ruled "both" — the checklist prevents it, the exit-2 message
makes the fix obvious).

Maintenance: update this file when files are added/removed or change
role.
