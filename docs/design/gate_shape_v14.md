# The quiet gate's shape after BD7 — record schema v1.4, the SPEC (2026-08-30)

STATUS: **SPEC, awaiting the critic panel** (plan row [B20]; the manager
skill §6). Written by the [B20] design lane from the PROPOSAL below
(kept verbatim as §H, "History") after Frank's ruling (inbox I-19 (1)):
BD7 — the 5-s mpstat average — is RATIFIED as the gate; his items (2)-(4)
ARE the v1.4 spread rule as proposed; the per-second peaks stay in `raw`.
Every constant in §3 is MEASURED from the canonical store
(`docs/dev/measurements/2026-08-30-trial-agreement-census.txt`,
`probe_trial_agreement.py`), not picked. Nothing in this note changes a
record today: the harness does what quiet_baseline.md's 2026-08-30 section
says until the implementation lane lands §4-§8 and the panel has ruled on
§9.

Sections: §1 the gate · §2 the after samples as provenance · §3 trial
agreement (the census, k, F, the block, `inconclusive-spread`) · §4 the
validator and schema changes · §5 the harness changes · §6 the reporter
changes · §7 migration · §8 the checks · §9 open questions · §H history
(the proposal as ruled on).

Vocabulary used throughout: a ROW is one (pattern, regime, form, subject)
cell of a record — its N trials are N match rows in the file; "ns/iter"
is `timing.elapsed_ns / timing.iterations`, the reporter's own
per-call comparable (`pcrecbench/reduce.py` `ns_per_call`); a PASS is
one trial's sweep over every subject of one (pattern, regime) group
(`harness.py`: trials are interleaved by group, so trial t of every
subject in a group is one contiguous 1-2 s of wall time).

---

## 1. THE GATE (BD7, ratified) — the pre-flight decides `inconclusive-load`

**The pre-flight**, run by `quiet.check()` + `quiet.gate()` BEFORE the
harness pins to the target core, refuses (exit 3, the message naming
every failing clause) unless ALL of:

| clause | instrument | limit | today |
|---|---|---|---|
| (a) `load.before.load1 ≤ LOAD1_LIMIT` | `/proc/loadavg`, one read | 2.0 (quiet_baseline.md) | unchanged |
| (b) every NON-TARGET core's 5-s average busy ≤ `MAX_BUSY_PCT_LIMIT`, the target's SMT sibling judged like any other core | `mpstat -P ALL 1 5`, the `Average:` block (BD7) | 10.0 % | unchanged |
| (c) **NEW — Frank's item 1, second clause:** the TARGET core's own 5-s average busy ≤ the same limit | the same capture; the target's row, which today is EXCLUDED from the judgement | 10.0 % | new |
| (d) the occupancy sample is not `unavailable` | — | — | unchanged (the v1.1 ruling) |

`--force-unquiet` turns the refusal into a record with `status =
inconclusive-load` and the reasons in `status_detail`, exactly as today.
Nothing else changes about `inconclusive-load`: it keeps its name, its
enum position, and its meaning "the box was not known to be quiet when
this was measured".

**Why (c), and why it must be a PRE-flight clause.** Nothing of ours runs
on the target core before the harness pins to it, so a busy target core
before the run is a competitor that will sit UNDER every trial. The
manager's correction (§H, accepted by pcrecdev1 and Frank) is exactly
that a steady competitor is invisible to trial agreement — it lowers the
pinned core's boost clock, or shares its execution resources,
UNIFORMLY across all five trials, so the trials agree with each other
and with the wrong number. A per-core sample before the run is the
only instrument that sees it, and today's `judge_mpstat(exclude_cpu=…)`
deliberately drops the one row that would. The AFTER sample cannot
serve here: after the run the target core reads OUR driver's own
decaying occupancy, which is not evidence of anything.

**Fields. One new OPTIONAL field on `occupancy_sample`, nothing else in
the sample blocks changes:**

| field | type | req | rule | why |
|---|---|---|---|---|
| `environment.occupancy.<sample>.target_busy_pct` | number 0-100 / null | o (v1.4: the harness writes it on BOTH samples whenever `pinning.cpu` is an integer; `null` iff the sample is `unavailable`) | in `before`, the target core's judged busy % over the same capture `max_busy_pct` came from; in `after`, the same number, DIAGNOSTIC only (it reads our own driver). NOT part of `verdict` — X26 is untouched: `verdict` is still `pass` iff `max_busy_pct ≤ limit_busy_pct`, the non-target judgement. X13 (§4) is what reads it | the number the new clause judged, beside the verdict it does not enter. `raw` already prints the target's row (BD7's "target cpuN excluded from the judgement" line); this makes it a field so X13 can be a rule and not a regex over `raw` |

The alternatives were weighed and rejected: (i) folding the target into
`before.max_busy_pct` changes the MEANING of an existing field for one
sample and not the other (a v1.3 reader would silently read a different
quantity); (ii) a third sample block `target_before` duplicates the
capture's timestamp and raw text for one number. A field beside the
verdict, with the verdict's rule unchanged, is the smallest true change
— and it keeps X26 holding for every sample of every version (the
brief's condition). The consequence the panel should see: a v1.4 record
can carry `before.verdict = pass` and `status = inconclusive-load`
because the target core was busy; `status_detail` says so by name
(§5). That is the same shape as today's `load.verdict = quiet` beside a
failed occupancy — two instruments, one status.

**The limit is the same 10 %.** The target core before the run is an
idle core like any other; the noise floor (2-7 %, quiet_baseline.md)
applies to it as to the others. A separate constant would be a number
nobody measured.

## 2. THE AFTER SAMPLES AS PROVENANCE

**X13, revised (v1.4).** `status = measured` requires:

1. `load.before.load1 ≤ load.limit` (the pre-flight's own load clause —
   note: NOT `load.verdict = quiet`; the verdict stays X20's "either
   sample" and becomes provenance, see below);
2. `occupancy.before.verdict = pass` (so not `fail`, not `unavailable`
   — the v1.1 ruling stands: an unmeasured pre-flight is not `measured`);
3. when `pinning.cpu` is an integer: `occupancy.before.target_busy_pct`
   is PRESENT, a number, and `≤ occupancy.limit_busy_pct`;
4. `trial_agreement.verdict ≠ disagree` (§3);
5. X14's compile-row clause, unchanged.

The AFTER samples — `load.after` and `occupancy.after` — are recorded
exactly as today, with X19 (the parse agrees with `loadavg_raw`) and X26
(the verdict agrees with the number) still enforced on them, and they
NEVER disqualify a v1.4 record. They are provenance: the number a
reader needs when a record's trials look odd, kept with its verdict so
the reader does not have to re-derive it, and kept with the per-second
peaks in `raw` (I-19: "keep the per-second peaks in raw as you do") so
the transient the average absorbed is still visible.

**`load.verdict` under v1.4.** X20 is unchanged — `loaded` iff EITHER
sample's `load1` exceeds `limit` — so a v1.4 record whose box got busy
after the run carries `load.verdict = loaded` beside `status =
measured`. That is deliberate, and it is why X13 reads `load.before`
directly instead of the verdict: the verdict answers "was the box
loaded at either end", which remains a true and useful filterable fact;
the status answers "was this number measured under the protocol", which
v1.4 defines as the pre-flight plus trial agreement. The alternative —
redefining X20 to the before sample only — changes the meaning of a
v1.3 field, which is a MAJOR bump by §4's rule.

**`status_detail` wording.** When any after sample failed on a
`measured` record, the harness appends ONE note per instrument to
`status_detail`, in this exact shape (a note, not a status; the reporter
prints it in the R1 excerpt of a `measured` row only under
`--include-provenance`, §6):

    after-sample (provenance, not a verdict): occupancy after the run 20.20% busy on the busiest non-target core (limit 10.00%); the trials' agreement decided the status (v1.4 X13)
    after-sample (provenance, not a verdict): load1 after the run 11.40 exceeds the limit 2.00; the trials' agreement decided the status (v1.4 X13)

Today `status_detail` is written only when `status ≠ measured`
(`harness.py` (5): `status_detail=(… if notes and status != "measured"
else None)`); under v1.4 it is written whenever there is a note, on
every status, so the provenance lands in the field the reporter already
excerpts. The schema already allows it (`status_detail` is optional
free_text on every record).

## 3. TRIAL AGREEMENT — the rule, its constants measured, the block, the status

### 3.1 The census (what the store says)

`docs/dev/measurements/probe_trial_agreement.py`, run read-only over
every record in the canonical store — **68 records** (schema 1.1 × 11,
1.2 × 3, 1.3 × 54; 59 `measured` + 9 `inconclusive-load`; five pcrec pins
and libpcre2 10.46; every one measured on `budu-ryzen1600` with core 11
pinned) — archived verbatim as
`docs/dev/measurements/2026-08-30-trial-agreement-census.txt`. Rows
judged: every timed row (`matched-as-expected`, `timing.iterations > 1`,
≥ 2 timed trials), grouped by (pattern, regime, form, subject): **62,923
rows, every one with exactly 5 trials.** Per row: the per-trial ns/iter,
the median; a trial is a SLOW outlier at k if it is strictly above k ×
median, a FAST outlier if the row's minimum is below median / k.

| k | rows with ≥ 1 slow (per-record median / max) | rows with ≥ 2 slow, all records | rows with a fast outlier, all records | rows DISAGREEING (≥ 2 slow OR fast), all records | records with any disagreeing row | worst record's disagreeing fraction |
|---|---|---|---|---|---|---|
| 1.25 | 0.81 % / 13.64 % | 21 (0.033 %) in 10 records | 37 | 58 (0.092 %) | 20 of 68 (6 above 0.5 %, 1 above 1 %) | **1.996 %** (10 of 501; the one `loaded` record, below) — the worst MEASURED record 0.93 % (3 of 321) |
| **1.5** | 0.17 % / 11.58 % | **0** | **1** | **1 (0.0016 %)** | 1 of 68 | **0.204 %** (1 of 490) |
| 2.0 | 0.00 % / 5.79 % | 0 | 0 | 0 | 0 | 0 |

Three facts the rule is built on:

1. **Single slow trials are common and are absorbed.** At k = 1.5 a row
   with ONE slow trial occurs at a per-record median of 0.17 % and up to
   11.6 % of rows; the median of five never moves for it. Their slowest
   trial's index over all 387 such rows: t1 36, t2 155, t3 41, t4 94,
   t5 61 — trial 1 is the LEAST frequent, so this is not warm-up, it is
   the box (the gate-shape probe's characterisation stands: one PASS of
   one group ~2× slower, a sibling burst or a boost drop).
2. **A second slow trial on the same row is absent from the store at
   k = 1.5.** Zero rows in 62,923. At k = 1.25 it appears (21 rows in 10
   records), which is the noise floor being reached, not disturbance:
   the p90 per-row spread of a clean cell is 6-19 % (the gate-shape
   probe), so 1.25× is inside what two ordinary trials can differ by.
3. **Fast outliers exist at 1.25× and vanish at 1.5×.** The proposal's
   model — "a burst can only add time" — is not exact at the 25 % level:
   37 rows have one trial ≥ 20 % FASTER than the median (e.g.
   `factored / short-subject-search / s-013`: 604.9 605.7 636.1 604.3
   **430.6**), a boost or cache state the model does not name. At 1.5×
   exactly one remains, a 3-2 split at the timer floor (the `floor`
   pattern, `s-081`: 13.9 9.3 14.2 9.2 13.9 ns — two clusters 5 ns
   apart on a 10 ns call). So the fast clause is a real clause, and it
   is quiet at 1.5.

**The one positive control the store has, and what it says.** The store
holds exactly one record measured while something large ran on the box:
`email-specimen@0.2 × libpcre2 interp`, 2026-08-29T18:48:41Z — load1
1.14 before / **11.40** after, occupancy 5.05 % before / **41.41 %**
after (`inconclusive-load` under v1.3, on both after samples). At
k = 1.25 it is the worst record in the store (1.996 % disagreeing, 10
rows); at k = 1.5 it has ZERO disagreeing rows. Which is right? Its set
medians against its clean re-run 111 minutes later (2026-08-29T20:39:45Z,
`measured`): `orig` throughput / match / search 1.009 / 1.017 / 1.015,
`factored` 1.006 / 1.018 / 1.002 — 0.2-1.8 % slower, INSIDE the box's
run-to-run spread (the 08-28 vs 08-30 pair of the same testee moves
0.3-1.0 %). The competitor arrived as the cell ended (a load1 of 11.4
takes minutes of ~11 runnable processes to build; the after sample saw
them, the trials did not). **k = 1.5's silence on this record is
correct; k = 1.25 would have flagged good numbers.** This is also the
honest limit of the rule: the store contains NO record whose numbers a
mid-run competitor actually moved, so the rule's positive case is
argued from the mechanism (§3.3), not shown on a record. §8 adds a
synthetic control; §9 Q3 asks whether a deliberate one should be
measured.

### 3.2 The rule: `v1.4-1of5`, k = 1.5, F = 1 %

Per judged row (≥ 2 timed trials, `iterations > 1`), with `m` the median
of the row's per-trial ns/iter:

- `slow` = the number of trials with ns/iter **> k · m**;
- `fast` = 1 if **min(ns/iter) < m / k**, else 0;
- the row **DISAGREES** iff `slow ≥ 2` OR `fast = 1`.

Per record: `rows_disagreeing / rows_judged > fraction_limit` ⇒ verdict
`disagree`, else `agree`. **k = 1.5, fraction_limit = 0.01.**

Read as the proposal wrote it: one slow trial of five is a tolerated
perturbation (the median is untouched; the store shows it is the box's
ordinary behaviour); two are a disagreement (two passes of the same
group were perturbed, or the cell is bimodal); a fast outlier is a
disagreement of the other kind — if one trial is faster than m / k
then the median is at least k× above a value the machine demonstrably
reached, i.e. the number the reporter would rank is itself perturbed.
The two clauses together say: the five trials agree on the number to
within 1.5×, allowing one of them to be off.

**Why k = 1.5 and not 1.25 or 2.0.** 1.25 is inside the clean spread
(fact 2 and 3 above: it flags 20 of 68 quiet-box records at some level,
one of them measured at 0.93 %, and the fast clause fires 37 times on
states that are not disturbances). 2.0 is blind to half of the
characterised bursts: the gate-shape probe's group-wide outliers are
2.25× (`cls-upto-32768 / match`, 24.5 vs 10.9) but also 1.76× (`dotted4
/ match`, 38.8 vs 22.1) and 1.70× (`nest2-64 / search_short`, 346 vs
204) — a two-pass disturbance of the 1.7× kind is invisible at k = 2.0
and counted at k = 1.5. 1.5 is the value that is both quiet on every
clean record (0 slow pairs, 1 fast outlier in 62,923 rows) and
sensitive to every burst size the box has been seen to produce.

**Why F = 1 %.** (a) NO FALSE POSITIVE ON THE STORE: the worst record's
disagreeing fraction at k = 1.5 is 0.204 % (1 row of 490); F = 1 % is
4.9× above it, and in rows: the smallest pinned cell (321 rows,
email@0.1) tolerates 3 disagreeing rows and has 0; the largest (1,536,
bounded) tolerates 15 and has 0; the worst has 1 of 490 against 4
allowed. (b) SENSITIVITY: the rule flags a cell where ≥ 2 of 5 trials
are ≥ 1.5× slower on more than 1 % of its rows — 16 rows on a bounded
cell, 5 on an email cell, 14 on a loglines cell. Every (pattern,
regime) group in the match and search regimes of the three sets has
≥ 23 subjects (bounded 23-30, email 85, loglines 112), so a disturbance
that overlaps TWO passes of ANY ONE such group flags the cell; a
disturbance confined to two passes of one throughput group (4-5
subjects) does not on its own — and does not need to, because the
median of that group is unmoved by a 3-2 split; a disturbance covering
THREE or more passes moves the median and is caught by the fast clause
on the same rows. (c) The margin is stated as a ratio (4.9×) rather
than as a count because the fraction, not the count, is what the rule
judges; §9 Q4 asks whether a tiny cell (a `quick` run of 10 rows, where
1 row is 10 %) needs a row-count floor — at the store's measured base
rate of 1 disagreeing row in 62,923 the false-flag probability of a
10-row cell is 0.016 %, so this spec does not add one.

**What the rule cannot see, stated once.** A slowdown UNIFORM across all
five trials — a steady competitor on any core (boost clock), a
competitor on the SMT sibling (execution resources), a competitor on
the target core itself, a thermal state. Those are the pre-flight's job
(§1 (b), (c); `cpu_mhz` in the environment), which is why the
pre-flight stays per-core and gains the target clause. The rule and the
gate are complementary instruments, not one checking the other.

### 3.3 The block: `trial_agreement` in the SETUP layer

| field | type | req | rule | why |
|---|---|---|---|---|
| `trial_agreement` | object | **REQUIRED at v1.4 on every record with ≥ 2 trials of any match row** (pinned or scratch; `--trials 1` runs — the smoke suite — have no agreement to judge and carry NO block); FORBIDDEN on a record with no match row of `trial ≥ 2` | the rule's inputs, outputs and verdict, every number recomputable from the rows (X32) | the status depends on it, so the record must carry what decided the status — the same argument as `load.limit` beside `load.verdict` (X20) and `limit_busy_pct` beside the occupancy verdicts (X26) |
| `trial_agreement.rule` | const `"v1.4-1of5"` | R | names THIS definition; a changed definition is a new const and a schema bump | a verdict without the rule that produced it is re-judgeable by nobody |
| `trial_agreement.k` | number > 1 | R | the outlier ratio the run used (1.5) | data, not a schema constant (quiet_baseline.md's own argument for `load.limit`) |
| `trial_agreement.fraction_limit` | number 0-1 | R | the per-record fraction the run used (0.01) | as above |
| `trial_agreement.rows_judged` | integer ≥ 0 | R | the count of (pattern, regime, form, subject) rows with ≥ 2 timed trials and `iterations > 1` (X32 recomputes it) | the denominator |
| `trial_agreement.rows_disagreeing` | integer ≥ 0 | R | the count of judged rows that DISAGREE per §3.2 (X32 recomputes it) | the numerator |
| `trial_agreement.worst_row` | object / null | R | `null` iff `rows_judged = 0`; else the judged row with the largest `max / median` ratio (ties: the first in `seq` order): `{pattern_id, regime, form, subject_id, ns_per_iter: [per trial, in trial order], slow, fast}`; its ids must exist in the record (X7's argument; X32 checks the ids and that `slow`/`fast` recompute) | the reader's first look, without re-reducing 1,500 rows; DIAGNOSTIC beyond the id check |
| `trial_agreement.verdict` | enum `agree` / `disagree` | R | X31: `disagree` iff `rows_disagreeing > fraction_limit × rows_judged` (so `rows_judged = 0` ⇒ `agree`, "0 of 0 rows disagree"); FILTERABLE | the verdict beside its numbers, required to agree with them |

Placement: the SETUP layer, beside `status`, not per match row. A
per-row flag would be 2-6 thousand copies of a boolean the rows already
imply (§4's own size argument against per-row facts), and the status is
a per-record fact. The block is the ONE place this schema stores a
number DERIVED from rows (record_schema.md §10.3 says statistics stay
reader-side); the justification is that it is a VERDICT with its
evidence, held to the X20/X26 standard — recomputable and required to
agree — and not a statistic anyone ranks on. §9 Q5 puts that tension to
the panel explicitly.

### 3.4 The status: `inconclusive-spread`

A new `record_status` value, stamped when the pre-flight PASSED
(otherwise `inconclusive-load` takes precedence — a box known to be
busy explains any spread, and one status must not hide the other's
reason) and `trial_agreement.verdict = disagree`. Meaning: "the box was
quiet when this started; the five trials do not agree on the number to
within k on more than F of the rows; something ran beside this cell for
at least two passes, or the cell is bimodal for a reason of its own".
`status_detail` carries the numbers:

    trial agreement (v1.4-1of5, k=1.5, limit 1.00%): 23 of 1536 rows disagree (1.50%); worst row cls-upto-32768 / match-compliance / plain / l-00: 12.9 13.0 13.2 29.8 28.7 ns/iter (slow=2 fast=0)

An `inconclusive-spread` record is UNRANKED (reporter R1, §6), exactly
like `inconclusive-load`, and its numbers are printed under the table
the same way; the store accepts it; the dedup rule R2 treats it as "not
measured" (a later measured re-run supersedes it; it never supersedes a
measured record). Precedence, in full: `harness-failure` (§9 Q2) >
`inconclusive-load` > `inconclusive-spread` > `measured`.

---

## 4. THE VALIDATOR AND SCHEMA CHANGES, enumerated

`schema_version` 1.3 → **1.4**, a MINOR bump by §4's rule with no
exception needed: one new enum value (`inconclusive-spread`), two new
OPTIONAL-in-the-schema fields (`target_busy_pct` on `occupancy_sample`;
the `trial_agreement` object on `setup`), one rule revised BY VERSION
(X13), two new rules (X31, X32) that can only fire on a record carrying
the new block. Every 1.1/1.2/1.3 record validates unchanged — see the
last item.

| # | change | file(s) |
|---|---|---|
| S1 | `$defs.record_status.enum` gains `inconclusive-spread` (fourth value; description cites this note) | `schema/record.schema.json` |
| S2 | `$defs.occupancy_sample.properties` gains `target_busy_pct: number 0-100 or null`; the existing `allOf` `if unavailable then max_busy_pct null` gains the same consequence for `target_busy_pct` | `schema/record.schema.json` |
| S3 | `$defs.trial_agreement` (the §3.3 table, `additionalProperties: false`, `worst_row` a nested object or null with its own required list) and `$defs.setup.properties.trial_agreement` referencing it; NOT in `setup.required` (the requirement is conditional on trials, which is X33's job, not JSON Schema's) | `schema/record.schema.json` |
| S4 | `x-record-schema-version` → `"1.4"`; the schema's `$comment` history line | `schema/record.schema.json` |
| V1 | **X13 revised, VERSIONED:** for `schema_version ≥ 1.4` the §2 clauses 1-5; for `< 1.4` the v1.1 text unchanged (both samples pass, `load.verdict = quiet`). The validator already parses the minor (X17's branch) — X13 becomes the first rule that reads it | `schema/validate.py` |
| V2 | **X31** (new): `trial_agreement.verdict` is `disagree` iff `rows_disagreeing > fraction_limit × rows_judged`, `agree` otherwise | `schema/validate.py` |
| V3 | **X32** (new): `trial_agreement.rows_judged` and `rows_disagreeing` equal the counts RECOMPUTED from the record's match rows under §3.2 with the block's own `k`; `worst_row` (when not null) names a (pattern, regime, form, subject) that exists among the judged rows and its `slow`/`fast` recompute. X20's argument: without X32, X31 is inert — a harness can stamp `0 of 1536` beside rows that say otherwise | `schema/validate.py` |
| V4 | **X33** (new): the `trial_agreement` block is PRESENT iff the record has a match row with `trial ≥ 2` (for `schema_version ≥ 1.4`; a `< 1.4` record never carries it — its presence there is rejected as a version error, X17's "written by a newer minor") | `schema/validate.py` |
| V5 | the `--expect-rule` help string and the module docstring: `X1..X33` | `schema/validate.py` |
| V6 | `validate.py`'s X32 recomputation is a SEPARATE implementation from `pcrecbench/reduce.py`'s (§5 H4): ~25 lines, no import of `pcrecbench` (the validator is the harness's dependency, not the reverse, and a control that shares source with what it controls proves nothing — the project's own convention) | `schema/validate.py` |
| E1 | `schema/examples/`: the pcrec example RE-STAMPED at 1.4 with a `trial_agreement` block (verdict `agree`, numbers recomputed from its rows) and `target_busy_pct` on both samples; the v8 and the local examples LEFT at their versions (the 1.1 → 1.2 → 1.3 precedent: the older examples prove the older minors still validate). Plus ONE NEW good example: a 1.4 record with `status = inconclusive-spread`, `verdict = disagree`, rows sabotaged to disagree on > 1 % (so the store's first such record is not the first one the validator ever saw) | `schema/examples/` + its CLAUDE.md |
| E2 | `schema/examples/bad/`, one per new rule, each the 1.4 good example with exactly ONE thing wrong and the hash restamped: `x13-measured-but-target-core-busy.jsonl` (`target_busy_pct` 55 on `before`, status `measured`); `x13-measured-but-trials-disagree.jsonl` (verdict `disagree`, status `measured`); `x13-measured-but-load-before-high.jsonl` (`load.before.load1` 9.8, `load.verdict` restamped `loaded` so X20 stays quiet, status `measured` — the control that shows v1.4 X13 reads the BEFORE sample); `x31-verdict-contradicts-fraction.jsonl` (`rows_disagreeing` 40 of 1536 with verdict `agree`); `x32-rows-disagreeing-not-recomputable.jsonl` (`rows_disagreeing` 0 with rows that disagree — the "stamp 0 beside the rows" sabotage); `x32-worst-row-unknown-subject.jsonl`; `x33-trial-agreement-missing.jsonl` (five trials, no block); `x33-trial-agreement-on-single-trial.jsonl` (one trial, a block); `schema-status-inconclusive-spread-misspelt.jsonl` (`inconclusive_spread` — the token-spelling rule); `schema-target-busy-beside-unavailable.jsonl` | `schema/examples/bad/` + its CLAUDE.md |
| E3 | the EXISTING controls `x13-occupancy-after-fail.jsonl` and `x13-occupancy-unavailable.jsonl` (the after sample `unavailable`) are v1.3-stamped and STAY: they prove the v1.3 branch of X13 still fires. A copy of `x13-occupancy-after-fail` re-stamped 1.4 must be ACCEPTED (an after-sample failure is provenance at 1.4) — that copy goes in `examples/` as the good example E1 describes, not in `bad/` | `schema/examples/` |
| C1 | `check_fields.py`: the §8 field tables of record_schema.md gain the rows of §1 and §3.3 (the diff against the JSON Schema is what it checks; a field in one and not the other fails the build) | `docs/design/record_schema.md` §8; `schema/check_fields.py` unchanged |
| C2 | `check_rules.py`: the §9 rule table gains X31, X32, X33 and the revised X13 text; the directory gains E2's files (a rule with no control, or a control naming no rule, fails the build) | `docs/design/record_schema.md` §9; `schema/check_rules.py` unchanged |
| D1 | `record_schema.md`: §4.1 the 1.4 row; §5 the enum row; §8 the fields; §9 X13 (versioned text), X31-X33; a §6.9 "trial agreement" subsection pointing here; §10.3's "no statistics in a record" amended with the §3.3 exception and its argument | `docs/design/record_schema.md` |
| M1 | **What stays byte-identical for v1.3 records:** every v1.1/1.2/1.3 record in the store validates unchanged (X13's `< 1.4` branch; X31-X33 never fire without the block; the new fields are optional in JSON Schema). `make check-schema` proves it on the older examples left at their versions, and `check-report`'s `mixed_version/minor_pair` fixture proves the reporter still reduces a 1.3 and a 1.4 record of one sub-bench in one invocation (a MINOR pair is accepted, §4) | — |

## 5. THE HARNESS CHANGES, enumerated

| # | change | file |
|---|---|---|
| H1 | `quiet.judge_mpstat(text, exclude_cpu, …)` also returns the target's own judged busy % (`target_busy_pct`, from the same Average block; `None` when `exclude_cpu` is None or the row is missing) in the sample dict; `raw` unchanged | `pcrecbench/quiet.py` |
| H2 | `quiet.gate(load_before, occ_sample, force, …)` gains the target clause: `target_busy_pct` present and `> MAX_BUSY_PCT_LIMIT` ⇒ a reason `"occupancy: the TARGET core cpu11 reads 55.00% busy before the run (limit 10.00%) -- a competitor is pinned where this cell will be"`; refusal / `--force-unquiet` unchanged | `pcrecbench/quiet.py` |
| H3 | `quiet.occupancy_ok(block)` becomes `quiet.preflight_ok(block)`: judges `before` only (verdict `pass`, and the target clause); a new `quiet.after_notes(block, load_block)` returns the §2 provenance sentences for a failed after sample. The `quiet` CLI prints the target core's number on every sample | `pcrecbench/quiet.py`, `pcrecbench/__main__.py` |
| H4 | **ONE derivation:** `reduce.judge_trial_agreement(rows, k=1.5, fraction_limit=0.01) -> dict` (the §3.3 block, computed from a record's match rows via `cells_from_record` + `ns_per_call` — the reporter's own comparable, so the rule and the ranking read the same number per row); used by the harness to stamp and by the reporter to render (§6) and by `quick` to print. The validator's X32 is the deliberate second implementation (§4 V6). `tools/selfcheck.py` pins both to one hand-computed fixture (§8) | `pcrecbench/reduce.py` |
| H5 | `run_cell` (5): status derivation becomes: `inconclusive-load` if the pre-flight had reasons (`gate()`'s list, i.e. `--force-unquiet` was needed: load before, non-target occupancy before, target core before, or `unavailable`); else `inconclusive-spread` if `judge_trial_agreement(rows)["verdict"] == "disagree"`; else `measured`. The after samples produce NOTES (H3), never a status. `status_detail` is written whenever `notes` is non-empty, on every status (§2) | `pcrecbench/harness.py` |
| H6 | the block is stamped on `setup["trial_agreement"]` iff any match row has `trial ≥ 2` (X33), computed AFTER every row exists and BEFORE `store.write` validates | `pcrecbench/harness.py`, `pcrecbench/record.py` (`build_setup` gains the argument) |
| H7 | `record.SCHEMA_VERSION` / the emitted `schema_version` → `"1.4"`; `HARNESS_VERSION` bumped; the `--trials 1` smoke path writes no block and still validates (X33's iff) | `pcrecbench/record.py`, `harness.py` |
| H8 | the per-second peaks stay in `raw` exactly as BD7 left them (I-19); `occupancy.tool` unchanged (`mpstat -P ALL 1 5`) | — |
| H9 | `quick` prints the trial-agreement line under its inline comparable (`trial agreement: agree (0 of 30 rows, k=1.5)`), scratch tier included: a scratch record carries the block and an honest status like any other (§6.8's "its status is still the truth") | `pcrecbench/__main__.py` |
| H10 | `scripts/run_window.sh`: an `inconclusive-spread` cell is retried once like a gate refusal is today (it is the same event — something ran beside the cell), with the first record kept (records are never deleted) and the index count reported per status | `scripts/run_window.sh` |

## 6. THE REPORTER CHANGES

| # | change |
|---|---|
| R1 | the status gate is UNCHANGED: `measured` ranks; anything else is listed under its table as `not ranked: <testee> — <status> (<status_detail excerpt>)`. An `inconclusive-spread` record therefore appears exactly where an `inconclusive-load` one does, with its status shown; `--include-unmeasured` ranks it with `status` in the row, as today |
| R2 | dedup is UNCHANGED in code and gains a case: an `inconclusive-spread` record NEWER than a measured one is "newer, not measured"; a measured re-run supersedes it |
| R3 | a LEGEND line under the status-policy bullet: `- trial-agreement policy (schema v1.4, X31-X33): a record's five trials must agree to within k=1.5 on all but 1 % of its rows (one slow trial of five tolerated; two, or one fast, is a disagreeing row); a record that fails is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance` |
| R4 | the per-testee line in the header's record list gains `agreement: agree 0/1536 (k=1.5)` from the block — from the BLOCK, not re-derived, so a reader sees what the harness stamped (the validator proved it recomputes); for a v1.3 record: `agreement: n/a (v1.3)` — the MIXED-VERSION rule: a v1.3 record has no block, the reporter never invents one, and never re-judges it (§7) |
| R5 | `--include-provenance` (new flag, default off): prints the §2 after-sample notes in the excerpt of a `measured` row's header line. Default off because the notes are provenance by ruling, and a report that printed them beside every measured row would read as a caveat on a number that has none |
| R6 | the R8 Δ note, from the abi-12 ledger §6(a) — a reporter/query FACT, not a v1.4 change, recorded here so the panel does not conflate them: the cross-pin `Δ vs previous version` column fires only when BOTH pins' records are in one query (a `--since` that admits one pin's window yields an empty `delta_verdict` on every row); a report meant to show a Δ must be bounded to include both. Separate row [B-next] in plan.md: matching pcrec testees on the id ROOT across pins |
| R7 | `REPORTER_VERSION` → v9 with a dated line; every committed report is re-rendered with its own query (the reports/CLAUDE.md rule) and the diff CLASSIFIED — the expected diff on existing records is the legend line (R3) and `agreement: n/a (v1.3)` on every pre-1.4 record, and nothing in any number |
| R8 | `pcrecbench/tests/test_report.py`: `test_status_gate_r1` gains the `inconclusive-spread` case; a new `test_trial_agreement_legend_and_na_v13` over a `mixed_version/minor_pair` of a 1.3 and a 1.4 record; a new fixture record at 1.4 with `status = inconclusive-spread` under `fixtures/store/` (validator-accepted by `check-report`'s own fixture gate) |

## 7. MIGRATION

**v1.3 records stay valid and are NOT re-stamped.** A record in the
store is never edited (requirements §6; record_schema.md's X6 corollary).
The validator's X13 is versioned, so a v1.3 record keeps the verdict its
harness computed under the rule of its day; the reporter renders its
agreement as `n/a (v1.3)` and its status as stamped.

**The nine historical `inconclusive-load` records** — the brief counted
five; the store holds nine, every one failed on an AFTER sample with
its pre-flight clean (load1 before 0.44-1.47, non-target occupancy
before 1.00-10.00 %, all `pass`); listed so the panel sees the whole
population:

| record id | after sample that failed |
|---|---|
| `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z` | occupancy 10.10 % (before exactly 10.00, pass) |
| `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z` | occupancy 10.20 % |
| `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z` | occupancy 11.00 % |
| `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260829T184841Z` | load1 11.40 AND occupancy 41.41 % — the §3.1 positive control |
| `email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T192934Z` | occupancy 11.11 % |
| `loglines@0.1__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T201129Z` | occupancy 13.00 % |
| `bounded@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T034510Z` | occupancy 10.10 % |
| `bounded@0.1__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260830T040352Z` | occupancy 20.20 % |
| `bounded@0.1__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260830T050354Z` | occupancy 10.10 % |

Under v1.4's X13 every one of the nine would pass the gate clauses, and
every one has `trial_agreement = agree` at k = 1.5 (0 disagreeing rows
in all nine) — so re-judging would turn all nine `measured`, including
the one with a load1 of 11.4. **They stay as they are.** Reasons: (i) a
record is history — its status is what the protocol of its day said,
and the census's value as evidence depends on the store not having
been rewritten to fit the rule it measured; (ii) nothing is lost:
every one of the nine has a `measured` re-run of the same testee at
the same version in the store, and reporter R2 already prefers the
measured re-run, so no ranking changes by leaving them; (iii) a
re-stamp would require the harness commit, the new hash and a
`migrated-from` field the schema does not have — a MAJOR-bump's worth
of machinery for zero ranking effect. The census file records their
agreement numbers, which is where a reader who wants the v1.4 reading
of them finds it.

## 8. THE CHECKS the implementation must add

Each with what it asserts and its CONTROL (the failing case that proves
the check is a check):

| target | check | asserts | control |
|---|---|---|---|
| check-schema | the 1.4 examples accepted | the good pcrec example at 1.4 and the `inconclusive-spread` example validate | E2's ten sabotages, each rejected FOR ITS OWN RULE (the Makefile loop) |
| check-schema | older examples still accepted | the 1.1 (v8), 1.2 (local) and 1.3 examples validate under the 1.4 validator | `x17-future-major-version` (existing) |
| check-schema | `check_fields` / `check_rules` | the note's tables match the schema; X31-X33 each have a control | delete any E2 file → build fails (existing mechanism) |
| check-schema | X13 is VERSIONED | `x13-occupancy-after-fail.jsonl` (1.3) is still rejected by X13; its 1.4 re-stamp (E3) is ACCEPTED | the pair itself: the same sabotage, two versions, two verdicts |
| check-harness | `check_target_core_preflight` (synthetic capture, like `check_occupancy_average`) | a capture with the target core at 60 % and every other core idle: `judge_mpstat` reports `target_busy_pct = 60`, `verdict = pass` (non-target), and `gate()` REFUSES naming the target core; the same capture with the target at 4 %: no refusal | the non-target verdict is `pass` in both — so the refusal comes from the new clause, not from X26's |
| check-harness | `check_after_sample_is_provenance` | a synthetic after sample at 40 % on a run whose pre-flight passed and whose rows agree: `status = measured`, `status_detail` carries the §2 sentence, `occupancy.after.verdict = fail` (X26 still holds), and the record validates at 1.4 | the same record re-stamped 1.3 is REJECTED by X13 |
| check-harness | `check_trial_agreement_fixture` | `reduce.judge_trial_agreement` on a hand-computed fixture (5 trials × 4 rows: one clean row; one with a single 3× trial → tolerated; one with two 1.6× trials → disagreeing; one with a 0.6× trial → disagreeing): `rows_judged 4`, `rows_disagreeing 2`, verdict `disagree` at F = 0.01 and `agree` at F = 0.5; `worst_row` is the 3× row | `validate.py`'s X32 recomputation on the same fixture written as a record gives the same two counts — two implementations, one fixture |
| check-harness | `check_spread_status_stamped` | a `run` into a scratch store whose driver is made to disagree (the deliberately-wrong-fixture mechanism: a driver flag that sleeps on trials 2 and 4 of every row — `PCRECBENCH_SMOKE_SLOW_TRIALS=2,4`, honoured only under `synthetic`) is written `status = inconclusive-spread` with the block's numbers; the same run without the flag is `measured` | the flag on trial 2 ONLY: one slow trial of five, status `measured` — the rule tolerates one, and the check shows it does |
| check-harness | `check_smoke_has_no_block` | the existing `--trials 1` smoke record carries no `trial_agreement` and validates | X33's `x33-trial-agreement-on-single-trial` control |
| check-harness | `check_scratch_carries_block` | `quick` with 3 trials writes a scratch record WITH the block and prints the agreement line | — |
| check-report | `test_status_gate_r1` extended | an `inconclusive-spread` fixture is unranked, listed by name, ranked under `--include-unmeasured` | the existing measured fixture in the same group ranks |
| check-report | `test_trial_agreement_legend_and_na_v13` | the legend line prints once; a 1.3 record shows `agreement: n/a (v1.3)`; a 1.4 record shows its block's numbers; the minor pair reduces in one invocation | `test_mixed_schema_versions_refused` (existing, MAJOR pair) |
| check-report | `test_provenance_flag` | the §2 sentence appears only under `--include-provenance` | default rendering of the same record lacks it |
| check-report | `test_reporter_version_pin` | v9 and every committed report re-rendered with a classified diff | the existing mechanism |

## 9. OPEN QUESTIONS for the panel

- **Q1 — can the target-core pre-flight ever fail on a pinned-idle
  core, and is 10 % the right bar for it?** Before the run nothing of
  ours is on core 11; the measured noise floor is 2-7 % per core. But
  the window script's own `quiet --samples 6` warm-up and the previous
  cell's driver decay could land on it; the gate-shape data (per-second
  peaks up to 12 % on non-target cores) says a 5-s average keeps it
  under 10. The implementation lane should print the target's number on
  every pre-flight of the first v1.4 window and report the distribution
  before the panel closes this.
- **Q2 — `harness-failure` is a schema value the harness never
  stamps.** `grep harness-failure pcrecbench/*.py` finds nothing: a
  harness exception aborts the run and writes no record. The precedence
  in §3.4 names it first for completeness; whether v1.4 should also make
  it REAL (a record written on a caught exception, X14 firing as
  designed) is a separate question this spec does not answer.
- **Q3 — the rule has no positive control in the store.** §3.1: the one
  contaminated record's numbers were not moved, so k = 1.5 was right
  not to flag it — and nothing in the store shows the rule flagging a
  cell whose numbers a competitor DID move. §8's synthetic control
  (slow trials 2 and 4) proves the arithmetic; a deliberate measured
  control — one cell run with a `yes > /dev/null` pinned to CPU 5 for
  two passes of one group, at the scratch tier, archived under
  measurements/ — would prove the instrument. Recommended; cheap; the
  panel decides whether it gates the implementation or follows it.
- **Q4 — small cells.** F is a fraction with no row-count floor; a
  10-row `quick` cell is flagged by a single disagreeing row (§3.2 (c)
  argues the base rate makes that a 0.016 % event). Scratch records are
  never ranked, so the cost is a printed status. Add
  `min(…, 1 row)`-style floor, or not?
- **Q5 — a derived number in a record.** §3.3 stores counts derived
  from rows, against record_schema.md §10.3's "no statistics in a
  record". The defence is that it is a verdict's evidence under the
  X20/X26 standard (X32 recomputes it). The alternative — the status
  alone, and the reporter re-deriving the counts — makes the status an
  unexplained stamp, which is what X20 was written to end.
- **Q6 — trials other than 5.** With 3 trials the slow-pair clause can
  never fire (at most one trial is above the median of three); with 4
  it can. The rule is defined for any N ≥ 2 and is simply weaker below
  5; should `pinned` require `trials ≥ 5` (X-rule or harness refusal)
  so the rule means the same thing on every ranked record? Today every
  one of the store's 62,923 rows has exactly 5.
- **Q7 — `--trials 1` and X33.** The smoke suite carries no block by
  construction (X33's iff). A `--trials 1` PINNED run would then be
  `measured` with no agreement judged. Q6's `trials ≥ 5` for `pinned`
  closes this too; otherwise the reporter's `agreement:` line should
  say `n/a (1 trial)` and the panel should say whether that ranks.
- **Q8 — `load.verdict = loaded` beside `status = measured`** (§2).
  Chosen to keep X20 and the field's meaning; a reader filtering on
  `load.verdict` gets a true fact. Confirm, or rule the field
  before-only (a MAJOR bump).
- **Q9 — the fast clause at the timer floor.** The single fast outlier
  in the store is a 3-2 split at 9-14 ns on the `floor` pattern — a
  10 ns call on a ~10 ns clock. Should rows whose median is within a
  small multiple of the record's floor-pattern per-call cost be
  exempt from the fast clause, or is one row in 62,923 not worth a
  clause of its own? This spec leaves them in.
- **Q10 — precedence of `inconclusive-load` over `-spread`** (§3.4). A
  forced-unquiet record that also disagrees shows both facts in
  `status_detail` but one status. Confirm.

---

## §H. History — the PROPOSAL as it was ruled on (2026-08-30, unchanged text)

STATUS then: PROPOSAL, not adopted. Written the night of the
bench/bounded@0.1 first window for Frank to rule on WITH the gate-shape
test run's data (docs/dev/measurements/probe_gate_shape.py; the archive
landed beside it). Adoption = a record-schema MIGRATION
(record_schema.md's migration rule), a critic panel (the manager skill
§6), and a reporter change.

### Where the ruling came from

Frank, 2026-08-30 ~01:2x EDT, relayed by pcrecdev1 (durable copy in
inbox I-18): "the gate is over-picky. Cells are pinned to core 11; a
non-target core at 10-20 % for one second is an order of magnitude below
the box's own run-to-run spread (~20 % on byte-identical binaries,
1.81-2.17 ns/B over five runs) — the after-sample rejects cells for a
perturbation the trials already absorb." The shape he asked for:

1. a COARSE PRE-FLIGHT gate — load1 below ~4 and no process pinned to the
   target core or its SMT sibling;
2. DROP the single-core 1-s after-sample as a pass/fail;
3. let TRIAL AGREEMENT decide measured vs inconclusive — the interleaved
   trials against the reporter's own spread rule;
4. record the load/occupancy samples as PROVENANCE, never as a verdict.

The manager's correction, accepted by pcrecdev1 the same night for I-18:
keep the PER-CORE pre-flight (BD7 made it burst-proof by averaging; the
target's SMT sibling — CPU 5 for CPU 11 on this box — is printed and
judged like any other core). Reason: a steady single-thread competitor
anywhere (load1 ≈ 2, passes "< 4") lowers the measured core's boost clock
UNIFORMLY across all five trials, and a competitor on the SMT sibling
halves its execution resources for the whole run — trial agreement cannot
see either; only a per-core sample taken before the run can. Items 2-4
became the proposal below.

### The evidence at the time (the six 36d5963 bounded records, 2026-08-30)

Every `inconclusive-load` record the pinned windows had produced —
`email x pcrec-vm` 11.1 % and `loglines x pcrec-nocaps` 13.0 % on
2026-08-29; bounded's `pcre2-jit` 10.10 %, `pcrec-auto` 20.20 %,
`pcrec-vm-in` 10.10 % on 2026-08-30 — failed on the AFTER sample alone,
load1 quiet, the before-sample clean. `pcrec-vm` passed at exactly
10.00 %. The trial-spread distribution (probe_gate_shape.py over all six):

| cell | after-sample | status | trial spread median / p90 / max | rows > 20 % (of ~1500) |
|---|---|---|---|---|
| pcre2-interp | 1.98 % | measured | 2.7 / 15.3 / 513.8 % | 92 |
| pcre2-jit | 10.10 % | inconclusive | 4.0 / 18.8 / 69.3 % | 127 |
| pcrec-auto | 20.20 % | inconclusive | 1.6 / 8.1 / 131.3 % | 38 |
| pcrec-nocaps | 1.00 % | measured | 1.3 / 6.3 / 75.4 % | 28 |
| pcrec-vm | 10.00 % | measured | 1.8 / 14.1 / 159.3 % | 72 |
| pcrec-vm-in | 10.10 % | inconclusive | 1.4 / 6.3 / 63.0 % | 35 |

The after-sample's verdict has no visible relation to trial agreement:
the "inconclusive" cells sit inside the "measured" cells' spread profile.

**The per-row outliers, characterised** (`probe_gate_shape.py
--outliers=50`, the same six records): 80 rows over 50 % in ~9,000; NOT
trial-1 warm-ups (odd-trial histogram over all six: t2:20 t3:21 t4:25
t5:7, t1: none). Each is ONE trial of five running ~2.2x slower across
EVERY subject of one (pattern, regime) group — `pcrec-auto
cls-upto-32768 / match`: trial 4 = 24.5 ns vs 10.9 on all 23 subjects;
`pcrec-vm dotted4 / match`: trial 3 = 38.8 vs 22.1 on all five `d-*`;
`pcrec-vm year4 / match`: trial 3 = 22-25 vs 9-11; `pcre2-jit nest2-64
/ search_short`: trial 4 = 346 vs 204 on both `r-*`. A trial is one
pass over the group's subjects (~1-2 s of wall time); a uniform ~2x on
the PINNED core for exactly one pass is a burst on its SMT sibling (CPU
5 shares core 11's execution resources) or a boost-clock drop — the
perturbations the after-sample was catching DO reach the measured core,
for one pass, and the median of five trials (`reduce.py`, the reporter's
own reduction) absorbs every one of them: no ranking number moved. That
is Frank's claim, measured: the trials absorb what the gate rejected.

(The three BD7 re-runs of the inconclusive cells, in the archived test
run, showed trial-1 outliers too — t1:3 of 5 rows over 50 % in the JIT
re-run — which the census in §3.1 confirms store-wide: trial 1 is the
LEAST frequent slowest trial, not absent.)

**The spread rule this suggested (P2):** the odd trial is always SLOWER,
never faster (a burst can only add time), so the robust statistics are
the median and the minimum. Rule candidate: per (pattern, regime,
subject) row, count trials above 1.5x the row's median; a row with ONE
such trial is a tolerated perturbation (the median is untouched); a row
with TWO or more (of five) is a disagreeing row; a cell with disagreeing
rows above a small fraction (to be set — 0 of ~1,500 in these six) is
`inconclusive-spread`. The 1.5x and the fraction are the panel's to
measure, not to pick. (§3.1 fact 3 corrects the "never faster" half.)

### The proposal (P1-P4)

**P1 — X13 revised.** `status = measured` requires `load.before` quiet
and `occupancy.before.verdict = pass` (the pre-flight, per-core, BD7's
5-s average). The AFTER samples stay in the record with their X26
verdicts (a verdict beside a number, recomputable) but no longer
disqualify: they are provenance. `inconclusive-load` keeps its meaning
for a pre-flight failure taken under `--force-unquiet`.

**P2 — a trial-agreement block and a status for it.** Per record, a
`trial_agreement` block in `setup` (or per match row — to be designed):
the rule, its parameters, the count of rows judged, the count failing.
A new status value `inconclusive-spread` for a cell whose rows disagree
beyond the rule. The RULE is the open design question: candidates are
(a) the reporter's R8 "within spread" (2 x stddev), (b) a per-row
(max-min)/median bound with a per-cell fraction, (c) a median-vs-min
bound that tolerates one slow trial (warm-up) and rejects a bimodal
cell. The probe's per-row outliers must be characterised first: a rule
set before the outliers are understood is a rule fitted to noise.

**P3 — the reporter.** Status gate R1 admits `measured` only; an
`inconclusive-spread` record is listed unranked with its numbers, like
`inconclusive-load`. The set-grain reduction is unchanged.

**P4 — the pre-flight's SMT sibling.** Already done in BD7's `raw` and
the `quiet` CLI: the sibling is named and judged. A pinned competitor on
the target core itself is caught by the target core reading busy BEFORE
the harness pins to it — a check `quiet.check()` does not make today
(the target is EXCLUDED from the judgement). Proposed: the pre-flight
also refuses if the TARGET core reads > limit before the run (nothing of
ours runs there yet), which is Frank's item 1 second clause.

**Migration.** v1.3 records validate unchanged (no field removed); the
validator's X13 is versioned by `schema_version`; the reporter treats a
v1.3 `inconclusive-load` record whose failure was an AFTER sample as
what it is — the migration note may re-judge those five records under
the v1.4 rule and say so in the report legend, or leave them; a ruling.

### What decided it

The test run: the three inconclusive bounded cells re-measured under
BD7, per cell the status, the spread distribution, and the old 1-s
verdict recomputed from the recorded peaks
(`docs/dev/measurements/2026-08-30-gate-shape-test-run.txt`): all three
measured on attempt 1 (after-samples 1.81 / 2.00 / 3.81 %), the old
1-s gate recomputed from the peaks fails `pcrec-vm-in` on one second at
11.88 %, spread medians repeat within 0.3 points. Frank ruled (I-19 (1)):
BD7 ratified as the gate; (2)-(4) the v1.4 spread rule. This spec is
the result; the panel is next; then [B20]'s implementation lane.
