# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, machine=budu-ryzen1600, testee=pcrec_a32bc86e_auto-caps-simdna, testee=pcrec_a32bc86e_auto-caps-simdna_nolitrun
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 2
- worst other-core busy: 25.0% (`pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `base10num-near-miss` / `large-subject-throughput`)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T081053Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna/capability@0.1__pcrec_a32bc86e_auto-caps-simdna__budu-ryzen1600__20260928T081053Z.jsonl) — agreement: agree (0 of 124 groups; 0 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun__budu-ryzen1600__20260928T084613Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna_nolitrun/capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun__budu-ryzen1600__20260928T084613Z.jsonl) — agreement: agree (0 of 124 groups; 0 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 2 record(s) (OD-B15; --all-records lists them)
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
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,114,370.7 | 3.7161 | 5,105,909.4 | 5,127,063.9 | 7,611.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 5,127,901.2 | 3.7260 | 5,121,755.6 | 5,130,231.2 | 2,988.6 | 1.003x | 1.003x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,901,384.3 | 3.7207 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,912,513.4 | 3.7313 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 971,216.7 | 3.7049 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 972,868.2 | 3.7112 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 242,689.1 | 3.7031 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 242,749.4 | 3.7041 |

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,032.7 | 1,030.3 | 1,054.3 | 9.1 | 1.000x | 1.000x | 75 | 13.8 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,033.7 | 1,031.0 | 1,035.3 | 1.5 | 1.001x | 1.001x | 75 | 13.8 | 8.9 | 100% |

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.7 | 17.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 17.9 | 0.0000 | 17.8 | 18.0 | 0.1 | 1.000x | 1.000x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.9 | 0.0001 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 517.6 | 516.4 | 528.2 | 4.6 | 1.000x | 1.000x | 75 | 6.9 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 531.3 | 514.6 | 534.5 | 7.1 | 1.027x | 1.027x | 75 | 7.1 | 8.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 72.0 | 0.0001 | 71.5 | 72.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 72.1 | 0.0001 | 71.5 | 72.7 | 0.4 | 1.002x | 1.002x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 24.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 23.9 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 23.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 24.1 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 24.1 | 0.0004 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,877.4 | 1,876.5 | 1,880.2 | 1.3 | 1.000x | 1.000x | 75 | 25.0 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,877.8 | 1,876.9 | 1,886.4 | 3.5 | 1.000x | 1.000x | 75 | 25.0 | 8.9 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 615,656.1 | 0.4473 | 606,938.8 | 642,359.6 | 15,128.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 616,851.9 | 0.4482 | 604,613.9 | 635,069.9 | 11,568.1 | 1.002x | 1.002x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 467,173.7 | 0.4455 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 475,956.1 | 0.4539 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 124,360.0 | 0.4744 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 117,709.7 | 0.4490 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 28,013.7 | 0.4275 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 27,200.1 | 0.4150 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 892.3 | 891.5 | 897.7 | 2.9 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 896.5 | 890.4 | 897.2 | 2.5 | 1.005x | 1.005x | 75 | 12.0 | 9.0 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 604,366.8 | 0.4391 | 602,903.3 | 608,999.2 | 2,244.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 614,742.9 | 0.4467 | 607,279.2 | 615,709.2 | 3,229.7 | 1.017x | 1.017x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 467,525.7 | 0.4459 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 475,296.8 | 0.4533 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 109,622.3 | 0.4182 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 109,141.3 | 0.4163 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 27,229.4 | 0.4155 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 27,888.7 | 0.4255 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 892.1 | 890.2 | 894.1 | 1.3 | 1.000x | 1.000x | 75 | 11.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 896.5 | 889.7 | 900.3 | 3.8 | 1.005x | 1.005x | 75 | 12.0 | 9.0 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 11,175,491.8 | 8.1202 | 11,172,828.4 | 11,179,125.5 | 2,513.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 11,176,134.5 | 8.1207 | 11,172,669.1 | 11,216,843.9 | 16,833.1 | 1.000x | 1.000x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 8,510,599.5 | 8.1163 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 8,514,188.7 | 8.1198 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,129,619.5 | 8.1239 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 2,128,559.2 | 8.1198 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 534,469.8 | 8.1554 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 533,386.7 | 8.1388 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 5,147.3 | 5,129.7 | 5,161.6 | 12.4 | 1.000x | 1.000x | 75 | 68.6 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 5,149.7 | 5,148.4 | 5,157.7 | 3.6 | 1.000x | 1.000x | 75 | 68.7 | 8.9 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 31.1 | 0.0000 | 31.1 | 73.1 | 16.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 31.2 | 0.0000 | 31.2 | 31.3 | 0.0 | 1.005x | 1.005x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.4 | 0.0002 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 843.4 | 842.4 | 845.5 | 1.2 | 1.000x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 844.2 | 842.5 | 866.2 | 9.1 | 1.001x | 1.001x | 75 | 11.3 | 9.0 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 25,428,766.4 | 18.4768 | 25,385,538.9 | 25,477,869.4 | 30,719.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 25,521,860.7 | 18.5444 | 25,421,922.1 | 25,709,043.5 | 105,485.8 | 1.004x | 1.004x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 19,379,592.9 | 18.4818 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 19,507,066.1 | 18.6034 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,843,780.0 | 18.4776 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,842,689.1 | 18.4734 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,199,487.9 | 18.3027 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,200,166.5 | 18.3131 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 20,829.2 | 20,765.6 | 20,837.5 | 29.1 | 1.000x | 1.000x | 75 | 277.7 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 20,834.9 | 20,816.2 | 20,855.0 | 12.3 | 1.000x | 1.000x | 75 | 277.8 | 8.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,132.5 | 0.0168 | 23,127.4 | 23,159.2 | 13.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,135.5 | 0.0168 | 23,108.5 | 23,139.4 | 11.7 | 1.000x | 1.000x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,638.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,645.8 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,385.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,381.5 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,111.5 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,107.9 | 0.0169 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,171.3 | 1,166.6 | 1,177.2 | 4.0 | 1.000x | 1.000x | 75 | 15.6 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,174.9 | 1,170.3 | 1,195.2 | 9.2 | 1.003x | 1.003x | 75 | 15.7 | 8.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 980.5 | 0.0007 | 975.1 | 987.0 | 4.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,003.6 | 0.0007 | 1,001.2 | 1,016.5 | 5.8 | 1.024x | 1.024x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 229.2 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 234.0 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 459.7 | 0.0018 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 458.5 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 290.4 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 312.0 | 0.0048 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 10,510.5 | 10,480.8 | 10,816.2 | 127.8 | 1.000x | 1.000x | 75 | 140.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,593.4 | 10,574.0 | 10,628.6 | 20.9 | 1.008x | 1.008x | 75 | 141.2 | 8.9 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 46.5 | 0.0000 | 45.7 | 49.3 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 49.0 | 0.0000 | 46.0 | 51.3 | 1.8 | 1.054x | 1.054x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 16.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 14.8 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 14.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.7 | 0.0002 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,365.2 | 1,361.1 | 1,383.6 | 8.2 | 1.000x | 1.000x | 75 | 18.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,367.9 | 1,363.6 | 1,382.2 | 7.0 | 1.002x | 1.002x | 75 | 18.2 | 9.0 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,005.5 | 0.0087 | 11,974.4 | 12,037.1 | 20.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 12,078.8 | 0.0088 | 11,965.1 | 12,139.2 | 58.5 | 1.006x | 1.006x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,244.8 | 0.0012 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,247.6 | 0.0012 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 44.9 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 45.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,721.9 | 0.1636 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10,776.4 | 0.1644 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 255,442.0 | 0.1856 | 255,255.5 | 255,627.6 | 136.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 255,500.1 | 0.1856 | 255,476.1 | 255,566.7 | 31.5 | 1.000x | 1.000x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 202,516.4 | 0.1931 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 202,472.1 | 0.1931 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 44,333.2 | 0.1691 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 44,345.8 | 0.1692 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 8,661.3 | 0.1322 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 8,697.5 | 0.1327 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 687.9 | 687.5 | 688.2 | 0.3 | 1.000x | 1.000x | 75 | 9.2 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 688.6 | 687.1 | 690.2 | 1.3 | 1.001x | 1.001x | 75 | 9.2 | 8.9 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,904,927.5 | 1.3841 | 1,900,255.5 | 1,912,077.0 | 4,069.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,908,594.1 | 1.3868 | 1,902,797.9 | 1,916,720.4 | 5,399.4 | 1.002x | 1.002x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,456,863.7 | 1.3894 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,461,466.6 | 1.3938 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 358,836.9 | 1.3689 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 359,217.8 | 1.3703 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 87,539.9 | 1.3358 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 87,887.9 | 1.3411 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,632.7 | 1,632.0 | 1,644.2 | 4.7 | 1.000x | 1.000x | 75 | 21.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,643.9 | 1,630.4 | 1,657.2 | 9.1 | 1.007x | 1.007x | 75 | 21.9 | 9.0 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,167.8 | 0.0168 | 23,143.5 | 23,266.2 | 42.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,175.2 | 0.0168 | 23,152.9 | 23,183.5 | 10.5 | 1.000x | 1.000x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,673.7 | 0.0169 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,681.1 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,381.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,383.5 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,112.0 | 0.0170 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 670.2 | 662.8 | 672.9 | 3.7 | 1.000x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 671.6 | 670.7 | 671.7 | 0.4 | 1.002x | 1.002x | 75 | 9.0 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 482,716.5 | 0.3507 | 482,682.0 | 483,742.3 | 404.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 482,836.1 | 0.3508 | 482,693.9 | 483,058.5 | 132.0 | 1.000x | 1.000x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 367,921.6 | 0.3509 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 367,997.8 | 0.3510 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 91,773.4 | 0.3501 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 91,790.0 | 0.3502 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 23,069.9 | 0.3520 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 22,990.7 | 0.3508 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,105.4 | 1,095.7 | 1,110.5 | 4.8 | 1.000x | 1.000x | 75 | 14.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,113.7 | 1,107.4 | 1,152.7 | 16.3 | 1.007x | 1.007x | 75 | 14.8 | 9.0 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.1 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.5 | 0.1 | 1.003x | 1.003x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0001 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 405.6 | 404.8 | 725.3 | 127.8 | 1.000x | 1.000x | 75 | 5.4 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 406.3 | 404.6 | 409.3 | 1.5 | 1.002x | 1.002x | 75 | 5.4 | 8.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 687,410.1 | 0.4995 | 682,487.1 | 690,952.4 | 3,191.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 690,878.2 | 0.5020 | 687,005.2 | 691,798.5 | 1,839.9 | 1.005x | 1.005x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 531,422.5 | 0.5068 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 534,130.5 | 0.5094 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 127,044.0 | 0.4846 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 127,610.0 | 0.4868 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 28,790.7 | 0.4393 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 29,137.6 | 0.4446 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 767.3 | 765.1 | 770.4 | 1.8 | 1.000x | 1.000x | 75 | 10.2 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 772.1 | 771.0 | 775.0 | 1.3 | 1.006x | 1.006x | 75 | 10.3 | 8.9 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 32.9 | 0.0000 | 32.9 | 33.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 33.9 | 0.0000 | 30.9 | 35.6 | 1.8 | 1.030x | 1.030x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.7 | 0.0002 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 807.3 | 805.9 | 809.9 | 1.6 | 1.000x | 1.000x | 75 | 10.8 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 833.1 | 832.5 | 835.5 | 1.1 | 1.032x | 1.032x | 75 | 11.1 | 8.9 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 30.9 | 0.0000 | 30.8 | 30.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 34.5 | 0.0000 | 34.3 | 36.3 | 0.9 | 1.117x | 1.117x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 11.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.1 | 0.0002 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 796.4 | 796.0 | 807.8 | 4.5 | 1.000x | 1.000x | 75 | 10.6 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 862.8 | 862.6 | 864.1 | 0.5 | 1.083x | 1.083x | 75 | 11.5 | 8.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,119.2 | 0.0168 | 23,103.8 | 23,140.3 | 12.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,139.0 | 0.0168 | 23,127.1 | 23,153.9 | 11.1 | 1.001x | 1.001x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,617.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,637.9 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,382.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,382.8 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,112.0 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.6 | 0.0169 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 681.6 | 681.0 | 683.6 | 1.1 | 1.000x | 1.000x | 75 | 9.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 692.1 | 681.7 | 697.5 | 5.2 | 1.015x | 1.015x | 75 | 9.2 | 8.9 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,082.8 | 0.0168 | 23,070.8 | 23,097.8 | 10.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,149.3 | 0.0168 | 23,126.1 | 23,162.5 | 14.8 | 1.003x | 1.003x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,599.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,658.6 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,377.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,379.0 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,107.1 | 0.0169 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,571.5 | 1,563.0 | 1,746.9 | 71.3 | 1.000x | 1.000x | 75 | 21.0 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,597.1 | 1,556.7 | 1,637.1 | 26.4 | 1.016x | 1.016x | 75 | 21.3 | 9.0 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.4 | 28.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 28.6 | 0.0000 | 28.5 | 31.1 | 1.0 | 1.003x | 1.003x |

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

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 814.8 | 806.4 | 825.8 | 6.2 | 1.000x | 1.000x | 75 | 10.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 816.3 | 811.4 | 865.7 | 20.1 | 1.002x | 1.002x | 75 | 10.9 | 9.0 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 30.8 | 0.0000 | 30.8 | 30.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 30.9 | 0.0000 | 30.5 | 30.9 | 0.2 | 1.003x | 1.003x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10.3 | 0.0002 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 883.5 | 880.8 | 890.2 | 3.5 | 1.000x | 1.000x | 75 | 11.8 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 890.2 | 883.3 | 896.3 | 4.2 | 1.008x | 1.008x | 75 | 11.9 | 8.9 | 100% |

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,506,963.0 | 4.7280 | 6,506,273.5 | 6,527,100.7 | 8,005.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 6,531,321.2 | 4.7457 | 6,500,650.8 | 6,535,222.4 | 15,737.8 | 1.004x | 1.004x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 4,963,779.6 | 4.7338 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,981,874.1 | 4.7511 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,235,995.0 | 4.7149 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,236,049.7 | 4.7152 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 307,974.2 | 4.6993 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 308,307.6 | 4.7044 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 6,622.3 | 6,572.3 | 6,903.6 | 123.8 | 1.000x | 1.000x | 75 | 88.3 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 6,625.9 | 6,616.8 | 6,745.2 | 55.3 | 1.001x | 1.001x | 75 | 88.3 | 8.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 224.0 | 0.0002 | 223.0 | 224.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 224.3 | 0.0002 | 222.8 | 227.9 | 1.7 | 1.001x | 1.001x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 58.7 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 58.5 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 95.5 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 96.2 | 0.0004 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 69.5 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 69.5 | 0.0011 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 12,107.0 | 12,097.6 | 12,163.4 | 24.3 | 1.000x | 1.000x | 75 | 161.4 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,141.4 | 12,118.6 | 12,191.4 | 24.4 | 1.003x | 1.003x | 75 | 161.9 | 8.9 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,039,893.2 | 7.2951 | 9,798,172.7 | 10,095,536.9 | 105,356.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 10,050,259.0 | 7.3026 | 9,762,992.9 | 10,071,252.1 | 115,341.7 | 1.001x | 1.001x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 7,649,408.5 | 7.2950 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 7,654,845.2 | 7.3002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,914,081.6 | 7.3016 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,907,243.0 | 7.2756 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 479,829.5 | 7.3216 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 467,223.7 | 7.1293 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,871.7 | 10,820.9 | 11,193.2 | 165.8 | 1.000x | 1.000x | 75 | 145.0 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 10,886.6 | 10,823.8 | 11,173.7 | 145.6 | 1.001x | 1.001x | 75 | 145.2 | 9.0 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 343,232.8 | 0.2494 | 342,913.3 | 343,569.6 | 216.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 343,338.0 | 0.2495 | 343,080.8 | 343,480.3 | 138.2 | 1.000x | 1.000x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 264,071.2 | 0.2518 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 264,033.6 | 0.2518 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 64,493.0 | 0.2460 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 64,534.3 | 0.2462 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 14,655.8 | 0.2236 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 14,761.9 | 0.2252 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 692.6 | 692.0 | 693.2 | 0.5 | 1.000x | 1.000x | 75 | 9.2 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 692.8 | 691.0 | 693.9 | 1.0 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,126.8 | 0.0168 | 23,117.1 | 23,136.8 | 6.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,171.7 | 0.0168 | 23,132.5 | 23,178.4 | 17.4 | 1.002x | 1.002x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,633.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,688.0 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,384.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,380.0 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,109.6 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,106.6 | 0.0169 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,148.7 | 1,147.2 | 1,153.9 | 2.7 | 1.000x | 1.000x | 75 | 15.3 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,155.9 | 1,141.0 | 1,163.4 | 7.8 | 1.006x | 1.006x | 75 | 15.4 | 8.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,120.9 | 0.0168 | 23,119.9 | 23,149.8 | 11.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,125.9 | 0.0168 | 23,096.1 | 23,156.2 | 20.2 | 1.000x | 1.000x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,636.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,633.9 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,377.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,383.3 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,109.2 | 0.0169 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,125.7 | 1,120.9 | 1,139.2 | 7.5 | 1.000x | 1.000x | 75 | 15.0 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,169.9 | 1,152.7 | 1,179.1 | 9.6 | 1.039x | 1.039x | 75 | 15.6 | 8.9 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 47.2 | 0.0000 | 47.1 | 48.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 0.0000 | 47.1 | 47.4 | 0.1 | 1.001x | 1.001x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 15.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15.7 | 0.0002 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 10,184,991.8 | 10,181,947.8 | 10,195,301.6 | 4,770.0 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 135,799.9 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 10,200,688.9 | 10,191,229.8 | 10,203,686.2 | 4,421.0 | 1.002x | 1.002x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 136,009.2 | 8.9 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 479,298.2 | 0.3483 | 479,011.8 | 480,093.3 | 393.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 479,788.9 | 0.3486 | 479,168.6 | 480,770.8 | 634.6 | 1.001x | 1.001x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 366,556.3 | 0.3496 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 366,696.7 | 0.3497 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 90,118.7 | 0.3438 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 90,414.6 | 0.3449 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 22,599.9 | 0.3448 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 22,572.3 | 0.3444 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,254.1 | 1,251.9 | 1,258.4 | 2.1 | 1.000x | 1.000x | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,254.7 | 1,252.9 | 1,266.4 | 5.4 | 1.000x | 1.000x | 75 | 16.7 | 9.0 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.2 | 0.0 | 1.001x | 1.001x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5.1 | 0.0001 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 524.6 | 523.3 | 528.2 | 1.8 | 1.000x | 1.000x | 75 | 7.0 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 527.2 | 523.4 | 530.0 | 2.3 | 1.005x | 1.005x | 75 | 7.0 | 8.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 218,965.7 | 0.1591 | 218,860.5 | 219,213.5 | 121.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 219,167.2 | 0.1592 | 218,967.4 | 219,773.6 | 279.5 | 1.001x | 1.001x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 168,520.0 | 0.1607 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 168,411.0 | 0.1606 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 40,304.6 | 0.1537 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 40,380.8 | 0.1540 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 10,129.7 | 0.1546 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 10,283.5 | 0.1569 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 682.9 | 681.8 | 702.6 | 8.0 | 1.000x | 1.000x | 75 | 9.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 690.9 | 682.8 | 706.1 | 8.3 | 1.012x | 1.012x | 75 | 9.2 | 8.9 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,196,118.7 | 3.0489 | 4,195,583.4 | 4,198,430.8 | 1,001.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,196,930.2 | 3.0495 | 4,195,791.8 | 4,198,722.1 | 988.9 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,197,705.9 | 3.0496 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,197,811.1 | 3.0497 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 800,270.0 | 3.0528 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 800,478.4 | 3.0536 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 198,238.0 | 3.0249 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 198,454.3 | 3.0282 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,482.4 | 2,478.1 | 2,485.1 | 2.7 | 1.000x | 1.000x | 75 | 33.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,499.3 | 2,485.7 | 2,511.3 | 9.2 | 1.007x | 1.007x | 75 | 33.3 | 8.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,090,682.0 | 1.5191 | 2,082,843.9 | 2,125,342.2 | 15,406.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,117,986.5 | 1.5389 | 2,098,584.6 | 2,130,705.4 | 12,557.9 | 1.013x | 1.013x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,600,353.8 | 1.5262 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,623,664.0 | 1.5484 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 391,784.4 | 1.4945 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 394,508.5 | 1.5049 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 98,543.9 | 1.5037 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 98,542.3 | 1.5036 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,510.7 | 1,496.3 | 1,517.5 | 7.5 | 1.000x | 1.000x | 75 | 20.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,513.6 | 1,504.7 | 1,514.8 | 4.0 | 1.002x | 1.002x | 75 | 20.2 | 8.9 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,106.8 | 0.0168 | 23,097.7 | 23,127.1 | 12.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,112.9 | 0.0168 | 23,089.8 | 23,128.6 | 13.5 | 1.000x | 1.000x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,613.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,623.8 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,378.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,380.4 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,106.7 | 0.0169 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 679.6 | 662.6 | 685.5 | 7.9 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 681.3 | 677.3 | 684.7 | 2.4 | 1.002x | 1.002x | 75 | 9.1 | 9.0 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,096.5 | 0.0168 | 23,078.6 | 23,119.5 | 13.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,123.1 | 0.0168 | 23,092.6 | 23,139.8 | 16.8 | 1.001x | 1.001x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,594.5 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,632.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,380.3 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,386.4 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,110.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,107.7 | 0.0169 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 742.4 | 725.3 | 745.1 | 7.2 | 1.000x | 1.000x | 75 | 9.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 750.1 | 742.3 | 753.4 | 4.5 | 1.010x | 1.010x | 75 | 10.0 | 9.0 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 37.9 | 0.0000 | 37.8 | 38.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 38.1 | 0.0000 | 37.9 | 56.2 | 7.3 | 1.006x | 1.006x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.7 | 0.0002 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,024.8 | 1,023.2 | 1,026.8 | 1.5 | 1.000x | 1.000x | 75 | 13.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,025.6 | 1,022.4 | 1,027.3 | 1.6 | 1.001x | 1.001x | 75 | 13.7 | 9.0 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,036,699.4 | 2.9331 | 4,033,933.2 | 4,045,474.8 | 3,977.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,041,078.3 | 2.9363 | 4,035,254.4 | 4,044,401.2 | 3,578.0 | 1.001x | 1.001x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,091,194.3 | 2.9480 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,091,734.8 | 2.9485 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 760,574.8 | 2.9014 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 762,816.2 | 2.9099 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 184,144.3 | 2.8098 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 184,315.5 | 2.8124 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,484.0 | 2,473.4 | 2,548.5 | 29.7 | 1.000x | 1.000x | 75 | 33.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,484.2 | 2,478.0 | 2,491.5 | 5.5 | 1.000x | 1.000x | 75 | 33.1 | 8.9 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,003,639.1 | 2.9091 | 4,001,568.5 | 4,040,284.3 | 14,871.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,007,222.3 | 2.9117 | 4,003,126.6 | 4,031,069.2 | 10,738.8 | 1.001x | 1.001x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,067,895.8 | 2.9258 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,069,270.5 | 2.9271 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 753,274.6 | 2.8735 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 754,945.4 | 2.8799 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 182,352.1 | 2.7825 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 183,006.4 | 2.7925 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,452.5 | 2,447.0 | 2,465.5 | 6.7 | 1.000x | 1.000x | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,456.8 | 2,446.1 | 2,527.4 | 29.3 | 1.002x | 1.002x | 75 | 32.8 | 9.0 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 936,658.6 | 0.6806 | 936,427.6 | 937,615.9 | 422.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,009,042.8 | 0.7332 | 1,007,747.7 | 1,009,638.8 | 712.0 | 1.077x | 1.077x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 716,916.1 | 0.6837 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 772,416.7 | 0.7366 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 175,353.1 | 0.6689 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 188,488.0 | 0.7190 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 44,474.3 | 0.6786 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 47,727.0 | 0.7283 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,888.1 | 1,882.3 | 1,888.8 | 2.4 | 1.000x | 1.000x | 75 | 25.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,924.2 | 1,920.9 | 1,929.9 | 3.1 | 1.019x | 1.019x | 75 | 25.7 | 9.0 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 930,370.0 | 0.6760 | 929,222.3 | 932,712.3 | 1,253.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 930,464.2 | 0.6761 | 928,977.6 | 932,116.0 | 1,126.9 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 711,825.6 | 0.6788 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 712,647.1 | 0.6796 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 174,349.7 | 0.6651 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 173,868.1 | 0.6633 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 44,106.6 | 0.6730 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 43,988.4 | 0.6712 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,830.1 | 1,789.5 | 1,833.0 | 16.5 | 1.000x | 1.000x | 75 | 24.4 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,830.2 | 1,826.9 | 1,831.9 | 1.8 | 1.000x | 1.000x | 75 | 24.4 | 8.9 | 100% |

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 3,987,618.5 | 2.8974 | 3,986,198.8 | 3,991,462.6 | 1,770.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,989,268.2 | 2.8986 | 3,986,942.2 | 3,989,917.2 | 1,152.1 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,036,103.2 | 2.8955 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,038,464.7 | 2.8977 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 761,480.0 | 2.9048 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 760,639.1 | 2.9016 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 190,817.6 | 2.9116 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 190,113.0 | 2.9009 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,765.3 | 1,762.1 | 1,782.8 | 8.0 | 1.000x | 1.000x | 75 | 23.5 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,782.0 | 1,779.0 | 1,807.8 | 10.4 | 1.009x | 1.009x | 75 | 23.8 | 9.0 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,132.5 | 0.0168 | 23,128.3 | 23,159.9 | 11.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,171.6 | 0.0168 | 23,148.0 | 23,201.2 | 18.8 | 1.002x | 1.002x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,646.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,635.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,381.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,426.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,109.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,111.8 | 0.0170 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 926.7 | 926.3 | 929.0 | 1.0 | 1.000x | 1.000x | 75 | 12.4 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 931.1 | 927.1 | 938.3 | 3.7 | 1.005x | 1.005x | 75 | 12.4 | 8.9 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 3,941,429.5 | 2.8639 | 3,940,639.3 | 3,945,946.2 | 1,911.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,083,618.4 | 2.9672 | 4,083,420.8 | 4,086,248.9 | 1,058.8 | 1.036x | 1.036x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,002,961.1 | 2.8638 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,111,540.4 | 2.9674 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 751,970.5 | 2.8685 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 779,156.4 | 2.9722 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 187,317.9 | 2.8582 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 193,073.4 | 2.9461 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,188.9 | 1,187.0 | 1,191.4 | 1.7 | 1.000x | 1.000x | 75 | 15.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,211.5 | 1,209.9 | 1,214.4 | 1.6 | 1.019x | 1.019x | 75 | 16.2 | 9.0 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 124,629.2 | 0.0906 | 124,386.3 | 124,962.2 | 184.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 124,662.6 | 0.0906 | 124,415.1 | 124,961.2 | 173.3 | 1.000x | 1.000x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 102,068.5 | 0.0973 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 102,181.3 | 0.0974 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 18,883.5 | 0.0720 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 18,946.7 | 0.0723 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 3,628.0 | 0.0554 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,472.9 | 0.0530 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,512.6 | 1,509.5 | 1,515.1 | 1.9 | 1.000x | 1.000x | 75 | 20.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,519.9 | 1,513.5 | 1,522.8 | 3.5 | 1.005x | 1.005x | 75 | 20.3 | 9.0 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 353,989.2 | 0.2572 | 353,897.4 | 354,105.1 | 67.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 354,294.8 | 0.2574 | 354,138.4 | 354,883.9 | 267.8 | 1.001x | 1.001x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 271,774.0 | 0.2592 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 271,992.1 | 0.2594 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 66,928.6 | 0.2553 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 66,998.1 | 0.2556 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 15,259.4 | 0.2328 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 15,295.5 | 0.2334 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,261.7 | 1,258.9 | 1,272.4 | 5.1 | 1.000x | 1.000x | 75 | 16.8 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,314.9 | 1,304.9 | 1,321.8 | 5.6 | 1.042x | 1.042x | 75 | 17.5 | 8.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,120.3 | 0.0168 | 23,095.6 | 23,145.3 | 18.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,143.4 | 0.0168 | 23,128.4 | 23,161.8 | 12.4 | 1.001x | 1.001x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,617.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,634.5 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,388.2 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,395.9 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,109.3 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,108.9 | 0.0169 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,044.2 | 1,042.3 | 1,045.8 | 1.3 | 1.000x | 1.000x | 75 | 13.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,074.8 | 1,074.1 | 1,077.2 | 1.1 | 1.029x | 1.029x | 75 | 14.3 | 9.0 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 352,301.6 | 0.2560 | 352,070.6 | 352,607.0 | 188.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 352,469.9 | 0.2561 | 351,951.3 | 353,771.2 | 702.7 | 1.000x | 1.000x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 282,857.7 | 0.2698 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 282,858.4 | 0.2698 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 58,464.3 | 0.2230 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 58,370.5 | 0.2227 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 11,055.3 | 0.1687 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11,093.2 | 0.1693 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 659.6 | 659.2 | 661.1 | 0.7 | 1.000x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 660.6 | 658.1 | 662.8 | 1.9 | 1.001x | 1.001x | 75 | 8.8 | 9.0 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 40.0 | 0.0000 | 40.0 | 40.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 40.0 | 0.0000 | 40.0 | 40.1 | 0.0 | 1.000x | 1.000x |

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

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 913.8 | 912.3 | 934.1 | 8.3 | 1.000x | 1.000x | 75 | 12.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 918.0 | 916.4 | 953.7 | 14.4 | 1.005x | 1.005x | 75 | 12.2 | 9.0 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 6,984,577.1 | 5.0751 | 6,958,609.2 | 7,014,284.4 | 19,416.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,000,686.7 | 5.0868 | 6,955,285.2 | 7,017,901.6 | 22,096.8 | 1.002x | 1.002x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5,355,484.4 | 5.1074 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 5,377,227.1 | 5.1281 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,305,138.7 | 4.9787 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 1,307,260.9 | 4.9868 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 313,542.4 | 4.7843 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 316,225.5 | 4.8252 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 3,117.7 | 3,102.9 | 3,122.1 | 7.1 | 1.000x | 1.000x | 75 | 41.6 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 3,119.6 | 3,107.2 | 3,143.4 | 13.5 | 1.001x | 1.001x | 75 | 41.6 | 9.0 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 37.9 | 0.0000 | 36.8 | 40.8 | 1.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 39.5 | 0.0000 | 38.7 | 41.6 | 1.0 | 1.041x | 1.041x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 13.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 14.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 12.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 12.9 | 0.0002 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,011.6 | 1,011.3 | 1,015.9 | 1.7 | 1.000x | 1.000x | 75 | 13.5 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,012.3 | 1,009.7 | 1,020.7 | 4.5 | 1.001x | 1.001x | 75 | 13.5 | 8.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 29.3 | 0.0000 | 29.3 | 31.6 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.4 | 0.0000 | 29.4 | 29.4 | 0.0 | 1.002x | 1.002x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0001 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 805.2 | 803.2 | 815.4 | 4.5 | 1.000x | 1.000x | 75 | 10.7 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 805.7 | 803.4 | 808.4 | 1.6 | 1.001x | 1.001x | 75 | 10.7 | 9.0 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 29.3 | 0.0000 | 29.2 | 29.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 29.3 | 0.0000 | 29.2 | 29.8 | 0.2 | 1.000x | 1.000x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 9.8 | 0.0001 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 756.0 | 755.8 | 760.3 | 1.7 | 1.000x | 1.000x | 75 | 10.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 757.7 | 756.9 | 758.6 | 0.6 | 1.002x | 1.002x | 75 | 10.1 | 8.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 82,495.0 | 0.0599 | 82,246.9 | 82,768.3 | 172.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 82,615.5 | 0.0600 | 82,474.9 | 82,718.1 | 78.1 | 1.001x | 1.001x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 68,278.8 | 0.0651 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 68,431.8 | 0.0653 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 11,732.1 | 0.0448 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 11,746.6 | 0.0448 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 2,454.0 | 0.0374 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 2,430.9 | 0.0371 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 691.5 | 690.7 | 697.6 | 3.2 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 693.2 | 690.1 | 698.6 | 3.5 | 1.002x | 1.002x | 75 | 9.2 | 9.0 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 4,077,774.3 | 2.9629 | 4,076,143.3 | 4,084,319.6 | 3,065.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 4,083,187.4 | 2.9669 | 4,074,977.4 | 4,085,771.0 | 4,262.1 | 1.001x | 1.001x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 3,109,527.2 | 2.9655 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 3,113,655.2 | 2.9694 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 776,496.4 | 2.9621 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 777,510.1 | 2.9660 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 191,371.3 | 2.9201 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 191,777.0 | 2.9263 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 2,691.5 | 2,689.2 | 2,707.0 | 6.5 | 1.000x | 1.000x | 75 | 35.9 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 2,694.8 | 2,693.4 | 2,702.2 | 3.2 | 1.001x | 1.001x | 75 | 35.9 | 8.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,360,745.7 | 0.9887 | 1,359,353.2 | 1,361,758.0 | 791.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,362,579.8 | 0.9901 | 1,360,847.7 | 1,371,510.1 | 4,276.3 | 1.001x | 1.001x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 1,029,493.2 | 0.9818 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,032,692.4 | 0.9849 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 261,531.8 | 0.9977 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 262,059.6 | 0.9997 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 68,816.0 | 1.0500 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 68,810.8 | 1.0500 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 667.8 | 667.3 | 673.9 | 2.5 | 1.000x | 1.000x | 75 | 8.9 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 670.8 | 666.5 | 698.1 | 11.7 | 1.004x | 1.004x | 75 | 8.9 | 8.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,004,974.1 | 0.7302 | 996,551.8 | 1,025,345.2 | 11,275.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,007,643.0 | 0.7322 | 999,103.4 | 1,022,778.6 | 8,487.2 | 1.003x | 1.003x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 756,650.3 | 0.7216 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 760,470.1 | 0.7252 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 201,096.6 | 0.7671 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 196,730.4 | 0.7505 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 48,812.1 | 0.7448 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 48,448.3 | 0.7393 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 1,157.5 | 1,151.9 | 1,162.0 | 3.5 | 1.000x | 1.000x | 75 | 15.4 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 1,161.5 | 1,157.6 | 1,162.4 | 1.7 | 1.003x | 1.003x | 75 | 15.5 | 8.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 12,101,921.3 | 8.7934 | 12,097,659.0 | 12,828,822.3 | 288,639.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 12,136,993.2 | 8.8188 | 12,103,450.8 | 12,247,554.2 | 51,514.8 | 1.003x | 1.003x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 9,229,610.1 | 8.8020 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 9,254,238.5 | 8.8255 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 2,298,960.0 | 8.7698 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 2,306,685.0 | 8.7993 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 574,667.5 | 8.7687 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 576,168.8 | 8.7916 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 7,342.5 | 7,334.4 | 7,441.8 | 40.0 | 1.000x | 1.000x | 75 | 97.9 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 7,355.8 | 7,336.7 | 7,411.7 | 25.3 | 1.002x | 1.002x | 75 | 98.1 | 9.0 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 23,139.5 | 0.0168 | 23,119.4 | 23,148.9 | 10.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 23,158.3 | 0.0168 | 23,126.7 | 23,170.5 | 15.6 | 1.001x | 1.001x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 17,611.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 17,656.1 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 4,417.8 | 0.0169 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 4,390.7 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 1,111.0 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,108.4 | 0.0169 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 692.4 | 689.0 | 693.9 | 1.7 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 694.7 | 692.4 | 703.7 | 3.9 | 1.003x | 1.003x | 75 | 9.3 | 9.0 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 19.6 | 0.0000 | 19.6 | 19.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 19.6 | 0.0000 | 19.6 | 19.6 | 0.0 | 1.002x | 1.002x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.5 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna` | 6.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6.5 | 0.0001 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | measured | `plain` | same program | 456.4 | 456.3 | 460.4 | 1.6 | 1.000x | 1.000x | 75 | 6.1 | 9.0 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna` | measured | `plain` | same program | 456.8 | 456.4 | 463.8 | 2.8 | 1.001x | 1.001x | 75 | 6.1 | 8.9 | 100% |

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
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,868 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,078 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 4,183 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,223 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,328 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,075 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,180 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,782 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,887 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1464711 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1485918 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
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
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 204,170,939.0 | 202,678,862.0 | 214,317,001.0 | 4,238,510.1 | 5 | 31,768 | 26,113 | 25,828 | 0.021 | compiled=5 | 1,662,279.0 | 202,273,509.0 | 192,401.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 209,465,756.0 | 205,006,974.0 | 216,399,161.0 | 4,144,752.3 | 5 | 31,768 | 26,331 | 26,046 | 0.020 | compiled=5 | 1,689,338.0 | 206,418,000.0 | 186,811.0 |
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 213,875,987.0 | 207,145,905.0 | 214,542,512.0 | 3,475,290.0 | 5 | 31,768 | 26,113 | 25,828 | 0.016 | compiled=5 | 1,598,677.0 | 212,058,599.0 | 106,401.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 214,241,260.0 | 208,972,254.0 | 214,705,844.0 | 2,192,573.2 | 5 | 31,768 | 26,331 | 26,046 | 0.010 | compiled=5 | 1,589,738.0 | 212,550,781.0 | 106,881.0 |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 147,013,185.0 | 141,032,804.0 | 152,568,484.0 | 4,281,632.4 | 5 | 27,736 | 16,705 | 14,320 | 0.029 | compiled=5 | 1,619,669.0 | 145,489,147.0 | 201,351.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 148,115,001.0 | 137,824,279.0 | 152,103,362.0 | 4,881,905.6 | 5 | 27,656 | 16,158 | 13,773 | 0.033 | compiled=5 | 1,710,779.0 | 146,415,862.0 | 188,621.0 |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 145,360,819.0 | 138,555,625.0 | 151,761,900.0 | 4,958,567.9 | 5 | 27,736 | 16,705 | 14,320 | 0.034 | compiled=5 | 1,620,388.0 | 143,798,301.0 | 102,871.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 143,283,229.0 | 135,875,233.0 | 148,718,654.0 | 5,249,842.4 | 5 | 27,656 | 16,158 | 13,773 | 0.037 | compiled=5 | 1,599,768.0 | 141,536,290.0 | 103,381.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 225,515,799.0 | 213,543,977.0 | 226,195,273.0 | 4,857,940.0 | 5 | 31,728 | 26,549 | 26,234 | 0.022 | compiled=5 | 1,744,129.0 | 223,678,709.0 | 97,471.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 225,428,177.0 | 221,244,537.0 | 228,413,613.0 | 2,389,675.9 | 5 | 31,728 | 26,664 | 26,349 | 0.011 | compiled=5 | 1,714,939.0 | 223,622,018.0 | 185,841.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 222,798,702.0 | 217,483,067.0 | 227,396,766.0 | 3,258,394.1 | 5 | 31,728 | 26,549 | 26,234 | 0.015 | compiled=5 | 1,911,759.0 | 219,460,445.0 | 186,721.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 218,085,010.0 | 215,525,917.0 | 228,648,022.0 | 5,579,617.2 | 5 | 31,728 | 26,664 | 26,349 | 0.026 | compiled=5 | 2,121,451.0 | 216,326,450.0 | 108,310.0 |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 351,390,474.0 | 349,059,093.0 | 362,081,940.0 | 4,929,611.6 | 5 | 32,072 | 35,699 | 27,100 | 0.014 | compiled=5 | 4,573,993.0 | 346,878,442.0 | 97,150.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 359,285,936.0 | 357,448,725.0 | 369,693,659.0 | 4,332,970.7 | 5 | 32,120 | 35,420 | 27,908 | 0.012 (max is trial 1) | compiled=5 | 2,180,221.0 | 357,019,304.0 | 103,430.0 |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 352,616,194.0 | 344,315,372.0 | 364,042,151.0 | 6,291,192.1 | 5 | 32,072 | 35,699 | 27,100 | 0.018 | compiled=5 | 2,174,640.0 | 350,337,264.0 | 104,290.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 354,518,104.0 | 351,770,890.0 | 363,605,059.0 | 4,588,465.4 | 5 | 32,120 | 35,420 | 27,908 | 0.013 | compiled=5 | 2,256,721.0 | 352,177,973.0 | 187,931.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 351,002,493.0 | 344,659,349.0 | 358,677,143.0 | 4,579,602.2 | 5 | 32,104 | 36,025 | 27,347 | 0.013 | compiled=5 | 2,220,831.0 | 348,685,461.0 | 110,001.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 360,138,779.0 | 355,370,675.0 | 361,755,258.0 | 2,348,075.8 | 5 | 32,160 | 35,750 | 28,159 | 0.007 | compiled=5 | 2,207,892.0 | 357,808,238.0 | 117,150.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 349,899,551.0 | 344,565,335.0 | 351,794,872.0 | 2,623,963.3 | 5 | 32,104 | 36,025 | 27,347 | 0.007 | compiled=5 | 2,099,741.0 | 347,624,510.0 | 110,791.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 357,748,769.0 | 352,488,054.0 | 363,413,488.0 | 3,787,020.6 | 5 | 32,160 | 35,750 | 28,159 | 0.011 (max is trial 1) | compiled=5 | 2,137,630.0 | 355,581,779.0 | 210,791.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 220,379,653.0 | 216,740,213.0 | 243,882,313.0 | 9,923,813.9 | 5 | 32,088 | 32,984 | 27,353 | 0.045 | compiled=5 | 2,161,101.0 | 215,936,099.0 | 111,220.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 230,371,364.0 | 221,155,056.0 | 233,542,969.0 | 5,197,766.2 | 5 | 32,184 | 35,010 | 28,761 | 0.023 | compiled=5 | 2,209,152.0 | 228,204,672.0 | 114,600.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 223,611,416.0 | 217,285,695.0 | 225,366,075.0 | 2,836,425.8 | 5 | 32,088 | 32,984 | 27,353 | 0.013 (max is trial 1) | compiled=5 | 1,995,820.0 | 221,407,645.0 | 107,401.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 229,713,526.0 | 215,120,485.0 | 234,652,370.0 | 6,730,858.2 | 5 | 32,184 | 35,010 | 28,761 | 0.029 | compiled=5 | 2,149,571.0 | 227,584,846.0 | 101,400.0 |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 260,743,800.0 | 255,997,426.0 | 264,381,799.0 | 2,810,594.5 | 5 | 31,952 | 33,849 | 31,823 | 0.011 | compiled=5 | 1,880,220.0 | 258,101,446.0 | 101,920.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,471,488.0 | 249,248,990.0 | 263,930,645.0 | 6,338,709.8 | 5 | 31,952 | 33,777 | 31,751 | 0.025 | compiled=5 | 1,875,389.0 | 250,650,768.0 | 100,860.0 |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 257,097,662.0 | 252,889,272.0 | 261,726,355.0 | 3,433,595.6 | 5 | 31,952 | 33,849 | 31,823 | 0.013 | compiled=5 | 1,861,569.0 | 255,267,523.0 | 218,381.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 254,603,349.0 | 245,266,223.0 | 263,872,527.0 | 6,124,027.2 | 5 | 31,952 | 33,777 | 31,751 | 0.024 | compiled=5 | 1,877,709.0 | 252,749,450.0 | 104,981.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 215,497,877.0 | 206,905,314.0 | 219,769,957.0 | 4,677,698.3 | 5 | 27,592 | 24,783 | 24,321 | 0.022 | compiled=5 | 1,683,989.0 | 213,734,888.0 | 195,301.0 |
| `doubled-word` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 212,728,323.0 | 202,086,128.0 | 216,175,661.0 | 5,217,725.4 | 5 | 27,592 | 24,896 | 24,434 | 0.025 | compiled=5 | 1,699,899.0 | 210,929,314.0 | 108,841.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 217,677,947.0 | 209,472,856.0 | 218,220,210.0 | 3,576,536.0 | 5 | 27,592 | 24,783 | 24,321 | 0.016 | compiled=5 | 1,592,128.0 | 215,961,449.0 | 118,420.0 |
| `doubled-word` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 211,864,468.0 | 205,482,097.0 | 216,624,902.0 | 3,992,700.5 | 5 | 27,592 | 24,896 | 24,434 | 0.019 | compiled=5 | 1,612,888.0 | 209,955,139.0 | 189,191.0 |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 236,591,816.0 | 223,122,686.0 | 246,170,255.0 | 8,145,341.9 | 5 | 31,856 | 27,735 | 27,219 | 0.034 | compiled=5 | 1,784,869.0 | 234,720,626.0 | 193,901.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 236,154,553.0 | 223,136,516.0 | 246,007,184.0 | 7,312,531.6 | 5 | 31,856 | 27,848 | 27,332 | 0.031 | compiled=5 | 1,760,599.0 | 234,215,263.0 | 104,861.0 |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 239,704,005.0 | 235,644,715.0 | 243,428,165.0 | 2,903,316.6 | 5 | 31,856 | 27,735 | 27,219 | 0.012 | compiled=5 | 1,704,369.0 | 235,949,717.0 | 194,611.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 237,302,835.0 | 236,037,207.0 | 241,571,865.0 | 1,974,016.2 | 5 | 31,856 | 27,848 | 27,332 | 0.008 (max is trial 1) | compiled=5 | 1,693,229.0 | 235,386,605.0 | 200,741.0 |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 206,673,472.0 | 201,395,364.0 | 208,387,341.0 | 2,945,944.1 | 5 | 31,792 | 27,235 | 25,162 | 0.014 | compiled=5 | 1,763,349.0 | 204,541,201.0 | 101,680.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 197,766,636.0 | 195,324,824.0 | 204,473,620.0 | 3,565,587.2 | 5 | 31,800 | 27,653 | 25,509 | 0.018 | compiled=5 | 1,790,829.0 | 195,607,535.0 | 98,110.0 |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 204,944,752.0 | 201,855,999.0 | 206,241,652.0 | 1,872,043.1 | 5 | 31,792 | 27,355 | 25,282 | 0.009 | compiled=5 | 1,689,308.0 | 203,145,884.0 | 103,210.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 200,377,642.0 | 198,779,084.0 | 200,537,171.0 | 668,137.6 | 5 | 31,800 | 27,773 | 25,629 | 0.003 | compiled=5 | 1,706,228.0 | 198,499,962.0 | 188,601.0 |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 224,566,794.0 | 219,483,048.0 | 233,613,840.0 | 4,570,219.7 | 5 | 31,912 | 29,236 | 27,290 | 0.020 | compiled=5 | 1,789,300.0 | 222,630,683.0 | 107,511.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 218,673,893.0 | 216,325,382.0 | 229,423,088.0 | 4,984,436.4 | 5 | 31,912 | 29,667 | 27,637 | 0.023 (max is trial 1) | compiled=5 | 3,451,378.0 | 214,081,399.0 | 182,381.0 |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 223,467,026.0 | 218,793,453.0 | 227,388,095.0 | 2,850,878.9 | 5 | 31,912 | 29,236 | 27,290 | 0.013 | compiled=5 | 1,834,499.0 | 221,536,816.0 | 102,651.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 225,112,534.0 | 215,074,185.0 | 228,683,722.0 | 5,078,152.8 | 5 | 31,912 | 29,667 | 27,637 | 0.023 | compiled=5 | 1,817,110.0 | 223,216,984.0 | 99,071.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 207,375,825.0 | 206,021,257.0 | 217,378,828.0 | 4,412,052.1 | 5 | 31,728 | 25,768 | 25,768 | 0.021 | compiled=5 | 1,596,068.0 | 205,567,916.0 | 104,071.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 216,055,219.0 | 208,952,684.0 | 226,405,093.0 | 6,062,853.4 | 5 | 31,728 | 25,881 | 25,881 | 0.028 | compiled=5 | 1,798,619.0 | 214,097,429.0 | 191,691.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 210,571,722.0 | 207,238,055.0 | 215,970,688.0 | 3,507,028.2 | 5 | 31,728 | 25,768 | 25,768 | 0.017 | compiled=5 | 1,679,419.0 | 206,964,694.0 | 207,521.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 212,938,384.0 | 207,571,428.0 | 221,227,525.0 | 5,233,395.5 | 5 | 31,728 | 25,881 | 25,881 | 0.025 | compiled=5 | 1,667,869.0 | 209,296,405.0 | 190,031.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 156,367,814.0 | 148,660,753.0 | 158,322,082.0 | 4,243,849.7 | 5 | 27,872 | 21,280 | 15,157 | 0.027 | compiled=5 | 1,970,731.0 | 153,618,579.0 | 116,920.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 165,654,991.0 | 162,759,537.0 | 172,080,533.0 | 3,594,737.9 | 5 | 28,016 | 24,424 | 17,358 | 0.022 | compiled=5 | 2,057,191.0 | 163,358,579.0 | 102,141.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 160,679,965.0 | 152,973,777.0 | 165,016,565.0 | 3,946,360.0 | 5 | 27,872 | 21,280 | 15,157 | 0.025 | compiled=5 | 1,980,960.0 | 157,011,127.0 | 207,381.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 171,434,328.0 | 162,282,713.0 | 173,132,007.0 | 4,322,925.1 | 5 | 28,016 | 24,424 | 17,358 | 0.025 | compiled=5 | 2,049,660.0 | 169,181,827.0 | 191,461.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 234,694,756.0 | 225,930,031.0 | 248,678,438.0 | 7,454,624.3 | 5 | 32,072 | 33,900 | 28,751 | 0.032 | compiled=5 | 2,057,830.0 | 232,454,644.0 | 99,081.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 236,600,806.0 | 231,232,568.0 | 243,931,183.0 | 4,361,817.8 | 5 | 32,160 | 34,742 | 29,284 | 0.018 | compiled=5 | 2,066,891.0 | 234,436,474.0 | 192,461.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 238,943,913.0 | 225,450,075.0 | 239,338,084.0 | 5,391,522.6 | 5 | 32,072 | 33,900 | 28,751 | 0.023 | compiled=5 | 1,972,670.0 | 236,861,162.0 | 110,971.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 230,187,749.0 | 221,930,149.0 | 238,856,841.0 | 5,977,603.8 | 5 | 32,160 | 34,742 | 29,284 | 0.026 | compiled=5 | 2,017,710.0 | 228,082,178.0 | 105,360.0 |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,431,049.0 | 145,376,887.0 | 159,441,649.0 | 4,669,648.0 | 5 | 27,872 | 19,793 | 14,796 | 0.030 | compiled=5 | 3,440,148.0 | 151,564,668.0 | 100,381.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 154,795,195.0 | 152,154,672.0 | 166,759,468.0 | 6,485,379.7 | 5 | 28,016 | 22,248 | 16,925 | 0.042 (max is trial 1) | compiled=5 | 3,560,858.0 | 150,630,894.0 | 182,561.0 |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 145,163,519.0 | 140,351,836.0 | 156,259,673.0 | 6,506,851.0 | 5 | 27,872 | 19,793 | 14,796 | 0.045 | compiled=5 | 1,786,849.0 | 143,156,229.0 | 184,601.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,965,436.0 | 154,791,336.0 | 166,863,816.0 | 4,559,446.7 | 5 | 28,016 | 22,248 | 16,925 | 0.028 | compiled=5 | 1,839,149.0 | 162,924,036.0 | 188,981.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 172,883,079.0 | 157,848,761.0 | 174,942,410.0 | 6,637,274.9 | 5 | 27,576 | 26,038 | 19,732 | 0.038 | compiled=5 | 1,961,840.0 | 170,605,326.0 | 106,040.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 161,919,302.0 | 155,114,737.0 | 162,471,785.0 | 2,781,837.1 | 5 | 28,008 | 24,852 | 17,725 | 0.017 | compiled=5 | 2,279,132.0 | 159,527,049.0 | 185,251.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 167,501,199.0 | 162,440,952.0 | 172,863,955.0 | 3,331,213.1 | 5 | 27,576 | 26,038 | 19,732 | 0.020 | compiled=5 | 1,851,749.0 | 163,240,458.0 | 204,351.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,695,714.0 | 151,627,070.0 | 172,409,163.0 | 7,484,916.9 | 5 | 28,008 | 24,852 | 17,725 | 0.045 | compiled=5 | 1,872,099.0 | 162,888,496.0 | 110,880.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 169,409,570.0 | 157,808,171.0 | 178,562,437.0 | 8,128,736.0 | 5 | 32,688 | 23,670 | 18,354 | 0.048 | compiled=5 | 1,801,309.0 | 167,514,891.0 | 101,520.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 167,070,099.0 | 159,330,758.0 | 171,956,293.0 | 4,142,022.9 | 5 | 32,480 | 22,748 | 17,432 | 0.025 | compiled=5 | 1,873,069.0 | 165,135,258.0 | 104,191.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,425,738.0 | 161,556,430.0 | 172,145,651.0 | 4,660,139.6 | 5 | 32,688 | 23,670 | 18,354 | 0.029 | compiled=5 | 1,702,508.0 | 161,405,548.0 | 98,191.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 166,144,912.0 | 155,264,138.0 | 169,562,188.0 | 5,124,001.9 | 5 | 32,480 | 22,748 | 17,432 | 0.031 (max is trial 1) | compiled=5 | 1,830,909.0 | 164,398,803.0 | 100,080.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 159,758,721.0 | 150,850,334.0 | 162,343,003.0 | 3,914,644.2 | 5 | 27,872 | 21,758 | 15,144 | 0.025 | compiled=5 | 1,984,460.0 | 157,433,309.0 | 105,230.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 168,489,615.0 | 161,467,220.0 | 171,477,790.0 | 4,236,281.4 | 5 | 28,016 | 26,179 | 17,353 | 0.025 | compiled=5 | 2,116,781.0 | 166,261,404.0 | 100,741.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 157,737,991.0 | 149,835,190.0 | 165,590,789.0 | 5,026,699.4 | 5 | 27,872 | 21,758 | 15,144 | 0.032 (max is trial 1) | compiled=5 | 1,978,500.0 | 155,560,230.0 | 194,591.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 160,481,984.0 | 155,049,887.0 | 170,951,916.0 | 6,403,622.6 | 5 | 28,016 | 26,179 | 17,353 | 0.040 | compiled=5 | 2,087,541.0 | 157,841,921.0 | 188,341.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 279,490,876.0 | 274,807,832.0 | 284,755,862.0 | 3,786,063.9 | 5 | 79,008 | 57,513 | 37,580 | 0.014 | compiled=5 | 2,712,934.0 | 273,630,296.0 | 224,362.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 280,802,162.0 | 275,426,176.0 | 286,377,271.0 | 4,090,430.0 | 5 | 78,968 | 57,440 | 37,507 | 0.015 | compiled=5 | 2,568,733.0 | 275,893,537.0 | 117,221.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 316,716,057.0 | 310,830,299.0 | 319,875,692.0 | 3,012,219.7 | 5 | 83,104 | 63,973 | 44,040 | 0.010 | compiled=5 | 2,578,943.0 | 313,750,442.0 | 114,371.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 320,406,636.0 | 318,663,577.0 | 320,850,567.0 | 759,898.8 | 5 | 83,064 | 63,900 | 43,967 | 0.002 | compiled=5 | 2,607,673.0 | 317,598,132.0 | 121,161.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 277,925,578.0 | 263,447,264.0 | 283,659,095.0 | 6,969,562.6 | 5 | 79,008 | 57,232 | 37,299 | 0.025 | compiled=5 | 2,565,423.0 | 275,245,814.0 | 114,660.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 276,063,147.0 | 270,435,559.0 | 284,764,053.0 | 4,921,808.8 | 5 | 78,968 | 57,159 | 37,226 | 0.018 | compiled=5 | 2,561,813.0 | 273,384,104.0 | 120,350.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 308,219,716.0 | 301,181,621.0 | 315,617,642.0 | 4,610,863.5 | 5 | 83,104 | 63,692 | 43,759 | 0.015 | compiled=5 | 2,695,324.0 | 305,384,371.0 | 127,081.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 315,278,860.0 | 312,496,036.0 | 321,884,032.0 | 3,829,279.2 | 5 | 83,064 | 63,619 | 43,686 | 0.012 | compiled=5 | 2,692,264.0 | 312,347,806.0 | 130,670.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 143,884,049.0 | 138,869,024.0 | 156,974,767.0 | 6,092,030.4 | 5 | 27,872 | 20,021 | 14,818 | 0.042 | compiled=5 | 1,885,230.0 | 141,788,518.0 | 182,111.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 162,623,496.0 | 156,004,722.0 | 171,026,989.0 | 5,008,260.4 | 5 | 28,016 | 22,440 | 16,835 | 0.031 | compiled=5 | 2,020,461.0 | 160,628,145.0 | 109,960.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 157,066,638.0 | 145,385,320.0 | 161,378,538.0 | 5,341,223.4 | 5 | 27,872 | 20,021 | 14,818 | 0.034 | compiled=5 | 1,958,510.0 | 155,040,528.0 | 120,001.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,223,162.0 | 157,537,479.0 | 167,520,138.0 | 3,272,478.6 | 5 | 28,016 | 22,440 | 16,835 | 0.020 (max is trial 1) | compiled=5 | 1,845,609.0 | 162,268,283.0 | 202,731.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 293,384,696.0 | 283,418,634.0 | 302,162,102.0 | 6,016,601.6 | 5 | 31,768 | 31,367 | 31,136 | 0.021 | compiled=5 | 1,821,799.0 | 289,621,387.0 | 101,000.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 282,502,600.0 | 279,852,908.0 | 291,502,857.0 | 4,083,981.5 | 5 | 31,768 | 31,483 | 31,252 | 0.014 | compiled=5 | 1,853,060.0 | 280,185,379.0 | 192,671.0 |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 290,670,099.0 | 281,580,023.0 | 298,587,228.0 | 5,562,346.4 | 5 | 31,768 | 31,931 | 31,700 | 0.019 (max is trial 1) | compiled=5 | 1,727,779.0 | 288,831,969.0 | 190,821.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 293,066,810.0 | 279,233,362.0 | 295,624,743.0 | 6,264,560.2 | 5 | 31,768 | 32,044 | 31,813 | 0.021 (max is trial 1) | compiled=5 | 1,727,519.0 | 291,242,721.0 | 185,971.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 220,148,621.0 | 214,674,882.0 | 222,605,123.0 | 2,836,422.1 | 5 | 31,832 | 28,898 | 27,216 | 0.013 | compiled=5 | 1,954,270.0 | 218,194,751.0 | 197,781.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 211,779,438.0 | 207,131,374.0 | 219,447,757.0 | 4,874,951.8 | 5 | 31,832 | 28,827 | 27,145 | 0.023 | compiled=5 | 1,778,709.0 | 207,929,559.0 | 191,281.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 219,330,086.0 | 209,419,996.0 | 223,647,827.0 | 4,675,051.8 | 5 | 31,832 | 28,898 | 27,216 | 0.021 (max is trial 1) | compiled=5 | 1,794,949.0 | 217,444,546.0 | 108,790.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 217,538,527.0 | 213,800,788.0 | 217,962,539.0 | 1,526,978.8 | 5 | 31,832 | 28,827 | 27,145 | 0.007 | compiled=5 | 1,811,129.0 | 215,610,367.0 | 100,161.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,749,391.0 | 215,564,137.0 | 241,220,249.0 | 8,998,023.8 | 5 | 31,912 | 30,126 | 28,184 | 0.039 | compiled=5 | 1,821,499.0 | 229,862,811.0 | 184,411.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 224,488,423.0 | 215,330,266.0 | 241,301,820.0 | 9,396,237.7 | 5 | 31,872 | 30,054 | 28,112 | 0.042 | compiled=5 | 1,835,509.0 | 222,673,244.0 | 193,081.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 226,919,901.0 | 224,407,860.0 | 232,024,377.0 | 3,277,067.8 | 5 | 31,912 | 30,126 | 28,184 | 0.014 | compiled=5 | 1,838,379.0 | 223,108,323.0 | 108,810.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 226,519,720.0 | 223,279,164.0 | 232,500,410.0 | 3,567,645.3 | 5 | 31,872 | 30,054 | 28,112 | 0.016 | compiled=5 | 1,838,369.0 | 222,551,211.0 | 117,820.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 294,207,502.0 | 276,143,607.0 | 299,532,919.0 | 8,243,757.3 | 5 | 31,520 | 23,681 | 23,681 | 0.028 | compiled=5 | 1,707,169.0 | 292,458,533.0 | 203,061.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 196,911,502.0 | 184,189,025.0 | 207,033,333.0 | 7,468,786.5 | 5 | 27,504 | 23,489 | 23,489 | 0.038 | compiled=5 | 1,673,928.0 | 195,127,342.0 | 182,751.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 291,957,265.0 | 284,341,107.0 | 293,554,982.0 | 4,028,583.5 | 5 | 31,520 | 23,681 | 23,681 | 0.014 | compiled=5 | 1,714,278.0 | 290,010,875.0 | 182,681.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 197,901,949.0 | 183,987,300.0 | 200,714,983.0 | 5,987,957.1 | 5 | 27,504 | 23,489 | 23,489 | 0.030 | compiled=5 | 2,039,740.0 | 195,387,247.0 | 187,661.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 251,944,965.0 | 238,940,667.0 | 254,848,089.0 | 5,893,565.3 | 5 | 32,072 | 33,230 | 30,589 | 0.023 | compiled=5 | 1,901,820.0 | 249,873,963.0 | 112,861.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 251,383,492.0 | 238,575,035.0 | 252,821,059.0 | 5,302,792.1 | 5 | 32,064 | 33,158 | 30,517 | 0.021 | compiled=5 | 1,887,020.0 | 249,302,201.0 | 185,031.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 241,899,937.0 | 231,383,885.0 | 253,408,683.0 | 7,020,722.6 | 5 | 32,072 | 33,230 | 30,589 | 0.029 | compiled=5 | 2,071,800.0 | 239,645,556.0 | 198,331.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 251,701,656.0 | 244,313,288.0 | 252,589,430.0 | 3,253,301.7 | 5 | 32,064 | 33,158 | 30,517 | 0.013 | compiled=5 | 1,792,419.0 | 249,701,906.0 | 207,331.0 |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 218,082,530.0 | 211,485,637.0 | 225,167,687.0 | 4,747,996.9 | 5 | 31,848 | 26,467 | 25,774 | 0.022 | compiled=5 | 1,869,780.0 | 216,020,280.0 | 189,231.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 220,174,141.0 | 212,347,511.0 | 233,098,777.0 | 7,516,474.5 | 5 | 31,848 | 26,580 | 25,887 | 0.034 | compiled=5 | 3,581,778.0 | 216,642,963.0 | 204,221.0 |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 218,834,622.0 | 213,042,475.0 | 221,808,328.0 | 3,349,048.5 | 5 | 31,848 | 26,467 | 25,774 | 0.015 | compiled=5 | 1,721,688.0 | 217,008,374.0 | 201,441.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 218,367,989.0 | 211,506,887.0 | 218,927,823.0 | 2,769,270.6 | 5 | 31,848 | 26,580 | 25,887 | 0.013 | compiled=5 | 1,647,078.0 | 216,614,931.0 | 108,811.0 |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 148,024,571.0 | 143,452,187.0 | 162,543,945.0 | 6,442,264.5 | 5 | 27,872 | 21,136 | 15,156 | 0.044 | compiled=5 | 2,080,061.0 | 146,108,251.0 | 182,001.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 157,533,089.0 | 157,106,397.0 | 161,253,659.0 | 1,753,129.3 | 5 | 28,016 | 23,964 | 17,357 | 0.011 (max is trial 1) | compiled=5 | 2,060,380.0 | 155,317,618.0 | 209,031.0 |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 152,473,625.0 | 149,179,729.0 | 160,878,136.0 | 5,218,092.1 | 5 | 27,872 | 21,136 | 15,156 | 0.034 | compiled=5 | 1,988,700.0 | 148,122,853.0 | 106,581.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 170,131,501.0 | 161,035,827.0 | 171,536,668.0 | 3,996,481.6 | 5 | 28,016 | 23,964 | 17,357 | 0.023 | compiled=5 | 2,053,020.0 | 167,540,599.0 | 101,261.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 287,814,220.0 | 277,457,745.0 | 293,314,697.0 | 5,423,229.4 | 5 | 31,896 | 33,533 | 33,017 | 0.019 | compiled=5 | 1,857,839.0 | 285,772,408.0 | 110,491.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 289,013,384.0 | 280,170,340.0 | 293,185,137.0 | 4,529,977.7 | 5 | 31,896 | 33,646 | 33,130 | 0.016 | compiled=5 | 1,872,360.0 | 287,029,174.0 | 114,801.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 288,782,409.0 | 276,878,330.0 | 289,955,816.0 | 5,056,294.9 | 5 | 31,896 | 33,953 | 33,437 | 0.018 | compiled=5 | 1,782,249.0 | 286,890,890.0 | 100,570.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 290,217,397.0 | 283,972,425.0 | 294,836,419.0 | 3,495,190.2 | 5 | 31,896 | 34,066 | 33,550 | 0.012 (max is trial 1) | compiled=5 | 1,798,399.0 | 288,310,917.0 | 111,141.0 |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 231,173,897.0 | 224,393,583.0 | 237,742,112.0 | 4,552,384.4 | 5 | 31,856 | 27,621 | 26,412 | 0.020 | compiled=5 | 1,803,110.0 | 227,315,467.0 | 99,050.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 235,439,499.0 | 226,504,294.0 | 244,425,265.0 | 7,275,987.9 | 5 | 31,856 | 27,734 | 26,525 | 0.031 | compiled=5 | 1,802,999.0 | 233,505,239.0 | 186,271.0 |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 235,355,715.0 | 229,188,984.0 | 238,133,927.0 | 2,990,810.2 | 5 | 31,856 | 27,761 | 26,552 | 0.013 | compiled=5 | 1,708,408.0 | 233,571,355.0 | 102,970.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 235,661,836.0 | 228,771,342.0 | 236,789,672.0 | 3,649,102.6 | 5 | 31,856 | 27,874 | 26,665 | 0.015 | compiled=5 | 1,729,129.0 | 233,842,987.0 | 110,540.0 |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 199,916,536.0 | 197,526,385.0 | 206,432,940.0 | 3,268,596.5 | 5 | 27,600 | 24,001 | 23,770 | 0.016 | compiled=5 | 1,646,999.0 | 198,352,229.0 | 113,030.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 200,877,052.0 | 194,603,210.0 | 210,140,979.0 | 5,884,352.9 | 5 | 31,696 | 24,115 | 23,884 | 0.029 (max is trial 1) | compiled=5 | 1,658,528.0 | 197,638,645.0 | 101,551.0 |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 197,276,896.0 | 190,241,871.0 | 204,553,711.0 | 4,623,739.4 | 5 | 27,600 | 24,001 | 23,770 | 0.023 | compiled=5 | 1,618,998.0 | 195,560,508.0 | 97,390.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 198,415,352.0 | 198,213,510.0 | 205,841,929.0 | 2,951,136.0 | 5 | 31,696 | 24,115 | 23,884 | 0.015 | compiled=5 | 1,645,278.0 | 196,517,173.0 | 189,430.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 186,247,167.0 | 185,447,023.0 | 195,452,714.0 | 3,687,770.3 | 5 | 31,896 | 28,425 | 23,623 | 0.020 | compiled=5 | 4,021,601.0 | 182,117,996.0 | 211,741.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 196,829,320.0 | 195,091,942.0 | 199,956,147.0 | 1,993,112.0 | 5 | 31,984 | 30,113 | 25,097 | 0.010 (max is trial 1) | compiled=5 | 1,886,179.0 | 194,844,600.0 | 173,921.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 190,573,403.0 | 184,201,651.0 | 192,274,781.0 | 3,094,582.7 | 5 | 31,896 | 28,425 | 23,623 | 0.016 | compiled=5 | 1,827,379.0 | 188,551,523.0 | 191,141.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 196,328,992.0 | 189,960,010.0 | 199,366,998.0 | 3,719,583.5 | 5 | 31,984 | 30,113 | 25,097 | 0.019 | compiled=5 | 1,831,999.0 | 194,400,122.0 | 104,561.0 |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 176,511,137.0 | 171,599,382.0 | 178,818,808.0 | 2,860,718.7 | 5 | 37,152 | 23,987 | 18,583 | 0.016 | compiled=5 | 1,730,449.0 | 174,587,487.0 | 177,251.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 179,789,464.0 | 175,690,942.0 | 181,131,201.0 | 1,850,692.3 | 5 | 37,112 | 23,809 | 18,405 | 0.010 | compiled=5 | 1,749,909.0 | 177,949,244.0 | 187,661.0 |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 179,234,396.0 | 170,033,531.0 | 184,945,715.0 | 4,791,821.2 | 5 | 37,152 | 23,987 | 18,583 | 0.027 | compiled=5 | 1,730,948.0 | 177,402,828.0 | 99,920.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 173,714,270.0 | 165,039,046.0 | 179,819,360.0 | 5,349,229.8 | 5 | 37,112 | 23,809 | 18,405 | 0.031 | compiled=5 | 1,778,219.0 | 171,745,140.0 | 111,361.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 154,363,733.0 | 145,801,220.0 | 157,218,567.0 | 4,968,600.9 | 5 | 27,872 | 19,793 | 14,796 | 0.032 | compiled=5 | 1,828,169.0 | 152,289,722.0 | 99,831.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 164,866,537.0 | 163,270,159.0 | 170,239,425.0 | 2,382,418.1 | 5 | 28,016 | 22,248 | 16,925 | 0.014 | compiled=5 | 1,862,410.0 | 162,820,836.0 | 113,191.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 157,817,921.0 | 151,070,438.0 | 165,217,167.0 | 4,834,037.1 | 5 | 27,872 | 19,793 | 14,796 | 0.031 | compiled=5 | 1,809,499.0 | 155,782,231.0 | 200,111.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 166,129,003.0 | 156,152,513.0 | 172,096,111.0 | 5,220,230.3 | 5 | 28,016 | 22,248 | 16,925 | 0.031 (max is trial 1) | compiled=5 | 1,893,829.0 | 164,057,782.0 | 183,011.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 159,068,297.0 | 152,625,844.0 | 164,323,244.0 | 4,056,236.0 | 5 | 28,200 | 28,744 | 16,479 | 0.025 | compiled=5 | 2,366,472.0 | 156,512,054.0 | 184,531.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 170,744,457.0 | 164,518,285.0 | 174,148,044.0 | 3,722,643.9 | 5 | 28,336 | 31,719 | 18,566 | 0.022 | compiled=5 | 2,443,662.0 | 166,880,927.0 | 101,091.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,015,746.0 | 161,855,950.0 | 170,288,133.0 | 3,033,618.5 | 5 | 28,200 | 28,744 | 16,479 | 0.019 | compiled=5 | 2,344,831.0 | 160,472,364.0 | 198,551.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 160,799,555.0 | 154,380,833.0 | 182,924,355.0 | 10,724,715.7 | 5 | 28,336 | 31,719 | 18,566 | 0.067 | compiled=5 | 5,317,976.0 | 156,728,855.0 | 106,410.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 151,117,896.0 | 148,618,213.0 | 153,884,341.0 | 1,987,422.3 | 5 | 27,864 | 23,557 | 15,235 | 0.013 | compiled=5 | 2,233,321.0 | 146,571,263.0 | 191,831.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 164,518,875.0 | 156,033,252.0 | 168,295,935.0 | 4,295,712.2 | 5 | 28,008 | 26,908 | 17,149 | 0.026 | compiled=5 | 2,236,241.0 | 162,114,713.0 | 100,960.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 154,637,215.0 | 141,698,491.0 | 161,407,570.0 | 7,964,081.5 | 5 | 27,864 | 23,557 | 15,235 | 0.052 | compiled=5 | 2,027,170.0 | 152,415,544.0 | 199,401.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,369,598.0 | 155,562,240.0 | 167,654,500.0 | 4,170,438.3 | 5 | 28,008 | 26,908 | 17,149 | 0.026 | compiled=5 | 2,172,251.0 | 158,557,784.0 | 187,711.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,230,768.0 | 147,531,538.0 | 165,733,981.0 | 5,841,418.5 | 5 | 27,872 | 19,795 | 14,798 | 0.038 | compiled=5 | 3,657,359.0 | 151,918,181.0 | 209,701.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 159,942,591.0 | 152,904,716.0 | 167,345,199.0 | 5,166,644.3 | 5 | 28,016 | 22,250 | 16,927 | 0.032 | compiled=5 | 3,704,679.0 | 155,801,450.0 | 201,011.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 152,021,922.0 | 144,819,367.0 | 155,161,488.0 | 3,561,627.1 | 5 | 27,872 | 19,795 | 14,798 | 0.023 | compiled=5 | 1,804,079.0 | 150,017,523.0 | 191,061.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,332,038.0 | 155,813,720.0 | 168,281,932.0 | 4,605,932.8 | 5 | 28,016 | 22,250 | 16,927 | 0.028 | compiled=5 | 1,841,099.0 | 161,388,898.0 | 189,331.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 155,407,658.0 | 149,428,719.0 | 162,837,906.0 | 4,852,158.1 | 5 | 27,872 | 21,173 | 15,078 | 0.031 | compiled=5 | 1,977,310.0 | 153,230,807.0 | 191,631.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 166,301,335.0 | 159,505,180.0 | 172,924,178.0 | 4,494,031.1 | 5 | 28,016 | 23,927 | 17,209 | 0.027 | compiled=5 | 2,017,320.0 | 164,108,503.0 | 102,291.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 156,895,947.0 | 147,585,000.0 | 158,757,976.0 | 3,976,039.7 | 5 | 27,872 | 21,173 | 15,078 | 0.025 | compiled=5 | 1,954,400.0 | 154,930,356.0 | 114,280.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,911,152.0 | 157,791,240.0 | 168,187,781.0 | 4,124,843.7 | 5 | 28,016 | 23,927 | 17,209 | 0.025 | compiled=5 | 2,005,280.0 | 159,455,469.0 | 97,370.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 595,943,472.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 16,375,331,006.0 | 16,230,657,811.0 | 16,393,242,767.0 | 69,342,558.5 | 5 | 150,848 | 484,520 (warned) | 482,896 | 0.004 | compiled=5 | 9,387,598,482.0 | 6,928,746,541.0 | 197,551.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 575,112,255.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,411,758,846.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 362,481,932.0 | 357,061,654.0 | 371,961,200.0 | 5,653,788.6 | 5 | 45,912 | 55,856 | 45,933 | 0.016 | compiled=5 | 5,121,176.0 | 357,098,834.0 | 184,340.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 347,550,215.0 | 346,063,848.0 | 358,042,459.0 | 4,453,661.4 | 5 | 45,544 | 54,295 | 44,372 | 0.013 (max is trial 1) | compiled=5 | 2,500,073.0 | 344,912,621.0 | 191,641.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 358,393,452.0 | 356,073,012.0 | 377,447,608.0 | 7,853,389.1 | 5 | 45,912 | 55,856 | 45,933 | 0.022 (max is trial 1) | compiled=5 | 2,402,522.0 | 355,916,771.0 | 114,270.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 350,853,687.0 | 343,969,212.0 | 356,802,584.0 | 4,744,032.9 | 5 | 45,544 | 54,295 | 44,372 | 0.014 | compiled=5 | 2,405,102.0 | 348,341,644.0 | 197,311.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 242,740,437.0 | 235,927,382.0 | 244,022,233.0 | 2,912,485.5 | 5 | 32,056 | 34,318 | 28,808 | 0.012 | compiled=5 | 2,083,620.0 | 240,557,866.0 | 99,220.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 244,148,223.0 | 237,159,918.0 | 245,246,490.0 | 3,333,242.8 | 5 | 32,152 | 35,390 | 29,455 | 0.014 | compiled=5 | 2,211,451.0 | 240,613,316.0 | 188,871.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 239,857,366.0 | 234,941,933.0 | 245,139,452.0 | 3,812,886.8 | 5 | 32,056 | 34,318 | 28,808 | 0.016 | compiled=5 | 4,189,450.0 | 235,310,994.0 | 99,111.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 243,203,974.0 | 238,682,511.0 | 246,420,760.0 | 2,568,658.0 | 5 | 32,152 | 35,390 | 29,455 | 0.011 | compiled=5 | 2,458,422.0 | 241,038,573.0 | 102,011.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 238,711,537.0 | 234,844,567.0 | 239,734,733.0 | 1,718,113.1 | 5 | 32,056 | 34,039 | 28,529 | 0.007 | compiled=5 | 2,065,671.0 | 236,546,295.0 | 102,420.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 237,418,919.0 | 232,669,515.0 | 240,191,524.0 | 2,749,389.7 | 5 | 32,152 | 35,108 | 29,173 | 0.012 | compiled=5 | 2,133,641.0 | 234,848,766.0 | 116,670.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 238,546,290.0 | 233,050,963.0 | 239,124,793.0 | 2,285,834.7 | 5 | 32,056 | 34,039 | 28,529 | 0.010 | compiled=5 | 1,973,849.0 | 236,467,760.0 | 99,090.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 239,241,323.0 | 232,321,530.0 | 245,475,124.0 | 4,942,601.3 | 5 | 32,152 | 35,108 | 29,173 | 0.021 (max is trial 1) | compiled=5 | 2,047,160.0 | 237,107,203.0 | 119,170.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 401,825,673.0 | 395,009,259.0 | 403,453,502.0 | 3,034,023.9 | 5 | 40,760 | 61,625 | 41,896 | 0.008 | compiled=5 | 5,177,047.0 | 395,354,511.0 | 102,030.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 415,734,846.0 | 406,493,008.0 | 428,410,190.0 | 6,980,972.6 | 5 | 40,856 | 66,268 | 43,396 | 0.017 | compiled=5 | 8,306,383.0 | 407,225,412.0 | 203,051.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 401,660,577.0 | 395,112,966.0 | 412,673,971.0 | 6,327,039.2 | 5 | 40,760 | 62,043 | 42,314 | 0.016 (max is trial 1) | compiled=5 | 5,129,396.0 | 396,467,881.0 | 188,941.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 415,571,266.0 | 400,947,414.0 | 420,298,640.0 | 6,882,520.4 | 5 | 40,856 | 66,686 | 43,814 | 0.017 (max is trial 1) | compiled=5 | 8,215,741.0 | 400,017,669.0 | 105,851.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 357,073,324.0 | 355,095,803.0 | 364,069,291.0 | 3,249,855.1 | 5 | 40,760 | 59,595 | 39,866 | 0.009 | compiled=5 | 4,999,786.0 | 350,989,953.0 | 191,431.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 375,398,787.0 | 366,775,044.0 | 386,310,024.0 | 6,236,056.5 | 5 | 40,856 | 64,238 | 41,366 | 0.017 | compiled=5 | 7,985,391.0 | 367,130,876.0 | 100,860.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 356,953,845.0 | 355,458,769.0 | 364,951,296.0 | 4,137,012.6 | 5 | 40,760 | 59,595 | 39,866 | 0.012 | compiled=5 | 4,907,034.0 | 352,128,152.0 | 189,391.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 380,690,885.0 | 366,380,012.0 | 387,571,906.0 | 8,004,016.9 | 5 | 40,856 | 64,238 | 41,366 | 0.021 | compiled=5 | 7,909,009.0 | 367,346,178.0 | 194,441.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 5,420,013,491.0 | 5,391,660,725.0 | 5,437,393,241.0 | 15,484,911.7 | 5 | 176,288 | 515,893 (warned) | 297,928 | 0.003 | compiled=5 | 599,944,532.0 | 4,818,556,331.0 | 101,170.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 6,446,688,805.0 | 6,408,714,449.0 | 6,469,325,382.0 | 20,715,321.9 | 5 | 180,480 | 525,510 (warned) | 299,348 | 0.003 | compiled=5 | 1,599,208,515.0 | 4,837,986,441.0 | 109,301.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 5,436,501,058.0 | 5,420,325,227.0 | 5,471,816,153.0 | 17,388,970.5 | 5 | 176,288 | 518,417 (warned) | 300,452 | 0.003 | compiled=5 | 603,041,574.0 | 4,826,920,682.0 | 97,650.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 6,457,391,389.0 | 6,441,657,521.0 | 6,488,083,221.0 | 16,635,871.4 | 5 | 180,480 | 528,034 (warned) | 301,872 | 0.003 | compiled=5 | 1,621,552,793.0 | 4,842,042,096.0 | 186,291.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 239,940,483.0 | 239,023,978.0 | 246,175,364.0 | 3,232,833.0 | 5 | 32,272 | 37,739 | 29,255 | 0.013 | compiled=5 | 2,309,832.0 | 236,862,777.0 | 110,930.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 252,792,130.0 | 248,291,006.0 | 261,351,463.0 | 4,850,776.6 | 5 | 32,408 | 41,083 | 30,780 | 0.019 | compiled=5 | 2,412,562.0 | 247,602,332.0 | 188,771.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 244,510,270.0 | 229,787,617.0 | 256,735,171.0 | 9,546,877.7 | 5 | 32,272 | 37,739 | 29,255 | 0.039 | compiled=5 | 2,117,161.0 | 242,285,278.0 | 194,111.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 255,269,433.0 | 248,526,689.0 | 256,265,038.0 | 3,322,446.3 | 5 | 32,408 | 41,083 | 30,780 | 0.013 | compiled=5 | 2,248,361.0 | 252,823,961.0 | 180,581.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 239,734,652.0 | 234,158,944.0 | 245,472,660.0 | 3,658,994.8 | 5 | 36,336 | 46,133 | 29,228 | 0.015 | compiled=5 | 3,270,177.0 | 236,385,464.0 | 101,591.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 253,125,681.0 | 252,366,376.0 | 274,240,618.0 | 8,542,576.9 | 5 | 36,432 | 48,666 | 30,765 | 0.034 (max is trial 1) | compiled=5 | 3,375,067.0 | 249,639,993.0 | 105,540.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 254,403,549.0 | 242,056,958.0 | 261,885,786.0 | 7,190,958.7 | 5 | 36,336 | 48,061 | 31,156 | 0.028 | compiled=5 | 3,410,867.0 | 250,796,691.0 | 112,850.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 252,651,420.0 | 248,702,471.0 | 260,397,837.0 | 4,220,743.8 | 5 | 36,432 | 50,594 | 32,693 | 0.017 | compiled=5 | 3,380,757.0 | 249,080,882.0 | 111,271.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 335,194,481.0 | 328,646,997.0 | 356,730,363.0 | 9,741,615.1 | 5 | 40,304 | 56,824 | 26,714 | 0.029 | compiled=5 | 4,568,573.0 | 328,398,437.0 | 109,421.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 338,570,130.0 | 330,163,407.0 | 338,955,222.0 | 3,363,987.7 | 5 | 40,400 | 60,192 | 28,249 | 0.010 | compiled=5 | 4,694,904.0 | 332,780,380.0 | 103,131.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 393,797,429.0 | 386,731,354.0 | 408,476,970.0 | 7,103,974.2 | 5 | 44,400 | 58,384 | 28,274 | 0.018 (max is trial 1) | compiled=5 | 4,592,953.0 | 389,094,666.0 | 108,810.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 393,894,749.0 | 391,182,265.0 | 399,722,917.0 | 3,633,570.0 | 5 | 40,400 | 61,754 | 29,811 | 0.009 (max is trial 1) | compiled=5 | 4,694,303.0 | 387,865,539.0 | 104,330.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 286,348,472.0 | 277,975,137.0 | 289,278,856.0 | 3,913,895.4 | 5 | 52,624 | 105,222 | 33,872 | 0.014 | compiled=5 | 7,710,360.0 | 278,538,621.0 | 209,591.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 298,688,404.0 | 296,942,875.0 | 309,770,761.0 | 4,697,209.4 | 5 | 52,720 | 112,577 | 35,416 | 0.016 (max is trial 1) | compiled=5 | 8,173,852.0 | 290,395,362.0 | 106,070.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 290,120,516.0 | 281,346,842.0 | 296,052,244.0 | 5,334,468.1 | 5 | 52,624 | 105,520 | 34,170 | 0.018 | compiled=5 | 7,670,038.0 | 278,857,939.0 | 113,601.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 290,083,986.0 | 277,155,731.0 | 297,357,072.0 | 6,783,608.3 | 5 | 52,720 | 112,875 | 35,714 | 0.023 | compiled=5 | 8,122,940.0 | 281,125,901.0 | 211,951.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 547,658,032.0 | 540,057,935.0 | 561,826,596.0 | 7,683,977.2 | 5 | 208,736 | 550,723 (warned) | 41,457 | 0.014 (max is trial 1) | compiled=5 | 58,084,948.0 | 489,794,096.0 | 105,400.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 555,655,536.0 | 546,585,629.0 | 558,228,987.0 | 4,100,827.9 | 5 | 212,928 | 565,513 (warned) | 42,745 | 0.007 | compiled=5 | 64,702,152.0 | 490,736,911.0 | 200,861.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 573,653,918.0 | 572,123,251.0 | 591,140,774.0 | 8,515,153.3 | 5 | 208,736 | 554,081 (warned) | 44,814 | 0.015 | compiled=5 | 59,075,812.0 | 515,624,271.0 | 95,771.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 590,330,781.0 | 581,451,197.0 | 599,161,804.0 | 5,950,165.0 | 5 | 212,928 | 568,871 (warned) | 46,102 | 0.010 | compiled=5 | 65,040,842.0 | 520,792,407.0 | 96,571.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 162,181,873.0 | 159,654,130.0 | 164,009,633.0 | 1,489,286.7 | 5 | 27,872 | 21,710 | 16,003 | 0.009 | compiled=5 | 2,004,811.0 | 159,856,831.0 | 101,391.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 162,086,922.0 | 152,876,555.0 | 179,705,134.0 | 8,896,577.3 | 5 | 28,016 | 23,954 | 17,347 | 0.055 | compiled=5 | 1,980,800.0 | 160,031,352.0 | 99,130.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,325,932.0 | 150,708,838.0 | 168,307,582.0 | 5,991,459.4 | 5 | 27,872 | 21,710 | 16,003 | 0.036 | compiled=5 | 2,001,400.0 | 162,306,013.0 | 109,720.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 166,181,192.0 | 161,254,629.0 | 175,453,529.0 | 4,958,339.3 | 5 | 28,016 | 23,954 | 17,347 | 0.030 | compiled=5 | 2,018,000.0 | 164,028,051.0 | 96,691.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 174,973,479.0 | 157,171,707.0 | 176,338,876.0 | 7,182,668.7 | 5 | 28,016 | 23,560 | 17,779 | 0.041 | compiled=5 | 1,905,370.0 | 172,877,348.0 | 101,130.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 169,113,320.0 | 160,493,675.0 | 175,063,140.0 | 6,110,712.5 | 5 | 28,016 | 23,132 | 17,351 | 0.036 | compiled=5 | 1,944,190.0 | 167,095,719.0 | 183,951.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 163,465,980.0 | 156,628,106.0 | 175,603,578.0 | 6,757,313.6 | 5 | 28,016 | 23,560 | 17,779 | 0.041 | compiled=5 | 1,910,669.0 | 161,477,870.0 | 101,831.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 158,602,335.0 | 147,720,081.0 | 169,465,848.0 | 8,747,404.6 | 5 | 28,016 | 23,132 | 17,351 | 0.055 | compiled=5 | 2,302,462.0 | 156,705,056.0 | 184,041.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 215,006,304.0 | 212,510,150.0 | 223,885,749.0 | 3,943,757.0 | 5 | 32,048 | 32,388 | 27,554 | 0.018 | compiled=5 | 1,954,470.0 | 212,864,893.0 | 182,161.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 227,456,268.0 | 220,304,752.0 | 231,016,076.0 | 4,087,448.2 | 5 | 32,144 | 33,867 | 28,803 | 0.018 | compiled=5 | 1,993,710.0 | 225,227,287.0 | 202,961.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 223,443,863.0 | 213,238,805.0 | 223,676,838.0 | 4,172,923.9 | 5 | 32,048 | 32,388 | 27,554 | 0.019 | compiled=5 | 1,993,479.0 | 221,260,554.0 | 182,081.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 228,863,683.0 | 221,092,393.0 | 236,319,629.0 | 5,604,367.8 | 5 | 32,144 | 33,867 | 28,803 | 0.024 | compiled=5 | 2,016,790.0 | 226,749,612.0 | 106,630.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 138,602,782.0 | 131,938,597.0 | 157,761,211.0 | 8,658,628.0 | 5 | 27,696 | 15,957 | 13,600 | 0.062 | compiled=5 | 1,642,288.0 | 136,487,471.0 | 202,531.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 148,655,504.0 | 144,435,603.0 | 154,247,252.0 | 3,239,025.5 | 5 | 27,696 | 15,780 | 13,423 | 0.022 | compiled=5 | 1,631,009.0 | 145,158,596.0 | 189,441.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 145,822,922.0 | 138,232,153.0 | 152,155,133.0 | 5,742,079.6 | 5 | 27,696 | 15,957 | 13,600 | 0.039 | compiled=5 | 1,626,638.0 | 144,095,393.0 | 104,321.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 142,495,255.0 | 133,146,910.0 | 149,649,359.0 | 5,891,150.8 | 5 | 27,696 | 15,780 | 13,423 | 0.041 | compiled=5 | 1,655,788.0 | 140,890,587.0 | 107,910.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 320,293,805.0 | 312,146,744.0 | 324,030,354.0 | 4,567,301.2 | 5 | 41,040 | 46,197 | 41,169 | 0.014 | compiled=5 | 2,127,451.0 | 318,065,104.0 | 101,250.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 315,244,439.0 | 311,069,298.0 | 316,125,823.0 | 1,909,718.2 | 5 | 40,832 | 45,380 | 40,352 | 0.006 | compiled=5 | 2,197,291.0 | 312,848,687.0 | 103,280.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 321,155,280.0 | 307,479,311.0 | 323,270,300.0 | 6,179,514.8 | 5 | 41,040 | 46,197 | 41,169 | 0.019 | compiled=5 | 2,275,862.0 | 318,778,297.0 | 203,811.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 309,450,121.0 | 306,734,248.0 | 316,582,756.0 | 4,459,949.1 | 5 | 40,832 | 45,380 | 40,352 | 0.014 | compiled=5 | 2,251,781.0 | 304,843,309.0 | 102,751.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 209,555,876.0 | 203,059,833.0 | 210,885,743.0 | 3,060,915.9 | 5 | 32,152 | 28,501 | 25,957 | 0.015 | compiled=5 | 1,795,759.0 | 207,565,146.0 | 110,550.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 208,014,579.0 | 198,774,721.0 | 212,262,200.0 | 4,666,624.3 | 5 | 32,064 | 28,241 | 25,697 | 0.022 (max is trial 1) | compiled=5 | 1,840,450.0 | 206,022,358.0 | 184,931.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 210,361,991.0 | 202,841,643.0 | 210,462,311.0 | 3,145,543.9 | 5 | 32,152 | 28,501 | 25,957 | 0.015 | compiled=5 | 1,816,779.0 | 208,339,741.0 | 189,281.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 208,379,701.0 | 201,325,757.0 | 214,619,311.0 | 4,965,370.4 | 5 | 32,064 | 28,241 | 25,697 | 0.024 | compiled=5 | 1,815,139.0 | 206,361,641.0 | 98,841.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 248,993,529.0 | 242,327,346.0 | 256,430,097.0 | 4,474,403.5 | 5 | 36,640 | 47,955 | 22,637 | 0.018 (max is trial 1) | compiled=5 | 3,277,317.0 | 245,486,951.0 | 101,041.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 254,802,158.0 | 251,841,944.0 | 261,493,263.0 | 3,199,315.7 | 5 | 36,784 | 50,932 | 24,341 | 0.013 (max is trial 1) | compiled=5 | 3,366,397.0 | 251,237,510.0 | 189,931.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 249,220,723.0 | 240,991,853.0 | 259,886,796.0 | 6,951,006.0 | 5 | 36,640 | 47,955 | 22,637 | 0.028 | compiled=5 | 7,110,225.0 | 241,119,653.0 | 182,541.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 249,953,987.0 | 248,354,169.0 | 256,727,641.0 | 3,597,921.2 | 5 | 36,784 | 50,932 | 24,341 | 0.014 | compiled=5 | 3,365,237.0 | 246,464,999.0 | 99,720.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 235,613,650.0 | 223,002,003.0 | 245,913,133.0 | 7,332,690.6 | 5 | 85,816 | 227,952 | 19,986 | 0.031 (max is trial 1) | compiled=5 | 16,828,246.0 | 214,801,783.0 | 190,851.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 237,227,239.0 | 234,081,972.0 | 243,635,982.0 | 3,980,991.4 | 5 | 94,152 | 237,783 | 21,962 | 0.017 | compiled=5 | 15,839,151.0 | 221,197,676.0 | 198,991.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 227,400,195.0 | 214,024,009.0 | 244,394,719.0 | 10,150,085.1 | 5 | 85,816 | 227,952 | 19,986 | 0.045 (max is trial 1) | compiled=5 | 14,493,572.0 | 209,564,947.0 | 99,311.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 243,816,386.0 | 237,523,795.0 | 259,431,715.0 | 7,642,642.1 | 5 | 94,152 | 237,783 | 21,962 | 0.031 (max is trial 1) | compiled=5 | 15,853,669.0 | 224,574,442.0 | 106,270.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 190,169,077.0 | 183,578,623.0 | 203,099,753.0 | 6,652,419.4 | 5 | 36,560 | 58,368 | 17,968 | 0.035 | compiled=5 | 4,627,004.0 | 185,441,122.0 | 106,881.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 208,098,309.0 | 201,093,964.0 | 217,225,234.0 | 5,631,780.7 | 5 | 36,704 | 62,147 | 19,759 | 0.027 | compiled=5 | 5,165,396.0 | 202,815,551.0 | 101,091.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 195,559,439.0 | 190,304,522.0 | 203,572,128.0 | 5,305,190.6 | 5 | 36,560 | 58,368 | 17,968 | 0.027 | compiled=5 | 4,549,143.0 | 185,737,339.0 | 101,011.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 207,407,197.0 | 203,717,757.0 | 210,823,781.0 | 2,640,077.6 | 5 | 36,704 | 62,147 | 19,759 | 0.013 | compiled=5 | 6,305,291.0 | 198,242,240.0 | 104,911.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 168,932,178.0 | 158,262,052.0 | 173,867,753.0 | 5,381,132.5 | 5 | 32,232 | 36,918 | 15,751 | 0.032 | compiled=5 | 3,191,106.0 | 165,520,540.0 | 191,761.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 179,166,290.0 | 175,031,660.0 | 188,583,288.0 | 5,100,899.0 | 5 | 32,376 | 39,942 | 17,763 | 0.028 | compiled=5 | 4,062,721.0 | 171,640,062.0 | 102,271.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 171,066,747.0 | 161,678,490.0 | 181,691,440.0 | 7,354,590.0 | 5 | 32,232 | 36,918 | 15,751 | 0.043 | compiled=5 | 3,313,446.0 | 167,069,827.0 | 190,991.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 176,767,815.0 | 174,775,864.0 | 182,928,245.0 | 3,444,351.6 | 5 | 32,376 | 39,942 | 17,763 | 0.019 | compiled=5 | 3,384,547.0 | 173,401,498.0 | 112,641.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 1,459,685,137.0 | 1,427,586,022.0 | 1,486,465,605.0 | 18,947,053.4 | 5 | 680,528 | 395,013 (warned) | 100,533 | 0.013 | compiled=5 | 13,599,440.0 | 1,446,729,371.0 | 273,121.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 1,396,235,983.0 | 1,363,990,387.0 | 1,398,306,642.0 | 14,982,863.4 | 5 | 659,992 | 402,219 (warned) | 102,683 | 0.011 (max is trial 1) | compiled=5 | 13,221,728.0 | 1,374,585,481.0 | 279,752.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,442,672,018.0 | 1,428,418,656.0 | 1,462,672,906.0 | 10,922,866.5 | 5 | 680,528 | 395,013 (warned) | 100,533 | 0.008 | compiled=5 | 12,862,773.0 | 1,429,231,081.0 | 291,471.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 1,384,138,669.0 | 1,363,268,595.0 | 1,397,787,495.0 | 12,468,254.3 | 5 | 659,992 | 402,219 (warned) | 102,683 | 0.009 (max is trial 1) | compiled=5 | 13,143,465.0 | 1,370,468,261.0 | 519,853.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 160,357,555.0 | 157,389,547.0 | 163,568,570.0 | 2,230,282.8 | 5 | 27,872 | 21,615 | 15,703 | 0.014 | compiled=5 | 2,239,691.0 | 157,999,872.0 | 108,500.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 173,655,803.0 | 163,618,000.0 | 181,214,311.0 | 5,596,320.7 | 5 | 28,016 | 24,222 | 17,792 | 0.032 | compiled=5 | 2,162,551.0 | 171,365,050.0 | 101,150.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 153,477,700.0 | 147,130,698.0 | 169,166,557.0 | 8,150,818.3 | 5 | 27,872 | 21,615 | 15,703 | 0.053 | compiled=5 | 2,164,801.0 | 151,072,637.0 | 183,841.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 164,354,693.0 | 158,985,345.0 | 174,411,602.0 | 5,217,514.8 | 5 | 28,016 | 24,222 | 17,792 | 0.032 | compiled=5 | 2,160,441.0 | 162,277,773.0 | 98,780.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna` | 137,076,423.0 | 136,190,499.0 | 152,196,503.0 | 6,168,938.8 | 5 | 27,656 | 15,346 | 13,263 | 0.045 | compiled=5 | 1,627,789.0 | 134,462,040.0 | 100,360.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna` | 146,061,340.0 | 134,374,850.0 | 150,433,713.0 | 6,796,590.9 | 5 | 27,616 | 15,169 | 13,086 | 0.047 | compiled=5 | 1,610,099.0 | 144,350,651.0 | 187,361.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 148,156,672.0 | 138,857,627.0 | 149,193,600.0 | 3,896,993.8 | 5 | 27,656 | 15,346 | 13,263 | 0.026 | compiled=5 | 1,618,968.0 | 146,409,274.0 | 108,891.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun` | 134,227,714.0 | 133,669,760.0 | 147,991,073.0 | 5,919,599.3 | 5 | 27,616 | 15,169 | 13,086 | 0.044 | compiled=5 | 1,645,748.0 | 132,455,155.0 | 102,911.0 |

