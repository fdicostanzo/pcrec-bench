# OD-B8 — what "quiet" means on this box, measured

STATUS: MEASURED 2026-08-25 by the [B3] lane, on `ubuntubudu` (AMD Ryzen 5
1600 Six-Core, 12 logical CPUs, linux-7.0.0-29-generic). These are the
numbers behind `pcrecbench/quiet.py`'s two defaults. Requirements §9(c):
what "quiet" is numerically is MEASURED on this box, not assumed.

## The caveat that comes first

**A genuinely idle baseline was NOT obtainable.** Another session was
running pcrec's long test batteries on this box for the whole of the
lane's window, and the mandate forbids interfering with it. So what
follows is a baseline of the box UNDER A KNOWN COMPETING WORKLOAD, plus
what that measurement implies about the idle floor. Where a number is
inferred rather than sampled, it says so. Re-measuring on a quiet box is
cheap (`python3 -m pcrecbench quiet --samples 12`) and should be done
before the thresholds are treated as settled.

## What was sampled

12 samples over ~60 s: `/proc/loadavg` and `mpstat -P ALL 1 1`, `LC_ALL=C`.

| quantity | min | max | mean |
|---|---|---|---|
| load1 | 1.28 | 1.47 | 1.39 |
| aggregate `%idle` (mpstat `all`) | 85.81 | 90.00 | ~88.5 |
| the WORST core's `%idle` in a sample | 61.62 | 81.00 | — |
| the BEST core's `%idle` in a sample | 92.86 | 97.96 | — |

`max_busy_pct` (= 100 − the worst core's `%idle`), per sample:
21.21, 27.00, 23.71, 29.29, 21.00, 26.26, 26.00, 19.80, 19.00, 38.38,
22.22, 32.00.

## The two thresholds, and where they come from

### `MAX_BUSY_PCT_LIMIT = 10.0` — "every non-target core ≥ 90% idle"

The derivation is the BEST-core column. In every one of the 12 samples
the quietest core sat at 92.86–97.96 % idle, i.e. **the instrument's own
noise floor is ~2–7 % busy per core** even when nothing is scheduled
there (timer ticks, mpstat itself, kernel housekeeping). A 10 % bar
clears that floor with headroom, so it will not refuse an idle box for
noise.

It is also a bar with a REAL POSITIVE CONTROL rather than a synthetic
one: **all 12 samples fail it** (the worst core never reached 90 % idle
while the battery ran). The gate was seen to fire on a box that was in
fact busy — which is the thing pcrec's check-design lesson says a gate
must be seen to do before it is believed.

### `LOAD1_LIMIT = 2.0` — and the finding that it is the WEAKER instrument

The harness runs ONE driver process at a time, so its own contribution to
load1 approaches 1.0 while a cell runs (and the AFTER sample is taken
while that contribution is still decaying out of the 1-minute average).
2.0 leaves exactly one core of headroom above our own work and no more.

pcrec's `compare.sh` uses `max(2.0, cores/2)`, which is 6.0 here. That is
right for a suite that may run several jobs in parallel and wrong for a
single pinned measurement: 6.0 admits five competing threads.

**The measured finding, and it is the one worth carrying to the panel:
the load gate did not fire once.** load1 stayed at 1.28–1.47 for the
whole window — comfortably under 2.0, and under `compare.sh`'s 6.0 by a
factor of four — while a test battery was demonstrably occupying the box
enough to fail the occupancy gate 12 times out of 12. load1 is a
1-minute-smoothed, box-wide number; it cannot see a moderate, steady
competing workload, which is exactly the shape of workload that
contaminates a single-core measurement.

So the division of labour is explicit, and the record carries both:

- **per-core occupancy is the DETECTOR.** It is sharp, it is per-core,
  and it is the check that actually refused this box.
- **load1 is a coarse BACKSTOP** for a heavily loaded box and for the
  AFTER-sample re-check (requirements §9(a), C7 — a box that went busy
  partway through). Its positive control at 2.0 is synthetic: lowering
  the limit to 1.0 makes it fire on the samples above.

A record that passes load1 and fails occupancy is `inconclusive-load`,
not `measured` (record_schema.md X13), so the weaker instrument's silence
cannot promote a contaminated run.

## What is still open

1. **The idle floor is inferred, not sampled.** Re-run on a quiet box.
   The expectation from the best-core column is `max_busy_pct` ≈ 4–8 and
   load1 ≈ 0.0–0.3.
2. **The AFTER-load limit may want to be different from the BEFORE
   limit.** One `environment.load.limit` field carries one number today
   (record_schema.md 10.2 deliberately left it as data). A long cell's
   own after-sample can approach 1.0 on its own; if the limit is ever
   tightened toward 1.0 for the before-sample, the after-sample needs its
   own, looser number.
3. ~~**`mpstat -P ALL 1 1` costs one wall second per check**, taken twice
   per run. Cheap, and not on the timed path.~~ Superseded 2026-08-30:
   the instrument is now `mpstat -P ALL 1 5` (five wall seconds per
   check, still off the timed path) -- see the section below.

## 2026-08-30 -- the occupancy sample is 5 x 1 s judged on its AVERAGE (BD7; OD-B12 closed)

EVIDENCE. Every `inconclusive-load` record the pinned windows produced
-- two on 2026-08-29 (`email x pcrec-vm` 11.1 %, `loglines x
pcrec-nocaps` 13.0 %) and three on 2026-08-30 (bench/bounded@0.1's
`pcre2-jit` 10.10 %, `pcrec-auto` 20.2 %, `pcrec-vm-in`) -- failed on
the AFTER sample alone: one non-target core over the 10 % bar on a
single 1-second `mpstat` interval, load1 quiet (1.0-1.2, the cell's own
driver), the before-sample clean, and nothing sustained on the box. The
culprits were identified by `pidstat -u 1` during the 2026-08-30
window: the VS Code remote server (`~/.vscode-server/.../node`, 40 % of
a core for about a second when a file it watches changes -- the store
write and the window log are such files), a streaming Claude session's
own ~9 %, and a per-refresh `gh pr list` from the sessions' status
lines (~40 % for ~0.5 s; since switched off). None of these touches the
pinned core; a 1-s sample cannot tell such a burst from a competitor.

RULING (BD7). `pcrecbench.quiet` runs `mpstat -P ALL 1 5` and judges
mpstat's own `Average:` block: the per-core busy AVERAGED over five
seconds. A half-second 40 % burst reads 4 %; a competing process at
100 % still reads 100 %; a streaming session at 9 % still reads 9 %.
The SAME instrument is used at both ends (`quiet.check()`: one code
path, two calls). `environment.occupancy.tool` names the command, so a
record judged by the 1-s instrument (`mpstat -P ALL 1 1`, every record
before 2026-08-30) is distinguishable from one judged by the 5-s one;
X26 (verdict iff `max_busy_pct <= limit_busy_pct`) is unchanged, and
`raw` now carries the Average block plus the per-second peak of the
busiest non-target core, so the transient the average absorbed is
still visible. The 10 % bar is NOT moved: the noise floor measured
above (2-7 % per core) is the same floor, and the two-manager residue
(a second streaming session, ~9 %) is now a steady number the average
reports honestly rather than a coin-flip the sample may or may not
catch -- both managers idle for a window remains the protocol (BD6).

CONTROLS (`tools/selfcheck.py check_occupancy_average`, seven checks on
a synthetic capture, no mpstat needed): a one-second 30 % burst
averages to 7.6 % and passes while the burst second judged ALONE reads
30 % (the old rule's fail -- so the rule, not the fixture, is what
passes it); a core at 100 % for all five seconds still fails; the
target core is excluded iff asked; a single-interval capture (no
Average block) is judged as itself; `raw` keeps the Average block and
the peaks. Cost: five wall seconds per check, twice per cell, plus the
window script's `quiet --samples 6` warm-up (30 s) -- off the timed
path.
