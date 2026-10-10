# [OPT-REVEND] states 1+2 ledger -- a15fb77b (abi 72, BEFORE) vs 7388f1c0 (abi 73, AFTER)

Lane `b135read`, plan row [B135] step (c). Window: `/var/tmp/b135win/chain.log`, 2026-10-10
12:13:19 to 19:19:56 EDT (`CHAIN_DONE suite_rc=0`), master 3e934be; 26/26 cells `measured` at attempt 1
(5 sentinel + 4 capability + 4 loglines + 4 email + 4 litrun + 5 sentinel:end), ABBA within a set
(`pcrec-auto@a15fb77b`, `pcrec-auto`, `pcrec-nocaps`, `pcrec-nocaps@a15fb77b`), ONE driver build for both pins.
~/pcrec was not touched; nothing was timed by this lane. Sources, all archived under
`docs/dev/measurements/` with source headers:

- `2026-10-10-b135-instrument-ab.txt` (the [B133] A/B), `-sentinel-open-end.txt`, `-acceptance.txt`,
  `-movers.txt`; scripts `2026-10-10-b135-sentinel-open-end.py`, `2026-10-10-b135-states12-analysis.py`.
- Reports `reports/2026-10-10-{capability-0.2,loglines-0.1,email-specimen-0.2,litrun-0.1}-budu-ryzen1600-revend-7388f1c0.*`
  (reporter v25; set grain tsv/md/matrix, subject-grain slice tsv + md, interpretation sidecars).
- Predictions: pcrec inbox I-142 s1 (scored in section 3 by hand; no machine-readable predictions TSV was authored).

Numbers are medians over 5 trials of the per-call (or per-set-sum) ns; "(min-max)" is the trial range. Ratios
are computed from those medians and marked as computed.

## 0. Four cautions, stated once

1. **Both pins ran in ONE window**, so a15fb77b -> 7388f1c0 is a same-window pair. It says nothing about
   cross-window stability; state 3 (b8337c33) is the owed cross-window control (I-142 s2).
2. **The reporter's "previous version" is chosen by RECORD TIMESTAMP, not pin order.** ABBA put the nocaps
   a15fb77b record (19:50Z) AFTER the nocaps 7388f1c0 record (18:58Z), so for `auto-nocaps` the reporter's
   R8 column, the D119 bar and the null band pair the testees BACKWARDS: the nocaps tail rows read
   "slower x71154.35" on the a15fb77b (BEFORE) row (`reports/...capability...revend...tsv`, column
   `delta_verdict`), where caps reads "faster x27037.25" on the 7388f1c0 row. The null-band header names
   both directions (`pcrec 7388f1c0 -> a15fb77b` and `pcrec a15fb77b -> 7388f1c0`). The medians are right; only the
   Δ column's direction and the sidecars' R-DELTA rows for nocaps are inverted. KB candidate (section 6);
   every ratio in THIS ledger is computed from medians directly. The trend report orders by `[[pin_order]]`
   and is not affected.
3. **Plain-form timing rows only in the acceptance table** (`large-subject-throughput`, `short-subject-search`
   plain). 285 of 297 rev-end census rows are whole-subject (`match-compliance`) forms, which the capability
   set does not time (email and litrun do).
4. The acceptance cells are per-subject medians (`reduce_match_cell`), not set sums; movers are set cells
   (`reduce_set_cell`), both the reporter's own arithmetic.

## 1. The [B133] instrument A/B -- did the driver change timing?

`scripts/instrument_ab.sh 2eb8938 /var/tmp/b135win/ab`, 25 cells x A/B/A/B, scratch tier, core 11, 12:13-12:48 EDT.

**The A/B was NOT a same-pin test.** The script's header says both trees "read testees/pcrec/configs.toml's
pin"; 2eb8938 predates the b135prep re-pin, so BEFORE built and ran pcrec at **255bcdd8**
(`pcrec_255bcdd8_auto-*` in `store-BEFORE*`) and AFTER at **7388f1c0** (`store-AFTER*`). For every pcrec cell
the ratio is driver x pin. The brief's "both at pin 7388f1c0" does not match the stores.

What can be said:

- `timed.c` / `timed.h` are byte-identical between 2eb8938 and 17cb77d (`git diff` empty); `driver.c` +12 and
  `shim.c` +28 lines are the `simd_guarded_bytes` info reader, off the timed path. The isolation is structural
  (b135prep's object-level proof, 7 identical / 0 differs).
- **pcre2-jit, the only pcrec-free rows, is flat:** 5 cells, AFTER/BEFORE geomean-of-reps min 0.982, median 0.998,
  max 1.014 (the ten AFTER/BEFORE rep ratios span 0.945-1.031, all with overlapping trial ranges; the one disjoint pair in the jit rows is a BEFORE2/BEFORE1 drift, winpath 0.970).
  This is the clean driver reading: no driver effect on pcre2.
- pcrec cells: median 0.985 (auto) / 1.004 (nocaps), range 0.665-1.047. The 0.665 / 0.669 cell is
  `wild-semdiv-dollar-trailing-newline-pcre2` (968 -> 643 ns), which is [OPT-REVEND] itself (rev-end stamp, section 4).
  The cells at 0.91-0.92 (`winpath-near-miss`: 500 -> 455 ns) and 1.04-1.05 (`numeric-id-nested-plus`,
  `phone-list-nested-plus`, `trim-nested-star` nocaps) are driver x pin and cannot be split here. For
  `winpath-near-miss` the pinned sentinel reads 455.0 (a15fb77b) and 459.8 / 454.7 (7388f1c0), so the 455 level
  holds at both window pins; the 500 level is 2eb8938 at 255bcdd8 (and 501.6 in the 2026-10-09 A/B at 255bcdd8 with the
  isolated driver). The trend report flags the 255bcdd8 -> a15fb77b pair `instrument_changed` (era) and shows
  `winpath-near-miss` 0.874 on a program-identical artifact, so the second step is either the abi 69-72
  text layout or the +28-line shim.c change; this A/B cannot tell which.
- **What matters for the window is unaffected:** both window states ran on ONE driver build (same `pcrec_driver`
  sha256 and mtime for `pcrec-auto@a15fb77b` and `pcrec-auto`, b135prep section 7), so the instrument term cancels in
  every a15fb77b -> 7388f1c0 ratio. The sentinel (section 2) is the check that it stayed still.
- **To resolve the pcrec half:** an A/B at one fixed pin (BEFORE tree 2eb8938 and AFTER tree 17cb77d both at 255bcdd8,
  or both at 7388f1c0). 17cb77d only honours `$PCRECBENCH_PCREC_PIN` for `also_pins`, so this needs 255bcdd8 added to
  `also_pins` for the run. OWED, manager's call; not needed for this window's verdict.
- Tooling note: `instrument_ab.sh` should print the two pins it resolved, or refuse when they differ.

## 2. The sentinels -- did the box and instrument hold?

`sentinel@0.1`, 15 patterns x 75 short subjects, set-grain sums, 5 trials. Open (12:49-13:22 EDT) vs end
(18:43-19:19 EDT), per testee, pinned tier (`2026-10-10-b135-sentinel-open-end.txt`):

| testee | cells | end/open min | median | max | disjoint trial ranges |
|---|---|---|---|---|---|
| pcrec 7388f1c0 auto-caps | 15 | 0.989 | 1.000 | 1.005 | 0 |
| pcrec 7388f1c0 auto-nocaps | 15 | 0.995 | 1.000 | 1.005 | 0 |
| pcrec a15fb77b auto-caps | 15 | 0.993 | 1.000 | 1.006 | 1 (`keyword-prefix-order` 0.993) |
| pcrec a15fb77b auto-nocaps | 15 | 0.990 | 1.001 | 1.006 | 1 (`floor-byte` 1.006) |
| pcre2-jit | 15 | 0.943 | 1.000 | 1.060 | 0 |

- pcrec is flat to <= 0.6% across 6.5 hours at BOTH pins, 60 cells, 2 disjoint-range exceptions both < 1%.
  pcre2-jit, the flat control, is flat inside its trial agreement (0.943-1.060, every pair overlapping; the three
  loudest, `router-prefix-order` 1.060, `wild-validator-us-zip-owasp` 1.057, `ipv4-near-miss` 0.943, are
  cells of ~3 us set-sum with one slow trial each).
- NOTES.md's reading: pcre2-jit flat AND pcrec flat -> "Sentinel flat across windows -> a pcrec Delta on other short
  cells of the same window is the engine's (the instrument demonstrably did not move)." The steps that need a PREVIOUS
  window's sentinel (step 1) cannot run: **this is the first window with a sentinel**; the cross-window half
  waits for state 3.
- The "VERDICT: NOT QUIET" print at the email set's start (17:15:36 EDT,
  right after the sidecar regeneration process) did not touch a cell: that cell's own pre-flight passed
  (`load1 0.71 occupancy pass`, attempt 1) and the record is `measured`. Worst other-core busy in the reports:
  capability 18.92%, loglines 20.7%, litrun 9.49%, email 2.53% (report headers, `worst_other_core_busy`), all
  below the gate's own thresholds as judged per cell.
- **Verdict: the window is clean by the sentinel's own reading** (instrument and box held, open vs end, at both pins).

## 3. THE ACCEPTANCE TABLE -- I-142 s1's 15 tail cells + `\s+$` x t-trim-nearmiss-16k

Predicted ns per call (rev-end) from I-142: no-match cells 7-24; `\w+\z` x t-tail-txt and `\s+$` x t-tail-space
13-42; `\d+$` and `\w+\z` x t-tail-digits 19-60; `[a-z]+\.txt$` x t-tail-txt 22-66; `.*\.txt$` x t-tail-txt 33-98;
`\s+$` x t-trim-nearmiss-16k 7-24. Predicted ratio = (a15fb77b median) / (predicted high .. low), computed. The
class of each cell (which subject matches) is my assignment from I-142's step counts. Measured: pinned records,
per-subject median (min-max over 5 trials). a15fb77b column: auto-caps median. Full output incl. nocaps and the stamps:
`docs/dev/measurements/2026-10-10-b135-acceptance.txt`.

| pattern | subject | predicted ns | auto-caps 7388f1c0 median (min-max) | auto-nocaps | auto-caps a15fb77b | ratio caps / nocaps | predicted ratio | verdict |
|---|---|---|---|---|---|---|---|---|
| `tail-digits-eol` | t-tail-digits-1m | 19-60 | 28.36 (26.03-28.69) | 26.91 (26.86-27.88) | 741,585 | x26,148 / x27,467 | x12,360-x39,031 | inside |
| `tail-digits-eol` | t-tail-txt-1m | 7-24 | 7.97 (7.97-7.98) | 7.97 (7.97-9.74) | 745,618 | x93,529 / x92,933 | x31,067-x106,517 | inside |
| `tail-digits-eol` | t-tail-space-1m | 7-24 | 7.97 (7.97-7.98) | 7.97 (7.97-9.74) | 737,872 | x92,567 / x92,721 | x30,745-x105,410 | inside |
| `tail-word-eoz` | t-tail-digits-1m | 19-60 | 23.48 (23.44-23.66) | 23.75 (23.41-25.11) | 2,252,351 | x95,928 / x94,814 | x37,539-x118,545 | inside |
| `tail-word-eoz` | t-tail-txt-1m | 13-42 | 21.55 (21.55-21.59) | 21.58 (21.55-21.81) | 2,245,460 | x104,186 / x102,707 | x53,463-x172,728 | inside |
| `tail-word-eoz` | t-tail-space-1m | 7-24 | 7.96 (6.59-8.92) | 7.87 (6.49-8.60) | 2,193,391 | x275,402 / x281,224 | x91,391-x313,342 | inside |
| `tail-space-eol` | t-tail-digits-1m | 7-24 | 8.80 (8.57-9.96) | 9.97 (8.57-10.04) | 1,775,444 | x201,781 / x178,174 | x73,977-x253,635 | inside |
| `tail-space-eol` | t-tail-txt-1m | 7-24 | 8.76 (8.56-10.02) | 8.76 (8.59-9.97) | 1,777,632 | x202,887 / x202,954 | x74,068-x253,947 | inside |
| `tail-space-eol` | t-tail-space-1m | 13-42 | 28.36 (27.59-29.64) | 29.05 (27.72-30.15) | 1,778,312 | x62,710 / x61,227 | x42,341-x136,793 | inside |
| `tail-ext-lower-txt` | t-tail-digits-1m | 7-24 | 8.56 (8.56-8.58) | 8.57 (8.56-8.72) | 2,891,848 | x337,855 / x337,821 | x120,494-x413,121 | inside |
| `tail-ext-lower-txt` | t-tail-txt-1m | 22-66 | 32.92 (32.87-33.02) | 33.02 (32.90-33.45) | 2,892,308 | x87,848 / x87,618 | x43,823-x131,469 | inside |
| `tail-ext-lower-txt` | t-tail-space-1m | 7-24 | 8.56 (8.56-8.58) | 8.56 (8.56-8.68) | 2,892,036 | x337,849 / x337,939 | x120,501-x413,148 | inside |
| `tail-dotstar-txt` | t-tail-digits-1m | 7-24 | 9.54 (9.35-10.35) | 9.34 (9.30-10.55) | 210,012 | x22,018 / x22,490 | x8,751-x30,002 | inside |
| `tail-dotstar-txt` | t-tail-txt-1m | 33-98 | 39.73 (39.31-40.80) | 40.74 (39.57-42.31) | 209,939 | x5,284 / x5,158 | x2,142-x6,362 | inside |
| `tail-dotstar-txt` | t-tail-space-1m | 7-24 | 9.34 (9.32-9.94) | 9.35 (9.30-10.50) | 209,972 | x22,482 / x22,479 | x8,749-x29,996 | inside |
| `tail-space-eol` | t-trim-nearmiss-16k | 7-24 | 10.02 (8.78-10.12) | 9.93 (8.78-10.43) | 29,052 | x2,898 / x2,932 | x1,211-x4,150 | inside |

**Verdict: 32 of 32 cells (16 x caps, nocaps) INSIDE the predicted ns range and inside the predicted ratio range.** Measured
ratios x2,898 (`\s+$` x trim, caps) to x337,939 (`[a-z]+\.txt$` x digits, nocaps); I-142's overall range was
2,100x-420,000x on the 1 MiB cells and 1,200x-4,300x on the trim cell. a15fb77b's own medians reproduce O-91 (c)'s
values (737-746 us, 1.78 ms, 2.25 ms, 2.89 ms, 210 us at 1 MiB), so the BEFORE is the O-91 BEFORE.

**Failure signatures, applied:**

1. ">150 ns or varying with body size = rev-end did not run": NOT fired. The largest 1 MiB cell is 40.74 ns
   (`.*\.txt$` x txt, nocaps), the largest anywhere in the table 40.74; No cell varies with BODY SIZE: the same pattern on t-64k / t-256k / t-1m
   (B, caps): `\w+\z` 6.6 / 6.7 / 6.6, `[a-z]+\.txt$` 10.6 / 10.6 / 10.6, `.*\.txt$` 13.3 / 13.3 / 13.3, `\s+$`
   32.0 / 31.1 / 30.7 ns. `\d+$` reads 11.8 / 12.2 / 30.5 because t-1m ends in two digits (`...systemd[20\n`) where t-64k and
   t-256k end in letters: the tail content, not the length (a 16x length change moves no other pattern). The a15fb77b
   column scales with length on the same bodies (`\d+$` 65,357 / 277,349 / 1,115,723).
2. "a short cell at 40-60 ns with flat sentinels is the instrument": NOT fired as stated. The one cell in 40-60 ns
   is `.*\.txt$` x t-tail-txt-1m (39.73 caps, 40.74 nocaps; nocaps is the 40.74), which is a MATCHING cell with
   predicted range 33-98; the short no-match cells (7-24) read 7.9-10.0. Sentinels flat (section 2).

Where in the range: all 9 no-match cells sit at 7.96-9.97 ns (the lower third of 7-24), the 6 matching cells at
21.6-40.7, `.*\.txt$` x txt (39.7 / 40.7) near the bottom of its 33-98 band; nothing is near an upper edge. The cheapest
body-size-check cells are 6.6 ns (`\w+\z` on t-64k..t-1m) against I-142's 5.6 ns call floor plus at least one step.

Stamps (both configs): every tail pattern `engine=dfa, sel=selected, dfa_scan=rev-end, dfa_start=reverse-pass,
prefilter=none, match=unwrapped` at 7388f1c0 (a15fb77b: `unanchored`, `byte-class-bounded`; `memchr-bounded` for
`.*\.txt$`); caps and nocaps differ only in `.flags`. `req_why`: **`dominated` on the two `.txt` patterns, `none` on
the other three** (I-142 omitted it; `memfn_libc memchr,memcmp -> none` with it). emit_bytes 72 -> 73: 25,328 -> 20,619 (`\d+$`),
32,145 -> 23,624, 26,791 -> 22,483, 26,223 -> 20,607, 29,993 -> 23,808 (-17.5% .. -27%).

## 4. Movers outside the tail family (set cells, all four sets, caps and nocaps)

`2026-10-10-b135-movers.txt`: 424 (set, config, pattern, regime, form) cells, 422 with numbers (2 are
`email-nested-plus` x throughput: pass-rate 0.818 at BOTH pins, no number either side, unchanged). Program
identity (`program_sha256`) is the same at both pins on 356 cells and differs on 66; the 66 are exactly the cells whose
`dfa_scan` moves unanchored -> rev-end (33 per config), nothing else.

**Null band.** On the 356 program-identical cells, the ratio B/A is p5 0.995, median 1.000, p95 1.006; 26 have
disjoint trial ranges, 25 within +-5%. **One program-identical outlier: `wild-logparse-quotedstring-grok` x
short-subject-search, caps only, 2,122.7 -> 2,525.2 ns (x1.190, disjoint).** It is a VM artifact (`engine=vm`, `sel=selected`),
`program_sha256` and `emit_bytes` (64,131) and `vm_program_bytes` (17,340) identical at both pins. Per subject: 74 of 75
subjects slower by +1.5..+7.3 ns, none faster, an additive ~6.5 ns per call (e.g. `waf-dbnames` 37.7 -> 45.1, `lp-quoted`
74.9 -> 81.4); nocaps (same pattern) +0..+2.7 ns on 9 of 75. Cause unknown; the layout hypothesis (I-37 precedent,
`-falign-functions=64`) is a hypothesis only. The state-3 cross-window control re-measures it.

**Better (the rev-end population, 33 cells per config).**

| group | set cells | ratio B/A |
|---|---|---|
| the five tail patterns + `letters-bounded-tail-z`, large-subject | 6 per config | 0.0000-0.0757 |
| same, short-subject-search (set sums, 75 subjects) | 6 per config | 0.37-0.95 (`[a-z]+\.txt$` 0.945; `.*\.txt$` is slower, below) |
| `wild-semdiv-dollar-trailing-newline-pcre2` | large / short | 0.744 / 0.676 caps (0.747 / 0.683 nocaps) |
| litrun `ctrl-abc-dollar` | large / short | 0.661 / 0.632 caps (0.659 / 0.633 nocaps) |
| litrun whole-subject `lit-l31`, `lit-l40` | match-compliance | 0.975-0.982 |

**Worse -- beyond trial overlap (DISJ), each reproduced on both configs unless stated.**

| cell | A (a15fb77b) | B (7388f1c0) | B/A | stamps / reading |
|---|---|---|---|---|
| `tail-dotstar-txt` x short-subject-search (set sum, 75 subjects) | 644.2 caps / 641.6 nocaps | 738.1 / 737.4 | **1.146 / 1.149** | prefilter `memchr-bounded -> none`, `dfa_scan unanchored -> rev-end`. 66 of 75 short subjects slower by +5.5 ns each (3.8 -> 9.3 ns), 7 faster: the old `memchr` dismissal of subjects with no `.` was cheaper than the reverse walk's floor |
| litrun whole-subject `alt-foo-tails` (27 subjects) | 280.9 / 280.3 | 302.7 / 302.0 | **1.077 / 1.077** | rev-end, run-pinned-bounded -> none; mean +0.84 ns per call (subject range 9.3-18.0 ns), max +2.5 (`at-match-b2`) |
| litrun whole `wild-secrets-aws-access-key-id` nocaps | 293.6 | 307.7 | 1.048 | rev-end, first-memchr-bounded -> none |
| litrun whole `lit-l4`, `lit-l2` | 266.0 / 256.0 | 275.0 / 264.3 | 1.034 / 1.032 | mean +0.36 / +0.29 ns per call; same on nocaps |
| litrun whole `lit-l8`, `wild-secrets-github-pat` caps | 286.8 / 328.2 | 293.2 / 335.7 | 1.022 / 1.023 | same family |
| `wild-logparse-quotedstring-grok` short, caps | 2,122.7 | 2,525.2 | 1.190 | PROGRAM-IDENTICAL, above |
| `bracket-array-define` throughput nocaps | 296.2 | 304.9 | 1.029 | program-identical; trend band 0.0208; one cell |

Flat where predicted to be: loglines (22 cells, no rev-end in the search regime; every program identical, all within
0.3% except `hex32-id` 0.997), email (the three whole-subject forms are rev-end but read 1.000: 73,129.5 -> 73,125.9 ns
for `orig`, a whole-subject match has to read the whole subject in either direction -- a hypothesis, not a stamp), litrun long-literal rows. **Regressions flagged:** the
`.*\.txt$` short-regime row (+14.6%, +5.5 ns on 66 subjects), the litrun whole-subject family (+1.5..+7.7%,
sub-ns to +2.5 ns on ~10 ns calls, 8 patterns), and the program-identical `quotedstring-grok` (+19%).
The size of every one is a few ns per call on cells that do not exceed 2.6 us; none is a correctness change: 0 wrong answers and 0 give-ups on every ranked row of the four reports. The one excluded cell is
`email-nested-plus` x large-subject (pass-rate 0.8182, 0 wrong, 0 give-ups) at all four testees, the same at both pins.

## 5. Window facts the next reader needs

- Statuses: 16 pinned pcrec records + 10 sentinel records, all `measured`; `trial_agreement` `agree` on every record
  (nocaps capability 7388f1c0: 15 of 6018 rows flagged, 0 of 140 groups).
- Times per cell (log): capability 46-52 min, loglines 8.3-8.4, email 5.8, litrun 13.2-15.7, sentinel 5.1-6.2 per pcrec cell and 9.3-9.4 for
  pcre2-jit (~35 min per five-cell sentinel pass). The suite ran 12:48:31-19:19:56 (6h31); the A/B 12:13-12:48 (35 min).
- The census prediction held for the sets read: capability 48 dfa_scan unanchored -> rev-end compile rows per config (plain + whole forms), 38 `dfa_start reverse-pass -> attempt-start` (attempt/empty bodies, stamp relabel only, same
  timing), 1 `size-cap-retry -> selected` (`wild-logparse-syslogbase-expanded` whole form, +35,755 B); loglines 11, email 3, litrun 15 rev-end rows.

## 6. Findings pcrec did not predict, and tooling findings

1. **The `.*\.txt$` short-regime regression** (section 4): the reverse walk removes the `memchr` prefilter that dismissed
   most short subjects in 3.8 ns; the rev-end floor is 9.3 ns. The tail patterns' other short rows still win (0.37-0.50)
   because their old prefilter was a byte-class scan, not a `memchr`.
2. **litrun whole-subject rows get 1.5-7.7% slower** (sub-ns to +2.5 ns per call) where the old end window was a few bytes
   (`end_window 2..16 -> none`) and the subject short; longer literals (l31, l40) win 2%.
3. **Whole-subject forms are 285 of 297 rev-end census rows**, and email's whole-subject cells (~73 us) do not move: a
   full-subject match must walk the whole subject in either direction. REVEND's measured surface in this suite is the
   search regime of the tail family.
4. **One program-identical +19%**: `wild-logparse-quotedstring-grok` short, caps only.
5. **abi 72 mis-stamps** `dfa_start reverse-pass` on attempt/empty bodies (38 capability rows here, 74 in the census); abi 73 corrects it.
   `req_why` is `dominated` on the two `.txt` tails (I-142 omitted it); 81 census rows go `emitted -> dominated`.
6. **13 census rows go `size-cap-retry -> selected` and grow** (+36 KB..+460 KB; one capability row here); a set-grain mean over
   altwide/utf8 whole forms mixes REVEND with the restored prefilter. Not measured in this window (altwide, utf8 excluded).
7. **Reporter/tooling (ours):** (i) the R8 "previous version" is timestamp-ordered, which inverts nocaps under ABBA
   (section 0 item 2): KB candidate, fix = order by `[[pin_order]]` (needs the catalogue in the reporter) or by the pins' declared order;
   until then the nocaps `delta_verdict`, D119 bar and the nocaps R-DELTA sidecar rows are direction-inverted for this
   window. (ii) `instrument_ab.sh` does not pin the pcrec revision across its two trees (section 1).
   (iii) the window script's set-boundary `quiet` print said NOT QUIET with no reason line.

## 7. Candidates, in order

1. pcrec: the `.*\.txt$` short-regime cost (6.1 above) -- is there a cheap rev-end dismissal (a memchr on the last byte
   of the required run) for end-pinned patterns whose old route was `memchr-bounded`?
2. Ours: fix the reporter's cross-pin pair ordering before state 3 (it will be ABBA again) and re-render these four
   groups and sidecars; re-run the A/B at a fixed pin if the pcrec half matters.
3. State 3 (b8337c33) over the same cells with a15fb77b or 7388f1c0 repeated as the cross-window control; it also re-measures
   `quotedstring-grok` caps and the litrun whole-subject family.
