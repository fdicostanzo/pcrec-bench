# [B138] b138chain -- tonight's re-baseline window chain (lane report)

Deliverable: `docs/dev/lanes/b138_chain.sh` (NOT RUN as a window). Branch `b138chain`.
Box: frank-desktop, Ryzen 7 7700X (8c/16t, 16 CPUs), Ubuntu 26.04. No timing run was made:
only the `--dry-run` rehearsal (synthetic, scratch tier, 1 trial) ran.

## Launch

    MACHINE_ID=<slug> TIERS="1" setsid bash docs/dev/lanes/b138_chain.sh > /dev/null 2>&1 &
    # TIERS defaults to "1 2"; STOP_AT_T1 / STOP_AT_T2 cap SETS (no cell starts after it);
    # PIN defaults to 7 (SMT sibling 15); DRYRUN=1 rehearses.

Log `/var/tmp/pcrecbench/b138win/chain.log`: `CHAIN_START`, `TIERn_DONE suite_rc=.. closing_rc=..`,
`CHAIN_DONE` (or `CHAIN_ABORT <why>`). The closing sentinel pass is a SEPARATE run_suite call,
so STOP_AT can never skip it. After the registration step `store/machines.tsv` has one new,
UNCOMMITTED row for the manager to commit.

## Rosters (all names resolve against `pcrecbench testees`; checked by the chain on every start)

CORE = pcrec-auto, pcrec-nocaps, pcrec-vm + pcre2-jit, pcre2-interp + ONE config per other engine
the set has records for (from b138hours_report.md tables).

| set (version) | roster | cells |
|---|---|---:|
| sentinel@0.1 (opening and closing of each tier) | pcrec-auto pcrec-nocaps pcre2-jit | 3 |
| email-specimen@0.2 | pcrec-{auto,nocaps,vm} pcre2-{jit,interp} rust-default | 6 |
| loglines@0.1 | same | 6 |
| altwide@0.3 | same | 6 |
| bounded@0.3 | same | 6 |
| litrun@0.1 | pcrec-{auto,nocaps,vm} pcre2-{jit,interp} (no other engine has records) | 5 |
| capability@0.2 | pcrec-{auto,nocaps,vm} pcre2-{jit,interp} onig-default vectorscan-block-nosom tre-default re2-default rust-default | 10 |
| syntax@0.1 | pcrec-{auto,nocaps,vm} pcre2-{jit,interp} rust-default | 6 |
| utf8@0.1 | pcrec-{auto,nocaps,vm}-utf8 pcre2-utf-{jit,interp} onig-utf8 re2-utf8 vectorscan-block-nosom-utf8 rust-default (rust has no -utf8 sibling) | 9 |

Cells: **tier 1 = 3 + 6+6+6+6+5 + 3 = 35**; **tier 2 = 3 + 10+6+9 + 3 = 31**; 66 total.
Not in CORE: pcre2-dfa, re2-longest, vectorscan-som, every pcrec deny/clang/align/bigcap sibling.
Order within a set: pcrec first, then pcre2, then the others.

## CELL_CAP (s) and the 5400 s question

Longest CORE cell at Zen-1 timings: capability pcre2-interp 71.9 min = 4,314 s; then 61.3 (pcrec-vm,
255bcdd8), 57.6 (onig); altwide jit 65.0; bounded vm 54-57. **No CORE cell exceeds 5400 s.**
(The 106.5 min capability cell is pcre2-dfa, not in CORE.) Caps: sentinel/email/loglines/litrun 3600,
altwide/bounded/syntax/utf8 5400, capability 7200 (4,314 s is 80% of 5400; 7200 leaves margin). Note
run_suite resolves the labelled `sentinel:endN` cap only from `CELL_CAP_sentinel_endN`, hence those are set.
The altwide pcre2-interp cell has no @0.3 record (0.1 took 41.9 min); its time is imputed.

## Estimates (assumption: new box = 2.0x Zen-1; the window measures it)

Zen-1 minutes (cell + 0.5/cell + 2.5/set, b138hours): sentinel 25 per pass, email 48, loglines 57,
altwide 158 (+45 imputed interp = 203), bounded 262, litrun 70, capability 443, syntax 247, utf8 330.

| tier | Zen-1 min | at 2.0 |
|---|---:|---:|
| 1 (2 sentinel passes + email, loglines, altwide, bounded, litrun) | 690 | ~345 min (~5.8 h) |
| 2 (2 sentinel passes + capability, syntax, utf8) | 1,070 | ~535 min (~8.9 h) |

Measured factor: the chain parses the sentinel window log after each tier's opening and closing
pass and logs `SENTINEL_FACTOR zen1_min=.. tonight_min=.. factor=..` (Zen-1 reference 6.1 + 6.1 + 9.1 min
for pcrec-auto, pcrec-nocaps, pcre2-jit, the 2026-10-13 cells). Record-side cross-check: a cell's span =
`environment.load.after.sampled_at - environment.load.before.sampled_at`, Zen-1 records vs tonight's.
Remaining estimate = remaining Zen-1 minutes / factor. (Caution: the factor from sentinel's short-call
cells may differ from the long-subject sets.)

## Rehearsal

`DRYRUN=1 TIERS="1 2"` (scratch store `/var/tmp/pcrecbench/b138chain/store`, machine `rehearsal-box`,
one cell per set, first roster name). Result:
- Roster names: all 9 rosters resolved ("roster names resolve").
- Registration: `rehearsal-box` registered in the SCRATCH store (hostname frank-desktop, cpu_model
  `amd-ryzen-7-7700x-8-core-processor`, cores 16: env.py's own derivation). Checks: no MACHINE_ID ->
  `CHAIN_ABORT` rc 9 (real mode, nothing measured); a second id for this box -> refused by name, abort;
  same id again -> no-op, chain proceeds.
- Tier 1 completed in full: sentinel, email, loglines, altwide, bounded, litrun, sentinel:end1, all
  rc=0, `TIER1_DONE suite_rc=0 closing_rc=0`; `SENTINEL_FACTOR` parser fired on both passes (synthetic
  timing, factor 4.8 is meaningless). Tier 2: sentinel, capability (10 min), syntax (9 min) rc=0.
- My own `gnutimeout 3000` on the rehearsal expired during tier 2's utf8 (rc=124 of the chain; the
  orphaned run_suite/run_window/python were then killed by PID, all started by me). So utf8 and
  sentinel:end2 were proved by a second, direct call with the chain's variables:
  `SENTINEL=0 SUITE="utf8 sentinel:end2" TESTEES_utf8=pcrec-auto-utf8 ... run_suite.sh --dry-run`:
  `set utf8 rc=0 8 min`, `set sentinel:end2 rc=0 1 min`, WINDOW_RUN_COMPLETE cells=1/1. So the exact
  tier-2 chain tail (TIER2_DONE / CHAIN_DONE lines) was not exercised end to end, but the same
  `run_tier` code ran for tier 1 and a `TIERS=9` pass printed `CHAIN_DONE` with the driver sha256.
- The real `store/` was never named; `git status` in the main tree stayed clean. Dry-run cost: a
  synthetic cell is minutes (it compiles every pattern), ~1h for the full 8-set rehearsal.
- Log tail (tier 1 end, from `/var/tmp/pcrecbench/b138win-dry/chain.log`):

      -- set litrun rc=0 3 min 2026-10-18T05:02:57-04:00
      -- set sentinel:end1 rc=0 1 min 2026-10-18T05:04:45-04:00
      TIER1_DONE suite_rc=0 closing_rc=0 2026-10-18T05:04:45-04:00
      2c5061115e52679d6e5a51e9d329e1c0edc943e038cf4ac2f6e161a6ce7b092d  build/work/pcrec-auto/pcrec_driver
      SENTINEL_FACTOR zen1_min=6.1 tonight_min=1.3 factor=4.82 cells=pcrec-auto:1.3

## Open questions / not resolved

1. **Core 7 read 100% busy** in the advisory `quiet` warm-up at the start of three sets during the
   rehearsal ("TARGET core cpu7 reads 100.00% busy"; the pinned dry-run drivers run on cpu7, and the
   warm-up sees the tail of the previous cell, but I could not confirm that). Real windows will refuse
   or retry on the pre-flight if it is another process (Frank's, or pcrecdev1's jobs; load was 2-10
   from their work during the rehearsal). The manager should check `mpstat -P ALL` for cpu7 and cpu15
   on a quiet box before launching, and override PIN if needed.
2. Registration needs Frank's id; the cpu_model/cores/hostname are auto-derived (cores = 16 from
   sched_getaffinity, so launching under a restricted affinity would register a different core count).
3. The 2.0 factor and the imputed 45 min for altwide pcre2-interp are guesses.
4. Driver builds happen inside the first sentinel cell (the start-of-chain sha256 line is empty on a
   fresh tree); the end-of-chain line is the one to compare with the post-tier-1 line.
5. The worktree's `build/` holds rehearsal driver builds/scratch only; the pcrec pin was reused from
   the main tree's `build/pcrec-6b2dbd3e` (pin.sh --path), nothing built there.

## Charter vs committed

| # | requirement | status |
|---|---|---|
| 1 | pin 6b2dbd3e only, no @also_pin, configs.toml untouched | done (no `@` entries; `git diff master -- testees` empty) |
| 2 | CORE roster per set, resolved against `testees`, listed | done (table above, chain re-checks at start) |
| 3 | tier 1 / tier 2 split, TIERS, STOP_AT_T1/T2, CELL_CAP per set, >5400 s check | done; no CORE cell > 5400 s |
| 4 | portable cd, /var/tmp/pcrecbench/b138win/, b136 markers, PIN=7 default + sibling 15 in header | done |
| 5 | MACHINE_ID env, abort without, idempotent registration | done and tested (3 arms) in the scratch store; real store untouched |
| 6 | preconditions: pin.sh --path, subjects (all gen scripts), quiet sample, driver sha256 | done |
| 7 | per-tier estimate (Zen-1 / 2.0) + how the sentinel yields the factor | done (header + SENTINEL_FACTOR line) |
| 8 | dry-run rehearsal, one cell per set + sentinel, scratch store, log tail | done, with the utf8/sentinel:end2 caveat above |
| 9 | lanes/CLAUDE.md + this report | done |
