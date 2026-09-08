# The interpreter — design note v1 ([B13])

STATUS: **DESIGN ONLY.** No code exists. This note is what the
adversarial critic panel attacks (docs/design/CLAUDE.md's own rule for a
design of this size; docs/dev/reviews/ R1-R3 are the precedent). Nothing
here is built until the panel has run and its findings are dispositioned.

Author: lane `b13design`, 2026-09-07. Charter: docs/dev/plan.md row
`[B13]`, agreed by Frank 2026-08-25 (docs/dev/dev_journal.md, second
session parts 5 and 7). Stated inputs:
`docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` and
`-repin-v2.md` — the pcrec manager session's two readings of the same
report, which are the only existing worked examples of a human doing by
hand exactly what this tool must do by rule.

---

## §0. The problem, in one paragraph

A committed report under `reports/` is a deterministic, diffable table.
Reading one takes a manager session hours and produces a ledger under
`docs/dev/ledgers/` — 1,085 lines for bench/syntax@0.1's first sample.
Most of that work is *judgment* and belongs to a person. But a
measurable fraction of it is not judgment at all: it is a fixed set of
questions asked of a fixed set of columns ("which records were not
`measured`?", "which cross-pin Δ is outside spread?", "which cell moved
across the reference arm?", "which stated prediction did this refute?").
Those questions are asked by hand today, which means they are sometimes
not asked at all. `[B13]` mechanises exactly that fraction and nothing
more, and it is designed so that it *cannot* creep past it.

Frank's constraint, verbatim from the plan row: **"no opinions, all
based on facts."** The design's whole architecture follows from taking
that literally rather than as an aspiration — see §7.

---

## §1. Scope, and the two parts

**Part 1 — `pcrecbench interpret`**, a deterministic fact-finder. Reads
the report **TSV** and `store/index.tsv` (never the markdown — the
markdown is a rendering of the TSV, and parsing a rendering is how a
reader ends up depending on a legend's wording). Emits the FIRED rules
with their rows, numbers and record ids, and the rules that did NOT fire
with the reason each did not. Gated by `make check-interpret`.

**Part 2 — the project skill `/pcrec-bench-interpret <report>`**, which
runs the renderer and commits a sidecar
`reports/<name>.interpretation.md`, stamped with the report's sha256 and
the catalogue version. Never a section inside the report: the reporter
stays deterministic and diffable, and its version bumps for its own
reasons (`REPORTER_VERSION`, report.py:896).

### §1.1 What is deliberately OUT of scope in v1

- **Per-set outlier bands.** `bench/syntax/NOTES.md`'s R2 (worse than ×2
  or better than ×20 against the JIT), R4 (family median ×3), R7 (a
  non-flat sweep outside [0.7, 1.4]) are *stated before a run by the set's
  author, about that set*. They are the reading lane's rules, not the
  catalogue's: a band is a judgement about what is interesting in one
  corpus, and importing it would make the interpreter opine. The
  catalogue carries only rules whose threshold is either (a) already
  computed by `report.py` and printed in the TSV, or (b) a measured
  quantity in the same report compared against itself.
  **If a later ruling wants set-local bands, they belong in the set's
  own sidecar (`subbench.toml`), read by `interpret` as data — not in
  the catalogue.** Named as open question Q3 (§11).
- **Causes.** The interpreter never says *why* a number moved. Where a
  cause is already recorded somewhere (outbox `O-n`, `known_issues.md`
  `KB-n`, `upstream_findings.md` `Un`), the rule may carry a LINK to it;
  it may not generate one.
- **Rankings of importance.** No rule sorts findings by how interesting
  they are. Output order is the catalogue's declaration order, which is
  stable and therefore diffable.

---

## §2. Inputs, exactly

### §2.1 The report TSV

Produced by `report.render_tsv` (report.py:4065). Two parts:

**A header comment line**, `# k: v; k: v; …` (report.py:4068-4091). The
keys `interpret` reads, by name:

| key | used by |
|---|---|
| `reporter` | the stamp; a catalogue rule may declare a minimum reporter version |
| `filters` | echoed into the sidecar; the query that made this population |
| `source` | carries `(N record(s) matching this query)` — the candidate count (KB-8) |
| `records` | the included count |
| `excluded_invalid`, `superseded`, `newer_not_measured` | R-STATUS-5 |
| `subbench_versions`, `machines`, `schema_versions` | R-STATUS-6 (a mixed-schema population) |
| `grain` | rules declare which grain they apply to; a set-grain-only rule does not fire on a subject-grain TSV and says so |
| `x13_rules`, `mixed_x13` | R-STATUS-7 |
| `worst_other_core_busy` | R-STATUS-8 |

**Data rows**, an 18-column table (report.py:4092-4094):

```
section  pattern  subject_or_na  regime_or_na  form  fact  testee  status
tier  rank_or_na  metric  value  n  pass_rate  n_gave_up  n_wrong
gave_up_summary  delta_verdict
```

`section` ∈ `record | rank | excluded | not_ranked | scratch |
did_not_compile | compile | compile_stamp`.

Two shapes matter and are easy to get wrong:

- a `record` row carries the RECORD ID in the `testee` column, the
  agreement string in `gave_up_summary`'s slot, and the after-sample
  failure in `delta_verdict`'s (report.py:4100-4107);
- a `rank` row is emitted SIX TIMES per (group, testee, form), once per
  `metric` ∈ `median_ns | min_ns | max_ns | stddev_ns |
  ratio_vs_baseline | ratio_vs_best` (report.py:4146-4153). Every rule
  below states which metric row it reads.

### §2.2 `store/index.tsv`

Eight columns (`store/index.tsv` line 1):
`path  subbench  version  testee_id  machine_id  timestamp  status  rows`.

**The join key between the two files** is the record id: a `record`
row's `testee` column is the basename of `path` without `.jsonl`. This
is the only join, and it is exact.

The index exists in the input set for one reason: **the report cannot
show what its own query excluded.** No committed report under
`reports/` today contains a single `not_ranked` row, because every
committed query names its roster and its window and therefore never
draws a non-`measured` record at all. Nine `inconclusive-load` records
and one `inconclusive-spread` record sit in `store/index.tsv` and appear
in no report. That absence is precisely what R-STATUS-2 exists to state.

### §2.3 The predictions file (optional third input)

See §6. Absent → every R-PRED rule reports `did-not-fire: input absent`.

### §2.4 What `interpret` does NOT read

The markdown renders, `bench/*/expectations.tsv`, any record JSONL, any
engine, any pcrec source. The reporter already made the reduction; a
second reduction here would be a second implementation of arithmetic
this project keeps in exactly one place (`pcrecbench/reduce.py`'s own
header states the rule).

---

## §3. The rule catalogue: file, format, versioning

### §3.1 Where it lives

```
catalogue/
  rules.toml        the catalogue
  CLAUDE.md         purpose + files (this project's convention)
  fixtures/         one directory per rule, the sabotaged inputs (§8)
```

At the repository ROOT, beside `schema/`, deliberately: the catalogue is
a *format* with a version, a validator and a fixture corpus, the same
shape as `schema/`, and it is read by two consumers (`interpret` and
`make check-interpret`). Putting it under `pcrecbench/` would make it
look like implementation detail of one module.

TOML because BD4 fixes python ≥ 3.11 and `tomllib` is stdlib; the
project already reads TOML in three places (`subbench.toml`,
`testees/*/configs.toml`, `pyproject.toml`), and multi-line strings make
a threshold's SOURCE citable inline instead of in a comment.

### §3.2 The shape of a rule

```toml
catalogue_version = "1.0"
# Every bump regenerates every committed sidecar in the same commit.

[[rule]]
id            = "R-DELTA-1"
title         = "cross-pin Δ outside spread"
class         = "delta"
since         = "1.0"
grain         = ["set"]              # which TSV grains it applies to
inputs        = [                    # EXACT columns, checked at load
  "report:rank.delta_verdict",
  "report:rank.metric=median_ns.value",
  "report:rank.testee",
]
predicate     = "delta_verdict matches '^(faster|slower) ×'"
threshold     = "none of this rule's own"
threshold_src = """
report.py:2234 `_cross_pin_verdict` ([B9] R8): `unchanged (within
spread)` iff |median_new - median_old| <= 2 * max(stddev_old,
stddev_new); otherwise faster/slower ×N.NN. This rule adds NO threshold
of its own -- it reads the verdict string the reporter already computed
and printed, so the interpreter and the report can never disagree about
what "beyond spread" means.
"""
slots         = ["pattern", "regime", "form", "testee", "verdict", "median_ns"]
template      = "{pattern} / {regime} / {form} / `{testee}`: the reporter's cross-pin Δ reads **{verdict}** (median {median_ns} ns)."
links         = []                   # see §7.3
example       = """
reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv,
factored / short-subject-search / plain / pcrec_692c2e8_vm-caps-simdna,
rank 5: median 69,537.5 ns, delta_verdict `faster ×1.19`.
"""
```

`predicate` is PROSE, for the reader. The executable predicate is a
python function in `pcrecbench/interpret.py` named exactly `id` with
`-` → `_` lowercased (`r_delta_1`). The catalogue is not a rule
*engine* — a DSL would be a second language to get wrong. The catalogue
is the **contract** the code is checked against: `make check-interpret`
asserts that every `[[rule]]` has a function, every function has a
`[[rule]]`, and that every function's declared `inputs` are the only
columns it touches (enforced by handing each rule function a row view
that raises on an undeclared column — see §7.2).

### §3.3 Versioning, and what a bump means for old sidecars

`catalogue_version` is `MAJOR.MINOR`, the same discipline as the record
schema (docs/design/record_schema.md §4) and for the same reason.

- **MINOR** — a rule added; a template's wording changed; a link added;
  an `example` refreshed. Old inputs still produce the same *facts*;
  only the rendering moves.
- **MAJOR** — a rule's PREDICATE or THRESHOLD changes, a rule is
  removed, or `inputs` change in a way that reads a different column.
  A sidecar stamped at an earlier MAJOR is no longer derivable from its
  inputs under the current catalogue.

A retired rule keeps its `[[rule]]` block with `retired_in = "2.0"` and
its `id` is never reused — the record schema's own reserved-id
discipline, and the reason a sidecar from 2026-09 can still be read in
2027.

**The bump rule that makes this safe:** a committed sidecar is
*generated*, and `make check-interpret` re-renders every committed
`reports/*.interpretation.md` from its recorded inputs and requires byte
equality. So a catalogue bump that changes any rendering forces
regeneration of every affected sidecar **in the same commit**. This is
exactly the precedent `REPORTER_VERSION` set (pcrecbench/CLAUDE.md, [B14]
R10: "bump whenever rendering changes, so two reports are never mistaken
for each other"), applied one layer up. A stale sidecar is a `make
check` failure, not a thing a reader has to notice.

---

## §4. The rules

Six classes, matching the plan row's six named kinds. Every threshold
below is either (a) a value `report.py` or `reduce.py` already computed
and printed, read as a string, or (b) a comparison of two measured
numbers *from the same report*. There is no tuned constant introduced by
this design. Where a boundary is definitional (`≥ 1.0`, "crosses 1.0")
it is named as definitional, not measured, and said so out loud.

### §4.1 Class R-STATUS — status caveats

| id | fires on |
|---|---|
| R-STATUS-1 | an included record whose `status` ≠ `measured` |
| R-STATUS-2 | a record in `store/index.tsv` for this report's (subbench, version, machine) that the query did NOT include, whose status ≠ `measured` |
| R-STATUS-3 | an `excluded` section row (a cell with `pass_rate` < 1) |
| R-STATUS-4 | a `did_not_compile` section row |
| R-STATUS-5 | header `superseded` / `newer_not_measured` / `excluded_invalid` > 0 |
| R-STATUS-6 | header `schema_versions` names more than one version |
| R-STATUS-7 | header `mixed_x13: True` |
| R-STATUS-8 | header `worst_other_core_busy` present and non-`n/a` |
| R-STATUS-9 | a `record` row whose agreement string starts `disagree` or `n/a` |
| R-STATUS-10 | a `record` row whose `delta_verdict` slot carries `after: …` |
| R-STATUS-11 | a `scratch` section row |
| R-STATUS-12 | one subject giving up under DIFFERENT codes on two patterns, one testee, one regime |

R-STATUS-12 is the second of the two interpreter rule facts the journal
names (dev_journal.md, second session part 7; `feedback_…-repin-v2.md`
§2's last bullet): *"the same 1 MB subject gives STEPS (−2) on
factored-VM and WORK (−4) on orig-VM — different budgets bind on the two
spellings."* Inputs: `report:excluded.{pattern,regime_or_na,form,testee,
gave_up_summary}`; the subject id and its size are parsed out of the
`(smallest: <id>, <n> B)` clause `_gave_up_cell_summary` renders ([B9]
R7) — the one place a rule reads a formatted string rather than a
column, and named as such (open question Q8, §11).

**Inputs.** R-STATUS-1: `report:record.testee` joined to
`index:status`. R-STATUS-2: `index:{subbench,version,machine_id,status,
testee_id,timestamp}` minus the report's `record` rows. R-STATUS-3:
`report:excluded.{pattern,regime_or_na,form,testee,pass_rate,n_gave_up,
n_wrong,gave_up_summary}`. R-STATUS-4:
`report:did_not_compile.{pattern,testee,gave_up_summary}` (the
diagnostic lives in `gave_up_summary` — report.py:4172). R-STATUS-9/10:
`report:record.{testee,value,delta_verdict}`.

**Thresholds and their sources.** None of R-STATUS-1..8, 10, 11 has a
threshold: each reads a recorded status token or a header integer.
R-STATUS-9 reads `reduce.agreement_line`'s output (reduce.py:351), whose
constants are `k = 1.5, d_min = 2, share_c = 3, N ≥ 5 and odd`
(reduce.py:246-250) — **measured over the store's 68 records at [B20]**,
census files under `docs/dev/measurements/`. The interpreter re-derives
nothing.

**Templates** (one per rule; slots in braces):

```
R-STATUS-1  "`{record_id}` (testee `{testee}`) is included with status
             **{status}**."
R-STATUS-2  "`{record_id}` (testee `{testee}`, {timestamp}) is in
             store/index.tsv for {subbench}@{version} on {machine} with
             status **{status}** and is NOT in this report's
             population."
R-STATUS-3  "{pattern} / {regime} / {form} / `{testee}` is EXCLUDED
             from ranking: pass-rate {pass_rate}, {n_wrong} wrong
             answer(s), {n_gave_up} give-up trial(s){give_up_clause}."
R-STATUS-12 "Subject `{subject}` ({subject_bytes} B) gives up as
             **{code_a}** on {pattern_a} and **{code_b}** on
             {pattern_b}, on `{testee}` in {regime}: a different budget
             binds on the two spellings."
R-STATUS-4  "{pattern} / `{testee}`: did-not-compile — {diagnostic}"
R-STATUS-5  "The query drew {candidates} candidate record(s) and
             included {included}; {superseded} superseded,
             {newer_not_measured} newer-but-not-measured,
             {excluded_invalid} invalid."
R-STATUS-9  "`{record_id}`: trial agreement reads {agreement}."
R-STATUS-10 "`{record_id}`: the after-sample failed — {after}. (After
             samples are PROVENANCE, not a verdict: schema v1.4,
             docs/design/gate_shape_v14.md.)"
```

**Worked example — R-STATUS-2**, against
`reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`.
The report's header reads `source: store/index.tsv (14 record(s)
matching this query); records: 9; superseded: 5`. `store/index.tsv`
carries 14 rows for `email-specimen@0.1` on `budu-ryzen1600`, of which
**three are `inconclusive-load`**:
`libpcre2_10.46_interp-caps-simdna` @ 2026-08-25T17:34:02Z,
`pcrec_692c2e8_auto-caps-simdna` @ 17:51:31Z,
`pcrec_692c2e8_auto-nocaps-simdna` @ 17:55:34Z. None of the three
appears anywhere in the report — each was superseded by a `measured`
record of the same testee at 22:1x-22:2x under [B9] R2's
newest-measured rule. R-STATUS-2 fires three times and names them; a
reader who wants to know whether the re-measure changed anything now has
the record ids to compare, which is exactly the question
`feedback_pcrecdev1_2026-08-25-repin-v2.md` §3 had to answer by hand.

**Worked example — R-STATUS-4**, against
`reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`: 172
`did_not_compile` rows, e.g.
`pcrec_d34c9131_auto-caps-simdna | pcrec: module 'conditionals' is
enabled but (?(...) is not implemented yet (pattern offset 8)`. The rule
fires once per (pattern, testee) pair, deduplicated across the ranking
groups the reporter repeats them in ([B12] R10 emits one row per group).

### §4.2 Class R-DELTA — cross-pin deltas beyond spread

| id | fires on `delta_verdict` matching |
|---|---|
| R-DELTA-1 | `^(faster\|slower) ×` |
| R-DELTA-2 | `^selection changed \(` |
| R-DELTA-3 | `^now measured \(was: ` |
| R-DELTA-4 | a R-DELTA-1 firing with NO prediction covering the cell (§6) |

**Inputs.** `report:rank.{pattern,regime_or_na,form,testee,rank_or_na,
delta_verdict}` plus the same row's `metric=median_ns.value`. Set grain
only (`delta_verdict` is computed for `grain == "set"` alone,
report.py:4143-4145) — on a subject-grain TSV all four report
`did-not-fire: grain`.

**Threshold and source.** *None of its own.* R-DELTA-1's boundary is
`_cross_pin_verdict`'s (report.py:2234-2248): unchanged iff the median
difference is within `2 × max(stddev_old, stddev_new)`. The interpreter
reads the string. This is the single most important design decision in
the note: **the interpreter must never be able to disagree with the
report about whether something moved.**

R-DELTA-2's source is [B16] R4 (`_cross_pin_info`, report.py:2447): when
the two pins compiled different ENGINES the reporter refuses a ratio and
prints the selection change instead. R-DELTA-2 therefore fires *instead
of* R-DELTA-1 on the same cell, never beside it — a property the fixture
in §8 pins.

**Worked example — R-DELTA-1**, the case the charter was written from.
In `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`:

- `factored` / short-subject-search / plain / `pcrec_692c2e8_vm-caps-simdna`,
  rank 5, median 69,537.5 ns, `faster ×1.19`;
- `orig` / match-compliance / whole-subject / `pcrec_692c2e8_vm-caps-simdna`,
  rank 2, median 80,227.6 ns, `faster ×1.26`.

Those are the two numbers `feedback_pcrecdev1_2026-08-25-repin-v2.md`
§2 calls "a cross-pin VM speedup with no attributed cause" and demands
be flagged "as loudly as a regression". Under this design they are
R-DELTA-1 firings, and — because no prediction in the eight-row list of
`feedback_…-repin.md` §3 covers them — they are ALSO R-DELTA-4 firings.
R-DELTA-4 is that feedback item, mechanised.

**Worked example — R-DELTA-2**: same report, `factored` /
short-subject-search / plain / `pcrec_692c2e8_auto-nocaps-simdna`, rank 1:
`selection changed (vm → dfa)`. And in
`reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`,
`cls-upto-8192` / match-compliance / whole-subject /
`pcrec_d34c9131_auto-caps-simdna`, rank 3: `selection changed (dfa → vm)`.

### §4.3 Class R-RANK — rank flips vs the reference arm

The reference arm is `report.py`'s own (`_is_reference`,
report.py:3153): a testee id beginning `libpcre2_` and containing
`_interp-`. It is the denominator of `ratio_vs_baseline`.

| id | fires on |
|---|---|
| R-RANK-1 | a cross-pin pair (same engine+config, different version slug) whose `ratio_vs_baseline` values lie on opposite sides of 1.0 |
| R-RANK-2 | a cross-pin pair whose `rank_or_na` order contradicts its own `delta_verdict` direction |
| R-RANK-3 | a ranking group in which the reference arm is absent (no ratio_vs_baseline denominator was measured; the reporter falls back to the best row, report.py:4134-4135) |

**Inputs.** `report:rank.{pattern,regime_or_na,form,testee,rank_or_na,
delta_verdict}` and `metric=ratio_vs_baseline.value`. The cross-pin pair
is formed by splitting a pcrec testee id on
`^pcrec_(?P<pin>[0-9a-f]+)_(?P<config>.*)$` — the composition rule in
docs/design/record_schema.md §6.4 — and grouping by `config` within a
(pattern, regime, form) group. Non-pcrec testees are unpinned and never
form a pair.

**Threshold and source.** R-RANK-1's boundary is **1.0 on
`ratio_vs_baseline`, and it is DEFINITIONAL, not tuned**: the reference
arm *is* 1.000× by construction ([B9] R5), so "crossed the reference
arm" is exactly "the ratio crossed 1". Stated as definitional in
`threshold_src` so a panel can see there is no hidden constant. R-RANK-2
has no threshold (an ordering comparison). R-RANK-3 has none.

**Template.**

```
R-RANK-1  "{pattern} / {regime} / {form} / config `{config}`: vs the
           reference arm `{reference}`, {old_pin} reads {old_ratio}× and
           {new_pin} reads {new_ratio}× — the cell crossed the reference
           arm between the two pins."
```

**Worked example.** `reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`,
`cls-upto-8192` / match-compliance / whole-subject, config
`auto-caps-simdna`: `pcrec_334fd10e` reads `ratio_vs_baseline` **1.788**
(slower than `libpcre2_10.46_interp-caps-simdna`) and `pcrec_d34c9131`
reads **0.269** (faster). R-RANK-1 fires. The *same cell* fires
R-DELTA-2 (`selection changed (dfa → vm)`) — and that co-firing is the
point: the rank flip is a fact, the selection change is a fact, and the
sentence "the flip is because the route changed" is a hypothesis the
interpreter does not write. A reader gets both facts adjacent and draws
it themselves in ten seconds. A second instance, on the older wave:
`reports/2026-08-29-loglines-0.1-budu-ryzen1600-repin-36d5963.tsv`,
`stack-frame` / short-subject-search / plain, config
`auto-caps-simdna`: 35e1ab1 **2.698×** → 36d5963 **0.155×**.

A census over the 42 committed report TSVs (run for this note, by the
predicate above) finds R-RANK-1 firing in **9 of 42** files, on **69
(pattern, regime, form, config) pairs** in total, concentrated in
`2026-09-05-altwide-0.2-…-after-334fd10e.tsv` (40 pairs) and spread thin
elsewhere (bounded@0.2 after-a7e0bdf 7; bounded@0.3 after-d34c9131 7;
loglines 4 + 4; email@0.2 2; loglines@0.1 after-1989c62 2; bounded@0.1
repin-96e44c2 2; bounded@0.3 step2-after-288d505 1). A plausibility
check that the rule is neither dead nor universal — and the altwide
concentration is itself the kind of thing a reader should see, since
that wave is where the refusal wall moved.

### §4.4 Class R-FLOOR — ratios inside the timer floor

Two genuinely different floors, and conflating them is the mistake this
class exists to prevent.

| id | fires on |
|---|---|
| R-FLOOR-1 | a `compile` section row with `metric=jitter, value=timer-floor` |
| R-FLOOR-2 | a ranked cell whose per-subject mean ≤ the floor pattern's per-subject mean for the same (regime, testee) |
| R-FLOOR-3 | a `compile` row whose `jitter` ratio is ≥ 1.0 (stddev at or above the median) |

**R-FLOOR-1.** Inputs: `report:compile.{pattern,form,testee,metric,
value}`. Threshold source: `_TIMER_FLOOR_NS = 20_000` (report.py:1927),
applied by `_jitter_flag` (report.py:2150-2165) — "20 microseconds, the
clock's practical floor"; a compile cell whose `min_ns` is under it
reports `timer-floor` instead of a ratio "that is mostly measuring the
clock, not the compile". **The interpreter reads the token, never the
constant.** In `reports/2026-09-07-syntax-…-first-d34c9131.tsv`, 190
compile rows carry `timer-floor` against 26/23/23/23 carrying real
ratios. This is the exact complaint of `feedback_…-repin-v2.md` §2 —
"the interpretive rows have stddev ≈ median (12.3 K vs 13.5 K)" —
answered upstream by [B14] R5 and surfaced here.

**R-FLOOR-2.** Inputs: `report:rank.{pattern,regime_or_na,form,testee,
n}` and `metric=median_ns.value`. Arithmetic, declared in the catalogue
and identical to `_floor_mean_for` (report.py:2582-2595):
`per_subject_mean = median_ns / n`, computed for the cell and for the
`role: floor` pattern of the same (subbench, regime, testee). The floor
pattern's id is **not hard-coded**: schema v1.3's `patterns[].role`
([B15]) names it, and at TSV level it is the pattern the reporter
titles as the per-call overhead control. v1 identifies it by the
sub-bench's `subbench.toml` — *the one place `interpret` reads outside
its two inputs*, and a deliberate, named exception (open question Q1,
§11: whether the reporter should instead emit a `floor_pattern:` header
key, which would close the exception in one line).

Threshold: **≤ 1.0 on the ratio, definitional** — "at or below the set's
own per-call overhead control".

Worked example, `reports/2026-09-07-syntax-0.1-…-first-d34c9131.tsv`:
`anc-caret` / short-subject-search / `pcrec_d34c9131_vm-caps-simdna`,
rank 1, median 246.458 ns over n = 42 subjects → **5.868 ns/subject**.
The `floor` pattern on the same testee and regime: median 800.099 ns
over 42 → **19.050 ns/subject**. The ranked cell is **0.308×** the
floor control. R-FLOOR-2 fires: a between-testee ratio on this cell is a
ratio between two numbers both smaller than the set's own overhead
control. (The ledger's §8 reading — that `floor` = `#` is a *scan* cell
in this set and not a pure per-call floor — is the judgment; the rule
states the arithmetic and stops.)

**R-FLOOR-3.** Threshold `≥ 1.0`, definitional ("stddev at or above the
median"), reading the ratio `_jitter_flag` already printed. This is the
`interp compile-cost variance` row of `feedback_…-repin.md` §3, the one
prediction-uncovered item in that table: "12..109 µs over 10 trials is
timer jitter — the report should say so rather than print a stddev
larger than the median."

### §4.5 Class R-PRED — predictions vs outcomes

Fires only with a predictions file (§6).

| id | fires on |
|---|---|
| R-PRED-1 | a prediction whose claim HOLDS against the report |
| R-PRED-2 | a prediction whose claim FAILS |
| R-PRED-3 | a prediction whose cell is absent from the report, or present but excluded/not-ranked |
| R-PRED-4 | (= R-DELTA-4) a R-DELTA-1 / R-RANK-1 / R-FLOOR-2 firing that no prediction's selector covers |

**Threshold.** None. A prediction states its own bounds; the rule
evaluates them. R-PRED-3 exists so a prediction can never be silently
dropped — the failure mode a hand-kept ledger has (`feedback_…-repin.md`
§3's eighth row is literally "UNCOVERED by any prediction").

**Template.**

```
R-PRED-1  "{prediction_id} ({source}) — **confirmed**: predicted
           {claim}; measured {measured}."
R-PRED-2  "{prediction_id} ({source}) — **refuted**: predicted
           {claim}; measured {measured}."
R-PRED-3  "{prediction_id} ({source}) — **not evaluable**: {reason}."
R-PRED-4  "{pattern} / {regime} / {form} / `{testee}`: {finding} — no
           prediction in {predictions_file} covers this cell."
```

### §4.6 Class R-BUCKET — registered buckets

A *registered bucket* is a known reading that is a FACT WITH A SOURCE —
the plan row's own example is "the `\z` regime artifact per feedback
2a". Buckets do not measure anything new; they attach a recorded,
citable caveat to a shape the report exhibits. Each has a `source` field
that must resolve to a committed file (§7.3).

| id | fires on | the registered fact, and its source |
|---|---|---|
| R-BUCKET-FORM | a ranking group whose rankable rows carry both `same program` and `separate artifact` in `fact` | pcrec has no end-anchored mode, so its whole-subject form is a SECOND ARTIFACT `(?:P)\z`; libpcre2 reaches the same regime with `PCRE2_ANCHORED\|PCRE2_ENDANCHORED` on its ordinary artifact. Source: docs/design/record_schema.md §5; report.py `_form_fact` ([B9] R4); pcrec [OS-4]. |
| R-BUCKET-VSBEST | a ranking group carrying ≥ 2 distinct pcrec pin slugs | `vs best` inverts visually wherever an OLDER pin's row ranks first; read same-pin rows or the Δ column. Source: reports/CLAUDE.md's reader's caveat (the a7e0bdf bounded entry), which records the "8192 inversion" REFUTED as a cross-pin `vs best` mis-reading ([B25]). |
| R-BUCKET-SPAN | a cross-pin pair whose two pins are not adjacent in the pin history | the Δ spans more than one abi step and is not a one-variable comparison. Source: reports/CLAUDE.md ("the bounded `vm-in` row's Δ partner is 288d505, not 334fd10e … spans THREE abi steps (16 → 22 → 23)"). |
| R-BUCKET-DOMINATED | a set cell > 90 % one subject | a ratio between two such sums is a real number about a real total AND a statement about ONE subject wearing the set's name. Source: `_DOMINANCE_SHARE = 0.90` (report.py:2326) and `_dominant_subject`'s docstring ([B16] R7). **Needs a subject-grain TSV** (§10 Q2). |
| R-BUCKET-KB | a cell matching a KNOWN OPEN defect's signature registered in the catalogue | e.g. KB-13: a `large-subject-throughput` cell whose exclusion reads `expected N non-overlapping match(es); observed M` with M < N and no give-up. Source: docs/dev/known_issues.md KB-13/KB-14/KB-15. |

R-BUCKET-KB is the one that earns the class. `interpret` does not
diagnose; it recognises a signature that has already been diagnosed and
written down, and prints the pointer. The signature is DATA in the
catalogue, so adding a newly-filed KB is a MINOR catalogue bump and no
code change.

**Worked example — R-BUCKET-FORM**, against the email repin report:
`orig` / match-compliance ranks nine rows in one table, of which seven
carry `whole-subject` / `separate artifact` (all pcrec) and two carry
`plain` / `same program` (both libpcre2). R-BUCKET-FORM fires once for
the group. This is `feedback_…-repin.md` §2's demand — "State 'same
program / separate artifact' as a column; the 'regime artifact' bucket
IS that fact, not a footnote" — met at both layers: the reporter has the
column ([B9] R4), and the interpreter states the reading with its
source.

**Worked example — R-BUCKET-VSBEST**: `reports/2026-09-06-bounded-0.3-…-after-d34c9131.tsv`,
`cls-upto-1024` / short-subject-search / plain: `pcrec_334fd10e_auto`
ranks **1** at 989.820 ns and `pcrec_d34c9131_auto` ranks **2** at
998.441 ns, while the same row's Δ reads `slower ×1.01` — the current
pin's `vs best` is worse than 1.000 purely because an older pin is in
the table. Three distinct pin slugs are present in that group
(288d505, 334fd10e, d34c9131), so the bucket fires.

---

## §5. Output of `interpret` (part 1)

Two modes, one code path:

```
python3 -m pcrecbench interpret reports/<name>.tsv \
    [--index store/index.tsv] [--predictions <file>] \
    [--subject-grain reports/<name>.subject-grain.tsv] \
    [--catalogue catalogue/rules.toml] [--format tsv|md] [--render]
```

- **`--format tsv` (default)** — the FACTS, machine-readable, one row
  per firing plus one row per non-firing rule. Columns:
  `rule_id  fired  pattern  subject_or_na  regime  form  testee
  record_id  slot  value`. Slots are emitted one per row (the same
  shape `render_tsv` uses for metrics) so a fact is greppable without a
  parser.
- **`--render`** — the sidecar markdown (§9), from the SAME slot values
  through the catalogue's templates.

A non-firing rule always emits a row with `fired=0` and a reason in
`value`: `no-matching-rows | input-absent | grain | reporter-version |
retired`. **A rule is never silently absent** — the plan row's "plus the
rules that did NOT fire" is the whole reason a reader can trust an empty
section.

Exit codes: `0` always on a successful read. Firing is not an error —
this is an instrument, not a gate. `2` on a malformed input, an unknown
column, an unresolvable link, or a catalogue/code mismatch.

---

## §6. Predictions as machine-readable input

### §6.1 There is no existing store — checked

`grep -rn "prediction" docs/dev/ pcrecbench/ schema/` returns prose
only: `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` §3's eight-row
markdown table, the ledger convention line in `docs/dev/CLAUDE.md`
("predictions ledgered"), `bench/syntax/NOTES.md`'s P1-P13, and free
text inside plan rows and inbox items. **No machine-readable prediction
exists anywhere in this repository.** This design must create the
minimal one.

### §6.2 What a prediction actually looks like today

Three real ones, spanning the shapes:

1. *"cls-upto-2048 ÷ 1024 stays in 0.90-1.10"* (pcrec I-38, scored in
   the [B34]/[B27] ledger as 1.986 → 1.987) — a RATIO BETWEEN TWO CELLS
   at one pin.
2. *"letters 3.65-6.05 → 1.76-2.00"* (pcrec I-27, [OPT-5] STEP 1) — a
   BAND on a ratio, before and after.
3. *"no compile time beyond ×10 the median on any compiled testee"*
   (bench/syntax NOTES P13, scored CONFIRMED at worst ×2.08) — a BOUND
   over a POPULATION.

A design that only handles (1) is useless. All three are the same shape
if a prediction names a *quantity*, a *selector*, and *bounds*.

### §6.3 The file

`docs/dev/predictions/<slug>.tsv`, one file per prediction SET, named
for the source that stated it (`I-38.tsv`,
`b36-syntax-0.1-notes-P1-P13.tsv`). TSV, not TOML, because these are
authored by hand alongside a ledger and reviewed in a diff, and because
the project's other hand-authored tabular data (`expectations.tsv`,
`coverage.tsv`, `list_axes.tsv`) is TSV.

Columns:

```
prediction_id   P13
source          bench/syntax/NOTES.md
source_ref      P13
stated_utc      2026-09-05T00:00:00Z
subbench        syntax
version         0.1
selector        pattern=*;regime=*;form=*;testee=*
quantity        compile:median_total_ns
reducer         ratio_to_median_over(testee)
op              lte
lo
hi              10
unit            x
note            "no compile time beyond x10 the median on any compiled testee"
```

- **`selector`** is a `;`-joined list of `key=glob` over the TSV's own
  key columns (`pattern`, `subject_or_na`, `regime_or_na`, `form`,
  `testee`). `*` is the only wildcard. A testee glob may name a config
  without a pin (`pcrec_*_auto-caps-simdna`) so a prediction survives a
  re-pin.
- **`quantity`** is drawn from a CLOSED SET the TSV can answer, declared
  in the catalogue and validated at load:
  `median_ns | min_ns | max_ns | stddev_ns | ratio_vs_baseline |
  ratio_vs_best | rank | pass_rate | n_gave_up | n_wrong |
  delta_verdict | status | section | compile:median_total_ns |
  compile:artifact_bytes | compile:emit_bytes |
  compile:emit_code_bytes | stamp:<name>`.
  A quantity outside the set is a load error, not a silent skip.
- **`reducer`** (optional) turns a population into one number:
  `identity | ratio_to(<selector>) | ratio_to_median_over(<key>) |
  max | min | median`. This is what lets (1), (2) and (3) share a form.
- **`op`** ∈ `lt lte gt gte between eq-token neq-token present absent`.
- Prediction (1) becomes:
  `selector pattern=cls-upto-2048;regime=match-compliance;form=plain;testee=pcrec_*_auto-caps-simdna`,
  `quantity median_ns`,
  `reducer ratio_to(pattern=cls-upto-1024;regime=match-compliance;form=plain;testee=<same>)`,
  `op between; lo 0.90; hi 1.10`.

### §6.4 How a prediction gets INTO the file

Written by hand, by the person who states it, **before the run**, and
committed before the run — the boilerplate's own rule ("a prediction is
stated BEFORE the run wherever the charter allows"). `stated_utc` is a
column so `make check-interpret` can assert it precedes the earliest
`timestamp` in the report's population, which makes post-hoc prediction
mechanically impossible to commit unnoticed.

Predictions stated in an inbox item are transcribed by the manager
session at ack time — the same motion that already moves an inbox item
into a plan row. **Parsing inbox prose is explicitly rejected:** a
regex over English is a second source of truth for what pcrec predicted,
and getting it wrong would be worse than not having it.

### §6.5 What v1 does not do

No back-fill. The eight predictions of `feedback_…-repin.md` §3 and the
thirteen of `bench/syntax/NOTES.md` may be transcribed later; the
acceptance test (§10) does not require it, and a lane transcribing 21
historical predictions is a separate, reviewable change.

---

## §7. The opinion firewall, enforced

The charter says "every sentence cites a fired rule". Discipline cannot
deliver that. Three structural properties do.

### §7.1 One template per rule, no free-text channel

The renderer is:

```
def render(rule_id, slots) -> str:
    rule = CATALOGUE[rule_id]
    missing = set(rule.slots) - set(slots)
    extra   = set(slots) - set(rule.slots)
    if missing or extra:
        raise InterpretError(...)          # a bug, not a warning
    return rule.template.format(**slots)
```

`str.format` on a template that declares its slots is the whole
sentence-production surface. There is **no code path** by which
`interpret` can emit a string that is not `stamp | heading | template
output | link | did-not-fire row`. Adding one would be a visible diff to
`interpret.py`'s renderer, and §8's no-prose check would fail it.

### §7.2 Slot values are copied, or computed by a declared arithmetic

Each rule function receives a **row view** that raises on any column not
in its declared `inputs`. A slot value must be one of:

- a literal cell value copied verbatim from an input file;
- an integer count of rows the rule itself matched;
- a number produced by an arithmetic written out in full in the
  catalogue's `arith` field (v1 has exactly two: R-FLOOR-2's
  `median_ns / n`, and R-RANK-1's side-of-1.0 test).

Every numeric slot is rendered by one formatter with a fixed precision
so two renders of the same input cannot differ in a digit.

### §7.3 Links are validated, never generated

A rule's `links` are repo-relative paths, optionally with a `#anchor` or
`:line`. At render time each is resolved: the file must exist, and an
anchor must appear as a heading or a literal id in it. An unresolvable
link exits 2. So a hypothesis can only appear in a sidecar if somebody
has already written it down and committed it — `docs/dev/outbox_to_pcrec.md`,
`docs/dev/known_issues.md`, `docs/dev/upstream_findings.md`,
`docs/dev/ledgers/`. The interpreter cannot invent a cause because it
has no way to say one.

### §7.4 The skill does not write prose either — a CHARTER DEVIATION, flagged

The plan row says the SKILL "phrases the fired rules into a SIDECAR".
This design instead puts the phrasing in `interpret --render` and leaves
the skill to run it, check the result and commit it (§9). The reason:
if a skill (i.e. a model) writes the sentences, the firewall is once
again a promise about behaviour rather than a property of the artifact,
and the sidecar stops being byte-reproducible — which kills §8's
determinism check and §3.3's regeneration rule at the same time.

**This is a deviation from the charter's letter and is offered for
Frank's / the panel's ruling, not assumed.** If it is rejected, the
fallback is: `--render` produces the sidecar as designed, and the skill
may add a clearly-fenced `## Reader's note` section that is EXCLUDED
from the byte-equality check — at the cost of the firewall applying to
part of the file only. This note recommends the deviation.

---

## §8. `make check-interpret`

A new target beside `check-schema` / `check-harness` / `check-report`,
added to `check`. Five sections.

**(1) Catalogue/code correspondence.** Every `[[rule]]` has a function;
every function has a `[[rule]]`; every declared `inputs` column exists
in `render_tsv`'s header or `store/index.tsv`'s header (read from the
source, not retyped — the project's derivations-are-imported rule);
every `quantity` token in every committed predictions file is in the
closed set; every `links` entry resolves; every rule has ≥ 1 fixture and
≥ 1 negative control.

**(2) Determinism.** `interpret` run twice on the same inputs produces
byte-identical output in both formats. Then, on **three named real
reports** (§10's acceptance set), the output is compared against
committed golden files `catalogue/golden/<report-basename>.facts.tsv`.
A change to any rule that moves a fact on a real report must move a
committed golden file in the same commit — the invariant `reports/CLAUDE.md`
already applies to renders, applied to facts.

**(3) Sidecar freshness.** Every committed
`reports/*.interpretation.md` is re-rendered from its recorded inputs
(the stamp names them and their sha256) and must come back byte-identical.
A report edited without re-rendering its sidecar, or a catalogue bump
without regeneration, fails here.

**(4) Sabotage fixtures — one per rule, named for the rule they
exercise.** Mirroring `schema/examples/bad/`'s pattern exactly (73
files, each rejected "FOR THE RULE ITS NAME CLAIMS"):

```
catalogue/fixtures/R-DELTA-1__faster-outside-spread/
    report.tsv      a minimal, schema-shaped report TSV
    index.tsv       a minimal store index
    expect.txt      R-DELTA-1
catalogue/fixtures/R-DELTA-1__control-unchanged-within-spread/
    report.tsv      the SAME file with delta_verdict = "unchanged (within spread)"
    index.tsv
    expect.txt      (empty — R-DELTA-1 must NOT fire)
```

The check asserts the named rule fires on the sabotage and does NOT fire
on its control, and that the control differs from the sabotage in the
minimum number of bytes (a fixture pair that diverges in ten places does
not prove which byte fired the rule). Fixtures are hand-written, small,
and share no source with the rule functions — the project's
controls-share-no-source discipline (pcrec D35, restated in this repo's
CLAUDE.md).

Rules needing a co-firing or mutual-exclusion property get a third
fixture: R-DELTA-1 and R-DELTA-2 must never fire on the same cell;
R-RANK-1 and R-DELTA-2 must be able to.

**(5) The no-prose check.** A generated sidecar is re-parsed and every
non-blank, non-heading, non-stamp line must be reproducible by
`render(rule_id, slots)` for some rule and some slot set present in the
facts TSV. A line that is not is a failure. This is the firewall's own
test, and it is the check that would catch a future lane quietly adding
a sentence.

Runtime budget: the fixtures are tiny and the golden set is three files,
so this target is seconds, not the ~20 minutes `check-harness` costs. It
goes into `check` without an argument about budget.

---

## §9. The skill, and the sidecar's exact format

### §9.1 The skill

`.claude/skills/pcrec-bench-interpret/SKILL.md` (+ `CLAUDE.md`, per
`.claude/skills/CLAUDE.md`'s convention). Invoked
`/pcrec-bench-interpret <report>` where `<report>` is a basename, a
`.md` or a `.tsv` path (all three resolve to the `.tsv`).

What it does, in order, and nothing else:

1. resolve the report group; refuse if the `.tsv` is absent;
2. locate the predictions file(s) whose `subbench`/`version` match the
   report's header, if any;
3. run `python3 -m pcrecbench interpret … --render`;
4. write `reports/<name>.interpretation.md`;
5. re-run `interpret` and byte-compare (the determinism check, locally);
6. report the fired-rule counts to the session and stop.

It does **not** summarise, rank, explain or extend. If a fired rule
looks wrong to the session, that is a catalogue change through a lane,
not an edit to the sidecar.

### §9.2 The sidecar, rendered by hand from a real current report

Below is what `/pcrec-bench-interpret 2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8`
must produce once built — every number taken from the committed
`.tsv` and from `store/index.tsv`, abridged with `…` only where a rule
fires many times. **This is a specification of output, not an example of
style.**

```markdown
<!-- pcrecbench interpret
report:          reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv
report_sha256:   <64 hex>
index:           store/index.tsv
index_sha256:    <64 hex>
predictions:     (none)
catalogue:       1.0
interpret:       v1
reporter:        v12 (2026-09-02)
query:           subbench=email-specimen, version=0.1
-->

# Interpretation — 2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8

Generated by `pcrecbench interpret` against catalogue 1.0. Every
sentence below is a rule template. No sentence is generated.

## R-STATUS-5 — query population (1 firing)

- The query drew 14 candidate record(s) and included 9; 5 superseded,
  0 newer-but-not-measured, 0 invalid.

## R-STATUS-2 — a non-measured record outside the population (3 firings)

- `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z`
  (testee `libpcre2_10.46_interp-caps-simdna`, 2026-08-25T17:34:02Z) is
  in store/index.tsv for email-specimen@0.1 on budu-ryzen1600 with
  status **inconclusive-load** and is NOT in this report's population.
- … `pcrec_692c2e8_auto-caps-simdna`, 2026-08-25T17:51:31Z …
  **inconclusive-load** …
- … `pcrec_692c2e8_auto-nocaps-simdna`, 2026-08-25T17:55:34Z …
  **inconclusive-load** …

## R-STATUS-6 — mixed schema versions (1 firing)

- This report's population spans record schema versions 1.1, 1.2.

## R-STATUS-3 — cells excluded from ranking (N firings)

- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_vm-caps-simdna` is EXCLUDED from ranking: pass-rate
  0.6667, 0 wrong answer(s), 5 give-up(s) — `-2:PCREC_ERR_STEPS×1
  (smallest: t-c-long-atom-run, 1,048,576 B)`.
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_vm-caps-simdna` … pass-rate 0.9412, 25 give-up(s) —
  `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)`.
- orig / large-subject-throughput / plain /
  `pcrec_692c2e8_vm-caps-simdna` … 5 give-up(s) — `-4:PCREC_ERR_WORK×1
  (smallest: t-c-long-atom-run, 1,048,576 B)`.
- …

(`n_gave_up` counts TRIALS; the `×N` in the summary counts SUBJECTS,
grouped by the dominant code — `_gave_up_cell_summary`, [B9] R7. The
template prints both, in those words, because a reader given one number
will read it as the other.)

## R-STATUS-12 — one subject, two give-up codes across two spellings (1 firing)

- Subject `t-c-long-atom-run` (1,048,576 B) gives up as
  **`-2:PCREC_ERR_STEPS`** on `factored` and **`-4:PCREC_ERR_WORK`** on
  `orig`, on `pcrec_692c2e8_vm-caps-simdna` in
  large-subject-throughput: a different budget binds on the two
  spellings.

## R-DELTA-1 — cross-pin Δ outside spread (N firings)

- factored / short-subject-search / plain /
  `pcrec_692c2e8_vm-caps-simdna`: the reporter's cross-pin Δ reads
  **faster ×1.19** (median 69,537.5 ns).
- orig / match-compliance / whole-subject /
  `pcrec_692c2e8_vm-caps-simdna`: the reporter's cross-pin Δ reads
  **faster ×1.26** (median 80,227.6 ns).
  Source: report.py `_cross_pin_verdict` ([B9] R8) — unchanged iff the
  median difference is within 2 × max(stddev_old, stddev_new).

## R-DELTA-2 — cross-pin selection change (6 firings)

- factored / short-subject-search / plain /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 1): **selection changed
  (vm → dfa)**. A ratio between two different engines is not computed
  ([B16] R4).
- …

## R-DELTA-4 — a Δ outside spread that no prediction covers (0 firings)

- did-not-fire: input-absent (no predictions file for
  email-specimen@0.1).

## R-BUCKET-FORM — the regime artifact (2 firings)

- orig / match-compliance ranks rows of BOTH facts: 7 `separate
  artifact` (whole-subject) and 2 `same program` (plain). pcrec has no
  end-anchored mode and compiles `(?:P)\z` as a second artifact;
  libpcre2 reaches the regime with runtime ANCHORED|ENDANCHORED on its
  ordinary artifact.
  See: docs/design/record_schema.md §5; pcrec [OS-4].
- …

## R-BUCKET-VSBEST — two pins in one ranking group (N firings)

- orig / short-subject-search / plain carries 2 pin slug(s)
  (8da6120, 692c2e8); `vs best` inverts wherever an older pin's row
  ranks first — read same-pin rows or the Δ column.
  See: reports/CLAUDE.md (reader's caveat).
- …

## R-FLOOR-1 — a compile ratio inside the timer floor (N firings)

- orig / plain / `libpcre2_10.46_interp-caps-simdna`: the compile-cost
  jitter reads `timer-floor` (min under 20 µs, report.py
  `_TIMER_FLOOR_NS`); the ratio measures the clock, not the compile.
- …

## Rules that did not fire

| rule | reason |
|---|---|
| R-STATUS-7 | no-matching-rows (mixed_x13: False) |
| R-STATUS-9 | no-matching-rows (every record reads `agree` or `n/a (v1.x)`) |
| R-STATUS-11 | no-matching-rows (no scratch rows) |
| R-RANK-1 | no-matching-rows |
| R-FLOOR-2 | no-matching-rows (no `role: floor` pattern in email-specimen@0.1) |
| R-PRED-1 … R-PRED-4 | input-absent |
| R-BUCKET-DOMINATED | input-absent (no subject-grain TSV supplied) |
| R-BUCKET-KB | no-matching-rows |
```

Note what the sidecar does NOT say: not one sentence about *why* the VM
got faster across the pin, which is the fact `feedback_…-repin-v2.md`
called "real and unexplained". The interpreter's job ends at flagging
it. That is the design working.

---

## §10. THE ACCEPTANCE TEST — catalogue v1's falsifiable promise

Frank's original phrasing (2026-08-25, plan row): *"catalogue v1 must
find, unprompted, the collapse, the three inconclusive records, the
give-ups and the vm-in result in the two existing reports."* Two of
those reports still exist; the corpus is now 42. Updated, and stated
**before any code exists**, so a later lane cannot quietly weaken it.

Three reports. For each: what v1 MUST surface unprompted, and what it
MUST NOT claim. Every number below is from the committed file.

### Report A — `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`
*(Frank's original target, preserved)*

MUST surface:

1. **The three inconclusive records**, by record id, as R-STATUS-2 —
   `libpcre2_10.46_interp-caps-simdna` @ 17:34:02Z,
   `pcrec_692c2e8_auto-caps-simdna` @ 17:51:31Z,
   `pcrec_692c2e8_auto-nocaps-simdna` @ 17:55:34Z, all
   `inconclusive-load`, none of them in the report. **This is the claim
   that requires `store/index.tsv` as an input**; a design reading the
   report alone fails it, which is why it is first.
2. **The collapse** as R-DELTA-2, six firings: `factored` under `auto`
   reads `selection changed (vm → dfa)` in all three regimes × two
   configs (short-subject-search ranks 1 and 2; match-compliance
   whole-subject ranks 1 and 2; large-subject-throughput ranks 1 and 2,
   the latter pair also carrying `now measured (was: gave-up)` →
   R-DELTA-3).
3. **The give-ups**, by code and smallest firing subject, as R-STATUS-3
   — all thirteen excluded cells, carrying
   `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)`,
   `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)` and
   `-4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B)`.
3b. **The STEPS-vs-WORK datum** as R-STATUS-12: subject
   `t-c-long-atom-run` gives up as `-2:PCREC_ERR_STEPS` on `factored`
   and `-4:PCREC_ERR_WORK` on `orig`, same testee, same regime — the
   second of the two rule facts the journal's part-7 entry sent to
   [B13]. A v1 that surfaces the give-ups but not this pairing has
   implemented half the charter.
4. **The vm-in result** — not as a verdict, as adjacency: `orig` /
   short-subject-search ranks `pcrec_692c2e8_vm-in-caps-simdna` at 6
   (12,546.19 ns) and `pcrec_692c2e8_vm-caps-simdna` at 7 (28,996.91 ns);
   `orig` / match-compliance ranks vm-in 1 (62,732.30) and vm 2
   (80,227.62). The rule that carries it is R-BUCKET-VSBEST plus the
   ranked rows themselves; **if v1 cannot make a reader see this pair
   without a human pointing at it, that is a finding against the design
   and belongs in the panel's report.** Stated as a risk, not a pass.
5. **The unpredicted Δ** as R-DELTA-1: `faster ×1.19` (factored /
   short-search / vm) and `faster ×1.26` (orig / compliance / vm) — the
   two numbers `feedback_…-repin-v2.md` §2 demanded be flagged "as
   loudly as a regression".
6. **The regime artifact** as R-BUCKET-FORM on `orig` /
   match-compliance and `factored` / match-compliance.
7. **The mixed schema population** as R-STATUS-6 (`1.1,1.2`).

MUST NOT claim: any cause for (5); that vm-in is "better"; that the
collapse is wave G's splice.

### Report B — `reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`
*(the current cross-pin wave)*

MUST surface:

1. **R-RANK-1 on `cls-upto-8192` / match-compliance / whole-subject /
   config `auto-caps-simdna`**: `ratio_vs_baseline` 1.788 at 334fd10e
   → 0.269 at d34c9131 — the cell crossed the reference arm.
2. **R-DELTA-2 on that same cell**: `selection changed (dfa → vm)`.
   The co-firing is required; a v1 that fires only one of the two on a
   cell that carries both is failing.
3. **R-BUCKET-SPAN on the `vm-in` rows**: their Δ partner is 288d505,
   not 334fd10e — a Δ across three abi steps (16 → 22 → 23), e.g.
   `cls-upto-1024` / large-subject-throughput / plain,
   `pcrec_d34c9131_vm-in-caps-simdna`, `faster ×1.53`, and
   `cls-upto-1024` / short-subject-search / plain, `faster ×1.25`. The
   fact reports/CLAUDE.md records by hand today.
4. **R-BUCKET-VSBEST** on every group carrying ≥ 2 pin slugs, including
   the visual inversion on `cls-upto-1024` / short-subject-search
   (334fd10e ranks 1 at 989.820 ns; d34c9131 ranks 2 at 998.441 ns; the
   Δ reads `slower ×1.01`).
5. **R-RANK-1 on the `dig-*` throughput rows**, at least
   `dig-exact-8`, `dig-upto-8`, `dig-exact-16`, `dig-upto-16`,
   `dig-exact-32` on config `vm-in-caps-simdna` (each crossing 1.0
   between 288d505 and d34c9131) — five firings, which is the rule
   showing it is not a one-off.

MUST NOT claim: that the STEP 2 match-axis customers moved (they did
not — ledger 2026-09-05, O-16); any attribution for the crossings.

### Report C — `reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`
*(the newest sample, and a set with a floor pattern)*

MUST surface:

1. **R-STATUS-4 on the refusal population**: 172 `did_not_compile` rows
   reducing to the distinct (pattern, testee) set, each with pcrec's own
   diagnostic verbatim (`module 'conditionals' is enabled but (?(...) is
   not implemented yet (pattern offset 8)`, etc.).
2. **R-STATUS-3 on the 23 excluded cells**, including `rec-1` /
   large-subject-throughput at `pass_rate 0.0000` with 15 wrong answers
   on five testees, and `asr-k-uc` / match-compliance / whole-subject at
   `0.9762` with 5 wrong answers on four pcrec arms.
3. **R-BUCKET-KB fires on both of those, and names them**: the `rec-*`
   throughput exclusions carry KB-13's signature (a match-count
   shortfall with no give-up recorded); `asr-k-uc` / whole-subject
   carries KB-14's (a whole-subject span mismatch on pcrec only).
   **This is v1's strongest claim: the three findings that headline the
   [B36] outlier read — KB-13, KB-14, KB-15 — were found by an opus
   lane reading for hours, and at least two of the three must be
   recognised from their signatures by rule.** If R-BUCKET-KB cannot
   express those two signatures from TSV columns alone, the class is
   under-designed and the panel should say so.
4. **R-FLOOR-2 on `anc-caret` / short-subject-search /
   `pcrec_d34c9131_vm-caps-simdna`**: 246.458 ns / 42 = 5.868
   ns/subject against the `floor` pattern's 800.099 / 42 = 19.050 — the
   ranked cell is 0.308× the set's own per-call control.
5. **R-FLOOR-1 on the 190 compile rows reading `timer-floor`.**
6. **R-STATUS-9 must NOT fire** — all six records read
   `agree (0 of N groups …)`. A rule that fires here is a false positive
   and fails the acceptance test.

MUST NOT claim: that `\G` is not treated as an anchor (ledger §4.1,
Q4 — a mechanism question, not a fact in the TSV); that the interpreter
found KB-13's *cause* (the ctypes probe that established
`PCRE2_ERROR_JIT_STACKLIMIT` is not something `interpret` can or should
do); any of NOTES.md's R2/R4/R7 band verdicts (out of scope, §1.1).

### The promise, in one sentence

**Catalogue v1 is accepted iff, run on those three reports with no
predictions file and no human hint, it surfaces every numbered MUST item
above and asserts none of the MUST-NOT items** — with items A.4 and C.3
called out in advance as the two most likely to fail, and their failure
being a finding about the design rather than an excuse.

---

## §11. Open questions the panel must rule on

- **Q1.** R-FLOOR-2 needs to know which pattern has `role: floor`, and
  the TSV does not carry it. v1 reads `bench/<dir>/subbench.toml` — the
  only read outside the two declared inputs. Alternative: the reporter
  emits a `floor_pattern:` header key (a one-line change,
  `REPORTER_VERSION` bump, every report regenerated). **Recommendation:
  the header key**; the exception is small but it is exactly the kind
  that grows.
- **Q2.** R-BUCKET-DOMINATED needs per-subject data, and no committed
  report group has a subject-grain TSV (only `.md`, `.subject-grain.md`,
  `.tsv`). Options: (a) add `--subject-grain` as an optional input and
  let the rule report `input-absent` — v1's default; (b) have the
  reporter also commit `<name>.subject-grain.tsv` for every group;
  (c) drop the rule from v1. **Recommendation: (a) now, (b) as a
  separate reporter change.**
- **Q3.** Should set-local outlier bands (`bench/*/NOTES.md`'s R0-R7)
  become catalogue-readable data in `subbench.toml`? §1.1 says not in
  v1. The argument for: the bands are already written before every run,
  and a machine that checks them is exactly this tool. The argument
  against: a band is a judgement, and mechanising it invites the
  catalogue to acquire opinions by increments.
- **Q4.** The §7.4 charter deviation (the skill does not phrase; the
  renderer does). Frank's ruling.
- **Q5.** Should a sidecar be written for every one of the 42 existing
  reports at v1 landing, or only for reports from the landing forward?
  Back-filling 42 sidecars is cheap to generate and expensive to
  review. **Recommendation: the three acceptance reports at landing,
  the rest on demand.**
- **Q6.** `interpret` exits 0 on any firing. Should a fired R-STATUS-9
  (`disagree`) or R-BUCKET-KB ever be a non-zero exit, so a window
  script can react? **Recommendation: no** — the instrument/gate
  separation is the same one BD7 and schema v1.4 drew, and a gate that
  reads a report is a different design.
- **Q7.** The catalogue's rule functions live in `pcrecbench/interpret.py`
  while the catalogue lives in `catalogue/rules.toml`. Two files must
  agree, checked by §8(1). Is that split right, or should the predicate
  be executable data? **Recommendation: keep the split** — a DSL is a
  second language to get wrong, and §8(1) makes drift a build failure.
- **Q8.** R-STATUS-12 parses the subject id and byte count out of
  `_gave_up_cell_summary`'s formatted string (`(smallest: <id>, <n> B)`)
  — the one rule that reads a rendering rather than a column, and
  therefore the one that breaks if [B9] R7's wording is ever reworded.
  Options: (a) accept it, pinned by a fixture that fails loudly on a
  wording change; (b) ask the reporter for `smallest_giveup_subject` /
  `_bytes` as their own TSV columns. **Recommendation: (b), and (a)
  until it lands** — the fixture makes the breakage a build failure
  rather than a silent non-firing.

---

## §12. What this note deliberately does not decide

- The exact python module layout of `interpret.py` beyond the renderer
  contract (§7.1-7.2).
- The wording of any individual template beyond the shapes shown — a
  template's wording is a MINOR catalogue bump and a lane's call under
  review.
- Whether `interpret` ever gains a second output consumer (a dashboard,
  a CI annotation). v1 has two: the sidecar and a human running it.
- Anything about `~/pcrec`. This tool reads this repository's own
  artifacts only (BD2).
