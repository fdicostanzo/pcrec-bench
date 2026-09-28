# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, machine=budu-ryzen1600, testee=pcrec_a32bc86e_auto-caps-simdna, testee=pcrec_a32bc86e_auto-caps-simdna_nolitrun
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 37.5% (`pcrec_a32bc86e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput`)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T050936Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna/capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T050936Z.jsonl) — agreement: agree (0 of 124 groups; 3 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun__budu-ryzen1600__20260928T054501Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna_nolitrun/capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun__budu-ryzen1600__20260928T054501Z.jsonl) — agreement: agree (0 of 72 groups; 0 of 2806 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
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

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,121,812.8 | 3.7216 | 5,118,691.5 | 5,135,536.5 | 6,238.1 | 1.000x | 1.000x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,906,396.4 | 3.7254 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 971,810.5 | 3.7072 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 243,481.1 | 3.7152 |

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,032.1 | 1,028.5 | 1,033.6 | 2.0 | 1.000x | 1.000x | 75 | 13.8 | 8.9 | 100% |

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 18.0 | 0.0000 | 17.8 | 19.1 | 0.5 | 1.003x | 1.003x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.0 | 0.0001 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 526.0 | 515.3 | 531.4 | 5.5 | 1.000x | 1.000x | 75 | 7.0 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 529.9 | 528.4 | 537.0 | 3.6 | 1.007x | 1.007x | 75 | 7.1 | 8.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 72.2 | 0.0001 | 71.8 | 75.6 | 1.4 | 1.000x | 1.000x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 24.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0004 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,877.7 | 1,876.3 | 1,879.3 | 1.1 | 1.000x | 1.000x | 75 | 25.0 | 8.9 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 607,173.5 | 0.4412 | 600,425.0 | 633,089.0 | 13,295.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 612,600.4 | 0.4451 | 601,889.3 | 621,806.6 | 6,544.9 | 1.009x | 1.009x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 466,998.5 | 0.4454 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 469,869.1 | 0.4481 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 109,719.3 | 0.4185 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 113,903.8 | 0.4345 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 27,339.2 | 0.4172 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,827.6 | 0.4399 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 891.1 | 889.6 | 899.6 | 3.6 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 897.9 | 890.9 | 899.2 | 3.1 | 1.008x | 1.008x | 75 | 12.0 | 8.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 617,546.3 | 0.4487 | 605,351.4 | 625,596.8 | 7,436.8 | 1.000x | 1.000x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 478,271.8 | 0.4561 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 111,988.5 | 0.4272 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,085.6 | 0.4286 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 896.9 | 890.7 | 900.0 | 3.2 | 1.000x | 1.000x | 75 | 12.0 | 8.9 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,250,842.7 | 8.1750 | 11,231,460.5 | 11,276,995.3 | 16,408.8 | 1.000x | 1.000x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 8,566,899.3 | 8.1700 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,133,996.2 | 8.1405 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 536,132.8 | 8.1807 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,151.2 | 5,149.9 | 5,154.3 | 1.6 | 1.000x | 1.000x | 75 | 68.7 | 8.9 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 31.1 | 0.0000 | 31.1 | 31.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 31.2 | 0.0000 | 31.2 | 31.4 | 0.1 | 1.003x | 1.003x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0002 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 842.2 | 842.1 | 872.8 | 12.1 | 1.000x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 843.8 | 841.8 | 846.3 | 1.6 | 1.002x | 1.002x | 75 | 11.3 | 8.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 25,397,237.5 | 18.4539 | 25,330,273.5 | 25,795,402.5 | 170,457.7 | 1.000x | 1.000x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 19,378,506.7 | 18.4808 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,827,430.0 | 18.4152 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,201,982.7 | 18.3408 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 20,793.3 | 20,780.9 | 21,108.7 | 126.7 | 1.000x | 1.000x | 75 | 277.2 | 8.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,127.3 | 0.0168 | 23,103.4 | 23,169.9 | 25.9 | 1.000x | 1.000x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,631.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,390.0 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.7 | 0.0169 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,188.3 | 1,169.7 | 1,195.7 | 11.2 | 1.000x | 1.000x | 75 | 15.8 | 8.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,003.0 | 0.0007 | 996.6 | 1,006.8 | 3.3 | 1.000x | 1.000x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 233.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 456.5 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 311.4 | 0.0048 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,623.1 | 10,614.6 | 10,631.4 | 5.7 | 1.000x | 1.000x | 75 | 141.6 | 8.9 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 46.6 | 0.0000 | 45.7 | 117.2 | 28.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 47.6 | 0.0000 | 46.5 | 53.5 | 2.6 | 1.022x | 1.022x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 16.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 15.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 14.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.0 | 0.0002 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,366.2 | 1,365.1 | 1,372.3 | 2.6 | 1.000x | 1.000x | 75 | 18.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,372.3 | 1,359.2 | 1,407.9 | 21.4 | 1.004x | 1.004x | 75 | 18.3 | 8.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,981.9 | 0.0087 | 11,650.2 | 12,069.5 | 180.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 12,049.1 | 0.0088 | 11,642.0 | 12,126.8 | 174.6 | 1.006x | 1.006x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,164.3 | 0.0011 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,166.8 | 0.0011 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 45.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 45.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,761.4 | 0.1642 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10,825.2 | 0.1652 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 255,373.5 | 0.1856 | 255,301.5 | 255,444.1 | 46.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 255,529.7 | 0.1857 | 255,321.6 | 255,783.2 | 169.9 | 1.001x | 1.001x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 202,416.1 | 0.1930 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 202,381.0 | 0.1930 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 44,336.2 | 0.1691 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 44,439.5 | 0.1695 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 8,649.1 | 0.1320 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 8,699.7 | 0.1327 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 687.5 | 687.2 | 687.6 | 0.2 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 687.7 | 687.1 | 688.0 | 0.3 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,906,684.5 | 1.3854 | 1,900,903.9 | 1,910,994.8 | 3,501.6 | 1.000x | 1.000x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,459,605.4 | 1.3920 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 358,737.6 | 1.3685 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 87,361.2 | 1.3330 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,641.8 | 1,639.1 | 1,658.6 | 7.8 | 1.000x | 1.000x | 75 | 21.9 | 8.9 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,118.4 | 0.0168 | 23,102.6 | 23,133.7 | 10.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,140.4 | 0.0168 | 23,121.9 | 23,183.3 | 20.6 | 1.001x | 1.001x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,636.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,649.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,375.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,386.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,106.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,104.9 | 0.0169 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 665.0 | 661.5 | 670.5 | 2.9 | 1.000x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 668.9 | 667.3 | 670.7 | 1.2 | 1.006x | 1.006x | 75 | 8.9 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 482,995.3 | 0.3509 | 482,657.2 | 484,361.8 | 613.3 | 1.000x | 1.000x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 367,939.9 | 0.3509 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 91,962.7 | 0.3508 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 23,071.8 | 0.3520 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,116.4 | 1,109.7 | 1,118.4 | 3.1 | 1.000x | 1.000x | 75 | 14.9 | 8.9 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 15.1 | 0.0000 | 15.1 | 15.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.9 | 0.3 | 1.005x | 1.005x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0001 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 404.5 | 404.0 | 405.8 | 0.7 | 1.000x | 1.000x | 75 | 5.4 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 406.3 | 404.5 | 407.9 | 1.2 | 1.004x | 1.004x | 75 | 5.4 | 8.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 682,276.5 | 0.4957 | 682,063.1 | 687,203.4 | 1,955.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 686,528.2 | 0.4988 | 682,695.3 | 691,094.9 | 3,183.0 | 1.006x | 1.006x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 527,395.6 | 0.5030 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 531,688.6 | 0.5071 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 126,209.2 | 0.4814 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 126,801.5 | 0.4837 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 28,741.9 | 0.4386 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,760.9 | 0.4389 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 769.5 | 767.2 | 772.3 | 1.8 | 1.000x | 1.000x | 75 | 10.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 771.8 | 770.1 | 774.1 | 1.4 | 1.003x | 1.003x | 75 | 10.3 | 8.9 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 33.0 | 0.0000 | 32.9 | 33.1 | 0.1 | 1.000x | 1.000x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11.5 | 0.0002 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 834.9 | 833.0 | 835.3 | 1.0 | 1.000x | 1.000x | 75 | 11.1 | 8.9 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 30.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 34.2 | 0.0000 | 34.0 | 34.5 | 0.2 | 1.107x | 1.107x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.1 | 0.0002 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 797.4 | 795.8 | 846.8 | 19.7 | 1.000x | 1.000x | 75 | 10.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 862.8 | 862.7 | 879.6 | 6.7 | 1.082x | 1.082x | 75 | 11.5 | 8.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,106.6 | 0.0168 | 23,102.7 | 23,156.7 | 20.2 | 1.000x | 1.000x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,624.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,382.5 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,105.6 | 0.0169 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 690.7 | 682.4 | 702.8 | 6.5 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,153.1 | 0.0168 | 23,134.4 | 23,167.2 | 10.7 | 1.000x | 1.000x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,660.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,385.9 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,107.8 | 0.0169 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,580.8 | 1,544.9 | 1,671.5 | 43.2 | 1.000x | 1.000x | 75 | 21.1 | 8.9 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.5 | 28.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 28.6 | 0.0000 | 28.6 | 29.5 | 0.4 | 1.004x | 1.004x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.6 | 0.0001 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 811.9 | 797.4 | 858.5 | 20.7 | 1.000x | 1.000x | 75 | 10.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 813.5 | 798.8 | 823.5 | 8.4 | 1.002x | 1.002x | 75 | 10.8 | 8.9 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 30.8 | 0.0000 | 30.6 | 30.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 31.1 | 0.1 | 1.003x | 1.003x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0002 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 884.6 | 883.4 | 889.3 | 2.2 | 1.000x | 1.000x | 75 | 11.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 888.2 | 884.6 | 921.5 | 13.9 | 1.004x | 1.004x | 75 | 11.8 | 8.9 | 100% |

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,527,078.6 | 4.7426 | 6,501,439.2 | 6,539,980.8 | 17,015.3 | 1.000x | 1.000x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 4,982,322.9 | 4.7515 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,235,356.8 | 4.7125 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 309,420.2 | 4.7214 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,701.4 | 6,662.5 | 6,721.3 | 22.1 | 1.000x | 1.000x | 75 | 89.4 | 8.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 224.3 | 0.0002 | 223.7 | 229.2 | 2.0 | 1.000x | 1.000x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 58.6 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 96.0 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 69.7 | 0.0011 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,097.4 | 12,078.0 | 12,184.1 | 36.8 | 1.000x | 1.000x | 75 | 161.3 | 8.9 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,041,101.1 | 7.2960 | 9,962,633.3 | 10,087,934.7 | 45,487.3 | 1.000x | 1.000x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 7,663,257.1 | 7.3083 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,902,527.8 | 7.2576 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 473,280.3 | 7.2217 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,235.4 | 10,856.6 | 17,974.0 | 2,765.9 | 1.000x | 1.000x | 75 | 149.8 | 8.9 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 343,303.0 | 0.2494 | 343,087.4 | 343,319.9 | 87.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 343,342.4 | 0.2495 | 342,841.9 | 343,496.4 | 226.0 | 1.000x | 1.000x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 264,023.3 | 0.2518 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 263,974.7 | 0.2517 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 64,468.0 | 0.2459 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 64,561.0 | 0.2463 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 14,755.1 | 0.2251 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 14,618.0 | 0.2231 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 692.9 | 691.6 | 693.3 | 0.6 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 693.1 | 691.1 | 744.1 | 20.8 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,136.4 | 0.0168 | 23,102.2 | 23,175.5 | 25.7 | 1.000x | 1.000x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,639.9 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,375.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.8 | 0.0169 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,160.8 | 1,155.8 | 1,163.9 | 2.9 | 1.000x | 1.000x | 75 | 15.5 | 8.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,133.0 | 0.0168 | 23,114.4 | 23,160.7 | 16.3 | 1.000x | 1.000x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,628.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,388.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.4 | 0.0169 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,166.3 | 1,163.6 | 1,178.6 | 5.5 | 1.000x | 1.000x | 75 | 15.6 | 8.9 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 47.4 | 0.0000 | 47.2 | 47.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 47.5 | 0.0000 | 47.0 | 48.0 | 0.4 | 1.002x | 1.002x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 15.9 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.8 | 0.0002 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 10,190,515.6 | 10,183,913.1 | 10,207,379.4 | 9,044.6 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 135,873.5 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,196,908.0 | 10,146,637.8 | 10,998,449.7 | 325,678.6 | 1.001x | 1.001x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 135,958.8 | 8.9 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 480,361.3 | 0.3490 | 478,893.9 | 481,452.9 | 903.3 | 1.000x | 1.000x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 366,655.7 | 0.3497 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 91,113.4 | 0.3476 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 22,548.3 | 0.3441 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,254.8 | 1,251.0 | 1,257.7 | 2.4 | 1.000x | 1.000x | 75 | 16.7 | 8.9 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.1 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.001x | 1.001x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0001 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 525.7 | 524.3 | 527.0 | 1.1 | 1.000x | 1.000x | 75 | 7.0 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 526.3 | 524.6 | 535.9 | 4.2 | 1.001x | 1.001x | 75 | 7.0 | 8.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 218,991.9 | 0.1591 | 218,846.9 | 219,208.3 | 128.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 219,277.7 | 0.1593 | 219,044.1 | 219,614.5 | 200.1 | 1.001x | 1.001x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 168,398.6 | 0.1606 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 168,628.8 | 0.1608 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 40,355.0 | 0.1539 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 40,435.4 | 0.1542 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10,279.8 | 0.1569 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,163.6 | 0.1551 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 696.4 | 689.2 | 700.9 | 3.9 | 1.000x | 1.000x | 75 | 9.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 702.1 | 683.6 | 705.0 | 8.8 | 1.008x | 1.008x | 75 | 9.4 | 8.9 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,195,590.8 | 3.0486 | 4,193,420.8 | 4,198,404.0 | 1,855.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,196,748.3 | 3.0494 | 4,194,381.6 | 4,196,857.6 | 996.0 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,198,047.5 | 3.0499 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,198,552.8 | 3.0504 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 800,127.7 | 3.0522 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 799,833.1 | 3.0511 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 197,951.0 | 3.0205 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 198,339.0 | 3.0264 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,481.5 | 2,476.6 | 2,484.4 | 2.6 | 1.000x | 1.000x | 75 | 33.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,499.3 | 2,496.6 | 2,501.7 | 1.7 | 1.007x | 1.007x | 75 | 33.3 | 8.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,103,164.2 | 1.5282 | 2,096,855.3 | 2,119,227.7 | 8,658.3 | 1.000x | 1.000x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,608,488.7 | 1.5340 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 392,760.0 | 1.4983 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 99,781.6 | 1.5225 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,510.4 | 1,499.4 | 1,514.8 | 5.3 | 1.000x | 1.000x | 75 | 20.1 | 8.9 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,111.9 | 0.0168 | 23,100.5 | 23,138.1 | 13.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,132.2 | 0.0168 | 23,107.8 | 23,144.0 | 13.2 | 1.001x | 1.001x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,615.0 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,625.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,386.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,384.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,110.6 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,105.4 | 0.0169 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 669.6 | 664.4 | 685.7 | 7.9 | 1.000x | 1.000x | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 678.7 | 678.3 | 684.0 | 2.3 | 1.014x | 1.014x | 75 | 9.0 | 8.9 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,118.9 | 0.0168 | 23,104.3 | 23,128.7 | 9.1 | 1.000x | 1.000x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,624.8 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,385.6 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.5 | 0.0169 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 740.0 | 723.9 | 747.4 | 8.3 | 1.000x | 1.000x | 75 | 9.9 | 8.9 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 38.1 | 0.0000 | 34.0 | 38.2 | 1.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 38.1 | 0.0000 | 37.7 | 38.2 | 0.2 | 1.001x | 1.001x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0002 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,023.5 | 1,023.1 | 1,024.8 | 0.6 | 1.000x | 1.000x | 75 | 13.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,026.0 | 1,022.6 | 1,034.6 | 5.0 | 1.002x | 1.002x | 75 | 13.7 | 8.9 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,036,307.3 | 2.9328 | 4,032,384.6 | 4,047,641.1 | 5,464.6 | 1.000x | 1.000x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,090,915.0 | 2.9477 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 761,201.2 | 2.9038 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 184,191.1 | 2.8105 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,493.7 | 2,491.3 | 2,515.5 | 9.2 | 1.000x | 1.000x | 75 | 33.2 | 8.9 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,009,035.4 | 2.9130 | 4,006,596.2 | 4,057,578.9 | 19,424.4 | 1.000x | 1.000x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,072,811.9 | 2.9305 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 754,449.0 | 2.8780 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 182,856.9 | 2.7902 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,457.3 | 2,444.5 | 2,546.6 | 38.1 | 1.000x | 1.000x | 75 | 32.8 | 8.9 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 937,630.0 | 0.6813 | 936,830.0 | 937,865.9 | 373.3 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 717,355.9 | 0.6841 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 175,659.3 | 0.6701 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 44,515.8 | 0.6793 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,888.6 | 1,886.0 | 1,896.0 | 3.8 | 1.000x | 1.000x | 75 | 25.2 | 8.9 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 930,496.2 | 0.6761 | 928,955.6 | 947,710.2 | 7,111.7 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 711,919.3 | 0.6789 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 174,575.9 | 0.6660 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 43,961.5 | 0.6708 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,832.2 | 1,830.5 | 1,837.5 | 3.0 | 1.000x | 1.000x | 75 | 24.4 | 8.9 | 100% |

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,987,580.5 | 2.8974 | 3,984,588.0 | 3,992,062.5 | 2,426.2 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,037,481.5 | 2.8968 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 760,214.9 | 2.9000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 190,362.8 | 2.9047 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,770.5 | 1,765.7 | 1,801.4 | 13.3 | 1.000x | 1.000x | 75 | 23.6 | 8.9 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,147.8 | 0.0168 | 23,138.1 | 23,159.0 | 7.0 | 1.000x | 1.000x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,658.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,376.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,111.6 | 0.0170 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 932.5 | 929.4 | 934.7 | 1.8 | 1.000x | 1.000x | 75 | 12.4 | 8.9 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 3,940,751.9 | 2.8634 | 3,940,523.7 | 3,944,949.3 | 1,664.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,084,696.9 | 2.9680 | 4,082,641.2 | 4,086,504.9 | 1,266.7 | 1.037x | 1.037x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,002,419.5 | 2.8633 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,111,755.0 | 2.9676 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 751,402.1 | 2.8664 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 779,128.6 | 2.9721 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 187,518.9 | 2.8613 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 192,843.9 | 2.9426 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,188.8 | 1,187.2 | 1,189.5 | 0.8 | 1.000x | 1.000x | 75 | 15.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,212.0 | 1,210.3 | 1,214.7 | 1.7 | 1.020x | 1.020x | 75 | 16.2 | 8.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 124,514.1 | 0.0905 | 124,312.2 | 124,567.9 | 91.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 124,697.0 | 0.0906 | 124,525.4 | 124,867.0 | 119.5 | 1.001x | 1.001x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 102,065.6 | 0.0973 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 102,182.4 | 0.0974 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 18,919.6 | 0.0722 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 18,891.9 | 0.0721 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,462.2 | 0.0528 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 3,651.5 | 0.0557 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,515.5 | 1,511.3 | 1,523.0 | 4.3 | 1.000x | 1.000x | 75 | 20.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,517.5 | 1,514.0 | 1,520.0 | 2.0 | 1.001x | 1.001x | 75 | 20.2 | 8.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 354,080.6 | 0.2573 | 353,969.0 | 354,772.6 | 296.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 354,258.9 | 0.2574 | 354,067.0 | 354,609.0 | 189.7 | 1.001x | 1.001x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 271,795.8 | 0.2592 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 271,924.5 | 0.2593 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 67,033.8 | 0.2557 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 66,946.6 | 0.2554 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15,259.6 | 0.2328 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15,377.6 | 0.2346 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,267.3 | 1,263.7 | 1,275.1 | 4.2 | 1.000x | 1.000x | 75 | 16.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,312.5 | 1,306.1 | 1,327.5 | 7.8 | 1.036x | 1.036x | 75 | 17.5 | 8.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,133.6 | 0.0168 | 23,115.4 | 23,151.6 | 14.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,149.2 | 0.0168 | 23,137.1 | 23,228.4 | 33.1 | 1.001x | 1.001x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,629.0 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,649.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,386.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,388.3 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,112.4 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,110.0 | 0.0169 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,045.5 | 1,043.7 | 1,047.1 | 1.1 | 1.000x | 1.000x | 75 | 13.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,075.3 | 1,072.6 | 1,079.7 | 2.3 | 1.029x | 1.029x | 75 | 14.3 | 8.9 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 352,040.3 | 0.2558 | 351,914.8 | 352,663.6 | 330.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 352,562.7 | 0.2562 | 352,177.2 | 354,404.1 | 814.1 | 1.001x | 1.001x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 282,824.7 | 0.2697 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 283,193.9 | 0.2701 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 58,399.9 | 0.2228 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 58,272.1 | 0.2223 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11,027.6 | 0.1683 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11,157.8 | 0.1703 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 659.6 | 659.1 | 660.8 | 0.6 | 1.000x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 660.8 | 658.4 | 661.6 | 1.4 | 1.002x | 1.002x | 75 | 8.8 | 8.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 40.0 | 0.0000 | 40.0 | 40.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 40.0 | 0.0000 | 40.0 | 40.6 | 0.3 | 1.000x | 1.000x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 13.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 13.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 13.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 13.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 13.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 13.4 | 0.0002 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 914.0 | 913.0 | 920.9 | 2.9 | 1.000x | 1.000x | 75 | 12.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 915.4 | 913.2 | 941.0 | 10.3 | 1.002x | 1.002x | 75 | 12.2 | 8.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 6,965,058.8 | 5.0609 | 6,940,000.5 | 6,988,159.9 | 19,292.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,003,254.1 | 5.0886 | 6,988,301.5 | 7,009,588.0 | 7,476.6 | 1.005x | 1.005x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5,347,268.5 | 5.0996 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5,375,672.2 | 5.1266 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,300,911.2 | 4.9626 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,309,101.3 | 4.9938 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 315,012.7 | 4.8067 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 316,598.6 | 4.8309 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 3,094.7 | 3,092.4 | 3,210.2 | 45.8 | 1.000x | 1.000x | 75 | 41.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,100.2 | 3,067.1 | 3,129.5 | 21.9 | 1.002x | 1.002x | 75 | 41.3 | 8.9 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 38.0 | 0.0000 | 37.3 | 40.4 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 39.1 | 0.0000 | 38.0 | 40.9 | 1.1 | 1.031x | 1.031x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 14.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 12.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.5 | 0.0002 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,000.6 | 999.0 | 1,005.1 | 2.5 | 1.000x | 1.000x | 75 | 13.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,011.6 | 1,009.4 | 1,014.9 | 1.8 | 1.011x | 1.011x | 75 | 13.5 | 8.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 0.0000 | 29.4 | 29.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 31.3 | 0.0000 | 29.4 | 31.8 | 1.1 | 1.065x | 1.065x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0001 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 804.2 | 803.6 | 805.9 | 0.9 | 1.000x | 1.000x | 75 | 10.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 805.3 | 805.0 | 808.8 | 1.4 | 1.001x | 1.001x | 75 | 10.7 | 8.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.0 | 0.0000 | 29.0 | 29.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 29.3 | 0.0000 | 29.3 | 29.6 | 0.1 | 1.009x | 1.009x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0001 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 755.7 | 754.8 | 759.4 | 1.7 | 1.000x | 1.000x | 75 | 10.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 757.8 | 756.0 | 774.0 | 6.6 | 1.003x | 1.003x | 75 | 10.1 | 8.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 82,339.2 | 0.0598 | 82,098.2 | 82,936.8 | 300.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 82,346.5 | 0.0598 | 82,213.4 | 82,613.1 | 131.5 | 1.000x | 1.000x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 68,352.6 | 0.0652 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 68,126.4 | 0.0650 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11,583.9 | 0.0442 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11,752.0 | 0.0448 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 2,413.8 | 0.0368 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 2,458.3 | 0.0375 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 689.3 | 688.6 | 691.7 | 1.1 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 695.3 | 689.7 | 698.2 | 3.4 | 1.009x | 1.009x | 75 | 9.3 | 8.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,079,247.3 | 2.9640 | 4,078,076.5 | 4,088,393.5 | 3,796.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,079,777.3 | 2.9644 | 4,076,518.1 | 4,092,570.0 | 5,839.3 | 1.000x | 1.000x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,110,982.0 | 2.9669 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,112,908.6 | 2.9687 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 776,048.0 | 2.9604 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 775,894.4 | 2.9598 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 191,871.7 | 2.9277 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 191,650.4 | 2.9244 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,692.3 | 2,682.6 | 2,713.6 | 10.4 | 1.000x | 1.000x | 75 | 35.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,695.7 | 2,692.0 | 2,702.2 | 3.7 | 1.001x | 1.001x | 75 | 35.9 | 8.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,358,812.3 | 0.9873 | 1,356,860.3 | 1,363,536.2 | 2,365.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,359,762.7 | 0.9880 | 1,355,161.4 | 1,361,297.0 | 2,306.1 | 1.001x | 1.001x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,031,315.4 | 0.9835 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,030,597.3 | 0.9829 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 258,361.5 | 0.9856 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 259,551.0 | 0.9901 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 68,913.4 | 1.0515 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 68,054.4 | 1.0384 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 667.8 | 667.4 | 675.2 | 3.0 | 1.000x | 1.000x | 75 | 8.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 672.0 | 670.7 | 684.1 | 4.9 | 1.006x | 1.006x | 75 | 9.0 | 8.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 999,148.7 | 0.7260 | 997,095.8 | 999,792.2 | 1,025.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,010,496.3 | 0.7342 | 999,595.7 | 1,014,921.8 | 5,707.0 | 1.011x | 1.011x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 757,984.8 | 0.7229 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 760,313.9 | 0.7251 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 191,125.4 | 0.7291 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 200,536.6 | 0.7650 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 50,243.5 | 0.7667 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 48,712.3 | 0.7433 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,157.9 | 1,147.5 | 1,171.2 | 8.3 | 1.000x | 1.000x | 75 | 15.4 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,158.0 | 1,139.8 | 1,170.7 | 10.2 | 1.000x | 1.000x | 75 | 15.4 | 8.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,118,975.0 | 8.8058 | 12,103,560.3 | 12,151,845.6 | 17,642.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 12,139,709.3 | 8.8208 | 12,109,252.3 | 12,151,178.0 | 15,473.2 | 1.002x | 1.002x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9,234,402.1 | 8.8066 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9,258,728.5 | 8.8298 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,303,374.4 | 8.7867 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 2,302,721.1 | 8.7842 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 576,707.5 | 8.7999 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 575,934.6 | 8.7881 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,342.1 | 7,322.8 | 7,468.5 | 53.1 | 1.000x | 1.000x | 75 | 97.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 7,350.4 | 7,324.4 | 7,386.7 | 23.7 | 1.001x | 1.001x | 75 | 98.0 | 8.9 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,131.1 | 0.0168 | 23,100.4 | 23,173.5 | 25.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,137.1 | 0.0168 | 23,118.4 | 23,144.4 | 9.0 | 1.000x | 1.000x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,633.8 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,625.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,389.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,407.1 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,105.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.8 | 0.0169 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 694.3 | 692.4 | 696.3 | 1.4 | 1.000x | 1.000x | 75 | 9.3 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 697.7 | 693.9 | 703.2 | 3.2 | 1.005x | 1.005x | 75 | 9.3 | 8.9 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 19.6 | 0.0000 | 19.6 | 19.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 19.7 | 0.0000 | 19.6 | 19.7 | 0.0 | 1.001x | 1.001x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 6.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0001 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 457.1 | 454.3 | 1,405.6 | 379.8 | 1.000x | 1.000x | 75 | 6.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 457.3 | 455.9 | 467.7 | 4.4 | 1.000x | 1.000x | 75 | 6.1 | 8.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
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
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 208,452,842.0 | 206,383,151.0 | 221,662,851.0 | 5,752,093.9 | 5 | 31,768 | 26,113 | 25,828 | 0.028 | compiled=5 | 1,702,399.0 | 205,189,185.0 | 204,941.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 214,373,012.0 | 206,883,884.0 | 219,042,827.0 | 4,245,280.6 | 5 | 31,768 | 26,331 | 26,046 | 0.020 | compiled=5 | 1,675,508.0 | 212,511,383.0 | 189,381.0 |
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 145,371,950.0 | 138,568,735.0 | 153,278,962.0 | 5,696,775.1 | 5 | 27,736 | 16,705 | 14,320 | 0.039 | compiled=5 | 1,783,989.0 | 143,339,570.0 | 102,021.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 147,682,043.0 | 144,237,525.0 | 148,994,101.0 | 1,743,208.2 | 5 | 27,656 | 16,158 | 13,773 | 0.012 | compiled=5 | 1,639,749.0 | 145,956,264.0 | 101,290.0 |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 152,797,205.0 | 142,759,144.0 | 153,664,870.0 | 4,721,125.0 | 5 | 27,736 | 16,705 | 14,320 | 0.031 | compiled=5 | 1,561,098.0 | 150,645,595.0 | 177,071.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 136,819,222.0 | 136,423,250.0 | 148,315,522.0 | 5,060,072.0 | 5 | 27,656 | 16,158 | 13,773 | 0.037 | compiled=5 | 1,780,669.0 | 134,672,930.0 | 182,871.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 225,221,190.0 | 213,123,235.0 | 225,745,301.0 | 4,891,966.1 | 5 | 31,728 | 26,549 | 26,234 | 0.022 | compiled=5 | 1,726,719.0 | 223,410,240.0 | 108,421.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 224,776,286.0 | 220,602,345.0 | 225,617,432.0 | 1,782,794.7 | 5 | 31,728 | 26,664 | 26,349 | 0.008 | compiled=5 | 1,719,029.0 | 222,978,837.0 | 113,031.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 350,123,883.0 | 340,140,481.0 | 351,826,391.0 | 4,347,160.1 | 5 | 32,072 | 35,699 | 27,100 | 0.012 | compiled=5 | 2,209,132.0 | 347,823,051.0 | 101,380.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 358,195,095.0 | 354,131,313.0 | 365,237,353.0 | 3,630,449.7 | 5 | 32,120 | 35,420 | 27,908 | 0.010 | compiled=5 | 2,163,552.0 | 355,949,114.0 | 102,980.0 |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 353,292,593.0 | 351,143,201.0 | 356,953,292.0 | 2,081,682.8 | 5 | 32,072 | 35,699 | 27,100 | 0.006 (max is trial 1) | compiled=5 | 2,111,971.0 | 351,080,712.0 | 114,491.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 353,965,816.0 | 351,456,613.0 | 360,405,510.0 | 3,655,739.3 | 5 | 32,120 | 35,420 | 27,908 | 0.010 | compiled=5 | 2,070,571.0 | 351,528,044.0 | 104,940.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 350,966,168.0 | 345,076,116.0 | 352,303,174.0 | 2,606,224.1 | 5 | 32,104 | 36,025 | 27,347 | 0.007 | compiled=5 | 2,200,982.0 | 348,572,585.0 | 106,981.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 353,496,450.0 | 349,871,930.0 | 365,418,924.0 | 5,723,797.7 | 5 | 32,160 | 35,750 | 28,159 | 0.016 | compiled=5 | 2,239,491.0 | 348,776,786.0 | 191,791.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 224,600,066.0 | 218,829,576.0 | 228,270,424.0 | 3,168,047.0 | 5 | 32,088 | 32,984 | 27,353 | 0.014 | compiled=5 | 4,057,342.0 | 222,260,914.0 | 187,291.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 230,919,989.0 | 223,133,308.0 | 234,668,099.0 | 3,798,788.1 | 5 | 32,184 | 35,010 | 28,761 | 0.016 | compiled=5 | 2,081,051.0 | 228,635,547.0 | 189,261.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 253,084,435.0 | 252,476,243.0 | 264,966,867.0 | 5,700,569.9 | 5 | 31,952 | 33,849 | 31,823 | 0.023 | compiled=5 | 1,725,779.0 | 251,278,805.0 | 115,650.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,462,451.0 | 244,381,000.0 | 270,497,115.0 | 8,788,456.5 | 5 | 31,952 | 33,777 | 31,751 | 0.035 | compiled=5 | 3,302,837.0 | 248,734,082.0 | 190,251.0 |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 255,296,887.0 | 250,145,420.0 | 282,545,011.0 | 11,667,351.6 | 5 | 31,952 | 33,849 | 31,823 | 0.046 | compiled=5 | 1,823,440.0 | 251,373,136.0 | 185,481.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 252,598,163.0 | 244,172,978.0 | 258,425,644.0 | 4,827,318.9 | 5 | 31,952 | 33,777 | 31,751 | 0.019 | compiled=5 | 3,475,399.0 | 249,021,123.0 | 103,010.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 214,990,815.0 | 210,490,090.0 | 218,096,322.0 | 2,579,313.9 | 5 | 27,592 | 24,783 | 24,321 | 0.012 | compiled=5 | 1,695,228.0 | 213,185,706.0 | 103,791.0 |
| `doubled-word` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 216,567,694.0 | 211,061,905.0 | 222,613,486.0 | 3,756,800.8 | 5 | 27,592 | 24,896 | 24,434 | 0.017 (max is trial 1) | compiled=5 | 1,699,979.0 | 214,706,054.0 | 187,401.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 229,680,983.0 | 219,861,912.0 | 239,371,402.0 | 6,186,208.4 | 5 | 31,856 | 27,735 | 27,219 | 0.027 | compiled=5 | 3,491,678.0 | 226,962,628.0 | 193,151.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 236,440,277.0 | 231,137,260.0 | 250,383,731.0 | 6,578,609.0 | 5 | 31,856 | 27,848 | 27,332 | 0.028 (max is trial 1) | compiled=5 | 1,788,029.0 | 234,549,158.0 | 109,111.0 |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 206,839,631.0 | 199,756,916.0 | 212,198,151.0 | 5,135,285.7 | 5 | 31,792 | 27,235 | 25,162 | 0.025 (max is trial 1) | compiled=5 | 2,026,960.0 | 204,713,392.0 | 189,131.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 204,808,223.0 | 187,695,174.0 | 216,185,542.0 | 9,642,847.1 | 5 | 31,800 | 27,653 | 25,509 | 0.047 | compiled=5 | 3,403,768.0 | 200,820,072.0 | 189,941.0 |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 223,729,482.0 | 217,322,539.0 | 223,986,842.0 | 2,986,066.1 | 5 | 31,912 | 29,236 | 27,290 | 0.013 | compiled=5 | 1,817,629.0 | 221,810,052.0 | 101,801.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 221,683,581.0 | 217,384,389.0 | 222,385,774.0 | 2,285,974.9 | 5 | 31,912 | 29,667 | 27,637 | 0.010 | compiled=5 | 1,795,549.0 | 219,891,452.0 | 106,411.0 |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 224,346,583.0 | 208,518,630.0 | 225,903,692.0 | 6,485,199.1 | 5 | 31,912 | 29,236 | 27,290 | 0.029 | compiled=5 | 1,737,099.0 | 222,412,173.0 | 108,901.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 219,331,435.0 | 216,489,231.0 | 224,007,552.0 | 3,004,381.9 | 5 | 31,912 | 29,667 | 27,637 | 0.014 | compiled=5 | 1,756,260.0 | 215,547,166.0 | 111,720.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 212,774,164.0 | 208,310,700.0 | 216,320,293.0 | 3,275,921.4 | 5 | 31,728 | 25,768 | 25,768 | 0.015 | compiled=5 | 1,697,129.0 | 209,190,115.0 | 198,091.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 210,850,034.0 | 202,000,168.0 | 215,038,216.0 | 4,383,842.0 | 5 | 31,728 | 25,881 | 25,881 | 0.021 | compiled=5 | 1,698,369.0 | 208,875,864.0 | 184,751.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 214,442,491.0 | 208,279,689.0 | 215,327,536.0 | 3,099,430.7 | 5 | 31,728 | 25,768 | 25,768 | 0.014 | compiled=5 | 1,622,259.0 | 212,642,382.0 | 113,101.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 209,592,924.0 | 200,129,236.0 | 214,916,574.0 | 5,320,059.6 | 5 | 31,728 | 25,881 | 25,881 | 0.025 | compiled=5 | 1,615,948.0 | 207,835,156.0 | 120,760.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 159,756,607.0 | 149,287,072.0 | 163,008,534.0 | 4,754,538.2 | 5 | 27,872 | 21,280 | 15,157 | 0.030 | compiled=5 | 1,994,100.0 | 155,575,225.0 | 101,620.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 165,211,874.0 | 163,527,287.0 | 172,405,403.0 | 3,793,431.2 | 5 | 28,016 | 24,424 | 17,358 | 0.023 | compiled=5 | 2,067,281.0 | 163,068,553.0 | 103,401.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 154,753,607.0 | 149,274,708.0 | 165,802,625.0 | 5,439,458.0 | 5 | 27,872 | 21,280 | 15,157 | 0.035 | compiled=5 | 1,832,720.0 | 152,919,977.0 | 108,621.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 160,741,109.0 | 154,782,056.0 | 171,953,536.0 | 6,865,047.1 | 5 | 28,016 | 24,424 | 17,358 | 0.043 | compiled=5 | 1,979,001.0 | 158,645,887.0 | 183,221.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,811,423.0 | 227,807,622.0 | 239,221,642.0 | 4,532,787.0 | 5 | 32,072 | 33,900 | 28,751 | 0.020 | compiled=5 | 2,083,101.0 | 229,499,711.0 | 109,091.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 242,456,359.0 | 234,087,996.0 | 253,492,716.0 | 6,857,489.0 | 5 | 32,160 | 34,742 | 29,284 | 0.028 | compiled=5 | 4,337,232.0 | 237,910,476.0 | 111,240.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 156,028,327.0 | 147,932,183.0 | 156,236,228.0 | 3,178,851.0 | 5 | 27,872 | 19,793 | 14,796 | 0.020 | compiled=5 | 1,833,159.0 | 154,011,976.0 | 111,930.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,431,851.0 | 157,528,635.0 | 173,932,121.0 | 5,962,084.0 | 5 | 28,016 | 22,248 | 16,925 | 0.037 | compiled=5 | 3,613,079.0 | 158,509,710.0 | 99,541.0 |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 154,134,203.0 | 144,782,024.0 | 160,566,067.0 | 5,178,862.7 | 5 | 27,872 | 19,793 | 14,796 | 0.034 | compiled=5 | 1,730,550.0 | 152,222,833.0 | 187,911.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 165,738,455.0 | 160,042,855.0 | 166,360,037.0 | 2,353,974.6 | 5 | 28,016 | 22,248 | 16,925 | 0.014 | compiled=5 | 1,781,839.0 | 163,859,724.0 | 99,861.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 174,027,552.0 | 167,859,269.0 | 178,789,225.0 | 3,482,001.9 | 5 | 27,576 | 26,038 | 19,732 | 0.020 | compiled=5 | 1,977,521.0 | 171,948,030.0 | 187,571.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 161,439,115.0 | 157,110,831.0 | 170,269,261.0 | 4,291,288.4 | 5 | 28,008 | 24,852 | 17,725 | 0.027 | compiled=5 | 2,013,100.0 | 159,248,334.0 | 101,701.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 170,074,150.0 | 169,069,585.0 | 174,763,394.0 | 2,126,143.4 | 5 | 32,688 | 23,670 | 18,354 | 0.013 (max is trial 1) | compiled=5 | 1,947,050.0 | 167,913,589.0 | 194,961.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 166,024,439.0 | 157,491,824.0 | 168,646,413.0 | 3,909,697.1 | 5 | 32,480 | 22,748 | 17,432 | 0.024 | compiled=5 | 2,070,291.0 | 162,119,679.0 | 184,491.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 171,273,944.0 | 170,282,298.0 | 173,255,972.0 | 1,102,451.2 | 5 | 32,688 | 23,670 | 18,354 | 0.006 (max is trial 1) | compiled=5 | 1,748,490.0 | 169,420,993.0 | 106,830.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 168,498,718.0 | 162,013,414.0 | 171,934,857.0 | 3,291,434.2 | 5 | 32,480 | 22,748 | 17,432 | 0.020 | compiled=5 | 1,781,890.0 | 166,618,668.0 | 100,881.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 154,344,437.0 | 148,387,787.0 | 160,011,488.0 | 4,195,707.3 | 5 | 27,872 | 21,758 | 15,144 | 0.027 | compiled=5 | 1,975,841.0 | 152,448,708.0 | 110,420.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 167,415,397.0 | 165,154,174.0 | 170,910,644.0 | 2,343,889.0 | 5 | 28,016 | 26,179 | 17,353 | 0.014 | compiled=5 | 4,253,332.0 | 165,187,235.0 | 100,971.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 154,323,013.0 | 150,823,405.0 | 157,685,322.0 | 2,595,831.8 | 5 | 27,872 | 21,758 | 15,144 | 0.017 | compiled=5 | 1,899,250.0 | 152,327,023.0 | 107,451.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 166,500,428.0 | 152,015,312.0 | 174,890,123.0 | 7,714,085.0 | 5 | 28,016 | 26,179 | 17,353 | 0.046 | compiled=5 | 2,036,081.0 | 164,386,907.0 | 180,801.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 279,841,676.0 | 273,442,222.0 | 285,555,834.0 | 4,713,372.1 | 5 | 79,008 | 57,513 | 37,580 | 0.017 | compiled=5 | 2,568,964.0 | 273,557,563.0 | 220,661.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 286,471,690.0 | 282,175,078.0 | 301,119,116.0 | 6,698,369.2 | 5 | 78,968 | 57,440 | 37,507 | 0.023 | compiled=5 | 2,589,423.0 | 283,680,815.0 | 222,251.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 272,499,827.0 | 264,641,576.0 | 281,723,655.0 | 5,454,008.2 | 5 | 79,008 | 57,232 | 37,299 | 0.020 | compiled=5 | 2,580,484.0 | 269,832,543.0 | 215,021.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 284,152,208.0 | 276,675,398.0 | 286,255,139.0 | 3,703,073.4 | 5 | 78,968 | 57,159 | 37,226 | 0.013 | compiled=5 | 2,598,714.0 | 281,414,453.0 | 119,521.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 313,526,583.0 | 309,669,135.0 | 328,158,889.0 | 6,439,067.2 | 5 | 83,104 | 63,692 | 43,759 | 0.021 | compiled=5 | 2,597,254.0 | 310,686,628.0 | 230,712.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 311,960,145.0 | 310,914,820.0 | 330,510,042.0 | 7,502,190.2 | 5 | 83,064 | 63,619 | 43,686 | 0.024 | compiled=5 | 2,580,214.0 | 308,210,666.0 | 220,721.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,267,954.0 | 144,686,957.0 | 156,558,620.0 | 4,476,358.8 | 5 | 27,872 | 20,021 | 14,818 | 0.029 | compiled=5 | 1,887,770.0 | 152,547,958.0 | 207,871.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 164,907,753.0 | 153,157,671.0 | 171,401,808.0 | 5,938,427.6 | 5 | 28,016 | 22,440 | 16,835 | 0.036 | compiled=5 | 1,920,700.0 | 162,890,703.0 | 188,361.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 290,302,620.0 | 282,317,047.0 | 312,469,906.0 | 10,595,435.9 | 5 | 31,768 | 31,367 | 31,136 | 0.036 | compiled=5 | 1,854,959.0 | 288,348,000.0 | 100,881.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 290,163,430.0 | 281,667,965.0 | 294,238,881.0 | 4,743,797.9 | 5 | 31,768 | 31,483 | 31,252 | 0.016 | compiled=5 | 1,823,529.0 | 288,187,719.0 | 111,581.0 |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 210,082,560.0 | 201,605,636.0 | 219,800,660.0 | 5,899,094.3 | 5 | 31,832 | 28,898 | 27,216 | 0.028 | compiled=5 | 1,725,430.0 | 208,301,960.0 | 109,531.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 217,519,119.0 | 212,201,160.0 | 221,045,749.0 | 2,935,625.7 | 5 | 31,832 | 28,827 | 27,145 | 0.013 | compiled=5 | 1,800,239.0 | 215,615,519.0 | 113,480.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 214,056,629.0 | 209,873,016.0 | 218,770,204.0 | 3,366,056.3 | 5 | 31,832 | 28,898 | 27,216 | 0.016 | compiled=5 | 1,791,169.0 | 210,515,211.0 | 182,651.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 215,665,688.0 | 210,171,058.0 | 216,937,644.0 | 2,385,462.1 | 5 | 31,832 | 28,827 | 27,145 | 0.011 | compiled=5 | 1,704,119.0 | 213,874,248.0 | 182,051.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,416,342.0 | 227,165,628.0 | 232,488,197.0 | 1,936,399.4 | 5 | 31,912 | 30,126 | 28,184 | 0.008 | compiled=5 | 1,850,919.0 | 229,464,322.0 | 101,260.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 230,853,059.0 | 216,696,224.0 | 240,360,009.0 | 8,661,384.1 | 5 | 31,872 | 30,054 | 28,112 | 0.038 | compiled=5 | 1,852,140.0 | 228,888,609.0 | 109,431.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 227,551,779.0 | 215,865,808.0 | 236,332,417.0 | 6,717,780.3 | 5 | 31,912 | 30,126 | 28,184 | 0.030 | compiled=5 | 1,771,979.0 | 224,119,662.0 | 98,670.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 229,031,098.0 | 218,322,943.0 | 237,758,574.0 | 6,553,870.2 | 5 | 31,872 | 30,054 | 28,112 | 0.029 | compiled=5 | 1,767,169.0 | 227,062,498.0 | 197,301.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 286,909,772.0 | 284,342,708.0 | 292,971,154.0 | 2,958,568.7 | 5 | 31,520 | 23,681 | 23,681 | 0.010 | compiled=5 | 1,756,910.0 | 283,972,687.0 | 170,021.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 197,501,923.0 | 194,509,948.0 | 205,505,406.0 | 3,898,770.5 | 5 | 27,504 | 23,489 | 23,489 | 0.020 | compiled=5 | 1,688,929.0 | 195,716,764.0 | 186,451.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 252,166,320.0 | 247,558,046.0 | 256,728,325.0 | 2,907,276.3 | 5 | 32,072 | 33,230 | 30,589 | 0.012 | compiled=5 | 2,072,981.0 | 250,139,710.0 | 110,460.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,093,300.0 | 248,625,802.0 | 261,012,708.0 | 4,155,399.4 | 5 | 32,064 | 33,158 | 30,517 | 0.016 | compiled=5 | 1,916,871.0 | 250,066,819.0 | 107,090.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 218,256,443.0 | 211,091,895.0 | 227,085,077.0 | 5,487,501.9 | 5 | 31,848 | 26,467 | 25,774 | 0.025 | compiled=5 | 1,731,679.0 | 216,449,923.0 | 100,201.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 212,089,601.0 | 204,518,212.0 | 218,962,457.0 | 5,492,645.9 | 5 | 31,848 | 26,580 | 25,887 | 0.026 | compiled=5 | 1,711,619.0 | 210,183,851.0 | 189,711.0 |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,646,675.0 | 151,350,314.0 | 159,827,466.0 | 3,019,717.9 | 5 | 27,872 | 21,136 | 15,156 | 0.019 | compiled=5 | 1,998,230.0 | 153,520,244.0 | 103,731.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 166,616,002.0 | 159,814,017.0 | 170,980,686.0 | 3,706,780.4 | 5 | 28,016 | 23,964 | 17,357 | 0.022 | compiled=5 | 2,048,921.0 | 164,465,621.0 | 188,521.0 |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 158,842,399.0 | 149,665,440.0 | 159,834,383.0 | 3,853,772.7 | 5 | 27,872 | 21,136 | 15,156 | 0.024 | compiled=5 | 1,921,740.0 | 156,827,087.0 | 104,061.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 167,047,440.0 | 165,670,803.0 | 170,527,820.0 | 1,629,406.0 | 5 | 28,016 | 23,964 | 17,357 | 0.010 | compiled=5 | 1,972,521.0 | 164,912,779.0 | 197,311.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 279,143,901.0 | 277,933,405.0 | 290,963,532.0 | 5,609,851.9 | 5 | 31,896 | 33,533 | 33,017 | 0.020 | compiled=5 | 1,904,469.0 | 276,962,450.0 | 101,480.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 289,224,643.0 | 283,378,413.0 | 290,346,130.0 | 2,716,034.3 | 5 | 31,896 | 33,646 | 33,130 | 0.009 | compiled=5 | 1,885,890.0 | 287,225,463.0 | 102,161.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 228,149,184.0 | 227,365,890.0 | 237,879,976.0 | 3,981,190.1 | 5 | 31,856 | 27,621 | 26,412 | 0.017 | compiled=5 | 1,822,529.0 | 226,118,254.0 | 117,681.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 225,188,579.0 | 219,981,092.0 | 228,401,846.0 | 2,782,700.9 | 5 | 31,856 | 27,734 | 26,525 | 0.012 | compiled=5 | 1,811,610.0 | 223,144,218.0 | 103,490.0 |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 205,729,058.0 | 198,013,917.0 | 216,110,723.0 | 6,080,138.7 | 5 | 27,600 | 24,001 | 23,770 | 0.030 | compiled=5 | 1,674,869.0 | 203,894,178.0 | 99,740.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 202,835,242.0 | 198,129,368.0 | 208,889,594.0 | 4,148,207.2 | 5 | 31,696 | 24,115 | 23,884 | 0.020 | compiled=5 | 3,157,946.0 | 199,265,923.0 | 189,491.0 |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 198,866,399.0 | 185,570,749.0 | 205,401,474.0 | 7,356,034.5 | 5 | 27,600 | 24,001 | 23,770 | 0.037 | compiled=5 | 1,594,319.0 | 197,073,789.0 | 181,851.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 206,593,870.0 | 194,001,874.0 | 216,457,632.0 | 7,206,820.5 | 5 | 31,696 | 24,115 | 23,884 | 0.035 (max is trial 1) | compiled=5 | 1,644,229.0 | 203,255,982.0 | 188,301.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 190,959,040.0 | 175,973,771.0 | 191,331,321.0 | 5,938,124.9 | 5 | 31,896 | 28,425 | 23,623 | 0.031 | compiled=5 | 1,931,670.0 | 188,940,739.0 | 106,521.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 197,231,323.0 | 182,078,113.0 | 207,902,598.0 | 8,267,618.3 | 5 | 31,984 | 30,113 | 25,097 | 0.042 | compiled=5 | 1,941,380.0 | 195,219,022.0 | 103,801.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 174,285,582.0 | 169,472,237.0 | 178,957,247.0 | 3,555,707.6 | 5 | 37,152 | 23,987 | 18,583 | 0.020 | compiled=5 | 1,758,469.0 | 170,557,993.0 | 111,841.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 172,259,922.0 | 171,690,699.0 | 181,306,989.0 | 4,305,280.2 | 5 | 37,112 | 23,809 | 18,405 | 0.025 | compiled=5 | 1,767,319.0 | 170,324,702.0 | 190,241.0 |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 174,401,560.0 | 169,997,017.0 | 178,609,052.0 | 3,185,511.8 | 5 | 37,152 | 23,987 | 18,583 | 0.018 | compiled=5 | 1,680,089.0 | 170,688,690.0 | 204,141.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 179,375,046.0 | 174,563,610.0 | 180,591,991.0 | 2,211,425.9 | 5 | 37,112 | 23,809 | 18,405 | 0.012 | compiled=5 | 1,676,819.0 | 177,340,445.0 | 106,581.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 141,977,024.0 | 132,982,006.0 | 156,532,840.0 | 8,168,175.6 | 5 | 27,872 | 19,793 | 14,796 | 0.058 | compiled=5 | 1,815,650.0 | 139,959,233.0 | 197,021.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 152,501,279.0 | 145,398,132.0 | 155,856,505.0 | 3,430,046.1 | 5 | 28,016 | 22,248 | 16,925 | 0.022 | compiled=5 | 1,853,189.0 | 150,551,778.0 | 185,651.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 144,846,554.0 | 139,339,324.0 | 146,909,895.0 | 2,778,413.0 | 5 | 27,872 | 19,793 | 14,796 | 0.019 | compiled=5 | 2,003,651.0 | 143,041,334.0 | 104,400.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,828,759.0 | 155,809,461.0 | 165,968,885.0 | 4,570,049.0 | 5 | 28,016 | 22,248 | 16,925 | 0.028 | compiled=5 | 1,789,120.0 | 162,936,739.0 | 102,900.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 164,388,091.0 | 159,578,156.0 | 168,819,134.0 | 3,075,374.7 | 5 | 28,200 | 28,744 | 16,479 | 0.019 | compiled=5 | 2,403,592.0 | 159,709,976.0 | 197,661.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,507,610.0 | 151,777,114.0 | 165,738,079.0 | 4,707,467.8 | 5 | 28,336 | 31,719 | 18,566 | 0.029 | compiled=5 | 2,469,663.0 | 157,844,716.0 | 190,961.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 149,175,977.0 | 142,875,394.0 | 154,632,755.0 | 4,526,004.4 | 5 | 28,200 | 28,744 | 16,479 | 0.030 | compiled=5 | 2,299,282.0 | 146,847,784.0 | 100,480.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 170,116,228.0 | 164,197,496.0 | 173,133,424.0 | 3,425,790.0 | 5 | 28,336 | 31,719 | 18,566 | 0.020 | compiled=5 | 2,376,103.0 | 167,513,013.0 | 186,141.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 154,316,868.0 | 152,176,047.0 | 158,551,721.0 | 2,276,312.7 | 5 | 27,864 | 23,557 | 15,235 | 0.015 (max is trial 1) | compiled=5 | 2,192,192.0 | 150,858,960.0 | 98,100.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 163,448,775.0 | 154,454,818.0 | 169,008,256.0 | 5,092,181.4 | 5 | 28,008 | 26,908 | 17,149 | 0.031 | compiled=5 | 2,306,752.0 | 161,040,483.0 | 99,371.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 145,705,433.0 | 141,916,152.0 | 156,413,588.0 | 5,871,445.4 | 5 | 27,872 | 19,795 | 14,798 | 0.040 | compiled=5 | 1,817,110.0 | 143,696,432.0 | 102,790.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 160,319,289.0 | 147,907,344.0 | 170,656,784.0 | 8,074,804.9 | 5 | 28,016 | 22,250 | 16,927 | 0.050 | compiled=5 | 1,867,009.0 | 158,228,088.0 | 207,171.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 156,552,066.0 | 139,099,384.0 | 159,528,321.0 | 7,986,610.8 | 5 | 27,872 | 19,795 | 14,798 | 0.051 | compiled=5 | 1,754,909.0 | 154,417,114.0 | 189,381.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,646,659.0 | 154,951,187.0 | 165,554,672.0 | 4,019,435.8 | 5 | 28,016 | 22,250 | 16,927 | 0.024 | compiled=5 | 1,789,090.0 | 161,674,122.0 | 200,601.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,799,847.0 | 152,288,897.0 | 160,544,611.0 | 2,800,748.8 | 5 | 27,872 | 21,173 | 15,078 | 0.018 | compiled=5 | 2,051,211.0 | 153,734,955.0 | 198,071.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 159,176,675.0 | 154,137,567.0 | 173,635,189.0 | 8,651,640.8 | 5 | 28,016 | 23,927 | 17,209 | 0.054 | compiled=5 | 2,041,791.0 | 154,790,331.0 | 168,191.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 599,052,326.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 16,177,238,265.0 | 16,072,557,246.0 | 16,352,970,525.0 | 99,749,615.2 | 5 | 150,848 | 484,520 (warned) | 482,896 | 0.006 | compiled=5 | 9,263,562,535.0 | 6,881,366,071.0 | 125,641.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 587,419,118.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,445,836,770.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 355,482,262.0 | 354,525,867.0 | 357,619,304.0 | 1,069,354.4 | 5 | 45,912 | 55,856 | 45,933 | 0.003 (max is trial 1) | compiled=5 | 2,418,352.0 | 352,655,447.0 | 112,301.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 354,186,585.0 | 347,461,800.0 | 368,102,188.0 | 6,983,903.8 | 5 | 45,544 | 54,295 | 44,372 | 0.020 | compiled=5 | 5,089,977.0 | 350,217,213.0 | 198,751.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 361,996,498.0 | 355,424,253.0 | 362,435,391.0 | 2,792,914.4 | 5 | 45,912 | 55,856 | 45,933 | 0.008 | compiled=5 | 2,321,412.0 | 359,591,376.0 | 102,051.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 350,837,800.0 | 345,189,091.0 | 358,089,627.0 | 4,145,780.3 | 5 | 45,544 | 54,295 | 44,372 | 0.012 (max is trial 1) | compiled=5 | 2,313,502.0 | 348,326,157.0 | 193,301.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 238,774,151.0 | 233,062,980.0 | 242,928,712.0 | 3,660,254.7 | 5 | 32,056 | 34,318 | 28,808 | 0.015 | compiled=5 | 2,106,262.0 | 234,279,607.0 | 186,491.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 242,796,850.0 | 240,454,808.0 | 257,606,969.0 | 6,212,508.8 | 5 | 32,152 | 35,390 | 29,455 | 0.026 | compiled=5 | 2,168,881.0 | 240,581,819.0 | 100,020.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 238,322,118.0 | 223,107,918.0 | 241,316,874.0 | 6,508,877.0 | 5 | 32,056 | 34,039 | 28,529 | 0.027 | compiled=5 | 2,071,711.0 | 236,041,946.0 | 196,521.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 235,316,541.0 | 232,788,909.0 | 239,980,356.0 | 3,156,258.0 | 5 | 32,152 | 35,108 | 29,173 | 0.013 | compiled=5 | 2,118,871.0 | 230,852,818.0 | 109,371.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 402,559,238.0 | 395,003,268.0 | 403,772,894.0 | 3,933,395.7 | 5 | 40,760 | 61,625 | 41,896 | 0.010 | compiled=5 | 5,240,027.0 | 397,185,030.0 | 192,291.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 413,638,316.0 | 408,501,260.0 | 421,366,147.0 | 4,814,889.4 | 5 | 40,856 | 66,268 | 43,396 | 0.012 | compiled=5 | 8,355,164.0 | 399,936,964.0 | 193,541.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 356,337,157.0 | 355,534,051.0 | 363,331,902.0 | 2,939,066.1 | 5 | 40,760 | 59,595 | 39,866 | 0.008 (max is trial 1) | compiled=5 | 5,036,676.0 | 351,087,969.0 | 111,201.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 374,586,381.0 | 367,149,442.0 | 378,222,820.0 | 3,659,155.2 | 5 | 40,856 | 64,238 | 41,366 | 0.010 (max is trial 1) | compiled=5 | 8,025,032.0 | 366,447,268.0 | 103,520.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 5,407,526,204.0 | 5,399,946,815.0 | 5,433,470,239.0 | 12,260,677.1 | 5 | 176,288 | 515,893 (warned) | 297,928 | 0.002 (max is trial 1) | compiled=5 | 598,747,135.0 | 4,808,573,168.0 | 185,171.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 6,435,887,458.0 | 6,416,894,449.0 | 6,446,040,812.0 | 10,199,385.2 | 5 | 180,480 | 525,510 (warned) | 299,348 | 0.002 | compiled=5 | 1,608,314,362.0 | 4,816,965,632.0 | 99,890.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 245,769,706.0 | 236,352,057.0 | 254,565,633.0 | 6,218,449.4 | 5 | 32,272 | 37,739 | 29,255 | 0.025 | compiled=5 | 2,206,582.0 | 243,428,285.0 | 107,291.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 255,352,138.0 | 248,197,630.0 | 256,506,914.0 | 3,516,393.8 | 5 | 32,408 | 41,083 | 30,780 | 0.014 (max is trial 1) | compiled=5 | 2,348,423.0 | 251,318,686.0 | 111,401.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 246,298,029.0 | 241,161,793.0 | 246,921,993.0 | 2,337,393.4 | 5 | 36,336 | 46,133 | 29,228 | 0.009 | compiled=5 | 3,264,637.0 | 242,891,622.0 | 106,740.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 245,753,607.0 | 242,658,780.0 | 257,675,090.0 | 5,610,894.7 | 5 | 36,432 | 48,666 | 30,765 | 0.023 | compiled=5 | 3,444,708.0 | 242,133,918.0 | 203,721.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 255,564,908.0 | 253,595,587.0 | 256,358,152.0 | 920,539.7 | 5 | 36,336 | 48,061 | 31,156 | 0.004 (max is trial 1) | compiled=5 | 3,262,077.0 | 252,065,469.0 | 192,981.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 257,736,547.0 | 252,668,243.0 | 260,607,884.0 | 3,366,775.4 | 5 | 36,432 | 50,594 | 32,693 | 0.013 | compiled=5 | 3,396,728.0 | 249,905,357.0 | 111,200.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 336,702,373.0 | 335,249,515.0 | 340,640,425.0 | 1,928,634.0 | 5 | 40,304 | 56,824 | 26,714 | 0.006 (max is trial 1) | compiled=5 | 4,597,454.0 | 330,839,902.0 | 110,390.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 331,160,074.0 | 322,041,836.0 | 338,216,631.0 | 5,141,245.5 | 5 | 40,400 | 60,192 | 28,249 | 0.016 | compiled=5 | 4,680,505.0 | 326,256,228.0 | 194,371.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 395,803,208.0 | 386,035,596.0 | 403,560,398.0 | 5,865,949.8 | 5 | 44,400 | 58,384 | 28,274 | 0.015 | compiled=5 | 4,625,595.0 | 390,298,688.0 | 98,421.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 399,928,300.0 | 398,156,020.0 | 410,035,262.0 | 4,239,264.9 | 5 | 40,400 | 61,754 | 29,811 | 0.011 (max is trial 1) | compiled=5 | 4,826,715.0 | 395,167,804.0 | 102,991.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 288,851,213.0 | 286,335,719.0 | 298,927,194.0 | 4,699,217.9 | 5 | 52,624 | 105,222 | 33,872 | 0.016 | compiled=5 | 7,793,201.0 | 278,619,609.0 | 101,430.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 301,207,487.0 | 290,018,528.0 | 311,676,991.0 | 8,046,884.9 | 5 | 52,720 | 112,577 | 35,416 | 0.027 | compiled=5 | 8,194,053.0 | 282,319,668.0 | 189,221.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 286,427,241.0 | 274,652,979.0 | 289,497,377.0 | 5,287,315.0 | 5 | 52,624 | 105,520 | 34,170 | 0.018 (max is trial 1) | compiled=5 | 7,566,940.0 | 278,029,996.0 | 191,001.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 291,012,525.0 | 289,912,718.0 | 309,996,465.0 | 7,541,298.5 | 5 | 52,720 | 112,875 | 35,714 | 0.026 | compiled=5 | 8,126,433.0 | 282,769,831.0 | 103,981.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 541,180,843.0 | 533,740,605.0 | 551,204,506.0 | 6,426,046.1 | 5 | 208,736 | 550,723 (warned) | 41,457 | 0.012 | compiled=5 | 57,677,702.0 | 480,575,836.0 | 105,230.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 557,952,482.0 | 550,162,480.0 | 578,441,028.0 | 9,916,244.1 | 5 | 212,928 | 565,513 (warned) | 42,745 | 0.018 (max is trial 1) | compiled=5 | 64,901,769.0 | 493,046,832.0 | 98,530.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 569,599,903.0 | 554,702,335.0 | 605,257,561.0 | 16,818,551.3 | 5 | 208,736 | 554,081 (warned) | 44,814 | 0.030 (max is trial 1) | compiled=5 | 58,033,096.0 | 511,735,129.0 | 180,701.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 588,486,804.0 | 580,723,732.0 | 594,813,937.0 | 4,476,256.5 | 5 | 212,928 | 568,871 (warned) | 46,102 | 0.008 | compiled=5 | 64,952,403.0 | 523,732,082.0 | 94,491.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 163,503,026.0 | 153,635,185.0 | 168,884,914.0 | 5,683,053.5 | 5 | 27,872 | 21,710 | 16,003 | 0.035 | compiled=5 | 4,104,931.0 | 158,894,222.0 | 188,701.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 169,219,946.0 | 162,635,801.0 | 171,852,230.0 | 3,620,432.4 | 5 | 28,016 | 23,954 | 17,347 | 0.021 | compiled=5 | 2,031,021.0 | 166,996,684.0 | 192,241.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 166,036,345.0 | 159,533,522.0 | 170,214,467.0 | 4,009,592.5 | 5 | 27,872 | 21,710 | 16,003 | 0.024 | compiled=5 | 1,872,880.0 | 164,060,875.0 | 112,210.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 169,240,802.0 | 158,823,898.0 | 170,840,931.0 | 4,419,824.2 | 5 | 28,016 | 23,954 | 17,347 | 0.026 | compiled=5 | 1,937,351.0 | 167,204,992.0 | 108,410.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 168,192,471.0 | 166,239,750.0 | 170,815,243.0 | 1,665,586.3 | 5 | 28,016 | 23,560 | 17,779 | 0.010 | compiled=5 | 1,932,861.0 | 165,074,704.0 | 100,380.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 161,904,138.0 | 159,115,323.0 | 173,407,988.0 | 5,698,402.3 | 5 | 28,016 | 23,132 | 17,351 | 0.035 | compiled=5 | 1,928,360.0 | 159,995,298.0 | 106,991.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 170,118,076.0 | 159,261,510.0 | 176,300,440.0 | 6,406,206.9 | 5 | 28,016 | 23,560 | 17,779 | 0.038 | compiled=5 | 1,858,170.0 | 168,211,967.0 | 191,231.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 170,009,187.0 | 159,760,712.0 | 187,664,020.0 | 9,158,904.4 | 5 | 28,016 | 23,132 | 17,351 | 0.054 | compiled=5 | 1,873,640.0 | 166,533,638.0 | 100,211.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 223,040,067.0 | 217,096,697.0 | 232,911,679.0 | 5,586,208.7 | 5 | 32,048 | 32,388 | 27,554 | 0.025 | compiled=5 | 1,971,000.0 | 220,967,397.0 | 100,720.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 222,987,087.0 | 210,595,903.0 | 235,521,563.0 | 8,528,029.1 | 5 | 32,144 | 33,867 | 28,803 | 0.038 | compiled=5 | 2,326,533.0 | 218,825,166.0 | 190,581.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 223,353,757.0 | 213,540,235.0 | 234,503,786.0 | 6,685,388.7 | 5 | 32,048 | 32,388 | 27,554 | 0.030 | compiled=5 | 1,874,470.0 | 221,287,827.0 | 197,591.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 227,017,258.0 | 224,441,832.0 | 227,854,021.0 | 1,375,592.0 | 5 | 32,144 | 33,867 | 28,803 | 0.006 | compiled=5 | 1,911,010.0 | 224,966,316.0 | 116,120.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 148,801,479.0 | 143,935,513.0 | 152,373,568.0 | 3,016,664.7 | 5 | 27,696 | 15,957 | 13,600 | 0.020 | compiled=5 | 1,677,329.0 | 145,354,851.0 | 101,630.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 149,366,411.0 | 137,965,673.0 | 150,042,636.0 | 5,652,151.3 | 5 | 27,696 | 15,780 | 13,423 | 0.038 | compiled=5 | 1,662,109.0 | 145,870,874.0 | 191,991.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 141,191,005.0 | 128,701,948.0 | 151,908,531.0 | 8,416,437.5 | 5 | 27,696 | 15,957 | 13,600 | 0.060 | compiled=5 | 1,551,558.0 | 139,556,126.0 | 110,590.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 138,219,009.0 | 133,416,563.0 | 151,914,011.0 | 6,752,433.1 | 5 | 27,696 | 15,780 | 13,423 | 0.049 | compiled=5 | 1,799,030.0 | 136,540,450.0 | 184,281.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 320,728,600.0 | 315,713,733.0 | 321,293,822.0 | 2,058,866.8 | 5 | 41,040 | 46,197 | 41,169 | 0.006 | compiled=5 | 2,177,281.0 | 318,483,758.0 | 112,420.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 315,156,280.0 | 298,230,211.0 | 317,045,830.0 | 7,118,462.4 | 5 | 40,832 | 45,380 | 40,352 | 0.023 | compiled=5 | 2,157,271.0 | 312,908,359.0 | 194,371.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 314,014,124.0 | 313,097,011.0 | 321,161,084.0 | 3,631,147.0 | 5 | 41,040 | 46,197 | 41,169 | 0.012 | compiled=5 | 2,060,160.0 | 311,756,963.0 | 179,561.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 309,105,880.0 | 307,543,022.0 | 315,564,823.0 | 2,905,732.6 | 5 | 40,832 | 45,380 | 40,352 | 0.009 | compiled=5 | 2,081,761.0 | 306,697,547.0 | 106,200.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 204,531,121.0 | 203,244,104.0 | 218,204,242.0 | 5,746,014.5 | 5 | 32,152 | 28,501 | 25,957 | 0.028 | compiled=5 | 1,830,760.0 | 201,472,325.0 | 194,271.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 206,766,243.0 | 201,255,173.0 | 211,828,419.0 | 3,477,737.3 | 5 | 32,064 | 28,241 | 25,697 | 0.017 | compiled=5 | 1,792,380.0 | 204,781,332.0 | 192,531.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 209,716,716.0 | 207,530,004.0 | 210,661,891.0 | 1,132,837.7 | 5 | 32,152 | 28,501 | 25,957 | 0.005 | compiled=5 | 1,748,539.0 | 207,822,646.0 | 187,841.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 208,582,521.0 | 203,638,703.0 | 215,606,497.0 | 3,850,387.6 | 5 | 32,064 | 28,241 | 25,697 | 0.018 | compiled=5 | 1,730,289.0 | 206,762,991.0 | 99,870.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 248,326,361.0 | 238,250,497.0 | 249,236,585.0 | 4,472,443.1 | 5 | 36,640 | 47,955 | 22,637 | 0.018 | compiled=5 | 3,285,937.0 | 244,840,022.0 | 189,961.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 259,845,901.0 | 255,422,627.0 | 261,135,527.0 | 2,279,492.1 | 5 | 36,784 | 50,932 | 24,341 | 0.009 | compiled=5 | 7,380,888.0 | 252,232,171.0 | 200,181.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 245,416,534.0 | 232,494,625.0 | 248,802,982.0 | 5,660,057.9 | 5 | 36,640 | 47,955 | 22,637 | 0.023 | compiled=5 | 3,202,106.0 | 238,251,586.0 | 113,381.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 249,694,167.0 | 248,201,839.0 | 258,420,412.0 | 3,687,786.5 | 5 | 36,784 | 50,932 | 24,341 | 0.015 | compiled=5 | 3,255,987.0 | 245,585,566.0 | 192,281.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 227,858,973.0 | 219,596,770.0 | 231,820,324.0 | 4,609,307.4 | 5 | 85,816 | 227,952 | 19,986 | 0.020 | compiled=5 | 14,481,726.0 | 207,827,688.0 | 97,880.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 244,786,962.0 | 243,537,725.0 | 246,408,529.0 | 1,010,592.9 | 5 | 94,152 | 237,783 | 21,962 | 0.004 (max is trial 1) | compiled=5 | 15,868,433.0 | 228,106,624.0 | 107,051.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 223,942,031.0 | 222,332,062.0 | 229,723,461.0 | 2,807,236.2 | 5 | 85,816 | 227,952 | 19,986 | 0.013 | compiled=5 | 14,413,496.0 | 208,091,538.0 | 101,710.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 247,883,687.0 | 241,462,524.0 | 257,981,430.0 | 5,845,852.8 | 5 | 94,152 | 237,783 | 21,962 | 0.024 | compiled=5 | 15,819,554.0 | 231,972,253.0 | 207,671.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 197,212,723.0 | 179,841,132.0 | 198,797,561.0 | 7,137,369.9 | 5 | 36,560 | 58,368 | 17,968 | 0.036 | compiled=5 | 4,652,984.0 | 192,459,468.0 | 102,671.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 209,772,328.0 | 201,704,887.0 | 215,720,838.0 | 4,850,209.2 | 5 | 36,704 | 62,147 | 19,759 | 0.023 | compiled=5 | 5,370,559.0 | 202,682,452.0 | 108,201.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 196,681,627.0 | 182,375,752.0 | 206,296,978.0 | 8,059,232.5 | 5 | 36,560 | 58,368 | 17,968 | 0.041 | compiled=5 | 4,573,274.0 | 191,935,572.0 | 186,821.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 206,708,029.0 | 201,378,482.0 | 208,357,569.0 | 2,679,181.0 | 5 | 36,704 | 62,147 | 19,759 | 0.013 | compiled=5 | 5,064,477.0 | 201,558,733.0 | 108,861.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 164,354,721.0 | 163,390,854.0 | 178,287,983.0 | 5,613,728.5 | 5 | 32,232 | 36,918 | 15,751 | 0.034 (max is trial 1) | compiled=5 | 3,878,701.0 | 160,239,659.0 | 101,500.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 174,434,564.0 | 166,043,870.0 | 187,238,611.0 | 7,102,694.2 | 5 | 32,376 | 39,942 | 17,763 | 0.041 | compiled=5 | 3,920,940.0 | 170,830,455.0 | 194,742.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 173,324,495.0 | 161,960,834.0 | 178,344,890.0 | 5,924,581.4 | 5 | 32,232 | 36,918 | 15,751 | 0.034 | compiled=5 | 3,340,328.0 | 166,835,460.0 | 113,620.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 182,497,632.0 | 174,074,827.0 | 188,779,215.0 | 4,700,848.1 | 5 | 32,376 | 39,942 | 17,763 | 0.026 (max is trial 1) | compiled=5 | 3,368,408.0 | 178,963,423.0 | 101,980.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 1,470,740,970.0 | 1,428,762,891.0 | 1,496,714,667.0 | 29,126,945.7 | 5 | 680,528 | 395,013 (warned) | 100,533 | 0.020 | compiled=5 | 12,779,837.0 | 1,457,515,122.0 | 281,232.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 1,377,330,262.0 | 1,368,977,968.0 | 1,431,779,785.0 | 22,881,074.1 | 5 | 659,992 | 402,219 (warned) | 102,683 | 0.017 (max is trial 1) | compiled=5 | 13,217,470.0 | 1,363,581,160.0 | 515,073.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,460,924,194.0 | 1,431,076,087.0 | 1,484,434,439.0 | 21,298,228.8 | 5 | 680,528 | 395,013 (warned) | 100,533 | 0.015 | compiled=5 | 12,629,457.0 | 1,448,018,776.0 | 285,282.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,407,283,350.0 | 1,383,588,956.0 | 1,445,562,022.0 | 20,735,933.8 | 5 | 659,992 | 402,219 (warned) | 102,683 | 0.015 | compiled=5 | 13,394,440.0 | 1,388,392,601.0 | 503,952.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 161,472,745.0 | 149,285,771.0 | 163,167,325.0 | 5,070,347.3 | 5 | 27,872 | 21,615 | 15,703 | 0.031 | compiled=5 | 2,128,982.0 | 159,246,934.0 | 192,731.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 163,397,456.0 | 157,348,524.0 | 173,141,088.0 | 6,123,295.4 | 5 | 28,016 | 24,222 | 17,792 | 0.037 | compiled=5 | 2,489,543.0 | 161,142,703.0 | 106,440.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 161,315,870.0 | 154,630,915.0 | 163,271,022.0 | 3,050,433.9 | 5 | 27,872 | 21,615 | 15,703 | 0.019 | compiled=5 | 2,022,911.0 | 159,096,849.0 | 207,961.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 173,454,124.0 | 167,851,995.0 | 174,192,809.0 | 2,855,381.7 | 5 | 28,016 | 24,222 | 17,792 | 0.016 | compiled=5 | 2,081,021.0 | 171,345,563.0 | 98,890.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 144,731,688.0 | 132,892,935.0 | 155,063,402.0 | 8,586,719.3 | 5 | 27,656 | 15,346 | 13,263 | 0.059 (max is trial 1) | compiled=5 | 1,630,429.0 | 143,028,419.0 | 188,081.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 144,719,947.0 | 136,902,067.0 | 146,225,506.0 | 3,461,635.4 | 5 | 27,616 | 15,169 | 13,086 | 0.024 | compiled=5 | 1,646,828.0 | 143,005,988.0 | 99,991.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 147,719,808.0 | 131,854,775.0 | 148,442,073.0 | 7,115,441.4 | 5 | 27,656 | 15,346 | 13,263 | 0.048 | compiled=5 | 1,564,668.0 | 146,077,020.0 | 112,871.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 134,282,038.0 | 133,758,145.0 | 144,444,871.0 | 4,089,183.6 | 5 | 27,616 | 15,169 | 13,086 | 0.030 | compiled=5 | 1,574,328.0 | 132,515,779.0 | 101,940.0 |

