# THE PREDICATE AUDIT — a design note (v1.1, 2026-09-18)

**Status: PROPOSED, not adopted. D6-panel input. NO code and NO catalogue
change in this lane** — nothing under `pcrecbench/`, `catalogue/`,
`reports/`, `schema/` or `store/` is touched. The note proposes; fixes
land on a ruling.

**v1.1** (2026-09-18, lane `lane/r7consol`): applies the R7 D6 panel's
accepted findings (`docs/dev/reviews/2026-09-18-r7-predicate-audit.md`,
17 findings across three lenses — population semantics `r7pop-1..5`,
catalogue/interpreter versioning `r7ver-1..9`, code reality `r7code-1..3`)
to the fix designs and the §6/§7 cost accounting below. Every accepted
edit cites its finding id in place; nothing under `pcrecbench/`,
`catalogue/`, `reports/`, `schema/` or `store/` moved, and the audit's
own findings F1-F27 are unchanged — this revision corrects the note's
OWN reasoning about its remediation, not the underlying catalogue defects.

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

**What it found, in one paragraph.** **Eleven** defects are LIVE — a committed
sidecar renders a structurally unsound verdict or an uninterpretable number
today — of which the sharpest three are: R-FLOOR-2 renders *"no ranked
cell is at or below its set's own
floor pattern"* on a report whose set has **no floor pattern at all** and
where the rule therefore never evaluated anything (and `interpreter_v1.md`
§4.5 specifies a different rendering, so this is a build deviation, not a
design gap); R-DELTA-4 renders *"no prediction … selects that cell"* about
cells a prediction names **by name** but could not evaluate; and
R-BUCKET-DOMINATED renders a dominance share *"of this cell's total"* for
eight cells the same report **excluded from ranking**, over a denominator
that silently omits the subjects that failed. Thirteen further findings are
silent omissions or latent, the two largest structural rather than textual:
**R-ARM-1 cannot see an arm pair one of whose arms refused to compile** (532
such triples in the corpus — the strongest possible arm difference, and
exactly what the deny-flag testees exist to measure), and **the reporter has
no "was measured, now failing" verdict at all**, so the whole R-DELTA class
is blind to a regression that removed a cell from the ranking. Two
narrowings audited CLEAN — and are recorded as clean, with the reason, so a
later pass does not "fix" them — beside one population that is inert
rather than sound.

---

## §0. What was measured in this lane, and how

**Seven** read-only probes, archived with their scripts and verbatim output
at `docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` +
`…-probe{1..7}.py`. Every probe imports `pcrecbench.interpret`'s **own**
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
| **M7** | the consequence of `render_tsv` emitting the `did_not_compile` section only INSIDE an existing ranking group — lane `b51preds`' finding 2, re-asked as a RULE-population question | 29 (report, pattern) pairs whose every compile cell is a refusal and which have NO `did_not_compile` row anywhere, so R-STATUS-4 cannot see them |
| **M6** | the THIRD predictions file (`capability-0.1-ext-roster.tsv`, merged to master mid-lane) re-resolved clause by clause, each also forced through the PRE-(α) `rank`-only default | whether the authoring lessons landed, which clauses ruling (α) is load-bearing for, and how exposed F14 is in freshly authored work |

**A labeling note (r7code-2): the M-numbers above are this note's own
bookkeeping, not all of them literal probe output.** The archived
`2026-09-18-predicate-audit-probes.txt` prints literal `M2`, `M3`, `M5`,
`M6` and `M8` section headers (all inside `probe2.py`'s output; `M8` is
the `not_ranked`/`scratch` occupancy census folded into M4's row above).
`M1` (probe1.py's structural census), `M4` (split across probe3.py's and
probe4.py's several `====` sections with no numeric label of their own)
and `M7` (probe7.py, headed only by `########## probe7.py ##########`)
never appear as that literal string in the archive — a reader `grep`-ing
for "M4" to find its evidence must know it means "probe3.py + probe4.py."
This does not affect any number's traceability (every M-labeled claim
below is independently re-derivable from the named script), and it is
purely a labeling mismatch between this table and the archive it points
to.

**The corpus, as of this lane** (`HEAD` = `4eb413a`, catalogue 2.0,
reporter v17, `interpreter_v1.md` v1.4, plus `a5018f8` merged in
mid-lane): 45 committed set-grain report TSVs, 3 committed
`.subject-grain.tsv` slices, **3** committed predictions files (**69**
clause rows — the third, `capability-0.1-ext-roster.tsv`, landed from
lane `b51preds` while this audit was running and is stated BEFORE its
sample, so no report scores it yet), 6 committed `.interpretation.md`
sidecars.

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
| R-STATUS-4 | `did_not_compile`, deduped to (pattern, testee); `:617-626` | **a pattern NO testee in the roster compiled** | **no**: `render_tsv` emits the section INSIDE the per-ranking-group loop (`report.py:4555-4564`), and a pattern nothing compiled has no ranking group, so no row exists for it anywhere. MEASURED: **29** (report, pattern) pairs | **D** F26 |
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
| `section` read against `did_not_compile` (either as a quantity or a `section=` clause) | the section as emitted | **partially** — a pattern NO testee compiled has no row there at all (F26) |
| `delta_verdict` (1) | `rank` | yes at set grain; **structurally empty at `grain=subject`** — 0 of 202,794 subject-grain rank rows carry one (`interpret_subject_grain_v1.md` §2.3) (F15). |
| `section` (1) | `rank` | **no**: with no explicit `section=` clause the only value readable is the literal `rank`, so the claim is decided before any measurement (F15). Both committed `section` clauses name `section=` explicitly and so escape it. |

### §3.2 By stage

| stage | the population question | verdict |
|---|---|---|
| `_sections_for` | §3.1 | see above |
| `_select`'s `excluded` scoping | the `metric=pass_rate` scope applies **only** under the (α) default, not under an explicit `section=excluded` | **L** F14 — and `metric` is not a selector key, so an author cannot separate them |
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

**On the ids.** F1-F25 were assigned in the first pass and are stable
(the §2/§3 tables cite them). F26 and F27 were added after lane
`b51preds` merged mid-audit and are filed by KIND, with the defects, not
by number — so the closing F23/F24/F25 block (the narrowings that audited
CLEAN) stays last, where it belongs.

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
and needs no predicate to move.

**Corrected, r7pop-5: the channel must be worked out for all three of
`r_floor_2`'s causes, not one.** `r_floor_2`'s single early return
(`interpret.py:946-948`) conflates THREE distinct causes into the one
`no-matching-rows` token: the header key absent, the literal string
`"none"`, and a comma-joined multi-value `floor_pattern`. `interpreter_v1.md`
§4.5's own worked precedent — the one this fix cites as proof the
rendering is "the code's own intended rendering" — only demonstrates the
wording for the `none` case (`no-matching-rows (floor_pattern: none)`,
`interpreter_v1.md:474`). The multi-value case is a materially different
population by `report.py:4418-4432`'s own docstring — multiple sub-benches,
each declaring a genuine but DIFFERENT floor pattern, an ambiguity about
WHICH comparison to make, not an absence of one to make — and needs its
own reason string, not a copy of the `none` wording. MEASURED (probe1's
`floor_pattern` census): 40 committed reports read `floor`, 3 read
`floor-byte`, 2 read `none`, and ZERO read a multi-valued header — the
third cause has **no corpus witness today**, so its wording is unverified
by any real sidecar and must be reviewed as carefully as the other two
(§8(6)), not assumed correct by analogy to the `none` case that does have
a witness. The reason set for R-FLOOR-2 therefore needs three closed
members, not one generic "the rule declined."

**Version: MINOR + §8(6) review + full sidecar regeneration** (§3.3's own
rule). The alternative — returning `input-absent` instead — is cheaper
still but leaves the sentence mismatched for every other rule with the
same shape.

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
alone. Code + `predicate` text.

**Cost, corrected (r7ver-1): this fix moves a committed sidecar, so it is
not "no sidecar regeneration."** The witness quoted above is a **currently
committed** `reports/*.interpretation.md` rendering, and this fix changes
what that exact line reads (the false `excluded (23)` clause is removed).
`interpreter_v1.md` §3.3's bump rule is explicit that regeneration is
forced by content, not by version-label bookkeeping — a change that
changes any rendering forces regeneration of every affected sidecar in the
same commit. F7 therefore does NOT belong with "no catalogue bump, no
sidecar regeneration" (see §6's Group 1, corrected). It also needs an
`INTERPRET_VERSION` bump — see the new §6.05 subsection below (r7ver-3).

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

**F7b splits in two, r7ver-2.** The finding's own closing line — "Code +
`example` correction" — is itself two different costs the note originally
filed as one "code only" item. The retry-mechanism half (dropping
impossible columns and saying which) is code only, and today changes
nothing any committed sidecar renders (P2.d's reason string is currently
DISCARDED by F8's own defect, not shown at all — see F8/F16's interaction
note). The `example`-field half is a literal edit to
`catalogue/rules.toml`'s R-PRED-3 `example` field, and the catalogue's own
versioning rule — stated identically at `catalogue/rules.toml:19-23`,
`catalogue/CLAUDE.md:66-68` and `interpreter_v1.md:730-733` — lists "an
`example` refreshed" as one of the enumerated **MINOR**-bump triggers, on
the same footing as a template wording change or a link add. So F7b's own
stated fix already names a catalogue field that moves the version and
forces the same full-sidecar regeneration F7 needs, above. Note, though,
that `example` is not one of the four fields (`template`/`no_fire`/
`legend`/`links`) `catalogue/CLAUDE.md` §8(6)'s named-reviewer gate lists
— so this half needs the MINOR bump and the regeneration, but not
necessarily the named-reviewer commit line the template-prose fields
require. **Version: F7b-code = code only, no bump; F7b-example = MINOR +
regeneration (no §8(6) named-reviewer line required) + an `INTERPRET_VERSION`
bump for the code half of the retry mechanism** (r7ver-3, below).

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

**RULED 2026-09-19 (Frank, live): YES** — R-ARM-2 adopted with both
panel conditions: its own control/sabotage fixture pair (r7ver-4), and
the goldens-may-move fact stated as UNMEASURED until implementation.
MINOR class under the reframed §3.3 (additive; both definitions agree
here); rides the held wave's single bump.

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

**Fix shape, corrected (r7pop-3): the widening as stated cannot reach half
of what it names.** "Widen the partner search to `excluded` and
`did_not_compile`" is not itself sufficient. `r_bucket_span` groups
candidate partners by `by_cell[(pattern, regime, form)]`
(`interpret.py:1050`) — the JOIN KEY includes `form` — and a
`did_not_compile` row's `form` column is unconditionally empty (§0 fact
3). Under the literal widening, a `did_not_compile` row can therefore
never satisfy the same `(pattern, regime, form)` key a ranked row groups
under, no matter how the section search is widened, because the key
excludes it before the search runs. Only the `excluded` half of the
widening (whose rows DO carry `form`) becomes reachable as originally
stated; the `did_not_compile` half needs its own re-keyed join — dropping
`form`, or falling back to `(pattern, regime)` when the candidate section
is `did_not_compile` — which neither this fix shape nor §7 Q2's discussion
specified. Widening the `excluded` half alone is still an `inputs` change
→ **MAJOR**; the `did_not_compile` half's join shape is **TBD AT
IMPLEMENTATION** and must be specified before it is built, or it silently
reproduces this same audit's own P5 shape — a population widened in name
that cannot structurally contain the counterevidence it claims to add —
inside the fix meant to close F11. The interim (holding the population,
correcting `threshold_src`, and adding a skip count to the rendering) is
unaffected by this correction and remains available either way. Either
way the current catalogue text is a claim the code does not keep.

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
verdict the ledger reached by hand). **And (α) is load-bearing
prospectively, not only retrospectively** — MEASURED (M6) over the
ext-roster file authored after the ruling: of its eleven
failure-quantity clauses, **seven** (P3.a/b, P4.a/b, P5.a, P7.a/b)
resolve entirely to `excluded` rows with ZERO rank rows, so under the
pre-(α) `rank`-only default every one of them would have scored
`not-evaluable`. (The probe substitutes a MEASURED testee glob for the
as-yet-unsampled ext-roster one, so this is a fact about the clause
SHAPE, not a score of P3-P7.)

**The four reducers are not equally at risk (corrected, r7pop-2).** The
original draft of this finding folded `median`, `count`, `max` and `min`
into one "100-158:1, arithmetically invisible" claim; read against
`_reduce`'s own code (`interpret.py:1873-1874,1880-1886`) with the op
actually used on this quantity in the corpus (`eq 0`, P5.a's own clause),
the four reducers split into three different risk classes:

- **`median` is genuinely vulnerable.** Verified by hand for P5.a
  (r7pop-1, Q4 below): the clean rows so outweigh the 3 counterevidence
  rows that the sorted median index lands inside the zeros either side of
  any row-count collapse — a real failure's VALUE can be arithmetically
  invisible, exactly as this finding names.
- **`min` carries a related but weaker exposure**, not the same shape.
  For an `eq 0` hypothesis, `min eq 0` proves only "at least one row is
  clean" — a near-vacuous claim when most rows are clean by construction.
  That is a different failure than median's silent overwrite (it never
  actively hides a violation the way `median` can), but it still cannot
  surface one.
- **`max` is, by contrast, the reducer LEAST susceptible to this class.**
  `max` picks `nums[-1]`, the single WORST value in the population: for an
  `n_wrong eq 0` hypothesis, if even one row is nonzero, `max` returns it
  and the clause correctly reads *refuted* regardless of how many
  thousands of clean rows dilute the population — the closest thing this
  catalogue has to `identity`'s own per-row guarantee. Grouping it with
  `median`/`min` under the same "100-158:1" severity number overstates its
  risk.
- **`count` (`len(values)`) never reads the quantity's VALUE at all** — it
  counts selected rows. Whatever hazard exists in its number is F6's
  row-count inflation (6× for a rank quantity, §0 fact 2), a different
  problem from value dilution, and should not be folded into the same
  severity claim as `median`/`min`.

**Fix shape.** Collapse the six identical rank metric rows to one per cell
for the four failure quantities before reducing (MAJOR: it changes what a
reducer computes — and it is the same fix F6 wants); plus a load check
refusing an averaging reducer (`median`, and arguably `min`) on a failure
quantity, or (β)-style per-section row counts in the rendering. The
collapse fixes F6's row-count inflation for all four reducers; it is
NOT, by itself, what makes `median`'s value-dilution hazard safe — see
Q4's correction below (r7pop-1).

### F14 — LATENT (mechanism in use), MEDIUM. An explicit `section=excluded` mixes two numbers under one column name

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

**Live mechanism, cell-dependent firing.** A committed prediction already
uses the shape — syntax P2.a's selector is
`section=excluded;pattern=rec-r-uc;regime_or_na=match-compliance;form=whole-subject`
with `quantity=n_wrong` — and MEASURED, its four selected rows are all
`pass_rate` base rows, because that cell happens to carry no give-up detail
rows. The mixing fires the first time such a clause lands on a cell that
does. It is not a hazard waiting on a new authoring habit; it is waiting on
a give-up.

**One accidental protection, and it is the interim fix.** MEASURED (M6):
`subject_or_na=(set)` excludes the detail rows, because a
`giveup_smallest` row carries a REAL subject id where the base row carries
the literal `(set)` — an explicit `section=excluded` read selects 26 rows
with that clause and 36 (26 base + 10 detail) without it. Every numeric
clause in the ext-roster file writes `subject_or_na=(set)` and is
therefore protected; its six `section=excluded` clauses that do NOT write
it all use `set_of(pattern)`, whose answer a detail row cannot change (a
detail row's `pattern` equals its base row's). So the hazard is contained
in today's authored work **by convention nobody wrote down**. Until
`metric` becomes a key, `docs/dev/predictions/CLAUDE.md` should state
`subject_or_na=(set)` as the base-row idiom, and say why.

And the author has no way out for the general case: **`metric` is not a
selector key**
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

**A note on Q6's OWED check (ii)** (every `testee=` glob must match ≥1
index testee for its own `(subbench, version)`, vacuous when unmeasured):
MEASURED (M6), each of the five ext-roster globs matches exactly one
`store/index.tsv` testee today, so the check would run NON-vacuously and
PASS on the newest predictions file. It would also have caught capability
P4's `pcrec_*-auto-*` — the defect it was designed for.

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

### F26 — LIVE, HIGH. A pattern nothing compiled has no refusal row at all

`render_tsv` emits the `did_not_compile` section from INSIDE the
per-ranking-group loop (`report.py:4555-4564`), and a ranking group exists
only where some testee produced match rows. So a pattern that **no testee
in the query's roster compiled** has no ranking group, and therefore no
`did_not_compile` row anywhere in the TSV — even though every one of its
records carries `compile_outcome: did-not-compile` in full.

Found by lane `b51preds` (its finding 2, about the `section=did_not_compile`
selector, where it cost that file three planned clauses); audited here as
the RULE-population question it also is. **R-STATUS-4's entire population
is that section**, so it cannot see these patterns, and its `no_fire`
sentence — *"every pattern compiled on every testee in this report"* —
is asserted over reports where eleven patterns compiled on nobody.

MEASURED (M7): **29 (report, pattern) pairs** across the committed corpus,
in two live shapes.

- **The understated firing.** The committed ext sidecar
  (`reports/2026-09-18-capability-0.1-…-ext-first-cf0962e3.interpretation.md:44`)
  renders *"R-STATUS-4 — a pattern that did not compile (5 firing(s),
  aggregated to 2 by testee)"* — while `balanced-parens-rec` (6 refused
  compile cells) and `negation-scope-lookbehind-var` (5) appear in no
  firing at all. The section is present and understates the refusals by
  eleven (pattern, testee) cells.
- **The flatly false negative, waiting to be rendered.**
  `reports/2026-09-05-bounded-0.3-…-ccboth-288d505.tsv` carries **zero**
  `did_not_compile` rows, so R-STATUS-4 would render its `no_fire` —
  while `cls-upto-65535` refused on all six testees. That is
  `bench/bounded`'s own headline refusal, the 65535 NFA cap [B11.4] built
  the count ladder to reach. No sidecar exists for that report yet; the
  sentence fires the first time anyone interprets it.
- Worst single case: `reports/2026-09-06-altwide-0.2-…-clsfold-d34c9131.tsv`,
  **11** such patterns (`ci-512`, `w-512`, `w-1024`, `w-2048`, `s-2048`,
  `s-4096`, `sfx-512`, `sh1-512`, `srt-512`, `nar4-512`, `wb-512`) — the
  whole refusal wall above `bench/altwide`'s ladder, invisible.

**Fix shape.** This is a REPORTER fix, and it is a small one: emit the
`did_not_compile` rows for a (sb, pattern) whose testee set intersects no
ranking group in a pass of their own, after the group loop, with
`regime_or_na` empty (there is no regime to name — nothing ran). Then
R-STATUS-4's population becomes the refusals, full stop, and a
`section=did_not_compile` clause can express the whole refusal set.
`REPORTER_VERSION` bump + full regeneration; the rule's predicate and
`inputs` do not move, so the catalogue side is at most the `example`
field. It belongs with F10's reporter wave.

### F27 — LIVE BLOCKER, HIGH (found by lane `b51preds`, audited here). `check_stated_utc`'s population is the wrong "before"

`check_stated_utc` anchors a prediction's `stated_utc` against the
**earliest** `store/index.tsv` timestamp for its `(subbench, version)`,
superseded rows included (`interpret.py:1700-1725`). That population is the
set's first-ever measurement, and it never moves forward — so a
predictions file about a LATER sample of an already-sampled set can never
pass, however honestly it was stated before its own run. Reproduced live
by that lane and re-verified here against the just-merged file:

> `interpret: docs/dev/predictions/capability-0.1-ext-roster.tsv:2 (P1.a):
> stated_utc 2026-09-18T00:00:00Z does not precede the earliest
> store/index.tsv timestamp for capability@0.1 (2026-09-17T00:50:53Z),
> superseded rows included (§6.5)`

The check raises before a single clause is scored, so the whole
`interpret` call aborts: **the newest committed predictions file cannot be
used through the CLI's default path at all.**

It belongs in this audit because it is the same class one layer up — a
GATE whose population cannot distinguish the thing it is checking
("stated before the population it predicts") from an unrelated fact
("stated after some earlier population of the same set"). `interpreter_v1.md`
§6.5's own honesty paragraph names what the check cannot PROVE; it does
not name that the check makes a whole legitimate class mechanically
unscoreable.

**Fix shape, rewritten (r7code-1): the cited join does not close the
window it claims to.** The v1 draft of this fix named "the join
R-STATUS-1 and R-BUCKET-SPAN already use" — the `record_id_of` join
against a report's `record` rows. That join recovers exactly the
*included* records' own index rows; it does **not** recover which OTHER
index rows those records superseded. The kept→superseded id mapping lives
only transiently inside `report.py`'s `dup_groups` processing
(`report.py:3166-3206`, `superseded.append((kept_r.setup["record_id"], […])`)
and the only trace of it that survives into a committed TSV is a scalar
count in the header (`report.py:4446`, `f"superseded: {sum(len(v) for _k,
v in rd.superseded)}"`) — the mapping itself is discarded after
rendering. A reader implementing the fix literally, via that join, gets
the report-scoped earliest timestamp with NO supersession extension at
all, which is not what this fix promises.

**The corrected construction**: reuse OD-B15's own dedup key, not the
R-STATUS-1/R-BUCKET-SPAN join. For each of the report's included records,
take its `(subbench, version, testee_id, machine_id)` tuple (via the
record_id→index-row join — the one piece `check_stated_utc` genuinely
gains from a `report` argument) — `index.tsv` carries `testee_id` and
`machine_id` directly (`INDEX_COLUMNS`, `interpret.py:67`) — then take the
minimum index timestamp over **every** `index.tsv` row sharing that
tuple. That recovers the superseded population by the same grouping key
the reporter itself dedups on (`report.py:3166-3168`), with no read of
the reporter's discarded mapping and no store load — KB-16 is preserved.
This keeps "code only, store-free," but it is a DIFFERENT join from the
one originally cited, one line longer, and the note's "Code only" framing
did not previously mention that `check_stated_utc(predictions, index,
where=...)` has no `report` parameter today (`interpret.py:1700`) and
needs a signature change at its one call site (`interpret.py:2159`).

**Two stated risks for the panel's ruling, both ways (r7ver-7, r7pop-4).**
Neither is disqualifying on its own; the panel should weigh them rather
than treat the re-anchor as a strict improvement, which is how the v1
draft (and §7 Q7 below) originally framed it.

1. **Gameability (r7ver-7).** The CURRENT global anchor — the earliest
   `store/index.tsv` timestamp for the whole `(subbench, version)`,
   monotonically non-decreasing — cannot be gamed by a report's own
   `--since`/`--until`/`--where` filters, because it never reads them. The
   proposed anchor IS a function of a scope decision made after the
   predictions were authored: an author who already knows a later
   sample's numbers (the exact honesty failure §6.5 exists to catch)
   could, in principle, construct or select a report whose filters
   exclude the early records that would make `stated_utc` fail, and pass
   a `stated_utc` the global anchor would have refused. This is not a
   contrived scenario here: `--since`/`--until`/`--where` queries are this
   project's ordinary way of building a report (`reports/CLAUDE.md`'s own
   convention), so report-scope narrowing is an everyday act, not an
   adversarial edge case that needs inventing.
2. **The fix closes only the same-testee half of the residual (r7pop-4).**
   Even with the OD-B15 join above closing the supersession window, the
   anchor is still only as recent as the report's OWN testee/config
   selection. A report scoped (by filter, not by the store's real state)
   to exclude an older baseline moves the anchor forward to the newest
   pin's own earliest record, and would then accept a `stated_utc`
   authored after the analyst had already seen results from OTHER,
   differently-configured testees of the SAME `(subbench, version)` that
   the report's filters simply chose not to include — the
   cross-testee/cross-config half of the "residual limit"
   `interpreter_v1.md` v1.1 already named once for a related supersession
   gap. The fix closes the SAME-testee half explicitly ("the supersession
   window closed") but not this half, and the panel should be told so
   rather than have the re-anchor read as a strict improvement.

**Cost, corrected (r7ver-8): the design note itself is now stale and owed
a revision.** `interpreter_v1.md` §6.5's own honesty paragraph names what
the check cannot PROVE; it does not name that the check makes a whole
legitimate class mechanically unscoreable — which is exactly what this
finding demonstrates. Consistent with how this project has always folded
a built-vs-designed correction back into the design note of record (v1.1
through v1.4 each did this), Group 5's cost list must include revising
`interpreter_v1.md` §6.5 to state the new class explicitly, alongside the
two stated risks above.

Code only, no catalogue change — but it changes what the check REFUSES,
needs `check_stated_utc`'s signature change, an `INTERPRET_VERSION` bump
(r7ver-3, below), the `interpreter_v1.md` §6.5 revision (r7ver-8), and a
fixture on both sides, so it wants the panel's word on the two stated
risks above before it lands. The interim, if the panel prefers to wait:
nothing in the tool, and a `--no-check-utc` style escape is NOT
recommended, because an escape hatch on the one check that keeps a
prediction honest is the wrong default to add.

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

Nothing here is adopted. **Rebuilt (r7ver-4) over all FOUR regeneration
surfaces this project's own tooling gates on** — `catalogue/rules.toml`
(the catalogue version), `INTERPRET_VERSION` (§6.05, new), committed
sidecars, and the two surfaces the v1 draft never named at all:
`catalogue/fixtures/fixtures.toml` (each of the 31 rules ships a
control/sabotage pair `make check-interpret`'s fixture section asserts by
name) and `catalogue/golden/<report>.facts.tsv` (`acceptance_10.py`'s
pinned facts for the three named acceptance reports, refreshed only by a
commit `catalogue/CLAUDE.md` recognizes as entitled to move a golden
fact). The v1 draft's groups named only two costs (catalogue bump,
sidecar regeneration) and — per r7ver-1/r7ver-2 — mis-bucketed F7 and
F7b against their own evidence. The table below is the corrected cost
model; the group prose after it is unchanged in shape but re-derived from
the table, not from the original two-cost framing.

| fix | catalogue bump | `INTERPRET_VERSION` | sidecars | fixtures | goldens |
|---|---|---|---|---|---|
| F15 (three load checks) | none | no | none today (no witness renders differently) | none | none |
| F16 (extreme by op direction) | none | no | none today (F8 must land first to expose it) | none | none |
| F19 (guard floats) | none | no | none today (0 witnesses) | none | none |
| F7b-code (retry `_elsewhere`, dropped columns) | none | **yes (r7ver-3)** | none today (same F8 dependency as F16) | none | none |
| **F7** (scope `_ELSEWHERE` by quantity class) | none | **yes (r7ver-3)** | **YES — moves the syntax sidecar's committed P13 line today (r7ver-1)** | none | none |
| **F7b-example** (R-PRED-3's `example` field) | **MINOR (r7ver-2)** | **yes (r7ver-3)** | full regen (§3.3's rule) | none | none |
| F1/F2 (reason channel) | MINOR | not separately asked (catalogue bump already signals) | full regen | none (existing rules' fixtures must still byte-match; no NEW pair) | none |
| F5 (reword + a version-literal check) | MINOR | — | full regen | none | none |
| F8 (R-PRED-4's three slots) | MINOR | — | full regen | none | possible — check against Reports A-D before assuming none |
| **F9** (new rule R-ARM-2) | MINOR | — | full regen | **NEW control/sabotage pair required (r7ver-4) — every one of the 31 existing rules has one; a 32nd rule is not exempt** | **possibly moved — UNMEASURED whether R-ARM-2 fires on any of Reports A-D (532 witnessed triples in the corpus make this plausible, not confirmed)** |
| F18/F20/F21/F22 (state narrowings, add slots) | MINOR each | — | full regen | none | none |
| **F3** (coverage from the selector) | MAJOR, precedent-grounded (r7ver-5/6) — **zero individual-rule field characters move** | **yes (r7ver-3)** | full regen | none | **possibly moved — UNMEASURED against Reports A-D** |
| F4 (read the slice's `excluded` rows) | MAJOR (new `inputs`) | — | full regen | none | **possibly moved — UNMEASURED against Reports A-D** |
| F6/F13 (collapse six rank rows) | MAJOR | — | full regen | none | none named |
| **F11** (widen R-BUCKET-SPAN's partner search) | MAJOR for the `excluded` half; the `did_not_compile` half's join is **TBD at implementation (r7pop-3)** | **yes (r7ver-3)** | full regen | none | none named |
| F14 (`metric` as a selector key) | MAJOR | — | full regen | none | none named |
| F26 (emit `did_not_compile` for a zero-ranking-group pattern) | none (rule's predicate/`inputs` unmoved) | — | `REPORTER_VERSION` bump + full regen | none | none named |
| F10 (`now failing (was: measured)` clause) | MINOR (one new rule) | — | `REPORTER_VERSION` bump + full regen | new pair for the new rule | none named |
| **F27** (`check_stated_utc`'s anchor, rewritten — r7code-1) | none | **yes (r7ver-3)** | fixture on both sides; no existing sidecar moves (the check currently REFUSES, it does not mis-render) | new pair | none | plus `interpreter_v1.md` §6.5 revision (r7ver-8) |

**§6.05 — `INTERPRET_VERSION`, a second stamp this note originally never
named (r7ver-3).** Every rendered sidecar's stamp block carries TWO
version fields, built in one place (`build_stamp`, `interpret.py:2173-2204`):
`("catalogue", cat["catalogue_version"])` and `("interpret",
INTERPRET_VERSION)`. `INTERPRET_VERSION = "v1"` (`interpret.py:54`) has
never moved since it was introduced, across every catalogue bump 1.0
through 2.0 and across multiple documented `interpret.py` changes. No
design document states a bump rule for it. `interpreter_v1.md` §3.3
models the catalogue's OWN regeneration discipline on `REPORTER_VERSION`'s
precedent — "bump whenever rendering changes, so two reports are never
mistaken for each other," applied one layer up. Applied one layer up
AGAIN: `INTERPRET_VERSION` should bump whenever a pure code change (no
catalogue text moves) alters what a sidecar renders — independent of
whether `catalogue_version` also moves, because two different
`interpret.py` builds could render a cell differently at the SAME
catalogue version. **Ruling applied here**: the code-only fix class —
F7, F7b-code, F11, F15, F16, F19 and F27, plus F3 (which per r7ver-5/6
gets a catalogue MAJOR bump with zero individual rule-field text moving,
leaving `INTERPRET_VERSION` as the only signal a reader can check against
the actual code) — MUST bump `INTERPRET_VERSION` in the same commit; this
is folded into each fix's cost line in the table above. `make
check-interpret`'s byte-equality freshness check (§3) already forces
regeneration by content regardless, so nothing is *silently* stale — the
gap is that a regenerated sidecar's own stamp line would read `interpret:
v1` before and after any of these fixes land, giving a reader no way to
tell from the stamp alone that the tool producing the file has changed.
This is the same "context around the numbers" class Frank's 2026-09-17
directive names, applied to the interpreter's own provenance rather than
to a rule's population.

**Group 1 — code only, no catalogue bump, no sidecar regeneration
(corrected).** F7b-code, F15, F16, F19. Each is independently landable
and each closes a whole class. (F7 is removed from this group — see
below.)

**Group 1B — code only, no catalogue bump, but sidecar regeneration IS
required (new, r7ver-1).** **F7** alone: its own witness quotes a
CURRENTLY COMMITTED sidecar line (the syntax report's P13 clause) that
the fix rewrites, so `interpreter_v1.md` §3.3's content-driven
regeneration rule fires even though no catalogue field moves. Plus an
`INTERPRET_VERSION` bump (§6.05).

**Group 2 — MINOR catalogue + §8(6) review (where the field is one of
the four gated ones) + full sidecar regeneration.** F1/F2 (the
did-not-fire REASON channel, now specified for all three of R-FLOOR-2's
causes per r7pop-5 — one mechanism, two live defects, and it is
`interpreter_v1.md` §4.5's own intended rendering for the `none` case),
**F7b-example** (R-PRED-3's `example` field — split out of the original
"F7b" per r7ver-2; `example` is not one of the four §8(6)-gated fields,
so the regeneration and version bump apply without the named-reviewer
line), F5 (reword + a `check-interpret` assertion that no prose names a
catalogue version), F8 (R-PRED-4's three discarded slots — **the cheapest
large win**), **F9** (the new rule R-ARM-2 — now costed with its own
required fixture pair and an unmeasured golden-file exposure, r7ver-4;
see §6.05's note above), F18 (state R-STATUS-12's narrowing), F20 (the
comparand pin), F21 (the 2-member group), F22 (R-STATUS-8's legend).

**Group 3 — MAJOR catalogue (a predicate, a threshold, or `inputs`
move).** **F3** (coverage from the selector, not from the matched rows —
a bug fix against the catalogue's own stated predicate; the panel's MAJOR
ruling now precedent-grounded rather than asserted, per r7ver-5/6 — see
§7 Q2), F4 (read the slice's `excluded` rows — check against Reports A-D
for golden movement before landing, r7ver-4), F6/F13 (collapse the six
identical rank rows before reducing — see the corrected Q4 in §7,
r7pop-1/r7pop-2), **F11** (widen R-BUCKET-SPAN's partner search — the
`excluded` half only; the `did_not_compile` half's join is a SEPARATE,
unspecified fix per r7pop-3, TBD at implementation), F14 (`metric` as a
selector key).

**Group 4 — reporter changes, on §2.5's P-1/P-2 precedent.** Two, and
they belong in one wave because both are `render_tsv` row-emission
changes with one regeneration between them: **F26** (emit the
`did_not_compile` rows for a pattern that reached no ranking group — the
smaller and strictly-additive of the two) and **F10** (a
`now failing (was: measured)` clause on the excluded / refused row,
after which a rule reads it as R-DELTA-3 reads its mirror).
`REPORTER_VERSION` bump + full regeneration + one MINOR rule (with its
own new fixture pair).

**Group 5 — the one gate.** F27, `check_stated_utc`'s population,
**rewritten (r7code-1)**: the anchor is the OD-B15 dedup key's own
minimum timestamp over `index.tsv` rows sharing an included record's
`(subbench, version, testee_id, machine_id)` tuple, not the
R-STATUS-1/R-BUCKET-SPAN join the v1 draft cited — see the finding text
above for the full correction, the `check_stated_utc` signature change it
needs, and the two stated risks (gameability, r7ver-7; the cross-config
look-ahead gap the fix does not close, r7pop-4) the panel weighs before
ruling. Code only, no catalogue change, but it changes what the tool
REFUSES, needs an `INTERPRET_VERSION` bump, an `interpreter_v1.md` §6.5
revision (r7ver-8), and it is blocking a committed file today.

**Recommended order**, if the panel wants one: **F27 first** — it is the
only finding blocking work that is already committed, now against its
corrected fix shape. Then Group 2's F8 and F1/F2 (they make every
existing sidecar honest and cost no predicate). Then Group 1 + Group 1B
(F7's own regeneration is now priced in, not assumed free). Then F9 —
**but only after checking, at implementation time, whether R-ARM-1's
fixture-pair discipline extends a measurable cost to F9 and whether it
fires on any of Reports A-D; this order treats F9 as cheap-then-expensive
on the UNMEASURED assumption that it does not move a golden fact, which
r7ver-4 flags as open, not confirmed.** Then Group 3's F3 and F4 — same
caveat: F3/F4's golden-file exposure over Reports A-D is unmeasured by
this note and must be checked before `refresh_golden.py` is skipped or
assumed necessary. Then Group 4's F26 + F10 as one reporter wave.

---

## §7. Questions for the panel / Frank

**Q1. The did-not-fire REASON channel (F1/F2) — adopt it, or reword the
two `no_fire` sentences?** *Recommend the channel.* Rewording fixes two
sentences; the channel fixes the class, is `interpreter_v1.md` §4.5's own
intended rendering, and keeps the firewall (reasons are declared,
slot-free, §8(6)-reviewed prose like `no_fire`).

**Q2. When the code and the catalogue's `predicate`/`threshold_src`
disagree and the PROSE is right (F3, F11) — is the code fix MINOR or
MAJOR?** *Recommend MAJOR — corrected and now precedent-grounded
(r7ver-5, r7ver-6).* The original framing of this question was a false
binary: checked directly against the catalogue text, R-DELTA-4's
`predicate` (`rules.toml:678-683`) and R-BUCKET-SPAN's `threshold_src`
(`rules.toml:1213-1220`) ALREADY read the corrected population F3/F11
fix — **zero characters of any individual rule's `predicate`, `threshold`,
`threshold_src` or `inputs` field would change**, because the declared
text is already right and only the `interpret.py` function is wrong.
Read literally, §3.3's MINOR/MAJOR definitions are worded entirely as
edits to catalogue FIELDS ("a rule's PREDICATE or THRESHOLD changes,"
"`inputs` change in a way that reads a different column"); a fix that
edits no field triggers neither definition on its own text, and there is
nothing in `rules.toml` for a mechanical version-bump process to diff.
**This is not a novel question — the project already answered it.** The
2.0 bump's own justification (`rules.toml:39-49`) is the identical
reasoning shape: "the `_select`'s DEFAULT section read for the four
failure-population quantities … widens … Both are `inputs`-shape changes
to what R-PRED-1..4 can see, at the SAME MAJOR bump" — a change to a
SHARED HELPER, classified MAJOR, without every affected rule's own
`predicate`/`inputs` text being edited line-by-line to match
(`R-PRED-1`'s own `inputs` array is untouched by the (α) widening, which
lives in `_select`). F3/F11 are the same shape: a shared-code fix,
correctly classified MAJOR at the catalogue-version level (a header-
comment-documented bump, `rules.toml`'s own historical practice for every
1.1-2.0 step), without any individual rule's field text moving. The
recommendation (MAJOR) stands, now grounded in this project's own working
precedent rather than asserted as a first-time call; see §6.05 for the
`INTERPRET_VERSION` bump this class also needs, since `catalogue_version`
moving at the header level is not, by itself, a signal a reader can trace
to `interpret.py`'s actual code.

**RULED 2026-09-19 (Frank, live): MAJOR, under a reframed §3.3.** Frank's
framing: MAJOR means incompatibility, MINOR means (compatible) change —
an appended column is MINOR. Applied to this artifact, the unit of
compatibility is not the file format but **whether emitted facts/verdicts
are comparable across the version boundary**: MAJOR = facts move on
unchanged inputs (a pre-fix and post-fix sidecar for the same report
disagree — the 2.0/P5 flip is the precedent instance); MINOR = additive,
every previously emitted fact stands. §3.3 is to be AMENDED to this
definition by the fix wave's first commit (field-text edits become one
instance of incompatibility, not the definition). The wave ships as ONE
catalogue bump at the highest class it contains (MAJOR: F3/F11/F27/Q4's
collapse move facts on unchanged inputs; Q1's reason channel and other
additive items ride the same bump), and `INTERPRET_VERSION` takes its
first bump alongside (r7ver-3).

**Q3. F4's fix: the full one (read the slice's `excluded` rows, MAJOR) or
the interim (state the denominator's subject count, MINOR)?**
*Recommend the full one.* Half the sentence's problem is the omitted
failures; stating only the denominator leaves "of this cell's total"
reading as the set cell's total.

**Q4. Should the six identical rank metric rows collapse to one per cell
for the four failure quantities (F6/F13)?** *Recommend yes, but corrected
(r7pop-1).* It is the root cause of the 6× inflated "over N value(s)" and
α's dilution, and for these four quantities the six rows are literally
duplicates. It is a MAJOR that changes no committed verdict under
`identity` (MEASURED: P5.a still refutes, P1.a-c still confirm). The
earlier draft of this recommendation also claimed the collapse "changes
every count/median/max/min one — which is the point," marked MEASURED
with no probe backing it; that clause is struck. Hand-derived from
probe2's own already-verified output: P5.a selects 321 `n_wrong` values,
318 zero and 3 at 10.000; `_reduce`'s `median` branch
(`interpret.py:1880-1886`) is `nums[len(nums) // 2]` after sorting, and
sorted ascending the 3 tens sit at the top — index `321 // 2 = 160` lands
inside the 318 zeros, so **median = 0**. Collapsing the six duplicate rank
rows to one per cell turns this into 66 values (51 rank + 15 `excluded`),
63 zero + 3 at 10.000; index `66 // 2 = 33` still lands inside the zeros
→ **median = 0, unchanged**. The collapse moves the clean:dirty ratio from
318:3 (106:1) to 63:3 (21:1) — still overwhelming, and the `median`
reducer's picked VALUE does not move, let alone flip a verdict. **The
collapse is still the right fix for F6's row-count inflation** (the
"over N value(s)" number stops meaning two different things depending on
quantity class) and it is necessary groundwork, but **on its own it does
NOT close F13's median-invisibility hazard** (see the corrected F13 text,
r7pop-2) — that needs the separate load check F13's own fix-shape
paragraph proposes (refusing an averaging reducer on a failure quantity),
landed together with the collapse, not instead of it.

**RULED 2026-09-19 (Frank, live): YES AS RECOMMENDED** — the collapse
(one row per cell for the four failure quantities) AND F13's companion
check (an averaging reducer refused on a failure quantity) land
TOGETHER. MAJOR class under the Q2 ruling (counts move on unchanged
inputs; the hand-derived no-verdict-flip stands as the identity
evidence, not as the class). Joins the held fix wave — one catalogue
bump with F3/F11 (and F27 when revisited).

**Q5. `metric` as a seventh selector key (F14)?** *Recommend yes* — the
additive half. It fixes the base-row/detail-row mixing, and it also lets a
clause target `jitter` or `artifact_bytes` explicitly, which no committed
prediction can express today.

**Q6. F10's reporter clause — now, or filed?** *Recommend filed with
a named trigger*: the first AFTER window whose ledger reports a cell that
left the ranking. All 38 corpus instances are improvements, so the hole has
not cost us anything yet; it will cost us exactly once, in the report where
it matters most.

**Q7. F27 — re-anchor `check_stated_utc` to the report's OWN records?**
*Recommend YES, and first, weighed against two stated risks (not a strict
improvement — r7ver-7, r7pop-4).* The check today anchors to the set's
first-ever measurement, which never moves, so no predictions file about a
second sample of an already-sampled set can pass — and one is committed
and unusable right now. Anchoring to the OD-B15-keyed earliest index
timestamp of the records THIS report includes (the corrected join,
r7code-1, not the R-STATUS-1 join this note originally cited), with the
supersession window closed the way §6.5's own correction closed it, is
strictly what the check wants to prove and moves forward with each
sample, staying store-free. **But it is a trade, not a pure gain**: the
current global anchor cannot be gamed by a report's own filters, and the
report-scoped one is a function of a scope decision made after the
predictions were authored (r7ver-7's gameability argument); and even with
the supersession window closed, the fix narrows only the same-testee half
of the residual `interpreter_v1.md` v1.1 already named, leaving the
cross-testee/cross-config half open (r7pop-4). Neither risk disqualifies
the fix — the gaming scenario needs an author already acting in bad
faith, which no anchor here was ever going to catch in every case — but
the panel should rule with both stated, per the full argument in F27's
§4 entry. No escape hatch: a `--no-check-utc` flag on the one check that
keeps a prediction honest is the wrong thing to add.

**DEFERRED 2026-09-19 (Frank, live): "I'll revisit this question later."**
Presented with both risks and the manager's fold-in (an unconditional
rendered line naming the anchor actually used, whichever anchor is
ruled). Until ruled: CLI prediction scoring stays blocked (the ext-roster
file's clauses stay hand-scored in ledgers, stated as such), and the fix
wave HOLDS rather than splitting into two MAJOR bumps — one catalogue
bump, one sidecar regen, when F27's ruling lands.

**Q8. F26 — emit the `did_not_compile` rows for a pattern that reached no
ranking group?** *Recommend YES*, in the same reporter wave as F10. It is
strictly additive to the TSV, it does not move R-STATUS-4's predicate or
`inputs`, and without it the rule's `no_fire` is a false sentence on any
report whose refusals are total — including the one carrying
`bench/bounded`'s own 65535-cap refusal.

**Q9. Does this audit want a standing `check-interpret` section?** A
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
reporter v17, `interpreter_v1.md` v1.4, record schema v1.6) plus seven
read-only probes run in this lane, archived with their scripts at
`docs/dev/measurements/2026-09-18-predicate-audit-probes.txt` and
`…-probe{1..7}.py`. Code citations are `pcrecbench/interpret.py`,
`pcrecbench/report.py`, `catalogue/rules.toml` and
`catalogue/check_interpret.py` as committed at that revision; document
citations are `docs/design/interpreter_v1.md` (v1.4),
`docs/design/interpret_subject_grain_v1.md`, `docs/dev/predictions/CLAUDE.md`
and the six committed `reports/*.interpretation.md` sidecars. Every
contested number is marked MEASURED and traceable to a named probe. No
file under `store/`, `reports/`, `catalogue/`, `pcrecbench/` or `~/pcrec`
was modified by this lane.

**v1.1's own source.** The R7 panel (`docs/dev/reviews/2026-09-18-r7-
predicate-audit.md`) re-derived every code citation and corpus count
independently against the same `HEAD` = `4eb413a` (`git diff` to
`8a0ec37` at panel time touched only `docs/`, confirmed zero code/
catalogue drift) plus re-runs of all seven archived probes and two
from-scratch one-liners sharing no code with `interpret.py`. No new
probe was run for v1.1 itself; every correction above is either a
hand-derivation from an already-archived probe's output (r7pop-1,
cited inline) or a direct code/contract citation (r7ver-1..8,
r7code-1..2), stated as such at each edit.
