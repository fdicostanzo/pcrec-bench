# [REQ-HANDOFF-L1] ledger -- BASE b8337c33 (abi 74) vs NEW 00c97769 (abi 75) vs DENY (`-fno-req-handoff`) vs canonical 6b2dbd3e (abi 76)

Lane `b136read`, plan row [B136] (the READ). Window: `/var/tmp/pcrecbench/b136win/chain.log`, `CHAIN_START 2026-10-12T11:08:16 EDT` to the tier-4
`CHAIN_DONE 2026-10-13T07:55:57 EDT` (two chain launches: tiers 1+2 from 11:08, tiers 3+4 from 21:06; chain `docs/dev/lanes/b136_chain.sh`; records
committed 687c1f49 + 54b70304). 58 cells, every one `attempt 1 rc=0` (no quiet-gate refusal, no `inconclusive-spread`), the pcrec driver sha256
`2c5061115e52679d6e5a51e9d329e1c0edc943e038cf4ac2f6e161a6ce7b092d` identical at chain start and end. Nothing was timed by this lane; ~/pcrec untouched
(read-only: `build/pcrec-6b2dbd3e/docs/dev/{optloop,lanes}`, `src/findings/default.rxt`, the shared main-tree `bench/*/subjects`).

Inputs, all archived under `docs/dev/measurements/` (`2026-10-13-b136-*.txt`; one script, `2026-10-13-b136-analysis.py`, read-only over the records, arithmetic =
`pcrecbench.reduce`, the reporter's own):

- reports `reports/2026-10-13-{loglines-0.1,altwide-0.3,bounded-0.3,syntax-0.1,utf8-0.1,litrun-0.1,capability-0.2,email-specimen-0.2}-budu-ryzen1600-handoff-6b2dbd3e.*`
  (reporter **v26**, the first report carrying `prefilter=handoff` and its legend line; query `since=2026-10-12T00:00:00Z` + the window's testee ids, so every
  b8337c33 side is THIS window's record, never the 2026-10-11 one; 40 files + 8 sidecars; email-specimen holds only the two pcre2 peers, litrun only 6b2dbd3e
  x {caps, nocaps} x {rev-end, `-fno-rev-end`} + peers);
- the per-subject and set-grain numbers below come from the records directly.

Notation. Medians over 5 trials; `[min..max]` = trial range; "ov" = the two trial ranges overlap, "DISJ" = they do not; ratios are medians, X/Y = X's median over
Y's (<1 = X faster). B = BASE b8337c33, N = NEW 00c97769, D = DENY (`pcrec-auto-noreqhandoff` @ 00c97769), C = canonical 6b2dbd3e; all caps (`pcrec-auto`).
A set cell = the per-trial SUM over the regime's subjects of per-subject ns/call (never one call), then the median over trials. All pcrec numbers are
`pcrec-auto` caps unless a nocaps cell is named.

## 0. What the window could and could not see

1. The tier-2 and tier-3 sets ran pcrec 3-4 times each (B, N, D, C). **litrun** ran only C and its `-fno-rev-end` twin (caps + nocaps): there is no B/N cell
   for litrun, so nothing in this ledger says what L1 did to litrun (the census says 0 litrun movers). **capability** ran B, N, C (no D, and **caps only**: no nocaps
   record exists, so the 15th `handoff` mover, `wild-secrets-username-password-pair` under `--no-captures`, is not asserted by value from a record). **bounded**
   ran B, N, D but **no C** (tier 1 listed `$ABD`): `dotted4` has no 6b2dbd3e cell. **email-specimen** ran no pcrec cell (tier 4 is peers only).
2. **The utf8 DENY arm is empty.** `pcrec-auto-utf8-noreqhandoff` has 3 compiled patterns (`asr-b-ascii`, `ci-ascii-control`, `floor`) and 73 of 76 plain-form
   patterns `unsupported-by-declaration` ("REQUIRES utf8-encoding; pcrec-auto-utf8-noreqhandoff declares none of it"): `bench/utf8/gen_patterns.py`'s
   `EXT_BENCH_ROSTER` (line 433) never got a row for it (the [B136] prep added the roster row for capability, `bench/capability/gen_patterns.py:1171`, not utf8's).
   So there is **no `-fno-req-handoff` measurement of `ci-strasse`** -- the cell I-147 says gates pcrec's T5 work -- and the utf8 D side is 1,573 rows
   (the record is 4.6% of the size of B/N/C's 34,509). Owed: one roster row in `bench/utf8/gen_patterns.py` and a one-cell re-run.
3. **Subject trees.** The landmark densities (section 5) read the generated subject trees of the MAIN tree (`/home/duxevents/pcrec-bench/bench/*/{subjects,throughput}`),
   not store records; their sha256 was not re-checked here (the harness checks it at every run).
4. Verdict lines below say what was read AND what was not. "Not read" items are collected in section 15.

## 1. Sentinels -- did the box and the instrument hold? (ask 7.4's per-window half)

`sentinel@0.1`, 15 patterns x 75 short subjects, set-grain sums, passes at open 15:09Z (11:09 EDT), end1 20:24Z, end2 00:30Z, end3 05:42Z; testees B, N, C (caps),
C nocaps, pcre2-jit; `2026-10-13-b136-sentinel.txt`. Ratios over the 15 cells (min / median / max, DISJ):

| testee | end1/open | end2/open | end3/open |
|---|---|---|---|
| pcrec b8337c33 caps | 0.996 / 1.001 / 1.006, 0 | 0.997 / 1.000 / 1.012, 0 | 0.983 / 1.000 / 1.003, 0 |
| pcrec 00c97769 caps | 0.978 / 1.001 / 1.005, 0 | 0.994 / 1.000 / 1.007, 0 | 0.995 / 1.001 / 1.011, 1 |
| pcrec 6b2dbd3e caps | 0.990 / 0.999 / 1.004, 1 | 0.993 / 1.000 / 1.004, 0 | 0.989 / 1.000 / 1.003, 0 |
| pcrec 6b2dbd3e nocaps | 0.990 / 1.000 / 1.006, 0 | 0.993 / 1.000 / 1.007, 1 | 0.994 / 1.000 / 1.008, 0 |
| pcre2-jit | 0.944 / 0.998 / 1.025, 0 | 0.933 / 1.001 / 1.061, 0 | 0.939 / 0.998 / 1.049, 0 |

The three pcrec pins against each other in the same pass (the sentinel patterns are program-identical): 6b2dbd3e/b8337c33 0.989-1.016 per cell, median 1.000-1.001 at all
four passes; 00c97769/b8337c33 0.976-1.015, median 0.999-1.001. **Verdict: the window is CLEAN** (pcrec per-cell ratios 0.976-1.016 over 21 h; 9 disjoint-range cells among the 480 pcrec cell comparisons above, none beyond 1.6%; jit per-cell 0.892-1.124, medians 0.997-1.003). Not read: the box's per-core occupancy (the records' `occupancy`), only the sentinel's own ratios.

## 2. Cross-window control -- b8337c33 here vs b8337c33 on 2026-10-11 (same testee id, caps)

`2026-10-13-b136-control.txt`, set cells of the six sets that have both: loglines 22, altwide 107, bounded 126, syntax 243, utf8 138, capability 137 = **773 cells**:
min 0.942, p5 0.992, p25 0.999, **median 1.000**, p75 1.001, p95 1.007, max 1.049; 35 disjoint-range cells (altwide 2, bounded 4, syntax 8, utf8 8, capability 13), 3 outside +-5%
(bounded `dig-exact-32` whole 0.942 and `dig-exact-16` whole 0.946, `line-80` whole 1.049; syntax `bak-2` short 0.947, all overlapping), 0 outside +-10%. That is the drift every
number below is read against: **+-0.7% (p5-p95)**, and the pcrec numbers of this window need no other correction. The gap report's pcrec side (b8337c33, 2026-10-11) is the same
instrument (its 30 trailing cells move 0.947-1.005 here, median 1.000: section 11).

## 3. (a) I-147 section 2's table, cell by cell

Set-cell medians, ns [min..max], this window (`2026-10-13-b136-table.txt`). N/B = NEW over BASE, D/B = DENY over BASE; "pred" = I-147 section 2 (scratch tier, Zen 4, memchr gate).

| cell | B | N | D | C | N/B | pred | D/B | pred | stamp B>N |
|---|---|---|---|---|---|---|---|---|---|
| loglines/ipv6 throughput | 10,621,376 | 2,286,719 | 10,585,396 | 2,287,114 | **0.215** DISJ | 0.305 | 0.997 | 1.000 | byte-class > handoff, K none>4 |
| loglines/ipv6 search_short | 259,217 | 71,823 | 260,112 | 71,822 | **0.277** DISJ | 0.325 | 1.003 | - | same |
| loglines/ipv4 throughput | 6,949,695 | 1,369,742 | 6,956,341 | 1,370,363 | **0.197** DISJ | 0.196 | 1.001 | 0.996 | byte-class > handoff, K none>3 |
| loglines/ipv4 search_short | 207,981 | 41,604 | 207,228 | 41,611 | **0.200** DISJ | 0.315 | 0.996 | - | same |
| altwide/sfx-64 throughput | 2,806,165 | 314,634 | 3,199,424 | 314,505 | **0.112** DISJ | 0.068 | 1.140 | 1.166 | byte-class > handoff, K 9>9 |
| altwide/sfx-256 throughput | 2,621,186 | 314,874 | 2,950,746 | 314,989 | 0.120 DISJ | (moves) | 1.126 | - | same |
| altwide/sfx-512 throughput | 1,867,037 | 315,373 | 3,253,850 | 315,660 | 0.169 DISJ | (moves) | 1.743 | - | same |
| loglines/kv-quoted throughput | 202,786 | 207,578 | 3,371,678 | 206,593 | **1.024** DISJ | 1.007 | **16.63** | 13.78 | first-class-bounded > handoff, K 32>32 |
| loglines/kv-quoted search_short | 5,698 | 5,898 | 11,774 | 5,897 | **1.035** DISJ | - | 2.066 | - | same |
| bounded/dotted4 throughput | 1,662.4 | 1,666.2 | 1,664.0 | - | 1.002 ov | 1.003 | 1.001 | 1.000 | byte-class > handoff, K none>3 |
| bounded/dotted4 search_short | 1,162.5 | 617.0 | 1,163.2 | - | **0.531** DISJ | 0.841 | 1.001 | - | same |
| altwide/sfx-64 search_short | 1,016.1 | 1,048.7 | 1,175.8 | 1,048.5 | 1.032 DISJ | - | 1.157 | - | same |
| hostile `a.{1,50000}z` throughput | -- | -- | -- | -- | -- | 1.000 | -- | 1.001 | **not in the bench** (grep of `bench/*/patterns/` for `50000`: no hit) |

Readings. (1) **Direction: all seven predicted-faster cells are faster beyond overlap and by MORE than predicted on ipv6 (x0.215 vs 0.305, search_short x0.277 vs 0.325), ipv4 search_short
(x0.200 vs 0.315) and dotted4 search_short (x0.531 vs 0.841); ipv4 throughput matches (0.197 vs 0.196). sfx-64 throughput is the one cell that falls short: x0.112 measured vs 0.068
predicted (the prediction was 1.65x better than this box shows); sfx-256/512 move x0.120/0.169.** (2) **D/B reproduces**: the no-handoff arm is 1.000 +-0.4% on ipv6, ipv4, dotted4, i.e.
`-fno-req-handoff` is the BASE program for the six new-K patterns; and x16.63 on kv-quoted throughput (pred 13.78), x1.140 on sfx-64 (pred 1.166), x1.743 on sfx-512 -- the K82 entry handoff that
the deny also removes. (3) **kv-quoted: the re-entry costs +2.4% throughput (DISJ) and +3.5% search_short (DISJ) here, against a predicted +0.7%.** (4) dotted4 throughput 1.002 ov, as predicted (its text has no `.`).
(5) The canonical column: C/N is 0.995-1.002 on every row (seam changes no handoff cell).

**Smoke set (all `REQ_HANDOFF != none` cells, N vs B, `2026-10-13-b136-smoke.txt`).** 96 cells read (48 patterns x tp/ss; 14 movers = 28 cells + 68 K-only cells).
Movers: 16 faster beyond overlap, 11 slower beyond overlap, 1 overlap. **Answers**: the cells with a failing subject or no number are the SAME 6 set cells at B, N, D and C and in the
2026-10-11 BASE record (syntax: `asr-k-uc` whole `f-kv` wrong, `rec-r-uc` whole `f-parens` wrong, `rec-1`/`rec-name`/`rec-r-uc` throughput `t-64k`/`t-256k`/`t-1m` gave up
`PCREC_ERR_FRAMES`; capability: `email-nested-plus` throughput, 2 of 11 subjects) -- `2026-10-13-b136-answers.txt`; 97,378 subject cells, no new wrong or gave-up subject at N, D or C.
**Cells more than +3% slower than BASE with REQ_HANDOFF set (the bound pcrec asked for): 7 of 96**, all handoff movers:

| cell | N/B | K | note |
|---|---|---|---|
| syntax/mod-r short | **1.076** DISJ | 0 | run `CAT` caseless @0; B 628.9 > N 676.7 |
| syntax/mod-i short | **1.069** DISJ | 0 | same shape; B 630.1 > N 673.8 |
| loglines/kv-quoted short | **1.035** DISJ | 32 | the K=32 run `="` |
| syntax/mod-r throughput | **1.033** DISJ | 0 | 3 landmark-ABSENT subjects, x1.031-1.036 |
| altwide/sfx-64 short | **1.032** DISJ | 9 | |
| altwide/sfx-256 short | **1.031** DISJ | 9 | (sfx-512 short 1.021, under the bound) |
| syntax/mod-i throughput | **1.031** DISJ | 0 | |

The other 68 K-set cells (prefilter unchanged: `stack-frame`, `mod-s`, `anc-m-*`, the utf8 `asr-*`/`lit-*`, capability `github-pat`/`slack-webhook`/`username-password-pair`, ...) are
**0.994-1.007** except `grp-atomic-alt` (the VM hybrid that gained K 2: **x0.926 throughput, x0.814 search_short**, faster). **K105's colon-dense caveat**: the shape
`[a-y]\d{0,N}:` does not exist in the bench (grep of `bench/*/patterns/` finds none), so the x1.13 / x1.50 hcolon cells are **not exercised**; ipv6 is the colon-dense cell the bench has and
it is x0.215-0.277.

Not read: the nocaps arm of any mover (no nocaps record except litrun and the sentinel), the DENY arm of utf8 (section 0.2) and capability, and `bench/*` patterns containing `.{1,50000}`-style hostile shapes (none).

## 4. (b) The `handoff` movers by value (`2026-10-13-b136-movers.txt`)

Plain-form patterns whose compile row stamps `dfa_prefilter=handoff` at N (and at C where a C record exists), with the stamp at B and at D:

| set | patterns (N = C = handoff; B shown) | K | D |
|---|---|---|---|
| loglines | `ipv4` (byte-class), `ipv6` (byte-class), `kv-quoted` (first-class-bounded) | 3, 4, 32 | byte-class, byte-class, first-class-bounded (K none for ipv4/ipv6; K none for kv-quoted too: the K82 handoff is gone) |
| altwide | `sfx-64`, `sfx-256`, `sfx-512` (byte-class) | 9 (B and N) | byte-class, K none |
| bounded | `dotted4` (byte-class) | 3 | byte-class, K none (no C record) |
| syntax | `cls-fold-pair`, `cls-pair-ctl` (memchr), `mod-i`, `mod-r` (byte-class), `qnt-poss-brace` (memchr) | 0, 0, 0, 0, 2 | memchr / byte-class (K none) |
| utf8 | `ci-ascii-control` (byte-class, K 0), `ci-strasse` (byte-class, K 2) | 0, 2 | `ci-ascii-control` byte-class; `ci-strasse` **no D record** (section 0.2) |

**14 patterns -- I-147's list exactly**, by value from records; 0 whole-subject rows stamp `handoff` anywhere (6 sets). K-only patterns that KEEP their prefilter:
`syntax/grp-atomic-alt` (K 2, memchr, a VM artifact -- the ENTRY generalization only). `utf8/cls-s-ucp` (I-147's K "4") is **`unsupported-by-declaration` on `pcrec-auto-utf8`** (UCP), so no
record carries it; it is asserted only by the b136prep compile census. The 15th mover (nocaps-only `wild-secrets-username-password-pair`) is not in any record (section 0.1).

## 5. (c) Ask 2 -- is there a byte landmark DENSER than the default prior predicts?

Method (`2026-10-13-b136-landmark.txt`, read-only): the landmark is the compile row's `req_run` (all bytes, with its caseless mask) or `req_byte`; the prior's hit rate is the product of each position's
mass in `src/findings/default.rxt` (6b2dbd3e, parts per million, sums to 1e6; for a run the independent-byte product, pcrec's own `req_landmark_hit_ppm` model); the observed density is
occurrences x run length / subject length over every subject of the set's manifests. "Denser" = observed > prior.

**Yes -- every mover has subjects denser than the prior, from 1 of 98 to 124 of 124.** Whether the density COSTS is a separate question; per-subject N/B of the densest and the slowest subjects:

| pattern | landmark | prior hit rate (1/h) | subjects denser than prior | densest observed | worst per-subject N/B (subject, base ns > new ns) |
|---|---|---|---|---|---|
| loglines/ipv6 | `:` (K 4) | 0.00665 (150 B) | **124 of 124** | 0.052 (x7.8) | **0.696** -- the slowest subject is still faster; all 124 faster beyond overlap |
| loglines/ipv4 | `.` (K 3) | 0.00997 (100 B) | 118 of 124 | 0.053 (x5.3) | 1.077 (`s-027`, 46.4>50.0), 1.070 (`s-010`, 53.2>57.0); 122 of 124 faster |
| loglines/kv-quoted | run `="`@1 (K 32) | 1e-5 (90,561 B) | 12 of 124 | 0.012 (x1,088) | **1.287** (`s-042`, 87.9>113.1); the 8 dense short subjects x1.09-1.29, the 4 dense throughput `-hit` subjects x1.033-1.040 -- all 12 slower |
| bounded/dotted4 | `.` (K 3) | 0.00997 (100 B) | 7 of 54 | 0.231 (x23) | 1.103 (`l-01`, 8.6>9.4 ov), 1.070 (`f-quad-3`, 20.9>22.4) |
| altwide/sfx-64 | run `ing`@2 (K 9) | 3e-5 (36,217 B) | 6 of 44 | 0.333 (`f-sfx`, x12,072) | 1.111 (`f-pfx3`), 1.105 (`f-sfx`, 42.1>46.5); the dense 128 KB throughput subject x0.113 |
| altwide/sfx-256, sfx-512 | same run | same | 6 of 44 | same | 1.103 / 1.107 (`f-sfx`); sfx-512's dense 128 KB subject **x0.791** (its siblings x0.113/0.121) |
| syntax/cls-fold-pair | run `cAt` caseless | 7e-5 | 8 of 45 | 1.0 (`f-cat`) | 1.289 (`f-num`, 3.8>4.9, a 3.8 ns call) |
| syntax/cls-pair-ctl | run `cat` caseless | 8e-5 | 8 of 45 | 1.0 | 1.052 (`f-ac`, 3.8>4.0) |
| syntax/mod-i, mod-r | run `CAT` caseless (K 0) | 8e-5 (12,524 B) | 10 of 45 | 1.0 (`f-cat-uc`) | 1.163 (`mod-r l-dup`, 22.6>26.3); x1.12-1.16 on the ten dense f-* subjects, **x1.031-1.036 on the three landmark-absent throughput subjects** |
| syntax/qnt-poss-brace | `b` (K 2) | 0.00989 (101 B) | 15 of 45 | 0.50 (`f-abba`, x50.6) | **2.397** (`f-tag`, 12.4>29.7; density 0.273, x27.6), 1.312 (`l-parens`, 13.9>18.2), 1.143 (`l-tags`) |
| utf8/ci-ascii-control | run `ABC`@2 caseless (K 0) | 1.3e-5 | 7 of 98 | 1.0 (`prp-*` 3-4 B subjects) | 1.095 (`prp-l-anchored-miss`, 21.1>23.2); the 64 KB subjects 0.994-1.010 |
| utf8/ci-strasse | run `TRA`@2 caseless (K 2) | 1.7e-4 (5,816 B) | 10 of 98 | 0.429 (`ci-strasse-nearmiss`, x2,493) | **1.270** (`lit-sharps-miss`, 24.1>30.6), 1.234 (`ci-strasse-nearmiss`); the 64 KB subjects 0.982-0.999 |

Across all 976 (pattern, subject) cells of the 14 movers (`2026-10-13-b136-subject-extremes.txt`): 436 faster beyond overlap, 309 slower beyond overlap, **37 at x1.10 or more, 5 at x1.25 or more,
ONE at x1.50 or more** (`syntax/qnt-poss-brace` search_short `f-tag`, x2.397, a 11-byte subject, +17.3 ns). **That one is the x1.5 case I-147 ask 2 describes** (an admitted re-entry meeting a landmark 27x denser
than the prior) -- and it is invisible at set grain, where `qnt-poss-brace` is x0.298 (throughput) and x0.800 (short). Readings: (1) the x1.5-class cost exists on tiny dense subjects but is **bounded by absolute size**
(+1 to +17 ns on 4-100 ns calls); on every LARGE subject the two regimes' dense cells (ipv6/ipv4 throughput, sfx dense, ci-strasse 64 KB) are faster or flat. (2) mod-i / mod-r are not a density effect:
their throughput subjects carry **zero** occurrences of the landmark and still read x1.031-1.036 -- the byte-class scan the handoff displaced is simply faster than the re-entered run test for a 3-byte caseless run at
K 0. (3) kv-quoted is the density-sensitive one: its 12 dense subjects (8 short x1.09-1.29, 4 throughput x1.033-1.040) are every one slower, which is what carries the set cells to +3.5% / +2.4%.

Not read: a timed sweep of landmark density (the bench has no such axis); the independent-byte product for runs is pcrec's own model, not a measured byte-pair frequency.

## 6. (d) Ask 3 -- a measured gap to a reverse-inner start (kv-quoted)

`2026-10-13-b136-kv.txt`. A reverse-inner start exists in **no** pcrec build and no bench testee, so a direct N-vs-reverse-inner gap cannot be measured here; its -8.7% on kv-quoted is et1twin's scratch figure
(`rlhtwin_report.md`). What the bench measures is the distance the re-entered handoff leaves to the fastest peer that has such a start (rust's regex does):

- kv-quoted throughput: B 202,786, N 207,578 (**+2.4% vs B**, DISJ), C 206,593; rust (2026-09-20 record, cross-window) 210,693 -> N/rust 0.985; short: B 5,698, N 5,898 (+3.5%), rust 9,142 -> N/rust 0.645.
- per throughput subject N/B: the `t-*-hit` subjects x1.033-1.040 (`t-256k-hit` 25,331>26,340), the fail and syslog subjects 0.995-1.003. N/rust on the hit subjects: 0.852 (`t-016k-hit`), 1.016 (`t-064k-hit`), 1.105 (`t-256k-hit`), **1.147** (`t-1024k-hit`);
  on the fail/syslog subjects N is 0.47-0.94 of rust except `t-1024k-fail` 1.003.
- pcre2-jit 14,983,129 / interp 66,575,548 on the same cell (this window): pcrec is x72 / x321 faster.

**Reading**: the re-entry leaves a measured **+2.4-4.0% cost on the matching subjects relative to the pre-L1 entry-only handoff**, and on the large matching subjects (256 KB, 1 MB) N is **x1.10-1.15 behind rust's
cross-window number** -- the standing candidate for "a cell where the re-entered handoff leaves a gap". It is a cross-window and cross-engine number; the bound on a real reverse-inner start is not measured. Not read: any
rust re-measure this window.

## 7. (e) Ask 4 -- litrun same-pin `-fno-rev-end` vs rev-end at 6b2dbd3e (rewtwin's box-vs-pin question)

`2026-10-13-b136-litrun.txt`: litrun@0.1 x {pcrec-auto, pcrec-nocaps} x {rev-end, `-fno-rev-end`} at 6b2dbd3e, 14 patterns (27 subjects each: a **cell is the SUM over 27 subjects of per-subject ns/call**, so the
answer to "is it ONE `rx_search` per subject or the cell total" is: one call per subject per trial, summed over the 27; same for the search-short regime).

**The O-96 (c)2 cells are the WHOLE form, regime `match-compliance`** (`(?:P)\z`; rev-end changes `dfa_scan` unanchored>`rev-end` and `dfa_start` to `reverse-pass` there; the plain form is program-identical with or
without the flag). Whole-form, rev-end / `-fno-rev-end` (caps | nocaps):

| pattern | caps | nocaps |
|---|---|---|
| alt-foo-tails | **1.079** DISJ (302.9 / 280.7) | **1.078** DISJ |
| ctrl-abc-dollar (`abc$`) | 1.028 DISJ | 1.027 DISJ |
| lit-l2 / lit-l4 / lit-l40 | 0.999 / 1.002 / 1.003 | 1.000 / 1.002 / 1.006 |
| lit-l3 | 1.023 DISJ | 1.027 DISJ |
| lit-l7 / lit-l8 | 1.024 / 1.023 DISJ | 1.021 / 1.024 DISJ |
| lit-l10 / lit-l16 | 1.008 / 1.007 DISJ | 1.007 / 1.007 DISJ |
| lit-l31 | 1.018 DISJ | 1.018 DISJ |
| aws-access-key-id | 1.000 ov | 1.041 ov |
| github-pat | 1.018 DISJ (VM hybrid) | 1.001 ov |

Distribution over the 14 whole-form cells: caps median **1.013** (min 0.999, p95 1.046, max 1.079); nocaps median **1.012** (1.000-1.078). **The +2..8% reproduces at the SAME pin on this box** (rev-end is slower by the same
amounts that O-96 read between two pins), so the cause is **the box (Zen 1), not the a15fb77b-vs-7388f1c0 comparison**. It is a small fixed per-call term (+3..+22 ns on a 260-400 ns 27-subject cell, 0.1-0.8 ns per
subject), not a scan-length term: the plain-form regimes are flat (throughput 1.000 median, 0.687 on `abc$` where rev-end wins x1.45; short 1.000, min 0.692), and the `abc$` PLAIN cell is x0.69 faster with rev-end
(253.9 vs 367.0 short; 257.8 vs 375.0 throughput) -- the 1.7-2.6x Zen-4 win pcrec read shows here as x1.45 on the one plain cell where rev-end applies. Not read: a Zen 4 box; per-subject structure of the whole-form
cell (the records carry it, `--grain subject`); the long-subject whole-form cells (litrun has none).

## 8. (f) I-148's seam movers, 6b2dbd3e vs 00c97769 (the 18 seam-changed patterns)

`2026-10-13-b136-seam.txt`. Set-cell CANON/NEW (<1 = canonical faster), predicted bak-1 +13.5%, bak-2 +9.7%, mod-j-uc +5.6% (i.e. ~0.88 / 0.91 / 0.95):

| pattern | short | throughput |
|---|---|---|
| **bak-1** | **0.856** DISJ | **0.883** DISJ |
| **bak-2** | **0.808** DISJ | 0.901 ov |
| **mod-j-uc** | **0.924** DISJ | **0.917** DISJ |
| bak-g-rel | 0.859 | 0.875 |
| bak-py | 0.864 | 0.873 |
| bak-k-named | **1.041** (slower) | 0.873 |
| lkb-pos | 0.885 | 0.989 |
| lkb-neg | 0.990 ov | 0.981 |
| utf8 asr-lb-fixed / varwidth / neg / class | 0.938 / 0.873 / 0.891 / **0.788** | 0.966 / 0.858 / 0.978 / **0.704** |
| capability doubled-word | **1.066** (slower) | 0.995 |
| capability dup-param-detect | 1.020 | 1.001 |
| capability phone-palindrome-6 | 0.885 | 0.878 |
| capability quoted-delim-match | 0.974 | 0.978 |
| capability tag-pair-match | **1.064** (slower) | 0.999 ov |
| capability tag-depth3-bound | 0.932 | 1.000 ov |

**Confirmed**: all three named movers are faster beyond overlap, bak-1 and bak-2 by MORE than predicted on short (x0.856 / x0.808 vs ~0.88 / ~0.91) and mod-j-uc in line (0.924 / 0.917 vs 0.95).
**The other 15 of the 18** are program changes the I-148 text did not name; over their 30 set cells (short + throughput): 22 faster beyond overlap (the whole `bak-*` family 0.86-0.88, utf8 `asr-lb-class` x0.704 throughput, `lkb-pos` 0.885 short), 3 overlapping, and
**five slower beyond overlap, four of them cells worth naming**: capability `doubled-word` short x1.066, `tag-pair-match` short x1.064, syntax `bak-k-named` short x1.041, capability `dup-param-detect` short x1.020 (and its throughput x1.001 DISJ). Per-subject (`2026-10-13-b136-seam-slower-subjects.txt`):
`tag-pair-match`, `dup-param-detect` and `bak-k-named` pay **+0.3..+2.1 ns on a ~10 ns quick-dismissal call** (65-73 of 75 subjects slower, each by a hair); `doubled-word` pays +20..+42 ns on a 170-280 ns
call (65 of 75 subjects slower, sum +411 ns of a 5,878 ns cell). The whole-subject (`match-compliance`) cells of the eight syntax seam patterns are ALL faster beyond overlap: `bak-2` **0.660** (394.1 > 259.9), `lkb-pos` 0.800, `bak-k-named` 0.863, `bak-g-rel` 0.941, `bak-1` 0.942, `lkb-neg` 0.942, `mod-j-uc` 0.945, `bak-py` 0.946 (the utf8 and capability records carry no whole-subject cell for their ten). The program-identical null (CANON vs NEW, other cells): loglines 22 cells 0.995-1.001; altwide 107 cells 0.972-1.008 (7 DISJ); syntax 219 cells
0.977-1.067; utf8 130 cells 0.984-1.026; capability 125 cells 0.978-1.018 -- p5-p95 stays inside 0.992-1.011. Not read: the nocaps arm of the seam (no record), a Zen 4 comparison; the cause of the four slower
cells is not located (hypothesis only: the inlined helper lengthens the VM hybrid's quick-dismissal path).

## 9. (g) The tail family and the grok control -- none should move

Tail family (`2026-10-13-b136-tail.txt`; capability@0.2 caps, B / N / C, the five `tail-*` patterns x {throughput, short}):

- 10 set cells: N/B 0.994-1.001 (2 DISJ, at 0.999), C/N 0.985-1.001, C/B 0.979-1.002; `stamps` (`dfa_scan rev-end`, `dfa_start reverse-pass`, `dfa_prefilter none`) and `program_sha256` identical at all three pins.
- 66 per-subject throughput cells (6 patterns, 11 subjects): N/B median 0.999 (min 0.957, p95 1.048, max 1.110; 3 DISJ), C/N 0.840-1.055 (0 DISJ), C/B 0.848-1.080 (1 DISJ); this window's B vs the 2026-10-11 B:
  median 1.002 (0.930-1.061, 0 DISJ).
- **Verdict: the tail family did not move.** The long-subject numbers: `tail-word-eoz` B 21,918.5 > N 21,905.3 > C 21,907.2; `tail-space-eol` 21,998.6 > 21,969.8 > 21,975.8.

Grok (`2026-10-13-b136-grok.txt`, `wild-logparse-quotedstring-grok` caps, `engine vm`, `program_sha256 ae9848c3aa54`, emit 64,131 B at all four records): short
b8337c33 2,147.0 (10-11) > 2,136.4 (10-12) > 2,141.3 (00c97769) > 2,137.7 (6b2dbd3e); every adjacent ratio 0.995-1.002, all ov; throughput 2,063,180 > 2,063,010 > 2,065,445 > 2,063,279 (1.000-1.001). Per-subject deltas
within +-3.7 ns, median 0.00. **Verdict: no grok move at any of the three pins, and the cell reads the same across the day (x0.995).** Not read: the nocaps arm (capability has no nocaps record in the window).

## 10. (h) Ask 5.2 -- loglines / altwide medians at a post-START-LANDING pin

`2026-10-13-b136-medians.txt` (every plain-form set cell: B, N, C medians + range, C/B, subjects, engine / `dfa_start` / `dfa_prefilter`). At 6b2dbd3e: **loglines** (11 patterns, 12 throughput subjects, 112 short):
throughput median 1,370,363 ns across patterns (min 206,593 `kv-quoted`, max 11,049,517 `hex32-id`), short median 33,432 ns (min 1,509 `floor`, max 297,762 `hex32-id`); **altwide@0.3** (34 patterns, 4 throughput
subjects, 40 short): throughput median 2,905,098 ns (min 15,415 `floor`, max 4,861,355 `s-2048`), short median 7,585 ns (min 458 `floor`, max 15,020 `s-2048`). `dfa_start` at 6b2dbd3e: loglines `end-minus-width` on
`floor`/`hex32-id`/`uuid`, `reverse-pass` on the other eight; altwide `reverse-pass` on 33 patterns, `end-minus-width` on `floor`, 5 unstamped (non-DFA or refused) (the START-LANDING `landing` value does not appear in these two sets). C/B is 1.000 +-0.3% on
every cell except the nine `handoff` movers. The per-pattern weights pcrec asked for are in the file. Not read: weights by traffic share (the bench has none).

## 11. (i) Ask 7.1 -- the jit / interp peers re-measured; the 30 sub-x1.5 trailing cells

Peers re-measured at current versions, this window vs the previous record of the SAME testee id (`2026-10-13-b136-peers.txt`), set-grain cells:

| set | jit old > new | jit now/old (median; p5-p95; >+-10%) | interp now/old (median; p5-p95; >+-10%) |
|---|---|---|---|
| bounded | 2026-09-05 | 0.991; 0.957-1.041; 0 | 0.991; 0.953-1.022; 1 |
| loglines | 2026-09-02 | 0.999; 0.994-1.002; 0 | 0.997; 0.989-1.014; 0 |
| syntax | 2026-09-07 | 1.002; 0.953-1.046; 0 | 0.998; 0.970-1.021; 4 |
| utf8 | 2026-09-26 | **0.988; 0.910-1.001; 5** (short median 0.954) | 0.999; **0.774-1.181; 43** |
| litrun | 2026-09-28 | 0.982; 0.938-1.029; 0 | (no earlier record) |
| email-specimen | 2026-09-02 | 0.998; 0.840-1.021; 1 | 0.996; 0.791-1.016; 2 |
| **all** | | n=633: **0.998; 0.935-1.034** | n=595: **0.998; 0.838-1.034** |

**The cross-window drift on the peers is: median 0.998 (both engines), p5-p95 0.935-1.034 (jit) / 0.838-1.034 (interp), concentrated in the SHORT-search regime of utf8 (jit median 0.954, 0.869-1.013; interp 0.715-1.275: `ci-turkish-i` 7,009 > 5,011, `cls-d-ascii` 4,627 > 5,900)
and in syntax interp short (`rec-back`/`rec-g-angle`/`rec-py` x1.22)**; the throughput regimes are flat (utf8 median 1.000, p5-p95 0.980-1.008; syntax jit 1.002, 0.998-1.036, interp 0.994, 0.966-1.017). The sentinel's own jit row says the box does not drift (section 13), so
these are a September-record-versus-today difference of the peers' own short cells, not a box effect; the cause is not located.

**The gap report's 30 sub-x1.5 trailing cells vs jit** (`rank.json`, `run_2026-10-11`, re-read with this window's jit; `2026-10-13-b136-gap30.txt`): **25 of 30 have a new jit number; all 25 still trail (0 flipped to lead, 0 reach
x1.5), none moved by more than 10%** (jit now/old 0.971-1.036, median 1.002; the pcrec side now/old 0.947-1.005, median 1.000). Per cell old > now: bounded `cls-atleast-4096` tp 1.47 > 1.47, `ctx-lazy-64` ss 1.22 > 1.24, `pw-8-64` tp
1.49 > 1.49; litrun `lit-l16` tp 1.27 > 1.30 (pcrec side 6b2dbd3e, no BASE cell), `lit-l8` tp 1.37 > 1.36; loglines `iso-ts` tp 1.20 > 1.20; syntax `bak-1` tp 1.27 > 1.27 / ss 1.21 > 1.22, `bak-2` ss 1.27 > **1.21**
(the b8337c33 side moved 0.947), `bak-g-rel` 1.27 > 1.27 / 1.21 > 1.20, `bak-py` 1.28 > 1.27 / 1.20 > 1.23, `esc-hex` 1.29 > 1.27, `esc-quote` 1.35 > 1.35, `grp-cap` 1.25 > 1.24, `grp-named` 1.26 > 1.24, `grp-named-quote`
1.25 > 1.25, `grp-noncap` 1.26 > 1.25, `lit-cat` 1.29 > 1.27, `mod-n` 1.27 > 1.26, `mod-reset` 1.29 > 1.27, `mod-unset` 1.28 > 1.27, `mod-x` 1.29 > 1.27, `qnt-quest` 1.34 > 1.29. **The five capability cells
(`high-byte-run` 1.19, `phone-palindrome-6` 1.26, `pwd-strength-chain` 1.45, `router-prefix-order` 1.43, `utf8-lead-no-cont` 1.13) have NO new jit number**: tier 4 did not include capability (the jit/interp
records there are 2026-10-08), so those five stay inside the unquantified drift; note `phone-palindrome-6` is one of the seam's 18 (its pcrec side moved 0.878 at 6b2dbd3e, i.e. x1.26 > ~x1.11). **Verdict: the 30 are
a real, not a drift, residue.** Not read: rust, re2 and onig (not re-measured), so "trailing vs the best peer" cells (87/113 in the gap report) are untouched by this refresh; the baseline of the 30 is the
gap report's b8337c33 numbers (cross-checked by section 2).

## 12. (j) Ask 7.2 -- the per-subject split of three capability throughput cells

`2026-10-13-b136-split.txt`: pcrec 6b2dbd3e caps (this window) vs jit (2026-10-08T22:03Z) and interp (2026-10-08T20:51Z), the newest records of each; per subject ns/call, 11 throughput subjects.

- **`wild-datetime-moment-iso8601`** (set cell pcrec 69,118 vs jit 6,467 = x10.69): **two subjects carry 99.8% of the pcrec sum**: `t-trim-match-60k` **54,449 ns** (jit 2,360, x23.07; interp 37,143) and
  `t-trim-nearmiss-16k` **14,563 ns** (jit 672, x21.67; interp 10,040) = 69,011 of 69,118. The other nine subjects: pcrec 11.4-15.5 ns, jit 55-62 ns on the prose/mixed subjects (**pcrec x0.19-0.26**); on the two
  `t-evil-*` subjects pcrec 11.4 vs jit 2,362 / 672.
- **`wild-validator-email-owasp`** (46,117 vs 6,387 = x7.22): `t-evil-match-60k` **36,309 ns** (jit 2,354, x15.42; interp 56,779) + `t-evil-nearmiss-16k` **9,716 ns** (jit 661, x14.69) = 46,025 of 46,117 (99.8%); the nine
  others pcrec 6.2-14.7 ns vs jit 43-63 (x0.14-0.25), including `t-trim-*` (6.2 ns vs jit 2,351 / 658).
- **`wild-waf-crs-942270-union-select`** (1,965,680 vs 207,011 = x9.50): **no single subject**: nine of the eleven subjects are x4.80-x10.68 behind jit and uniformly so (the three 1 MiB prose subjects 487,062-487,784 ns vs jit 45,658-45,732 =
  **x10.65-10.68**; `t-1m` x7.99, `t-256k` x7.28, `t-64k` x5.82; `t-evil-match-60k` x5.83, `t-evil-nearmiss-16k` x4.80, `t-mixed-runs-4k` x4.85); only the two `t-trim-*` subjects pcrec is faster (x0.76 / x0.58 of jit).

**Reading**: the ANCH-ATTEMPT pair is **two hazard subjects per pattern (the trim pair for moment-iso8601, the evil pair for email-owasp)**, not the prose; on the ordinary prose pcrec is x4-x7 FASTER than jit on both. union-select is the opposite:
a uniform per-byte gap (the 1 MiB prose is x10.7). The jit/interp records are four days older than the pcrec record; the sentinel's jit row moves <= 0.3% in median over 10-10 to 10-13 (section 13). Not read: why the
trim/evil subjects cost 54/36 us (the store carries no stamp for it; `dfa_scan` etc. are in the compile rows, not read here).

## 13. (k) Ask 7.4 -- the sentinel jit row across 10-10 .. 10-13

`2026-10-13-b136-jitrow.txt`: `sentinel@0.1` x `libpcre2_10.46_jit-caps-simdna`, **nine records** (2026-10-10T17:13Z through 2026-10-13T06:08Z), 15 pattern cells, set-grain. Against the first record: medians 0.999-1.006 (every record),
per-cell min-max 0.892-1.125 (the widest single cell: 1.125 in the 10-13T00:54Z record), 1 disjoint-range cell in the whole series; sum of the 15 cell medians 10,419,806-10,477,653 ns (**+-0.28%** around 10,455,000).
Adjacent-record median ratios 0.997-1.003. **The peer-drift number across four days is +-0.3% in median (cell-level +-6%, p5-p95), and it is flat enough that the peers' ordinary cross-window difference in
section 11 is NOT a box effect.** The row is in every sentinel pass of this chain (`SENT_OPEN`/`SENT_CLOSE`), so it is kept.

## 14. Findings not asked for

1. **mod-i / mod-r pay x1.07-1.08 search_short and x1.03 throughput** (K 0, run `CAT` caseless, 3 landmark-absent subjects included): the first handoff movers that are **slower** beyond the +3% bound on a LARGE landmark-absent subject. Not in I-147's list of cells.
2. **qnt-poss-brace's `f-tag` x2.40** and **kv-quoted's 12 dense subjects x1.033-1.29** are the density-sensitive costs (section 5); sfx-512's dense subject (`t-128k-dense`) is x0.791 against x0.113 / x0.121 on sfx-64 / 256.
3. **The utf8 DENY arm is empty** (section 0.2): `ci-strasse` has no `-fno-req-handoff` cell.
4. **Seam**: four slower cells (section 8), all in programs that gained the static-inline helper.
5. **Rev-end whole form +1.2% median on this box** (section 7), the same sign and magnitude as O-96 (c)2.
6. Peers drift on utf8 short-search (section 11).

## 15. Not read / checklist for the next sample

Not read: nocaps arms (except litrun and the sentinel), capability D, bounded C, utf8 D beyond `ci-ascii-control`/`asr-b-ascii`/`floor`, the nocaps-only 15th mover, rust/re2/onig/vectorscan this window, Zen 4, the box's occupancy
columns, subject sha256s, any cause (every "hypothesis" above is labelled). The next window should (1) add the utf8 roster row and re-run `pcrec-auto-utf8-noreqhandoff` on utf8, (2) run capability `-nocaps` B/N and bounded C,
(3) add a capability `jit` + `interp` refresh to the peer tier, (4) consider mod-i / mod-r as the post-L1 regression cells.

## Correction (2026-10-13, inbox I-151)

Finding (i) above described mod-i / mod-r as paying the RE-ENTRY's cost on landmark-absent text. That is wrong. pcrec's emitted-C reading (its `docs/dev/lanes/o101ans_report.md`) shows that BASE and NEW make identical memchr call counts on those subjects (2/2, 3533/3533, 12112/12112). Both return 0 from the ENTRY pre-check before any DFA work, so the re-entry never runs.

What differs is the compiled form of the entry loop: a larger frame and one more live value. Read finding (i) as an entry-loop codegen cost on Zen 1. On Zen 4 the throughput x1.03 does not reproduce, while the short-call +0.5-0.7 ns does.

The same item answers the other asks:
- ask 1: the K-0 admission is a known gap, pcrec's [PRIOR-COST-UNIFY] / K105;
- ask 2: f-tag is a landmark-density case, recorded by pcrec as a [START-DENSE] witness;
- ask 3: the four slower seam cells have byte-identical search and match code at -O2, so they are layout or noise;
- ask 4: the rev-end sign is box-dependent, a win on Zen 4 and what we measured on Zen 1.
