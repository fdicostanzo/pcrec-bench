## O-67 (2026-09-28, pcrec-bench manager) — I-115 Q2's placement twin: both headline misses shrink toward null, neither disappears; a roster gap found on the new testees

**Context**: I-115 Q2 asked whether O-64's two named-population misses
(`wild-secrets-aws-access-key-id` throughput ×1.037 slower,
`logparse-atomic-removed` +0.7-1.4 ns/call slower, both auto ÷
auto-nolitrun at `-fno-lit-run`, pin a32bc86e) are CODE or PLACEMENT.
O-66 built the two testees the question needs
(`pcrec-auto-align64loops`, `pcrec-auto-nolitrun-align64loops`, both
= their unaligned namesake + `-falign-functions=64 -falign-loops=64`)
and handed back the window; it ran 2026-09-28 06:15-06:58 EDT
(`capability@0.1` only, 2/2 measured at attempt 1). This item is that
window's read.

**Where it is**: report
`reports/2026-09-28-capability-0.1-budu-ryzen1600-align64loops-a32bc86e.*`;
ledger `docs/dev/ledgers/2026-09-28-capability-0.1-i115q2-align64loops-a32bc86e.md`;
measurement archive `docs/dev/measurements/2026-09-28-b110-align64loops-placement.txt`
(+ its reproducing script).

1. **The twin's own precondition holds: `program_sha256` is IDENTICAL,
   aligned vs unaligned, on every checked cell.** Both named witnesses,
   both forms (4/4), plus every one of 73/72 shared DFA-null
   (program-identical between auto and nolitrun) compile keys still
   available on the aligned pair (0 diffs either arm). Your own phase-2
   code is provably unmoved by our `cflags`; only placement can differ.
   And it does: `objdump -d` on the real `.so` files (both witnesses,
   the unaligned vs aligned build of the SAME arm) shows distinct file
   sha256 and every `rx_*` function after `rx_match_anchored` shifted
   0x30-0x80 bytes. The twin measures what Q2 asks.

2. **Neither miss survives intact — both shrink substantially toward
   null, one nearly into its own window's noise band, the other not.**
   Ratios below are auto ÷ auto-nolitrun, set grain, plain form; the
   DFA-null noise band is this window's own spread over 61 program-
   identical cells (narrowed by item 4 below).

   | cell | unaligned (O-65) | aligned (this window) | this window's DFA-null band |
   |---|---|---|---|
   | aws-access-key-id / throughput | 1.0361 | **1.0144** | ±3.9% (thr, n=31) |
   | aws-access-key-id / search | 0.9813 | 1.0089 | ±2.4% (srch, n=30) |
   | logparse-atomic-removed / throughput | **1.1174** | **1.0286** | ±3.9% |
   | logparse-atomic-removed / search | **1.0833** | **1.0341** | ±2.4% |
   | router-prefix-order (DFA control) | 1.0003 / 1.0003 | 1.0004 / 0.9977 | — |

   aws throughput: ~60% of the 3.61% excess is gone (to 1.44%), which is
   INSIDE this window's ±3.9% throughput band. lp-removed throughput: ~83%
   of the 11.74% excess is gone (to 2.86%), also inside the ±3.9% band.
   lp-removed search: ~59% gone (8.33%→3.41%), still OUTSIDE its ±2.4%
   band — the one residual that stands on this window's own noise.
   (Caveat: this window's DFA-null band is wider than the ~±1% the
   O-64/O-65 twins read, so "inside the band" is a weaker statement than
   "null".) **Read plainly: alignment removes most of both misses; on
   this window's own noise only lp-removed's search residual remains —
   a mostly-placement finding, not a clean either/or.**

3. **The aligned/unaligned-per-arm table, stated with its caveat.**
   Not asked directly, but sitting in the same numbers: does adding the
   alignment flags alone move either arm's own absolute time?

   | cell | auto: aligned/unaligned | nolitrun: aligned/unaligned |
   |---|---|---|
   | aws thr | 0.9781 | 0.9990 |
   | aws srch | 0.9745 | 0.9479 |
   | lp-removed thr | 0.9554 | 1.0379 |
   | lp-removed srch | 0.9530 | 0.9983 |
   | router-prefix-order thr / srch (control) | 0.9916 / 1.0226 | 0.9915 / 1.0254 |

   This is a CROSS-WINDOW comparison (unaligned ran 04:10-05:21 EDT,
   aligned 06:15-06:58 EDT — different box states, worst-other-core-busy
   25.0% vs 38.1%). The DFA control itself reads 1-2.5% off unity in
   BOTH directions across the two windows, so individual cells here are
   not reliably separable from cross-window noise at this grain; we are
   not claiming a directional finding from this table alone.

4. **UNPLANNED FINDING: the O-64/O-65 roster-declaration gap recurs,
   unfixed, on the two new testees.** `bench/capability/patterns.rxt`'s
   `ext bench` roster declares NO capability tokens for
   `pcrec-auto-align64loops`/`pcrec-auto-nolitrun-align64loops` — the
   same class of gap O-64/O-65 found and fixed for `pcrec-auto-nolitrun`
   itself (commit `fef55af`), not ported to these two testees when they
   were added. 27/64 patterns refuse `unsupported-by-declaration`
   identically on both aligned arms, including `logparse-atomic` (your
   own Q3 pattern — it has NO reading on this twin at all) and three of
   O-65's own P2 FLAT cells (`tag-pair-match`, `nested-comment-rec`,
   `email-local-nodup`). Neither Q2 headline witness nor the
   `router-prefix-order` control is affected. This is a bench-side
   artifact, not filed as a finding about pcrec; a fix + re-measure is
   OWED on our side (same shape as O-64→O-65).

**What was NOT measured**: no `perf`/hardware-counter reading (this box
refuses unprivileged `perf`, no sudo used, same constraint as O-66); no
same-window unaligned-vs-aligned control (O-66's own choice, not added
here); the roster gap is not fixed and no re-measurement was launched.

`make check-interpret`: see below (this lane's report has the exact
count).
