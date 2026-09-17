# interpret at SUBJECT GRAIN — a design note (v1, 2026-09-17)

**Status: PROPOSED, not adopted. D6-panel input.** Written by lane
`b42subgrain` on Frank's charter at the 2026-09-17 reset ([B42] follow-up
(iii)). The question of record is
`docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md` §7.1: *"Give
`interpret` a subject-grain input for this set's next sample … so
P2/P3/P4/P6/P7/P10 become evaluable rather than six of ten predictions
landing `not evaluable` by construction. A catalogue/interpreter design
question, not a rendering flag."*

This note takes that question seriously enough to test it, and the first
thing the test says is that **the ledger's diagnosis is right for four of
the six and wrong for two**. Everything below is derived from the
committed artefacts and from measurements run in this lane; every number
carries its source. Contested cells are marked MEASURED or UNMEASURED
explicitly.

**Scope.** This note decides nothing. It states the mechanism, prices the
options, names the acceptance cases, and puts eleven questions to Frank
(§6). Implementation is a later lane against whatever is ruled.

---

## §0. What was measured in this lane, and how

Four probes, all read-only, none touching `store/` or `~/pcrec`:

| # | probe | method | where |
|---|---|---|---|
| M1 | per-clause selector attribution for all 15 clause rows of `capability-0.1-first.tsv` against the committed set-grain TSV | a python probe importing `interpret.parse_selector`, `interpret._glob_match` and `interpret._COMPILE_METRIC` — the interpreter's OWN resolution, not a reimplementation | §1 |
| M2 | the same 15 clauses against a real subject-grain TSV of the identical query | as M1, over the file M3 rendered | §4 |
| M3 | a `--grain subject --format tsv` render of the capability report's own committed query | `python3 -m pcrecbench report … --grain subject --format tsv`, detached, `/usr/bin/time -v` | §2, §3 |
| M4 | `n_wrong`/`n_gave_up` over every `rank` row in every committed report TSV | a python scan of all 43 `reports/*.tsv` | §5 |

M3's exact command is the committed query from the report's own header
(`reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.tsv:1`),
with `--grain subject --format tsv` substituted. It ran at
**100.75 s wall, 678,016 KB peak RSS**, exit 0, on the live store
(169-row `store/index.tsv`), producing **206,331 lines / 35,126,390 bytes**.

---

## §1. Why six of ten predictions were machine-unevaluable

### §1.1 The mechanism, from the code

`interpret._select` (`pcrecbench/interpret.py:1706-1731`) resolves a
prediction's selector in three steps:

1. `section` is popped out of the selector.
2. The sections to read are chosen: `["compile"]` if the `quantity` is one
   of the four `compile:` metrics; else the sections the `section` glob
   names; else — **and this is the default that matters** —
   `["rank"]` (`interpret.py:1723-1724`).
3. Every remaining selector clause is glob-matched against the row's own
   column of that name (`interpret.py:1728`).

A clause that matches no row anywhere in the chosen sections yields an
empty selection, which R-PRED-3 renders as `not evaluable: no row in this
report matches the selector` (`interpret.py:1948-1950`).

Two column conventions decide the outcome, and they are not the same
convention:

- **`subject_or_na` on ranking-family rows is the literal `(set)` at set
  grain** (`report.py:4413`: `subject_id = "(set)"`). MEASURED on the
  capability report: `awk -F'\t' '$1=="rank"{print $3}' | sort -u` returns
  exactly one value, `(set)`, over all 5,088 `rank` rows.
- **`subject_or_na` AND `regime_or_na` on `compile` rows are the EMPTY
  STRING** (`report.py:4493`, which writes `"", ""` into both slots).
  MEASURED: the same `awk` over `$1=="compile"` returns exactly `[][]`.

`docs/design/interpreter_v1.md:344-350` already records the first half of
this ("`subject_or_na` has two spellings of 'absent'", panel build #16).
It does not extend the observation to `regime_or_na`, and
`docs/dev/predictions/CLAUDE.md` — the file an author of a prediction
reads — states neither.

### §1.2 The attribution, clause by clause (M1)

Re-resolving all fifteen clause rows of
`docs/dev/predictions/capability-0.1-first.tsv` through the interpreter's
own functions against the committed set-grain TSV:

| clause | quantity | section read | rows matched | the clause that matched ZERO rows |
|---|---|---|---|---|
| P1.a / P1.b / P1.c | `n_wrong` | `rank` | 18 each | — |
| **P2.a** | `compile:median_total_ns` | `compile` | **0** | `regime_or_na=n/a` |
| **P2.b** | `compile:median_total_ns` | `compile` | **0** | `regime_or_na=n/a` |
| **P3** | `median_ns` | `rank` | **0** | `subject_or_na=t-1m` |
| **P4.a** | `compile:artifact_bytes` | `compile` | **0** | `testee=pcrec_*-auto-*` |
| **P4.b** | `median_ns` | `rank` | **0** | `subject_or_na=lp-atomic-nonmatch` **and** `testee=pcrec_*-auto-*` |
| P5.a | `n_wrong` | `rank` | 198 | — (see §5) |
| **P6.a / P6.b** | `n_wrong` | `rank` | **0** | `subject_or_na=v-uuid-badnibble` |
| **P7** | `n_wrong` | `rank` | **0** | `subject_or_na=v-ipv4\|v-ipv4-oor` |
| P8 | `section` | `did_not_compile` | 10 | — |
| **P10.a / P10.b** | `n_wrong` | `rank` | **0** | `subject_or_na=nu-lead-no-cont` / `nu-lead-with-cont` |

The eleven zero-matching clauses fall into **three distinct causes, not
one**:

**Cause A — the grain gap. Seven clauses, five parents (P3, P4.b, P6.a,
P6.b, P7, P10.a, P10.b).** The clause names a real subject id;
`subject_or_na` at set grain holds `(set)`; no row in the file can match.
This is the cause the ledger names, and it is a majority — but not all — of
the failures.

**Cause B — `n/a` is not how the TSV spells "no regime". Two clauses, one
parent (P2.a, P2.b).** The author wrote `regime_or_na=n/a`, a literal
reading of the column's own NAME. `compile` rows carry `""`. **A
subject-grain input does not help P2 at all**: the `compile` section is
rendered by a loop (`report.py:4490-4513`) that is entirely independent of
`rd.grain`, so `regime_or_na` is `""` at both grains. MEASURED in M2:
P2.a/P2.b still match zero rows in the subject-grain TSV.

**Cause C — a testee glob that matches no testee that exists. Two clauses,
one parent (P4.a, and jointly P4.b).** `testee=pcrec_*-auto-*` compiles
(via `interpret._glob_match`, `interpret.py:1616-1621`) to
`^pcrec_.*\-auto\-.*$`. Every pcrec testee id in this store is
`pcrec_<pin>_auto-<caps>-simdna` — an **underscore** before `auto`, not a
hyphen: `pcrec_a770139e_auto-caps-simdna` fails the glob. Grain is
irrelevant; MEASURED in M2, P4.a/P4.b still match zero rows at subject
grain.

### §1.3 The correction to the ledger, stated plainly

> A subject-grain input alone makes **four** of the six not-evaluable
> parents evaluable (P3, P6, P7, P10) and **half of a fifth** (P4.b, which
> still needs its testee glob repaired). **P2 is untouched by any grain
> change whatsoever.**

This matters for the charter. "Give `interpret` a subject-grain input"
(ledger §7 item 1) is necessary but not sufficient, and two of the six
failures are authoring / column-convention defects that a grain change
would leave in place while *appearing* to have addressed them — the next
sample would report 2 of 10 not-evaluable and a reader would reasonably
conclude the remaining two were genuine measurement gaps. They are not.

### §1.4 A fourth finding: `_elsewhere` is blinded by the same gap

`interpret._elsewhere` (`interpret.py:1737-1742`) exists precisely so
R-PRED-3 can say WHERE a missing cell went (`excluded`, `not_ranked`,
`did_not_compile`, `scratch`) instead of "absent". It did not fire for any
of the eleven clauses, and the sidecar's six R-PRED-3 lines all read the
bare `no row in this report matches the selector`
(`reports/2026-09-17-capability-0.1-budu-ryzen1600-first-a770139e.interpretation.md`,
the R-PRED-3 block). The reason: `_elsewhere` re-runs the SAME selector
against the other sections, and those sections carry `(set)` in
`subject_or_na` too (`report.py:4457`, the `others` loop) — so a
subject-scoped clause is unsatisfiable there as well.

Consequence: today the interpreter cannot distinguish

- "the selector is unsatisfiable at this grain" (Cause A),
- "the selector is misspelled" (Causes B and C), and
- "the cell genuinely is not in this report",

and prints the same sentence for all three. That is a diagnosis gap
independent of the grain gap, and it is the cheapest thing on this page to
fix (§6 Q6, Q10).

---

## §2. The options

Throughout: **the invariant that `interpret` never loads the record store
is treated as inviolable** unless a proposal explicitly argues to break it.
None does; see §3.

### §2.0 The mechanism that already exists (and is untested)

This is the single most important fact for costing every option below, and
it is not recorded in the ledger or in `docs/design/interpreter_v1.md`'s
own §11 Q2.

**`interpret` already accepts a second, subject-grain report TSV.**

- `--subject-grain PATH` is a real, shipped CLI flag
  (`interpret.py:2101`).
- It is threaded to `InterpretCtx.subject_grain` as a second `ReportTsv`
  (`interpret.py:1274-1280`, `2040-2056`).
- One rule consumes it: `r_bucket_dominated` builds a second `RuleView`
  over that file under its own declared `inputs`
  (`interpret.py:1084-1087`), and returns the token `input-absent` when it
  is not supplied.
- `docs/design/interpreter_v1.md:481` already anticipates the file by name
  — `<name>.subject-grain.tsv` for every report group — as a recorded
  follow-up, and §11 Q2 rules `input-absent` "until a separate reporter
  change commits" it.

So option (a) is not a new architecture; it is **a half-built one**. What
is missing is three things, and each is a separate cost:

- **(a1) No `.subject-grain.tsv` exists.** The reporter commits a
  `.subject-grain.md` for all 43 report groups and has never committed the
  TSV. MEASURED at `HEAD`: `reports/*.tsv` 43, set-grain `*.md` 43,
  `*.subject-grain.md` 43, **`*.subject-grain.tsv` 0**, `*.interpretation.md`
  4. (`reports/CLAUDE.md:38` states the same three-renderings-per-group
  shape at its own 42-group vintage.)
- **(a2) The prediction evaluator cannot reach it.** `_select` reads
  `view` — the PRIMARY report — and nothing else (`interpret.py:1726-1727`).
  No prediction clause can select a subject row however the file is
  supplied. This is the whole of option (b).
- **(a3) The stamp is not closed over it — a live latent defect.**
  `build_stamp` (`interpret.py:2067-2086`) records `report`, `index`,
  `predictions` and their sha256s; it does not record `--subject-grain`.
  `catalogue/check_interpret.py`'s section-3 freshness re-render recovers
  inputs from the stamp and calls `run_interpret(report, index, pred, "md")`
  (`check_interpret.py:254-267`) with **no** subject-grain argument. So a
  sidecar rendered today WITH `--subject-grain` would re-render WITHOUT it,
  the facts would differ (R-BUCKET-DOMINATED flips from `input-absent` to a
  firing list), and `make check-interpret` section 3 would fail on an
  unmodified file. **This is broken today**, and is unexposed only because
  no committed sidecar uses the flag. It should be fixed regardless of
  every ruling below (§6 Q10).

Corollary worth stating for the panel: **R-BUCKET-DOMINATED's firing path
has never been executed by a fixture, a golden or a committed sidecar.**
`catalogue/fixtures/fixtures.toml:442-446` declares exactly one fixture for
it, `R-BUCKET-DOMINATED__input-absent`, with `expect_token = {
"R-BUCKET-DOMINATED" = "input-absent" }`. `fixtures.toml` has no
`subject_grain` key at all, and `check_interpret.py` never passes one. Any
option that starts supplying the file is also the first real test of ~30
lines of shipped code.

### §2.1 Option (a) — a subject-grain TSV as a second interpret input

*The reporter commits `<name>.subject-grain.tsv` beside the existing
`.tsv` / `.md` / `.subject-grain.md`; `interpret` is invoked with
`--subject-grain` on it.*

**Determinism.** Unchanged in kind. The subject-grain TSV is a
deterministic function of the same records under the same query; two input
files with two sha256 stamps is exactly the contract `report` + `index` +
`predictions` already carry. Requires (a3) fixed so the stamp is closed
over the second input, and `check_interpret.py`'s re-render to pass it.

**Fixture / golden strategy.** `make check-interpret` still never loads
the store: both inputs are committed TSVs, and the fixture generator
already slices a committed report (`catalogue/fixtures/gen.py`, declared in
`fixtures.toml`). The changes:

- `fixtures.toml` gains an optional per-fixture `subject_grain` source, and
  `gen.py` materialises a second slice into the fixture directory. This is
  the same "generated base plus one declared mutation" shape §8(4) already
  fixes (`interpreter_v1.md:2190`); a subject-grain slice is a second
  *base*, not a mutation, so the "exactly one declared mutation" assertion
  is unaffected.
- R-BUCKET-DOMINATED gets its first firing fixture and a control. That is a
  net GAIN in coverage, not a cost.
- Golden facts: the three acceptance reports' goldens move iff they are
  re-derived with a subject-grain input. Recommendation is that they are
  NOT (keep the acceptance set at set grain only), so §10's 25/25 is
  untouched — but this is a ruling (§6 Q8).

**Catalogue versioning.** Two cases, and the panel should be clear which
it is buying:
- Supplying the file and letting only R-BUCKET-DOMINATED consume it:
  **no catalogue change at all** (no rule's `inputs`, predicate or
  threshold moves). MINOR at most, for the `example` field that currently
  says "No committed report group has a `.subject-grain.tsv`"
  (`rules.toml:1208-1212`), which becomes false.
- Letting R-PRED-* consume it (i.e. adopting (b) too): the four R-PRED
  rules' `inputs` change to read a **different file**. By §3.3's letter —
  "`inputs` change in a way that reads a different column" — this is at
  minimum arguable and at maximum **MAJOR**. §6 Q3 puts it to Frank.

**Cost.** One extra `report` invocation per group — a STORE-LOADING run.
Priced in §3.

**Size.** MEASURED (M3): for the capability report's own query, the
subject-grain TSV is **35,126,390 bytes / 206,331 lines** against the
set-grain TSV's **1,230,812 bytes / 8,217 lines** — **×28.5 by bytes,
×25.1 by lines**. Section breakdown: `rank` 202,794 rows (was 5,088),
`did_not_compile` 390 (was 10), `excluded` 53 (was 25),
`compile` 3,031, `compile_stamp` 54, `record` 7 — the last three
byte-identical in content to the set-grain file, since those loops are
grain-independent.

33.5 MiB of committed TSV per report group is the strongest argument
against (a) as stated, and the reason §2.5 exists.

### §2.2 Option (b) — a catalogue selector extension

*Extend the prediction selector grammar (`interpreter_v1.md` §6.3) so a
clause can say which grain it means — a sixth key `grain=subject`, or a
`subject:` quantity prefix mirroring the existing `compile:` prefix.*

**This is not an alternative to (a); it is the second half of it.** A
selector that says `grain=subject` with no subject-grain file supplied is
unsatisfiable, and a subject-grain file with no way to route a clause to it
leaves every R-PRED clause exactly as blind as it is today (a2). The two
must be ruled together or neither is worth building.

**Determinism.** Unaffected. The routing is a pure function of the parsed
prediction row.

**Closed-set discipline.** `SELECTOR_KEYS` is a closed set whose violation
is a named LOAD ERROR (`interpret.py:1608-1611`), and `docs/dev/predictions/
CLAUDE.md:31-33` states the same discipline for `quantity` / `reducer` /
`op`. Adding a key is therefore a deliberate, checkable, one-line change —
and every existing predictions file keeps loading, because the new key is
optional and its absence means "set grain", which is what every committed
row means today.

**Which spelling.** Two candidates:
- `grain=subject` as a sixth selector key. Says WHERE to look, alongside
  the five keys that already say which rows.
- a `subject:` quantity prefix (`subject:median_ns`), mirroring `compile:`.
  Rejected here: `compile:` already conflates WHAT is measured with WHICH
  section is read, and P2 is direct evidence that readers misunderstand
  that conflation — the author wrote a `regime_or_na` clause for a quantity
  whose section route had already been decided by its prefix. Repeating the
  pattern doubles the confusion. Recommendation and reasoning at §6 Q2.

**Fixtures.** One prediction fixture with a subject-grain input, plus its
control. `catalogue/fixtures/predictions-inexpressible.tsv` is the existing
precedent for a prediction-shaped fixture
(`docs/dev/predictions/CLAUDE.md:48-49`).

**Catalogue versioning.** MAJOR, most likely, per §2.1.

### §2.3 Option (c) — per-grain interpret runs

*Run `interpret` twice — once on the set-grain TSV, once on the
subject-grain TSV as the PRIMARY report — and commit two sidecars.*

**This does not work for predictions, and the reason is in the catalogue.**
All four R-PRED rules declare `grain = ["set"]` (MEASURED by reading every
`id`/`grain` pair out of `catalogue/rules.toml`: R-PRED-1, R-PRED-2,
R-PRED-3 and R-PRED-4 are all set-only; 13 of the 31 rules are). On a
subject-grain report they do not fire at all — they emit the `grain`
did-not-fire token — so **no prediction would be scored in the
subject-grain run**, which is the entire purpose of the exercise.

Flipping them to both grains is not a wording change. `interpreter_v1.md`
§3.2.1 states why `grain` became mandatory in the first place, and both
reasons bite here, MEASURED on M3's file:

- `_n_and_pass_rate` returns `n_subjects` at set grain and `n_trials` at
  subject grain **into the same `n` column** (`report.py:3436-3438`).
  MEASURED: the capability set-grain `rank` rows carry `n=75` (subjects);
  the subject-grain rows carry `n=5` (trials). A rule or prediction reading
  `n` means two different things depending on which file it got.
- `delta_verdict` is populated only at set grain (`report.py:4441`).
  MEASURED: **0 of 202,794** subject-grain `rank` rows carry a non-empty
  `delta_verdict`. Every cross-pin prediction and all four R-DELTA rules go
  dark.

Two further costs:

- A subject-grain sidecar would be ~42 % did-not-fire rows by construction
  (13 set-only rules of 31). A reader must reconcile two documents that
  disagree about which rules are silent — precisely the "two reports
  mistaken for each other" failure `REPORTER_VERSION`'s bump discipline
  exists to prevent (`pcrecbench/CLAUDE.md`, [B14] R10).
- The sidecar corpus doubles, and §8(3) re-renders every committed sidecar
  on every catalogue or reporter bump. §11 Q5 deliberately capped that
  corpus at three at landing.
- MEASURED loss at subject grain: the `excluded` section carries **only**
  `pass_rate` rows — the [B13.2] P-2 `giveup_smallest` detail rows are
  set-grain only by construction (`report.py:4455`, `has_detail = grain ==
  "set" and hasattr(r, "failing_detail")`). So R-STATUS-12, whose only
  input is those rows, is structurally dead at subject grain too.

**Verdict: rejected as the primary mechanism.** It retains one genuine
merit — it needs no new grammar and no catalogue MAJOR — and it is worth
keeping as an ad-hoc human diagnostic (`interpret <name>.subject-grain.tsv`
run by hand when a reader wants the subject-level R-STATUS/R-FLOOR reading),
which costs nothing because the flag combination already works.

### §2.4 Option (d) — emit subject rows INTO the set-grain TSV

*Surfaced by this analysis, not in the brief.* The reporter already does
this once: [B13.2] P-2 emits, beside each `excluded` row, one extra
`excluded` row per give-up code carrying a **real subject id** in
`subject_or_na` and `metric=giveup_smallest` (`report.py:4471-4476`). The
design note calls this out as the sanctioned idiom: *"An extra metric row
is `render_tsv`'s existing extension idiom"* (`interpreter_v1.md:460`). The
same idiom could emit per-subject `median_ns` rows under `rank` at set
grain.

**Merits.** One file, one sha256, no stamp change, no second input, no
`--subject-grain` plumbing, no catalogue MAJOR; R-BUCKET-DOMINATED becomes
computable from the primary report; every existing selector keeps working
unchanged, because the added rows carry a real subject id where the
existing rows carry `(set)`.

**Why it is rejected: size, measured.** The set-grain TSV is the file every
reader opens, every fixture slices, and every `git diff` renders. Adding
the subject rows to it means adding M3's 202,794 `rank` rows to its 5,088 —
the same ×25 blow-up as (a), except paid in the file that must stay
readable rather than in a sibling a reader opens deliberately. On
`bench/syntax` the equivalent rendering is already 10.2 MB / ~108k lines
(`reports/CLAUDE.md:92`, `:190`), and `reports/CLAUDE.md` records that this
size "made" a regeneration problem of its own. A set-grain report should
stay about sets.

**Kept on the table as a narrow variant**: emit subject rows at set grain
*only for cells R-BUCKET-DOMINATED needs* (a dominated cell's own subjects).
That is a few dozen rows per report, it closes Q2 outright, and it does
nothing for predictions. Noted, not recommended.

### §2.5 Option (e) — a subject-grain SLICE, not the whole grain

*Surfaced by this analysis.* Commit a `.subject-grain.tsv` that carries
only the rows a second input is actually consulted for: the `record` rows,
and the ranking-family rows whose `metric` is `median_ns`, `pass_rate` or
`giveup_smallest` — dropping the five non-median `rank` metrics (`min_ns`,
`max_ns`, `stddev_ns`, `ratio_vs_baseline`, `ratio_vs_best`) and the
`compile` / `compile_stamp` sections, which are byte-identical to the
set-grain file's own and are already available there.

**MEASURED (M3 + a filter over it): 34,251 lines / 5,895,262 bytes
(5.62 MiB) — 16.6 % of the full subject-grain file, ×4.8 the set-grain TSV
rather than ×28.5.**

**What it can still answer.** All of §4's acceptance cases: every failing
clause selects `n_wrong` (a column present on `pass_rate`-metric rows) or
`median_ns`. R-BUCKET-DOMINATED's own declared `inputs` ask for exactly
`report:rank?metric=median_ns.{pattern,subject_or_na,regime_or_na,form,
testee,value}` (`rules.toml:1184`) — a strict subset of the slice.

**What it costs.** A SECOND rendering shape with its own contract. The
18-column TSV is deliberately one shape, and a slice is a shape a reader
must be told about. The mitigation is that the slice is a row FILTER, not a
column or format change — the header and all 18 columns are identical, so
`ReportTsv` reads it with no change at all, and the contract is one
sentence in the header comment.

**Recommendation: adopt (a) with (e)'s row filter**, i.e. the committed
file is the slice, and the full `--grain subject` render stays available
ad hoc for a human. §6 Q4.

### §2.6 Summary table

| option | fixes P3/P6/P7/P10? | fixes P2? | fixes P4? | new input | catalogue bump | committed bytes / group |
|---|---|---|---|---|---|---|
| (a) subject-grain TSV alone | no (a2: no route) | no | no | yes | none…MAJOR | 33.5 MiB (M3) |
| (b) selector extension alone | no (no data) | no | no | no | MAJOR | 0 |
| **(a)+(b)** | **yes (M2)** | **no** | half | yes | MAJOR | 33.5 MiB |
| (c) per-grain runs | no (R-PRED set-only) | no | no | no | none | 0 (+1 sidecar/group) |
| (d) subject rows in the set TSV | yes, with (b) | no | no | no | none | +32 MiB in the READ file |
| **(a)+(b) with (e)'s slice** | **yes (M2)** | **no** | half | yes | MAJOR | **5.6 MiB (measured)** |

P2 and the P4 testee glob are fixed by authoring/load-check changes
(§4), by no option on this table.

---

## §3. The KB-16 memory constraint

**The invariant, as it stands today.** `interpret` reads a report TSV and
`store/index.tsv` and nothing else — no markdown, no `bench/*/subbench.toml`,
no record JSONL, no engine (`pcrecbench/CLAUDE.md`, the [B13.3] section:
*"It reads the TSV and the index, and nothing else"*).
`make check-interpret` never loads the store either, and
`interpreter_v1.md` §8(2) pins its golden to a FROZEN index snapshot
(`catalogue/golden/index@2026-09-09.tsv`) for exactly this reason: so a
records-only commit can never fail it. KB-16 itself names the interpreter
as the consumer that must not acquire the cost
(`docs/dev/known_issues.md:625-627`).

**Every option in §2 preserves the invariant, without exception**, because
every one of them hands `interpret` a committed TSV. The cost lands on the
REPORTER, which already loads the store, at render time, once per report
group. **No proposal here argues to break the invariant, and the note
recommends that none ever should**: the reason KB-16's fix was worth
measuring is that the load is the expensive part, and the interpreter's
value is that it is cheap enough to run on every committed report.

**The cost, quantified.** KB-16's own committed AFTER measurement is
**116.78 s wall / 762,940 KB peak RSS** for a 6-record query over the
store's largest records (`docs/dev/known_issues.md`, the KB-16 table).
M3 measures the capability query at **100.75 s / 678,016 KB** — the same
order, on a 7-record query. So the subject-grain TSV costs **roughly one
KB-16-sized store load per report group**: ~100 s and ~680 MiB, on a box
that is not in a measurement window.

Two facts that bound how bad this is:

- **The store is already loaded three times per report group today** — once
  for the `.md`, once for the `.tsv`, once for the `.subject-grain.md`
  (`reports/CLAUDE.md:38` counts all three as separate committed
  renderings from the same query). A `.subject-grain.tsv` is a **fourth**
  load, a ~33 % increase on a cost the project already pays, not a new
  class of cost.
- **678 MiB peak is well inside the harness's memory heuristic.** The kills
  the boilerplate warns about were at ~3.6-3.8 GiB (KB-16's BEFORE row);
  the post-fix footprint is ~5× smaller, and M3 ran as a detached job
  without incident. The boilerplate's detached-run rule still applies to any
  store-loading run and this note does not propose relaxing it.

**The real mitigation, and why it is a follow-up and not a precondition.**
`report.main()` does one `load_all` and then one `build_report` at one
grain. `build_report` is grain-parameterised (`rd.grain`), so rendering
BOTH grains needs two `build_report` calls but **one** `load_all` — and the
load is the expensive part, not the reduction. A reporter change that emits
several renderings from one load would cut today's 3 loads per group to 1
and absorb the 4th for free. **UNMEASURED**: this lane did not measure the
`build_report`-only cost, so the claim "the load dominates" rests on
KB-16's own before/after (which changed only what is opened, not what is
rendered, and moved the wall clock ×6.55) rather than on a direct
measurement. It is a strong inference, not a number. §6 Q5 asks whether to
couple the two; the recommendation is **no** — coupling delays the fix that
unblocks predictions behind a reporter refactor nobody has scoped.

---

## §4. The acceptance cases: P2, P3, P4, P6, P7, P10

For each: the input and selector shape that makes it machine-evaluable.
The "matched" column is MEASURED (M2) against the real subject-grain TSV
M3 produced.

### P2 — **needs no new input.** Two authoring fixes and a load check.

Selector `pattern=…;regime_or_na=n/a;testee=libpcre2_*_jit-*`, quantity
`compile:median_total_ns`, reducer `ratio_to(libpcre2_*_interp-*)`.

- **Shape that works today:** drop the `regime_or_na=n/a` clause entirely.
  A `compile:` quantity already routes to the `compile` section without the
  selector naming anything (`interpret.py:1718-1720`), so the clause is
  redundant as well as wrong.
- **The prediction itself is TRUE.** The ledger read it by hand:
  `wild-waf-crs-942360-concat-sqli` compiles at 386,192 ns on `jit` against
  73,020 ns on `interp`, ratio 5.29 > 1 (ledger §3, P2 row). So this is
  purely an authoring defect over a correct prediction — the worst kind to
  leave undiagnosed.
- **Proposed load check (store-free):** a `compile:` quantity's selector
  MAY NOT name `subject_or_na` or `regime_or_na`. Enforced in
  `load_predictions` on the existing closed-set precedent
  (`interpret.py:1641-1646`), it converts a silent `not-evaluable` into a
  LOAD ERROR naming the reason — the §6.4 discipline
  `docs/dev/predictions/CLAUDE.md:44-49` already states for inexpressible
  clauses.
- Subject-grain matched: **0** (unchanged — grain-independent).

### P3 — **genuinely needs subject grain.**

Selector `pattern=codegrammar-flat;subject_or_na=t-1m;regime_or_na=
large-subject-throughput;testee=libpcre2_*_interp-*`, `median_ns`,
`ratio_to(wild-codegrammar-json-constant)`.

- **Shape that works:** the same selector, routed to the subject-grain
  input — `grain=subject` under option (b), with the file supplied under
  (a). Subject-grain matched: **6**.
- `ratio_to` joins the two populations on every key column the two
  selectors share (`interpret.py:1823-1827`), which at subject grain
  includes `subject_or_na` — so the ratio is computed subject-for-subject,
  which is what P3 means.
- **Cannot be restated at set grain.** `large-subject-throughput` on this
  set has three subjects (`t-1m`, `t-256k`, `t-64k`; the ledger's excluded
  table shows `n=3` for that regime) and the report header's
  `single_subject_regimes:` is EMPTY (MEASURED on both grain renderings).
  A set-grain cell is their sum; restating the clause there would change
  the claim.

### P4 — **(a) needs an authoring fix only; (b) needs both.**

- **P4.a** (`compile:artifact_bytes`, `testee=pcrec_*-auto-*`): repair the
  glob to `pcrec_*_auto-*`. Compile rows are grain-independent; **no new
  input**. Subject-grain matched: 0 (unchanged).
- **P4.b** (`median_ns`, `subject_or_na=lp-atomic-nonmatch` + the same
  glob): needs the glob repair AND the subject-grain route. Subject-grain
  matched: 0, because the glob still fails — this is the one clause where
  a reader could wrongly conclude from M2 that subject grain "did not
  help".
- **Proposed load check (store-free):** every `testee=` glob in a
  predictions file must match at least one testee id in `store/index.tsv`
  for that prediction's own `(subbench, version)` — the same file
  `interpret` already reads, 169 lines, never the store. It must be
  VACUOUS when that population has never been measured, exactly as
  `check_stated_utc` already is (`interpret.py:1679-1681`), so a prediction
  may still anticipate a testee that does not exist yet.

### P6 — **(a) restatable at set grain with a stated loss; (b) is not, at any grain.**

Both clauses are `n_wrong eq 0` on `v-uuid-badnibble`. Subject-grain
matched: **18 each**.

- **P6.a** (`uuid-near-miss` correctly REJECTS the bad-nibble UUID): at set
  grain, `n_wrong eq 0` on the whole `short-subject-search` cell is
  strictly STRONGER than on one subject — if the set is clean, that subject
  is. So P6.a is checkable today as a weaker-but-sound claim. Subject grain
  gives the precise one.
- **P6.b is a trap worth naming.** Its note says the grok import "still
  HITS the same subject — the pair diverges as designed". That is an
  **answer** claim, and `interpreter_v1.md` §6.4 / `docs/dev/predictions/
  CLAUDE.md:40-49` say the report TSV carries no answer, span or capture at
  ANY grain. The clause as written (`n_wrong eq 0`) does not say the pair
  diverged; it says both answered as the oracle said. **Subject grain
  rescues the clause that was written, not the claim the note describes.**
  The honest transcription of P6's real content is two clauses —
  `n_wrong eq 0` on each arm — plus a stated note that the divergence
  itself is inexpressible, or a new reporter column that carries it (out of
  scope here, and `interpreter_v1.md:483` already tracks the adjacent
  `expectation_detail` idea on §2.5's own follow-up list).

### P7 — **restatable at set grain with a loss; subject grain gives the pair.**

`n_wrong eq 0` on `v-ipv4|v-ipv4-oor` across two patterns. Subject-grain
matched: **24**. Same shape as P6.a: the set-grain form is sound and
weaker. The "IDENTICAL answers" half of P7's note is, again, an answer
claim (§6.4), inexpressible at either grain.

### P10 — **restatable at set grain with a loss; subject grain gives the contrast.**

`n_wrong eq 0` on `nu-lead-no-cont` (P10.a) and `nu-lead-with-cont`
(P10.b). Subject-grain matched: **18 each**. The pair's POINT is that the
pattern hits one subject and not the other — and since both are oracled,
`n_wrong eq 0` on each is the correct machine form of that at subject
grain, and is exactly what subject grain delivers. **P10 is the cleanest
win of the six**: unlike P6/P7 there is no residual answer claim; the
oracle already encodes the designed contrast.

### §4.1 Scoreboard

| prediction | needs a subject-grain input | needs an authoring fix | evaluable after (a)+(b) alone |
|---|---|---|---|
| P2 | no | **yes** (drop `regime_or_na=n/a`) | **no** |
| P3 | **yes** | no | **yes** |
| P4.a | no | **yes** (`pcrec_*_auto-*`) | **no** |
| P4.b | **yes** | **yes** (same glob) | **no** |
| P6.a | preferable | no | **yes** |
| P6.b | preferable | the claim is §6.4-inexpressible | yes, as written |
| P7 | preferable | as P6.b for the "identical" half | **yes** |
| P10.a/b | **yes** | no | **yes** |

Four parents evaluable from the input change alone; two need the authoring
fixes §4 specifies; two of the eight clause notes describe claims that are
inexpressible at any grain and should say so in the file.

---

## §5. The P5 rank-blindness lesson

### §5.1 What happened

P5.a's selector names no `section`, so `_select` defaults to `rank`
(`interpret.py:1723-1724`). The quantity is `n_wrong`, the op is `eq 0`.
The sidecar reports **confirmed** over 198 values. The ledger read the same
cells by hand and scored P5 **REFUTED** on `evil-alt-nested`: 10 of 75
wrong on `dfa-nocaps` and `auto-nocaps`, give-ups on `interp`/`jit`,
timeouts on the three captures-requiring pcrec arms — every one of them on
`short-subject-search`, exactly P5's regime (ledger §3 P5 row, §1.2
Finding C).

### §5.2 The measurement that settles it (M4)

A cell with `n_wrong > 0` is moved to the `excluded` section by
`build_report` before the TSV is written (`report.py:4421-4422`: a cell is
`excluded` when `r.expectation_failing or not n_timed`). So the question is
whether a `rank` row can carry a non-zero failure count at all.

**Scanned: all 43 committed `reports/*.tsv`, 92,892 `rank` rows.**

> **`rank` rows with `n_wrong > 0` or `n_gave_up > 0`: ZERO.**
>
> `excluded` base rows (`metric=pass_rate`): 111, of which **33 carry
> `n_wrong > 0`.**

So `n_wrong eq 0` — or `n_gave_up eq 0`, or `pass_rate eq 1` — evaluated
over the default `rank` section **is a tautology across the entire
committed corpus**. It cannot fail. The population such a prediction exists
to check is the 33 rows it is structurally forbidden from seeing.

(Caveat, stated because the panel should not over-read M4: the `excluded`
predicate is `expectation_failing or not n_timed`, **not** `pass_rate < 1`
— `interpreter_v1.md:352-358` makes this point and this note repeats it.
M4 shows the two coincide on today's corpus in the direction that matters
(no rank row carries a failure count); it does not prove the reporter could
not emit one under some future shape. The recommendation below does not
depend on the stronger claim.)

### §5.3 Should `section=` be MANDATORY for failure-population predictions?

**FOR:**

1. M4. The default silently makes a whole class of prediction unfalsifiable,
   corpus-wide, and no author can be expected to know that from
   `docs/dev/predictions/CLAUDE.md`, which does not mention the default at
   all.
2. The failure mode is a **false CONFIRM**, not a refusal. R-PRED-3's
   `not-evaluable` is honest and visible; R-PRED-1's "confirmed" is
   actively misleading, and it is the one verdict a reader will not
   double-check. The project's whole instrument discipline runs the other
   way — X13's explicit rule versioning, KB-8's query-filtered count, and
   pcrec I-5's own rule *"read the value, never the absence"*
   (`pcrecbench/CLAUDE.md`, [B16] R1).
3. The cost is one token per row, paid at authoring time by the person
   stating the prediction — the same person `docs/dev/predictions/
   CLAUDE.md:66-73` already makes responsible for writing it by hand before
   the run.
4. Precedent: `quantity`, `op` and `reducer` are closed sets whose
   violation is a named load error, never a silent skip
   (`interpret.py:1641-1654`). `section` is the one field in the row where
   an *unstated* choice silently decides the answer.
5. It is cheaply checkable at load: "quantity ∈ {`n_wrong`, `n_gave_up`,
   `pass_rate`, `status`} ⇒ the selector must name `section`" is a
   two-line predicate over an already-parsed row, deterministic, store-free
   and fixture-able.

**AGAINST:**

1. **It is a migration with teeth.** 9 of the 15 clause rows in
   `capability-0.1-first.tsv` use `n_wrong`, and `syntax-0.1-first.tsv`'s
   35 rows would need the same audit. Every touched row moves a committed
   golden and every affected sidecar — a catalogue MAJOR plus regeneration
   under §3.3 and §8(3).
2. **It buys compliance, not correctness.** A prediction that writes
   `section=rank` explicitly is exactly as blind as one that omits it — and
   now carries a token that LOOKS deliberate, which is worse for a reviewer
   than a visible omission. The real content of P5 is "no cell of this
   family is wrong ANYWHERE", which needs `section=rank|excluded`, and
   nothing about mandating the field makes an author write that instead of
   the narrower thing.
3. It addresses the symptom in exactly one place. The identical blindness
   sits in `_elsewhere` (§1.4), which is silent for the same structural
   reason, and no amount of mandating fixes that.

**Two alternatives the analysis surfaces, which the mandate does not
consider:**

**(α) Make the DEFAULT honest instead of mandatory.** For a
failure-population quantity (`n_wrong`, `n_gave_up`, `pass_rate`,
`status`), have `_select`'s default read `rank` **and** `excluded` rather
than `rank` alone. Mechanically sound: `excluded` base rows carry
`n_wrong`, `n_gave_up` and `pass_rate` in their own columns
(`report.py:4457-4460`), so `_value_of` reads them without change; and for
a `median_ns`-class quantity the excluded rows carry `metric=pass_rate`, so
`_value_of` returns `None` and the existing "the selected rows carry no …"
path handles it — meaning the change can be scoped to the four quantities
where the default was the bug, and is a no-op everywhere else. Under (α),
P5.a refutes on `evil-alt-nested` — the verdict the ledger reached by hand.
Costs: a catalogue MAJOR (a rule reads a different section), and it changes
the verdict of already-committed prediction files without those files
changing. That second cost cuts both ways — it FIXES them — and §3.3's
MAJOR-bump contract ("a sidecar stamped at an earlier MAJOR is no longer
derivable from its inputs under the current catalogue") is the precise,
honest label for it.

**(β) Make the tool say what it looked at.** `_elsewhere` already computes
the non-ranked population for a selector (`interpret.py:1737-1742`) but is
consulted ONLY when the primary selection is empty. Extend it: whenever a
prediction is confirmed on `rank` AND the same selector (minus `section`)
matches rows in `_ELSEWHERE`, annotate the verdict — *"confirmed on 198
`rank` rows; 50 rows of the same selector are in the `excluded` section"*.
That is exactly the sentence that would have made the ledger's manual catch
unnecessary. Additive, flips no verdict, needs no authoring migration.
Note that (β) is blinded by the grain gap today for a subject-scoped
selector (§1.4), so it wants (a) to be fully useful — but it works today for
every pattern-scoped selector, which is all six of the affected ones here.

### §5.4 Recommendation

> **Adopt (α) and (β). Do NOT mandate `section=`.**

Reasoning: (α) makes the default correct for precisely the quantities where
the default was the bug, with a scoped, mechanically-verified change and no
authoring migration. (β) makes the instrument state its own population,
which is the durable fix and catches the whole class — including the cases
where an author dutifully writes `section=rank` and is wrong anyway.
Mandating a token asks every author to remember a rule the tool can enforce
by reading the quantity it was already handed, and (AGAINST 2) buys ritual
compliance at the price of a corpus-wide migration.

`section=` should stay AVAILABLE, and `docs/dev/predictions/CLAUDE.md`
should state the default explicitly and RECOMMEND naming `section` whenever
a narrower population is meant deliberately. Documenting the default is
non-negotiable either way: it is currently stated in no file an author
reads.

---

## §6. Questions for Frank / rulings needed

> **ALL ELEVEN RULED (Frank, live, 2026-09-17, twenty-fourth session —
> one question at a time, recorded by the manager):** every
> recommendation below is RATIFIED as stated. Q1 (a)+(b) as one ruling;
> Q2 the `grain=subject` selector key; Q3 MAJOR, catalogue 2.0; Q4 the
> slice (with Frank's growth concern noted — it feeds Q9 and the
> data-management white paper chartered the same session); Q5 not
> coupled, the reporter refactor a follow-up with its own measurement
> first; Q6 both load checks, under Frank's stated general posture
> "fail loudly generally"; Q7 (α)+(β) — and a WIDER DIRECTIVE beyond
> this note: audit the other predicates/queries for the same class of
> structurally-incomplete answer, and make results carry the context
> around their numbers, especially where a Claude session is the
> consumer (chartered as its own follow-up lane); Q8 goldens stay at
> set grain, subject-grain coverage as new fixtures; Q9 new samples
> plus on demand, no back-fill; Q10 the stamp gap fixed now,
> unconditionally; Q11 rulings fold into `interpreter_v1.md`, this
> file stays the derivation record. The text below is kept as the
> pre-ruling record.

Each with this lane's recommendation. None of these is decided here.

**Q1. Adopt (a)+(b) — commit a subject-grain TSV per report group AND give
the prediction selector a route to it?**
*Recommend: YES, as one ruling.* They are halves of one mechanism (§2.2);
either alone changes nothing. The mechanism is already half-built (§2.0),
and M2 proves it makes four of the six not-evaluable predictions evaluable.

**Q2. Which routing spelling — a sixth selector key `grain=subject`, or a
`subject:` quantity prefix mirroring `compile:`?**
*Recommend: the selector key.* `compile:` already conflates WHAT is
measured with WHICH section is read, and P2 is direct measured evidence
that a competent author misread that conflation (§4, P2). A key that says
where to look, beside the five keys that say which rows, adds no second
meaning to `quantity`.

**Q3. Is a rule reading a second declared FILE a catalogue MAJOR?**
*Recommend: YES, MAJOR (2.0).* §3.3 makes MAJOR the bar for "`inputs`
change in a way that reads a different column"; a different file is at
least that. The regeneration it forces is **four** committed sidecars today
(MEASURED: `ls reports/*.interpretation.md` → 4 — §11 Q5's three acceptance
sidecars plus capability's), which is cheap, and the honest label matters
more than the cheapness.

**Q4. Full subject-grain render, or (e)'s row slice?**
*Recommend: the SLICE.* MEASURED: 5.62 MiB against 33.5 MiB per group, a
strict superset of everything §4 and R-BUCKET-DOMINATED need, read by
`ReportTsv` with no code change because the header and all 18 columns are
unchanged. The full `--grain subject --format tsv` render stays available
ad hoc.

**Q5. Couple this to a reporter change that renders several grains from one
`load_all`?**
*Recommend: NO — file it as a follow-up.* The 4th store load is ~100 s /
678 MiB (M3), a ~33 % increase on a cost already paid three times per group
(§3). Coupling delays the fix that unblocks predictions behind a reporter
refactor nobody has scoped. UNMEASURED and flagged as such: that a
one-load-many-renders change would actually save ~3× rests on inference
from KB-16's before/after, not on a direct `build_report`-only measurement.

**Q6. Add the two store-free load-time checks to `load_predictions`?**
(i) a `compile:` quantity's selector may not name `subject_or_na` or
`regime_or_na`; (ii) every `testee=` glob must match ≥1 index testee for
its own measured `(subbench, version)`, vacuous when that population is
unmeasured.
*Recommend: YES, both.* They are exactly the P2 and P4.a defects turned
into named LOAD ERRORS, on the discipline `docs/dev/predictions/CLAUDE.md`
already states, and neither reads the store. Together they close Causes B
and C (§1.2) at authoring time rather than at reading time.

**Q7. The P5 rank-blindness ruling — mandate `section=`, change the default
for failure quantities (α), or annotate the elsewhere-population (β)?**
*Recommend: (α) + (β), not the mandate.* Full argument at §5.3-§5.4.

**Q8. Do the three §10 acceptance goldens get a subject-grain input?**
*Recommend: NO.* Keep the acceptance set at set grain so §10's 25/25 and
the frozen-index contract are untouched; add subject-grain coverage as new
fixtures instead (which also gives R-BUCKET-DOMINATED its first firing
fixture — §2.0).

**Q9. Back-fill: all 43 report groups get a `.subject-grain.tsv`, or new
samples only?**
*Recommend: new samples plus on demand* — §11 Q5's own precedent for
sidecars, for the same reason (the cost that matters is review weight, not
CPU), and at 5.62 MiB × 43 a full back-fill is ~240 MiB of committed TSV
for reports nobody is re-reading.

**Q10. Fix the `--subject-grain` stamp gap now, independently of every
ruling above?**
*Recommend: YES, unconditionally.* `build_stamp` does not record the
subject-grain input and `check_interpret.py`'s freshness re-render does not
pass it (§2.0 a3), so a sidecar rendered with the flag fails `make
check-interpret` section 3 on an unmodified file. That is broken today; it
is unexposed only because no sidecar uses the flag, and every option in §2
exposes it.

**Q11. Where does this note land — folded into `interpreter_v1.md` as v1.4,
or kept separate?**
*Recommend: fold the RULINGS into `interpreter_v1.md`* (a new §6.7 for the
selector route, an amendment to §11 Q2, which explicitly rules
`input-absent` "until a separate reporter change commits
`<name>.subject-grain.tsv`" — this note is that change), and keep THIS file
as the derivation record. Precedent: `gate_shape_v14.md` stayed a separate
SPEC beside `record_schema.md`.

---

## §7. What this note deliberately does not decide

- The reporter's flag spelling for emitting the slice, and whether it is a
  new `--grain subject-slice` or a filter applied to `--grain subject`.
- Whether `docs/dev/predictions/capability-0.1-first.tsv` is REPAIRED in
  place or re-transcribed as a `-second` set. A prediction is stated before
  a run and `check_stated_utc` (`interpret.py:1662-1687`) enforces that
  against the index; editing a committed prediction file after its
  population was measured is a question about the prediction discipline,
  not about grain, and belongs to whoever owns the next capability sample.
- P9's absence from the machine-readable file (ledger §3, P9 row) — a
  transcription gap, tracked in the ledger's own checklist item 3.
- Any change to `report.py`'s markdown rendering. Everything here is TSV.

---

## Source header

Derived from committed artefacts at `HEAD` = `bf809b1`, plus four
read-only probes run in this lane (§0). Code citations are
`pcrecbench/interpret.py`, `pcrecbench/report.py`,
`catalogue/rules.toml`, `catalogue/fixtures/fixtures.toml`,
`catalogue/check_interpret.py` as committed at that revision. Document
citations are `docs/design/interpreter_v1.md` (v1.3),
`docs/dev/predictions/CLAUDE.md`, `docs/dev/known_issues.md` (KB-16),
`reports/CLAUDE.md`, `pcrecbench/CLAUDE.md` and
`docs/dev/ledgers/2026-09-17-capability-0.1-first-a770139e.md`. The
subject-grain TSV measured in M2/M3 was rendered to the session scratchpad
and is NOT committed; it is reproducible byte-for-byte from the report's
own committed query with `--grain subject --format tsv`. No file under
`store/`, `reports/` or `~/pcrec` was modified by this lane.
