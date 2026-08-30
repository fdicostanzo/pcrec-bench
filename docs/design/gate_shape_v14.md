# The quiet gate's shape after BD7 — a schema v1.4 PROPOSAL (2026-08-30)

STATUS: PROPOSAL, not adopted. Written the night of the bench/bounded@0.1
first window for Frank to rule on WITH the gate-shape test run's data
(docs/dev/measurements/probe_gate_shape.py; the archive lands beside it).
Adoption = a record-schema MIGRATION (record_schema.md's migration rule),
a critic panel (the manager skill §6), and a reporter change. Nothing in
this note changes a record today; BD7 (the 5-s averaged occupancy sample)
is what the harness does now.

## Where the ruling came from

Frank, 2026-08-30 ~01:2x EDT, relayed by pcrecdev1 (durable copy owed in
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
are the proposal below.

## The evidence so far (the six 36d5963 bounded records, 2026-08-30)

Every `inconclusive-load` record the pinned windows have produced —
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

**The spread rule this suggests (P2):** the odd trial is always SLOWER,
never faster (a burst can only add time), so the robust statistics are
the median and the minimum. Rule candidate: per (pattern, regime,
subject) row, count trials above 1.5x the row's median; a row with ONE
such trial is a tolerated perturbation (the median is untouched); a row
with TWO or more (of five) is a disagreeing row; a cell with disagreeing
rows above a small fraction (to be set — 0 of ~1,500 in these six) is
`inconclusive-spread`. The 1.5x and the fraction are the panel's to
measure, not to pick.

## The proposal

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

## What decides it

The test run: the three inconclusive bounded cells re-measured under
BD7, per cell the status, the spread distribution, and the old 1-s
verdict recomputed from the recorded peaks. If BD7 alone measures them
and the spread profile matches the measured cells', P1 is supported by
data and P2's rule can be set from the characterised outliers. Frank
rules; the panel reviews; then [B20].
