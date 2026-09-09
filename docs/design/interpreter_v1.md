# The interpreter — design note v1.2 ([B13])

STATUS: **IMPLEMENTED (lane b13impl, 2026-09-09)** — part 1 is built
against this note as it stands: `catalogue/rules.toml` (catalogue 1.0,
31 rules), `pcrecbench/interpret.py` + the `interpret` subcommand,
`docs/dev/predictions/`, `catalogue/fixtures/` + `catalogue/golden/`,
and `make check-interpret` (six sections, 129 checks). §10's acceptance
test RAN: 25 of 25 items pass. The implementation's deviations from this
note — none of them changes a rule's predicate or threshold — are listed
in `docs/dev/lanes/b13impl_report.md`; this note is NOT rewritten to fit
the build. Part 2 (the `/pcrec-bench-interpret` skill and the committed
`.interpretation.md` sidecars) is [B13.4], **IMPLEMENTED (lane
`b13skill`, 2026-09-09)**: the skill at
`.claude/skills/pcrec-bench-interpret/SKILL.md` and the three §10
acceptance-report sidecars committed under `reports/`. What follows is
the design as v1.2 stated it. **v1.2, 2026-09-08** — v1.1
(lane `b13rev`, 2026-09-07) revised in place by lane `b13v12` under the
pcrec manager session's cross-review of v1.1, inbox item I-58: **APPROVED
CONDITIONAL**, four spec edits, one revision commit, no re-panel. v1.1
was itself v1 (lane `b13design`, merged `651a7ce`) revised under every
disposition of the r4 adversarial critic panel
(`docs/dev/reviews/2026-09-07-r4-interpreter-v1.md`, three lenses:
source verification, charter fidelity, implementability — 11 BLOCKING,
8 SHOULD-FIX, ~14 documentation corrections, all accepted or
accepted-amended by the manager). It is a single coherent design, not a
diff: read it as the corrected design, and where a citation would
otherwise confuse a reader who knows an earlier version, a short
"corrected from v1" or "cross-review I-58" note says what moved and why.

**What v1.2 changed, in one list (I-58's four must-fix edits plus two
minors and one honesty edit, all in this one commit):** the header
comment's known-key split is now NORMATIVE, not "equivalent" to the
regex-rejoin form, which are shown to diverge in both directions (§2.1);
R-STATUS-3's predicate is scoped to `metric = pass_rate` so precondition
P-2's `giveup_smallest` rows (read only by R-STATUS-12) cannot make it
double-fire (§2.5, §4.1); `section` is added to §6.3's closed selector
key list, which §6.6's own P1 transcription already needed; the R-DELTA-1
aggregate key's `config` and `direction` (and R-DELTA-2/3's `config`) are
now declared decompositions in each rule's `arith` field, extending
§7.2's decomposition table (§4.2, §7.2); an aggregated bullet's rendering
is now defined for a rule with no numeric slot (the specimen's own
full-sorted-id-list behaviour, now stated as the rule) and a rule may
declare its own `extremal` slot, which R-DELTA-1 now does (`ratio`, the
biggest mover, not the largest-median cell) (§5.2, §3.2); the
`reduce.py:373-379` citation for the `agree (…)` string is corrected to
`reduce.py:372-376` against the 376-line file (§4.1); and §6.5's
`stated_utc` check now reads the earliest index timestamp for the
population INCLUDING superseded records, closing the supersession window
a report-scoped check leaves open, with the residual limit stated
honestly rather than claimed away (§6.5, §13). The r4 review's own
step-2 confirmation pass, run by the pcrec manager session at Frank's
ask, is recorded in `docs/dev/reviews/2026-09-07-r4-interpreter-v1.md`'s
new closing section.

The panel's own summary of what survives unchanged is recorded in §13,
so a later reader does not mistake the revision's size for a rewrite:
no rule introduces a tuned constant, the interpreter reads the
reporter's own verdict strings rather than re-deriving them, it reads
the TSV and never the markdown, and the acceptance test (§10) was
written before any code existed — which is why the panel could find
these gaps at a cost of one design pass.

Author: lane `b13design`, 2026-09-07; revised by lane `b13rev`,
2026-09-07; revised again by lane `b13v12`, 2026-09-08. Charter:
docs/dev/plan.md row `[B13]`, agreed by Frank 2026-08-25
(docs/dev/dev_journal.md, second session parts 5 and 7). Stated inputs:
`docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` and `-repin-v2.md` —
the pcrec manager session's two readings of the same report, which are
the only existing worked examples of a human doing by hand exactly what
this tool must do by rule.

---

## §0. The problem, in one paragraph

A committed report under `reports/` is a deterministic, diffable table.
Reading one takes a manager session hours and produces a ledger under
`docs/dev/ledgers/` — 1,085 lines for bench/syntax@0.1's first sample.
Most of that work is *judgment* and belongs to a person. But a
measurable fraction of it is not judgment at all: it is a fixed set of
questions asked of a fixed set of columns ("which records were not
`measured`?", "which cross-pin Δ is outside spread?", "which two arms of
one engine differ by more than their own spread?", "which stated
prediction did this refute?"). Those questions are asked by hand today,
which means they are sometimes not asked at all. `[B13]` mechanises
exactly that fraction.

Frank's constraint, verbatim from the plan row: **"no opinions, all
based on facts."** The design's whole architecture follows from taking
that literally rather than as an aspiration — see §7.

**What that constraint can and cannot buy (corrected from v1, panel
F9).** v1 claimed the design "*cannot* creep past" its scope. That
overstates what architecture delivers, and the overstatement was itself
the hole: if opinions were structurally impossible, nobody would need to
review the catalogue's template prose or its registered signatures, and
that is exactly where the panel found two opinions sitting unaudited
(F1, F2). The true and stronger claim is this: **the catalogue is where
this project's opinions are deliberately concentrated** — stated once,
in one versioned file, each with its threshold's source, diffable,
reviewable, and bumpable — instead of being re-improvised in prose every
time a report is read. Everything in §7 is built to keep them there and
to make them visible, not to pretend they do not exist.

An honest statement of the value (panel F13): the interpreter mechanises
a ledger's **inventory** sections — which records, which exclusions,
which refusals, which Δs moved, which arms differ — and touches almost
none of its *reading* sections. On the [B36] syntax sample it would have
listed the three `inconclusive-load` records nobody would have listed by
hand, the give-up code pairing, the refusal inventory and the arm gaps,
and it would have named no defect. That is worth having every time,
cheaply, forever; it is not a claim to have found KB-13.

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
  computed by `report.py` and printed in the TSV, or (b) a comparison of
  two measured quantities in the same report.
  **If a later ruling wants set-local bands, they belong in the set's
  own sidecar (`subbench.toml`), read by `interpret` as data — not in
  the catalogue.** Named as open question Q3 (§11), the one question the
  r4 panel left to Frank.
- **Causes.** The interpreter never says *why* a number moved. Where a
  cause is already recorded somewhere (outbox `O-n`, `known_issues.md`
  `KB-n`, `upstream_findings.md` `Un`), the rule may carry a LINK to it;
  it may not generate one, and it may not assert one in template prose
  either (§7.1, the fix the panel's F1 required).
- **Rankings of importance.** No rule sorts findings by how interesting
  they are. Output order is the catalogue's declaration order, which is
  stable and therefore diffable. Declaration order is itself editorial —
  §0 says so rather than denying it — and it is reviewed as part of the
  catalogue.
- **Compression that is not arithmetic.** A rule may collapse many
  firings into one COUNTED firing plus its extremal rows (§5.2's
  `aggregate`), which is a reduction, not a judgment. Nothing may drop a
  firing, and the facts TSV always carries every one.

---

## §2. Inputs, exactly

### §2.1 The report TSV

Produced by `report.render_tsv` (report.py:4065). Two parts.

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
| `floor_pattern` | R-FLOOR-2 — **a new key, precondition P-1 (§2.5)**, appended at the END of the header line (after `worst_other_core_busy`), so the known-key list at reporter v16 gains exactly this one key in exactly this position |

**The header's parse rule (corrected from v1.1, panel/manager cross-review
I-58 edit 1): the KNOWN-KEY split is NORMATIVE, not "equivalent" to a
regex-rejoin.** `; ` is NOT a sufficient delimiter: `x13_rules`'s own
value is built with `"; ".join(...)` (report.py:4084-4085) and three
committed reports carry a two-clause value, e.g. `x13_rules: v1.1-1.3 X13
(both samples quiet) on 14; v1.4 X13 (pre-flight + trial agreement) on
2`. A naive `split("; ")` produces a key-less fragment and shifts every
later key by one. `filters` contains `, ` and `=`; `worst_other_core_busy`
contains `%`, ` / ` and parentheses.

v1.1 offered two formulations and called them equivalent:

> (a) Split on `; ` and then RE-JOIN, with `; `, any fragment that does
> not match `^[a-z0-9_]+: `.
> (b) Split only before a known key.

**They are not equivalent — they diverge in both directions, and each
divergence is a real, reachable case, not a corner case:**

1. **A newer reporter's header gains a key `interpret` does not know
   about yet** (exactly the position `floor_pattern` is in at this
   revision, before P-1 lands): form (a) keeps it as its own fragment,
   because it does not match `^[a-z0-9_]+: `'s failure mode the way a
   *value* does — it IS a `key: value` shaped fragment, so (a) leaves it
   separate. Form (b), consulting a known-key list that has not yet been
   updated, does not recognise the new key and silently RE-JOINS it into
   the PREVIOUS key's value.
2. **A future value contains `word: `-shaped text** (nothing in the
   corpus today does, but nothing rules it out — a future `filters`
   value quoting a selector like `pattern: foo`, say). Form (a) sees a
   fragment matching `^[a-z0-9_]+: ` and wrongly treats it as a new key,
   splitting a single value in two. Form (b), which only ever splits
   before a name already on its list, correctly leaves it joined into
   the value it belongs to.

**Ruling: form (b), the known-key split, is normative.** It fails safe on
an unrecognised VALUE shape (case 2, which is the more likely future
defect — this project's own values already carry `,`, `=`, `%`, `/` and
parentheses), and its remaining exposure (case 1, a brand-new key) is
bounded by construction: the known-key list is obtained at CHECK time by
running `report --format tsv` over `check-interpret`'s own fixture store
and reading the emitted keys back out (the same motion `check-report`
already makes), so a reporter bump that adds a header key and an
`interpret`/`catalogue` bump that recognises it are the same commit's
concern (§3.3, §8's regeneration rule) — the list cannot silently go
stale the way a hand-maintained one could. Form (a)'s regex-rejoin is
demoted to a HEURISTIC NOTE, useful only as a human's sanity check when
reading a header by eye, never as `interpret`'s own algorithm:

> Heuristic only, not what `interpret` runs: split on `; ` and then
> re-join, with `; `, any fragment that does not match `^[a-z0-9_]+: `.
> A human eyeballing a header this way will occasionally see it disagree
> with `interpret`'s own known-key split — that disagreement is case 2
> above, not a bug in either.

The known-key list is not retyped from this note. §8(1) obtains it as
described above — because the header keys are an f-string block at
report.py:4068-4091 and are the one part of the input that cannot be
read out of `render_tsv`'s `header` list.

**Data rows**, an 18-column table (report.py:4092-4094):

```
section  pattern  subject_or_na  regime_or_na  form  fact  testee  status
tier  rank_or_na  metric  value  n  pass_rate  n_gave_up  n_wrong
gave_up_summary  delta_verdict
```

`section` ∈ `record | rank | excluded | not_ranked | scratch |
did_not_compile | compile | compile_stamp`.

Four shapes matter and are easy to get wrong:

- a `record` row carries the RECORD ID in the `testee` column, **the
  agreement string in `value`, paired with `metric = agreement`**, and
  the after-sample failure in `delta_verdict`'s slot (report.py:4104-4107).
  `gave_up_summary` is EMPTY on every `record` row.
  *(Corrected from v1, panel B1: v1's §2.1 said the agreement string sat
  in `gave_up_summary`'s slot, copying report.py's own stale comment at
  4097-4099 rather than the emitted row; v1's §4.1 Inputs line was
  already right. Verified against data: every `record` row of every
  committed report reads `$11=agreement`, `$12=n/a (v1.x)` or an
  `agree`/`disagree` line, `$17=""`. R-STATUS-9's fixture is built by
  projecting a REAL `record` row, §8(4), so the column position is
  pinned by data and not by this paragraph.)*
- a `rank` row is emitted SIX TIMES per (group, testee, form), once per
  `metric` ∈ `median_ns | min_ns | max_ns | stddev_ns |
  ratio_vs_baseline | ratio_vs_best` (report.py:4146-4153). Every rule
  below states which metric row it reads.
- **`delta_verdict` is a `; `-separated LIST of independent clauses, not
  a token.** `_cross_pin_info` (report.py:2520-2535) builds a compound
  deliberately: "A selection change EXPLAINS a 'now measured' rather
  than replacing it." The reachable clause shapes are exactly
  `unchanged (within spread)`, `faster ×N.NN`, `slower ×N.NN`
  (`_cross_pin_verdict`), `selection changed (<prev> → <new>)`, and
  `now measured (was: <reason>)` with `<reason>` ∈ `gave-up | wrong |
  gave-up+wrong | no-data | other` (`_set_cell_failure_reason`,
  report.py:2251-2264). Across the 42-file corpus the value space is
  `unchanged (within spread)` (9,900 rows), `faster ×N` (5,928),
  `slower ×N` (2,280), `selection changed (vm → dfa); now measured (was:
  gave-up)` (24), `selection changed (vm → dfa)` (12), `selection
  changed (dfa → vm)` (6). **Every R-DELTA rule matches its anchor
  against each CLAUSE, never against the whole string.**
  *(Corrected from v1, panel B3: v1 anchored R-DELTA-3 at
  `^now measured \(was: `, which matches nothing in the corpus, while
  §10 A.2 required it to fire on four cells. Under the clause rule it
  fires on those four. A bare `now measured (…)` verdict is reachable
  (report.py:2523, no selection change) and simply has not occurred yet.)*
- **`subject_or_na` has two spellings of "absent"** (panel build #16):
  `rank`, `excluded`, `not_ranked`, `scratch` and `did_not_compile` rows
  carry the literal `(set)` at set grain (report.py:4115); `record`,
  `compile` and `compile_stamp` rows carry the empty string. A rule that
  keys on emptiness to mean "not subject-scoped" is wrong for half the
  sections.

One more shape a rule must not assume: the `excluded` section is
selected by `r.expectation_failing or not n_timed` (report.py:4123-4124),
**not** by `pass_rate < 1`. In practice every committed excluded row has
`pass_rate < 1`, but the predicate is the reporter's, and
`expectation_failing` covers wrong answers, give-ups, crashes and
timed-out subjects, of which only the first two have count columns
(panel D19, build #11).

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

**Which index the tool reads (panel B8).** For a human run,
`--index store/index.tsv` (the default) — the live index, which is the
whole point of R-STATUS-2. For `make check-interpret`'s pinned golden
comparison, a FROZEN snapshot committed beside the golden files
(`catalogue/golden/index@<date>.tsv`), never the live index. §8(2) states
the consequences of that split in full.

### §2.3 The predictions file (optional third input)

See §6. Absent → every R-PRED rule and R-DELTA-4 report
`did-not-fire: input-absent`.

### §2.4 What `interpret` does NOT read

The markdown renders, `bench/*/expectations.tsv`, `bench/*/subbench.toml`,
any record JSONL, any engine, any pcrec source. The reporter already made
the reduction; a second reduction here would be a second implementation
of arithmetic this project keeps in exactly one place (`pcrecbench/reduce.py`'s
own header states the rule).

*(Corrected from v1: v1 named `bench/<dir>/subbench.toml` as "the one
place `interpret` reads outside its two inputs", for R-FLOOR-2's floor
pattern. The panel measured that this re-creates KB-2 exactly — the
reporter deliberately stopped importing `pcrecbench.subbench` because a
record measured on another box or against an older sub-bench version has
no matching checkout beside it, and the skew is live today: acceptance
Report A is `email-specimen@0.1` while `bench/email/` is at `@0.2`.
Because `role` defaults silently to `member`, the failure would be a
silent `no-matching-rows`. The exception is REMOVED and replaced by
precondition P-1 below. `interpret` now really does have exactly the two
inputs this section claims.)*

The one derived quantity `interpret` computes over rows the TSV already
carries — an ORDERING of patterns within one (testee, regime), used by
R-PRED for a cross-pattern prediction (§6.3) — is a reduction of numbers
the reporter already reduced, not a second reduction of records, and is
declared as such in the catalogue's `arith` block.

### §2.5 PRECONDITIONS: two reporter changes v1 depends on

Both are `REPORTER_VERSION` bumps with a full regeneration of committed
reports — a motion this project has executed thirteen times — and both
ride in **one** reporter change, landed before the implementation lane
opens. Neither is optional; each closes a rule that would otherwise be
silently wrong.

**P-1 — `floor_pattern: <pattern_id|none>` in the header comment**
(panel S8 / B-tier ruling on Q1; one line in the block at
report.py:4068-4091). The value already exists in the reporter:
`floor_pattern_by_sb` is computed at report.py:2927/2989 from the
RECORDS' own `patterns[].role` (schema v1.3, [B15]) — so the key carries
the floor pattern *of the records in this report*, which is the only
correct answer and the one `bench/` cannot give. On a population of
pre-1.3 records (Report A) the value is `none`, and R-FLOOR-2 then
reports `no-matching-rows (floor_pattern: none)` — true, and not a
silent miss.

**P-2 — the give-up smallest subject as its own metric rows** (panel S4,
promoting Q8's option (b) from recommendation to precondition). Today the
smallest give-up subject and its byte count exist only inside
`_gave_up_cell_summary`'s rendering, `<code>×<n> (smallest: <id>, <n> B)`,
one `; `-joined clause per code (report.py:1216-1222) — and the parse is
harder than it looks: `<bytes>` may be `?`, and for a non-pcrec engine
`<code>` is `reduce.giveup_code`'s FALLBACK, "the raw diagnostic
(truncated to 64 chars)", which may itself contain `;`, `,` and
parentheses. No committed report exercises that fallback, so **the first
pcre2 give-up ever recorded is the day a parse would break silently.**

The reporter therefore emits, beside each `excluded` row, ONE EXTRA ROW
PER GIVE-UP CODE in `render_tsv`'s own idiom:

```
excluded  <pattern>  <smallest_subject_id>  <regime>  <form>  <fact>
          <testee>  <status>  <tier>  ""  giveup_smallest  <code>
          <bytes|"">  ""  <n_subjects_with_this_code>  ""  ""  ""
```

*Deliberate refinement of the disposition, flagged:* the panel's wording
was "the reporter emits `smallest_giveup_subject`/`_bytes` columns". Two
new COLUMNS would take the layout from 18 to 20 and move every consumer's
column index; and because "smallest" is per code, two columns cannot
carry a two-code cell without re-introducing a `; `-joined value — the
exact defect being closed. An extra metric row is `render_tsv`'s existing
extension idiom (`rank` already emits six rows per cell; `compile` emits
`jitter` and the size metrics as their own rows), keeps the 18-column
contract, and carries one code per row. `gave_up_summary` stays exactly as
it is, for the human render.

**Recorded as follow-ups, NOT preconditions** (each would remove a
derivation, none is required for a rule to be correct):

- `baseline_is: reference|best` per ranking group (panel B6). Not needed:
  the same fact is derivable EXACTLY from the TSV — the reporter falls
  back to the best row iff no *rankable* reference row exists in the
  group (report.py:4133-4136), and a rankable row is precisely a `rank`
  row, so "no `rank` row in this group whose testee id satisfies
  `_is_reference`" is the fallback's own condition, not an approximation.
  R-STATUS-13 states it and R-RANK-1 is guarded by it (§4.1, §4.3).
- an exclusion-cause column (panel build #11). `_set_cell_failure_reason`
  (report.py:2251-2264) already computes `gave-up | wrong | gave-up+wrong
  | no-data | other` for the `now measured (was: …)` verdict and throws
  it away for the excluded row. Until it is emitted, R-STATUS-3's
  template says only what the columns support (§4.1).
- `<name>.subject-grain.tsv` for every report group, which would let
  R-BUCKET-DOMINATED fire (Q2, ruled: `input-absent` until then).
- an `expectation_detail` slot that would make R-BUCKET-KB reachable
  (§4.7, B4 — **not designed here**, and the reason is stated there).

---

## §3. The rule catalogue: file, format, versioning

### §3.1 Where it lives

```
catalogue/
  rules.toml        the catalogue
  CLAUDE.md         purpose + files (this project's convention)
  fixtures/
    gen.py          the fixture generator (§8(4))
    <RULE>__<case>/ one directory per fixture: source.toml + the projected files
  golden/
    <report-basename>.facts.tsv     the pinned facts for the §10 reports
    index@<date>.tsv                the frozen index those facts were derived against
```

At the repository ROOT, beside `schema/`, deliberately: the catalogue is
a *format* with a version, a validator and a fixture corpus, the same
shape as `schema/`, and it is read by two consumers (`interpret` and
`make check-interpret`). Putting it under `pcrecbench/` would make it
look like implementation detail of one module.

TOML because BD4 fixes python ≥ 3.11 and `tomllib` is stdlib; the
project already reads TOML at runtime in two places (`subbench.toml` via
`pcrecbench/subbench.py` and `report.py`; `testees/*/configs.toml` via
`pcrecbench/adapters.py`), and multi-line strings make a threshold's
SOURCE citable inline instead of in a comment. *(Corrected from v1,
panel D18: v1 said "three places" and counted `pyproject.toml`, which is
consumed by build tooling only and never read at runtime.)*

### §3.2 The shape of a rule

```toml
catalogue_version = "1.0"
# Every bump regenerates every committed sidecar in the same commit.

[[pin_order]]                        # see R-BUCKET-SPAN, §4.7
engine = "pcrec"
pins   = ["8da6120", "692c2e8", "35e1ab1", "36d5963", "96e44c2",
          "263b013", "a7e0bdf", "1989c62", "288d505", "334fd10e",
          "d34c9131"]

[[rule]]
id            = "R-DELTA-1"
title         = "cross-pin Δ outside spread"
class         = "delta"
since         = "1.0"
grain         = ["set"]              # MANDATORY on every rule (§3.2.1)
aggregate     = ["regime", "config", "direction"]   # §5.2; [] = one bullet per firing
inputs        = [                    # EXACT columns, checked at load
  "report:rank?metric=median_ns.{pattern,regime_or_na,form,testee,rank_or_na,value,delta_verdict}",
  "report:rank?metric=stddev_ns.value",
]
predicate     = """
Any `; `-separated clause of `delta_verdict` matching `^(faster|slower) ×`.
"""
threshold     = "none of this rule's own"
threshold_src = """
report.py:2234 `_cross_pin_verdict` ([B9] R8): `unchanged (within
spread)` iff |median_new - median_old| <= 2 * max(stddev_old,
stddev_new); otherwise faster/slower ×N.NN. This rule adds NO threshold
of its own -- it reads the verdict clause the reporter already computed
and printed, so the interpreter and the report can never disagree about
what "beyond spread" means.
"""
slots         = ["pattern", "regime", "form", "testee", "verdict", "median_ns", "config", "direction", "ratio"]
arith         = [                    # §7.2's declared derivations (added, cross-review I-58 edit 4)
  "config: testee_id with version_slug removed -- see §7.2's testee-id decomposition row, same split minus the version_slug field",
  "direction: the matched clause's own leading token ('faster' or 'slower'), copied verbatim from the predicate's own match",
  "ratio: the matched clause's own trailing '×N.NN', parsed as a float, copied verbatim from the predicate's own match",
]
extremal      = "ratio"              # §5.2; overrides the default (first numeric slot, median_ns) -- the biggest MOVER, not the largest-median cell
template      = "{pattern} / {regime} / {form} / `{testee}`: the reporter's cross-pin Δ reads **{verdict}** (median {median_ns} ns)."
no_fire       = "no rank row carries a faster/slower clause"
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
columns it touches, enforced by handing each rule function a view that
raises on an undeclared column (§3.3, §7.2).

Fields every rule carries: `id`, `title`, `class`, `since`, `grain`,
`aggregate`, `inputs`, `predicate`, `threshold`, `threshold_src`,
`slots`, `arith`, `template`, `no_fire`, `links`, `example`. One field is
OPTIONAL and declared only to override its default: `extremal` — which
slot §5.2's aggregation renders as the group's extremal firing; a rule
that omits it gets the default, the rule's first numeric slot (§5.2).

#### §3.2.1 `grain` is mandatory (panel S7)

`grain` was declared on the R-DELTA class only in v1. It matters
elsewhere and silently: `_n_and_pass_rate` (report.py:3196-3200) returns
`n_subjects` at set grain and `n_trials` at subject grain **into the same
`n` column**, so R-FLOOR-2's declared `median_ns / n` is a per-subject
mean at set grain and a meaningless number at subject grain — one that
still computes. And `delta_verdict` is populated only at set grain
(report.py:4143-4145), so every rule reading it is set-only.

`grain` is therefore required on every `[[rule]]`, checked at load by
§8(1). Set-only in v1: all four R-DELTA, R-RANK-1, R-ARM-1, R-FLOOR-2,
R-STATUS-13, R-BUCKET-FORM/VSBEST/SPAN, all four R-PRED. Subject-grain
only: R-BUCKET-DOMINATED. Both grains: the remaining R-STATUS rules,
R-FLOOR-1 and R-FLOOR-3 (compile rows are grain-independent).

#### §3.2.2 The `inputs` grammar and the view contract (panel S5)

Stated here, not left to the implementation lane, because it is the one
part of "module layout" that two competent lanes would build differently
while each passed its own tests — so it is a contract, not a detail.

```
inputs entry := <file> ":" <section> [ "?" <col> "=" <val> { "&" <col> "=" <val> } ]
                        [ "." <column> | "." "{" <column> { "," <column> } "}" ]
<file>       := "report" | "index"
<section>    := a `section` value, or "header" for the comment line
```

Examples, all from the rules below:

```
report:rank?metric=median_ns.{pattern,regime_or_na,testee,value}
report:header.floor_pattern
report:excluded?metric=giveup_smallest.{pattern,subject_or_na,value,n}
index.{subbench,version,testee_id,machine_id,timestamp,status}
```

The view handed to a rule function exposes exactly three methods, each
raising `UndeclaredColumn` on any key outside that rule's `inputs`:

```python
view.rows(section, **eq) -> Sequence[Mapping]   # report rows, filtered
view.header(key)         -> str                 # one header value
view.index_rows(**eq)    -> Sequence[Mapping]   # store/index.tsv rows
```

`rows()` returns a table, not a row: at least eight rules are
group-scoped or cross-row (R-STATUS-12 joins across patterns; R-RANK-1
and R-ARM-1 pair across testees; R-STATUS-13, R-BUCKET-FORM and
R-BUCKET-VSBEST count over a group's rows; R-FLOOR-2 reads a different
pattern's cell), and a row-shaped view cannot express them.

**The strength of the guarantee, stated honestly** (panel build #9(a)):
a raising view enforces "this rule did not touch an undeclared column
*on the paths its fixtures exercised*". With one sabotage, one control
and the golden reports per rule that is a handful of paths — a good
check, not a proof. §3.2 says "checked", not "guaranteed".

### §3.3 Versioning, and what a bump means for old sidecars

`catalogue_version` is `MAJOR.MINOR`, the same discipline as the record
schema (docs/design/record_schema.md §4) and for the same reason.

- **MINOR** — a rule added; a template's wording changed under §8(6)'s
  review gate; a link added; an `example` refreshed; a `[[pin_order]]`
  entry appended at a re-pin. Old inputs still produce the same *facts*;
  only the rendering moves.
- **MAJOR** — a rule's PREDICATE or THRESHOLD changes, a rule is
  removed, `inputs` change in a way that reads a different column, **or a
  signature is registered with R-BUCKET-KB**. A sidecar stamped at an
  earlier MAJOR is no longer derivable from its inputs under the current
  catalogue.

*(Signature registration is MAJOR, corrected from v1, panel B4: v1 made
it MINOR — "adding a newly-filed KB is a MINOR catalogue bump and no code
change" — which put the single most interpretive object in the design
behind the lowest review bar it defines. The inversion is backwards: the
more a rule asserts, the more review it should cost.)*

A retired rule keeps its `[[rule]]` block with `retired_in = "2.0"` and
its `id` is never reused — the record schema's own reserved-id
discipline, and the reason a sidecar from 2026-09 can still be read in
2027. (An id that never shipped is not "retired": v1's draft R-RANK-2 is
simply absent from v1.0 — see §4.3.)

**The bump rule that makes this safe:** a committed sidecar is
*generated*, and `make check-interpret` re-renders every committed
`reports/*.interpretation.md` from its recorded inputs and requires byte
equality. So a catalogue bump that changes any rendering forces
regeneration of every affected sidecar **in the same commit**. This is
exactly the precedent `REPORTER_VERSION` set (pcrecbench/CLAUDE.md, [B14]
R10: "bump whenever rendering changes, so two reports are never mistaken
for each other"), applied one layer up. A stale sidecar is a `make
check` failure, not a thing a reader has to notice.

Two other things also move a sidecar, and §8(2) states who owns each: a
**reporter** bump (which regenerates the reports the sidecars are
derived from) and a **records-only** commit (which must not move
anything, and is why the golden reads a frozen index).

---

## §4. The rules

Seven classes: the six the plan row named, plus **R-ARM** (§4.4), which
the r4 panel required because the charter's own blinded acceptance test
names a finding — the `vm-in` result — that no cross-pin or status-shaped
rule can reach (panel B7/F6).

Every threshold below is either (a) a value `report.py` or `reduce.py`
already computed and printed, read as a string, or (b) a comparison of
two measured numbers *from the same report*. There is no tuned constant
introduced by this design. Where a boundary is definitional (`≥ 1.0`,
"crosses 1.0") it is named as definitional, not measured, and said so out
loud.

**Thirty-one rules.** R-STATUS 13, R-DELTA 4, R-RANK 1, R-ARM 1,
R-FLOOR 3, R-PRED 4, R-BUCKET 5.

**Note on "group".** Every rule below that says *ranking group* means
`_ranking_groups`'s own key (report.py:3161-3176): **`(subbench,
pattern, regime)` at set grain**, `(subbench, pattern, subject, regime)`
at subject grain. `form` is DELIBERATELY NOT in the key — the docstring
says so in capitals, reversing the module's own first cut on a
2026-08-25 manager fix request, precisely so a compliance regime's pcrec
`whole-subject` rows rank against libpcre2's `plain` rows. A cross-PIN
pair, by contrast, IS keyed on form (`_cross_pin_info` looks up
`rd.set_cells[(sb, prev_tid, pattern, regime, form)]`, report.py:2481),
and so is an ARM pair (§4.4), because comparing two different artifacts
would confound the comparison. Where this note says "group" it means the
first; where it means the second it says "cell" or "pair".

*(Corrected from v1, panel B5 — the highest-value fix in the note. v1's
§4.3 defined the ranking group as `(pattern, regime, form)`, which made
R-BUCKET-FORM unsatisfiable by construction (a single-form group can
never carry both facts) and inflated R-STATUS-13's population from 891
of 2,514 groups (35 %) to 1,323 of 2,946 (45 %). v1's §4.6 described the
group correctly; the two sections contradicted each other. Every rule
below has been re-derived from `_ranking_groups` and its worked examples
re-verified against the corrected key.)*

### §4.1 Class R-STATUS — status and population caveats

| id | grain | aggregate | fires on |
|---|---|---|---|
| R-STATUS-1 | both | `["status"]` | an INCLUDED record whose `status` ≠ `measured` |
| R-STATUS-2 | both | `["status"]` | a record in `store/index.tsv` for this report's (subbench, version, machine) that the query did NOT include, whose status ≠ `measured` |
| R-STATUS-3 | both | `[]` | an `excluded` section row **whose `metric` is `pass_rate`** (§4.1's cross-review note below) |
| R-STATUS-4 | both | `["testee"]` | a `did_not_compile` section row (deduplicated to the distinct (pattern, testee) set) |
| R-STATUS-5 | both | `[]` | header `superseded` / `newer_not_measured` / `excluded_invalid` > 0 |
| R-STATUS-6 | both | `[]` | header `schema_versions` names more than one version |
| R-STATUS-7 | both | `[]` | header `mixed_x13: True` |
| R-STATUS-8 | both | `[]` | header `worst_other_core_busy` present and non-`n/a` |
| R-STATUS-9 | both | `[]` | a `record` row whose agreement string starts **`disagree`** |
| R-STATUS-10 | both | `[]` | a `record` row whose `delta_verdict` slot carries `after: …` |
| R-STATUS-11 | both | `["testee"]` | a `scratch` section row |
| R-STATUS-12 | set | `[]` | one subject giving up under DIFFERENT codes on two patterns, one testee, one regime |
| R-STATUS-13 | set | `[]` | a ranking group with no rankable reference arm — `ratio_vs_baseline` is a ratio to the group's BEST row, not to the reference |

**R-STATUS-9, corrected from v1 (panel B2).** v1 fired on an agreement
string starting `disagree` **or `n/a`**, while v1's §9.2 asserted the
rule did not fire on Report A "because every record reads `agree` or
`n/a (v1.x)`" — and all nine of Report A's records read exactly
`n/a (v1.1)`/`n/a (v1.2)`, so the two statements could not both be true.
The ruling: **only `disagree` fires R-STATUS-9.** The five reachable
strings, enumerated in `threshold_src` with their sources, are:

| string | produced by | what it means | who reports it |
|---|---|---|---|
| `agree (N of N groups; …)` | `agreement_line`, reduce.py:372-376 | the v1.4 rule judged and agreed | nobody — the normal case |
| `agree 0/0 groups -- nothing judged (N rows unjudged)` | reduce.py:371 | nothing was judgeable | R-STATUS-3's own give-up/wrong facts already say why |
| `disagree (N of N groups; worst … d=N of n=N; …)` | reduce.py:365-369 | the trials did not agree | **R-STATUS-9** |
| `n/a (N trials)` | reduce.py:359, verdict `n/a-trials` | fewer than 5 trials, or an even count — a short or scratch run | R-STATUS-11 (scratch) where it applies; otherwise provenance |
| `n/a (v<schema>)` | `_agreement_display`, report.py:2788-2792 | the record PREDATES the block (schema < 1.4) | **R-STATUS-6**, as provenance about the population's age |

`n/a (v<schema>)` is provenance about a record's AGE, not a finding about
its trials, so it belongs with R-STATUS-6's mixed-schema-population fact
and is rendered there. The v1.4 rule's constants (`k = 1.5, d_min = 2,
share_c = 3, N ≥ 5 and odd`, reduce.py:246-250, with "and odd" stated in
the comment at 241-242) were MEASURED over the store's 68 records at
[B20]; the census files are under `docs/dev/measurements/`. The
interpreter re-derives nothing.

**R-STATUS-12** is the second of the two interpreter rule facts the
journal names (dev_journal.md, second session part 7;
`feedback_…-repin-v2.md` §2's last bullet). Inputs, under precondition
P-2: `report:excluded?metric=giveup_smallest.{pattern,subject_or_na,
regime_or_na,form,testee,value,n}` — the subject id is a COLUMN
(`subject_or_na`), the code is `value`, the byte count is `n`. No parse.

**R-STATUS-13** was v1's R-RANK-3, moved here (panel F11 / the r4
worth-noting list): it is a population caveat, not a rank flip, and its
real job is to gate R-RANK-1. Its predicate is exact, not an
approximation: the reporter's fallback triggers iff no *rankable*
reference row exists in the group (report.py:4133-4136), and a rankable
row is exactly a `rank` row, so the rule is "this group has no `rank` row
whose testee id satisfies `_is_reference`" — `base.startswith("libpcre2_")
and "_interp-" in base`, after stripping a possible `@<timestamp>`
suffix (report.py:3153-3159), copied verbatim as a declared
decomposition (§7.2). Population: **891 of the corpus's 2,514 ranking
groups**, concentrated in altwide, where libpcre2 refuses at its own
compiled-size ceiling.

**R-STATUS-3 vs precondition P-2, resolved (cross-review I-58 edit 2).**
§9.2's specimen pins 13 firings on Report A's excluded section, but P-2
(§2.5) adds `metric=giveup_smallest` rows INTO the same `excluded`
section, one extra row per give-up code beside each base row that has a
give-up. R-STATUS-3's predicate as v1.1 stated it — "an excluded section
row" — declared no `inputs` column named `metric` or `value`, so under
§3.2.2's raising view it could not even *see* the new rows' `metric`
column to filter them out without an `UndeclaredColumn` error, and left
unfiltered it would double-fire once per code on any cell that has one.
**Fact, verified against the committed corpus for this revision:** every
base `excluded` row today carries `metric = pass_rate` —
`awk -F'\t' '$1=="excluded"' reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv | head -1`
reads `excluded  factored  (set)  large-subject-throughput  plain  same
program  libpcre2_10.46_jit-caps-simdna  measured  pinned    pass_rate
0.6667  3  0.6667  0  0  0` — column 11 (`metric`) is `pass_rate` on
every one of the 13 rows
(`awk -F'\t' '$1=="excluded"' … | wc -l` → 13, confirmed by re-running
for this revision). **Fix: `metric` is now a declared input, and the
predicate is scoped to the base row, `metric = pass_rate`.** P-2's
`giveup_smallest` rows are declared as R-STATUS-12's inputs only (§2.5,
already the case) and are never matched by R-STATUS-3. Report A's count
is unaffected by this fix today (the corpus predates P-2, so every
excluded row already reads `metric = pass_rate` and the scoped predicate
still selects all 13); the fix matters the moment P-2 lands and the
report is regenerated with the extra rows alongside them.

**The same hazard, checked against every other reader of the `excluded`
section, per I-58's ask.** R-STATUS-12 already declares
`report:excluded?metric=giveup_smallest…` (below) — scoped correctly
from v1.1, no change needed. No R-BUCKET rule (§4.7) reads the `excluded`
section: R-BUCKET-FORM reads only *rankable* (`rank`) rows by its own
predicate (§4.1 note above §4.7). R-PRED-3 (§4.6) tests only whether a
predicted cell's `section` value is `excluded` (a presence check across
whichever rows match its selector, never a read of `metric`, `pass_rate`
or the give-up columns), so an extra `giveup_smallest` row beside a base
row changes nothing it reads — no hazard there. §9.2's "13 firings" and
§10 A.3's "all thirteen excluded cells" (Report A) and §10 C.2's
"23 excluded cells" (Report C) all describe the scoped, `metric =
pass_rate` count, and are unchanged by this fix, because the corpus they
describe predates P-2.

**Inputs.** R-STATUS-1: `report:record.testee` joined to `index.status`.
R-STATUS-2: `index.{subbench,version,machine_id,status,testee_id,
timestamp}` minus the report's `record` rows. R-STATUS-3:
`report:excluded?metric=pass_rate.{pattern,regime_or_na,form,testee,
pass_rate,n_gave_up,n_wrong,gave_up_summary}`. R-STATUS-4:
`report:did_not_compile.{pattern,testee,gave_up_summary}` (the
diagnostic lives in `gave_up_summary` — report.py:4172).
R-STATUS-9/10: `report:record.{testee,metric,value,delta_verdict}`.
R-STATUS-13: `report:rank?metric=median_ns.{pattern,regime_or_na,testee}`.

**Templates** (one per rule; slots in braces; every clause is a slot or
is definitional — §7.1):

```
R-STATUS-1  "`{record_id}` (testee `{testee}`) is included with status
             **{status}**."
R-STATUS-2  "`{record_id}` (testee `{testee}`, {timestamp}) is in
             store/index.tsv for {subbench}@{version} on {machine} with
             status **{status}** and is NOT in this report's
             population."
R-STATUS-3  "{pattern} / {regime} / {form} / `{testee}` is EXCLUDED
             from ranking: pass-rate {pass_rate}; {n_wrong} wrong
             answer(s); {n_gave_up} give-up trial(s); give-up summary
             {gave_up_summary}. (`n_gave_up` counts TRIALS; a `×N` in
             the summary counts SUBJECTS.)"
R-STATUS-4  "{pattern} / `{testee}`: did-not-compile — {diagnostic}"
R-STATUS-5  "The query drew {candidates} candidate record(s) and
             included {included}; {superseded} superseded,
             {newer_not_measured} newer-but-not-measured,
             {excluded_invalid} invalid."
R-STATUS-6  "This report's population spans record schema versions
             {schema_versions}; {n_pre_14} of {n_records} record(s)
             predate the v1.4 trial-agreement block and read
             `n/a (v<schema>)` for agreement."
R-STATUS-7  "The population mixes X13 rule revisions: {x13_rules}."
R-STATUS-8  "The busiest other core during a measured window read
             {worst_other_core_busy}."
R-STATUS-9  "`{record_id}`: trial agreement reads {agreement}."
R-STATUS-10 "`{record_id}`: the after-sample failed — {after}."
             links = [gate_shape_v14.md, record_schema.md §6.9]
R-STATUS-11 "{pattern} / {regime} / {form} / `{testee}` is a SCRATCH-tier
             row and is not in the ranking."
R-STATUS-12 "Subject `{subject}` ({subject_bytes} B) gives up as
             **{code_a}** on {pattern_a} and **{code_b}** on
             {pattern_b}, on `{testee}` in {regime}."
             links = [feedback_pcrecdev1_2026-08-25-repin-v2.md §2]
R-STATUS-13 "{pattern} / {regime}: no reference arm is rankable in this
             group, so `ratio_vs_baseline` is a ratio to the group's
             fastest row (`{best_testee}`), not to the reference arm.
             R-RANK-1 does not fire in this group."
```

Two template changes are worth naming, because both were opinions
hiding in fixed prose (panel B11/F1):

- **R-STATUS-12** rendered, in v1, "*: a different budget binds on the
  two spellings*" — a mechanism claim, exactly what §1.1 forbids,
  asserted in template voice with no link. It is now a `links` entry to
  `feedback_pcrecdev1_2026-08-25-repin-v2.md` §2, where a human already
  committed that reading, and the renderer appends the link.
- **R-STATUS-3** rendered, in v1, "{n_wrong} wrong answer(s),
  {n_gave_up} give-up trial(s)" and stopped — which on Report A's
  `factored / large-subject-throughput / plain /
  libpcre2_10.46_jit-caps-simdna` row (pass-rate 0.6667, `n_wrong` 0,
  `n_gave_up` 0, `gave_up_summary` `0`) renders a sentence naming no
  cause at all, on a row whose cause the TSV genuinely does not carry
  (panel build #11, which the consolidated review did not carry as a
  numbered item — applied here under B11's authority and flagged in the
  lane report). The template now names the columns it has and stops
  short of implying they explain the exclusion; the exclusion-cause
  column is a recorded follow-up (§2.5).

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
record of the same testee at 22:16:51Z / 22:24:22Z / 22:28:40Z under
[B9] R2's newest-measured rule. R-STATUS-2 fires three times and names
them; a reader who wants to know whether the re-measure changed anything
now has the record ids to compare, which is exactly the question
`feedback_pcrecdev1_2026-08-25-repin-v2.md` §3 had to answer by hand.

**Worked example — R-STATUS-4**, against
`reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`: 172
`did_not_compile` rows reducing to 60 distinct (pattern, testee) pairs,
e.g. `pcrec_d34c9131_auto-caps-simdna | pcrec: module 'conditionals' is
enabled but (?(...) is not implemented yet (pattern offset 8)` on
pattern `cnd-group`. The reporter emits one row per group ([B12] R10);
the rule deduplicates to the pair, and its `aggregate = ["testee"]`
renders **four** firings (15 patterns each) rather than 60.

**Worked example — R-STATUS-13.** `reports/2026-09-05-altwide-0.2-…-after-334fd10e.tsv`
is where the 891 concentrate: libpcre2 refuses the wide rungs at its own
compiled-size ceiling, so every group above the wall ranks pcrec against
pcrec and `ratio_vs_baseline` silently becomes a ratio to the best pcrec
row. On Report A the rule fires **zero** times — all six ranking groups
carry the interp arm.

### §4.2 Class R-DELTA — cross-pin deltas beyond spread

| id | grain | aggregate | fires on a `delta_verdict` CLAUSE matching |
|---|---|---|---|
| R-DELTA-1 | set | `["regime","config","direction"]` | `^(faster\|slower) ×` |
| R-DELTA-2 | set | `["regime","config"]` | `^selection changed \(` |
| R-DELTA-3 | set | `["regime","config"]` | `^now measured \(was: ` |
| R-DELTA-4 | set | `["rule_id","regime"]` | a R-DELTA-1 / R-RANK-1 / R-ARM-1 / R-FLOOR-2 firing that no prediction's selector covers (§6) |

**Inputs.** `report:rank?metric=median_ns.{pattern,regime_or_na,form,
testee,rank_or_na,value,delta_verdict}` plus the same cell's
`metric=stddev_ns.value`. Set grain only — `delta_verdict` is computed
for `grain == "set"` alone (report.py:4143-4145) — so on a subject-grain
TSV all four report `did-not-fire: grain`.

**The `config` and `direction` aggregate keys are declared decompositions,
not raw columns (cross-review I-58 edit 4).** R-DELTA-1's table above
declares `aggregate = ["regime","config","direction"]`, and R-DELTA-2/3
declare `aggregate = ["regime","config"]`, but neither `config` nor
`direction` is a TSV column: `config` is `testee` with its `version_slug`
decomposed OUT (the testee-id split §7.2 already declares for R-RANK-1 /
R-ARM-1 / R-BUCKET-VSBEST / R-BUCKET-SPAN, minus the one field a
cross-pin pair is guaranteed to differ on), and `direction` is the
matched clause's own leading token (`faster` or `slower`). Both are now
declared, per rule, in each R-DELTA rule's `arith` field (§3.2's R-DELTA-1
example shows the exact wording) and in §7.2's decomposition table below
— the same firewall bookkeeping §7.2 already requires for every other
non-literal slot value, extended to cover these three rules' aggregation
keys. This is mechanical: no rule's PREDICATE or THRESHOLD changes, only
what is declared about how its aggregate key is computed.

**The clause rule.** Each rule matches its anchor against each `; `
-separated clause (§2.1). Consequences, all pinned by fixtures in §8(4):

- R-DELTA-1 and R-DELTA-2 **never co-fire on one cell**: `_cross_pin_info`
  returns either a selection-change verdict or a faster/slower one, never
  both (report.py:2533-2547).
- R-DELTA-2 and R-DELTA-3 **do co-fire**, on the compound
  `selection changed (vm → dfa); now measured (was: gave-up)` — 24 rows
  in the corpus, which is **four cells** (six metric rows each), and all
  four are in Report A. This is the co-firing fixture v1 lacked, and
  those four cells are §10 A.2.

**Threshold and source.** *None of its own.* R-DELTA-1's boundary is
`_cross_pin_verdict`'s (report.py:2234-2248): unchanged iff the median
difference is within `2 × max(stddev_old, stddev_new)`. The interpreter
reads the string. This is the single most important design decision in
the note: **the interpreter must never be able to disagree with the
report about whether something moved.** R-DELTA-2's source is [B16] R4
(`_cross_pin_info`, report.py:2447, the block commented at 2486): when
the two pins compiled different ENGINES the reporter refuses a ratio and
prints the selection change instead.

**R-DELTA-4, defined once (corrected from v1, panel D16 + S1).** v1
declared R-DELTA-4 and R-PRED-4 to be the same rule and then defined them
with different scopes — R-DELTA-4 over R-DELTA-1 firings, R-PRED-4 over
R-DELTA-1 / R-RANK-1 / R-FLOOR-2 firings — which §3.2's
one-function-per-id contract cannot satisfy. There is now exactly one
such rule, **R-DELTA-4**, with the wider scope (R-DELTA-1, R-RANK-1,
R-ARM-1, R-FLOOR-2), and R-PRED-4 is a different rule (the `partial`
verdict, §4.6). R-DELTA-4 is a cross-class rule and keeps its R-DELTA id
for continuity with the acceptance test and the sidecar heading.

**And it does not fire with no predictions file.** With none supplied,
"no prediction covers this cell" is universally true: on
`2026-09-06-bounded-0.3-…-after-d34c9131.tsv` R-DELTA-1 fires 202 times,
so R-DELTA-4 would fire 202 times, and "flag the UNPREDICTED Δ as loudly
as a regression" (`feedback_…-repin-v2.md` §2) degenerates into flagging
everything, which is flagging nothing. **R-DELTA-4 reports
`did-not-fire: input-absent` whenever no predictions file is supplied**,
like the rest of the prediction machinery. *(Corrected from v1, panel S1:
v1's §9.2 mock-up already did this and v1's §4.2 table contradicted it;
the table is what changed.)*

**Worked example — R-DELTA-1**, the case the charter was written from.
In `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`
the predicate matches **three** cells, not two:

- `factored` / short-subject-search / plain / `pcrec_692c2e8_vm-caps-simdna`,
  rank 5, median 69,537.5 ns, `faster ×1.19`;
- `orig` / match-compliance / whole-subject / `pcrec_692c2e8_vm-caps-simdna`,
  rank 2, median 80,227.6 ns, `faster ×1.26`;
- `orig` / match-compliance / whole-subject / `pcrec_692c2e8_auto-nocaps-simdna`,
  rank 4, median 233,982.1 ns, `faster ×1.00`.

The first two are the numbers `feedback_pcrecdev1_2026-08-25-repin-v2.md`
§2 calls "a cross-pin VM speedup with no attributed cause" and demands be
flagged "as loudly as a regression". The third is the rule being what it
is: a Δ is "beyond spread" when the spread is small, not when the ratio is
large, and v1's §9.2 and §10 A.5 both silently omitted it (panel D17). It
is rendered.

**Worked example — R-DELTA-2**: same report, six cells carry
`selection changed (vm → dfa)`, at ranks 1 and 2 in each of three regimes
on `auto-caps-simdna` and `auto-nocaps-simdna`. And in
`reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`,
`cls-upto-8192` / match-compliance / whole-subject /
`pcrec_d34c9131_auto-caps-simdna`, rank 3: `selection changed (dfa → vm)`.

**Worked example — R-DELTA-3**: Report A, **four** cells carry the
`now measured (was: gave-up)` clause — `factored` /
large-subject-throughput ranks 1 and 2, AND `factored` /
match-compliance / whole-subject ranks 1 and 2 — each as the second
clause of a compound with R-DELTA-2. *(Corrected from v1, panel D4: v1's
§10 A.2 said "the latter pair", i.e. two.)*

### §4.3 Class R-RANK — rank flips vs the reference arm

One rule. The reference arm is `report.py`'s own (`_is_reference`,
report.py:3153): a testee id beginning `libpcre2_` and containing
`_interp-`. It is the denominator of `ratio_vs_baseline`.

| id | grain | aggregate | fires on |
|---|---|---|---|
| R-RANK-1 | set | `["regime","config"]` | a cross-pin pair (same engine + config, different version slug, same form) whose `ratio_vs_baseline` values lie on opposite sides of 1.0 — **in a group where R-STATUS-13 does not fire** |

**The guard (panel B6/F5).** `report.py:4135` reads
`ref_ns = ref.median_ns if ref else (rankable[0][2].median_ns …)`, and
the TSV emits no marker distinguishing the two cases. Without the guard,
R-RANK-1's template asserts "the reference arm" about a number that is a
ratio to the group's fastest row, and the `{reference}` slot is either
unfillable (§7.1's strict renderer raises, exit 2 on a legitimate
committed report) or filled with the fallback row, which puts a falsehood
in template voice. All 69 current R-RANK-1 firings sit in groups that DO
have a reference arm, so this does not bite today; 891 of 2,514 groups
lack one, concentrated in altwide, where 40 of the 69 firings live. It is
one re-pin away.

**Inputs.** `report:rank?metric=ratio_vs_baseline.{pattern,regime_or_na,
form,testee,rank_or_na,value}`, plus `metric=median_ns.value` for the
template, plus the group's testee list for the R-STATUS-13 guard. The
cross-pin pair is formed by decomposing a pcrec testee id (§7.2's
declared decomposition, and the composition rule is
docs/design/record_schema.md §6.4) and grouping by `config` within a
ranking group **at one form**. Non-pcrec testees are unpinned and never
form a pair.

**Threshold and source.** The boundary is **1.0 on `ratio_vs_baseline`,
and it is DEFINITIONAL, not tuned**: the reference arm *is* 1.000× by
construction ([B9] R5), so "crossed the reference arm" is exactly "the
ratio crossed 1". Stated as definitional in `threshold_src` so a panel
can see there is no hidden constant.

**Template.**

```
R-RANK-1  "{pattern} / {regime} / {form} / config `{config}`: vs the
           reference arm `{reference}`, {old_pin} reads {old_ratio}× and
           {new_pin} reads {new_ratio}× — the cell crossed the reference
           arm between the two pins."
```

**Worked example.** `reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`,
`cls-upto-8192` / match-compliance / whole-subject, config
`auto-caps-simdna`: `pcrec_334fd10e` reads `ratio_vs_baseline` **1.788241**
(slower than `libpcre2_10.46_interp-caps-simdna`) and `pcrec_d34c9131`
reads **0.269358** (faster). R-RANK-1 fires. The *same cell* fires
R-DELTA-2 (`selection changed (dfa → vm)`) — and that co-firing is the
point: the rank flip is a fact, the selection change is a fact, and the
sentence "the flip is because the route changed" is a hypothesis the
interpreter does not write. A reader gets both facts adjacent and draws
it themselves in ten seconds. A second instance, on the older wave:
`reports/2026-08-29-loglines-0.1-budu-ryzen1600-repin-36d5963.tsv`,
`stack-frame` / short-subject-search / plain, config
`auto-caps-simdna`: 35e1ab1 **2.697803×** → 36d5963 **0.155111×**.

A census over the 42 committed report TSVs (run for this note, by the
predicate above, and independently reproduced by the r4 source critic to
the pair) finds R-RANK-1 firing in **9 of 42** files, on **69
(pattern, regime, form, config) pairs** in total, concentrated in
`2026-09-05-altwide-0.2-…-after-334fd10e.tsv` (40 pairs) and spread thin
elsewhere (bounded@0.2 after-a7e0bdf 7; bounded@0.3 after-d34c9131 7;
loglines 4 + 4; email@0.2 2; loglines@0.1 after-1989c62 2; bounded@0.1
repin-96e44c2 2; bounded@0.3 step2-after-288d505 1). A plausibility
check that the rule is neither dead nor universal.

**What is NOT in this class (corrected from v1).** v1 declared an
R-RANK-2 firing on "a cross-pin pair whose `rank_or_na` order contradicts
its own `delta_verdict` direction". It is **not in v1.0**, and the
argument for dropping rather than fixing it is short: `rank_or_na` is a
position among ALL testees in the group and `delta_verdict` compares ONE
testee against its own older pin, so there is no reason the two must
agree — a cell can get faster across a pin and still lose rank because a
third row got faster still. The predicate encodes an expectation that is
simply false in general, and "contradicts" is an interpretive word for an
ordinary consequence of a third row moving. It was also the only rule in
v1's §4 with no worked example, which is exactly what the charter's
example-per-rule discipline exists to catch (panel F11). A rule that
would need a *reason* to fire is a rule with an opinion; the honest
version of the question ("which rows moved, and where do they now rank")
is already answered by R-DELTA-1 and the `rank_or_na` column side by
side. Because R-RANK-2 never shipped, this is an absence, not a
retirement, and the id is available. v1's R-RANK-3 moved to R-STATUS-13.

### §4.4 Class R-ARM — same pin, one config token apart

**New in v1.1 (panel B7/F6).** Frank's blinded acceptance test names four
things catalogue v1 must find unprompted: the collapse, the three
inconclusive records, the give-ups, and **the `vm-in` result**. v1
covered three with real rules and conceded in §10 A.4 that it could not
reach the fourth, because all six classes are cross-pin or status-shaped
and the `vm-in` result is a SAME-PIN, cross-config comparison. So are
three of the five candidate rows in the grounding feedback document this
design cites — `[OPT-1]` (`vm-in` vs `vm`), `[OPT-2]`, `[OPT-C]` — and so
is every deny-flag testee this project has built (`-noedge`, `-noisland`,
`-noclsfold`, `-align64`, `-bigcap`, the `-clang` siblings): they exist
*only* to be read this way, and nothing in v1 read them.

| id | grain | aggregate | fires on |
|---|---|---|---|
| R-ARM-1 | set | `["arm_pair","regime"]` | two testee ids in one ranking group, **at the same engine and version slug**, **at the same form**, whose config decomposes to four tokens differing in exactly ONE, and whose medians differ by more than `2 × max(stddev_a, stddev_b)` |

**No new constant.** The threshold is the identical arithmetic
R-DELTA-1 inherits from `_cross_pin_verdict` (report.py:2234-2248),
applied WITHIN a report instead of across pins. It is the one place in
the catalogue where a rule computes rather than reads — because the
reporter computes no within-report spread comparison to read — so it is
declared in the rule's `arith` field in full, and it is the copied
threshold, not a chosen one. §4's "no tuned constant" property survives.

**The config decomposition**, declared (§7.2, slot kind 4), from
docs/design/record_schema.md §6.4 and verified against all 59 testee ids
in `store/index.tsv`:

```
testee_id = <engine> "_" <version_slug> "_" <config_slug> [ "_" <config_extra> ]
config_slug = <mode> "-" <caps> "-" <simd>        # parsed from the RIGHT:
                                                  # simd is the last hyphen field,
                                                  # caps the one before it,
                                                  # mode is everything before that
                                                  # (`vm-in` contains a hyphen)
tokens      = (mode, caps, simd, config_extra or "(none)")
```

Live examples of a one-token difference: `vm-in-caps-simdna` vs
`vm-caps-simdna` (mode); `auto-caps-simdna` vs `auto-nocaps-simdna`
(caps); `auto-caps-simdna` vs `auto-caps-simdna_noedge` (extra);
`auto-caps-simdna` vs `auto-caps-simdna_cc-clang` (extra);
`auto-caps-simdna` vs `vm-caps-simdna` (mode — the route arm).

**Two exclusions, both definitional.**

1. **Same form.** `form` is not in the ranking-group key, so a group can
   hold a pcrec `whole-subject` row beside a libpcre2 `plain` one. Two
   arms at different forms are two different artifacts and the comparison
   would confound; the pair requires equal `form`.
2. **Neither arm is the reference arm.** `ratio_vs_baseline` already
   prints exactly that comparison on every row of the report, so a rule
   that repeated it would be a census of a column. (This is arithmetic
   about what the report already carries, not a judgment about interest.)

**Template.**

```
R-ARM-1   "{pattern} / {regime} / {form}, pin {pin}: `{config_a}`
           {median_a} ns vs `{config_b}` {median_b} ns — ×{ratio}, beyond
           2 × max(stddev) = {spread} ns. The two arms differ in exactly
           one config token ({token_name}: {token_a} vs {token_b})."
```

**Worked example — this is §10 A.4, and it passes.**
`reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv`,
pin 692c2e8, mode token `vm-in` vs `vm`:

- `orig` / short-subject-search / plain: `vm-in-caps-simdna` **12,546.2 ns**
  (rank 6) vs `vm-caps-simdna` **28,996.9 ns** (rank 7) — **×2.31**,
  spread 862.2 ns;
- `orig` / match-compliance / whole-subject: `vm-in-caps-simdna`
  **62,732.3 ns** (rank 1) vs `vm-caps-simdna` **80,227.6 ns** (rank 2) —
  **×1.28**, spread 318.8 ns.

Those are precisely the two pairs `feedback_…-repin.md` §1 (a) records as
the `[OPT-1]` finding, and v1 could only reach them by asking a human to
look at two adjacent rank rows. The same rule also reaches the feedback's
row (c) — the DFA `\z` form against the VM form — as `orig` /
match-compliance / whole-subject, `vm-in-caps-simdna` 62,732.3 vs
`auto-caps-simdna` 234,082.1, **×3.73** (the feedback's "3.7× slower",
found by rule).

**Volume, measured, and why `aggregate` is mandatory here.** R-ARM-1
fires **14** times on Report A, **432** on Report B and **635** on
Report C. Aggregated by `["arm_pair", "regime"]` those become **8**,
**9** and **12** rendered firings, each carrying the count and its
extremal cell — and on Report A the extremal cell of
(`vm` vs `vm-in`, short-subject-search) is the ×2.31 pair above, so A.4
survives aggregation intact. Every one of the 635 rows is still in the
facts TSV.

### §4.5 Class R-FLOOR — ratios inside the timer floor

Two genuinely different floors, and conflating them is the mistake this
class exists to prevent.

| id | grain | aggregate | fires on |
|---|---|---|---|
| R-FLOOR-1 | both | `["testee"]` | a `compile` section row with `metric=jitter, value=timer-floor` |
| R-FLOOR-2 | set | `["regime","testee"]` | a ranked cell whose per-subject mean ≤ the floor pattern's per-subject mean for the same (regime, testee) |
| R-FLOOR-3 | both | `["testee"]` | a `compile` row whose `jitter` ratio is ≥ 1.0 (stddev at or above the median) |

**R-FLOOR-1.** Inputs: `report:compile?metric=jitter.{pattern,form,
testee,value}`. Threshold source: `_TIMER_FLOOR_NS = 20_000`
(report.py:1927), applied by `_jitter_flag` (report.py:2150-2165) — "20
microseconds, the clock's practical floor"; a compile cell whose `min_ns`
is under it reports `timer-floor` instead of a ratio "that is mostly
measuring the clock, not the compile". **The interpreter reads the token,
never the constant.** In `reports/2026-09-07-syntax-…-first-d34c9131.tsv`,
**190** compile rows carry `timer-floor` (95 on each libpcre2 arm)
against **644** carrying a real ratio (161 on each of the four pcrec
arms). *(Corrected from v1, panel D3: v1 printed "26/23/23/23", which are
the frequencies of the four most common ratio VALUES — 0.025, 0.032,
0.029, 0.018 — not a count of rows and not a per-testee split. Verified
by re-derivation for this revision.)* This is the exact complaint of
`feedback_…-repin-v2.md` §2 — "the interpretive rows have stddev ≈ median
(12.3 K vs 13.5 K)" — answered upstream by [B14] R5 and surfaced here.

**R-FLOOR-2.** Inputs: `report:rank?metric=median_ns.{pattern,
regime_or_na,form,testee,value,n}` and `report:header.floor_pattern`.
Arithmetic, declared in the catalogue's `arith` field and identical to
`_floor_mean_for` (report.py:2582-2595): `per_subject_mean = median_ns /
n`, computed for the cell and for the pattern named by the header key
`floor_pattern`, at the same (regime, testee). Set grain only — at
subject grain `n` is a trial count (§3.2.1). Threshold: **≤ 1.0 on the
ratio, definitional** — "at or below the set's own per-call overhead
control".

Worked example, `reports/2026-09-07-syntax-0.1-…-first-d34c9131.tsv`:
`anc-caret` / short-subject-search / `pcrec_d34c9131_vm-caps-simdna`,
rank 1, median 246.457657 ns over n = 42 subjects → **5.868 ns/subject**.
The `floor` pattern on the same testee and regime: median 800.098671 ns
over 42 → **19.050 ns/subject**. The ranked cell is **0.308×** the
floor control. R-FLOOR-2 fires: a between-testee ratio on this cell is a
ratio between two numbers both smaller than the set's own overhead
control. (The ledger's §8 reading — that `floor` = `#` is a *scan* cell
in this set and not a pure per-call floor — is the judgment; the rule
states the arithmetic and stops.)

On Report A the rule reports `no-matching-rows (floor_pattern: none)`:
the report's records are schema 1.1/1.2 and predate `patterns[].role`
entirely, so its only patterns are `factored` and `orig`. *(Corrected
from v1, panel D6: v1's §9.2 gave the reason as "no `role: floor`
pattern in email-specimen@0.1", which is false about the tree — the
`bench/email/` sidecar DOES declare one, at version 0.2. Reading that
sidecar to interpret an @0.1 report is the KB-2 mistake precondition P-1
removes.)*

**R-FLOOR-3.** Threshold `≥ 1.0`, definitional ("stddev at or above the
median"), reading the ratio `_jitter_flag` already printed. This is the
`interp compile-cost variance` row of `feedback_…-repin.md` §3 — the
seventh row, the one marked "UNCOVERED by any prediction": "12..109 µs
over 10 trials is timer jitter — the report should say so rather than
print a stddev larger than the median." *(Corrected from v1, panel D8:
v1 called it the eighth row; the eighth is `JIT absent on
factored/throughput (from U1) | CONFIRMED (5/5)`.)* Census, re-derived
for this revision over all 42 committed report TSVs: **43 firings in 14
files**, concentrated in loglines (3-5 per file) and bounded (1-4), one
of them on Report B. Not dead, not universal.

### §4.6 Class R-PRED — predictions vs outcomes

Fires only with a predictions file (§6).

| id | grain | aggregate | fires on |
|---|---|---|---|
| R-PRED-1 | set | `[]` | a prediction clause whose claim HOLDS against the report |
| R-PRED-2 | set | `[]` | a prediction clause whose claim FAILS |
| R-PRED-3 | set | `[]` | a prediction clause whose cell is absent from the report, or present but excluded / not-ranked / did-not-compile |
| R-PRED-4 | set | `[]` | a COMPOUND prediction whose clauses do not agree — verdict `partial` |

**R-PRED-4 is new (panel F7/S2)**: `partial` is the modal outcome in the
one committed, fully-scored prediction set in this repository — the
[B36] syntax ledger's tally is "three CONFIRMED outright, five REFUTED,
five PARTIAL" — and v1's trichotomy (confirmed / refuted / not-evaluable)
had no rule for it. Its predicate is arithmetic over the clause verdicts,
not a judgment: all-confirmed → R-PRED-1, all-refuted → R-PRED-2, any
mix → R-PRED-4. §6.6 states what that roll-up can and cannot reproduce.

*(v1's R-PRED-4 — "a finding no prediction covers" — is R-DELTA-4, §4.2,
where it is defined once. Panel D16.)*

**Threshold.** None. A prediction states its own bounds; the rule
evaluates them. R-PRED-3 exists so a prediction can never be silently
dropped — the failure mode a hand-kept ledger has.

**Template.**

```
R-PRED-1  "{prediction_id} ({source} {source_ref}) — **confirmed**:
           predicted {claim}; measured {measured}."
R-PRED-2  "{prediction_id} ({source} {source_ref}) — **refuted**:
           predicted {claim}; measured {measured}."
R-PRED-3  "{prediction_id} ({source} {source_ref}) — **not evaluable**:
           {reason}."
R-PRED-4  "{prediction_id} ({source} {source_ref}) — **partial**:
           {n_confirmed} clause(s) confirmed, {n_refuted} refuted,
           {n_not_evaluable} not evaluable: {clause_verdicts}."
```

### §4.7 Class R-BUCKET — registered buckets

A *registered bucket* is a known reading that is a FACT WITH A SOURCE —
the plan row's own example is "the `\z` regime artifact per feedback
2a". Buckets do not measure anything new; they attach a recorded,
citable caveat to a shape the report exhibits. Each has a `source` field
that must resolve to a committed file (§7.3).

| id | grain | aggregate | fires on | the registered fact, and its source |
|---|---|---|---|---|
| R-BUCKET-FORM | set | `[]` | a ranking group whose *rankable* rows carry both `same program` and `separate artifact` in `fact` | pcrec has no end-anchored mode, so its whole-subject form is a SECOND ARTIFACT `(?:P)\z`; libpcre2 reaches the same regime with `PCRE2_ANCHORED\|PCRE2_ENDANCHORED` on its ordinary artifact. Source: docs/design/record_schema.md §5; report.py `_form_fact` ([B9] R4); pcrec [OS-4]. |
| R-BUCKET-VSBEST | set | `[]` | a ranking group carrying ≥ 2 distinct pcrec pin slugs | `vs best` inverts visually wherever an OLDER pin's row ranks first; read same-pin rows or the Δ column. Source: reports/CLAUDE.md's reader's caveat (the a7e0bdf bounded entry), which records the "8192 inversion" REFUTED as a cross-pin `vs best` mis-reading ([B25]). |
| R-BUCKET-SPAN | set | `["config"]` | a cross-pin pair whose two pins are not adjacent in `[[pin_order]]` | the Δ spans more than one pin and is not a one-variable comparison. Source: reports/CLAUDE.md ("the bounded `vm-in` row's Δ partner is 288d505, not 334fd10e … spans THREE abi steps (16 → 22 → 23)"). |
| R-BUCKET-DOMINATED | subject | `["testee"]` | a set cell > 90 % one subject | a ratio between two such sums is a real number about a real total AND a statement about ONE subject wearing the set's name. Source: `_DOMINANCE_SHARE = 0.90` (report.py:2326) and `_dominant_subject`'s docstring ([B16] R7). **Needs a subject-grain TSV** (§11 Q2, ruled (a): `input-absent` until the reporter commits one). |
| R-BUCKET-KB | set | `["kb_id"]` | a cell matching a REGISTERED signature | **No signature is registered in catalogue v1.0. See below.** |

**R-BUCKET-FORM's predicate says *rankable* deliberately**: the `fact`
column is emitted on `rank`, `excluded`, `not_ranked`, `scratch` and
`did_not_compile` rows alike, and a group whose only `separate artifact`
row was excluded is not a group where two forms rank together.

**R-BUCKET-SPAN reads catalogue DATA, not an inferred order** (panel
B10). "Adjacent in the pin history" appears in neither declared input:
`store/index.tsv` has no pin-order column, and ordering pin slugs by
earliest timestamp gives *store*-adjacency, which is a different
predicate — it breaks on exactly the example §10 B.3 gives, a `vm-in` row
whose Δ partner skipped 334fd10e *because that pin has no `vm-in` row in
that sub-bench*. The order is therefore a `[[pin_order]]` table in
`rules.toml`, maintained by hand at each re-pin (one line, the same
precedent the catalogue already sets for registered data), and v1.0's
`pcrec` row is the eleven pins in `store/index.tsv`:
`8da6120, 692c2e8, 35e1ab1, 36d5963, 96e44c2, 263b013, a7e0bdf,
1989c62, 288d505, 334fd10e, d34c9131`. A pin absent from the table is a
load error (`exit 2`), never a silent non-firing. Appending a pin at a
re-pin is a MINOR bump; §8(1) checks that every pcrec pin slug appearing
in a golden report is in the table.

**R-BUCKET-KB ships with no registered signature, and §10 C.3 fails
plainly** (panel B4/F2). v1 called recognising KB-13 and KB-14 "from
their signatures" its strongest claim. It is not reachable: the
signature text — `expected N non-overlapping match(es); observed M` —
occurs **zero times** in the report `.tsv` and `.md` at any grain. It
lives in `docs/dev/known_issues.md:489` and in the record JSONL, which
§2.4 excludes. What the TSV supports is `(regime, form, n_wrong > 0,
n_gave_up == 0)` — and by that predicate KB-13's rows and KB-14's rows
are *identical in evidence*, separable only by their coordinates. A rule
firing on that would attach a diagnosed cause on the strength of "this is
the regime the bug was found in", which is a coordinate lookup wearing a
signature's clothes, and it would do so in the voice of a fact with a
source.

So, in v1.0:

- the class EXISTS, with its registration bar stated: a `[[signature]]`
  must name a **column-level discriminator that no other registered
  signature matches**, checked by `make check-interpret` against every
  golden report;
- registration is a **MAJOR** bump (§3.3);
- **no signature is registered**, so the rule always reports
  `did-not-fire: no-registered-signatures`;
- §10 C.3 is a stated known gap of v1, not a MUST (§10).

**The one-line reporter precondition was considered and NOT taken.** The
panel left the door open for an `expectation_detail` slot in
`gave_up_summary`'s style ([B9] R7's shape). It is not one line: the
observed-vs-expected string is derived per SUBJECT inside the record's
`observed` field, and the reporter computes nothing like it today
(`_set_cell_failure_reason` gives a one-word class — `gave-up | wrong |
gave-up+wrong | no-data | other` — which does not discriminate KB-13 from
KB-14 either). Designing it would be a reporter change of real size, made
to serve one rule that asserts more than any other. If a later ruling
wants it, it is a separate change with its own review, and this note
records the requirement it would have to meet (the discriminator bar
above) rather than pretending the requirement is already met.

**Worked example — R-BUCKET-FORM**, against the email repin report:
`orig` / match-compliance ranks nine rows in ONE group (form is not in
the group key), of which seven carry `whole-subject` / `separate
artifact` (all pcrec) and two carry `plain` / `same program` (both
libpcre2). `factored` / match-compliance is the same shape, 3 + 2. The
rule fires on both groups and on no other group in the report. This is
`feedback_…-repin.md` §2's demand — "State 'same program / separate
artifact' as a column; the 'regime artifact' bucket IS that fact, not a
footnote" — met at both layers: the reporter has the column ([B9] R4),
and the interpreter states the reading with its source.

**Worked example — R-BUCKET-VSBEST**: `reports/2026-09-06-bounded-0.3-…-after-d34c9131.tsv`,
`cls-upto-1024` / short-subject-search: `pcrec_334fd10e_auto-caps-simdna`
ranks **1** at 989.819865 ns and `pcrec_d34c9131_auto-caps-simdna` ranks
**2** at 998.441155 ns, while the same row's Δ reads `slower ×1.01` — the
current pin's `vs best` is worse than 1.000 purely because an older pin
is in the table. Three distinct pin slugs are present in that group
(288d505, 334fd10e, d34c9131), so the bucket fires. On Report A four of
the six ranking groups carry two slugs (8da6120, 692c2e8), and the
`aggregate = []` rendering names all four in one firing.

---

## §5. Output of `interpret` (part 1)

Two modes, one code path:

```
python3 -m pcrecbench interpret reports/<name>.tsv \
    [--index store/index.tsv] [--predictions <file>] \
    [--subject-grain reports/<name>.subject-grain.tsv] \
    [--catalogue catalogue/rules.toml] [--format tsv|md] [--render]
```

### §5.1 The facts TSV (`--format tsv`, the default)

The FACTS, machine-readable, one row per slot plus one row per non-firing
rule. Columns:

```
rule_id  fired  firing_seq  pattern  subject_or_na  regime  form
testee  record_id  prediction_id  slot  value
```

`firing_seq` is an integer, per rule, in emit order — **required**,
because the key columns cannot identify a firing for at least four rule
shapes (panel B9): R-STATUS-12 names TWO patterns against one `pattern`
column; R-STATUS-5, R-STATUS-6, R-STATUS-7 and R-STATUS-8 are header
facts with no key columns at all; R-BUCKET-FORM / R-BUCKET-VSBEST /
R-STATUS-13 are group-scoped with counts computed over a group's rows;
R-PRED-* are keyed by a prediction id. Without an ordinal, one-slot-per-
row output cannot be reassembled into slot SETS, and §8(5) — the
firewall's own test — becomes a self-consistency check against a freshly
re-run `interpret` rather than a check of the committed artifact.
`prediction_id` is its own column for the same reason; it is empty on
every non-R-PRED row.

Slots are emitted one per row (the same shape `render_tsv` uses for
metrics) so a fact is greppable without a parser. **Aggregation never
touches this file**: every one of R-ARM-1's 635 firings on Report C is
here, each with its own `firing_seq`.

A non-firing rule always emits a row with `fired=0`, `firing_seq=0` and a
reason token in `value`: `no-matching-rows | input-absent | grain |
reporter-version | no-registered-signatures | retired`. **A rule is never
silently absent** — the plan row's "plus the rules that did NOT fire" is
the whole reason a reader can trust an empty section.

Exit codes: `0` always on a successful read. Firing is not an error —
this is an instrument, not a gate (Q6, ruled: unchanged). `2` on a
malformed input, an unknown column, an unresolvable link, a pin absent
from `[[pin_order]]`, or a catalogue/code mismatch.

### §5.2 `aggregate` — the counted collapse (panel S1)

A rule declares `aggregate = [<slot name>, …]`. At RENDER time (never in
the facts TSV) its firings are grouped by those slot values and each
group renders as ONE bullet carrying:

1. the count of firings in the group;
2. **if the rule has a numeric slot**, the EXTREMAL firing by that slot
   (max), and, when the group has more than two members, the minimum as
   well; **if the rule has none**, the full SORTED LIST of the group's
   firing keys instead (see below — corrected from v1.1, panel/manager
   cross-review I-58 edit 5(a));
3. a pointer to the facts TSV for the rest.

`aggregate = []` means one bullet per firing. Aggregate groups render in
**sorted order of their key**, and — for a rule WITH a numeric slot — the
extremal firing inside a group is chosen by the rule's declared
`extremal` slot, defaulting to the rule's first numeric slot when
`extremal` is not declared (§3.2 lists it as an optional field), with
ties broken by the sorted key columns (`pattern`, `subject_or_na`,
`regime_or_na`, `form`, `testee`) — so the rendering is a total order
with no free choice in it. There is no threshold and no cut-off: the
collapse is a pure arithmetic reduction of a declared key, deterministic
and diffable, and it is NOT a ranking by interest (§1.1). Nothing is
dropped.

**Rules with NO numeric slot, and the default this note left undefined
(cross-review I-58 edit 5(a)).** v1.1 specified step 2 only for a rule
with a numeric slot, and §9.2's own worked specimen contradicts it on two
rules that have none: R-STATUS-2 (whose slots are record ids and
timestamps) renders its three `inconclusive-load` firings as a full
sorted list of record ids, not an extremal-plus-minimum pair, because
"extremal by first numeric slot" has no first numeric slot to be extremal
BY; R-BUCKET-VSBEST similarly renders all four ranking-group names in one
firing rather than picking one. **Ruling: this is the specimen's
behaviour, and the spec now says so as a rule, not an accident of the
worked example** — a rule whose declared `slots` contain no numeric
member (checked at load, §8(1)) renders its aggregated bullet as the
count plus the group's FULL SORTED LIST of firing keys (sorted the same
way as the group order itself, §5.2's own total order), never an
extremal/minimum pair. A rule with a numeric slot never falls back to
this form, even where its group has only one member.

**The extremal slot is declared per rule, default the first numeric
slot (cross-review I-58 edit 5(a), the R-DELTA-1 half).** Reading §5.2's
"extremal by first numeric slot" literally, R-DELTA-1's extremal would be
its first numeric slot, `median_ns` — which picks the LARGEST-MEDIAN
CELL in a group, not the biggest MOVER, and a reader collapsing 202
firings to 17 bullets wants the biggest ratio, not the slowest cell that
happens to also carry a faster/slower clause. R-DELTA-1 now declares
`extremal = "ratio"` (§3.2's TOML example; `ratio` is the clause's own
parsed `×N.NN`, a declared decomposition per §7.2), and the general rule
is stated once here rather than special-cased silently: **a rule may
declare `extremal = <slot>` to name which of its numeric slots is
"biggest" for aggregation purposes; a rule that omits it gets the
default, the first numeric slot in its `slots` list.** Every other rule
in §4 that declares a numeric slot keeps the default (`median_ns` is
already the biggest-cell reading R-ARM-1's own worked example in §9.2
uses, and it is what a reader comparing two config arms wants).

A rule whose individual bullets carry evidence a reader must see keeps
`aggregate = []` even where its count is largish: R-STATUS-3 renders all
thirteen (Report A) / twenty-three (Report C) excluded cells, because
each carries its own give-up summary and §10 A.3 requires all three
distinct summaries to appear, not just an extremal one.

The mechanism is required, not cosmetic. Measured, on the three
acceptance reports, firings → rendered bullets:

| rule | Report A | Report B | Report C |
|---|---|---|---|
| R-DELTA-1 | 3 → 3 | **202 → 17** | 0 |
| R-DELTA-2 | 6 → 6 | 1 → 1 | 0 |
| R-DELTA-3 | 4 → 4 | 0 | 0 |
| R-ARM-1 | 14 → 8 | **432 → 9** | **635 → 12** |
| R-FLOOR-1 | 2 → 1 | **81 → 2** | **190 → 2** |
| R-STATUS-3 | 13 → 13 (`[]`) | 0 | 23 → 23 (`[]`) |
| R-STATUS-4 | 0 | 6 → 2 | **172 rows / 60 pairs → 4** |
| R-BUCKET-VSBEST | 4 → 1 | 129 → 1 | 0 |

Rendered sidecar size lands **of order 40-50 bullets on all three
reports** (44 on Report A, enumerated rule by rule in §9.2) — against the
~40 / ~420 / ~275 the panel measured for v1 as specified. v1's §9.2
specimen showed ~15 bullets and never stated what its own output looked
like at modern report density; that gap is what this mechanism closes.

---

## §6. Predictions as machine-readable input

### §6.1 There is no existing store — checked

`grep -rn "prediction" docs/dev/ pcrecbench/ schema/ bench/` returns prose
only: `docs/dev/feedback_pcrecdev1_2026-08-25-repin.md` §3's eight-row
markdown table, the ledger convention line in `docs/dev/CLAUDE.md`
("predictions ledgered"), `bench/syntax/NOTES.md`'s P1-P13, one prose
line at `pcrecbench/harness.py:353`, and free text inside plan rows and
inbox items. **No machine-readable prediction exists anywhere in this
repository.** This design must create the minimal one. *(The grep path is
corrected from v1, panel D13: v1's cited command omitted `bench/` while
listing a result from it.)*

### §6.2 What a prediction actually looks like today

The design target is not three hand-picked shapes; it is the one
committed, fully-scored prediction set this project has —
`bench/syntax/NOTES.md`'s **P1-P13**, stated 2026-09-05 before any run
and scored in `docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md`
§6. §6.6 reports what happened when this note's format was tested against
all thirteen. Three predictions from elsewhere fix the simpler shapes:

1. *"cls-upto-2048 ÷ 1024 stays in 0.90-1.10"* (pcrec I-38, scored in
   the [B34]/[B27] ledger as 1.986 → 1.987) — a RATIO BETWEEN TWO CELLS
   at one pin.
2. *"letters 3.65-6.05 → 1.76-2.00"* (pcrec I-27, [OPT-5] STEP 1) — a
   BAND on a ratio, before and after.
3. *"no compile time beyond ×10 the median on any compiled testee"*
   (NOTES P13, scored CONFIRMED at worst ×2.08) — a BOUND over a
   POPULATION.

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
clause          (empty, or a suffix: P5.a, P5.b -- see below)
source          bench/syntax/NOTES.md
source_ref      P13
stated_utc      2026-09-05T00:00:00Z
subbench        syntax
version         0.1
selector        pattern=*;regime=*;form=*;testee=*
quantity        compile:median_total_ns
reducer         ratio_to_median_over(pattern)
op              lte
lo
hi              10
unit            x
note            "no compile time beyond x10 the median on any compiled testee"
```

- **`prediction_id` + `clause`.** A compound prediction is decomposed at
  AUTHORING time into clause-suffixed sub-ids (`P5.a`, `P5.b`), one row
  each. This is required, not optional: ten of the thirteen real
  predictions were scored per-clause. The parent id's verdict is
  R-PRED-1/2/4's arithmetic roll-up over its clauses (§4.6).
- **`selector`** is a `;`-joined list of `key=glob` over the TSV's own
  key columns (`pattern`, `subject_or_na`, `regime_or_na`, `form`,
  `testee`) **and `section`** (cross-review I-58 edit 3: v1.1's closed
  key list omitted `section` while §6.6's own P1 transcription already
  used it, `selector section=did_not_compile;testee=pcrec_*`, which was
  otherwise inexpressible against a grammar that did not name the key it
  matched on). `*` is the only wildcard, and a `|`-joined alternation is
  permitted in one field (`pattern=anc-caret|anc-A|anc-G`). A testee glob
  may name a config without a pin (`pcrec_*_auto-caps-simdna`) so a
  prediction survives a re-pin.
- **`quantity`** is drawn from a CLOSED SET the TSV can answer, declared
  in the catalogue and validated at load:
  `median_ns | min_ns | max_ns | stddev_ns | ratio_vs_baseline |
  ratio_vs_best | rank_in_group | pass_rate | n_gave_up | n_wrong |
  delta_verdict | status | section | compile:median_total_ns |
  compile:artifact_bytes | compile:emit_bytes |
  compile:emit_code_bytes | stamp:<name>`.
  A quantity outside the set is a load error, not a silent skip.
  - `rank_in_group` is v1's spelling of the TSV's `rank_or_na`
    **column** — the rank of a TESTEE within a ranking group
    (report.py:4137). It is renamed from v1's bare `rank` because a
    prediction author reaching for "rank" usually means the rank of a
    PATTERN within a set, which is a different number and is produced by
    the `rank_over` reducer below. v1 offered `rank` and warned about
    nothing; that was a live trap (panel F7).
  - `compile:median_total_ns` means "whichever compile-cost metric the
    row carries" — `render_tsv` emits either `median_total_ns` or
    `derived_first_match_row_minus_steady_state_ns` for a `lazy-jit`
    cost class (report.py:4177). No committed report exercises the
    second; the token covers both so a lazy-JIT prediction is not
    unloadable (panel build #15).
- **`reducer`** (optional) turns a population into one number or one
  set: `identity | ratio_to(<selector>) | ratio_to_median_over(<key>) |
  ratio_max_min_over(<key>) | rank_over(<key>) | count | set_of(<key>) |
  max | min | median`.
  - `ratio_max_min_over(<key>)` is max ÷ min over the population grouped
    by `<key>` — the "every member of this group agrees within ×N" shape
    (P3, P11).
  - `rank_over(<key>)` orders the selected rows by the quantity and
    returns the 1-based position of each — a cross-pattern ordering
    (P5, P7). It is an ordering of numbers the reporter already reduced
    and printed, not a second reduction of records (§2.4).
  - `set_of(<key>)` collects the distinct values of a key column over
    the selected rows (P1).
- **`op`** ∈ `lt lte gt gte between eq neq eq-token neq-token set-eq
  set-subset present absent`. `eq`/`neq` are numeric; `set-eq` and
  `set-subset` take a `|`-joined member list in `hi`.

Prediction (1) becomes:
`selector pattern=cls-upto-2048;regime=match-compliance;form=plain;testee=pcrec_*_auto-caps-simdna`,
`quantity median_ns`,
`reducer ratio_to(pattern=cls-upto-1024;regime=match-compliance;form=plain;testee=<same>)`,
`op between; lo 0.90; hi 1.10`.

### §6.4 What a prediction CANNOT say, stated plainly

The report TSV carries `n_wrong` and `pass_rate`; it never carries an
answer, a span, or a capture. So:

- **an answer/span prediction that AGREES with the oracle** is
  expressible, as `quantity n_wrong; op eq; hi 0` — the expectations
  encode the oracle's answer, so "answers as the oracle says" is exactly
  `n_wrong == 0` (this is how P10's semantics clause and P12's agreement
  clause were in fact scored: "zero wrong answers");
- **an answer/span prediction that DISAGREES with the oracle** is
  expressible only as `n_wrong > 0` on the named cell, plus `n_wrong ==
  0` on the named controls (this is how P2's wrapper clause was scored);
- **the specific answer or span is NOT expressible**, and `interpret`
  must say so rather than approximate it. P9 ("`asr-k-uc` reports span
  [4,9] on `key=value`") is the case: the cell's `n_wrong` can say the
  span was wrong, and nothing in the two declared inputs can say it was
  [0,9]. A prediction whose `quantity` needs an answer or a span is a
  LOAD ERROR with a named reason, never a silent `not-evaluable`.

This is a real limit of reading a report rather than the records, and it
is the limit that keeps §2.4 honest.

### §6.5 How a prediction gets INTO the file

Written by hand, by the person who states it, **before the run**, and
committed before the run — the boilerplate's own rule ("a prediction is
stated BEFORE the run wherever the charter allows"). `stated_utc` is a
column so `make check-interpret` can assert it precedes a timestamp
this section defines precisely (below).

**The check, corrected (cross-review I-58's honesty edit).** v1.1 claimed
checking `stated_utc` against the earliest `timestamp` IN THE REPORT'S
OWN POPULATION makes post-hoc prediction "mechanically impossible to
commit unnoticed." That overclaims: supersession opens a window. A
person can read run 1's actual numbers, then state a prediction with
`stated_utc` dated after run 1 but before a later re-measure, aimed at
the re-measured population; if the check only looks at the REPORT's own
population, the earliest timestamp it sees is the LATER re-measure's, so
a `stated_utc` stated after reading run 1 (and therefore not a
prediction at all) passes as if it predated everything.

**The fix that closes the window is checking against the EARLIEST
`timestamp`-comparable value across ALL rows of `store/index.tsv` for
this (subbench, version, machine) — including SUPERSEDED ones — not just
the rows the report's own query included.** Run 1's record, even
superseded and absent from every later report, is still a row in the
index (§2.2: `index.{subbench,version,machine_id,timestamp,status}`, all
four columns already declared there — no new column is needed for this
check). Anchoring on that earliest index timestamp instead of the
report's own earliest one closes exactly the case above: a `stated_utc`
after run 1 fails the check even when the report being interpreted is
run 2's re-measure. This is a check `make check-interpret` runs against
`index.*` directly (§2.2), not a declared `inputs` entry of any one rule
— no R-PRED rule's `inputs` needs a column beyond what §2.2 already
lists.

**The residual limit, stated honestly rather than left implied.** Even
this fix does not make post-hoc prediction impossible in the fullest
sense: it can only prove a `stated_utc` precedes the FIRST time this
project ever measured this (subbench, version, machine) population, by
any pin, at any point in `store/index.tsv`'s history. It cannot see a
prediction informed by reading pcrec's own source or commit history
(someone could know an optimization already shipped and predict its
effect without ever having read a bench run), and it has no anchor at
all for a population that has never been measured before (the check is
vacuous, not restrictive, on a first-ever sample). **A prediction stated
before the first record of a population was ever measured is the only
thing the check can prove — not that no other channel informed it.**
Still the design's best single idea for the part it does close, which is
the part that bites in practice (a person re-reading THIS project's own
committed reports before writing a prediction down).

Predictions stated in an inbox item are transcribed by the manager
session at ack time — the same motion that already moves an inbox item
into a plan row. **Parsing inbox prose is explicitly rejected:** a
regex over English is a second source of truth for what pcrec predicted,
and getting it wrong would be worse than not having it.

No back-fill. The eight predictions of `feedback_…-repin.md` §3 and the
thirteen of `bench/syntax/NOTES.md` may be transcribed later; the
acceptance test (§10) does not require it, and a lane transcribing 21
historical predictions is a separate, reviewable change.

### §6.6 The format tested against P1-P13 — the result

Panel S2 required this format to be tried against the thirteen real,
scored predictions *before* a loader exists, and to express ≥ 9 of 13.
The transcription was done for this revision (the exercise, not a
committed file — §6.5's no-back-fill rule stands). Result, per
prediction, against the clause the ledger actually scored:

| P | expressible | how, and what it needed |
|---|---|---|
| P1 | **yes** | `quantity section; reducer set_of(pattern); op set-eq` over `selector section=did_not_compile;testee=pcrec_*` — needed `set_of` + `set-eq` |
| P2 | **yes, as the oracle-disagreement proxy** | `.a` = `n_wrong gt 0` on `rec-r-uc`/match-compliance/whole-subject; `.b`/`.c` = `n_wrong eq 0` on the controls; `.d` (`vrb-accept`) → R-PRED-3 `not evaluable` (the pattern is a refusal at this pin). The specific answer is not expressible (§6.4) |
| P3 | **yes** | `reducer ratio_max_min_over(pattern)` per spelling group × regime × testee; `op lte 1.5` |
| P4 | **yes** | `ratio_to(<selector>)`; `op lte 1.0`; one clause per regime |
| P5 | **yes** | `.a` = `reducer rank_over(pattern); op lte 3` per testee in the throughput regime — needed `rank_over` and the `rank_in_group` rename; `.b` = `ratio_to(floor)` `op lte 1.0`, which needs precondition P-1 |
| P6 | **yes** | `ratio_to(<selector>)`; `op lte 1.5` |
| P7 | **yes** | `.a` = `rank_over(pattern) gte 90` (the slowest cells); `.b` = `ratio_to(<selector>) lte 2` |
| P8 | **yes** | two clauses, `ratio_to` at different bounds per regime |
| P9 | **headline clause NO**, cost clause yes | the span [4,9] is not in the TSV at any grain (§6.4). `.a` loads as an error naming the span limitation; `.b` (`asr-k-uc ÷ lit-cat` tput) is an ordinary `ratio_to` |
| P10 | **yes, as the oracle-agreement proxy** | `.a` = `n_wrong eq 0` on `grp-atomic-alt`; `.b` = `ratio_to lte 1.5` |
| P11 | **yes** | `ratio_max_min_over` across the two families, per regime |
| P12 | **cost clause yes, agreement clause NO** | "`mod-j-uc` agrees with `bak-1` on every subject" is an answer-equality claim BETWEEN TWO PATTERNS; each pattern's `n_wrong == 0` is a claim about the ORACLE, not about the other pattern, so the proxy does not carry the claim and the clause loads as an error |
| P13 | **yes** | `ratio_to_median_over(pattern); op lte 10` — the format's own worked example |

**Twelve of thirteen** are expressible in the clause the ledger scored;
**eight** are expressible in every clause; **two** (P9.a, P12's agreement
clause) are inexpressible and now fail loudly at load rather than
silently; **one** (P2.d) is expressible and correctly lands as
`not-evaluable`. *(Checked against §6.3's edit 3 fix: P1 is the one
transcription in this table that names `section` in its selector, and it
was already counted among the twelve — the fix makes its own selector
syntactically legal against the closed key list rather than changing
which predictions are expressible. The 12-of-13 count is unchanged.)*

**Four things changed because of the exercise**, none of which v1's
three-prediction survey would have surfaced: `set_of` + `set-eq` (P1),
`rank_over` and the `rank_in_group` rename (P5, P7), the clause-suffixed
ids and the `partial` verdict (ten of thirteen), and §6.4's explicit
statement that answers and spans are out of reach (P9, P12).

**On reproducing the ledger's 3/5/5 tally — it does not, and that is the
right outcome.** Every CLAUSE verdict reproduces. The parent roll-up
differs on four of thirteen (P1, P4, P6, P12), always in the direction of
the arithmetic rule being stricter than the human tally:

- **P6** the ledger tallied CONFIRMED, describing interp as "marginal";
  one measured ratio is **1.722** against a stated bound of ×1.5, so the
  clause is refuted and the roll-up is `partial`. "Marginal" is charity a
  rule does not have.
- **P1** the ledger tallied PARTIAL ("13/15 as stated"); both clauses
  fail as stated (one named pattern compiled, one unnamed pattern
  refused), so the roll-up is `refuted`.
- **P4** and **P12** the ledger listed under REFUTED while naming the
  refuted clause only ("P4 in the search regime", "P12's cost clause");
  mechanically both are `partial`.

The ruling this note takes: **the per-clause verdicts are `interpret`'s
output and are authoritative; the parent verdict is the stated
arithmetic; a ledger's tally is a human reading and the tool must not try
to reproduce it.** The four disagreements are the "no opinions" property
working, and a reader who wants the human tally has the ledger.

---

## §7. The opinion firewall, enforced

The charter says "every sentence cites a fired rule". Discipline cannot
deliver that. Four structural properties plus one human gate do — and
§0 says plainly what they buy: not the impossibility of opinion, but its
concentration in one reviewed, versioned file.

### §7.1 One template per rule, no free-text channel

The renderer is:

```python
def render(rule_id, slots) -> str:
    rule = CATALOGUE[rule_id]
    missing = set(rule.slots) - set(slots)
    extra   = set(slots) - set(rule.slots)
    if missing or extra:
        raise InterpretError(...)          # a bug, not a warning
    text = rule.template.format(**slots)
    for link in rule.links:                # §7.3, appended not embedded
        text += f"\n  See: {link}"
    return text
```

`str.format` on a template that declares its slots is the whole
sentence-production surface. There is **no code path** by which
`interpret` can emit a string that is not `stamp | heading | template
output | link | did-not-fire row`.

**And the template's own fixed prose is audited (panel B11/F1).** v1's
three properties covered the number of sentence shapes, the values
substituted into them, and the pointers appended — and said nothing about
the words between the braces, which is exactly where an opinion fits.
v1's own catalogue proved it: R-STATUS-12's template ended "*: a
different budget binds on the two spellings*", a mechanism claim that
§1.1 forbids, asserted with no link, and §8(5)'s no-prose check passed it
by construction because a template that carries an opinion is still
reproducible template output. The rule now:

> **Every clause in a template that is not a slot and not definitional
> must either be a `links` entry the renderer appends, or be removed.**

"Definitional" means a clause that restates the rule's own predicate or
names the source of its threshold (e.g. "beyond 2 × max(stddev)"), never
a claim about mechanism or cause. §8(6) is the human-reviewed
template-diff gate that enforces it, because template text is the one
unmechanised prose surface in the system and the only honest way to check
prose is to read it.

**The same rule applies to did-not-fire reasons** (panel F10, which the
consolidated review did not carry as a numbered item — applied here under
B11 and flagged in the lane report). v1 specified the reason as a closed
token and rendered it in §9.2 as free text (`no-matching-rows (every
record reads agree or n/a (v1.x))`), which is a second unchecked prose
channel. In v1.1 a rule carries a `no_fire` field — one sentence, no
slots, reviewed under §8(6) exactly like `template` — and the render is
`<token> (<no_fire>)`. Nothing else may appear there.

### §7.2 Slot values are copied, counted, computed or decomposed

Each rule function receives a view that raises on any column not in its
declared `inputs` (§3.2.2). A slot value must be one of **four** kinds:

1. a literal cell value copied verbatim from an input file;
2. an integer count of rows the rule itself matched (including an
   `aggregate` group's count);
3. a number produced by an arithmetic written out in full in the
   catalogue's `arith` field;
4. **a declared decomposition — a named regex or split rule, written out
   in full in the catalogue's `arith` field, applied to one named input
   value.**

Kind 4 is new (panel S4). v1 permitted only the first three and
separately claimed R-STATUS-12 was "the ONE place a rule reads a
formatted string rather than a column"; the panel found at least four
more, so the firewall's audit surface was silently incomplete. The
declared decompositions in v1.0, each written out in `arith`:

| rule | decomposition | of |
|---|---|---|
| R-RANK-1, R-ARM-1, R-BUCKET-VSBEST, R-BUCKET-SPAN | `testee_id` → `(engine, version_slug, mode, caps, simd, extra)`, splitting the config slug from the RIGHT (§4.4) | a column |
| R-DELTA-1, R-DELTA-2, R-DELTA-3 (cross-review I-58 edit 4) | `testee_id` → `config` = `(engine, mode, caps, simd, extra)` with `version_slug` removed — the SAME split as the row above, minus the one field a cross-pin pair is guaranteed to differ on | a column |
| R-DELTA-1 (cross-review I-58 edit 4) | `direction` = the matched clause's own leading token (`faster` or `slower`), copied verbatim from the predicate's own match; `ratio` = the same clause's trailing `×N.NN`, parsed as a float, also copied verbatim | a column |
| R-STATUS-5 | `source` → the candidate count in `(N record(s) matching this query)` | a header value |
| R-STATUS-13, R-RANK-1 | `_is_reference`: strip `@…`, then `startswith("libpcre2_") and "_interp-" in base` (report.py:3153-3159, copied) | a column |
| all four R-DELTA | `delta_verdict` → the `; `-separated clause list (§2.1) | a column |
| §2.1's header parse | the `; `-with-known-keys split (§2.1, normative form) | the header line |

R-STATUS-12's parse of `_gave_up_cell_summary`'s rendering — v1's Q8, and
the fragile one — is GONE, replaced by precondition P-2's columns (§2.5).
R-STATUS-9 reads the agreement string's leading token (`disagree`), which
is a `startswith` on a value whose five shapes are enumerated in
`threshold_src` (§4.1), not a parse of a rendering's interior.

The declared arithmetic in v1.0: R-FLOOR-2's `median_ns / n`, R-RANK-1's
side-of-1.0 test, R-ARM-1's `|median_a − median_b| > 2 × max(stddev_a,
stddev_b)` and its ratio, R-PRED's per-clause bound evaluation, and
R-PRED-4's roll-up. Every numeric slot is rendered by one formatter with
a fixed precision so two renders of the same input cannot differ in a
digit.

### §7.3 Links are validated, never generated

A rule's `links` are repo-relative paths, optionally with a `#anchor` or
`:line`. At render time each is resolved: the file must exist, and an
anchor must appear as a heading or a literal id in it. An unresolvable
link exits 2. So a hypothesis can only appear in a sidecar if somebody
has already written it down and committed it —
`docs/dev/outbox_to_pcrec.md`, `docs/dev/known_issues.md`,
`docs/dev/upstream_findings.md`, `docs/dev/ledgers/`,
`docs/dev/feedback_*.md`. The interpreter cannot invent a cause because
it has no way to say one, and after §7.1 it cannot smuggle one into a
template either.

### §7.4 Who phrases — RULED, not deviated from

v1 flagged a charter deviation and offered a fallback. Both are resolved
(panel B11 + F12, ruled by the manager in the r4 consolidation; no
escalation to Frank was needed).

The plan row says the SKILL "phrases the fired rules into a SIDECAR". The
reading v1 took — that "phrases" means "generates prose at run time" — is
not the only one, and not the best one. **The renderer phrases; the
templates are human-reviewed prose, authored ONCE, before any run,
committed and reviewed under §8(6).** Under that reading nothing deviates
from the charter: the sentences are written by the same kind of author
the charter imagined, just written *before* the run rather than during
it — which is strictly better for a project whose whole discipline is
stating things before measuring them — and byte-reproducibility, §8(3)'s
freshness check and §3.3's regeneration rule all survive.

**v1's fallback is REJECTED, not deprecated.** v1 offered, if the
deviation were refused, a clearly-fenced `## Reader's note` section in
the sidecar, excluded from the byte-equality check. That option is
deleted: it creates exactly the unchecked prose channel this firewall
exists to prevent, inside the artifact the firewall is about, and it
would make §8(3) and §8(5) both partial. A human reading belongs in a
ledger under `docs/dev/ledgers/`, which is where human readings already
live and which nothing here proposes to change.

---

## §8. `make check-interpret`

A new target beside `check-schema` / `check-harness` / `check-report`,
added to `check`. **Six** sections.

**(1) Catalogue/code correspondence.** Every `[[rule]]` has a function;
every function has a `[[rule]]`; every rule declares `grain`,
`aggregate`, `no_fire` and every other required field; every declared
`inputs` entry parses under §3.2.2's grammar and names a section and
columns that exist — the data columns read from `render_tsv`'s own
`header` list in the source, the header KEYS read by running `report
--format tsv` over the check's fixture store (§2.1); every `quantity`
token in every committed predictions file is in the closed set; every
`links` entry resolves; every pcrec pin slug appearing in a golden report
is in `[[pin_order]]`; every registered R-BUCKET-KB signature (none in
v1.0) names a discriminator no other signature matches, checked against
the goldens; every rule has ≥ 1 fixture and ≥ 1 negative control.

**(2) Determinism and the golden facts.** `interpret` run twice on the
same inputs produces byte-identical output in both formats. Then, on the
**three named real reports** (§10's acceptance set), the output is
compared against committed golden files
`catalogue/golden/<report-basename>.facts.tsv`.

**The golden runs against a FROZEN index snapshot** committed beside it,
`catalogue/golden/index@<date>.tsv` — never against live
`store/index.tsv`. The live index stays `interpret`'s default for a human
run; it is the pinned check that must not read it. The reason is
measured: R-STATUS-2's whole purpose is to look outside the report, and
`store/index.tsv` has been rewritten in 16 commits and stands at 160
rows, so the moment any future window measures another record with a
non-`measured` status in a covered (subbench, version, machine), the
facts for an already-committed, unmodified report would change and `make
check` would fail on a commit whose only content is new records. **That
is KB-8's failure mode one layer up**, and it is closed by the snapshot,
not managed. *(New in v1.1, panel B8.)*

**What may and may not fail, and who owns the fix** (the second half of
B8, which v1 did not address at all):

| a commit that… | may `check-interpret` fail? | who regenerates |
|---|---|---|
| adds records only (a window's output) | **NO** — the frozen snapshot makes it impossible | — |
| bumps `catalogue_version` | **YES**, by design | the catalogue lane, in the same commit (§3.3) |
| bumps `REPORTER_VERSION` | **YES** — `reports/CLAUDE.md`'s standing rule regenerates every report, and a regenerated report can move a fact and always moves the sidecar's `report_sha256` | the reporter lane, in the same commit: re-run `interpret --render` for every committed sidecar and re-derive the three goldens. This is the same motion the bump already requires for the reports themselves |
| refreshes the index snapshot | **YES**, if a fact moves | the lane refreshing it, in the same commit, with the new date in the filename |

A reporter bump therefore costs one extra regeneration step, on a corpus
Q5 deliberately keeps at three sidecars at landing (§11).

**(3) Sidecar freshness.** Every committed
`reports/*.interpretation.md` is re-rendered from its recorded inputs
(the stamp names them and their sha256) and must come back byte-identical.
A report edited without re-rendering its sidecar, or a catalogue bump
without regeneration, fails here.

**(4) Fixtures — GENERATED base plus one declared mutation.**

v1 said this section mirrored `schema/examples/bad/`'s pattern and
described that pattern as hand-written. It is not: `schema/examples/bad/`
holds **72** sabotage records plus a `CLAUDE.md`, and the Makefile's own
`check-schema` comment states that "every v1.4 sabotage in bad/ is a
one-field mutation" of `gen_example_14.py`'s output, pinned by
`gen_example_14.py --check`. The precedent is *generated base plus
declared mutation*. v1's plan would also have cost ~190 hand-typed files,
each of which must stay consistent with `render_tsv`'s 18-column order
forever, and — worse — a hand-typed fixture carries combinations
`render_tsv` cannot emit (`ratio_vs_baseline`, `pass_rate`, `n` and
`fact` are all derived by the reporter), so a rule would be proven to
fire on a shape that does not exist. And "the control differs from the
sabotage in the minimum number of bytes" is not a computable predicate:
minimum over what? *(Panel S6.)*

v1.1 adopts `catalogue/fixtures/gen.py`, run with `--check` inside
`check-interpret` exactly as `gen_example_14.py --check` runs inside
`check-schema`. Each fixture directory carries:

```
catalogue/fixtures/R-DELTA-1__faster-outside-spread/
    source.toml     report = "reports/2026-08-25-email-...-repin-692c2e8.tsv"
                    select = { pattern = "factored", regime = "short-subject-search" }
                    index  = "catalogue/golden/index@2026-09-07.tsv"
                    expect = ["R-DELTA-1"]
    report.tsv      GENERATED: a real reporter-produced slice
    index.tsv       GENERATED: the matching index slice
catalogue/fixtures/R-DELTA-1__control-unchanged-within-spread/
    source.toml     ... plus  mutate = { section = "rank", column = "delta_verdict",
                                         value = "unchanged (within spread)" }
                    expect = []
    report.tsv      the SAME slice with EXACTLY ONE declared field changed
    index.tsv
```

The check asserts the named rule fires on the sabotage and does NOT fire
on its control, and that **exactly one declared field differs** — the
well-defined replacement for "the minimum number of bytes". The generator
shares source with `report.py`'s OUTPUT, never with `interpret.py`'s rule
functions, so the project's controls-share-no-source discipline (pcrec
D35) holds where it matters.

Three fixture kinds beyond the pair:

- **co-firing and mutual-exclusion**: R-DELTA-1 and R-DELTA-2 must never
  fire on one cell; **R-DELTA-2 and R-DELTA-3 must**, on the compound
  `selection changed (vm → dfa); now measured (was: gave-up)` (panel B3);
  R-RANK-1 and R-DELTA-2 must be able to.
- **guard**: a group with no rankable reference arm must fire R-STATUS-13
  and must NOT fire R-RANK-1 (panel B6).
- **the null control (new in v1.1, panel S3)**: a synthetic *clean*
  report — every record `measured`, no cell excluded, no
  `did_not_compile` row, no Δ outside spread, no arm pair outside spread,
  one pin, one schema version, `mixed_x13: False`,
  `worst_other_core_busy: n/a` — on which **all 31 rules must report
  `fired=0`**. §10 has no report on which the tool should stay quiet and
  cannot have one (R-STATUS-5 and R-FLOOR-1 fire on essentially every
  committed report), so the missing false-positive control is
  constructible only here, and it is required.

**(5) The no-prose check.** A generated sidecar is re-parsed and every
non-blank, non-heading, non-stamp line must be reproducible by
`render(rule_id, slots)` for some rule and some slot set present in the
facts TSV — reassembled by `(rule_id, firing_seq)`, which is why §5.1
carries that column. A line that is not is a failure.

**(6) The template-diff gate (new in v1.1, panel B11/F1).** Every diff
that touches a `template`, `no_fire` or `links` field, or adds a
`[[signature]]`, is flagged by the check with the before/after text and
**must carry a reviewer's approval line in the commit message** naming
the rule ids reviewed. The check cannot judge prose; what it can do is
refuse to let prose change invisibly. This is the one place in the design
where a human is the mechanism, and it is deliberate: template text is
the only unmechanised prose surface in the system, and §7.1's rule
("every clause is a slot, definitional, or a link") is a rule a person
applies.

Runtime budget: parsing all 42 committed report TSVs (135,891 data rows)
takes 0.25 s measured; the fixtures are small projections and the golden
set is three files, so this target is seconds, not the ~20 minutes
`check-harness` costs. It goes into `check` without an argument about
budget. The resource actually at risk is the REVIEW budget — the golden
facts file for Report B is ~2,500 rows and moves on any catalogue change
that touches a fact — which is why Q5's three-sidecars-at-landing
recommendation stands (§11).

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

It does **not** summarise, rank, explain, extend, or add a reader's note
(§7.4). If a fired rule looks wrong to the session, that is a catalogue
change through a lane, not an edit to the sidecar.

### §9.2 The sidecar, rendered by hand from a real current report

Below is what `/pcrec-bench-interpret 2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8`
must produce once built. Every number is taken from the committed `.tsv`
and from `store/index.tsv`; every section is checked against every fix in
this revision; **every one of the 31 rules appears, firing or not** —
twelve fire, nineteen do not, and the rendered file is **44 bullets**.
`…` marks a place where THIS NOTE abridges a repeated bullet list to stay
readable; the generated file elides nothing, and no rule is ever omitted
from it. **This is a specification of output, not an example of
style.** It assumes preconditions P-1 and P-2 have landed and the report
has been regenerated at the bumped `REPORTER_VERSION` (so `floor_pattern:
none` is in its header, and the `giveup_smallest` rows exist).

```markdown
<!-- pcrecbench interpret
report:          reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.tsv
report_sha256:   <64 hex>
index:           store/index.tsv
index_sha256:    <64 hex>
predictions:     (none)
catalogue:       1.0
interpret:       v1
reporter:        v16 (<date>)
query:           subbench=email-specimen, version=0.1
-->

# Interpretation — 2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8

Generated by `pcrecbench interpret` against catalogue 1.0. Every
sentence below is a rule template. No sentence is generated.

## R-STATUS-5 — query population (1 firing)

- The query drew 14 candidate record(s) and included 9; 5 superseded,
  0 newer-but-not-measured, 0 invalid.

## R-STATUS-2 — a non-measured record outside the population (3 firings, aggregated by status)

- 3 record(s) with status **inconclusive-load** are in store/index.tsv
  for email-specimen@0.1 on budu-ryzen1600 and are NOT in this report's
  population:
  `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z`
  (testee `libpcre2_10.46_interp-caps-simdna`, 2026-08-25T17:34:02Z);
  `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z`
  (2026-08-25T17:51:31Z);
  `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z`
  (2026-08-25T17:55:34Z).

## R-STATUS-6 — mixed schema versions (1 firing)

- This report's population spans record schema versions 1.1, 1.2; 9 of 9
  record(s) predate the v1.4 trial-agreement block and read
  `n/a (v<schema>)` for agreement.

## R-STATUS-3 — cells excluded from ranking (13 firings, not aggregated)

- factored / large-subject-throughput / plain /
  `libpcre2_10.46_jit-caps-simdna` is EXCLUDED from ranking: pass-rate
  0.6667; 0 wrong answer(s); 0 give-up trial(s); give-up summary `0`.
  (`n_gave_up` counts TRIALS; a `×N` in the summary counts SUBJECTS.)
- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_vm-caps-simdna` is EXCLUDED from ranking: pass-rate
  0.6667; 0 wrong answer(s); 5 give-up trial(s); give-up summary
  `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)`.
  (`n_gave_up` counts TRIALS; a `×N` in the summary counts SUBJECTS.)
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_vm-caps-simdna` is EXCLUDED from ranking: pass-rate
  0.9412; 0 wrong answer(s); 25 give-up trial(s); give-up summary
  `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)`. (…)
- orig / large-subject-throughput / plain /
  `pcrec_692c2e8_vm-caps-simdna` is EXCLUDED from ranking: pass-rate
  0.6667; 0 wrong answer(s); 5 give-up trial(s); give-up summary
  `-4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B)`. (…)
- … (9 more bullets of the same template, abridged HERE only: the four
  remaining `-2:PCREC_ERR_STEPS` cells on 692c2e8 `vm-in` and on
  8da6120's three arms, the three remaining `-3:PCREC_ERR_FRAMES` cells
  on 8da6120, and the two remaining `-4:PCREC_ERR_WORK` cells)

## R-STATUS-12 — one subject, two give-up codes across two spellings (3 firings, not aggregated)

- Subject `t-c-long-atom-run` (1,048,576 B) gives up as
  **`-2:PCREC_ERR_STEPS`** on `factored` and **`-4:PCREC_ERR_WORK`** on
  `orig`, on `pcrec_692c2e8_vm-caps-simdna` in large-subject-throughput.
  See: docs/dev/feedback_pcrecdev1_2026-08-25-repin-v2.md §2
- … (2 more bullets of the same template, abridged HERE only: the same
  pairing on `pcrec_692c2e8_vm-in-caps-simdna` and on
  `pcrec_8da6120_vm-caps-simdna`)

## R-DELTA-1 — cross-pin Δ outside spread (3 firings, aggregated to 3 by regime × config × direction)

- factored / short-subject-search / plain /
  `pcrec_692c2e8_vm-caps-simdna`: the reporter's cross-pin Δ reads
  **faster ×1.19** (median 69,537.5 ns).
- orig / match-compliance / whole-subject /
  `pcrec_692c2e8_vm-caps-simdna`: the reporter's cross-pin Δ reads
  **faster ×1.26** (median 80,227.6 ns).
- orig / match-compliance / whole-subject /
  `pcrec_692c2e8_auto-nocaps-simdna`: the reporter's cross-pin Δ reads
  **faster ×1.00** (median 233,982.1 ns).

## R-DELTA-2 — cross-pin selection change (6 firings, aggregated to 6 by regime × config)

- factored / short-subject-search / plain /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 1): **selection changed
  (vm → dfa)**.
- factored / short-subject-search / plain /
  `pcrec_692c2e8_auto-caps-simdna` (rank 2): **selection changed
  (vm → dfa)**.
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 1): **selection changed
  (vm → dfa)**.
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_auto-caps-simdna` (rank 2): **selection changed
  (vm → dfa)**.
- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_auto-caps-simdna` (rank 1): **selection changed
  (vm → dfa)**.
- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 2): **selection changed
  (vm → dfa)**.

## R-DELTA-3 — a cell that is now measured (4 firings, aggregated to 4 by regime × config)

- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_auto-caps-simdna` (rank 1): **now measured (was:
  gave-up)**.
- factored / large-subject-throughput / plain /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 2): **now measured (was:
  gave-up)**.
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_auto-caps-simdna` (rank 2): **now measured (was:
  gave-up)**.
- factored / match-compliance / whole-subject /
  `pcrec_692c2e8_auto-nocaps-simdna` (rank 1): **now measured (was:
  gave-up)**.

## R-ARM-1 — two arms one config token apart (14 firings, aggregated to 8 by arm pair × regime; groups in sorted key order, each showing its extremal cell)

- `auto-caps-simdna` vs `auto-nocaps-simdna`, match-compliance — 1
  firing. factored / whole-subject, pin 692c2e8: `auto-nocaps-simdna`
  234,096.5 ns vs `auto-caps-simdna` 234,963.8 ns — ×1.00, beyond
  2 × max(stddev) = 367.3 ns. The two arms differ in exactly one config
  token (caps: nocaps vs caps).
- `auto-caps-simdna` vs `auto-nocaps-simdna`, short-subject-search — 1
  firing. factored / plain, pin 692c2e8: `auto-nocaps-simdna` 6,136.3 ns
  vs `auto-caps-simdna` 6,291.5 ns — ×1.03, beyond 2 × max(stddev) =
  39.2 ns (caps: nocaps vs caps).
- `auto-caps-simdna` vs `vm-caps-simdna`, match-compliance — 2 firings.
  Extremal: orig / whole-subject, pin 692c2e8: `vm-caps-simdna` 80,227.6
  ns vs `auto-caps-simdna` 234,082.1 ns — ×2.92, beyond 2 × max(stddev)
  = 318.8 ns (mode: vm vs auto). Minimum: pin 8da6120, ×2.33.
- `auto-caps-simdna` vs `vm-caps-simdna`, short-subject-search — 3
  firings. Extremal: factored / plain, pin 692c2e8: `auto-caps-simdna`
  6,291.5 ns vs `vm-caps-simdna` 69,537.5 ns — ×11.05, beyond
  2 × max(stddev) = 826.9 ns (mode: auto vs vm). Minimum: orig / plain,
  pin 692c2e8, ×4.73.
- `auto-caps-simdna` vs `vm-in-caps-simdna`, match-compliance — 2
  firings. Extremal: orig / whole-subject, pin 692c2e8:
  `vm-in-caps-simdna` 62,732.3 ns vs `auto-caps-simdna` 234,082.1 ns —
  ×3.73, beyond 2 × max(stddev) = 304.7 ns (mode: vm-in vs auto).
  Minimum: factored / whole-subject, ×1.98.
- `auto-caps-simdna` vs `vm-in-caps-simdna`, short-subject-search — 2
  firings. Extremal: factored / plain, pin 692c2e8: `auto-caps-simdna`
  6,291.5 ns vs `vm-in-caps-simdna` 54,117.6 ns — ×8.60, beyond
  2 × max(stddev) = 695.9 ns (mode: auto vs vm-in). Minimum: orig /
  plain, ×2.05.
- `vm-caps-simdna` vs `vm-in-caps-simdna`, match-compliance — 1 firing.
  orig / whole-subject, pin 692c2e8: `vm-in-caps-simdna` 62,732.3 ns vs
  `vm-caps-simdna` 80,227.6 ns — ×1.28, beyond 2 × max(stddev) = 318.8
  ns (mode: vm-in vs vm).
- `vm-caps-simdna` vs `vm-in-caps-simdna`, short-subject-search — 2
  firings. Extremal: orig / plain, pin 692c2e8: `vm-in-caps-simdna`
  12,546.2 ns vs `vm-caps-simdna` 28,996.9 ns — ×2.31, beyond
  2 × max(stddev) = 862.2 ns (mode: vm-in vs vm). Minimum: factored /
  plain, ×1.28.

## R-BUCKET-FORM — the regime artifact (2 firings)

- orig / match-compliance ranks rows of BOTH facts in one group: 7
  `separate artifact` (whole-subject) and 2 `same program` (plain).
  See: docs/design/record_schema.md §5
  See: docs/dev/pcrec_references.md (pcrec [OS-4])
- factored / match-compliance ranks rows of BOTH facts in one group: 3
  `separate artifact` and 2 `same program`.
  See: docs/design/record_schema.md §5
  See: docs/dev/pcrec_references.md (pcrec [OS-4])

## R-BUCKET-VSBEST — two pins in one ranking group (4 firings, aggregated to 1)

- 4 of 6 ranking groups carry 2 pin slug(s) (8da6120, 692c2e8):
  factored / short-subject-search; orig / short-subject-search;
  orig / match-compliance; orig / large-subject-throughput.
  See: reports/CLAUDE.md (reader's caveat)

## R-FLOOR-1 — a compile ratio inside the timer floor (2 firings, aggregated to 1)

- 2 compile row(s) on `libpcre2_10.46_interp-caps-simdna` read
  `timer-floor` (patterns: factored, orig): `min_ns` under
  `_TIMER_FLOOR_NS`, so the ratio measures the clock, not the compile.

## Rules that did not fire

| rule | reason |
|---|---|
| R-STATUS-1 | no-matching-rows (every included record is `measured`; `include_unmeasured: False`) |
| R-STATUS-4 | no-matching-rows (no did_not_compile row) |
| R-STATUS-7 | no-matching-rows (`mixed_x13: False`) |
| R-STATUS-8 | no-matching-rows (`worst_other_core_busy: n/a`) |
| R-STATUS-9 | no-matching-rows (no record reads `disagree`) |
| R-STATUS-10 | no-matching-rows (no record carries an `after:` failure) |
| R-STATUS-11 | no-matching-rows (no scratch row) |
| R-STATUS-13 | no-matching-rows (all 6 ranking groups carry a rankable reference arm) |
| R-DELTA-4 | input-absent (no predictions file for email-specimen@0.1) |
| R-RANK-1 | no-matching-rows (no cross-pin pair crosses 1.0 on ratio_vs_baseline) |
| R-FLOOR-2 | no-matching-rows (`floor_pattern: none`) |
| R-FLOOR-3 | no-matching-rows (highest compile jitter ratio is 0.645) |
| R-PRED-1 | input-absent (no predictions file) |
| R-PRED-2 | input-absent (no predictions file) |
| R-PRED-3 | input-absent (no predictions file) |
| R-PRED-4 | input-absent (no predictions file) |
| R-BUCKET-SPAN | no-matching-rows (8da6120 and 692c2e8 are adjacent in pin_order) |
| R-BUCKET-DOMINATED | input-absent (no subject-grain TSV supplied) |
| R-BUCKET-KB | no-registered-signatures (catalogue 1.0 registers none) |
```

Twelve rules fire, nineteen do not, thirty-one are named. Every
non-template sentence v1's specimen carried — the six the source critic
counted, including "Source: report.py `_cross_pin_verdict` …", "A ratio
between two different engines is not computed", "(min under 20 µs …)" and
the free-standing `n_gave_up` parenthetical — is gone or has become
either a `links` line, a declared `no_fire` sentence, or part of a
template. §8(5) would now accept this document; it would have rejected
v1's.

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

Three reports plus one synthetic. For each: what v1 MUST surface
unprompted, and what it MUST NOT claim. Every number below is from the
committed file. *(Revised per panel S3: v1's A.4 was both a MUST and "a
risk, not a pass", and its C.3 stated two different bars in one
paragraph. Both are now unambiguous — A.4 passes by rule, C.3 fails
plainly — and the missing null control is added.)*

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
   whole-subject ranks 1 and 2; large-subject-throughput ranks 1 and 2)
   — and as R-DELTA-3, **four** firings, the `now measured (was:
   gave-up)` clause on the large-subject-throughput pair AND the
   match-compliance whole-subject pair. The R-DELTA-2 + R-DELTA-3
   co-firing on those four cells is required: they are two clauses of
   one verdict string, not alternatives.
3. **The give-ups**, by code and smallest firing subject, as R-STATUS-3
   — all thirteen excluded cells, carrying
   `-2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B)`,
   `-3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B)` and
   `-4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B)` —
   including the `libpcre2_10.46_jit-caps-simdna` row whose exclusion
   the TSV cannot explain, rendered without a fabricated cause.
3b. **The STEPS-vs-WORK datum** as R-STATUS-12, on **three** testees
   (`pcrec_692c2e8_vm-caps-simdna`, `pcrec_692c2e8_vm-in-caps-simdna`,
   `pcrec_8da6120_vm-caps-simdna`): subject `t-c-long-atom-run` gives up
   as `-2:PCREC_ERR_STEPS` on `factored` and `-4:PCREC_ERR_WORK` on
   `orig`, same regime — the second of the two rule facts the journal's
   part-7 entry sent to [B13]. A v1 that surfaces the give-ups but not
   this pairing has implemented half the charter.
4. **The vm-in result**, as **R-ARM-1**, by rule and by number:
   `orig` / short-subject-search / plain, pin 692c2e8, `vm-in` 12,546.2
   ns vs `vm` 28,996.9 ns, ×2.31 beyond a spread of 862.2; and `orig` /
   match-compliance / whole-subject, `vm-in` 62,732.3 vs `vm` 80,227.6,
   ×1.28 beyond 318.8. *(v1 could not surface this and said so; the
   panel required the R-ARM class rather than accepting the gap. This
   item is now an ordinary MUST, not a risk.)*
5. **The unpredicted Δ** as R-DELTA-1, **three** firings: `faster ×1.19`
   (factored / short-search / vm), `faster ×1.26` (orig / compliance /
   vm) and `faster ×1.00` (orig / compliance / auto-nocaps). The first
   two are the numbers `feedback_…-repin-v2.md` §2 demanded be flagged
   "as loudly as a regression"; the third is required because omitting it
   is how v1's own specimen and acceptance item disagreed with the data.
6. **The regime artifact** as R-BUCKET-FORM on `orig` /
   match-compliance and `factored` / match-compliance — one firing per
   GROUP, both groups holding two forms because `form` is not in the
   group key.
7. **The mixed schema population** as R-STATUS-6 (`1.1,1.2`), carrying
   the `n/a (v1.x)` agreement provenance for all nine records.
8. **R-STATUS-9 must NOT fire.** All nine records read `n/a (v1.x)`,
   which is provenance about their age, not a trial disagreement. A rule
   that fires here is the false positive B2 was about.

MUST NOT claim: any cause for (5); that vm-in is "better" (R-ARM-1 states
a ratio and a spread, never a preference); that the collapse is wave G's
splice; any exclusion cause for the jit throughput row in (3).

### Report B — `reports/2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.tsv`
*(the current cross-pin wave)*

MUST surface:

1. **R-RANK-1 on `cls-upto-8192` / match-compliance / whole-subject /
   config `auto-caps-simdna`**: `ratio_vs_baseline` 1.788241 at 334fd10e
   → 0.269358 at d34c9131 — the cell crossed the reference arm. The
   group carries a rankable reference arm, so the R-STATUS-13 guard does
   not suppress it.
2. **R-DELTA-2 on that same cell**: `selection changed (dfa → vm)`.
   The co-firing is required; a v1 that fires only one of the two on a
   cell that carries both is failing.
3. **R-BUCKET-SPAN on the `vm-in` rows**: their Δ partner is 288d505,
   not 334fd10e — non-adjacent in `[[pin_order]]` (288d505 → 334fd10e →
   d34c9131), e.g. `cls-upto-1024` / large-subject-throughput / plain,
   `pcrec_d34c9131_vm-in-caps-simdna`, `faster ×1.53`, and
   `cls-upto-1024` / short-subject-search / plain, `faster ×1.25`. The
   fact reports/CLAUDE.md records by hand today.
4. **R-BUCKET-VSBEST** on every group carrying ≥ 2 pin slugs, including
   the visual inversion on `cls-upto-1024` / short-subject-search
   (334fd10e ranks 1 at 989.819865 ns; d34c9131 ranks 2 at 998.441155;
   the Δ reads `slower ×1.01`).
5. **R-RANK-1 on the `dig-*` throughput rows**, at least
   `dig-exact-8`, `dig-upto-8`, `dig-exact-16`, `dig-upto-16`,
   `dig-exact-32` on config `vm-in-caps-simdna` (288d505 reads 1.081 /
   1.058 / 1.591 / 1.603 / 1.770 and d34c9131 reads 0.643 / 0.620 /
   0.946 / 0.951 / 0.926) — five firings, which is the rule showing it
   is not a one-off.
6. **R-DELTA-1's 202 firings rendered as 17 aggregated bullets**, each
   carrying its count and its extremal cell, with all 202 in the facts
   TSV. A v1 that prints 202 bullets has failed the legibility
   requirement §5.2 exists for, and one that prints fewer than 202 rows
   in the facts TSV has dropped a fact.
7. **R-DELTA-4 must NOT fire** (no predictions file is supplied): it
   reports `input-absent`. A v1 that fires it 202 times has turned "flag
   the unpredicted Δ" into "flag every Δ".

MUST NOT claim: that the STEP 2 match-axis customers moved (they did
not — ledger 2026-09-05, O-16); any attribution for the crossings.

### Report C — `reports/2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.tsv`
*(the newest sample, and a set with a floor pattern)*

MUST surface:

1. **R-STATUS-4 on the refusal population**: 172 `did_not_compile` rows
   reducing to the 60 distinct (pattern, testee) pairs and rendering as
   four aggregated firings (one per pcrec testee, 15 patterns each),
   each pattern with pcrec's own diagnostic verbatim (`module
   'conditionals' is enabled but (?(...) is not implemented yet (pattern
   offset 8)`, etc.).
2. **R-STATUS-3 on the 23 excluded cells**, including `rec-1` /
   large-subject-throughput at `pass_rate 0.0000` with 15 wrong answers
   on five testees, and `asr-k-uc` / match-compliance / whole-subject at
   `0.9762` with 5 wrong answers on four pcrec arms.
3. **R-BUCKET-KB does NOT fire, and the sidecar says
   `no-registered-signatures`.** This is a STATED KNOWN GAP of v1, not a
   MUST-surface item. v1 claimed KB-13 and KB-14 would be recognised
   from their signatures and called it "v1's strongest claim"; measured,
   the signature text occurs zero times in the report at any grain, and
   what the TSV supports — `(regime, form, n_wrong > 0, n_gave_up == 0)`
   — cannot discriminate KB-13's rows from KB-14's or from an unrelated
   future defect of the same shape. **v1 does not find those defects, and
   this note says so rather than softening it.** What v1 does surface on
   this sample is the exclusion inventory (2) and the refusal inventory
   (1), from which a reader reaches the same cells in minutes.
4. **R-FLOOR-2 on `anc-caret` / short-subject-search /
   `pcrec_d34c9131_vm-caps-simdna`**: 246.457657 ns / 42 = 5.868
   ns/subject against the `floor` pattern's 800.098671 / 42 = 19.050 —
   the ranked cell is 0.308× the set's own per-call control. This
   requires precondition P-1: the floor pattern comes from the header
   key, never from `bench/syntax/subbench.toml`.
5. **R-FLOOR-1 on the 190 compile rows reading `timer-floor`**, rendered
   as two aggregated firings (95 rows on each libpcre2 arm), against the
   644 compile rows carrying a real ratio (161 on each pcrec arm).
6. **R-STATUS-9 must NOT fire** — all six records read
   `agree (0 of N groups …)`. A rule that fires here is a false positive
   and fails the acceptance test.
7. **R-ARM-1's 635 firings rendered as 12 aggregated bullets**, all 635
   in the facts TSV.

MUST NOT claim: that `\G` is not treated as an anchor (ledger §4.1,
Q4 — a mechanism question, not a fact in the TSV); that the interpreter
found KB-13's *cause* (the ctypes probe that established
`PCRE2_ERROR_JIT_STACKLIMIT` is not something `interpret` can or should
do); any of NOTES.md's R2/R4/R7 band verdicts (out of scope, §1.1).

### Report D — the synthetic clean report (the null control)

`catalogue/fixtures/CLEAN__all-measured/` (§8(4)): a generated,
reporter-shaped report in which every record is `measured`, no cell is
excluded, no pattern fails to compile, no Δ is outside spread, no arm
pair is outside spread, there is one pin and one schema version,
`mixed_x13: False`, `worst_other_core_busy: n/a`, and
`floor_pattern: none`. **All 31 rules must report `fired=0`.** This is
the false-positive control §10 otherwise lacks and cannot have: R-STATUS-5
and R-FLOOR-1 fire on essentially every real committed report, so
"quiet on a quiet report" is only demonstrable on a constructed one.

### The promise, in one sentence

**Catalogue v1 is accepted iff, run on Reports A, B and C with no
predictions file and no human hint, it surfaces every numbered MUST item
above and asserts none of the MUST-NOT items, and iff it fires zero rules
on Report D.** Item C.3 is a declared known gap and is not part of the
promise; item A.4, which v1 could not meet, is met by R-ARM-1 and is an
ordinary MUST.

---

## §11. Open questions

Of v1's eight, seven were ruled by the r4 panel and are recorded here as
settled. One remains Frank's.

- **Q1** (which input names the floor pattern) — **RULED: the reporter
  emits `floor_pattern:`**, precondition P-1 (§2.5). v1's
  `subbench.toml` read is removed: it re-created KB-2 and the version
  skew is live today.
- **Q2** (subject-grain input for R-BUCKET-DOMINATED) — **RULED: (a)**,
  `input-absent` until a separate reporter change commits
  `<name>.subject-grain.tsv` for every group.
- **Q3** (should set-local outlier bands, `bench/*/NOTES.md`'s R0-R7,
  become catalogue-readable data in `subbench.toml`?) — **OPEN, Frank's
  call.** §1.1 says not in v1. For: the bands are already written before
  every run, and a machine that checks them is exactly this tool.
  Against: a band is a judgement, and mechanising it invites the
  catalogue to acquire opinions by increments. No r4 finding bears on it
  either way. **This is the only question in this note that is not
  settled.**
- **Q4** (who phrases: the skill or the renderer) — **RULED, no
  deviation** (§7.4): the renderer phrases, the templates are
  human-reviewed prose authored once before any run, §8(6) gates their
  diffs, and the `## Reader's note` fallback is rejected outright.
- **Q5** (back-fill sidecars for all 42 reports, or only the acceptance
  set?) — **RULED: the three acceptance reports at landing, the rest on
  demand.** The cost that matters is review weight, not CPU (§8's
  budget note), so the blast radius stays small.
- **Q6** (should a fired R-STATUS-9 or R-BUCKET-KB ever be a non-zero
  exit?) — **RULED: no.** The instrument/gate separation is the one BD7
  and schema v1.4 drew; a gate that reads a report is a different design.
- **Q7** (catalogue-as-data vs executable predicate) — **RULED: keep the
  split.** A DSL is a second language to get wrong, §8(1) makes drift a
  build failure, and the correspondence mechanism is ~30 lines with a
  working precedent in `schema/check_rules.py`.
- **Q8** (R-STATUS-12 parsing a rendering) — **RULED: option (b),
  promoted to precondition P-2** (§2.5). The parse is gone.

Two questions this revision opens, neither blocking:

- **Q9.** Should the reporter emit an exclusion-cause column
  (`_set_cell_failure_reason`'s existing one-word class)? It would let
  R-STATUS-3 say why a cell was excluded on the rows where the count
  columns are silent. Recorded as a follow-up in §2.5; not required for
  any rule to be correct.
- **Q10.** `[[pin_order]]` must be appended at every re-pin, or
  R-BUCKET-SPAN exits 2 on the next report that carries the new pin.
  Should that append be a line in the re-pin checklist
  (`testees/pcrec/CLAUDE.md`, the manager skill) or an item in
  `make check-interpret`'s failure message only? **Recommendation: both**
  — the checklist prevents it, the exit-2 message with the missing slug
  named makes the fix obvious.

---

## §12. What this note deliberately does not decide

- The exact python module layout of `interpret.py` beyond the renderer
  contract (§7.1-7.2), the view contract and the `inputs` grammar
  (§3.2.2) — those three ARE decided here, because they are contracts
  two implementations could otherwise satisfy differently while each
  passed its own tests.
- The wording of any individual template beyond the shapes shown — a
  template's wording is a MINOR catalogue bump, a lane's call, and a
  human review under §8(6).
- Whether `interpret` ever gains a second output consumer (a dashboard,
  a CI annotation). v1 has two: the sidecar and a human running it.
- Anything about `~/pcrec`. This tool reads this repository's own
  artifacts only (BD2).

One implementation detail is fixed here rather than left open, because
it is a determinism property rather than a style choice: **every
`open()` and `write()` in `interpret.py` passes `encoding="utf-8"`
explicitly.** `delta_verdict` carries `×` (U+00D7) and `→` (U+2192) and
`_gave_up_cell_summary` carries `×`; `report.py`'s `main()` sets
`LC_ALL=C` and the Makefile sets it for `check-harness`, and on a box
where that yields an ASCII default encoding an implicit `open()` would
raise on read and the golden compare would be non-reproducible. Cheap
insurance for pcrec D2's stranger's-`make` posture.

---

## §13. What the r4 panel found sound, recorded so a later pass does not sand it off

- **No rule introduces a tuned constant.** Every threshold in §4
  re-derives to a token the reporter already computed (`timer-floor`,
  `faster ×N`, `selection changed`, `agree`/`disagree`), a header
  integer, or a definitional 1.0 named as definitional. R-ARM-1, added
  in v1.1, copies `_cross_pin_verdict`'s arithmetic rather than choosing
  a bound, so the property survives the addition.
- **"The interpreter must never be able to disagree with the report
  about whether something moved"** (§4.2) — the correct architectural
  choice, correctly implemented by reading the verdict string.
- **Reading the TSV and never the markdown** (§1), with the reason given.
- **§6.5's `stated_utc` precedence check**, checked against the earliest
  index timestamp for the population INCLUDING superseded records
  (corrected in this revision, cross-review I-58) — closes the
  supersession window a report-scoped check leaves open, though it
  proves only that a prediction predates the population's first-ever
  measurement, stated as the honest residual rather than "mechanically
  impossible."
- **§8(4)'s minimum-diff control requirement** — this project's
  controls-share-no-source discipline applied to a new surface; v1.1
  keeps the requirement and makes it computable ("exactly one declared
  field differs").
- **Writing §10 before any code exists**, which is why a panel could
  find eleven blocking defects at the cost of one design pass instead of
  a lane's first week.
