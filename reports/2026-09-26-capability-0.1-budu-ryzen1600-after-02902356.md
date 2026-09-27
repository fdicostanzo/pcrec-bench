# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, since=2026-09-25T00:00:00Z, until=2026-09-27T02:00:00Z, testee=pcrec_ce658cb7_auto-caps-simdna, testee=pcrec_02902356_auto-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 20.0% (`pcrec_02902356_auto-caps-simdna` / `numeric-id-nested-plus` / `large-subject-throughput`)
    - `capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z` (store/records/capability@0.1/pcrec_02902356_auto-caps-simdna/capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z.jsonl) — agreement: agree (0 of 124 groups; 2 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_ce658cb7_auto-caps-simdna__budu-ryzen1600__20260925T231327Z` (store/records/capability@0.1/pcrec_ce658cb7_auto-caps-simdna/capability@0.1__pcrec_ce658cb7_auto-caps-simdna__budu-ryzen1600__20260925T231327Z.jsonl) — agreement: agree (0 of 124 groups; 1 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.7
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

- D119 bar (inbox I-93 block B / I-104): a cross-pin cell moved iff |Δ%| > max(IQR%, null band) -- Δ% = (after - before) / before; IQR% = the BEFORE side's Type-7 IQR of its per-trial set sums over the before median; null band = the largest |Δ%| any PROGRAM-IDENTICAL cell of the same (regime, baseline scale) stratum reached across the same pin pair (symmetric); a stratum with fewer than 10 program-identical cells has NO usable band and its verdicts say `IQR only` by name.
- baseline scale: the BEFORE (older pin) set-grain median -- `>=1us` / `100ns-1us` / `<100ns`; strata are per REGIME (I-104).
- sufficiency: a stratum needs >= 10 program-identical cells -- the band is a sample maximum, and one more null cell exceeds the maximum of n with chance 1/(n+1) (<= 9.1% at n = 10).
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec ce658cb7 -> 02902356`: the BEFORE (`ce658cb7`) records carry `program_sha256` (124 of 124 compiled cell(s)), the AFTER (`02902356`) records carry `program_sha256` (124 of 124 compiled cell(s)).

### `pcrec ce658cb7 -> 02902356` (capability@0.1)

- identity from the records ([B88], schema v1.7): 123 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 123 cross-pin set cell(s) measured on both sides; 95 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 30 | -2.40% | -0.03% | +4.03% | ±4.03% | ok |
| `large-subject-throughput` | `100ns-1us` | 2 | +0.05% | +0.15% | +0.24% | n/a | insufficient (n=2 < 10) |
| `large-subject-throughput` | `<100ns` | 16 | -3.96% | -0.36% | +0.96% | ±3.96% | ok |
| `short-subject-search` | `>=1us` | 26 | -0.86% | -0.03% | +1.41% | ±1.41% | ok |
| `short-subject-search` | `100ns-1us` | 21 | -1.98% | +0.01% | +2.35% | ±2.35% | ok |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 123 cross-pin cell(s): 4 improve, 10 regress, 14 within the bar, 95 null-control (program identical -- the band's own population); 0 of the verdicts are IQR-only (their stratum's band is not usable)._

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,111,913.6 | 3.7144 | 5,106,258.7 | 5,121,759.8 | 5,418.4 | 1.000x | 1.000x | faster ×1.01 | -1.40% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 5,184,526.3 | 3.7671 | 5,163,989.4 | 5,195,069.9 | 12,910.8 | 1.014x | 1.014x | - | - |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,899,201.4 | 3.7186 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,955,336.0 | 3.7721 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 970,648.5 | 3.7027 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 983,049.8 | 3.7500 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 242,843.5 | 3.7055 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 246,974.9 | 3.7685 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,899,201.4 ns, 1,048,576 B

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 983.8 | 981.0 | 1,160.1 | 71.0 | 1.000x | 1.000x | - | - | 75 | 13.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007.9 | 1,003.6 | 1,044.4 | 15.4 | 1.024x | 1.024x | unchanged (within spread) | +2.44% vs bar 2.35% (band) → **regress** | 75 | 13.4 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `waf-concat`, 142.6 ns, 48 B; largest Δ: `rec-parens-balanced`, +1.4 ns (now 51.2 ns), 7 B

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 0.0000 | 18.2 | 18.4 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.47% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 18.4 | 0.0000 | 18.1 | 18.5 | 0.1 | 1.005x | 1.005x | - | - |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 6.1 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 6.2 ns, 1,048,576 B; largest Δ: `t-256k`, -0.1 ns (now 6.1 ns), 262,144 B

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 543.4 | 532.4 | 544.0 | 4.9 | 1.000x | 1.000x | unchanged (within spread) | -0.20% (null control: program identical) | 75 | 7.2 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 544.5 | 524.6 | 549.2 | 10.6 | 1.002x | 1.002x | - | - | 75 | 7.3 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 36.4 ns, 20 B; largest Δ: `lp-num-neg-dec`, -1.8 ns (now 17.5 ns), 7 B

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 0.0001 | 71.9 | 72.4 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 0.0001 | 71.8 | 73.3 | 0.5 | 1.003x | 1.003x | - | - |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 23.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 24.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 24.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 24.1 | 0.0004 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-256k`, 24.1 ns, 262,144 B; largest Δ: `t-1m`, -0.1 ns (now 23.9 ns), 1,048,576 B

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,879.2 | 1,878.6 | 1,879.8 | 0.5 | 1.000x | 1.000x | faster ×1.00 | -0.17% (null control: program identical) | 75 | 25.1 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,882.3 | 1,882.0 | 1,885.9 | 1.5 | 1.002x | 1.002x | - | - | 75 | 25.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `rec-array-define`, 87.7 ns, 11 B

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 617,517.9 | 0.4487 | 602,272.9 | 641,063.0 | 14,129.0 | 1.000x | 1.000x | unchanged (within spread) | -1.86% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 629,192.9 | 0.4572 | 602,461.9 | 631,911.4 | 11,389.1 | 1.019x | 1.019x | - | - |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 480,003.4 | 0.4578 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 485,755.4 | 0.4633 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 111,522.2 | 0.4254 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 111,672.8 | 0.4260 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 27,987.3 | 0.4271 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 29,384.6 | 0.4484 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 480,003.4 ns, 1,048,576 B

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 891.2 | 888.5 | 891.7 | 1.1 | 1.000x | 1.000x | - | - | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 892.0 | 888.1 | 898.7 | 3.4 | 1.001x | 1.001x | unchanged (within spread) | +0.09% (null control: program identical) | 75 | 11.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `cg-key-colon`, 41.9 ns, 7 B; largest Δ: `sec-slack-webhook`, +0.7 ns (now 12.6 ns), 81 B

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 607,496.7 | 0.4414 | 597,509.1 | 615,428.4 | 6,729.6 | 1.000x | 1.000x | faster ×1.02 | -2.40% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 622,423.1 | 0.4523 | 610,576.2 | 627,896.4 | 5,923.1 | 1.025x | 1.025x | - | - |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 467,248.8 | 0.4456 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 468,110.8 | 0.4464 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 110,680.2 | 0.4222 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 119,784.9 | 0.4569 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 29,073.8 | 0.4436 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 28,703.6 | 0.4380 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 467,248.8 ns, 1,048,576 B; largest Δ: `t-256k`, -9,104.7 ns (now 110,680.2 ns), 262,144 B

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 890.1 | 888.3 | 894.1 | 2.3 | 1.000x | 1.000x | - | - | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 893.5 | 892.0 | 895.7 | 1.2 | 1.004x | 1.004x | unchanged (within spread) | +0.38% (null control: program identical) | 75 | 11.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `cg-key-colon`, 42.2 ns, 7 B; largest Δ: `sec-github-pat`, +0.9 ns (now 12.5 ns), 93 B

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 11,169,592.7 | 8.1159 | 11,167,219.2 | 11,253,022.2 | 32,781.6 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 11,179,860.5 | 8.1234 | 11,170,825.5 | 11,187,052.2 | 5,215.3 | 1.001x | 1.001x | - | - |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8,509,284.2 | 8.1151 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 8,511,323.5 | 8.1170 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,126,560.1 | 8.1122 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 2,131,198.0 | 8.1299 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 534,760.1 | 8.1598 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 534,953.2 | 8.1627 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 8,509,284.2 ns, 1,048,576 B; largest Δ: `t-256k`, -4,637.8 ns (now 2,126,560.1 ns), 262,144 B

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 5,077.4 | 5,073.2 | 5,099.3 | 11.8 | 1.000x | 1.000x | - | - | 75 | 67.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,149.2 | 5,134.2 | 5,160.8 | 9.9 | 1.014x | 1.014x | slower ×1.01 | +1.41% (null control: program identical) | 75 | 68.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-syslog`, 485.6 ns, 56 B; largest Δ: `v-ipv4`, +9.2 ns (now 133.6 ns), 11 B

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.7 | 30.9 | 0.1 | 1.000x | 1.000x | faster ×1.03 | -2.49% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 31.7 | 0.0000 | 31.5 | 32.3 | 0.3 | 1.026x | 1.026x | - | - |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10.6 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-256k`, 10.3 ns, 262,144 B; largest Δ: `t-64k`, -0.3 ns (now 10.3 ns), 65,536 B

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 834.7 | 827.8 | 880.3 | 19.5 | 1.000x | 1.000x | - | - | 75 | 11.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 839.6 | 837.6 | 840.2 | 1.1 | 1.006x | 1.006x | unchanged (within spread) | +0.58% (null control: program identical) | 75 | 11.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 61.4 ns, 20 B; largest Δ: `rd-numeric-id-hit`, -0.7 ns (now 13.2 ns), 4 B

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 25,427,164.0 | 18.4756 | 25,411,702.0 | 25,470,049.7 | 21,532.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 25,438,453.7 | 18.4838 | 25,264,260.2 | 26,138,014.4 | 308,079.6 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 19,406,597.5 | 18.5076 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 19,380,938.1 | 18.4831 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,816,636.5 | 18.3740 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,837,275.2 | 18.4527 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,201,055.5 | 18.3267 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,203,012.2 | 18.3565 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 19,380,938.1 ns, 1,048,576 B

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 20,916.3 | 20,833.2 | 21,017.4 | 60.3 | 1.000x | 1.000x | - | - | 75 | 278.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20,936.5 | 20,893.9 | 20,969.1 | 26.1 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 279.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-slack-webhook`, 1,326.8 ns, 81 B; largest Δ: `waf-benign`, +12.8 ns (now 680.8 ns), 39 B

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,135.1 | 0.0168 | 23,117.6 | 23,139.9 | 9.4 | 1.000x | 1.000x | unchanged (within spread) | -0.17% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,174.1 | 0.0168 | 23,117.1 | 23,202.1 | 29.6 | 1.002x | 1.002x | - | - |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,635.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,634.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,385.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,428.9 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,106.2 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,635.2 ns, 1,048,576 B; largest Δ: `t-256k`, -43.8 ns (now 4,385.1 ns), 262,144 B

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,162.1 | 1,157.7 | 1,166.7 | 3.0 | 1.000x | 1.000x | - | - | 75 | 15.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,174.7 | 1,170.4 | 1,177.6 | 2.8 | 1.011x | 1.011x | slower ×1.01 | +1.09% vs bar 1.41% (band) → **within** | 75 | 15.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `waf-benign`, 399.2 ns, 39 B

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 977.0 | 0.0007 | 969.9 | 984.6 | 5.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 977.5 | 0.0007 | 972.3 | 982.7 | 3.4 | 1.001x | 1.001x | unchanged (within spread) | +0.05% (null control: program identical) |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 225.3 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 229.9 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 459.6 | 0.0018 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 456.8 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 289.7 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 289.3 | 0.0044 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-256k`, 456.8 ns, 262,144 B; largest Δ: `t-1m`, +4.6 ns (now 229.9 ns), 1,048,576 B

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,517.7 | 10,475.0 | 10,575.5 | 32.7 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) | 75 | 140.2 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 10,520.3 | 10,503.1 | 10,552.6 | 16.7 | 1.000x | 1.000x | - | - | 75 | 140.3 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 926.8 ns, 61 B; largest Δ: `sd-empty-alt-miss`, -2.1 ns (now 911.4 ns), 60 B

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 46.6 | 0.0000 | 45.6 | 47.9 | 0.8 | 1.000x | 1.000x | faster ×1.04 | -3.92% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 48.5 | 0.0000 | 47.1 | 49.5 | 0.8 | 1.041x | 1.041x | - | - |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 14.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 15.4 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 15.7 ns, 1,048,576 B

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,354.5 | 1,350.0 | 1,366.8 | 5.6 | 1.000x | 1.000x | - | - | 75 | 18.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,368.9 | 1,356.1 | 1,378.0 | 7.0 | 1.011x | 1.011x | slower ×1.01 | +1.07% (null control: program identical) | 75 | 18.3 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 75.6 ns, 93 B; largest Δ: `la-negation-hit`, +2.7 ns (now 19.6 ns), 19 B

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 11,625.4 | 0.0084 | 11,621.5 | 12,134.6 | 200.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,094.3 | 0.0088 | 11,897.6 | 12,169.4 | 93.1 | 1.040x | 1.040x | slower ×1.04 | +4.03% (null control: program identical) |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 1,168.7 | 0.0011 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,223.5 | 0.0012 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 45.3 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 45.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10,434.9 | 0.1592 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,825.6 | 0.1652 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 10,825.6 ns, 65,536 B

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 255,493.9 | 0.1856 | 255,315.2 | 255,621.0 | 98.3 | 1.000x | 1.000x | faster ×1.02 | -1.96% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 260,610.5 | 0.1894 | 260,551.6 | 260,812.2 | 105.9 | 1.020x | 1.020x | - | - |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 202,386.3 | 0.1930 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 207,415.5 | 0.1978 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 44,401.9 | 0.1694 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 44,469.0 | 0.1696 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8,685.4 | 0.1325 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 8,739.6 | 0.1334 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 202,386.3 ns, 1,048,576 B

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 675.9 | 675.7 | 677.0 | 0.5 | 1.000x | 1.000x | - | - | 75 | 9.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.1 | 686.5 | 687.9 | 0.5 | 1.017x | 1.017x | slower ×1.02 | +1.65% vs bar 2.35% (band) → **within** | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sd-fileext-short`, 27.2 ns, 14 B; largest Δ: `v-ipv4-oor`, -5.9 ns (now 12.1 ns), 9 B

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,888,100.8 | 1.3719 | 1,884,218.3 | 1,910,982.0 | 10,074.1 | 1.000x | 1.000x | unchanged (within spread) | -0.22% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,892,212.5 | 1.3749 | 1,890,809.3 | 1,937,453.3 | 18,244.0 | 1.002x | 1.002x | - | - |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,446,031.4 | 1.3790 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 1,448,097.2 | 1.3810 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 356,011.0 | 1.3581 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 357,415.9 | 1.3634 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 86,264.5 | 1.3163 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 87,054.7 | 1.3283 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,446,031.4 ns, 1,048,576 B

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,638.9 | 1,630.8 | 1,652.6 | 8.2 | 1.000x | 1.000x | unchanged (within spread) | -0.86% (null control: program identical) | 75 | 21.9 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,653.1 | 1,637.7 | 1,657.2 | 7.2 | 1.009x | 1.009x | - | - | 75 | 22.0 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `v-ipv4`, 248.3 ns, 11 B; largest Δ: `la-currency`, -2.7 ns (now 60.2 ns), 10 B

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,095.2 | 0.0168 | 23,077.3 | 23,102.2 | 9.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,126.4 | 0.0168 | 23,110.3 | 23,158.8 | 18.7 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,608.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,640.7 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,381.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.4 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,107.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,104.2 | 0.0168 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,640.7 ns, 1,048,576 B

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.0 | 662.5 | 667.1 | 1.8 | 1.000x | 1.000x | unchanged (within spread) | -0.04% (null control: program identical) | 75 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 667.3 | 661.6 | 669.3 | 2.6 | 1.000x | 1.000x | - | - | 75 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `floor-hit`, 16.9 ns, 1 B; largest Δ: `v-email`, -0.2 ns (now 8.6 ns), 24 B

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 482,662.5 | 0.3507 | 482,612.5 | 482,971.4 | 129.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 483,087.0 | 0.3510 | 482,752.7 | 483,416.5 | 210.9 | 1.001x | 1.001x | slower ×1.00 | +0.09% (null control: program identical) |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 368,020.4 | 0.3510 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 368,071.8 | 0.3510 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 91,672.1 | 0.3497 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,954.1 | 0.3508 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 22,985.0 | 0.3507 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,066.0 | 0.3520 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 368,071.8 ns, 1,048,576 B; largest Δ: `t-256k`, +282.0 ns (now 91,954.1 ns), 262,144 B

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,063.9 | 1,061.2 | 1,072.8 | 4.0 | 1.000x | 1.000x | unchanged (within spread) | -0.33% (null control: program identical) | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,067.4 | 1,056.3 | 1,073.6 | 5.8 | 1.003x | 1.003x | - | - | 75 | 14.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 52.0 ns, 93 B; largest Δ: `sec-slack-webhook`, +0.7 ns (now 49.1 ns), 81 B

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 13.8 | 0.0000 | 13.7 | 13.9 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.14% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 13.8 | 0.0000 | 13.6 | 14.0 | 0.1 | 1.001x | 1.001x | - | - |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 4.6 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-64k`, 4.6 ns, 65,536 B; largest Δ: `t-256k`, +0.0 ns (now 4.6 ns), 262,144 B

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 412.1 | 405.6 | 422.5 | 5.6 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) | 75 | 5.5 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 413.1 | 410.1 | 417.0 | 2.4 | 1.003x | 1.003x | - | - | 75 | 5.5 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `v-ipv4`, 17.1 ns, 11 B; largest Δ: `sd-empty-alt-hit`, -0.5 ns (now 4.0 ns), 61 B

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687,715.0 | 0.4997 | 685,324.2 | 688,495.4 | 1,111.0 | 1.000x | 1.000x | faster ×1.69 | -40.78% vs bar 4.03% (band) → **improve** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,161,262.1 | 0.8438 | 1,159,088.9 | 1,163,492.4 | 1,465.4 | 1.689x | 1.689x | - | - |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 531,816.0 | 0.5072 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 899,888.9 | 0.8582 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 126,911.4 | 0.4841 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 213,032.6 | 0.8127 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 28,894.0 | 0.4409 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 48,195.7 | 0.7354 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 531,816.0 ns, 1,048,576 B

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 717.9 | 714.8 | 720.1 | 2.2 | 1.000x | 1.000x | - | - | 75 | 9.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 766.0 | 764.1 | 769.5 | 2.3 | 1.067x | 1.067x | slower ×1.07 | +6.70% vs bar 2.35% (band) → **regress** | 75 | 10.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `br-quoted-delim`, 20.4 ns, 15 B; largest Δ: `rec-comment-nested`, -6.2 ns (now 20.0 ns), 34 B

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 30.8 | 0.0000 | 30.8 | 31.1 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 31.0 | 0.0 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.7 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-64k`, 10.7 ns, 65,536 B; largest Δ: `t-256k`, -0.0 ns (now 10.1 ns), 262,144 B

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 807.7 | 807.4 | 819.8 | 4.8 | 1.000x | 1.000x | unchanged (within spread) | -0.50% (null control: program identical) | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 811.7 | 808.1 | 817.5 | 4.0 | 1.005x | 1.005x | - | - | 75 | 10.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `lp-atomic-hit`, 78.5 ns, 31 B

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 31.3 | 0.0000 | 31.2 | 31.5 | 0.1 | 1.000x | 1.000x | faster ×1.04 | -3.45% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 32.4 | 0.0000 | 32.3 | 33.1 | 0.3 | 1.036x | 1.036x | - | - |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 11.2 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-64k`, 10.9 ns, 65,536 B; largest Δ: `t-1m`, -0.4 ns (now 10.2 ns), 1,048,576 B

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 808.0 | 806.4 | 840.8 | 13.2 | 1.000x | 1.000x | - | - | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 808.9 | 806.9 | 835.2 | 10.8 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 10.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-atomic-hit`, 69.1 ns, 31 B; largest Δ: `nu-high-byte`, +0.8 ns (now 10.7 ns), 2 B

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,164.0 | 0.0168 | 23,140.5 | 23,174.1 | 13.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,167.0 | 0.0168 | 23,130.1 | 23,191.5 | 23.2 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,651.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,385.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,391.4 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,108.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.0 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,649.3 ns, 1,048,576 B; largest Δ: `t-256k`, +5.6 ns (now 4,391.4 ns), 262,144 B

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 686.2 | 685.8 | 687.0 | 0.4 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 686.3 | 686.0 | 687.8 | 0.7 | 1.000x | 1.000x | - | - | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `nu-mojibake`, 36.1 ns, 7 B

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,145.5 | 0.0168 | 23,119.7 | 23,148.1 | 11.3 | 1.000x | 1.000x | unchanged (within spread) | -0.17% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,184.6 | 0.0168 | 23,176.1 | 23,299.0 | 46.6 | 1.002x | 1.002x | - | - |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,651.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,678.4 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,375.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,398.7 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,105.5 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,651.9 ns, 1,048,576 B

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,473.6 | 1,445.8 | 1,502.9 | 22.6 | 1.000x | 1.000x | - | - | 75 | 19.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,582.0 | 1,577.0 | 1,646.4 | 31.4 | 1.074x | 1.074x | slower ×1.07 | +7.36% vs bar 2.84% (IQR) → **regress** | 75 | 21.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `rec-comment-nested`, 628.1 ns, 34 B

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 28.9 | 0.0000 | 28.7 | 40.7 | 4.7 | 1.000x | 1.000x | unchanged (within spread) | -3.31% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 29.9 | 0.0000 | 29.9 | 30.1 | 0.1 | 1.034x | 1.034x | - | - |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 9.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10.0 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 9.7 ns, 1,048,576 B; largest Δ: `t-64k`, -0.4 ns (now 9.6 ns), 65,536 B

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 815.5 | 801.6 | 827.1 | 8.1 | 1.000x | 1.000x | unchanged (within spread) | -0.13% (null control: program identical) | 75 | 10.9 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 816.5 | 804.4 | 819.6 | 6.0 | 1.001x | 1.001x | - | - | 75 | 10.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 34.7 ns, 20 B; largest Δ: `v-us-zip-plus4`, -0.6 ns (now 16.7 ns), 10 B

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 0.0000 | 29.8 | 30.1 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.24% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 30.1 | 0.0000 | 29.8 | 30.3 | 0.2 | 1.002x | 1.002x | - | - |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 9.9 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 10.0 ns, 1,048,576 B; largest Δ: `t-256k`, -0.1 ns (now 10.0 ns), 262,144 B

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 874.3 | 871.6 | 884.7 | 4.7 | 1.000x | 1.000x | - | - | 75 | 11.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 887.4 | 868.5 | 891.6 | 8.5 | 1.015x | 1.015x | unchanged (within spread) | +1.49% (null control: program identical) | 75 | 11.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-phone-list-hit`, 46.0 ns, 7 B; largest Δ: `rd-numeric-id-hit`, +1.8 ns (now 33.4 ns), 4 B

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 6,531,542.7 | 4.7459 | 6,503,300.1 | 6,534,974.2 | 14,638.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,541,533.0 | 4.7531 | 6,504,044.4 | 6,547,064.1 | 19,609.1 | 1.002x | 1.002x | unchanged (within spread) | +0.15% (null control: program identical) |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 4,986,504.3 | 4.7555 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4,988,794.4 | 4.7577 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 1,237,146.8 | 4.7193 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,239,933.8 | 4.7300 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 308,408.7 | 4.7059 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 309,249.6 | 4.7188 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 4,988,794.4 ns, 1,048,576 B; largest Δ: `t-256k`, +2,786.9 ns (now 1,239,933.8 ns), 262,144 B

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 6,623.3 | 6,564.6 | 6,753.7 | 65.6 | 1.000x | 1.000x | - | - | 75 | 88.3 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,705.9 | 6,535.9 | 6,895.6 | 150.4 | 1.012x | 1.012x | unchanged (within spread) | +1.25% (null control: program identical) | 75 | 89.4 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-slack-webhook`, 492.8 ns, 81 B; largest Δ: `v-ipv4-oor`, +22.6 ns (now 85.8 ns), 9 B

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 222.5 | 0.0002 | 221.5 | 223.1 | 0.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 223.0 | 0.0002 | 222.8 | 223.5 | 0.3 | 1.002x | 1.002x | unchanged (within spread) | +0.24% (null control: program identical) |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 58.1 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 58.5 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 95.4 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 95.1 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 69.0 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 69.3 | 0.0011 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-256k`, 95.1 ns, 262,144 B; largest Δ: `t-1m`, +0.4 ns (now 58.5 ns), 1,048,576 B

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 12,134.2 | 12,064.1 | 12,167.7 | 39.4 | 1.000x | 1.000x | - | - | 75 | 161.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,153.6 | 12,102.8 | 12,179.4 | 31.6 | 1.002x | 1.002x | unchanged (within spread) | +0.16% (null control: program identical) | 75 | 162.0 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 918.3 ns, 93 B; largest Δ: `waf-union`, +3.5 ns (now 586.2 ns), 43 B

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 9,979,301.2 | 7.2511 | 9,929,072.7 | 10,017,401.4 | 28,582.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,034,269.2 | 7.2910 | 9,949,749.5 | 10,058,744.9 | 37,707.7 | 1.006x | 1.006x | unchanged (within spread) | +0.55% (null control: program identical) |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 7,638,262.7 | 7.2844 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 7,643,126.9 | 7.2891 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 1,861,383.4 | 7.1006 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,914,759.2 | 7.3042 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 466,748.2 | 7.1220 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 476,629.0 | 7.2728 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 7,643,126.9 ns, 1,048,576 B; largest Δ: `t-256k`, +53,375.8 ns (now 1,914,759.2 ns), 262,144 B

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 10,859.8 | 10,703.6 | 11,237.1 | 197.1 | 1.000x | 1.000x | - | - | 75 | 144.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,870.9 | 10,805.1 | 11,349.0 | 209.5 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 144.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 658.3 ns, 93 B; largest Δ: `v-email`, +8.2 ns (now 178.7 ns), 24 B

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 343,378.8 | 0.2495 | 343,154.1 | 343,424.4 | 116.1 | 1.000x | 1.000x | faster ×2.09 | -52.19% vs bar 4.03% (band) → **improve** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 718,170.1 | 0.5218 | 717,929.0 | 718,508.5 | 211.1 | 2.091x | 2.091x | - | - |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 263,947.0 | 0.2517 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 553,056.2 | 0.5274 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 64,523.6 | 0.2461 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 135,393.9 | 0.5165 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 14,750.4 | 0.2251 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 29,643.5 | 0.4523 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 263,947.0 ns, 1,048,576 B

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.4 | 687.2 | 687.9 | 0.2 | 1.000x | 1.000x | faster ×1.03 | -3.11% vs bar 2.35% (band) → **improve** | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 709.4 | 708.6 | 711.2 | 0.9 | 1.032x | 1.032x | - | - | 75 | 9.5 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-slack-webhook`, 35.9 ns, 81 B; largest Δ: `sd-router-short`, -4.1 ns (now 29.4 ns), 6 B

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,140.0 | 0.0168 | 23,118.8 | 23,157.6 | 14.1 | 1.000x | 1.000x | unchanged (within spread) | -0.04% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,149.1 | 0.0168 | 23,145.6 | 23,182.5 | 14.8 | 1.000x | 1.000x | - | - |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,650.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,643.0 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.9 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,393.3 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,113.7 | 0.0170 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,650.6 ns, 1,048,576 B; largest Δ: `t-256k`, -10.3 ns (now 4,382.9 ns), 262,144 B

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,120.8 | 1,119.2 | 1,131.3 | 4.4 | 1.000x | 1.000x | - | - | 75 | 14.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,213.5 | 1,212.7 | 1,220.0 | 3.1 | 1.083x | 1.083x | slower ×1.08 | +8.27% vs bar 1.41% (band) → **regress** | 75 | 16.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `br-tag-mismatch`, 192.3 ns, 19 B; largest Δ: `rec-tag-depth3`, +8.9 ns (now 124.9 ns), 22 B

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,107.0 | 0.0168 | 23,100.5 | 23,138.2 | 14.2 | 1.000x | 1.000x | unchanged (within spread) | -0.07% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,122.2 | 0.0168 | 23,090.4 | 24,726.0 | 644.6 | 1.001x | 1.001x | - | - |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,620.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,625.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,388.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,107.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,112.4 | 0.0170 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,620.6 ns, 1,048,576 B; largest Δ: `t-256k`, -9.8 ns (now 4,379.0 ns), 262,144 B

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,066.1 | 1,062.5 | 1,066.5 | 1.5 | 1.000x | 1.000x | - | - | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,139.2 | 1,135.7 | 1,144.4 | 3.1 | 1.069x | 1.069x | slower ×1.07 | +6.85% vs bar 1.41% (band) → **regress** | 75 | 15.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `br-tag-mismatch`, 173.2 ns, 19 B; largest Δ: `br-tag-pair`, +4.0 ns (now 75.6 ns), 18 B

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 47.2 | 0.0000 | 46.9 | 47.3 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -0.50% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 47.4 | 0.0000 | 47.3 | 47.7 | 0.1 | 1.005x | 1.005x | - | - |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 15.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 15.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 15.8 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 15.7 ns, 262,144 B

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 10,180,134.9 | 10,178,593.5 | 10,185,240.5 | 2,678.3 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | - | - | 75 | 135,735.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,184,333.1 | 10,180,682.9 | 10,194,056.2 | 4,531.4 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | unchanged (within spread) | +0.04% (null control: program identical) | 75 | 135,791.1 | 8.9 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `rd-trim-near-miss`, 10,182,930.7 ns, 20 B

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 480,758.4 | 0.3493 | 480,060.6 | 481,148.2 | 478.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 481,402.0 | 0.3498 | 481,072.5 | 481,492.0 | 147.0 | 1.001x | 1.001x | unchanged (within spread) | +0.13% (null control: program identical) |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 366,555.4 | 0.3496 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 366,548.7 | 0.3496 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 91,620.5 | 0.3495 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,710.0 | 0.3498 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 22,601.6 | 0.3449 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,074.0 | 0.3521 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 366,548.7 ns, 1,048,576 B; largest Δ: `t-64k`, +472.4 ns (now 23,074.0 ns), 65,536 B

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,204.7 | 1,200.0 | 1,207.7 | 2.9 | 1.000x | 1.000x | - | - | 75 | 16.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,208.8 | 1,205.7 | 1,212.0 | 2.1 | 1.003x | 1.003x | unchanged (within spread) | +0.34% (null control: program identical) | 75 | 16.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 55.6 ns, 93 B

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 14.7 | 0.0000 | 14.4 | 14.8 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 0.0000 | 14.7 | 15.0 | 0.1 | 1.007x | 1.007x | unchanged (within spread) | +0.72% (null control: program identical) |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 4.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 5.0 ns, 262,144 B

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 520.7 | 517.1 | 525.4 | 3.0 | 1.000x | 1.000x | - | - | 75 | 6.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 521.4 | 517.8 | 532.5 | 5.3 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) | 75 | 7.0 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 39.6 ns, 36 B

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 219,310.8 | 0.1594 | 219,141.4 | 219,634.2 | 178.1 | 1.000x | 1.000x | faster ×1.00 | -0.20% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 219,742.8 | 0.1597 | 219,557.6 | 219,877.1 | 119.3 | 1.002x | 1.002x | - | - |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 168,903.9 | 0.1611 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 169,309.0 | 0.1615 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 40,322.7 | 0.1538 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 40,223.5 | 0.1534 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,119.8 | 0.1544 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10,117.5 | 0.1544 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 168,903.9 ns, 1,048,576 B

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 679.2 | 677.7 | 680.6 | 1.0 | 1.000x | 1.000x | - | - | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 679.7 | 677.6 | 680.9 | 1.2 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) | 75 | 9.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-syslog`, 18.2 ns, 56 B; largest Δ: `rec-array-define`, +0.3 ns (now 17.4 ns), 11 B

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 4,197,582.0 | 3.0500 | 4,195,748.7 | 4,198,026.8 | 823.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,197,626.6 | 3.0500 | 4,195,320.1 | 4,199,298.7 | 1,396.3 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,197,902.6 | 3.0498 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,199,059.3 | 3.0509 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 800,466.3 | 3.0535 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 800,126.6 | 3.0522 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 198,600.6 | 3.0304 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 198,822.6 | 3.0338 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,199,059.3 ns, 1,048,576 B

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,408.2 | 2,406.0 | 2,412.5 | 2.7 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 32.1 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,410.2 | 2,407.9 | 2,413.8 | 2.2 | 1.001x | 1.001x | - | - | 75 | 32.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 178.6 ns, 93 B; largest Δ: `cg-array-begin`, +1.4 ns (now 8.9 ns), 1 B

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,161,777.6 | 1.5708 | 2,157,756.8 | 2,164,971.7 | 2,408.9 | 1.000x | 1.000x | faster ×1.01 | -0.70% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,177,114.0 | 1.5819 | 2,171,793.7 | 2,189,096.9 | 6,123.2 | 1.007x | 1.007x | - | - |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,657,528.3 | 1.5807 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 1,665,919.6 | 1.5887 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 402,144.7 | 1.5341 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 406,777.9 | 1.5517 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 102,167.9 | 1.5590 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 102,175.6 | 1.5591 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,657,528.3 ns, 1,048,576 B

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,383.1 | 1,374.1 | 1,390.5 | 5.3 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) | 75 | 18.4 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,384.3 | 1,354.0 | 1,386.6 | 12.2 | 1.001x | 1.001x | - | - | 75 | 18.5 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 69.6 ns, 20 B; largest Δ: `v-uuid-valid`, -1.1 ns (now 16.1 ns), 36 B

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,103.9 | 0.0168 | 23,092.4 | 23,109.7 | 5.7 | 1.000x | 1.000x | faster ×1.00 | -0.16% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,140.0 | 0.0168 | 23,130.0 | 23,171.4 | 15.1 | 1.002x | 1.002x | - | - |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,604.8 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,639.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,381.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,390.3 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,107.5 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,604.8 ns, 1,048,576 B

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 661.6 | 660.9 | 662.0 | 0.4 | 1.000x | 1.000x | - | - | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 661.7 | 660.1 | 662.6 | 0.9 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 8.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `cg-object-begin`, 17.0 ns, 1 B

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,109.0 | 0.0168 | 23,096.3 | 23,113.9 | 6.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,109.7 | 0.0168 | 23,084.1 | 23,144.7 | 21.7 | 1.000x | 1.000x | unchanged (within spread) | +0.00% (null control: program identical) |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,619.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,607.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,387.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,109.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,111.1 | 0.0170 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,607.1 ns, 1,048,576 B

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 723.8 | 721.9 | 726.4 | 1.9 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 724.1 | 723.8 | 724.9 | 0.4 | 1.001x | 1.001x | - | - | 75 | 9.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 35.2 ns, 24 B; largest Δ: `lp-winpath`, -0.1 ns (now 26.5 ns), 22 B

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 32.2 | 0.0000 | 32.1 | 40.5 | 3.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 0.0000 | 32.5 | 32.7 | 0.1 | 1.010x | 1.010x | unchanged (within spread) | +0.96% (null control: program identical) |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 10.9 ns, 262,144 B

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 952.9 | 951.8 | 963.7 | 5.1 | 1.000x | 1.000x | unchanged (within spread) | -0.17% (null control: program identical) | 75 | 12.7 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 954.6 | 953.9 | 963.8 | 3.8 | 1.002x | 1.002x | - | - | 75 | 12.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `dt-iso8601`, 93.3 ns, 20 B

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 4,046,219.2 | 2.9400 | 4,045,132.0 | 4,060,357.5 | 5,670.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,058,134.8 | 2.9487 | 4,044,291.1 | 4,223,617.9 | 67,731.3 | 1.003x | 1.003x | unchanged (within spread) | +0.29% (null control: program identical) |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,100,354.0 | 2.9567 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,109,180.9 | 2.9651 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 763,508.2 | 2.9126 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,673.8 | 2.9056 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 184,266.8 | 2.8117 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 185,099.4 | 2.8244 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,109,180.9 ns, 1,048,576 B

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,454.1 | 2,448.2 | 2,499.3 | 19.1 | 1.000x | 1.000x | - | - | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,454.4 | 2,450.8 | 2,520.9 | 26.8 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) | 75 | 32.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 117.8 ns, 20 B; largest Δ: `waf-comment-obfuscation`, -1.5 ns (now 54.9 ns), 18 B

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 4,011,091.7 | 2.9145 | 4,006,359.2 | 4,015,737.3 | 3,011.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,016,077.8 | 2.9181 | 4,005,031.0 | 4,048,101.7 | 17,917.6 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,073,761.7 | 2.9314 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,078,760.7 | 2.9361 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 755,142.0 | 2.8806 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 754,672.1 | 2.8788 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 182,225.8 | 2.7805 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 182,584.1 | 2.7860 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,078,760.7 ns, 1,048,576 B

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,431.5 | 2,429.4 | 2,931.8 | 199.2 | 1.000x | 1.000x | unchanged (within spread) | -0.14% (null control: program identical) | 75 | 32.4 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,434.9 | 2,427.1 | 2,480.6 | 19.5 | 1.001x | 1.001x | - | - | 75 | 32.5 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 116.6 ns, 20 B; largest Δ: `sec-aws-key`, -1.0 ns (now 43.1 ns), 20 B

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007,600.2 | 0.7321 | 1,007,490.2 | 1,008,452.4 | 349.7 | 1.000x | 1.000x | unchanged (within spread) | -0.24% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,010,032.8 | 0.7339 | 1,009,551.4 | 1,013,141.8 | 1,294.6 | 1.002x | 1.002x | - | - |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 771,752.2 | 0.7360 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 773,709.5 | 0.7379 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 188,328.7 | 0.7184 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 188,555.1 | 0.7193 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 47,627.3 | 0.7267 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 47,776.1 | 0.7290 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 771,752.2 ns, 1,048,576 B

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,931.1 | 1,919.8 | 1,939.0 | 7.6 | 1.000x | 1.000x | unchanged (within spread) | -0.45% (null control: program identical) | 75 | 25.7 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,939.8 | 1,936.0 | 1,948.0 | 4.0 | 1.005x | 1.005x | - | - | 75 | 25.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 152.1 ns, 16 B; largest Δ: `br-quoted-delim`, +4.3 ns (now 117.3 ns), 15 B

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 929,037.9 | 0.6750 | 928,706.1 | 929,382.6 | 267.3 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 931,350.2 | 0.6767 | 929,680.2 | 932,877.6 | 1,169.7 | 1.002x | 1.002x | - | - |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 710,823.5 | 0.6779 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 712,687.9 | 0.6797 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 173,862.3 | 0.6632 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 174,580.5 | 0.6660 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 44,070.5 | 0.6725 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 44,118.7 | 0.6732 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 710,823.5 ns, 1,048,576 B

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,834.4 | 1,822.6 | 1,890.7 | 24.7 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) | 75 | 24.5 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,834.9 | 1,828.6 | 1,846.0 | 6.6 | 1.000x | 1.000x | - | - | 75 | 24.5 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 126.7 ns, 16 B; largest Δ: `br-quoted-delim`, +7.9 ns (now 98.2 ns), 15 B

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,988,946.6 | 2.8984 | 3,985,988.0 | 3,990,696.5 | 1,928.7 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 3,990,257.9 | 2.8994 | 3,986,286.8 | 3,991,754.8 | 1,941.2 | 1.000x | 1.000x | - | - |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,036,180.2 | 2.8955 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,038,248.6 | 2.8975 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,018.1 | 2.9031 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 760,985.0 | 2.9029 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 190,600.3 | 2.9083 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 190,650.2 | 2.9091 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,036,180.2 ns, 1,048,576 B

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,781.8 | 1,776.2 | 1,783.7 | 2.8 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) | 75 | 23.8 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,782.3 | 1,779.9 | 1,817.3 | 14.2 | 1.000x | 1.000x | - | - | 75 | 23.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `lp-syslog`, 640.0 ns, 56 B

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,121.0 | 0.0168 | 23,113.0 | 23,144.3 | 10.7 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,134.1 | 0.0168 | 23,113.5 | 23,155.0 | 14.9 | 1.001x | 1.001x | - | - |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,630.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,634.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,389.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,113.1 | 0.0170 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,630.3 ns, 1,048,576 B; largest Δ: `t-256k`, -9.7 ns (now 4,379.4 ns), 262,144 B

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 930.6 | 926.9 | 933.5 | 2.2 | 1.000x | 1.000x | - | - | 75 | 12.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 933.1 | 925.3 | 934.3 | 3.6 | 1.003x | 1.003x | unchanged (within spread) | +0.27% (null control: program identical) | 75 | 12.4 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `lp-winpath`, 78.3 ns, 22 B

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 3,939,620.9 | 2.8626 | 3,939,163.4 | 3,941,338.8 | 794.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,941,061.0 | 2.8636 | 3,940,441.6 | 3,943,170.1 | 1,103.4 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,001,735.7 | 2.8627 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,003,059.3 | 2.8639 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 751,286.2 | 2.8659 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 751,290.9 | 2.8659 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 186,444.5 | 2.8449 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 186,921.8 | 2.8522 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,003,059.3 ns, 1,048,576 B

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,165.8 | 1,165.7 | 1,172.4 | 2.6 | 1.000x | 1.000x | unchanged (within spread) | -0.06% (null control: program identical) | 75 | 15.5 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,166.6 | 1,164.5 | 1,173.4 | 3.2 | 1.001x | 1.001x | - | - | 75 | 15.6 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 178.0 ns, 93 B; largest Δ: `sec-aws-key`, -0.4 ns (now 96.8 ns), 20 B

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 124,699.4 | 0.0906 | 124,535.5 | 124,820.2 | 93.7 | 1.000x | 1.000x | faster ×1.04 | -3.52% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 129,253.0 | 0.0939 | 129,074.0 | 129,503.1 | 145.3 | 1.037x | 1.037x | - | - |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 102,066.8 | 0.0973 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 106,372.5 | 0.1014 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 18,930.6 | 0.0722 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 19,480.6 | 0.0743 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 3,621.6 | 0.0553 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 3,427.7 | 0.0523 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 102,066.8 ns, 1,048,576 B

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,085.3 | 1,082.7 | 1,085.9 | 1.2 | 1.000x | 1.000x | - | - | 75 | 14.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,515.1 | 1,513.6 | 1,517.9 | 1.5 | 1.396x | 1.396x | slower ×1.40 | +39.60% vs bar 1.41% (band) → **regress** | 75 | 20.2 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 464.8 ns, 93 B

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 347,728.5 | 0.2527 | 347,602.5 | 347,874.2 | 103.5 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 354,034.8 | 0.2572 | 353,916.6 | 354,061.6 | 62.9 | 1.018x | 1.018x | slower ×1.02 | +1.81% vs bar 4.03% (band) → **within** |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 267,016.5 | 0.2546 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 271,742.8 | 0.2592 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 65,636.1 | 0.2504 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 66,855.1 | 0.2550 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 15,002.2 | 0.2289 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15,330.8 | 0.2339 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 271,742.8 ns, 1,048,576 B

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,176.6 | 1,173.0 | 1,182.7 | 3.3 | 1.000x | 1.000x | - | - | 75 | 15.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,252.7 | 1,248.6 | 1,257.5 | 3.2 | 1.065x | 1.065x | slower ×1.06 | +6.47% vs bar 1.41% (band) → **regress** | 75 | 16.7 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 392.1 ns, 81 B

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,099.3 | 0.0168 | 23,094.6 | 23,130.4 | 14.2 | 1.000x | 1.000x | faster ×1.00 | -0.14% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,131.0 | 0.0168 | 23,114.0 | 23,136.2 | 8.6 | 1.001x | 1.001x | - | - |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,611.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,628.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,380.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,386.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,112.7 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,110.5 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,611.2 ns, 1,048,576 B

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,052.5 | 1,051.4 | 1,053.0 | 0.6 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) | 75 | 14.0 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,053.0 | 1,052.3 | 1,054.6 | 1.0 | 1.001x | 1.001x | - | - | 75 | 14.0 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-userpass`, 255.4 ns, 33 B; largest Δ: `waf-benign`, -0.7 ns (now 33.8 ns), 39 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 352,292.7 | 0.2560 | 351,592.9 | 592,751.9 | 96,238.4 | 1.000x | 1.000x | unchanged (within spread) | -1.75% vs bar 4.03% (band) → **within** |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 358,572.8 | 0.2605 | 357,818.4 | 359,102.4 | 413.1 | 1.018x | 1.018x | - | - |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 282,877.2 | 0.2698 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 287,262.2 | 0.2740 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 58,459.8 | 0.2230 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 59,805.1 | 0.2281 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 11,027.6 | 0.1683 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 11,466.1 | 0.1750 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 282,877.2 ns, 1,048,576 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 643.4 | 639.7 | 648.4 | 3.0 | 1.000x | 1.000x | - | - | 75 | 8.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 657.5 | 657.3 | 658.7 | 0.5 | 1.022x | 1.022x | slower ×1.02 | +2.19% vs bar 2.35% (band) → **within** | 75 | 8.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-slack-webhook`, 13.3 ns, 81 B; largest Δ: `nu-high-byte`, -3.0 ns (now 5.0 ns), 2 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 26.9 | 0.0000 | 26.8 | 28.7 | 0.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 0.0000 | 39.2 | 39.8 | 0.2 | 1.459x | 1.459x | slower ×1.46 | +45.87% vs bar 3.96% (band) → **regress** |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 9.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 13.1 ns, 262,144 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 617.5 | 617.1 | 618.3 | 0.5 | 1.000x | 1.000x | - | - | 75 | 8.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 872.5 | 871.5 | 877.4 | 2.2 | 1.413x | 1.413x | slower ×1.41 | +41.30% vs bar 2.35% (band) → **regress** | 75 | 11.6 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `la-negation-hit`, 16.5 ns, 19 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,542,898.4 | 5.4807 | 7,521,327.7 | 7,611,419.9 | 30,850.8 | 1.000x | 1.000x | unchanged (within spread) | -0.86% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 7,608,262.5 | 5.5282 | 7,552,875.7 | 7,653,667.4 | 39,793.3 | 1.009x | 1.009x | - | - |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 5,783,435.1 | 5.5155 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 5,820,988.5 | 5.5513 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,418,365.5 | 5.4106 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 1,434,813.3 | 5.4734 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 342,059.0 | 5.2194 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 345,013.8 | 5.2645 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 5,783,435.1 ns, 1,048,576 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,855.3 | 2,847.2 | 2,860.9 | 5.5 | 1.000x | 1.000x | - | - | 75 | 38.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,860.5 | 2,850.4 | 2,876.2 | 10.2 | 1.002x | 1.002x | unchanged (within spread) | +0.18% (null control: program identical) | 75 | 38.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 926.5 ns, 61 B; largest Δ: `v-us-zip`, -2.1 ns (now 34.2 ns), 5 B

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 39.3 | 0.0000 | 38.2 | 40.0 | 0.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.5 | 0.0000 | 37.3 | 42.1 | 1.6 | 1.006x | 1.006x | unchanged (within spread) | +0.56% (null control: program identical) |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 14.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 11.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 12.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 12.3 | 0.0002 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 15.2 ns, 1,048,576 B

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,053.2 | 1,049.7 | 1,064.7 | 5.2 | 1.000x | 1.000x | unchanged (within spread) | -0.45% (null control: program identical) | 75 | 14.0 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,057.9 | 1,041.5 | 1,063.8 | 7.9 | 1.004x | 1.004x | - | - | 75 | 14.1 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 72.5 ns, 93 B; largest Δ: `v-email`, +1.1 ns (now 51.5 ns), 24 B

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 0.0000 | 26.2 | 26.4 | 0.1 | 1.000x | 1.000x | faster ×1.02 | -1.68% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 0.0000 | 26.6 | 26.8 | 0.1 | 1.017x | 1.017x | - | - |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 8.8 ns, 1,048,576 B; largest Δ: `t-64k`, -0.2 ns (now 8.8 ns), 65,536 B

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 795.7 | 793.0 | 796.2 | 1.4 | 1.000x | 1.000x | faster ×1.02 | -1.98% (null control: program identical) | 75 | 10.6 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 811.7 | 811.5 | 811.8 | 0.1 | 1.020x | 1.020x | - | - | 75 | 10.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `v-ipv4`, 64.1 ns, 11 B

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 0.0000 | 26.7 | 28.4 | 0.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 0.0000 | 26.7 | 26.8 | 0.1 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 8.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 8.9 ns, 65,536 B

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 734.9 | 734.4 | 735.7 | 0.4 | 1.000x | 1.000x | - | - | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 735.1 | 734.8 | 738.1 | 1.2 | 1.000x | 1.000x | unchanged (within spread) | +0.03% (null control: program identical) | 75 | 9.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 32.0 ns, 10 B; largest Δ: `rd-numeric-id-hit`, +0.3 ns (now 12.3 ns), 4 B

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 81,991.4 | 0.0596 | 81,889.3 | 82,716.1 | 338.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 82,536.0 | 0.0600 | 82,271.7 | 83,000.2 | 264.8 | 1.007x | 1.007x | unchanged (within spread) | +0.66% vs bar 4.03% (band) → **within** |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 68,295.4 | 0.0651 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 68,444.1 | 0.0653 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 11,334.1 | 0.0432 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11,619.0 | 0.0443 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 2,437.9 | 0.0372 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 2,400.0 | 0.0366 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 68,444.1 ns, 1,048,576 B; largest Δ: `t-256k`, +284.8 ns (now 11,619.0 ns), 262,144 B

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 681.9 | 677.9 | 685.3 | 2.7 | 1.000x | 1.000x | faster ×1.14 | -12.04% vs bar 2.35% (band) → **improve** | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 775.2 | 770.3 | 787.5 | 5.7 | 1.137x | 1.137x | - | - | 75 | 10.3 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `v-uuid-valid`, 92.0 ns, 36 B; largest Δ: `v-uuid-badnibble`, -5.5 ns (now 90.1 ns), 36 B

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,080,790.5 | 2.9651 | 4,077,154.4 | 4,088,404.5 | 3,759.2 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 4,082,159.3 | 2.9661 | 4,079,596.5 | 4,085,436.5 | 2,105.9 | 1.000x | 1.000x | - | - |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,112,749.5 | 2.9685 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 3,112,942.9 | 2.9687 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 776,394.8 | 2.9617 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 777,709.3 | 2.9667 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 191,610.1 | 2.9237 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 191,674.3 | 2.9247 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 3,112,749.5 ns, 1,048,576 B; largest Δ: `t-256k`, -1,314.5 ns (now 776,394.8 ns), 262,144 B

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 2,692.5 | 2,690.1 | 2,702.7 | 4.5 | 1.000x | 1.000x | - | - | 75 | 35.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,693.0 | 2,687.0 | 2,694.9 | 2.9 | 1.000x | 1.000x | unchanged (within spread) | +0.02% (null control: program identical) | 75 | 35.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `sec-github-pat`, 184.8 ns, 93 B; largest Δ: `sec-slack-webhook`, +0.9 ns (now 156.0 ns), 81 B

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,357,172.5 | 0.9861 | 1,355,617.8 | 1,360,635.2 | 1,888.0 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,358,250.8 | 0.9869 | 1,356,936.6 | 1,360,266.0 | 1,085.5 | 1.001x | 1.001x | - | - |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,028,682.2 | 0.9810 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 1,030,231.8 | 0.9825 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 260,617.0 | 0.9942 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 259,647.7 | 0.9905 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 67,873.2 | 1.0357 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 68,228.8 | 1.0411 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,028,682.2 ns, 1,048,576 B

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.3 | 664.0 | 670.7 | 2.7 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 669.0 | 666.1 | 672.2 | 2.2 | 1.002x | 1.002x | - | - | 75 | 8.9 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `waf-concat`, 47.3 ns, 48 B; largest Δ: `waf-sleep`, -3.2 ns (now 44.3 ns), 16 B

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 997,728.6 | 0.7250 | 995,339.0 | 1,004,743.7 | 3,211.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,000,077.4 | 0.7267 | 997,444.6 | 1,001,259.3 | 1,549.1 | 1.002x | 1.002x | unchanged (within spread) | +0.24% (null control: program identical) |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 760,098.1 | 0.7249 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 759,695.9 | 0.7245 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 190,235.8 | 0.7257 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 192,069.1 | 0.7327 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 48,126.1 | 0.7343 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 48,170.8 | 0.7350 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 759,695.9 ns, 1,048,576 B; largest Δ: `t-256k`, +1,833.3 ns (now 192,069.1 ns), 262,144 B

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 1,092.1 | 1,082.5 | 1,683.1 | 237.2 | 1.000x | 1.000x | - | - | 75 | 14.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,095.0 | 1,079.0 | 1,109.4 | 9.9 | 1.003x | 1.003x | unchanged (within spread) | +0.27% (null control: program identical) | 75 | 14.6 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `waf-union`, 75.0 ns, 43 B; largest Δ: `cg-constant`, -1.3 ns (now 9.0 ns), 4 B

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,133,714.5 | 8.8165 | 12,106,982.1 | 12,242,434.1 | 49,192.1 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 12,136,502.5 | 8.8185 | 12,109,053.2 | 12,271,334.1 | 60,169.4 | 1.000x | 1.000x | - | - |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9,252,129.7 | 8.8235 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 9,248,818.5 | 8.8204 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,306,117.0 | 8.7971 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 2,305,130.4 | 8.7934 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 575,832.8 | 8.7865 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 576,687.6 | 8.7996 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 9,252,129.7 ns, 1,048,576 B

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,333.2 | 7,324.9 | 7,359.1 | 13.3 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) | 75 | 97.8 | 8.9 | 100% |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 7,335.5 | 7,305.0 | 7,403.6 | 33.0 | 1.000x | 1.000x | - | - | 75 | 97.8 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 448.5 ns, 81 B

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 23,132.0 | 0.0168 | 23,110.7 | 23,144.0 | 11.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,172.9 | 0.0168 | 23,111.3 | 23,183.8 | 26.4 | 1.002x | 1.002x | unchanged (within spread) | +0.18% vs bar 4.03% (band) → **within** |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 17,630.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,641.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 4,393.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,419.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 1,107.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,106.2 | 0.0169 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 17,641.3 ns, 1,048,576 B; largest Δ: `t-256k`, +25.9 ns (now 4,419.2 ns), 262,144 B

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 638.3 | 635.2 | 639.4 | 1.6 | 1.000x | 1.000x | - | - | 75 | 8.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 694.0 | 692.4 | 697.3 | 1.7 | 1.087x | 1.087x | slower ×1.09 | +8.74% vs bar 2.35% (band) → **regress** | 75 | 9.3 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `waf-comment-obfuscation`, 78.6 ns, 18 B; largest Δ: `cg-object-begin`, -2.7 ns (now 4.1 ns), 1 B

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20.2 | 0.0000 | 20.0 | 20.3 | 0.1 | 1.000x | 1.000x | faster ×1.04 | -3.96% (null control: program identical) |
| 2 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 21.0 | 0.0000 | 20.8 | 21.2 | 0.1 | 1.041x | 1.041x | - | - |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_ce658cb7_auto-caps-simdna` | 7.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_ce658cb7_auto-caps-simdna` | 7.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_ce658cb7_auto-caps-simdna` | 7.0 | 0.0001 |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `t-1m`, 6.8 ns, 1,048,576 B; largest Δ: `t-256k`, -0.3 ns (now 6.7 ns), 262,144 B

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_ce658cb7_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_ce658cb7_auto-caps-simdna` | measured | `plain` | same program | 465.9 | 461.3 | 473.5 | 4.9 | 1.000x | 1.000x | - | - | 75 | 6.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 476.8 | 471.2 | 487.6 | 5.6 | 1.023x | 1.023x | unchanged (within spread) | +2.35% (null control: program identical) | 75 | 6.4 | 8.9 | 100% |

- Δ detail: `pcrec_02902356_auto-caps-simdna` vs previous `pcrec_ce658cb7_auto-caps-simdna`: worst now: `lp-winpath`, 32.2 ns, 22 B; largest Δ: `rec-comment-nested`, +0.3 ns (now 5.7 ns), 34 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_02902356_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_02902356_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,868 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,075 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,180 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,782 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,887 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1464301 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1485508 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,868 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_ce658cb7_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,075 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,180 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,782 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,887 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1464301 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1485508 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_ce658cb7_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - `prefilter declined, no cap hit` = pcrec abi 14's `declined-nullable-default` ([OPT-4.2]): the SAME ask-(b) bucket (sel is neither `selected` nor `forced`) but NOTHING overflowed -- no rung was involved, and the ordinary hybrid's own EXACT prefilter language is nullable, so the prefilter was declined. pcrec's own reading keeps it out of the five `fell back` values for that reason (match_api.md 6.3); this column keeps it in the bucket and says which reading it is, so a row is never read as a cap that was hit. Such an artifact carries `vm_prefilter=none` and NO `lang=` clause.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `pcrec_02902356_auto-caps-simdna` | 205,068,114.0 | 197,968,411.0 | 209,023,102.0 | 3,622,965.8 | 5 | 27,592 | 25,703 | 25,418 | 0.018 (max is trial 1) | compiled=5 | 1,641,007.0 | 203,382,906.0 | 103,830.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,275,326.0 | 201,234,125.0 | 224,838,786.0 | 7,509,753.4 | 5 | 31,688 | 25,921 | 25,636 | 0.035 | compiled=5 | 1,902,869.0 | 212,265,687.0 | 107,750.0 |
| `balanced-parens-rec` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 211,496,463.0 | 201,863,381.0 | 215,140,093.0 | 4,501,642.6 | 5 | 27,592 | 25,459 | 25,228 | 0.021 (max is trial 1) | compiled=5 | 1,672,189.0 | 209,738,404.0 | 199,051.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 206,083,595.0 | 197,640,040.0 | 217,597,136.0 | 6,792,440.8 | 5 | 31,688 | 25,677 | 25,446 | 0.033 | compiled=5 | 1,649,748.0 | 204,330,386.0 | 103,461.0 |
| `base10num-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,094,211.0 | 138,333,610.0 | 151,301,477.0 | 4,719,692.3 | 5 | 27,648 | 16,320 | 13,935 | 0.032 | compiled=5 | 1,631,628.0 | 146,294,401.0 | 101,161.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 137,940,318.0 | 136,577,931.0 | 146,910,385.0 | 4,662,255.4 | 5 | 27,576 | 15,773 | 13,388 | 0.034 | compiled=5 | 1,635,779.0 | 136,205,539.0 | 194,471.0 |
| `base10num-near-miss` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 144,536,877.0 | 140,355,526.0 | 154,074,868.0 | 4,995,534.2 | 5 | 27,648 | 16,320 | 13,935 | 0.035 | compiled=5 | 1,623,739.0 | 142,000,304.0 | 103,291.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 148,313,988.0 | 137,847,292.0 | 148,416,048.0 | 4,127,079.6 | 5 | 27,576 | 15,773 | 13,388 | 0.028 | compiled=5 | 1,597,198.0 | 146,606,069.0 | 106,600.0 |
| `bracket-array-define` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,270,669.0 | 211,163,963.0 | 224,199,463.0 | 4,882,486.6 | 5 | 31,648 | 26,139 | 25,824 | 0.022 | compiled=5 | 1,686,498.0 | 221,482,451.0 | 101,720.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 228,014,961.0 | 222,442,095.0 | 241,491,844.0 | 6,362,092.8 | 5 | 31,648 | 26,254 | 25,939 | 0.028 (max is trial 1) | compiled=5 | 1,699,348.0 | 225,781,060.0 | 114,391.0 |
| `bracket-array-define` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 224,989,696.0 | 215,514,385.0 | 238,922,569.0 | 7,942,112.9 | 5 | 31,648 | 26,139 | 25,824 | 0.035 | compiled=5 | 1,668,649.0 | 223,220,096.0 | 111,300.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 223,341,706.0 | 211,471,363.0 | 224,624,553.0 | 5,068,859.8 | 5 | 31,648 | 26,254 | 25,939 | 0.023 | compiled=5 | 1,697,139.0 | 221,454,386.0 | 197,471.0 |
| `codegrammar-flat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 350,410,210.0 | 347,739,808.0 | 352,229,248.0 | 1,465,395.4 | 5 | 31,984 | 35,289 | 26,690 | 0.004 | compiled=5 | 2,188,300.0 | 348,176,700.0 | 102,460.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,590,435.0 | 343,778,670.0 | 361,485,642.0 | 6,386,224.1 | 5 | 32,032 | 35,010 | 27,498 | 0.018 | compiled=5 | 2,135,140.0 | 349,531,146.0 | 99,890.0 |
| `codegrammar-flat` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 345,849,347.0 | 342,715,900.0 | 353,783,799.0 | 3,857,195.7 | 5 | 31,984 | 35,289 | 26,690 | 0.011 | compiled=5 | 2,137,952.0 | 343,689,266.0 | 204,761.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 358,873,626.0 | 349,862,408.0 | 366,463,897.0 | 6,071,276.6 | 5 | 32,032 | 35,010 | 27,498 | 0.017 | compiled=5 | 4,368,923.0 | 355,489,418.0 | 102,171.0 |
| `codegrammar-xflag` | `plain` | `pcrec_02902356_auto-caps-simdna` | 349,902,468.0 | 344,855,334.0 | 351,068,773.0 | 2,466,814.7 | 5 | 32,024 | 35,615 | 26,937 | 0.007 | compiled=5 | 2,202,800.0 | 347,633,747.0 | 104,040.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,322,484.0 | 344,475,522.0 | 358,781,989.0 | 4,895,962.2 | 5 | 32,072 | 35,340 | 27,749 | 0.014 | compiled=5 | 2,154,780.0 | 348,723,862.0 | 111,441.0 |
| `codegrammar-xflag` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 349,565,027.0 | 346,881,573.0 | 352,156,491.0 | 1,709,071.6 | 5 | 32,024 | 35,615 | 26,937 | 0.005 | compiled=5 | 2,146,052.0 | 347,319,245.0 | 110,841.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 358,947,867.0 | 351,192,526.0 | 362,893,308.0 | 3,946,634.1 | 5 | 32,072 | 35,340 | 27,749 | 0.011 (max is trial 1) | compiled=5 | 2,154,192.0 | 356,681,615.0 | 189,981.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 224,567,663.0 | 217,270,151.0 | 232,909,143.0 | 5,249,245.5 | 5 | 32,008 | 32,574 | 26,943 | 0.023 | compiled=5 | 2,034,759.0 | 222,317,773.0 | 171,681.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 229,759,429.0 | 227,431,818.0 | 235,263,025.0 | 2,622,800.3 | 5 | 32,096 | 34,600 | 28,351 | 0.011 | compiled=5 | 2,097,270.0 | 227,096,016.0 | 103,261.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 217,433,835.0 | 216,727,771.0 | 224,144,961.0 | 3,321,608.2 | 5 | 32,008 | 32,574 | 26,943 | 0.015 | compiled=5 | 2,019,151.0 | 215,208,793.0 | 101,990.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 229,293,038.0 | 222,432,261.0 | 232,167,944.0 | 3,674,411.0 | 5 | 32,096 | 34,600 | 28,351 | 0.016 | compiled=5 | 2,076,991.0 | 226,990,636.0 | 98,750.0 |
| `date-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 251,160,339.0 | 249,828,153.0 | 264,233,379.0 | 5,768,044.1 | 5 | 31,872 | 33,439 | 31,413 | 0.023 | compiled=5 | 1,862,789.0 | 249,273,970.0 | 188,011.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 249,914,942.0 | 246,615,467.0 | 257,896,949.0 | 4,535,537.5 | 5 | 31,872 | 33,367 | 31,341 | 0.018 | compiled=5 | 1,881,209.0 | 247,932,523.0 | 117,800.0 |
| `date-nested-plus` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 258,433,393.0 | 250,968,794.0 | 259,320,068.0 | 3,639,106.6 | 5 | 31,872 | 33,439 | 31,413 | 0.014 | compiled=5 | 1,903,120.0 | 256,322,122.0 | 111,300.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 256,881,144.0 | 250,905,902.0 | 262,433,893.0 | 3,745,741.1 | 5 | 31,872 | 33,367 | 31,341 | 0.015 (max is trial 1) | compiled=5 | 1,877,870.0 | 254,911,753.0 | 100,990.0 |
| `doubled-word` | `plain` | `pcrec_02902356_auto-caps-simdna` | 215,788,773.0 | 207,712,437.0 | 216,861,368.0 | 3,390,669.8 | 5 | 27,504 | 24,373 | 23,911 | 0.016 | compiled=5 | 1,680,198.0 | 213,931,115.0 | 196,271.0 |
| `doubled-word` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,520,938.0 | 208,120,917.0 | 221,358,749.0 | 4,855,937.6 | 5 | 27,504 | 24,486 | 24,024 | 0.023 (max is trial 1) | compiled=5 | 1,686,258.0 | 212,716,719.0 | 118,301.0 |
| `doubled-word` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 215,167,273.0 | 202,054,934.0 | 218,506,601.0 | 6,094,074.9 | 5 | 27,504 | 24,373 | 23,911 | 0.028 | compiled=5 | 1,657,419.0 | 213,396,013.0 | 106,240.0 |
| `doubled-word` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 207,039,040.0 | 196,110,231.0 | 210,676,399.0 | 4,927,954.9 | 5 | 27,504 | 24,486 | 24,024 | 0.024 | compiled=5 | 1,660,579.0 | 205,161,440.0 | 195,821.0 |
| `dup-param-detect` | `plain` | `pcrec_02902356_auto-caps-simdna` | 234,612,641.0 | 227,933,080.0 | 241,146,671.0 | 4,181,673.6 | 5 | 31,776 | 27,325 | 26,809 | 0.018 (max is trial 1) | compiled=5 | 1,754,538.0 | 232,771,902.0 | 110,041.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,092,611.0 | 217,763,663.0 | 234,533,541.0 | 6,289,871.0 | 5 | 31,776 | 27,438 | 26,922 | 0.027 | compiled=5 | 1,725,488.0 | 226,268,403.0 | 104,011.0 |
| `dup-param-detect` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 233,862,842.0 | 229,457,928.0 | 237,480,812.0 | 2,674,929.6 | 5 | 31,776 | 27,081 | 26,619 | 0.011 | compiled=5 | 1,749,229.0 | 232,027,562.0 | 106,071.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 233,465,061.0 | 233,129,327.0 | 237,728,501.0 | 1,738,737.2 | 5 | 31,776 | 27,194 | 26,732 | 0.007 (max is trial 1) | compiled=5 | 1,748,419.0 | 231,631,100.0 | 107,830.0 |
| `email-local-nodup` | `plain` | `pcrec_02902356_auto-caps-simdna` | 204,559,462.0 | 191,806,192.0 | 205,457,235.0 | 5,327,770.4 | 5 | 31,712 | 26,945 | 24,872 | 0.026 | compiled=5 | 1,766,369.0 | 202,687,053.0 | 192,130.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,071,763.0 | 191,308,920.0 | 200,424,182.0 | 3,176,949.1 | 5 | 31,720 | 27,363 | 25,219 | 0.016 | compiled=5 | 1,749,518.0 | 192,347,385.0 | 120,181.0 |
| `email-local-nodup` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 202,318,455.0 | 190,872,634.0 | 205,482,051.0 | 5,919,796.3 | 5 | 31,712 | 26,945 | 24,872 | 0.029 | compiled=5 | 1,746,919.0 | 200,460,754.0 | 107,281.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 199,965,242.0 | 192,848,724.0 | 201,310,449.0 | 3,083,240.9 | 5 | 31,720 | 27,363 | 25,219 | 0.015 | compiled=5 | 1,777,490.0 | 197,986,381.0 | 115,101.0 |
| `email-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,213,978.0 | 214,580,838.0 | 223,994,381.0 | 3,771,618.7 | 5 | 31,832 | 28,826 | 26,880 | 0.017 | compiled=5 | 1,832,518.0 | 221,267,189.0 | 186,060.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 216,172,054.0 | 210,298,878.0 | 223,508,450.0 | 4,860,331.8 | 5 | 31,832 | 29,257 | 27,227 | 0.022 | compiled=5 | 1,800,538.0 | 214,180,096.0 | 192,210.0 |
| `email-nested-plus` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 222,478,092.0 | 213,330,243.0 | 232,987,197.0 | 8,598,220.3 | 5 | 31,832 | 28,826 | 26,880 | 0.039 | compiled=5 | 1,792,800.0 | 220,571,542.0 | 209,701.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 226,874,314.0 | 213,686,274.0 | 230,945,396.0 | 6,639,714.7 | 5 | 31,832 | 29,257 | 27,227 | 0.029 | compiled=5 | 1,834,000.0 | 223,945,530.0 | 198,031.0 |
| `evil-alt-nested` | `plain` | `pcrec_02902356_auto-caps-simdna` | 214,074,876.0 | 209,341,143.0 | 216,527,358.0 | 2,408,841.2 | 5 | 27,552 | 25,358 | 25,358 | 0.011 | compiled=5 | 1,662,718.0 | 212,224,787.0 | 207,241.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,635,217.0 | 201,477,147.0 | 215,388,932.0 | 5,333,958.1 | 5 | 27,552 | 25,471 | 25,471 | 0.025 | compiled=5 | 1,690,068.0 | 212,805,989.0 | 102,860.0 |
| `evil-alt-nested` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 207,793,163.0 | 205,490,861.0 | 216,041,118.0 | 3,625,628.2 | 5 | 27,552 | 25,358 | 25,358 | 0.017 | compiled=5 | 1,671,849.0 | 205,978,434.0 | 104,740.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 213,855,345.0 | 209,000,800.0 | 217,380,985.0 | 2,975,071.7 | 5 | 27,552 | 25,471 | 25,471 | 0.014 | compiled=5 | 1,655,038.0 | 212,010,386.0 | 104,261.0 |
| `file-ext-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,250,270.0 | 140,732,663.0 | 158,455,936.0 | 5,665,182.7 | 5 | 27,792 | 20,895 | 14,772 | 0.038 | compiled=5 | 1,948,959.0 | 145,949,819.0 | 203,391.0 |
| `file-ext-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,129,179.0 | 156,221,896.0 | 173,711,608.0 | 5,936,766.4 | 5 | 27,936 | 24,039 | 16,973 | 0.036 | compiled=5 | 2,138,890.0 | 163,115,219.0 | 205,831.0 |
| `file-ext-order` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 151,595,745.0 | 143,747,963.0 | 158,946,114.0 | 5,274,309.2 | 5 | 27,792 | 21,081 | 14,958 | 0.035 | compiled=5 | 1,937,280.0 | 147,423,833.0 | 101,341.0 |
| `file-ext-order` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 170,934,277.0 | 163,557,819.0 | 174,753,938.0 | 3,656,611.6 | 5 | 27,936 | 24,153 | 17,087 | 0.021 | compiled=5 | 2,167,822.0 | 168,593,686.0 | 109,781.0 |
| `float-literal-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,941,994.0 | 230,001,560.0 | 239,382,663.0 | 3,929,306.9 | 5 | 31,984 | 33,490 | 28,341 | 0.017 | compiled=5 | 2,041,769.0 | 228,819,344.0 | 198,701.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,345,992.0 | 227,149,656.0 | 237,412,245.0 | 3,380,353.5 | 5 | 32,080 | 34,332 | 28,874 | 0.015 | compiled=5 | 2,055,780.0 | 227,823,219.0 | 112,461.0 |
| `float-literal-bound` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 238,353,486.0 | 237,633,152.0 | 239,710,323.0 | 682,665.3 | 5 | 31,984 | 33,490 | 28,341 | 0.003 | compiled=5 | 2,032,131.0 | 236,021,503.0 | 194,561.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 236,588,677.0 | 229,713,410.0 | 237,174,758.0 | 2,797,755.9 | 5 | 32,080 | 34,332 | 28,874 | 0.012 | compiled=5 | 2,054,591.0 | 234,432,915.0 | 114,110.0 |
| `floor-byte` | `plain` | `pcrec_02902356_auto-caps-simdna` | 155,008,700.0 | 143,501,097.0 | 155,719,114.0 | 4,762,276.9 | 5 | 27,792 | 19,408 | 14,411 | 0.031 | compiled=5 | 1,780,579.0 | 153,053,781.0 | 188,591.0 |
| `floor-byte` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,083,528.0 | 155,416,843.0 | 166,119,563.0 | 3,972,416.0 | 5 | 27,936 | 21,863 | 16,540 | 0.024 | compiled=5 | 1,859,818.0 | 163,235,379.0 | 190,261.0 |
| `floor-byte` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 148,447,739.0 | 138,728,516.0 | 160,264,141.0 | 7,642,262.4 | 5 | 27,792 | 19,408 | 14,411 | 0.051 | compiled=5 | 1,775,290.0 | 146,687,219.0 | 117,141.0 |
| `floor-byte` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 159,676,798.0 | 153,092,343.0 | 163,471,658.0 | 3,589,978.5 | 5 | 27,936 | 21,863 | 16,540 | 0.022 | compiled=5 | 1,819,210.0 | 157,380,226.0 | 192,451.0 |
| `high-byte-run` | `plain` | `pcrec_02902356_auto-caps-simdna` | 169,620,318.0 | 153,693,524.0 | 173,204,545.0 | 7,061,656.2 | 5 | 27,488 | 25,653 | 19,347 | 0.042 | compiled=5 | 1,933,769.0 | 167,578,339.0 | 112,740.0 |
| `high-byte-run` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 169,622,188.0 | 163,646,892.0 | 171,473,048.0 | 2,650,434.4 | 5 | 27,928 | 24,467 | 17,340 | 0.016 (max is trial 1) | compiled=5 | 1,949,179.0 | 167,097,708.0 | 199,941.0 |
| `high-byte-run` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 171,219,269.0 | 165,417,828.0 | 172,342,477.0 | 2,944,461.3 | 5 | 27,488 | 25,653 | 19,347 | 0.017 | compiled=5 | 1,929,551.0 | 169,129,449.0 | 100,601.0 |
| `high-byte-run` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 168,737,827.0 | 153,854,517.0 | 170,354,615.0 | 6,572,909.7 | 5 | 27,928 | 24,467 | 17,340 | 0.039 | compiled=5 | 1,928,280.0 | 166,601,265.0 | 198,791.0 |
| `ipv4-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 170,419,577.0 | 161,408,870.0 | 172,392,567.0 | 4,137,927.8 | 5 | 32,608 | 23,285 | 17,969 | 0.024 | compiled=5 | 1,847,110.0 | 166,539,457.0 | 199,661.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 164,072,064.0 | 154,857,626.0 | 166,538,377.0 | 4,241,398.8 | 5 | 32,400 | 22,363 | 17,047 | 0.026 | compiled=5 | 1,882,020.0 | 162,120,374.0 | 194,501.0 |
| `ipv4-near-miss` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 162,943,246.0 | 153,408,425.0 | 170,287,214.0 | 6,054,009.1 | 5 | 32,608 | 23,285 | 17,969 | 0.037 | compiled=5 | 1,720,960.0 | 160,864,174.0 | 198,962.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 158,003,019.0 | 146,682,968.0 | 163,734,809.0 | 5,795,298.7 | 5 | 32,400 | 22,363 | 17,047 | 0.037 | compiled=5 | 1,833,220.0 | 154,151,159.0 | 197,131.0 |
| `keyword-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,124,687.0 | 147,423,135.0 | 159,997,653.0 | 4,588,629.6 | 5 | 27,792 | 21,373 | 14,759 | 0.030 (max is trial 1) | compiled=5 | 3,929,019.0 | 150,279,519.0 | 106,880.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 162,479,826.0 | 159,682,963.0 | 170,528,473.0 | 4,867,929.2 | 5 | 27,936 | 25,794 | 16,968 | 0.030 | compiled=5 | 2,084,449.0 | 160,468,406.0 | 198,911.0 |
| `keyword-prefix-order` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 153,368,764.0 | 146,474,698.0 | 161,429,677.0 | 5,009,855.3 | 5 | 27,792 | 21,932 | 15,318 | 0.033 | compiled=5 | 2,168,592.0 | 148,833,150.0 | 120,311.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 167,922,462.0 | 164,413,654.0 | 173,729,272.0 | 3,752,262.4 | 5 | 27,936 | 26,353 | 17,527 | 0.022 | compiled=5 | 2,085,181.0 | 164,160,961.0 | 111,510.0 |
| `logparse-atomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 316,824,599.0 | 314,742,678.0 | 320,805,700.0 | 2,144,910.4 | 5 | 83,024 | 63,563 | 43,630 | 0.007 (max is trial 1) | compiled=5 | 2,703,634.0 | 313,899,064.0 | 221,901.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,585,933.0 | 312,902,408.0 | 320,630,098.0 | 2,936,477.8 | 5 | 82,984 | 63,490 | 43,557 | 0.009 | compiled=5 | 2,686,644.0 | 316,769,058.0 | 130,231.0 |
| `logparse-atomic` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 314,981,213.0 | 308,365,967.0 | 339,843,815.0 | 11,192,591.4 | 5 | 83,024 | 63,563 | 43,630 | 0.036 | compiled=5 | 2,682,125.0 | 311,495,154.0 | 226,491.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 317,358,587.0 | 314,372,910.0 | 328,712,566.0 | 5,267,004.2 | 5 | 82,984 | 63,490 | 43,557 | 0.017 | compiled=5 | 2,784,505.0 | 314,335,099.0 | 227,751.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 314,151,105.0 | 306,248,263.0 | 319,478,292.0 | 5,091,018.5 | 5 | 83,024 | 63,282 | 43,349 | 0.016 (max is trial 1) | compiled=5 | 2,640,974.0 | 311,347,630.0 | 129,241.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,728,574.0 | 314,575,567.0 | 322,566,349.0 | 2,653,143.6 | 5 | 82,984 | 63,209 | 43,276 | 0.008 | compiled=5 | 2,694,314.0 | 316,910,999.0 | 121,910.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 313,747,798.0 | 300,369,825.0 | 315,135,385.0 | 5,541,948.4 | 5 | 83,024 | 63,282 | 43,349 | 0.018 | compiled=5 | 2,674,464.0 | 310,862,941.0 | 216,421.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 318,372,612.0 | 311,012,452.0 | 321,902,649.0 | 4,132,737.9 | 5 | 82,984 | 63,209 | 43,276 | 0.013 | compiled=5 | 2,654,214.0 | 315,180,324.0 | 226,791.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,861,807.0 | 147,480,596.0 | 154,937,280.0 | 2,590,803.2 | 5 | 27,792 | 19,636 | 14,433 | 0.017 | compiled=5 | 1,886,669.0 | 149,911,427.0 | 102,521.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,905,413.0 | 152,217,487.0 | 167,914,941.0 | 6,347,373.2 | 5 | 27,936 | 22,055 | 16,450 | 0.039 | compiled=5 | 1,980,399.0 | 159,936,974.0 | 194,641.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 152,922,813.0 | 136,652,296.0 | 156,917,714.0 | 8,098,585.2 | 5 | 27,792 | 19,636 | 14,433 | 0.053 | compiled=5 | 1,870,600.0 | 150,847,772.0 | 196,051.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 164,067,912.0 | 147,896,585.0 | 165,432,859.0 | 6,688,832.1 | 5 | 27,936 | 22,055 | 16,450 | 0.041 | compiled=5 | 1,894,300.0 | 162,077,151.0 | 105,570.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_02902356_auto-caps-simdna` | 287,310,097.0 | 282,527,124.0 | 291,975,619.0 | 3,234,697.7 | 5 | 31,688 | 31,521 | 31,290 | 0.011 | compiled=5 | 1,881,739.0 | 283,405,708.0 | 103,980.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 291,557,535.0 | 275,806,332.0 | 293,634,205.0 | 6,762,529.5 | 5 | 31,688 | 31,634 | 31,403 | 0.023 | compiled=5 | 1,918,699.0 | 289,668,927.0 | 111,690.0 |
| `nested-comment-rec` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 285,505,076.0 | 283,988,567.0 | 307,939,224.0 | 8,985,504.6 | 5 | 31,688 | 31,539 | 31,308 | 0.031 | compiled=5 | 1,811,959.0 | 283,204,455.0 | 198,821.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 291,836,210.0 | 288,488,613.0 | 299,822,882.0 | 3,896,353.1 | 5 | 31,688 | 31,652 | 31,421 | 0.013 | compiled=5 | 1,806,940.0 | 289,825,619.0 | 186,771.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 217,885,073.0 | 207,805,977.0 | 220,599,306.0 | 4,415,192.0 | 5 | 31,752 | 28,488 | 26,806 | 0.020 | compiled=5 | 1,797,289.0 | 216,014,035.0 | 191,421.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 217,457,921.0 | 210,867,200.0 | 218,995,039.0 | 2,883,203.4 | 5 | 31,752 | 28,417 | 26,735 | 0.013 | compiled=5 | 1,778,848.0 | 215,469,212.0 | 206,521.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 219,407,065.0 | 212,330,237.0 | 227,991,901.0 | 6,177,239.3 | 5 | 31,752 | 28,488 | 26,806 | 0.028 | compiled=5 | 1,767,339.0 | 217,429,285.0 | 190,121.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 216,648,180.0 | 215,681,735.0 | 220,044,949.0 | 1,582,292.7 | 5 | 31,752 | 28,417 | 26,735 | 0.007 | compiled=5 | 1,771,839.0 | 214,722,780.0 | 191,391.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 225,125,868.0 | 217,514,821.0 | 230,756,862.0 | 4,460,607.6 | 5 | 31,832 | 29,716 | 27,774 | 0.020 | compiled=5 | 1,831,488.0 | 221,687,611.0 | 192,331.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 222,629,486.0 | 215,127,080.0 | 228,743,694.0 | 4,951,425.5 | 5 | 31,792 | 29,644 | 27,702 | 0.022 | compiled=5 | 1,824,198.0 | 220,193,374.0 | 187,581.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 231,449,959.0 | 216,667,200.0 | 242,546,438.0 | 9,456,502.1 | 5 | 31,832 | 29,716 | 27,774 | 0.041 | compiled=5 | 1,821,249.0 | 229,535,300.0 | 191,011.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 228,865,765.0 | 218,512,330.0 | 230,320,853.0 | 4,312,127.4 | 5 | 31,792 | 29,644 | 27,702 | 0.019 | compiled=5 | 1,838,280.0 | 226,817,504.0 | 193,661.0 |
| `phone-palindrome-6` | `plain` | `pcrec_02902356_auto-caps-simdna` | 292,820,412.0 | 286,676,783.0 | 293,029,143.0 | 2,642,137.5 | 5 | 27,344 | 23,271 | 23,271 | 0.009 | compiled=5 | 1,772,489.0 | 291,041,523.0 | 102,150.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,440,195.0 | 189,423,051.0 | 197,308,879.0 | 3,154,488.2 | 5 | 27,424 | 23,079 | 23,079 | 0.016 | compiled=5 | 1,635,797.0 | 191,035,019.0 | 108,211.0 |
| `phone-palindrome-6` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 290,728,915.0 | 284,765,983.0 | 291,966,461.0 | 2,545,848.6 | 5 | 27,344 | 23,271 | 23,271 | 0.009 | compiled=5 | 1,645,819.0 | 288,983,655.0 | 190,431.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 197,107,537.0 | 189,049,735.0 | 213,006,561.0 | 7,921,832.1 | 5 | 27,424 | 23,079 | 23,079 | 0.040 (max is trial 1) | compiled=5 | 1,657,689.0 | 195,349,478.0 | 100,320.0 |
| `pwd-strength-chain` | `plain` | `pcrec_02902356_auto-caps-simdna` | 252,513,566.0 | 246,928,378.0 | 258,536,103.0 | 3,812,285.6 | 5 | 31,984 | 32,820 | 30,179 | 0.015 | compiled=5 | 1,920,739.0 | 250,441,875.0 | 191,851.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 242,853,379.0 | 235,803,237.0 | 256,657,053.0 | 7,366,398.6 | 5 | 31,984 | 32,748 | 30,107 | 0.030 | compiled=5 | 1,857,339.0 | 240,807,110.0 | 190,301.0 |
| `pwd-strength-chain` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 244,230,687.0 | 238,717,578.0 | 251,485,515.0 | 4,062,165.3 | 5 | 31,984 | 32,820 | 30,179 | 0.017 | compiled=5 | 1,875,880.0 | 242,148,217.0 | 121,321.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 250,929,693.0 | 243,172,322.0 | 254,907,463.0 | 4,618,000.4 | 5 | 31,984 | 32,748 | 30,107 | 0.018 | compiled=5 | 1,876,130.0 | 248,959,492.0 | 99,181.0 |
| `quoted-delim-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 218,731,857.0 | 204,654,862.0 | 221,932,213.0 | 6,360,569.8 | 5 | 31,768 | 26,057 | 25,364 | 0.029 | compiled=5 | 1,712,258.0 | 216,928,989.0 | 104,370.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 212,245,628.0 | 203,503,576.0 | 218,781,397.0 | 5,618,585.4 | 5 | 31,768 | 26,170 | 25,477 | 0.026 | compiled=5 | 1,684,268.0 | 210,604,730.0 | 105,360.0 |
| `quoted-delim-match` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 216,090,747.0 | 210,359,898.0 | 220,233,700.0 | 3,503,473.7 | 5 | 31,768 | 26,057 | 25,364 | 0.016 | compiled=5 | 1,704,149.0 | 214,271,798.0 | 185,731.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 217,562,315.0 | 211,385,893.0 | 218,501,382.0 | 3,300,873.7 | 5 | 31,768 | 26,170 | 25,477 | 0.015 | compiled=5 | 1,717,979.0 | 215,732,576.0 | 194,141.0 |
| `router-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 150,587,451.0 | 141,122,647.0 | 160,300,795.0 | 6,270,160.8 | 5 | 27,792 | 20,751 | 14,771 | 0.042 | compiled=5 | 1,982,569.0 | 148,723,912.0 | 102,691.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 160,820,168.0 | 153,542,685.0 | 161,812,563.0 | 3,307,435.2 | 5 | 27,936 | 23,579 | 16,972 | 0.021 (max is trial 1) | compiled=5 | 2,022,219.0 | 158,242,906.0 | 190,141.0 |
| `router-prefix-order` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 153,199,273.0 | 148,245,006.0 | 163,070,006.0 | 5,614,518.2 | 5 | 27,792 | 20,935 | 14,955 | 0.037 | compiled=5 | 1,946,270.0 | 148,966,281.0 | 200,341.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 167,420,420.0 | 166,253,042.0 | 169,346,169.0 | 1,022,483.9 | 5 | 27,936 | 23,691 | 17,084 | 0.006 | compiled=5 | 1,982,651.0 | 165,326,598.0 | 104,560.0 |
| `tag-depth3-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 288,433,500.0 | 277,958,793.0 | 291,477,567.0 | 4,794,577.6 | 5 | 31,816 | 33,543 | 33,027 | 0.017 | compiled=5 | 1,853,588.0 | 286,449,823.0 | 110,011.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 286,343,192.0 | 281,916,582.0 | 288,441,001.0 | 2,421,918.9 | 5 | 31,816 | 33,656 | 33,140 | 0.008 | compiled=5 | 1,849,879.0 | 284,287,512.0 | 105,571.0 |
| `tag-depth3-bound` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 286,599,172.0 | 281,860,478.0 | 287,633,988.0 | 2,429,689.0 | 5 | 31,816 | 33,317 | 32,855 | 0.008 | compiled=5 | 1,888,900.0 | 284,663,252.0 | 102,470.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 287,756,117.0 | 279,535,315.0 | 290,743,204.0 | 3,959,869.8 | 5 | 31,816 | 33,430 | 32,968 | 0.014 | compiled=5 | 1,913,990.0 | 285,612,536.0 | 113,990.0 |
| `tag-pair-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 235,483,335.0 | 226,488,733.0 | 242,345,747.0 | 5,563,115.7 | 5 | 31,776 | 27,351 | 26,142 | 0.024 | compiled=5 | 1,782,258.0 | 233,492,516.0 | 211,751.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 231,911,019.0 | 226,272,912.0 | 240,164,277.0 | 4,755,950.5 | 5 | 31,776 | 27,464 | 26,255 | 0.021 | compiled=5 | 1,793,698.0 | 229,548,938.0 | 194,851.0 |
| `tag-pair-match` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 233,107,608.0 | 223,684,447.0 | 234,405,675.0 | 3,996,671.5 | 5 | 31,776 | 27,125 | 25,970 | 0.017 | compiled=5 | 1,801,649.0 | 231,233,958.0 | 112,051.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 234,316,045.0 | 227,143,737.0 | 234,567,526.0 | 2,881,556.9 | 5 | 31,776 | 27,238 | 26,083 | 0.012 | compiled=5 | 1,800,120.0 | 232,283,913.0 | 103,871.0 |
| `trim-nested-star` | `plain` | `pcrec_02902356_auto-caps-simdna` | 205,170,163.0 | 194,203,813.0 | 205,709,646.0 | 4,936,153.9 | 5 | 27,512 | 23,591 | 23,360 | 0.024 | compiled=5 | 1,651,438.0 | 203,283,615.0 | 106,760.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,039,954.0 | 199,593,018.0 | 204,630,652.0 | 1,947,756.5 | 5 | 27,512 | 23,705 | 23,474 | 0.010 | compiled=5 | 1,651,167.0 | 201,290,756.0 | 104,570.0 |
| `trim-nested-star` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 200,055,003.0 | 197,279,819.0 | 205,548,891.0 | 3,024,984.1 | 5 | 27,512 | 23,591 | 23,360 | 0.015 | compiled=5 | 1,642,879.0 | 197,848,011.0 | 192,391.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 203,301,689.0 | 197,169,457.0 | 208,146,415.0 | 4,244,891.5 | 5 | 27,512 | 23,705 | 23,474 | 0.021 | compiled=5 | 1,638,729.0 | 201,448,520.0 | 107,180.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,589,682.0 | 186,516,878.0 | 193,034,517.0 | 2,111,820.7 | 5 | 31,816 | 28,015 | 23,213 | 0.011 | compiled=5 | 1,913,739.0 | 187,574,873.0 | 103,051.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 195,997,671.0 | 191,905,032.0 | 199,909,889.0 | 2,539,046.0 | 5 | 31,904 | 29,703 | 24,687 | 0.013 | compiled=5 | 1,907,719.0 | 194,006,163.0 | 102,530.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 187,215,284.0 | 181,629,115.0 | 193,220,256.0 | 4,326,349.4 | 5 | 31,816 | 28,015 | 23,213 | 0.023 | compiled=5 | 1,879,420.0 | 183,037,042.0 | 110,090.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 190,368,561.0 | 182,006,987.0 | 197,476,328.0 | 5,662,336.3 | 5 | 31,904 | 29,703 | 24,687 | 0.030 | compiled=5 | 1,907,231.0 | 188,217,989.0 | 109,110.0 |
| `uuid-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 177,306,022.0 | 170,009,575.0 | 178,885,161.0 | 3,620,951.4 | 5 | 37,072 | 23,602 | 18,198 | 0.020 | compiled=5 | 1,735,369.0 | 175,458,523.0 | 112,130.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 173,594,354.0 | 163,611,851.0 | 182,161,508.0 | 6,060,446.7 | 5 | 37,032 | 23,424 | 18,020 | 0.035 | compiled=5 | 1,762,910.0 | 171,354,672.0 | 206,041.0 |
| `uuid-near-miss` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 177,043,111.0 | 168,485,475.0 | 178,898,080.0 | 3,816,936.8 | 5 | 37,072 | 23,602 | 18,198 | 0.022 | compiled=5 | 1,731,779.0 | 175,195,950.0 | 106,941.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 174,846,928.0 | 170,355,065.0 | 179,389,683.0 | 3,500,990.3 | 5 | 37,032 | 23,424 | 18,020 | 0.020 | compiled=5 | 1,737,959.0 | 171,008,358.0 | 110,461.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,159,039.0 | 146,948,134.0 | 154,338,498.0 | 2,683,977.6 | 5 | 27,792 | 19,408 | 14,411 | 0.018 | compiled=5 | 1,830,278.0 | 145,323,646.0 | 196,051.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,117,822.0 | 148,165,720.0 | 162,967,238.0 | 5,042,822.8 | 5 | 27,936 | 21,863 | 16,540 | 0.033 | compiled=5 | 3,548,726.0 | 151,482,235.0 | 116,011.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 154,930,653.0 | 147,143,941.0 | 156,440,581.0 | 3,522,516.1 | 5 | 27,792 | 19,408 | 14,411 | 0.023 | compiled=5 | 1,805,000.0 | 153,025,883.0 | 106,160.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 155,654,437.0 | 153,226,734.0 | 168,211,124.0 | 6,164,597.4 | 5 | 27,936 | 21,863 | 16,540 | 0.040 | compiled=5 | 1,831,819.0 | 152,687,011.0 | 192,791.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,325,668.0 | 150,784,142.0 | 157,123,131.0 | 2,229,834.1 | 5 | 28,112 | 28,359 | 16,094 | 0.015 (max is trial 1) | compiled=5 | 2,692,762.0 | 149,492,626.0 | 192,071.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,102,239.0 | 156,585,180.0 | 182,357,058.0 | 9,662,757.1 | 5 | 28,256 | 31,334 | 18,181 | 0.059 | compiled=5 | 2,778,193.0 | 160,616,687.0 | 100,730.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 148,514,669.0 | 147,035,830.0 | 173,034,859.0 | 11,164,467.4 | 5 | 28,112 | 28,359 | 16,094 | 0.075 | compiled=5 | 2,313,202.0 | 146,000,376.0 | 193,781.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 170,780,117.0 | 162,428,174.0 | 172,844,837.0 | 4,714,459.1 | 5 | 28,256 | 31,334 | 18,181 | 0.028 | compiled=5 | 2,418,633.0 | 168,275,244.0 | 100,090.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,291,179.0 | 144,234,151.0 | 156,807,730.0 | 4,158,631.4 | 5 | 27,784 | 23,172 | 14,850 | 0.028 | compiled=5 | 2,093,600.0 | 145,179,765.0 | 201,841.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,864,495.0 | 154,640,848.0 | 172,180,451.0 | 6,530,659.9 | 5 | 27,928 | 26,523 | 16,764 | 0.042 | compiled=5 | 2,319,021.0 | 153,340,953.0 | 193,821.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 149,422,883.0 | 144,104,096.0 | 156,290,931.0 | 5,164,812.9 | 5 | 27,784 | 23,172 | 14,850 | 0.035 | compiled=5 | 2,101,952.0 | 144,838,859.0 | 188,141.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 165,864,360.0 | 150,828,380.0 | 166,452,994.0 | 6,807,701.1 | 5 | 27,928 | 26,523 | 16,764 | 0.041 | compiled=5 | 2,216,262.0 | 163,541,109.0 | 173,311.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 149,682,477.0 | 143,503,517.0 | 158,570,648.0 | 5,971,834.3 | 5 | 27,792 | 19,410 | 14,413 | 0.040 | compiled=5 | 1,761,198.0 | 145,874,429.0 | 103,331.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,850,874.0 | 146,484,851.0 | 165,597,341.0 | 7,429,494.0 | 5 | 27,936 | 21,865 | 16,542 | 0.048 | compiled=5 | 1,830,449.0 | 153,621,964.0 | 207,861.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 155,371,226.0 | 150,307,069.0 | 157,244,624.0 | 2,801,339.7 | 5 | 27,792 | 19,410 | 14,413 | 0.018 | compiled=5 | 1,822,750.0 | 153,481,505.0 | 110,000.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 161,644,628.0 | 151,419,054.0 | 166,975,086.0 | 5,596,765.7 | 5 | 27,936 | 21,865 | 16,542 | 0.035 | compiled=5 | 1,829,339.0 | 159,608,258.0 | 207,331.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_02902356_auto-caps-simdna` | 154,503,939.0 | 137,125,829.0 | 157,145,741.0 | 7,847,919.6 | 5 | 27,792 | 20,788 | 14,693 | 0.051 | compiled=5 | 1,959,849.0 | 150,304,429.0 | 205,081.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,620,620.0 | 161,107,759.0 | 166,187,664.0 | 1,665,031.3 | 5 | 27,936 | 23,542 | 16,824 | 0.010 | compiled=5 | 1,997,599.0 | 161,517,271.0 | 190,871.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 155,382,835.0 | 145,182,660.0 | 157,617,317.0 | 4,580,736.4 | 5 | 27,792 | 20,788 | 14,693 | 0.029 | compiled=5 | 1,986,941.0 | 153,239,164.0 | 103,880.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 163,048,076.0 | 160,247,703.0 | 167,643,031.0 | 2,568,760.3 | 5 | 27,936 | 23,542 | 16,824 | 0.016 | compiled=5 | 2,003,001.0 | 160,935,914.0 | 102,871.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 576,388,570.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,247,714,708.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 579,952,650.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,303,690,461.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,338,075.0 | 361,869,673.0 | 370,076,501.0 | 3,261,612.4 | 5 | 45,832 | 55,446 | 45,523 | 0.009 (max is trial 1) | compiled=5 | 2,342,761.0 | 359,831,154.0 | 117,050.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 350,317,570.0 | 334,239,615.0 | 351,187,503.0 | 6,503,231.7 | 5 | 45,464 | 53,885 | 43,962 | 0.019 | compiled=5 | 2,430,571.0 | 347,837,418.0 | 199,971.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 362,034,901.0 | 354,016,009.0 | 367,100,569.0 | 4,388,463.7 | 5 | 45,832 | 55,446 | 45,523 | 0.012 | compiled=5 | 2,401,682.0 | 359,550,069.0 | 108,800.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 349,838,208.0 | 345,187,532.0 | 365,857,833.0 | 7,579,427.5 | 5 | 45,464 | 53,885 | 43,962 | 0.022 | compiled=5 | 2,423,783.0 | 347,272,184.0 | 194,481.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 237,290,446.0 | 231,316,804.0 | 245,960,600.0 | 5,714,327.3 | 5 | 31,976 | 33,908 | 28,398 | 0.024 | compiled=5 | 2,090,641.0 | 232,811,032.0 | 192,921.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 246,142,221.0 | 233,371,684.0 | 252,066,191.0 | 7,422,745.9 | 5 | 32,072 | 34,980 | 29,045 | 0.030 (max is trial 1) | compiled=5 | 2,104,261.0 | 241,590,197.0 | 194,071.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 243,215,362.0 | 236,374,526.0 | 244,034,657.0 | 2,811,122.8 | 5 | 31,976 | 33,908 | 28,398 | 0.012 | compiled=5 | 2,190,202.0 | 240,863,399.0 | 102,891.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 244,253,148.0 | 237,800,034.0 | 246,382,748.0 | 2,957,457.7 | 5 | 32,072 | 34,980 | 29,045 | 0.012 | compiled=5 | 2,108,051.0 | 242,030,615.0 | 108,751.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,151,498.0 | 231,093,062.0 | 236,998,853.0 | 2,064,415.7 | 5 | 31,976 | 33,629 | 28,119 | 0.009 | compiled=5 | 2,043,771.0 | 229,879,126.0 | 109,001.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 240,890,644.0 | 231,783,847.0 | 245,950,040.0 | 4,830,727.1 | 5 | 32,072 | 34,698 | 28,763 | 0.020 | compiled=5 | 2,104,761.0 | 238,206,500.0 | 108,841.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 236,134,664.0 | 231,267,647.0 | 239,036,320.0 | 3,424,552.4 | 5 | 31,976 | 33,629 | 28,119 | 0.015 | compiled=5 | 2,057,761.0 | 231,106,867.0 | 200,741.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 238,519,027.0 | 227,429,258.0 | 239,080,290.0 | 4,405,215.8 | 5 | 32,072 | 34,698 | 28,763 | 0.018 | compiled=5 | 2,101,132.0 | 235,981,523.0 | 122,051.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 410,361,126.0 | 389,258,935.0 | 412,174,335.0 | 8,476,483.0 | 5 | 40,680 | 61,633 | 41,904 | 0.021 | compiled=5 | 5,137,327.0 | 400,032,002.0 | 193,601.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 414,227,586.0 | 403,260,857.0 | 415,743,663.0 | 4,791,466.9 | 5 | 40,776 | 66,276 | 43,404 | 0.012 | compiled=5 | 8,259,983.0 | 405,708,401.0 | 193,411.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 406,967,961.0 | 393,426,269.0 | 418,341,652.0 | 9,119,146.9 | 5 | 40,680 | 61,633 | 41,904 | 0.022 (max is trial 1) | compiled=5 | 5,172,958.0 | 401,729,873.0 | 196,391.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 416,576,933.0 | 413,564,586.0 | 427,724,502.0 | 4,925,976.0 | 5 | 40,776 | 66,276 | 43,404 | 0.012 | compiled=5 | 8,217,484.0 | 407,267,523.0 | 192,601.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,494,897.0 | 354,488,595.0 | 364,639,699.0 | 3,632,735.8 | 5 | 40,680 | 59,185 | 39,456 | 0.010 | compiled=5 | 4,989,566.0 | 356,707,876.0 | 193,201.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 375,793,157.0 | 365,474,932.0 | 386,638,593.0 | 7,675,001.2 | 5 | 40,776 | 63,828 | 40,956 | 0.020 | compiled=5 | 18,567,707.0 | 357,489,900.0 | 195,751.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 368,605,708.0 | 354,403,212.0 | 370,169,907.0 | 7,068,452.4 | 5 | 40,680 | 59,185 | 39,456 | 0.019 | compiled=5 | 11,298,050.0 | 357,121,507.0 | 204,981.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 374,999,562.0 | 365,989,063.0 | 384,106,051.0 | 5,758,909.1 | 5 | 40,776 | 63,828 | 40,956 | 0.015 | compiled=5 | 7,879,641.0 | 366,905,839.0 | 194,721.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_02902356_auto-caps-simdna` | 5,446,416,952.0 | 5,427,347,513.0 | 5,490,679,283.0 | 22,705,595.8 | 5 | 176,208 | 518,007 (warned) | 300,042 | 0.004 | compiled=5 | 599,367,599.0 | 4,848,712,922.0 | 104,491.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 6,440,923,029.0 | 6,428,778,045.0 | 6,483,773,802.0 | 23,122,738.7 | 5 | 180,400 | 527,624 (warned) | 301,462 | 0.004 | compiled=5 | 1,597,453,843.0 | 4,841,745,826.0 | 102,270.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 5,432,962,683.0 | 5,414,669,006.0 | 5,452,919,310.0 | 12,808,009.3 | 5 | 176,208 | 518,007 (warned) | 300,042 | 0.002 | compiled=5 | 597,397,113.0 | 4,829,192,608.0 | 102,301.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 6,441,478,499.0 | 6,413,074,889.0 | 6,476,675,006.0 | 23,318,027.3 | 5 | 180,400 | 527,624 (warned) | 301,462 | 0.004 | compiled=5 | 1,607,461,887.0 | 4,833,915,602.0 | 101,200.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 243,714,108.0 | 237,783,439.0 | 249,010,057.0 | 4,185,869.1 | 5 | 32,192 | 37,329 | 28,845 | 0.017 (max is trial 1) | compiled=5 | 2,326,392.0 | 241,362,536.0 | 103,890.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 251,426,368.0 | 246,983,875.0 | 261,178,300.0 | 5,232,178.0 | 5 | 32,328 | 40,673 | 30,370 | 0.021 | compiled=5 | 2,284,812.0 | 248,930,105.0 | 199,591.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 239,212,611.0 | 236,650,758.0 | 244,233,846.0 | 3,270,535.0 | 5 | 32,192 | 37,329 | 28,845 | 0.014 | compiled=5 | 2,176,132.0 | 234,443,395.0 | 198,131.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 255,313,315.0 | 252,530,541.0 | 259,082,137.0 | 2,249,398.6 | 5 | 32,328 | 40,673 | 30,370 | 0.009 | compiled=5 | 2,311,733.0 | 252,878,573.0 | 112,050.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_02902356_auto-caps-simdna` | 245,666,419.0 | 241,410,265.0 | 253,353,299.0 | 4,606,066.9 | 5 | 36,256 | 47,651 | 30,746 | 0.019 | compiled=5 | 3,191,957.0 | 242,187,321.0 | 187,331.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 258,180,164.0 | 245,346,406.0 | 260,020,843.0 | 5,863,146.8 | 5 | 36,352 | 50,184 | 32,283 | 0.023 | compiled=5 | 3,304,887.0 | 254,810,406.0 | 188,071.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 251,607,506.0 | 245,133,482.0 | 263,093,369.0 | 5,890,131.8 | 5 | 36,256 | 47,651 | 30,746 | 0.023 | compiled=5 | 3,169,797.0 | 248,391,289.0 | 187,811.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 259,727,920.0 | 252,525,511.0 | 274,340,987.0 | 7,129,327.0 | 5 | 36,352 | 50,184 | 32,283 | 0.027 (max is trial 1) | compiled=5 | 3,313,688.0 | 256,315,671.0 | 116,611.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 392,491,672.0 | 384,915,983.0 | 398,643,295.0 | 4,999,999.4 | 5 | 44,320 | 57,974 | 27,864 | 0.013 | compiled=5 | 4,485,413.0 | 387,920,869.0 | 103,981.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 399,138,288.0 | 391,772,370.0 | 407,136,649.0 | 5,635,371.5 | 5 | 40,320 | 61,344 | 29,401 | 0.014 | compiled=5 | 4,615,554.0 | 394,447,313.0 | 106,991.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 405,319,354.0 | 398,751,268.0 | 405,722,575.0 | 2,844,193.9 | 5 | 44,320 | 58,463 | 28,353 | 0.007 | compiled=5 | 4,428,114.0 | 396,372,925.0 | 115,371.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 409,714,855.0 | 401,057,180.0 | 409,998,798.0 | 4,020,300.9 | 5 | 40,320 | 61,833 | 29,890 | 0.010 | compiled=5 | 4,511,844.0 | 404,965,880.0 | 101,550.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_02902356_auto-caps-simdna` | 283,575,716.0 | 276,111,877.0 | 295,733,599.0 | 6,886,383.7 | 5 | 52,544 | 105,110 | 33,760 | 0.024 | compiled=5 | 7,559,209.0 | 268,870,880.0 | 126,821.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 295,760,879.0 | 293,203,976.0 | 302,838,666.0 | 3,229,025.8 | 5 | 52,632 | 112,465 | 35,304 | 0.011 (max is trial 1) | compiled=5 | 8,017,302.0 | 287,496,876.0 | 177,341.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 280,529,759.0 | 275,924,026.0 | 287,237,906.0 | 3,623,653.7 | 5 | 52,544 | 105,612 | 34,262 | 0.013 | compiled=5 | 7,471,399.0 | 272,832,199.0 | 104,231.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 299,508,031.0 | 291,977,721.0 | 309,762,466.0 | 5,766,804.2 | 5 | 52,632 | 112,967 | 35,806 | 0.019 | compiled=5 | 7,926,992.0 | 290,652,574.0 | 191,991.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_02902356_auto-caps-simdna` | 562,562,478.0 | 561,219,771.0 | 594,114,281.0 | 12,774,766.0 | 5 | 208,656 | 553,671 (warned) | 44,404 | 0.023 | compiled=5 | 57,414,179.0 | 505,252,319.0 | 100,781.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 584,255,100.0 | 578,788,762.0 | 587,614,919.0 | 3,458,060.0 | 5 | 212,840 | 568,461 (warned) | 45,692 | 0.006 | compiled=5 | 64,427,765.0 | 519,153,422.0 | 100,701.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 569,294,811.0 | 558,386,886.0 | 572,826,663.0 | 5,473,208.7 | 5 | 208,656 | 553,671 (warned) | 44,404 | 0.010 (max is trial 1) | compiled=5 | 57,281,404.0 | 505,459,004.0 | 97,370.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 584,560,685.0 | 578,629,293.0 | 601,860,567.0 | 8,657,904.7 | 5 | 212,840 | 568,461 (warned) | 45,692 | 0.015 | compiled=5 | 64,259,762.0 | 516,191,961.0 | 202,531.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,340,903.0 | 145,899,509.0 | 162,439,555.0 | 5,968,137.6 | 5 | 27,792 | 21,325 | 15,618 | 0.039 | compiled=5 | 2,010,979.0 | 149,233,544.0 | 193,391.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 167,827,129.0 | 164,869,317.0 | 169,465,149.0 | 1,605,057.6 | 5 | 27,936 | 23,569 | 16,962 | 0.010 | compiled=5 | 1,989,980.0 | 165,754,860.0 | 104,680.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 157,638,438.0 | 155,144,004.0 | 164,998,257.0 | 3,592,649.1 | 5 | 27,792 | 21,514 | 15,807 | 0.023 | compiled=5 | 1,918,850.0 | 154,376,140.0 | 200,571.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 172,126,694.0 | 162,853,524.0 | 176,331,426.0 | 5,436,465.5 | 5 | 27,936 | 23,686 | 17,079 | 0.032 | compiled=5 | 1,954,040.0 | 169,977,272.0 | 199,351.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 173,031,084.0 | 163,323,360.0 | 174,495,752.0 | 4,072,581.7 | 5 | 27,936 | 23,175 | 17,394 | 0.024 | compiled=5 | 1,886,598.0 | 171,041,485.0 | 112,610.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,294,120.0 | 158,513,327.0 | 168,208,792.0 | 3,885,366.0 | 5 | 27,936 | 22,747 | 16,966 | 0.024 | compiled=5 | 1,919,719.0 | 158,960,809.0 | 198,811.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 172,240,223.0 | 170,001,084.0 | 177,358,283.0 | 2,766,367.0 | 5 | 27,936 | 23,718 | 17,937 | 0.016 | compiled=5 | 1,892,240.0 | 170,418,145.0 | 101,131.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 173,419,361.0 | 159,329,437.0 | 173,928,954.0 | 6,272,051.8 | 5 | 27,936 | 23,290 | 17,509 | 0.036 | compiled=5 | 1,913,021.0 | 169,288,049.0 | 109,901.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,019,948.0 | 212,639,978.0 | 235,379,945.0 | 7,305,895.4 | 5 | 31,968 | 31,978 | 27,144 | 0.033 (max is trial 1) | compiled=5 | 1,965,579.0 | 220,842,927.0 | 115,001.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 226,549,874.0 | 219,254,800.0 | 234,221,279.0 | 4,742,685.9 | 5 | 32,064 | 33,457 | 28,393 | 0.021 (max is trial 1) | compiled=5 | 1,975,149.0 | 224,481,324.0 | 103,061.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 220,023,228.0 | 217,982,907.0 | 227,411,647.0 | 3,343,508.5 | 5 | 31,968 | 31,978 | 27,144 | 0.015 | compiled=5 | 3,922,870.0 | 215,763,886.0 | 104,341.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 227,039,004.0 | 220,328,310.0 | 227,534,468.0 | 2,855,106.7 | 5 | 32,064 | 33,457 | 28,393 | 0.013 | compiled=5 | 1,995,651.0 | 223,525,577.0 | 102,930.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 147,010,445.0 | 141,100,084.0 | 147,544,529.0 | 2,423,674.6 | 5 | 27,616 | 15,572 | 13,215 | 0.016 | compiled=5 | 1,646,539.0 | 143,670,578.0 | 192,061.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 144,960,004.0 | 140,811,513.0 | 148,829,875.0 | 2,763,951.6 | 5 | 27,616 | 15,395 | 13,038 | 0.019 | compiled=5 | 1,627,789.0 | 142,254,310.0 | 199,671.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 149,280,663.0 | 130,360,361.0 | 149,392,263.0 | 7,361,316.3 | 5 | 27,616 | 15,572 | 13,215 | 0.049 | compiled=5 | 1,639,598.0 | 147,533,974.0 | 101,841.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 137,537,290.0 | 137,345,950.0 | 142,443,576.0 | 2,439,131.1 | 5 | 27,616 | 15,395 | 13,038 | 0.018 | compiled=5 | 1,616,039.0 | 135,722,521.0 | 101,820.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 319,124,980.0 | 306,564,465.0 | 320,182,985.0 | 5,061,663.7 | 5 | 40,960 | 45,787 | 40,759 | 0.016 | compiled=5 | 2,161,951.0 | 316,850,578.0 | 114,100.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 309,255,209.0 | 307,068,898.0 | 315,302,491.0 | 3,400,535.3 | 5 | 40,752 | 44,970 | 39,942 | 0.011 | compiled=5 | 2,177,061.0 | 304,925,337.0 | 196,301.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 319,147,435.0 | 310,530,409.0 | 319,405,447.0 | 3,462,451.7 | 5 | 40,960 | 45,787 | 40,759 | 0.011 | compiled=5 | 2,134,212.0 | 316,915,623.0 | 102,330.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 314,280,848.0 | 311,323,153.0 | 315,258,425.0 | 1,331,628.9 | 5 | 40,752 | 44,970 | 39,942 | 0.004 | compiled=5 | 2,128,401.0 | 312,036,797.0 | 192,751.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 209,529,840.0 | 207,844,643.0 | 216,443,617.0 | 2,996,674.5 | 5 | 32,064 | 28,091 | 25,547 | 0.014 | compiled=5 | 1,846,170.0 | 207,646,571.0 | 112,190.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,430,178.0 | 198,829,524.0 | 211,917,983.0 | 4,981,310.1 | 5 | 31,984 | 27,831 | 25,287 | 0.024 | compiled=5 | 3,627,409.0 | 199,592,999.0 | 111,661.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 209,245,791.0 | 201,782,012.0 | 210,347,388.0 | 3,167,971.7 | 5 | 32,064 | 28,091 | 25,547 | 0.015 | compiled=5 | 1,789,679.0 | 207,351,542.0 | 101,601.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 206,842,168.0 | 196,628,774.0 | 218,363,640.0 | 7,555,283.3 | 5 | 31,984 | 27,831 | 25,287 | 0.037 | compiled=5 | 1,802,540.0 | 204,968,479.0 | 185,971.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 248,667,125.0 | 247,389,987.0 | 249,350,336.0 | 713,337.6 | 5 | 36,560 | 47,570 | 22,252 | 0.003 (max is trial 1) | compiled=5 | 3,139,197.0 | 244,844,735.0 | 114,061.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 254,578,446.0 | 237,743,136.0 | 260,078,933.0 | 8,557,911.3 | 5 | 36,704 | 50,547 | 23,956 | 0.034 | compiled=5 | 3,530,438.0 | 251,130,047.0 | 105,861.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 249,226,194.0 | 236,949,547.0 | 255,143,456.0 | 6,710,957.8 | 5 | 36,560 | 47,701 | 22,383 | 0.027 | compiled=5 | 3,162,516.0 | 245,976,426.0 | 206,781.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 256,685,492.0 | 249,171,783.0 | 261,343,678.0 | 4,099,726.0 | 5 | 36,704 | 50,678 | 24,087 | 0.016 (max is trial 1) | compiled=5 | 3,229,367.0 | 253,233,654.0 | 208,241.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_02902356_auto-caps-simdna` | 229,191,262.0 | 223,914,035.0 | 232,111,759.0 | 2,803,121.6 | 5 | 85,736 | 227,567 | 19,601 | 0.012 (max is trial 1) | compiled=5 | 14,409,165.0 | 212,936,348.0 | 202,591.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 237,999,609.0 | 227,990,656.0 | 264,816,148.0 | 12,497,419.2 | 5 | 89,968 | 237,398 | 21,577 | 0.053 | compiled=5 | 15,698,432.0 | 219,954,604.0 | 114,691.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 225,576,668.0 | 221,054,873.0 | 229,058,617.0 | 3,076,708.1 | 5 | 85,736 | 227,567 | 19,601 | 0.014 | compiled=5 | 14,293,236.0 | 210,979,201.0 | 117,321.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 243,483,283.0 | 236,927,509.0 | 255,045,035.0 | 6,696,712.4 | 5 | 89,968 | 237,398 | 21,577 | 0.028 (max is trial 1) | compiled=5 | 15,665,463.0 | 226,262,852.0 | 109,681.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,777,328.0 | 179,414,043.0 | 205,820,181.0 | 10,879,652.8 | 5 | 36,480 | 57,983 | 17,583 | 0.057 | compiled=5 | 4,437,913.0 | 185,234,484.0 | 112,400.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 201,473,079.0 | 199,305,187.0 | 208,614,054.0 | 3,890,559.5 | 5 | 36,624 | 61,762 | 19,374 | 0.019 (max is trial 1) | compiled=5 | 5,971,871.0 | 196,218,491.0 | 190,701.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 188,888,594.0 | 182,361,518.0 | 197,006,346.0 | 5,327,205.7 | 5 | 36,480 | 57,983 | 17,583 | 0.028 | compiled=5 | 4,481,694.0 | 184,025,937.0 | 208,241.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 206,577,306.0 | 204,690,608.0 | 215,803,197.0 | 3,907,438.4 | 5 | 36,624 | 61,762 | 19,374 | 0.019 | compiled=5 | 5,080,927.0 | 201,483,620.0 | 114,321.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_02902356_auto-caps-simdna` | 163,497,120.0 | 153,596,240.0 | 175,232,262.0 | 7,735,900.2 | 5 | 32,152 | 36,533 | 15,366 | 0.047 | compiled=5 | 3,220,967.0 | 160,079,823.0 | 103,531.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 174,634,920.0 | 173,275,822.0 | 183,728,935.0 | 4,388,530.0 | 5 | 32,296 | 39,557 | 17,378 | 0.025 | compiled=5 | 3,343,477.0 | 170,707,648.0 | 101,411.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 170,507,426.0 | 162,431,383.0 | 176,455,928.0 | 4,632,423.5 | 5 | 32,152 | 36,533 | 15,366 | 0.027 (max is trial 1) | compiled=5 | 3,219,457.0 | 166,129,343.0 | 188,531.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 173,325,801.0 | 166,473,004.0 | 183,196,283.0 | 5,613,005.1 | 5 | 32,296 | 39,557 | 17,378 | 0.032 | compiled=5 | 3,358,078.0 | 169,779,802.0 | 104,530.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_02902356_auto-caps-simdna` | 1,458,152,128.0 | 1,429,600,059.0 | 1,482,915,127.0 | 19,768,038.2 | 5 | 680,448 | 394,628 (warned) | 100,148 | 0.014 | compiled=5 | 12,683,376.0 | 1,442,632,247.0 | 527,822.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 1,390,345,675.0 | 1,368,604,382.0 | 1,399,114,831.0 | 10,678,984.5 | 5 | 659,912 | 401,834 (warned) | 102,298 | 0.008 | compiled=5 | 13,089,838.0 | 1,377,098,256.0 | 284,651.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 1,446,000,491.0 | 1,434,471,289.0 | 1,475,477,056.0 | 14,599,793.3 | 5 | 680,448 | 394,628 (warned) | 100,148 | 0.010 | compiled=5 | 13,502,782.0 | 1,430,279,866.0 | 522,493.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 1,376,248,700.0 | 1,371,695,156.0 | 1,405,481,503.0 | 12,372,577.5 | 5 | 659,912 | 401,834 (warned) | 102,298 | 0.009 | compiled=5 | 12,945,219.0 | 1,360,496,575.0 | 285,711.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_02902356_auto-caps-simdna` | 158,663,416.0 | 155,513,879.0 | 160,131,514.0 | 1,680,890.4 | 5 | 27,792 | 21,230 | 15,318 | 0.011 | compiled=5 | 2,091,171.0 | 155,211,357.0 | 210,731.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 172,289,356.0 | 167,989,804.0 | 178,167,247.0 | 3,366,296.1 | 5 | 27,936 | 23,837 | 17,407 | 0.020 (max is trial 1) | compiled=5 | 2,120,791.0 | 169,968,264.0 | 172,811.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 159,776,208.0 | 151,388,784.0 | 166,162,123.0 | 5,216,003.7 | 5 | 27,792 | 21,248 | 15,336 | 0.033 | compiled=5 | 2,162,721.0 | 157,503,887.0 | 109,031.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 162,566,743.0 | 154,852,542.0 | 171,161,190.0 | 6,764,146.3 | 5 | 27,936 | 23,855 | 17,425 | 0.042 | compiled=5 | 2,055,881.0 | 160,427,682.0 | 111,361.0 |
| `winpath-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 135,167,833.0 | 134,530,291.0 | 148,679,943.0 | 6,699,706.4 | 5 | 27,576 | 14,961 | 12,878 | 0.050 | compiled=5 | 1,605,008.0 | 133,360,644.0 | 194,471.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 140,141,629.0 | 125,986,237.0 | 148,527,122.0 | 8,241,331.0 | 5 | 27,536 | 14,784 | 12,701 | 0.059 | compiled=5 | 1,630,418.0 | 138,396,580.0 | 104,720.0 |
| `winpath-near-miss` | `plain` | `pcrec_ce658cb7_auto-caps-simdna` | 135,157,517.0 | 127,047,724.0 | 152,034,916.0 | 8,730,094.8 | 5 | 27,576 | 14,961 | 12,878 | 0.065 | compiled=5 | 1,633,048.0 | 133,456,489.0 | 100,791.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_ce658cb7_auto-caps-simdna` | 141,227,630.0 | 131,771,990.0 | 147,031,910.0 | 6,018,457.4 | 5 | 27,536 | 14,784 | 12,701 | 0.043 | compiled=5 | 1,612,649.0 | 139,539,502.0 | 112,081.0 |

