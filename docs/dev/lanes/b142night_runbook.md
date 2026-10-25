# b142 night runbook (2026-10-25 -> 26): two box-queue reservations

Written by lane b147chains. NOT RUN. Part 1 (`b142win_chain.sh`) is the
afternoon window and is already running or done; this is the night behind it.

## The two commands (launch from the MAIN tree, in this order)

```
cd /home/pcrec/projects/pcrec-bench
MACHINE_ID=ryzen7700x setsid scripts/boxq_window --name b142-part2 --prio 710 \
    --cap 14520 --patience 86400 --idle-ok 600 --start-s 300 -- \
    docs/dev/lanes/b142win2_chain.sh > /dev/null 2>&1 &
MACHINE_ID=ryzen7700x setsid scripts/boxq_window --name b142-tier2 --prio 720 \
    --cap 29700 --patience 86400 --idle-ok 600 --start-s 300 -- \
    docs/dev/lanes/b142win3_chain.sh > /dev/null 2>&1 &
```

Both reservations may be written up front (names, priorities 710 < 720 order
them in pcrec's queue; the wrapper polls the state file and starts each chain
when its state reads RUNNING). The chains are executable; `MACHINE_ID` passes
through the wrapper to the chain.

| name | prio | chain | estimate | cap = est x 1.3 |
|---|---|---|---|---|
| b142-part2 | 710 | b142win2_chain.sh (bench/subst at 9ae59f5d4) | ~3.1 h (186 min) | 14,520 s (186 x 1.3 = 242 min) |
| b142-tier2 | 720 | b142win3_chain.sh (litrun, syntax, utf8, email, bounded, loglines x {auto, auto@6b2dbd3e}) | ~6.4 h (381 min) | 29,700 s (381 x 1.3 = 495 min) |

`--idle-ok 600` is a GUESS at the argument's meaning ("the quiet gate":
seconds of idle the box must show before the start). Neither the wrapper nor
our docs define it (the key is pcrec's contract; boxq_window only forwards the
number). Confirm the unit and meaning with pcrecdev1 before launching, or drop
the flag (it is optional).

The caps are the reservation's ceiling, not the plan: each chain carries its
own deadline, `STOP_AT_NIGHT` (default 09:30 on the morning after launch;
launching after midnight and before noon uses today's date), after which no
cell starts that is expected to end past STOP_AT_NIGHT + 10 min; the closing
sentinel's cells start before STOP_AT_NIGHT + 10 min. So nothing runs past
~09:47 whatever the queue does. If part 2 starts late and tier 2 therefore
starts late, tier 2 loses sets from its tail (bounded first, then email); the
closing sentinel still runs. A chain refuses to start (CHAIN_ABORT) with under
90 minutes left before its STOP_AT_NIGHT. Because tier 2's cap (8.25 h) exceeds
the 00:00-10:00 night, the chain deadline, not the cap, is what ends it; the
cap is the hard kill only if the chain stalls.

## Before the reservation starts (no CPU rule applies once the afternoon window is done)

1. Pre-generate the 362 MB subject (otherwise part 2 does it inside its own
   reservation, ~10-15 min, unmeasured):
   `python3 bench/subst/gen_subjects.py --out /var/tmp/pcrecbench/subst/subjects`
   (default location the chain checks: `/var/tmp/pcrecbench/subst/subjects`,
   override `PCRECBENCH_SUBST_SUBJECTS`). Do NOT run it while a timing window
   is running.
2. `bash -n` both chains (done by the lane); `git status` clean for tracked
   files the chains read (they write only `store/`, `build/`, `/var/tmp/`).
3. Part 1 of loglines: if `b142win_chain.sh` measured loglines x {auto,
   auto@6b2dbd3e} (it did in the plan), launch tier 2 with `LOGLINES=0` added
   to its environment (`LOGLINES=0 MACHINE_ID=... setsid scripts/boxq_window
   ...`). If part 1 dropped it (STOP_AT 18:30 reached), leave the default (on).
4. Ask pcrecdev1 to confirm the two reservations and the meaning of `--idle-ok`.

## How the manager checks state

* Wrapper run log (one per reservation; wrapper lines only):
  `worktrees/.mgr/boxqueue/logs/b142-part2.log` / `b142-tier2.log`. It ends
  `BENCH_WINDOW_COMPLETE rc=0` (chain returned 0) or
  `BENCH_WINDOW_FAILED <why>` (chain rc != 0, abort, or state left RUNNING).
  The chain's own stdout/stderr: `/var/tmp/pcrecbench/b142-part2win/run.log.chain`.
* Chain logs: `/var/tmp/pcrecbench/b142win2/chain.log` and
  `/var/tmp/pcrecbench/b142win3/chain.log`: the last line is `CHAIN_DONE`
  (finished) or `CHAIN_ABORT <why>` (nothing measured: unresolved testee,
  missing tool binary, subject mismatch, too late). Progress lines:
  `SENT0_DONE`, `LIB_DONE`, `JITSTACK_CHECK`, `TOOLS_DONE`, `SENT1_DONE`
  (part 2); `SENT0_DONE`, `SET_DONE <set> rc=N`, `SENT1_DONE` (tier 2).
* Per-set suite logs next to them: `suite_*.log` (each ends
  `SUITE_RUN_COMPLETE`; a skipped set/cell says `STOP_AT`); the window logs
  under `build/windows/window_*.log` (grep `KILLED by the per-cell cap`,
  `inconclusive-spread`, `STOP_AT reached`).
* Part 2 specials in the chain log: `JITSTACK_CHECK files=N hits=M gave_up_rows=K`
  (hits=0 = no -46 on acc-main; any `JITSTACK_HIT <record>` names the cell),
  `SUBJECT ok ...`, `drvsum` sha256 lines (driver identity before/after).
* Queue state (read-only): `/home/pcrec/projects/pcrec/worktrees/.boxqueue/reservations/710-bench-b142-part2.state`
  (`QUEUED` / `RUNNING` / `DONE...`).
* Records: `python3 -m pcrecbench index` is run by every window; do NOT run
  heavy reporter loads during a window.
* Cancel before start: `scripts/boxq_window --cancel b142-part2` (writes the
  cancel file; a running chain is killed by the wrapper when the state leaves
  RUNNING).
* After each: `git status` shows the window dirtied `store/index.tsv` by
  design; stage explicit paths only (no `commit -a`).

## What each window answers

* Part 2: first timed bench/subst records at 9ae59f5d4 (library tier 10
  testees, tools tier 5), the JIT-stack check on acc-main, the BD16 (3)
  sentinel reads owed by b140drv/b140drv2/b140pcrec (pcre2-jit, rust-default,
  re2-default, pcrec-auto; opening vs closing pass; rust/re2 have no earlier
  sentinel read that we have checked, so within-window agreement is their
  only baseline).
* Tier 2: b142prep_report.md section 8 tier 2 (the movers' sets at both pins
  with a sentinel pair).

OWED to the manager before launching (unresolved by this lane): the meaning
of `--idle-ok`; whether the pcrec queue accepts both names at once; the
spread-rule ruling for substitution records (b140drv finding 1: the v1.4
trial-agreement rule is blind at iterations = 1, but schema v1.10 `v1.10-group`
(B144) says a substitution trial is judged at >= 1, so this should be
resolved; verify it on the first part 2 record).
