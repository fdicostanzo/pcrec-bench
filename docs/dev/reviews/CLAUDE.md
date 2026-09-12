# docs/dev/reviews/ — critic-panel reviews (pcrec D6 style)

A REVIEW is the compiled output of an adversarial critic panel on a
design or a major piece of code (the manager skill §6): 2-4 independent
READ-ONLY critics with distinct lenses, briefed to refute, whose findings
the manager consolidates with a triage DISPOSITION per finding —
`accepted (applied)`, `accepted-amended per R-n`, `rejected: <why>`,
`escalated: <what must be ruled>`, `deferred: <to whom>` — and fixes
with measurement before disposition where a finding is measurable.
Files are named `YYYY-MM-DD-rN-<topic>.md` and never edited after the
dispositions are applied (a later panel on the same topic is r(N+1)).
The manager's rulings that decide a panel's blockers may be recorded
beside it as `…-rN-rulings-<topic>.md` (verbatim, dated), so a
disposition's authority is citable.

| file | what |
|---|---|
| `2026-08-24-r1-requirements.md` | the requirements note ([B1]) panel |
| `2026-08-25-r2-record-schema.md` | the record schema ([B2]) panel — the format the later files follow |
| `2026-08-30-r3-rulings-gate-shape-v14.md` | the manager's rulings R-1..R-20 on the r3 blockers (MINOR with §4 amended; the tri-state target field + pre-flight refusal; §3.5 arithmetic; the GROUP rule replacing F; N ≥ 5 and odd; exit code 4; harness-failure left unreachable; KB-4's schema half; the timeline as provenance; k stays 1.5) — written before r3 was compiled |
| `2026-08-30-r3-gate-shape-v14.md` | the [B20] panel on docs/design/gate_shape_v14.md (three lenses: measurement validity, schema/validator consistency, harness/reporter/checks/migration): 45 findings, 29 accepted / 15 amended / 1 deferred / 0 rejected; E-1..E-3 escalated and ruled; the spec was rewritten from it (merge 2aca1cd) |
| `2026-09-07-r4-interpreter-v1-source.md` / `-charter.md` / `-build.md` / `2026-09-07-r4-interpreter-v1.md` | the [B13] panel on docs/design/interpreter_v1.md (three lenses: source verification, charter fidelity/scope, implementability): 56 raw findings across the three individual reports, consolidated into 11 BLOCKING + 8 SHOULD-FIX + ~14 WORTH-NOTING in the merged file, all accepted/accepted-amended by the manager (Q3 the only item carried forward to Frank, pre-existing and untouched by this panel) — architecture sound, several rules as specified don't match the TSV they read, the §10 acceptance test cannot be satisfied as written; a revision lane produces v1.1 before any implementation lane opens. **Closed 2026-09-08** by two APPENDED sections (the one sanctioned edit after dispositions: a cycle's closing record, session_discipline.md §7(a)/(b)): the step-2 confirmation pass run by pcrecdev1 at Frank's ask (inbox I-58: 19/19 dispositions confirmed, one stale citation, four spec edits → v1.2) and the by-id completeness table over all 56 raw finding ids — which found a THIRD dropped id (charter F9) beyond the two the revision lane had named, all three already applied in v1.1/v1.2 |
| `2026-09-12-r5-capability-set-v1-charter.md` / `-semantics.md` / `-schema.md` / `2026-09-12-r5-capability-set-v1.md` | the [B42] panel on docs/design/capability_set_v1.md v0.1 (three lenses: charter fidelity/provenance/build plan, engine semantics/measurement validity, schema/harness/reporter/.rxt consistency): 26 raw findings consolidated into 8 BLOCKING + 8 SHOULD-FIX + 8 WORTH-NOTING, every claim independently re-verified against source, by-id completeness 26/26 at drafting; all dispositions RATIFIED by the manager with three amendments from Frank's same-day live rulings (Q2 resolved as realism-not-ratio; Q10-Q12 superseded — the set is built ON `.rxt` for real and the effort PARKS at the format's capability roadblock, feeding pcrecdev1 `docs/design/rxt_needs_v1.md`; Q3 BLOCK at the restart). Headline defects: convention-based scoring and `variant.kind` rendering both claimed built and both unimplemented; `patterns[].tags` bucketing dead by the schema's own rule; the hazard-rewrite rule keyed on an unassigned field; the ReDoS family's calibration risk; the match-regime cut over-broad |

Maintenance: add a row per review; do not renumber.
