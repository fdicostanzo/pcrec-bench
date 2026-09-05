# THE LEDGER — the [B37] DENY-FLAG-SPLIT AFTER, pcrec pin `334fd10e` (abi 22)

Read-only extraction by lane b37read, 2026-09-05, over the 2026-09-05
DAYTIME window (03:48:36 → 07:22:14 EDT): `altwide@0.2` × {`auto`,
`auto-noisland`, `auto-nocaps`, `vm`, `vm-in`} (the [ENG-ISL] island's
pair and the set's AFTER), `loglines@0.1` × {`auto`, `auto-noedge`} (the
[OPT-EDGE] pair's THIRD sample; the abi-19/21 dispatch's AFTER), and
`bounded@0.3` × {`auto`, `vm`, `auto-clang`} (the [CC-DIFF] fold witnesses,
the `vm`-arm dispatch question, the I-37 cell). The pin carries SIX abi
steps over 288d505 (abi 16): [CC-DIFF] STEP 1's uniform-table fold (17,
`folds=`), the VM alternation ISLAND (18, `islands=`), the scan-edge
dispatch (19) and [OPT-EDGE] STEP 1.1 (21) — no stamp, .rxt composition
(20) — no stamp, [CC-DIFF] STEP 2's entry shape (22, `shape=<token> (prog:
N B)`). ONE CHANGE PER PIN cannot hold, so the AFTER is SPLIT BY DENY FLAG
inside the pin where a deny flag exists, and read CROSS-PIN where none
does. Scored against: **ledger 2026-09-05 §7** (the 12-point checklist,
"PRED" below), **inbox I-43** (the island's altwide facts; the [OPT-EDGE]
×0.9995), **I-44** (step11/after ≈ 0.99–1.01; the entry shape; "run your
gcc arm at this pin and read the stamp"), **I-41** (the fold sizes),
**ledger 2026-09-03 §2–§5** (altwide's first sample, P9–P18; the noedge
first sample) and **plan.md [B37]** (the re-pin's build facts).

Numbers only; the manager's interpretation goes to O-17.

**Ratio convention throughout: `A ÷ B`, so > 1 means A is SLOWER (or
larger).** Where a verdict reads `faster ×N` it is the reporter's own R8
column and N is a speed-up.

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE

**Records**: **10, every one `measured`, schema 1.5, tier `pinned`, machine
`budu-ryzen1600`, every one at attempt 1** (zero retries, zero cap kills,
zero `inconclusive-*`), store index 134 → 144, COMMITTED on master
(344ebb6) before this extraction; this lane read them from
`~/pcrec-bench/store` and commits none of them.

**Reports** (five groups × 3 files under `reports/`, reporter **v14
(2026-09-05)**, rendered in-process with the CLI-equivalence and
determinism checks recorded in `reports/CLAUDE.md`'s [B37] paragraph):

| cite | file group |
|---|---|
| `ISL:<line>` | `2026-09-05-altwide-0.2-budu-ryzen1600-island-334fd10e.md` (the pair, 2 records) |
| `ALT:<line>` | `2026-09-05-altwide-0.2-budu-ryzen1600-after-334fd10e.md` (cross-pin vs 1989c62, 11 records, 0 superseded) |
| `ALTS:<line>` | its `.subject-grain.md` |
| `NOE:<line>` | `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-334fd10e.md` (the pair, 2 records) |
| `NOX:<line>` | `2026-09-05-loglines-0.1-budu-ryzen1600-noedge-3pins-334fd10e.md` (three pins, 6 records) |
| `FLD:<line>` | `2026-09-05-bounded-0.3-budu-ryzen1600-fold-334fd10e.md` (cross-pin vs 288d505, 6 records, 0 superseded) |
| `FLDS:<line>` | its `.subject-grain.md` |
| `L1..L3` | `build/windows/window_altwide_isl_20260905T074836Z.log`, `window_loglines_edge_20260905T084536Z.log`, `window_bounded_fold_20260905T090230Z.log` (main tree) |

Everything marked **REC** was recomputed by this lane from the record files
with `pcrecbench.reduce.reduce_match_cell` / `reduce_set_cell` (median over
five trials of `elapsed_ns/iterations`) and agrees with the committed
renderings everywhere both exist. The BEFORE records: altwide = the
2026-09-03 1989c62 records (altwide was NOT measured at 288d505); loglines =
the 2026-09-05 288d505 pair (03:48:09Z / 03:56:40Z) and the 2026-09-03
1989c62 pair; bounded = the 288d505 records of the same night — `auto`
**04:10:50Z** (the ccboth pass; the six-testee 00:47:59Z record is quoted
beside it where they differ — they agree to median 0.9998, ledger
2026-09-05 §4.3), `vm` 02:12:49Z, `auto_cc-clang` 04:50:54Z.

### 0.1 The ten records

| # | set | testee (`pcrec_334fd10e_…`) | record ts (UTC) | cell wall (L1–L3) | pre-flight target busy % (max any core) | load1 before → after | TA rows judged / disagreeing (unjudged) | worst other-core busy % (where) |
|---|---|---|---|---|---|---|---|---|
| 1 | altwide | `auto` | 07:49:11 | 9.0 min | 1.2 (5.81) | 0.08 → 1.01 | 1,436 / 0 | **29.22** (`srt-256` thr, cpu0) |
| 2 | altwide | `auto_noisland` | 07:58:25 | 8.9 min | 0.0 (0.6) | 0.72 → 1.00 | 1,436 / 0 | 3.87 |
| 3 | altwide | `auto-nocaps` | 08:07:36 | 8.6 min | 0.8 (1.6) | 0.72 → 1.00 | 1,436 / 0 | 2.40 |
| 4 | altwide | `vm` | 08:16:26 | 14.5 min | 0.0 (1.0) | 0.72 → 1.03 | 1,844 / 0 (4) | 11.36 (`pfx3-512` thr, cpu0) |
| 5 | altwide | `vm-in` | 08:31:09 | 14.5 min | 0.2 (0.8) | 0.74 → 1.00 | 1,844 / 0 (4) | 4.49 |
| 6 | loglines | `auto` | 08:46:11 | 7.9 min | 0.4 (0.6) | 0.56 → 1.04 | 1,364 / 0 | 1.36 |
| 7 | loglines | `auto_noedge` | 08:54:20 | 8.2 min | 0.0 (0.8) | 0.74 → 1.04 | 1,364 / 0 | 2.82 |
| 8 | bounded | `auto` | 09:03:05 | 44.8 min | 0.0 (0.8) | 0.58 → 1.01 | 4,200 / 0 | 6.55 |
| 9 | bounded | `vm` | 09:48:10 | 45.7 min | 0.2 (0.8) | 0.73 → 1.00 | 4,300 / 0 | 7.34 |
| 10 | bounded | `auto_cc-clang` | 10:34:07 | 48.2 min | 0.0 (0.8) | 0.73 → 1.10 | 4,200 / 0 | **57.14** (`hex32` thr, cpu8) |

- **Pre-flight** (BD7's `mpstat` Average, target core, limit 10 %):
  **0.0 – 1.2 %, mean 0.28 %**, n=10; `load.verdict` `quiet` on all 10 —
  the quietest window yet (PRED point 10's cumulative band 0.40–7.85 %,
  n=66, is now **0.0–7.85 %, n=76**). The 1.2 % on record 1 is the
  suite's first cell (`max_busy_pct` 5.81 on another core, L1:2).
- **Trial agreement** (`v1.4-group`): `agree` on all 10 and **0 disagreeing
  rows of 23,424 judged; 0 groups of 714** — the first window with no
  disagreeing row at all (PRED point 10: "rows disagreeing 0–6 per
  record"). 8 rows unjudged (`few_timed_trials` 4 on each altwide VM arm).
  `inconclusive-spread` base rate: 0 in 10 (running 1 in 76).
- **Two other-core readings past 25 %**, both on cores the target (CPU 11)
  was not on: record 1 at `srt-256` / throughput (29.22 % on cpu0) and
  record 10 at `hex32` / throughput (57.14 % on cpu8). Neither moved its
  cell: `srt-256` throughput on `auto` reads 2,911,948 against 2,905,532 on
  the `noisland` twin measured nine minutes later (×1.002) and 2,916,179 at
  1989c62 (×0.999); `hex32` throughput on clang reads 259,073 against
  254,302 at 288d505 (×1.019) while the gcc arm, spike-free, moved
  ×1.051 on the same cell (255,810 → 268,965; REC). Recorded, not discarded.
- **Answers**: zero wrong answers, zero give-ups, zero time-outs on all 10
  (`matched-as-expected` 7,180 / 7,180 on each altwide auto-route record,
  9,240 on each VM arm, 6,820 loglines, 21,000 / 21,500 / 21,000 bounded;
  REC). Every pcrec disagreement with the oracle is a REFUSAL.

### 0.2 Cell wall clock against `scripts/CLAUDE.md`'s table

| set / testee | table | this window | |
|---|---|---|---|
| altwide@0.2, `auto` | 8.8 min (ledger 2026-09-03 §3.3) | **9.0** | in band |
| altwide@0.2, `auto-noisland` | "the `auto` figure plus a third" ≈ 11.7 (scripts/CLAUDE.md's estimate) | **8.9** | the estimate's premise (VM-selected forms carrying a chain) is EMPTY on this set — §1.1; the cell is `auto`'s to 1 % |
| altwide@0.2, `vm` / `vm-in` | 17.2 | **14.5 / 14.5** | 16 % UNDER, with four MORE compiled cells (44 vs 40): the compiled artifacts are smaller (§1.5) and the timing loops calibrate on a ×100 faster VM |
| loglines@0.1, gcc | 8.8 | 7.9 / 8.2 | in band |
| bounded@0.3, gcc worst | 48.4 (`vm-in`) | 45.7 (`vm`) | in band |
| bounded@0.3, clang | 49.4 | 48.2 | in band |

Suite wall 3 h 34 min (57 + 16 + 139 min per the suite log). No cell came
within 3× of the 5,400 s cap.

---

## 1. THE ISLAND (altwide@0.2)

### 1.1 The pair `auto` vs `auto-noisland` is a NULL PAIR — the deny flag has nothing to deny on this set

The deny arm is real: `build_flags` reads `pcrec flags --features all
-fno-alt-island` with the [B32] denied-axis sentence, `config_extra`
`noisland` (REC, the setup line). And it moves NOTHING:

- **Engine census on the auto route: 34 of 34 compiled (pattern × form)
  cells are `engine=dfa`, `sel=selected`; 32 refused** (the same 32 on both
  arms, the same diagnostics to the byte). No VM-selected form exists on
  `altwide@0.2` under `pcrec-auto` — `islands=` prints on NO legend line of
  ISL (0 occurrences), `folds=0` on all 34 (ISL:706 / ISL:740, the `w-256`
  pair).
- **Sizes byte-identical on all 34**: `emit_bytes` / `emit_code_bytes` /
  `artifact_bytes` equal on every cell (`w-256` plain 977,922 / 19,696 /
  306,048 on both, ISL:855 / ISL:857).
- **Timings**: 53 shared set cells; `noisland ÷ auto` = **0.9988–1.0040 on
  the 19 throughput cells, 0.9950–1.0086 on the 19 search cells,
  0.9918–1.0102 on the 15 match cells** (REC; e.g. `w-256` throughput
  2,899,328.6 vs 2,902,386.8, ISL:544–545). No Δ fires (the deny word
  lives in `config_extra`).

So the island's effect on altwide is NOT readable as a one-variable pair
at this pin. It is readable on the forced-VM arms (§1.2–1.6), CROSS-PIN
against 1989c62, where the VM artifact carries three abi-17..22 changes at
once: the island (abi 18), `always_inline` on the frameless helpers (abi 17
— every island artifact is `frameless=1`, §1.7), and the `shared` entry
shape (abi 22). The ONE-VARIABLE island reading of this window is on
bounded's `ctx-*` hybrids (§3.4), which are framed (`frameless=0`,
`shape=plain`) and so untouched by abi 17 and 22.

### 1.2 The island on the forced-VM route — every island-bearing cell, 1989c62 → 334fd10e

`pcrec_334fd10e_vm` ÷ `pcrec_1989c62_vm`, set grain (REC; ALT's Δ column
reads the reciprocals as `faster ×N`; `vm-in` agrees to ≤ 1 % on every
cell — its ratios are in brackets where they differ by > 0.5 %):

| pattern / form | `islands=` | code bytes 1989c62 → 334fd10e (ratio) | throughput | search | match (whole) |
|---|---|---|---|---|---|
| `s-512` | 1 | 474,309 → 348,052 (0.734) | **0.0032** | 0.0020 | 0.0014 |
| `s-256` | 1 | 242,286 → 185,044 (0.764) | 0.0079 | 0.0046 | 0.0031 |
| `sfx-256` | 1 | 412,930 → 366,454 (0.887) | 0.0080 | 0.0046 | 0.0032 |
| `w-256` | 1 | 341,111 → 292,043 (0.856) | **0.0082** | 0.0047 | 0.0036 |
| `nar4-256` | 1 | 365,440 → 298,224 (0.816) | 0.0046 | 0.0025 | 0.0049 |
| `w-192` | 1 | 258,989 → 224,235 (0.866) | 0.0120 | 0.0067 | 0.0051 |
| `wb-256` | 1 | 341,768 → 292,700 (0.856) | 0.0129 | 0.0104 | 0.0124 |
| `w-128` | 1 | 178,736 → 157,691 (0.882) | 0.0184 | 0.0106 | 0.0084 |
| `w-96` | 1 | 140,135 → 125,672 (0.897) | 0.0286 | 0.0199 | 0.0177 |
| `cnt-64` | **3** | 258,773 → 234,271 (0.905) | 0.0386 | 0.0336 | 0.0309 |
| `sh1-256` | 1 | 334,901 → 283,807 (0.847) | 0.0404 | 0.0390 | 0.1387 |
| `sfx-64` | 1 | 117,127 → 110,487 (0.943) | 0.0419 | 0.0306 | 0.0265 |
| `w-64` | 1 | 97,406 → 89,130 (0.915) | 0.0426 | 0.0299 | 0.0262 |
| `nar4-64` | 1 | 103,029 → 91,231 (0.886) | 0.0533 | 0.0285 | 0.0487 |
| `srt-256` | 1 | 301,957 → 292,043 (0.967) | **0.0729** | 0.0424 | 0.0512 |
| `sh1-64` | 1 | 91,046 → 82,728 (0.909) | 0.2345 | 0.2354 | 0.4938 |
| `w-8` | 1 | 25,393 → 24,923 (0.982) | 0.4289 | 0.2960 | 0.3554 [0.33] |
| `pfx3-256` | 1 | 285,306 → 231,659 (0.812) | **0.8037** | 0.7313 [0.72] | 0.9083 [0.85] |
| *control* `ci-256` (declined: class-leading) | 0, `shape=plain`, frames 256 | 450,860 → 451,050 (1.0004) | 1.0016 | 0.9978 | 0.9964 [0.985] |
| *control* `floor` (no alternation) | 0, `shape=forward`, frames 1 | 17,258 → 17,623 (1.021) | **2.0014** | 0.8904 [0.92] | **1.1128** [0.997] |

- **40 of the 44 compiled VM artifacts carry an island** (38 × `islands=1`,
  `cnt-64` × 2 with `islands=3`); `ci-256` (both forms) and `floor` (both
  forms) carry 0 — I-43's "declines class-leading alternations" holds on
  `ci-256` (§1.7: it is also the only VM artifact with `shape=plain` on this
  set).
- **Over the 54 island-bearing set cells the ratio is 0.0014–0.9083,
  median 0.0264**; throughput alone 0.0032–0.8037 (18 cells). The
  island's win scales with width: `w-8` ×0.43, `w-64` ×0.043, `w-128`
  ×0.018, `w-256` ×0.0082; `s-512` ×0.0032. `pfx3-256` gains least
  (×0.80): its chain already started with a `memchr` on the shared 3-byte
  prefix (2026-09-03 §2.8), so the island shortens only the branch walk.
- **Answer identity**: 9,240 / 9,240 rows `matched-as-expected` on both VM
  arms; no budget-bound cell differs between the arms (§0.1).
- **The `floor` control FIRED the forced-VM floor tripwire** (PRED point
  5): `floor` / throughput on `vm` 271,666 → **543,708 ns/set, ×2.0014**
  (ALT:332 table: 1989c62 rank 9, 334fd10e rank 11, `slower ×2.00`);
  per subject 0.296 → 0.593 ns/B on all four subjects (REC). The same cell
  on bounded reads the same ×1.996 (§3.3). `floor` search ×0.89, `floor`
  match ×1.11 (`vm-in` 0.92 / 1.00).

### 1.3 THE ORDER PAIR — `w-256` vs `srt-256` on the VM route: the ×8.87 is GONE

I-43: "w-256 and srt-256 now emit within 2 bytes of each other — the
×8.87/×20.1 branch-ORDER effect is gone at the source"; [B37]'s build
table: IDENTICAL in `emit_bytes` (292,043 each) and program bytes. The
window (REC; ALT:2447–2457 `w-256` throughput, ALT:1902–1912 `srt-256`
throughput, ALT:2541–2548 `w-256` search; ALTS the per-subject rows):

| quantity | `w-256` | `srt-256` | `w-256 ÷ srt-256` | at 1989c62 (2026-09-03 §2.5) |
|---|---|---|---|---|
| vm `emit_bytes` = code bytes | **292,043** | **292,043** | identical | 341,111 vs 301,957 (srt 11.5 % smaller) |
| vm `shape=` / program bytes | shared / **305,686** | shared / **305,686** | identical | — (no stamp) |
| vm `artifact_bytes` | 68,080 | 68,080 | identical | 87,952 vs 79,760 |
| vm gcc phase (median of 5) | 1.89 s | 1.88 s | — | 1.88 / 1.72 s |
| **vm throughput ns/set** | **15,886,650.0** | **15,875,364.4** | **×1.0007** | 1,931,273,182 vs 217,648,612 = **×8.87** |
| vm search ns/set | 44,420.2 | 44,364.9 | ×1.0012 | 9,470,938 vs 1,047,072 = ×9.05 |
| vm match ns/set (whole) | 384.9 | 382.9 | ×1.0052 | 108,217 vs 7,476 = ×14.5 |
| vm-in throughput / search / match | 15,891,676 / 44,350 / 407.7 | 15,891,862 / 44,365 / 409.0 | ×1.0000 / 1.0010 / 0.9968 | ×8.82 / 9.02 / 14.0 |
| auto throughput (DFA, both pins) | 2,899,328.6 | 2,911,948.0 | ×0.996 | ×1.006 |
| auto DFA artifact bytes (emit / code / .so) | 977,922 / 19,696 / 306,048 | 977,922 / 19,696 / 306,048 | **byte-identical** (ALT:4019 / 3911) | byte-identical (977,055 / 18,829 / 305,448) |
| jit throughput | 238,434,208.5 | 245,364,649.0 | ×0.972 | (same records) |

- **Per subject, vm throughput `w-256 ÷ srt-256`: 1.0007 / 0.9994 /
  1.0005 / 1.0014** on `t-128k-clean` / `-dense` / `-sparse` /
  `t-512k-sparse` (REC; 1989c62: 8.864 / 8.860 / 8.881 / 8.879).
  **CONFIRMED: the order effect is gone, to four figures.**
- **The absolutes**: `w-256` vm throughput moved **×0.0082** (1,931 ms →
  15.9 ms per set; the Δ column `faster ×121.57`, ALT:2451), `srt-256`
  **×0.0729** (`faster ×13.71`, ALT:1906); search ×0.0047 (`faster
  ×213.21`, ALT:2545) / ×0.0424; match ×0.0036 / ×0.0512. Both land on the
  SAME number because the island is the same trie for both spellings.
- **The DFA route is untouched by the island on this pair**: the two auto
  artifacts stay byte-identical to each other (as at 1989c62) and each
  moved +867 B across the pin (§1.8).

### 1.4 The refusal wall — `w-384` COMPILES on the VM route, and so does `pfx3-512`

I-43 / [B37]: "w-384 COMPILES on the VM route (427,824 B, cap 500,000)
where the chain was refused at 508,477; the VM wall moves 256<w≤384 →
384<w≤512; the DFA route's w-384 refusal unmoved". The window (ALT:4043
the compile row; ALT:2558–2565 throughput, ALT:2617–2625 search,
ALT:2596–2605 match; REC):

| cell | 334fd10e `vm` | `vm-in` | jit | interp | 1989c62 `vm` |
|---|---|---|---|---|---|
| `w-384` plain compile | **compiled, 427,824 B** (85.6 % of the cap), gcc 3.26 s, artifact 92,656 B, `shape=shared (prog: 456,975 B)`, `islands=1` | same | — | — | **refused at 508,517** (1.7 % over) |
| `w-384` throughput ns/set | **16,542,968.3** (18.03 ns/B; sd 118,935) | 16,734,286.9 | 411,250,824.0 | 3,492,010,278.0 | refused |
| `w-384` search ns/set | **53,296.1** | 52,614.8 | 1,893,000.1 | 15,880,500.1 | refused |
| `w-384` match ns/set (whole) | **401.7** | 409.0 | 76,997.9 (plain) | 77,069.6 | refused |
| `w-384 ÷ w-256`, vm throughput / search / match | ×1.041 / ×1.200 / ×1.044 | | | | |
| `w-384` vm ÷ jit | **0.0402** throughput, **0.0282** search | | | | |
| **`pfx3-512` plain compile** | **compiled, 440,187 B**, gcc 3.27 s, `prog: 483,720 B`, `islands=1` (ALT:3719) | same | — | — | refused at 562,897 (ALT:3709) |
| `pfx3-512` throughput / search / match | 2,708,750.4 / 15,494.5 / 327.5 | 2,689,344.5 / 14,045.5 / 367.1 | 815,003.8 / 7,507.0 | 273,812,803.5 / 1,136,325.7 | refused |
| `w-512` plain | **refused at 563,823** (12.8 % over; 1989c62: 678,310) | | | | |

- **The VM wall moved exactly as I-43 said: 384 < w ≤ 512 CONFIRMED**
  (`w-384` in, `w-512` out at 563,823). The VM refusal count fell **26 →
  22** of 66 (REC): `w-384` both forms and `pfx3-512` both forms now
  compile. `pfx3-512` is NOT in [B37]'s build facts or I-43's list — a
  second rung crossed the wall (the island shrinks `pfx3`'s program by
  0.812, §1.2, and 562,897 × 0.782 = 440,187 lands 12 % under the cap).
- The per-subject `w-384` throughput rows read 2,346,717 / 2,363,854 /
  2,384,145 / 9,446,369 ns against `w-256`'s 2,273,375 / 2,244,847 /
  2,268,161 / 9,103,521 (ALTS; ×1.03–1.05 on all four) — the island's cost
  per branch is close to flat between 256 and 384.
- **The DFA wall is unmoved**: `w-384` `auto` refuses at **1,432,392 B**
  of source (was 1,431,536; +856 is the dispatch's bytes, §1.8), `w-256`
  whole at 1,033,793 (was 1,033,155), `ci-256` whole 1,045,834; the auto
  refusal count stays 32 of 66 on all three auto-route arms, at 113.4–113.7
  s of refusal cost per pass (was 113.8; the most expensive refusal
  `s-4096` whole 32.50 s, was 32.58).
- **Every VM refusal diagnostic shrank** with the island: `w-512` 678,310
  → 563,823, `srt-512` 584,802 → 563,824 (the order pair's refusals also
  now 1 B apart, as their compiled siblings are 0 B apart), `s-2048`
  1,862,324 → 1,188,227, `s-4096` 3,741,040 → 2,236,549, `w-2048`
  2,757,095 → 2,124,737, `nar4-512` 700,057 → 544,925, `sh1-512` 656,433 →
  538,083; `ci-512` 900,858 → 901,048 (+190, the non-island control).

### 1.5 The code-byte ratios against [B37]'s build table

[B37] measured island ÷ chain at the SAME pin (the `-fno-alt-island` arm's
chain): `w-256` 0.8557, `pfx3-256` 0.8114, `s-256` 0.7631 (I-43: 0.856 /
0.812 / 0.764). The window's denominators are the 1989c62 chain (the only
chain the store holds for the VM arms), which is 98–275 B smaller than the
same-pin chain (the abi-17..22 stamp bytes, §3.6):

| pattern | window: 334fd10e island ÷ 1989c62 chain | [B37] same-pin | I-43 |
|---|---|---|---|
| `w-256` | 292,043 / 341,111 = **0.8562** | 0.8557 | 0.856 |
| `pfx3-256` | 231,659 / 285,306 = **0.8120** | 0.8114 | 0.812 |
| `s-256` | 185,044 / 242,286 = **0.7637** | 0.7631 | 0.764 |
| `srt-256` | 292,043 / 301,957 = 0.9672 | (−10,004 B vs 302,147) | — |
| `s-512` | 348,052 / 474,309 = 0.7338 | (−126,347 B) | — |
| `sh1-64` | 82,728 / 91,046 = 0.9086 | (−8,408 B) | — |

Agreement to 4 decimals on the three named ratios once the denominator's
+98 B is allowed for. `RX_VM_PROGRAM_BYTES` exceeds `emit_code_bytes` on
every island artifact (`w-256` 305,686 vs 292,043; `w-384` 456,975 vs
427,824; `s-512` 393,655 vs 348,052) — [B37]'s finding, reproduced on all
38 `shared` artifacts.

### 1.6 The VM against the JIT and against the DFA, at this pin

`vm ÷ jit`, set grain, plain form (REC; the ALT tables):

| pattern | throughput 334fd10e | throughput 1989c62 | search 334fd10e | search 1989c62 |
|---|---|---|---|---|
| `s-512` | **0.029** | 9.19 | 0.020 | 10.00 |
| `s-256` | 0.058 | 7.37 | 0.037 | 7.97 |
| `srt-256` | 0.065 | 0.887 | 0.037 | 0.877 |
| `w-256` | **0.067** | 8.10 | 0.039 | 8.26 |
| `sfx-256` | 0.068 | 8.49 | 0.051 | 10.94 |
| `w-192` | 0.096 | 7.97 | 0.057 | 8.43 |
| `w-128` | 0.176 | 9.55 | 0.106 | 9.98 |
| `w-96` | 0.186 | 6.50 | 0.142 | 7.16 |
| `wb-256` | 0.190 | 14.80 | 0.160 | 15.37 |
| `nar4-256` | 0.215 | 46.19 | 0.135 | 54.12 |
| `sh1-256` | 0.278 | 6.88 | 0.272 | 6.99 |
| `cnt-64` | 0.307 | 7.94 | 0.281 | 8.35 |
| `w-64` | 0.389 | 9.13 | 0.285 | 9.55 |
| `sfx-64` | 0.405 | 9.67 | 0.331 | 10.81 |
| `nar4-64` | 1.070 | 20.07 | 0.647 | 22.67 |
| `sh1-64` | 1.527 | 6.51 | 1.426 | 6.06 |
| `w-8` | 2.791 | 6.51 | 2.788 | 9.42 |
| `pfx3-512` | 3.324 | refused | 2.064 | refused |
| `w-384` | 0.040 | refused | 0.028 | refused |
| `pfx3-256` | 8.252 | 10.27 | 3.449 | 4.72 |
| `ci-256` (no island) | 7.945 | 7.93 | 8.385 | 8.40 |
| `floor` | 15.75 | 7.87 | 0.230 | 0.258 |

- **The VM beats the JIT on 32 of 44 shared cells at 334fd10e; it beat it
  on 3 of 40 at 1989c62** (`srt-256` throughput and search, `floor`
  search). P11's "vm ÷ jit within a factor 1.5 of itself across rungs
  8..384, no crossing" (2026-09-03 §2.4) is now REFUTED in the VM's
  favour: the ratio runs 2.79 → 0.040 over `w-8` → `w-384` (a factor 70),
  crossing 1.0 between `w-8` and `w-64`.
- **`vm ÷ auto`** on the island forms is **3.8–8.0 throughput / 4.8–12.1
  search** (REC; `w-256` 5.48 / 5.83, `w-8` 4.08 / 6.81, `pfx3-256` 7.96 /
  12.12) — the DFA is still ahead on every compiled cell but the margin is
  no longer ×660 (`w-256` throughput at 1989c62).
- **Match (whole) on the VM route is now BELOW the DFA's on every island
  form**: `vm ÷ auto` 0.75–0.86 (`w-64` 434.7 vs 503.2, ALT:2775 /
  2779; `s-256` 371.5 vs 451.8) — at 1989c62 the same ratio was 19–376.

### 1.7 `shape=`, `frameless=`, `islands=` — the census

Per record, over every compiled artifact (REC; ALT's legend lines carry the
same values):

| record | `shape=shared` | `plain` | `forward` | `inline` | `islands=` 1 / 3 / 0 | `frameless=` 1 / 0 |
|---|---|---|---|---|---|---|
| altwide `vm`, `vm-in` (44 compiled) | **38** (all > 4,096 program B: 8,558 `w-8` … 483,829 `pfx3-512` whole) | 4 (`ci-256` ×2 at 442,627 B / frames 256; `cnt-64` ×2 at 240,561 B / frames 3) | 2 (`floor` ×2, 236 / 339 B) | **0** | 38 / 2 / 4 | 40 / 4 |
| altwide `auto`, `auto_noisland`, `auto-nocaps` (34 compiled) | 0 (all DFA) | 0 | 0 | 0 | absent | absent |

- pcrec's AUTO rule (framed → `plain`; frameless ≤ 4,096 B → `forward` /
  `inline`; > 4,096 → `shared` / `plain`) holds on **44 of 44** VM
  artifacts. `inline` prints nowhere in the wave (bounded and loglines
  included, §3.7): no bench artifact is a frameless chain under 4,096 B
  with the shape pcrec inlines.
- `frameless=1` on exactly the 40 island-or-floor artifacts; `cnt-64`
  (`\b`-counted, frames 3) and `ci-256` (frames 256) are the framed ones.
  `frameless=` == `resume_frames == 1` on 44 / 44.

### 1.8 The DFA route across the pin (1989c62 → 334fd10e) — the control, and the match-axis movement

`pcrec_334fd10e_auto ÷ pcrec_1989c62_auto`, set grain (REC; ALT's Δ column
on the auto rows):

| regime | n cells | ratio range | Δ column reads |
|---|---|---|---|
| `large-subject-throughput` | 19 | **0.982 – 1.026** (`w-96` 0.982, `nar4-64` 1.026) | `unchanged` ×10, `slower ×1.00–1.03` ×5, `faster ×1.00–1.02` ×3, `cnt-64` `faster ×1.37` |
| `short-subject-search` | 19 | **0.949 – 1.027** — the `w-*` ladder 0.957–0.968, `ci-256` 0.949, `cnt-64` **0.504** | `faster ×1.03–1.04` on the six `w-*` rungs and `srt-256`/`pfx3-256`, `faster ×1.05` `ci-256`, **`faster ×1.98` `cnt-64`**, `slower ×1.02–1.03` on `s-256`/`s-512`/`sfx-*`, `unchanged` ×4 |
| `match-compliance` (whole) | 15 | **0.571 – 0.919** | `faster ×1.09` (`floor`) … `×1.75` (`w-64`, `w-128`) on 14, `unchanged` on `nar4-256` (its 1989c62 spread) |

- **`cnt-64`** (`\b`-counted; `edges=8 (match: 4)`, the set's most
  edge-bearing DFA) moved ×0.504 search / ×0.729 throughput — the
  abi-19/21 dispatch on the pattern with the most edges, the same shape
  loglines' `iso-ts` shows (§2).
- **Every whole-subject `match-compliance` cell moved 0.57–0.92**
  (`w-64` 880.4 → 503.2, ALT:2776 / 2779; `w-128` 886.2 → 505.5; `s-256`
  714.2 → 451.8; `floor` 413.8 → 380.2). Per subject on `w-64` (ALTS): the
  18 FAILING subjects 0.29–0.79 (`f-near` 72.5 → 21.3, `f-cnt2` 73.0 →
  22.6, the sixteen `f-*` at ~19.5 → 10.9–11.0), the 22 matching subjects
  0.79 flat (13.9 → 11.0). Every one of these artifacts is `edges=2–4
  (match: 2–4)`, `match=unwrapped`, `start=reverse-pass`, `folds=0`; the
  `floor` whole (`edges=0/0`) moved 0.919 too, so the dispatch is not the
  whole of it. NOT one-variable: abi 16–22 all lie between the two records.
- **Sizes** (auto, emit bytes): every plain DFA **+856…+869** (= the abi-16
  +110 plus 746–759 B of dispatch on `edges=2–4`; `w-256` 977,055 →
  977,922 = +867, ALT:4011 / 4019; `sh1-64` +858 = 110 + 748, [B37]'s
  figure to the byte), every whole **+627…+640**, `floor` **+141** (= 110 +
  31); `artifact_bytes` +600 on 30 of 34, +4,696 on `floor` plain/whole,
  `w-192` plain and `w-96` whole (page alignment).

### 1.9 P9–P18 re-scored where the window can

| # | 2026-09-03 verdict | at 334fd10e |
|---|---|---|
| P9 (auto flat band) | CONFIRMED | still flat: auto 2.26 (`w-8`) – 3.43 (`w-64`) ms, 2.90 at `w-256`; unchanged |
| P11 (vm ÷ jit within 1.5× of itself, no crossing) | CONFIRMED | **REFUTED** — 2.79 → 0.040 over the ladder, crosses below 1.0 by `w-64` (§1.6) |
| P12 (srt vs w: DFA byte-identical, VM 10–15 % apart) | CONFIRMED | the DFA half holds (byte-identical); the VM half's premise is REMOVED — 0 B, ×1.0007 (§1.3) |
| P13 (`s-512` VM code within ±10 % of the cap, 0.71 × `w-512`) | CONFIRMED | `s-512` 348,052 = **69.6 % of the cap** (was 94.9 %); 0.617 × `w-512`'s 563,823 |
| P14 (`s-256 ÷ w-256` = the byte ratio 0.71 on the VM) | CONFIRMED exactly | now **0.634** (185,044 / 292,043) — the trie ratio 0.61 fits the island where the byte ratio fit the chain |
| P18 (refusal-cost asymmetry) | CONFIRMED ×190 | ×142 (113.7 s over 32 vs 0.8 s over 22); VM compiled sum 74.4 s vs auto 13.5 s (was 66.8 / 13.1) |
| the wall (§3.1 of 2026-09-03: "both routes cross at the same rung") | 256 < w ≤ 384 both | **DFA 256 < w ≤ 384, VM 384 < w ≤ 512** — the coincidence is broken (§1.4) |

---

## 2. [OPT-EDGE] — THE THIRD SAMPLE, AND THE DISPATCH'S AFTER (loglines@0.1)

### 2.1 The pair at 334fd10e beside the two earlier samples

`noedge ÷ auto` (below 1 = the edge COSTS); NOE:325–326 `iso-ts` search,
NOE:289–290 throughput; the 288d505 and 1989c62 columns from ledger
2026-09-05 §2.1 (REC for all):

| pattern | `edges=` (s / m) | search 334fd10e | 288d505 | 1989c62 | thr 334fd10e | 288d505 | 1989c62 |
|---|---|---|---|---|---|---|---|
| **`iso-ts`** | 8 / 4 | **0.9846** | 0.9157 | 0.9181 | **0.9945** | 0.9388 | 0.9373 |
| `http-5xx` | 1 / 1 | 0.9811 | 0.9747 | 0.9713 | 0.9985 | 0.9680 | 0.9714 |
| `ipv6` | 1 / 0 | 0.9926 | 0.9744 | 0.9778 | 0.9829 | 0.9751 | 0.9755 |
| `bignum` | 0 | 1.0032 | 0.9917 | 1.0126 | 1.0008 | 0.9997 | 0.9923 |
| `floor` | 0 | 0.9977 | 0.9970 | 1.0008 | 1.0009 | 1.0011 | 0.9991 |
| `hex32-id` | 0 | 1.0087 | 0.9966 | 0.9986 | 1.0035 | 0.9921 | 1.0012 |
| `ipv4` | 0 | 1.0013 | 1.0005 | 1.0016 | 0.9984 | 1.0016 | 1.0041 |
| `kv-quoted` | 0 | 1.0108 | 1.0031 | 1.0030 | 1.0029 | 0.9839 | 0.9988 |
| `level-context` | 0 (`islands=2`) | 0.9994 | 1.0019 | 1.0005 | 1.0008 | 1.0012 | 0.9965 |
| `stack-frame` | 0 | 1.0001 | 1.0009 | 0.9990 | 0.9995 | 0.9987 | 0.9999 |
| `uuid` | 0 | 1.0006 | 1.0013 | 0.9960 | 1.0003 | 1.0015 | 0.9966 |

- **The scan edge's cost on `iso-ts` fell from ×1.092 / ×1.065 to ×1.016
  search / ×1.006 throughput** (`auto ÷ noedge`). I-43 predicted
  branch/noedge ×0.9995 on pcrec's harness; I-44 "step11/after ≈
  0.99–1.01"; our instrument reads **1.0156 / 1.0055** — inside I-44's
  band on throughput, 0.6 % outside it on search. The residual is
  concentrated: per subject on throughput (NOE's sweep; REC) the `hit`
  flavour reads noedge ÷ auto 1.039 / 1.055 / 1.018 / 1.006 at 16 K / 64 K /
  256 K / 1 M (the edge now WINS on the matching subjects), `fail` 1.041 /
  1.005 / 1.009 / 0.994, `syslog` 0.995 / 0.980 / 0.969 / 0.966 (the edge
  still costs 3 % on syslog text).
- `http-5xx` and `ipv6` moved the same way (0.975 → 0.981 / 0.993 search).
  The eight zero-edge patterns sit at 0.998–1.011 — `kv-quoted` search
  1.0108 and `hex32-id` 1.0087 are the widest, both with the edge-free
  artifact 6 B larger, as before.
- The arm is still one-variable: `edge=`/`edges=` to `none`/`0` on the
  three edge patterns and nothing else differs on any of the 22 legend
  pairs (`folds=0` on all 22 both arms; `islands=2`, `shape=plain (prog:
  12,026 B)`, `frameless=0` on `level-context` both arms — NOE:516 /
  NOE:538 the `iso-ts` pair).

### 2.2 `auto` across the pin 288d505 → 334fd10e (22 cells) — where the dispatch's win landed

NOX's Δ column (the 334fd10e auto rows against the 288d505 ones; REC):

| pattern | search 334fd10e ÷ 288d505 | thr | Δ (NOX) | emit bytes 288d505 → 334fd10e |
|---|---|---|---|---|
| **`iso-ts`** | **0.9311** | **0.9437** | `faster ×1.07` / `×1.06` (NOX:785 / 692) | 32,717 → **34,185 (+1,468)** plain; 38,444 → 39,290 (+846) whole |
| `http-5xx` | 0.9969 | **0.9725** | `faster ×1.03` thr | 51,785 → 52,302 (**+517**) |
| `ipv6` | 0.9814 | 0.9926 | `faster ×1.02` search | 25,332 → 25,725 (**+393**) |
| the eight zero-edge | 0.9873 – 1.0045 | 0.9929 – 1.0045 | `unchanged` / `faster ×1.01` / `slower ×1.01` | **+31** each (`floor` 18,075 → 18,106; `uuid` 31,364 → 31,395) |
| `level-context` (hybrid) | 0.9995 | 0.9972 | `unchanged` | 76,182 → 76,384 (+202) |

- The three edge patterns recovered 0.93–0.99 of their edge cost across
  the pin; the 19 edge-free cells sit at 0.987–1.005 (the same-pin floor
  of ledger 2026-09-03 §5.6 was 1.32 %).
- **The `noedge` arm is FLAT across all three pins**: `iso-ts` throughput
  1,142,842 (1989c62) / 1,142,674 (288d505) / 1,142,263 (334fd10e) ns/set
  — NOX:689–691, `unchanged (within spread)` twice; search 20,494 / 20,438
  / 20,462 (NOX:782–784). `noedge ÷ noedge` across the pin 0.9949–1.0121
  on all 22 cells. The deny arm is the control that says the pin moved
  nothing on loglines EXCEPT the edge's dispatch.
- 73 of NOX's 88 Δ cells read `unchanged (within spread)`; the 15 firings
  are the three edge patterns' six auto cells (`faster ×1.02–1.07`) and
  nine `×1.00–1.01` noise cells.
- **Sizes**: the dispatch costs `iso-ts` **+1,468 B** on 8 + 4 edges,
  `http-5xx` +517, `ipv6` +393, everything else +31 — [B37]'s size books
  to the byte. The `noedge` artifacts moved +31 (`iso-ts` 27,898 → 27,929;
  REC), so the noedge side is now 6,256 B SMALLER than auto on `iso-ts`
  (was 4,819 smaller) — the edge's byte cost grew by exactly the dispatch's
  1,437 B. `artifact_bytes`: `iso-ts` plain 27,560 → 31,656 (+4,096, page
  alignment), everything else +312 / +48.
- `level-context` stamps `islands=2` and did not move (0.9995 / 0.9972):
  the two islands live under a `collapsed-prefilter` hybrid whose cost is
  the prefilter DFA's, not the program's (contrast §3.4).

---

## 3. BOUNDED@0.3 — THE FOLD WITNESSES, THE VM DISPATCH, THE I-37 CELL, THE LADDER

### 3.1 The fold witnesses ([B33] (3), I-41)

I-41 predicted (pcrec's gcc): `cls-upto-4` `.rodata` 627 → 47 B, `dig-upto-16`
forced-VM `.text` 1,561 → 1,417 B; [B37] measured on this box's gcc `-O2 -c`
of the artifact alone: `cls-upto-4` `.text` 681 → 537 / `.rodata` gone,
`dig-upto-16` vm `.text` 1,449 → 633. The RECORDS carry `emit_bytes` /
`emit_code_bytes` / `artifact_bytes` (the `.so`), not sections (REC; FLD's
compile table FLD:4178 / 4184 for `cls-upto-4` auto, FLD:4374 / 4380 for
`dig-upto-16` vm):

| witness | stamps at 334fd10e | emit 288d505 → 334fd10e | code | `.so` | compile (median, ms) |
|---|---|---|---|---|---|
| `cls-upto-4` plain, `auto` (gcc) | `folds=4`, `start=pinned`, `edges=1` | 16,292 → **16,553 (+261)** | 12,949 → 13,598 (+649) | 22,920 → **22,936 (+16)** | 148.1 → 141.4 |
| `cls-upto-4` plain, `auto-clang` | same | same | same | 22,336 → 22,648 (+312) | 180.7 → 178.4 |
| `cls-upto-4` whole (control: `folds=0`, `reverse-pass`) | `folds=0` | 22,211 → 22,242 (+31) | +31 | 27,352 → 27,664 (+312) | 154.3 → 156.9 |
| `dig-upto-16` plain, `vm` | `shape=forward (prog: 646 B)`, `frameless=1`, `islands=0` | 17,882 → **18,157 (+275)** | +275 | 22,704 → 22,984 (+280) | 160.1 → 157.3 |
| `dig-upto-16` plain, `auto` (DFA control) | `folds=0`, `edges=2 (match: 1)` | 21,570 → 22,654 (+1,084) | +1,084 | 27,208 → 27,520 (+312) | 159.8 → 168.7 |

**Timings** (set grain; FLD:855–860 `cls-upto-4` throughput, FLD:2196–2201
`dig-upto-16` match, FLD:2144–2149 `dig-upto-16` throughput; REC):

| witness cell | 334fd10e | 288d505 (04:10Z; 00:47Z) | ratio | Δ (FLD) |
|---|---|---|---|---|
| `cls-upto-4` / throughput / `auto` | **200,391.4** | 319,394.8; 319,094.6 | **0.627** | `faster ×1.59` |
| `cls-upto-4` / search / `auto` | 454.1 | 526.8; 527.1 | 0.862 | `faster ×1.16` |
| `cls-upto-4` / match (whole; `folds=0`) / `auto` | 531.1 | 545.6 | 0.974 | `faster ×1.03` |
| `cls-upto-4` / throughput / `auto-clang` | 150,264.5 | 153,658.9 | 0.978 | `faster ×1.02` |
| `cls-upto-4` / throughput / `vm` (no fold; `forward`) | 291,053.9 | 448,349.7 | 0.649 | `faster ×1.54` |
| `dig-upto-16` / match (whole) / `vm` | **551.9** | 710.9 | **0.776** | `faster ×1.29` |
| `dig-upto-16` / search / `vm` | 2,622.6 | 4,010.5 | 0.654 | `faster ×1.53` |
| `dig-upto-16` / throughput / `vm` | 197,970.3 | 333,161.3 | 0.594 | `faster ×1.68` |
| `dig-upto-16` / throughput / `auto` (DFA, `folds=0`) | 75,226.0 | 84,177.7; 84,548.0 | 0.894 | `faster ×1.12` |
| `dig-upto-16` / throughput / `auto-clang` | 65,177.1 | 89,626.9 | 0.727 | `faster ×1.38` |

- The two fold witnesses' `.so` files moved **+16 B** (`cls-upto-4` gcc)
  and **+280 B** (`dig-upto-16` vm) where every non-fold DFA artifact moved
  +312 B and every framed VM artifact +312 — the fold's saving is visible
  as the gap between +16 and +312 (≈ 296 B on the linked object, gcc arm),
  not as a negative delta: the abi-17..22 stamp block (+261 / +275 B of
  source) is larger than the tables folded away.
- `cls-upto-4`'s throughput ×0.627 on gcc is NOT the fold alone: the whole
  pinned ladder moved (§3.5), and clang's arm (the same fold, `folds=4`)
  moved only ×0.978 on the same cell. `dig-upto-16` on `vm` ×0.59–0.78 is
  the frameless VM population's move (§3.2), shared with every `forward`
  artifact.

### 3.2 The `vm` arm's failing-call dispatch — moved AGAIN, past the 1989c62 value

PRED point 4: `floor` match 5.6 ns/subject (275.2 ns/set), every rung's
`d-01024` 10.2; "a move back to 5.0 / 9.1 is the abi-16 regression
undone". Measured (FLD:2688–2693 the `floor` match table; FLDS:2787–2798
`cls-upto-1024` / `d-01024`; REC):

| cell (`vm` arm) | 1989c62 | 288d505 | **334fd10e** | 334fd10e ÷ 288d505 |
|---|---|---|---|---|
| `floor` / match (whole), ns/set | 246.2 | 275.2 | **275.2** | **0.9998** — `unchanged (within spread)` (FLD:2690) |
| — per subject (49, all alike) | 5.02–5.03 | 5.61–5.64 | **5.61–5.63** | the +0.6 ns PERSISTED |
| `d-01024` on `cls-upto-4` … `cls-upto-65535` (16 rungs, whole) | 9.0–9.2 | 10.2–10.3 | **7.0** (7.3 on `cls-upto-32/64`; 8.7 / 9.5 / 8.9 on `cls-upto-4/8/16`) | **0.686** (0.84–0.92 on the four lowest rungs) |
| `d-01024` on `grp-upto-1024` | 9.1 | 10.2 | 7.0 | 0.686 |
| `d-01024` on `cls-atleast-4096` | 10.9 | 11.3 | 9.6 | 0.847 |
| `d-01024` on `cls-lazy-16384` (framed, `plain`) | 11.9 | 11.9 | 11.9 | 0.996 — the framed control did not move |
| `floor` / throughput, ns/set (0.296 ns/B at 288d505) | 31,574.6 | 31,637.5 | **63,140.3** | **1.996** — `slower ×2.00` (FLD:2641); 0.593 ns/B on all five subjects (1.980–1.998) |
| `floor` / search | 1,106.6 | 1,063.5 | 1,496.4 | 1.407 |

- **The failing dispatch on the cls rungs went 9.1 → 10.2 → 7.0 ns**: the
  abi-16 +1.1 ns is not merely undone, the call is 2.1 ns UNDER 1989c62 —
  on exactly the artifacts that stamp `shape=forward`, `frameless=1`. The
  `floor` MATCH cell (also `forward`, 236 B program) did NOT move (5.6 kept),
  so two `forward` artifacts read opposite ways on the failing-call axis.
- **The forced-VM floor tripwire FIRED** (PRED point 5): `floor` throughput
  ×1.996 on bounded, ×2.001 on altwide (§1.2), 0.296 → 0.593 ns/B. PRED
  said "a return toward 2.66 ns/B is the frameless shape lost"; the shape
  is NOT lost (`frameless=1`, `shape=forward` on `floor`), and the number
  is ×2.0, not ×9. `floor`'s program is 236 B — the smallest in the set —
  and it is the only `forward` artifact whose throughput got slower.
- The `vm` arm over all 129 set cells, 334fd10e ÷ 288d505 (REC): match
  median **0.904** (p10 0.745, min 0.646 `ctx-lazy-64` whole, max 1.019),
  search median **0.836** (min 0.517 `dig-upto-2`, max **1.407 `floor`**),
  throughput median **0.703** (min 0.503 `dig-exact-2`, max **1.996
  `floor`**); 101 of 129 cells past ±5 %. The digit family leads: `dig-*`
  throughput 0.503–0.597, search 0.517–0.680; `year4` throughput **0.572**
  (the 288d505 ×1.163 regression more than undone: 337,879 → 193,259);
  `nest3-3` throughput 0.709 / search 0.759 (the 288d505 ×1.41 / ×1.32 undone
  and past); `hex32` 0.659 / 0.632. The framed (`shape=plain`) artifacts:
  `cls-lazy-16384` 1.000 / 1.031 / 0.999, `csv5` 1.000 / 1.001 / 0.995,
  `dotted4` 1.029 / 1.013 / 0.986, `nest2-64` 1.003 / 1.001 / 0.996 — flat
  except `nest2-4` throughput **×1.362** (465,148 → 633,363) and `pw-8-64`
  search ×1.101, both framed.
- **Three noisy rows on the `vm` arm**, all matching-subject `r-01024`
  cells: `cls-upto-1024` whole 710.2 ns median with per-trial 690 / 830 /
  683 / 710 / 872 (sd 78; 288d505 632.4 sd 0.4), `grp-upto-1024` 655.6 sd
  62, `cls-upto-512` 322.2 sd 48 — the v1.4 rule did not fire (872 / 710 =
  1.23 < k). The rungs on either side read 621.0 (`cls-upto-2048`) and
  318.5 (`r-00512`), so the true `cls-upto-1024` / `r-01024` value is
  ≈ 621 (×0.98), and the 710 / 1.123 in FLDS:3557ff is the noise. `vm-in`
  was not measured at this pin (no control for the `_in` entry).

### 3.3 The I-37 cell — both arms at the pin, and the stamp that is not there

FLD:2688–2693 (`floor` / `match-compliance` / whole; REC for the trials):

| arm | 334fd10e | 288d505 | ratio | per subject (49) | Δ (FLD) |
|---|---|---|---|---|---|
| gcc (`pcrec-auto`) | **459.6** (sd 4.1; trials 451.7 / 460.4 / 451.4 / 459.6 / 459.7) | 492.2 (04:10Z); 492.9 (00:47Z); 503.3 (1989c62) | **0.934** | 9.33–9.40 ns (was 10.04–10.13) | `faster ×1.07` |
| clang (`pcrec-auto-clang`) | **217.1** (sd 0.0) | 231.5; 217.5 (1989c62) | 0.938 | 4.43–4.45 ns (was 4.72–4.73) | `faster ×1.07` |
| **clang ÷ gcc** | **0.4725** | 0.470 (288d505); 0.432 (1989c62, two windows) | | | |
| `vm` (`forward`, 236 B) | 275.2 | 275.2 | 1.000 | 5.61–5.63 | `unchanged` |

- **I-44's instruction — "run your gcc arm at this pin and read the
  stamp" — cannot be carried out on this cell: the I-37 cell is a DFA
  artifact** (`engine=dfa`, `match=unwrapped`, `start=reverse-pass`,
  `folds=0`, `edges=0/0`; emit 20,449 B, +31 across the pin) and
  `RX_VM_ENTRY_SHAPE` is a VM-scope stamp. No `shape=` prints on it, on
  either arm (FLD's legend lines for `floor` carry `folds=0` and no
  `shape=`). The VM artifacts under `auto` that DO carry the stamp are
  `cls-upto-32768` plain / whole and `cls-upto-16384` whole (`forward`,
  653 / 756 B, `frameless=1`) and the eleven framed hybrids (`plain`,
  §3.7).
- Both arms moved the same ×0.93–0.94 across the pin, so the ratio is
  0.4725 (was 0.470). The gcc arm's per-subject cost is now **9.3–9.4 ns**
  against pcrec's hand-driver 6.3 ns (307 ns / 49); the gap is 3.0 ns per
  call, was 3.7–3.9. clang's 4.4 ns is the 1989c62 value again (217.5 →
  231.5 → 217.1: the 288d505 +6.4 % was a one-pin excursion).
- **On the VM artifacts that DO stamp `shape=`, gcc vs clang at this pin
  (REC)**: `cls-upto-32768` plain (`forward`) throughput gcc 172,351.8 /
  clang 160,302.5 = **0.930** (288d505: 0.630 — gcc moved ×0.702, clang
  ×1.036), search 0.944 (was 0.812); `cls-upto-32768` whole match gcc
  1,832.5 / clang 2,017.5 = **1.101** (was 0.984; gcc ×0.904, clang ×1.011).
  The `forward` shape gave gcc the ×0.70 that clang already had; clang did
  not move on it. `ctx-lazy-64` whole (`plain`, `islands=2`): gcc 1,211.6 /
  clang 1,151.9 = 0.951 (was 1.106; both arms ×0.65 / ×0.56 — the island,
  §3.4).
- The 2026-09-05 §4.2 rows at this pin: `cls-upto-4` thr clang ÷ gcc
  **0.750** (was 0.481: gcc ×0.627, clang ×0.978); `cls-upto-4` match 0.496
  (0.503); `ctx-lazy-64` search 1.305 (1.349); `nest3-16` thr 1.211
  (1.138); `dig-upto-16` match 0.694 (0.682); `cls-atleast-4096` thr 1.186
  (1.167). Whole-set clang ÷ gcc medians at 334fd10e: match **0.831**,
  search **0.961**, throughput **0.935** (288d505: 0.835 / 0.965 / 0.872 —
  throughput closed by 6 points because gcc's ladder moved and clang's did
  not, §3.5).
- **clang across the pin, 126 cells**: median 0.991, 44 past ±5 %; the
  movers are the four `ctx-*` match wholes 0.559–0.675 (the island) and
  fourteen `dig-*` / `nest*` / `cls-upto-16..128` throughput / search cells
  0.711–0.890; the one regression **`dig-upto-8` throughput ×1.336** (64,248
  → 85,843) and search ×1.182, on clang only (gcc reads 0.859 / 0.936 on
  the same cells).

### 3.4 The one-variable island reading: bounded's `ctx-*` hybrids (`islands=2`, framed)

Under `auto` the four `ctx-*` patterns are `sel=collapsed-prefilter` VM
hybrids stamping **`islands=2`, `shape=plain (prog: 9,357–9,681 B)`,
`frameless=0`, `resume_frames 2`** — framed, so abi 17's `always_inline`
(frameless-gated) and abi 22's shape (`plain` = the pre-abi-22 entry)
leave them alone; the only abi-17..22 content on these artifacts is the
island and +187 B of stamp block (59,642 → 59,829). FLD:1786–1791
(`ctx-lazy-64` match); REC:

| cell (`auto`, gcc) | 288d505 | 334fd10e | ratio | Δ (FLD) | clang | `vm` arm |
|---|---|---|---|---|---|---|
| `ctx-lazy-64` / match (whole) | 1,862.5 | **1,211.6** | **0.651** | `faster ×1.54` | 0.559 | 0.646 |
| `ctx-lazy-256` / match | 2,162.1 | 1,450.5 | 0.671 | `faster ×1.49` | 0.582 | 0.657 |
| `ctx-lazy-1024` / match | 2,165.3 | 1,448.6 | 0.669 | `faster ×1.49` | 0.582 | 0.654 |
| `ctx-greedy-256` / match | 988.2 | 668.8 | 0.677 | `faster ×1.48` | 0.675 | 0.716 |
| `ctx-lazy-64` / search | 8,898.2 | 8,377.7 | 0.942 | `faster ×1.06` | 0.910 | 0.706 |
| `ctx-lazy-256/1024` / search | 9,616.9 / 9,620.2 | 8,809.2 / 8,821.9 | 0.916 / 0.917 | | 0.873 / 0.875 | 0.707 / 0.709 |
| `ctx-greedy-256` / search | 7,182.4 | 7,193.7 | 1.002 | `unchanged` | 1.020 | 0.774 |
| `ctx-lazy-*` / throughput | 197,329–197,409 | 200,163–200,449 | **1.014–1.016** | `slower ×1.01` | 0.996–0.999 | 0.867–0.869 |
| `ctx-greedy-256` / throughput | 200,080.7 | 198,665.4 | 0.993 | | 1.048 | 0.931 |
| *control* `nest2-64` whole (hybrid, `islands=0`, frames 128) | 2,164.0 | 2,177.8 | 1.006 | `unchanged` | 1.007 | 0.996 |
| *control* `nest3-16` whole (hybrid, `islands=0`, frames 512) | 3,985.5 | 3,862.1 | 0.969 | | 0.934 | 0.998 |
| *control* `level-context` (loglines hybrid, `islands=2`, frames 2) | — | — | 0.9995 / 0.9972 (§2.2) | `unchanged` | — | — |

- **The island is worth ×0.65–0.68 on the `ctx-*` MATCH cells (all three
  toolchain/route arms agree: gcc 0.651–0.677, clang 0.559–0.675, `vm`
  0.646–0.716), ×0.92–0.94 on the lazy family's search, and ×1.015 SLOWER
  on their throughput** (gcc; clang flat 0.996–0.999). The `vm` arm's
  0.87 on the same throughput cells is the same framed program
  (`shape=plain` there too) under the forced route's own entry — a second
  reading of the island, not the frameless-population move. The
  two hybrid controls with `islands=0` read 0.97–1.01. `level-context`
  (`islands=2`) reads 1.00 on both regimes: its per-call cost is the
  prefilter DFA's scan over 1 MB of log text, and the `\b(?:DEBUG|INFO|…)`
  program runs once per candidate.

### 3.5 The plain ladder and the whole-form customers across the pin — the continuity control, and a new move

PRED points 1–3, 6; FLD:199–204 (`cls-upto-1024` throughput), FLD:579–584
(`cls-upto-2048` match); the 04:10Z record is the ranked BEFORE, the
00:47Z six-pass record is quoted where it differs by > 0.3 % (REC):

| rung (plain; `pinned`, `folds=4` to 2048, `folds=2` from 4096) | search 334fd10e / 288d505 / ratio | throughput 334fd10e / 288d505 / ratio | whole `r-01024` ratio | `d-01024` 334fd10e / 288d505 |
|---|---|---|---|---|
| `cls-upto-4` | 454.1 / 526.8 / **0.862** | 200,391 / 319,395 / **0.627** | 0.976 | 10.2 / 10.6 |
| `cls-upto-8` | 474.7 / 545.7 / 0.870 | 174,455 / 236,891 / 0.736 | 1.001 | 10.1 / 10.5 |
| `cls-upto-16` | 512.8 / 591.1 / 0.868 | 165,029 / 201,058 / 0.821 | 1.001 | 10.2 / 10.6 |
| `cls-upto-32` | 576.7 / 655.2 / 0.880 | 157,897 / 178,165 / 0.886 | 0.999 | 10.2 / 10.4 |
| `cls-upto-64` | 710.3 / 790.6 / 0.899 | 159,887 / 182,616 / 0.876 | 0.997 | 10.2 / 10.4 |
| `cls-upto-128` | 833.2 / 897.8 / 0.928 | 136,243 / 169,268 / 0.805 | 0.994 | 10.3 / 10.4 |
| `cls-upto-256` | 989.0 / 1,051.2 / 0.941 | 130,463 / 161,684 / 0.807 | 0.999 | 10.2 / 10.5 |
| `cls-upto-512` | 987.4 / 1,046.5 / 0.944 | 127,101 / 157,614 / 0.806 | 1.000 | 10.3 / 10.5 |
| **`cls-upto-1024`** | 989.8 / 1,048.9 / **0.944** | **125,550 / 155,869 / 0.805** (`faster ×1.24`, FLD:201) | **1.000** (1,905.5 / 1,906.0) | 10.0 / 10.6 |
| `cls-upto-2048` (whole: search-filter customer) | 990.1 / 1,046.7 / 0.946 | 124,523 / 154,873 / 0.804 | **0.9985** (3,780.9 / 3,786.5) | **393.3 / 395.0** |
| `cls-upto-4096` | 985.8 / 1,046.3 / 0.942 | 124,317 / 155,320 / 0.800 | 1.0011 | 393.3 / 395.2 |
| `cls-upto-8192` | 985.1 / 1,048.3 / 0.940 | 124,225 / 154,533 / 0.804 | 0.9990 | 393.2 / 395.6 |
| `cls-upto-16384` | 986.5 / 1,048.1 / 0.941 | 123,905 / 154,826 / 0.800 | 0.982 (VM whole, `forward`) | 7.0 / 10.2 |
| `cls-upto-32768` (VM, `declined-nullable`, `forward`) | 1,107.9 / 1,292.5 / 0.857 | 172,352 / 245,793 / **0.701** | 0.982 | 7.0 / 10.2 |
| `cls-lazy-16384` (`pinned`, `folds=4`, emit **−543**) | 326.3 / 448.6 / **0.727** | 378,461 / 474,798 / 0.797 | 0.986 | 11.9 / 11.8 |
| `cls-atleast-4096` (`reverse-pass`, `edges=4`) | 2,314.3 / 2,654.2 / 0.872 | 86,327 / 87,358 / 0.988 | 0.970 | 388.6 / 389.3 |
| `grp-upto-1024` | 989.0 / 1,046.7 / 0.945 | 125,426 / 156,058 / 0.804 | 1.000 | 10.1 / 10.5 |

- **The STEP 2 letters win is still there (PRED point 2)**: `cls-upto-1024`
  throughput on `t-letters-064k` 0.610 ns/B at 334fd10e vs 0.614 at 288d505
  vs 1.215 at 1989c62 — **×0.502 against 1989c62**, ×0.994 across this
  pin. The customers' `cls-upto-2048 ÷ cls-upto-1024` at `r-01024` reads
  **1.984** (288d505 1.987; 2.041 / 2.013 / 1.994 / 1.987 on the smaller
  subjects — PRED point 1 unchanged, FLDS:8349 / 3557); every whole-subject
  search-filter customer 0.9985–1.0011 and `start=reverse-pass`, `edges=0/0`
  still; `d-01024` search-filter 393.2–393.3 (was 395.0–395.6) against the
  unwrapped 10.0 → **×39.1** (was ×37.4: the unwrapped failing call got
  0.6 ns cheaper, the search-filter one 1.7 ns).
- **The pinned ladder moved AGAIN, and on DIGITS this time**: per byte on
  `t-digits-016k` **5.03–5.06 → 3.55–3.58 ns/B on EVERY pinned rung
  (×0.702–0.712)**, uniform from `cls-upto-4` to `cls-upto-16384`; on
  letters the long rungs are flat (`cls-upto-1024` 0.994, `cls-upto-8192`
  1.001, `cls-upto-16384` 1.000 on `t-letters-064k`) while the short rungs
  moved — `cls-upto-4` **0.589** (2.511 → 1.478 ns/B), `cls-upto-32`
  **1.143 SLOWER** (0.865 → 0.988), `cls-upto-128` 0.970. The digit
  subjects never take the `[a-z]` scan edge, so what they see is the
  generic path — I-43's "29 → 15 instructions" — and ×0.70 is that
  number's size on this box. The set-grain throughput column (×0.80–0.89
  from rung 16 up) is the digits subjects' ×0.70 diluted by the flat
  letters ones.
- **`auto ÷ vm` on letters throughput** (the [OPT-5] frame): `cls-upto-4`
  0.720 (was 0.812), `cls-upto-32` 1.304 (0.893), `cls-upto-128` 0.970,
  `cls-upto-1024` **0.997** (0.994), `cls-upto-16384` 1.002 — parity kept
  from rung 512 up (both routes moved together: the VM's 0.618 → 0.612
  ns/B). On digits `auto ÷ vm` 0.60–0.64 (was 0.53–0.57: the VM's digits
  moved ×0.63 too, 9.47 → 5.92 ns/B at `cls-upto-1024`). Set-grain
  `auto ÷ vm` throughput 0.69–0.73 on every rung (was 0.99–1.00 from 512).
- **`auto ÷ jit` search** at `cls-upto-1024` **0.386** (was 0.409; 0.672 at
  1989c62); `grp-upto-1024` 0.217 (0.229); `cls-lazy-16384` 0.163.
- `cls-lazy-16384` plain (`pinned`, unwrapped) emit **14,947 → 14,404
  (−543 B)** — the ONLY artifact in the wave that shrank; `folds=4` — and
  moved ×0.727 search / ×0.797 throughput (0.796–0.799 per byte on all three
  subjects, letters and digits alike).
- **Controls**: unwrapped wholes 1.861 ns/B kept (`cls-upto-1024` /
  `r-01024` 1,905.5, ratio 1.000); low-rung wholes 0.976–1.001; the digit
  family whole `dig-exact-k` / `dig-upto-k` at `d-00033` within 0.2 ns
  (REC); `cls-atleast-4096` throughput 0.988 (the `reverse-pass` cls
  artifact — flat where the `pinned` ones moved), but its search ×0.872
  and its whole `r-01024` 0.970.
- **Beyond the ladder, `auto` across the pin** (126 cells; REC): match
  median 0.984 (min 0.651 `ctx-lazy-64` — the island; max 1.011), search
  median 0.936 (min 0.728 `cls-lazy-16384`, max 1.044 `csv5`), throughput
  median 0.867 (min 0.627 `cls-upto-4`, max **1.126 `dotted4`**, 66,414 →
  74,736 — the one auto-route regression past 5 %, on a `reverse-pass` DFA
  with `edges=2`; clang reads 0.998 on the same cell). `dig-exact-2`
  throughput 0.665, `nest2-letters-6` throughput **0.679** (195,589 →
  132,748), `year4` 0.713, `dig-*` 0.81–0.90, `nest2-4` / `nest3-3` 0.87–0.89
  — the `reverse-pass` DFAs with edges moved 0.66–0.90 on throughput too.

### 3.6 Sizes — the census against [B37]'s size books

`pcrec_334fd10e_auto` vs `pcrec_288d505_auto` (04:10Z), Δ `emit_bytes` /
`emit_code_bytes` / `artifact_bytes` (REC, 84 compiled artifacts):

| class | n | Δ emit | Δ code | Δ `.so` | [B37]'s book | example |
|---|---|---|---|---|---|---|
| `reverse-pass` DFA, `edges=0`, `folds=0` | 22 | **+31** | +31 | +312 (+320 ×2) | edge-free reverse-pass DFA +31 | `floor` plain 18,075 → 18,106; `year4` whole |
| `pinned` plain DFA, `folds=4`, `edges=1` (`cls-upto-4…2048`, `grp-upto-1024`) | 11 | **+261** | +649 | **+16** | +261 total / +649 code | `cls-upto-4` 16,292 → 16,553 |
| `pinned` plain, `folds=2` (`cls-upto-4096/8192/16384`) | 3 | +143 | +336 | +168 | +143 / +336 | 13,159 → 13,302 |
| `pinned` plain `cls-lazy-16384`, `folds=4`, `edges=0` | 1 | **−543** | −195 | +16 | — (not in the book) | 14,947 → 14,404 |
| `reverse-pass` DFA, `edges=2`, `folds=0` (plain `dig-*`, `nest*`, `dotted4`) | 7 | +1,084 (+1,087) | same | +312 | `dig-upto-16` auto +1,084 | 21,570 → 22,654 |
| `reverse-pass` DFA, `edges=1` (their wholes) | 7 | +275 (+276–279) | same | +312 | — | `dig-upto-4` whole |
| `reverse-pass` DFA, `edges=2`, `folds=2` (`year4`, `hex32` plain and 4 more) | 6 | +1,078 | +1,287 | **−4,080** ×5 / +16 | — | `year4` plain (page alignment the other way) |
| `reverse-pass` DFA, `edges=4` (`pw-8-64` [`folds=2`], `line-80`, `cls-atleast-4096` plain) | 3 | +927 … +1,373 | +927 … +1,373 (+1,287 on `pw-8-64`) | +16 / +312 / **+4,416** | — | `cls-atleast-4096` plain 18,942 → 19,869; `pw-8-64` 31,989 → 33,039 |
| `collapsed-prefilter` hybrid, `islands=2`, framed | 8 | **+187** | +188 | +312 / +320 | — | `ctx-lazy-64` 59,642 → 59,829 |
| `collapsed-prefilter` hybrid, `islands=0` (`nest2-64` / `nest3-16` whole) | 2 | +373 / +374 | same | +320 | — | 46,227 → 46,601 |
| `declined-nullable` VM, `forward`, frameless | 3 | **+275** | +275 | +280 | plain frameless VM +275 flat | `cls-upto-32768` 17,979 → 18,254 |
| `declined-nullable` VM, `plain`, framed (`cls-lazy-16384` whole) | 1 | +97 | +97 | +312 | framed VM +98..+131 | 18,810 → 18,907 |
| the two warns (`cls-upto-4096/8192` whole) | | 471,516 → **471,547**; 937,560 → **937,591** (+31) | | | | |
| refusal (`cls-upto-65535` both forms) | 2 | unchanged, `NFA exceeds 131072 states`, 20.6 ms | | | | |

The `vm` arm (86 artifacts): 62 `forward` / frameless **+275** emit,
+280 `.so`; 24 `plain` / framed **+97…+99** (+156 on the eight `ctx-*`
with `islands=2`), +312 `.so`. Every number [B37] predicted for a class
this window measured is reproduced to the byte; the classes the book did
not name are the edge-bearing `reverse-pass` DFAs (+927…+1,373 by edge
count, §2.2's dispatch bytes) and `cls-lazy-16384`'s −543.

### 3.7 The `shape=` / `folds=` / `islands=` census on bounded and loglines

| record | `shape=forward` | `plain` | `shared` / `inline` | `folds=` 4 / 2 / 0 | `islands=` 2 / 0 / absent | `frameless=` 1 / 0 |
|---|---|---|---|---|---|---|
| bounded `auto` (84 compiled) | 3 (`cls-upto-32768` ×2, `cls-upto-16384` whole; 653–756 B) | 11 (the 8 `ctx-*`, `cls-lazy-16384` whole, `nest2-64` whole, `nest3-16` whole; 890–18,325 B) | 0 / 0 | 12 / 10 / 58 | 8 / 6 / 70 | 3 / 11 |
| bounded `auto_cc-clang` | 3 | 11 | 0 / 0 | 12 / 10 / 58 | 8 / 6 / 70 | 3 / 11 |
| bounded `vm` (86) | **62** (all `frameless=1`, 599–756 B) | **24** (all framed: `cls-lazy-16384`, `csv5`, `ctx-*`, `dotted4`, `nest*`; 787–18,325 B) | 0 / 0 | — | 8 / 78 / — | 62 / 24 |
| loglines `auto`, `auto_noedge` (22) | 0 | 2 (`level-context`, 12,026 / 12,131 B) | 0 / 0 | 0 / 0 / 22 | 2 / 0 / 20 | 0 / 2 |

- **`folds=` on bounded**: 4 on the eleven `cls-upto-4…2048` +
  `grp-upto-1024` + `cls-lazy-16384` pinned plains (both machines fold
  whole), 2 on the three search-filter pinned plains (one machine), 0 on
  every `reverse-pass` artifact (58) and every hybrid's DFA part — [B37]'s
  witness table (`4 on cls-upto-4 / cls-upto-2048`, `2 on cls-upto-16384`)
  reproduced on the whole ladder. `folds=` is absent on the 4 pure-VM
  artifacts under `auto`.
- `start=pinned` **15**, `reverse-pass` 65 on both auto-route records —
  PRED point 11 reproduced exactly (the deny flags are on other axes).
- `frameless=` == `resume_frames == 1` on 100 / 100 VM artifacts of the
  two gcc arms (PRED point 12: 3 / 62 / 0, reproduced).

---

## 4. THE INSTRUMENT

- Pre-flight band 0.0–1.2 % (n=10; cumulative 0.0–7.85 %, n=76); zero
  refusals; the first daytime window under I-47's grant, and the quietest.
- Spread rule: zero firings; **zero disagreeing rows** of 23,424 — but
  §3.2's three noisy `r-01024` rows on the `vm` arm (sd 48–78 ns on
  ~320–710 ns medians, worst trial 1.23× the median) slipped under k=1.5
  and put a ×1.12 into FLDS:3557 that the neighbouring rungs refute.
- Cell timings: §0.2; the `noisland` estimate in `scripts/CLAUDE.md` is
  32 % high for this set (its premise is empty); the VM cells 16 % under
  the table with four more compiles.
- Other-core: two readings past 25 % (29.22 / 57.14), neither on a moved
  cell (§0.1).
- Report rendering: the 144-record store validates in **582 s** in one
  process (535 s at 134 records — 4.3 s per record, linear); the five
  groups render in 77 s (the altwide AFTER 24 s, the bounded fold 44 s).
- `vm-in` was not run on bounded at this pin, so §3.2's `_in`-vs-plain
  question (I-50's owed probe) has no 334fd10e reading.

---

## 5. RANKED CANDIDATES AND ASKS, AS NUMBERS

1. **The forced-VM `floor` doubled on throughput** on two sets (bounded
   31,637.5 → 63,140.3 ns/set, altwide 271,666 → 543,708; 0.296 → 0.593
   ns/B on all nine subjects), search ×1.41 / ×0.89, match flat / ×1.11;
   `shape=forward (prog: 236 B)`, `frameless=1`, `islands=0`, +275 B —
   while every OTHER `forward` artifact got 0.50–0.70× faster on
   throughput. Ask: what the 236-byte `forward` chain does per byte on a
   never-matching subject that the 645-byte `cls-upto-*` chains do not
   (the failing scan's per-position cost went 0.30 → 0.59 ns).
2. **The `vm`-arm failing dispatch moved again**: `d-01024` 9.1 → 10.2 →
   **7.0 ns** on 16 `forward` rungs, while `floor` match (also `forward`)
   stays at 5.6 (the abi-16 +0.6 kept). Beside I-50's probe: two `forward`
   artifacts, opposite answers on the failing-call axis.
3. **The pinned ladder's digits ×0.70** (5.05 → 3.55 ns/B on every pinned
   rung, `t-digits-016k`), letters flat at the long rungs, `cls-upto-4`
   letters ×0.59, `cls-upto-32` letters **×1.14 slower**. Ask: is the
   generic-path 29 → 15 the ×0.70, and what makes the 32-rung's letters
   the one slower cell in the ladder.
4. **The island's throughput cost on framed hybrids**: `ctx-lazy-*`
   ×1.014–1.016 slower on `large-subject-throughput` (gcc) where the same
   programs' match cells gain ×0.65–0.68 and search ×0.92–0.94; `nest2-4`
   (framed, `islands=0`, `vm`) ×1.362 slower on throughput. Numbers for
   I-43's "identity modulo which budget binds" — no answer differed.
5. **`pfx3-512` crossed the VM wall** (562,897 → 440,187 B) beside `w-384`;
   [B37]/I-43 named only `w-384`. The VM refusal count 26 → 22; the DFA's
   32 unchanged. Ask (bench-side too): the census in
   `docs/dev/measurements/2026-09-02-altwide-raised-cap-sizes.txt` §1 is
   stale for the VM route by −18…−26 % per rung.
6. **The DFA route's whole-subject `match` cells moved ×0.57–0.92 on
   altwide** (`w-64` 880 → 503; failing subjects ×0.29–0.79) and ×0.93 on
   bounded's `floor` (492 → 460) with `edges=0/0` on the latter — the
   abi-16..22 content on an `unwrapped` DFA `_match` entry. Ask: which
   step (the fold is `folds=0` on all of them; the dispatch's `match: N`
   edges are 2–4 on altwide, 0 on `floor`).
7. **I-44's stamp reading is impossible on the I-37 cell** (DFA artifact,
   no `RX_VM_ENTRY_SHAPE`); gcc 459.6 / clang 217.1 = 0.4725 at this pin,
   gcc 9.3–9.4 ns per subject vs the hand driver's 6.3. On the cells that
   DO stamp `forward` under `auto`, gcc caught clang: `cls-upto-32768`
   throughput clang ÷ gcc 0.630 → **0.930**. Ask: the capability-probe
   result on THIS box's gcc 15.2 (does the always_inline workaround fire
   here), against the 0.70 the `forward` shape bought the gcc arm.
8. `dotted4` throughput ×1.126 on gcc `auto` (66,414 → 74,736; clang 0.998)
   and `dig-upto-8` throughput ×1.336 on clang (64,248 → 85,843; gcc 0.859)
   — one regression per toolchain, on different cells.
9. `cls-lazy-16384` plain: −543 B and ×0.73 / ×0.80 — the only shrinking
   artifact; not in the size books.

---

## 6. WHAT THE NEXT SAMPLE (the [B39] abi-23 re-pin, the cls-fold AFTER) IS READ AGAINST

Measured at 334fd10e (this window); **a cell outside these bands is
movement**. [B39]'s `-fno-cls-fold` deny arm should reproduce the 334fd10e
`auto` numbers on every non-`(?i)` artifact; the `(?i)` witnesses are
altwide's `ci-256` (VM: `plain`, frames 256, 451,050 B; DFA: 989,963 B,
`edge=bitmap`) and whatever email/loglines carries.

1. **The order pair**: `w-256` / `srt-256` on `vm` 15,886,650 / 15,875,364
   throughput, 44,420 / 44,365 search, 384.9 / 382.9 match; 292,043 B both;
   ratio 1.0007–1.0052.
2. **The VM wall**: `w-384` 427,824 B compiles (16,542,968 / 53,296 /
   401.7); `pfx3-512` 440,187 B compiles; `w-512` refuses at 563,823. The
   DFA wall: `w-384` refuses at 1,432,392; 32 / 22 refusals per auto / VM
   arm.
3. **Island-bearing VM cells**: 54 cells at 0.0014–0.9083 of their 1989c62
   values; `vm ÷ jit` 0.029–2.79 across the ladder, VM under JIT on 32 of
   44; `vm ÷ auto` 3.8–8.0 throughput.
4. **The forced-VM floor tripwire**: `floor` throughput on `vm` **63,140.3
   ns/set bounded / 543,708.5 altwide, 0.593 ns/B**; search 1,496.4 /
   388.2; match 275.2 (5.6 ns/subject). A return to 31,600 / 0.296 is
   candidate 1 answered.
5. **The `vm` failing dispatch**: `d-01024` **7.0** on the cls rungs
   (`forward`), 11.9 on `cls-lazy-16384` (`plain`), 9.6 on
   `cls-atleast-4096`.
6. **The noedge pair**: `iso-ts` noedge ÷ auto **0.9846 / 0.9945**;
   `http-5xx` 0.9811 / 0.9985; `ipv6` 0.9926 / 0.9829; zero-edge 0.998–1.011;
   the noedge arm 1,142,263 / 20,461.9 on `iso-ts` (flat over three pins);
   auto `iso-ts` 1,148,538.8 / 20,781.2.
7. **The plain ladder**: `cls-upto-1024` plain search 989.8, throughput
   125,550 (0.610 ns/B letters, **3.554 digits**); `cls-upto-4` throughput
   200,391; `cls-upto-32` letters 0.988 ns/B; `auto ÷ vm` letters 0.997 at
   1024; `auto ÷ jit` search 0.386.
8. **The customers**: `cls-upto-2048/4096/8192` whole `r-01024`
   3,780.0–3,782.8; ratio 1.984; `d-01024` 393.2–393.3 (×39.1);
   `start=reverse-pass`, `edges=0/0`.
9. **The `ctx-*` hybrids** (`islands=2`, `plain`, framed): match 1,211.6 /
   1,450.5 / 1,448.6 / 668.8; search 8,377.7 / 8,809.2 / 8,821.9 / 7,193.7;
   throughput 200,163–200,449 / 198,665.
10. **The I-37 cell**: gcc 459.6 (9.33–9.40 ns), clang 217.1 (4.43–4.45),
    ratio 0.4725; no `shape=` on it. `cls-upto-32768` throughput gcc
    172,351.8 / clang 160,302.5.
11. **Sizes**: `pinned` plains 13,302–16,575 B (`cls-lazy-16384` 14,404);
    `reverse-pass` DFA edge-free +31 over 288d505; `iso-ts` 34,185 /
    27,929 (noedge); `w-256` vm 292,043 / auto 977,922; `.so` `floor` 27,528
    / 27,672 (gcc), 22,648-class (clang). [B39] predicts fold-bearing VM
    artifacts SHRINK (a 32-byte bitmap per `(?i)` letter pair): `ci-256`
    vm 451,050 B and `RX_VM_CLS_FOLDS` on every VM artifact (0 spelled) are
    the reading.
12. **Stamps**: `shape=` forward 62 / plain 24 on `vm`, forward 3 / plain
    11 under `auto`, shared 38 on altwide VM, `inline` 0 anywhere;
    `folds=` 4 ×12 / 2 ×10 / 0 ×58 on bounded `auto`; `islands=` 2 ×8 on
    bounded, 1 ×38 + 3 ×2 on altwide VM, 2 ×2 on loglines;
    `start=pinned` 15; `frameless=` == `resume_frames == 1` on 100 / 100.
13. **Instrument**: pre-flight 0.0–7.85 % (n=76); rows disagreeing 0 per
    record this window; cells 8.6–14.5 (altwide) / 7.9–8.2 (loglines) /
    44.8–48.2 (bounded) min; store validation 582 s at 144 records.
14. **The regressions to watch**: `dotted4` throughput 74,736 (gcc auto);
    `dig-upto-8` throughput 85,843 (clang); `nest2-4` throughput 633,363
    (`vm`); `cls-upto-32` letters 0.988 ns/B (auto).

---

## 7. DISTILLED SUMMARY FOR O-17 (≤ 25 lines, each with its number and citation)

1. 10 cells, 10 `measured` at attempt 1; pre-flight 0.0–1.2 % (mean 0.28); `agree` ×10 with **0 disagreeing rows** of 23,424; 0 wrong answers; suite 3 h 34 min by day (§0.1–0.2).
2. **The island pair is a NULL pair on altwide**: `pcrec-auto` selects the DFA on 34/34 compiled cells, `-fno-alt-island` changes 0 bytes and 0 stamps, 53 cells within 0.992–1.010 (§1.1; ISL:544–545, 855/857).
3. **The ×8.87 order effect is GONE**: `w-256 ÷ srt-256` on the VM route **1.0007** throughput / 1.0012 search / 1.0052 match (per subject 0.9994–1.0014), both 292,043 B code / 305,686 B program / `islands=1` / `shape=shared` (§1.3; ALT:2451, 1906, 4025/3917).
4. The absolutes: `w-256` vm throughput 1,931 ms → **15.9 ms per set (×0.0082, `faster ×121.57`)**, search ×0.0047; `srt-256` ×0.0729 (§1.3).
5. **`w-384` COMPILES on the VM route** at 427,824 B (85.6 % of the cap): 16,542,968 ns/set throughput = **0.040 × the JIT**, search 53,296 = 0.028 × JIT, match 401.7; `w-512` refuses at 563,823 — the wall is 384 < w ≤ 512 as I-43 said; **`pfx3-512` crossed too** (440,187 B), unpredicted (§1.4; ALT:4043, 2562, 3719).
6. The DFA wall is unmoved: `w-384` auto refuses at 1,432,392 (+856 = the dispatch), 32/66 refusals on all three auto arms, 113.7 s per pass (§1.4).
7. Island effect over 54 VM cells: **×0.0014–0.91, median ×0.026** vs 1989c62 (three abi steps travel together: island + `always_inline` + `shape=shared`); `pfx3-256` gains least (×0.80), `s-512` most (×0.0032); `ci-256` (declined) flat 0.996–1.002 (§1.2).
8. **The VM now beats libpcre2's JIT on 32 of 44 altwide cells** (3 of 40 at 1989c62): `vm ÷ jit` 0.029 (`s-512`) … 0.067 (`w-256`) … 2.79 (`w-8`); P11 REFUTED in the VM's favour (§1.6).
9. Code-byte ratios island ÷ chain 0.8562 / 0.8120 / 0.7637 (`w-256` / `pfx3-256` / `s-256`) vs [B37]'s 0.8557 / 0.8114 / 0.7631 — the +98 B denominator (§1.5). `shape=inline` prints nowhere; the AUTO rule holds on 100 % of 130 VM artifacts (§1.7, §3.7).
10. **The forced-VM floor tripwire FIRED**: `floor` throughput on `vm` **×1.996 bounded / ×2.001 altwide** (0.296 → 0.593 ns/B), `frameless=1`, `shape=forward (prog: 236 B)` — the only `forward` artifact that got slower (§1.2, §3.2; FLD:2641, ALT:332).
11. **[OPT-EDGE] third sample: `iso-ts` noedge ÷ auto 0.9157 / 0.9388 → 0.9846 / 0.9945** — the edge's cost fell from ×1.09 / ×1.07 to ×1.016 / ×1.006 (I-44's 0.99–1.01 met on throughput, 0.6 % short on search); `http-5xx` 0.981 / 0.999, `ipv6` 0.993 / 0.983; the noedge arm FLAT across three pins (1,142,263 / 1,142,674 / 1,142,842); `iso-ts` +1,468 B as predicted (§2; NOE:289–290, 325–326; NOX:689–694).
12. **Fold witnesses**: `cls-upto-4` auto `folds=4`, emit +261 / code +649 / `.so` **+16** (every non-fold DFA +312); `dig-upto-16` vm `shape=forward (646 B)`, +275 / `.so` +280; timings `cls-upto-4` throughput ×0.627 (gcc; clang ×0.978), `dig-upto-16` vm match ×0.776 / throughput ×0.594 (§3.1; FLD:855–860, 2196–2201).
13. **The `vm` dispatch: `floor` match 5.6 ns PERSISTED (275.2 → 275.2); `d-01024` on the cls rungs 10.2 → 7.0** (×0.686, under 1989c62's 9.1) on `shape=forward`; the framed `cls-lazy-16384` 11.9 unmoved (§3.2; FLDS:2793–2798).
14. The `vm` arm broadly: throughput median ×0.703 (`dig-*` 0.50–0.60, `year4` 0.572 undoing its ×1.163), search ×0.836, match ×0.904 — 101 of 129 cells past ±5 %; framed artifacts flat except `nest2-4` throughput ×1.362 (§3.2).
15. **The one-variable island reading is on bounded's `ctx-*` hybrids** (`islands=2`, `plain`, framed, +187 B): match **×0.65–0.68** on gcc / clang / `vm` alike, search ×0.92–0.94, throughput ×1.015 SLOWER; `nest2-64` / `nest3-16` wholes (`islands=0`) 0.97–1.01; `level-context` (`islands=2`, prefilter-bound) 1.00 (§3.4; FLD:1786–1791).
16. **The plain ladder moved again — on digits**: 5.05 → 3.55 ns/B on every pinned rung (×0.70), letters flat from rung 128 up (`cls-upto-1024` 0.610 ns/B = ×0.502 vs 1989c62 still), `cls-upto-4` letters ×0.59, `cls-upto-32` letters ×1.14 slower; set-grain throughput ×0.80 from rung 128, search ×0.94 (§3.5; FLD:199–204).
17. Customers unchanged: `cls-upto-2048 ÷ cls-upto-1024` at r-01024 **1.984**, wholes 0.9985–1.0011, `reverse-pass` / `edges=0/0`; `d-01024` ×39.1 (§3.5; FLDS:8349 / 3557).
18. **I-37 cell: gcc 459.6 / clang 217.1 = 0.4725** (was 0.470), both ×0.93–0.94 across the pin; gcc 9.3–9.4 ns per subject vs pcrec's 6.3; **no `shape=` on it — a DFA artifact**; where `forward` DOES stamp under `auto` (`cls-upto-32768`), clang ÷ gcc throughput 0.630 → 0.930 (§3.3; FLD:2688–2693).
19. Sizes: [B37]'s books reproduced to the byte on every named class (+31 / +261 / +143 / +275 / +97 / +187 / +1,468 / +517 / +393); the unnamed classes are the edge-bearing `reverse-pass` DFAs (+927…+1,373) and `cls-lazy-16384` **−543** (§3.6, §2.2).
20. `start=pinned` 15 / `reverse-pass` 65, `frameless=` == `resume_frames == 1` on 100/100, `folds=` 4 ×12 / 2 ×10 / 0 ×58 — PRED points 11–12 reproduced (§3.7).
21. Altwide's DFA route across the pin: throughput 0.98–1.03, search 0.95–1.03 (`cnt-64`, 8 edges, 0.504), **whole-subject `match` ×0.57–0.92 on all 15** (`w-64` 880 → 503; failing subjects ×0.29–0.79) — abi 16–22 unseparated (§1.8; ALT:2775–2781).
22. Regressions: `dotted4` throughput ×1.126 (gcc auto), `dig-upto-8` throughput ×1.336 (clang only), `nest2-4` ×1.362 (`vm`, framed), `cls-upto-32` letters ×1.14 (§3.5, §3.3, §3.2).
23. Instrument: three noisy `r-01024` rows on the `vm` arm (sd 48–78 ns, k not reached) — read FLDS:3557's ×1.12 as noise; `noisland`'s cell estimate 32 % high (its premise empty); store validation 582 s (§4).
24. Asks as numbers: §5 items 1–7 (the `floor` ×2.0 on `forward`, the 7.0-vs-5.6 dispatch split, the digits ×0.70 and the 32-rung, the island's +1.5 % throughput on framed hybrids, `pfx3-512`, the DFA `_match` ×0.57–0.92, the stamp-less I-37 cell).
