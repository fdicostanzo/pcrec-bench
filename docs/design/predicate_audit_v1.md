# THE PREDICATE AUDIT — a design note (v1, 2026-09-18)

**Status: PROPOSED, not adopted. D6-panel input. NO code and NO catalogue
change in this lane** — nothing under `pcrecbench/`, `catalogue/`,
`reports/`, `schema/` or `store/` is touched. The note proposes; fixes
land on a ruling.

Written by lane `b50predaudit` on Frank's standing directive of
2026-09-17 — `docs/dev/plan.md`'s `[B42]` tail charter (i), recorded as
the wider half of `interpret_subject_grain_v1.md` §6 Q7's ruling:

> *"audit the other predicates/queries for the same class of
> structurally-incomplete answer, and make results carry the context
> around their numbers, especially where a Claude session is the
> consumer."*

The class, named for its first instance: **P5** — *a verdict read from a
population that cannot contain the counterevidence that would refute it.*
On `bench/capability@0.1`'s first sample, prediction P5 read `n_wrong eq 0`
over `_select`'s default `rank` section and the interpreter reported
**confirmed**, while every wrong-answer row in the corpus sat in the
`excluded` section by construction. The measurement that settled it
(`interpret_subject_grain_v1.md` §5.2, re-derived larger for this note in
§0 below) is that **no `rank` row in any committed report has ever carried
`n_wrong > 0`**: the verdict was not merely wrong, it was unfalsifiable.
Rulings (α) and (β), landed with catalogue 2.0, fixed that instance.

This note is the systematic sweep for every other instance. It audits all
**31 catalogue rules** and all **17 prediction-scoring quantities** against
four questions, and it audits the **rendered sentences** separately, because
a sound predicate rendered as a sentence that omits its population is the
same failure one step later.

**What it found, in one paragraph.** Eight defects are LIVE — a committed
sidecar renders a structurally unsound verdict today — of which the sharpest
three are: R-FLOOR-2 renders *"no ranked cell is at or below its set's own
floor pattern"* on a report whose set has **no floor pattern at all** and
where the rule therefore never evaluated anything (and `interpreter_v1.md`
§4.5 specifies a different rendering, so this is a build deviation, not a
design gap); R-DELTA-4 renders *"no prediction … selects that cell"* about
cells a prediction names **by name** but could not evaluate; and
R-BUCKET-DOMINATED renders a dominance share *"of this cell's total"* for
eight cells the same report **excluded from ranking**, over a denominator
that silently omits the subjects that failed. Fourteen further defects are
silent omissions or latent. Two narrowings audited clean, and are recorded
as clean so a later pass does not "fix" them.

---

## §0. What was measured in this lane, and how

Five read-only probes, archived with their scripts and verbatim output at
`docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` +
`…-probe{1..5}.py`. Every probe imports `pcrecbench.interpret`'s **own**
functions (`parse_selector`, `_glob_match`, `_select`, `_sections_for`,
`_keyed_values`, `_reduce`, `_op_holds`, `_measured_text`, `_elsewhere`,
`split_testee`, `config_of`, `is_reference`, `r_arm_1`,
`r_bucket_dominated`, `evaluate_predictions`) rather than reimplementing
any of them — the same discipline `interpret_subject_grain_v1.md` §0 used,
for the same reason: an audit that reimplements the predicate audits its
own reimplementation.

| # | probe | what it establishes |
|---|---|---|
| **M1** | a (section × column × metric) census over all **45** committed set-grain report TSVs | which columns are ever non-empty in which section — the structural facts every (c) answer rests on |
| **M2** | every clause of both committed predictions files re-resolved through `_select` / `_sections_for` / `_keyed_values` | the real population, row count, distinct-cell count and per-section split of each clause |
| **M3** | `_reduce` + `_op_holds` + `_measured_text` replayed per clause against the true min/max | what the rendered "worst … over N value(s)" sentence says against what the population actually holds |
| **M4** | the per-rule blind-spot search (arm pairs with a refused arm; cross-pin pairs with an unranked side; `floor_pattern` header values; non-finite numerics; `not_ranked`/`scratch` occupancy) | whether each at-risk population has a real witness in the corpus, and how many |
| **M5** | the Δ-partner divergence and the give-up subject coverage | R-BUCKET-SPAN's partner population against the reporter's own; R-STATUS-12's subject population against the subjects that gave up |

**The corpus, as of this lane** (`HEAD` = `4eb413a`, catalogue 2.0,
reporter v17, `interpreter_v1.md` v1.4): 45 committed set-grain report
TSVs, 3 committed `.subject-grain.tsv` slices, 2 committed predictions
files (50 clause rows), 6 committed `.interpretation.md` sidecars.

**The four structural facts the whole audit rests on** (M1, all MEASURED):

1. **`rank` rows: 103,488 across the corpus, ZERO with `n_wrong > 0` or
   `n_gave_up > 0`.** (The v1.4 note's figure was 92,892 over 43 reports;
   the two newer capability reports do not change the zero.) `excluded`:
   229 rows, **211** carrying one or both.
2. **A `rank` cell is exactly SIX rows.** 17,248 cells × 6 metric rows
   (`median_ns`, `min_ns`, `max_ns`, `stddev_ns`, `ratio_vs_baseline`,
   `ratio_vs_best`), and `n_wrong`/`n_gave_up`/`pass_rate`/`status` are
   identical on all six. No cell in the corpus has any other row count.
3. **Each section's always-empty columns are a hard constraint on every
   selector.** `compile` rows carry NO `subject_or_na`, `regime_or_na`,
   `status`, `pass_rate`, `n_gave_up`, `n_wrong` or `delta_verdict`.
   `did_not_compile` rows carry NO `form`, `fact`, `metric`, `value`, `n`,
   `pass_rate`, `n_gave_up`, `n_wrong` or `delta_verdict` — only
   `pattern`, `subject_or_na`, `regime_or_na`, `testee`,
   `status` (`did-not-compile`) and the diagnostic in `gave_up_summary`.
   `excluded` rows carry NO `rank_or_na` or `delta_verdict`.
4. **`not_ranked` and `scratch` have ZERO rows in all 45 reports.** Every
   finding about them below is latent by construction, and said to be.

---

## §1. The audit's four questions, and what counts as an answer

For every rule and every prediction quantity:

- **(a) What population does its predicate actually read?** Named by code
  path, not by the catalogue's prose — where the two differ, that is
  itself a finding (F11).
- **(b) What counterevidence class would refute the verdict it renders?**
  The verdict is not only a firing: a rule that does not fire renders its
  `no_fire` sentence, which is a claim about the whole population and is
  the more dangerous of the two, because nobody double-checks a negative.
- **(c) Can that counterevidence appear in the population it reads?**
  yes / no / partially, with the structural reason.
- **(d) If no or partially:** the concrete failure shape with a real
  witness where one exists, a severity, and a candidate fix.

**Three distinctions the table keeps.** A *false sentence* (the tool
asserts something untrue) is worse than a *silent omission* (the tool
fails to assert something true), which is worse than a *latent* hole (the
population is incomplete but the corpus has never exercised it). And a
*deliberate, stated* narrowing — R-BUCKET-FORM's rankable-only read, say —
is not a defect at all; it is recorded as sound so a later pass does not
sand it off (`interpreter_v1.md` §13's own rule).

---

## §2. THE AUDIT TABLE — the 31 rules

`V` = verdict: **S** sound · **L** latent · **O** silent omission ·
**D** live defect (a committed sidecar is affected).

| rule | (a) population read (code path) | (b) counterevidence that would refute it | (c) reachable? | V |
|---|---|---|---|---|
| R-STATUS-1 | `record` rows joined to `index` by `record_id_of`; `interpret.py:558-571` | an included record whose index status is not `measured` — **or whose id joins to no index row at all** | **partially**: `hit is None → continue` treats an unjoined record as measured; the `no_fire` asserts the join succeeded | **O** F12 |
| R-STATUS-2 | `index` rows filtered by the header's own `subbench_versions` × `machines`; `:574-601` | a non-measured index row in the population | yes — the index is the whole store's | S |
| R-STATUS-3 | `excluded?metric=pass_rate`; `:604-614` | an excluded cell not reported | yes — every excluded base row fires | S |
| R-STATUS-4 | `did_not_compile`, deduped to (pattern, testee); `:617-626` | a refusal not reported | yes | S |
| R-STATUS-5 | three header integers; `:629-638` | a candidate dropped for a fourth reason | **partially**: the header carries only these three classes; a reason the reporter does not count is invisible to any rule | L |
| R-STATUS-6 | `header.schema_versions` + `record` agreement strings; `:648-656` | a mixed population | yes | S |
| R-STATUS-7 | `header.mixed_x13`; `:659-662` | a mixed X13 population | yes (the reporter's own boolean) | S |
| R-STATUS-8 | `header.worst_other_core_busy`; `:665-669` | — (a fact, not a verdict) | n/a; the **rendering** is the issue (F22) | **D** F22 |
| R-STATUS-9 | `record` agreement strings prefixed `disagree`; `:672-679` | a disagreeing record | yes; a pre-v1.4 record reads `n/a (v…)` and is R-STATUS-6's, by design | S |
| R-STATUS-10 | `record.delta_verdict` prefixed `after: `; `:682-691` | a failed after-sample | yes | S |
| R-STATUS-11 | `scratch` rows; `:694-701` | a scratch row in a report | yes — but **0 such rows exist corpus-wide** | L |
| R-STATUS-12 | `excluded?metric=giveup_smallest`; `:704-724` | a subject giving up under two codes on two patterns | **partially**: the reporter emits ONE row per (cell, code) naming the SMALLEST firing subject. MEASURED: 188 subjects gave up corpus-wide, **76** are named (40%), 1 row per cell in every case. A subject that is not the smallest for its code is unreachable | **O** F18 |
| R-STATUS-13 | `rank?metric=median_ns` grouped by (pattern, regime); `:734-747` | a rankable reference arm in the group | yes — rankable rows are exactly `rank` rows, so the predicate IS the reporter's condition | S |
| R-DELTA-1 | `rank?metric=median_ns` rows with a non-empty `delta_verdict`, matched `^(faster\|slower) ×`; `:762-781` | **a cell that moved so far it left the ranking** — a regression into wrongness, give-up or refusal | **no**: `delta_verdict` is written only in the rankable loop (`report.py:4517-4520`), and the reporter has no "was measured, now failing" verdict at all. The improvement direction has R-DELTA-3; the regression direction has nothing | **O** F10 |
| R-DELTA-2 | the same rows, `^selection changed \(`; `:800-801` | as R-DELTA-1 | no, same reason | **O** F10 |
| R-DELTA-3 | the same rows, `^now measured \(was: `; `:804-805` | — (the improvement direction, which the reporter does compute) | yes | S |
| R-DELTA-4 | `ctx.prediction_coverage`, built ONLY from clauses whose `_select` returned rows (`:2035-2038`) | **a prediction that DOES name the cell but was not evaluable** | **no**: a not-evaluable clause `continue`s before `coverage.add`. MEASURED: 6 of 10 capability predictions are not-evaluable and contribute zero coverage | **D** F3 |
| R-RANK-1 | `rank?metric=ratio_vs_baseline` + `median_ns` in a group with a rankable reference; `:830-875` | a crossing pair one of whose ratios is exactly `1.000000` | **partially**: `(r_a-1)*(r_b-1) >= 0 → continue` skips a product of zero | L F17 |
| R-ARM-1 | `rank` `median_ns` + `stddev_ns`, same engine+pin+form, config one token apart; `:880-928` | **an arm pair one of whose arms did not compile** — the largest possible arm difference | **no**: a refusal has no `rank` row. MEASURED: **532** (cell, ranked arm, refused arm) triples in the corpus satisfy R-ARM-1's own one-token rule and are unreachable | **O** F9 |
| R-FLOOR-1 | `compile?metric=jitter` = `timer-floor`; `:933-942` | a timer-floor compile cell not reported | yes. MEASURED: 1,266 of 12,741 compile cells carry no jitter row, and all 1,266 are exactly the refusal cells (empty median) — a cell with no compile time **has** no jitter, so no counterevidence can live there | S F23 |
| R-FLOOR-2 | `header.floor_pattern` + `rank?metric=median_ns`; `:945-981` | a ranked cell at or below the floor — and, for the `no_fire`, **the possibility that no comparison was made** | **no** for the second: `floor_pattern` absent / `none` / multi-valued returns `no-matching-rows`, and the renderer pairs that token with a verdict sentence. Separately **partially** for the first: a cell whose floor arm is itself excluded is skipped silently (`fm is None → continue`) | **D** F1 + **O** F1b |
| R-FLOOR-3 | `compile?metric=jitter`, ratio ≥ 1.0; `:984-1001` | a high-jitter compile cell not reported | yes, same as R-FLOOR-1 | S F23 |
| R-PRED-1..4 | see §3 | see §3 | see §3 | **D** |
| R-BUCKET-FORM | `rank?metric=median_ns` `fact` values, RANKABLE only; `:1006-1019` | a group whose second-form row was excluded | **no — and deliberately**: the catalogue's own predicate states the narrowing and its reason ("a group whose only `separate artifact` row was excluded is not a group where two forms rank together") | S F24 |
| R-BUCKET-VSBEST | distinct pcrec version slugs among `rank` rows; `:1022-1037` | a second pin in the group | yes (an existence rule over exactly the ranked population `ratio_vs_best` is computed over) | S |
| R-BUCKET-SPAN | `rank` rows with a `delta_verdict`, partner searched **within the same (pattern, regime, form) cell's rank rows**; `:1040-1089` | a Δ whose partner is not a rank row of that cell | **no**: the reporter picks the partner from `record_ts_by_testee` × `set_cells` — every reduction cell, rankable or not (`report.py:2729-2752`). MEASURED: 4 rows on the capability AFTER report carry a Δ whose partner is in `excluded`; the rule finds no partner and skips, while its `no_fire` asserts every Δ is adjacent | **O** F11 |
| R-BUCKET-DOMINATED | the `--subject-grain` slice's `rank?metric=median_ns`; `:1092-1122` | a failing subject inside the cell, and the fact that the set cell may not rank at all | **no**: the slice's `rank` rows are the surviving subjects only; the excluded ones are in its `excluded` section, which the rule's `inputs` do not name. MEASURED: **8 of 33** firings on the capability AFTER report are about set cells the report EXCLUDED | **D** F4 |
| R-BUCKET-KB | `ctx.catalogue["signature"]`; `:1125-1130` | a registered signature | yes (none registered); the **rendering** is stale prose | **D** F5 |

---

## §3. THE AUDIT TABLE — the prediction-scoring quantities

The scoring path is `_sections_for` → `_select` → `_value_of` /
`_keyed_values` → `_reduce` → `_op_holds` → `_measured_text`, rolled up by
`evaluate_predictions`. Each stage has its own population question.

### §3.1 By quantity

| quantity class | default population (`_sections_for`) | counterevidence reachable? |
|---|---|---|
| `median_ns`, `min_ns`, `max_ns`, `stddev_ns`, `ratio_vs_baseline`, `ratio_vs_best`, `rank_in_group` (7) | `rank` | **partially.** A cell that regressed out of the ranking is absent; (β) now names the section it went to, which is the honest answer — but only when the selector can MATCH there (F7b). |
| `n_wrong`, `n_gave_up`, `pass_rate`, `status` (4) | `rank` ∪ `excluded` (base rows) — ruling (α) | **yes, but diluted 100-158:1** (F13), and still omitting `not_ranked` (inert, §0 fact 4) and `did_not_compile` (where all four columns are EMPTY, §0 fact 3 — so widening there would add rows and no values; (β)'s annotation is the only honest route, and this note does not propose widening). |
| `compile:median_total_ns`, `compile:artifact_bytes`, `compile:emit_bytes`, `compile:emit_code_bytes` (4) | `compile` | **no for refusals** — a refused pattern has no compile metric row. (β) annotates `did_not_compile`, correctly; it also annotates `excluded`, which for a compile claim is a **different population entirely** (F7). |
| `delta_verdict` (1) | `rank` | yes at set grain; **structurally empty at `grain=subject`** — 0 of 202,794 subject-grain rank rows carry one (`interpret_subject_grain_v1.md` §2.3) (F15). |
| `section` (1) | `rank` | **no**: with no explicit `section=` clause the only value readable is the literal `rank`, so the claim is decided before any measurement (F15). Both committed `section` clauses name `section=` explicitly and so escape it. |

### §3.2 By stage

| stage | the population question | verdict |
|---|---|---|
| `_sections_for` | §3.1 | see above |
| `_select`'s `excluded` scoping | the `metric=pass_rate` scope applies **only** under the (α) default, not under an explicit `section=excluded` | **D** F14 — and `metric` is not a selector key, so an author cannot separate them |
| `_keyed_values` | a row whose quantity column is empty or non-finite is DROPPED (`_float_or_none`) | sound, and the reason `did_not_compile` cannot be widened into |
| `_reduce` (`ratio_to`) | the denominator's own population size is never stated; `med = sorted(denom)[len//2]` silently collapses N values to one | **O** F6b |
| `_reduce` (`count`/`median`/`max`/`min`) | reduces over ROWS, which for a rank quantity is 6× the cells | **D** F6/F13 |
| `_op_holds` | a non-numeric quantity with a numeric op raises a bare `ValueError`, not an `InterpretError` — `main()` does not catch it | **L** F15 (traceback, not the exit-2 named error the discipline requires) |
| `_measured_text` | picks the extreme by max, irrespective of the op's direction | **O** F16 |
| `_elsewhere` (β) | re-runs the SAME selector against the other sections — so a clause naming a column those sections leave EMPTY is blind there | **D** F7b |
| `evaluate_predictions` roll-up | `partial` discards `claim`, `measured` AND `reason`, all three computed | **D** F8 |

---

## §4. Findings, ranked

Severity is the product of *how wrong the sentence is* and *how likely a
reader acts on it*. Frank's directive makes a Claude session the reader of
record, and a Claude session does not double-check a negative.

### F1 — LIVE, HIGH. R-FLOOR-2 renders a verdict it never evaluated

`r_floor_2` (`interpret.py:946-948`) returns the did-not-fire token
`no-matching-rows` when the header's `floor_pattern` is absent, `none`, or
multi-valued. `render_markdown` (`:1580-1581`) pairs every token with the
rule's own `no_fire` sentence, so the sidecar reads:

> `| R-FLOOR-2 | no-matching-rows (no ranked cell is at or below its set's own floor pattern on the same testee and regime) |`

**Witness, committed:**
`reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.interpretation.md:152`,
whose report header reads `floor_pattern: none` (MEASURED: 2 of 45
committed reports do, and this is the one with a sidecar). **The set has no
floor pattern; no cell was compared to anything; the rendered sentence
asserts the negative result of a comparison that did not happen.**

This is a **build deviation, not a design gap**: `interpreter_v1.md` §4.5
specifies the intended rendering verbatim — *"On Report A the rule reports
`no-matching-rows (floor_pattern: none)`"*. The code has no channel for
that parenthetical, because `DID_NOT_FIRE_TOKENS` is a closed set of six
bare strings and the renderer always substitutes `no_fire`.

**Fix shape.** A per-rule did-not-fire REASON channel: a rule may return
`(token, reason)` where `reason` is drawn from a closed, slot-free set
declared in the rule's own block, and the renderer prints
`token (reason)` in place of `no_fire` when one is given. That closes F1,
F2 and the F5 class in one mechanism, keeps the opinion firewall intact
(the reason strings are declared prose under §8(6) review, like `no_fire`),
and needs no predicate to move. **Version: MINOR + §8(6) review + full
sidecar regeneration** (§3.3's own rule). The alternative — returning
`input-absent` instead — is cheaper still but leaves the sentence
mismatched for every other rule with the same shape.

### F2 — LIVE, HIGH. R-DELTA-4's `input-absent` renders a coverage claim

Identical mechanism, different rule. With no predictions file the rule
returns `input-absent` and the sidecar reads *"input-absent (every finding
of R-DELTA-1, R-RANK-1, R-ARM-1 and R-FLOOR-2 is covered by a prediction
selector)"* — a claim of complete coverage rendered because there was
nothing to cover with. **Witness:** the same sidecar, line 150; also the
bounded and email sidecars. The catalogue's own predicate says the right
thing (*"With no predictions file supplied the rule reports `input-absent`:
'no prediction covers this cell' is then universally true, and flagging
every Δ is flagging none"*) — the `no_fire` sentence does not. Fix: F1's
reason channel, or a reworded `no_fire`.

### F3 — LIVE, HIGH. R-DELTA-4 denies a prediction that names the cell

`coverage` is populated only from clauses whose `_select` returned rows
(`interpret.py:2035-2038`); a clause that is `not-evaluable` — for any of
the three causes `interpret_subject_grain_v1.md` §1.2 enumerates — reaches
`continue` first and contributes nothing.

**Witness, committed:**
`reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.interpretation.md`'s
R-DELTA-4 block names *"codegrammar-flat / large-subject-throughput / plain
/ `pcrec_cf0962e3_vm-in-caps-simdna` and no prediction in
docs/dev/predictions/capability-0.1-first.tsv selects that cell"* — while
P3's selector in that very file reads
`pattern=codegrammar-flat;subject_or_na=t-1m;regime_or_na=large-subject-throughput;…`.
P3 names the cell; it was not evaluable (its `subject_or_na=t-1m` clause
cannot match a set-grain row); the tool says no prediction names it.
MEASURED: 6 of 10 capability predictions are not-evaluable, contributing
zero coverage, against 777 R-DELTA-4 firings.

**Fix shape.** The catalogue's own `threshold_src` already describes the
right predicate — *"the coverage test is a prediction selector's own glob
match"* — so compute coverage from the **selector**, not from the rows it
happened to match: a firing cell is covered when some clause's selector
glob-matches its (pattern, regime, form, testee), evaluable or not. Then
split the rendering in two, because the two facts are different and both
matter: *no prediction names this cell* vs *the prediction that names it
(P3) was not evaluable*. **Version: this changes which cells a rule fires
on → MAJOR**, on the honest reading of §3.3, even though it is a bug fix
against the catalogue's own stated predicate. The panel should rule which
label applies when code and catalogue prose disagree and the prose is
right.

### F4 — LIVE, HIGH. R-BUCKET-DOMINATED's total is not the cell's total

The rule sums `median_ns` over the subject-grain slice's `rank` rows
(`interpret.py:1104-1114`). Those are the SURVIVING subjects: a subject
that gave up or answered wrongly is in the slice's `excluded` section,
which the rule's `inputs` do not name. Two consequences, both rendered:

1. **The denominator omits the failures.** The share is "this subject over
   the subjects that worked", presented as *"{share} of this cell's total"*.
2. **The cell may not be a ranked cell at all.** A set cell excludes if ANY
   subject fails, so the rule reports dominance for cells the set-grain
   report refused to rank.

**Witness, committed**, in the capability AFTER sidecar's R-BUCKET-DOMINATED
block: *"evil-alt-nested / short-subject-search /
`libpcre2_10.46_interp-caps-simdna`: subject `lp-atomic-nonmatch` is 94.6%
of this cell's total"* — and eleven lines earlier, in the same sidecar's
R-STATUS-3 block, *"evil-alt-nested / short-subject-search / plain /
`libpcre2_10.46_interp-caps-simdna` is EXCLUDED from ranking: pass-rate
0.9733; 0 wrong answer(s); 10 give-up trial(s)"*. MEASURED: the share is
computed over **73** ranked subjects while **2** subjects of the same cell
sit in the slice's `excluded` section; **8 of the 33 firings** are on
set cells the report excluded (25 are on ranked cells).

**Fix shape.** Two slots and a template clause: the ranked-subject count in
the denominator, and the excluded-subject count beside it — (β)'s principle
applied to a rule instead of a prediction. Reading the slice's `excluded`
rows is an `inputs` change → **MAJOR**; the template change is MINOR +
§8(6). A cheaper interim: state the denominator's subject count only
(already available from the rows the rule reads) — MINOR, and it at least
stops "this cell's total" reading as the set cell's total.

### F5 — LIVE, MEDIUM. R-BUCKET-KB's `no_fire` names the wrong catalogue

*"catalogue 1.0 registers no signature"*, rendered on all six committed
sidecars at catalogue **2.0**. The sentence was true when written and is a
version-pinned assertion inside prose that no bump rewrites. Fix: reword
version-independently (*"no signature is registered in this catalogue"*).
MINOR + §8(6). Worth a `check-interpret` assertion of its own: no
`template`/`no_fire`/`legend`/`example` string may name a
`catalogue_version` literal.

### F6 — LIVE, MEDIUM. "over N value(s)" is a row count, and N means two things

`_measured_text` reports `len(reduced)`, which is a ROW count. Because a
rank cell is six rows (§0 fact 2) and all six carry the same
`n_wrong`/`pass_rate`/`status`, the number is **6× the cells** for every
rank-row quantity and **1× the cells** for a compile quantity — in the same
sidecar, in the same phrase. MEASURED:

| rendered | real population |
|---|---|
| P1.a *"over 18 value(s)"* | **3** cells (3 testees × 6 metric rows) |
| P5.a *"over 321 value(s)"* | **66** cells (306 rank rows = 51 cells × 6, plus 15 `excluded` base rows) |
| P13 *"over 834 value(s)"* | **834** compile cells (1 row each) |

**Fix shape.** Render both, named: *"over 66 cell(s) / 321 row(s)"*. And
— the deeper fix, which F13 shares — collapse the six rank metric rows to
one per cell before reducing, for the four quantities whose value is
identical across them. Template change MINOR + §8(6); the collapse changes
what a reducer computes → MAJOR.

**F6b, same family, LOW:** `ratio_to`'s denominator population is never
reported. `_reduce` takes `sorted(denom)[len(denom)//2]` — a median over an
unstated number of rows — and `_measured_text` reports only the numerator's
count. A reader cannot tell a 1-row denominator from a 24-row one.

### F7 — LIVE, MEDIUM. (β) annotates a population the claim is not about

`_ELSEWHERE` is a fixed four-tuple (`excluded`, `not_ranked`,
`did_not_compile`, `scratch`) minus the primary read, applied without
regard to the quantity's class. For a `compile:` quantity the primary read
is `compile`, so **all four** are consulted — and the `excluded` rows are
MATCH failures with no bearing on a compile-cost claim.

**Witness, committed**, the syntax sidecar: *"P13 … **confirmed**: …
measured P13: worst … = 2.543 over 834 value(s); **also present in:
did_not_compile (172), excluded (23)**"*. The 172 refusals are exactly the
right annotation — 172 compile cells whose cost was never measured. The 23
`excluded` rows are match cells; a reader, and certainly a Claude session,
will read them as 23 excluded compile cells. Fix: scope `_ELSEWHERE` by
quantity class — a `compile:` quantity's elsewhere is `did_not_compile`
alone. Code + `predicate` text; no template moves.

**F7b — LIVE, MEDIUM. (β) is blind wherever the selector names a column
the other sections leave empty.** `_elsewhere` re-runs the same selector,
and `did_not_compile` rows carry NO `form` (§0 fact 3). So every clause
naming `form=` is structurally unable to be told that its cell is a
refusal. MEASURED, and it **falsifies a committed catalogue `example`**:
R-PRED-3's `example` field says of syntax P2.d (`vrb-accept`) *"the pattern
is a refusal at this pin, so the cell is in the `did_not_compile` section
and the clause is not evaluable"* — the tool in fact produces
`"P2.d: no row in this report matches the selector"`, the bare reason,
because P2.d's selector names `form=whole-subject`. This is
`interpret_subject_grain_v1.md` §1.4's grain blindness in a second column,
and the same fix applies: when a re-run finds nothing, retry with the
columns the target section cannot carry DROPPED, and say which were
dropped. Code + `example` correction.

### F8 — LIVE, MEDIUM. A `partial` prediction renders no number at all

`evaluate_predictions` computes `claim`, `measured` and `reason` for every
parent; R-PRED-4's `slots` carry none of the three, so the modal outcome —
the catalogue's own `threshold_src` says `partial` is modal — renders as a
bare verdict list. MEASURED, discarded from the syntax sidecar:

- P7 renders *"1 clause(s) confirmed, 1 refuted, 0 not evaluable: P7.a
  refuted; P7.b confirmed"*. Discarded: `claim` *"P7.a: median_ns gte 90;
  P7.b: median_ns lte 2x"* and `measured` *"P7.a: worst
  unp-p-lc/(set)/large-subject-throughput/plain/libpcre2_10.46_jit-caps-simdna
  = 89.000 over 24 value(s); …"*.
- P2 renders four clause verdicts. Discarded: the numbers **and** P2.d's
  reason *"no row in this report matches the selector"*.

Fix: add `claim`, `measured` and `reason` to R-PRED-4's slots and template.
MINOR + §8(6). This is the single cheapest large win for Frank's directive:
four of the six committed sidecars carry `partial` predictions, and today a
reader must re-run the tool to learn what any of them measured.

### F9 — SILENT OMISSION, HIGH. R-ARM-1 cannot see a refused arm

The largest possible difference between two arms one config token apart is
that one of them does not compile — and that is precisely the shape the
deny-flag testees exist to measure ([B32]'s `-fno-scan-edge`, [B37]'s
`-fno-alt-island` where `w-384` compiles as an island and **refuses** under
the denial, [B39]'s `-fno-cls-fold`). R-ARM-1 reads `rank` rows; a refusal
has none; its `no_fire` asserts *"no two arms one config token apart differ
by more than twice the larger of their two standard deviations"*.

MEASURED: **532** (cell, ranked arm, refused arm) triples across the corpus
satisfy R-ARM-1's own one-token rule. Clean witness, `bench/loglines`:
`level-context` / short-subject-search / plain, `pcrec_35e1ab1_vm-caps-simdna`
ranks while `pcrec_35e1ab1_auto-caps-simdna` is in `did_not_compile` — one
token apart (`mode`: `vm` vs `auto`).

**Fix shape.** A sibling rule, **R-ARM-2**, *"two arms one config token
apart, one of which did not compile"*, reading
`report:rank?metric=median_ns` and `report:did_not_compile` and rendering
the ranked median, the refused arm and its diagnostic. A new rule is
**MINOR** (§3.3's own list) and introduces no threshold — it is an
existence rule. This is the highest-value single addition the audit found.

### F10 — SILENT OMISSION, HIGH. There is no "was measured, now failing"

R-DELTA-3 reports the improvement direction (`now measured (was: …)`).
There is no counterpart, at any layer: `delta_verdict` is written only for
rankable rows (`report.py:4517-4520`), so a cell that regressed OUT of the
ranking carries no verdict for any rule to read. The R-DELTA class's
`no_fire` sentences — *"no rank row carries a faster/slower clause"* —
therefore read as "nothing moved" in exactly the case that matters most.

MEASURED: **38** pairs in the corpus where one pin ranks a cell and the
same config at another pin is `excluded` or `did_not_compile` in the same
report. All 38 are in the improvement direction (e.g.
`2026-08-29-loglines-0.1-…-repin-36d5963`: `level-context` under
`auto-caps-simdna` ranks at 36d5963 and did not compile at 35e1ab1), so
this is an **asymmetry that has not yet cost us a missed regression** — and
that is luck, not design.

**Fix shape.** This one is PRECONDITION-shaped, like §2.5's P-1/P-2: the
reporter is the only component that knows both pins' cells, and the honest
fix is for `_cross_pin_info` to emit a clause on the EXCLUDED /
`did_not_compile` row (`now failing (was: measured)`, with the reason
`_set_cell_failure_reason` already computes), after which a rule reads it
the way R-DELTA-3 reads its mirror. Reporter change + `REPORTER_VERSION`
bump + a new rule (MINOR). An interpreter-only alternative — a rule joining
`rank` ∪ `excluded` ∪ `did_not_compile` by (engine, config, pin) — is
possible but would reimplement the reporter's partner selection, which is
exactly the mistake F11 documents.

### F11 — SILENT OMISSION, MEDIUM. R-BUCKET-SPAN's partner is not the reporter's

The catalogue asserts *"The partner is `_cross_pin_info`'s own choice"*.
It is not. The reporter chooses from `rd.record_ts_by_testee` and then
looks up `rd.set_cells[(sb, prev_tid, pattern, regime, form)]` — every
reduction cell, rankable or not (`report.py:2729-2752`). `r_bucket_span`
searches `cell_rows`, the `rank` rows of that cell (`interpret.py:1062-1073`).
Where the partner's cell is not rankable, the rule finds no partner, skips
silently, and its `no_fire` asserts *"every cross-pin Δ in this report
pairs two pins adjacent in `[[pin_order]]`"*.

MEASURED: 4 rows on the capability AFTER report —
`mojibake-curly-quote / short-subject-search / plain /
pcrec_cf0962e3_{auto-caps,auto-nocaps,vm-caps,vm-in-caps}-simdna`, each
carrying `now measured (was: wrong)` — have a partner at pin `a770139e`
that sits in the `excluded` section. R-BUCKET-SPAN cannot reach it. (484
of the other 488 Δ-carrying rows have exactly one same-config sibling in
the cell, so the divergence is narrow, not pervasive.)

**Fix shape.** Widen the partner search to `excluded` and
`did_not_compile` — an `inputs` change → **MAJOR** — or, if the panel
prefers to hold the population, correct the catalogue's `threshold_src` to
say what the rule actually reads and add the skip count to the rendering.
Either way the current text is a claim the code does not keep.

### F12 — SILENT OMISSION, MEDIUM. R-STATUS-1 treats an unjoined record as measured

`hit is None → continue` (`interpret.py:566-567`). The `no_fire` asserts
both halves — *"every included record **joins to an index row** whose
status is `measured`"* — and the predicate checks only the second. The
exposure is designed in: `check-interpret` section 2 runs the golden
comparison against a FROZEN index snapshot
(`catalogue/golden/index@2026-09-09.tsv`) precisely so a records-only
commit cannot fail it, so a report over newer records joins nothing and
R-STATUS-1 reports the clean negative over an empty join. Fix: a third
outcome naming the unjoined count — F1's reason channel carries it, or a
slot on a new firing.

### F13 — SILENT OMISSION, MEDIUM. Ruling (α)'s widened population is 0.6-4.7% of what it reduces over

(α) made the counterevidence REACHABLE. It did not make it WEIGHTY.
MEASURED on the capability AFTER report:

| clause | rank rows | `excluded` rows | rows carrying the counterevidence |
|---|---|---|---|
| P5.a | 306 (= 51 cells × 6) | 15 | **3** (0.9% of 321) |
| a synthetic regime-wide `n_gave_up` clause | 3,948 (= 658 cells × 6) | 25 (0.63%) | — |

With `identity` + a per-row op this is sound: `_op_holds` runs per row and
one violator refutes, which is why P5 now correctly reads **refuted** (the
verdict the ledger reached by hand). With `median`, `count`, `max` or `min`
the clean rank rows outweigh the counterevidence **100-158:1** and a real
failure can be arithmetically invisible. **Fix shape.** Collapse the six
identical rank metric rows to one per cell for the four failure quantities
before reducing (MAJOR: it changes what a reducer computes — and it is the
same fix F6 wants); plus a load check refusing an averaging reducer on a
failure quantity, or (β)-style per-section row counts in the rendering.

### F14 — LIVE, MEDIUM. An explicit `section=excluded` mixes two numbers under one column name

`_select` scopes the `excluded` section to `metric=pass_rate` base rows
**only when the section came from the (α) default** (`explicit_section` gate,
`interpret.py:1787-1789`). Under an explicit `section=excluded` the P-2
`giveup_smallest` detail rows come too — and [B13.2] P-2 deliberately put a
SUBJECT count in the same `n_gave_up` column where the base row carries a
TRIAL count. MEASURED, a synthetic `section=excluded` +
`regime_or_na=short-subject-search` + `quantity=n_gave_up` clause on the
capability AFTER report selects **34 rows: 25 `pass_rate` base rows
(n_gave_up = 25, 10, 75, 15 — trials) and 9 `giveup_smallest` rows
(n_gave_up = 5, 2, 3, 15 — subjects)**, reduced together. A `max` returns
75 trials; a `count` returns a meaningless 34.

And the author has no way out: **`metric` is not a selector key**
(`SELECTOR_KEYS` is `pattern`, `subject_or_na`, `regime_or_na`, `form`,
`testee`, `section`, `grain`). Fix: either add `metric` to the closed key
set (MAJOR — a new member of a closed set, and the right answer, because it
also lets a clause target `jitter` or `artifact_bytes` explicitly), or
extend the `metric=pass_rate` scoping to the explicit case too (MAJOR — it
changes what an existing clause reads). The first is additive; the second
is a silent change to committed prediction files.

### F15 — LATENT, MEDIUM. Three quantity/op combinations are decided before measurement

Each is a one-line, store-free load check on Q6's own precedent:

1. **`quantity=section` with no explicit `section=` clause.** The default
   population is `rank`, so the only value readable is the literal `rank`:
   `section eq-token did_not_compile` can never hold and
   `section neq-token did_not_compile` can never fail. Both committed
   `section` clauses name `section=` and escape it. Check: `quantity=section
   ⇒ the selector must name section`.
2. **`quantity=delta_verdict` with `grain=subject`.** MEASURED (the v1.4
   note's own §2.3): 0 of 202,794 subject-grain rank rows carry a
   `delta_verdict`; the column is not written at that grain
   (`report.py:4518`). `_value_of` returns `""` rather than None, so the
   clause EVALUATES against empty strings and can "confirm" a
   `neq-token`. Check: refuse the combination.
3. **A non-numeric quantity with a numeric op.** `_op_holds` reaches a bare
   `float(value)` for `lt`/`lte`/`gt`/`gte`/`eq`/`neq`/`between`;
   MEASURED, `float("measured")`, `float("faster ×1.19")` and
   `float("did_not_compile")` each raise `ValueError` — **not** an
   `InterpretError`, so `main()`'s handler does not catch it and the tool
   exits on a traceback instead of the exit-2 named error the discipline
   requires. Check: `quantity ∈ {status, section, delta_verdict} ⇒ op ∈
   {eq-token, neq-token, set-eq, set-subset, present, absent}`.

All three are `load_predictions` additions, no catalogue change.

### F16 — SILENT OMISSION, LOW-MEDIUM. "worst" is the wrong extreme for a lower-bound op

`_measured_text` picks `max(bad, key=|v|)` in the violating branch and
`max(reduced, key=v)` in the confirming branch, irrespective of the op's
direction. For `gt`/`gte` the worst violation is the MINIMUM and the
weakest confirmation is the minimum too. MEASURED on syntax P7.a
(`median_ns gte 90`, 24 values, 22 violations, true range 61.000-92.000):
the tool computes *"worst … = **89.000**"* — the mildest violation, one
unit from the bound — where the worst violator is **61.000**.

Not currently visible on any committed sidecar, because every `gt`/`gte`
clause in both predictions files sits inside a `partial` parent, whose
`measured` text F8 discards. **The two findings interlock: fixing F8 makes
F16 visible.** Fix: choose the extreme by the op's direction (`lt`/`lte`
→ max; `gt`/`gte` → min; `between` → the farther side; `eq`/`neq` → the
largest deviation from the bound). Code only.

### F17 — LATENT, LOW. R-RANK-1 skips a pair that touches exactly 1.000000

`(r_a - 1.0) * (r_b - 1.0) >= 0 → continue` treats a product of zero as
"did not cross". A non-reference cell reading exactly `1.000000` against
the reference arm at one pin and crossing at the other is invisible. The
threshold is DEFINITIONAL and the catalogue says so; the boundary
convention is not stated anywhere. Fix: a `legend` line (catalogue 1.1's
own mechanism, MINOR), or `> 0` with the equality case stated.

### F18 — SILENT OMISSION, LOW. R-STATUS-12's population is "smallest-per-code", not "subjects"

The reporter emits ONE `giveup_smallest` row per (cell, code), naming that
code's SMALLEST firing subject (`report.py:4548-4553`). MEASURED: **188**
subjects gave up across the corpus; **76** are named by a
`giveup_smallest` row (40%); every cell in the corpus has exactly one such
row. A subject that gives up under code A on pattern 1 (where it is
smallest) and under code B on pattern 2 (where it is not) cannot be seen.
The predicate prose — *"One subject id that gives up under two DIFFERENT
codes on two different patterns"* — is true of what the rule reads and
over-general as a claim about subjects; the `no_fire` inherits the
over-generality. Fix: state the narrowing in `predicate` and `no_fire`
(MINOR + §8(6)). Widening it needs a reporter change and is not worth one.

### F19 — LATENT, LOW. R-ARM-1's unguarded floats and its zero-spread default

`float(r["value"])` on `median_ns` and `stddev_ns` (`interpret.py:886-890`)
is unguarded, and `stddev.get(k, 0.0)` makes a missing stddev row a spread
of ZERO — which fires the rule on any difference at all. MEASURED: 0
non-finite or empty numeric values in 103,488 rank rows, and stddev rows
are emitted 1:1 with median rows, so both paths are unreachable today. The
reporter does write `""` for a None value (`report.py:4526`), so the
hazard is real if `stddev_ns` ever comes back None. Fix: `_float_or_none`
and an explicit skip, as `_keyed_values` already does. Code only.

### F20 — RENDERING, LOW. The R-DELTA templates name no comparand

*"the reporter's cross-pin Δ reads **faster ×1.19** (median 69,537.5 ns)"*
does not say faster **than what pin**. The fact is available and
unambiguous: MEASURED, **484 of 488** Δ-carrying rows on the capability
AFTER report and **384 of 384** on the bounded AFTER report have exactly
ONE same-config sibling at another pin in the cell. Fix: an `old_pin` slot
(R-BUCKET-SPAN already computes exactly this) in R-DELTA-1/2/3's templates.
`arith` + template = MINOR + §8(6).

### F21 — RENDERING, LOW. A two-member aggregate group hides one member

`render_bullets` prints the extremal firing, and the minimum only when
`n > 2` (`interpret.py:1490-1492`) — so a group of exactly TWO renders one
firing and does not even list the other's key, while the no-`extremal`
branch lists every key under *"Also:"*. Witness: the capability AFTER
sidecar's R-BUCKET-DOMINATED groups for `pcrec_a770139e_auto-caps-simdna`
and `pcrec_cf0962e3_auto-caps-simdna`, each *"2 firing(s)"* naming one
cell. Fix: drop the `n > 2` guard (the minimum of a 2-group is its other
member) or append the remaining keys. Code only; regeneration required.

### F22 — LIVE RENDERING, LOW-MEDIUM. R-STATUS-8 states a percentage without its bar

*"The busiest other core during a measured window read 30.15% (…)"* — with
no statement that the project's own quiet bar is **10%** and that this
number is NOT judged against it. It is the `/proc/stat` timeline's worst
other core, recorded as PROVENANCE ([B32]); the gate is the pre-flight's
busiest non-target 5-second AVERAGE (BD7). A reader — and Frank's directive
makes a Claude session the reader — sees 30.15% against a 10% bar and
concludes the window was not quiet. It was: the gate passed. Fix: a
`legend` line, exactly the mechanism catalogue 1.1 added for R-ARM-1's own
misreadable ×1.00. MINOR + §8(6).

### F23 / F24 / F25 — audited CLEAN, recorded so a later pass does not "fix" them

- **F23, R-FLOOR-1 and R-FLOOR-3.** MEASURED: 1,266 of 12,741 compile
  cells (9.9%) carry no `jitter` row, and all 1,266 are exactly the cells
  whose compile median is EMPTY — the refusals. `_jitter_flag` returns `""`
  when there is no median to divide (`report.py:2432-2433`). A cell with no
  compile time has no jitter, so the omitted population cannot hold
  counterevidence. **Sound narrowing, fully explained.**
- **F24, R-BUCKET-FORM.** The rankable-only read is deliberate and the
  catalogue's own `predicate` states both the choice and its reason.
  **Sound.**
- **F25, `not_ranked` and `scratch`.** ZERO rows in all 45 committed
  reports (the canonical store refuses a scratch record on write and on
  index; no committed query uses `--include-unmeasured`). R-STATUS-11 has
  never fired, and (α)'s omission of `not_ranked` is **inert, not benign** —
  a future `--include-unmeasured` query or an `inconclusive-spread` cell
  would populate it, and no prediction's default population reads it.

---

## §5. The rendered-sentence audit (Frank's directive, separately)

> *"make results carry the context around their numbers, especially where
> a Claude session is the consumer."*

A sound predicate can still render a sentence a reader cannot act on. The
table flags every template and `no_fire` that states a verdict or a number
without its population. `interpreter_v1.md` §7.1's firewall guarantees the
sentence is a declared template — it does not guarantee the template is
complete.

| surface | what the sentence omits | finding |
|---|---|---|
| every `no_fire`, paired with any token | that the token may mean *"the rule declined"* rather than *"the population is clean"* — the renderer substitutes `no_fire` for all six tokens alike | **F1, F2** (the structural one) |
| R-BUCKET-KB `no_fire` | names catalogue 1.0 at catalogue 2.0 | F5 |
| R-BUCKET-DOMINATED template | the denominator's subject count; the excluded subjects; whether the set cell ranks | F4 |
| R-PRED-1/2 `measured` | how many CELLS (vs rows); which sections were read; the denominator's size under `ratio_to` | F6, F6b |
| R-PRED-4 template | the claim, the measured value AND the not-evaluable reason — all three computed and discarded | **F8** |
| R-PRED-3 reason | whether the cell is missing because the selector is unsatisfiable at this grain, misspelled, or genuinely absent — `interpret_subject_grain_v1.md` §1.4's open gap, plus F7b's second column | F7b |
| R-DELTA-1/2/3 templates | the comparand pin | F20 |
| R-STATUS-8 template | that 30.15% is provenance, not the gate, and that the gate is 10% | **F22** |
| R-ARM-1 template | nothing — it names both arms, both medians, the spread, the differing token, AND carries a `legend` for its ×1.00 case | **the model to copy** |
| R-STATUS-3 template | nothing — it even carries the trials-vs-subjects clarification inline | **the model to copy** |
| R-FLOOR-2 template | nothing — it names both means, both populations and the ratio | **the model to copy** |
| aggregated bullets | nothing in the collapse itself (the count is always stated and the facts TSV always carries every firing) — except a 2-member group's second firing | F21 |

**The pattern in the three models.** Every sentence that reads well names
*both* sides of its comparison and the size of what it read. Every sentence
flagged above names one side, or a number with no denominator. That is the
whole of the directive, and it is a template-level fix in six of the eight
cases.

---

## §6. Proposed fixes, grouped by what they cost

Nothing here is adopted. The grouping is what a panel needs to buy in
order.

**Group 1 — code only, no catalogue bump, no sidecar regeneration.**
F7 (scope `_ELSEWHERE` by quantity class), F7b (retry `_elsewhere` with
impossible columns dropped, and say which), F15 (the three load checks),
F16 (pick the extreme by the op's direction), F19 (guard the floats).
Each is independently landable and each closes a whole class.

**Group 2 — MINOR catalogue + §8(6) review + full sidecar regeneration.**
F1/F2 (the did-not-fire REASON channel — one mechanism, two live defects,
and it is `interpreter_v1.md` §4.5's own intended rendering), F5 (reword
+ a `check-interpret` assertion that no prose names a catalogue version),
F8 (R-PRED-4's three discarded slots — **the cheapest large win**), F9
(the new rule R-ARM-2), F18 (state R-STATUS-12's narrowing), F20 (the
comparand pin), F21 (the 2-member group), F22 (R-STATUS-8's legend).

**Group 3 — MAJOR catalogue (a predicate, a threshold, or `inputs` move).**
F3 (coverage from the selector, not from the matched rows — a bug fix
against the catalogue's own stated predicate, which is why the panel must
rule on the label), F4 (read the slice's `excluded` rows), F6/F13 (collapse
the six identical rank rows before reducing), F11 (widen R-BUCKET-SPAN's
partner search), F14 (`metric` as a selector key).

**Group 4 — a reporter PRECONDITION, on §2.5's P-1/P-2 precedent.**
F10 alone: a `now failing (was: measured)` clause on the excluded /
refused row, after which a rule reads it as R-DELTA-3 reads its mirror.
`REPORTER_VERSION` bump + full regeneration + a MINOR rule.

**Recommended order**, if the panel wants one: Group 2's F8 and F1/F2
first (they make every existing sidecar honest and cost no predicate),
then Group 1 entire, then F9, then Group 3's F3 and F4 (the two remaining
live defects), then F10.

---

## §7. Questions for the panel / Frank

**Q1. The did-not-fire REASON channel (F1/F2) — adopt it, or reword the
two `no_fire` sentences?** *Recommend the channel.* Rewording fixes two
sentences; the channel fixes the class, is `interpreter_v1.md` §4.5's own
intended rendering, and keeps the firewall (reasons are declared,
slot-free, §8(6)-reviewed prose like `no_fire`).

**Q2. When the code and the catalogue's `predicate`/`threshold_src`
disagree and the PROSE is right (F3, F11) — is the code fix MINOR or
MAJOR?** *Recommend MAJOR*, because the firing set moves and a sidecar
stamped at the old version is no longer derivable — §3.3's own test — even
though no declared predicate changes. The panel should settle this once;
it will recur.

**Q3. F4's fix: the full one (read the slice's `excluded` rows, MAJOR) or
the interim (state the denominator's subject count, MINOR)?**
*Recommend the full one.* Half the sentence's problem is the omitted
failures; stating only the denominator leaves "of this cell's total"
reading as the set cell's total.

**Q4. Should the six identical rank metric rows collapse to one per cell
for the four failure quantities (F6/F13)?** *Recommend yes.* It is the
root cause of both the 6× inflated "over N value(s)" and α's 100-158:1
dilution, and for these four quantities the six rows are literally
duplicates. It is a MAJOR that changes no committed verdict under
`identity` (MEASURED: P5.a still refutes, P1.a-c still confirm) and
changes every count/median/max/min one — which is the point.

**Q5. `metric` as a seventh selector key (F14)?** *Recommend yes* — the
additive half. It fixes the base-row/detail-row mixing, and it also lets a
clause target `jitter` or `artifact_bytes` explicitly, which no committed
prediction can express today.

**Q6. F10's reporter precondition — now, or filed?** *Recommend filed with
a named trigger*: the first AFTER window whose ledger reports a cell that
left the ranking. All 38 corpus instances are improvements, so the hole has
not cost us anything yet; it will cost us exactly once, in the report where
it matters most.

**Q7. Does this audit want a standing `check-interpret` section?** A
seventh section asserting the invariants the audit turned up — no prose
names a catalogue version (F5); every rule that can decline has a reason
distinct from its `no_fire` (F1); every quantity/op pair is in the declared
legal matrix (F15) — would make the class self-policing instead of
re-audited. *Recommend yes, after the fixes land*; auditing is not the same
as gating, and a gate written before the fixes would encode today's shape.

---

## §8. What this note deliberately does not decide

- **Whether any committed prediction file is repaired in place.** The
  audit names the authoring defects (F15's three combinations) but
  `interpret_subject_grain_v1.md` §7 already rules that editing a
  committed prediction after its population was measured is a question
  about the prediction discipline, not about this audit.
- **Any change to `report.py`'s markdown rendering.** F10 is the one
  reporter change proposed, and it is a TSV/verdict change.
- **The `no_fire` and `template` WORDING** of any fix. §8(6) makes every
  prose diff a human's, by rule id, in a commit message; this note names
  which sentences are wrong and why, not what they should say.
- **Set-local outlier bands.** Still `interpreter_v1.md` §1.1's exclusion
  and §11's open Q3, untouched here.
- **Whether R-BUCKET-KB should register a signature.** §10 C.3's stated
  known gap, unchanged; only its `no_fire` prose is a finding.

---

## Source header

Derived from committed artefacts at `HEAD` = `4eb413a` (catalogue 2.0,
reporter v17, `interpreter_v1.md` v1.4, record schema v1.6) plus five
read-only probes run in this lane, archived with their scripts at
`docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` and
`…-probe{1..5}.py`. Code citations are `pcrecbench/interpret.py`,
`pcrecbench/report.py`, `catalogue/rules.toml` and
`catalogue/check_interpret.py` as committed at that revision; document
citations are `docs/design/interpreter_v1.md` (v1.4),
`docs/design/interpret_subject_grain_v1.md`, `docs/dev/predictions/CLAUDE.md`
and the six committed `reports/*.interpretation.md` sidecars. Every
contested number is marked MEASURED and traceable to a named probe. No
file under `store/`, `reports/`, `catalogue/`, `pcrecbench/` or `~/pcrec`
was modified by this lane.
