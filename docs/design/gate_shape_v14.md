# The quiet gate's shape after BD7 — record schema v1.4, the SPEC (2026-08-30)

STATUS: **SPEC, the r3 critic panel APPLIED (2026-08-30), awaiting the
implementation lane** (plan row [B20]; the manager skill §6). Written by
the [B20] design lane from the PROPOSAL below (kept verbatim as §H,
"History") after Frank's ruling (inbox I-19 (1)): BD7 — the 5-s mpstat
average — is RATIFIED as the gate; his items (2)-(4) ARE the v1.4 spread
rule as proposed; the per-second peaks stay in `raw`. Reviewed by a
three-lens read-only panel (measurement validity, schema/validator
consistency, harness/reporter/checks) whose 45 findings and the
manager's rulings R-1..R-20 are compiled in
`docs/dev/reviews/2026-08-30-r3-gate-shape-v14.md`; every accepted
finding is applied in this text, and §H.2 summarises what the panel
changed. Every constant in §3 is MEASURED from the canonical store
(`docs/dev/measurements/2026-08-30-trial-agreement-census.txt` — the
row-level census — and `2026-08-30-trial-agreement-census-groups.txt`
— the group-level census the r3 rule is read from; both from
`probe_trial_agreement.py`), not picked. Nothing in this note changes a
record today: the harness does what quiet_baseline.md's 2026-08-30
section says until the implementation lane lands §4-§8. The items the
panel left for the manager are listed in §9 under "escalated".

Sections: §1 the gate · §2 the after samples as provenance · §3 trial
agreement (the census, the rule as a GROUP rule, its constants, what it
cannot see, the block, the status, the arithmetic, the per-group
timeline) · §4 the validator and schema changes · §5 the harness
changes and the status decision table · §6 the reporter changes · §7
migration · §8 the checks · §9 open questions and escalations · §H
history (the proposal as ruled on; §H.2 the panel).

Vocabulary used throughout: a ROW is one (pattern, regime, form,
subject) cell of a record — its N trials are N match rows in the file
(a row's `form` is `plain` when the rows omit it); a GROUP is one
(pattern, regime, form) — the set of rows one trial sweeps in one
pass; "ns/iter" is `timing.elapsed_ns / timing.iterations`, the
reporter's own per-call comparable (`pcrecbench/reduce.py`
`ns_per_call`); a PASS is one trial's sweep over every subject of one
group (`harness.py`: trials are interleaved by group, so trial t of
every subject in a group is one contiguous stretch of wall time —
MEASURED per group over the store's records: **0.07-20.2 s**, bounded
0.07-20.15 s, email@0.1 4.52-19.92 s, email@0.2 2.63-20.21 s, loglines
0.83-12.76 s; the ceiling is `TRIAL_BUDGET_SECONDS = 20`,
`harness.py`). The proposal's "1-2 s" was the six bounded cells' typical
pass, not the range; every duration argument below uses the measured
range.

---

## 1. THE GATE (BD7, ratified) — the pre-flight decides `inconclusive-load`

**The pre-flight**, run by `quiet.check()` + `quiet.gate()` BEFORE the
harness pins to the target core, refuses (exit 3, the message naming
every failing clause) unless ALL of:

| clause | instrument | limit | today |
|---|---|---|---|
| (a) `load.before.load1 ≤ LOAD1_LIMIT` | `/proc/loadavg`, one read | 2.0 (quiet_baseline.md) | unchanged |
| (b) every NON-TARGET core's 5-s average busy ≤ `MAX_BUSY_PCT_LIMIT`, the target's SMT sibling judged like any other core | `mpstat -P ALL 1 5`, the `Average:` block (BD7) | 10.0 % | unchanged |
| (c) **NEW — Frank's item 1, second clause — applies iff `pinning.cpu` is an integer (the driver really will be pinned there); INERT when nothing is pinned:** the TARGET core's own 5-s average busy ≤ the same limit | the same capture; the target's row, which today is EXCLUDED from the judgement | 10.0 % | new |
| (c′) **NEW (panel C F2, ruling R-2) — applies iff `pinning.cpu` is an integer:** the target's row EXISTS in the capture. A capture without it (`--pin` to an offline core, a restricted cpuset, a row the parser skipped) is a refusal in its own right — reason `"occupancy: the target core cpuN does not appear in the mpstat capture; the clause that judges it cannot run"` — so a missing row is refused BEFORE the run, never discovered by X13 at `store.write` after a 20-minute cell | the same capture | — | new |
| (d) the occupancy sample is not `unavailable` | — | — | unchanged (the v1.1 ruling) |

**One source for "the target core" (panel C F1, ruling R-2).** The
harness computes `pinning` (`quiet.pinning(pin_cpu)`) BEFORE
`quiet.check()`, and passes `pinning["cpu"]` as `exclude_cpu` — never
the reverse. On a box where `taskset` is missing or `sched_getaffinity`
fails, `pinning.cpu` is `null`, `exclude_cpu` is `None`, clauses (c)
and (c′) are inert and the field below is ABSENT. A record's `pinning`
block and its occupancy judgement are thereby provably about the same
core.

`--force-unquiet` turns the refusal into a record with `status =
inconclusive-load` and the reasons in `status_detail`, exactly as
today; on a QUIET box `--force-unquiet` changes nothing (the reasons
list is empty, the status is derived as if the flag were absent — the
flag is not a status). Nothing else changes about `inconclusive-load`:
it keeps its name, its enum position, and its meaning "the box was not
known to be quiet when this was measured".

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

**Fields. One new OPTIONAL field on `occupancy_sample` — TWO field-table
rows, one per sample, because `check_fields.py` expands the `$ref` once
per parent (panel B B1) — nothing else in the sample blocks changes:**

| field | type | req | rule | why |
|---|---|---|---|---|
| `environment.occupancy.before.target_busy_pct` | number 0-100 / null | o — TRI-STATE (ruling R-2): ABSENT when `pinning.cpu` is not an integer; `null` when the target's row was not in the capture; a number otherwise. It is `null` (never a number) whenever the sample is `unavailable` — the schema enforces THAT direction only (§4 S2's `then` branch); a `null` beside `pass` means the capture had no row for the target core, which the pre-flight refuses (clause (c′)) and X13 clause 3 refuses `measured` for | the target core's judged busy % over the same capture `max_busy_pct` came from. NOT part of `verdict` — X26 is untouched: `verdict` is still `pass` iff `max_busy_pct ≤ limit_busy_pct`, the non-target judgement. X13 (§4) is what reads it | the number the new clause judged, beside the verdict it does not enter. `raw` already prints the target's row (BD7's "target cpuN excluded from the judgement" line); this makes it a field so X13 can be a rule and not a regex over `raw` |
| `environment.occupancy.after.target_busy_pct` | number 0-100 / null | o — the same tri-state; the harness writes it whenever it writes `before`'s (the same code path, the same capture shape) | the same number after the run, DIAGNOSTIC only: it reads our own driver's decay. Only the `before` value on a `measured` record is ENFORCED (X13 clause 3); the presence of the `after` value is a harness convention, not a rule (panel B B12: a rule for a diagnostic field's presence would be a rule with no consequence; stated here so nobody reads "written on both" as enforced) | the number the NEXT cell's pre-flight will see 15 s later (panel C F4): the first v1.4 window reads the post-cell decay off this field (§9 Q1) |

The alternatives were weighed and rejected: (i) folding the target into
`before.max_busy_pct` changes the MEANING of an existing field for one
sample and not the other (a v1.3 reader would silently read a different
quantity); (ii) a third sample block `target_before` duplicates the
capture's timestamp and raw text for one number. A field beside the
verdict, with the verdict's rule unchanged, is the smallest true change
— and it keeps X26 holding for every sample of every version (the
brief's condition). The consequence the panel should see: a v1.4 record
can carry `before.verdict = pass` and `status = inconclusive-load`
because the target core was busy (or absent from the capture);
`status_detail` says so by name (§5). That is the same shape as today's
`load.verdict = quiet` beside a failed occupancy — two instruments, one
status.

**The limit is the same 10 %.** The target core before the run is an
idle core like any other; the noise floor (2-7 %, quiet_baseline.md)
applies to it as to the others. A separate constant would be a number
nobody measured. **The retry budget is unchanged pending the first
window (panel C F4, ruling R-11):** the previous cell's driver was
pinned to the target core, so its post-exit decay lands exactly where
clause (c) now looks; a 1-2 s residue at 100 % inside a 5-s average is
20-40 %, so clause (c) MAY cost a retry per cell. The window script's
12 × 30 s budget stays; the implementation lane prints the target's
number on every pre-flight of the first v1.4 window and reads the
distribution from the records' `after.target_busy_pct` (§9 Q1). If the
residue exceeds 10 %, the fix is a longer `sleep` after the cell, not a
higher bar (BD7's own argument).

## 2. THE AFTER SAMPLES AS PROVENANCE

**X13, revised (v1.4).** `status = measured` requires:

1. `load.before.load1 ≤ load.limit` (the pre-flight's own load clause —
   note: NOT `load.verdict = quiet`; the verdict stays X20's "either
   sample" and becomes provenance, see below);
2. `occupancy.before.verdict = pass` (so not `fail`, not `unavailable`
   — the v1.1 ruling stands: an unmeasured pre-flight is not `measured`);
3. when `pinning.cpu` is an integer: `occupancy.before.target_busy_pct`
   is PRESENT, a NUMBER (so not `null`: a target row missing from the
   capture is the same unknown as `unavailable`), and `≤
   occupancy.limit_busy_pct`; when `pinning.cpu` is not an integer the
   clause is satisfied (the field is absent by §1);
4. `trial_agreement.verdict = agree` on a `pinned` record (`tier`
   absent = `pinned`); `trial_agreement.verdict ≠ disagree` on a
   `scratch` record (so `n/a-trials` — §3.4 — is not `measured` on the
   ranked tier and is the pre-flight's status on the scratch tier). At
   v1.4 the block is ALWAYS present (X33, §4), so this clause never
   reads an absent block;
5. X14's compile-row clause, unchanged.

The AFTER samples — `load.after` and `occupancy.after` — are recorded
exactly as today, with X19 (the parse agrees with `loadavg_raw`) and X26
(the verdict agrees with the number) still enforced on them, and they
NEVER disqualify a v1.4 record. They are provenance: the number a
reader needs when a record's trials look odd, kept with its verdict so
the reader does not have to re-derive it, and kept with the per-second
peaks in `raw` (I-19: "keep the per-second peaks in raw as you do") so
the transient the average absorbed is still visible.

**`load.verdict` under v1.4 (ruling R-13, confirmed).** X20 is unchanged
— `loaded` iff EITHER sample's `load1` exceeds `limit` — so a v1.4
record whose box got busy after the run carries `load.verdict = loaded`
beside `status = measured`. That is deliberate, and it is why X13 reads
`load.before` directly instead of the verdict: the verdict answers "was
the box loaded at either end", which remains a true and useful
filterable fact; the status answers "was this number measured under the
protocol", which v1.4 defines as the pre-flight plus trial agreement.
The alternative — redefining X20 to the before sample only — changes
the meaning of a v1.3 field, which is a MAJOR bump by §4's rule. The
reporter shows the loaded-beside-measured case under
`--include-provenance` (§6 R5) and, whenever an after sample FAILED, on
the header's record line unconditionally (§6 R5′).

**Where the sentences go (rulings R-4 and R-5; panel C F5/F6, panel B
B6).** Today's split is KEPT: `status_detail` is written ONLY when
`status ≠ measured`; `setup.note` is the operator's `--note` prefix plus
the run's other sentences (calibration, adapter notes, did-not-compile,
the scratch-tier sentence). What changes is the ORDER and the home of
two new sentence classes:

- the STATUS-DECIDING sentence(s) — the gate's reasons, or the §3.4
  trial-agreement line — are always FIRST in `status_detail`; the
  harness passes them to `record.join_notes` through a new `first=`
  argument, so `join_notes`' drop-from-the-END elision (`record.py`,
  the 8192-byte `free_text` cap that bench/bounded's 72 calibration
  sentences already exceed) can never remove the sentence that
  explains the status;
- the AFTER-SAMPLE PROVENANCE sentence(s) — one per instrument, in this
  exact shape, a note and never a status —

      after-sample (provenance, not a verdict): occupancy after the run 20.20% busy on the busiest non-target core (limit 10.00%); the trials' agreement decided the status (v1.4 X13)
      after-sample (provenance, not a verdict): load1 after the run 11.40 exceeds the limit 2.00; the trials' agreement decided the status (v1.4 X13)

  go SECOND: into `status_detail` on a non-`measured` record (after the
  status sentence), into `note` on a `measured` record (after the
  operator's prefix, before the calibration sentences);
- everything else keeps its place, last. The elision marker's text
  names the class it dropped ("calibration/adapter note(s)"), because
  under this ordering that is the only class it can drop.

Today's "occupancy differed across the run" sentence (`harness.py`,
written when the two samples' verdicts differed) is RETIRED: the
provenance sentence above carries the after number and the verdict,
which is the same fact with its evidence. The reporter renders the
provenance sentence from wherever it sits (§6 R5).

## 3. TRIAL AGREEMENT — the rule, its constants measured, the block, the status

### 3.1 The census (what the store says)

`docs/dev/measurements/probe_trial_agreement.py`, run read-only over
every record in the canonical store — **68 records** (schema 1.1 × 11,
1.2 × 3, 1.3 × 54; 59 `measured` + 9 `inconclusive-load`; five pcrec pins
and libpcre2 10.46; every one measured on `budu-ryzen1600` with core 11
pinned) — archived verbatim TWICE: the ROW-level census
(`2026-08-30-trial-agreement-census.txt`, the no-argument run: 62,923
judged rows, every one with exactly 5 trials) and the GROUP-level
census (`2026-08-30-trial-agreement-census-groups.txt`, `--groups`,
the §3.5 arithmetic: 63,028 row keys, 62,928 judged — the 62,923 plus
five rows R-19 counts, below — 100 unjudged, 1,731 groups). Per row:
the per-trial ns/iter, the median; a trial is a SLOW outlier at k if it
is strictly above k × median, a FAST outlier if the row's minimum is
below median / k. The row-level table:

| k | rows with ≥ 1 slow (per-record median / max) | rows with ≥ 2 slow, all records | rows with a fast outlier, all records | rows DISAGREEING (≥ 2 slow OR fast), all records | records with any disagreeing row | worst record's disagreeing fraction |
|---|---|---|---|---|---|---|
| 1.25 | 0.81 % / 13.64 % | 21 (0.033 %) in 10 records | 37 | 58 (0.092 %) | 20 of 68 (6 above 0.5 %, 1 above 1 %) | **1.996 %** (10 of 501; the one `loaded` record, below) — the worst MEASURED record 0.93 % (3 of 321) |
| **1.5** | 0.17 % / 11.58 % | **0** | **1** | **1 (0.0016 %)** | 1 of 68 | **0.204 %** (1 of 490) |
| 2.0 | 0.00 % / 5.79 % | 0 | 0 | 0 | 0 | 0 |

The per-row `max/median` distribution (panel A, `an1.py`): p50 1.0101,
p90 1.0688, p99 1.3376, p99.9 2.0760, max 6.13; `min/median` p50
0.9955, p10 0.9779, p1 0.9126, p0.1 0.8243, min 0.6638. The fast tail
is far thinner than the slow tail, which is why the fast clause fires
once and the slow clause never — the two clauses are NOT calibrated to
comparable quantiles; 1.5 sits at the 99.385th percentile of
`max/median` (0.615 % of rows exceed it). Verified clean for the
record: `timing.iterations` is constant across the trials of every row
(0 exceptions), so per-trial ns/iter is a fair comparable; no row has
mixed outcomes across trials.

Three facts the rule is built on, as the panel corrected them:

1. **Single slow trials are common, are absorbed, and are SYSTEMATIC
   and PHASE-DEPENDENT, not random box noise (panel A F7).** At k = 1.5
   a row with ONE slow trial occurs at a per-record median of 0.17 %
   and up to 11.6 % of rows; the median of five never moves for it.
   Their slowest trial's index over all 387 such rows: t1 36, t2 155,
   t3 41, t4 94, t5 61 — χ² against uniform = 124.1 on 4 df (expected
   77.4 each), p < 1e-24, so this is not warm-up (trial 1 is the least
   frequent) and it is not uniform noise either. The excess is
   concentrated: **158 of the 387 events come from one record,
   `loglines@0.1 × pcrec_35e1ab1_vm-caps` (2026-08-28), t2:110 t4:48 —
   11.6 % of its 1,364 rows perturbed by > 1.5×, with `slow ≥ 2` on
   none of them because the t2 hits and the t4 hits fall on DISJOINT
   groups.** That record is stamped `measured` and reads `agree`; had
   the same on/off competitor been phased half a pass differently, the
   t2 and t4 hits would have landed on the same groups and it would
   read `disagree`. Its phase reading, recorded as a note (ruling
   R-20): an intermittent competitor with a period near two passes of
   its groups, visible to the rule only by phase. The scale k should be
   read against (panel A F7): the set-grain medians of `loglines@0.1 ×
   libpcre2` reproduce across its 08-28 / 08-29 / 08-30 runs to
   ×0.999-1.006 (interp) and ×0.990-1.019 (jit) — the ranked number's
   run-to-run reproducibility on this box is 0.5-2 %, while the rule
   polices per-row agreement at 50 %. The median is doing essentially
   all the work; the rule is a coarse net over an already-robust
   reduction — an argument for adopting it cheaply, and against
   describing it as the instrument that establishes measurement
   validity.
2. **A second slow trial on the same row is absent from the store at
   k = 1.5.** Zero rows in 62,923. At k = 1.25 it appears (21 rows in 10
   records), which is the noise floor being reached, not disturbance:
   the p90 per-row spread of a clean cell is 6-19 % (the gate-shape
   probe), so 1.25× is inside what two ordinary trials can differ by.
3. **Fast outliers exist at 1.25× and vanish at 1.5× — except one, and
   that one is REAL (ruling R-14 as amended by panel A F8).** The
   proposal's model — "a burst can only add time" — is not exact at the
   25 % level: 37 rows have one trial ≥ 20 % FASTER than the median
   (e.g. `factored / short-subject-search / s-013`: 604.9 605.7 636.1
   604.3 **430.6**), a boost or cache state the model does not name. At
   1.5× exactly one remains, `email-specimen@0.2 × pcrec_35e1ab1_vm-caps`,
   `floor / short-subject-search / s-081`: trials of 18,308,341 /
   12,254,934 / 18,710,152 / 12,153,193 / 18,348,981 ns over 1,319,262
   iterations each = 13.88 / 9.29 / 14.18 / 9.21 / 13.91 ns/iter. Each
   trial is 12-19 MILLISECONDS of wall time over 1.32 M iterations, so
   clock resolution is irrelevant at that amortisation: this is a clean,
   repeatable two-cluster 51 % difference between whole trials — and the
   same pattern and subject in the `match-compliance` artifact of the
   same record is flat at 7.97-7.99 ns across all five. The split is a
   property of one artifact's execution on that pass (a code-path,
   alignment or frequency state), i.e. exactly the "bimodal cell" §3.4
   names. It is the fast clause's one demonstrated positive at the row
   level; the earlier draft's "a timer-floor artifact" was wrong (rows
   with median < 20 ns are 17.2 % of the store and their fast tail is
   THINNER than the store's, `min/median` p1 0.950 vs 0.913), and there
   is no exemption (§9 records the residue: one row is real but one row
   is not a disturbed group, which is what the GROUP rule of §3.2 says).

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
argued from the mechanism (§3.2), not shown on a record. §8 adds an
arithmetic control; §9 Q3 makes the measured control a plan row that
FOLLOWS the implementation.

### 3.2 The rule: `v1.4-group` — k = 1.5, a GROUP disagrees at d ≥ 2 and 3·d ≥ n, N ≥ 5 and odd

**The record-level fraction F of the earlier draft is DROPPED (ruling
R-16, from panel A F1).** Disagreements are not row-independent: a burst
hits one contiguous PASS of one group, so it disagrees all of that
group's rows or none; the effective quantum of `rows_disagreeing` is
the GROUP SIZE, and a fraction of the record reduces to "does some
group's size exceed F × rows_judged" — which on seven real
`email-specimen@0.2` records (500-501 judged rows, 5-row throughput
groups) had a margin of 0.00-0.01 rows, and for which no single F is
clean across the three sets (email needs F > 5/501 to keep ignoring
its throughput groups; bounded needs F < 30/1536 to catch a 30-row
match group; F = 2 % silences a fully disturbed bounded group). The
rule's unit is a pass of a group, so its threshold is a SHARE OF THE
GROUP, never of the record, in integer arithmetic.

**The rule.** Per judged row (§3.5 says exactly which rows are judged),
with `m` the median of the row's per-trial ns/iter:

- `slow` = the number of trials with ns/iter **> k · m**;
- `fast` = 1 if **min(ns/iter) < m / k**, else 0;
- the row **DISAGREES** iff `slow ≥ 2` OR `fast = 1` (or, ruling R-19,
  it carries a `timed-out` trial — §3.5, and the escalation in §9 E-1).

Per GROUP (pattern, regime, form), with `n` its judged rows and `d`
its disagreeing rows: the group **DISAGREES** iff **`d ≥ D_MIN` AND
`c · d ≥ n`** — integer constants, integer comparison. Per record: the
verdict is `disagree` iff **≥ 1 group disagrees**, `agree` otherwise —
PROVIDED the record's trial count N is **≥ 5 and odd** (ruling R-12 as
amended); otherwise the verdict is `n/a-trials` and nothing is judged
(§3.4). **k = 1.5, D_MIN = 2, c = 3, N = 5.**

Read as the proposal wrote it: one slow trial of five is a tolerated
perturbation (the median is untouched; the store shows it is the box's
ordinary behaviour); two are a disagreement (two passes of the same
group were perturbed, or the cell is bimodal); a fast outlier is a
disagreement of the other kind — if one trial is faster than m / k
then the median is at least k× above a value the machine demonstrably
reached, i.e. the number the reporter would rank is itself perturbed.
The group test then says: a disturbance is something that reached a
THIRD of a group's rows on two passes, and never fewer than two rows.

**Why k = 1.5 (ruling R-20; the honest reading from panel A F6).** The
row-level k sweep over all 62,923 rows, with the record-level fraction
the earlier draft judged (its last two columns are that draft's F = 1 %,
kept so the margin is visible):

| k | rows ≥ 1 slow | rows ≥ 2 slow | fast rows | disagreeing rows | worst record's fraction | records over the old F = 1 % |
|---|---|---|---|---|---|---|
| 1.30 | 724 | 14 | 21 | 35 | **1.1976 %** | **1** |
| 1.35 | 595 | 10 | 7 | 17 | 0.7984 % | 0 |
| 1.40 | 514 | 6 | 2 | 8 | 0.5988 % | 0 |
| 1.45 | 436 | 3 | 1 | 4 | 0.2041 % | 0 |
| **1.50** | 387 | **0** | **1** | **1** | **0.2041 %** | 0 |
| 1.55 | 343 | 0 | 0 | 0 | 0.0000 % | 0 |
| 1.60-2.00 | 300-128 | 0 | 0 | 0 | 0.0000 % | 0 |

And the same sweep at the GROUP level under the chosen (D_MIN = 2,
c = 3), from the group census (its "per k" block; the five `timed-out`
rows R-19 counts are in every line, d = 1 each, and never flag):

| k | rows disagreeing | largest d in any group (where) | groups disagreeing (2,3) |
|---|---|---|---|
| 1.25 | 63 | 10 (`loglines@0.1 × libpcre2 interp` 08-28, `kv-quoted / short-subject-search`, n = 112) | 2 (1 record) |
| 1.30 | 40 | 7 (the same group) | 1 |
| 1.35 | 22 | 4 (the same group) | 1 |
| 1.40 | 13 | 3 (**the `loaded` control record**, `floor / large-subject-throughput`, n = 5) | **1** |
| 1.45 | 9 | 1 | 0 |
| **1.50** | **6** | **1** | **0** |
| 1.55-2.00 | 5 | 1 (the five timed-out rows only) | 0 |

The store bounds k from BELOW and not from above: under the group rule
the contaminated-but-correct record of §3.1 is flagged at k ≤ 1.40 (3 of
its 5 floor-throughput rows carry two trials 1.4× over their median —
numbers its clean re-run shows were right to within 1.8 %) and clears
at k ≥ 1.45; **k = 1.5 is 0.05-0.10 from a false positive, not 4.9×
away**, and the store is UNINFORMATIVE above 1.55 (every k from 1.55 to
2.0 gives the same five timed-out rows and nothing else). The case
for 1.5 over a higher k therefore rests on the four characterised burst
magnitudes of the gate-shape probe — 2.25× (`cls-upto-32768 / match`,
24.5 vs 10.9), 1.76× (`dotted4 / match`, 38.8 vs 22.1), 1.70×
(`nest2-64 / search_short`, 346 vs 204) and the ~2× typical — a sample
of four, one of which is 13 % from the threshold; a two-pass
disturbance of the 1.7× kind is invisible at k = 2.0 and counted at
k = 1.5. So: **1.5 is the lowest value in the store-clean region, chosen
to keep the observed burst magnitudes inside detection; it is a
measurement of quietness and an anecdote about sensitivity**, and k
stays 1.5 (R-20) with that margin stated rather than a larger one
claimed.

**Why (D_MIN, c) = (2, 3) — read from the group census under R-16's two
constraints.** The census evaluates every candidate in
{2, 3} × {2, 3, 4} (`d ≥ D_MIN and c · d ≥ n`) against (i) ZERO
disagreeing groups on the store's 68 records at k = 1.5, and (ii) the
LEAST SENSITIVE candidate that still flags BOTH disturbance shapes at
every named group size (n = 4, 5, 30, 85, 112): a WHOLE-group two-pass
disturbance (every row two slow trials, d = n) and a HALF-pass overlap
(a window covering 1.5 passes, so the rows hit on both passes are half
the group, d = ⌊n/2⌋ — the pessimistic half). Constraint (i) pushes the
threshold up, (ii) pulls it down; "least sensitive" is the reading under
which the pair is determined (the more sensitive (2, 4) also satisfies
both and is the runner-up, §9). Group sizes actually present in the
store (per sub-bench, judged rows per group; this corrects the earlier
draft's "≥ 23 subjects" and panel A F10's list): bounded 4 and 30;
email@0.1 2, 3, 77, 80, 85; email@0.2 4, 5, 77, 80, 85; loglines 12 and
112. The store's largest d in any group at k = 1.5 is **1** (the fast
row of §3.1 fact 3, 1 of 77; and the five timed-out rows, 1 of 3 or
1 of 5) — so EVERY candidate satisfies (i). Constraint (ii):

| candidate | flags WHOLE at every size | flags HALF at every named size | fails at |
|---|---|---|---|
| (2, 2) | yes | **NO** | n = 5, 77, 85 (odd n: ⌊n/2⌋ · 2 < n) |
| **(2, 3)** | **yes** | **yes** | — |
| (2, 4) | yes | yes | — (more sensitive: T = ⌈n/4⌉) |
| (3, 2) / (3, 3) / (3, 4) | yes (n ≥ 3) | **NO** | n = 4, 5 (⌊n/2⌋ = 2 < D_MIN) |

The margins under (2, 3), in ROWS per group size — T is the smallest d
that disagrees, `max(2, ⌈n/3⌉)`; "store" is T minus the largest d the
store shows at that size; "half" is ⌊n/2⌋ − T, the rows to spare before
the half shape stops flagging; "whole" is n − T:

| n | T | margin over the store | margin of the HALF shape | margin of the WHOLE shape |
|---|---|---|---|---|
| 4 | 2 | 2 | 0 | 2 |
| 5 | 2 | **1** (a d = 1 timed-out row exists at n = 5) | 0 | 3 |
| 30 | 10 | 10 | 5 | 20 |
| 85 | 29 | 29 | 13 | 56 |
| 112 | 38 | 38 | 18 | 74 |
| (2, 3, 12, 77, 80 — also present) | 2, 2, 4, 26, 27 | 2, 1, 4, 25, 27 | −1, −1, 2, 12, 13 | 0, 1, 8, 51, 53 |

So the whole-group shape flags at every size in the store; the half
shape flags at every named size, with no rows to spare at n = 4 and 5
(the throughput groups: a 1.5-pass window there must reach 2 of the 4
or 5 rows on both passes) and 5-18 rows to spare on the match/search
groups; the 2- and 3-row groups of email@0.1 cannot show the half shape
at all (⌊n/2⌋ = 1 < D_MIN), which is the price of "never one row". The
store's single fast row (1 of 77) and its five timed-out rows (1 of 3,
1 of 5) remain NON-disagreements, as R-16 requires: one row is not a
disturbed group.

**What the rule cannot see, stated in full (ruling R-17; panel A F2,
F3).** Three blind bands, in decreasing order of how much they can move
the ranked number:

1. **A slowdown of factor s ≤ k on ANY number of passes is invisible**,
   and at j ≥ 3 of the 5 passes such a slowdown MOVES THE ROW MEDIAN BY
   s. Algebra: at j = 3 or 4 the median IS the slow value, so no trial
   exceeds k·m; the fast clause needs min < m/k, i.e. s > k strictly.
   The rule's detection threshold and the error it silently admits are
   the SAME number — a competitor that makes the ranked median 49 %
   wrong passes as `agree`. For a competitor multiplying j of the 5
   passes by s (`an5.py`, k = 1.5):

   | s | j=1 | j=2 | j=3 | j=4 | j=5 | median moved by |
   |---|---|---|---|---|---|---|
   | 1.20 | — | — | — | — | — | ×1.20 at j ≥ 3 |
   | 1.40 | — | — | — | — | — | ×1.40 at j ≥ 3 |
   | **1.49** | — | — | **—** | **—** | — | **×1.49** |
   | 1.60 | — | FLAG | FLAG | FLAG | — | ×1.60 |
   | 2.25 | — | FLAG | FLAG | FLAG | — | ×2.25 |

   This band is populated on this box: of the 724 rows whose worst
   trial is ≥ 1.3× its median, 337 (46 %) are perturbed BELOW 1.5×
   (magnitude census of `max/median`: 1.1-1.2: 2622; 1.2-1.3: 731;
   1.3-1.4: 210; 1.4-1.5: 127; 1.5-1.7: 128; 1.7-2.0: 131; ≥ 2.0: 128).
   Those same perturbations, had they lasted three passes instead of
   one, would have moved the number 30-50 % and been stamped `measured`.
2. **A competitor spanning ALL FIVE passes of a group is invisible by
   construction** (j = 5: uniform, the trials agree with each other and
   with the wrong number) — a steady competitor on any core (boost
   clock), one on the SMT sibling (execution resources), one on the
   target core itself, a thermal state. The pre-flight (§1 (b), (c)) and
   BD6/BD7's box discipline are the defence; the after sample is
   provenance; `cpu_mhz` in the environment is the reader's clue.
3. **A burst shorter than one pass is essentially never caught** — fine
   and intended (the median absorbs it), but it means the rule cannot
   be described as catching "the perturbations the after sample was
   catching" (§H characterises those as ONE-pass events).

**The rule's POWER, honestly (panel A F3, `an4.py`).** From each cell's
measurement timeline reconstructed in `seq` order from
`timing.elapsed_ns` (calibration and overhead excluded — approximate),
every (group, trial) pass interval, and a competitor window of duration
T swept over 400 start positions, assuming s > 1.5 so every overlapped
pass is detectable — P(the record is flagged), computed under the
earlier draft's record fraction, which the group rule matches within a
few points on these three cells (its unit is the same group quantum):

| competitor duration | bounded (1,472 rows) | email@0.2 (501) | loglines (1,364) |
|---|---|---|---|
| 2 s | 2 % | 0 % | 0 % |
| 5 s | 27 % | 7 % | 0 % |
| 10 s | 60 % | 25 % | 27 % |
| 30 s | 82 % | 57 % | 92 % |
| 60 s | 84 % | 80 % | 76 % |
| 300 s | 74 % | 58 % | 56 % |
| 600 s | 68 % | 58 % | 54 % |

Two facts to carry: a burst shorter than one pass (0.07-20 s) is
essentially never caught; and power does NOT increase with duration —
a competitor running for ten minutes is missed about one time in three,
because it covers all five passes of every group it fully spans (band
2) and only the two boundary groups are detectable. That is the case
v1.3's after sample used to catch, and the one v1.4 hands to the rule
plus the per-group timeline of §3.6 (provenance).

**The rule judges rows the reporter never ranks (panel C F10).**
`reduce.reduce_set_cell` EXCLUDES a whole set cell if ANY subject is
expectation-failing, while §3.5 judges every row with ≥ 2 timed trials
regardless. A row judged here and ranked nowhere can still flag its
group — correctly: the rule is about the box, not the ranking. On
bench/bounded the two populations differ materially.

### 3.3 The block: `trial_agreement` in the SETUP layer

| field | type | req | rule | why |
|---|---|---|---|---|
| `trial_agreement` | object | **REQUIRED at v1.4 on EVERY record** (X33 — pinned or scratch, any trial count, even a record with no match rows: the block then says `n/a-trials` with `trials: 0`); FORBIDDEN on a record stamped `< 1.4` (X33's other direction, panel B B4) | the rule's inputs, outputs and verdict, every number recomputable from the rows (X32) | the status depends on it, so the record must carry what decided the status — the same argument as `load.limit` beside `load.verdict` (X20) and `limit_busy_pct` beside the occupancy verdicts (X26) |
| `trial_agreement.rule` | const `"v1.4-group"` | R | names THIS definition (§3.5); a changed definition is a new const and a schema bump | a verdict without the rule that produced it is re-judgeable by nobody |
| `trial_agreement.k` | number > 1 | R | the outlier ratio the run used (1.5) | data, not a schema constant (quiet_baseline.md's own argument for `load.limit`) |
| `trial_agreement.d_min` | integer ≥ 1 | R | the least disagreeing rows a group needs (2) | as above |
| `trial_agreement.share_c` | integer ≥ 1 | R | the share denominator: a group disagrees at `share_c · d ≥ n` (3) | as above |
| `trial_agreement.trials` | integer ≥ 0 | R | the run's trial count: the largest `trial` among the record's match rows, 0 when there are none (X32 recomputes it) | the precondition the verdict depends on (ruling R-12): the same `k` denotes four different rules at N = 2, 3, 4, 5 (panel A F4), so N is in the block |
| `trial_agreement.groups_judged` | integer ≥ 0 | R | the count of groups with ≥ 1 judged row (X32 recomputes it); 0 under `n/a-trials` | the denominator of the verdict |
| `trial_agreement.groups_disagreeing` | integer ≥ 0 | R | the count of judged groups that DISAGREE per §3.2 (X32 recomputes it); 0 under `n/a-trials` | the numerator of the verdict |
| `trial_agreement.rows_judged` | integer ≥ 0 | R | the count of judged rows (§3.5; X32 recomputes it); 0 under `n/a-trials` | the evidence behind the group counts |
| `trial_agreement.rows_disagreeing` | integer ≥ 0 | R | the count of judged rows that DISAGREE (X32 recomputes it); 0 under `n/a-trials` | as above |
| `trial_agreement.rows_unjudged` | integer ≥ 0 | R | the count of row keys NOT judged — fewer than 2 timed trials and no `timed-out` trial (`iterations ≤ 1` rows, expectation-failing rows); under `n/a-trials` EVERY row key; `rows_judged + rows_unjudged` = the record's match-row keys (X32 recomputes it) | a record that is 30 % unjudgeable cannot present "0 of 42 groups disagree" as though the cell had been examined (panel A F5); the reporter renders it |
| `trial_agreement.worst_group` | object / null | R | `null` iff `groups_judged = 0`; else `{pattern_id, regime, form, d, n}` of the judged group with the LARGEST `d`, ties → the SMALLEST `n`, ties → the LOWEST `seq` among the group's rows; `form` always spelled explicitly (`plain` when the rows omit it); its ids must exist in the record (X7's argument) and `d`/`n` recompute (X32) | the reader's first look, without re-reducing 1,500 rows — the group nearest the threshold, with its two integers. The earlier draft's `worst_row` with its per-trial `ns_per_iter` array is DROPPED (ruling R-16; panel B B8/B9: a stored per-call time checked by nobody is the shape X20 and X26 were written to end, and the ids are the irreducible part) |
| `trial_agreement.verdict` | enum `agree` / `disagree` / `n/a-trials` | R | X31: `n/a-trials` iff `trials < 5` or `trials` is even; else `disagree` iff `groups_disagreeing ≥ 1`; else `agree` (so `groups_judged = 0` with 5 trials ⇒ `agree`, "0 of 0 groups disagree", which the reporter renders DISTINCTLY, §6 R4); FILTERABLE | the verdict beside its numbers, required to agree with them |

Placement: the SETUP layer, beside `status`, not per match row. A
per-row flag would be 2-6 thousand copies of a boolean the rows already
imply (§4's own size argument against per-row facts), and the status is
a per-record fact. The block is the ONE place this schema stores
numbers DERIVED from rows — COUNTS, never a time (record_schema.md
§10.3 says statistics stay reader-side, and its "no `n` field" bullet
says a count the rows determine is a second source of one truth); the
justification is that these are a VERDICT with its evidence, held to
the X20/X26 standard — recomputable and required to agree (X32) — and
not a statistic anyone ranks on. §4 D1 amends BOTH §10.3 bullets with
that one exception (panel B B9), and the exception covers counts under
a recomputation rule and does NOT cover a stored per-call time, which
keeps the "no ns/call" bullet true as written.

### 3.4 The status: `inconclusive-spread`

A new `record_status` value, stamped when the pre-flight PASSED
(otherwise `inconclusive-load` takes precedence — a box known to be
busy explains any spread, and one status must not hide the other's
reason; ruling R-15 confirms, and BOTH facts go in `status_detail`,
the gate's reasons first) and EITHER `trial_agreement.verdict =
disagree` OR (`tier = pinned` and `verdict = n/a-trials`, ruling R-12:
a measurement that did not meet the rule's precondition is not a
measurement). Meaning: "the box was quiet when this started; either
the five trials do not agree on the number to within k on a third of
some group's rows — something ran beside this cell for at least two
passes, or the cell is bimodal for a reason of its own — or the run
did not have the five odd trials the rule needs". `status_detail`
carries the numbers FROM THE BLOCK, in this exact shape, FIRST (§2):

    trial agreement (v1.4-group, k=1.5, d_min=2, share_c=3, trials=5): 1 of 72 groups disagree; 23 of 1536 rows disagree, 0 unjudged; worst group cls-upto-32768 / match-compliance / plain: d=23 of n=30
    trial agreement (v1.4-group): n/a-trials (3 trials; the rule requires >= 5, odd) -- nothing judged, 501 rows unjudged

**Tiers and `n/a-trials` (ruling R-12 as amended, and one explicit
choice).** A PINNED record needs `trials ≥ 5` and odd for the rule to
judge; a pinned record with 1-4 or an even number of trials carries the
block with `verdict: n/a-trials`, all counts 0, `rows_unjudged` = every
row key, `worst_group: null`, and is `inconclusive-spread` (so a
`--trials 1` pinned run is not `measured`, closing the earlier draft's
Q6/Q7). A SCRATCH record (`quick`'s default is 3 trials) carries the
same block with `n/a-trials` and — the choice this spec makes, flagged
in §9 for the manager — keeps the PRE-FLIGHT's status: `measured` when
the box was quiet, because the ruling separates the two tiers ("never
ranked anyway") and because the smoke suite (`--trials 1 --iters 1`,
scratch, `synthetic`) would otherwise write `inconclusive-spread` on
every clean run; the block says `n/a-trials` in the record, `quick`
prints `agreement: n/a (3 trials)`, and the reporter never ranks the
tier. X13 clause 4 is worded per tier for exactly this (§2). A pinned
record with 5 trials and `rows_judged = 0` (every timed row at
`iterations ≤ 1`, or every subject expectation-failing — reachable on
bench/bounded) is `agree` and `measured` with `rows_unjudged` saying
what was not examined; the reporter renders "agree 0/0 — nothing
judged" distinctly (§6 R4) and §9 records it as a residue.

An `inconclusive-spread` record is UNRANKED (reporter R1, §6), exactly
like `inconclusive-load`, and its numbers are printed under the table
FROM THE BLOCK (ruling R-4); the store accepts it; the dedup rule R2
treats it as "not measured" (a later measured re-run supersedes it; it
never supersedes a measured record) and has NO PREFERENCE between the
two inconclusive values (panel C F11: in a group with no measured
record the newest overall stands, whichever it is — the precedence
below is a STAMPING precedence, not a ranking rule). The window script
sees it through exit code 4 (§5 H10, ruling R-6). Precedence, in full:
`harness-failure` > `inconclusive-load` > `inconclusive-spread` >
`measured` — where `harness-failure` is the documentation of an enum
value NO CODE PATH PRODUCES (ruling R-8, panel C F14: every exception
path in contract 4 either writes no record or stamps a per-row outcome;
reaching it would mean writing a record from an exception handler,
which contract-4 step 5 forbids and X14 would reject); v1.4 does not
make it real, and the enum's ORDER is not its precedence (§4 S1).

### 3.5 The rule, as arithmetic — the ONE statement both implementations follow (ruling R-3; R-16; R-19)

`reduce.judge_trial_agreement` (the harness stamps and the reporter
renders from it, §5 H4) and `validate.py`'s X32 (the deliberate second
implementation, §4 V6) both implement THIS, and X32 compares INTEGER
COUNTS and the `worst_group` key only — never floats — so the two must
agree on a verdict, not on a bit pattern. One hand-computed fixture
pins both (§8).

    # inputs: the record's match rows (the dicts as written; store.serialize
    # performs no projection, so the rows the harness judges are the rows
    # X32 re-judges), k, d_min, share_c
    row key      = (pattern_id, regime, form or "plain", subject_id)
    group key    = row key[:3]
    trials       = max(row.trial over all match rows), or 0 with none
    if trials < 5 or trials % 2 == 0:
        verdict = "n/a-trials"; every count = 0; rows_unjudged = len(row keys);
        worst_group = null; STOP
    for each row key, in any order:
        timed  = { trial: elapsed_ns / iterations (float64)
                   for the key's rows with match_outcome == "matched-as-expected"
                   and timing.iterations > 1 }            # a TRIAL is timed iff both
        if any of the key's rows has match_outcome == "timed-out":
            judged, disagreeing = True, True               # R-19 (see 9 E-1)
        elif len(timed) >= 2:                              # a ROW is judged iff >= 2 timed trials
            xs   = [timed[t] for t in sorted(timed)]       # sorted by trial; mixed outcomes: judged on the timed ones
            m    = statistics.median(xs)                   # even count: the mean of the two middle values
            slow = sum(1 for x in xs if x > k * m)         # STRICT; spelled exactly so
            fast = 1 if min(xs) < m / k else 0             # spelled exactly so (not min*k < m)
            judged, disagreeing = True, (slow >= 2 or fast == 1)
        else:
            judged = False; rows_unjudged += 1; continue
        rows_judged += 1; group[n] += 1
        if disagreeing: rows_disagreeing += 1; group[d] += 1
    groups_judged      = the groups with n >= 1
    a group DISAGREES iff d >= d_min and share_c * d >= n   # integers
    groups_disagreeing = count of them
    verdict            = "disagree" if groups_disagreeing >= 1 else "agree"
    worst_group        = the judged group maximising (d, -n, -min_seq)
                         # largest d; then smallest n; then the LOWEST seq
                         # among the group's match rows; null iff groups_judged == 0

Ties in the float comparisons are NOT disagreements (`x == k·m` is not
slow; `min == m/k` is not fast) — and because X32 compares the counts,
a row on the exact boundary yields the same integer in both
implementations as long as both spell the expressions as above.
`worst_group` is recomputable in full (two integers and a key), unlike
the earlier draft's per-trial array.

### 3.6 The per-group occupancy TIMELINE — provenance, never a verdict (ruling R-17; panel A F2 (b))

The only instrument that can see band 1 of §3.2 (s ≤ 1.5 across
several passes) at all is one that looks DURING the run. The pre-flight
samples 5 s before; the after sample is now provenance; between them
nothing looks. The panel's proposal — read `/proc/stat` per core at
every GROUP boundary (microseconds, no new process, no mpstat) and
record the per-group busy % of the target core, its SMT sibling and the
busiest other core — is ACCEPTED AS PROVENANCE ONLY (Frank's item 4):
no rule reads it, no status depends on it, the reporter renders it
under `--include-provenance`.

**The field, designed for `additionalProperties: false`:** one optional
array on `environment.occupancy` (the setup layer — a group is not a
row, and the per-row alternative would repeat one fact on every trial
of every subject):

| field | type | req | rule | why |
|---|---|---|---|---|
| `environment.occupancy.timeline` | array | o (v1.4: written by the harness whenever `/proc/stat` is readable and the run has ≥ 1 group; absent otherwise — a field no mechanism fills is a claim in a schema's clothes, §10.3's own argument, so the SCHEMA half and the HARNESS half land together or not at all) | one item per (pattern, regime, form) group in measurement order; `additionalProperties: false`, every member required | the occupancy of the box WHILE each group was measured, which neither sample sees |
| `environment.occupancy.timeline[].pattern_id` / `.regime` / `.form` | slug / enum / slug | R | the group's key; `form` explicit | the same key as `worst_group` |
| `environment.occupancy.timeline[].elapsed_ms` | integer ≥ 0 | R | the group's wall time, all its passes, from the `/proc/stat` readings' timestamps | the denominator of the busy percentages |
| `environment.occupancy.timeline[].target_busy_pct` | number 0-100 | R | the target core's busy % over `elapsed_ms` — OUR driver, so ~100 % is expected; a value well UNDER that is the signal (the core was shared) | reads our own driver: the deviation is the evidence |
| `environment.occupancy.timeline[].sibling_busy_pct` | number 0-100 / null | R | the target's SMT sibling (`null` when the topology gives none) | the sibling shares execution resources (§H) |
| `environment.occupancy.timeline[].max_other_busy_pct` / `.max_other_cpu` | number 0-100 / integer ≥ 0 | R | the busiest core other than the target and its sibling, and which | a steady competitor elsewhere (boost clock) |
| `environment.occupancy.timeline_tool` | string | o (present iff `timeline` is) | `"/proc/stat"` | BD7's `tool` argument: the instrument's name beside its numbers |

Marked **v1.4**: the schema hunk is clean (one optional array under a
sibling object, no `$ref` reuse, no rule), and the harness half is a
`/proc/stat` read at each group boundary in `run_cell`'s existing
per-group loop. `check_fields` gains the rows above; no X-rule; one
good-example item and one `schema-timeline-item-missing-member`
control. If the implementation lane finds the harness half does not fit
the change, BOTH halves defer to v1.5 together (never the field alone).

---

## 4. THE VALIDATOR AND SCHEMA CHANGES, enumerated

`schema_version` 1.3 → **1.4, a MINOR bump under record_schema.md §4 AS
AMENDED IN THE SAME CHANGE (ruling R-1; panel B B3).** The additive
items — one new enum value (`inconclusive-spread`), new OPTIONAL-in-the-
schema fields (`target_busy_pct` on `occupancy_sample`; the
`trial_agreement` object and the occupancy `timeline` on `setup`), a
relaxed constraint (KB-4's `cost` beside a refusal, ruling R-9), rules
that only fire on a record carrying the new block — are MINOR by the
rule as written. The revision of X13 is NOT: a v1.3 `measured` asserts
both samples quiet and both occupancy samples `pass`; a v1.4 `measured`
asserts the pre-flight plus trial agreement and may carry `load.verdict
= loaded`; §4's own table makes "a changed meaning" MAJOR, and its
one-time exception is spent. The panel's blocker is resolved by the
manager's ruling, whose reasons are these: a MAJOR bump makes the
reporter refuse 1.3 + 1.4 in one query by default — the first v1.4
window's cross-pin reports would need `--allow-mixed-versions` on every
query — and would split the store for ZERO ranking difference (§7:
every record's rank is unchanged). **The clause to insert in
record_schema.md §4, after the MAJOR bullet, drafted here exactly and
applied by the implementation lane (D1):**

> - **A cross-line RULE may be revised at a MINOR bump** (v1.4, X13)
>   provided (i) the revision is KEYED ON `schema_version` in the
>   validator, so a record is judged by the rule of its own version;
>   (ii) older records keep the verdict of their own version — never
>   re-stamped, never re-judged; (iii) the reporter renders the rule's
>   version beside every status it ranks — a `rule:` marker in the
>   ranking rows and the legend, not only in a per-record column
>   (docs/design/gate_shape_v14.md §6 R4′). A revision that fails any
>   of the three is a changed meaning and MAJOR by the bullet above.

And the X17 sub-finding (panel B B3): §4's "A reader on an older minor
MUST accept the file" is contradicted by `validate.py`, which REJECTS a
newer minor under X17 ("written by a newer schema minor … upgrade the
validator"). **The validator's behaviour is the rule** (ruling R-1);
record_schema.md §4's MINOR bullet is amended to: "A reader on a NEWER
minor MUST accept every older minor's file unchanged; a reader on an
older minor REFUSES a newer one by name (X17: upgrade the validator
rather than read it half-blind). MUST treat an enum value it does not
know …" (the rest unchanged).

| # | change | file(s) |
|---|---|---|
| S1 | `$defs.record_status.enum` gains `inconclusive-spread` as its FOURTH value; its description cites this note and says the enum's ORDER is not the §3.4 precedence (panel B B17.1) | `schema/record.schema.json` |
| S2 | `$defs.occupancy_sample.properties` gains `"target_busy_pct": { "type": ["number", "null"], "minimum": 0, "maximum": 100 }` (optional — the tri-state's ABSENT state is "not in `required`"); the existing three-branch `allOf` changes in its `then` ONLY: `"then": { "properties": { "max_busy_pct": { "type": "null" }, "target_busy_pct": { "type": "null" } } }`, the `else` UNCHANGED (`max_busy_pct: number` — a `null` target beside `pass` is the missing-row case, which the pre-flight refuses and X13 clause 3 reads; the schema enforces the one direction, ruling R-2, panel B B2) | `schema/record.schema.json` |
| S3 | `$defs.trial_agreement` (the §3.3 table: `additionalProperties: false`, every member required, `rule` a const, `verdict` its three-value enum, `worst_group` a nested object with its own `required` and `additionalProperties: false`, or `null`) and `$defs.setup.properties.trial_agreement` referencing it; NOT in `setup.required` (the schema is version-blind — 1.3 records validate against the same file; the requirement at 1.4 and the prohibition below it are X33's job) | `schema/record.schema.json` |
| S4 | `x-record-schema-version` → `"1.4"`; the schema's `$comment` history line | `schema/record.schema.json` |
| S5 | **KB-4's schema half (ruling R-9, panel C F16):** `$defs.compile_row.allOf[4]` ("No cost for a compile that did not happen") is REMOVED — `cost` may sit beside any `compile_outcome` (a refused compile may carry the bench's clock around the pcrec exec); `cost` stays REQUIRED when `compile_outcome = compiled` and `cost_class ≠ lazy-jit` (the other `allOf` branch, unchanged). The adapter half (time `emit-c` on every outcome) and the reporter half stay KB-4's own plan row, which must say the schema is already there | `schema/record.schema.json` |
| S6 | the §3.6 `timeline` array and `timeline_tool` on `environment.occupancy` (optional; `additionalProperties: false` throughout) | `schema/record.schema.json` |
| V1 | **X13 revised, VERSIONED:** for `schema_version ≥ 1.4` the §2 clauses 1-5 (clause 3's tri-state; clause 4 per tier); for `< 1.4` the v1.1 text unchanged (both samples pass, `load.verdict = quiet`). The validator already parses the minor (X17's branch) — X13 becomes the first rule that reads it, under the §4 clause above | `schema/validate.py` |
| V2 | **X31** (new): `trial_agreement.verdict` is `n/a-trials` iff `trials < 5` or even; else `disagree` iff `groups_disagreeing ≥ 1`; else `agree` | `schema/validate.py` |
| V3 | **X32** (new): `trials`, `groups_judged`, `groups_disagreeing`, `rows_judged`, `rows_disagreeing`, `rows_unjudged` equal the values RECOMPUTED from the record's match rows under §3.5 with the block's own `k`, `d_min`, `share_c`; `worst_group` (when not null) equals the recomputed one (key, `d`, `n`) and its ids exist among the record's patterns/subjects/regimes; `rows_judged + rows_unjudged` = the record's row keys. X20's argument: without X32, X31 is inert — a harness can stamp `0 of 72` beside rows that say otherwise | `schema/validate.py` |
| V4 | **X33** (new, TWO-DIRECTIONAL, panel B B4): for `schema_version ≥ 1.4` the `trial_agreement` block is REQUIRED on every record; for `< 1.4` it is FORBIDDEN — a block on a record stamped before the version that defined it is a mis-stamped record, not a forward-compatible one (X17 never looks at fields, so this needs its own rule and control) | `schema/validate.py` |
| V5 | the `--expect-rule` help string and the module docstring: `X1..X33`; the X13 message text (`validate.py`'s "only a passing occupancy check on BOTH samples supports `measured`") becomes version-specific | `schema/validate.py` |
| V6 | `validate.py`'s X32 recomputation is a SEPARATE implementation from `pcrecbench/reduce.py`'s (§5 H4): ~30 lines, no import of `pcrecbench`. Why this is right here and importing is right for X3/X5/X6 (panel B B14, reconciling `record.py`'s docstring): X3/X5/X6 derive IDENTIFIERS FROM A CONVENTION — there is no fact of the matter to check, and a second implementation only creates drift that rejects honest records, so `record.py` imports the validator's functions; X32 checks A VERDICT A HARNESS STAMPED BESIDE ROWS IT ALSO WROTE — X20's and X26's situation exactly, where an imported recomputation would make X31 inert. The implementation lane scopes `record.py`'s docstring to derivations-of-convention in the same change. The drift risk this accepts is tolerable only because §3.5 leaves no room for it, and X32 compares integers | `schema/validate.py`, `pcrecbench/record.py` (docstring) |
| E1 | `schema/examples/` — the ACTUAL store is three good records: pcrec 1.1, v8 1.1, local 1.2; there is NO 1.3 good example (ruling R-10, panel B B10). ADD ONE 1.4 good example, built FROM the pcrec example, and bump nothing else (the 1.1 → 1.2 → 1.3 precedent is that no example was ever re-stamped): `email-specimen@0.1__pcrec_…__example-box__<new timestamp>.jsonl` with a new `run.timestamp` → new `record_id` → new filename (X3/X4/X5) and a re-stamped `content_hash`, GROWN TO 5 TRIALS (X9 dense 1..5 per row, X18 `seq` renumbered dense over all rows, X21 calibration on every timed row), `tier: pinned`, `pinning.cpu = 2`, `target_busy_pct` on both samples (a number on `before` ≤ limit), a `trial_agreement` block whose counts X32 recomputes (`verdict: agree`), a FAILED after sample (`occupancy.after.verdict = fail` at 20.20 % with X26 holding, `load.after.load1` 11.40 with `load.verdict = loaded` so X20 holds) so the after-as-provenance and the loaded-beside-measured cases are both exercised by the record that validates, ONE did-not-compile compile row carrying `cost` (S5), and a `timeline` with one item per group (S6); `status = measured`. The 1.4 example must be GENERATED (a script under `schema/examples/`, committed, deterministic), not hand-written: five trials × 12 rows with dense `seq` and per-row calibration is not hand-edit material, and every bad example below is a one-field sabotage of its output | `schema/examples/` + its CLAUDE.md |
| E2 | `schema/examples/bad/`, one per new rule, each the 1.4 good example with exactly ONE thing wrong and the hash re-stamped, and each constructed to fire ONLY its rule (panel B B7): `x13-measured-but-target-core-busy.jsonl` (`before.target_busy_pct` 55, status `measured`); `x13-measured-but-target-busy-null.jsonl` (`before.target_busy_pct: null` beside `verdict: pass`, `pinning.cpu = 2`, status `measured` — the missing-row control, ruling R-2); `x13-measured-but-trials-disagree.jsonl` (rows of one group sabotaged so it disagrees, the block RECOMPUTED to `disagree`, status left `measured` — X31/X32 quiet, X13 alone fires); `x13-measured-but-load-before-high.jsonl` (`load.before.load1` 9.8, `load.verdict` `loaded` so X20 stays quiet, status `measured` — the control that shows v1.4 X13 reads the BEFORE sample); `x13-measured-but-na-trials-pinned.jsonl` (the example truncated to 3 trials, the block recomputed to `n/a-trials`, status `measured`, `tier: pinned`); `x31-verdict-contradicts-groups.jsonl` (rows of one group sabotaged to disagree, `groups_disagreeing: 1` and every count CORRECT, only `verdict: agree` wrong — X32 quiet, X31 alone); `x32-groups-disagreeing-not-recomputable.jsonl` (rows that disagree, block stamped `0` and `verdict: agree` — self-consistent, X31 quiet, X32 alone: the "stamp 0 beside the rows" sabotage); `x32-trials-not-recomputable.jsonl` (`trials: 7` on a 5-trial record); `x32-rows-unjudged-not-recomputable.jsonl`; `x32-worst-group-unknown-pattern.jsonl`; `x33-trial-agreement-missing.jsonl` (1.4, no block); `x33-trial-agreement-on-a-v13-record.jsonl` (the block on a record stamped 1.3 — the other direction); `schema-status-inconclusive-spread-misspelt.jsonl` (`inconclusive_spread` — the token-spelling rule); `schema-target-busy-beside-unavailable.jsonl` (a number beside `unavailable` — S2's `then`); `schema-trial-agreement-unknown-member.jsonl` (`additionalProperties`); `schema-timeline-item-missing-member.jsonl` (S6) | `schema/examples/bad/` + its CLAUDE.md |
| E3 | the EXISTING controls `x13-occupancy-after-fail.jsonl`, `x13-occupancy-unavailable.jsonl` AND `x13-measured-but-loaded.jsonl` are **v1.1**-stamped (as is every file in `bad/` except `x17-future-major-version` at 2.0 — the earlier draft's "v1.3-stamped" was wrong, panel B B15) and STAY: they prove the `< 1.4` branch of X13 still fires; the third is Q8's case exactly (load1 11.40 after, both occupancy samples `pass`), LEGAL at 1.4 and rejected at 1.1. The "same sabotage, two versions, two verdicts" pair is: those three (rejected at 1.1) against the E1 good example (which carries the SAME after-sample failure and the SAME loaded `load.verdict`, accepted at 1.4). No re-stamped copy is needed | `schema/examples/bad/` (unchanged files) |
| C1 | `check_fields.py`: the §8 field tables of record_schema.md gain, in the SETUP table, exactly these paths (the walk expands `$ref`s once per parent and descends `items` only for objects with named properties, so an array of numbers is one row and each `timeline[]` member is one): `environment.occupancy.before.target_busy_pct`, `environment.occupancy.after.target_busy_pct`, `environment.occupancy.timeline`, `environment.occupancy.timeline[].pattern_id`, `…[].regime`, `…[].form`, `…[].elapsed_ms`, `…[].target_busy_pct`, `…[].sibling_busy_pct`, `…[].max_other_busy_pct`, `…[].max_other_cpu`, `environment.occupancy.timeline_tool`, `trial_agreement`, `trial_agreement.rule`, `.k`, `.d_min`, `.share_c`, `.trials`, `.groups_judged`, `.groups_disagreeing`, `.rows_judged`, `.rows_disagreeing`, `.rows_unjudged`, `.worst_group`, `.worst_group.pattern_id`, `.worst_group.regime`, `.worst_group.form`, `.worst_group.d`, `.worst_group.n`, `.verdict` (29 setup rows); and in the COMPILE table the `cost` row's rule cell changes from "present IFF `compile_outcome` = `compiled` AND …" to "REQUIRED when `compile_outcome` = `compiled` AND `cost_class` ≠ `lazy-jit`; OPTIONAL otherwise (v1.4, KB-4: a refusal's cost)" (no new path). A field in one and not the other fails the build | `docs/design/record_schema.md` §8; `schema/check_fields.py` unchanged |
| C2 | `check_rules.py`: the §9 rule table gains X31, X32, X33 and the revised (versioned) X13 text; the directory gains E2's files (a rule with no control, or a control naming no rule, fails the build). The two `schema-`-prefixed controls work as named (`check_rules.py` exempts the `schema` token; the Makefile uppercases it) | `docs/design/record_schema.md` §9; `schema/check_rules.py` unchanged |
| D1 | `record_schema.md`, the SAME-COMMIT edit list (panel B B13): §4 the two amendments drafted above (the rule-revision clause; the MINOR bullet's reader sentence); §4.1 the 1.4 row; §5 the `status` enum row; §8 the C1 rows and the `cost` cell; §9 X13 (versioned text), X31-X33; the v1.1 RULING "`unavailable` occupancy is not `measured`" gains a v1.4 paragraph (at 1.4 it is true of the `before` sample only; `validate.py`'s message text likewise); a §6.9 "trial agreement" subsection pointing here; §10.3's "Any statistic" bullet AND its "coverage or `n` field" bullet each gain one sentence naming `trial_agreement` as the single argued exception (counts under a recomputation rule, X32) — and the first bullet's "no ns/call" stays true because the block stores none; §10.2 gains the `timeline` as a v1.4 field. `schema/CLAUDE.md`: the `record.schema.json` bullet's version sentence ("IMPLEMENTS (1.3)" → 1.4), the `validate.py` bullet's rule list (X33 the last named), and "Rules for changing the format → No statistics" qualified by the same exception. `schema/examples/CLAUDE.md` and `bad/CLAUDE.md`: E1-E3 as written (no 1.3 example exists; nothing re-stamped) | `docs/design/record_schema.md`, `schema/CLAUDE.md`, `schema/examples/*/CLAUDE.md` |
| M1 | **What stays byte-identical for older records:** every v1.1/1.2/1.3 record in the store validates unchanged (X13's `< 1.4` branch; X31/X32 never fire without the block; X33's `< 1.4` direction is satisfied by every existing record; the new fields are optional in JSON Schema; S5 relaxes). `make check-schema` witnesses the 1.1 and 1.2 acceptance branches on the examples left at their versions; **the 1.3 acceptance branch is witnessed by `check-report`'s fixture gate and by the store's 54 × 1.3 records, NOT by `check-schema`** (there is no 1.3 example, panel B B10 (a)); and the reporter's reduction of a 1.3 and a 1.4 record in one invocation is witnessed by a NEW fixture pair (§6 R8 — the existing `mixed_version/minor_pair` fixture is a 1.0-shaped INVALID record beside a valid 1.1 one and proves only that the query is not refused, panel B B16.2) | — |

## 5. THE HARNESS CHANGES, enumerated

| # | change | file |
|---|---|---|
| H0 | **`pinning` before `quiet.check` (ruling R-2, panel C F1):** `run_cell` computes `pinning = quiet.pinning(pin_cpu)` FIRST and calls `quiet.check(exclude_cpu=pinning["cpu"])` — one source for the target core | `pcrecbench/harness.py` |
| H1 | `quiet.judge_mpstat(text, exclude_cpu, …)` also returns the target's own judged busy % (`target_busy_pct`) in the sample dict: ABSENT when `exclude_cpu` is None; `None` when the target's row is missing from the `Average:` block; a number otherwise; `None` on the `unavailable` early returns (`quiet.occupancy()`'s two early returns and `judge_mpstat`'s `not considered` return build the dict by hand and must add the key explicitly when `exclude_cpu` is an integer — panel C F17); `raw` unchanged | `pcrecbench/quiet.py` |
| H2 | `quiet.gate(load_before, occ_sample, force, …)` gains TWO clauses: `target_busy_pct` a number and `> MAX_BUSY_PCT_LIMIT` ⇒ `"occupancy: the TARGET core cpu11 reads 55.00% busy before the run (limit 10.00%) -- a competitor is pinned where this cell will be"`; `exclude_cpu` an integer and `target_busy_pct is None` and `verdict != unavailable` ⇒ `"occupancy: the target core cpu11 does not appear in the mpstat capture; the clause that judges it cannot run"` (the pre-flight refusal, §1 (c′)); refusal / `--force-unquiet` unchanged | `pcrecbench/quiet.py` |
| H3 | `quiet.occupancy_ok(block)` becomes `quiet.preflight_ok(block)`: judges `before` only (verdict `pass`, the target clauses); a new `quiet.after_notes(occ_block, load_block)` returns the §2 provenance sentences (0, 1 or 2) for a failed after sample; the "occupancy differed across the run" sentence is retired (§2) | `pcrecbench/quiet.py`, `pcrecbench/harness.py` |
| H3′ | **`cmd_quiet` judges through `quiet.gate()` (ruling R-7, panel C F3):** the CLI calls `quiet.check(exclude_cpu=…)` per sample and reduces each with `quiet.gate(load, occ, force=True)` — the reasons list is exactly what a `run`'s gate would say (load1, the per-core average, the target core; today's CLI ignores load1 and never judges the target) — printing the target's number and the sibling's on every sample and the reasons, exit 3 if any sample produced any. One instrument, one decision function, both ends (BD7's "same instrument"). `scripts/run_window.sh`'s warm-up pipes the CLI into `tail | tee`, discarding its exit code: the lane adds `set -o pipefail` locally or states in the script's comment that the warm-up is advisory | `pcrecbench/__main__.py`, `scripts/run_window.sh` |
| H4 | **ONE derivation:** `reduce.judge_trial_agreement(rows, k=1.5, d_min=2, share_c=3) -> dict` (the §3.3 block, computed from a record's match rows by the §3.5 arithmetic; `reduce.cells_from_record` already groups on (pattern_id, regime, form) → subject and `ns_per_call` takes the record row shape, so the harness calls it at step (5) with no new plumbing — panel C F8); used by the harness to stamp, by the reporter to render (§6) and by `quick` to print. The validator's X32 is the deliberate second implementation (§4 V6). `tools/selfcheck.py` pins both to one hand-computed fixture (§8) | `pcrecbench/reduce.py` |
| H5 | **the status derivation becomes a PURE function** `harness.derive_status(reasons, agreement, tier) -> (status, status_sentences)` (ruling R-10, panel C F13) implementing the DECISION TABLE below; `run_cell` (5) calls it once. The after samples produce NOTES (H3), never a status | `pcrecbench/harness.py` |
| H5′ | `record.join_notes(notes, prefix=None, first=None, limit=…)`: the `first` sentences are placed at offset 0 and NEVER elided; the elision marker names the class dropped (ruling R-4). `status_detail` = `join_notes(other_status_notes, first=status_sentences)` when `status ≠ measured`, else absent; `note` = `join_notes(rest, prefix=--note)` with the after-sample provenance sentences at the head of `rest` on a `measured` record (ruling R-5) | `pcrecbench/record.py`, `pcrecbench/harness.py` |
| H6 | the block is stamped on `setup["trial_agreement"]` on EVERY record (X33), computed AFTER every row exists and BEFORE `store.write` validates; `record.build_setup` gains the argument. Note for the lane: `store.serialize` performs NO projection and the comment at `harness.py`'s "PROJECT to the emitted schema version LAST" describes something that does not happen — delete it or say the projection is the identity, so nobody wonders whether the judged rows are the written rows (they are; panel C F8/F17) | `pcrecbench/harness.py`, `pcrecbench/record.py` |
| H7 | `record.SCHEMA_VERSION` / the emitted `schema_version` → `"1.4"`; `HARNESS_VERSION` bumped; the `--trials 1` smoke path writes the block with `n/a-trials` and still validates (X33); the two "mpstat takes ~1 s" comments become "5 s" (BD7; panel C F17) | `pcrecbench/record.py`, `harness.py` |
| H8 | the per-second peaks stay in `raw` exactly as BD7 left them (I-19); `occupancy.tool` unchanged (`mpstat -P ALL 1 5`); the §3.6 `timeline` is read from `/proc/stat` at every group boundary in `run_cell`'s per-group loop (both halves or neither) | `pcrecbench/harness.py` |
| H9 | `quick` prints the trial-agreement line under its inline comparable FROM THE BLOCK: `trial agreement: agree (0 of 6 groups; 0 of 30 rows; 0 unjudged; k=1.5, d_min=2, c=3; 5 trials)` when run with `--trials 5`, and at its DEFAULT 3 trials `trial agreement: n/a (3 trials -- the rule needs 5, odd; pass --trials 5 to judge)` (ruling R-12; panel B B11): a scratch record carries the block and an honest status like any other (§6.8's "its status is still the truth"; §3.4 says which status) | `pcrecbench/__main__.py` |
| H10 | **contract 4 gains EXIT CODE 4 = the written record's status is `inconclusive-spread`** (ruling R-6, panel C F7) — the record IS written and indexed; the exit code is what tells a script; documented in `harness_contract.md` §4 beside exit 3. `scripts/run_window.sh` retries an rc = 4 cell ONCE (a spread is not a gate transient; one re-measure, logged, then move on — never the 12 × 30 s budget), keeps the first record (records are never deleted), and `pcrecbench index` prints a PER-STATUS breakdown beside its total | `pcrecbench/__main__.py`, `scripts/run_window.sh`, `docs/design/harness_contract.md` |

**The STATUS DECISION TABLE `derive_status` implements** (panel C's
table, every undefined case U1-U9 resolved). Inputs: `R` = `gate()`'s
reasons (empty on a quiet box even under `--force-unquiet`, U9); `V` =
the block's verdict; `tier`; `A` = `after_notes` (0-2 provenance
sentences); `O` = the other sentences (scratch-tier, calibration,
adapter, did-not-compile).

| # | R | V | tier | status | `status_detail` (ordered; absent when `measured`) | `note` (ordered, after the `--note` prefix) |
|---|---|---|---|---|---|---|
| 1 | non-empty | any | any | `inconclusive-load` | R's reasons; then the §3.4 line iff V = `disagree` or (pinned and `n/a-trials`) (both facts, ruling R-15, U6); then A | O |
| 2 | empty | `agree` | any | `measured` | — | A; then O — with the "nothing judged (N rows unjudged)" sentence in O when `groups_judged = 0` (U4) |
| 3 | empty | `disagree` | any | `inconclusive-spread` | the §3.4 line FIRST; then A | O |
| 4 | empty | `n/a-trials` | pinned | `inconclusive-spread` | the §3.4 `n/a-trials` line FIRST; then A | O |
| 5 | empty | `n/a-trials` | scratch | `measured` (the explicit choice of §3.4, flagged in §9) | — | the §3.4 `n/a-trials` line; then A; then O (U8: the scratch-tier sentence is in O, as today) |

`harness-failure` appears in no row (ruling R-8). The resolved cases by
name: U1 (`--pin` given, `taskset` missing ⇒ `pinning.cpu = null` ⇒ no
target clause, no field — H0); U2 (target row absent ⇒ refusal, H2);
U3 (no `--pin` ⇒ clause (c) inert, §1); U4 (`rows_judged = 0` at 5
trials ⇒ row 2 with the sentence); U5 (X13 clause 4 never reads an
absent block at 1.4 — X33; the `< 1.4` branch does not read it); U6
(row 1); U7 (the "differed" sentence retired, §2); U8 (row 5); U9
(`--force-unquiet` on a quiet box is not a status, §1).

## 6. THE REPORTER CHANGES

| # | change |
|---|---|
| R1 | the status gate is UNCHANGED: `measured` ranks; anything else is listed under its table as `not ranked: <testee> — <status> (…)`. For an `inconclusive-spread` record the parenthesis is printed FROM THE BLOCK (ruling R-4, panel C F5): `1 of 72 groups disagree, worst cls-upto-32768 / match-compliance / plain d=23 of n=30, k=1.5` — not from the free text, whose 120-character `_excerpt` cut the earlier draft's 191-character sentence mid-token; `_excerpt` stays 120 for other statuses. `--include-unmeasured` ranks it with `status` in the row, as today |
| R2 | dedup is UNCHANGED in code and gains a case: an `inconclusive-spread` record NEWER than a measured one is "newer, not measured"; a measured re-run supersedes it; between the two inconclusive values dedup has no preference (§3.4) |
| R3 | a LEGEND line under the status-policy bullet: `- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance` |
| R4 | the header's record list gains, per RECORD line (there is no per-testee line — `rd.included` is `[(record_id, path)]`; the block is threaded into `ReportData` as `agreement_by_record` beside `status_by_testee`, panel C F12), `agreement: agree (0 of 72 groups; 0 of 1536 rows; 0 unjudged; k=1.5, 2/3; 5 trials)` from the BLOCK — not re-derived, so a reader sees what the harness stamped (the validator proved it recomputes); the stated strings for every other case (panel B B16.1, panel C F9): `agreement: disagree (1 of 72 groups; worst cls-upto-32768 / match-compliance / plain d=23 of n=30)`; `agreement: agree 0/0 groups — nothing judged (1536 rows unjudged)`; `agreement: n/a (3 trials)`; and for a pre-1.4 record `agreement: n/a (v1.3)` — the MIXED-VERSION rule: a v1.3 record has no block, the reporter never invents one, and never re-judges it (§7) |
| R4′ | **the rule marker (ruling R-1 (iii)):** the status-policy legend names the X13 rule version(s) the query's records were judged by (`status rule: v1.3 X13 (both samples quiet) on 54 records; v1.4 X13 (pre-flight + trial agreement) on 12`), and when ONE query mixes X13 versions every ranking row's status cell carries the version (`measured@1.3` / `measured@1.4`) — so a table never carries one token meaning two things without saying so; a single-version query's rows are unchanged |
| R5 | `--include-provenance` (new flag, default off): prints the §2 after-sample sentence(s) in the excerpt of a `measured` row's header line, from `note` or `status_detail` wherever they sit (ruling R-5), the `load.verdict = loaded` fact, and the §3.6 timeline (one line per group whose target/sibling/other reading departs from the run's median by more than the noise floor). Default off because the notes are provenance by ruling, and a report that printed them beside every measured row would read as a caveat on a number that has none |
| R5′ | ALWAYS, flag or not: when either after sample FAILED, the header's record line carries one short clause — `after: load1 11.40 / occ 41.41%` (9 of 68 records historically) — so the demoted instrument stays visible where a reader looks for provenance (panel C F12) |
| R6 | the R8 Δ note, from the abi-12 ledger §6(a) — a reporter/query FACT, not a v1.4 change, recorded here so the panel does not conflate them: the cross-pin `Δ vs previous version` column fires only when BOTH pins' records are in one query (a `--since` that admits one pin's window yields an empty `delta_verdict` on every row); a report meant to show a Δ must be bounded to include both. Separate row [B-next] in plan.md: matching pcrec testees on the id ROOT across pins |
| R7 | `REPORTER_VERSION` → v9 with a dated line; every committed report is re-rendered with its own query (the reports/CLAUDE.md rule) and the diff CLASSIFIED. The regeneration is forced by R3/R4/R4′/R5′ (they change the rendering of EXISTING records), not by the schema bump itself — reports/CLAUDE.md ties regeneration to rendering, and the precedent stays clean if §7 says so (panel C F15). The expected diff on existing records: the legend lines (R3, R4′), `agreement: n/a (v1.3)` on every pre-1.4 record line, the `after:` clause on the nine, and nothing in any number; the `record source: … (N candidate file(s))` count moves with the store and is not grounds to reject |
| R8 | `pcrecbench/tests/test_report.py`: `test_status_gate_r1` gains the `inconclusive-spread` case; a NEW fixture pair under `fixtures/store/` — two VALID records, 1.3 and 1.4, same sub-bench, both included (panel B B16.2) — for `test_trial_agreement_legend_and_na_v13`; a new 1.4 fixture record with `status = inconclusive-spread` whose block X32 recomputes (`test_all_fixtures_validate`: one group of ≥ 2 rows with two slow trials each suffices under (2, 3)); `test_rule_marker_on_mixed_x13_versions` (R4′); `test_provenance_flag`; `test_after_clause_unconditional` (R5′) |

## 7. MIGRATION

**v1.3 records stay valid and are NOT re-stamped.** A record in the
store is never edited (requirements §6; record_schema.md's X6 corollary).
The validator's X13 is versioned, so a v1.3 record keeps the verdict its
harness computed under the rule of its day; the reporter renders its
agreement as `n/a (v1.3)`, its status as stamped, and — when a query
mixes X13 versions — the rule version beside the status (§6 R4′).

**The nine historical `inconclusive-load` records** — the brief counted
five; the store holds nine (verified by panel B against `store/index.tsv`,
id by id), every one failed on an AFTER sample with its pre-flight
clean (load1 before 0.44-1.47, non-target occupancy before 1.00-10.00 %,
all `pass`); listed so the panel sees the whole population:

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

Under v1.4's X13 every one of the nine would pass every gate clause THE
RECORDS CARRY EVIDENCE FOR (clause 3, the target core, cannot be
evaluated for any of them — no record in the store carries the field;
panel B B15), and every one has `trial_agreement = agree` under the
group rule at k = 1.5 (0 disagreeing groups in all nine) — so
re-judging would turn all nine `measured`, including the one with a
load1 of 11.4. **They stay as they are.** Reasons: (i) a record is
history — its status is what the protocol of its day said, and the
census's value as evidence depends on the store not having been
rewritten to fit the rule it measured; (ii) nothing is lost: every one
of the nine has a `measured` re-run of the same testee at the same
version in the store (verified: 2, 1, 1, 1, 2, 1, 1, 1, 3 of them), and
reporter R2 keeps the newest MEASURED record and lists a newer
non-measured one as "newer, not measured", so no ranking changes by
leaving them, in either direction; (iii) a re-stamp would require the
harness commit, the new hash and a `migrated-from` field the schema
does not have — a MAJOR-bump's worth of machinery for zero ranking
effect. The census files record their agreement numbers, which is where
a reader who wants the v1.4 reading of them finds it.

## 8. THE CHECKS the implementation must add

Each with what it asserts and its CONTROL (the failing case that proves
the check is a check); no sleep injection in the production drivers
(ruling R-10): the end-to-end assertion goes through a hand-assembled
record and `store.write`, which validates, so X31/X32/X33 fire on the
harness's own stamp — that is the reason `check_spread_status_stamped`
is an end-to-end check at all, and it is stated here so nobody ever
passes `validate=False` and loses it.

| target | check | asserts | control |
|---|---|---|---|
| check-schema | the 1.4 example accepted | the generated 1.4 good example (E1: 5 trials, both samples' `target_busy_pct`, the block, the failed after sample, the loaded verdict, the `cost` on a refusal, the timeline) validates | E2's sixteen sabotages, each rejected FOR ITS OWN RULE (the Makefile loop; `check_rules.py` enforces rule ↔ control pairing) |
| check-schema | older examples still accepted | the 1.1 (pcrec, v8) and 1.2 (local) examples validate under the 1.4 validator | E3's three 1.1-stamped X13 controls, rejected at 1.1 for sabotages the 1.4 example carries legally |
| check-schema | `check_fields` / `check_rules` | the note's tables match the schema (C1's 29 + 1 cells); X31-X33 each have a control | delete any E2 file → build fails (existing mechanism) |
| check-schema | X13 is VERSIONED | `x13-occupancy-after-fail.jsonl`, `x13-occupancy-unavailable.jsonl` and `x13-measured-but-loaded.jsonl` (1.1) are still rejected by X13; the 1.4 example carrying the same after-sample failure and the same `loaded` verdict is ACCEPTED | the pair itself: the same sabotage, two versions, two verdicts |
| check-schema | X33 both directions | `x33-trial-agreement-missing` (1.4, no block) and `x33-trial-agreement-on-a-v13-record` (1.3, a block) both rejected by X33 | the 1.4 example (block, accepted) and the 1.1 examples (no block, accepted) |
| check-schema | the example generator is deterministic | running `schema/examples/gen_example_14.py` reproduces the committed 1.4 example byte for byte | the generic gate `make check-harness` already applies to `gen_*.py` |
| check-harness | `check_target_core_preflight` (synthetic captures, like `check_occupancy_average`; `_mpstat_capture` shares no source with `judge_mpstat`) | THREE captures with `exclude_cpu = 11`: target at 60 %, others idle ⇒ `target_busy_pct = 60`, `verdict = pass`, `gate()` REFUSES naming the target core; target at 4 % ⇒ no refusal; the target's ROW ABSENT ⇒ `target_busy_pct is None`, `verdict = pass`, `gate()` REFUSES with the missing-row reason (ruling R-2) | the non-target verdict is `pass` in all three — the refusals come from the new clauses, not from X26's; and the same three captures with `exclude_cpu = None` ⇒ no field, no refusal (clause inert, H0) |
| check-harness | `check_quiet_cli_agrees_with_gate` (ruling R-7) | one synthetic capture: `cmd_quiet`'s reduction and `gate()`'s reasons are the same list, including load1 | a capture that passes both |
| check-harness | `check_after_sample_is_provenance` | a synthetic after sample at 40 % on a run whose pre-flight passed and whose rows agree (5 trials): `status = measured`, `note` carries the §2 sentence SECOND (after the prefix), `occupancy.after.verdict = fail` (X26 still holds), the record validates at 1.4 | the same record re-stamped 1.3 is REJECTED by X13 (and by X33, honestly — both fire) |
| check-harness | `check_trial_agreement_fixture` | `reduce.judge_trial_agreement` on a hand-computed fixture — 5 trials; group A of 4 rows: one clean, one with a single 3× trial (tolerated), one with two 1.6× trials (disagreeing), one with a 0.6× trial (disagreeing) ⇒ d = 2, n = 4, DISAGREES at (2, 3); group B of 5 rows, one disagreeing ⇒ d = 1, does not; group C of 3 rows all `iterations = 1` ⇒ unjudged: `trials 5`, `groups_judged 2`, `groups_disagreeing 1`, `rows_judged 9`, `rows_disagreeing 3`, `rows_unjudged 3`, `worst_group` = A (d = 2, n = 4), verdict `disagree`; with `share_c = 1` ⇒ `agree`; truncated to 3 trials ⇒ `n/a-trials` with every count 0 and `rows_unjudged 12` | `validate.py`'s X32 recomputation on the same fixture written as a record gives the same integers and the same `worst_group` — two implementations, one fixture, no shared source (V6); PLUS the boundary rows: a trial at exactly `k · m` (not slow) and a minimum at exactly `m / k` (not fast) give the same counts in both |
| check-harness | `check_spread_status_stamped` (ruling R-10) | `harness.derive_status` on all five rows of the §5 decision table returns the stated status and the stated sentence order; then a hand-assembled record whose rows make one group disagree, stamped through the same function and written through `store.write` into a scratch store, comes back `inconclusive-spread` with the block's numbers and the §3.4 line at offset 0 of `status_detail` | the same rows with ONE slow trial per row instead of two ⇒ `measured` — the rule tolerates one, and the check shows it does |
| check-harness | `check_status_sentence_never_elided` (ruling R-4) | a record whose calibration sentences exceed the free_text cap (bench/bounded's shape) still has its status-deciding sentence at offset 0 and the elision marker names the class dropped | the same sentences joined WITHOUT `first=` show the status sentence elided |
| check-harness | `check_smoke_block_na_trials` | the existing `--trials 1` smoke record carries the block with `verdict: n/a-trials`, `trials: 1`, every count 0, `rows_unjudged` = its row keys, and validates; its status is `measured` on the scratch tier (§5 row 5) | X33's `x33-trial-agreement-missing` control; and the same record re-tiered `pinned` through `derive_status` ⇒ `inconclusive-spread` (§5 row 4) |
| check-harness | `check_scratch_carries_block` | `quick --trials 5` writes a scratch record WITH the block (verdict `agree`) and prints the agreement line | `quick` at its default 3 trials writes the block with `n/a-trials` and prints `agreement: n/a (3 trials …)` |
| check-harness | `check_exit_code_4` (ruling R-6) | a `run` whose record is `inconclusive-spread` returns 4 with the record written and indexed; `pcrecbench index` prints the per-status breakdown | the same run `measured` returns 0 |
| check-harness | `check_timeline_provenance` (§3.6) | a `run` on a box with `/proc/stat` writes one `timeline` item per group with `elapsed_ms > 0` and the target core the busiest; validates | a run with `/proc/stat` made unreadable writes NO `timeline` and no `timeline_tool`, and validates |
| check-report | `test_status_gate_r1` extended | an `inconclusive-spread` fixture is unranked, listed by name with its block's numbers, ranked under `--include-unmeasured` | the existing measured fixture in the same group ranks |
| check-report | `test_trial_agreement_legend_and_na_v13` | over the NEW 1.3 + 1.4 valid pair: the legend line prints once; the 1.3 record shows `agreement: n/a (v1.3)`; the 1.4 record shows its block's numbers; both reduce in one invocation | `test_mixed_schema_versions_refused` (existing, MAJOR pair) |
| check-report | `test_rule_marker_on_mixed_x13_versions` (R4′) | the mixed pair's ranking rows carry `measured@1.3` / `measured@1.4` and the legend names both rules | a single-version query's rows carry no suffix |
| check-report | `test_v13_record_still_renders` (panel C F13) | the existing fixture store renders and the ONLY new lines against the committed rendering are the R3/R4′ legend lines, `agreement: n/a (v1.3)` per record and the `after:` clause where an after sample failed | the same diff with a number changed is refused by the test |
| check-report | `test_provenance_flag` / `test_after_clause_unconditional` | the §2 sentence appears only under `--include-provenance`; the `after:` clause appears without it on a record whose after sample failed | default rendering of the same record lacks the sentence; a record with clean after samples lacks the clause |
| check-report | `test_reporter_version_pin` | v9 and every committed report re-rendered with a classified diff | the existing mechanism |

## 9. OPEN QUESTIONS, ESCALATIONS AND RESIDUE

Closed by the panel and the rulings, and no longer listed here: Q2
(`harness-failure` stays documentation, R-8), Q4 (the base-rate
arithmetic is withdrawn; the group rule makes it moot), Q5 (the block
stays, counts only, both §10.3 bullets amended), Q6/Q7 (N ≥ 5 and odd,
R-12), Q8 (confirmed, R-13), Q9 (no exemption — the row is real, R-14
as amended), Q10 (confirmed, R-15).

**Escalated — the manager must rule:**

- **E-1 — R-19 and the five all-trials-`timed-out` rows.** R-19 counts a
  row with a `timed-out` trial as DISAGREEING ("a trial that hit the
  alarm is a disturbance, not a measurement"). The group census finds
  five such rows in the store, and every one is `libpcre2 jit ×
  factored / large-subject-throughput / t-c-long-atom-run` with ALL
  FIVE trials `timed-out` (two records of email@0.1, three of
  email@0.2): a consistent engine refusal on a 1 MB subject, not a
  disturbance — the trials AGREE that the engine cannot do it inside
  the budget. Under (2, 3) they do not flag (d = 1 of 3 or 5), so the
  store is clean either way; but a second such subject in the 5-row
  email@0.2 throughput group WOULD make that record `inconclusive-spread`
  for a fact about the engine, and the margin at n = 5 is one row. §3.5
  applies R-19 as ruled and this spec asks whether it should instead
  read: a row with a `timed-out` trial BESIDE ≥ 1 timed trial (a MIXED
  row — the alarm hit some passes and not others) disagrees; a row whose
  EVERY trial timed out is an outcome, not a spread, and is counted in
  `rows_unjudged`. The census numbers are the same under both readings
  today.
- **E-2 — the scratch tier under `n/a-trials`.** §3.4/§5 row 5 keep the
  pre-flight's status (`measured`) on a scratch record whose block says
  `n/a-trials`, so `quick`'s default and the smoke suite do not write
  `inconclusive-spread` on every clean run; R-12 rules the pinned case
  and separates the tiers without saying this. Confirm, or rule the
  status tier-independent (then `check_after_sample_is_provenance` and
  the smoke suite run at `--trials 5`, or assert `inconclusive-spread`).
- **E-3 — the reading of R-16's second constraint.** §3.2 chose (2, 3)
  as the LEAST SENSITIVE candidate that still flags both shapes at
  every named size; (2, 4) also satisfies both (T = ⌈n/4⌉: 2, 2, 8, 22,
  28 at n = 4, 5, 30, 85, 112; half-shape margins 0, 0, 7, 20, 28;
  store margins 2, 1, 8, 22, 28). If "the smallest threshold" meant the
  smaller T, the constants are (2, 4) — a one-line change, every table
  in §3.2 carries both.

**Open, not gating the implementation:**

- **Q1 — the target-core pre-flight's own distribution (ruling R-11).**
  Not gated on a measurement: the first v1.4 window prints the target's
  number on every pre-flight and reads the post-cell decay from each
  record's `after.target_busy_pct` (the AFTER number of cell n is what
  cell n+1's pre-flight sees 15 s later). If the residue exceeds 10 %,
  the sleep grows, not the bar; the retry budget stays 12 × 30 s.
- **Q3 — the measured positive control (panel A F11).** A plan row, not
  an open question, and it FOLLOWS the implementation: two scratch-tier
  cells archived under `measurements/` — (a) a memory-bandwidth loop
  pinned to CPU 5 (the SMT sibling) started at a known offset for a
  duration covering 2-3 passes of one large group (the rule should
  flag); (b) the same covering an entire group's five passes (§3.2 band
  2 predicts the rule MISSES it, and the §3.6 timeline should show it) —
  the first measured statement of what the instrument can and cannot do.
  §8's fixture proves the arithmetic; only this proves the instrument.

**Residue — known and stated, no rule:**

- the rule's margin in k is 0.05-0.10, not 4.9× (§3.2); the store cannot
  choose k above 1.55; four characterised bursts carry the sensitivity
  argument;
- a bimodal artifact (§3.1 fact 3) and a two-pass disturbance are the
  same shape to the rule; a disagreeing group says "look", not "why";
- a pinned record with 5 trials and `groups_judged = 0` is `agree` and
  `measured` with `rows_unjudged` saying what was not examined (§3.4);
  the store's 100 unjudged row keys are 38 keys (190 trial-rows) at
  `iterations ≤ 1` — every one `factored / large-subject-throughput`,
  the 1 MB email subjects where one call already exceeds the budget,
  unjudgeable by construction and exactly the rows a throughput ranking
  reads — plus 62 keys whose every trial is `gave-up` (40
  `whole-subject` match-compliance, 22 large-subject-throughput, the
  bounded set's give-up axis), which are outcomes, not spreads;
- the presence of `after.target_busy_pct` is a harness convention, not
  a rule (§1);
- `harness-failure` is an enum value no code path produces (§3.4);
- the `loglines@0.1 × pcrec_35e1ab1_vm-caps` record of 2026-08-28
  (§3.1 fact 1) is `measured` by phase, not by the quality of its
  numbers — which its cross-run reproducibility shows were fine.

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

### §H.2 The r3 panel (2026-08-30) — what it changed

Three read-only critics (measurement validity; schema and validator
consistency; harness, reporter, checks and migration) filed 45 findings
against the SPEC above as merged at fa152d3; the manager ruled R-1..R-20
before the compile; the review is
`docs/dev/reviews/2026-08-30-r3-gate-shape-v14.md`. What moved: the
record-level fraction F = 1 % was shown to sit ON a group-size boundary
(0.00-0.01 rows of margin on seven real records, no safe F across the
three sets) and was replaced by the GROUP rule `v1.4-group` — a group
disagrees at d ≥ 2 and 3·d ≥ n, constants read from a new group-level
census (`2026-08-30-trial-agreement-census-groups.txt`); the rule now
requires N ≥ 5 and odd (`n/a-trials` otherwise; a pinned record with
fewer is `inconclusive-spread`); the block records `trials`,
`rows_unjudged` and a two-integer `worst_group` instead of a per-trial
array; the arithmetic is stated once as pseudocode (§3.5) so the
validator's second implementation cannot drift; k = 1.5 stays, with its
margin stated honestly (0.05-0.10 in k; the store uninformative above
1.55) and the three blind bands and the power table put in §3; the
single fast row was re-read as a real bimodality, not a timer artifact;
`target_busy_pct` became a tri-state keyed on `pinning.cpu` with a
missing target row refused BEFORE the run; the status-deciding sentence
goes first and is never elided, today's `note`/`status_detail` split is
kept, the reporter prints an `inconclusive-spread` record's numbers
from the block; contract 4 gained exit code 4 for the window script;
the `quiet` CLI judges through `gate()`; the bump stays MINOR under a
drafted §4 amendment (a rule revision keyed on version, older records
never re-judged, the rule version rendered beside every ranked status);
the examples plan was rewritten against the examples that actually
exist; KB-4's schema half rides along; a per-group `/proc/stat`
timeline was designed as provenance only; and `harness-failure` stays
an enum value no code path produces. Three items are escalated (§9
E-1..E-3).
