# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, since=2026-09-27T00:00:00Z, until=2026-09-27T02:00:00Z, testee=pcrec_02902356_auto-caps-simdna, testee=pcrec_02902356_auto-caps-simdna_noreqbyte
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 47.37% (`pcrec_02902356_auto-caps-simdna_noreqbyte` / `logparse-atomic` / `large-subject-throughput`)
    - `capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z` (store/records/capability@0.1/pcrec_02902356_auto-caps-simdna/capability@0.1__pcrec_02902356_auto-caps-simdna__budu-ryzen1600__20260927T003406Z.jsonl) — agreement: agree (0 of 124 groups; 2 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_02902356_auto-caps-simdna_noreqbyte__budu-ryzen1600__20260927T010719Z` (store/records/capability@0.1/pcrec_02902356_auto-caps-simdna_noreqbyte/capability@0.1__pcrec_02902356_auto-caps-simdna_noreqbyte__budu-ryzen1600__20260927T010719Z.jsonl) — agreement: agree (0 of 124 groups; 4 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
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

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,111,913.6 | 3.7144 | 5,106,258.7 | 5,121,759.8 | 5,418.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 5,493,170.1 | 3.9914 | 5,483,403.2 | 5,495,737.6 | 4,933.7 | 1.075x | 1.075x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,899,201.4 | 3.7186 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,184,710.1 | 3.9909 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 970,648.5 | 3.7027 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,045,673.6 | 3.9889 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 242,843.5 | 3.7055 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 261,209.9 | 3.9857 |

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007.9 | 1,003.6 | 1,044.4 | 15.4 | 1.000x | 1.000x | 75 | 13.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 6,496.6 | 6,362.6 | 6,582.3 | 79.1 | 6.446x | 6.446x | 75 | 86.6 | 8.9 | 100% |

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 18.1 | 0.0000 | 18.0 | 19.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 18.3 | 0.0000 | 18.2 | 18.4 | 0.1 | 1.008x | 1.008x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.1 | 0.0001 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 540.5 | 528.5 | 543.9 | 5.6 | 1.000x | 1.000x | 75 | 7.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 543.4 | 532.4 | 544.0 | 4.9 | 1.005x | 1.005x | 75 | 7.2 | 8.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 72.0 | 0.0001 | 71.9 | 72.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 73.8 | 0.0001 | 72.1 | 73.9 | 0.8 | 1.024x | 1.024x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 23.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 24.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 24.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 24.1 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 24.7 | 0.0004 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,879.2 | 1,878.6 | 1,879.8 | 0.5 | 1.000x | 1.000x | 75 | 25.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,879.9 | 1,878.4 | 1,892.4 | 5.2 | 1.000x | 1.000x | 75 | 25.1 | 8.9 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 605,668.9 | 0.4401 | 604,060.4 | 611,144.6 | 2,919.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 617,517.9 | 0.4487 | 602,272.9 | 641,063.0 | 14,129.0 | 1.020x | 1.020x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 467,033.4 | 0.4454 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 480,003.4 | 0.4578 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 109,588.5 | 0.4180 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 111,522.2 | 0.4254 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 27,888.8 | 0.4256 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 27,987.3 | 0.4271 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 892.0 | 888.1 | 898.7 | 3.4 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 892.1 | 888.4 | 896.2 | 2.6 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 607,496.7 | 0.4414 | 597,509.1 | 615,428.4 | 6,729.6 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 616,089.6 | 0.4477 | 606,543.5 | 627,601.6 | 7,014.8 | 1.014x | 1.014x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 467,248.8 | 0.4456 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 475,478.0 | 0.4535 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 110,680.2 | 0.4222 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 112,223.8 | 0.4281 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 29,073.8 | 0.4436 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 27,465.8 | 0.4191 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 893.5 | 892.0 | 895.7 | 1.2 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 894.1 | 890.3 | 895.0 | 1.9 | 1.001x | 1.001x | 75 | 11.9 | 8.9 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 11,169,592.7 | 8.1159 | 11,167,219.2 | 11,253,022.2 | 32,781.6 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 11,177,376.1 | 8.1216 | 11,170,888.2 | 11,189,859.5 | 7,265.6 | 1.001x | 1.001x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8,509,284.2 | 8.1151 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8,515,801.3 | 8.1213 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,126,560.1 | 8.1122 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 2,128,742.1 | 8.1205 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 534,760.1 | 8.1598 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 534,568.5 | 8.1569 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 5,116.4 | 5,090.6 | 5,122.5 | 12.4 | 1.000x | 1.000x | 75 | 68.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 5,149.2 | 5,134.2 | 5,160.8 | 9.9 | 1.006x | 1.006x | 75 | 68.7 | 8.9 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 30.8 | 0.0000 | 30.7 | 31.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.7 | 30.9 | 0.1 | 1.001x | 1.001x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0002 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 838.8 | 822.2 | 839.2 | 6.6 | 1.000x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 839.6 | 837.6 | 840.2 | 1.1 | 1.001x | 1.001x | 75 | 11.2 | 8.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 25,438,453.7 | 18.4838 | 25,264,260.2 | 26,138,014.4 | 308,079.6 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 25,503,013.6 | 18.5307 | 25,288,971.6 | 25,759,783.9 | 151,240.0 | 1.003x | 1.003x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 19,380,938.1 | 18.4831 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 19,433,711.7 | 18.5334 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,837,275.2 | 18.4527 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,847,582.9 | 18.4921 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,203,012.2 | 18.3565 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,204,148.0 | 18.3738 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 20,878.6 | 20,823.4 | 21,125.2 | 105.1 | 1.000x | 1.000x | 75 | 278.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20,936.5 | 20,893.9 | 20,969.1 | 26.1 | 1.003x | 1.003x | 75 | 279.2 | 8.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,135.1 | 0.0168 | 23,117.6 | 23,139.9 | 9.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 13,419,269.9 | 9.7506 | 13,414,372.8 | 13,467,170.7 | 19,813.0 | 580.041x | 580.041x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,635.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10,237,099.7 | 9.7629 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,385.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 2,558,668.0 | 9.7605 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 626,703.2 | 9.5627 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,174.7 | 1,170.4 | 1,177.6 | 2.8 | 1.000x | 1.000x | 75 | 15.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 10,833.2 | 10,750.6 | 10,844.4 | 38.0 | 9.222x | 9.222x | 75 | 144.4 | 8.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 977.5 | 0.0007 | 972.3 | 982.7 | 3.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 978.9 | 0.0007 | 971.3 | 982.2 | 3.9 | 1.001x | 1.001x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 229.9 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 229.1 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 456.8 | 0.0017 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 458.8 | 0.0018 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 289.3 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 289.8 | 0.0044 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,517.7 | 10,475.0 | 10,575.5 | 32.7 | 1.000x | 1.000x | 75 | 140.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 10,539.4 | 10,500.5 | 10,650.1 | 52.0 | 1.002x | 1.002x | 75 | 140.5 | 8.9 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 46.6 | 0.0000 | 45.6 | 47.9 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 50.0 | 0.0000 | 48.0 | 51.3 | 1.1 | 1.073x | 1.073x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 18.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 15.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 15.2 | 0.0002 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,368.9 | 1,356.1 | 1,378.0 | 7.0 | 1.000x | 1.000x | 75 | 18.3 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,371.6 | 1,363.4 | 1,372.8 | 4.0 | 1.002x | 1.002x | 75 | 18.3 | 8.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 12,025.3 | 0.0087 | 11,627.5 | 12,158.6 | 227.0 | 1.000x | 1.000x | **dominated**: `t-64k` is 90.0% of this set |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,094.3 | 0.0088 | 11,897.6 | 12,169.4 | 93.1 | 1.006x | 1.006x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,154.6 | 0.0011 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,223.5 | 0.0012 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 45.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 45.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10,828.9 | 0.1652 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,825.6 | 0.1652 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 255,493.9 | 0.1856 | 255,315.2 | 255,621.0 | 98.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 292,677.0 | 0.2127 | 292,463.3 | 292,756.4 | 118.9 | 1.146x | 1.146x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 202,386.3 | 0.1930 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 228,544.5 | 0.2180 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 44,401.9 | 0.1694 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 52,563.0 | 0.2005 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8,685.4 | 0.1325 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 11,464.0 | 0.1749 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.1 | 686.5 | 687.9 | 0.5 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 816.1 | 813.5 | 822.7 | 3.2 | 1.188x | 1.188x | 75 | 10.9 | 8.9 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,790,268.6 | 1.3008 | 1,787,226.8 | 1,790,764.2 | 1,621.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,888,100.8 | 1.3719 | 1,884,218.3 | 1,910,982.0 | 10,074.1 | 1.055x | 1.055x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,369,502.4 | 1.3061 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,446,031.4 | 1.3790 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 337,560.1 | 1.2877 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 356,011.0 | 1.3581 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 82,314.1 | 1.2560 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 86,264.5 | 1.3163 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,638.9 | 1,630.8 | 1,652.6 | 8.2 | 1.000x | 1.000x | 75 | 21.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,458.6 | 2,450.2 | 2,469.7 | 7.0 | 1.500x | 1.500x | 75 | 32.8 | 8.9 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 23,121.4 | 0.0168 | 23,116.8 | 23,133.2 | 5.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,126.4 | 0.0168 | 23,110.3 | 23,158.8 | 18.7 | 1.000x | 1.000x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,631.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,640.7 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,383.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.4 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,109.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,104.2 | 0.0168 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 666.9 | 665.0 | 667.6 | 0.9 | 1.000x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.0 | 662.5 | 667.1 | 1.8 | 1.000x | 1.000x | 75 | 8.9 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 483,001.4 | 0.3510 | 482,738.5 | 483,115.6 | 137.0 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 483,087.0 | 0.3510 | 482,752.7 | 483,416.5 | 210.9 | 1.000x | 1.000x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 368,091.9 | 0.3510 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 368,071.8 | 0.3510 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 91,727.5 | 0.3499 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,954.1 | 0.3508 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 22,975.3 | 0.3506 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,066.0 | 0.3520 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,063.9 | 1,061.2 | 1,072.8 | 4.0 | 1.000x | 1.000x | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,067.0 | 1,062.7 | 1,070.6 | 2.8 | 1.003x | 1.003x | 75 | 14.2 | 8.9 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 13.8 | 0.0000 | 13.7 | 13.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 13.8 | 0.0000 | 13.7 | 14.0 | 0.1 | 1.002x | 1.002x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.6 | 0.0001 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 412.1 | 405.6 | 422.5 | 5.6 | 1.000x | 1.000x | 75 | 5.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 412.7 | 412.0 | 417.3 | 1.9 | 1.001x | 1.001x | 75 | 5.5 | 8.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687,715.0 | 0.4997 | 685,324.2 | 688,495.4 | 1,111.0 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 688,024.6 | 0.4999 | 687,109.5 | 688,551.5 | 634.6 | 1.000x | 1.000x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 531,816.0 | 0.5072 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 531,629.0 | 0.5070 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 126,911.4 | 0.4841 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 127,206.0 | 0.4853 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 28,894.0 | 0.4409 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 29,011.4 | 0.4427 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 765.2 | 763.0 | 766.3 | 1.2 | 1.000x | 1.000x | 75 | 10.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 766.0 | 764.1 | 769.5 | 2.3 | 1.001x | 1.001x | 75 | 10.2 | 8.9 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 30.8 | 0.0000 | 30.8 | 31.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 31.0 | 0.0 | 1.001x | 1.001x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.7 | 0.0002 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 807.7 | 807.1 | 809.8 | 1.1 | 1.000x | 1.000x | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 807.7 | 807.4 | 819.8 | 4.8 | 1.000x | 1.000x | 75 | 10.8 | 8.9 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 31.3 | 0.0000 | 31.2 | 31.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 31.3 | 0.0000 | 31.2 | 31.5 | 0.1 | 1.000x | 1.000x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.9 | 0.0002 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 807.9 | 805.9 | 809.5 | 1.2 | 1.000x | 1.000x | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 808.9 | 806.9 | 835.2 | 10.8 | 1.001x | 1.001x | 75 | 10.8 | 8.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 23,133.0 | 0.0168 | 23,125.2 | 23,143.5 | 6.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,167.0 | 0.0168 | 23,130.1 | 23,191.5 | 23.2 | 1.001x | 1.001x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,636.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,382.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,391.4 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,108.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.0 | 0.0169 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 679.2 | 679.0 | 679.5 | 0.2 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 686.2 | 685.8 | 687.0 | 0.4 | 1.010x | 1.010x | 75 | 9.1 | 8.9 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,145.5 | 0.0168 | 23,119.7 | 23,148.1 | 11.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 7,786,811.0 | 5.6580 | 7,777,931.9 | 7,801,449.4 | 8,774.8 | 336.428x | 336.428x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,651.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 5,933,718.6 | 5.6588 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,375.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,482,074.1 | 5.6537 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 371,018.4 | 5.6613 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,582.0 | 1,577.0 | 1,646.4 | 31.4 | 1.000x | 1.000x | 75 | 21.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 9,280.2 | 9,273.8 | 9,855.0 | 229.8 | 5.866x | 5.866x | 75 | 123.7 | 8.9 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 28.9 | 0.0000 | 28.7 | 40.7 | 4.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 29.2 | 0.0000 | 29.0 | 29.3 | 0.1 | 1.009x | 1.009x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 9.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 9.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 9.8 | 0.0001 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 815.5 | 801.6 | 827.1 | 8.1 | 1.000x | 1.000x | 75 | 10.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 817.4 | 804.5 | 819.9 | 5.6 | 1.002x | 1.002x | 75 | 10.9 | 8.9 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 29.9 | 0.0000 | 29.9 | 30.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 0.0000 | 29.8 | 30.1 | 0.1 | 1.003x | 1.003x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 9.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.0 | 0.0002 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 885.9 | 878.4 | 889.3 | 4.3 | 1.000x | 1.000x | 75 | 11.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 887.4 | 868.5 | 891.6 | 8.5 | 1.002x | 1.002x | 75 | 11.8 | 8.9 | 100% |

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 6,540,084.7 | 4.7521 | 6,532,342.2 | 6,545,675.0 | 4,918.8 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,541,533.0 | 4.7531 | 6,504,044.4 | 6,547,064.1 | 19,609.1 | 1.000x | 1.000x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,988,587.9 | 4.7575 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4,988,794.4 | 4.7577 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,241,665.5 | 4.7366 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,239,933.8 | 4.7300 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 309,466.3 | 4.7221 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 309,249.6 | 4.7188 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 6,705.9 | 6,535.9 | 6,895.6 | 150.4 | 1.000x | 1.000x | 75 | 89.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 6,834.9 | 6,731.0 | 6,886.4 | 59.9 | 1.019x | 1.019x | 75 | 91.1 | 8.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 223.0 | 0.0002 | 222.8 | 223.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 223.7 | 0.0002 | 222.7 | 224.4 | 0.7 | 1.003x | 1.003x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 58.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 58.5 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 95.1 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 95.5 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 69.3 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 69.4 | 0.0011 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 12,153.5 | 12,087.6 | 12,181.7 | 31.2 | 1.000x | 1.000x | 75 | 162.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,153.6 | 12,102.8 | 12,179.4 | 31.6 | 1.000x | 1.000x | 75 | 162.0 | 8.9 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 10,009,198.3 | 7.2728 | 9,626,459.8 | 10,043,193.5 | 157,861.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,034,269.2 | 7.2910 | 9,949,749.5 | 10,058,744.9 | 37,707.7 | 1.003x | 1.003x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 7,648,989.0 | 7.2946 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 7,643,126.9 | 7.2891 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,858,055.2 | 7.0879 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,914,759.2 | 7.3042 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 470,075.8 | 7.1728 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 476,629.0 | 7.2728 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,870.9 | 10,805.1 | 11,349.0 | 209.5 | 1.000x | 1.000x | 75 | 144.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 11,143.2 | 10,716.1 | 11,287.6 | 227.9 | 1.025x | 1.025x | 75 | 148.6 | 8.9 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 343,378.8 | 0.2495 | 343,154.1 | 343,424.4 | 116.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 392,255.2 | 0.2850 | 391,762.3 | 392,496.1 | 272.1 | 1.142x | 1.142x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 263,947.0 | 0.2517 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 300,760.2 | 0.2868 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 64,523.6 | 0.2461 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 74,229.7 | 0.2832 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 14,750.4 | 0.2251 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,040.0 | 0.2600 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 687.4 | 687.2 | 687.9 | 0.2 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 767.8 | 767.1 | 772.0 | 1.8 | 1.117x | 1.117x | 75 | 10.2 | 8.9 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,140.0 | 0.0168 | 23,118.8 | 23,157.6 | 14.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,478,771.2 | 3.2543 | 4,475,978.7 | 4,480,329.9 | 1,785.4 | 193.551x | 193.551x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,650.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,411,644.7 | 3.2536 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,382.9 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 852,689.6 | 3.2528 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 214,189.4 | 3.2683 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,213.5 | 1,212.7 | 1,220.0 | 3.1 | 1.000x | 1.000x | 75 | 16.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 7,196.7 | 6,932.8 | 7,234.6 | 117.7 | 5.931x | 5.931x | 75 | 96.0 | 8.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,107.0 | 0.0168 | 23,100.5 | 23,138.2 | 14.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,652,697.2 | 3.3807 | 4,635,720.8 | 4,662,199.9 | 10,337.7 | 201.355x | 201.355x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,620.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,543,160.0 | 3.3790 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 887,425.1 | 3.3853 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,107.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 222,235.0 | 3.3910 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,139.2 | 1,135.7 | 1,144.4 | 3.1 | 1.000x | 1.000x | 75 | 15.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 6,020.5 | 5,991.0 | 6,224.1 | 84.7 | 5.285x | 5.285x | 75 | 80.3 | 8.9 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 47.0 | 0.0000 | 46.8 | 47.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 47.2 | 0.0000 | 46.9 | 47.3 | 0.1 | 1.002x | 1.002x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 15.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 15.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 15.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15.7 | 0.0002 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 10,184,333.1 | 10,180,682.9 | 10,194,056.2 | 4,531.4 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 135,791.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 10,184,971.6 | 10,180,851.5 | 10,189,821.5 | 3,197.8 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 135,799.6 | 8.9 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 481,402.0 | 0.3498 | 481,072.5 | 481,492.0 | 147.0 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 481,442.3 | 0.3498 | 481,218.6 | 481,762.4 | 205.5 | 1.000x | 1.000x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 366,548.7 | 0.3496 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 366,732.9 | 0.3497 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 91,710.0 | 0.3498 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 91,654.5 | 0.3496 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 23,074.0 | 0.3521 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 22,986.7 | 0.3507 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,205.6 | 1,198.3 | 1,217.8 | 6.4 | 1.000x | 1.000x | 75 | 16.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,208.8 | 1,205.7 | 1,212.0 | 2.1 | 1.003x | 1.003x | 75 | 16.1 | 8.9 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 14.8 | 0.0000 | 14.7 | 15.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 14.8 | 0.0000 | 14.7 | 14.9 | 0.1 | 1.000x | 1.000x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 4.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4.9 | 0.0001 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 521.4 | 517.8 | 532.5 | 5.3 | 1.000x | 1.000x | 75 | 7.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 522.4 | 521.2 | 531.1 | 3.6 | 1.002x | 1.002x | 75 | 7.0 | 8.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 219,310.8 | 0.1594 | 219,141.4 | 219,634.2 | 178.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 219,491.8 | 0.1595 | 219,393.5 | 220,936.6 | 585.6 | 1.001x | 1.001x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 168,903.9 | 0.1611 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 169,008.9 | 0.1612 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 40,322.7 | 0.1538 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 40,244.0 | 0.1535 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10,119.8 | 0.1544 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10,241.9 | 0.1563 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 679.7 | 677.6 | 680.9 | 1.2 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 680.0 | 679.8 | 682.6 | 1.2 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,196,392.5 | 3.0491 | 4,195,493.0 | 4,197,359.2 | 782.6 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,197,626.6 | 3.0500 | 4,195,320.1 | 4,199,298.7 | 1,396.3 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,197,542.8 | 3.0494 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,199,059.3 | 3.0509 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 799,941.9 | 3.0515 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 800,126.6 | 3.0522 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 198,512.7 | 3.0291 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 198,822.6 | 3.0338 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,408.2 | 2,406.0 | 2,412.5 | 2.7 | 1.000x | 1.000x | 75 | 32.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,408.9 | 2,404.2 | 2,409.6 | 2.0 | 1.000x | 1.000x | 75 | 32.1 | 8.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,161,777.6 | 1.5708 | 2,157,756.8 | 2,164,971.7 | 2,408.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,167,392.6 | 1.5748 | 2,161,254.3 | 2,172,110.3 | 4,010.3 | 1.003x | 1.003x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,657,528.3 | 1.5807 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,656,923.5 | 1.5802 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 402,144.7 | 1.5341 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 405,522.6 | 1.5469 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 102,167.9 | 1.5590 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 103,317.1 | 1.5765 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,375.5 | 1,357.6 | 1,386.6 | 10.3 | 1.000x | 1.000x | 75 | 18.3 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,383.1 | 1,374.1 | 1,390.5 | 5.3 | 1.006x | 1.006x | 75 | 18.4 | 8.9 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,103.9 | 0.0168 | 23,092.4 | 23,109.7 | 5.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 23,169.1 | 0.0168 | 23,158.1 | 26,011.8 | 1,136.5 | 1.003x | 1.003x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,604.8 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,672.9 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,381.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,382.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,108.8 | 0.0169 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 661.7 | 660.1 | 662.6 | 0.9 | 1.000x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 663.0 | 661.8 | 665.3 | 1.2 | 1.002x | 1.002x | 75 | 8.8 | 8.9 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,109.7 | 0.0168 | 23,084.1 | 23,144.7 | 21.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 23,123.2 | 0.0168 | 23,110.7 | 23,139.4 | 9.8 | 1.001x | 1.001x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,607.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,623.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,387.7 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,389.3 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,111.1 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,107.5 | 0.0169 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 723.8 | 721.9 | 726.4 | 1.9 | 1.000x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 729.0 | 727.1 | 732.5 | 1.8 | 1.007x | 1.007x | 75 | 9.7 | 8.9 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 32.6 | 0.0000 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 32.6 | 0.0000 | 32.5 | 32.9 | 0.1 | 1.000x | 1.000x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 10.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 10.9 | 0.0002 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 952.9 | 951.8 | 963.7 | 5.1 | 1.000x | 1.000x | 75 | 12.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 964.2 | 959.9 | 973.3 | 4.6 | 1.012x | 1.012x | 75 | 12.9 | 8.9 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,058,134.8 | 2.9487 | 4,044,291.1 | 4,223,617.9 | 67,731.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,061,506.5 | 2.9511 | 4,045,951.6 | 4,544,778.3 | 193,877.6 | 1.001x | 1.001x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,109,180.9 | 2.9651 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,108,763.9 | 2.9647 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,673.8 | 2.9056 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 766,700.6 | 2.9247 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 185,099.4 | 2.8244 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 186,042.0 | 2.8388 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,454.4 | 2,450.8 | 2,520.9 | 26.8 | 1.000x | 1.000x | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,489.6 | 2,452.1 | 2,511.2 | 19.9 | 1.014x | 1.014x | 75 | 33.2 | 8.9 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,012,743.3 | 2.9157 | 4,007,371.2 | 4,022,263.2 | 5,295.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,016,077.8 | 2.9181 | 4,005,031.0 | 4,048,101.7 | 17,917.6 | 1.001x | 1.001x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,075,380.3 | 2.9329 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,078,760.7 | 2.9361 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 755,167.9 | 2.8807 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 754,672.1 | 2.8788 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 182,538.9 | 2.7853 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 182,584.1 | 2.7860 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,431.5 | 2,429.4 | 2,931.8 | 199.2 | 1.000x | 1.000x | 75 | 32.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,439.1 | 2,431.0 | 2,514.5 | 31.6 | 1.003x | 1.003x | 75 | 32.5 | 8.9 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,007,600.2 | 0.7321 | 1,007,490.2 | 1,008,452.4 | 349.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,008,715.7 | 0.7329 | 1,007,570.3 | 1,068,611.5 | 24,101.9 | 1.001x | 1.001x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 771,752.2 | 0.7360 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 772,560.9 | 0.7368 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 188,328.7 | 0.7184 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 188,524.5 | 0.7192 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 47,627.3 | 0.7267 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 47,658.8 | 0.7272 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,920.4 | 1,880.7 | 1,928.8 | 17.7 | 1.000x | 1.000x | 75 | 25.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,931.1 | 1,919.8 | 1,939.0 | 7.6 | 1.006x | 1.006x | 75 | 25.7 | 8.9 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 929,037.9 | 0.6750 | 928,706.1 | 929,382.6 | 267.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 930,513.5 | 0.6761 | 927,755.1 | 943,413.4 | 5,552.8 | 1.002x | 1.002x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 710,823.5 | 0.6779 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 712,137.8 | 0.6791 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 173,862.3 | 0.6632 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 174,601.5 | 0.6661 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 44,070.5 | 0.6725 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 44,160.6 | 0.6738 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,834.0 | 1,827.2 | 1,941.0 | 43.3 | 1.000x | 1.000x | 75 | 24.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,834.4 | 1,822.6 | 1,890.7 | 24.7 | 1.000x | 1.000x | 75 | 24.5 | 8.9 | 100% |

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,988,946.6 | 2.8984 | 3,985,988.0 | 3,990,696.5 | 1,928.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 3,990,162.0 | 2.8993 | 3,988,230.3 | 3,990,351.4 | 867.8 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,036,180.2 | 2.8955 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,036,857.2 | 2.8962 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 761,018.1 | 2.9031 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 761,585.4 | 2.9052 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 190,600.3 | 2.9083 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 190,445.1 | 2.9060 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,781.8 | 1,776.2 | 1,783.7 | 2.8 | 1.000x | 1.000x | 75 | 23.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 3,737.7 | 3,719.0 | 3,761.9 | 14.7 | 2.098x | 2.098x | 75 | 49.8 | 8.9 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,121.0 | 0.0168 | 23,113.0 | 23,144.3 | 10.7 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 3,461,245.7 | 2.5150 | 3,454,935.7 | 10,511,424.7 | 2,818,994.9 | 149.701x | 149.701x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,630.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 2,636,106.8 | 2.5140 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 659,506.1 | 2.5158 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,108.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 165,064.7 | 2.5187 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 933.1 | 925.3 | 934.3 | 3.6 | 1.000x | 1.000x | 75 | 12.4 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,611.0 | 2,607.5 | 2,616.5 | 3.2 | 2.798x | 2.798x | 75 | 34.8 | 8.9 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 3,941,061.0 | 2.8636 | 3,940,441.6 | 3,943,170.1 | 1,103.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,007,254.0 | 2.9117 | 4,005,573.2 | 4,008,218.6 | 903.6 | 1.017x | 1.017x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,003,059.3 | 2.8639 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,051,285.8 | 2.9099 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 751,290.9 | 2.8659 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 765,371.3 | 2.9197 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 186,921.8 | 2.8522 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 190,527.9 | 2.9072 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,165.8 | 1,165.7 | 1,172.4 | 2.6 | 1.000x | 1.000x | 75 | 15.5 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,672.4 | 2,667.6 | 5,392.3 | 1,088.4 | 2.292x | 2.292x | 75 | 35.6 | 8.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 124,414.9 | 0.0904 | 124,369.0 | 124,737.1 | 138.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 124,699.4 | 0.0906 | 124,535.5 | 124,820.2 | 93.7 | 1.002x | 1.002x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 102,511.9 | 0.0978 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 102,066.8 | 0.0973 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 18,628.5 | 0.0711 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 18,930.6 | 0.0722 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,328.2 | 0.0508 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 3,621.6 | 0.0553 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,515.1 | 1,513.6 | 1,517.9 | 1.5 | 1.000x | 1.000x | 75 | 20.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,626.8 | 1,625.6 | 1,632.4 | 2.5 | 1.074x | 1.074x | 75 | 21.7 | 8.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 341,120.3 | 0.2479 | 340,940.7 | 341,397.3 | 160.9 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 354,034.8 | 0.2572 | 353,916.6 | 354,061.6 | 62.9 | 1.038x | 1.038x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 261,976.9 | 0.2498 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 271,742.8 | 0.2592 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 64,438.3 | 0.2458 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 66,855.1 | 0.2550 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 14,667.0 | 0.2238 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 15,330.8 | 0.2339 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,252.7 | 1,248.6 | 1,257.5 | 3.2 | 1.000x | 1.000x | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,272.6 | 1,271.1 | 1,284.3 | 4.8 | 1.016x | 1.016x | 75 | 17.0 | 8.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,099.3 | 0.0168 | 23,094.6 | 23,130.4 | 14.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,286,469.6 | 0.9348 | 1,285,314.2 | 1,293,396.2 | 3,070.5 | 55.693x | 55.693x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,611.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 975,845.3 | 0.9306 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,380.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 247,541.5 | 0.9443 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,112.7 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 63,110.8 | 0.9630 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,052.5 | 1,051.4 | 1,053.0 | 0.6 | 1.000x | 1.000x | 75 | 14.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,811.8 | 1,807.4 | 2,049.4 | 95.6 | 1.721x | 1.721x | 75 | 24.2 | 8.9 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 352,292.7 | 0.2560 | 351,592.9 | 592,751.9 | 96,238.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 409,252.7 | 0.2974 | 408,639.2 | 409,347.9 | 258.3 | 1.162x | 1.162x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 282,877.2 | 0.2698 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 325,805.6 | 0.3107 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 58,459.8 | 0.2230 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 70,008.0 | 0.2671 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 11,027.6 | 0.1683 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 13,405.3 | 0.2045 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 657.5 | 657.3 | 658.7 | 0.5 | 1.000x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 704.7 | 702.5 | 798.7 | 37.9 | 1.072x | 1.072x | 75 | 9.4 | 8.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.2 | 0.0000 | 39.2 | 39.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 42.1 | 0.0000 | 42.0 | 43.5 | 0.6 | 1.074x | 1.074x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 14.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 14.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 13.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 14.1 | 0.0002 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 872.5 | 871.5 | 877.4 | 2.2 | 1.000x | 1.000x | 75 | 11.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 970.6 | 969.9 | 971.2 | 0.5 | 1.112x | 1.112x | 75 | 12.9 | 8.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,542,898.4 | 5.4807 | 7,521,327.7 | 7,611,419.9 | 30,850.8 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 7,557,264.4 | 5.4912 | 7,510,326.7 | 7,646,556.6 | 46,892.1 | 1.002x | 1.002x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 5,783,435.1 | 5.5155 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 5,804,644.9 | 5.5357 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 1,418,365.5 | 5.4106 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,412,926.4 | 5.3899 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 342,059.0 | 5.2194 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 339,693.1 | 5.1833 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,850.7 | 2,844.5 | 2,858.8 | 5.3 | 1.000x | 1.000x | 75 | 38.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,860.5 | 2,850.4 | 2,876.2 | 10.2 | 1.003x | 1.003x | 75 | 38.1 | 8.9 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 39.5 | 0.0000 | 37.3 | 42.1 | 1.6 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 39.6 | 0.0000 | 38.1 | 40.7 | 0.9 | 1.002x | 1.002x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 15.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 14.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 11.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 12.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 13.0 | 0.0002 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,052.0 | 1,042.1 | 1,066.4 | 7.9 | 1.000x | 1.000x | 75 | 14.0 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,053.2 | 1,049.7 | 1,064.7 | 5.2 | 1.001x | 1.001x | 75 | 14.0 | 8.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.3 | 0.0000 | 26.2 | 26.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 26.4 | 0.0000 | 26.3 | 26.7 | 0.2 | 1.005x | 1.005x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.8 | 0.0001 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 795.5 | 794.3 | 796.4 | 0.8 | 1.000x | 1.000x | 75 | 10.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 795.7 | 793.0 | 796.2 | 1.4 | 1.000x | 1.000x | 75 | 10.6 | 8.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 26.7 | 0.0000 | 26.7 | 26.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 26.7 | 0.0000 | 26.7 | 26.8 | 0.1 | 1.000x | 1.000x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 8.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 8.9 | 0.0001 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 734.4 | 733.9 | 735.3 | 0.5 | 1.000x | 1.000x | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 735.1 | 734.8 | 738.1 | 1.2 | 1.001x | 1.001x | 75 | 9.8 | 8.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 82,536.0 | 0.0600 | 82,271.7 | 83,000.2 | 264.8 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 82,586.8 | 0.0600 | 82,203.6 | 82,690.4 | 196.5 | 1.001x | 1.001x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 68,444.1 | 0.0653 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 68,327.8 | 0.0652 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 11,619.0 | 0.0443 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 11,732.1 | 0.0448 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 2,400.0 | 0.0366 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 2,443.4 | 0.0373 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 681.9 | 677.9 | 685.3 | 2.7 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 683.5 | 676.9 | 685.8 | 3.9 | 1.002x | 1.002x | 75 | 9.1 | 8.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 4,078,719.4 | 2.9636 | 4,077,124.0 | 4,081,653.7 | 1,566.0 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 4,080,790.5 | 2.9651 | 4,077,154.4 | 4,088,404.5 | 3,759.2 | 1.001x | 1.001x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 3,110,087.2 | 2.9660 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 3,112,749.5 | 2.9685 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 776,282.0 | 2.9613 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 776,394.8 | 2.9617 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 191,982.2 | 2.9294 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 191,610.1 | 2.9237 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 2,692.9 | 2,687.1 | 2,700.4 | 4.4 | 1.000x | 1.000x | 75 | 35.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 2,693.0 | 2,687.0 | 2,694.9 | 2.9 | 1.000x | 1.000x | 75 | 35.9 | 8.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,268,119.7 | 0.9214 | 1,264,436.8 | 1,269,624.5 | 1,780.3 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,357,172.5 | 0.9861 | 1,355,617.8 | 1,360,635.2 | 1,888.0 | 1.070x | 1.070x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 963,334.1 | 0.9187 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 1,028,682.2 | 0.9810 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 240,488.4 | 0.9174 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 260,617.0 | 0.9942 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 64,297.2 | 0.9811 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 67,873.2 | 1.0357 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 667.3 | 664.0 | 670.7 | 2.7 | 1.000x | 1.000x | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,240.9 | 1,217.8 | 1,261.1 | 16.2 | 1.860x | 1.860x | 75 | 16.5 | 8.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,000,077.4 | 0.7267 | 997,444.6 | 1,001,259.3 | 1,549.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,011,518.5 | 0.7350 | 997,010.7 | 1,017,427.2 | 7,790.7 | 1.011x | 1.011x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 759,695.9 | 0.7245 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 759,679.6 | 0.7245 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 192,069.1 | 0.7327 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 203,268.4 | 0.7754 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 48,170.8 | 0.7350 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 48,410.4 | 0.7387 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 1,095.0 | 1,079.0 | 1,109.4 | 9.9 | 1.000x | 1.000x | 75 | 14.6 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 1,103.2 | 1,096.6 | 1,108.2 | 4.3 | 1.007x | 1.007x | 75 | 14.7 | 8.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 12,133,714.5 | 8.8165 | 12,106,982.1 | 12,242,434.1 | 49,192.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 12,145,222.9 | 8.8248 | 12,110,731.3 | 12,828,515.9 | 272,933.4 | 1.001x | 1.001x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 9,252,129.7 | 8.8235 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 9,258,915.4 | 8.8300 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 2,306,117.0 | 8.7971 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 2,308,481.2 | 8.8062 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 575,832.8 | 8.7865 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 577,826.2 | 8.8169 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 7,333.2 | 7,324.9 | 7,359.1 | 13.3 | 1.000x | 1.000x | 75 | 97.8 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 7,340.0 | 7,314.5 | 7,416.4 | 43.2 | 1.001x | 1.001x | 75 | 97.9 | 8.9 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 23,172.9 | 0.0168 | 23,111.3 | 23,183.8 | 26.4 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 23,191.6 | 0.0169 | 23,151.6 | 23,196.3 | 17.5 | 1.001x | 1.001x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 17,641.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 17,679.2 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 4,419.2 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 4,389.5 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 1,106.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,111.4 | 0.0170 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 694.0 | 692.4 | 697.3 | 1.7 | 1.000x | 1.000x | 75 | 9.3 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 732.6 | 729.4 | 734.9 | 2.0 | 1.056x | 1.056x | 75 | 9.8 | 8.9 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 20.1 | 0.0000 | 20.0 | 20.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 20.2 | 0.0000 | 20.0 | 20.3 | 0.1 | 1.003x | 1.003x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_02902356_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_02902356_auto-caps-simdna` | 6.7 | 0.0001 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_02902356_auto-caps-simdna_noreqbyte (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_02902356_auto-caps-simdna_noreqbyte` | measured | `plain` | same program | 466.3 | 459.5 | 470.4 | 4.3 | 1.000x | 1.000x | 75 | 6.2 | 8.9 | 100% |
| 2 | `pcrec_02902356_auto-caps-simdna` | measured | `plain` | same program | 476.8 | 471.2 | 487.6 | 5.6 | 1.023x | 1.023x | 75 | 6.4 | 8.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_02902356_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |

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
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,868 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,075 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,180 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,782 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,887 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1464176 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1485383 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_02902356_auto-caps-simdna_noreqbyte` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
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
| `balanced-parens-rec` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 204,325,452.0 | 196,557,402.0 | 217,416,990.0 | 6,859,392.8 | 5 | 27,544 | 25,314 | 25,083 | 0.034 | compiled=5 | 1,566,939.0 | 202,036,899.0 | 110,000.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 209,484,558.0 | 203,603,828.0 | 210,182,262.0 | 2,391,194.0 | 5 | 27,544 | 25,532 | 25,301 | 0.011 | compiled=5 | 1,566,848.0 | 207,820,130.0 | 102,451.0 |
| `base10num-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,094,211.0 | 138,333,610.0 | 151,301,477.0 | 4,719,692.3 | 5 | 27,648 | 16,320 | 13,935 | 0.032 | compiled=5 | 1,631,628.0 | 146,294,401.0 | 101,161.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 137,940,318.0 | 136,577,931.0 | 146,910,385.0 | 4,662,255.4 | 5 | 27,576 | 15,773 | 13,388 | 0.034 | compiled=5 | 1,635,779.0 | 136,205,539.0 | 194,471.0 |
| `base10num-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 150,151,893.0 | 141,351,045.0 | 152,485,684.0 | 4,283,064.4 | 5 | 27,648 | 16,329 | 13,944 | 0.029 | compiled=5 | 1,527,968.0 | 148,523,744.0 | 100,181.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 136,454,910.0 | 131,962,666.0 | 141,550,067.0 | 3,480,242.4 | 5 | 27,576 | 15,782 | 13,397 | 0.026 | compiled=5 | 1,749,659.0 | 134,419,039.0 | 183,931.0 |
| `bracket-array-define` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,270,669.0 | 211,163,963.0 | 224,199,463.0 | 4,882,486.6 | 5 | 31,648 | 26,139 | 25,824 | 0.022 | compiled=5 | 1,686,498.0 | 221,482,451.0 | 101,720.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 228,014,961.0 | 222,442,095.0 | 241,491,844.0 | 6,362,092.8 | 5 | 31,648 | 26,254 | 25,939 | 0.028 (max is trial 1) | compiled=5 | 1,699,348.0 | 225,781,060.0 | 114,391.0 |
| `bracket-array-define` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 223,581,413.0 | 217,875,852.0 | 225,895,654.0 | 3,284,120.7 | 5 | 31,648 | 26,148 | 25,833 | 0.015 | compiled=5 | 1,699,269.0 | 221,879,493.0 | 110,991.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 228,400,316.0 | 224,394,986.0 | 234,977,101.0 | 3,867,559.3 | 5 | 31,648 | 26,263 | 25,948 | 0.017 | compiled=5 | 3,037,926.0 | 225,203,070.0 | 101,860.0 |
| `codegrammar-flat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 350,410,210.0 | 347,739,808.0 | 352,229,248.0 | 1,465,395.4 | 5 | 31,984 | 35,289 | 26,690 | 0.004 | compiled=5 | 2,188,300.0 | 348,176,700.0 | 102,460.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,590,435.0 | 343,778,670.0 | 361,485,642.0 | 6,386,224.1 | 5 | 32,032 | 35,010 | 27,498 | 0.018 | compiled=5 | 2,135,140.0 | 349,531,146.0 | 99,890.0 |
| `codegrammar-flat` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 341,894,858.0 | 332,623,439.0 | 344,493,280.0 | 4,318,647.4 | 5 | 31,984 | 35,295 | 26,696 | 0.013 | compiled=5 | 1,949,000.0 | 339,624,335.0 | 207,441.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 357,712,069.0 | 346,320,391.0 | 358,771,802.0 | 4,694,923.7 | 5 | 32,032 | 35,016 | 27,504 | 0.013 | compiled=5 | 2,040,681.0 | 355,471,767.0 | 106,050.0 |
| `codegrammar-xflag` | `plain` | `pcrec_02902356_auto-caps-simdna` | 349,902,468.0 | 344,855,334.0 | 351,068,773.0 | 2,466,814.7 | 5 | 32,024 | 35,615 | 26,937 | 0.007 | compiled=5 | 2,202,800.0 | 347,633,747.0 | 104,040.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 351,322,484.0 | 344,475,522.0 | 358,781,989.0 | 4,895,962.2 | 5 | 32,072 | 35,340 | 27,749 | 0.014 | compiled=5 | 2,154,780.0 | 348,723,862.0 | 111,441.0 |
| `codegrammar-xflag` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 340,914,392.0 | 338,344,228.0 | 353,234,936.0 | 5,904,653.7 | 5 | 32,024 | 35,621 | 26,943 | 0.017 | compiled=5 | 2,029,361.0 | 338,854,811.0 | 195,481.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 357,088,906.0 | 345,259,243.0 | 363,146,135.0 | 5,994,401.2 | 5 | 32,072 | 35,346 | 27,755 | 0.017 | compiled=5 | 2,043,250.0 | 354,995,564.0 | 105,931.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 224,567,663.0 | 217,270,151.0 | 232,909,143.0 | 5,249,245.5 | 5 | 32,008 | 32,574 | 26,943 | 0.023 | compiled=5 | 2,034,759.0 | 222,317,773.0 | 171,681.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 229,759,429.0 | 227,431,818.0 | 235,263,025.0 | 2,622,800.3 | 5 | 32,096 | 34,600 | 28,351 | 0.011 | compiled=5 | 2,097,270.0 | 227,096,016.0 | 103,261.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 219,920,361.0 | 207,432,508.0 | 228,083,486.0 | 6,946,204.4 | 5 | 32,008 | 32,583 | 26,952 | 0.032 | compiled=5 | 1,968,310.0 | 215,703,700.0 | 204,001.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 224,024,434.0 | 221,394,340.0 | 228,649,848.0 | 2,628,570.5 | 5 | 32,096 | 34,609 | 28,360 | 0.012 | compiled=5 | 1,965,680.0 | 220,826,748.0 | 185,421.0 |
| `date-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 251,160,339.0 | 249,828,153.0 | 264,233,379.0 | 5,768,044.1 | 5 | 31,872 | 33,439 | 31,413 | 0.023 | compiled=5 | 1,862,789.0 | 249,273,970.0 | 188,011.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 249,914,942.0 | 246,615,467.0 | 257,896,949.0 | 4,535,537.5 | 5 | 31,872 | 33,367 | 31,341 | 0.018 | compiled=5 | 1,881,209.0 | 247,932,523.0 | 117,800.0 |
| `date-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 258,943,336.0 | 243,627,416.0 | 262,829,946.0 | 7,045,326.7 | 5 | 31,872 | 33,448 | 31,422 | 0.027 | compiled=5 | 3,384,728.0 | 257,064,916.0 | 109,251.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 250,881,004.0 | 242,135,476.0 | 275,367,021.0 | 11,193,643.3 | 5 | 31,872 | 33,376 | 31,350 | 0.045 | compiled=5 | 1,762,660.0 | 249,210,405.0 | 105,660.0 |
| `doubled-word` | `plain` | `pcrec_02902356_auto-caps-simdna` | 215,788,773.0 | 207,712,437.0 | 216,861,368.0 | 3,390,669.8 | 5 | 27,504 | 24,373 | 23,911 | 0.016 | compiled=5 | 1,680,198.0 | 213,931,115.0 | 196,271.0 |
| `doubled-word` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,520,938.0 | 208,120,917.0 | 221,358,749.0 | 4,855,937.6 | 5 | 27,504 | 24,486 | 24,024 | 0.023 (max is trial 1) | compiled=5 | 1,686,258.0 | 212,716,719.0 | 118,301.0 |
| `doubled-word` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 210,121,412.0 | 208,750,525.0 | 218,050,214.0 | 3,344,125.5 | 5 | 27,504 | 24,382 | 23,920 | 0.016 | compiled=5 | 1,416,997.0 | 208,538,123.0 | 103,250.0 |
| `doubled-word` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 210,561,554.0 | 208,414,842.0 | 215,780,031.0 | 2,554,982.8 | 5 | 27,504 | 24,495 | 24,033 | 0.012 | compiled=5 | 1,738,219.0 | 207,786,200.0 | 100,970.0 |
| `dup-param-detect` | `plain` | `pcrec_02902356_auto-caps-simdna` | 234,612,641.0 | 227,933,080.0 | 241,146,671.0 | 4,181,673.6 | 5 | 31,776 | 27,325 | 26,809 | 0.018 (max is trial 1) | compiled=5 | 1,754,538.0 | 232,771,902.0 | 110,041.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,092,611.0 | 217,763,663.0 | 234,533,541.0 | 6,289,871.0 | 5 | 31,776 | 27,438 | 26,922 | 0.027 | compiled=5 | 1,725,488.0 | 226,268,403.0 | 104,011.0 |
| `dup-param-detect` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 223,518,661.0 | 223,385,230.0 | 224,825,437.0 | 616,334.8 | 5 | 31,720 | 26,936 | 26,474 | 0.003 (max is trial 1) | compiled=5 | 1,456,777.0 | 221,911,923.0 | 100,900.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 224,921,228.0 | 223,689,872.0 | 236,166,297.0 | 4,805,731.4 | 5 | 31,720 | 27,049 | 26,587 | 0.021 (max is trial 1) | compiled=5 | 1,619,488.0 | 223,071,079.0 | 192,281.0 |
| `email-local-nodup` | `plain` | `pcrec_02902356_auto-caps-simdna` | 204,559,462.0 | 191,806,192.0 | 205,457,235.0 | 5,327,770.4 | 5 | 31,712 | 26,945 | 24,872 | 0.026 | compiled=5 | 1,766,369.0 | 202,687,053.0 | 192,130.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,071,763.0 | 191,308,920.0 | 200,424,182.0 | 3,176,949.1 | 5 | 31,720 | 27,363 | 25,219 | 0.016 | compiled=5 | 1,749,518.0 | 192,347,385.0 | 120,181.0 |
| `email-local-nodup` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 203,611,268.0 | 190,002,976.0 | 213,262,749.0 | 7,871,030.6 | 5 | 31,712 | 26,954 | 24,881 | 0.039 | compiled=5 | 1,660,908.0 | 201,847,798.0 | 107,211.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 192,840,162.0 | 180,579,798.0 | 200,745,784.0 | 6,572,073.9 | 5 | 31,720 | 27,372 | 25,228 | 0.034 | compiled=5 | 1,684,179.0 | 190,955,722.0 | 195,211.0 |
| `email-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,213,978.0 | 214,580,838.0 | 223,994,381.0 | 3,771,618.7 | 5 | 31,832 | 28,826 | 26,880 | 0.017 | compiled=5 | 1,832,518.0 | 221,267,189.0 | 186,060.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 216,172,054.0 | 210,298,878.0 | 223,508,450.0 | 4,860,331.8 | 5 | 31,832 | 29,257 | 27,227 | 0.022 | compiled=5 | 1,800,538.0 | 214,180,096.0 | 192,210.0 |
| `email-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 216,236,724.0 | 207,477,048.0 | 223,766,383.0 | 5,702,153.9 | 5 | 31,832 | 28,830 | 26,884 | 0.026 | compiled=5 | 1,718,078.0 | 214,369,444.0 | 186,131.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 212,484,524.0 | 212,143,392.0 | 218,025,363.0 | 2,231,058.3 | 5 | 31,832 | 29,261 | 27,231 | 0.010 (max is trial 1) | compiled=5 | 1,709,419.0 | 210,281,063.0 | 203,361.0 |
| `evil-alt-nested` | `plain` | `pcrec_02902356_auto-caps-simdna` | 214,074,876.0 | 209,341,143.0 | 216,527,358.0 | 2,408,841.2 | 5 | 27,552 | 25,358 | 25,358 | 0.011 | compiled=5 | 1,662,718.0 | 212,224,787.0 | 207,241.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 214,635,217.0 | 201,477,147.0 | 215,388,932.0 | 5,333,958.1 | 5 | 27,552 | 25,471 | 25,471 | 0.025 | compiled=5 | 1,690,068.0 | 212,805,989.0 | 102,860.0 |
| `evil-alt-nested` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 213,768,481.0 | 211,853,481.0 | 215,195,418.0 | 1,100,951.3 | 5 | 27,552 | 25,367 | 25,367 | 0.005 | compiled=5 | 1,588,469.0 | 212,075,272.0 | 113,141.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 214,058,353.0 | 207,546,939.0 | 218,310,144.0 | 3,659,053.3 | 5 | 27,552 | 25,480 | 25,480 | 0.017 | compiled=5 | 1,611,259.0 | 212,403,234.0 | 107,731.0 |
| `file-ext-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,250,270.0 | 140,732,663.0 | 158,455,936.0 | 5,665,182.7 | 5 | 27,792 | 20,895 | 14,772 | 0.038 | compiled=5 | 1,948,959.0 | 145,949,819.0 | 203,391.0 |
| `file-ext-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,129,179.0 | 156,221,896.0 | 173,711,608.0 | 5,936,766.4 | 5 | 27,936 | 24,039 | 16,973 | 0.036 | compiled=5 | 2,138,890.0 | 163,115,219.0 | 205,831.0 |
| `file-ext-order` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 145,206,214.0 | 143,219,825.0 | 159,554,538.0 | 6,139,821.1 | 5 | 27,792 | 20,556 | 14,433 | 0.042 | compiled=5 | 2,253,972.0 | 143,156,524.0 | 194,311.0 |
| `file-ext-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 167,276,289.0 | 156,424,261.0 | 168,552,566.0 | 4,542,215.8 | 5 | 27,936 | 23,628 | 16,562 | 0.027 (max is trial 1) | compiled=5 | 1,907,750.0 | 164,261,414.0 | 207,511.0 |
| `float-literal-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,941,994.0 | 230,001,560.0 | 239,382,663.0 | 3,929,306.9 | 5 | 31,984 | 33,490 | 28,341 | 0.017 | compiled=5 | 2,041,769.0 | 228,819,344.0 | 198,701.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 230,345,992.0 | 227,149,656.0 | 237,412,245.0 | 3,380,353.5 | 5 | 32,080 | 34,332 | 28,874 | 0.015 | compiled=5 | 2,055,780.0 | 227,823,219.0 | 112,461.0 |
| `float-literal-bound` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 232,813,800.0 | 227,639,502.0 | 248,381,681.0 | 7,236,317.7 | 5 | 31,936 | 33,365 | 28,216 | 0.031 | compiled=5 | 2,333,672.0 | 228,451,347.0 | 115,170.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 234,935,739.0 | 219,990,025.0 | 236,401,828.0 | 6,324,998.0 | 5 | 32,024 | 34,207 | 28,749 | 0.027 | compiled=5 | 1,950,710.0 | 232,871,949.0 | 101,461.0 |
| `floor-byte` | `plain` | `pcrec_02902356_auto-caps-simdna` | 155,008,700.0 | 143,501,097.0 | 155,719,114.0 | 4,762,276.9 | 5 | 27,792 | 19,408 | 14,411 | 0.031 | compiled=5 | 1,780,579.0 | 153,053,781.0 | 188,591.0 |
| `floor-byte` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 165,083,528.0 | 155,416,843.0 | 166,119,563.0 | 3,972,416.0 | 5 | 27,936 | 21,863 | 16,540 | 0.024 | compiled=5 | 1,859,818.0 | 163,235,379.0 | 190,261.0 |
| `floor-byte` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 151,210,176.0 | 145,295,555.0 | 158,786,855.0 | 4,568,736.0 | 5 | 27,792 | 19,413 | 14,416 | 0.030 | compiled=5 | 1,709,939.0 | 149,286,686.0 | 111,341.0 |
| `floor-byte` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 160,881,256.0 | 156,938,725.0 | 164,714,666.0 | 2,762,186.4 | 5 | 27,936 | 21,868 | 16,545 | 0.017 | compiled=5 | 1,740,189.0 | 159,052,827.0 | 109,861.0 |
| `high-byte-run` | `plain` | `pcrec_02902356_auto-caps-simdna` | 169,620,318.0 | 153,693,524.0 | 173,204,545.0 | 7,061,656.2 | 5 | 27,488 | 25,653 | 19,347 | 0.042 | compiled=5 | 1,933,769.0 | 167,578,339.0 | 112,740.0 |
| `high-byte-run` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 169,622,188.0 | 163,646,892.0 | 171,473,048.0 | 2,650,434.4 | 5 | 27,928 | 24,467 | 17,340 | 0.016 (max is trial 1) | compiled=5 | 1,949,179.0 | 167,097,708.0 | 199,941.0 |
| `high-byte-run` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 165,411,979.0 | 162,084,553.0 | 172,337,264.0 | 3,634,451.6 | 5 | 27,488 | 25,662 | 19,356 | 0.022 | compiled=5 | 1,653,879.0 | 163,556,800.0 | 110,200.0 |
| `high-byte-run` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 162,300,312.0 | 153,009,335.0 | 169,505,010.0 | 6,232,151.1 | 5 | 27,928 | 24,476 | 17,349 | 0.038 | compiled=5 | 1,853,750.0 | 160,255,782.0 | 102,261.0 |
| `ipv4-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 170,419,577.0 | 161,408,870.0 | 172,392,567.0 | 4,137,927.8 | 5 | 32,608 | 23,285 | 17,969 | 0.024 | compiled=5 | 1,847,110.0 | 166,539,457.0 | 199,661.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 164,072,064.0 | 154,857,626.0 | 166,538,377.0 | 4,241,398.8 | 5 | 32,400 | 22,363 | 17,047 | 0.026 | compiled=5 | 1,882,020.0 | 162,120,374.0 | 194,501.0 |
| `ipv4-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 169,799,986.0 | 163,606,384.0 | 172,755,912.0 | 3,015,638.1 | 5 | 32,608 | 23,289 | 17,973 | 0.018 (max is trial 1) | compiled=5 | 1,711,239.0 | 167,990,587.0 | 104,591.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 163,562,392.0 | 156,948,219.0 | 166,068,207.0 | 3,295,185.9 | 5 | 32,400 | 22,367 | 17,051 | 0.020 (max is trial 1) | compiled=5 | 1,755,199.0 | 161,375,312.0 | 179,471.0 |
| `keyword-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,124,687.0 | 147,423,135.0 | 159,997,653.0 | 4,588,629.6 | 5 | 27,792 | 21,373 | 14,759 | 0.030 (max is trial 1) | compiled=5 | 3,929,019.0 | 150,279,519.0 | 106,880.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 162,479,826.0 | 159,682,963.0 | 170,528,473.0 | 4,867,929.2 | 5 | 27,936 | 25,794 | 16,968 | 0.030 | compiled=5 | 2,084,449.0 | 160,468,406.0 | 198,911.0 |
| `keyword-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 157,140,807.0 | 147,531,356.0 | 158,863,676.0 | 4,150,014.2 | 5 | 27,792 | 21,376 | 14,762 | 0.026 | compiled=5 | 1,832,909.0 | 155,078,356.0 | 211,621.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 165,658,651.0 | 157,931,181.0 | 168,999,716.0 | 3,991,697.2 | 5 | 27,936 | 25,797 | 16,971 | 0.024 | compiled=5 | 2,002,320.0 | 163,575,290.0 | 189,881.0 |
| `logparse-atomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 316,824,599.0 | 314,742,678.0 | 320,805,700.0 | 2,144,910.4 | 5 | 83,024 | 63,563 | 43,630 | 0.007 (max is trial 1) | compiled=5 | 2,703,634.0 | 313,899,064.0 | 221,901.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,585,933.0 | 312,902,408.0 | 320,630,098.0 | 2,936,477.8 | 5 | 82,984 | 63,490 | 43,557 | 0.009 | compiled=5 | 2,686,644.0 | 316,769,058.0 | 130,231.0 |
| `logparse-atomic` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 315,428,465.0 | 304,080,244.0 | 325,042,476.0 | 7,265,517.3 | 5 | 83,024 | 63,565 | 43,632 | 0.023 | compiled=5 | 2,540,903.0 | 312,694,851.0 | 208,461.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 318,543,842.0 | 312,552,860.0 | 321,094,576.0 | 3,568,973.6 | 5 | 82,984 | 63,492 | 43,559 | 0.011 | compiled=5 | 2,527,684.0 | 312,712,021.0 | 116,261.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_02902356_auto-caps-simdna` | 314,151,105.0 | 306,248,263.0 | 319,478,292.0 | 5,091,018.5 | 5 | 83,024 | 63,282 | 43,349 | 0.016 (max is trial 1) | compiled=5 | 2,640,974.0 | 311,347,630.0 | 129,241.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 319,728,574.0 | 314,575,567.0 | 322,566,349.0 | 2,653,143.6 | 5 | 82,984 | 63,209 | 43,276 | 0.008 | compiled=5 | 2,694,314.0 | 316,910,999.0 | 121,910.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 312,795,361.0 | 307,019,101.0 | 314,834,842.0 | 3,103,552.9 | 5 | 83,024 | 63,284 | 43,351 | 0.010 | compiled=5 | 2,552,733.0 | 310,001,596.0 | 124,741.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 309,466,403.0 | 298,156,754.0 | 317,499,297.0 | 7,049,368.2 | 5 | 82,984 | 63,211 | 43,278 | 0.023 | compiled=5 | 2,529,094.0 | 306,802,650.0 | 213,121.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,861,807.0 | 147,480,596.0 | 154,937,280.0 | 2,590,803.2 | 5 | 27,792 | 19,636 | 14,433 | 0.017 | compiled=5 | 1,886,669.0 | 149,911,427.0 | 102,521.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,905,413.0 | 152,217,487.0 | 167,914,941.0 | 6,347,373.2 | 5 | 27,936 | 22,055 | 16,450 | 0.039 | compiled=5 | 1,980,399.0 | 159,936,974.0 | 194,641.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 154,205,360.0 | 142,624,759.0 | 157,170,927.0 | 5,089,796.2 | 5 | 27,792 | 19,641 | 14,438 | 0.033 | compiled=5 | 1,783,629.0 | 152,304,951.0 | 116,780.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 164,226,034.0 | 153,179,356.0 | 164,921,277.0 | 5,360,718.9 | 5 | 27,936 | 22,060 | 16,455 | 0.033 | compiled=5 | 1,798,519.0 | 160,906,146.0 | 124,731.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_02902356_auto-caps-simdna` | 287,310,097.0 | 282,527,124.0 | 291,975,619.0 | 3,234,697.7 | 5 | 31,688 | 31,521 | 31,290 | 0.011 | compiled=5 | 1,881,739.0 | 283,405,708.0 | 103,980.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 291,557,535.0 | 275,806,332.0 | 293,634,205.0 | 6,762,529.5 | 5 | 31,688 | 31,634 | 31,403 | 0.023 | compiled=5 | 1,918,699.0 | 289,668,927.0 | 111,690.0 |
| `nested-comment-rec` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 285,131,731.0 | 277,431,913.0 | 290,310,249.0 | 4,439,505.1 | 5 | 31,640 | 31,000 | 30,769 | 0.016 | compiled=5 | 1,721,859.0 | 283,337,022.0 | 100,490.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 286,553,669.0 | 279,708,084.0 | 288,066,877.0 | 3,099,201.0 | 5 | 31,640 | 31,113 | 30,882 | 0.011 | compiled=5 | 1,706,459.0 | 284,742,009.0 | 103,431.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 217,885,073.0 | 207,805,977.0 | 220,599,306.0 | 4,415,192.0 | 5 | 31,752 | 28,488 | 26,806 | 0.020 | compiled=5 | 1,797,289.0 | 216,014,035.0 | 191,421.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 217,457,921.0 | 210,867,200.0 | 218,995,039.0 | 2,883,203.4 | 5 | 31,752 | 28,417 | 26,735 | 0.013 | compiled=5 | 1,778,848.0 | 215,469,212.0 | 206,521.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 217,253,609.0 | 211,856,111.0 | 218,311,045.0 | 2,626,683.8 | 5 | 31,752 | 28,497 | 26,815 | 0.012 | compiled=5 | 1,701,469.0 | 215,495,580.0 | 202,321.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 216,997,888.0 | 211,504,929.0 | 218,525,286.0 | 2,448,726.0 | 5 | 31,752 | 28,426 | 26,744 | 0.011 | compiled=5 | 1,737,629.0 | 215,079,408.0 | 101,231.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna` | 225,125,868.0 | 217,514,821.0 | 230,756,862.0 | 4,460,607.6 | 5 | 31,832 | 29,716 | 27,774 | 0.020 | compiled=5 | 1,831,488.0 | 221,687,611.0 | 192,331.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 222,629,486.0 | 215,127,080.0 | 228,743,694.0 | 4,951,425.5 | 5 | 31,792 | 29,644 | 27,702 | 0.022 | compiled=5 | 1,824,198.0 | 220,193,374.0 | 187,581.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 230,020,765.0 | 226,013,473.0 | 235,656,764.0 | 3,146,102.0 | 5 | 31,832 | 29,725 | 27,783 | 0.014 | compiled=5 | 1,739,499.0 | 228,096,625.0 | 204,251.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 223,561,591.0 | 214,359,183.0 | 232,151,716.0 | 6,079,213.9 | 5 | 31,792 | 29,653 | 27,711 | 0.027 | compiled=5 | 1,830,389.0 | 220,506,476.0 | 103,960.0 |
| `phone-palindrome-6` | `plain` | `pcrec_02902356_auto-caps-simdna` | 292,820,412.0 | 286,676,783.0 | 293,029,143.0 | 2,642,137.5 | 5 | 27,344 | 23,271 | 23,271 | 0.009 | compiled=5 | 1,772,489.0 | 291,041,523.0 | 102,150.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 194,440,195.0 | 189,423,051.0 | 197,308,879.0 | 3,154,488.2 | 5 | 27,424 | 23,079 | 23,079 | 0.016 | compiled=5 | 1,635,797.0 | 191,035,019.0 | 108,211.0 |
| `phone-palindrome-6` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 292,467,201.0 | 285,167,411.0 | 300,445,381.0 | 5,400,304.1 | 5 | 27,344 | 23,280 | 23,280 | 0.018 | compiled=5 | 1,525,518.0 | 290,724,071.0 | 197,941.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 192,699,941.0 | 189,351,902.0 | 198,052,629.0 | 3,484,418.0 | 5 | 27,424 | 23,088 | 23,088 | 0.018 | compiled=5 | 1,541,718.0 | 189,620,045.0 | 188,011.0 |
| `pwd-strength-chain` | `plain` | `pcrec_02902356_auto-caps-simdna` | 252,513,566.0 | 246,928,378.0 | 258,536,103.0 | 3,812,285.6 | 5 | 31,984 | 32,820 | 30,179 | 0.015 | compiled=5 | 1,920,739.0 | 250,441,875.0 | 191,851.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 242,853,379.0 | 235,803,237.0 | 256,657,053.0 | 7,366,398.6 | 5 | 31,984 | 32,748 | 30,107 | 0.030 | compiled=5 | 1,857,339.0 | 240,807,110.0 | 190,301.0 |
| `pwd-strength-chain` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 251,286,836.0 | 245,062,401.0 | 252,000,310.0 | 2,613,165.3 | 5 | 31,984 | 32,829 | 30,188 | 0.010 | compiled=5 | 1,772,690.0 | 249,399,056.0 | 110,560.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 251,105,534.0 | 250,549,882.0 | 255,092,375.0 | 1,689,096.4 | 5 | 31,984 | 32,757 | 30,116 | 0.007 (max is trial 1) | compiled=5 | 1,802,209.0 | 249,235,965.0 | 193,681.0 |
| `quoted-delim-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 218,731,857.0 | 204,654,862.0 | 221,932,213.0 | 6,360,569.8 | 5 | 31,768 | 26,057 | 25,364 | 0.029 | compiled=5 | 1,712,258.0 | 216,928,989.0 | 104,370.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 212,245,628.0 | 203,503,576.0 | 218,781,397.0 | 5,618,585.4 | 5 | 31,768 | 26,170 | 25,477 | 0.026 | compiled=5 | 1,684,268.0 | 210,604,730.0 | 105,360.0 |
| `quoted-delim-match` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 211,369,789.0 | 202,925,244.0 | 219,109,458.0 | 6,032,743.3 | 5 | 31,768 | 26,066 | 25,373 | 0.029 | compiled=5 | 1,648,339.0 | 209,512,639.0 | 195,171.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 208,119,682.0 | 203,648,638.0 | 209,400,549.0 | 2,042,157.9 | 5 | 31,768 | 26,179 | 25,486 | 0.010 | compiled=5 | 1,612,049.0 | 206,342,492.0 | 102,081.0 |
| `router-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna` | 150,587,451.0 | 141,122,647.0 | 160,300,795.0 | 6,270,160.8 | 5 | 27,792 | 20,751 | 14,771 | 0.042 | compiled=5 | 1,982,569.0 | 148,723,912.0 | 102,691.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 160,820,168.0 | 153,542,685.0 | 161,812,563.0 | 3,307,435.2 | 5 | 27,936 | 23,579 | 16,972 | 0.021 (max is trial 1) | compiled=5 | 2,022,219.0 | 158,242,906.0 | 190,141.0 |
| `router-prefix-order` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 154,328,021.0 | 136,048,756.0 | 156,614,484.0 | 8,010,349.2 | 5 | 27,792 | 20,407 | 14,427 | 0.052 | compiled=5 | 1,851,390.0 | 152,326,521.0 | 196,431.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 162,396,334.0 | 156,076,070.0 | 164,926,387.0 | 3,320,832.7 | 5 | 27,936 | 23,163 | 16,556 | 0.020 | compiled=5 | 1,908,690.0 | 160,312,243.0 | 175,401.0 |
| `tag-depth3-bound` | `plain` | `pcrec_02902356_auto-caps-simdna` | 288,433,500.0 | 277,958,793.0 | 291,477,567.0 | 4,794,577.6 | 5 | 31,816 | 33,543 | 33,027 | 0.017 | compiled=5 | 1,853,588.0 | 286,449,823.0 | 110,011.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 286,343,192.0 | 281,916,582.0 | 288,441,001.0 | 2,421,918.9 | 5 | 31,816 | 33,656 | 33,140 | 0.008 | compiled=5 | 1,849,879.0 | 284,287,512.0 | 105,571.0 |
| `tag-depth3-bound` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 281,185,841.0 | 277,296,391.0 | 289,903,757.0 | 4,481,800.0 | 5 | 31,768 | 32,778 | 32,316 | 0.016 | compiled=5 | 1,760,990.0 | 279,436,292.0 | 190,571.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 281,463,783.0 | 275,262,911.0 | 290,163,248.0 | 5,095,189.1 | 5 | 31,768 | 32,891 | 32,429 | 0.018 | compiled=5 | 1,753,409.0 | 279,601,623.0 | 108,751.0 |
| `tag-pair-match` | `plain` | `pcrec_02902356_auto-caps-simdna` | 235,483,335.0 | 226,488,733.0 | 242,345,747.0 | 5,563,115.7 | 5 | 31,776 | 27,351 | 26,142 | 0.024 | compiled=5 | 1,782,258.0 | 233,492,516.0 | 211,751.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 231,911,019.0 | 226,272,912.0 | 240,164,277.0 | 4,755,950.5 | 5 | 31,776 | 27,464 | 26,255 | 0.021 | compiled=5 | 1,793,698.0 | 229,548,938.0 | 194,851.0 |
| `tag-pair-match` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 227,782,903.0 | 219,225,690.0 | 227,954,314.0 | 3,528,400.6 | 5 | 27,632 | 26,586 | 25,431 | 0.015 | compiled=5 | 1,682,979.0 | 225,914,074.0 | 112,060.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 227,492,802.0 | 220,941,177.0 | 230,996,820.0 | 3,475,619.8 | 5 | 27,632 | 26,699 | 25,544 | 0.015 | compiled=5 | 1,681,478.0 | 225,706,022.0 | 191,741.0 |
| `trim-nested-star` | `plain` | `pcrec_02902356_auto-caps-simdna` | 205,170,163.0 | 194,203,813.0 | 205,709,646.0 | 4,936,153.9 | 5 | 27,512 | 23,591 | 23,360 | 0.024 | compiled=5 | 1,651,438.0 | 203,283,615.0 | 106,760.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,039,954.0 | 199,593,018.0 | 204,630,652.0 | 1,947,756.5 | 5 | 27,512 | 23,705 | 23,474 | 0.010 | compiled=5 | 1,651,167.0 | 201,290,756.0 | 104,570.0 |
| `trim-nested-star` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 197,646,036.0 | 197,128,146.0 | 204,330,361.0 | 2,747,329.4 | 5 | 27,512 | 23,600 | 23,369 | 0.014 | compiled=5 | 1,551,528.0 | 196,007,278.0 | 196,531.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 203,495,377.0 | 196,960,473.0 | 208,940,625.0 | 3,887,994.8 | 5 | 27,512 | 23,714 | 23,483 | 0.019 | compiled=5 | 1,553,248.0 | 201,824,009.0 | 107,190.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,589,682.0 | 186,516,878.0 | 193,034,517.0 | 2,111,820.7 | 5 | 31,816 | 28,015 | 23,213 | 0.011 | compiled=5 | 1,913,739.0 | 187,574,873.0 | 103,051.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 195,997,671.0 | 191,905,032.0 | 199,909,889.0 | 2,539,046.0 | 5 | 31,904 | 29,703 | 24,687 | 0.013 | compiled=5 | 1,907,719.0 | 194,006,163.0 | 102,530.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 188,804,461.0 | 182,063,256.0 | 198,800,512.0 | 5,627,614.5 | 5 | 31,816 | 28,024 | 23,222 | 0.030 | compiled=5 | 1,809,420.0 | 186,910,441.0 | 106,131.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 196,392,850.0 | 190,199,928.0 | 200,646,173.0 | 3,405,744.3 | 5 | 31,904 | 29,712 | 24,696 | 0.017 (max is trial 1) | compiled=5 | 1,818,259.0 | 194,382,300.0 | 185,701.0 |
| `uuid-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 177,306,022.0 | 170,009,575.0 | 178,885,161.0 | 3,620,951.4 | 5 | 37,072 | 23,602 | 18,198 | 0.020 | compiled=5 | 1,735,369.0 | 175,458,523.0 | 112,130.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 173,594,354.0 | 163,611,851.0 | 182,161,508.0 | 6,060,446.7 | 5 | 37,032 | 23,424 | 18,020 | 0.035 | compiled=5 | 1,762,910.0 | 171,354,672.0 | 206,041.0 |
| `uuid-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 181,403,738.0 | 176,504,362.0 | 181,908,291.0 | 2,092,003.5 | 5 | 37,072 | 23,606 | 18,202 | 0.012 | compiled=5 | 1,626,119.0 | 177,016,794.0 | 199,761.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 174,057,148.0 | 169,971,787.0 | 182,678,553.0 | 4,352,860.0 | 5 | 37,032 | 23,428 | 18,024 | 0.025 (max is trial 1) | compiled=5 | 1,650,969.0 | 172,423,240.0 | 190,761.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,159,039.0 | 146,948,134.0 | 154,338,498.0 | 2,683,977.6 | 5 | 27,792 | 19,408 | 14,411 | 0.018 | compiled=5 | 1,830,278.0 | 145,323,646.0 | 196,051.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,117,822.0 | 148,165,720.0 | 162,967,238.0 | 5,042,822.8 | 5 | 27,936 | 21,863 | 16,540 | 0.033 | compiled=5 | 3,548,726.0 | 151,482,235.0 | 116,011.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 154,805,025.0 | 134,042,797.0 | 158,069,421.0 | 9,028,742.1 | 5 | 27,792 | 19,414 | 14,417 | 0.058 | compiled=5 | 1,681,148.0 | 152,857,284.0 | 190,351.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 163,296,318.0 | 148,399,980.0 | 166,788,647.0 | 6,643,010.0 | 5 | 27,936 | 21,869 | 16,546 | 0.041 | compiled=5 | 1,760,519.0 | 161,302,128.0 | 191,231.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_02902356_auto-caps-simdna` | 152,325,668.0 | 150,784,142.0 | 157,123,131.0 | 2,229,834.1 | 5 | 28,112 | 28,359 | 16,094 | 0.015 (max is trial 1) | compiled=5 | 2,692,762.0 | 149,492,626.0 | 192,071.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,102,239.0 | 156,585,180.0 | 182,357,058.0 | 9,662,757.1 | 5 | 28,256 | 31,334 | 18,181 | 0.059 | compiled=5 | 2,778,193.0 | 160,616,687.0 | 100,730.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 161,648,390.0 | 153,000,975.0 | 170,131,983.0 | 6,054,477.0 | 5 | 28,112 | 28,368 | 16,103 | 0.037 | compiled=5 | 2,221,861.0 | 159,070,716.0 | 193,411.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 170,907,948.0 | 158,840,576.0 | 179,099,800.0 | 6,584,053.8 | 5 | 28,256 | 31,343 | 18,190 | 0.039 | compiled=5 | 2,414,903.0 | 168,294,284.0 | 111,181.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_02902356_auto-caps-simdna` | 148,291,179.0 | 144,234,151.0 | 156,807,730.0 | 4,158,631.4 | 5 | 27,784 | 23,172 | 14,850 | 0.028 | compiled=5 | 2,093,600.0 | 145,179,765.0 | 201,841.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,864,495.0 | 154,640,848.0 | 172,180,451.0 | 6,530,659.9 | 5 | 27,928 | 26,523 | 16,764 | 0.042 | compiled=5 | 2,319,021.0 | 153,340,953.0 | 193,821.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 155,055,466.0 | 138,164,208.0 | 162,429,794.0 | 8,143,392.3 | 5 | 27,784 | 23,181 | 14,859 | 0.053 | compiled=5 | 1,988,510.0 | 152,968,415.0 | 192,661.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 163,795,772.0 | 154,863,874.0 | 164,529,945.0 | 3,841,353.2 | 5 | 27,928 | 26,532 | 16,773 | 0.023 | compiled=5 | 2,137,841.0 | 161,561,370.0 | 113,291.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_02902356_auto-caps-simdna` | 149,682,477.0 | 143,503,517.0 | 158,570,648.0 | 5,971,834.3 | 5 | 27,792 | 19,410 | 14,413 | 0.040 | compiled=5 | 1,761,198.0 | 145,874,429.0 | 103,331.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 155,850,874.0 | 146,484,851.0 | 165,597,341.0 | 7,429,494.0 | 5 | 27,936 | 21,865 | 16,542 | 0.048 | compiled=5 | 1,830,449.0 | 153,621,964.0 | 207,861.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 145,694,417.0 | 143,562,516.0 | 160,923,257.0 | 6,779,568.1 | 5 | 27,792 | 19,415 | 14,418 | 0.047 | compiled=5 | 1,696,249.0 | 143,757,627.0 | 192,241.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 157,737,439.0 | 155,026,476.0 | 167,335,789.0 | 4,266,379.8 | 5 | 27,936 | 21,870 | 16,547 | 0.027 | compiled=5 | 1,729,319.0 | 155,078,336.0 | 102,121.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_02902356_auto-caps-simdna` | 154,503,939.0 | 137,125,829.0 | 157,145,741.0 | 7,847,919.6 | 5 | 27,792 | 20,788 | 14,693 | 0.051 | compiled=5 | 1,959,849.0 | 150,304,429.0 | 205,081.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 163,620,620.0 | 161,107,759.0 | 166,187,664.0 | 1,665,031.3 | 5 | 27,936 | 23,542 | 16,824 | 0.010 | compiled=5 | 1,997,599.0 | 161,517,271.0 | 190,871.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 147,334,696.0 | 145,148,774.0 | 154,818,833.0 | 3,362,112.6 | 5 | 27,792 | 20,794 | 14,699 | 0.023 | compiled=5 | 2,215,691.0 | 144,103,109.0 | 103,260.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 163,945,722.0 | 156,960,565.0 | 174,722,498.0 | 5,950,111.5 | 5 | 27,936 | 23,548 | 16,830 | 0.036 (max is trial 1) | compiled=5 | 1,869,540.0 | 161,886,781.0 | 108,130.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 576,388,570.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,247,714,708.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 589,117,501.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,433,644,294.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,338,075.0 | 361,869,673.0 | 370,076,501.0 | 3,261,612.4 | 5 | 45,832 | 55,446 | 45,523 | 0.009 (max is trial 1) | compiled=5 | 2,342,761.0 | 359,831,154.0 | 117,050.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 350,317,570.0 | 334,239,615.0 | 351,187,503.0 | 6,503,231.7 | 5 | 45,464 | 53,885 | 43,962 | 0.019 | compiled=5 | 2,430,571.0 | 347,837,418.0 | 199,971.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 353,599,977.0 | 351,719,048.0 | 372,378,035.0 | 7,779,205.7 | 5 | 45,832 | 55,450 | 45,527 | 0.022 | compiled=5 | 2,242,601.0 | 351,245,105.0 | 104,471.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 350,299,910.0 | 333,932,135.0 | 350,575,812.0 | 6,572,422.0 | 5 | 45,464 | 53,889 | 43,966 | 0.019 | compiled=5 | 2,299,092.0 | 347,888,337.0 | 102,171.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 237,290,446.0 | 231,316,804.0 | 245,960,600.0 | 5,714,327.3 | 5 | 31,976 | 33,908 | 28,398 | 0.024 | compiled=5 | 2,090,641.0 | 232,811,032.0 | 192,921.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 246,142,221.0 | 233,371,684.0 | 252,066,191.0 | 7,422,745.9 | 5 | 32,072 | 34,980 | 29,045 | 0.030 (max is trial 1) | compiled=5 | 2,104,261.0 | 241,590,197.0 | 194,071.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 234,991,360.0 | 225,590,860.0 | 240,294,819.0 | 4,910,450.3 | 5 | 31,976 | 33,917 | 28,407 | 0.021 | compiled=5 | 1,985,021.0 | 232,888,389.0 | 112,111.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 241,878,987.0 | 235,274,722.0 | 243,040,123.0 | 3,528,111.5 | 5 | 32,072 | 34,989 | 29,054 | 0.015 | compiled=5 | 2,011,150.0 | 239,765,596.0 | 101,900.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 232,151,498.0 | 231,093,062.0 | 236,998,853.0 | 2,064,415.7 | 5 | 31,976 | 33,629 | 28,119 | 0.009 | compiled=5 | 2,043,771.0 | 229,879,126.0 | 109,001.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 240,890,644.0 | 231,783,847.0 | 245,950,040.0 | 4,830,727.1 | 5 | 32,072 | 34,698 | 28,763 | 0.020 | compiled=5 | 2,104,761.0 | 238,206,500.0 | 108,841.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 238,337,588.0 | 229,575,211.0 | 242,658,811.0 | 5,559,121.8 | 5 | 31,976 | 33,638 | 28,128 | 0.023 | compiled=5 | 4,108,532.0 | 236,208,006.0 | 193,491.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 237,834,594.0 | 230,078,515.0 | 249,329,707.0 | 6,162,525.7 | 5 | 32,072 | 34,707 | 28,772 | 0.026 | compiled=5 | 2,006,321.0 | 235,637,144.0 | 191,991.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 410,361,126.0 | 389,258,935.0 | 412,174,335.0 | 8,476,483.0 | 5 | 40,680 | 61,633 | 41,904 | 0.021 | compiled=5 | 5,137,327.0 | 400,032,002.0 | 193,601.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 414,227,586.0 | 403,260,857.0 | 415,743,663.0 | 4,791,466.9 | 5 | 40,776 | 66,276 | 43,404 | 0.012 | compiled=5 | 8,259,983.0 | 405,708,401.0 | 193,411.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 401,800,741.0 | 394,686,033.0 | 402,922,477.0 | 2,931,487.4 | 5 | 40,680 | 61,642 | 41,913 | 0.007 | compiled=5 | 5,030,057.0 | 396,578,404.0 | 188,491.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 406,565,336.0 | 401,043,328.0 | 414,417,496.0 | 4,265,465.1 | 5 | 40,776 | 66,285 | 43,413 | 0.010 | compiled=5 | 8,163,733.0 | 398,218,672.0 | 200,291.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna` | 362,494,897.0 | 354,488,595.0 | 364,639,699.0 | 3,632,735.8 | 5 | 40,680 | 59,185 | 39,456 | 0.010 | compiled=5 | 4,989,566.0 | 356,707,876.0 | 193,201.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 375,793,157.0 | 365,474,932.0 | 386,638,593.0 | 7,675,001.2 | 5 | 40,776 | 63,828 | 40,956 | 0.020 | compiled=5 | 18,567,707.0 | 357,489,900.0 | 195,751.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 363,366,968.0 | 359,229,826.0 | 364,446,214.0 | 1,847,724.3 | 5 | 40,680 | 59,194 | 39,465 | 0.005 | compiled=5 | 4,808,276.0 | 358,472,032.0 | 193,032.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 374,511,528.0 | 357,599,697.0 | 376,017,154.0 | 6,870,771.1 | 5 | 40,776 | 63,837 | 40,965 | 0.018 (max is trial 1) | compiled=5 | 7,848,331.0 | 365,349,528.0 | 101,551.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_02902356_auto-caps-simdna` | 5,446,416,952.0 | 5,427,347,513.0 | 5,490,679,283.0 | 22,705,595.8 | 5 | 176,208 | 518,007 (warned) | 300,042 | 0.004 | compiled=5 | 599,367,599.0 | 4,848,712,922.0 | 104,491.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 6,440,923,029.0 | 6,428,778,045.0 | 6,483,773,802.0 | 23,122,738.7 | 5 | 180,400 | 527,624 (warned) | 301,462 | 0.004 | compiled=5 | 1,597,453,843.0 | 4,841,745,826.0 | 102,270.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 5,436,333,252.0 | 5,415,464,563.0 | 5,443,215,119.0 | 10,033,725.4 | 5 | 176,160 | 517,882 (warned) | 299,917 | 0.002 | compiled=5 | 608,823,443.0 | 4,825,237,798.0 | 204,621.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 6,447,925,601.0 | 6,444,372,652.0 | 6,477,653,165.0 | 13,256,032.5 | 5 | 180,352 | 527,499 (warned) | 301,337 | 0.002 (max is trial 1) | compiled=5 | 1,601,848,183.0 | 4,845,772,887.0 | 203,851.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 243,714,108.0 | 237,783,439.0 | 249,010,057.0 | 4,185,869.1 | 5 | 32,192 | 37,329 | 28,845 | 0.017 (max is trial 1) | compiled=5 | 2,326,392.0 | 241,362,536.0 | 103,890.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 251,426,368.0 | 246,983,875.0 | 261,178,300.0 | 5,232,178.0 | 5 | 32,328 | 40,673 | 30,370 | 0.021 | compiled=5 | 2,284,812.0 | 248,930,105.0 | 199,591.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 238,556,679.0 | 236,321,947.0 | 244,355,699.0 | 2,948,487.6 | 5 | 32,136 | 37,204 | 28,720 | 0.012 | compiled=5 | 2,348,922.0 | 234,291,507.0 | 109,450.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 252,255,753.0 | 243,085,123.0 | 266,200,923.0 | 8,317,810.8 | 5 | 32,272 | 40,548 | 30,245 | 0.033 | compiled=5 | 2,317,242.0 | 249,730,808.0 | 207,702.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_02902356_auto-caps-simdna` | 245,666,419.0 | 241,410,265.0 | 253,353,299.0 | 4,606,066.9 | 5 | 36,256 | 47,651 | 30,746 | 0.019 | compiled=5 | 3,191,957.0 | 242,187,321.0 | 187,331.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 258,180,164.0 | 245,346,406.0 | 260,020,843.0 | 5,863,146.8 | 5 | 36,352 | 50,184 | 32,283 | 0.023 | compiled=5 | 3,304,887.0 | 254,810,406.0 | 188,071.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 251,454,537.0 | 243,901,467.0 | 252,523,063.0 | 3,938,767.7 | 5 | 36,208 | 47,526 | 30,621 | 0.016 | compiled=5 | 3,085,046.0 | 248,321,650.0 | 109,981.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 256,658,003.0 | 242,353,330.0 | 257,760,990.0 | 6,158,734.6 | 5 | 36,296 | 50,059 | 32,158 | 0.024 | compiled=5 | 3,165,807.0 | 253,363,726.0 | 119,361.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_02902356_auto-caps-simdna` | 392,491,672.0 | 384,915,983.0 | 398,643,295.0 | 4,999,999.4 | 5 | 44,320 | 57,974 | 27,864 | 0.013 | compiled=5 | 4,485,413.0 | 387,920,869.0 | 103,981.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 399,138,288.0 | 391,772,370.0 | 407,136,649.0 | 5,635,371.5 | 5 | 40,320 | 61,344 | 29,401 | 0.014 | compiled=5 | 4,615,554.0 | 394,447,313.0 | 106,991.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 393,548,645.0 | 386,382,157.0 | 404,092,351.0 | 5,667,782.3 | 5 | 40,224 | 57,891 | 27,781 | 0.014 (max is trial 1) | compiled=5 | 4,295,352.0 | 388,960,641.0 | 194,821.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 391,996,268.0 | 390,112,098.0 | 427,834,552.0 | 14,281,711.8 | 5 | 40,320 | 61,261 | 29,318 | 0.036 (max is trial 1) | compiled=5 | 4,389,502.0 | 387,370,513.0 | 206,841.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_02902356_auto-caps-simdna` | 283,575,716.0 | 276,111,877.0 | 295,733,599.0 | 6,886,383.7 | 5 | 52,544 | 105,110 | 33,760 | 0.024 | compiled=5 | 7,559,209.0 | 268,870,880.0 | 126,821.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 295,760,879.0 | 293,203,976.0 | 302,838,666.0 | 3,229,025.8 | 5 | 52,632 | 112,465 | 35,304 | 0.011 (max is trial 1) | compiled=5 | 8,017,302.0 | 287,496,876.0 | 177,341.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 283,733,994.0 | 275,948,934.0 | 297,381,235.0 | 7,395,115.4 | 5 | 52,544 | 105,055 | 33,705 | 0.026 | compiled=5 | 8,599,234.0 | 270,600,876.0 | 110,761.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 293,975,557.0 | 292,483,290.0 | 298,484,961.0 | 2,137,949.1 | 5 | 52,632 | 112,410 | 35,249 | 0.007 (max is trial 1) | compiled=5 | 7,837,500.0 | 285,753,734.0 | 193,111.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_02902356_auto-caps-simdna` | 562,562,478.0 | 561,219,771.0 | 594,114,281.0 | 12,774,766.0 | 5 | 208,656 | 553,671 (warned) | 44,404 | 0.023 | compiled=5 | 57,414,179.0 | 505,252,319.0 | 100,781.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 584,255,100.0 | 578,788,762.0 | 587,614,919.0 | 3,458,060.0 | 5 | 212,840 | 568,461 (warned) | 45,692 | 0.006 | compiled=5 | 64,427,765.0 | 519,153,422.0 | 100,701.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 568,923,397.0 | 560,339,740.0 | 572,494,354.0 | 4,347,832.4 | 5 | 208,600 | 553,546 (warned) | 44,279 | 0.008 | compiled=5 | 57,012,296.0 | 512,225,181.0 | 98,471.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 591,149,620.0 | 584,717,147.0 | 599,346,593.0 | 5,580,505.3 | 5 | 212,792 | 568,336 (warned) | 45,567 | 0.009 (max is trial 1) | compiled=5 | 64,085,653.0 | 521,090,327.0 | 99,260.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_02902356_auto-caps-simdna` | 151,340,903.0 | 145,899,509.0 | 162,439,555.0 | 5,968,137.6 | 5 | 27,792 | 21,325 | 15,618 | 0.039 | compiled=5 | 2,010,979.0 | 149,233,544.0 | 193,391.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 167,827,129.0 | 164,869,317.0 | 169,465,149.0 | 1,605,057.6 | 5 | 27,936 | 23,569 | 16,962 | 0.010 | compiled=5 | 1,989,980.0 | 165,754,860.0 | 104,680.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 147,084,884.0 | 146,813,032.0 | 148,819,354.0 | 728,628.2 | 5 | 27,792 | 20,990 | 15,283 | 0.005 (max is trial 1) | compiled=5 | 1,792,159.0 | 145,106,084.0 | 187,261.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 165,167,699.0 | 147,212,694.0 | 166,275,564.0 | 7,239,064.9 | 5 | 27,936 | 23,162 | 16,555 | 0.044 | compiled=5 | 1,859,610.0 | 163,114,468.0 | 204,201.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 173,031,084.0 | 163,323,360.0 | 174,495,752.0 | 4,072,581.7 | 5 | 27,936 | 23,175 | 17,394 | 0.024 | compiled=5 | 1,886,598.0 | 171,041,485.0 | 112,610.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 161,294,120.0 | 158,513,327.0 | 168,208,792.0 | 3,885,366.0 | 5 | 27,936 | 22,747 | 16,966 | 0.024 | compiled=5 | 1,919,719.0 | 158,960,809.0 | 198,811.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 172,961,338.0 | 162,755,846.0 | 175,171,629.0 | 4,906,720.3 | 5 | 27,936 | 23,161 | 17,380 | 0.028 | compiled=5 | 1,808,099.0 | 171,047,129.0 | 103,140.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 159,792,111.0 | 150,029,361.0 | 168,093,094.0 | 6,690,299.2 | 5 | 27,936 | 22,733 | 16,952 | 0.042 | compiled=5 | 1,832,740.0 | 157,740,750.0 | 119,751.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna` | 223,019,948.0 | 212,639,978.0 | 235,379,945.0 | 7,305,895.4 | 5 | 31,968 | 31,978 | 27,144 | 0.033 (max is trial 1) | compiled=5 | 1,965,579.0 | 220,842,927.0 | 115,001.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 226,549,874.0 | 219,254,800.0 | 234,221,279.0 | 4,742,685.9 | 5 | 32,064 | 33,457 | 28,393 | 0.021 (max is trial 1) | compiled=5 | 1,975,149.0 | 224,481,324.0 | 103,061.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 220,904,957.0 | 215,091,057.0 | 229,444,873.0 | 4,666,168.7 | 5 | 31,968 | 31,987 | 27,153 | 0.021 (max is trial 1) | compiled=5 | 1,880,320.0 | 219,088,008.0 | 106,281.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 219,255,630.0 | 216,619,875.0 | 229,941,266.0 | 4,673,212.3 | 5 | 32,064 | 33,466 | 28,402 | 0.021 (max is trial 1) | compiled=5 | 1,884,100.0 | 217,126,969.0 | 101,550.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 147,010,445.0 | 141,100,084.0 | 147,544,529.0 | 2,423,674.6 | 5 | 27,616 | 15,572 | 13,215 | 0.016 | compiled=5 | 1,646,539.0 | 143,670,578.0 | 192,061.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 144,960,004.0 | 140,811,513.0 | 148,829,875.0 | 2,763,951.6 | 5 | 27,616 | 15,395 | 13,038 | 0.019 | compiled=5 | 1,627,789.0 | 142,254,310.0 | 199,671.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 148,405,054.0 | 130,475,088.0 | 150,590,735.0 | 8,293,307.0 | 5 | 27,616 | 15,576 | 13,219 | 0.056 | compiled=5 | 1,523,509.0 | 146,690,264.0 | 192,551.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 139,924,199.0 | 132,006,577.0 | 148,155,162.0 | 5,483,785.6 | 5 | 27,616 | 15,399 | 13,042 | 0.039 | compiled=5 | 1,560,539.0 | 138,262,919.0 | 109,061.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 319,124,980.0 | 306,564,465.0 | 320,182,985.0 | 5,061,663.7 | 5 | 40,960 | 45,787 | 40,759 | 0.016 | compiled=5 | 2,161,951.0 | 316,850,578.0 | 114,100.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 309,255,209.0 | 307,068,898.0 | 315,302,491.0 | 3,400,535.3 | 5 | 40,752 | 44,970 | 39,942 | 0.011 | compiled=5 | 2,177,061.0 | 304,925,337.0 | 196,301.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 319,119,255.0 | 306,132,275.0 | 319,372,656.0 | 5,238,229.9 | 5 | 40,960 | 45,791 | 40,763 | 0.016 | compiled=5 | 2,037,281.0 | 317,003,853.0 | 109,751.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 310,553,679.0 | 300,165,064.0 | 316,476,310.0 | 6,093,925.9 | 5 | 40,752 | 44,974 | 39,946 | 0.020 | compiled=5 | 2,112,981.0 | 308,345,597.0 | 188,431.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna` | 209,529,840.0 | 207,844,643.0 | 216,443,617.0 | 2,996,674.5 | 5 | 32,064 | 28,091 | 25,547 | 0.014 | compiled=5 | 1,846,170.0 | 207,646,571.0 | 112,190.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 203,430,178.0 | 198,829,524.0 | 211,917,983.0 | 4,981,310.1 | 5 | 31,984 | 27,831 | 25,287 | 0.024 | compiled=5 | 3,627,409.0 | 199,592,999.0 | 111,661.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 207,327,084.0 | 193,061,128.0 | 209,193,883.0 | 6,112,973.4 | 5 | 32,064 | 28,100 | 25,556 | 0.029 | compiled=5 | 1,702,269.0 | 205,506,504.0 | 115,661.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 202,196,607.0 | 192,440,345.0 | 219,243,808.0 | 8,990,550.5 | 5 | 31,984 | 27,840 | 25,296 | 0.044 | compiled=5 | 3,252,297.0 | 198,628,458.0 | 99,780.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_02902356_auto-caps-simdna` | 248,667,125.0 | 247,389,987.0 | 249,350,336.0 | 713,337.6 | 5 | 36,560 | 47,570 | 22,252 | 0.003 (max is trial 1) | compiled=5 | 3,139,197.0 | 244,844,735.0 | 114,061.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 254,578,446.0 | 237,743,136.0 | 260,078,933.0 | 8,557,911.3 | 5 | 36,704 | 50,547 | 23,956 | 0.034 | compiled=5 | 3,530,438.0 | 251,130,047.0 | 105,861.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 251,928,820.0 | 239,188,643.0 | 260,668,696.0 | 7,111,806.4 | 5 | 36,560 | 47,576 | 22,258 | 0.028 | compiled=5 | 6,682,285.0 | 245,047,654.0 | 198,881.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 246,373,520.0 | 245,030,813.0 | 254,006,441.0 | 3,720,543.7 | 5 | 36,704 | 50,553 | 23,962 | 0.015 | compiled=5 | 3,095,166.0 | 243,058,183.0 | 112,121.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_02902356_auto-caps-simdna` | 229,191,262.0 | 223,914,035.0 | 232,111,759.0 | 2,803,121.6 | 5 | 85,736 | 227,567 | 19,601 | 0.012 (max is trial 1) | compiled=5 | 14,409,165.0 | 212,936,348.0 | 202,591.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 237,999,609.0 | 227,990,656.0 | 264,816,148.0 | 12,497,419.2 | 5 | 89,968 | 237,398 | 21,577 | 0.053 | compiled=5 | 15,698,432.0 | 219,954,604.0 | 114,691.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 229,138,660.0 | 221,612,062.0 | 230,039,195.0 | 3,112,059.4 | 5 | 85,736 | 227,576 | 19,610 | 0.014 (max is trial 1) | compiled=5 | 14,175,804.0 | 214,523,564.0 | 101,731.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 237,893,685.0 | 234,587,650.0 | 256,657,094.0 | 8,092,482.5 | 5 | 89,968 | 237,407 | 21,586 | 0.034 (max is trial 1) | compiled=5 | 15,797,532.0 | 219,184,738.0 | 194,901.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_02902356_auto-caps-simdna` | 189,777,328.0 | 179,414,043.0 | 205,820,181.0 | 10,879,652.8 | 5 | 36,480 | 57,983 | 17,583 | 0.057 | compiled=5 | 4,437,913.0 | 185,234,484.0 | 112,400.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 201,473,079.0 | 199,305,187.0 | 208,614,054.0 | 3,890,559.5 | 5 | 36,624 | 61,762 | 19,374 | 0.019 (max is trial 1) | compiled=5 | 5,971,871.0 | 196,218,491.0 | 190,701.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 194,394,401.0 | 188,414,199.0 | 202,041,950.0 | 4,352,980.9 | 5 | 36,432 | 57,858 | 17,458 | 0.022 | compiled=5 | 5,223,447.0 | 189,816,036.0 | 102,671.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 202,012,429.0 | 195,680,407.0 | 205,218,176.0 | 3,585,760.2 | 5 | 36,568 | 61,637 | 19,249 | 0.018 | compiled=5 | 4,932,715.0 | 191,944,808.0 | 108,470.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_02902356_auto-caps-simdna` | 163,497,120.0 | 153,596,240.0 | 175,232,262.0 | 7,735,900.2 | 5 | 32,152 | 36,533 | 15,366 | 0.047 | compiled=5 | 3,220,967.0 | 160,079,823.0 | 103,531.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 174,634,920.0 | 173,275,822.0 | 183,728,935.0 | 4,388,530.0 | 5 | 32,296 | 39,557 | 17,378 | 0.025 | compiled=5 | 3,343,477.0 | 170,707,648.0 | 101,411.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 162,250,893.0 | 162,002,533.0 | 171,258,299.0 | 4,224,188.9 | 5 | 32,152 | 36,542 | 15,375 | 0.026 (max is trial 1) | compiled=5 | 3,104,696.0 | 159,032,116.0 | 101,580.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 178,625,399.0 | 173,597,293.0 | 182,896,531.0 | 3,401,096.3 | 5 | 32,296 | 39,566 | 17,387 | 0.019 | compiled=5 | 3,230,197.0 | 171,524,321.0 | 190,161.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_02902356_auto-caps-simdna` | 1,458,152,128.0 | 1,429,600,059.0 | 1,482,915,127.0 | 19,768,038.2 | 5 | 680,448 | 394,628 (warned) | 100,148 | 0.014 | compiled=5 | 12,683,376.0 | 1,442,632,247.0 | 527,822.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 1,390,345,675.0 | 1,368,604,382.0 | 1,399,114,831.0 | 10,678,984.5 | 5 | 659,912 | 401,834 (warned) | 102,298 | 0.008 | compiled=5 | 13,089,838.0 | 1,377,098,256.0 | 284,651.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,452,257,635.0 | 1,413,869,967.0 | 1,485,509,307.0 | 26,597,665.6 | 5 | 680,448 | 394,637 (warned) | 100,157 | 0.018 | compiled=5 | 12,431,815.0 | 1,439,637,590.0 | 303,151.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 1,389,218,479.0 | 1,375,835,288.0 | 1,413,011,641.0 | 12,099,094.6 | 5 | 659,912 | 401,843 (warned) | 102,307 | 0.009 (max is trial 1) | compiled=5 | 12,667,845.0 | 1,376,092,450.0 | 287,681.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_02902356_auto-caps-simdna` | 158,663,416.0 | 155,513,879.0 | 160,131,514.0 | 1,680,890.4 | 5 | 27,792 | 21,230 | 15,318 | 0.011 | compiled=5 | 2,091,171.0 | 155,211,357.0 | 210,731.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 172,289,356.0 | 167,989,804.0 | 178,167,247.0 | 3,366,296.1 | 5 | 27,936 | 23,837 | 17,407 | 0.020 (max is trial 1) | compiled=5 | 2,120,791.0 | 169,968,264.0 | 172,811.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 157,861,990.0 | 139,166,042.0 | 159,285,098.0 | 7,674,365.5 | 5 | 27,792 | 20,729 | 14,817 | 0.049 | compiled=5 | 1,925,160.0 | 155,679,339.0 | 186,931.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 166,687,936.0 | 158,685,034.0 | 167,085,058.0 | 3,462,351.8 | 5 | 27,936 | 23,336 | 16,906 | 0.021 | compiled=5 | 1,980,200.0 | 164,620,125.0 | 115,141.0 |
| `winpath-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna` | 135,167,833.0 | 134,530,291.0 | 148,679,943.0 | 6,699,706.4 | 5 | 27,576 | 14,961 | 12,878 | 0.050 | compiled=5 | 1,605,008.0 | 133,360,644.0 | 194,471.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna` | 140,141,629.0 | 125,986,237.0 | 148,527,122.0 | 8,241,331.0 | 5 | 27,536 | 14,784 | 12,701 | 0.059 | compiled=5 | 1,630,418.0 | 138,396,580.0 | 104,720.0 |
| `winpath-near-miss` | `plain` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 135,878,997.0 | 130,253,657.0 | 146,394,830.0 | 5,342,144.5 | 5 | 27,576 | 14,963 | 12,880 | 0.039 | compiled=5 | 1,488,947.0 | 134,318,148.0 | 101,691.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_02902356_auto-caps-simdna_noreqbyte` | 139,722,096.0 | 133,134,341.0 | 146,251,940.0 | 5,433,438.0 | 5 | 27,536 | 14,786 | 12,703 | 0.039 | compiled=5 | 1,508,478.0 | 136,169,557.0 | 207,311.0 |

