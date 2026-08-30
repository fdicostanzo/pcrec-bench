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

Maintenance: add a row per review; do not renumber.
