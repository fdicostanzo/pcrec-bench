# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=capability, version=0.1, since=2026-09-18T06:00:00Z, until=2026-09-19T05:00:00Z, testee=re2_11.0.0_default-caps-simdna, testee=tre_0.9.0_default-caps-simdna, testee=vectorscan_5.4.11_block-nosom-nocaps-simd
- record source: store/index.tsv (3 record(s) matching this query)
- records included: 3
- worst other-core busy: 33.33% (`re2_11.0.0_default-caps-simdna` / `logparse-atomic-removed` / `large-subject-throughput`)
    - `capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260919T032209Z` (store/records/capability@0.1/re2_11.0.0_default-caps-simdna/capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260919T032209Z.jsonl) — agreement: agree (0 of 77 groups; 0 of 3037 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260919T033612Z` (store/records/capability@0.1/tre_0.9.0_default-caps-simdna/capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260919T033612Z.jsonl) — agreement: agree (0 of 79 groups; 0 of 3142 rows; 56 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260919T035552Z` (store/records/capability@0.1/vectorscan_5.4.11_block-nosom-nocaps-simd/capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260919T035552Z.jsonl) — agreement: agree (0 of 80 groups; 0 of 3118 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 3 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.8 | 0.0001 | 167.6 | 176.0 | 3.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.9 | 0.0002 | 283.3 | 287.6 | 1.8 | 1.698x | 1.698x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,842,838.8 | 8.6051 | 11,797,877.3 | 11,924,289.2 | 44,904.5 | 70578.768x | 70578.768x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 8,990,462.0 | 8.5740 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,254,399.1 | 8.5999 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 565,094.0 | 8.6227 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,051.2 | 2,045.9 | 2,056.0 | 4.1 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,066.2 | 4,061.9 | 4,067.0 | 1.9 | 1.982x | 1.982x | 75 | 54.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,605.5 | 18,486.1 | 18,805.0 | 106.9 | 9.071x | 9.071x | 75 | 248.1 | 27.9 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,332.8 | 0.0882 | 121,232.7 | 121,541.0 | 111.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,627.3 | 1.6259 | 2,236,494.0 | 2,241,591.7 | 1,835.7 | 18.442x | 18.442x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,969,063.6 | 46.4805 | 63,711,186.4 | 65,136,253.4 | 524,881.8 | 527.220x | 527.220x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,514.9 | 0.0882 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,191.7 | 1.6186 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 48,591,284.2 | 46.3403 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,060.5 | 0.0880 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,430.5 | 1.6191 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,260,570.0 | 46.7704 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,756.0 | 0.0878 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,706.9 | 1.7655 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,072,513.0 | 46.8828 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,471.1 | 2,464.4 | 2,476.7 | 4.7 | 1.000x | 1.000x | 75 | 32.9 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,690.0 | 7,660.0 | 8,275.6 | 239.3 | 3.112x | 3.112x | 75 | 102.5 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,957.2 | 23,942.3 | 24,648.5 | 278.6 | 9.695x | 9.695x | 75 | 319.4 | 27.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,304.1 | 0.0881 | 120,649.4 | 121,731.3 | 369.0 | 1.000x | 1.000x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,596.0 | 0.0883 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,042.9 | 0.0879 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,750.1 | 0.0877 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,468.2 | 2,457.0 | 2,474.7 | 5.8 | 1.000x | 1.000x | 75 | 32.9 | 27.2 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.8 | 167.2 | 0.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 283.4 | 290.5 | 2.5 | 1.714x | 1.714x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,687,624.6 | 6.3125 | 8,682,949.6 | 8,722,121.4 | 15,359.7 | 52011.099x | 52011.099x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,617,874.8 | 6.3113 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.7 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,493.1 | 6.3152 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,326.4 | 6.3374 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,866.0 | 1,864.4 | 1,878.8 | 5.2 | 1.000x | 1.000x | 75 | 24.9 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,631.6 | 9,491.2 | 10,574.8 | 398.4 | 5.162x | 5.162x | 75 | 128.4 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,750.6 | 13,719.8 | 13,805.6 | 31.5 | 7.369x | 7.369x | 75 | 183.3 | 27.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 214,644,617.5 | 155.9627 | 214,203,910.0 | 215,813,103.0 | 603,659.5 | 1.000x | 1.000x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 163,981,124.0 | 156.3846 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 40,734,300.0 | 155.3890 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 10,124,105.0 | 154.4816 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 211,358.9 | 210,893.3 | 211,918.7 | 327.1 | 1.000x | 1.000x | 75 | 2,818.1 | 27.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 185,048,882.0 | 134.4582 | 183,980,472.0 | 186,006,427.0 | 793,633.8 | 1.000x | 1.000x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 140,873,785.5 | 134.3477 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 35,411,058.5 | 135.0825 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,764,038.0 | 133.7286 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 196,700.5 | 195,658.9 | 197,204.7 | 623.0 | 1.000x | 1.000x | 75 | 2,622.7 | 27.9 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 341.4 | 0.0002 | 338.4 | 350.0 | 4.0 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,608.8 | 0.0230 | 31,591.8 | 31,745.3 | 57.3 | 92.586x | 92.586x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,946,697.0 | 15.9467 | 21,270,517.4 | 22,587,559.6 | 492,877.2 | 64284.437x | 64284.437x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 113.0 | 0.0001 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,106.2 | 0.0230 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,627,798.2 | 15.8575 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 102.1 | 0.0004 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,960.8 | 0.0227 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,236,584.6 | 16.1613 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 125.1 | 0.0019 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.4 | 0.0233 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,071,430.8 | 16.3487 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,842.8 | 1,841.1 | 1,846.6 | 2.2 | 1.000x | 1.000x | 75 | 24.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 44,042.2 | 43,672.6 | 44,380.6 | 257.6 | 23.900x | 23.900x | 75 | 587.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 204,644.0 | 204,232.7 | 205,863.3 | 560.9 | 111.052x | 111.052x | 75 | 2,728.6 | 27.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 169.8 | 0.0001 | 169.7 | 170.1 | 0.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 313.2 | 0.0002 | 310.6 | 364.8 | 20.6 | 1.844x | 1.844x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,233,238.4 | 7.4356 | 10,204,195.9 | 10,275,745.2 | 23,436.7 | 60260.810x | 60260.810x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 100.6 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,798,637.2 | 7.4374 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 90.5 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,951,998.2 | 7.4463 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 58.7 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 122.9 | 0.0019 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 488,977.6 | 7.4612 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 84,722.6 | 0.0616 | 84,681.4 | 84,797.9 | 41.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 250,537.7 | 0.1820 | 250,375.8 | 250,683.8 | 129.5 | 2.957x | 2.957x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,659,286.9 | 18.6443 | 25,645,177.6 | 25,751,021.9 | 38,923.5 | 302.862x | 302.862x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 64,532.4 | 0.0615 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 196,838.5 | 0.1877 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,542,557.4 | 18.6372 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,066.7 | 0.0613 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 42,607.1 | 0.1625 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,894,560.0 | 18.6713 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,107.3 | 0.0627 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 10,930.1 | 0.1668 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,227,590.2 | 18.7315 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,477.7 | 2,474.8 | 2,484.5 | 3.3 | 1.000x | 1.000x | 75 | 33.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,642.3 | 7,629.0 | 7,652.1 | 8.1 | 3.084x | 3.084x | 75 | 101.9 | 100.0 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,231.6 | 0.0169 | 23,207.7 | 23,329.0 | 44.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,754.4 | 0.0173 | 23,746.0 | 23,848.9 | 44.5 | 1.023x | 1.023x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,371.4 | 0.0235 | 32,354.8 | 32,533.6 | 66.0 | 1.393x | 1.393x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,673.0 | 0.0169 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,809.6 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,549.8 | 0.0234 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,410.8 | 0.0168 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,508.8 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,143.1 | 0.0234 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,143.7 | 0.0175 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,441.9 | 0.0220 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,673.2 | 0.0255 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,040.9 | 2,039.2 | 2,042.2 | 1.0 | 1.000x | 1.000x | 75 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,093.3 | 2,089.0 | 2,157.5 | 26.5 | 1.026x | 1.026x | 75 | 27.9 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,498.7 | 7,496.4 | 7,543.6 | 18.5 | 3.674x | 3.674x | 75 | 100.0 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 64,041.8 | 0.0465 | 63,989.0 | 64,175.5 | 76.5 | 1.000x | 1.000x | 3 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,046.8 | 1.6255 | 2,231,987.1 | 2,241,666.4 | 3,740.3 | 34.931x | 34.931x | 3 | 100% |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48,674.5 | 0.0464 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,697.6 | 1.6191 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 12,217.2 | 0.0466 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,942.2 | 1.6172 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,144.3 | 0.0480 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,393.1 | 1.7760 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,643.3 | 2,634.7 | 2,647.0 | 4.7 | 1.000x | 1.000x | 75 | 35.2 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,683.7 | 9,646.3 | 9,746.8 | 33.6 | 3.663x | 3.663x | 75 | 129.1 | 100.0 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.3 | 32.3 | 0.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.8 | 0.0002 | 285.2 | 291.9 | 2.8 | 9.411x | 9.411x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,414,828.9 | 11.2006 | 15,367,175.8 | 16,262,951.8 | 345,482.0 | 505774.141x | 505774.141x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,695,006.9 | 11.1532 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,969,110.2 | 11.3263 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.9 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 749,468.9 | 11.4360 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 951.0 | 950.1 | 953.9 | 1.3 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,818.3 | 6,807.5 | 6,837.2 | 11.3 | 7.170x | 7.170x | 75 | 90.9 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,706.0 | 30,327.9 | 30,878.0 | 228.1 | 32.289x | 32.289x | 75 | 409.4 | 27.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 291.4 | 0.0002 | 291.1 | 292.3 | 0.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,435,148.9 | 1.7694 | 2,428,039.7 | 2,489,567.4 | 25,033.8 | 8355.860x | 8355.860x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 29,472,540.3 | 21.4150 | 29,439,365.8 | 29,561,204.2 | 47,868.4 | 101130.747x | 101130.747x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,858,714.8 | 1.7726 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,432,575.7 | 21.3934 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 123.7 | 0.0005 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 456,628.9 | 1.7419 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,618,181.4 | 21.4317 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81.8 | 0.0012 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 119,284.3 | 1.8201 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,411,843.2 | 21.5430 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,667.3 | 2,666.2 | 2,670.5 | 1.5 | 1.000x | 1.000x | 75 | 35.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,951.8 | 7,924.2 | 8,062.4 | 50.4 | 2.981x | 2.981x | 75 | 106.0 | 100.0 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 135.0 | 0.0001 | 134.7 | 136.0 | 0.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.0 | 0.0002 | 286.5 | 314.5 | 11.0 | 2.126x | 2.126x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,219,633.4 | 13.9652 | 19,129,025.2 | 19,928,501.2 | 333,094.2 | 142407.152x | 142407.152x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.7 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,649,327.5 | 13.9707 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.5 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,656,527.9 | 13.9485 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45.7 | 0.0007 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 110.7 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 916,344.5 | 13.9823 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,150.4 | 1,145.8 | 1,164.6 | 6.4 | 1.000x | 1.000x | 75 | 15.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,889.9 | 7,859.6 | 8,447.0 | 224.8 | 6.859x | 6.859x | 75 | 105.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 41,466.3 | 41,188.4 | 41,615.7 | 141.0 | 36.046x | 36.046x | 75 | 552.9 | 27.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,781.0 | 0.0173 | 23,730.3 | 23,982.8 | 88.2 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,604.1 | 0.0230 | 31,599.9 | 31,640.3 | 16.0 | 1.329x | 1.329x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,720,481.9 | 15.7823 | 20,799,474.3 | 22,717,032.7 | 606,971.7 | 913.354x | 913.354x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,832.4 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,118.2 | 0.0230 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,468,005.4 | 15.7051 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,500.1 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,968.0 | 0.0228 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,126,468.7 | 15.7412 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,447.3 | 0.0221 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.5 | 0.0233 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,109,084.1 | 16.9233 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,044.8 | 2,036.8 | 2,052.4 | 5.6 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,560.5 | 7,534.7 | 7,618.2 | 30.3 | 3.698x | 3.698x | 75 | 100.8 | 100.0 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.5 | 0.0001 | 166.8 | 169.8 | 1.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 285.0 | 301.2 | 5.9 | 1.711x | 1.711x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,694,208.3 | 6.3173 | 8,684,286.3 | 8,772,257.7 | 32,602.9 | 51896.112x | 51896.112x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,625,504.8 | 6.3186 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.2 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,366.4 | 6.3147 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.1 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,593.9 | 6.3415 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,963.8 | 1,959.9 | 1,965.1 | 1.8 | 1.000x | 1.000x | 75 | 26.2 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,657.8 | 9,570.4 | 9,783.1 | 67.9 | 4.918x | 4.918x | 75 | 128.8 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,295.3 | 13,281.9 | 13,361.0 | 30.7 | 6.770x | 6.770x | 75 | 177.3 | 27.9 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 167.1 | 0.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.2 | 0.0002 | 284.3 | 289.5 | 1.9 | 1.713x | 1.713x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,683,755.6 | 6.3097 | 8,673,709.6 | 8,710,308.4 | 13,344.1 | 51996.508x | 51996.508x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.3 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,614,472.7 | 6.3081 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,458.6 | 6.3074 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 416,018.2 | 6.3479 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,984.0 | 1,983.3 | 2,101.8 | 46.0 | 1.000x | 1.000x | 75 | 26.5 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,014.8 | 9,965.3 | 10,124.4 | 65.9 | 5.048x | 5.048x | 75 | 133.5 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,004.8 | 14,930.0 | 15,031.3 | 36.6 | 7.563x | 7.563x | 75 | 200.1 | 27.9 | 100% |

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,963,805.0 | 21.0454 | 28,720,721.8 | 29,121,590.8 | 155,206.3 | 1.000x | 1.000x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,160,921.6 | 21.1343 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,459,734.8 | 20.8272 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,356,522.7 | 20.6989 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,494.1 | 30,054.2 | 31,238.8 | 391.5 | 1.000x | 1.000x | 75 | 406.6 | 27.9 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,249.4 | 0.0009 | 1,248.8 | 1,250.2 | 0.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 400,035.5 | 0.2907 | 399,107.4 | 403,813.4 | 1,728.4 | 320.180x | 320.180x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 26,327,343.3 | 19.1297 | 26,305,079.1 | 26,585,831.7 | 104,626.0 | 21071.844x | 21071.844x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85.2 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 304,523.3 | 0.2904 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 20,052,616.4 | 19.1237 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 632.8 | 0.0024 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 74,622.2 | 0.2847 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,019,417.1 | 19.1476 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 531.2 | 0.0081 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 20,094.7 | 0.3066 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,253,820.8 | 19.1318 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,297.6 | 2,294.2 | 2,306.2 | 4.1 | 1.000x | 1.000x | 75 | 30.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,631.1 | 7,599.5 | 8,310.2 | 274.6 | 3.321x | 3.321x | 75 | 101.7 | 100.0 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 34,508,904.2 | 25.0745 | 34,440,542.6 | 34,914,541.2 | 176,483.6 | 1.000x | 1.000x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,286,922.8 | 25.0692 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,574,723.4 | 25.0806 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,647,258.1 | 25.1352 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,435.2 | 47,322.8 | 47,514.6 | 67.4 | 1.000x | 1.000x | 75 | 632.5 | 27.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 27,821,937.3 | 20.2157 | 27,753,897.0 | 27,866,656.7 | 42,766.3 | 1.000x | 1.000x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,149,505.7 | 20.1697 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,353,807.2 | 20.4232 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,337,324.6 | 20.4060 |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 167.0 | 0.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 284.8 | 290.4 | 2.1 | 1.716x | 1.716x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,837,748.5 | 8.6014 | 11,782,156.0 | 12,121,955.0 | 120,069.7 | 70903.338x | 70903.338x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,019,656.5 | 8.6018 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,253,144.9 | 8.5951 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.1 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 567,622.6 | 8.6612 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,862.7 | 1,861.4 | 1,865.5 | 1.6 | 1.000x | 1.000x | 75 | 24.8 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,422.8 | 9,396.7 | 9,439.7 | 14.7 | 5.059x | 5.059x | 75 | 125.6 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,453.6 | 19,386.4 | 19,630.7 | 89.3 | 10.444x | 10.444x | 75 | 259.4 | 27.9 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.5 | 0.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 300.0 | 0.0002 | 297.2 | 301.8 | 1.8 | 9.887x | 9.887x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,818,773.0 | 8.5876 | 11,801,817.3 | 12,165,588.1 | 138,902.9 | 389532.593x | 389532.593x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.6 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 8,996,919.4 | 8.5801 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,262,264.4 | 8.6299 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 122.4 | 0.0019 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 568,892.3 | 8.6806 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 572.9 | 572.2 | 590.3 | 7.1 | 1.000x | 1.000x | 75 | 7.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,225.7 | 4,211.3 | 4,488.0 | 105.1 | 7.377x | 7.377x | 75 | 56.3 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,438.8 | 35,347.3 | 35,547.4 | 68.3 | 61.864x | 61.864x | 75 | 472.5 | 27.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 124.1 | 0.0001 | 123.3 | 126.4 | 1.1 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 700,512.6 | 0.5090 | 699,859.4 | 702,019.4 | 716.7 | 5646.980x | 5646.980x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 1,642,847.0 | 1.1937 | 1,638,657.9 | 1,677,721.6 | 16,213.1 | 13243.337x | 13243.337x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 43.5 | 0.0000 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 536,571.4 | 0.5117 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,249,453.9 | 1.1916 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 40.7 | 0.0002 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 129,736.7 | 0.4949 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 303,013.6 | 1.1559 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 39.6 | 0.0006 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 34,144.6 | 0.5210 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 90,208.6 | 1.3765 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,070.7 | 2,070.2 | 2,074.0 | 1.4 | 1.000x | 1.000x | 75 | 27.6 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,189.5 | 2,187.1 | 2,191.4 | 1.6 | 1.057x | 1.057x | 75 | 29.2 | 27.9 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,733.9 | 7,724.4 | 7,973.7 | 96.7 | 3.735x | 3.735x | 75 | 103.1 | 100.0 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 182,488.3 | 0.1326 | 182,296.3 | 182,993.6 | 295.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,236,308.9 | 1.6249 | 2,233,007.0 | 2,244,237.8 | 4,044.7 | 12.255x | 12.255x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 65,630,395.8 | 47.6876 | 64,850,068.0 | 66,804,147.6 | 643,650.1 | 359.642x | 359.642x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 140,280.6 | 0.1338 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,695,063.0 | 1.6165 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 49,895,688.6 | 47.5842 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 33,759.6 | 0.1288 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,967.9 | 1.6173 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,558,671.6 | 47.9075 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 8,359.4 | 0.1276 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,091.0 | 1.7714 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,111,675.4 | 47.4804 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,988.3 | 2,983.5 | 3,000.0 | 5.8 | 1.000x | 1.000x | 75 | 39.8 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,583.1 | 9,559.0 | 9,687.4 | 47.3 | 3.207x | 3.207x | 75 | 127.8 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 64,048.8 | 63,695.4 | 64,260.0 | 185.8 | 21.433x | 21.433x | 75 | 854.0 | 27.9 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,288.8 | 0.0169 | 23,228.5 | 24,324.8 | 417.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,769.9 | 0.0173 | 23,747.4 | 23,804.4 | 20.6 | 1.021x | 1.021x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,309.3 | 0.0235 | 32,294.8 | 32,532.0 | 91.2 | 1.387x | 1.387x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,697.5 | 0.0169 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,775.7 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,503.7 | 0.0234 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,425.7 | 0.0169 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,539.8 | 0.0173 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,134.5 | 0.0234 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,139.0 | 0.0174 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,452.5 | 0.0222 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,672.2 | 0.0255 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,041.4 | 2,038.9 | 2,042.3 | 1.4 | 1.000x | 1.000x | 75 | 27.2 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,092.7 | 2,092.1 | 2,097.8 | 2.1 | 1.025x | 1.025x | 75 | 27.9 | 27.9 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,539.0 | 7,498.0 | 7,757.7 | 97.0 | 3.693x | 3.693x | 75 | 100.5 | 100.0 | 100% |

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 650.7 | 0.0005 | 649.3 | 651.3 | 0.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 946,749,306.0 | 687.9166 | 905,452,639.0 | 1,002,090,124.0 | 35,544,164.5 | 1454909.082x | 1454909.082x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 208.7 | 0.0002 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 716,191,416.0 | 683.0134 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 213.8 | 0.0008 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 177,913,008.0 | 678.6843 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 228.2 | 0.0035 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 51,148,487.0 | 780.4640 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,749.2 | 3,745.1 | 3,858.0 | 43.1 | 1.000x | 1.000x | 75 | 50.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 183,049.2 | 182,072.6 | 185,479.3 | 1,169.2 | 48.824x | 48.824x | 75 | 2,440.7 | 100.0 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 148.4 | 0.0001 | 147.1 | 149.1 | 0.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.0 | 0.0002 | 282.9 | 287.7 | 1.8 | 1.935x | 1.935x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,449,886.9 | 11.2260 | 15,371,742.6 | 16,080,823.3 | 269,784.2 | 104144.193x | 104144.193x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.2 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,745,622.6 | 11.2015 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.0 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.3 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,951,209.5 | 11.2580 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.7 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 745,620.3 | 11.3773 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,618.6 | 1,617.2 | 2,044.7 | 168.0 | 1.000x | 1.000x | 75 | 21.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,725.1 | 9,667.1 | 9,953.8 | 101.4 | 6.008x | 6.008x | 75 | 129.7 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 42,412.1 | 42,319.1 | 42,752.5 | 152.8 | 26.202x | 26.202x | 75 | 565.5 | 27.9 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292,497.5 | 0.2125 | 292,378.8 | 293,479.4 | 401.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,687.1 | 1.6267 | 2,236,183.7 | 2,248,860.0 | 4,513.5 | 7.654x | 7.654x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 173,226,369.0 | 125.8678 | 171,118,674.0 | 178,723,876.5 | 2,931,049.9 | 592.232x | 592.232x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 223,208.2 | 0.2129 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,341.3 | 1.6187 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 131,533,949.5 | 125.4405 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55,294.8 | 0.2109 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,708.1 | 1.6239 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 33,634,450.0 | 128.3052 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 14,002.4 | 0.2137 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,455.6 | 1.7770 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,363,821.0 | 127.6218 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,105.2 | 2,103.4 | 2,110.5 | 2.5 | 1.000x | 1.000x | 75 | 28.1 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,902.8 | 9,868.0 | 9,943.5 | 25.1 | 4.704x | 4.704x | 75 | 132.0 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 174,869.9 | 173,420.5 | 177,029.0 | 1,329.1 | 83.068x | 83.068x | 75 | 2,331.6 | 27.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,270.7 | 0.0438 | 60,264.5 | 60,280.9 | 5.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,637.4 | 1.6295 | 2,239,616.6 | 2,246,612.1 | 2,319.0 | 37.209x | 37.209x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,071,017.5 | 18.2168 | 24,963,976.9 | 25,119,971.4 | 69,434.8 | 415.973x | 415.973x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,842.4 | 0.0437 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,777.5 | 1.6210 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,113,100.1 | 18.2277 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,477.6 | 0.0438 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,549.6 | 1.6233 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,767,293.4 | 18.1858 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,955.1 | 0.0451 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 117,200.9 | 1.7883 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,193,589.5 | 18.2127 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 827.4 | 826.6 | 1,019.6 | 76.7 | 1.000x | 1.000x | 75 | 11.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,219.9 | 10,125.4 | 10,368.2 | 79.0 | 12.352x | 12.352x | 75 | 136.3 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 56,743.7 | 56,665.9 | 56,839.2 | 58.3 | 68.579x | 68.579x | 75 | 756.6 | 27.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 111,971.3 | 0.0814 | 111,773.9 | 112,352.4 | 214.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,307.0 | 0.3192 | 438,961.5 | 439,652.1 | 252.6 | 3.923x | 3.923x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,182,018.8 | 25.5636 | 35,133,374.8 | 35,400,926.1 | 93,622.9 | 314.206x | 314.206x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86,603.8 | 0.0826 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,888.6 | 0.3156 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,800,021.4 | 25.5585 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,538.4 | 0.0783 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 83,175.2 | 0.3173 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,713,634.1 | 25.6105 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,872.3 | 0.0743 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,163.0 | 0.3840 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,679,405.8 | 25.6257 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 694.7 | 694.5 | 695.9 | 0.5 | 1.000x | 1.000x | 75 | 9.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,030.9 | 8,997.8 | 9,102.2 | 34.5 | 12.999x | 12.999x | 75 | 120.4 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 74,945.8 | 74,888.0 | 75,161.5 | 105.2 | 107.878x | 107.878x | 75 | 999.3 | 27.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 475,639.5 | 0.3456 | 474,966.7 | 477,227.5 | 841.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,244,413.2 | 1.6308 | 2,233,465.1 | 2,368,475.8 | 51,202.5 | 4.719x | 4.719x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 377,913.1 | 0.3604 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,218.2 | 1.6215 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81,021.7 | 0.3091 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,587.4 | 1.6197 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,517.5 | 0.2520 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,505.2 | 1.7777 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,648.8 | 1,646.1 | 1,656.1 | 3.3 | 1.000x | 1.000x | 75 | 22.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,401.1 | 10,251.0 | 10,837.3 | 204.3 | 6.308x | 6.308x | 75 | 138.7 | 100.0 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 153,324.4 | 0.1114 | 153,208.5 | 153,646.1 | 149.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 325,819.5 | 0.2367 | 325,598.9 | 326,135.1 | 187.8 | 2.125x | 2.125x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,627,126.7 | 20.8007 | 28,540,578.1 | 29,458,641.2 | 345,586.0 | 186.710x | 186.710x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 116,831.6 | 0.1114 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 256,347.8 | 0.2445 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,750,661.5 | 20.7430 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 29,096.1 | 0.1110 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 55,017.0 | 0.2099 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,456,195.5 | 20.8137 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,353.6 | 0.1122 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 14,455.2 | 0.2206 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,369,745.4 | 20.9007 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,405.6 | 2,403.5 | 2,445.3 | 16.2 | 1.000x | 1.000x | 75 | 32.1 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,492.3 | 7,478.0 | 7,588.8 | 41.3 | 3.115x | 3.115x | 75 | 99.9 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,950.7 | 30,851.5 | 31,460.2 | 223.5 | 12.866x | 12.866x | 75 | 412.7 | 27.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 223.8 | 0.0002 | 223.8 | 254.3 | 12.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 315.8 | 0.0002 | 312.1 | 317.3 | 1.7 | 1.411x | 1.411x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,557,154.3 | 13.4838 | 18,341,529.1 | 18,579,317.1 | 89,780.6 | 82902.264x | 82902.264x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.0 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 99.1 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,136,239.7 | 13.4814 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 99.2 | 0.0004 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,534,583.7 | 13.4834 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.5 | 0.0011 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 118.3 | 0.0018 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 888,250.8 | 13.5536 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,764.9 | 2,763.4 | 2,857.4 | 37.1 | 1.000x | 1.000x | 75 | 36.9 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,352.1 | 7,330.8 | 7,366.6 | 12.4 | 2.659x | 2.659x | 75 | 98.0 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 12,699.1 | 12,675.2 | 12,715.8 | 13.4 | 4.593x | 4.593x | 75 | 169.3 | 27.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 242.0 | 0.0002 | 241.3 | 242.5 | 0.4 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 46,745,767.7 | 33.9659 | 45,643,450.0 | 46,832,126.5 | 528,821.9 | 193196.900x | 193196.900x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 64,501,084.6 | 46.8671 | 64,309,175.6 | 65,906,957.4 | 592,380.5 | 266578.350x | 266578.350x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.0 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 35,583,869.0 | 33.9354 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 49,317,533.6 | 47.0329 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 78.9 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 8,842,669.5 | 33.7321 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 12,189,440.6 | 46.4990 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 79.2 | 0.0012 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,208,607.0 | 33.7007 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 3,023,928.6 | 46.1415 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,900.6 | 3,895.7 | 3,909.3 | 4.7 | 1.000x | 1.000x | 75 | 52.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 19,831.7 | 19,791.4 | 19,982.7 | 79.9 | 5.084x | 5.084x | 75 | 264.4 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,646.3 | 30,613.0 | 30,716.3 | 35.7 | 7.857x | 7.857x | 75 | 408.6 | 27.9 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 202.1 | 0.0001 | 196.0 | 202.7 | 2.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 364.0 | 392.2 | 10.5 | 1.818x | 1.818x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 22,258,020.6 | 16.1729 | 21,077,869.0 | 22,376,360.2 | 501,461.0 | 110148.833x | 110148.833x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 72.7 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 112.8 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,925,301.5 | 16.1412 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 60.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 101.2 | 0.0004 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,258,091.4 | 16.2433 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 68.4 | 0.0010 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 153.7 | 0.0023 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,070,981.8 | 16.3419 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,248.6 | 2,245.6 | 2,255.5 | 3.3 | 1.000x | 1.000x | 75 | 30.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,127.6 | 8,094.8 | 8,171.0 | 24.3 | 3.614x | 3.614x | 75 | 108.4 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 120,654.4 | 120,381.9 | 120,833.8 | 194.1 | 53.657x | 53.657x | 75 | 1,608.7 | 27.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 35.5 | 2.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 287.2 | 0.0002 | 282.1 | 543.3 | 102.7 | 9.454x | 9.454x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,445,909.9 | 11.2231 | 15,411,565.3 | 15,503,843.6 | 33,320.8 | 508506.591x | 508506.591x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.5 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,736,709.9 | 11.1930 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 91.0 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,946,854.8 | 11.2414 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 746,044.7 | 11.3837 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 953.4 | 950.9 | 966.6 | 5.6 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,344.2 | 9,301.7 | 9,386.8 | 28.4 | 9.801x | 9.801x | 75 | 124.6 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 38,754.2 | 38,537.2 | 38,879.6 | 121.8 | 40.647x | 40.647x | 75 | 516.7 | 27.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.4 | 36.7 | 2.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 283.5 | 286.9 | 1.4 | 9.382x | 9.382x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,695,277.0 | 6.3181 | 8,692,212.8 | 8,736,184.0 | 16,684.0 | 284632.521x | 284632.521x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.9 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,625,106.1 | 6.3182 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,655,985.7 | 6.3171 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.8 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,258.1 | 6.3363 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 986.0 | 985.7 | 1,052.1 | 26.0 | 1.000x | 1.000x | 75 | 13.1 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,041.7 | 2,037.8 | 2,485.1 | 177.6 | 2.071x | 2.071x | 75 | 27.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,928.4 | 13,910.8 | 14,002.7 | 32.1 | 14.126x | 14.126x | 75 | 185.7 | 27.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243,258.4 | 0.1768 | 243,026.3 | 243,534.2 | 176.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,753.9 | 1.6260 | 2,232,636.1 | 2,244,177.6 | 3,715.4 | 9.199x | 9.199x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 72,093,852.0 | 52.3840 | 71,893,388.8 | 72,336,540.8 | 171,659.5 | 296.367x | 296.367x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 185,633.7 | 0.1770 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,698,742.3 | 1.6200 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 54,871,984.2 | 52.3300 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 46,111.3 | 0.1759 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,558.5 | 1.6157 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 13,733,608.5 | 52.3896 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,415.9 | 0.1742 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,773.2 | 1.7666 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,447,786.5 | 52.6090 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,623.9 | 1,622.4 | 1,628.3 | 2.1 | 1.000x | 1.000x | 75 | 21.7 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,919.5 | 9,782.7 | 10,083.5 | 105.0 | 6.108x | 6.108x | 75 | 132.3 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 122,037.8 | 120,842.6 | 126,332.4 | 1,992.1 | 75.149x | 75.149x | 75 | 1,627.2 | 27.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 600,282.9 | 0.4362 | 600,078.2 | 600,746.5 | 223.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,241,475.2 | 1.6287 | 2,234,637.2 | 2,244,885.2 | 4,405.6 | 3.734x | 3.734x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 281,837,562.0 | 204.7857 | 272,627,907.0 | 286,118,153.0 | 4,960,497.9 | 469.508x | 469.508x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 477,896.7 | 0.4558 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,006.7 | 1.6222 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 215,696,548.0 | 205.7043 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 101,855.2 | 0.3885 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,421.6 | 1.6229 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 52,648,788.0 | 200.8392 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,504.8 | 0.3129 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,404.0 | 1.7762 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 13,470,716.0 | 205.5468 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,412.2 | 3,406.3 | 3,413.1 | 2.9 | 1.000x | 1.000x | 75 | 45.5 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,613.9 | 9,602.1 | 9,672.9 | 26.7 | 2.818x | 2.818x | 75 | 128.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 322,509.9 | 318,340.6 | 323,735.3 | 1,968.8 | 94.517x | 94.517x | 75 | 4,300.1 | 27.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 160,319.3 | 0.1165 | 160,095.4 | 160,605.1 | 165.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,967.6 | 1.6269 | 2,232,496.8 | 2,242,778.2 | 3,588.2 | 13.966x | 13.966x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 60,083,206.6 | 43.6570 | 60,035,694.2 | 60,306,357.8 | 95,487.1 | 374.772x | 374.772x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 122,178.9 | 0.1165 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,488.6 | 1.6208 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 45,771,680.4 | 43.6513 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 30,405.1 | 0.1160 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,635.7 | 1.6160 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 11,441,602.0 | 43.6462 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,760.4 | 0.1184 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,321.8 | 1.7749 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,884,170.2 | 44.0089 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,424.2 | 2,416.2 | 2,427.8 | 4.6 | 1.000x | 1.000x | 75 | 32.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,635.8 | 9,548.8 | 9,873.0 | 115.5 | 3.975x | 3.975x | 75 | 128.5 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 71,092.0 | 71,064.1 | 71,195.9 | 56.8 | 29.326x | 29.326x | 75 | 947.9 | 27.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 86,476.9 | 0.0628 | 86,305.2 | 86,557.0 | 87.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,297.2 | 0.3192 | 438,987.8 | 439,658.3 | 261.4 | 5.080x | 5.080x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,934,558.2 | 22.4773 | 30,890,917.0 | 30,980,398.6 | 28,546.6 | 357.720x | 357.720x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 65,906.4 | 0.0629 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,774.1 | 0.3155 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 23,548,538.8 | 22.4576 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,432.6 | 0.0627 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 83,260.4 | 0.3176 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,894,987.8 | 22.4876 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,148.6 | 0.0633 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,172.3 | 0.3841 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,481,620.7 | 22.6077 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,911.9 | 1,907.5 | 1,914.9 | 2.5 | 1.000x | 1.000x | 75 | 25.5 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,262.9 | 8,250.8 | 8,311.3 | 22.1 | 4.322x | 4.322x | 75 | 110.2 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 39,238.2 | 39,190.5 | 39,256.3 | 23.6 | 20.523x | 20.523x | 75 | 523.2 | 27.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 880,368.1 | 0.6397 | 877,335.7 | 882,480.2 | 1,938.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,249,243.6 | 1.6343 | 2,246,083.4 | 2,255,865.2 | 3,271.8 | 2.555x | 2.555x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 1,160,121,978.0 | 842.9551 | 1,154,183,359.0 | 1,166,509,339.0 | 4,250,939.9 | 1317.769x | 1317.769x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 702,149.3 | 0.6696 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,703,248.2 | 1.6243 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 882,783,148.0 | 841.8876 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 149,164.9 | 0.5690 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 425,660.0 | 1.6238 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 221,954,228.0 | 846.6882 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 28,235.7 | 0.4308 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120,044.4 | 1.8317 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 55,695,713.0 | 849.8491 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 4,583.6 | 4,573.4 | 4,629.5 | 20.7 | 1.000x | 1.000x | 75 | 61.1 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,587.6 | 9,552.7 | 9,857.9 | 112.0 | 2.092x | 2.092x | 75 | 127.8 | 100.0 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,189.8 | 0.0437 | 60,164.4 | 60,402.4 | 89.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,147.6 | 0.3191 | 438,846.7 | 440,586.2 | 637.6 | 7.296x | 7.296x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,782.7 | 0.0437 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 331,221.7 | 0.3159 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,465.1 | 0.0437 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,981.8 | 0.3166 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,937.4 | 0.0448 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 24,908.9 | 0.3801 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,355.5 | 2,351.8 | 2,361.1 | 3.7 | 1.000x | 1.000x | 75 | 31.4 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,422.8 | 8,232.6 | 8,709.3 | 178.5 | 3.576x | 3.576x | 75 | 112.3 | 100.0 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 133.2 | 0.0001 | 133.0 | 133.7 | 0.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 300.5 | 0.0002 | 294.6 | 352.1 | 21.1 | 2.256x | 2.256x |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,186,248.8 | 7.4014 | 10,179,917.6 | 10,232,577.4 | 20,502.3 | 76474.091x | 76474.091x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 93.7 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,756,042.3 | 7.3967 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 94.2 | 0.0004 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,942,251.4 | 7.4091 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.8 | 0.0007 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 113.5 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 487,053.9 | 7.4319 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,471.6 | 1,461.4 | 1,472.9 | 4.6 | 1.000x | 1.000x | 75 | 19.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,930.6 | 6,872.6 | 6,980.6 | 40.1 | 4.710x | 4.710x | 75 | 92.4 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,811.7 | 25,755.9 | 26,039.7 | 100.9 | 17.540x | 17.540x | 75 | 344.2 | 27.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `high-byte-run` | `large-subject-throughput` | `plain` | `tre_0.9.0_default-caps-simdna` | 3 | 0% | 0 | 15 | `t-1m` (wrong), `t-256k` (wrong), `t-64k` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 48% | 0 | 195 | `br-dup-param` (wrong), `br-palindrome` (wrong), `cg-number` (wrong), `dt-iso8601` (wrong), `dt-prose-month` (wrong), `la-currency` (wrong), `la-float-bound` (wrong), `la-float-dotted` (wrong), `la-pwd-strong` (wrong), `la-pwd-weak` (wrong), `lp-num-leadzero` (wrong), `lp-num-neg-dec` (wrong), `lp-syslog` (wrong), `lp-winpath` (wrong), `lp-winpath-reserved` (wrong), `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong), `rd-date-hit` (wrong), `rd-email-hit` (wrong), `rd-numeric-id-hit` (wrong), `rd-numeric-id-near-miss` (wrong), `rd-phone-list-hit` (wrong), `rec-array-define` (wrong), `rec-tag-depth3` (wrong), `sec-aws-key` (wrong), `sec-github-pat` (wrong), `sec-slack-webhook` (wrong), `v-ipv4` (wrong), `v-ipv4-oor` (wrong), `v-us-zip` (wrong), `v-us-zip-plus4` (wrong), `v-uuid-badnibble` (wrong), `v-uuid-valid` (wrong), `waf-benign` (wrong), `waf-comment-obfuscation` (wrong), `waf-concat` (wrong), `waf-dbnames` (wrong), `waf-sleep` (wrong), `waf-union` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `tag-pair-match` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `br-tag-pair` (wrong) |
| `wild-waf-crs-942360-concat-sqli` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `waf-union` (wrong) |

## Compile cost (by execution-model class; never pooled across classes)

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 24,310.0 | 19,370.0 | 128,541.0 | 42,092.4 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,011,236.0 | 2,950,235.0 | 4,223,783.0 | 495,453.0 | 5 | 5,896 | 0.165 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,115,027.0 | 2,977,666.0 | 4,598,145.0 | 604,604.3 | 5 | 6,376 | 0.194 (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `re2_11.0.0_default-caps-simdna` | 28,290.0 | 20,720.0 | 134,331.0 | 43,202.3 | 5 | 19 | 1.527 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,317,627.0 | 1,264,897.0 | 2,413,513.0 | 446,399.0 | 5 | 6,088 | 0.339 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,701,830.0 | 1,614,509.0 | 2,773,775.0 | 441,302.4 | 5 | 3,672 | 0.259 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-xflag` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,313,077.0 | 1,271,797.0 | 2,375,822.0 | 428,378.3 | 5 | 6,088 | 0.326 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,684,110.0 | 1,663,789.0 | 2,879,496.0 | 477,323.8 | 5 | 3,672 | 0.283 (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 19,320.0 | 14,620.0 | 113,590.0 | 37,909.7 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,092,496.0 | 1,062,165.0 | 2,138,501.0 | 418,027.9 | 5 | 5,736 | 0.383 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,163,306.0 | 1,130,056.0 | 2,201,942.0 | 415,022.4 | 5 | 6,024 | 0.357 (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 22,200.0 | 16,450.0 | 120,171.0 | 39,797.9 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 562,724.0 | 533,742.0 | 1,510,198.0 | 379,578.1 | 5 | 5,784 | 0.675 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 850,025.0 | 806,634.0 | 1,865,040.0 | 409,248.7 | 5 | 6,232 | 0.481 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,430.0 | 11,300.0 | 108,280.0 | 37,351.9 | 5 | 9 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 595,423.0 | 572,213.0 | 1,555,489.0 | 381,152.2 | 5 | 5,704 | 0.640 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 749,144.0 | 685,024.0 | 1,720,819.0 | 394,948.5 | 5 | 5,992 | 0.527 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 15,980.0 | 12,600.0 | 109,541.0 | 37,650.6 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 507,983.0 | 454,952.0 | 1,385,988.0 | 358,741.6 | 5 | 4,776 | 0.706 (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 573,523.0 | 542,843.0 | 1,551,288.0 | 391,487.8 | 5 | 2,120 | 0.683 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,791.0 | 3,890.0 | 82,310.0 | 31,039.9 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 93,711.0 | 88,111.0 | 549,083.0 | 182,283.6 | 5 | 936 | 1.945 (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 321,662.0 | 304,682.0 | 1,172,446.0 | 339,349.0 | 5 | 1,704 | 1.055 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,120.0 | 10,650.0 | 110,630.0 | 39,067.2 | 5 | 10 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 595,863.0 | 526,692.0 | 1,463,748.0 | 361,108.3 | 5 | 5,784 | 0.606 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 502,832.0 | 485,493.0 | 1,387,567.0 | 352,381.9 | 5 | 1,832 | 0.701 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 66,190.0 | 59,041.0 | 191,061.0 | 50,231.8 | 5 | 49 | 0.759 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,032,681.0 | 2,008,021.0 | 3,119,357.0 | 433,981.6 | 5 | 3,464 | 0.214 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 755,564.0 | 736,334.0 | 1,214,507.0 | 185,579.3 | 5 | 2,824 | 0.246 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 21,530.0 | 13,391.0 | 108,261.0 | 37,494.5 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 543,143.0 | 508,623.0 | 1,434,127.0 | 362,359.2 | 5 | 4,840 | 0.667 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 633,843.0 | 604,713.0 | 1,498,038.0 | 347,004.0 | 5 | 2,504 | 0.547 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `re2_11.0.0_default-caps-simdna` | 33,860.0 | 29,601.0 | 111,711.0 | 31,345.8 | 5 | 80 | 0.926 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,952,881.0 | 3,737,390.0 | 10,969,299.0 | 3,004,810.0 | 5 | 10,168 | 0.760 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,439,378.0 | 3,421,809.0 | 4,140,323.0 | 282,624.1 | 5 | 9,496 | 0.082 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `re2_11.0.0_default-caps-simdna` | 10,510.0 | 8,420.0 | 109,211.0 | 39,434.7 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 723,894.0 | 679,633.0 | 1,753,209.0 | 414,940.0 | 5 | 5,992 | 0.573 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,071,046.0 | 1,057,546.0 | 2,194,412.0 | 447,008.4 | 5 | 3,352 | 0.417 (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 11,010.0 | 8,610.0 | 104,761.0 | 37,612.8 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 819,034.0 | 798,775.0 | 1,780,400.0 | 384,195.0 | 5 | 5,704 | 0.469 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 886,445.0 | 873,925.0 | 1,879,420.0 | 396,102.2 | 5 | 5,992 | 0.447 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,100.0 | 13,660.0 | 111,501.0 | 37,381.7 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 968,455.0 | 932,145.0 | 1,980,060.0 | 406,169.2 | 5 | 5,736 | 0.419 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,029,536.0 | 988,935.0 | 2,046,341.0 | 409,200.8 | 5 | 5,992 | 0.397 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,960.0 | 12,321.0 | 97,500.0 | 33,138.8 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 519,923.0 | 455,633.0 | 1,380,108.0 | 353,995.5 | 5 | 4,776 | 0.681 (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 555,163.0 | 534,283.0 | 1,443,578.0 | 354,765.9 | 5 | 2,120 | 0.639 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `trim-nested-star` | `plain` | `re2_11.0.0_default-caps-simdna` | 12,600.0 | 9,450.0 | 100,780.0 | 35,504.0 | 5 | 8 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 738,664.0 | 711,424.0 | 1,702,769.0 | 388,171.2 | 5 | 5,736 | 0.526 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,710,339.0 | 1,667,779.0 | 2,845,635.0 | 454,563.2 | 5 | 2,600 | 0.266 (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 63,961.0 | 59,480.0 | 197,421.0 | 53,228.4 | 5 | 69 | 0.832 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,274,837.0 | 1,242,517.0 | 2,222,272.0 | 383,276.4 | 5 | 2,216 | 0.301 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 460,543.0 | 447,722.0 | 872,405.0 | 164,967.5 | 5 | 2,088 | 0.358 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,010.0 | 1,600.0 | 43,380.0 | 16,580.5 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 94,250.0 | 87,200.0 | 554,853.0 | 184,471.6 | 5 | 936 | 1.957 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 332,422.0 | 302,122.0 | 1,154,656.0 | 333,616.9 | 5 | 1,704 | 1.004 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `re2_11.0.0_default-caps-simdna` | 23,100.0 | 18,780.0 | 116,671.0 | 37,698.7 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,901,266.0 | 2,886,945.0 | 4,186,413.0 | 512,415.6 | 5 | 7,928 | 0.177 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 771,784.0 | 755,235.0 | 1,708,069.0 | 372,333.9 | 5 | 2,504 | 0.482 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,920.0 | 4,120.0 | 84,061.0 | 31,638.2 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,541.0 | 86,381.0 | 564,413.0 | 188,703.4 | 5 | 936 | 2.039 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 313,222.0 | 300,492.0 | 1,164,837.0 | 340,346.3 | 5 | 1,704 | 1.087 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,922,904.0 | 1,487,307.0 | 4,501,191.0 | 1,151,956.0 | 5 | 3,248 | 0.394 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,776,991,153.0 | 1,772,793,750.0 | 1,812,998,038.0 | 14,890,885.5 | 5 | 158,072 | 0.008 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,726,853,571.0 | 1,724,867,871.0 | 1,763,271,999.0 | 14,636,534.1 | 5 | 141,928 | 0.008 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `re2_11.0.0_default-caps-simdna` | 119,571.0 | 106,681.0 | 272,261.0 | 62,382.1 | 5 | 75 | 0.522 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,001,146.0 | 2,993,956.0 | 3,645,500.0 | 258,346.2 | 5 | 4,232 | 0.086 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,020,816.0 | 2,970,616.0 | 3,559,579.0 | 223,712.2 | 5 | 4,488 | 0.074 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `re2_11.0.0_default-caps-simdna` | 31,150.0 | 25,090.0 | 90,951.0 | 24,956.6 | 5 | 68 | 0.801 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,533,994.0 | 2,368,823.0 | 5,709,950.0 | 1,086,766.1 | 5 | 11,752 | 0.240 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,946,271.0 | 1,731,039.0 | 3,014,116.0 | 460,918.1 | 5 | 3,464 | 0.237 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `re2_11.0.0_default-caps-simdna` | 78,291.0 | 71,950.0 | 157,611.0 | 32,265.3 | 5 | 265 | 0.412 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,077,952.0 | 1,899,340.0 | 5,524,290.0 | 1,309,038.4 | 5 | 7,224 | 0.321 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,975,492.0 | 2,241,302.0 | 5,519,519.0 | 1,060,860.9 | 5 | 2,352 | 0.267 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `re2_11.0.0_default-caps-simdna` | 99,410.0 | 86,101.0 | 172,411.0 | 32,161.8 | 5 | 181 | 0.324 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,556,518.0 | 1,533,998.0 | 2,107,771.0 | 224,138.4 | 5 | 3,504 | 0.144 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,101,583.0 | 2,097,941.0 | 5,316,839.0 | 1,038,276.0 | 5 | 5,048 | 0.253 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `re2_11.0.0_default-caps-simdna` | 390,452.0 | 351,712.0 | 637,673.0 | 105,476.7 | 5 | 412 | 0.270 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 26,746,265.0 | 26,524,793.0 | 40,582,489.0 | 5,505,525.8 | 5 | 129,576 | 0.206 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,956,987.0 | 4,914,106.0 | 13,947,335.0 | 3,502,982.2 | 5 | 10,072 | 0.707 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,750.0 | 12,860.0 | 104,430.0 | 35,853.7 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 481,963.0 | 444,203.0 | 1,353,538.0 | 354,485.3 | 5 | 4,776 | 0.736 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 535,623.0 | 512,362.0 | 1,453,707.0 | 368,342.7 | 5 | 2,120 | 0.688 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 8,370.0 | 6,650.0 | 93,550.0 | 34,134.1 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 577,493.0 | 549,772.0 | 1,524,608.0 | 382,707.2 | 5 | 5,592 | 0.663 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 356,872.0 | 326,452.0 | 1,172,966.0 | 331,263.9 | 5 | 1,832 | 0.928 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,950.0 | 10,661.0 | 110,390.0 | 38,796.7 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 581,604.0 | 529,112.0 | 1,572,329.0 | 402,858.0 | 5 | 3,944 | 0.693 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,116,336.0 | 1,077,986.0 | 2,153,162.0 | 415,922.6 | 5 | 6,056 | 0.373 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 48,881.0 | 39,400.0 | 163,041.0 | 46,623.4 | 5 | 29 | 0.954 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,132,926.0 | 1,100,746.0 | 2,199,912.0 | 426,384.2 | 5 | 6,104 | 0.376 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 553,763.0 | 538,793.0 | 1,075,666.0 | 208,743.1 | 5 | 6,488 | 0.377 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 95,910.0 | 73,360.0 | 217,581.0 | 53,531.5 | 5 | 53 | 0.558 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,941,141.0 | 1,890,280.0 | 2,991,426.0 | 419,073.6 | 5 | 2,984 | 0.216 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 722,034.0 | 690,133.0 | 1,169,376.0 | 184,120.4 | 5 | 2,824 | 0.255 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 20,940.0 | 17,870.0 | 119,841.0 | 39,402.4 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 689,674.0 | 650,993.0 | 1,609,699.0 | 367,167.5 | 5 | 2,312 | 0.532 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 230,191.0 | 209,781.0 | 616,253.0 | 156,871.6 | 5 | 2,088 | 0.681 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | 68,951.0 | 52,610.0 | 182,441.0 | 48,604.4 | 5 | 72 | 0.705 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,882,346.0 | 2,019,311.0 | 6,228,684.0 | 1,391,757.5 | 5 | 7,472 | 0.285 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,060,646.0 | 1,044,886.0 | 1,983,200.0 | 366,524.7 | 5 | 1,896 | 0.346 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `re2_11.0.0_default-caps-simdna` | 292,202.0 | 263,341.0 | 510,042.0 | 91,487.0 | 5 | 221 | 0.313 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10,744,178.0 | 10,695,418.0 | 22,996,804.0 | 4,905,904.1 | 5 | 31,592 | 0.457 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,433,019.0 | 5,408,519.0 | 15,046,372.0 | 3,773,380.9 | 5 | 19,608 | 0.695 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `re2_11.0.0_default-caps-simdna` | 52,791.0 | 45,620.0 | 178,821.0 | 50,715.6 | 5 | 35 | 0.961 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,997,886.0 | 2,953,216.0 | 4,302,553.0 | 521,059.8 | 5 | 9,144 | 0.174 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,219,777.0 | 1,202,407.0 | 1,841,440.0 | 249,483.6 | 5 | 4,904 | 0.205 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,540.0 | 10,910.0 | 69,620.0 | 22,498.5 | 5 | 23 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,957,031.0 | 1,849,110.0 | 3,161,057.0 | 500,712.2 | 5 | 11,160 | 0.256 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,955,150.0 | 1,898,750.0 | 3,184,487.0 | 499,313.7 | 5 | 4,936 | 0.255 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `re2_11.0.0_default-caps-simdna` | 1,130,796.0 | 1,064,665.0 | 1,449,627.0 | 140,171.9 | 5 | 859 | 0.124 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 35,551,603.0 | 35,528,062.0 | 48,413,902.0 | 5,127,046.8 | 5 | 99,944 | 0.144 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 38,635,739.0 | 38,597,088.0 | 49,429,037.0 | 4,298,439.5 | 5 | 89,624 | 0.111 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,140.0 | 15,410.0 | 78,441.0 | 24,229.8 | 5 | 20 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,185,897.0 | 1,128,406.0 | 2,450,234.0 | 505,179.9 | 5 | 6,136 | 0.426 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 699,214.0 | 655,134.0 | 1,335,447.0 | 257,618.8 | 5 | 3,496 | 0.368 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 44,070.0 | 35,240.0 | 161,391.0 | 47,890.8 | 5 | 28 | 1.087 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,088,531.0 | 2,043,191.0 | 3,356,148.0 | 508,088.0 | 5 | 4,152 | 0.243 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,667,289.0 | 1,643,208.0 | 2,893,086.0 | 487,965.5 | 5 | 4,184 | 0.293 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 15,390.0 | 10,650.0 | 38,150.0 | 10,117.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 14,050.0 | 11,900.0 | 36,490.0 | 9,184.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `tre_0.9.0_default-caps-simdna` | 13,330.0 | 11,610.0 | 49,871.0 | 14,542.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 14,830.0 | 13,010.0 | 42,730.0 | 11,225.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,660.0 | 6,080.0 | 22,090.0 | 5,955.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,050.0 | 7,350.0 | 27,210.0 | 7,437.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `tre_0.9.0_default-caps-simdna` | 14,231.0 | 12,130.0 | 40,410.0 | 10,610.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 15,590.0 | 13,420.0 | 41,630.0 | 10,685.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,130.0 | 13,680.0 | 44,040.0 | 11,215.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 20,721.0 | 15,340.0 | 43,550.0 | 10,277.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 43,440.0 | 32,010.0 | 112,240.0 | 29,750.3 | 5 | - | 0.685 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 37,391.0 | 32,390.0 | 97,540.0 | 24,756.0 | 5 | - | 0.662 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `tre_0.9.0_default-caps-simdna` | 14,090.0 | 10,990.0 | 43,891.0 | 12,314.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,990.0 | 14,670.0 | 49,440.0 | 12,829.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 16,530.0 | 14,590.0 | 48,920.0 | 13,018.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,230.0 | 7,410.0 | 23,080.0 | 5,937.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `tre_0.9.0_default-caps-simdna` | 2,030.0 | 1,520.0 | 24,030.0 | 8,792.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,690.0 | 2,910.0 | 15,820.0 | 4,899.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `tre_0.9.0_default-caps-simdna` | 17,821.0 | 15,650.0 | 68,060.0 | 19,918.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,970.0 | 17,960.0 | 71,120.0 | 20,272.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,810.0 | 36,190.0 | 86,531.0 | 18,815.0 | 5 | - | 0.440 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 39,740.0 | 38,660.0 | 118,270.0 | 30,896.5 | 5 | - | 0.777 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,320.0 | 6,600.0 | 21,540.0 | 5,683.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,490.0 | 7,560.0 | 22,900.0 | 5,808.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `tre_0.9.0_default-caps-simdna` | 54,860.0 | 42,490.0 | 95,000.0 | 19,076.6 | 5 | - | 0.348 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 46,510.0 | 43,841.0 | 98,861.0 | 20,921.0 | 5 | - | 0.450 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `tre_0.9.0_default-caps-simdna` | 17,390.0 | 7,410.0 | 26,860.0 | 7,149.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,921.0 | 8,690.0 | 40,510.0 | 12,091.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 13,620.0 | 11,270.0 | 48,181.0 | 13,997.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 18,880.0 | 12,980.0 | 48,290.0 | 12,905.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 20,550.0 | 17,390.0 | 74,420.0 | 21,727.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,500.0 | 19,710.0 | 69,561.0 | 18,679.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `tre_0.9.0_default-caps-simdna` | 9,570.0 | 8,630.0 | 28,361.0 | 7,539.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 11,240.0 | 10,050.0 | 33,610.0 | 8,996.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,290.0 | 6,520.0 | 21,940.0 | 5,859.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,320.0 | 7,360.0 | 22,500.0 | 6,479.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,921.0 | 32,740.0 | 83,230.0 | 18,564.0 | 5 | - | 0.433 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 51,100.0 | 35,121.0 | 92,951.0 | 21,065.1 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `tre_0.9.0_default-caps-simdna` | 27,471.0 | 19,670.0 | 54,140.0 | 12,515.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,790.0 | 21,151.0 | 65,000.0 | 16,557.3 | 5 | - | 0.696 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,140.0 | 14,890.0 | 54,281.0 | 14,819.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 26,550.0 | 19,690.0 | 82,601.0 | 23,396.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 47,050.0 | 44,750.0 | 125,130.0 | 30,773.9 | 5 | - | 0.654 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 50,190.0 | 46,441.0 | 128,931.0 | 31,291.4 | 5 | - | 0.623 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,970.0 | 1,540.0 | 11,441.0 | 3,785.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,531.0 | 2,860.0 | 16,620.0 | 5,265.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `tre_0.9.0_default-caps-simdna` | 12,720.0 | 8,880.0 | 31,680.0 | 8,317.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 22,760.0 | 20,050.0 | 78,881.0 | 22,414.8 | 5 | - | 0.985 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 2,100.0 | 1,510.0 | 17,770.0 | 6,287.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 3,430.0 | 2,680.0 | 14,610.0 | 4,530.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-moment-iso8601` | `plain` | `tre_0.9.0_default-caps-simdna` | 88,061.0 | 84,010.0 | 144,451.0 | 22,432.0 | 5 | - | 0.255 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 89,141.0 | 86,021.0 | 145,841.0 | 22,575.2 | 5 | - | 0.253 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `tre_0.9.0_default-caps-simdna` | 43,050.0 | 33,270.0 | 85,440.0 | 19,151.0 | 5 | - | 0.445 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 43,750.0 | 34,360.0 | 90,330.0 | 20,395.3 | 5 | - | 0.466 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `tre_0.9.0_default-caps-simdna` | 128,800.0 | 112,120.0 | 362,212.0 | 95,748.7 | 5 | - | 0.743 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 117,001.0 | 114,311.0 | 363,092.0 | 97,913.0 | 5 | - | 0.837 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `tre_0.9.0_default-caps-simdna` | 142,170.0 | 100,221.0 | 271,512.0 | 62,578.0 | 5 | - | 0.440 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 141,631.0 | 102,710.0 | 285,351.0 | 67,204.4 | 5 | - | 0.475 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-secrets-username-password-pair` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,740.0 | 5,860.0 | 23,270.0 | 6,592.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,820.0 | 6,570.0 | 23,740.0 | 6,463.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 3,770.0 | 3,130.0 | 13,830.0 | 4,061.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 5,170.0 | 4,320.0 | 15,441.0 | 4,187.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 8,630.0 | 6,910.0 | 27,600.0 | 7,777.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,960.0 | 8,370.0 | 31,350.0 | 8,666.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 26,360.0 | 23,440.0 | 71,470.0 | 18,116.9 | 5 | - | 0.687 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 34,300.0 | 27,490.0 | 72,830.0 | 16,699.4 | 5 | - | 0.487 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 42,700.0 | 36,380.0 | 85,520.0 | 18,551.5 | 5 | - | 0.434 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 42,661.0 | 38,080.0 | 85,461.0 | 17,596.8 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 11,830.0 | 9,860.0 | 33,310.0 | 9,130.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 12,020.0 | 10,600.0 | 34,540.0 | 9,116.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | 47,660.0 | 39,640.0 | 119,790.0 | 29,959.4 | 5 | - | 0.629 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 44,490.0 | 41,490.0 | 120,861.0 | 30,188.4 | 5 | - | 0.679 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `tre_0.9.0_default-caps-simdna` | 276,491.0 | 229,641.0 | 495,392.0 | 97,784.6 | 5 | - | 0.354 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 289,811.0 | 228,851.0 | 498,172.0 | 98,486.8 | 5 | - | 0.340 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `tre_0.9.0_default-caps-simdna` | 41,410.0 | 36,820.0 | 95,550.0 | 22,179.7 | 5 | - | 0.536 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 42,410.0 | 37,690.0 | 89,060.0 | 19,123.2 | 5 | - | 0.451 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `tre_0.9.0_default-caps-simdna` | 19,580.0 | 18,311.0 | 50,840.0 | 12,348.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 28,430.0 | 19,590.0 | 55,781.0 | 13,031.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,600,428.0 | 1,115,305.0 | 2,669,973.0 | 511,051.5 | 5 | - | 0.319 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 1,581,517.0 | 1,105,026.0 | 2,713,833.0 | 534,774.8 | 5 | - | 0.338 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `winpath-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 22,330.0 | 19,900.0 | 63,061.0 | 16,468.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,290.0 | 20,660.0 | 72,161.0 | 19,568.6 | 5 | - | 0.840 (max is trial 1) | compiled=5 |

