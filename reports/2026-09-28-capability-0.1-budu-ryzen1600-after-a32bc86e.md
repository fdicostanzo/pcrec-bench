# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, machine=budu-ryzen1600, testee=pcrec_02902356_auto-caps-simdna, testee=pcrec_a32bc86e_auto-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 37.5% (`pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput`)
    - `capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z` (store/records/capability@0.1/pcrec_02902356_auto-caps-simdna/capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z.jsonl) — agreement: agree (0 of 124 groups; 2 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T050936Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna/capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T050936Z.jsonl) — agreement: agree (0 of 124 groups; 3 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
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
- identity: the records' own `engine_metadata.program_sha256` ([B88], schema v1.7) where BOTH compile rows of a cell carry it; otherwise OUR OWN census (`tools/program_identity.py`: both pins re-emitted with the pinned binaries under each config's recorded flags, `.c` + `.h` compared after dropping ONLY the generated-by line, the `.abi` integer and one-sided `#define` stamps). Which records carry the field, per side: `pcrec 02902356 -> a32bc86e`: the BEFORE (`02902356`) records carry `program_sha256` (124 of 124 compiled cell(s)), the AFTER (`a32bc86e`) records carry `program_sha256` (125 of 125 compiled cell(s)).

### `pcrec 02902356 -> a32bc86e` (capability@0.1)

- identity from the records ([B88], schema v1.7): 123 cell(s) read `engine_metadata.program_sha256` on BOTH compile rows, 0 fell back to the census; no census for this pair
- cells: 123 cross-pin set cell(s) measured on both sides; 99 program-identical (the null population)

| regime | baseline scale | n null cells | min Δ% | median Δ% | max Δ% | band (±) | status |
|---|---|---|---|---|---|---|---|
| `large-subject-throughput` | `>=1us` | 34 | -7.15% | -0.04% | +1.65% | ±7.15% | ok |
| `large-subject-throughput` | `100ns-1us` | 1 | +0.58% | +0.58% | +0.58% | n/a | insufficient (n=1 < 10) |
| `large-subject-throughput` | `<100ns` | 15 | -2.51% | +1.94% | +17.08% | ±17.08% | ok |
| `short-subject-search` | `>=1us` | 23 | -3.95% | +0.17% | +9.21% | ±9.21% | ok |
| `short-subject-search` | `100ns-1us` | 26 | -4.10% | +0.59% | +7.40% | ±7.40% | ok |
| `short-subject-search` | `<100ns` | 0 | - | - | - | n/a | empty (n=0) |

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

_D119 bar in this view: |Δ%| > max(IQR%, null band), the `D119 bar` column (definition, strata and bands in the null-control section above). This view's own threshold population: 123 cross-pin cell(s): 0 improve, 1 regress, 23 within the bar, 99 null-control (program identical -- the band's own population); 1 of the verdicts are IQR-only (their stratum's band is not usable)._

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,111,913.6 | 3.7144 | 5,106,258.7 | 5,121,759.8 | 5,418.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,121,812.8 | 3.7216 | 5,118,691.5 | 5,135,536.5 | 6,238.1 | 1.002x | 1.002x | unchanged (within spread) | +0.19% (null control: program identical) |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,899,201.4 | 3.7186 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,906,396.4 | 3.7254 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 970,648.5 | 3.7027 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 971,810.5 | 3.7072 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 242,843.5 | 3.7055 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 243,481.1 | 3.7152 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,906,396.4 ns, 1,048,576 B

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007.9 | 1,003.6 | 1,044.4 | 15.4 | 1.000x | 1.000x | - | - | 75 | 13.4 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,032.1 | 1,028.5 | 1,033.6 | 2.0 | 1.024x | 1.024x | unchanged (within spread) | +2.41% (null control: program identical) | 75 | 13.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `waf-concat`, 157.1 ns, 48 B

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x | faster ×1.02 | -2.00% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 0.0000 | 18.2 | 18.4 | 0.1 | 1.020x | 1.020x | - | - |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-64k`, 5.9 ns, 65,536 B; largest Δ: `t-1m`, -0.3 ns (now 5.9 ns), 1,048,576 B

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 526.0 | 515.3 | 531.4 | 5.5 | 1.000x | 1.000x | faster ×1.03 | -3.21% (null control: program identical) | 75 | 7.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 543.4 | 532.4 | 544.0 | 4.9 | 1.033x | 1.033x | - | - | 75 | 7.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 36.6 ns, 20 B; largest Δ: `rd-phone-list-hit`, -1.2 ns (now 10.1 ns), 7 B

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 0.0001 | 71.9 | 72.4 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 0.0001 | 71.8 | 75.6 | 1.4 | 1.002x | 1.002x | unchanged (within spread) | +0.19% (null control: program identical) |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 23.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 24.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0004 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 24.1 ns, 262,144 B

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,877.7 | 1,876.3 | 1,879.3 | 1.1 | 1.000x | 1.000x | unchanged (within spread) | -0.08% (null control: program identical) | 75 | 25.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,879.2 | 1,878.6 | 1,879.8 | 0.5 | 1.001x | 1.001x | - | - | 75 | 25.1 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `rec-array-define`, 85.1 ns, 11 B

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 612,600.4 | 0.4451 | 601,889.3 | 621,806.6 | 6,544.9 | 1.000x | 1.000x | unchanged (within spread) | -0.80% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 617,517.9 | 0.4487 | 602,272.9 | 641,063.0 | 14,129.0 | 1.008x | 1.008x | - | - |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 469,869.1 | 0.4481 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 480,003.4 | 0.4578 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 113,903.8 | 0.4345 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 111,522.2 | 0.4254 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,827.6 | 0.4399 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 27,987.3 | 0.4271 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 469,869.1 ns, 1,048,576 B

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 892.0 | 888.1 | 898.7 | 3.4 | 1.000x | 1.000x | - | - | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 897.9 | 890.9 | 899.2 | 3.1 | 1.007x | 1.007x | unchanged (within spread) | +0.67% (null control: program identical) | 75 | 12.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `cg-key-colon`, 42.0 ns, 7 B; largest Δ: `waf-dbnames`, +0.8 ns (now 12.1 ns), 39 B

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 607,496.7 | 0.4414 | 597,509.1 | 615,428.4 | 6,729.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 617,546.3 | 0.4487 | 605,351.4 | 625,596.8 | 7,436.8 | 1.017x | 1.017x | unchanged (within spread) | +1.65% (null control: program identical) |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 467,248.8 | 0.4456 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 478,271.8 | 0.4561 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 110,680.2 | 0.4222 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 111,988.5 | 0.4272 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 29,073.8 | 0.4436 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,085.6 | 0.4286 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 478,271.8 ns, 1,048,576 B

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 893.5 | 892.0 | 895.7 | 1.2 | 1.000x | 1.000x | - | - | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 896.9 | 890.7 | 900.0 | 3.2 | 1.004x | 1.004x | unchanged (within spread) | +0.38% (null control: program identical) | 75 | 12.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `cg-key-colon`, 42.1 ns, 7 B; largest Δ: `lp-quoted`, +0.8 ns (now 19.7 ns), 13 B

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 11,169,592.7 | 8.1159 | 11,167,219.2 | 11,253,022.2 | 32,781.6 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,250,842.7 | 8.1750 | 11,231,460.5 | 11,276,995.3 | 16,408.8 | 1.007x | 1.007x | slower ×1.01 | +0.73% (null control: program identical) |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8,509,284.2 | 8.1151 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 8,566,899.3 | 8.1700 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,126,560.1 | 8.1122 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,133,996.2 | 8.1405 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 534,760.1 | 8.1598 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 536,132.8 | 8.1807 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 8,566,899.3 ns, 1,048,576 B

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,149.2 | 5,134.2 | 5,160.8 | 9.9 | 1.000x | 1.000x | - | - | 75 | 68.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,151.2 | 5,149.9 | 5,154.3 | 1.6 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) | 75 | 68.7 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `lp-syslog`, 482.5 ns, 56 B; largest Δ: `dt-prose-month`, -7.2 ns (now 92.0 ns), 13 B

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.7 | 30.9 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 31.1 | 0.0000 | 31.1 | 31.2 | 0.0 | 1.009x | 1.009x | slower ×1.01 | +0.87% (null control: program identical) |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 10.4 ns, 65,536 B

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 839.6 | 837.6 | 840.2 | 1.1 | 1.000x | 1.000x | - | - | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 843.8 | 841.8 | 846.3 | 1.6 | 1.005x | 1.005x | slower ×1.01 | +0.51% (null control: program identical) | 75 | 11.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 61.5 ns, 20 B; largest Δ: `dt-iso8601`, -0.8 ns (now 22.3 ns), 20 B

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 25,397,237.5 | 18.4539 | 25,330,273.5 | 25,795,402.5 | 170,457.7 | 1.000x | 1.000x | unchanged (within spread) | -0.16% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 25,438,453.7 | 18.4838 | 25,264,260.2 | 26,138,014.4 | 308,079.6 | 1.002x | 1.002x | - | - |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 19,378,506.7 | 18.4808 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 19,380,938.1 | 18.4831 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,827,430.0 | 18.4152 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,837,275.2 | 18.4527 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,201,982.7 | 18.3408 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,203,012.2 | 18.3565 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 19,378,506.7 ns, 1,048,576 B; largest Δ: `t-256k`, -9,845.2 ns (now 4,827,430.0 ns), 262,144 B

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 20,793.3 | 20,780.9 | 21,108.7 | 126.7 | 1.000x | 1.000x | unchanged (within spread) | -0.68% (null control: program identical) | 75 | 277.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20,936.5 | 20,893.9 | 20,969.1 | 26.1 | 1.007x | 1.007x | - | - | 75 | 279.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-slack-webhook`, 1,323.4 ns, 81 B; largest Δ: `waf-benign`, -12.8 ns (now 668.0 ns), 39 B

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,127.3 | 0.0168 | 23,103.4 | 23,169.9 | 25.9 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,135.1 | 0.0168 | 23,117.6 | 23,139.9 | 9.4 | 1.000x | 1.000x | - | - |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,631.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,635.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,390.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,385.1 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.3 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 17,631.4 ns, 1,048,576 B; largest Δ: `t-256k`, +4.9 ns (now 4,390.0 ns), 262,144 B

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,174.7 | 1,170.4 | 1,177.6 | 2.8 | 1.000x | 1.000x | - | - | 75 | 15.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,188.3 | 1,169.7 | 1,195.7 | 11.2 | 1.012x | 1.012x | unchanged (within spread) | +1.15% (null control: program identical) | 75 | 15.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `waf-benign`, 416.1 ns, 39 B

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 977.5 | 0.0007 | 972.3 | 982.7 | 3.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,003.0 | 0.0007 | 996.6 | 1,006.8 | 3.3 | 1.026x | 1.026x | slower ×1.03 | +2.61% vs bar 0.29% (IQR-only) → **regress (IQR only: band n=1 < 10)** |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 229.9 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 233.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 456.8 | 0.0017 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 456.5 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 289.3 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 311.4 | 0.0048 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-256k`, 456.5 ns, 262,144 B; largest Δ: `t-64k`, +22.1 ns (now 311.4 ns), 65,536 B

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,517.7 | 10,475.0 | 10,575.5 | 32.7 | 1.000x | 1.000x | - | - | 75 | 140.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,623.1 | 10,614.6 | 10,631.4 | 5.7 | 1.010x | 1.010x | slower ×1.01 | +1.00% vs bar 9.21% (band) → **within** | 75 | 141.6 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 941.3 ns, 61 B; largest Δ: `sec-slack-webhook`, -20.3 ns (now 447.5 ns), 81 B

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 46.6 | 0.0000 | 45.6 | 47.9 | 0.8 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 0.0000 | 46.5 | 53.5 | 2.6 | 1.021x | 1.021x | unchanged (within spread) | +2.08% (null control: program identical) |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 15.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.0 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17.2 ns, 1,048,576 B

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,366.2 | 1,365.1 | 1,372.3 | 2.6 | 1.000x | 1.000x | unchanged (within spread) | -0.20% (null control: program identical) | 75 | 18.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,368.9 | 1,356.1 | 1,378.0 | 7.0 | 1.002x | 1.002x | - | - | 75 | 18.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 75.9 ns, 93 B; largest Δ: `la-email-nodup`, +1.7 ns (now 35.6 ns), 9 B

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,981.9 | 0.0087 | 11,650.2 | 12,069.5 | 180.6 | 1.000x | 1.000x | unchanged (within spread) | -0.93% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,094.3 | 0.0088 | 11,897.6 | 12,169.4 | 93.1 | 1.009x | 1.009x | - | - |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,164.3 | 0.0011 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,223.5 | 0.0012 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 45.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 45.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,761.4 | 0.1642 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,825.6 | 0.1652 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 10,761.4 ns, 65,536 B

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 255,493.9 | 0.1856 | 255,315.2 | 255,621.0 | 98.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 255,529.7 | 0.1857 | 255,321.6 | 255,783.2 | 169.9 | 1.000x | 1.000x | unchanged (within spread) | +0.01% (null control: program identical) |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 202,386.3 | 0.1930 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 202,381.0 | 0.1930 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 44,401.9 | 0.1694 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 44,439.5 | 0.1695 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8,685.4 | 0.1325 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 8,699.7 | 0.1327 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 202,381.0 ns, 1,048,576 B; largest Δ: `t-256k`, +37.6 ns (now 44,439.5 ns), 262,144 B

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.1 | 686.5 | 687.9 | 0.5 | 1.000x | 1.000x | - | - | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 687.5 | 687.2 | 687.6 | 0.2 | 1.000x | 1.000x | unchanged (within spread) | +0.05% (null control: program identical) | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sd-fileext-short`, 27.2 ns, 14 B; largest Δ: `waf-dbnames`, +0.1 ns (now 13.2 ns), 39 B

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,888,100.8 | 1.3719 | 1,884,218.3 | 1,910,982.0 | 10,074.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,906,684.5 | 1.3854 | 1,900,903.9 | 1,910,994.8 | 3,501.6 | 1.010x | 1.010x | unchanged (within spread) | +0.98% (null control: program identical) |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,446,031.4 | 1.3790 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,459,605.4 | 1.3920 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 356,011.0 | 1.3581 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 358,737.6 | 1.3685 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 86,264.5 | 1.3163 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 87,361.2 | 1.3330 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,459,605.4 ns, 1,048,576 B

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,638.9 | 1,630.8 | 1,652.6 | 8.2 | 1.000x | 1.000x | - | - | 75 | 21.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,641.8 | 1,639.1 | 1,658.6 | 7.8 | 1.002x | 1.002x | unchanged (within spread) | +0.17% (null control: program identical) | 75 | 21.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `v-ipv4`, 245.6 ns, 11 B

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,118.4 | 0.0168 | 23,102.6 | 23,133.7 | 10.8 | 1.000x | 1.000x | unchanged (within spread) | -0.03% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,126.4 | 0.0168 | 23,110.3 | 23,158.8 | 18.7 | 1.000x | 1.000x | - | - |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,636.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,640.7 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,375.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.4 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,106.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,104.2 | 0.0168 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 17,636.7 ns, 1,048,576 B; largest Δ: `t-256k`, -7.4 ns (now 4,375.0 ns), 262,144 B

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.0 | 662.5 | 667.1 | 1.8 | 1.000x | 1.000x | - | - | 75 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 668.9 | 667.3 | 670.7 | 1.2 | 1.003x | 1.003x | unchanged (within spread) | +0.29% (null control: program identical) | 75 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `floor-hit`, 17.0 ns, 1 B; largest Δ: `sd-empty-alt-hit`, -0.5 ns (now 9.3 ns), 61 B

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 482,995.3 | 0.3509 | 482,657.2 | 484,361.8 | 613.3 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 483,087.0 | 0.3510 | 482,752.7 | 483,416.5 | 210.9 | 1.000x | 1.000x | - | - |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 367,939.9 | 0.3509 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 368,071.8 | 0.3510 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 91,962.7 | 0.3508 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,954.1 | 0.3508 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 23,071.8 | 0.3520 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,066.0 | 0.3520 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 367,939.9 ns, 1,048,576 B

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,063.9 | 1,061.2 | 1,072.8 | 4.0 | 1.000x | 1.000x | - | - | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,116.4 | 1,109.7 | 1,118.4 | 3.1 | 1.049x | 1.049x | slower ×1.05 | +4.94% (null control: program identical) | 75 | 14.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 52.1 ns, 93 B; largest Δ: `lp-atomic-hit`, +6.9 ns (now 24.7 ns), 31 B

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 13.8 | 0.0000 | 13.7 | 13.9 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.9 | 0.3 | 1.103x | 1.103x | slower ×1.10 | +10.32% (null control: program identical) |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 5.1 ns, 262,144 B

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 406.3 | 404.5 | 407.9 | 1.2 | 1.000x | 1.000x | unchanged (within spread) | -1.40% (null control: program identical) | 75 | 5.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 412.1 | 405.6 | 422.5 | 5.6 | 1.014x | 1.014x | - | - | 75 | 5.5 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `v-ipv4`, 18.0 ns, 11 B

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 686,528.2 | 0.4988 | 682,695.3 | 691,094.9 | 3,183.0 | 1.000x | 1.000x | unchanged (within spread) | -0.17% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687,715.0 | 0.4997 | 685,324.2 | 688,495.4 | 1,111.0 | 1.002x | 1.002x | - | - |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 531,688.6 | 0.5071 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 531,816.0 | 0.5072 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 126,801.5 | 0.4837 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 126,911.4 | 0.4841 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,760.9 | 0.4389 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 28,894.0 | 0.4409 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 531,688.6 ns, 1,048,576 B; largest Δ: `t-64k`, -133.1 ns (now 28,760.9 ns), 65,536 B

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 766.0 | 764.1 | 769.5 | 2.3 | 1.000x | 1.000x | - | - | 75 | 10.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 771.8 | 770.1 | 774.1 | 1.4 | 1.008x | 1.008x | slower ×1.01 | +0.76% (null control: program identical) | 75 | 10.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `br-quoted-delim`, 20.7 ns, 15 B; largest Δ: `waf-benign`, +0.9 ns (now 10.3 ns), 39 B

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 31.0 | 0.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 33.0 | 0.0000 | 32.9 | 33.1 | 0.1 | 1.067x | 1.067x | slower ×1.07 | +6.74% vs bar 17.08% (band) → **within** |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11.5 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 11.5 ns, 65,536 B

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 807.7 | 807.4 | 819.8 | 4.8 | 1.000x | 1.000x | - | - | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 834.9 | 833.0 | 835.3 | 1.0 | 1.034x | 1.034x | slower ×1.03 | +3.37% vs bar 7.40% (band) → **within** | 75 | 11.1 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-atomic-hit`, 74.7 ns, 31 B

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 31.3 | 0.0000 | 31.2 | 31.5 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 34.2 | 0.0000 | 34.0 | 34.5 | 0.2 | 1.090x | 1.090x | slower ×1.09 | +9.02% vs bar 17.08% (band) → **within** |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.1 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 12.1 ns, 65,536 B

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 808.9 | 806.9 | 835.2 | 10.8 | 1.000x | 1.000x | - | - | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 862.8 | 862.7 | 879.6 | 6.7 | 1.067x | 1.067x | slower ×1.07 | +6.67% vs bar 7.40% (band) → **within** | 75 | 11.5 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-atomic-hit`, 76.6 ns, 31 B

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,106.6 | 0.0168 | 23,102.7 | 23,156.7 | 20.2 | 1.000x | 1.000x | faster ×1.00 | -0.26% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,167.0 | 0.0168 | 23,130.1 | 23,191.5 | 23.2 | 1.003x | 1.003x | - | - |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,624.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,382.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,391.4 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,105.6 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.0 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,624.4 ns, 1,048,576 B

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 686.2 | 685.8 | 687.0 | 0.4 | 1.000x | 1.000x | - | - | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 690.7 | 682.4 | 702.8 | 6.5 | 1.007x | 1.007x | unchanged (within spread) | +0.67% (null control: program identical) | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `nu-mojibake`, 36.3 ns, 7 B; largest Δ: `rd-phone-list-hit`, +0.6 ns (now 9.4 ns), 7 B

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,145.5 | 0.0168 | 23,119.7 | 23,148.1 | 11.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,153.1 | 0.0168 | 23,134.4 | 23,167.2 | 10.7 | 1.000x | 1.000x | unchanged (within spread) | +0.03% vs bar 7.15% (band) → **within** |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,651.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,660.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,375.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,385.9 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,107.8 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 17,660.2 ns, 1,048,576 B; largest Δ: `t-256k`, +10.2 ns (now 4,385.9 ns), 262,144 B

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,580.8 | 1,544.9 | 1,671.5 | 43.2 | 1.000x | 1.000x | unchanged (within spread) | -0.08% vs bar 9.21% (band) → **within** | 75 | 21.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,582.0 | 1,577.0 | 1,646.4 | 31.4 | 1.001x | 1.001x | - | - | 75 | 21.1 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `rec-comment-nested`, 642.7 ns, 34 B

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.5 | 28.8 | 0.1 | 1.000x | 1.000x | unchanged (within spread) | -1.33% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 28.9 | 0.0000 | 28.7 | 40.7 | 4.7 | 1.013x | 1.013x | - | - |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 9.6 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-64k`, 9.5 ns, 65,536 B; largest Δ: `t-1m`, -0.2 ns (now 9.5 ns), 1,048,576 B

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 813.5 | 798.8 | 823.5 | 8.4 | 1.000x | 1.000x | unchanged (within spread) | -0.25% (null control: program identical) | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 815.5 | 801.6 | 827.1 | 8.1 | 1.003x | 1.003x | - | - | 75 | 10.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 35.4 ns, 20 B; largest Δ: `lp-num-leadzero`, +1.1 ns (now 28.8 ns), 4 B

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 0.0000 | 29.8 | 30.1 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 31.1 | 0.1 | 1.029x | 1.029x | slower ×1.03 | +2.94% (null control: program identical) |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 10.3 ns, 1,048,576 B; largest Δ: `t-64k`, +0.3 ns (now 10.3 ns), 65,536 B

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 884.6 | 883.4 | 889.3 | 2.2 | 1.000x | 1.000x | unchanged (within spread) | -0.32% (null control: program identical) | 75 | 11.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 887.4 | 868.5 | 891.6 | 8.5 | 1.003x | 1.003x | - | - | 75 | 11.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-phone-list-hit`, 45.8 ns, 7 B; largest Δ: `br-palindrome`, -1.8 ns (now 34.7 ns), 6 B

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,527,078.6 | 4.7426 | 6,501,439.2 | 6,539,980.8 | 17,015.3 | 1.000x | 1.000x | unchanged (within spread) | -0.22% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,541,533.0 | 4.7531 | 6,504,044.4 | 6,547,064.1 | 19,609.1 | 1.002x | 1.002x | - | - |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 4,982,322.9 | 4.7515 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4,988,794.4 | 4.7577 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,235,356.8 | 4.7125 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,239,933.8 | 4.7300 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 309,420.2 | 4.7214 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 309,249.6 | 4.7188 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 4,982,322.9 ns, 1,048,576 B

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,701.4 | 6,662.5 | 6,721.3 | 22.1 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 89.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,705.9 | 6,535.9 | 6,895.6 | 150.4 | 1.001x | 1.001x | - | - | 75 | 89.4 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-slack-webhook`, 492.2 ns, 81 B; largest Δ: `lp-num-neg-dec`, +37.0 ns (now 90.5 ns), 7 B

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 223.0 | 0.0002 | 222.8 | 223.5 | 0.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 224.3 | 0.0002 | 223.7 | 229.2 | 2.0 | 1.006x | 1.006x | unchanged (within spread) | +0.58% (null control: program identical) |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 58.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 58.6 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 95.1 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 96.0 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 69.3 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 69.7 | 0.0011 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 96.0 ns, 262,144 B

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,097.4 | 12,078.0 | 12,184.1 | 36.8 | 1.000x | 1.000x | unchanged (within spread) | -0.46% (null control: program identical) | 75 | 161.3 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,153.6 | 12,102.8 | 12,179.4 | 31.6 | 1.005x | 1.005x | - | - | 75 | 162.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 921.1 ns, 93 B; largest Δ: `sec-slack-webhook`, +4.0 ns (now 884.8 ns), 81 B

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,034,269.2 | 7.2910 | 9,949,749.5 | 10,058,744.9 | 37,707.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,041,101.1 | 7.2960 | 9,962,633.3 | 10,087,934.7 | 45,487.3 | 1.001x | 1.001x | unchanged (within spread) | +0.07% (null control: program identical) |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 7,643,126.9 | 7.2891 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 7,663,257.1 | 7.3083 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,914,759.2 | 7.3042 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,902,527.8 | 7.2576 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 476,629.0 | 7.2728 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 473,280.3 | 7.2217 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 7,663,257.1 ns, 1,048,576 B

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,870.9 | 10,805.1 | 11,349.0 | 209.5 | 1.000x | 1.000x | - | - | 75 | 144.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,235.4 | 10,856.6 | 17,974.0 | 2,765.9 | 1.034x | 1.034x | unchanged (within spread) | +3.35% (null control: program identical) | 75 | 149.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 674.5 ns, 93 B

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 343,303.0 | 0.2494 | 343,087.4 | 343,319.9 | 87.1 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 343,378.8 | 0.2495 | 343,154.1 | 343,424.4 | 116.1 | 1.000x | 1.000x | - | - |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 264,023.3 | 0.2518 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 263,947.0 | 0.2517 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 64,468.0 | 0.2459 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 64,523.6 | 0.2461 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 14,755.1 | 0.2251 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 14,750.4 | 0.2251 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 264,023.3 ns, 1,048,576 B

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.4 | 687.2 | 687.9 | 0.2 | 1.000x | 1.000x | - | - | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 692.9 | 691.6 | 693.3 | 0.6 | 1.008x | 1.008x | slower ×1.01 | +0.81% (null control: program identical) | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-slack-webhook`, 35.9 ns, 81 B; largest Δ: `cg-string-escape`, +0.3 ns (now 5.3 ns), 2 B

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,136.4 | 0.0168 | 23,102.2 | 23,175.5 | 25.7 | 1.000x | 1.000x | unchanged (within spread) | -0.02% vs bar 7.15% (band) → **within** |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,140.0 | 0.0168 | 23,118.8 | 23,157.6 | 14.1 | 1.000x | 1.000x | - | - |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,639.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,650.6 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,375.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.9 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,639.9 ns, 1,048,576 B

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,160.8 | 1,155.8 | 1,163.9 | 2.9 | 1.000x | 1.000x | faster ×1.05 | -4.34% vs bar 9.21% (band) → **within** | 75 | 15.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,213.5 | 1,212.7 | 1,220.0 | 3.1 | 1.045x | 1.045x | - | - | 75 | 16.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `br-tag-mismatch`, 191.4 ns, 19 B; largest Δ: `rec-tag-depth3`, -23.7 ns (now 101.3 ns), 22 B

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,107.0 | 0.0168 | 23,100.5 | 23,138.2 | 14.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,133.0 | 0.0168 | 23,114.4 | 23,160.7 | 16.3 | 1.001x | 1.001x | unchanged (within spread) | +0.11% vs bar 7.15% (band) → **within** |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,620.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,628.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,388.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,107.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.4 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 17,628.3 ns, 1,048,576 B; largest Δ: `t-256k`, +9.9 ns (now 4,388.8 ns), 262,144 B

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,139.2 | 1,135.7 | 1,144.4 | 3.1 | 1.000x | 1.000x | - | - | 75 | 15.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,166.3 | 1,163.6 | 1,178.6 | 5.5 | 1.024x | 1.024x | slower ×1.02 | +2.38% vs bar 9.21% (band) → **within** | 75 | 15.6 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `br-tag-mismatch`, 173.3 ns, 19 B; largest Δ: `br-tag-pair`, -2.6 ns (now 72.9 ns), 18 B

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 47.2 | 0.0000 | 46.9 | 47.3 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 47.4 | 0.0000 | 47.2 | 47.7 | 0.2 | 1.005x | 1.005x | unchanged (within spread) | +0.53% (null control: program identical) |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 15.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-256k`, 15.9 ns, 262,144 B

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,184,333.1 | 10,180,682.9 | 10,194,056.2 | 4,531.4 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | - | - | 75 | 135,791.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,196,908.0 | 10,146,637.8 | 10,998,449.7 | 325,678.6 | 1.001x | 1.001x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | unchanged (within spread) | +0.12% (null control: program identical) | 75 | 135,958.8 | 8.9 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `rd-trim-near-miss`, 10,195,731.9 ns, 20 B

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 480,361.3 | 0.3490 | 478,893.9 | 481,452.9 | 903.3 | 1.000x | 1.000x | unchanged (within spread) | -0.22% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 481,402.0 | 0.3498 | 481,072.5 | 481,492.0 | 147.0 | 1.002x | 1.002x | - | - |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 366,655.7 | 0.3497 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 366,548.7 | 0.3496 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 91,113.4 | 0.3476 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,710.0 | 0.3498 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 22,548.3 | 0.3441 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,074.0 | 0.3521 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 366,655.7 ns, 1,048,576 B; largest Δ: `t-256k`, -596.5 ns (now 91,113.4 ns), 262,144 B

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,208.8 | 1,205.7 | 1,212.0 | 2.1 | 1.000x | 1.000x | - | - | 75 | 16.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,254.8 | 1,251.0 | 1,257.7 | 2.4 | 1.038x | 1.038x | slower ×1.04 | +3.81% (null control: program identical) | 75 | 16.7 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 55.5 ns, 93 B; largest Δ: `rd-evil-alt-near-miss`, +1.8 ns (now 16.2 ns), 18 B

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 0.0000 | 14.7 | 15.0 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.1 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.024x | 1.024x | slower ×1.02 | +2.40% (null control: program identical) |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-256k`, 5.1 ns, 262,144 B; largest Δ: `t-1m`, +0.1 ns (now 5.0 ns), 1,048,576 B

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 521.4 | 517.8 | 532.5 | 5.3 | 1.000x | 1.000x | - | - | 75 | 7.0 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 525.7 | 524.3 | 527.0 | 1.1 | 1.008x | 1.008x | unchanged (within spread) | +0.83% (null control: program identical) | 75 | 7.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 38.4 ns, 36 B

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 219,277.7 | 0.1593 | 219,044.1 | 219,614.5 | 200.1 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 219,310.8 | 0.1594 | 219,141.4 | 219,634.2 | 178.1 | 1.000x | 1.000x | - | - |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 168,628.8 | 0.1608 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 168,903.9 | 0.1611 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 40,435.4 | 0.1542 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 40,322.7 | 0.1538 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,163.6 | 0.1551 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,119.8 | 0.1544 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 168,628.8 ns, 1,048,576 B

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 679.7 | 677.6 | 680.9 | 1.2 | 1.000x | 1.000x | - | - | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 696.4 | 689.2 | 700.9 | 3.9 | 1.025x | 1.025x | slower ×1.02 | +2.45% (null control: program identical) | 75 | 9.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `lp-syslog`, 18.4 ns, 56 B; largest Δ: `sec-slack-webhook`, +0.6 ns (now 10.3 ns), 81 B

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,195,590.8 | 3.0486 | 4,193,420.8 | 4,198,404.0 | 1,855.4 | 1.000x | 1.000x | unchanged (within spread) | -0.05% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,197,626.6 | 3.0500 | 4,195,320.1 | 4,199,298.7 | 1,396.3 | 1.000x | 1.000x | - | - |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,198,047.5 | 3.0499 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,199,059.3 | 3.0509 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 800,127.7 | 3.0522 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 800,126.6 | 3.0522 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 197,951.0 | 3.0205 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 198,822.6 | 3.0338 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,198,047.5 ns, 1,048,576 B

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,408.2 | 2,406.0 | 2,412.5 | 2.7 | 1.000x | 1.000x | - | - | 75 | 32.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,499.3 | 2,496.6 | 2,501.7 | 1.7 | 1.038x | 1.038x | slower ×1.04 | +3.79% (null control: program identical) | 75 | 33.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 179.0 ns, 93 B; largest Δ: `rd-numeric-id-hit`, +6.0 ns (now 15.4 ns), 4 B

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,103,164.2 | 1.5282 | 2,096,855.3 | 2,119,227.7 | 8,658.3 | 1.000x | 1.000x | faster ×1.03 | -2.71% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,161,777.6 | 1.5708 | 2,157,756.8 | 2,164,971.7 | 2,408.9 | 1.028x | 1.028x | - | - |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,608,488.7 | 1.5340 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,657,528.3 | 1.5807 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 392,760.0 | 1.4983 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 402,144.7 | 1.5341 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 99,781.6 | 1.5225 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 102,167.9 | 1.5590 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,608,488.7 ns, 1,048,576 B

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,383.1 | 1,374.1 | 1,390.5 | 5.3 | 1.000x | 1.000x | - | - | 75 | 18.4 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,510.4 | 1,499.4 | 1,514.8 | 5.3 | 1.092x | 1.092x | slower ×1.09 | +9.21% (null control: program identical) | 75 | 20.1 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 69.7 ns, 20 B; largest Δ: `waf-comment-obfuscation`, +9.9 ns (now 35.1 ns), 18 B

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,103.9 | 0.0168 | 23,092.4 | 23,109.7 | 5.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,132.2 | 0.0168 | 23,107.8 | 23,144.0 | 13.2 | 1.001x | 1.001x | slower ×1.00 | +0.12% (null control: program identical) |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,604.8 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,625.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,381.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,384.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,105.4 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,625.5 ns, 1,048,576 B

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 661.7 | 660.1 | 662.6 | 0.9 | 1.000x | 1.000x | - | - | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 678.7 | 678.3 | 684.0 | 2.3 | 1.026x | 1.026x | slower ×1.03 | +2.56% (null control: program identical) | 75 | 9.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `cg-object-begin`, 17.0 ns, 1 B; largest Δ: `sec-slack-webhook`, +0.5 ns (now 10.3 ns), 81 B

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,109.7 | 0.0168 | 23,084.1 | 23,144.7 | 21.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,118.9 | 0.0168 | 23,104.3 | 23,128.7 | 9.1 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,607.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,624.8 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,387.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,385.6 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,111.1 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.5 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,624.8 ns, 1,048,576 B

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 723.8 | 721.9 | 726.4 | 1.9 | 1.000x | 1.000x | - | - | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 740.0 | 723.9 | 747.4 | 8.3 | 1.022x | 1.022x | unchanged (within spread) | +2.24% (null control: program identical) | 75 | 9.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `lp-winpath-reserved`, 35.2 ns, 24 B; largest Δ: `rec-parens-balanced`, +0.4 ns (now 9.0 ns), 7 B

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 0.0000 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 38.1 | 0.0000 | 37.7 | 38.2 | 0.2 | 1.171x | 1.171x | slower ×1.17 | +17.08% (null control: program identical) |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 12.7 ns, 1,048,576 B

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 952.9 | 951.8 | 963.7 | 5.1 | 1.000x | 1.000x | - | - | 75 | 12.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,023.5 | 1,023.1 | 1,024.8 | 0.6 | 1.074x | 1.074x | slower ×1.07 | +7.40% (null control: program identical) | 75 | 13.6 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `dt-iso8601`, 87.0 ns, 20 B

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,036,307.3 | 2.9328 | 4,032,384.6 | 4,047,641.1 | 5,464.6 | 1.000x | 1.000x | unchanged (within spread) | -0.54% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,058,134.8 | 2.9487 | 4,044,291.1 | 4,223,617.9 | 67,731.3 | 1.005x | 1.005x | - | - |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,090,915.0 | 2.9477 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,109,180.9 | 2.9651 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 761,201.2 | 2.9038 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,673.8 | 2.9056 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 184,191.1 | 2.8105 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 185,099.4 | 2.8244 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,090,915.0 ns, 1,048,576 B

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,454.4 | 2,450.8 | 2,520.9 | 26.8 | 1.000x | 1.000x | - | - | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,493.7 | 2,491.3 | 2,515.5 | 9.2 | 1.016x | 1.016x | unchanged (within spread) | +1.60% (null control: program identical) | 75 | 33.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 117.6 ns, 20 B; largest Δ: `rd-email-hit`, +2.3 ns (now 22.1 ns), 10 B

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,009,035.4 | 2.9130 | 4,006,596.2 | 4,057,578.9 | 19,424.4 | 1.000x | 1.000x | unchanged (within spread) | -0.18% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,016,077.8 | 2.9181 | 4,005,031.0 | 4,048,101.7 | 17,917.6 | 1.002x | 1.002x | - | - |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,072,811.9 | 2.9305 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,078,760.7 | 2.9361 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 754,449.0 | 2.8780 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 754,672.1 | 2.8788 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 182,856.9 | 2.7902 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 182,584.1 | 2.7860 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,072,811.9 ns, 1,048,576 B

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,431.5 | 2,429.4 | 2,931.8 | 199.2 | 1.000x | 1.000x | - | - | 75 | 32.4 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,457.3 | 2,444.5 | 2,546.6 | 38.1 | 1.011x | 1.011x | unchanged (within spread) | +1.06% (null control: program identical) | 75 | 32.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `rd-numeric-id-near-miss`, 115.8 ns, 20 B; largest Δ: `sd-empty-alt-hit`, +4.8 ns (now 72.5 ns), 61 B

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 937,630.0 | 0.6813 | 936,830.0 | 937,865.9 | 373.3 | 1.000x | 1.000x | faster ×1.07 | -6.94% vs bar 7.15% (band) → **within** |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007,600.2 | 0.7321 | 1,007,490.2 | 1,008,452.4 | 349.7 | 1.075x | 1.075x | - | - |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 717,355.9 | 0.6841 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 771,752.2 | 0.7360 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 175,659.3 | 0.6701 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 188,328.7 | 0.7184 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 44,515.8 | 0.6793 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 47,627.3 | 0.7267 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 717,355.9 ns, 1,048,576 B

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,888.6 | 1,886.0 | 1,896.0 | 3.8 | 1.000x | 1.000x | faster ×1.02 | -2.20% vs bar 9.21% (band) → **within** | 75 | 25.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,931.1 | 1,919.8 | 1,939.0 | 7.6 | 1.023x | 1.023x | - | - | 75 | 25.7 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-quoted-escaped`, 124.8 ns, 16 B

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 929,037.9 | 0.6750 | 928,706.1 | 929,382.6 | 267.3 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 930,496.2 | 0.6761 | 928,955.6 | 947,710.2 | 7,111.7 | 1.002x | 1.002x | unchanged (within spread) | +0.16% (null control: program identical) |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 710,823.5 | 0.6779 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 711,919.3 | 0.6789 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 173,862.3 | 0.6632 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 174,575.9 | 0.6660 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 44,070.5 | 0.6725 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 43,961.5 | 0.6708 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 711,919.3 ns, 1,048,576 B

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,832.2 | 1,830.5 | 1,837.5 | 3.0 | 1.000x | 1.000x | unchanged (within spread) | -0.12% (null control: program identical) | 75 | 24.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,834.4 | 1,822.6 | 1,890.7 | 24.7 | 1.001x | 1.001x | - | - | 75 | 24.5 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `lp-quoted-escaped`, 127.1 ns, 16 B; largest Δ: `br-quoted-delim`, -11.5 ns (now 86.7 ns), 15 B

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,987,580.5 | 2.8974 | 3,984,588.0 | 3,992,062.5 | 2,426.2 | 1.000x | 1.000x | unchanged (within spread) | -0.03% vs bar 7.15% (band) → **within** |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,988,946.6 | 2.8984 | 3,985,988.0 | 3,990,696.5 | 1,928.7 | 1.000x | 1.000x | - | - |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,037,481.5 | 2.8968 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,036,180.2 | 2.8955 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 760,214.9 | 2.9000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,018.1 | 2.9031 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 190,362.8 | 2.9047 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 190,600.3 | 2.9083 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,037,481.5 ns, 1,048,576 B

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,770.5 | 1,765.7 | 1,801.4 | 13.3 | 1.000x | 1.000x | unchanged (within spread) | -0.64% vs bar 9.21% (band) → **within** | 75 | 23.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,781.8 | 1,776.2 | 1,783.7 | 2.8 | 1.006x | 1.006x | - | - | 75 | 23.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-syslog`, 623.4 ns, 56 B

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,121.0 | 0.0168 | 23,113.0 | 23,144.3 | 10.7 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,147.8 | 0.0168 | 23,138.1 | 23,159.0 | 7.0 | 1.001x | 1.001x | slower ×1.00 | +0.12% (null control: program identical) |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,630.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,658.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,376.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,111.6 | 0.0170 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,658.4 ns, 1,048,576 B

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 932.5 | 929.4 | 934.7 | 1.8 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) | 75 | 12.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 933.1 | 925.3 | 934.3 | 3.6 | 1.001x | 1.001x | - | - | 75 | 12.4 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-winpath-reserved`, 79.3 ns, 24 B

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,941,061.0 | 2.8636 | 3,940,441.6 | 3,943,170.1 | 1,103.4 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,084,696.9 | 2.9680 | 4,082,641.2 | 4,086,504.9 | 1,266.7 | 1.036x | 1.036x | slower ×1.04 | +3.64% vs bar 7.15% (band) → **within** |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,003,059.3 | 2.8639 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,111,755.0 | 2.9676 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 751,290.9 | 2.8659 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 779,128.6 | 2.9721 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 186,921.8 | 2.8522 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 192,843.9 | 2.9426 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 3,111,755.0 ns, 1,048,576 B

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,165.8 | 1,165.7 | 1,172.4 | 2.6 | 1.000x | 1.000x | - | - | 75 | 15.5 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,188.8 | 1,187.2 | 1,189.5 | 0.8 | 1.020x | 1.020x | slower ×1.02 | +1.97% vs bar 9.21% (band) → **within** | 75 | 15.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 178.4 ns, 93 B; largest Δ: `sec-userpass`, +0.6 ns (now 10.3 ns), 33 B

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 124,697.0 | 0.0906 | 124,525.4 | 124,867.0 | 119.5 | 1.000x | 1.000x | unchanged (within spread) | -0.00% vs bar 7.15% (band) → **within** |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 124,699.4 | 0.0906 | 124,535.5 | 124,820.2 | 93.7 | 1.000x | 1.000x | - | - |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 102,182.4 | 0.0974 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 102,066.8 | 0.0973 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 18,891.9 | 0.0721 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 18,930.6 | 0.0722 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 3,651.5 | 0.0557 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 3,621.6 | 0.0553 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 102,182.4 ns, 1,048,576 B

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,515.1 | 1,513.6 | 1,517.9 | 1.5 | 1.000x | 1.000x | - | - | 75 | 20.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,515.5 | 1,511.3 | 1,523.0 | 4.3 | 1.000x | 1.000x | unchanged (within spread) | +0.03% vs bar 9.21% (band) → **within** | 75 | 20.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `sec-github-pat`, 460.2 ns, 93 B

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 354,034.8 | 0.2572 | 353,916.6 | 354,061.6 | 62.9 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 354,258.9 | 0.2574 | 354,067.0 | 354,609.0 | 189.7 | 1.001x | 1.001x | unchanged (within spread) | +0.06% vs bar 7.15% (band) → **within** |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 271,742.8 | 0.2592 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 271,924.5 | 0.2593 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 66,855.1 | 0.2550 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 66,946.6 | 0.2554 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15,330.8 | 0.2339 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15,377.6 | 0.2346 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 271,924.5 ns, 1,048,576 B

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,252.7 | 1,248.6 | 1,257.5 | 3.2 | 1.000x | 1.000x | - | - | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,312.5 | 1,306.1 | 1,327.5 | 7.8 | 1.048x | 1.048x | slower ×1.05 | +4.78% vs bar 9.21% (band) → **within** | 75 | 17.5 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 407.0 ns, 81 B

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,099.3 | 0.0168 | 23,094.6 | 23,130.4 | 14.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,149.2 | 0.0168 | 23,137.1 | 23,228.4 | 33.1 | 1.002x | 1.002x | unchanged (within spread) | +0.22% vs bar 7.15% (band) → **within** |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,611.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,649.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,380.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,388.3 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,112.7 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,110.0 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,649.5 ns, 1,048,576 B

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,045.5 | 1,043.7 | 1,047.1 | 1.1 | 1.000x | 1.000x | faster ×1.01 | -0.66% vs bar 9.21% (band) → **within** | 75 | 13.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,052.5 | 1,051.4 | 1,053.0 | 0.6 | 1.007x | 1.007x | - | - | 75 | 14.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `sec-userpass`, 247.9 ns, 33 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 352,040.3 | 0.2558 | 351,914.8 | 352,663.6 | 330.1 | 1.000x | 1.000x | unchanged (within spread) | -0.07% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 352,292.7 | 0.2560 | 351,592.9 | 592,751.9 | 96,238.4 | 1.001x | 1.001x | - | - |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 282,824.7 | 0.2697 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 282,877.2 | 0.2698 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 58,399.9 | 0.2228 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 58,459.8 | 0.2230 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11,027.6 | 0.1683 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 11,027.6 | 0.1683 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 282,824.7 ns, 1,048,576 B; largest Δ: `t-256k`, -59.9 ns (now 58,399.9 ns), 262,144 B

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 657.5 | 657.3 | 658.7 | 0.5 | 1.000x | 1.000x | - | - | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 659.6 | 659.1 | 660.8 | 0.6 | 1.003x | 1.003x | slower ×1.00 | +0.32% (null control: program identical) | 75 | 8.8 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-slack-webhook`, 13.5 ns, 81 B; largest Δ: `nu-lead-with-cont`, +0.3 ns (now 5.3 ns), 2 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 0.0000 | 39.2 | 39.8 | 0.2 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 40.0 | 0.0000 | 40.0 | 40.6 | 0.3 | 1.019x | 1.019x | slower ×1.02 | +1.94% (null control: program identical) |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 13.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 13.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 13.4 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 13.4 ns, 65,536 B

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 872.5 | 871.5 | 877.4 | 2.2 | 1.000x | 1.000x | - | - | 75 | 11.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 915.4 | 913.2 | 941.0 | 10.3 | 1.049x | 1.049x | slower ×1.05 | +4.92% (null control: program identical) | 75 | 12.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `la-negation-hit`, 17.4 ns, 19 B; largest Δ: `rd-email-near-miss`, +1.1 ns (now 12.4 ns), 20 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,003,254.1 | 5.0886 | 6,988,301.5 | 7,009,588.0 | 7,476.6 | 1.000x | 1.000x | faster ×1.08 | -7.15% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,542,898.4 | 5.4807 | 7,521,327.7 | 7,611,419.9 | 30,850.8 | 1.077x | 1.077x | - | - |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5,375,672.2 | 5.1266 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 5,783,435.1 | 5.5155 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,309,101.3 | 4.9938 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,418,365.5 | 5.4106 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 316,598.6 | 4.8309 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 342,059.0 | 5.2194 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 5,375,672.2 ns, 1,048,576 B

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,860.5 | 2,850.4 | 2,876.2 | 10.2 | 1.000x | 1.000x | - | - | 75 | 38.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,100.2 | 3,067.1 | 3,129.5 | 21.9 | 1.084x | 1.084x | slower ×1.08 | +8.38% (null control: program identical) | 75 | 41.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sd-empty-alt-hit`, 934.5 ns, 61 B; largest Δ: `waf-concat`, +12.2 ns (now 56.7 ns), 48 B

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 39.1 | 0.0000 | 38.0 | 40.9 | 1.1 | 1.000x | 1.000x | unchanged (within spread) | -0.85% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.5 | 0.0000 | 37.3 | 42.1 | 1.6 | 1.009x | 1.009x | - | - |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 14.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 12.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 12.3 | 0.0002 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 14.8 ns, 1,048,576 B

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,011.6 | 1,009.4 | 1,014.9 | 1.8 | 1.000x | 1.000x | faster ×1.04 | -3.95% (null control: program identical) | 75 | 13.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,053.2 | 1,049.7 | 1,064.7 | 5.2 | 1.041x | 1.041x | - | - | 75 | 14.0 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 72.8 ns, 93 B; largest Δ: `la-negation-hit`, -18.9 ns (now 15.5 ns), 19 B

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 0.0000 | 26.2 | 26.4 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 0.0000 | 29.4 | 29.4 | 0.0 | 1.119x | 1.119x | slower ×1.12 | +11.95% (null control: program identical) |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-64k`, 9.8 ns, 65,536 B

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 795.7 | 793.0 | 796.2 | 1.4 | 1.000x | 1.000x | - | - | 75 | 10.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 804.2 | 803.6 | 805.9 | 0.9 | 1.011x | 1.011x | slower ×1.01 | +1.07% (null control: program identical) | 75 | 10.7 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `v-ipv4`, 64.1 ns, 11 B; largest Δ: `br-palindrome`, +0.3 ns (now 12.7 ns), 6 B

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 0.0000 | 26.7 | 26.8 | 0.1 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.0 | 0.0000 | 29.0 | 29.2 | 0.1 | 1.088x | 1.088x | slower ×1.09 | +8.77% (null control: program identical) |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-64k`, 9.7 ns, 65,536 B; largest Δ: `t-1m`, +0.8 ns (now 9.7 ns), 1,048,576 B

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 735.1 | 734.8 | 738.1 | 1.2 | 1.000x | 1.000x | - | - | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 757.8 | 756.0 | 774.0 | 6.6 | 1.031x | 1.031x | slower ×1.03 | +3.09% (null control: program identical) | 75 | 10.1 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `v-us-zip-plus4`, 32.1 ns, 10 B; largest Δ: `v-email`, +0.6 ns (now 8.9 ns), 24 B

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 82,339.2 | 0.0598 | 82,098.2 | 82,936.8 | 300.7 | 1.000x | 1.000x | unchanged (within spread) | -0.24% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 82,536.0 | 0.0600 | 82,271.7 | 83,000.2 | 264.8 | 1.002x | 1.002x | - | - |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 68,352.6 | 0.0652 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 68,444.1 | 0.0653 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11,583.9 | 0.0442 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11,619.0 | 0.0443 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 2,413.8 | 0.0368 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 2,400.0 | 0.0366 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 68,352.6 ns, 1,048,576 B

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 681.9 | 677.9 | 685.3 | 2.7 | 1.000x | 1.000x | - | - | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 689.3 | 688.6 | 691.7 | 1.1 | 1.011x | 1.011x | slower ×1.01 | +1.09% (null control: program identical) | 75 | 9.2 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `v-uuid-valid`, 90.4 ns, 36 B

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,079,777.3 | 2.9644 | 4,076,518.1 | 4,092,570.0 | 5,839.3 | 1.000x | 1.000x | unchanged (within spread) | -0.02% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,080,790.5 | 2.9651 | 4,077,154.4 | 4,088,404.5 | 3,759.2 | 1.000x | 1.000x | - | - |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,112,908.6 | 2.9687 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,112,749.5 | 2.9685 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 775,894.4 | 2.9598 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 776,394.8 | 2.9617 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 191,650.4 | 2.9244 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 191,610.1 | 2.9237 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 3,112,908.6 ns, 1,048,576 B; largest Δ: `t-256k`, -500.4 ns (now 775,894.4 ns), 262,144 B

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,693.0 | 2,687.0 | 2,694.9 | 2.9 | 1.000x | 1.000x | - | - | 75 | 35.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,695.7 | 2,692.0 | 2,702.2 | 3.7 | 1.001x | 1.001x | unchanged (within spread) | +0.10% (null control: program identical) | 75 | 35.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `sec-github-pat`, 184.5 ns, 93 B; largest Δ: `rd-trim-near-miss`, +1.8 ns (now 16.5 ns), 20 B

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,357,172.5 | 0.9861 | 1,355,617.8 | 1,360,635.2 | 1,888.0 | 1.000x | 1.000x | - | - |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,358,812.3 | 0.9873 | 1,356,860.3 | 1,363,536.2 | 2,365.0 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,028,682.2 | 0.9810 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,031,315.4 | 0.9835 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 260,617.0 | 0.9942 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 258,361.5 | 0.9856 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 67,873.2 | 1.0357 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 68,913.4 | 1.0515 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 1,031,315.4 ns, 1,048,576 B

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.3 | 664.0 | 670.7 | 2.7 | 1.000x | 1.000x | - | - | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 667.8 | 667.4 | 675.2 | 3.0 | 1.001x | 1.001x | unchanged (within spread) | +0.08% (null control: program identical) | 75 | 8.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `waf-concat`, 47.0 ns, 48 B; largest Δ: `waf-sleep`, +1.0 ns (now 45.3 ns), 16 B

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 999,148.7 | 0.7260 | 997,095.8 | 999,792.2 | 1,025.1 | 1.000x | 1.000x | unchanged (within spread) | -0.09% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,000,077.4 | 0.7267 | 997,444.6 | 1,001,259.3 | 1,549.1 | 1.001x | 1.001x | - | - |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 757,984.8 | 0.7229 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 759,695.9 | 0.7245 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 191,125.4 | 0.7291 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 192,069.1 | 0.7327 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 50,243.5 | 0.7667 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 48,170.8 | 0.7350 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-1m`, 757,984.8 ns, 1,048,576 B; largest Δ: `t-64k`, +2,072.8 ns (now 50,243.5 ns), 65,536 B

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,095.0 | 1,079.0 | 1,109.4 | 9.9 | 1.000x | 1.000x | - | - | 75 | 14.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,158.0 | 1,139.8 | 1,170.7 | 10.2 | 1.057x | 1.057x | slower ×1.06 | +5.75% (null control: program identical) | 75 | 15.4 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `waf-union`, 75.1 ns, 43 B; largest Δ: `waf-sleep`, +2.3 ns (now 13.4 ns), 16 B

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,118,975.0 | 8.8058 | 12,103,560.3 | 12,151,845.6 | 17,642.8 | 1.000x | 1.000x | unchanged (within spread) | -0.12% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,133,714.5 | 8.8165 | 12,106,982.1 | 12,242,434.1 | 49,192.1 | 1.001x | 1.001x | - | - |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9,234,402.1 | 8.8066 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9,252,129.7 | 8.8235 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,303,374.4 | 8.7867 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,306,117.0 | 8.7971 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 576,707.5 | 8.7999 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 575,832.8 | 8.7865 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 9,234,402.1 ns, 1,048,576 B

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,333.2 | 7,324.9 | 7,359.1 | 13.3 | 1.000x | 1.000x | - | - | 75 | 97.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,342.1 | 7,322.8 | 7,468.5 | 53.1 | 1.001x | 1.001x | unchanged (within spread) | +0.12% (null control: program identical) | 75 | 97.9 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `sec-slack-webhook`, 456.5 ns, 81 B

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,137.1 | 0.0168 | 23,118.4 | 23,144.4 | 9.0 | 1.000x | 1.000x | unchanged (within spread) | -0.15% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,172.9 | 0.0168 | 23,111.3 | 23,183.8 | 26.4 | 1.002x | 1.002x | - | - |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,625.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,641.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,407.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,419.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,106.2 | 0.0169 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `t-1m`, 17,625.5 ns, 1,048,576 B

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 694.0 | 692.4 | 697.3 | 1.7 | 1.000x | 1.000x | - | - | 75 | 9.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 694.3 | 692.4 | 696.3 | 1.4 | 1.000x | 1.000x | unchanged (within spread) | +0.04% (null control: program identical) | 75 | 9.3 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `waf-comment-obfuscation`, 78.6 ns, 18 B; largest Δ: `rec-comment-nested`, +2.5 ns (now 46.8 ns), 34 B

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 0.0000 | 19.6 | 19.7 | 0.0 | 1.000x | 1.000x | faster ×1.03 | -2.51% (null control: program identical) |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20.2 | 0.0000 | 20.0 | 20.3 | 0.1 | 1.026x | 1.026x | - | - |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0001 |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now: `t-256k`, 6.6 ns, 262,144 B; largest Δ: `t-1m`, -0.2 ns (now 6.5 ns), 1,048,576 B

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | D119 bar | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 457.3 | 455.9 | 467.7 | 4.4 | 1.000x | 1.000x | faster ×1.04 | -4.10% (null control: program identical) | 75 | 6.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 476.8 | 471.2 | 487.6 | 5.6 | 1.043x | 1.043x | - | - | 75 | 6.4 | 8.9 | 100% |

- Δ detail: `pcrec_a32bc86e_auto-caps-simdna` vs previous `pcrec_02902356_auto-caps-simdna`: worst now (also the largest Δ): `lp-winpath`, 33.0 ns, 22 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_02902356_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |

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
- `pcrec_a32bc86e_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,868 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,676 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,781 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,687 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,792 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,277 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,382 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 9,869 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 9,977 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,655 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,760 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,642 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,747 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-datetime-datefinder-alternation` / `whole-subject`: engine=vm, sel=overflowed-prefilter (DFA fallback tripped), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 508,522 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=49/74 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,426 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,531 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1462187 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 298,587 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1483394 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 298,696 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 5,475 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 5,580 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,326 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,431 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,307 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,412 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
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
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 208,452,842.0 | 206,383,151.0 | 221,662,851.0 | 5,752,093.9 | 5 | 31,768 | 26,113 | 25,828 | 0.028 | compiled=5 | 1,702,399.0 | 205,189,185.0 | 204,941.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 214,373,012.0 | 206,883,884.0 | 219,042,827.0 | 4,245,280.6 | 5 | 31,768 | 26,331 | 26,046 | 0.020 | compiled=5 | 1,675,508.0 | 212,511,383.0 | 189,381.0 |
| `base10num-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,094,211.0 | 138,333,610.0 | 151,301,477.0 | 4,719,692.3 | 5 | 27,648 | 16,320 | 13,935 | 0.032 | compiled=5 | 1,631,628.0 | 146,294,401.0 | 101,161.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 137,940,318.0 | 136,577,931.0 | 146,910,385.0 | 4,662,255.4 | 5 | 27,576 | 15,773 | 13,388 | 0.034 | compiled=5 | 1,635,779.0 | 136,205,539.0 | 194,471.0 |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 145,371,950.0 | 138,568,735.0 | 153,278,962.0 | 5,696,775.1 | 5 | 27,736 | 16,705 | 14,320 | 0.039 | compiled=5 | 1,783,989.0 | 143,339,570.0 | 102,021.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 147,682,043.0 | 144,237,525.0 | 148,994,101.0 | 1,743,208.2 | 5 | 27,656 | 16,158 | 13,773 | 0.012 | compiled=5 | 1,639,749.0 | 145,956,264.0 | 101,290.0 |
| `bracket-array-define` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,270,669.0 | 211,163,963.0 | 224,199,463.0 | 4,882,486.6 | 5 | 31,648 | 26,139 | 25,824 | 0.022 | compiled=5 | 1,686,498.0 | 221,482,451.0 | 101,720.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 228,014,961.0 | 222,442,095.0 | 241,491,844.0 | 6,362,092.8 | 5 | 31,648 | 26,254 | 25,939 | 0.028 (max is trial 1) | compiled=5 | 1,699,348.0 | 225,781,060.0 | 114,391.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 225,221,190.0 | 213,123,235.0 | 225,745,301.0 | 4,891,966.1 | 5 | 31,728 | 26,549 | 26,234 | 0.022 | compiled=5 | 1,726,719.0 | 223,410,240.0 | 108,421.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 224,776,286.0 | 220,602,345.0 | 225,617,432.0 | 1,782,794.7 | 5 | 31,728 | 26,664 | 26,349 | 0.008 | compiled=5 | 1,719,029.0 | 222,978,837.0 | 113,031.0 |
| `codegrammar-flat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 350,410,210.0 | 347,739,808.0 | 352,229,248.0 | 1,465,395.4 | 5 | 31,984 | 35,289 | 26,690 | 0.004 | compiled=5 | 2,188,300.0 | 348,176,700.0 | 102,460.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,590,435.0 | 343,778,670.0 | 361,485,642.0 | 6,386,224.1 | 5 | 32,032 | 35,010 | 27,498 | 0.018 | compiled=5 | 2,135,140.0 | 349,531,146.0 | 99,890.0 |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 350,123,883.0 | 340,140,481.0 | 351,826,391.0 | 4,347,160.1 | 5 | 32,072 | 35,699 | 27,100 | 0.012 | compiled=5 | 2,209,132.0 | 347,823,051.0 | 101,380.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 358,195,095.0 | 354,131,313.0 | 365,237,353.0 | 3,630,449.7 | 5 | 32,120 | 35,420 | 27,908 | 0.010 | compiled=5 | 2,163,552.0 | 355,949,114.0 | 102,980.0 |
| `codegrammar-xflag` | `plain` | `pcrec_02902356_auto-caps-simdna` | 349,902,468.0 | 344,855,334.0 | 351,068,773.0 | 2,466,814.7 | 5 | 32,024 | 35,615 | 26,937 | 0.007 | compiled=5 | 2,202,800.0 | 347,633,747.0 | 104,040.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,322,484.0 | 344,475,522.0 | 358,781,989.0 | 4,895,962.2 | 5 | 32,072 | 35,340 | 27,749 | 0.014 | compiled=5 | 2,154,780.0 | 348,723,862.0 | 111,441.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 350,966,168.0 | 345,076,116.0 | 352,303,174.0 | 2,606,224.1 | 5 | 32,104 | 36,025 | 27,347 | 0.007 | compiled=5 | 2,200,982.0 | 348,572,585.0 | 106,981.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 353,496,450.0 | 349,871,930.0 | 365,418,924.0 | 5,723,797.7 | 5 | 32,160 | 35,750 | 28,159 | 0.016 | compiled=5 | 2,239,491.0 | 348,776,786.0 | 191,791.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 224,567,663.0 | 217,270,151.0 | 232,909,143.0 | 5,249,245.5 | 5 | 32,008 | 32,574 | 26,943 | 0.023 | compiled=5 | 2,034,759.0 | 222,317,773.0 | 171,681.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 229,759,429.0 | 227,431,818.0 | 235,263,025.0 | 2,622,800.3 | 5 | 32,096 | 34,600 | 28,351 | 0.011 | compiled=5 | 2,097,270.0 | 227,096,016.0 | 103,261.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 224,600,066.0 | 218,829,576.0 | 228,270,424.0 | 3,168,047.0 | 5 | 32,088 | 32,984 | 27,353 | 0.014 | compiled=5 | 4,057,342.0 | 222,260,914.0 | 187,291.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 230,919,989.0 | 223,133,308.0 | 234,668,099.0 | 3,798,788.1 | 5 | 32,184 | 35,010 | 28,761 | 0.016 | compiled=5 | 2,081,051.0 | 228,635,547.0 | 189,261.0 |
| `date-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 251,160,339.0 | 249,828,153.0 | 264,233,379.0 | 5,768,044.1 | 5 | 31,872 | 33,439 | 31,413 | 0.023 | compiled=5 | 1,862,789.0 | 249,273,970.0 | 188,011.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 249,914,942.0 | 246,615,467.0 | 257,896,949.0 | 4,535,537.5 | 5 | 31,872 | 33,367 | 31,341 | 0.018 | compiled=5 | 1,881,209.0 | 247,932,523.0 | 117,800.0 |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 253,084,435.0 | 252,476,243.0 | 264,966,867.0 | 5,700,569.9 | 5 | 31,952 | 33,849 | 31,823 | 0.023 | compiled=5 | 1,725,779.0 | 251,278,805.0 | 115,650.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,462,451.0 | 244,381,000.0 | 270,497,115.0 | 8,788,456.5 | 5 | 31,952 | 33,777 | 31,751 | 0.035 | compiled=5 | 3,302,837.0 | 248,734,082.0 | 190,251.0 |
| `doubled-word` | `plain` | `pcrec_02902356_auto-caps-simdna` | 215,788,773.0 | 207,712,437.0 | 216,861,368.0 | 3,390,669.8 | 5 | 27,504 | 24,373 | 23,911 | 0.016 | compiled=5 | 1,680,198.0 | 213,931,115.0 | 196,271.0 |
| `doubled-word` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,520,938.0 | 208,120,917.0 | 221,358,749.0 | 4,855,937.6 | 5 | 27,504 | 24,486 | 24,024 | 0.023 (max is trial 1) | compiled=5 | 1,686,258.0 | 212,716,719.0 | 118,301.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 214,990,815.0 | 210,490,090.0 | 218,096,322.0 | 2,579,313.9 | 5 | 27,592 | 24,783 | 24,321 | 0.012 | compiled=5 | 1,695,228.0 | 213,185,706.0 | 103,791.0 |
| `doubled-word` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 216,567,694.0 | 211,061,905.0 | 222,613,486.0 | 3,756,800.8 | 5 | 27,592 | 24,896 | 24,434 | 0.017 (max is trial 1) | compiled=5 | 1,699,979.0 | 214,706,054.0 | 187,401.0 |
| `dup-param-detect` | `plain` | `pcrec_02902356_auto-caps-simdna` | 234,612,641.0 | 227,933,080.0 | 241,146,671.0 | 4,181,673.6 | 5 | 31,776 | 27,325 | 26,809 | 0.018 (max is trial 1) | compiled=5 | 1,754,538.0 | 232,771,902.0 | 110,041.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,092,611.0 | 217,763,663.0 | 234,533,541.0 | 6,289,871.0 | 5 | 31,776 | 27,438 | 26,922 | 0.027 | compiled=5 | 1,725,488.0 | 226,268,403.0 | 104,011.0 |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 229,680,983.0 | 219,861,912.0 | 239,371,402.0 | 6,186,208.4 | 5 | 31,856 | 27,735 | 27,219 | 0.027 | compiled=5 | 3,491,678.0 | 226,962,628.0 | 193,151.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 236,440,277.0 | 231,137,260.0 | 250,383,731.0 | 6,578,609.0 | 5 | 31,856 | 27,848 | 27,332 | 0.028 (max is trial 1) | compiled=5 | 1,788,029.0 | 234,549,158.0 | 109,111.0 |
| `email-local-nodup` | `plain` | `pcrec_02902356_auto-caps-simdna` | 204,559,462.0 | 191,806,192.0 | 205,457,235.0 | 5,327,770.4 | 5 | 31,712 | 26,945 | 24,872 | 0.026 | compiled=5 | 1,766,369.0 | 202,687,053.0 | 192,130.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,071,763.0 | 191,308,920.0 | 200,424,182.0 | 3,176,949.1 | 5 | 31,720 | 27,363 | 25,219 | 0.016 | compiled=5 | 1,749,518.0 | 192,347,385.0 | 120,181.0 |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 206,839,631.0 | 199,756,916.0 | 212,198,151.0 | 5,135,285.7 | 5 | 31,792 | 27,235 | 25,162 | 0.025 (max is trial 1) | compiled=5 | 2,026,960.0 | 204,713,392.0 | 189,131.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 204,808,223.0 | 187,695,174.0 | 216,185,542.0 | 9,642,847.1 | 5 | 31,800 | 27,653 | 25,509 | 0.047 | compiled=5 | 3,403,768.0 | 200,820,072.0 | 189,941.0 |
| `email-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,213,978.0 | 214,580,838.0 | 223,994,381.0 | 3,771,618.7 | 5 | 31,832 | 28,826 | 26,880 | 0.017 | compiled=5 | 1,832,518.0 | 221,267,189.0 | 186,060.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 216,172,054.0 | 210,298,878.0 | 223,508,450.0 | 4,860,331.8 | 5 | 31,832 | 29,257 | 27,227 | 0.022 | compiled=5 | 1,800,538.0 | 214,180,096.0 | 192,210.0 |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 223,729,482.0 | 217,322,539.0 | 223,986,842.0 | 2,986,066.1 | 5 | 31,912 | 29,236 | 27,290 | 0.013 | compiled=5 | 1,817,629.0 | 221,810,052.0 | 101,801.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 221,683,581.0 | 217,384,389.0 | 222,385,774.0 | 2,285,974.9 | 5 | 31,912 | 29,667 | 27,637 | 0.010 | compiled=5 | 1,795,549.0 | 219,891,452.0 | 106,411.0 |
| `evil-alt-nested` | `plain` | `pcrec_02902356_auto-caps-simdna` | 214,074,876.0 | 209,341,143.0 | 216,527,358.0 | 2,408,841.2 | 5 | 27,552 | 25,358 | 25,358 | 0.011 | compiled=5 | 1,662,718.0 | 212,224,787.0 | 207,241.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,635,217.0 | 201,477,147.0 | 215,388,932.0 | 5,333,958.1 | 5 | 27,552 | 25,471 | 25,471 | 0.025 | compiled=5 | 1,690,068.0 | 212,805,989.0 | 102,860.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 212,774,164.0 | 208,310,700.0 | 216,320,293.0 | 3,275,921.4 | 5 | 31,728 | 25,768 | 25,768 | 0.015 | compiled=5 | 1,697,129.0 | 209,190,115.0 | 198,091.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 210,850,034.0 | 202,000,168.0 | 215,038,216.0 | 4,383,842.0 | 5 | 31,728 | 25,881 | 25,881 | 0.021 | compiled=5 | 1,698,369.0 | 208,875,864.0 | 184,751.0 |
| `file-ext-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,250,270.0 | 140,732,663.0 | 158,455,936.0 | 5,665,182.7 | 5 | 27,792 | 20,895 | 14,772 | 0.038 | compiled=5 | 1,948,959.0 | 145,949,819.0 | 203,391.0 |
| `file-ext-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,129,179.0 | 156,221,896.0 | 173,711,608.0 | 5,936,766.4 | 5 | 27,936 | 24,039 | 16,973 | 0.036 | compiled=5 | 2,138,890.0 | 163,115,219.0 | 205,831.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 159,756,607.0 | 149,287,072.0 | 163,008,534.0 | 4,754,538.2 | 5 | 27,872 | 21,280 | 15,157 | 0.030 | compiled=5 | 1,994,100.0 | 155,575,225.0 | 101,620.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 165,211,874.0 | 163,527,287.0 | 172,405,403.0 | 3,793,431.2 | 5 | 28,016 | 24,424 | 17,358 | 0.023 | compiled=5 | 2,067,281.0 | 163,068,553.0 | 103,401.0 |
| `float-literal-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,941,994.0 | 230,001,560.0 | 239,382,663.0 | 3,929,306.9 | 5 | 31,984 | 33,490 | 28,341 | 0.017 | compiled=5 | 2,041,769.0 | 228,819,344.0 | 198,701.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,345,992.0 | 227,149,656.0 | 237,412,245.0 | 3,380,353.5 | 5 | 32,080 | 34,332 | 28,874 | 0.015 | compiled=5 | 2,055,780.0 | 227,823,219.0 | 112,461.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,811,423.0 | 227,807,622.0 | 239,221,642.0 | 4,532,787.0 | 5 | 32,072 | 33,900 | 28,751 | 0.020 | compiled=5 | 2,083,101.0 | 229,499,711.0 | 109,091.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 242,456,359.0 | 234,087,996.0 | 253,492,716.0 | 6,857,489.0 | 5 | 32,160 | 34,742 | 29,284 | 0.028 | compiled=5 | 4,337,232.0 | 237,910,476.0 | 111,240.0 |
| `floor-byte` | `plain` | `pcrec_02902356_auto-caps-simdna` | 155,008,700.0 | 143,501,097.0 | 155,719,114.0 | 4,762,276.9 | 5 | 27,792 | 19,408 | 14,411 | 0.031 | compiled=5 | 1,780,579.0 | 153,053,781.0 | 188,591.0 |
| `floor-byte` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,083,528.0 | 155,416,843.0 | 166,119,563.0 | 3,972,416.0 | 5 | 27,936 | 21,863 | 16,540 | 0.024 | compiled=5 | 1,859,818.0 | 163,235,379.0 | 190,261.0 |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 156,028,327.0 | 147,932,183.0 | 156,236,228.0 | 3,178,851.0 | 5 | 27,872 | 19,793 | 14,796 | 0.020 | compiled=5 | 1,833,159.0 | 154,011,976.0 | 111,930.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,431,851.0 | 157,528,635.0 | 173,932,121.0 | 5,962,084.0 | 5 | 28,016 | 22,248 | 16,925 | 0.037 | compiled=5 | 3,613,079.0 | 158,509,710.0 | 99,541.0 |
| `high-byte-run` | `plain` | `pcrec_02902356_auto-caps-simdna` | 169,620,318.0 | 153,693,524.0 | 173,204,545.0 | 7,061,656.2 | 5 | 27,488 | 25,653 | 19,347 | 0.042 | compiled=5 | 1,933,769.0 | 167,578,339.0 | 112,740.0 |
| `high-byte-run` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 169,622,188.0 | 163,646,892.0 | 171,473,048.0 | 2,650,434.4 | 5 | 27,928 | 24,467 | 17,340 | 0.016 (max is trial 1) | compiled=5 | 1,949,179.0 | 167,097,708.0 | 199,941.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 174,027,552.0 | 167,859,269.0 | 178,789,225.0 | 3,482,001.9 | 5 | 27,576 | 26,038 | 19,732 | 0.020 | compiled=5 | 1,977,521.0 | 171,948,030.0 | 187,571.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 161,439,115.0 | 157,110,831.0 | 170,269,261.0 | 4,291,288.4 | 5 | 28,008 | 24,852 | 17,725 | 0.027 | compiled=5 | 2,013,100.0 | 159,248,334.0 | 101,701.0 |
| `ipv4-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 170,419,577.0 | 161,408,870.0 | 172,392,567.0 | 4,137,927.8 | 5 | 32,608 | 23,285 | 17,969 | 0.024 | compiled=5 | 1,847,110.0 | 166,539,457.0 | 199,661.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 164,072,064.0 | 154,857,626.0 | 166,538,377.0 | 4,241,398.8 | 5 | 32,400 | 22,363 | 17,047 | 0.026 | compiled=5 | 1,882,020.0 | 162,120,374.0 | 194,501.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 170,074,150.0 | 169,069,585.0 | 174,763,394.0 | 2,126,143.4 | 5 | 32,688 | 23,670 | 18,354 | 0.013 (max is trial 1) | compiled=5 | 1,947,050.0 | 167,913,589.0 | 194,961.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 166,024,439.0 | 157,491,824.0 | 168,646,413.0 | 3,909,697.1 | 5 | 32,480 | 22,748 | 17,432 | 0.024 | compiled=5 | 2,070,291.0 | 162,119,679.0 | 184,491.0 |
| `keyword-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,124,687.0 | 147,423,135.0 | 159,997,653.0 | 4,588,629.6 | 5 | 27,792 | 21,373 | 14,759 | 0.030 (max is trial 1) | compiled=5 | 3,929,019.0 | 150,279,519.0 | 106,880.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 162,479,826.0 | 159,682,963.0 | 170,528,473.0 | 4,867,929.2 | 5 | 27,936 | 25,794 | 16,968 | 0.030 | compiled=5 | 2,084,449.0 | 160,468,406.0 | 198,911.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 154,344,437.0 | 148,387,787.0 | 160,011,488.0 | 4,195,707.3 | 5 | 27,872 | 21,758 | 15,144 | 0.027 | compiled=5 | 1,975,841.0 | 152,448,708.0 | 110,420.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 167,415,397.0 | 165,154,174.0 | 170,910,644.0 | 2,343,889.0 | 5 | 28,016 | 26,179 | 17,353 | 0.014 | compiled=5 | 4,253,332.0 | 165,187,235.0 | 100,971.0 |
| `logparse-atomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 316,824,599.0 | 314,742,678.0 | 320,805,700.0 | 2,144,910.4 | 5 | 83,024 | 63,563 | 43,630 | 0.007 (max is trial 1) | compiled=5 | 2,703,634.0 | 313,899,064.0 | 221,901.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,585,933.0 | 312,902,408.0 | 320,630,098.0 | 2,936,477.8 | 5 | 82,984 | 63,490 | 43,557 | 0.009 | compiled=5 | 2,686,644.0 | 316,769,058.0 | 130,231.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 279,841,676.0 | 273,442,222.0 | 285,555,834.0 | 4,713,372.1 | 5 | 79,008 | 57,513 | 37,580 | 0.017 | compiled=5 | 2,568,964.0 | 273,557,563.0 | 220,661.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 286,471,690.0 | 282,175,078.0 | 301,119,116.0 | 6,698,369.2 | 5 | 78,968 | 57,440 | 37,507 | 0.023 | compiled=5 | 2,589,423.0 | 283,680,815.0 | 222,251.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 314,151,105.0 | 306,248,263.0 | 319,478,292.0 | 5,091,018.5 | 5 | 83,024 | 63,282 | 43,349 | 0.016 (max is trial 1) | compiled=5 | 2,640,974.0 | 311,347,630.0 | 129,241.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,728,574.0 | 314,575,567.0 | 322,566,349.0 | 2,653,143.6 | 5 | 82,984 | 63,209 | 43,276 | 0.008 | compiled=5 | 2,694,314.0 | 316,910,999.0 | 121,910.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 272,499,827.0 | 264,641,576.0 | 281,723,655.0 | 5,454,008.2 | 5 | 79,008 | 57,232 | 37,299 | 0.020 | compiled=5 | 2,580,484.0 | 269,832,543.0 | 215,021.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 284,152,208.0 | 276,675,398.0 | 286,255,139.0 | 3,703,073.4 | 5 | 78,968 | 57,159 | 37,226 | 0.013 | compiled=5 | 2,598,714.0 | 281,414,453.0 | 119,521.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,861,807.0 | 147,480,596.0 | 154,937,280.0 | 2,590,803.2 | 5 | 27,792 | 19,636 | 14,433 | 0.017 | compiled=5 | 1,886,669.0 | 149,911,427.0 | 102,521.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,905,413.0 | 152,217,487.0 | 167,914,941.0 | 6,347,373.2 | 5 | 27,936 | 22,055 | 16,450 | 0.039 | compiled=5 | 1,980,399.0 | 159,936,974.0 | 194,641.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,267,954.0 | 144,686,957.0 | 156,558,620.0 | 4,476,358.8 | 5 | 27,872 | 20,021 | 14,818 | 0.029 | compiled=5 | 1,887,770.0 | 152,547,958.0 | 207,871.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 164,907,753.0 | 153,157,671.0 | 171,401,808.0 | 5,938,427.6 | 5 | 28,016 | 22,440 | 16,835 | 0.036 | compiled=5 | 1,920,700.0 | 162,890,703.0 | 188,361.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_02902356_auto-caps-simdna` | 287,310,097.0 | 282,527,124.0 | 291,975,619.0 | 3,234,697.7 | 5 | 31,688 | 31,521 | 31,290 | 0.011 | compiled=5 | 1,881,739.0 | 283,405,708.0 | 103,980.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 291,557,535.0 | 275,806,332.0 | 293,634,205.0 | 6,762,529.5 | 5 | 31,688 | 31,634 | 31,403 | 0.023 | compiled=5 | 1,918,699.0 | 289,668,927.0 | 111,690.0 |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 290,302,620.0 | 282,317,047.0 | 312,469,906.0 | 10,595,435.9 | 5 | 31,768 | 31,367 | 31,136 | 0.036 | compiled=5 | 1,854,959.0 | 288,348,000.0 | 100,881.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 290,163,430.0 | 281,667,965.0 | 294,238,881.0 | 4,743,797.9 | 5 | 31,768 | 31,483 | 31,252 | 0.016 | compiled=5 | 1,823,529.0 | 288,187,719.0 | 111,581.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 217,885,073.0 | 207,805,977.0 | 220,599,306.0 | 4,415,192.0 | 5 | 31,752 | 28,488 | 26,806 | 0.020 | compiled=5 | 1,797,289.0 | 216,014,035.0 | 191,421.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 217,457,921.0 | 210,867,200.0 | 218,995,039.0 | 2,883,203.4 | 5 | 31,752 | 28,417 | 26,735 | 0.013 | compiled=5 | 1,778,848.0 | 215,469,212.0 | 206,521.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 210,082,560.0 | 201,605,636.0 | 219,800,660.0 | 5,899,094.3 | 5 | 31,832 | 28,898 | 27,216 | 0.028 | compiled=5 | 1,725,430.0 | 208,301,960.0 | 109,531.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 217,519,119.0 | 212,201,160.0 | 221,045,749.0 | 2,935,625.7 | 5 | 31,832 | 28,827 | 27,145 | 0.013 | compiled=5 | 1,800,239.0 | 215,615,519.0 | 113,480.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 225,125,868.0 | 217,514,821.0 | 230,756,862.0 | 4,460,607.6 | 5 | 31,832 | 29,716 | 27,774 | 0.020 | compiled=5 | 1,831,488.0 | 221,687,611.0 | 192,331.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 222,629,486.0 | 215,127,080.0 | 228,743,694.0 | 4,951,425.5 | 5 | 31,792 | 29,644 | 27,702 | 0.022 | compiled=5 | 1,824,198.0 | 220,193,374.0 | 187,581.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,416,342.0 | 227,165,628.0 | 232,488,197.0 | 1,936,399.4 | 5 | 31,912 | 30,126 | 28,184 | 0.008 | compiled=5 | 1,850,919.0 | 229,464,322.0 | 101,260.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 230,853,059.0 | 216,696,224.0 | 240,360,009.0 | 8,661,384.1 | 5 | 31,872 | 30,054 | 28,112 | 0.038 | compiled=5 | 1,852,140.0 | 228,888,609.0 | 109,431.0 |
| `phone-palindrome-6` | `plain` | `pcrec_02902356_auto-caps-simdna` | 292,820,412.0 | 286,676,783.0 | 293,029,143.0 | 2,642,137.5 | 5 | 27,344 | 23,271 | 23,271 | 0.009 | compiled=5 | 1,772,489.0 | 291,041,523.0 | 102,150.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,440,195.0 | 189,423,051.0 | 197,308,879.0 | 3,154,488.2 | 5 | 27,424 | 23,079 | 23,079 | 0.016 | compiled=5 | 1,635,797.0 | 191,035,019.0 | 108,211.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 286,909,772.0 | 284,342,708.0 | 292,971,154.0 | 2,958,568.7 | 5 | 31,520 | 23,681 | 23,681 | 0.010 | compiled=5 | 1,756,910.0 | 283,972,687.0 | 170,021.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 197,501,923.0 | 194,509,948.0 | 205,505,406.0 | 3,898,770.5 | 5 | 27,504 | 23,489 | 23,489 | 0.020 | compiled=5 | 1,688,929.0 | 195,716,764.0 | 186,451.0 |
| `pwd-strength-chain` | `plain` | `pcrec_02902356_auto-caps-simdna` | 252,513,566.0 | 246,928,378.0 | 258,536,103.0 | 3,812,285.6 | 5 | 31,984 | 32,820 | 30,179 | 0.015 | compiled=5 | 1,920,739.0 | 250,441,875.0 | 191,851.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 242,853,379.0 | 235,803,237.0 | 256,657,053.0 | 7,366,398.6 | 5 | 31,984 | 32,748 | 30,107 | 0.030 | compiled=5 | 1,857,339.0 | 240,807,110.0 | 190,301.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 252,166,320.0 | 247,558,046.0 | 256,728,325.0 | 2,907,276.3 | 5 | 32,072 | 33,230 | 30,589 | 0.012 | compiled=5 | 2,072,981.0 | 250,139,710.0 | 110,460.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,093,300.0 | 248,625,802.0 | 261,012,708.0 | 4,155,399.4 | 5 | 32,064 | 33,158 | 30,517 | 0.016 | compiled=5 | 1,916,871.0 | 250,066,819.0 | 107,090.0 |
| `quoted-delim-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 218,731,857.0 | 204,654,862.0 | 221,932,213.0 | 6,360,569.8 | 5 | 31,768 | 26,057 | 25,364 | 0.029 | compiled=5 | 1,712,258.0 | 216,928,989.0 | 104,370.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 212,245,628.0 | 203,503,576.0 | 218,781,397.0 | 5,618,585.4 | 5 | 31,768 | 26,170 | 25,477 | 0.026 | compiled=5 | 1,684,268.0 | 210,604,730.0 | 105,360.0 |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 218,256,443.0 | 211,091,895.0 | 227,085,077.0 | 5,487,501.9 | 5 | 31,848 | 26,467 | 25,774 | 0.025 | compiled=5 | 1,731,679.0 | 216,449,923.0 | 100,201.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 212,089,601.0 | 204,518,212.0 | 218,962,457.0 | 5,492,645.9 | 5 | 31,848 | 26,580 | 25,887 | 0.026 | compiled=5 | 1,711,619.0 | 210,183,851.0 | 189,711.0 |
| `router-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 150,587,451.0 | 141,122,647.0 | 160,300,795.0 | 6,270,160.8 | 5 | 27,792 | 20,751 | 14,771 | 0.042 | compiled=5 | 1,982,569.0 | 148,723,912.0 | 102,691.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 160,820,168.0 | 153,542,685.0 | 161,812,563.0 | 3,307,435.2 | 5 | 27,936 | 23,579 | 16,972 | 0.021 (max is trial 1) | compiled=5 | 2,022,219.0 | 158,242,906.0 | 190,141.0 |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,646,675.0 | 151,350,314.0 | 159,827,466.0 | 3,019,717.9 | 5 | 27,872 | 21,136 | 15,156 | 0.019 | compiled=5 | 1,998,230.0 | 153,520,244.0 | 103,731.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 166,616,002.0 | 159,814,017.0 | 170,980,686.0 | 3,706,780.4 | 5 | 28,016 | 23,964 | 17,357 | 0.022 | compiled=5 | 2,048,921.0 | 164,465,621.0 | 188,521.0 |
| `tag-depth3-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 288,433,500.0 | 277,958,793.0 | 291,477,567.0 | 4,794,577.6 | 5 | 31,816 | 33,543 | 33,027 | 0.017 | compiled=5 | 1,853,588.0 | 286,449,823.0 | 110,011.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 286,343,192.0 | 281,916,582.0 | 288,441,001.0 | 2,421,918.9 | 5 | 31,816 | 33,656 | 33,140 | 0.008 | compiled=5 | 1,849,879.0 | 284,287,512.0 | 105,571.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 279,143,901.0 | 277,933,405.0 | 290,963,532.0 | 5,609,851.9 | 5 | 31,896 | 33,533 | 33,017 | 0.020 | compiled=5 | 1,904,469.0 | 276,962,450.0 | 101,480.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 289,224,643.0 | 283,378,413.0 | 290,346,130.0 | 2,716,034.3 | 5 | 31,896 | 33,646 | 33,130 | 0.009 | compiled=5 | 1,885,890.0 | 287,225,463.0 | 102,161.0 |
| `tag-pair-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 235,483,335.0 | 226,488,733.0 | 242,345,747.0 | 5,563,115.7 | 5 | 31,776 | 27,351 | 26,142 | 0.024 | compiled=5 | 1,782,258.0 | 233,492,516.0 | 211,751.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 231,911,019.0 | 226,272,912.0 | 240,164,277.0 | 4,755,950.5 | 5 | 31,776 | 27,464 | 26,255 | 0.021 | compiled=5 | 1,793,698.0 | 229,548,938.0 | 194,851.0 |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 228,149,184.0 | 227,365,890.0 | 237,879,976.0 | 3,981,190.1 | 5 | 31,856 | 27,621 | 26,412 | 0.017 | compiled=5 | 1,822,529.0 | 226,118,254.0 | 117,681.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 225,188,579.0 | 219,981,092.0 | 228,401,846.0 | 2,782,700.9 | 5 | 31,856 | 27,734 | 26,525 | 0.012 | compiled=5 | 1,811,610.0 | 223,144,218.0 | 103,490.0 |
| `trim-nested-star` | `plain` | `pcrec_02902356_auto-caps-simdna` | 205,170,163.0 | 194,203,813.0 | 205,709,646.0 | 4,936,153.9 | 5 | 27,512 | 23,591 | 23,360 | 0.024 | compiled=5 | 1,651,438.0 | 203,283,615.0 | 106,760.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,039,954.0 | 199,593,018.0 | 204,630,652.0 | 1,947,756.5 | 5 | 27,512 | 23,705 | 23,474 | 0.010 | compiled=5 | 1,651,167.0 | 201,290,756.0 | 104,570.0 |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 205,729,058.0 | 198,013,917.0 | 216,110,723.0 | 6,080,138.7 | 5 | 27,600 | 24,001 | 23,770 | 0.030 | compiled=5 | 1,674,869.0 | 203,894,178.0 | 99,740.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 202,835,242.0 | 198,129,368.0 | 208,889,594.0 | 4,148,207.2 | 5 | 31,696 | 24,115 | 23,884 | 0.020 | compiled=5 | 3,157,946.0 | 199,265,923.0 | 189,491.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,589,682.0 | 186,516,878.0 | 193,034,517.0 | 2,111,820.7 | 5 | 31,816 | 28,015 | 23,213 | 0.011 | compiled=5 | 1,913,739.0 | 187,574,873.0 | 103,051.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 195,997,671.0 | 191,905,032.0 | 199,909,889.0 | 2,539,046.0 | 5 | 31,904 | 29,703 | 24,687 | 0.013 | compiled=5 | 1,907,719.0 | 194,006,163.0 | 102,530.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 190,959,040.0 | 175,973,771.0 | 191,331,321.0 | 5,938,124.9 | 5 | 31,896 | 28,425 | 23,623 | 0.031 | compiled=5 | 1,931,670.0 | 188,940,739.0 | 106,521.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 197,231,323.0 | 182,078,113.0 | 207,902,598.0 | 8,267,618.3 | 5 | 31,984 | 30,113 | 25,097 | 0.042 | compiled=5 | 1,941,380.0 | 195,219,022.0 | 103,801.0 |
| `uuid-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 177,306,022.0 | 170,009,575.0 | 178,885,161.0 | 3,620,951.4 | 5 | 37,072 | 23,602 | 18,198 | 0.020 | compiled=5 | 1,735,369.0 | 175,458,523.0 | 112,130.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 173,594,354.0 | 163,611,851.0 | 182,161,508.0 | 6,060,446.7 | 5 | 37,032 | 23,424 | 18,020 | 0.035 | compiled=5 | 1,762,910.0 | 171,354,672.0 | 206,041.0 |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 174,285,582.0 | 169,472,237.0 | 178,957,247.0 | 3,555,707.6 | 5 | 37,152 | 23,987 | 18,583 | 0.020 | compiled=5 | 1,758,469.0 | 170,557,993.0 | 111,841.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 172,259,922.0 | 171,690,699.0 | 181,306,989.0 | 4,305,280.2 | 5 | 37,112 | 23,809 | 18,405 | 0.025 | compiled=5 | 1,767,319.0 | 170,324,702.0 | 190,241.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,159,039.0 | 146,948,134.0 | 154,338,498.0 | 2,683,977.6 | 5 | 27,792 | 19,408 | 14,411 | 0.018 | compiled=5 | 1,830,278.0 | 145,323,646.0 | 196,051.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,117,822.0 | 148,165,720.0 | 162,967,238.0 | 5,042,822.8 | 5 | 27,936 | 21,863 | 16,540 | 0.033 | compiled=5 | 3,548,726.0 | 151,482,235.0 | 116,011.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 141,977,024.0 | 132,982,006.0 | 156,532,840.0 | 8,168,175.6 | 5 | 27,872 | 19,793 | 14,796 | 0.058 | compiled=5 | 1,815,650.0 | 139,959,233.0 | 197,021.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 152,501,279.0 | 145,398,132.0 | 155,856,505.0 | 3,430,046.1 | 5 | 28,016 | 22,248 | 16,925 | 0.022 | compiled=5 | 1,853,189.0 | 150,551,778.0 | 185,651.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,325,668.0 | 150,784,142.0 | 157,123,131.0 | 2,229,834.1 | 5 | 28,112 | 28,359 | 16,094 | 0.015 (max is trial 1) | compiled=5 | 2,692,762.0 | 149,492,626.0 | 192,071.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,102,239.0 | 156,585,180.0 | 182,357,058.0 | 9,662,757.1 | 5 | 28,256 | 31,334 | 18,181 | 0.059 | compiled=5 | 2,778,193.0 | 160,616,687.0 | 100,730.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 164,388,091.0 | 159,578,156.0 | 168,819,134.0 | 3,075,374.7 | 5 | 28,200 | 28,744 | 16,479 | 0.019 | compiled=5 | 2,403,592.0 | 159,709,976.0 | 197,661.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,507,610.0 | 151,777,114.0 | 165,738,079.0 | 4,707,467.8 | 5 | 28,336 | 31,719 | 18,566 | 0.029 | compiled=5 | 2,469,663.0 | 157,844,716.0 | 190,961.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,291,179.0 | 144,234,151.0 | 156,807,730.0 | 4,158,631.4 | 5 | 27,784 | 23,172 | 14,850 | 0.028 | compiled=5 | 2,093,600.0 | 145,179,765.0 | 201,841.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,864,495.0 | 154,640,848.0 | 172,180,451.0 | 6,530,659.9 | 5 | 27,928 | 26,523 | 16,764 | 0.042 | compiled=5 | 2,319,021.0 | 153,340,953.0 | 193,821.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 154,316,868.0 | 152,176,047.0 | 158,551,721.0 | 2,276,312.7 | 5 | 27,864 | 23,557 | 15,235 | 0.015 (max is trial 1) | compiled=5 | 2,192,192.0 | 150,858,960.0 | 98,100.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 163,448,775.0 | 154,454,818.0 | 169,008,256.0 | 5,092,181.4 | 5 | 28,008 | 26,908 | 17,149 | 0.031 | compiled=5 | 2,306,752.0 | 161,040,483.0 | 99,371.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 149,682,477.0 | 143,503,517.0 | 158,570,648.0 | 5,971,834.3 | 5 | 27,792 | 19,410 | 14,413 | 0.040 | compiled=5 | 1,761,198.0 | 145,874,429.0 | 103,331.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,850,874.0 | 146,484,851.0 | 165,597,341.0 | 7,429,494.0 | 5 | 27,936 | 21,865 | 16,542 | 0.048 | compiled=5 | 1,830,449.0 | 153,621,964.0 | 207,861.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 145,705,433.0 | 141,916,152.0 | 156,413,588.0 | 5,871,445.4 | 5 | 27,872 | 19,795 | 14,798 | 0.040 | compiled=5 | 1,817,110.0 | 143,696,432.0 | 102,790.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,319,289.0 | 147,907,344.0 | 170,656,784.0 | 8,074,804.9 | 5 | 28,016 | 22,250 | 16,927 | 0.050 | compiled=5 | 1,867,009.0 | 158,228,088.0 | 207,171.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_02902356_auto-caps-simdna` | 154,503,939.0 | 137,125,829.0 | 157,145,741.0 | 7,847,919.6 | 5 | 27,792 | 20,788 | 14,693 | 0.051 | compiled=5 | 1,959,849.0 | 150,304,429.0 | 205,081.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,620,620.0 | 161,107,759.0 | 166,187,664.0 | 1,665,031.3 | 5 | 27,936 | 23,542 | 16,824 | 0.010 | compiled=5 | 1,997,599.0 | 161,517,271.0 | 190,871.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,799,847.0 | 152,288,897.0 | 160,544,611.0 | 2,800,748.8 | 5 | 27,872 | 21,173 | 15,078 | 0.018 | compiled=5 | 2,051,211.0 | 153,734,955.0 | 198,071.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 159,176,675.0 | 154,137,567.0 | 173,635,189.0 | 8,651,640.8 | 5 | 28,016 | 23,927 | 17,209 | 0.054 | compiled=5 | 2,041,791.0 | 154,790,331.0 | 168,191.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 576,388,570.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,247,714,708.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 599,052,326.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 16,177,238,265.0 | 16,072,557,246.0 | 16,352,970,525.0 | 99,749,615.2 | 5 | 150,848 | 484,520 (warned) | 482,896 | 0.006 | compiled=5 | 9,263,562,535.0 | 6,881,366,071.0 | 125,641.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,338,075.0 | 361,869,673.0 | 370,076,501.0 | 3,261,612.4 | 5 | 45,832 | 55,446 | 45,523 | 0.009 (max is trial 1) | compiled=5 | 2,342,761.0 | 359,831,154.0 | 117,050.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 350,317,570.0 | 334,239,615.0 | 351,187,503.0 | 6,503,231.7 | 5 | 45,464 | 53,885 | 43,962 | 0.019 | compiled=5 | 2,430,571.0 | 347,837,418.0 | 199,971.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 355,482,262.0 | 354,525,867.0 | 357,619,304.0 | 1,069,354.4 | 5 | 45,912 | 55,856 | 45,933 | 0.003 (max is trial 1) | compiled=5 | 2,418,352.0 | 352,655,447.0 | 112,301.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 354,186,585.0 | 347,461,800.0 | 368,102,188.0 | 6,983,903.8 | 5 | 45,544 | 54,295 | 44,372 | 0.020 | compiled=5 | 5,089,977.0 | 350,217,213.0 | 198,751.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 237,290,446.0 | 231,316,804.0 | 245,960,600.0 | 5,714,327.3 | 5 | 31,976 | 33,908 | 28,398 | 0.024 | compiled=5 | 2,090,641.0 | 232,811,032.0 | 192,921.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 246,142,221.0 | 233,371,684.0 | 252,066,191.0 | 7,422,745.9 | 5 | 32,072 | 34,980 | 29,045 | 0.030 (max is trial 1) | compiled=5 | 2,104,261.0 | 241,590,197.0 | 194,071.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 238,774,151.0 | 233,062,980.0 | 242,928,712.0 | 3,660,254.7 | 5 | 32,056 | 34,318 | 28,808 | 0.015 | compiled=5 | 2,106,262.0 | 234,279,607.0 | 186,491.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 242,796,850.0 | 240,454,808.0 | 257,606,969.0 | 6,212,508.8 | 5 | 32,152 | 35,390 | 29,455 | 0.026 | compiled=5 | 2,168,881.0 | 240,581,819.0 | 100,020.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,151,498.0 | 231,093,062.0 | 236,998,853.0 | 2,064,415.7 | 5 | 31,976 | 33,629 | 28,119 | 0.009 | compiled=5 | 2,043,771.0 | 229,879,126.0 | 109,001.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 240,890,644.0 | 231,783,847.0 | 245,950,040.0 | 4,830,727.1 | 5 | 32,072 | 34,698 | 28,763 | 0.020 | compiled=5 | 2,104,761.0 | 238,206,500.0 | 108,841.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 238,322,118.0 | 223,107,918.0 | 241,316,874.0 | 6,508,877.0 | 5 | 32,056 | 34,039 | 28,529 | 0.027 | compiled=5 | 2,071,711.0 | 236,041,946.0 | 196,521.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 235,316,541.0 | 232,788,909.0 | 239,980,356.0 | 3,156,258.0 | 5 | 32,152 | 35,108 | 29,173 | 0.013 | compiled=5 | 2,118,871.0 | 230,852,818.0 | 109,371.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 410,361,126.0 | 389,258,935.0 | 412,174,335.0 | 8,476,483.0 | 5 | 40,680 | 61,633 | 41,904 | 0.021 | compiled=5 | 5,137,327.0 | 400,032,002.0 | 193,601.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 414,227,586.0 | 403,260,857.0 | 415,743,663.0 | 4,791,466.9 | 5 | 40,776 | 66,276 | 43,404 | 0.012 | compiled=5 | 8,259,983.0 | 405,708,401.0 | 193,411.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 402,559,238.0 | 395,003,268.0 | 403,772,894.0 | 3,933,395.7 | 5 | 40,760 | 61,625 | 41,896 | 0.010 | compiled=5 | 5,240,027.0 | 397,185,030.0 | 192,291.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 413,638,316.0 | 408,501,260.0 | 421,366,147.0 | 4,814,889.4 | 5 | 40,856 | 66,268 | 43,396 | 0.012 | compiled=5 | 8,355,164.0 | 399,936,964.0 | 193,541.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,494,897.0 | 354,488,595.0 | 364,639,699.0 | 3,632,735.8 | 5 | 40,680 | 59,185 | 39,456 | 0.010 | compiled=5 | 4,989,566.0 | 356,707,876.0 | 193,201.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 375,793,157.0 | 365,474,932.0 | 386,638,593.0 | 7,675,001.2 | 5 | 40,776 | 63,828 | 40,956 | 0.020 | compiled=5 | 18,567,707.0 | 357,489,900.0 | 195,751.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 356,337,157.0 | 355,534,051.0 | 363,331,902.0 | 2,939,066.1 | 5 | 40,760 | 59,595 | 39,866 | 0.008 (max is trial 1) | compiled=5 | 5,036,676.0 | 351,087,969.0 | 111,201.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 374,586,381.0 | 367,149,442.0 | 378,222,820.0 | 3,659,155.2 | 5 | 40,856 | 64,238 | 41,366 | 0.010 (max is trial 1) | compiled=5 | 8,025,032.0 | 366,447,268.0 | 103,520.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_02902356_auto-caps-simdna` | 5,446,416,952.0 | 5,427,347,513.0 | 5,490,679,283.0 | 22,705,595.8 | 5 | 176,208 | 518,007 (warned) | 300,042 | 0.004 | compiled=5 | 599,367,599.0 | 4,848,712,922.0 | 104,491.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 6,440,923,029.0 | 6,428,778,045.0 | 6,483,773,802.0 | 23,122,738.7 | 5 | 180,400 | 527,624 (warned) | 301,462 | 0.004 | compiled=5 | 1,597,453,843.0 | 4,841,745,826.0 | 102,270.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 5,407,526,204.0 | 5,399,946,815.0 | 5,433,470,239.0 | 12,260,677.1 | 5 | 176,288 | 515,893 (warned) | 297,928 | 0.002 (max is trial 1) | compiled=5 | 598,747,135.0 | 4,808,573,168.0 | 185,171.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 6,435,887,458.0 | 6,416,894,449.0 | 6,446,040,812.0 | 10,199,385.2 | 5 | 180,480 | 525,510 (warned) | 299,348 | 0.002 | compiled=5 | 1,608,314,362.0 | 4,816,965,632.0 | 99,890.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 243,714,108.0 | 237,783,439.0 | 249,010,057.0 | 4,185,869.1 | 5 | 32,192 | 37,329 | 28,845 | 0.017 (max is trial 1) | compiled=5 | 2,326,392.0 | 241,362,536.0 | 103,890.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 251,426,368.0 | 246,983,875.0 | 261,178,300.0 | 5,232,178.0 | 5 | 32,328 | 40,673 | 30,370 | 0.021 | compiled=5 | 2,284,812.0 | 248,930,105.0 | 199,591.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 245,769,706.0 | 236,352,057.0 | 254,565,633.0 | 6,218,449.4 | 5 | 32,272 | 37,739 | 29,255 | 0.025 | compiled=5 | 2,206,582.0 | 243,428,285.0 | 107,291.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 255,352,138.0 | 248,197,630.0 | 256,506,914.0 | 3,516,393.8 | 5 | 32,408 | 41,083 | 30,780 | 0.014 (max is trial 1) | compiled=5 | 2,348,423.0 | 251,318,686.0 | 111,401.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_02902356_auto-caps-simdna` | 245,666,419.0 | 241,410,265.0 | 253,353,299.0 | 4,606,066.9 | 5 | 36,256 | 47,651 | 30,746 | 0.019 | compiled=5 | 3,191,957.0 | 242,187,321.0 | 187,331.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 258,180,164.0 | 245,346,406.0 | 260,020,843.0 | 5,863,146.8 | 5 | 36,352 | 50,184 | 32,283 | 0.023 | compiled=5 | 3,304,887.0 | 254,810,406.0 | 188,071.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 246,298,029.0 | 241,161,793.0 | 246,921,993.0 | 2,337,393.4 | 5 | 36,336 | 46,133 | 29,228 | 0.009 | compiled=5 | 3,264,637.0 | 242,891,622.0 | 106,740.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 245,753,607.0 | 242,658,780.0 | 257,675,090.0 | 5,610,894.7 | 5 | 36,432 | 48,666 | 30,765 | 0.023 | compiled=5 | 3,444,708.0 | 242,133,918.0 | 203,721.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 392,491,672.0 | 384,915,983.0 | 398,643,295.0 | 4,999,999.4 | 5 | 44,320 | 57,974 | 27,864 | 0.013 | compiled=5 | 4,485,413.0 | 387,920,869.0 | 103,981.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 399,138,288.0 | 391,772,370.0 | 407,136,649.0 | 5,635,371.5 | 5 | 40,320 | 61,344 | 29,401 | 0.014 | compiled=5 | 4,615,554.0 | 394,447,313.0 | 106,991.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 336,702,373.0 | 335,249,515.0 | 340,640,425.0 | 1,928,634.0 | 5 | 40,304 | 56,824 | 26,714 | 0.006 (max is trial 1) | compiled=5 | 4,597,454.0 | 330,839,902.0 | 110,390.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 331,160,074.0 | 322,041,836.0 | 338,216,631.0 | 5,141,245.5 | 5 | 40,400 | 60,192 | 28,249 | 0.016 | compiled=5 | 4,680,505.0 | 326,256,228.0 | 194,371.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_02902356_auto-caps-simdna` | 283,575,716.0 | 276,111,877.0 | 295,733,599.0 | 6,886,383.7 | 5 | 52,544 | 105,110 | 33,760 | 0.024 | compiled=5 | 7,559,209.0 | 268,870,880.0 | 126,821.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 295,760,879.0 | 293,203,976.0 | 302,838,666.0 | 3,229,025.8 | 5 | 52,632 | 112,465 | 35,304 | 0.011 (max is trial 1) | compiled=5 | 8,017,302.0 | 287,496,876.0 | 177,341.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 288,851,213.0 | 286,335,719.0 | 298,927,194.0 | 4,699,217.9 | 5 | 52,624 | 105,222 | 33,872 | 0.016 | compiled=5 | 7,793,201.0 | 278,619,609.0 | 101,430.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 301,207,487.0 | 290,018,528.0 | 311,676,991.0 | 8,046,884.9 | 5 | 52,720 | 112,577 | 35,416 | 0.027 | compiled=5 | 8,194,053.0 | 282,319,668.0 | 189,221.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_02902356_auto-caps-simdna` | 562,562,478.0 | 561,219,771.0 | 594,114,281.0 | 12,774,766.0 | 5 | 208,656 | 553,671 (warned) | 44,404 | 0.023 | compiled=5 | 57,414,179.0 | 505,252,319.0 | 100,781.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 584,255,100.0 | 578,788,762.0 | 587,614,919.0 | 3,458,060.0 | 5 | 212,840 | 568,461 (warned) | 45,692 | 0.006 | compiled=5 | 64,427,765.0 | 519,153,422.0 | 100,701.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 541,180,843.0 | 533,740,605.0 | 551,204,506.0 | 6,426,046.1 | 5 | 208,736 | 550,723 (warned) | 41,457 | 0.012 | compiled=5 | 57,677,702.0 | 480,575,836.0 | 105,230.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 557,952,482.0 | 550,162,480.0 | 578,441,028.0 | 9,916,244.1 | 5 | 212,928 | 565,513 (warned) | 42,745 | 0.018 (max is trial 1) | compiled=5 | 64,901,769.0 | 493,046,832.0 | 98,530.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,340,903.0 | 145,899,509.0 | 162,439,555.0 | 5,968,137.6 | 5 | 27,792 | 21,325 | 15,618 | 0.039 | compiled=5 | 2,010,979.0 | 149,233,544.0 | 193,391.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 167,827,129.0 | 164,869,317.0 | 169,465,149.0 | 1,605,057.6 | 5 | 27,936 | 23,569 | 16,962 | 0.010 | compiled=5 | 1,989,980.0 | 165,754,860.0 | 104,680.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 163,503,026.0 | 153,635,185.0 | 168,884,914.0 | 5,683,053.5 | 5 | 27,872 | 21,710 | 16,003 | 0.035 | compiled=5 | 4,104,931.0 | 158,894,222.0 | 188,701.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 169,219,946.0 | 162,635,801.0 | 171,852,230.0 | 3,620,432.4 | 5 | 28,016 | 23,954 | 17,347 | 0.021 | compiled=5 | 2,031,021.0 | 166,996,684.0 | 192,241.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 173,031,084.0 | 163,323,360.0 | 174,495,752.0 | 4,072,581.7 | 5 | 27,936 | 23,175 | 17,394 | 0.024 | compiled=5 | 1,886,598.0 | 171,041,485.0 | 112,610.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,294,120.0 | 158,513,327.0 | 168,208,792.0 | 3,885,366.0 | 5 | 27,936 | 22,747 | 16,966 | 0.024 | compiled=5 | 1,919,719.0 | 158,960,809.0 | 198,811.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 168,192,471.0 | 166,239,750.0 | 170,815,243.0 | 1,665,586.3 | 5 | 28,016 | 23,560 | 17,779 | 0.010 | compiled=5 | 1,932,861.0 | 165,074,704.0 | 100,380.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 161,904,138.0 | 159,115,323.0 | 173,407,988.0 | 5,698,402.3 | 5 | 28,016 | 23,132 | 17,351 | 0.035 | compiled=5 | 1,928,360.0 | 159,995,298.0 | 106,991.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,019,948.0 | 212,639,978.0 | 235,379,945.0 | 7,305,895.4 | 5 | 31,968 | 31,978 | 27,144 | 0.033 (max is trial 1) | compiled=5 | 1,965,579.0 | 220,842,927.0 | 115,001.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 226,549,874.0 | 219,254,800.0 | 234,221,279.0 | 4,742,685.9 | 5 | 32,064 | 33,457 | 28,393 | 0.021 (max is trial 1) | compiled=5 | 1,975,149.0 | 224,481,324.0 | 103,061.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 223,040,067.0 | 217,096,697.0 | 232,911,679.0 | 5,586,208.7 | 5 | 32,048 | 32,388 | 27,554 | 0.025 | compiled=5 | 1,971,000.0 | 220,967,397.0 | 100,720.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 222,987,087.0 | 210,595,903.0 | 235,521,563.0 | 8,528,029.1 | 5 | 32,144 | 33,867 | 28,803 | 0.038 | compiled=5 | 2,326,533.0 | 218,825,166.0 | 190,581.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 147,010,445.0 | 141,100,084.0 | 147,544,529.0 | 2,423,674.6 | 5 | 27,616 | 15,572 | 13,215 | 0.016 | compiled=5 | 1,646,539.0 | 143,670,578.0 | 192,061.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 144,960,004.0 | 140,811,513.0 | 148,829,875.0 | 2,763,951.6 | 5 | 27,616 | 15,395 | 13,038 | 0.019 | compiled=5 | 1,627,789.0 | 142,254,310.0 | 199,671.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 148,801,479.0 | 143,935,513.0 | 152,373,568.0 | 3,016,664.7 | 5 | 27,696 | 15,957 | 13,600 | 0.020 | compiled=5 | 1,677,329.0 | 145,354,851.0 | 101,630.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 149,366,411.0 | 137,965,673.0 | 150,042,636.0 | 5,652,151.3 | 5 | 27,696 | 15,780 | 13,423 | 0.038 | compiled=5 | 1,662,109.0 | 145,870,874.0 | 191,991.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 319,124,980.0 | 306,564,465.0 | 320,182,985.0 | 5,061,663.7 | 5 | 40,960 | 45,787 | 40,759 | 0.016 | compiled=5 | 2,161,951.0 | 316,850,578.0 | 114,100.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 309,255,209.0 | 307,068,898.0 | 315,302,491.0 | 3,400,535.3 | 5 | 40,752 | 44,970 | 39,942 | 0.011 | compiled=5 | 2,177,061.0 | 304,925,337.0 | 196,301.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 320,728,600.0 | 315,713,733.0 | 321,293,822.0 | 2,058,866.8 | 5 | 41,040 | 46,197 | 41,169 | 0.006 | compiled=5 | 2,177,281.0 | 318,483,758.0 | 112,420.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 315,156,280.0 | 298,230,211.0 | 317,045,830.0 | 7,118,462.4 | 5 | 40,832 | 45,380 | 40,352 | 0.023 | compiled=5 | 2,157,271.0 | 312,908,359.0 | 194,371.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 209,529,840.0 | 207,844,643.0 | 216,443,617.0 | 2,996,674.5 | 5 | 32,064 | 28,091 | 25,547 | 0.014 | compiled=5 | 1,846,170.0 | 207,646,571.0 | 112,190.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,430,178.0 | 198,829,524.0 | 211,917,983.0 | 4,981,310.1 | 5 | 31,984 | 27,831 | 25,287 | 0.024 | compiled=5 | 3,627,409.0 | 199,592,999.0 | 111,661.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 204,531,121.0 | 203,244,104.0 | 218,204,242.0 | 5,746,014.5 | 5 | 32,152 | 28,501 | 25,957 | 0.028 | compiled=5 | 1,830,760.0 | 201,472,325.0 | 194,271.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 206,766,243.0 | 201,255,173.0 | 211,828,419.0 | 3,477,737.3 | 5 | 32,064 | 28,241 | 25,697 | 0.017 | compiled=5 | 1,792,380.0 | 204,781,332.0 | 192,531.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 248,667,125.0 | 247,389,987.0 | 249,350,336.0 | 713,337.6 | 5 | 36,560 | 47,570 | 22,252 | 0.003 (max is trial 1) | compiled=5 | 3,139,197.0 | 244,844,735.0 | 114,061.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 254,578,446.0 | 237,743,136.0 | 260,078,933.0 | 8,557,911.3 | 5 | 36,704 | 50,547 | 23,956 | 0.034 | compiled=5 | 3,530,438.0 | 251,130,047.0 | 105,861.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 248,326,361.0 | 238,250,497.0 | 249,236,585.0 | 4,472,443.1 | 5 | 36,640 | 47,955 | 22,637 | 0.018 | compiled=5 | 3,285,937.0 | 244,840,022.0 | 189,961.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 259,845,901.0 | 255,422,627.0 | 261,135,527.0 | 2,279,492.1 | 5 | 36,784 | 50,932 | 24,341 | 0.009 | compiled=5 | 7,380,888.0 | 252,232,171.0 | 200,181.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_02902356_auto-caps-simdna` | 229,191,262.0 | 223,914,035.0 | 232,111,759.0 | 2,803,121.6 | 5 | 85,736 | 227,567 | 19,601 | 0.012 (max is trial 1) | compiled=5 | 14,409,165.0 | 212,936,348.0 | 202,591.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 237,999,609.0 | 227,990,656.0 | 264,816,148.0 | 12,497,419.2 | 5 | 89,968 | 237,398 | 21,577 | 0.053 | compiled=5 | 15,698,432.0 | 219,954,604.0 | 114,691.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 227,858,973.0 | 219,596,770.0 | 231,820,324.0 | 4,609,307.4 | 5 | 85,816 | 227,952 | 19,986 | 0.020 | compiled=5 | 14,481,726.0 | 207,827,688.0 | 97,880.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 244,786,962.0 | 243,537,725.0 | 246,408,529.0 | 1,010,592.9 | 5 | 94,152 | 237,783 | 21,962 | 0.004 (max is trial 1) | compiled=5 | 15,868,433.0 | 228,106,624.0 | 107,051.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,777,328.0 | 179,414,043.0 | 205,820,181.0 | 10,879,652.8 | 5 | 36,480 | 57,983 | 17,583 | 0.057 | compiled=5 | 4,437,913.0 | 185,234,484.0 | 112,400.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 201,473,079.0 | 199,305,187.0 | 208,614,054.0 | 3,890,559.5 | 5 | 36,624 | 61,762 | 19,374 | 0.019 (max is trial 1) | compiled=5 | 5,971,871.0 | 196,218,491.0 | 190,701.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 197,212,723.0 | 179,841,132.0 | 198,797,561.0 | 7,137,369.9 | 5 | 36,560 | 58,368 | 17,968 | 0.036 | compiled=5 | 4,652,984.0 | 192,459,468.0 | 102,671.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 209,772,328.0 | 201,704,887.0 | 215,720,838.0 | 4,850,209.2 | 5 | 36,704 | 62,147 | 19,759 | 0.023 | compiled=5 | 5,370,559.0 | 202,682,452.0 | 108,201.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_02902356_auto-caps-simdna` | 163,497,120.0 | 153,596,240.0 | 175,232,262.0 | 7,735,900.2 | 5 | 32,152 | 36,533 | 15,366 | 0.047 | compiled=5 | 3,220,967.0 | 160,079,823.0 | 103,531.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 174,634,920.0 | 173,275,822.0 | 183,728,935.0 | 4,388,530.0 | 5 | 32,296 | 39,557 | 17,378 | 0.025 | compiled=5 | 3,343,477.0 | 170,707,648.0 | 101,411.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 164,354,721.0 | 163,390,854.0 | 178,287,983.0 | 5,613,728.5 | 5 | 32,232 | 36,918 | 15,751 | 0.034 (max is trial 1) | compiled=5 | 3,878,701.0 | 160,239,659.0 | 101,500.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 174,434,564.0 | 166,043,870.0 | 187,238,611.0 | 7,102,694.2 | 5 | 32,376 | 39,942 | 17,763 | 0.041 | compiled=5 | 3,920,940.0 | 170,830,455.0 | 194,742.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_02902356_auto-caps-simdna` | 1,458,152,128.0 | 1,429,600,059.0 | 1,482,915,127.0 | 19,768,038.2 | 5 | 680,448 | 394,628 (warned) | 100,148 | 0.014 | compiled=5 | 12,683,376.0 | 1,442,632,247.0 | 527,822.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 1,390,345,675.0 | 1,368,604,382.0 | 1,399,114,831.0 | 10,678,984.5 | 5 | 659,912 | 401,834 (warned) | 102,298 | 0.008 | compiled=5 | 13,089,838.0 | 1,377,098,256.0 | 284,651.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 1,470,740,970.0 | 1,428,762,891.0 | 1,496,714,667.0 | 29,126,945.7 | 5 | 680,528 | 395,013 (warned) | 100,533 | 0.020 | compiled=5 | 12,779,837.0 | 1,457,515,122.0 | 281,232.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 1,377,330,262.0 | 1,368,977,968.0 | 1,431,779,785.0 | 22,881,074.1 | 5 | 659,992 | 402,219 (warned) | 102,683 | 0.017 (max is trial 1) | compiled=5 | 13,217,470.0 | 1,363,581,160.0 | 515,073.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_02902356_auto-caps-simdna` | 158,663,416.0 | 155,513,879.0 | 160,131,514.0 | 1,680,890.4 | 5 | 27,792 | 21,230 | 15,318 | 0.011 | compiled=5 | 2,091,171.0 | 155,211,357.0 | 210,731.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 172,289,356.0 | 167,989,804.0 | 178,167,247.0 | 3,366,296.1 | 5 | 27,936 | 23,837 | 17,407 | 0.020 (max is trial 1) | compiled=5 | 2,120,791.0 | 169,968,264.0 | 172,811.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 161,472,745.0 | 149,285,771.0 | 163,167,325.0 | 5,070,347.3 | 5 | 27,872 | 21,615 | 15,703 | 0.031 | compiled=5 | 2,128,982.0 | 159,246,934.0 | 192,731.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 163,397,456.0 | 157,348,524.0 | 173,141,088.0 | 6,123,295.4 | 5 | 28,016 | 24,222 | 17,792 | 0.037 | compiled=5 | 2,489,543.0 | 161,142,703.0 | 106,440.0 |
| `winpath-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 135,167,833.0 | 134,530,291.0 | 148,679,943.0 | 6,699,706.4 | 5 | 27,576 | 14,961 | 12,878 | 0.050 | compiled=5 | 1,605,008.0 | 133,360,644.0 | 194,471.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 140,141,629.0 | 125,986,237.0 | 148,527,122.0 | 8,241,331.0 | 5 | 27,536 | 14,784 | 12,701 | 0.059 | compiled=5 | 1,630,418.0 | 138,396,580.0 | 104,720.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 144,731,688.0 | 132,892,935.0 | 155,063,402.0 | 8,586,719.3 | 5 | 27,656 | 15,346 | 13,263 | 0.059 (max is trial 1) | compiled=5 | 1,630,429.0 | 143,028,419.0 | 188,081.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 144,719,947.0 | 136,902,067.0 | 146,225,506.0 | 3,461,635.4 | 5 | 27,616 | 15,169 | 13,086 | 0.024 | compiled=5 | 1,646,828.0 | 143,005,988.0 | 99,991.0 |

