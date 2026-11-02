# b149mon -- the READ of the Monday window: unusual@0.1's first PINNED records, pcrec cb32eda28 (abi 93) and @614d45eb3

Lane b149monread (Sonnet), 2026-11-02. A READ of committed records and the window logs; nothing was timed, `store/` and ~/pcrec were not written.
Window: chain `docs/dev/lanes/b149mon_chain.sh`, 2026-11-02 03:40:26 -> 13:36:54 EDT (9 h 56 min) on `ryzen7700x` (core 7), store commit bbc5fb7a,
23 cells, 23 `measured`. Logs: `/var/tmp/pcrecbench/b149mon/{chain,suite,suite_end}.log`, `build/windows/window_*_20261102T*.log` (main tree).
Reports (reporter v28, rendered detached by `docs/dev/measurements/2026-11-02-b149monread/gen.py`, each group loading only its own 3-11 records, 14-40 s):
`reports/2026-11-02-{unusual-0.1-ryzen7700x-first,capability-0.4-ryzen7700x-noedge,syntax-0.2-ryzen7700x,sentinel-0.1-ryzen7700x}-cb32eda28.*`
(unusual also `.stream.md/.tsv`; each with a `.interpretation.md`). Every number below not otherwise cited comes from
`docs/dev/measurements/2026-11-02-b149monread/an*.py` (outputs in `out/`). Pre-registered charters read: bench/unusual/NOTES.md sections 4-5 (D-1..D-5, R0-R5),
docs/dev/lanes/b149prep_report.md section 0.5/5 (K134), b148inline2_report.md, the L9 ledgers, outbox O-113/O-116.

## 0. Window quality (each verdict: what was read, what was not)

* **Usable, not quiet.** All 23 records `measured`, trial agreement `agree` on all 23 (0 disagreeing groups on any). The opening `quiet` read NOT QUIET (rc=3; advisory by design).
  Pre-flight refused 19 attempts (rc=3, nothing written): 11 of 23 cells needed more than one attempt (jit-deep 5, onig-deep 3, vm-deep 3, jit sentinel 3, vm@614 3, syntax noedge 3, five others 2),
  12 passed at attempt 1; 42 attempts in all. Of the 23 records, 16 carry an AFTER load1 above 2.00 and 11 a failed AFTER occupancy sample (7 both) -- provenance under v1.4, not a verdict.
  Pre-flight busiest other core 1.8-9.7 % (limit 10), target core <= 6.01 % on every record. One 1-second spike to 50.0 % on another core inside `pcrec_614d45eb3_auto-caps-simdna`
  (wild-json-validate-onig / large-subject-throughput, R-STATUS-8). Read: every record's setup row (`an11`), the chain log. NOT read: which process the load was (no per-process accounting).
* **Driver unchanged across the window:** `build/work/pcrec-{auto,nocaps}/pcrec_driver` sha256 `0e877032...` on the chain's first and last lines (b147read's start/end mismatch was a rebuild; none here).
* **Cell walls** (start to `attempt N rc=0`): sentinel 5-9 min; unusual pcrec default/inline 19.4-20.6 min, `_in` arms 41.9 / 44.6 min, pcre2-jit-deep 21.5, onig-deep 54.9, pcre2-interp-deep **60.7 min = 3,639 s = 0.51 of
  `CELL_CAP_unusual` 7,200 s** (L9's proposed cap held with x2 margin); capability noedge 61.6 min; syntax 40.5-40.9 min. Sets: sentinel 28 min, unusual 352, capability 63, syntax 124, closing sentinel 26.
* **Cross-window control (sentinel@0.1, pcrec side, NOT clean, opposite sign to b147read's):** `pcrec_cb32eda28_auto-caps` 1,125 subject cells, close/open this window 1.001 (short cells, 15 pattern cells median; 0.955-1.071);
  but this window vs W2 (11-01 12:59 open) median **0.940** (p5 0.82), W2 open->close 0.9965; auto-nocaps the same (0.940); `pcrec_614d45eb3_auto-caps` 11-02 vs 10-28 0.956 and vs W2 1.000;
  libpcre2-jit this window vs W2 0.546/0.544 (flat). So pcrec's sentinel cells read ~5-6 % faster on 11-02 than on 10-28/11-01, on both pins, jit flat. harness_commit moved e516461f -> af4a1ad7 between W2 and
  here but `git diff` shows only `testees/pcrec/adapter.py` (compile-side Python), configs.toml and a CLAUDE.md -- no driver.c / shim.c / timed.c change. **Cause not isolated.** Consequence: every cross-WINDOW short
  cell below (capability noedge vs W2 auto; syntax cb32eda28 vs the 10-28 614d45eb3 records) carries about -5 %; large cells do not (large-cell medians of the same comparisons 0.998). In-window pairs (the
  unusual cb32/614 and sep/inline pairs, closing sentinels) are unaffected.
* **Not read:** the L9-class `inconclusive-load` question does not arise (no such status); the viewer / trend / front page (`make trend`, `make frontpage`) were not run.

## 1. (a) unusual@0.1, the first PINNED records (11 cells)

Cell counts below are trial-1 outcomes of (pattern, regime, subject) cells (a call-stream is one cell), 3,013 per pcrec arm; all five trials of every cell agree on the outcome. Source `an1`-`an5`, `an15`.

### 1.1 Outcomes by arm

| arm | gave-up cells | other non-ok | notes |
|---|---|---|---|
| pcrec-auto @614d45eb3 / pcrec-vm @614d45eb3 | 62 (8 call-stream, 50 throughput, 4 short) | 0 | = L9 scratch: 24 + 24 cscan/cscan-onig, 8 sexp, 3 + 3 json (byte-identical outcome sets auto vs vm) |
| pcrec-auto / pcrec-vm @cb32eda28 | **34** (0 stream, 30 throughput, 4 short) | 0 | auto == vm cell for cell (3,013/3,013) |
| pcrec-{auto,vm}-inline @cb32eda28 | 34 (identical to the separate-TU arm on all 3,007 shared cells) | 0 | 3,007 cells, not 3,013 (section 1.4) |
| pcrec-{auto,vm}-in (deep, 1 GiB caller buffer) | **0** | 0 | 3,013 cells all `matched-as-expected` |
| libpcre2 jit-deep | 0 | 0 | 3,331 cells |
| libpcre2 interp-deep | 0 | 4 timed-out (cscan and cscan-onig x nest-brace-32k and -100k) | |
| oniguruma deep | 0 | 3 timed-out (cscan, cscan-onig nest-brace-100k; wild-sexp-balanced nest-paren-100k) + 2 wrong (cscan `define-witness`, `cs-define`: observed [0,12], expected [0,6]) | |

R0: the two onig wrong rows are the verbatim `(?(DEFINE)` spelling, excluded; `cscan-onig` is right (what the D-3 variant exists for). The oracle (libpcre2 interpreter) declines `cscan`/`cscan-onig` on nest-brace-100k
(NOTES section 3), so those two cells are scored by the reference scanner alone, as before.

### 1.2 K134 (trail compaction), by value, 614d45eb3 -> cb32eda28, same window (the 614 cells ran 09:53-10:14, the cb32 cells 09:10-09:52)

b149prep predicted: the five flat cscan subjects and a substantial part of the stream give-ups flip; `nest-brace-<d>` (live nesting) stay, "boundary ~342 -> ~763", `nest-brace-128` FLIPS; wild-json/sexp "mostly unchanged".
The brief's "24 cscan + 8 + 3 FRAMES now answer" is **not what happened**; measured (auto; vm identical):

| group | at 614d45eb3 | at cb32eda28 | verdict |
|---|---|---|---|
| cscan / cscan-onig, call-stream (seg-s, seg-l, sqlite-bodies, sqlite-bodies-s) | 4 + 4 cells gave up (100/256, 1,723/4,096, 163/311, 2,620/4,971 calls: byte-identical to O-112/O-113) | **0 give-ups on all four streams**, matched/nomatch = 251/5, 4,049/47, 4,971/0, 311/0 (the expectation counts; results_sha256 == expectations_stream.tsv, outcome `matched-as-expected`) | CONFIRMED in full |
| cscan / cscan-onig, flat throughput: comment-5m, idents-1m, splice-1m, nest-paren-{512,1k,2k,8k,10k,32k,100k} | 10 + 10 cells gave up | **0** (10 + 10 flip to `matched-as-expected`) | CONFIRMED (the five named subjects and the seven nest-paren rungs) |
| cscan / cscan-onig, `nest-brace-{128,512,1k,2k,8k,10k,32k,100k}` + `nest-digraph-10k` | 9 + 9 cells | **9 + 9 still `PCREC_ERR_FRAMES`** | stay, as predicted for >= 512; **`nest-brace-128` does NOT flip: that prediction is REFUTED** |
| cscan / cscan-onig short `cs-nest-100` | gave up | gave up (FRAMES) | unchanged |
| wild-sexp-balanced (8 throughput), wild-json-validate(-onig) (2 throughput js-1m / js-near-1m + short `js-deep-arr`) | 8, 3, 3 | 8, 3, 3, same subjects | unchanged ("mostly unchanged" held; the brief's "8 + 3 now answer" did not) |
| total | 62 cells | 34 | 28 flipped (14 per cscan spelling), 0 unflipped-to-new |

So 14 of each cscan spelling's 24 gave-ups flip and 10 remain; the 10 are live nesting (brace ladder, digraph) plus `cs-nest-100`. The depth boundary for cscan is below 128 braces (the 342 -> 763 figure is for
pcrec's `^(a(?1)?b)$` specimen; cscan spends more frames per level -- the stamps are the same `resume_frames 2048` / `trail_frames 3072` / `fast_frames 37` / `fast_trail 56` at both pins). Gave-up diagnostics are
all `giveup:-3:PCREC_ERR_FRAMES` (named, X49). **Cost on answered cells (b149prep predicted +1-4 %):** across the 2,894 short cells answered at both pins the cb32/614 median is 0.992 (auto) / 0.999 (vm);
sum-ratio 1.004 / 0.976; so no short-cell shift at all. Answered flat throughput cells of the cscan family: `literal-100k` x1.000-1.025, `define-witness` x0.98-1.03, `nest-paren-128` x0.96-0.99,
**`unterminated-5m` x1.072 (cscan-onig) / x1.100 (cscan) auto, x1.059 / x1.088 vm**, trial ranges disjoint for cscan (34,531-34,660 -> 36,583-38,190 ns): the one cell above the predicted band; whether K134's
`TRAIL_CHECK` per backward goto is the cause is not isolated (REQRUN-VM also touches the pre-check this subject exercises).

### 1.3 Other cross-pin movers in the same window (in-window, 614d45eb3 -> cb32eda28, auto)

* **isbn / member callout members, large cells: x0.38-0.59** (co-member-pass x0.384, co-isbn-pass x0.481, co-member x0.487, co-isbn x0.589; the same on vm 0.38-0.57), and the TWIN arms on the VM route
  (co-isbn-twin 434,005 -> 199,223 ns, co-member-twin 588,236 -> 195,537 ns); co-luhn and co-netstr flat. Attribution by stamp: `req_handoff` **`none` -> `0`** on exactly co-isbn*, co-member* (an6; abi 91 [REQRUN-VM]),
  `req_run`/`req_byte`/`vm_program_bytes` unchanged; emit +3,0xx B everywhere (the cb32 shim/abi block). It is not a callout effect (the twin moves too).
* `floor` on the eight small `nest-*` subjects x0.65-0.79 (9.7-24.7 ns); the floor on the VM route is flat (x0.97-1.04), so it is the auto (DFA) route's floor that moved.
* Set-level: 2,894 short cells median 0.992, 51 large cells median 0.983 (auto) -- the movers above are 12 of 51.

### 1.4 The inline pair and the 66 rows

`pcrec_cb32eda28_{auto,vm}-caps-simdna_inline` = 15,222 index rows vs the separate-TU arm's 15,288 (jsonl lines 15,223 vs 15,289). **The 66 are fully accounted for by the four vars members** (`va-route`, `va-tenant`, `va-term`,
`va-term-bang`), which the inline testees do not declare (`VARS_NATIVE` untouched, b148inline2 section 3): the inline record carries ONE `unsupported-by-declaration` compile row per member (diagnostic "REQUIRES unusual-va-*, vars;
pcrec-auto-inline declares none of it") where the separate-TU arm has 5 compiled plain rows + 5 whole-subject rows and 6 call-stream cells x 5 trials:
30 stream match rows + 20 whole-subject compile rows + 16 extra plain compile trials (4 members x (5 - 1)) = **66**, exactly (`an1`; match rows 15,065 vs 15,035, compile rows 223 vs 187). The same 6 streams are the
only cells missing (3,013 vs 3,007). Outcome equality on the 3,007 shared cells: 0 differences, all five trials (`an15`).
Inline vs separate-TU, same pin (inline cells ran 10:35-10:55, separate 09:10-09:52; in-window but 25-85 min apart), large 1 MB subjects, vm route / auto route:

| member | site cost `pass - twin` ns (sep -> inline) | callee `real - pass` ns (sep -> inline) | `real` ns (sep -> inline), ratio |
|---|---|---|---|
| co-luhn (11,308 fires, sep count) | 95,322 -> 11,527 | 295,493 -> 327,722 | 937,922 -> 881,902 (x0.940) |
| co-isbn (8,429) | 29,988 -> 4,977 | 99,261 -> 114,669 | 328,472 -> 317,510 (x0.967) |
| co-member (13,158) | 51,694 -> 6,995 | 120,964 -> 143,258 | 368,195 -> 345,569 (x0.939) |
| co-netstr native (`consume`, 34,127 fires) | -- | -- | 1,497,150 -> 1,356,480 (x0.906) |

Per fire (sep fire counts applied to the inline rows; the inline artifacts carry no `callout_fires` by design, b148inline_report 4.5): luhn site 8.4 -> 1.0 ns, isbn 3.6 -> 0.6, member 3.9 -> 0.5. The
callee term grows 11-18 % on the inline arm (the pass arm's stub inlines away, so the residual `real - pass` is larger): the net win is x0.91-0.97 on the real arm. Short-subject set sums: inline/sep 0.96-1.06, no consistent sign.
Artifacts: inline emit +6,975..+9,109 B (co-luhn 28,285 -> 35,736), `.so` 51,368 -> 41,104 B, gcc phase 333 -> 259 ms (-22 %); `callout_binding = inline`, `code_langs c`, `callout_bindings ""` on every inline compile row.
The auto route's `pass - twin` is negative (-375 us on luhn): the auto `twin` is a DFA artifact and the `pass` arm is a VM -- two routes, not a callout saving (the L9 reader's caveat holds; read the vm pair).
Not read: the inline arm's per-call callee cost independent of fire counts (no `callout_fires` on inline rows), vars on the inline arm.

### 1.5 The five deep arms (BD17 `--prime` in the throughput regime)

* **Outcomes** in 1.1. pcrec `_in` answers every cell (the K134 flips included, so the brace ladder, which gave up on the DEFAULT arm, is answered under the 1 GiB buffer: D-2 "every rung answered under `_in`" CONFIRMED again).
* **L9 reproduces where nothing moved:** nest-brace ladder ratios now/L9 (cscan-onig): jit-deep 0.95-1.04, onig-deep 0.99-1.02, pcrec `_in` 1.00-1.03 up to 32k (0.86-0.88 at 100k), interp-deep 0.90-1.02 (8k 1.665 s vs 1.64 s).
* **interp-deep nest-brace-32k is now `timed-out`** (all 5 trials, "the per-subject alarm fired"; 60 s per-subject alarm) where L9 measured 31.0 s (IL). 100k timed out in L9 too. onig-deep 32k answers (9.246 s vs 9.2 s)
  and onig-deep **wild-sexp-balanced nest-paren-100k is a new timeout** (L9 answered it). So 4 + 3 timed-out cells vs L9's 2 + 2. Cause not isolated (the prime run is inside the alarm window; load; the L9 cells were IL). Cost to the cells: 5 trials x 60 s each.
* **js-1m (BD17's own revisit item "W1 measures whether js-1m drops toward x5.9"):** `wild-json-validate-onig` js-1m pcrec `_in` **18.19 ms** (auto) / 19.25 ms (vm) vs L9's 129.5 / 127.4 ms (614d45eb3, unprimed): x0.14.
  libpcre2 jit-deep 3.25 ms (L9 5.94-6.18), **interp-deep 37.9 ms (L9 455 ms, x0.083)**, onig-deep 77.3 ms (L9 76.2-76.8, flat). So the pcrec/jit-deep R1 ratio on js-1m is **x5.6** (L9: x21.9) -- BD17's prediction (L9's
  figure measured first-touch page faults) holds for pcrec; BD17's stated caveat that "pcre2-interp's heap ... allocated per call" would still pay is NOT what the records show (interp falls x12, Onig does not). The unprimed
  default-arm and primed `_in` figures are different protocols (R4-adjacent), so this is a protocol-change effect, not an engine change; no same-protocol cb32eda28-vs-614d45eb3 pair exists for the `_in` arm.
* **Callout fire counts are DOUBLED on every primed arm:** co-luhn-1m `callout_fires` 22,616 on pcrec `_in`, jit-deep, interp-deep and onig-deep vs 11,308 on the unprimed default arms (isbn 16,858 vs 8,429, member 26,316 vs 13,158,
  netstr consume 68,254 vs 34,127, netstr-assist 1,870,682 vs 935,341); L9 scratch (unprimed) read 11,308 everywhere. The untimed fire pass evidently counts the prime run too. Consequence: **every per-fire figure on a deep
  arm (`real - pass` / fires) is half the true value** (luhn vm_in 12.6 ns vs vm 26.1; the `_in`/deep callee shares and break-even lines in the reports' callout tables are halved); the fire COUNT equality check (real == pass) still
  holds. A harness finding for the manager (not an engine one).

### 1.6 Streams and vars (reporter `--grain stream`, rendered before the set grain)

* cscan seg-l, 4,096 calls: pcre2-jit-deep 14.44 ms (283.6k calls/s), onig-deep 145.8 ms, interp-deep 194.7 ms, **pcrec default 60.9 ms (67.3k calls/s, 58.9 MB/s), `_in` 46.2 ms (88.7k/s, 77.6 MB/s)** (L9: `_in` 46.6 ms; reproduced
  to 1 %). sqlite-bodies: jit 20.2, pcrec default 92.2, `_in` 72.4, onig 204, interp 303 ms. So pcrec's default arm is now complete at the compiler's access pattern but x4.2 behind pcre2-jit (x3.2 on `_in`), ahead of Onig x2.4
  (x3.1 `_in`) and interp x3.2. The `_in` arm is faster than the default by x0.75-0.78 on streams (the L9 note, "3-5 % slower", is for vars; here fast-tier escalation on cscan's deep calls).
* `_in` vs default on SHORT cells: median ratio 1.126 overall, but **cscan 43 / cscan-onig 41 / wild-json 148 + 146 / wild-sexp 3 short cells are >= 2x faster on `_in`** (e.g. cscan `cs-02` 411 -> 89 ns): the default arm's fast tier
  (`fast_frames 37`, `fast_trail 56`) overflows on those subjects and re-runs the call at the configured capacity ([OPT-1] two-tier; stamps read, mechanism not separately timed).
* **vars (D-5):** pcrec tenant ladder FLAT in d at cb32eda28 auto: 196.5 us (d4), 204.4 (d64), 217.2 (d4096) -- +10.5 % over x1,024 the distinct values (L9: +13 %); 614d45eb3 auto 196.3 / 206.0 / 221.4. D-5's "assist grows with d" half
  (re2/rust) is NOT re-measured: no re2/rust cell was in this window. Every vars call count equals the oracle's (matched/nomatch/refused 11,818/4,566/0 ... 2,137/1,758/201), 0 give-ups. Vars are on the separate-TU arms only.
* R1 (cell > 3x the best non-excluded engine) on large cells, pcrec `_in` vs best of {jit, interp, onig}-deep: **46 of 100 cells exceed 3x, 36 are pcrec-best** (jit-deep is the comparator on all 46): cscan nest-paren family x5.0-5.3,
  nest-brace x4.1-4.3, nest-digraph x4.0, wild-json js-1m / js-near-1m x5.4-5.6 (was x21.9), wild-sexp nest-paren x3.4-3.7. Short-subject set means: cscan x3.69, cscan-onig x3.70, wild-json x4.74 / x4.72 over jit-deep
  (L9: x3.6 / x4.8); callout members and the floor are 0.32-0.86 of jit-deep (pcrec ahead).

### 1.7 Charter-prediction scoring (bench/unusual/NOTES.md sections 4-5, scratch vs pinned)

| prediction | scratch (L9, 614d45eb3) | pinned (this window) |
|---|---|---|
| D-1 onig default silent wrong at nest level 20 | CONFIRMED | **not re-measured**: no `onig-default` (non-deep) cell in this window; onig-deep wrong rows = the DEFINE spelling only |
| D-2 jit default first give-up at 512 | confirmed | not re-measured (jit default arm absent); jit-deep 0 give-ups |
| D-2 pcre2-interp answers every rung | confirmed to 32k | **32k now timed-out at the 60 s alarm** (above) |
| D-2 pcrec default arm FRAMES from 512 | REFUTED (128 and flat input) | flat input now answered (K134); **128 still gives up**; `_in` answers all |
| D-5 vars flat in d / assists grow | CONFIRMED | pcrec half confirmed (+10.5 %); assist half not measured |
| R3 depth-of-failure table | | the stream report's depth section (`reports/...stream.md`) carries it for cscan, cscan-onig, floor, wild-sexp |

## 2. (b) capability@0.4 x pcrec-auto-noedge, against W2's same-pin `pcrec_cb32eda28_auto-caps-simdna` (store 69b9af2e record, 2026-11-01 13:39Z) -- CROSS-WINDOW

Source `an8`, `an9`. The noedge record is 2026-11-02 15:02Z; the auto record is W2's. Stamps confirm the arm: `-fno-scan-edge` gives `dfa_scan_edge none`, `scan_edges 0/0` on every named row; all other stamps equal.
Sentinel offset between the windows is ~ -5 % on short cells and ~0 on large cells (section 0), so short ratios below carry it.

| pattern (plain) | auto edge stamp | large noedge/auto | short noedge/auto |
|---|---|---|---|
| `wild-logparse-base10num-noatomic` | mixed, edges 2/1 (DFA) | **x0.823** (7.518 -> 6.186 ms) | x0.786 |
| `wild-logparse-base10num-grok` | mixed, edges 2/0 (VM, byte-class-bounded) | **x0.876** (9.810 -> 8.590 ms) | x0.837 |
| `wild-secrets-username-password-pair` | mixed, edges 3/0 (VM, `handoff`) | x1.046 | x0.963 |

**O-111 ask (a) answered: yes, the scan edge costs on base10num** -- denying it recovers 18 % (noatomic) / 12 % (grok) on the large cells, where the cross-window offset is zero (all 66 large cells: noedge/auto median 0.998, p5-p95
0.958-1.095), matching the 9ae59f5d4 -> 614d45eb3 slowdown b147read measured (x1.200 / x1.102). Short cells x0.79 / x0.84 are consistent after the -5 % offset (about x0.83 / x0.88). **username-password-pair: no cost** (large x1.046 is inside
the null, short x0.963 is the offset). Its stamp moved between the pins though: `dfa_prefilter byte-class` (614d45eb3) -> `handoff` (cb32eda28), emit 553,919 -> 555,019 B.
The same arm reproduces the edge's WIN where it is a win: `tail-space-eol` large auto 12,101 vs noedge 73,203 ns (**x6.05**), `tail-word-eoz` x5.69, `tail-digits-eol` x5.38, `letters-bounded-tail-z` x2.81 (b147read: `\s+$` x6.1).
Short cells overall noedge/auto median 0.960 (n=69) = the offset. Rule hits: R-STATUS-13 135 groups with no rankable reference arm (the set has no libpcre2 testee -- all ranking is pcrec auto vs noedge), R-ARM-1 (the arm pair), 6 excluded cells and
2 did-not-compile patterns (see the sidecar). Not read: nocaps (not in this window), the other 134 cells beyond the movers listed in `an8`.

## 3. (c) syntax@0.2 x {auto, nocaps, auto-noedge} at cb32eda28, against the 10-28 614d45eb3 records (window offset named)

The cross-pin pair is cb32eda28 (this window, 16:06-17:28Z... 11:05-13:09 EDT) vs 614d45eb3 (2026-10-28 21:12 / 21:56Z): **five days apart, a cross-WINDOW pair**; the reporter joins them (same `syntax@0.2`) and its null band reads
the records' `program_sha256_v3`. Short-cell offset ~ -4.5 % (section 0: pcrec 614 sentinel 0.956). Source `an8`, `an9`, `an14`.

* **Program identity (v3) over the 84 plain patterns compiled at both pins: 52 identical, 32 changed.** Identical: large set-sum cb/614 median **1.003** (p5-p95 0.981-1.024), short 0.975 (the offset).
  Changed: large median **0.827** (p5 0.137, min 0.133), short 0.842 (min 0.640). 27 of the 32 changed patterns show `dfa_scan unanchored -> cover` (abi 92 [MEMFN] S3; `dfa_start end-minus-width -> attempt-start`, the
  prefilter -> `none`), 11 `req_handoff`, 10 `req_why emitted -> dominated`. Largest: `mod-i`, `mod-r` x0.133 / x0.137 (3.96 -> 0.53 ms), `cls-n-uc` x0.438, `grp-callout` x0.446 (VM, `req_handoff none -> 0`, REQRUN-VM),
  `mod-s` x0.459, `esc-octal-0` x0.535 (the 10-28 record read 126k/160k bimodal, b147read), `asr-nwb` x0.603, `cls-i-class` x0.623.
* **`cls-s-uc` and `cls-range` (b147read's [SCANEDGE-SET] two-sign pair), program-identical at both pins:** `cls-s-uc` cb/614 large x1.001, short x0.986 -- the 614d45eb3 slowdown persists unchanged (x1.116 vs 9ae59f5d4 per b147read); with the
  edge denied (noedge/cb) large **x0.898**, short x0.920, whole-subject x1.082 (edge helps the whole form). `cls-range`: cb/614 large x1.014, noedge/cb large **x1.201** (the edge is a x0.83 win), short x1.020, whole x1.002.
  Edge shapes: `cls-s-uc` bitmap 2/1 (plain), `cls-range` bitmap 1/1.
* **noedge vs auto, same window (adjacent cells, no offset):** medians 1.000 on every regime; movers beyond 10 % large: `unp-p-lc` x1.356, `cls-w` x1.335, `cls-posix` x1.330, `mod-a` x1.325, `cls-range` x1.201, `rec-back` x1.160,
  `rec-g-angle` x1.154, `cls-d` x1.130, `rec-py` x1.106 (edge wins), `cls-s-uc` x0.898 (edge loses). The edge's two signs both reproduce on the same-window A/B that b147read only had cross-pin.
* nocaps cb32eda28 vs 614d45eb3 nocaps: `cls-s-uc` x1.022 large, `cls-range` x1.022.
* Not read: all 306 R-DELTA-1 firings individually (the sidecar aggregates them to 10 by regime x config x direction), the 55 did-not-compile rows (R-STATUS-4: 5 testees), the 25 excluded cells.

## 4. (d) sentinels (sentinel@0.1 x 4, opening 03:41-04:09 and closing 13:10-13:36)

Per-testee close/open on the 15 pattern cells: pcrec auto 1.001 (0.955-1.071), nocaps 0.998 (0.910-1.050), 614d45eb3 auto 1.004 (0.967-1.011), libpcre2-jit 0.9996 (0.844-1.035; the jit minimum is one cell). In-window cb32/614 auto: 0.992 at open,
0.996 at close (p5 0.85, the same one or two cells at both ends). So the window did not drift. The cross-WINDOW shift (section 0) is the thing to carry. Three R-STATUS-10 after-sample failures and R-FLOOR-1 on 28 compile ratios are in the sidecar.
Opening pass: three pre-flight refusals (nocaps 1, jit 2) before measuring.

## 5. Checks

`make check-interpret` in the worktree (see the lane report). Sidecars: four, deterministic (`cmp` clean), stamped against `store/index.tsv` at bbc5fb7a. No predictions file matches unusual@0.1, capability@0.4 or syntax@0.2.

## 6. Reader / harness findings (for the manager's KB list)

1. **Stream view is empty if the set grain is built first over the same loaded records.** `report.build_report` drops the call-stream rows from `LoadedRecord.rows` in place, so `report_stream.build_stream_report` over the same list
   prints "no ranked call-stream cell". `gen.py` builds the stream view first; the standalone CLI loads fresh and is unaffected. (First found as an empty `.stream.md` in this lane's first render.)
2. **Callout `callout_fires` double on every `--prime` arm** (1.5 above): per-fire figures and callee shares on deep arms are half; fix at the fire pass or declare it.
3. BD17's interp/Onig caveat is contradicted for interp (1.5): the revisit it names is answered for js-1m.
4. The `callout` section of the stream TSV is 8,424 of ~9,300 rows (short-subject zero rows); the committed `.stream.tsv` is 2.3 MB, `.stream.md` 1.4 MB, `.subject-grain.tsv/.md` 6.1 / 5.9 MB (< 50 MB warn).
