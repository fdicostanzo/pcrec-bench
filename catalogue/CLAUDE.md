# catalogue/ — the interpreter's RULE CATALOGUE and its checks

The versioned catalogue `pcrecbench interpret` reads ([B13];
`docs/design/interpreter_v1.md` is the design note, at v1.2). It sits at
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
| `rules.toml` | THE CATALOGUE: `catalogue_version`, the `[[pin_order]]` table, and 31 `[[rule]]` blocks in 7 classes (R-STATUS 13, R-DELTA 4, R-RANK 1, R-ARM 1, R-FLOOR 3, R-PRED 4, R-BUCKET 5). Every rule carries `id`, `title`, `class`, `since`, `grain`, `aggregate`, `inputs`, `predicate`, `threshold`, `threshold_src`, `slots`, `arith`, `template`, `no_fire`, `links`, `example`, and optionally `extremal`. |
| `check_interpret.py` | `make check-interpret`'s six sections (interpreter_v1.md §8). Never loads the record store. |
| `acceptance_10.py` | §10's ACCEPTANCE TEST, run: every numbered MUST / MUST-NOT on Reports A, B, C and D with its actual firing. Not part of `make check`; run at a catalogue change. |
| `refresh_golden.py` | Regenerates `golden/*.facts.tsv`. Run ONLY in a commit entitled to move a golden fact (§8(2)'s table). |
| `fixtures/fixtures.toml` | The one authored fixture DECLARATION: 58 fixtures, each a real reporter-produced slice plus at most one declared mutation. |
| `fixtures/gen.py` | The generator (`--check` re-derives and diffs), and the synthetic §10 Report D null control. |
| `fixtures/<name>/` | `source.toml` (the declaration, materialised) + the GENERATED `report.tsv` / `index.tsv` / `predictions.tsv`. |
| `fixtures/predictions-inexpressible.tsv` | The two §6.4 clauses that MUST fail at load (P9's span, P12's answer-equality). A fixture, never a committed prediction. |
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

**A diff that touches prose needs a human.** `template`, `no_fire` and
`links` are the only unmechanised prose surface in the system, so
`check-interpret` section 6 flags any diff that touches one and requires
a reviewer's approval line in the commit message naming the rule ids
reviewed (§8(6)). Registering a `[[signature]]` for R-BUCKET-KB is a
MAJOR version bump; catalogue 1.0 registers none, and says so.

## Versioning

`catalogue_version` is MAJOR.MINOR, the record schema's own discipline
(§3.3). MINOR: a rule added, a template's wording, a link, an `example`,
a `[[pin_order]]` append at a re-pin. MAJOR: a predicate or threshold
changes, a rule is removed, `inputs` read a different column, or a
signature is registered. A retired rule keeps its block with
`retired_in` and its id is never reused.

**Every bump regenerates every committed sidecar in the same commit** —
`check-interpret` section 3 re-renders each `reports/*.interpretation.md`
from its own stamped inputs and requires byte equality, so a stale
sidecar is a `make check` failure rather than something a reader has to
notice.

## Running

    python3 -m pcrecbench interpret reports/<name>.tsv            # facts TSV
    python3 -m pcrecbench interpret --render reports/<name>.tsv   # the sidecar
    make check-interpret
    python3 catalogue/acceptance_10.py

At a RE-PIN, append the new pin to `[[pin_order]]` (a MINOR bump): a pin
absent from the table makes R-BUCKET-SPAN exit 2 naming the missing slug
(§11 Q10, ruled "both" — the checklist prevents it, the exit-2 message
makes the fix obvious).

Maintenance: update this file when files are added/removed or change
role.
