# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=capability, version=0.1, since=2026-09-22T00:00:00Z, until=2026-09-22T07:00:00Z, testee=pcrec_25b1984f_auto-caps-simdna, testee=pcrec_25b1984f_auto-nocaps-simdna, testee=pcrec_25b1984f_vm-caps-simdna, testee=pcrec_25b1984f_vm-in-caps-simdna, testee=oniguruma_6.9.10_default-caps-simdna, testee=rust_1.13.1_default-caps-simdna, testee=vectorscan_5.4.11_block-nosom-nocaps-simd
- record source: store/index.tsv (7 record(s) matching this query)
- records included: 7
- worst other-core busy: 62.5% (`pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `large-subject-throughput`)
    - `capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260922T043951Z` (store/records/capability@0.1/oniguruma_6.9.10_default-caps-simdna/capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260922T043951Z.jsonl) — agreement: agree (0 of 123 groups; 0 of 4831 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260922T021127Z` (store/records/capability@0.1/pcrec_25b1984f_auto-caps-simdna/capability@0.1__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260922T021127Z.jsonl) — agreement: agree (0 of 124 groups; 6 of 4834 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260922T024402Z` (store/records/capability@0.1/pcrec_25b1984f_auto-nocaps-simdna/capability@0.1__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260922T024402Z.jsonl) — agreement: agree (0 of 126 groups; 3 of 4912 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260922T031341Z` (store/records/capability@0.1/pcrec_25b1984f_vm-caps-simdna/capability@0.1__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260922T031341Z.jsonl) — agreement: agree (0 of 124 groups; 5 of 4829 rows; 7 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260922T035712Z` (store/records/capability@0.1/pcrec_25b1984f_vm-in-caps-simdna/capability@0.1__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260922T035712Z.jsonl) — agreement: agree (0 of 124 groups; 6 of 4829 rows; 7 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260922T051752Z` (store/records/capability@0.1/rust_1.13.1_default-caps-simdna/capability@0.1__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260922T051752Z.jsonl) — agreement: agree (0 of 82 groups; 2 of 3194 rows; 4 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260922T053300Z` (store/records/capability@0.1/vectorscan_5.4.11_block-nosom-nocaps-simd/capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260922T053300Z.jsonl) — agreement: agree (0 of 80 groups; 1 of 3118 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 7 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `balanced-parens-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_vm-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,472,646.1 | 3.9765 | 5,468,169.0 | 5,479,109.6 | 3,914.9 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5,482,139.0 | 3.9834 | 5,480,380.8 | 5,499,211.1 | 7,019.8 | 1.002x | 1.002x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5,482,899.1 | 3.9839 | 5,480,903.4 | 5,499,722.3 | 8,550.5 | 1.002x | 1.002x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,508,887.8 | 4.0028 | 5,494,534.0 | 5,519,114.0 | 9,322.4 | 1.007x | 1.007x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 4,169,638.8 | 3.9765 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,179,483.1 | 3.9859 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,179,397.8 | 3.9858 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,190,540.3 | 3.9964 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,042,507.0 | 3.9768 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,043,114.6 | 3.9792 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,040,955.0 | 3.9709 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,044,945.0 | 3.9861 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 260,855.4 | 3.9803 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 260,272.1 | 3.9714 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 260,392.7 | 3.9733 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 261,732.4 | 3.9937 |

- not ranked: `oniguruma_6.9.10_default-caps-simdna` — did-not-compile (onig_new failed (code -116): unmatched close parenthesis)

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,542.3 | 6,456.4 | 6,642.9 | 63.3 | 1.000x | 1.000x | 75 | 87.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,567.8 | 6,544.6 | 6,634.3 | 31.6 | 1.004x | 1.004x | 75 | 87.6 | 18.1 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,639.6 | 6,567.5 | 6,655.6 | 38.2 | 1.015x | 1.015x | 75 | 88.5 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,692.7 | 6,435.2 | 6,700.3 | 102.8 | 1.023x | 1.023x | 75 | 89.2 | 17.3 | 100% |

- not ranked: `oniguruma_6.9.10_default-caps-simdna` — did-not-compile (onig_new failed (code -116): unmatched close parenthesis)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.9 | 17.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.9 | 17.0 | 0.0 | 1.003x | 1.003x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 90.9 | 0.0001 | 88.5 | 96.9 | 3.0 | 5.386x | 5.386x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.0 | 0.0001 | 96.9 | 98.3 | 0.5 | 5.745x | 5.745x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.7 | 0.0001 | 167.6 | 190.3 | 9.0 | 9.933x | 9.933x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,066,746.1 | 2.9549 | 4,064,639.7 | 4,067,280.9 | 1,052.4 | 240823.714x | 240823.714x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,067,134.5 | 2.9552 | 4,065,220.7 | 4,083,106.3 | 6,728.5 | 240846.713x | 240846.713x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,096,170.6 | 2.9527 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,096,595.2 | 2.9531 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 31.1 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.2 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 774,588.7 | 2.9548 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 775,113.4 | 2.9568 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 5.7 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 32.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 194,432.7 | 2.9668 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,699.1 | 2.9709 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 548.1 | 539.9 | 553.4 | 5.4 | 1.000x | 1.000x | 75 | 7.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 551.3 | 547.2 | 556.6 | 3.4 | 1.006x | 1.006x | 75 | 7.4 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,047.1 | 2,044.4 | 2,051.7 | 2.4 | 3.735x | 3.735x | 75 | 27.3 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,222.9 | 2,199.6 | 2,266.7 | 22.1 | 4.056x | 4.056x | 75 | 29.6 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,632.6 | 5,625.5 | 5,645.1 | 6.5 | 10.277x | 10.277x | 75 | 75.1 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,704.3 | 5,697.7 | 5,710.7 | 5.1 | 10.408x | 10.408x | 75 | 76.1 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,898.6 | 7,716.4 | 8,010.1 | 103.2 | 14.411x | 14.411x | 75 | 105.3 | 58.6 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.6 | 0.0001 | 93.3 | 94.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,877,809.1 | 3.5443 | 4,876,780.5 | 4,901,432.7 | 9,474.9 | 52108.441x | 52108.441x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,879,347.9 | 3.5454 | 4,878,467.3 | 4,880,391.4 | 634.5 | 52124.879x | 52124.879x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,879,964.2 | 3.5458 | 4,878,973.0 | 4,882,740.8 | 1,366.5 | 52131.463x | 52131.463x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,881,399.6 | 3.5469 | 4,879,618.6 | 4,891,155.2 | 4,318.1 | 52146.797x | 52146.797x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,714,751.9 | 3.5427 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,715,866.6 | 3.5437 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,715,758.4 | 3.5436 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,718,477.3 | 3.5462 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 929,663.3 | 3.5464 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 929,647.9 | 3.5463 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 930,543.2 | 3.5497 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 929,715.6 | 3.5466 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 233,148.7 | 3.5576 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 233,661.7 | 3.5654 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 233,527.9 | 3.5634 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 233,796.3 | 3.5674 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,928.4 | 2,910.9 | 5,510.9 | 1,031.8 | 1.000x | 1.000x | 75 | 39.0 | 58.6 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,825.8 | 6,811.1 | 6,831.4 | 7.9 | 2.331x | 2.331x | 75 | 91.0 | 18.1 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,832.2 | 6,825.9 | 6,922.6 | 38.1 | 2.333x | 2.333x | 75 | 91.1 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,880.6 | 6,872.5 | 7,333.1 | 182.2 | 2.350x | 2.350x | 75 | 91.7 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,083.0 | 7,063.0 | 7,086.1 | 10.2 | 2.419x | 2.419x | 75 | 94.4 | 17.3 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,319.8 | 0.0882 | 121,246.2 | 122,078.0 | 310.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 608,738.6 | 0.4423 | 599,396.8 | 609,770.3 | 3,848.0 | 5.018x | 5.018x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 654,515.9 | 0.4756 | 637,681.0 | 659,744.9 | 9,127.1 | 5.395x | 5.395x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,021,147.5 | 1.4686 | 2,014,182.6 | 2,044,334.7 | 11,405.0 | 16.660x | 16.660x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,444,112.5 | 1.7759 | 2,441,280.6 | 2,447,598.9 | 2,420.8 | 20.146x | 20.146x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,421,654.5 | 3.2128 | 4,413,112.3 | 4,434,208.5 | 7,951.2 | 36.446x | 36.446x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,780,403.8 | 7.1065 | 9,608,014.9 | 10,055,338.5 | 144,106.6 | 80.617x | 80.617x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,522.2 | 0.0882 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 466,800.5 | 0.4452 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 494,449.6 | 0.4715 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,540,376.4 | 1.4690 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,861,174.2 | 1.7750 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,366,349.7 | 3.2104 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,455,539.7 | 7.1102 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,033.6 | 0.0879 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 113,300.5 | 0.4322 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 127,464.5 | 0.4862 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 378,331.3 | 1.4432 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,342.7 | 1.7713 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 842,223.4 | 3.2128 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,831,319.1 | 6.9859 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,769.4 | 0.0880 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 27,532.0 | 0.4201 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 29,848.7 | 0.4555 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 99,159.6 | 1.5131 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,639.8 | 1.7798 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 211,907.7 | 3.2335 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 463,764.4 | 7.0765 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 727.0 | 724.2 | 728.4 | 1.4 | 1.000x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 938.9 | 936.1 | 940.8 | 1.7 | 1.291x | 1.291x | 75 | 12.5 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,556.2 | 1,553.2 | 1,559.1 | 2.4 | 2.140x | 2.140x | 75 | 20.7 | 18.1 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,487.1 | 2,422.6 | 2,807.7 | 135.5 | 3.421x | 3.421x | 75 | 33.2 | 16.3 | 100% |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,499.0 | 2,487.4 | 2,506.5 | 6.3 | 3.437x | 3.437x | 75 | 33.3 | 27.2 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,768.2 | 3,764.0 | 3,768.9 | 1.8 | 5.183x | 5.183x | 75 | 50.2 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,624.6 | 5,612.9 | 5,654.0 | 15.8 | 7.736x | 7.736x | 75 | 75.0 | 58.6 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,342.4 | 0.0882 | 121,220.9 | 122,125.4 | 335.4 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 617,657.7 | 0.4488 | 600,865.3 | 623,199.4 | 7,827.2 | 5.090x | 5.090x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 638,026.8 | 0.4636 | 624,274.6 | 656,979.9 | 14,019.2 | 5.258x | 5.258x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,010,864.6 | 1.4611 | 2,000,368.9 | 2,016,501.7 | 5,451.8 | 16.572x | 16.572x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,442,938.1 | 1.7751 | 2,441,040.0 | 2,446,941.3 | 2,141.5 | 20.133x | 20.133x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,417,868.1 | 3.2101 | 4,412,434.3 | 4,430,188.4 | 6,863.7 | 36.408x | 36.408x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,673,603.1 | 7.0289 | 9,612,036.9 | 10,000,098.6 | 144,314.7 | 79.722x | 79.722x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,525.5 | 0.0882 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 463,013.7 | 0.4416 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 485,938.4 | 0.4634 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,530,807.4 | 1.4599 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,860,925.2 | 1.7747 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,361,112.8 | 3.2054 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,383,958.1 | 7.0419 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,026.6 | 0.0878 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 122,357.7 | 0.4668 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 122,900.8 | 0.4688 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 380,587.1 | 1.4518 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 464,208.7 | 1.7708 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 836,923.1 | 3.1926 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,833,823.2 | 6.9955 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,743.1 | 0.0876 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 27,942.0 | 0.4264 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 28,399.1 | 0.4333 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 97,516.9 | 1.4880 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 116,573.2 | 1.7788 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 214,606.9 | 3.2746 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 460,149.6 | 7.0213 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 726.1 | 724.9 | 727.9 | 1.1 | 1.000x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 938.3 | 930.0 | 939.8 | 3.6 | 1.292x | 1.292x | 75 | 12.5 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,557.0 | 1,555.4 | 1,560.4 | 2.0 | 2.144x | 2.144x | 75 | 20.8 | 18.1 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,492.7 | 2,483.2 | 2,494.9 | 4.2 | 3.433x | 3.433x | 75 | 33.2 | 27.2 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,519.1 | 2,486.3 | 2,558.1 | 24.2 | 3.469x | 3.469x | 75 | 33.6 | 16.3 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,768.7 | 3,768.5 | 3,771.5 | 1.1 | 5.190x | 5.190x | 75 | 50.2 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,631.7 | 5,615.5 | 5,686.1 | 24.1 | 7.756x | 7.756x | 75 | 75.1 | 58.6 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,587,640.4 | 6.9665 | 9,577,984.9 | 9,599,921.8 | 7,164.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,109,489.0 | 8.0723 | 11,086,549.7 | 11,163,811.0 | 27,342.0 | 1.159x | 1.159x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,122,427.9 | 8.0817 | 11,115,388.3 | 19,857,936.2 | 3,490,070.5 | 1.160x | 1.160x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 11,171,694.4 | 8.1175 | 11,165,609.0 | 11,253,599.9 | 37,085.4 | 1.165x | 1.165x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 11,188,283.7 | 8.1295 | 11,172,587.3 | 11,222,224.6 | 20,844.3 | 1.167x | 1.167x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,351,086.1 | 7.0105 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 8,464,754.9 | 8.0726 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 8,470,508.7 | 8.0781 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 8,507,269.5 | 8.1132 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 8,511,062.8 | 8.1168 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,803,856.8 | 6.8812 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,115,281.1 | 8.0692 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 2,118,712.9 | 8.0822 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,129,572.8 | 8.1237 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,131,838.2 | 8.1323 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 438,853.5 | 6.6964 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 528,592.2 | 8.0657 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 532,194.2 | 8.1206 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 535,042.6 | 8.1641 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 535,353.4 | 8.1688 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 5,163.3 | 5,152.4 | 5,172.1 | 6.7 | 1.000x | 1.000x | 75 | 68.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 5,165.7 | 5,152.2 | 5,176.0 | 8.9 | 1.000x | 1.000x | 75 | 68.9 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,391.0 | 12,366.8 | 12,403.7 | 12.2 | 2.400x | 2.400x | 75 | 165.2 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,581.4 | 12,556.5 | 12,735.4 | 66.0 | 2.437x | 2.437x | 75 | 167.8 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,455.3 | 17,320.4 | 17,470.2 | 62.9 | 3.381x | 3.381x | 75 | 232.7 | 58.6 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 16.0 | 0.0000 | 16.0 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.6 | 0.0000 | 30.5 | 31.2 | 0.2 | 1.909x | 1.909x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 77.1 | 0.0001 | 74.4 | 78.4 | 1.4 | 4.804x | 4.804x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.4 | 0.0001 | 94.3 | 94.6 | 0.1 | 5.885x | 5.885x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.1 | 0.0001 | 167.0 | 167.4 | 0.1 | 10.416x | 10.416x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,863,544.6 | 2.8073 | 3,861,744.3 | 3,874,043.9 | 4,537.2 | 240877.443x | 240877.443x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,865,018.4 | 2.8084 | 3,862,664.5 | 3,883,142.6 | 8,229.5 | 240969.327x | 240969.327x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 24.7 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,942,767.5 | 2.8064 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,941,781.7 | 2.8055 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 25.7 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 736,078.7 | 2.8079 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 736,544.1 | 2.8097 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 26.5 | 0.0004 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 184,941.1 | 2.8220 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 185,041.7 | 2.8235 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 489.1 | 488.9 | 491.2 | 1.1 | 1.000x | 1.000x | 75 | 6.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 868.9 | 867.8 | 869.1 | 0.5 | 1.776x | 1.776x | 75 | 11.6 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,762.4 | 1,760.8 | 1,766.6 | 2.1 | 3.603x | 3.603x | 75 | 23.5 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,868.7 | 1,866.7 | 1,869.6 | 1.2 | 3.820x | 3.820x | 75 | 24.9 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,684.7 | 5,651.2 | 5,742.5 | 39.9 | 11.622x | 11.622x | 75 | 75.8 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,109.3 | 6,093.7 | 6,132.0 | 12.4 | 12.490x | 12.490x | 75 | 81.5 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,300.1 | 6,290.7 | 6,315.1 | 9.3 | 12.880x | 12.880x | 75 | 84.0 | 17.3 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 25,345,451.8 | 18.4162 | 25,291,167.1 | 25,465,686.8 | 62,453.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 25,481,053.2 | 18.5148 | 25,418,429.3 | 25,945,580.5 | 196,450.4 | 1.005x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 25,572,780.9 | 18.5814 | 25,402,254.4 | 25,722,067.3 | 107,526.3 | 1.009x | 1.009x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 25,816,152.8 | 18.7582 | 25,412,656.6 | 26,379,028.0 | 350,588.4 | 1.019x | 1.019x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 79,438,113.2 | 57.7204 | 79,001,158.5 | 86,370,341.8 | 2,830,930.3 | 3.134x | 3.134x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 19,332,187.6 | 18.4366 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 19,448,484.2 | 18.5475 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 19,512,797.3 | 18.6089 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 19,674,277.2 | 18.7629 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 60,380,887.5 | 57.5837 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,829,215.7 | 18.4220 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,839,420.5 | 18.4609 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,858,232.5 | 18.5327 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,909,607.7 | 18.7287 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 15,207,734.2 | 58.0129 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,206,201.2 | 18.4052 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,208,257.5 | 18.4365 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,208,867.5 | 18.4459 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,207,539.8 | 18.4256 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,833,858.8 | 58.5000 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20,814.1 | 20,752.7 | 20,866.7 | 43.9 | 1.000x | 1.000x | 75 | 277.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20,851.0 | 20,811.0 | 20,900.5 | 30.1 | 1.002x | 1.002x | 75 | 278.0 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 20,908.4 | 20,752.4 | 20,959.0 | 74.8 | 1.005x | 1.005x | 75 | 278.8 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 21,036.4 | 21,015.0 | 22,650.9 | 642.0 | 1.011x | 1.011x | 75 | 280.5 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 89,442.6 | 88,879.8 | 89,518.2 | 274.5 | 4.297x | 4.297x | 75 | 1,192.6 | 58.6 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,859.6 | 1.6188 | 2,226,719.6 | 2,233,694.8 | 2,538.2 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 13,402,325.9 | 9.7383 | 13,327,524.6 | 13,482,315.2 | 50,822.8 | 6.016x | 6.016x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 13,442,181.4 | 9.7672 | 13,429,549.8 | 13,470,725.1 | 14,447.4 | 6.034x | 6.034x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 13,471,556.7 | 9.7886 | 13,438,450.1 | 13,491,588.4 | 22,391.3 | 6.047x | 6.047x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 13,480,044.6 | 9.7947 | 13,437,880.4 | 13,484,057.6 | 20,320.6 | 6.051x | 6.051x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,922.6 | 1.6183 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10,215,067.6 | 9.7418 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 10,259,583.4 | 9.7843 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 10,279,499.2 | 9.8033 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10,252,136.5 | 9.7772 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,441.4 | 1.6191 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,558,044.8 | 9.7582 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,557,962.0 | 9.7579 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 2,558,943.6 | 9.7616 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,560,483.9 | 9.7675 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,295.9 | 1.6219 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 630,101.1 | 9.6146 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 627,510.5 | 9.5751 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 630,233.9 | 9.6166 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 631,771.6 | 9.6401 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,860.1 | 8,827.0 | 8,885.5 | 20.8 | 1.000x | 1.000x | 75 | 118.1 | 58.6 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,798.9 | 10,757.5 | 10,830.7 | 29.1 | 1.219x | 1.219x | 75 | 144.0 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,856.5 | 10,841.1 | 10,877.7 | 14.5 | 1.225x | 1.225x | 75 | 144.8 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10,873.7 | 10,849.8 | 10,890.7 | 14.5 | 1.227x | 1.227x | 75 | 145.0 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,966.8 | 10,866.2 | 11,049.6 | 75.4 | 1.238x | 1.238x | 75 | 146.2 | 17.3 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 977.1 | 0.0007 | 975.1 | 980.1 | 2.0 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 980.6 | 0.0007 | 978.1 | 986.1 | 2.8 | 1.004x | 1.004x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,378.4 | 0.0010 | 1,369.3 | 1,394.1 | 8.6 | 1.411x | 1.411x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,862,999.1 | 2.8069 | 3,861,606.5 | 3,864,500.1 | 1,126.9 | 3953.352x | 3953.352x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,868,400.0 | 2.8108 | 3,863,224.7 | 3,877,286.2 | 4,750.2 | 3958.879x | 3958.879x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 229.0 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 232.4 | 0.0002 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 388.4 | 0.0004 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,941,878.8 | 2.8056 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,942,730.0 | 2.8064 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 458.1 | 0.0017 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 457.5 | 0.0017 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 555.6 | 0.0021 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 736,464.6 | 2.8094 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 737,096.6 | 2.8118 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 291.3 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 289.7 | 0.0044 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 435.0 | 0.0066 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 184,862.8 | 2.8208 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 185,505.6 | 2.8306 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,636.1 | 10,623.6 | 10,675.4 | 17.9 | 1.000x | 1.000x | 75 | 141.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,648.4 | 10,594.1 | 10,719.3 | 40.4 | 1.001x | 1.001x | 75 | 142.0 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 15,944.8 | 15,922.7 | 15,976.7 | 19.0 | 1.499x | 1.499x | 75 | 212.6 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,126.3 | 16,084.1 | 16,182.3 | 33.2 | 1.516x | 1.516x | 75 | 215.0 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 18,535.8 | 18,434.9 | 19,759.1 | 503.4 | 1.743x | 1.743x | 75 | 247.1 | 58.6 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 32.0 | 0.0000 | 30.7 | 34.3 | 1.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 47.3 | 0.0000 | 46.6 | 50.6 | 1.6 | 1.478x | 1.478x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 107.6 | 0.0001 | 107.5 | 109.5 | 0.8 | 3.365x | 3.365x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,640.1 | 0.0230 | 31,607.5 | 31,662.7 | 20.5 | 989.353x | 989.353x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,675.2 | 1.6186 | 2,225,987.2 | 2,232,628.4 | 2,381.6 | 69657.180x | 69657.180x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,480,502.2 | 3.2556 | 4,479,624.4 | 4,481,763.4 | 772.6 | 140100.831x | 140100.831x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,480,668.0 | 3.2557 | 4,477,548.2 | 4,496,453.7 | 7,099.6 | 140106.016x | 140106.016x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 11.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 16.6 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.0 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,132.3 | 0.0230 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,695,804.9 | 1.6172 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,411,319.3 | 3.2533 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,411,899.6 | 3.2538 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 15.3 | 0.0001 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 33.1 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,982.6 | 0.0228 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,340.9 | 1.6187 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 852,580.3 | 3.2523 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 852,620.4 | 3.2525 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 15.0 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.7 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,525.6 | 0.0233 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,482.6 | 1.6248 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 216,311.7 | 3.3007 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 216,148.0 | 3.2982 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 976.2 | 974.0 | 1,159.5 | 73.4 | 1.000x | 1.000x | 75 | 13.0 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,436.2 | 1,427.0 | 1,457.8 | 10.5 | 1.471x | 1.471x | 75 | 19.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,851.7 | 1,844.9 | 1,855.1 | 4.4 | 1.897x | 1.897x | 75 | 24.7 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,051.1 | 4,046.1 | 4,125.2 | 30.5 | 4.150x | 4.150x | 75 | 54.0 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,056.7 | 5,050.2 | 5,064.8 | 4.8 | 5.180x | 5.180x | 75 | 67.4 | 58.6 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 26.9 | 0.0000 | 26.8 | 27.6 | 0.4 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87.7 | 0.0001 | 87.4 | 89.7 | 0.9 | 3.254x | 3.254x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 169.8 | 0.0001 | 169.7 | 169.8 | 0.0 | 6.302x | 6.302x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,602.4 | 0.0128 | 17,577.2 | 17,698.4 | 47.3 | 653.298x | 653.298x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,280,622.2 | 3.1103 | 4,279,129.7 | 4,292,720.0 | 4,934.5 | 158871.204x | 158871.204x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,282,218.8 | 3.1115 | 4,278,908.3 | 5,075,690.9 | 317,005.8 | 158930.463x | 158930.463x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,282,437.3 | 3.1117 | 4,280,705.2 | 4,328,933.5 | 18,447.5 | 158938.572x | 158938.572x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.3 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,905.4 | 0.0018 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,252,480.2 | 3.1018 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,252,999.2 | 3.1023 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,254,164.4 | 3.1034 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.2 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0002 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 296.3 | 0.0011 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,077.5 | 3.1016 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,272.7 | 3.1024 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 812,956.8 | 3.1012 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 11.9 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 33.1 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 58.8 | 0.0009 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 15,418.5 | 0.2353 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 215,269.1 | 3.2847 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 215,021.7 | 3.2810 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 215,207.2 | 3.2838 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,487.5 | 0.0338 | 46,408.2 | 46,574.3 | 54.0 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 84,752.4 | 0.0616 | 84,650.4 | 86,197.1 | 590.5 | 1.823x | 1.823x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 292,413.5 | 0.2125 | 292,121.0 | 293,064.1 | 316.6 | 6.290x | 6.290x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 292,767.6 | 0.2127 | 292,338.9 | 293,591.6 | 433.2 | 6.298x | 6.298x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,180,108.0 | 0.8575 | 1,160,497.6 | 1,180,705.0 | 9,392.2 | 25.385x | 25.385x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,854,116.9 | 2.8004 | 3,851,653.0 | 3,871,755.6 | 8,996.0 | 82.906x | 82.906x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,856,267.9 | 2.8020 | 3,849,644.3 | 3,857,700.9 | 2,863.5 | 82.953x | 82.953x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,288.1 | 0.0337 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 64,537.4 | 0.0615 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 228,417.8 | 0.2178 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 228,602.9 | 0.2180 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 897,464.3 | 0.8559 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,935,887.1 | 2.7999 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,936,800.4 | 2.8008 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,887.5 | 0.0339 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,067.8 | 0.0613 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 52,587.1 | 0.2006 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 52,721.9 | 0.2011 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 225,869.4 | 0.8616 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 734,513.2 | 2.8019 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 735,085.1 | 2.8041 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,281.5 | 0.0348 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,110.3 | 0.0627 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 11,343.1 | 0.1731 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 11,293.6 | 0.1723 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 56,784.4 | 0.8665 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 183,766.8 | 2.8041 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 184,040.5 | 2.8082 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 838.8 | 827.7 | 871.3 | 15.8 | 1.000x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 862.5 | 826.5 | 911.3 | 29.8 | 1.028x | 1.028x | 75 | 11.5 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,417.9 | 1,411.6 | 2,790.0 | 546.3 | 1.690x | 1.690x | 75 | 18.9 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,476.4 | 2,474.0 | 2,482.9 | 3.1 | 2.952x | 2.952x | 75 | 33.0 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,169.5 | 3,164.3 | 3,183.4 | 6.4 | 3.779x | 3.779x | 75 | 42.3 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,584.0 | 4,516.0 | 4,691.5 | 71.8 | 5.465x | 5.465x | 75 | 61.1 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,716.5 | 4,591.9 | 4,907.1 | 120.5 | 5.623x | 5.623x | 75 | 62.9 | 18.1 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,790,225.4 | 1.3008 | 1,784,407.8 | 1,793,670.5 | 3,739.5 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,791,555.1 | 1.3018 | 1,785,787.9 | 1,803,832.2 | 6,142.8 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,354,984.6 | 9.7039 | 13,300,067.1 | 13,560,804.3 | 95,816.6 | 7.460x | 7.460x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18,893,460.4 | 13.7282 | 18,850,216.5 | 18,997,039.6 | 49,008.1 | 10.554x | 10.554x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 19,041,147.9 | 13.8355 | 18,944,822.7 | 19,102,654.9 | 53,339.3 | 10.636x | 10.636x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,369,750.5 | 1.3063 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,372,035.4 | 1.3085 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 10,239,198.2 | 9.7649 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 14,398,172.1 | 13.7312 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 14,530,915.5 | 13.8578 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 337,819.1 | 1.2887 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 337,642.6 | 1.2880 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,510,868.7 | 9.5782 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,595,034.7 | 13.7140 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,604,621.7 | 13.7505 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 82,527.6 | 1.2593 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 82,497.9 | 1.2588 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 604,563.9 | 9.2249 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 906,082.9 | 13.8257 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 905,058.7 | 13.8101 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,489.5 | 2,480.1 | 2,516.0 | 13.0 | 1.000x | 1.000x | 75 | 33.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,502.2 | 2,489.1 | 2,509.6 | 7.4 | 1.005x | 1.005x | 75 | 33.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 19,839.7 | 19,795.5 | 19,848.1 | 20.4 | 7.969x | 7.969x | 75 | 264.5 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,087.6 | 20,051.6 | 20,255.6 | 72.3 | 8.069x | 8.069x | 75 | 267.8 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 20,529.8 | 20,426.3 | 20,649.5 | 80.1 | 8.247x | 8.247x | 75 | 273.7 | 58.6 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,126.4 | 0.0168 | 23,119.3 | 23,139.6 | 7.6 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,142.7 | 0.0168 | 23,131.2 | 23,261.4 | 49.1 | 1.001x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,418.6 | 0.0170 | 23,385.8 | 23,493.6 | 36.2 | 1.013x | 1.013x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,370.1 | 0.0235 | 32,315.0 | 32,374.4 | 22.5 | 1.400x | 1.400x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 814,079.5 | 0.5915 | 813,773.5 | 814,700.2 | 315.9 | 35.201x | 35.201x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 814,259.1 | 0.5916 | 813,657.2 | 818,702.0 | 2,161.9 | 35.209x | 35.209x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,434.9 | 1.6199 | 2,228,640.9 | 2,230,675.0 | 739.4 | 96.402x | 96.402x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,638.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,632.5 | 0.0168 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,833.6 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,529.8 | 0.0234 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,162.1 | 0.5914 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,290.4 | 0.5916 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,682.3 | 1.6190 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,379.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,398.9 | 0.0168 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,441.0 | 0.0169 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,142.4 | 0.0234 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 155,015.7 | 0.5913 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 154,989.7 | 0.5912 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,832.0 | 1.6206 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,108.2 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,110.3 | 0.0169 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,132.2 | 0.0173 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,679.6 | 0.0256 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 38,939.2 | 0.5942 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 38,925.3 | 0.5940 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,380.5 | 1.6232 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 666.2 | 660.9 | 669.0 | 2.9 | 1.000x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 667.8 | 661.5 | 671.4 | 3.2 | 1.002x | 1.002x | 75 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,225.5 | 1,224.6 | 1,235.6 | 4.2 | 1.839x | 1.839x | 75 | 16.3 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,298.7 | 1,297.7 | 1,301.0 | 1.4 | 1.949x | 1.949x | 75 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,355.4 | 1,354.4 | 1,360.6 | 2.3 | 2.034x | 2.034x | 75 | 18.1 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,041.3 | 2,037.4 | 2,041.9 | 1.7 | 3.064x | 3.064x | 75 | 27.2 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.1 | 4,388.5 | 4,404.6 | 6.7 | 6.600x | 6.600x | 75 | 58.6 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 64,145.5 | 0.0466 | 64,104.5 | 64,366.2 | 96.7 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 483,016.9 | 0.3510 | 482,812.9 | 484,495.4 | 641.9 | 7.530x | 7.530x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 483,131.8 | 0.3510 | 482,650.4 | 485,205.8 | 924.3 | 7.532x | 7.532x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,034,266.9 | 1.4781 | 2,033,316.8 | 2,039,583.7 | 2,254.3 | 31.713x | 31.713x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,034,863.1 | 1.4785 | 2,033,935.6 | 2,039,981.9 | 2,141.6 | 31.723x | 31.723x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,035,372.3 | 1.4789 | 2,034,084.6 | 2,042,785.0 | 3,904.7 | 31.731x | 31.731x |
| 7 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,443,839.4 | 1.7757 | 2,442,960.0 | 2,455,910.1 | 4,827.8 | 38.098x | 38.098x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48,751.7 | 0.0465 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 367,983.3 | 0.3509 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 367,996.6 | 0.3509 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,549,492.0 | 1.4777 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,549,841.8 | 1.4780 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,550,220.8 | 1.4784 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,860,957.8 | 1.7747 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 12,226.6 | 0.0466 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 91,959.9 | 0.3508 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 91,995.9 | 0.3509 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 387,365.5 | 1.4777 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,571.8 | 1.4785 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 387,443.5 | 1.4780 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 465,532.5 | 1.7759 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,161.0 | 0.0482 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 23,188.2 | 0.3538 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 22,998.8 | 0.3509 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 97,294.2 | 1.4846 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,413.1 | 1.4864 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 97,305.9 | 1.4848 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 117,009.7 | 1.7854 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,113.8 | 1,110.3 | 1,121.7 | 3.9 | 1.000x | 1.000x | 75 | 14.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,137.1 | 1,123.2 | 1,140.0 | 6.0 | 1.021x | 1.021x | 75 | 15.2 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,687.7 | 2,682.4 | 2,698.6 | 5.3 | 2.413x | 2.413x | 75 | 35.8 | 27.2 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,763.8 | 2,760.1 | 2,774.6 | 6.0 | 2.481x | 2.481x | 75 | 36.9 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,864.7 | 2,863.9 | 2,869.8 | 2.4 | 2.572x | 2.572x | 75 | 38.2 | 18.1 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,197.5 | 5,193.1 | 5,229.2 | 13.5 | 4.666x | 4.666x | 75 | 69.3 | 58.6 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 17.9 | 0.0000 | 17.9 | 18.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 19.0 | 0.1 | 1.044x | 1.044x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 18.8 | 0.0000 | 18.7 | 18.8 | 0.0 | 1.047x | 1.047x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 30.6 | 0.1 | 1.695x | 1.695x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 370.6 | 0.0003 | 368.3 | 379.1 | 4.1 | 20.653x | 20.653x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,065,788.8 | 2.9542 | 4,065,030.9 | 4,067,127.2 | 716.6 | 226583.247x | 226583.247x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,067,060.2 | 2.9552 | 4,064,769.2 | 4,486,509.9 | 167,933.7 | 226654.103x | 226654.103x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 306.3 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,096,313.4 | 2.9529 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,097,980.0 | 2.9545 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 774,688.4 | 2.9552 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,360.2 | 2.9539 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.2 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 194,902.7 | 2.9740 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,720.0 | 2.9712 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 492.1 | 491.4 | 494.8 | 1.3 | 1.000x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 497.0 | 493.5 | 499.2 | 2.0 | 1.010x | 1.010x | 75 | 6.6 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 951.5 | 949.3 | 967.5 | 6.6 | 1.933x | 1.933x | 75 | 12.7 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,451.0 | 1,448.7 | 1,539.8 | 34.9 | 2.949x | 2.949x | 75 | 19.3 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,433.4 | 3,400.8 | 3,678.6 | 105.2 | 6.977x | 6.977x | 75 | 45.8 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,392.7 | 6,373.1 | 6,430.4 | 22.0 | 12.990x | 12.990x | 75 | 85.2 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,407.7 | 6,340.3 | 6,408.3 | 26.3 | 13.021x | 13.021x | 75 | 85.4 | 18.1 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 290.0 | 0.0002 | 289.0 | 291.2 | 0.8 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 354,380.0 | 0.2575 | 354,209.8 | 356,195.2 | 743.8 | 1221.809x | 1221.809x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 731,121.5 | 0.5312 | 730,127.8 | 732,968.3 | 953.3 | 2520.714x | 2520.714x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 731,389.9 | 0.5314 | 731,077.6 | 734,454.1 | 1,327.3 | 2521.640x | 2521.640x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,958,046.4 | 2.8760 | 3,939,856.7 | 4,074,975.7 | 48,561.7 | 13646.301x | 13646.301x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,181,697.9 | 3.0385 | 4,181,074.2 | 4,185,179.8 | 1,641.5 | 14417.392x | 14417.392x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,193,358.5 | 3.0469 | 4,192,499.1 | 4,199,887.3 | 2,905.5 | 14457.595x | 14457.595x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85.5 | 0.0001 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 271,202.1 | 0.2586 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 564,296.3 | 0.5382 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 564,452.2 | 0.5383 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,021,006.3 | 2.8811 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,185,191.7 | 3.0376 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,193,477.0 | 3.0455 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 122.0 | 0.0005 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 67,001.8 | 0.2556 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 135,433.8 | 0.5166 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 135,347.4 | 0.5163 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 754,859.4 | 2.8796 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 797,028.4 | 3.0404 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 799,909.4 | 3.0514 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 82.0 | 0.0013 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 16,198.2 | 0.2472 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 31,322.1 | 0.4779 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 31,320.0 | 0.4779 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 185,081.5 | 2.8241 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 199,444.3 | 3.0433 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 200,748.6 | 3.0632 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 774.4 | 771.8 | 788.4 | 7.1 | 1.000x | 1.000x | 75 | 10.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 774.5 | 772.0 | 778.0 | 2.1 | 1.000x | 1.000x | 75 | 10.3 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,612.3 | 1,608.1 | 1,629.6 | 7.5 | 2.082x | 2.082x | 75 | 21.5 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,673.1 | 2,671.4 | 2,690.1 | 7.0 | 3.452x | 3.452x | 75 | 35.6 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,040.7 | 4,031.4 | 4,102.1 | 25.4 | 5.218x | 5.218x | 75 | 53.9 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,711.7 | 4,512.7 | 4,718.6 | 78.8 | 6.085x | 6.085x | 75 | 62.8 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,744.6 | 4,713.6 | 4,769.4 | 18.8 | 6.127x | 6.127x | 75 | 63.3 | 17.3 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.0 | 0.0000 | 30.0 | 30.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 32.3 | 0.0000 | 29.9 | 32.8 | 1.2 | 1.076x | 1.076x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 98.1 | 0.0001 | 97.6 | 98.2 | 0.2 | 3.268x | 3.268x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,847,149.6 | 2.0688 | 2,845,224.3 | 2,979,077.2 | 52,985.5 | 94855.660x | 94855.660x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,855,387.8 | 2.0748 | 2,846,412.0 | 3,650,328.9 | 319,666.8 | 95130.122x | 95130.122x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,167,361.2 | 2.0670 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,168,237.9 | 2.0678 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.8 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 542,210.1 | 2.0684 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 542,625.2 | 2.0700 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 136,210.2 | 2.0784 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 136,279.4 | 2.0795 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 838.7 | 836.5 | 852.1 | 5.8 | 1.000x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 852.2 | 844.1 | 862.2 | 7.4 | 1.016x | 1.016x | 75 | 11.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,122.7 | 4,113.0 | 4,123.9 | 4.0 | 4.915x | 4.915x | 75 | 55.0 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,124.0 | 4,123.2 | 4,130.9 | 3.1 | 4.917x | 4.917x | 75 | 55.0 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,017.0 | 4,980.6 | 5,043.8 | 21.8 | 5.982x | 5.982x | 75 | 66.9 | 58.6 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.8 | 0.0000 | 18.7 | 18.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 31.6 | 0.5 | 1.615x | 1.615x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 88.2 | 0.0001 | 87.1 | 88.3 | 0.5 | 4.700x | 4.700x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.4 | 98.0 | 0.2 | 5.207x | 5.207x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 161.5 | 0.0001 | 161.4 | 161.6 | 0.1 | 8.601x | 8.601x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,658,667.7 | 2.6584 | 3,657,339.5 | 3,667,365.9 | 3,652.8 | 194875.144x | 194875.144x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,660,145.8 | 2.6595 | 3,658,800.8 | 3,671,043.0 | 4,874.4 | 194953.872x | 194953.872x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.5 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 53.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,786,079.1 | 2.6570 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,786,993.8 | 2.6579 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 29.3 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 53.4 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 697,535.5 | 2.6609 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 697,401.5 | 2.6604 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 32.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 54.5 | 0.0008 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 174,939.8 | 2.6694 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 175,132.3 | 2.6723 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 492.6 | 492.5 | 494.5 | 0.7 | 1.000x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 809.5 | 809.0 | 813.5 | 1.7 | 1.643x | 1.643x | 75 | 10.8 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,185.3 | 1,168.4 | 1,208.3 | 14.1 | 2.406x | 2.406x | 75 | 15.8 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,583.9 | 1,535.5 | 2,870.8 | 523.1 | 3.215x | 3.215x | 75 | 21.1 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,789.7 | 4,786.6 | 4,798.3 | 4.1 | 9.723x | 9.723x | 75 | 63.9 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,817.0 | 4,804.4 | 4,819.8 | 5.7 | 9.778x | 9.778x | 75 | 64.2 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,015.2 | 4,973.8 | 5,138.0 | 58.0 | 10.181x | 10.181x | 75 | 66.9 | 58.6 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,126.2 | 0.0168 | 23,120.6 | 23,164.1 | 18.5 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,146.1 | 0.0168 | 23,141.5 | 23,237.1 | 36.1 | 1.001x | 1.001x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,617.2 | 0.0230 | 31,605.1 | 31,727.3 | 44.7 | 1.367x | 1.367x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 814,127.7 | 0.5916 | 813,850.4 | 816,957.3 | 1,137.4 | 35.204x | 35.204x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 814,492.4 | 0.5918 | 814,368.7 | 814,750.9 | 144.0 | 35.219x | 35.219x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,534.7 | 1.6193 | 2,228,320.7 | 2,233,992.4 | 2,616.0 | 96.364x | 96.364x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,634.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,661.0 | 0.0168 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,116.3 | 0.0230 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,158.3 | 0.5914 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,386.1 | 0.5916 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,462.8 | 1.6188 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,388.0 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,391.5 | 0.0168 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,971.0 | 0.0228 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 154,979.5 | 0.5912 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 155,068.6 | 0.5915 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,709.1 | 1.6201 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,110.4 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,107.4 | 0.0169 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,531.0 | 0.0234 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 38,951.3 | 0.5943 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 39,037.7 | 0.5957 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,530.8 | 1.6255 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (pattern is not valid UTF-8 at byte 0: invalid utf-8 sequence of 1 bytes from index 0)

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 691.1 | 690.0 | 692.7 | 0.9 | 1.000x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 693.7 | 692.4 | 695.2 | 0.9 | 1.004x | 1.004x | 75 | 9.2 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,515.5 | 1,511.7 | 1,519.2 | 2.7 | 2.193x | 2.193x | 75 | 20.2 | 17.3 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,522.7 | 1,521.8 | 1,523.8 | 0.7 | 2.203x | 2.203x | 75 | 20.3 | 18.1 | 100% |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,040.6 | 2,030.6 | 2,046.6 | 6.3 | 2.953x | 2.953x | 75 | 27.2 | 27.2 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,428.4 | 4,425.4 | 4,431.7 | 2.6 | 6.408x | 6.408x | 75 | 59.0 | 58.6 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (pattern is not valid UTF-8 at byte 0: invalid utf-8 sequence of 1 bytes from index 0)

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,979.2 | 1.0892 | 1,498,327.4 | 1,504,367.1 | 2,254.5 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,798,115.1 | 5.6662 | 7,783,975.9 | 7,803,702.5 | 6,655.4 | 5.202x | 5.202x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,799,381.6 | 5.6671 | 7,791,508.6 | 7,810,334.6 | 7,263.6 | 5.203x | 5.203x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,799,560.3 | 5.6672 | 7,793,502.0 | 7,834,353.9 | 18,166.8 | 5.203x | 5.203x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,808,166.4 | 5.6735 | 7,803,400.8 | 7,827,125.7 | 8,273.9 | 5.209x | 5.209x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,586.2 | 1.0887 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,942,368.2 | 5.6671 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 5,945,211.6 | 5.6698 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 5,942,685.3 | 5.6674 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5,948,393.6 | 5.6728 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,387.1 | 1.0887 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,484,907.5 | 5.6645 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,483,111.1 | 5.6576 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,485,042.5 | 5.6650 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,486,515.4 | 5.6706 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,727.1 | 1.0945 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 372,200.9 | 5.6793 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 371,336.8 | 5.6662 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 372,272.5 | 5.6804 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 371,623.6 | 5.6705 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,456.3 | 4,450.2 | 4,462.2 | 4.2 | 1.000x | 1.000x | 75 | 59.4 | 58.6 | 100% |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,066.4 | 9,050.5 | 9,080.6 | 9.8 | 2.035x | 2.035x | 75 | 120.9 | 17.3 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,282.1 | 9,270.5 | 9,326.5 | 20.9 | 2.083x | 2.083x | 75 | 123.8 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 9,289.8 | 9,270.4 | 9,300.2 | 10.6 | 2.085x | 2.085x | 75 | 123.9 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 9,295.3 | 9,286.5 | 9,338.2 | 18.5 | 2.086x | 2.086x | 75 | 123.9 | 8.9 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 27.6 | 0.0000 | 27.5 | 29.5 | 0.8 | 1.820x | 1.820x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 85.3 | 0.0001 | 85.1 | 85.5 | 0.1 | 5.618x | 5.618x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.4 | 0.0001 | 93.7 | 94.6 | 0.3 | 6.218x | 6.218x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.8 | 167.1 | 0.1 | 10.987x | 10.987x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,066,506.8 | 2.9548 | 4,064,375.1 | 4,206,374.5 | 55,036.2 | 267758.459x | 267758.459x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,082,929.6 | 2.9667 | 4,071,528.7 | 4,121,362.6 | 18,022.7 | 268839.815x | 268839.815x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.4 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,096,396.6 | 2.9530 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,110,636.4 | 2.9665 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 28.9 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 774,986.3 | 2.9563 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 775,177.8 | 2.9571 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 9.3 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.0 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0009 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 194,130.2 | 2.9622 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 198,121.0 | 3.0231 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 470.2 | 469.3 | 471.4 | 0.8 | 1.000x | 1.000x | spread | 75 | 6.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 846.0 | 834.4 | 849.8 | 5.5 | 1.799x | 1.799x | spread | 75 | 11.3 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,959.8 | 1,958.3 | 1,969.4 | 4.0 | 4.168x | 4.168x | spread | 75 | 26.1 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,665.6 | 2,639.6 | 2,675.4 | 12.0 | 5.669x | 5.669x | spread | 75 | 35.5 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,235,076.7 | 9,231,578.0 | 9,239,957.9 | 3,195.9 | 19641.162x | 19641.162x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 123,134.4 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,239,556.0 | 9,233,647.1 | 9,249,927.7 | 5,461.9 | 19650.689x | 19650.689x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 123,194.1 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,552,668.2 | 12,545,052.4 | 12,565,660.4 | 8,446.4 | 26697.016x | 26697.016x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 167,368.9 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.1 | 0.0000 | 15.1 | 15.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.4 | 28.6 | 0.1 | 1.883x | 1.883x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87.7 | 0.0001 | 83.9 | 90.4 | 2.2 | 5.801x | 5.801x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 93.3 | 101.6 | 3.1 | 6.229x | 6.229x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.8 | 169.5 | 1.0 | 11.042x | 11.042x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,863,456.4 | 2.8072 | 3,861,847.1 | 3,875,377.9 | 4,927.8 | 255532.581x | 255532.581x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,866,151.7 | 2.8092 | 3,862,585.3 | 3,885,593.4 | 8,369.2 | 255710.854x | 255710.854x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.6 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,941,709.2 | 2.8054 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,942,374.8 | 2.8061 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 30.1 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 736,126.0 | 2.8081 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 736,383.7 | 2.8091 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 30.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 185,320.4 | 2.8278 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 185,208.7 | 2.8261 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 480.3 | 479.2 | 483.4 | 1.4 | 1.000x | 1.000x | spread | 75 | 6.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 894.7 | 893.3 | 903.9 | 3.9 | 1.863x | 1.863x | spread | 75 | 11.9 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,985.9 | 1,980.8 | 1,990.7 | 3.5 | 4.134x | 4.134x | spread | 75 | 26.5 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,960.4 | 2,956.7 | 2,971.5 | 5.1 | 6.163x | 6.163x | spread | 75 | 39.5 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,972,479.2 | 9,964,862.0 | 9,980,881.6 | 5,575.9 | 20760.993x | 20760.993x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 132,966.4 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,990,745.8 | 9,968,266.3 | 10,001,669.0 | 12,721.8 | 20799.021x | 20799.021x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 133,209.9 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 16,695,116.2 | 16,657,091.7 | 16,738,362.5 | 27,458.3 | 34756.372x | 34756.372x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 222,601.5 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,585,253.9 | 4.7849 | 6,558,512.8 | 6,869,189.0 | 117,809.4 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,964,412.4 | 5.0604 | 6,586,534.9 | 7,433,783.1 | 376,767.6 | 1.058x | 1.058x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,467,667.0 | 5.4261 | 7,183,652.0 | 7,658,019.5 | 156,916.3 | 1.134x | 1.134x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,529,083.8 | 5.4707 | 7,347,358.5 | 7,757,747.4 | 159,024.0 | 1.143x | 1.143x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 14,493,362.5 | 10.5310 | 14,449,045.9 | 15,799,347.2 | 526,473.4 | 2.201x | 2.201x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,022,974.1 | 4.7903 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 5,389,178.3 | 5.1395 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 5,758,652.3 | 5.4919 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5,911,212.8 | 5.6374 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 11,112,525.9 | 10.5977 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,250,547.1 | 4.7705 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,264,960.7 | 4.8254 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,393,301.1 | 5.3150 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,329,793.4 | 5.0728 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,720,979.8 | 10.3797 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 309,416.2 | 4.7213 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 309,478.3 | 4.7223 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 313,438.2 | 4.7827 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 316,014.3 | 4.8220 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 659,856.8 | 10.0686 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_vm-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,405.2 | 7,172.9 | 7,725.0 | 177.8 | 1.000x | 1.000x | 75 | 98.7 | 18.1 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,445.5 | 7,071.1 | 7,688.4 | 242.8 | 1.005x | 1.005x | 75 | 99.3 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,595.9 | 7,516.5 | 7,634.3 | 41.6 | 1.026x | 1.026x | 75 | 101.3 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,788.2 | 7,601.4 | 7,901.0 | 96.7 | 1.052x | 1.052x | 75 | 103.8 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,881.3 | 22,736.6 | 23,046.3 | 109.2 | 3.090x | 3.090x | 75 | 305.1 | 58.6 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 221.7 | 0.0002 | 220.4 | 222.8 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 222.4 | 0.0002 | 221.0 | 224.4 | 1.2 | 1.003x | 1.003x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,054.8 | 0.0029 | 4,043.8 | 4,097.6 | 18.7 | 18.286x | 18.286x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,680,031.3 | 2.6739 | 3,676,830.1 | 3,692,190.6 | 5,305.4 | 16595.664x | 16595.664x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,681,397.9 | 2.6749 | 3,678,068.2 | 3,690,419.8 | 4,440.3 | 16601.827x | 16601.827x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 57.6 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 57.6 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 577.3 | 0.0006 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,801,301.5 | 2.6715 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,802,400.1 | 2.6726 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 95.0 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 96.2 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,843.2 | 0.0070 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 701,198.1 | 2.6749 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 702,307.4 | 2.6791 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 69.0 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 68.4 | 0.0010 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,636.4 | 0.0250 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 176,533.4 | 2.6937 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 176,527.3 | 2.6936 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12,382.6 | 12,349.8 | 12,721.9 | 141.5 | 1.000x | 1.000x | 75 | 165.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12,384.2 | 12,340.6 | 12,761.4 | 178.2 | 1.000x | 1.000x | 75 | 165.1 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 14,461.9 | 14,439.9 | 14,606.8 | 62.5 | 1.168x | 1.168x | 75 | 192.8 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 14,719.7 | 14,714.0 | 14,780.9 | 24.7 | 1.189x | 1.189x | 75 | 196.3 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 36,373.3 | 36,110.2 | 36,524.2 | 183.4 | 2.937x | 2.937x | 75 | 485.0 | 58.6 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,862,308.4 | 2.8064 | 3,831,481.4 | 3,875,638.2 | 17,953.9 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 9,931,912.1 | 7.2166 | 9,838,742.9 | 9,945,276.9 | 39,352.9 | 2.571x | 2.571x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 10,078,110.5 | 7.3228 | 10,056,458.2 | 10,082,479.0 | 10,872.2 | 2.609x | 2.609x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,120,410.9 | 7.3536 | 10,085,434.0 | 10,130,804.3 | 16,369.8 | 2.620x | 2.620x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 10,153,359.1 | 7.3775 | 10,111,303.3 | 10,180,988.1 | 25,543.8 | 2.629x | 2.629x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,957,280.7 | 2.8203 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 7,569,158.1 | 7.2185 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 7,713,180.5 | 7.3559 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,707,993.9 | 7.3509 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,739,731.3 | 7.3812 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 719,753.1 | 2.7456 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,879,699.9 | 7.1705 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,887,445.9 | 7.2000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,922,931.6 | 7.3354 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,932,471.4 | 7.3718 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 182,077.9 | 2.7783 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 471,637.7 | 7.1966 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 463,496.9 | 7.0724 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 480,213.4 | 7.3275 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 481,420.1 | 7.3459 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,091.1 | 7,073.6 | 7,425.5 | 133.3 | 1.000x | 1.000x | 75 | 94.5 | 58.6 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 11,296.6 | 11,131.5 | 11,417.8 | 91.8 | 1.593x | 1.593x | 75 | 150.6 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,328.2 | 11,266.6 | 11,425.8 | 54.9 | 1.598x | 1.598x | 75 | 151.0 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 11,349.6 | 11,307.7 | 11,416.7 | 36.4 | 1.601x | 1.601x | 75 | 151.3 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,583.5 | 11,581.6 | 11,595.3 | 5.0 | 1.634x | 1.634x | 75 | 154.4 | 17.3 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,245.7 | 0.0009 | 1,243.0 | 1,249.2 | 2.0 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 60,481.8 | 0.0439 | 60,380.8 | 60,620.4 | 81.1 | 48.553x | 48.553x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 393,757.0 | 0.2861 | 393,634.1 | 394,677.0 | 388.2 | 316.097x | 316.097x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 393,998.2 | 0.2863 | 393,390.0 | 395,859.5 | 926.3 | 316.291x | 316.291x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,361,334.6 | 0.9892 | 1,358,939.9 | 1,364,817.5 | 1,944.5 | 1092.841x | 1092.841x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,067,713.3 | 2.9556 | 4,061,103.2 | 4,069,292.5 | 3,298.7 | 3265.445x | 3265.445x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,068,366.3 | 2.9561 | 4,055,235.6 | 4,180,683.4 | 46,056.3 | 3265.969x | 3265.969x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.7 | 0.0001 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 46,187.0 | 0.0440 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 302,132.5 | 0.2881 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 302,029.9 | 0.2880 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,039,498.9 | 0.9913 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,101,795.8 | 2.9581 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,102,213.3 | 2.9585 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 634.1 | 0.0024 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 11,503.6 | 0.0439 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 74,477.9 | 0.2841 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 74,683.0 | 0.2849 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 259,361.4 | 0.9894 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 773,625.2 | 2.9511 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 773,319.4 | 2.9500 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 527.1 | 0.0080 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,726.0 | 0.0416 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 17,172.3 | 0.2620 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,047.9 | 0.2601 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 62,488.1 | 0.9535 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 192,560.1 | 2.9382 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 192,383.7 | 2.9355 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 783.4 | 772.6 | 788.8 | 6.8 | 1.000x | 1.000x | 75 | 10.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 785.1 | 779.1 | 791.7 | 4.7 | 1.002x | 1.002x | 75 | 10.5 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,308.9 | 1,308.3 | 1,311.8 | 1.4 | 1.671x | 1.671x | 75 | 17.5 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,306.1 | 2,301.2 | 2,308.4 | 2.6 | 2.944x | 2.944x | 75 | 30.7 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,811.8 | 2,803.9 | 2,836.1 | 14.3 | 3.589x | 3.589x | 75 | 37.5 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,594.7 | 4,499.0 | 4,638.1 | 47.2 | 5.865x | 5.865x | 75 | 61.3 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,616.2 | 4,336.9 | 4,693.2 | 124.7 | 5.893x | 5.893x | 75 | 61.5 | 18.1 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,161.7 | 1.6197 | 2,228,885.5 | 2,237,374.3 | 3,263.6 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,488,622.5 | 3.2615 | 4,486,491.8 | 4,508,993.1 | 8,230.0 | 2.014x | 2.014x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,497,628.2 | 3.2680 | 4,489,328.2 | 4,509,418.3 | 6,848.0 | 2.018x | 2.018x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,507,247.6 | 3.2750 | 4,488,540.4 | 4,522,118.2 | 13,560.9 | 2.022x | 2.022x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,685,352.5 | 3.4044 | 4,678,392.6 | 4,709,871.0 | 11,062.8 | 2.102x | 2.102x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,806.1 | 1.6192 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,412,267.5 | 3.2542 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,412,122.1 | 3.2541 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,412,157.1 | 3.2541 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,567,862.1 | 3.4026 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,841.9 | 1.6206 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 853,121.9 | 3.2544 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 855,731.3 | 3.2644 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 854,854.4 | 3.2610 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 891,743.6 | 3.4017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,469.9 | 1.6246 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 222,320.6 | 3.3923 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 225,043.5 | 3.4339 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 224,872.6 | 3.4313 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 224,070.0 | 3.4190 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,577.8 | 6,537.9 | 6,582.7 | 16.5 | 1.000x | 1.000x | 75 | 87.7 | 58.6 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,958.2 | 6,889.3 | 7,020.3 | 43.8 | 1.058x | 1.058x | 75 | 92.8 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,057.8 | 6,881.3 | 7,108.1 | 94.5 | 1.073x | 1.073x | 75 | 94.1 | 17.3 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,294.8 | 7,116.3 | 7,300.5 | 70.8 | 1.109x | 1.109x | 75 | 97.3 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,330.5 | 6,993.7 | 7,700.2 | 224.7 | 1.114x | 1.114x | 75 | 97.7 | 8.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,888.6 | 1.6188 | 2,226,140.9 | 2,232,832.8 | 2,309.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,638,824.0 | 3.3706 | 4,634,493.6 | 4,652,236.4 | 6,209.0 | 2.082x | 2.082x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,647,427.0 | 3.3769 | 4,636,410.9 | 4,667,888.2 | 12,313.8 | 2.086x | 2.086x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,651,273.7 | 3.3797 | 4,641,930.9 | 4,653,062.5 | 3,994.7 | 2.088x | 2.088x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,651,655.4 | 3.3799 | 4,649,071.6 | 4,651,924.2 | 1,057.0 | 2.088x | 2.088x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,306.9 | 1.6187 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,533,020.6 | 3.3694 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,540,005.8 | 3.3760 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,541,923.6 | 3.3778 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,541,334.5 | 3.3773 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,328.5 | 1.6187 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 882,670.6 | 3.3671 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 885,843.5 | 3.3792 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 887,193.9 | 3.3844 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 887,158.2 | 3.3842 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,260.5 | 1.6214 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 222,724.8 | 3.3985 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 221,772.1 | 3.3840 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 222,848.2 | 3.4004 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 222,648.8 | 3.3974 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_vm-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,964.3 | 5,958.0 | 6,040.0 | 33.5 | 1.000x | 1.000x | 75 | 79.5 | 18.1 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,995.4 | 5,972.6 | 6,070.4 | 36.6 | 1.005x | 1.005x | 75 | 79.9 | 58.6 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 6,016.8 | 5,967.7 | 6,044.9 | 27.8 | 1.009x | 1.009x | 75 | 80.2 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 6,111.8 | 6,102.1 | 6,303.8 | 76.8 | 1.025x | 1.025x | 75 | 81.5 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,274.4 | 6,264.3 | 6,303.5 | 14.7 | 1.052x | 1.052x | 75 | 83.7 | 17.3 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.2 | 0.1 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82.9 | 0.0001 | 79.8 | 95.8 | 5.6 | 5.463x | 5.463x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.8 | 0.0001 | 166.8 | 166.9 | 0.0 | 10.993x | 10.993x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 735.8 | 0.0005 | 732.2 | 757.0 | 9.0 | 48.487x | 48.487x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,253,228.8 | 2.3638 | 3,251,726.5 | 3,313,982.3 | 24,434.3 | 214365.411x | 214365.411x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,254,602.8 | 2.3648 | 3,252,430.8 | 3,266,471.9 | 5,145.2 | 214455.949x | 214455.949x |
| 7 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,258,460.6 | 2.3676 | 3,252,489.3 | 3,269,311.5 | 6,507.6 | 214710.156x | 214710.156x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.0 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 245.8 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,477,727.1 | 2.3629 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,476,999.7 | 2.3623 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 2,477,093.3 | 2.3623 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 27.6 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0002 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 244.3 | 0.0009 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 620,185.4 | 2.3658 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,089.5 | 2.3655 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 620,574.2 | 2.3673 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 29.1 | 0.0004 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 245.6 | 0.0037 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 155,825.5 | 2.3777 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 155,933.0 | 2.3793 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 155,908.8 | 2.3790 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 427.4 | 426.9 | 429.3 | 0.9 | 1.000x | 1.000x | spread | 75 | 5.7 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,863.0 | 1,861.8 | 1,867.5 | 2.1 | 4.359x | 4.359x | spread | 75 | 24.8 | 27.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,989.9 | 1,988.3 | 2,009.0 | 7.7 | 4.656x | 4.656x | spread | 75 | 26.5 | 16.3 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 8,959,572.2 | 8,956,901.5 | 8,962,881.2 | 2,108.3 | 20964.898x | 20964.898x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,461.0 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 8,960,666.2 | 8,955,200.5 | 8,970,953.1 | 5,555.2 | 20967.458x | 20967.458x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,475.5 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,013,059.6 | 9,001,706.6 | 9,026,871.5 | 8,372.1 | 21090.056x | 21090.056x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 120,174.1 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,555,980.4 | 12,530,611.8 | 12,959,519.9 | 165,417.0 | 29380.293x | 29380.293x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 167,413.1 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 480,709.1 | 0.3493 | 479,349.3 | 484,011.7 | 2,027.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 481,273.2 | 0.3497 | 479,545.4 | 481,896.3 | 822.7 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,035,281.9 | 1.4789 | 2,034,924.1 | 2,036,091.1 | 448.1 | 4.234x | 4.234x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,661,486.2 | 2.6605 | 3,661,451.2 | 3,704,382.7 | 17,001.9 | 7.617x | 7.617x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,664,116.9 | 2.6624 | 3,660,867.2 | 3,688,366.8 | 10,121.8 | 7.622x | 7.622x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 366,757.3 | 0.3498 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 366,841.9 | 0.3498 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,550,114.5 | 1.4783 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,788,363.2 | 2.6592 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,790,961.1 | 2.6617 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 91,439.3 | 0.3488 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 91,154.1 | 0.3477 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,710.7 | 1.4790 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 698,257.6 | 2.6636 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 697,988.2 | 2.6626 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 22,543.2 | 0.3440 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 22,634.3 | 0.3454 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,411.2 | 1.4864 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 175,282.0 | 2.6746 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 175,557.6 | 2.6788 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,250.3 | 1,245.8 | 1,258.6 | 4.4 | 1.000x | 1.000x | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,258.6 | 1,251.3 | 1,266.5 | 5.9 | 1.007x | 1.007x | 75 | 16.8 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,932.4 | 4,921.0 | 5,203.4 | 108.9 | 3.945x | 3.945x | 75 | 65.8 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,946.4 | 4,938.4 | 4,952.7 | 5.2 | 3.956x | 3.956x | 75 | 66.0 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,036.0 | 5,027.4 | 5,347.4 | 125.8 | 4.028x | 4.028x | 75 | 67.1 | 17.3 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.3 | 0.0000 | 18.1 | 18.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.9 | 0.0000 | 19.9 | 22.5 | 1.0 | 1.087x | 1.087x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 19.9 | 0.0000 | 19.9 | 20.1 | 0.1 | 1.088x | 1.088x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.3 | 0.0000 | 30.2 | 30.4 | 0.1 | 1.654x | 1.654x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.3 | 0.0001 | 93.0 | 117.7 | 9.8 | 5.094x | 5.094x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,444,993.8 | 1.7766 | 2,438,895.2 | 3,116,162.5 | 262,175.0 | 133466.521x | 133466.521x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,766,890.8 | 2.0104 | 2,439,442.4 | 3,168,940.6 | 271,091.5 | 151038.126x | 151038.126x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,857,817.6 | 1.7718 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,185,287.3 | 2.0841 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.1 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 464,944.6 | 1.7736 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 465,009.5 | 1.7739 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 8.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 8.0 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.1 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 116,699.8 | 1.7807 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 117,049.3 | 1.7860 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 562.0 | 561.5 | 566.9 | 2.0 | 1.000x | 1.000x | 75 | 7.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 565.5 | 563.7 | 566.4 | 0.9 | 1.006x | 1.006x | 75 | 7.5 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 573.7 | 571.4 | 588.3 | 6.5 | 1.021x | 1.021x | 75 | 7.6 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 696.2 | 695.9 | 697.0 | 0.4 | 1.239x | 1.239x | 75 | 9.3 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,792.1 | 2,782.6 | 2,822.2 | 14.4 | 4.969x | 4.969x | 75 | 37.2 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,452.8 | 3,986.7 | 4,613.5 | 271.4 | 7.924x | 7.924x | 75 | 59.4 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,757.9 | 4,636.0 | 4,950.2 | 113.7 | 8.467x | 8.467x | 75 | 63.4 | 17.3 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 124.3 | 0.0001 | 123.8 | 130.7 | 2.7 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 263,616.4 | 0.1915 | 263,532.4 | 264,374.9 | 347.8 | 2120.612x | 2120.612x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 263,784.5 | 0.1917 | 263,426.9 | 264,584.2 | 393.6 | 2121.964x | 2121.964x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 306,970.7 | 0.2230 | 306,464.2 | 308,042.2 | 543.7 | 2469.367x | 2469.367x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 955,686.2 | 0.6944 | 954,424.4 | 957,966.8 | 1,245.2 | 7687.834x | 7687.834x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 957,768.1 | 0.6959 | 954,391.8 | 962,933.8 | 2,954.9 | 7704.581x | 7704.581x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,992,314.9 | 2.9009 | 3,955,276.5 | 4,064,531.5 | 35,968.9 | 32115.411x | 32115.411x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 43.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 202,588.1 | 0.1932 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 202,735.2 | 0.1933 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 236,202.4 | 0.2253 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 727,433.6 | 0.6937 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 729,416.1 | 0.6956 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,048,098.6 | 2.9069 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 41.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 48,668.2 | 0.1857 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 48,580.9 | 0.1853 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 56,698.9 | 0.2163 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 181,110.6 | 0.6909 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 181,811.5 | 0.6936 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 751,354.8 | 2.8662 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 39.2 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 12,397.4 | 0.1892 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 12,360.4 | 0.1886 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 14,049.7 | 0.2144 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 46,697.5 | 0.7125 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 46,023.3 | 0.7023 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 192,865.8 | 2.9429 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 684.3 | 682.0 | 710.4 | 12.7 | 1.000x | 1.000x | 75 | 9.1 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 690.9 | 686.3 | 710.2 | 8.5 | 1.010x | 1.010x | 75 | 9.2 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,274.6 | 1,269.8 | 1,277.8 | 2.9 | 1.863x | 1.863x | 75 | 17.0 | 17.3 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,331.7 | 1,329.2 | 1,379.3 | 19.4 | 1.946x | 1.946x | 75 | 17.8 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,333.8 | 1,332.7 | 1,334.5 | 0.7 | 1.949x | 1.949x | 75 | 17.8 | 18.1 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,072.3 | 2,069.5 | 2,117.8 | 18.4 | 3.028x | 3.028x | 75 | 27.6 | 27.2 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,650.1 | 4,644.1 | 5,196.3 | 217.8 | 6.795x | 6.795x | 75 | 62.0 | 58.6 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 182,624.7 | 0.1327 | 182,331.9 | 183,474.5 | 401.1 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,513.8 | 0.2038 | 280,406.5 | 281,500.3 | 404.2 | 1.536x | 1.536x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,196,460.1 | 3.0492 | 4,194,829.0 | 4,209,404.5 | 5,389.3 | 22.979x | 22.979x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,197,409.4 | 3.0499 | 4,194,036.7 | 4,209,203.6 | 5,226.6 | 22.984x | 22.984x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,715,051.6 | 3.4260 | 4,704,741.4 | 4,739,417.0 | 13,122.9 | 25.818x | 25.818x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,722,881.9 | 3.4317 | 4,704,439.6 | 4,756,574.4 | 17,705.5 | 25.861x | 25.861x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,564,899.2 | 4.7701 | 6,550,284.1 | 6,601,302.4 | 17,917.1 | 35.947x | 35.947x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 140,387.4 | 0.1339 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,610.5 | 0.2037 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,198,802.5 | 3.0506 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,197,408.9 | 3.0493 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,588,428.0 | 3.4222 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,588,882.8 | 3.4226 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 4,986,305.4 | 4.7553 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 33,851.5 | 0.1291 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,442.7 | 0.2039 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 799,810.8 | 3.0510 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 800,746.8 | 3.0546 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 902,832.7 | 3.4440 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 904,638.9 | 3.4509 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,257,248.7 | 4.7960 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 8,375.5 | 0.1278 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,453.7 | 0.2053 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 198,254.2 | 3.0251 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 198,041.0 | 3.0219 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 228,263.7 | 3.4830 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 228,816.3 | 3.4915 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 318,970.5 | 4.8671 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,449.4 | 2,447.1 | 2,459.5 | 4.7 | 1.000x | 1.000x | 75 | 32.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,450.7 | 2,445.5 | 2,453.9 | 2.8 | 1.001x | 1.001x | 75 | 32.7 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,008.8 | 3,001.4 | 3,016.8 | 5.1 | 1.228x | 1.228x | 75 | 40.1 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,069.1 | 3,043.7 | 3,109.9 | 22.2 | 1.253x | 1.253x | 75 | 40.9 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,349.3 | 3,327.8 | 3,370.5 | 15.9 | 1.367x | 1.367x | 75 | 44.7 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,422.2 | 3,348.2 | 3,439.2 | 34.5 | 1.397x | 1.397x | 75 | 45.6 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,458.7 | 13,309.2 | 13,677.5 | 134.1 | 5.495x | 5.495x | 75 | 179.4 | 58.6 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,447,555.9 | 1.7784 | 2,442,009.9 | 2,451,745.9 | 3,214.4 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,458,707.3 | 1.7865 | 2,448,152.9 | 2,471,229.0 | 7,452.7 | 1.005x | 1.005x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,931,234.3 | 7.2161 | 9,878,941.8 | 10,087,013.9 | 79,774.4 | 4.058x | 4.058x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 10,082,199.6 | 7.3258 | 10,017,807.3 | 10,559,761.1 | 203,033.0 | 4.119x | 4.119x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 10,598,387.1 | 7.7009 | 10,571,054.0 | 10,605,601.8 | 12,048.1 | 4.330x | 4.330x |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,343,632.8 | 16.9617 | 23,270,124.9 | 24,111,968.0 | 321,674.8 | 9.538x | 9.538x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,874,153.7 | 1.7873 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,886,988.3 | 1.7996 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,602,963.4 | 7.2508 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,642,969.1 | 7.2889 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 8,112,216.6 | 7.7364 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 17,905,951.1 | 17.0764 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 456,973.9 | 1.7432 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 457,076.0 | 1.7436 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,882,265.5 | 7.1803 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,916,223.8 | 7.3098 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 1,995,749.4 | 7.6132 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,462,895.6 | 17.0246 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 113,853.7 | 1.7373 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 114,643.0 | 1.7493 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 467,652.6 | 7.1358 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 474,708.3 | 7.2435 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 488,512.7 | 7.4541 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,056,250.8 | 16.1171 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,415.6 | 1,397.2 | 1,430.3 | 10.7 | 1.000x | 1.000x | 75 | 18.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,417.6 | 1,402.5 | 1,421.1 | 6.6 | 1.001x | 1.001x | 75 | 18.9 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,344.4 | 7,332.0 | 7,952.9 | 240.5 | 5.188x | 5.188x | 75 | 97.9 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,428.0 | 7,417.7 | 7,442.9 | 8.5 | 5.247x | 5.247x | 75 | 99.0 | 17.3 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 11,660.4 | 11,637.4 | 12,698.7 | 410.5 | 8.237x | 8.237x | 75 | 155.5 | 16.3 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,704.6 | 11,657.2 | 11,843.2 | 65.6 | 8.268x | 8.268x | 75 | 156.1 | 58.6 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,122.0 | 0.0168 | 23,106.8 | 23,215.1 | 38.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,134.0 | 0.0168 | 23,113.0 | 23,301.2 | 71.1 | 1.001x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,421.4 | 0.0170 | 23,404.0 | 23,481.3 | 28.6 | 1.013x | 1.013x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,318.3 | 0.0235 | 32,253.0 | 32,628.7 | 133.3 | 1.398x | 1.398x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 813,573.8 | 0.5912 | 813,385.4 | 817,387.5 | 1,693.2 | 35.186x | 35.186x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 814,864.4 | 0.5921 | 814,499.6 | 824,237.2 | 3,754.5 | 35.242x | 35.242x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,339.1 | 1.6191 | 2,227,187.0 | 2,232,898.5 | 1,964.9 | 96.373x | 96.373x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,636.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,642.4 | 0.0168 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,836.0 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,508.9 | 0.0234 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 619,702.7 | 0.5910 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,688.9 | 0.5919 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,443.9 | 1.6188 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,377.8 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,386.7 | 0.0167 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,446.3 | 0.0170 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,148.7 | 0.0235 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 155,046.4 | 0.5915 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 155,112.3 | 0.5917 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,795.7 | 1.6205 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,107.7 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,106.3 | 0.0169 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,132.2 | 0.0173 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,678.4 | 0.0256 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 38,945.8 | 0.5943 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 38,935.0 | 0.5941 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,488.6 | 1.6249 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 662.7 | 661.8 | 691.9 | 11.5 | 1.000x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 665.3 | 661.7 | 688.0 | 11.7 | 1.004x | 1.004x | 75 | 8.9 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,226.6 | 1,225.3 | 1,227.0 | 0.6 | 1.851x | 1.851x | 75 | 16.4 | 16.3 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,309.0 | 1,295.5 | 1,311.5 | 6.4 | 1.975x | 1.975x | 75 | 17.5 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,356.2 | 1,354.8 | 1,360.3 | 1.9 | 2.046x | 2.046x | 75 | 18.1 | 18.1 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,042.7 | 2,040.4 | 2,063.1 | 8.7 | 3.082x | 3.082x | 75 | 27.2 | 27.2 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,388.9 | 4,383.7 | 4,456.4 | 27.3 | 6.623x | 6.623x | 75 | 58.5 | 58.6 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,160.6 | 0.0168 | 23,135.6 | 23,367.1 | 85.5 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,169.4 | 0.0168 | 23,095.6 | 23,266.0 | 61.1 | 1.000x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 23,568.9 | 0.0171 | 23,566.0 | 23,840.4 | 106.2 | 1.018x | 1.018x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,545.0 | 1.6193 | 2,227,478.4 | 2,228,998.0 | 513.2 | 96.221x | 96.221x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,915,587.6 | 2.8451 | 3,913,653.0 | 3,931,553.7 | 6,608.5 | 169.062x | 169.062x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,916,741.8 | 2.8459 | 3,916,602.0 | 3,965,176.6 | 19,290.1 | 169.112x | 169.112x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,667.3 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,672.2 | 0.0169 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,893.4 | 0.0171 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,923.5 | 1.6193 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,981,701.5 | 2.8436 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,982,856.7 | 2.8447 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,387.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,382.1 | 0.0167 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 4,500.2 | 0.0172 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,310.8 | 1.6186 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 746,032.4 | 2.8459 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 746,291.4 | 2.8469 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,112.1 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,107.6 | 0.0169 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 1,168.9 | 0.0178 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,253.0 | 1.6213 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 187,403.6 | 2.8596 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 187,658.3 | 2.8634 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 735.7 | 723.4 | 749.6 | 9.0 | 1.000x | 1.000x | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 748.6 | 727.2 | 749.0 | 8.8 | 1.017x | 1.017x | 75 | 10.0 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,950.2 | 2,944.0 | 2,982.5 | 13.7 | 4.010x | 4.010x | 75 | 39.3 | 16.3 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,030.3 | 5,017.9 | 5,039.2 | 6.9 | 6.837x | 6.837x | 75 | 67.1 | 58.6 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,414.1 | 5,355.5 | 5,664.6 | 120.2 | 7.359x | 7.359x | 75 | 72.2 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,550.4 | 5,206.5 | 5,613.7 | 158.5 | 7.544x | 7.544x | 75 | 74.0 | 18.1 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 664.5 | 0.0005 | 663.9 | 687.5 | 9.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 10,416,746.5 | 7.5689 | 10,415,260.7 | 10,467,104.4 | 20,179.2 | 15677.151x | 15677.151x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 34,955,033.5 | 25.3986 | 34,875,931.0 | 35,467,619.0 | 237,386.8 | 52607.148x | 52607.148x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,130,195,568.0 | 1547.8193 | 2,128,387,168.0 | 2,150,492,762.0 | 8,257,604.0 | 3205933.517x | 3205933.517x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 213.4 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 7,936,463.0 | 7.5688 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 24,312,714.8 | 23.1864 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,621,643,077.0 | 1546.5194 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 217.7 | 0.0008 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,982,468.7 | 7.5625 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,485,901.5 | 28.5564 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 407,805,360.0 | 1555.6540 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 233.3 | 0.0036 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 496,998.9 | 7.5836 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,106,137.2 | 47.3959 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 102,359,990.0 | 1561.8895 |

- not ranked: `pcrec_25b1984f_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670159 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,012.7 | 2,006.7 | 2,019.3 | 4.0 | 1.000x | 1.000x | 75 | 26.8 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,755.9 | 3,753.9 | 3,761.1 | 2.5 | 1.866x | 1.866x | 75 | 50.1 | 27.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 87,697.4 | 87,186.0 | 88,012.9 | 318.5 | 43.571x | 43.571x | 75 | 1,169.3 | 16.3 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 766,271.8 | 763,257.0 | 775,743.1 | 4,414.0 | 380.713x | 380.713x | 75 | 10,217.0 | 58.6 | 100% |

- not ranked: `pcrec_25b1984f_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670159 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_25b1984f_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665107 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 19.7 | 0.0000 | 19.6 | 21.6 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 32.9 | 0.0000 | 32.8 | 33.0 | 0.1 | 1.672x | 1.672x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 146.8 | 0.0001 | 146.4 | 151.4 | 1.9 | 7.459x | 7.459x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 300.5 | 0.0002 | 299.7 | 310.5 | 4.0 | 15.265x | 15.265x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 985.3 | 0.0007 | 980.8 | 1,013.6 | 12.2 | 50.056x | 50.056x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,271,081.5 | 3.1034 | 4,267,281.7 | 4,296,011.4 | 11,783.6 | 216980.063x | 216980.063x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,272,179.9 | 3.1042 | 4,268,759.0 | 4,285,583.9 | 6,827.3 | 217035.864x | 217035.864x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.1 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 40.9 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 299.3 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,251,196.1 | 3.1006 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,253,085.8 | 3.1024 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.9 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48.8 | 0.0002 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 127.0 | 0.0005 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 414.6 | 0.0016 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,946.6 | 3.1050 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,944.6 | 3.1050 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 11.0 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.0 | 0.0007 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 133.0 | 0.0020 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 270.9 | 0.0041 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 204,061.1 | 3.1137 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 204,699.9 | 3.1235 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 589.1 | 588.2 | 593.7 | 2.0 | 1.000x | 1.000x | 75 | 7.9 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 980.7 | 979.7 | 982.5 | 1.0 | 1.665x | 1.665x | 75 | 13.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,618.4 | 1,617.5 | 1,623.2 | 2.1 | 2.748x | 2.748x | 75 | 21.6 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,056.3 | 2,037.0 | 2,063.0 | 8.8 | 3.491x | 3.491x | 75 | 27.4 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,294.9 | 6,290.9 | 6,297.3 | 2.2 | 10.686x | 10.686x | 75 | 83.9 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,322.0 | 6,316.8 | 6,352.1 | 13.1 | 10.732x | 10.732x | 75 | 84.3 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,640.0 | 11,607.3 | 12,095.6 | 182.2 | 19.760x | 19.760x | 75 | 155.2 | 58.6 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,033,368.0 | 2.9307 | 4,029,796.9 | 4,045,486.7 | 6,181.4 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,082,283.0 | 2.9662 | 4,019,953.3 | 4,800,486.6 | 294,603.2 | 1.012x | 1.012x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23,346,197.8 | 16.9636 | 23,216,402.8 | 23,489,684.5 | 91,028.0 | 5.788x | 5.788x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,793,876.7 | 17.2888 | 23,643,353.1 | 24,528,511.9 | 329,784.4 | 5.899x | 5.899x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 27,136,727.1 | 19.7178 | 27,088,807.8 | 27,175,597.3 | 33,026.7 | 6.728x | 6.728x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,093,119.7 | 2.9498 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,111,899.4 | 2.9677 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,781,887.8 | 16.9581 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 18,011,660.1 | 17.1773 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 20,788,943.8 | 19.8259 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 759,020.7 | 2.8954 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 773,434.7 | 2.9504 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,438,819.6 | 16.9328 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,615,310.6 | 17.6060 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 5,110,807.4 | 19.4962 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 184,709.8 | 2.8184 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 190,926.7 | 2.9133 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,127,504.7 | 17.2044 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,155,510.5 | 17.6317 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,234,883.9 | 18.8428 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,499.5 | 2,492.7 | 2,599.1 | 39.7 | 1.000x | 1.000x | 75 | 33.3 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,506.4 | 2,486.8 | 2,526.9 | 13.4 | 1.003x | 1.003x | 75 | 33.4 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,869.7 | 15,748.6 | 15,945.0 | 64.9 | 6.349x | 6.349x | 75 | 211.6 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 18,291.5 | 18,260.6 | 18,317.9 | 21.7 | 7.318x | 7.318x | 75 | 243.9 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 18,643.3 | 18,610.8 | 20,746.4 | 843.8 | 7.459x | 7.459x | 75 | 248.6 | 17.3 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,986,220.4 | 2.8964 | 3,982,256.7 | 3,991,033.6 | 2,966.7 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,987,279.3 | 2.8972 | 3,982,611.1 | 4,014,559.1 | 11,789.8 | 1.000x | 1.000x |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 23,362,962.1 | 16.9757 | 23,202,978.5 | 23,748,964.5 | 186,115.3 | 5.861x | 5.861x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,474,583.4 | 17.0568 | 23,335,555.9 | 32,247,834.8 | 3,501,206.8 | 5.889x | 5.889x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 25,662,944.7 | 18.6469 | 25,584,875.2 | 26,040,035.9 | 167,887.8 | 6.438x | 6.438x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,050,989.4 | 2.9097 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,053,117.2 | 2.9117 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,847,481.5 | 17.0207 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 17,779,000.0 | 16.9554 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 19,667,372.2 | 18.7563 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 751,588.1 | 2.8671 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 749,608.3 | 2.8595 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,401,331.1 | 16.7897 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,437,611.0 | 16.9281 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,827,028.7 | 18.4137 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 181,345.6 | 2.7671 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 181,902.3 | 2.7756 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,112,455.3 | 16.9747 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,176,320.2 | 17.9492 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,175,872.0 | 17.9424 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,472.2 | 2,470.3 | 3,244.2 | 308.8 | 1.000x | 1.000x | 75 | 33.0 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,477.7 | 2,473.2 | 2,568.8 | 37.1 | 1.002x | 1.002x | 75 | 33.0 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,914.6 | 15,830.8 | 16,152.9 | 113.2 | 6.437x | 6.437x | 75 | 212.2 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 17,986.4 | 17,797.4 | 18,144.5 | 130.4 | 7.275x | 7.275x | 75 | 239.8 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 18,011.5 | 17,842.3 | 27,664.4 | 3,868.9 | 7.286x | 7.286x | 75 | 240.2 | 17.3 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,010,763.0 | 0.7344 | 1,008,373.7 | 1,013,305.5 | 1,772.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,013,117.8 | 0.7361 | 1,008,885.0 | 1,028,338.2 | 7,325.3 | 1.002x | 1.002x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,468,163.7 | 2.5200 | 3,438,061.5 | 3,492,510.9 | 18,643.1 | 3.431x | 3.431x |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 46,668,425.2 | 33.9097 | 46,637,763.3 | 46,841,691.3 | 93,496.0 | 46.171x | 46.171x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 46,812,411.2 | 34.0143 | 46,636,503.5 | 52,094,082.8 | 2,128,095.9 | 46.314x | 46.314x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 773,071.6 | 0.7373 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 777,386.0 | 0.7414 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,652,742.3 | 2.5299 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 35,522,169.7 | 33.8766 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 35,709,079.7 | 34.0548 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 188,692.9 | 0.7198 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 188,369.8 | 0.7186 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 648,880.4 | 2.4753 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 8,892,795.5 | 33.9233 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 8,882,754.2 | 33.8850 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 47,648.9 | 0.7271 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 47,630.4 | 0.7268 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 163,685.8 | 2.4976 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,230,368.0 | 34.0327 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 2,238,814.0 | 34.1616 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,961.3 | 1,956.4 | 1,968.2 | 4.4 | 1.000x | 1.000x | 75 | 26.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,962.7 | 1,955.6 | 1,968.0 | 5.1 | 1.001x | 1.001x | 75 | 26.2 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,298.3 | 6,267.4 | 6,471.0 | 73.0 | 3.211x | 3.211x | 75 | 84.0 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,994.8 | 48,985.8 | 49,011.5 | 10.2 | 24.981x | 24.981x | 75 | 653.3 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 49,149.4 | 49,111.6 | 49,195.2 | 28.9 | 25.060x | 25.060x | 75 | 655.3 | 17.3 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 929,769.2 | 0.6756 | 928,128.6 | 936,047.8 | 2,746.6 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 932,805.8 | 0.6778 | 930,676.3 | 946,446.4 | 5,729.0 | 1.003x | 1.003x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,265,325.1 | 2.3726 | 3,254,397.3 | 3,301,336.2 | 16,280.2 | 3.512x | 3.512x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 22,994,263.9 | 16.7078 | 22,876,074.8 | 23,268,344.8 | 143,236.1 | 24.731x | 24.731x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 23,029,113.2 | 16.7332 | 23,016,442.3 | 23,196,942.6 | 70,739.6 | 24.769x | 24.769x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 711,599.1 | 0.6786 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 712,723.5 | 0.6797 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,495,212.5 | 2.3796 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 17,543,953.8 | 16.7312 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 17,554,799.5 | 16.7416 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 174,186.9 | 0.6645 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 175,784.8 | 0.6706 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 614,588.9 | 2.3445 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,372,022.6 | 16.6779 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,388,976.6 | 16.7426 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 43,983.2 | 0.6711 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 44,168.2 | 0.6740 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 154,604.0 | 2.3591 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,096,122.8 | 16.7255 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,100,453.1 | 16.7916 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,855.1 | 1,848.0 | 1,861.5 | 4.4 | 1.000x | 1.000x | spread | 75 | 24.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,861.0 | 1,854.6 | 1,865.8 | 3.8 | 1.003x | 1.003x | spread | 75 | 24.8 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 114,108.8 | 113,982.2 | 114,247.0 | 99.5 | 61.510x | 61.510x | spread | 75 | 1,521.5 | 18.1 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 114,561.3 | 114,264.4 | 114,629.5 | 153.6 | 61.754x | 61.754x | spread | 75 | 1,527.5 | 17.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 289,071.9 | 288,036.2 | 291,865.5 | 1,642.4 | 155.823x | 155.823x | **dominated**: `waf-sleep` is 98.0% of this set | 75 | 3,854.3 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,989,947.3 | 2.8991 | 3,988,061.7 | 3,997,590.8 | 3,330.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,990,079.4 | 2.8992 | 3,987,701.4 | 4,001,838.4 | 5,081.7 | 1.000x | 1.000x |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 41,425,257.0 | 30.1000 | 41,251,343.1 | 42,074,755.1 | 283,045.8 | 10.382x | 10.382x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 41,587,687.4 | 30.2180 | 41,335,341.6 | 41,777,687.3 | 158,925.6 | 10.423x | 10.423x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 69,526,109.5 | 50.5183 | 69,436,479.0 | 69,721,555.8 | 99,145.8 | 17.425x | 17.425x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,037,288.5 | 2.8966 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,038,696.3 | 2.8979 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 31,657,651.1 | 30.1911 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 31,752,531.3 | 30.2816 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 52,896,242.0 | 50.4458 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 760,771.7 | 2.9021 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 761,359.8 | 2.9044 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,864,027.4 | 29.9989 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 7,876,306.7 | 30.0457 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 13,312,656.5 | 50.7838 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 191,433.9 | 2.9210 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 190,641.8 | 2.9090 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,953,911.4 | 29.8143 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,960,612.4 | 29.9166 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,320,966.0 | 50.6739 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,577.8 | 3,571.2 | 3,588.6 | 6.3 | 1.000x | 1.000x | 75 | 47.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,768.7 | 3,762.8 | 3,797.9 | 14.1 | 1.053x | 1.053x | 75 | 50.2 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,463.4 | 23,336.7 | 23,617.2 | 89.3 | 6.558x | 6.558x | 75 | 312.8 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 40,050.0 | 39,976.5 | 57,011.0 | 6,785.4 | 11.194x | 11.194x | 75 | 534.0 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 40,962.3 | 40,859.4 | 41,237.4 | 128.1 | 11.449x | 11.449x | 75 | 546.2 | 17.3 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,611.9 | 1.6193 | 2,227,431.4 | 2,233,948.9 | 2,342.8 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,473,038.3 | 2.5235 | 3,470,255.0 | 3,480,615.8 | 3,885.3 | 1.558x | 1.558x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,475,924.2 | 2.5256 | 3,462,918.0 | 3,487,299.3 | 10,445.6 | 1.560x | 1.560x |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 19,585,971.2 | 14.2313 | 19,359,921.2 | 19,649,611.0 | 102,249.2 | 8.788x | 8.788x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,147,936.1 | 14.6397 | 19,724,329.6 | 20,348,383.3 | 222,571.2 | 9.041x | 9.041x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,367.4 | 1.6187 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 2,649,104.5 | 2.5264 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,651,472.4 | 2.5286 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 14,970,094.9 | 14.2766 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 15,593,253.3 | 14.8709 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,510.5 | 1.6194 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 659,770.4 | 2.5168 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 661,057.3 | 2.5217 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,734,735.5 | 14.2469 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,695,862.3 | 14.0986 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,435.3 | 1.6241 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 164,242.1 | 2.5061 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 164,545.5 | 2.5108 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 874,956.8 | 13.3508 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 906,660.7 | 13.8345 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,640.9 | 2,637.4 | 2,657.6 | 7.9 | 1.000x | 1.000x | 75 | 35.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,645.3 | 2,635.0 | 2,665.2 | 10.2 | 1.002x | 1.002x | 75 | 35.3 | 8.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,333.8 | 5,319.6 | 5,370.6 | 18.2 | 2.020x | 2.020x | 75 | 71.1 | 58.6 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 22,945.1 | 22,933.5 | 23,002.1 | 24.5 | 8.688x | 8.688x | 75 | 305.9 | 18.1 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 24,419.9 | 23,726.7 | 24,999.7 | 404.2 | 9.247x | 9.247x | 75 | 325.6 | 17.3 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 135,353.4 | 0.0983 | 134,881.8 | 135,641.7 | 253.3 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292,715.6 | 0.2127 | 292,486.5 | 292,907.9 | 138.2 | 2.163x | 2.163x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,169,998.5 | 1.5767 | 2,169,573.3 | 2,170,995.6 | 500.0 | 16.032x | 16.032x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,009,771.6 | 2.9135 | 4,005,307.7 | 4,013,416.1 | 2,705.2 | 29.624x | 29.624x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,200,484.6 | 3.0521 | 4,199,420.3 | 4,200,924.0 | 506.9 | 31.033x | 31.033x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,328,970.6 | 6.7785 | 9,323,065.2 | 9,404,733.9 | 30,333.4 | 68.923x | 68.923x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,357,212.3 | 6.7990 | 9,350,613.0 | 9,544,350.4 | 73,808.7 | 69.132x | 69.132x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 104,949.7 | 0.1001 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 223,361.1 | 0.2130 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,653,129.1 | 1.5765 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,052,295.9 | 2.9109 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,201,028.0 | 3.0527 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,119,389.1 | 6.7896 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,139,327.3 | 6.8086 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 24,958.1 | 0.0952 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55,341.5 | 0.2111 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 413,095.2 | 1.5758 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 765,843.6 | 2.9215 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 800,561.6 | 3.0539 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,772,424.3 | 6.7613 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,778,145.0 | 6.7831 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 5,366.2 | 0.0819 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 14,046.7 | 0.2143 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 103,946.7 | 1.5861 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 190,313.9 | 2.9040 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 198,647.9 | 3.0311 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 440,673.2 | 6.7241 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 443,470.4 | 6.7668 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,100.3 | 2,098.1 | 2,101.6 | 1.2 | 1.000x | 1.000x | 75 | 28.0 | 27.2 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,150.7 | 2,136.3 | 2,156.7 | 8.3 | 1.024x | 1.024x | 75 | 28.7 | 16.3 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,464.9 | 2,460.4 | 2,479.6 | 6.6 | 1.174x | 1.174x | 75 | 32.9 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,723.9 | 2,718.0 | 2,726.5 | 2.9 | 1.297x | 1.297x | 75 | 36.3 | 8.9 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,511.2 | 7,473.9 | 7,562.0 | 29.5 | 3.576x | 3.576x | 75 | 100.1 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 7,749.8 | 7,723.6 | 7,833.4 | 38.8 | 3.690x | 3.690x | 75 | 103.3 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 7,864.7 | 7,851.7 | 7,962.5 | 41.0 | 3.745x | 3.745x | 75 | 104.9 | 17.3 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 46,778.6 | 0.0340 | 46,731.6 | 46,869.8 | 46.5 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,233.4 | 0.0438 | 60,099.4 | 60,316.8 | 83.6 | 1.288x | 1.288x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 124,561.7 | 0.0905 | 124,435.2 | 124,905.4 | 172.3 | 2.663x | 2.663x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 124,571.0 | 0.0905 | 124,527.0 | 125,079.6 | 209.2 | 2.663x | 2.663x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 414,276.2 | 0.3010 | 414,097.9 | 414,384.9 | 107.8 | 8.856x | 8.856x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,776,127.5 | 3.4704 | 4,764,302.1 | 4,788,620.1 | 8,857.8 | 102.101x | 102.101x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,228,975.3 | 3.7994 | 5,226,900.3 | 5,252,187.0 | 10,563.6 | 111.781x | 111.781x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 35,548.9 | 0.0339 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,797.1 | 0.0437 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 102,520.4 | 0.0978 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 102,536.1 | 0.0978 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 315,199.4 | 0.3006 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,639,215.6 | 3.4706 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,985,582.7 | 3.8009 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 8,939.3 | 0.0341 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,476.2 | 0.0438 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 18,580.9 | 0.0709 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 18,603.0 | 0.0710 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 79,019.5 | 0.3014 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 906,911.4 | 3.4596 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 993,100.7 | 3.7884 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,288.4 | 0.0349 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,949.0 | 0.0450 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,438.1 | 0.0525 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 3,435.4 | 0.0524 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 19,987.7 | 0.3050 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 225,493.1 | 3.4408 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 248,989.6 | 3.7993 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 824.4 | 823.4 | 827.0 | 1.4 | 1.000x | 1.000x | 75 | 11.0 | 27.2 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,374.0 | 1,371.1 | 1,378.9 | 2.6 | 1.667x | 1.667x | 75 | 18.3 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,705.5 | 1,699.0 | 1,711.4 | 4.3 | 2.069x | 2.069x | 75 | 22.7 | 8.9 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,709.6 | 1,704.5 | 1,796.7 | 39.8 | 2.074x | 2.074x | 75 | 22.8 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,962.6 | 2,932.9 | 3,132.0 | 72.5 | 3.594x | 3.594x | 75 | 39.5 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,148.7 | 3,142.8 | 3,153.3 | 3.8 | 3.819x | 3.819x | 75 | 42.0 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,638.8 | 3,627.6 | 3,648.3 | 7.2 | 4.414x | 4.414x | 75 | 48.5 | 17.3 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 111,588.1 | 0.0811 | 111,541.9 | 111,722.4 | 68.7 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 338,487.8 | 0.2459 | 338,281.2 | 339,090.3 | 311.2 | 3.033x | 3.033x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 341,069.2 | 0.2478 | 340,899.1 | 341,496.4 | 220.6 | 3.057x | 3.057x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 645,403.6 | 0.4690 | 645,007.8 | 648,225.5 | 1,277.8 | 5.784x | 5.784x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,249,728.7 | 0.9081 | 1,249,324.3 | 1,251,105.1 | 654.1 | 11.199x | 11.199x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,775,991.7 | 3.4703 | 4,774,315.2 | 4,799,901.9 | 9,618.1 | 42.800x | 42.800x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,776,737.9 | 3.4708 | 4,774,203.3 | 4,789,473.8 | 6,964.9 | 42.807x | 42.807x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86,290.6 | 0.0823 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 259,808.2 | 0.2478 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 261,933.7 | 0.2498 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 494,203.7 | 0.4713 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 952,771.5 | 0.9086 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,638,027.3 | 3.4695 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,637,544.9 | 3.4690 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,510.9 | 0.0782 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 64,071.6 | 0.2444 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 64,435.7 | 0.2458 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 121,819.1 | 0.4647 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 237,785.5 | 0.9071 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 910,004.2 | 3.4714 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 909,928.4 | 3.4711 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,848.7 | 0.0740 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 14,666.0 | 0.2238 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 14,723.8 | 0.2247 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 29,273.5 | 0.4467 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 59,081.3 | 0.9015 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 228,231.2 | 3.4825 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 229,143.3 | 3.4964 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 693.8 | 693.5 | 695.0 | 0.5 | 1.000x | 1.000x | 75 | 9.3 | 27.2 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 928.0 | 927.8 | 928.4 | 0.2 | 1.338x | 1.338x | 75 | 12.4 | 8.9 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,307.7 | 1,304.9 | 1,309.0 | 1.4 | 1.885x | 1.885x | 75 | 17.4 | 8.9 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,657.6 | 2,655.8 | 2,662.0 | 2.1 | 3.830x | 3.830x | 75 | 35.4 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,370.0 | 3,347.5 | 3,415.9 | 23.8 | 4.857x | 4.857x | 75 | 44.9 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,620.4 | 5,609.1 | 5,624.0 | 6.4 | 8.100x | 8.100x | 75 | 74.9 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,739.3 | 5,718.7 | 5,783.2 | 23.1 | 8.272x | 8.272x | 75 | 76.5 | 17.3 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 475,300.9 | 0.3454 | 474,921.1 | 478,357.7 | 1,269.8 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 488,283.4 | 0.3548 | 487,944.0 | 488,657.0 | 245.7 | 1.027x | 1.027x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,281,220.0 | 0.9309 | 1,280,425.0 | 1,286,992.6 | 2,453.9 | 2.696x | 2.696x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,284,785.7 | 0.9335 | 1,282,321.7 | 1,291,174.5 | 3,286.7 | 2.703x | 2.703x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,839,830.3 | 3.5167 | 4,833,993.0 | 4,841,579.2 | 2,683.4 | 10.183x | 10.183x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,879,102.3 | 4.2718 | 5,852,911.3 | 5,895,791.5 | 13,754.9 | 12.369x | 12.369x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,880,549.9 | 4.2729 | 5,877,909.2 | 5,894,656.6 | 7,416.3 | 12.372x | 12.372x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 377,999.5 | 0.3605 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 371,587.1 | 0.3544 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 972,132.9 | 0.9271 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 972,598.4 | 0.9275 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,673,731.4 | 3.5035 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,474,636.2 | 4.2673 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 4,476,312.4 | 4.2689 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 80,972.7 | 0.3089 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 93,703.3 | 0.3574 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 245,649.3 | 0.9371 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 248,984.7 | 0.9498 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 927,848.3 | 3.5395 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,121,745.4 | 4.2791 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,120,925.1 | 4.2760 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,404.5 | 0.2503 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 22,862.0 | 0.3488 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 64,058.3 | 0.9775 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 63,119.5 | 0.9631 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 236,377.1 | 3.6068 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 282,144.0 | 4.3052 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 281,468.9 | 4.2949 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,372.6 | 1,367.3 | 1,379.7 | 4.4 | 1.000x | 1.000x | 75 | 18.3 | 8.9 | 100% |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,761.0 | 1,760.6 | 1,764.7 | 1.5 | 1.283x | 1.283x | 75 | 23.5 | 27.2 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,863.6 | 1,862.2 | 1,869.5 | 3.1 | 1.358x | 1.358x | 75 | 24.8 | 8.9 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,438.8 | 2,435.4 | 2,444.5 | 3.2 | 1.777x | 1.777x | 75 | 32.5 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,388.3 | 6,321.1 | 6,458.1 | 50.1 | 4.654x | 4.654x | 75 | 85.2 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,591.2 | 6,481.5 | 6,650.4 | 63.3 | 4.802x | 4.802x | 75 | 87.9 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,009.9 | 8,990.2 | 9,116.4 | 58.0 | 6.564x | 6.564x | 75 | 120.1 | 58.6 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 82,113.0 | 0.0597 | 81,814.0 | 82,401.7 | 190.6 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 153,217.2 | 0.1113 | 153,133.3 | 153,863.4 | 272.2 | 1.866x | 1.866x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 408,869.9 | 0.2971 | 408,065.0 | 410,037.3 | 695.2 | 4.979x | 4.979x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 410,146.0 | 0.2980 | 409,007.4 | 412,859.0 | 1,452.3 | 4.995x | 4.995x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,340,923.6 | 0.9743 | 1,330,893.2 | 1,342,368.7 | 4,184.8 | 16.330x | 16.330x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,941,797.2 | 2.8641 | 3,930,981.7 | 3,943,708.6 | 4,834.3 | 48.005x | 48.005x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,944,640.0 | 2.8662 | 3,943,953.3 | 3,977,504.5 | 13,277.4 | 48.039x | 48.039x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 63,418.9 | 0.0605 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 116,734.9 | 0.1113 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 325,885.8 | 0.3108 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 326,422.2 | 0.3113 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,020,752.8 | 0.9735 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,002,677.8 | 2.8636 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,004,224.8 | 2.8651 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 15,109.3 | 0.0576 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 29,116.4 | 0.1111 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 69,787.3 | 0.2662 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 70,349.1 | 0.2684 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 255,999.1 | 0.9766 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 751,487.5 | 2.8667 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 751,833.1 | 2.8680 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 3,595.0 | 0.0549 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,381.2 | 0.1126 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 13,225.3 | 0.2018 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 13,377.1 | 0.2041 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 64,171.7 | 0.9792 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 188,267.0 | 2.8727 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 188,558.8 | 2.8772 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 710.3 | 706.4 | 711.8 | 1.9 | 1.000x | 1.000x | 75 | 9.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 711.6 | 705.4 | 712.7 | 3.0 | 1.002x | 1.002x | 75 | 9.5 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,344.5 | 1,342.5 | 1,346.0 | 1.3 | 1.893x | 1.893x | 75 | 17.9 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,410.1 | 2,402.6 | 2,867.1 | 183.6 | 3.393x | 3.393x | 75 | 32.1 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,988.1 | 2,979.9 | 3,008.2 | 10.2 | 4.207x | 4.207x | 75 | 39.8 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,634.0 | 4,498.8 | 4,730.4 | 78.1 | 6.524x | 6.524x | 75 | 61.8 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,950.5 | 4,832.6 | 5,121.3 | 106.5 | 6.970x | 6.970x | 75 | 66.0 | 17.3 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 80.8 | 0.0001 | 78.7 | 102.6 | 9.2 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 151.3 | 0.0001 | 151.2 | 154.4 | 1.5 | 1.872x | 1.872x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 218.3 | 0.0002 | 218.2 | 218.6 | 0.1 | 2.701x | 2.701x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 109,563.9 | 0.0796 | 109,529.1 | 109,919.9 | 160.7 | 1355.716x | 1355.716x |
| 5 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 109,709.6 | 0.0797 | 109,434.8 | 109,822.0 | 137.5 | 1357.519x | 1357.519x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 1,671,839.2 | 1.2148 | 1,671,388.0 | 1,676,090.2 | 1,772.2 | 20686.928x | 20686.928x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,671,960.2 | 1.2149 | 1,670,963.8 | 1,679,366.5 | 3,385.5 | 20688.426x | 20688.426x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 26.3 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 50.3 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 72.2 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 89,409.9 | 0.0853 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 89,355.3 | 0.0852 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,273,120.1 | 1.2141 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 1,273,803.7 | 1.2148 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 26.5 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 73.4 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 16,771.5 | 0.0640 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 16,824.6 | 0.0642 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 317,955.7 | 1.2129 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 317,815.0 | 1.2124 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 28.0 | 0.0004 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 50.6 | 0.0008 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 72.7 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 3,483.6 | 0.0532 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,494.5 | 0.0533 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 80,952.8 | 1.2352 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 80,714.4 | 1.2316 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,186.8 | 1,183.0 | 1,199.0 | 6.5 | 1.000x | 1.000x | 75 | 15.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,187.1 | 1,180.3 | 1,202.9 | 7.5 | 1.000x | 1.000x | 75 | 15.8 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,596.2 | 1,593.6 | 1,598.5 | 1.9 | 1.345x | 1.345x | 75 | 21.3 | 16.3 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 2,003.1 | 1,997.0 | 2,010.2 | 4.7 | 1.688x | 1.688x | 75 | 26.7 | 17.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 2,145.9 | 2,137.5 | 2,155.4 | 6.1 | 1.808x | 1.808x | 75 | 28.6 | 18.1 | 100% |
| 6 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,745.4 | 2,739.2 | 2,751.9 | 4.3 | 2.313x | 2.313x | 75 | 36.6 | 27.2 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,476.7 | 3,464.2 | 3,481.5 | 6.0 | 2.930x | 2.930x | 75 | 46.4 | 58.6 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243.2 | 0.0002 | 242.6 | 243.5 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,815,862.7 | 2.7726 | 3,789,922.3 | 3,872,616.8 | 28,018.4 | 15689.534x | 15689.534x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,000,451.7 | 5.0866 | 6,979,527.8 | 7,019,620.5 | 14,802.9 | 28783.484x | 28783.484x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,155,051.0 | 9.5586 | 13,136,711.4 | 14,573,119.8 | 567,946.0 | 54089.111x | 54089.111x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 25,326,087.5 | 18.4022 | 25,222,464.1 | 25,523,597.7 | 99,530.7 | 104132.287x | 104132.287x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 25,909,063.3 | 18.8258 | 25,818,475.5 | 27,848,983.3 | 788,419.9 | 106529.286x | 106529.286x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 100,170,778.7 | 72.7850 | 99,345,551.0 | 100,340,716.3 | 398,471.3 | 411868.288x | 411868.288x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.6 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,917,753.5 | 2.7826 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 5,380,021.3 | 5.1308 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 10,072,926.4 | 9.6063 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 19,331,452.4 | 18.4359 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 19,758,697.3 | 18.8434 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 76,491,564.0 | 72.9480 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 78.9 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 718,307.7 | 2.7401 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 1,303,804.0 | 4.9736 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 2,479,690.8 | 9.4593 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 4,795,733.5 | 18.2943 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 4,918,514.6 | 18.7626 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 18,923,778.3 | 72.1885 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 79.4 | 0.0012 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 173,342.5 | 2.6450 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 315,426.4 | 4.8130 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 602,482.3 | 9.1932 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 1,202,505.2 | 18.3488 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,230,642.3 | 18.7781 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 4,671,819.3 | 71.2863 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,232.5 | 1,229.3 | 1,236.8 | 3.0 | 1.000x | 1.000x | 75 | 16.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,893.7 | 2,879.7 | 2,912.4 | 12.5 | 2.348x | 2.348x | 75 | 38.6 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,884.3 | 3,879.7 | 3,893.9 | 4.9 | 3.152x | 3.152x | 75 | 51.8 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,205.5 | 13,150.9 | 13,262.1 | 42.0 | 10.714x | 10.714x | 75 | 176.1 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,243.3 | 17,104.3 | 18,397.4 | 496.6 | 13.991x | 13.991x | 75 | 229.9 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 101,862.0 | 101,775.3 | 102,424.1 | 234.9 | 82.646x | 82.646x | 75 | 1,358.2 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 104,063.0 | 104,049.7 | 104,212.6 | 63.6 | 84.432x | 84.432x | 75 | 1,387.5 | 18.1 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 39.0 | 0.0000 | 36.0 | 39.6 | 1.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 40.4 | 0.0000 | 39.5 | 41.6 | 0.7 | 1.038x | 1.038x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 108.7 | 0.0001 | 108.0 | 144.1 | 13.9 | 2.789x | 2.789x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 195.5 | 0.0001 | 194.4 | 196.6 | 0.8 | 5.018x | 5.018x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,039.3 | 1.6196 | 2,226,680.9 | 2,234,241.7 | 2,533.5 | 57222.160x | 57222.160x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,474,056.9 | 3.2509 | 4,471,247.6 | 4,512,419.3 | 16,151.4 | 114854.502x | 114854.502x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,474,981.0 | 3.2516 | 4,473,066.4 | 4,493,541.8 | 9,363.3 | 114878.225x | 114878.225x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 13.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 15.1 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 37.6 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 71.7 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,453.4 | 1.6179 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,407,891.8 | 3.2500 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,406,222.1 | 3.2484 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 11.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 11.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 33.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 60.9 | 0.0002 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,729.4 | 1.6202 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 851,829.6 | 3.2495 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 852,229.4 | 3.2510 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 12.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 13.4 | 0.0002 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 37.6 | 0.0006 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 61.9 | 0.0009 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,692.3 | 1.6280 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 214,222.8 | 3.2688 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 214,269.0 | 3.2695 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,063.7 | 1,056.8 | 1,066.1 | 3.6 | 1.000x | 1.000x | 75 | 14.2 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,065.6 | 1,064.4 | 1,072.1 | 2.8 | 1.002x | 1.002x | 75 | 14.2 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,338.7 | 2,331.9 | 2,353.0 | 8.1 | 2.199x | 2.199x | 75 | 31.2 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,566.8 | 2,565.6 | 2,569.2 | 1.3 | 2.413x | 2.413x | 75 | 34.2 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,252.3 | 5,222.7 | 5,509.9 | 113.6 | 4.938x | 4.938x | 75 | 70.0 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,417.4 | 6,412.3 | 6,433.3 | 7.4 | 6.033x | 6.033x | 75 | 85.6 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,489.4 | 6,484.2 | 6,500.0 | 5.3 | 6.101x | 6.101x | 75 | 86.5 | 18.1 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.2 | 0.0000 | 18.1 | 18.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.7 | 0.0 | 1.028x | 1.028x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 32.1 | 0.7 | 1.672x | 1.672x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 32.1 | 0.0000 | 32.1 | 32.3 | 0.1 | 1.767x | 1.767x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 368.9 | 0.0003 | 366.5 | 371.2 | 1.7 | 20.283x | 20.283x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,269,920.7 | 3.1026 | 4,267,743.0 | 4,284,915.6 | 7,105.0 | 234780.272x | 234780.272x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,270,443.9 | 3.1029 | 4,267,914.7 | 4,287,920.8 | 7,736.6 | 234809.039x | 234809.039x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.8 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 300.1 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,251,341.9 | 3.1007 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,250,594.7 | 3.1000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 34.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 813,573.1 | 3.1035 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 813,379.6 | 3.1028 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 34.4 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 204,133.6 | 3.1148 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 204,427.8 | 3.1193 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 498.6 | 498.0 | 499.0 | 0.3 | 1.000x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 871.9 | 871.2 | 877.8 | 2.4 | 1.749x | 1.749x | 75 | 11.6 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 949.8 | 949.6 | 954.6 | 2.0 | 1.905x | 1.905x | 75 | 12.7 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,258.5 | 1,252.1 | 1,489.3 | 93.4 | 2.524x | 2.524x | 75 | 16.8 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,588.6 | 3,582.1 | 3,591.4 | 3.9 | 7.197x | 7.197x | 75 | 47.8 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,434.6 | 6,421.1 | 6,442.5 | 7.9 | 12.904x | 12.904x | 75 | 85.8 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,611.2 | 6,576.0 | 6,669.0 | 32.1 | 13.258x | 13.258x | 75 | 88.1 | 17.3 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 18.2 | 0.0000 | 17.9 | 18.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 18.6 | 0.0000 | 17.8 | 62.1 | 17.6 | 1.022x | 1.022x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.8 | 0.2 | 1.664x | 1.664x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.6 | 0.0000 | 30.3 | 31.5 | 0.4 | 1.680x | 1.680x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.4 | 0.0001 | 93.9 | 95.1 | 0.4 | 5.183x | 5.183x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,564,789.3 | 2.5902 | 3,559,395.3 | 3,579,315.0 | 7,453.5 | 195693.994x | 195693.994x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,582,070.6 | 2.6028 | 3,564,952.4 | 3,681,949.4 | 41,788.1 | 196642.678x | 196642.678x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,712,215.1 | 2.5866 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 2,727,108.0 | 2.6008 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 679,911.7 | 2.5937 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 681,713.2 | 2.6005 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0005 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 170,444.6 | 2.6008 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 171,449.9 | 2.6161 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 484.6 | 484.0 | 486.4 | 0.9 | 1.000x | 1.000x | 75 | 6.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 809.5 | 808.4 | 815.8 | 2.7 | 1.671x | 1.671x | 75 | 10.8 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 987.3 | 983.6 | 1,037.8 | 20.6 | 2.037x | 2.037x | 75 | 13.2 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,661.7 | 1,660.1 | 1,665.7 | 2.0 | 3.429x | 3.429x | 75 | 22.2 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,898.1 | 4,890.1 | 4,908.1 | 6.8 | 10.108x | 10.108x | 75 | 65.3 | 18.1 | 100% |
| 6 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,006.0 | 4,965.1 | 5,071.9 | 38.1 | 10.330x | 10.330x | 75 | 66.7 | 58.6 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,103.2 | 5,095.0 | 5,121.1 | 9.5 | 10.531x | 10.531x | 75 | 68.0 | 17.3 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 82,553.5 | 0.0600 | 82,185.5 | 82,775.1 | 210.3 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 82,564.1 | 0.0600 | 82,156.9 | 83,073.9 | 307.1 | 1.000x | 1.000x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 210,732.6 | 0.1531 | 206,641.6 | 211,670.6 | 1,769.6 | 2.553x | 2.553x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243,311.3 | 0.1768 | 243,073.3 | 244,429.2 | 505.6 | 2.947x | 2.947x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,418,457.0 | 1.7573 | 2,417,419.5 | 2,425,442.5 | 2,896.5 | 29.296x | 29.296x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 8,125,465.4 | 5.9040 | 8,109,162.3 | 8,131,521.5 | 7,635.9 | 98.427x | 98.427x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 8,142,842.0 | 5.9167 | 8,114,778.8 | 8,152,341.7 | 15,254.1 | 98.637x | 98.637x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 68,368.7 | 0.0652 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 68,422.7 | 0.0653 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 164,982.4 | 0.1573 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 185,723.3 | 0.1771 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,842,666.8 | 1.7573 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 6,203,781.4 | 5.9164 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 6,197,759.3 | 5.9106 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 11,729.6 | 0.0447 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 11,627.7 | 0.0444 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 37,247.9 | 0.1421 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 46,117.4 | 0.1759 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 459,512.6 | 1.7529 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,535,501.8 | 5.8575 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,536,298.4 | 5.8605 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,417.2 | 0.0369 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 2,423.2 | 0.0370 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 8,493.3 | 0.1296 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,423.9 | 0.1743 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 116,225.9 | 1.7735 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 384,695.9 | 5.8700 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 389,329.8 | 5.9407 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 716.4 | 713.8 | 722.6 | 2.9 | 1.000x | 1.000x | 75 | 9.6 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 723.3 | 714.9 | 729.3 | 5.0 | 1.010x | 1.010x | 75 | 9.6 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,243.9 | 1,241.2 | 1,248.7 | 2.8 | 1.736x | 1.736x | 75 | 16.6 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,622.0 | 1,621.1 | 1,663.1 | 16.5 | 2.264x | 2.264x | 75 | 21.6 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,236.6 | 4,225.8 | 4,292.9 | 29.3 | 5.913x | 5.913x | 75 | 56.5 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,781.7 | 6,719.4 | 6,805.4 | 37.2 | 9.466x | 9.466x | 75 | 90.4 | 17.3 | 100% |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,867.1 | 6,820.1 | 6,954.0 | 43.5 | 9.585x | 9.585x | 75 | 91.6 | 18.1 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 600,527.6 | 0.4363 | 600,203.3 | 602,501.2 | 846.3 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,447,677.8 | 1.7785 | 2,446,347.1 | 2,454,808.3 | 3,300.7 | 4.076x | 4.076x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 4,079,409.2 | 2.9641 | 4,076,639.5 | 4,099,688.2 | 10,066.2 | 6.793x | 6.793x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 4,086,165.0 | 2.9690 | 4,075,513.0 | 4,093,195.4 | 6,617.9 | 6.804x | 6.804x |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 20,856,952.2 | 15.1548 | 20,805,797.3 | 20,955,925.9 | 55,243.3 | 34.731x | 34.731x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 20,876,695.2 | 15.1692 | 20,814,111.0 | 20,994,499.7 | 62,321.3 | 34.764x | 34.764x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 65,243,715.4 | 47.4067 | 65,161,138.8 | 65,345,329.8 | 60,460.6 | 108.644x | 108.644x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 477,850.1 | 0.4557 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,863,447.3 | 1.7771 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,111,077.8 | 2.9670 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,117,928.2 | 2.9735 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 15,879,825.4 | 15.1442 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 15,927,286.4 | 15.1894 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 49,718,266.8 | 47.4150 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 101,890.8 | 0.3887 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 466,267.0 | 1.7787 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 777,343.1 | 2.9653 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 775,655.0 | 2.9589 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,964,720.2 | 15.1242 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 3,962,722.6 | 15.1166 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 12,411,363.2 | 47.3456 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,612.3 | 0.3145 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 118,326.0 | 1.8055 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 192,434.8 | 2.9363 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 191,884.7 | 2.9279 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 989,308.1 | 15.0956 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 989,432.4 | 15.0975 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,117,649.4 | 47.5716 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 2,702.1 | 2,698.1 | 2,704.2 | 2.1 | 1.000x | 1.000x | 75 | 36.0 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 2,708.9 | 2,699.1 | 2,729.4 | 10.3 | 1.003x | 1.003x | 75 | 36.1 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,508.7 | 3,500.3 | 3,520.2 | 7.4 | 1.298x | 1.298x | 75 | 46.8 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,414.7 | 4,409.5 | 4,482.1 | 27.4 | 1.634x | 1.634x | 75 | 58.9 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 16,350.5 | 16,325.6 | 16,408.8 | 27.9 | 6.051x | 6.051x | 75 | 218.0 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 16,527.9 | 16,458.2 | 18,060.3 | 620.9 | 6.117x | 6.117x | 75 | 220.4 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 44,914.8 | 44,699.6 | 45,064.0 | 135.3 | 16.622x | 16.622x | 75 | 598.9 | 58.6 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 160,000.2 | 0.1163 | 159,822.9 | 160,520.2 | 234.0 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 388,781.2 | 0.2825 | 388,413.3 | 391,438.7 | 1,130.8 | 2.430x | 2.430x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,266,849.9 | 0.9205 | 1,263,015.1 | 1,270,424.9 | 2,426.8 | 7.918x | 7.918x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,268,060.9 | 0.9214 | 1,262,542.6 | 1,272,120.7 | 3,424.4 | 7.925x | 7.925x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,953,542.1 | 3.5993 | 4,918,625.3 | 5,204,082.4 | 106,725.1 | 30.960x | 30.960x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 9,964,561.2 | 7.2403 | 9,923,345.8 | 9,989,856.6 | 24,795.4 | 62.278x | 62.278x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 9,991,229.3 | 7.2597 | 9,937,780.1 | 10,011,686.1 | 25,155.4 | 62.445x | 62.445x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 121,840.3 | 0.1162 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 296,213.3 | 0.2825 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 963,176.9 | 0.9186 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 962,364.3 | 0.9178 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,772,266.3 | 3.5975 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 7,591,641.1 | 7.2400 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 7,610,662.7 | 7.2581 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 30,369.0 | 0.1158 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 74,336.8 | 0.2836 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 239,344.7 | 0.9130 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 241,508.7 | 0.9213 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 935,619.9 | 3.5691 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 1,904,275.7 | 7.2642 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 1,902,396.7 | 7.2571 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,759.0 | 0.1184 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 18,598.8 | 0.2838 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 64,673.8 | 0.9868 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 65,167.3 | 0.9944 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 246,387.6 | 3.7596 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 475,852.6 | 7.2609 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 476,995.7 | 7.2784 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,311.1 | 1,292.4 | 1,329.0 | 11.8 | 1.000x | 1.000x | 75 | 17.5 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,315.2 | 1,308.6 | 1,327.3 | 6.3 | 1.003x | 1.003x | 75 | 17.5 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,655.5 | 2,652.1 | 2,892.4 | 95.2 | 2.025x | 2.025x | 75 | 35.4 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 3,205.3 | 3,199.6 | 3,263.9 | 24.1 | 2.445x | 2.445x | 75 | 42.7 | 16.3 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 11,064.6 | 11,040.6 | 11,075.7 | 15.1 | 8.439x | 8.439x | 75 | 147.5 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 11,254.3 | 11,247.4 | 11,279.5 | 11.6 | 8.584x | 8.584x | 75 | 150.1 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,521.1 | 12,435.0 | 12,650.6 | 76.4 | 9.550x | 9.550x | 75 | 166.9 | 58.6 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 86,460.7 | 0.0628 | 86,417.9 | 88,276.0 | 727.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 280,535.1 | 0.2038 | 280,292.1 | 281,913.4 | 587.4 | 3.245x | 3.245x |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 999,938.0 | 0.7266 | 994,373.0 | 1,014,362.1 | 7,045.4 | 11.565x | 11.565x |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,001,628.0 | 0.7278 | 998,998.7 | 1,004,278.4 | 2,125.6 | 11.585x | 11.585x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,426,906.6 | 2.4900 | 3,424,244.4 | 3,456,801.1 | 12,370.6 | 39.635x | 39.635x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,310,554.1 | 3.1321 | 4,306,801.5 | 4,322,129.6 | 6,241.6 | 49.856x | 49.856x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,312,914.5 | 3.1338 | 4,310,335.0 | 4,323,223.5 | 4,498.1 | 49.883x | 49.883x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 65,907.0 | 0.0629 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 213,566.4 | 0.2037 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 759,553.5 | 0.7244 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 761,054.1 | 0.7258 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,606,030.6 | 2.4853 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,281,557.8 | 3.1295 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,282,418.2 | 3.1304 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,415.1 | 0.0626 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 53,413.9 | 0.2038 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 190,714.5 | 0.7275 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 192,326.8 | 0.7337 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 655,035.1 | 2.4988 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 821,649.7 | 3.1343 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 823,006.1 | 3.1395 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,151.7 | 0.0634 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 13,462.0 | 0.2054 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 48,260.3 | 0.7364 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 48,282.4 | 0.7367 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 166,383.1 | 2.5388 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 207,066.8 | 3.1596 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 207,442.9 | 3.1653 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,151.9 | 1,142.8 | 1,158.7 | 5.8 | 1.000x | 1.000x | 75 | 15.4 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,153.6 | 1,136.5 | 1,158.8 | 7.8 | 1.001x | 1.001x | 75 | 15.4 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,132.0 | 2,126.4 | 2,159.3 | 11.5 | 1.851x | 1.851x | 75 | 28.4 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,160.0 | 2,156.9 | 2,167.8 | 4.1 | 1.875x | 1.875x | 75 | 28.8 | 27.2 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 5,247.4 | 5,240.6 | 5,255.2 | 5.4 | 4.556x | 4.556x | 75 | 70.0 | 18.1 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 5,298.1 | 5,290.8 | 5,308.7 | 6.0 | 4.600x | 4.600x | 75 | 70.6 | 17.3 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,720.9 | 8,702.9 | 8,807.7 | 36.7 | 7.571x | 7.571x | 75 | 116.3 | 58.6 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 878,544.4 | 0.6384 | 877,906.5 | 884,943.3 | 2,643.8 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,456,623.7 | 1.7850 | 2,452,896.6 | 2,562,372.7 | 42,248.5 | 2.796x | 2.796x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 12,146,302.4 | 8.8256 | 12,104,328.1 | 12,268,470.6 | 57,853.3 | 13.825x | 13.825x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 12,197,521.8 | 8.8628 | 12,121,998.2 | 12,278,151.6 | 60,432.4 | 13.884x | 13.884x |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,342,762.5 | 35.1263 | 47,987,543.7 | 48,557,390.5 | 205,687.6 | 55.026x | 55.026x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 48,430,775.3 | 35.1902 | 48,119,495.3 | 48,533,536.2 | 143,204.5 | 55.126x | 55.126x |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 149,241,780.0 | 108.4404 | 138,342,420.5 | 152,569,384.5 | 6,372,964.6 | 169.874x | 169.874x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 701,073.3 | 0.6686 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,057.5 | 1.7815 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 9,263,082.5 | 8.8340 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 9,295,603.7 | 8.8650 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 36,839,353.5 | 35.1327 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 36,937,771.3 | 35.2266 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 113,880,103.5 | 108.6045 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 149,170.5 | 0.5690 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 468,069.2 | 1.7855 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 2,317,259.4 | 8.8396 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 2,324,687.1 | 8.8680 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 9,200,042.8 | 35.0954 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 9,187,093.8 | 35.0460 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 28,291,947.0 | 107.9252 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 28,284.5 | 0.4316 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 120,065.7 | 1.8321 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 577,600.5 | 8.8135 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 577,231.0 | 8.8078 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 2,295,924.5 | 35.0330 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 2,298,093.5 | 35.0661 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 7,044,319.0 | 107.4878 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 4,566.7 | 4,563.3 | 4,582.6 | 8.6 | 1.000x | 1.000x | 75 | 60.9 | 27.2 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 4,824.8 | 4,819.1 | 4,835.3 | 6.1 | 1.057x | 1.057x | 75 | 64.3 | 16.3 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 7,404.7 | 7,376.1 | 7,420.1 | 14.3 | 1.621x | 1.621x | 75 | 98.7 | 8.9 | 100% |
| 4 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 7,405.0 | 7,365.5 | 7,432.4 | 23.7 | 1.622x | 1.622x | 75 | 98.7 | 8.9 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 48,509.9 | 48,405.1 | 48,729.2 | 127.2 | 10.623x | 10.623x | 75 | 646.8 | 17.3 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 48,545.1 | 48,414.4 | 48,854.0 | 149.7 | 10.630x | 10.630x | 75 | 647.3 | 18.1 | 100% |
| 7 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 143,493.3 | 142,250.6 | 153,891.3 | 4,382.0 | 31.422x | 31.422x | 75 | 1,913.2 | 58.6 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 23,099.9 | 0.0168 | 23,071.7 | 23,235.9 | 60.7 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 23,120.7 | 0.0168 | 23,093.3 | 23,145.9 | 19.3 | 1.001x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 41,263.1 | 0.0300 | 41,241.7 | 41,587.7 | 130.2 | 1.786x | 1.786x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,208.1 | 0.0437 | 60,168.2 | 60,455.9 | 105.8 | 2.606x | 2.606x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,159.6 | 1.0886 | 1,497,937.3 | 1,499,103.4 | 467.4 | 64.856x | 64.856x |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,085,792.3 | 2.9688 | 4,082,663.8 | 4,087,038.9 | 1,606.3 | 176.875x | 176.875x |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,086,071.0 | 2.9690 | 4,082,865.3 | 4,103,257.9 | 7,232.1 | 176.887x | 176.887x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,601.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,624.2 | 0.0168 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 31,358.2 | 0.0299 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,802.5 | 0.0437 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,140,969.5 | 1.0881 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,114,946.4 | 2.9706 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,114,430.9 | 2.9702 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 4,380.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,377.4 | 0.0167 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 7,886.0 | 0.0301 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,467.3 | 0.0437 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,456.0 | 1.0889 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 778,103.3 | 2.9682 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 777,623.0 | 2.9664 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 1,108.9 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,109.3 | 0.0169 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 2,017.5 | 0.0308 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,942.7 | 0.0449 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,616.8 | 1.0928 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 193,068.7 | 2.9460 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 193,471.8 | 2.9521 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 733.1 | 732.2 | 743.7 | 4.4 | 1.000x | 1.000x | 75 | 9.8 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 737.7 | 734.9 | 742.1 | 2.3 | 1.006x | 1.006x | 75 | 9.8 | 8.9 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,427.9 | 2,369.3 | 2,502.9 | 42.7 | 3.312x | 3.312x | 75 | 32.4 | 16.3 | 100% |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,468.5 | 2,465.8 | 3,051.7 | 233.4 | 3.367x | 3.367x | 75 | 32.9 | 27.2 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,885.6 | 3,873.1 | 3,934.2 | 21.2 | 5.300x | 5.300x | 75 | 51.8 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,772.0 | 4,584.1 | 4,836.8 | 89.8 | 6.509x | 6.509x | 75 | 63.6 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,789.6 | 4,777.1 | 4,817.4 | 14.0 | 6.533x | 6.533x | 75 | 63.9 | 17.3 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 20.1 | 0.0000 | 20.0 | 20.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 20.4 | 0.0000 | 20.2 | 20.7 | 0.1 | 1.015x | 1.015x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 90.3 | 0.0001 | 86.4 | 95.0 | 2.9 | 4.494x | 4.494x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.3 | 0.0001 | 92.9 | 93.9 | 0.3 | 4.644x | 4.644x |
| 5 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 156.4 | 0.0001 | 156.0 | 156.5 | 0.2 | 7.787x | 7.787x |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 4,923,754.4 | 3.5776 | 4,908,216.0 | 4,942,748.3 | 14,647.6 | 245113.420x | 245113.420x |
| 7 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 4,930,833.3 | 3.5828 | 4,915,966.7 | 4,981,864.3 | 23,088.9 | 245465.817x | 245465.817x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 27.4 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.0 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 52.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 3,753,273.9 | 3.5794 |
| `t-1m` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 3,763,628.7 | 3.5893 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-caps-simdna` | 6.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `rust_1.13.1_default-caps-simdna` | 30.3 | 0.0001 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.1 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 52.1 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-in-caps-simdna` | 933,040.1 | 3.5593 |
| `t-256k` | 262,144 | `pcrec_25b1984f_vm-caps-simdna` | 931,911.1 | 3.5550 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_25b1984f_auto-nocaps-simdna` | 6.8 | 0.0001 |
| `t-64k` | 65,536 | `rust_1.13.1_default-caps-simdna` | 32.5 | 0.0005 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 52.3 | 0.0008 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-in-caps-simdna` | 236,529.1 | 3.6091 |
| `t-64k` | 65,536 | `pcrec_25b1984f_vm-caps-simdna` | 233,743.1 | 3.5666 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 499.8 | 499.7 | 501.2 | 0.7 | 1.000x | 1.000x | 75 | 6.7 | 8.9 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 499.9 | 499.7 | 501.0 | 0.5 | 1.000x | 1.000x | 75 | 6.7 | 8.9 | 100% |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,484.0 | 1,480.6 | 1,486.5 | 2.2 | 2.969x | 2.969x | 75 | 19.8 | 27.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 1,796.6 | 1,793.0 | 1,797.9 | 1.8 | 3.595x | 3.595x | 75 | 24.0 | 16.3 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,930.6 | 2,928.3 | 2,963.7 | 13.3 | 5.864x | 5.864x | 75 | 39.1 | 58.6 | 100% |
| 6 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 6,162.0 | 6,159.9 | 6,183.1 | 8.7 | 12.330x | 12.330x | 75 | 82.2 | 18.1 | 100% |
| 7 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 6,177.2 | 6,173.7 | 6,179.0 | 1.8 | 12.360x | 12.360x | 75 | 82.4 | 17.3 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 75 | 93% | -2:PCREC_ERR_STEPS×5 (smallest: v-uuid-badnibble, 36 B) | 0 | `sd-empty-alt-hit` (gave-up), `sd-empty-alt-miss` (gave-up), `sec-github-pat` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up) |
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 75 | 93% | -2:PCREC_ERR_STEPS×5 (smallest: v-uuid-badnibble, 36 B) | 0 | `sd-empty-alt-hit` (gave-up), `sd-empty-alt-miss` (gave-up), `sec-github-pat` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 75 | 97% | -17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `rust_1.13.1_default-caps-simdna` | 75 | 97% | 0 | 10 | `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_25b1984f_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1463025 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1484232 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-flat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-flat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-xflag` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `date-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `date-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `email-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `evil-alt-nested` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `evil-alt-nested` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,914 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,019 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic-removed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_auto-nocaps-simdna` / `numeric-id-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-list-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `trim-nested-star` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `trim-nested-star` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-datefinder-alternation` / `plain`: engine=dfa, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1419282 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 257,968 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1440489 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 258,077 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-github-pat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_vm-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 970 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,073 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_25b1984f_vm-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=5/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,957 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=5/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 970 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,073 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_25b1984f_vm-in-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-number-extended` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,957 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,112 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 301,221 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
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
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 200,523,582.0 | 198,153,961.0 | 209,390,578.0 | 4,405,441.5 | 5 | 27,360 | 24,163 | 23,932 | 0.022 | compiled=5 | 2,889,712.0 | 197,192,938.0 | 106,750.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 206,609,816.0 | 199,950,499.0 | 210,691,092.0 | 4,315,445.7 | 5 | 27,360 | 24,381 | 24,150 | 0.021 | compiled=5 | 2,262,669.0 | 204,462,568.0 | 204,011.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 206,955,439.0 | 197,019,332.0 | 215,588,187.0 | 5,939,633.1 | 5 | 27,360 | 24,163 | 23,932 | 0.029 | compiled=5 | 3,003,374.0 | 204,025,576.0 | 112,451.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 205,908,800.0 | 196,122,603.0 | 209,664,862.0 | 5,333,033.9 | 5 | 27,360 | 24,381 | 24,150 | 0.026 (max is trial 1) | compiled=5 | 2,823,932.0 | 202,981,008.0 | 103,860.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 203,678,233.0 | 199,256,685.0 | 207,606,607.0 | 3,298,323.0 | 5 | 27,360 | 24,161 | 23,930 | 0.016 (max is trial 1) | compiled=5 | 4,404,908.0 | 198,850,542.0 | 207,052.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 207,165,666.0 | 190,073,287.0 | 210,809,319.0 | 7,336,285.6 | 5 | 27,360 | 24,379 | 24,148 | 0.035 | compiled=5 | 2,851,179.0 | 204,176,177.0 | 191,581.0 |
| `balanced-parens-rec` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 204,033,246.0 | 200,526,595.0 | 208,725,293.0 | 3,263,923.1 | 5 | 27,360 | 24,161 | 23,930 | 0.016 | compiled=5 | 2,889,797.0 | 199,203,488.0 | 196,001.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 207,933,559.0 | 207,275,685.0 | 211,699,689.0 | 1,893,316.1 | 5 | 27,360 | 24,379 | 24,148 | 0.009 | compiled=5 | 2,914,867.0 | 204,919,821.0 | 101,981.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,984,952.0 | 150,061,898.0 | 154,920,897.0 | 1,768,780.9 | 5 | 23,376 | 15,211 | 12,826 | 0.012 | compiled=5 | 4,323,067.0 | 146,078,482.0 | 196,761.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 137,695,806.0 | 128,088,939.0 | 147,158,936.0 | 6,165,465.8 | 5 | 23,296 | 14,664 | 12,279 | 0.045 (max is trial 1) | compiled=5 | 4,327,198.0 | 131,612,242.0 | 197,471.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 144,896,327.0 | 130,081,506.0 | 148,378,539.0 | 6,457,889.8 | 5 | 23,376 | 15,211 | 12,826 | 0.045 | compiled=5 | 4,293,468.0 | 140,495,999.0 | 112,740.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 144,834,856.0 | 143,240,260.0 | 155,142,768.0 | 4,316,564.6 | 5 | 23,296 | 14,664 | 12,279 | 0.030 | compiled=5 | 4,368,677.0 | 140,473,299.0 | 171,991.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 187,232,748.0 | 179,721,410.0 | 189,436,571.0 | 3,624,854.4 | 5 | 27,200 | 21,142 | 21,142 | 0.019 | compiled=5 | 2,859,028.0 | 184,311,990.0 | 190,951.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 180,254,022.0 | 178,581,003.0 | 190,645,060.0 | 4,681,902.5 | 5 | 27,200 | 21,255 | 21,255 | 0.026 | compiled=5 | 2,891,388.0 | 177,262,924.0 | 99,710.0 |
| `base10num-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 186,364,393.0 | 179,055,978.0 | 191,202,601.0 | 4,112,172.4 | 5 | 27,200 | 21,142 | 21,142 | 0.022 | compiled=5 | 2,864,647.0 | 183,273,964.0 | 102,051.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 185,946,279.0 | 183,289,513.0 | 192,177,296.0 | 3,026,989.2 | 5 | 27,200 | 21,255 | 21,255 | 0.016 | compiled=5 | 2,881,566.0 | 182,964,042.0 | 100,671.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 219,350,269.0 | 210,839,564.0 | 237,615,942.0 | 8,869,482.0 | 5 | 27,400 | 24,958 | 24,643 | 0.040 | compiled=5 | 2,871,152.0 | 215,244,441.0 | 188,421.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 217,378,780.0 | 205,818,224.0 | 217,918,793.0 | 4,716,931.8 | 5 | 27,400 | 25,073 | 24,758 | 0.022 | compiled=5 | 2,897,052.0 | 214,287,657.0 | 187,810.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 216,650,464.0 | 211,131,953.0 | 218,963,975.0 | 2,584,826.8 | 5 | 27,400 | 24,959 | 24,643 | 0.012 | compiled=5 | 2,913,843.0 | 213,531,080.0 | 107,461.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 208,048,438.0 | 198,525,304.0 | 209,008,306.0 | 3,892,031.5 | 5 | 27,400 | 25,074 | 24,758 | 0.019 (max is trial 1) | compiled=5 | 3,100,415.0 | 204,770,862.0 | 111,841.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 216,833,717.0 | 214,942,435.0 | 219,840,857.0 | 1,585,896.0 | 5 | 27,400 | 24,956 | 24,641 | 0.007 | compiled=5 | 2,926,828.0 | 213,805,598.0 | 104,320.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 217,260,421.0 | 207,805,490.0 | 227,031,733.0 | 7,008,488.4 | 5 | 27,400 | 25,071 | 24,756 | 0.032 | compiled=5 | 2,870,858.0 | 214,273,891.0 | 114,991.0 |
| `bracket-array-define` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 218,226,889.0 | 211,774,281.0 | 222,266,463.0 | 3,394,677.2 | 5 | 27,400 | 24,956 | 24,641 | 0.016 | compiled=5 | 2,873,407.0 | 215,206,721.0 | 184,801.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 216,930,761.0 | 209,601,008.0 | 217,546,996.0 | 3,006,136.8 | 5 | 27,400 | 25,071 | 24,756 | 0.014 | compiled=5 | 2,954,048.0 | 213,791,852.0 | 108,531.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 352,488,776.0 | 341,015,130.0 | 364,274,225.0 | 8,756,377.0 | 5 | 31,808 | 34,144 | 25,545 | 0.025 (max is trial 1) | compiled=5 | 4,937,920.0 | 347,458,017.0 | 101,890.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 353,830,183.0 | 351,419,892.0 | 358,597,501.0 | 2,389,013.6 | 5 | 31,856 | 33,865 | 26,353 | 0.007 | compiled=5 | 4,844,260.0 | 349,008,912.0 | 107,040.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 176,565,072.0 | 166,183,430.0 | 179,080,481.0 | 4,467,435.1 | 5 | 27,832 | 28,185 | 15,235 | 0.025 | compiled=5 | 4,957,959.0 | 170,546,824.0 | 102,201.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 167,924,544.0 | 162,693,904.0 | 180,947,126.0 | 6,399,196.0 | 5 | 27,888 | 26,435 | 15,884 | 0.038 | compiled=5 | 3,349,086.0 | 161,739,985.0 | 101,201.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 312,489,569.0 | 305,097,822.0 | 317,072,979.0 | 4,328,752.4 | 5 | 27,200 | 21,230 | 20,768 | 0.014 | compiled=5 | 2,973,679.0 | 309,439,300.0 | 110,231.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 319,094,602.0 | 317,220,180.0 | 331,339,710.0 | 5,656,686.7 | 5 | 27,200 | 21,341 | 20,879 | 0.018 | compiled=5 | 2,872,568.0 | 316,148,283.0 | 192,622.0 |
| `codegrammar-flat` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 312,409,771.0 | 312,032,829.0 | 313,521,847.0 | 617,401.5 | 5 | 27,200 | 21,230 | 20,768 | 0.002 | compiled=5 | 2,973,978.0 | 308,947,020.0 | 109,870.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 318,482,877.0 | 317,566,822.0 | 321,096,042.0 | 1,222,506.1 | 5 | 27,200 | 21,341 | 20,879 | 0.004 (max is trial 1) | compiled=5 | 2,914,587.0 | 315,381,358.0 | 198,731.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 348,215,149.0 | 342,826,059.0 | 358,132,319.0 | 5,792,066.1 | 5 | 31,848 | 34,470 | 25,792 | 0.017 | compiled=5 | 5,037,150.0 | 345,728,119.0 | 111,450.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 360,765,410.0 | 348,301,040.0 | 366,985,225.0 | 6,241,497.8 | 5 | 31,896 | 34,195 | 26,604 | 0.017 | compiled=5 | 3,357,403.0 | 354,982,467.0 | 112,711.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 175,247,311.0 | 167,551,680.0 | 176,614,782.0 | 3,427,118.1 | 5 | 27,872 | 28,462 | 15,432 | 0.020 | compiled=5 | 3,420,847.0 | 171,722,713.0 | 116,931.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 171,163,999.0 | 165,364,513.0 | 173,799,350.0 | 2,781,931.1 | 5 | 27,928 | 26,714 | 16,083 | 0.016 | compiled=5 | 3,392,526.0 | 167,652,092.0 | 108,631.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 312,070,566.0 | 305,408,084.0 | 319,043,070.0 | 4,706,484.6 | 5 | 27,240 | 21,556 | 21,015 | 0.015 | compiled=5 | 2,908,438.0 | 310,034,314.0 | 201,541.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 319,363,274.0 | 315,322,928.0 | 328,859,614.0 | 4,517,946.3 | 5 | 27,240 | 21,671 | 21,130 | 0.014 | compiled=5 | 2,897,728.0 | 316,347,525.0 | 106,801.0 |
| `codegrammar-xflag` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 312,486,081.0 | 303,104,496.0 | 314,589,055.0 | 4,251,797.8 | 5 | 27,240 | 21,556 | 21,015 | 0.014 (max is trial 1) | compiled=5 | 2,911,297.0 | 309,479,504.0 | 100,300.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 318,574,986.0 | 305,058,219.0 | 337,938,800.0 | 12,110,397.2 | 5 | 27,240 | 21,671 | 21,130 | 0.038 | compiled=5 | 2,916,098.0 | 315,593,719.0 | 195,771.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 217,758,342.0 | 212,308,169.0 | 228,245,443.0 | 5,495,865.4 | 5 | 31,824 | 31,432 | 25,801 | 0.025 (max is trial 1) | compiled=5 | 3,189,883.0 | 212,350,459.0 | 121,880.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 226,411,937.0 | 221,825,498.0 | 236,825,118.0 | 4,948,704.0 | 5 | 31,920 | 33,458 | 27,209 | 0.022 | compiled=5 | 3,293,443.0 | 222,984,533.0 | 113,370.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 220,581,076.0 | 214,749,821.0 | 224,327,985.0 | 3,325,356.0 | 5 | 31,824 | 31,432 | 25,801 | 0.015 | compiled=5 | 3,177,245.0 | 217,280,079.0 | 99,651.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 226,196,700.0 | 220,842,916.0 | 229,078,342.0 | 3,011,425.6 | 5 | 31,920 | 33,458 | 27,209 | 0.013 | compiled=5 | 3,235,875.0 | 222,862,064.0 | 208,701.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 195,467,341.0 | 179,957,131.0 | 198,850,933.0 | 6,868,071.0 | 5 | 27,288 | 21,621 | 21,390 | 0.035 | compiled=5 | 2,854,198.0 | 192,531,632.0 | 108,171.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 196,219,597.0 | 194,342,483.0 | 199,651,268.0 | 1,744,412.5 | 5 | 27,288 | 21,734 | 21,503 | 0.009 | compiled=5 | 2,971,249.0 | 193,041,806.0 | 108,551.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 197,592,639.0 | 188,790,117.0 | 198,107,421.0 | 4,062,283.7 | 5 | 27,288 | 21,621 | 21,390 | 0.021 | compiled=5 | 2,978,847.0 | 194,491,230.0 | 209,342.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 197,484,858.0 | 186,884,944.0 | 205,322,683.0 | 5,925,101.8 | 5 | 27,288 | 21,734 | 21,503 | 0.030 | compiled=5 | 2,889,137.0 | 194,413,350.0 | 99,150.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 262,306,922.0 | 257,680,614.0 | 266,003,417.0 | 2,822,881.7 | 5 | 31,696 | 32,258 | 30,232 | 0.011 | compiled=5 | 3,097,383.0 | 257,152,621.0 | 195,191.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 256,055,486.0 | 249,532,920.0 | 256,280,978.0 | 2,828,054.0 | 5 | 31,696 | 32,186 | 30,160 | 0.011 | compiled=5 | 3,134,333.0 | 252,871,744.0 | 113,690.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 142,587,565.0 | 134,057,899.0 | 148,740,853.0 | 4,782,942.5 | 5 | 23,184 | 13,194 | 11,399 | 0.034 | compiled=5 | 2,808,862.0 | 140,668,490.0 | 100,531.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 139,276,718.0 | 128,315,294.0 | 144,365,310.0 | 5,307,254.5 | 5 | 23,184 | 13,017 | 11,222 | 0.038 | compiled=5 | 2,803,962.0 | 134,774,254.0 | 109,720.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 245,124,658.0 | 239,460,422.0 | 250,213,181.0 | 3,962,867.1 | 5 | 27,400 | 27,830 | 27,599 | 0.016 (max is trial 1) | compiled=5 | 2,932,749.0 | 242,087,599.0 | 106,680.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 243,784,111.0 | 239,887,045.0 | 245,564,340.0 | 2,127,144.9 | 5 | 27,400 | 27,943 | 27,712 | 0.009 | compiled=5 | 2,897,418.0 | 240,793,761.0 | 107,951.0 |
| `date-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 244,367,703.0 | 235,479,419.0 | 248,021,733.0 | 4,421,093.0 | 5 | 27,400 | 27,830 | 27,599 | 0.018 (max is trial 1) | compiled=5 | 2,973,858.0 | 241,206,854.0 | 101,831.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 244,518,083.0 | 235,828,392.0 | 246,034,721.0 | 4,072,737.4 | 5 | 27,400 | 27,943 | 27,712 | 0.017 | compiled=5 | 3,015,627.0 | 241,381,015.0 | 185,181.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 216,255,105.0 | 211,467,796.0 | 217,298,399.0 | 2,162,006.4 | 5 | 27,328 | 23,220 | 22,758 | 0.010 | compiled=5 | 2,855,622.0 | 213,289,033.0 | 114,750.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 212,980,471.0 | 207,292,819.0 | 219,840,420.0 | 5,229,634.5 | 5 | 27,328 | 23,333 | 22,871 | 0.025 | compiled=5 | 3,448,924.0 | 207,938,052.0 | 98,651.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 212,108,490.0 | 206,729,108.0 | 217,108,589.0 | 3,755,690.4 | 5 | 27,328 | 23,202 | 22,740 | 0.018 | compiled=5 | 2,892,313.0 | 207,349,082.0 | 109,911.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 214,293,366.0 | 201,978,430.0 | 216,192,751.0 | 5,092,476.7 | 5 | 27,328 | 23,315 | 22,853 | 0.024 (max is trial 1) | compiled=5 | 2,885,363.0 | 211,189,512.0 | 206,541.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 207,200,206.0 | 201,093,817.0 | 219,743,545.0 | 6,864,352.9 | 5 | 27,328 | 23,218 | 22,756 | 0.033 | compiled=5 | 2,850,708.0 | 205,240,664.0 | 199,811.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 213,553,397.0 | 207,544,408.0 | 214,502,223.0 | 2,587,315.6 | 5 | 27,328 | 23,331 | 22,869 | 0.012 | compiled=5 | 2,865,659.0 | 210,575,877.0 | 184,971.0 |
| `doubled-word` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 214,959,790.0 | 207,786,727.0 | 222,170,902.0 | 5,299,860.2 | 5 | 27,328 | 23,218 | 22,756 | 0.025 | compiled=5 | 2,929,047.0 | 211,859,752.0 | 103,721.0 |
| `doubled-word` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 214,215,464.0 | 213,683,892.0 | 214,525,118.0 | 272,846.9 | 5 | 27,328 | 23,331 | 22,869 | 0.001 | compiled=5 | 2,884,677.0 | 211,254,888.0 | 108,761.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 227,871,793.0 | 222,476,071.0 | 230,091,561.0 | 2,598,575.6 | 5 | 27,448 | 25,774 | 25,312 | 0.011 | compiled=5 | 2,911,812.0 | 224,866,320.0 | 191,071.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 229,743,779.0 | 220,792,094.0 | 232,318,191.0 | 4,867,924.8 | 5 | 27,448 | 25,887 | 25,425 | 0.021 | compiled=5 | 3,046,783.0 | 224,716,950.0 | 113,711.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 228,806,930.0 | 222,133,718.0 | 235,617,013.0 | 4,578,460.9 | 5 | 27,448 | 25,756 | 25,294 | 0.020 | compiled=5 | 2,890,422.0 | 225,778,357.0 | 112,431.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 220,617,367.0 | 213,210,540.0 | 228,170,365.0 | 5,287,998.0 | 5 | 27,448 | 25,869 | 25,407 | 0.024 | compiled=5 | 2,946,143.0 | 217,298,330.0 | 109,011.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 228,755,554.0 | 224,362,176.0 | 231,060,829.0 | 2,200,888.5 | 5 | 27,448 | 25,772 | 25,310 | 0.010 | compiled=5 | 2,946,889.0 | 225,730,594.0 | 101,171.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 223,080,398.0 | 221,352,957.0 | 233,259,342.0 | 4,540,445.9 | 5 | 27,448 | 25,885 | 25,423 | 0.020 | compiled=5 | 2,860,618.0 | 218,815,020.0 | 194,351.0 |
| `dup-param-detect` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 225,062,457.0 | 220,500,902.0 | 230,163,668.0 | 3,507,194.9 | 5 | 27,448 | 25,772 | 25,310 | 0.016 | compiled=5 | 2,959,047.0 | 220,348,411.0 | 190,951.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 228,520,849.0 | 227,386,073.0 | 230,117,178.0 | 1,040,096.3 | 5 | 27,448 | 25,885 | 25,423 | 0.005 (max is trial 1) | compiled=5 | 2,763,496.0 | 225,438,171.0 | 100,851.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 204,407,808.0 | 201,743,516.0 | 212,699,941.0 | 3,991,618.9 | 5 | 31,536 | 25,764 | 23,691 | 0.020 | compiled=5 | 2,940,292.0 | 199,934,969.0 | 187,921.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 197,964,371.0 | 189,560,847.0 | 198,532,173.0 | 3,561,929.9 | 5 | 31,536 | 26,182 | 24,038 | 0.018 | compiled=5 | 2,985,592.0 | 192,978,791.0 | 108,800.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 203,060,729.0 | 197,685,517.0 | 217,367,231.0 | 6,581,018.6 | 5 | 31,536 | 25,764 | 23,691 | 0.032 (max is trial 1) | compiled=5 | 2,980,324.0 | 199,980,364.0 | 101,461.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 199,577,762.0 | 195,827,383.0 | 202,238,211.0 | 2,054,053.6 | 5 | 31,536 | 26,182 | 24,038 | 0.010 | compiled=5 | 2,999,474.0 | 196,370,996.0 | 194,072.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 192,557,843.0 | 187,414,639.0 | 201,046,686.0 | 4,958,869.8 | 5 | 27,280 | 22,104 | 21,642 | 0.026 | compiled=5 | 2,688,767.0 | 190,680,540.0 | 114,310.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 190,400,089.0 | 187,465,129.0 | 197,880,356.0 | 3,998,944.1 | 5 | 27,240 | 22,217 | 21,755 | 0.021 | compiled=5 | 3,138,180.0 | 187,535,280.0 | 101,321.0 |
| `email-local-nodup` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 195,015,732.0 | 186,567,994.0 | 201,875,033.0 | 5,565,740.1 | 5 | 27,280 | 22,104 | 21,642 | 0.029 | compiled=5 | 2,899,837.0 | 191,888,604.0 | 110,031.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 196,166,609.0 | 188,689,336.0 | 198,723,295.0 | 3,649,485.9 | 5 | 27,240 | 22,217 | 21,755 | 0.019 | compiled=5 | 2,909,387.0 | 192,891,810.0 | 186,671.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 220,805,974.0 | 212,443,760.0 | 222,316,390.0 | 3,843,313.9 | 5 | 31,648 | 27,640 | 25,694 | 0.017 | compiled=5 | 3,012,622.0 | 215,834,284.0 | 189,361.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 222,440,241.0 | 221,390,276.0 | 225,154,391.0 | 1,292,723.8 | 5 | 31,648 | 28,071 | 26,041 | 0.006 | compiled=5 | 2,979,022.0 | 218,898,536.0 | 114,840.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 139,845,513.0 | 131,971,352.0 | 141,786,589.0 | 4,065,799.4 | 5 | 23,184 | 12,699 | 10,984 | 0.029 | compiled=5 | 2,823,362.0 | 135,335,218.0 | 107,661.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 138,486,493.0 | 130,138,468.0 | 141,834,509.0 | 4,110,054.2 | 5 | 23,184 | 13,025 | 11,226 | 0.030 | compiled=5 | 2,811,572.0 | 135,573,880.0 | 187,631.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 210,448,097.0 | 200,719,874.0 | 213,642,468.0 | 4,544,870.4 | 5 | 27,360 | 23,711 | 23,480 | 0.022 | compiled=5 | 2,926,679.0 | 207,405,317.0 | 115,671.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 211,285,312.0 | 207,137,285.0 | 218,514,899.0 | 3,716,601.0 | 5 | 27,360 | 23,824 | 23,593 | 0.018 | compiled=5 | 2,892,308.0 | 208,291,113.0 | 106,631.0 |
| `email-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 208,251,871.0 | 202,153,695.0 | 221,947,780.0 | 7,204,818.7 | 5 | 27,360 | 23,711 | 23,480 | 0.035 (max is trial 1) | compiled=5 | 2,877,606.0 | 205,202,382.0 | 192,981.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 212,245,733.0 | 204,910,571.0 | 219,635,827.0 | 5,346,500.9 | 5 | 27,360 | 23,824 | 23,593 | 0.025 | compiled=5 | 2,903,087.0 | 207,457,236.0 | 185,911.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 214,267,107.0 | 210,507,412.0 | 217,496,670.0 | 2,223,625.5 | 5 | 27,360 | 24,177 | 24,177 | 0.010 | compiled=5 | 2,875,802.0 | 210,945,644.0 | 100,760.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 213,358,564.0 | 207,824,411.0 | 214,150,558.0 | 2,275,228.6 | 5 | 27,360 | 24,290 | 24,290 | 0.011 (max is trial 1) | compiled=5 | 2,867,222.0 | 209,489,228.0 | 200,551.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 125,313,989.0 | 124,117,180.0 | 136,188,586.0 | 4,507,724.3 | 5 | 23,144 | 12,686 | 11,075 | 0.036 | compiled=5 | 2,807,052.0 | 122,376,897.0 | 193,722.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 135,621,391.0 | 122,263,208.0 | 139,664,943.0 | 6,887,931.0 | 5 | 23,104 | 12,509 | 10,898 | 0.051 | compiled=5 | 2,783,082.0 | 132,694,148.0 | 103,251.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 213,851,508.0 | 198,127,998.0 | 216,462,735.0 | 6,622,209.8 | 5 | 27,360 | 24,158 | 24,158 | 0.031 | compiled=5 | 2,896,059.0 | 210,872,479.0 | 100,751.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 213,517,626.0 | 206,258,469.0 | 214,039,580.0 | 3,076,255.1 | 5 | 27,360 | 24,271 | 24,271 | 0.014 | compiled=5 | 2,882,428.0 | 210,535,277.0 | 101,561.0 |
| `evil-alt-nested` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 213,098,358.0 | 206,039,687.0 | 220,487,982.0 | 5,176,102.9 | 5 | 27,360 | 24,158 | 24,158 | 0.024 | compiled=5 | 2,902,877.0 | 210,146,291.0 | 173,241.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 212,804,546.0 | 197,253,676.0 | 214,164,706.0 | 6,447,646.6 | 5 | 27,360 | 24,271 | 24,271 | 0.030 | compiled=5 | 2,940,457.0 | 209,813,539.0 | 111,521.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 148,931,652.0 | 142,721,758.0 | 155,352,518.0 | 4,011,152.6 | 5 | 27,608 | 19,438 | 13,315 | 0.027 | compiled=5 | 3,102,162.0 | 144,952,806.0 | 100,230.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 161,269,753.0 | 159,488,305.0 | 163,510,023.0 | 1,673,624.7 | 5 | 27,752 | 22,398 | 15,332 | 0.010 (max is trial 1) | compiled=5 | 3,174,013.0 | 157,683,028.0 | 187,341.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,553,674.0 | 142,961,619.0 | 157,345,221.0 | 6,194,964.2 | 5 | 27,608 | 19,438 | 13,315 | 0.043 | compiled=5 | 3,156,275.0 | 141,341,196.0 | 111,740.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 160,129,852.0 | 156,379,143.0 | 161,184,561.0 | 1,874,829.4 | 5 | 27,752 | 22,398 | 15,332 | 0.012 | compiled=5 | 3,232,415.0 | 156,727,126.0 | 198,492.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 164,224,201.0 | 158,212,082.0 | 173,562,281.0 | 5,780,116.5 | 5 | 23,104 | 19,314 | 19,314 | 0.035 | compiled=5 | 2,800,348.0 | 161,935,086.0 | 101,841.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 172,696,266.0 | 170,012,329.0 | 175,408,703.0 | 1,785,781.7 | 5 | 23,104 | 19,427 | 19,427 | 0.010 | compiled=5 | 2,797,988.0 | 169,798,766.0 | 109,961.0 |
| `file-ext-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 172,852,713.0 | 163,690,719.0 | 175,136,587.0 | 4,692,772.1 | 5 | 23,104 | 19,314 | 19,314 | 0.027 (max is trial 1) | compiled=5 | 2,855,066.0 | 169,956,176.0 | 108,610.0 |
| `file-ext-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 167,299,912.0 | 164,999,767.0 | 177,970,132.0 | 4,986,851.2 | 5 | 23,104 | 19,427 | 19,427 | 0.030 | compiled=5 | 3,037,998.0 | 162,769,814.0 | 195,041.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 234,986,422.0 | 232,571,702.0 | 235,575,024.0 | 1,036,258.2 | 5 | 31,752 | 32,214 | 27,065 | 0.004 | compiled=5 | 3,254,233.0 | 231,541,557.0 | 110,461.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 234,734,840.0 | 232,405,780.0 | 238,886,408.0 | 2,117,275.9 | 5 | 31,848 | 33,056 | 27,598 | 0.009 (max is trial 1) | compiled=5 | 3,241,194.0 | 231,373,797.0 | 123,890.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 236,263,047.0 | 228,101,074.0 | 242,117,825.0 | 4,829,728.3 | 5 | 31,752 | 32,214 | 27,065 | 0.020 | compiled=5 | 3,228,385.0 | 233,915,270.0 | 108,021.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 228,056,744.0 | 225,352,673.0 | 250,977,323.0 | 9,494,373.1 | 5 | 31,848 | 33,056 | 27,598 | 0.042 (max is trial 1) | compiled=5 | 3,275,165.0 | 224,901,160.0 | 199,202.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 200,454,472.0 | 192,907,575.0 | 206,412,530.0 | 4,429,803.0 | 5 | 27,288 | 22,154 | 21,923 | 0.022 | compiled=5 | 2,892,909.0 | 197,474,634.0 | 109,450.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 202,900,410.0 | 196,830,039.0 | 226,272,607.0 | 10,297,823.4 | 5 | 27,288 | 22,267 | 22,036 | 0.051 | compiled=5 | 2,857,768.0 | 199,913,019.0 | 100,330.0 |
| `float-literal-bound` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 200,967,417.0 | 192,038,715.0 | 202,195,915.0 | 3,707,148.5 | 5 | 27,288 | 22,154 | 21,923 | 0.018 (max is trial 1) | compiled=5 | 2,876,237.0 | 197,425,937.0 | 189,141.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 203,020,309.0 | 199,371,048.0 | 206,986,632.0 | 2,415,364.1 | 5 | 27,288 | 22,267 | 22,036 | 0.012 | compiled=5 | 2,900,307.0 | 199,969,372.0 | 194,421.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 148,590,642.0 | 147,849,748.0 | 154,967,237.0 | 2,606,899.1 | 5 | 27,608 | 18,295 | 13,298 | 0.018 | compiled=5 | 2,996,583.0 | 145,484,949.0 | 103,410.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,002,928.0 | 152,874,979.0 | 162,510,748.0 | 3,269,148.8 | 5 | 27,752 | 20,638 | 15,315 | 0.020 | compiled=5 | 3,339,564.0 | 156,901,995.0 | 105,271.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 150,608,838.0 | 141,220,834.0 | 157,588,982.0 | 6,382,652.8 | 5 | 27,608 | 18,295 | 13,298 | 0.042 | compiled=5 | 2,997,963.0 | 147,270,762.0 | 103,641.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 160,623,998.0 | 151,023,370.0 | 165,417,215.0 | 5,695,383.6 | 5 | 27,752 | 20,638 | 15,315 | 0.035 | compiled=5 | 3,013,213.0 | 157,372,962.0 | 110,311.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 140,762,951.0 | 129,847,261.0 | 143,115,535.0 | 5,054,979.1 | 5 | 23,072 | 17,838 | 17,838 | 0.036 | compiled=5 | 2,740,338.0 | 137,919,313.0 | 101,490.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 133,589,764.0 | 130,345,614.0 | 142,725,284.0 | 4,962,026.5 | 5 | 23,072 | 17,949 | 17,949 | 0.037 | compiled=5 | 2,783,407.0 | 129,310,347.0 | 98,470.0 |
| `floor-byte` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 137,276,314.0 | 120,045,544.0 | 141,449,598.0 | 7,814,920.0 | 5 | 23,072 | 17,838 | 17,838 | 0.057 | compiled=5 | 2,810,737.0 | 132,765,658.0 | 99,700.0 |
| `floor-byte` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 138,421,811.0 | 126,085,258.0 | 142,780,426.0 | 5,708,970.2 | 5 | 23,072 | 17,949 | 17,949 | 0.041 | compiled=5 | 2,775,406.0 | 135,431,973.0 | 109,410.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 169,274,315.0 | 166,274,553.0 | 179,513,647.0 | 4,508,579.4 | 5 | 23,216 | 24,544 | 18,238 | 0.027 (max is trial 1) | compiled=5 | 3,124,153.0 | 166,045,462.0 | 110,760.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 164,915,307.0 | 160,859,581.0 | 170,167,299.0 | 3,068,669.1 | 5 | 27,744 | 23,246 | 16,119 | 0.019 | compiled=5 | 3,141,663.0 | 161,585,544.0 | 100,800.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 169,182,422.0 | 166,199,180.0 | 172,994,564.0 | 2,476,484.9 | 5 | 23,216 | 24,544 | 18,238 | 0.015 | compiled=5 | 3,174,635.0 | 163,650,630.0 | 194,822.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 166,435,123.0 | 156,723,916.0 | 170,750,565.0 | 4,918,322.4 | 5 | 27,744 | 23,246 | 16,119 | 0.030 | compiled=5 | 3,162,375.0 | 163,169,167.0 | 103,581.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 163,411,685.0 | 154,185,967.0 | 165,772,130.0 | 4,622,478.9 | 5 | 23,072 | 18,383 | 18,383 | 0.028 | compiled=5 | 2,790,678.0 | 160,547,007.0 | 101,031.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 167,469,111.0 | 163,408,396.0 | 169,571,063.0 | 2,287,720.8 | 5 | 23,072 | 18,494 | 18,494 | 0.014 | compiled=5 | 2,771,908.0 | 164,488,882.0 | 99,391.0 |
| `high-byte-run` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 163,557,059.0 | 155,750,053.0 | 169,073,320.0 | 4,333,067.5 | 5 | 23,072 | 18,383 | 18,383 | 0.026 | compiled=5 | 3,223,369.0 | 158,834,011.0 | 188,721.0 |
| `high-byte-run` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 166,411,236.0 | 159,491,414.0 | 167,715,033.0 | 2,975,273.5 | 5 | 23,072 | 18,494 | 18,494 | 0.018 | compiled=5 | 2,851,787.0 | 162,612,783.0 | 111,391.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 169,146,685.0 | 164,942,989.0 | 173,303,881.0 | 3,119,757.6 | 5 | 32,424 | 22,055 | 16,739 | 0.018 | compiled=5 | 4,457,338.0 | 164,343,245.0 | 107,310.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 165,546,600.0 | 155,842,591.0 | 169,802,567.0 | 4,833,295.7 | 5 | 32,224 | 21,133 | 15,817 | 0.029 | compiled=5 | 4,547,548.0 | 159,711,766.0 | 189,331.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 166,656,874.0 | 152,258,027.0 | 169,517,807.0 | 6,568,361.7 | 5 | 32,424 | 22,055 | 16,739 | 0.039 | compiled=5 | 4,504,988.0 | 162,054,896.0 | 112,351.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,134,009.0 | 152,732,648.0 | 164,295,646.0 | 3,909,317.6 | 5 | 32,224 | 21,133 | 15,817 | 0.025 | compiled=5 | 4,493,939.0 | 155,767,150.0 | 196,300.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 262,159,337.0 | 253,794,852.0 | 264,134,370.0 | 3,634,076.3 | 5 | 27,200 | 30,904 | 30,904 | 0.014 | compiled=5 | 4,460,379.0 | 257,561,368.0 | 112,691.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 260,477,927.0 | 253,320,032.0 | 262,160,757.0 | 3,165,521.5 | 5 | 27,200 | 31,017 | 31,017 | 0.012 | compiled=5 | 4,527,779.0 | 255,752,096.0 | 189,802.0 |
| `ipv4-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 254,892,384.0 | 251,133,610.0 | 262,043,884.0 | 4,185,755.4 | 5 | 27,200 | 30,904 | 30,904 | 0.016 | compiled=5 | 4,331,035.0 | 250,258,957.0 | 109,090.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 259,610,992.0 | 252,393,528.0 | 265,130,034.0 | 4,211,142.2 | 5 | 27,200 | 31,017 | 31,017 | 0.016 (max is trial 1) | compiled=5 | 3,051,748.0 | 256,368,302.0 | 107,260.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 152,642,678.0 | 143,659,712.0 | 159,859,328.0 | 5,147,573.4 | 5 | 27,608 | 20,258 | 13,644 | 0.034 | compiled=5 | 3,109,623.0 | 149,290,854.0 | 196,111.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 167,062,865.0 | 157,878,219.0 | 169,867,668.0 | 4,261,945.7 | 5 | 27,752 | 24,563 | 15,737 | 0.026 | compiled=5 | 3,412,263.0 | 163,283,071.0 | 114,811.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 145,509,358.0 | 143,910,895.0 | 155,809,279.0 | 4,371,515.8 | 5 | 27,608 | 20,258 | 13,644 | 0.030 | compiled=5 | 3,174,775.0 | 141,915,921.0 | 108,261.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 167,708,533.0 | 164,695,408.0 | 172,727,121.0 | 2,866,430.0 | 5 | 27,752 | 24,563 | 15,737 | 0.017 | compiled=5 | 3,362,936.0 | 161,896,957.0 | 198,462.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 172,436,834.0 | 164,248,721.0 | 174,330,316.0 | 4,465,020.6 | 5 | 23,104 | 19,790 | 19,790 | 0.026 | compiled=5 | 2,799,678.0 | 168,762,370.0 | 106,941.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 174,230,095.0 | 168,516,079.0 | 177,014,222.0 | 2,969,520.9 | 5 | 23,104 | 19,903 | 19,903 | 0.017 | compiled=5 | 2,904,899.0 | 171,051,635.0 | 108,131.0 |
| `keyword-prefix-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 162,785,693.0 | 162,635,883.0 | 172,545,522.0 | 3,871,517.0 | 5 | 23,104 | 19,790 | 19,790 | 0.024 | compiled=5 | 2,808,017.0 | 159,930,717.0 | 100,340.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 175,468,729.0 | 158,001,947.0 | 176,758,495.0 | 7,089,338.5 | 5 | 23,104 | 19,903 | 19,903 | 0.040 | compiled=5 | 2,847,437.0 | 172,285,970.0 | 113,971.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 319,768,794.0 | 312,976,756.0 | 323,870,951.0 | 3,498,582.8 | 5 | 82,840 | 62,375 | 42,442 | 0.011 | compiled=5 | 6,455,156.0 | 311,252,630.0 | 121,100.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 318,930,271.0 | 313,382,558.0 | 320,524,578.0 | 2,594,980.3 | 5 | 82,800 | 62,302 | 42,369 | 0.008 | compiled=5 | 5,754,314.0 | 311,915,503.0 | 116,861.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 311,168,100.0 | 303,107,078.0 | 316,984,944.0 | 4,422,833.7 | 5 | 82,840 | 62,067 | 42,134 | 0.014 (max is trial 1) | compiled=5 | 5,389,232.0 | 305,328,247.0 | 219,391.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 315,736,079.0 | 303,890,271.0 | 317,493,366.0 | 5,046,333.7 | 5 | 82,800 | 61,994 | 42,061 | 0.016 | compiled=5 | 5,305,322.0 | 310,180,696.0 | 256,431.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 247,741,436.0 | 240,127,556.0 | 249,125,753.0 | 4,125,139.7 | 5 | 27,240 | 32,008 | 31,777 | 0.017 (max is trial 1) | compiled=5 | 3,100,309.0 | 244,533,795.0 | 187,501.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 247,300,032.0 | 239,963,835.0 | 250,415,473.0 | 3,598,999.6 | 5 | 27,240 | 32,121 | 31,890 | 0.015 | compiled=5 | 3,097,860.0 | 244,022,211.0 | 111,021.0 |
| `logparse-atomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 247,743,352.0 | 240,431,889.0 | 249,055,798.0 | 3,189,024.9 | 5 | 27,240 | 32,008 | 31,777 | 0.013 | compiled=5 | 3,130,218.0 | 244,527,483.0 | 98,680.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 248,836,959.0 | 248,183,634.0 | 251,708,895.0 | 1,293,383.3 | 5 | 27,240 | 32,121 | 31,890 | 0.005 (max is trial 1) | compiled=5 | 3,256,949.0 | 245,551,409.0 | 101,331.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 308,662,280.0 | 300,940,889.0 | 313,932,631.0 | 4,149,493.0 | 5 | 82,840 | 62,094 | 42,161 | 0.013 | compiled=5 | 5,453,362.0 | 303,096,596.0 | 120,341.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 320,169,067.0 | 313,653,959.0 | 335,169,227.0 | 7,535,238.5 | 5 | 82,800 | 62,021 | 42,088 | 0.024 | compiled=5 | 8,325,284.0 | 314,771,994.0 | 130,331.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 199,460,477.0 | 197,447,579.0 | 203,331,063.0 | 2,243,119.9 | 5 | 74,496 | 39,607 | 19,905 | 0.011 | compiled=5 | 3,468,444.0 | 195,522,502.0 | 213,591.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 196,262,336.0 | 191,927,717.0 | 203,716,655.0 | 4,413,692.3 | 5 | 74,448 | 39,429 | 19,727 | 0.022 (max is trial 1) | compiled=5 | 3,318,113.0 | 192,726,460.0 | 122,150.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 245,627,401.0 | 239,689,225.0 | 248,462,310.0 | 3,344,187.7 | 5 | 27,240 | 31,727 | 31,496 | 0.014 | compiled=5 | 3,084,990.0 | 242,428,031.0 | 179,511.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 245,836,884.0 | 238,341,205.0 | 248,546,951.0 | 3,550,767.5 | 5 | 27,240 | 31,840 | 31,609 | 0.014 | compiled=5 | 3,080,980.0 | 242,671,433.0 | 184,531.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 246,163,781.0 | 239,021,762.0 | 254,822,164.0 | 5,341,380.1 | 5 | 27,240 | 31,727 | 31,496 | 0.022 | compiled=5 | 3,117,139.0 | 242,838,832.0 | 108,941.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 246,070,752.0 | 237,939,825.0 | 250,244,736.0 | 4,225,692.9 | 5 | 27,240 | 31,840 | 31,609 | 0.017 (max is trial 1) | compiled=5 | 3,156,389.0 | 242,763,823.0 | 192,891.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,836,721.0 | 142,660,247.0 | 157,600,559.0 | 5,241,038.3 | 5 | 27,608 | 18,523 | 13,320 | 0.035 | compiled=5 | 3,055,513.0 | 147,708,028.0 | 105,970.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 161,706,134.0 | 160,440,099.0 | 166,587,104.0 | 2,144,562.5 | 5 | 27,752 | 20,942 | 15,337 | 0.013 | compiled=5 | 3,075,642.0 | 158,185,220.0 | 103,740.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,753,964.0 | 141,998,652.0 | 154,340,469.0 | 5,268,139.3 | 5 | 27,608 | 18,523 | 13,320 | 0.037 | compiled=5 | 3,153,745.0 | 140,387,778.0 | 198,432.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 161,744,225.0 | 155,033,593.0 | 163,052,265.0 | 2,960,475.3 | 5 | 27,752 | 20,942 | 15,337 | 0.018 | compiled=5 | 3,114,014.0 | 158,434,659.0 | 189,841.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 166,224,313.0 | 158,572,734.0 | 167,063,699.0 | 3,268,927.1 | 5 | 23,072 | 19,082 | 19,082 | 0.020 | compiled=5 | 2,799,898.0 | 163,376,505.0 | 99,941.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 168,291,548.0 | 152,809,057.0 | 171,395,816.0 | 6,694,246.5 | 5 | 23,072 | 19,194 | 19,194 | 0.040 | compiled=5 | 2,824,718.0 | 165,131,347.0 | 100,201.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 161,617,528.0 | 158,228,707.0 | 166,702,815.0 | 3,101,887.5 | 5 | 23,072 | 19,082 | 19,082 | 0.019 | compiled=5 | 4,170,854.0 | 158,758,380.0 | 111,420.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 167,616,562.0 | 156,941,130.0 | 169,143,290.0 | 4,538,961.5 | 5 | 23,072 | 19,194 | 19,194 | 0.027 | compiled=5 | 2,816,507.0 | 164,698,315.0 | 101,331.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 283,965,930.0 | 274,695,982.0 | 287,168,933.0 | 4,210,209.7 | 5 | 27,360 | 29,849 | 29,618 | 0.015 | compiled=5 | 2,984,582.0 | 280,302,695.0 | 112,481.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 283,811,869.0 | 274,807,143.0 | 287,677,695.0 | 4,688,608.4 | 5 | 27,360 | 29,962 | 29,731 | 0.017 | compiled=5 | 3,003,222.0 | 280,726,647.0 | 98,640.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 283,101,405.0 | 278,554,849.0 | 295,768,764.0 | 6,018,793.1 | 5 | 27,360 | 29,835 | 29,604 | 0.021 | compiled=5 | 3,011,973.0 | 280,027,551.0 | 189,841.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 274,953,191.0 | 264,499,049.0 | 286,831,494.0 | 8,512,537.0 | 5 | 27,360 | 29,948 | 29,717 | 0.031 | compiled=5 | 2,990,624.0 | 271,838,876.0 | 112,101.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 283,364,773.0 | 281,808,574.0 | 285,154,844.0 | 1,080,725.6 | 5 | 27,360 | 29,847 | 29,616 | 0.004 | compiled=5 | 2,966,959.0 | 280,259,544.0 | 189,291.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 277,904,219.0 | 264,428,662.0 | 283,827,117.0 | 6,543,283.3 | 5 | 27,360 | 29,960 | 29,729 | 0.024 | compiled=5 | 3,039,040.0 | 274,673,178.0 | 192,001.0 |
| `nested-comment-rec` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 283,628,832.0 | 283,001,748.0 | 285,570,802.0 | 1,013,522.9 | 5 | 27,360 | 29,847 | 29,616 | 0.004 (max is trial 1) | compiled=5 | 3,012,717.0 | 280,347,842.0 | 109,060.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 278,358,102.0 | 273,712,464.0 | 286,732,761.0 | 4,720,150.3 | 5 | 27,360 | 29,960 | 29,729 | 0.017 (max is trial 1) | compiled=5 | 3,010,898.0 | 276,393,140.0 | 192,232.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 216,770,747.0 | 208,718,835.0 | 217,261,360.0 | 3,223,032.9 | 5 | 31,568 | 27,307 | 25,625 | 0.015 | compiled=5 | 2,977,482.0 | 213,686,225.0 | 106,311.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 214,000,867.0 | 207,036,789.0 | 214,913,739.0 | 2,926,411.9 | 5 | 31,568 | 27,236 | 25,554 | 0.014 | compiled=5 | 2,981,152.0 | 210,815,473.0 | 188,101.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 137,112,643.0 | 130,572,352.0 | 140,371,557.0 | 3,483,928.3 | 5 | 23,144 | 12,911 | 11,229 | 0.025 | compiled=5 | 2,822,053.0 | 133,045,420.0 | 194,932.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 133,668,686.0 | 127,012,634.0 | 139,750,954.0 | 4,734,102.1 | 5 | 23,144 | 12,735 | 11,053 | 0.035 | compiled=5 | 2,770,792.0 | 130,911,575.0 | 227,842.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 205,638,325.0 | 196,907,230.0 | 208,747,097.0 | 4,168,012.5 | 5 | 27,320 | 23,152 | 23,152 | 0.020 | compiled=5 | 2,862,918.0 | 202,665,497.0 | 107,091.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 205,530,355.0 | 201,164,008.0 | 209,072,347.0 | 2,578,208.7 | 5 | 27,320 | 23,266 | 23,266 | 0.013 | compiled=5 | 2,878,338.0 | 202,548,477.0 | 103,291.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,239,518.0 | 198,132,681.0 | 207,353,875.0 | 3,388,456.0 | 5 | 27,320 | 23,152 | 23,152 | 0.016 (max is trial 1) | compiled=5 | 2,907,307.0 | 202,499,896.0 | 108,710.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,774,932.0 | 195,520,295.0 | 212,283,824.0 | 6,566,991.4 | 5 | 27,320 | 23,266 | 23,266 | 0.032 | compiled=5 | 4,358,615.0 | 203,033,700.0 | 187,131.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 229,816,711.0 | 222,171,339.0 | 235,499,103.0 | 4,254,650.4 | 5 | 31,648 | 28,535 | 26,593 | 0.019 (max is trial 1) | compiled=5 | 3,018,022.0 | 226,692,958.0 | 108,050.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 228,249,564.0 | 220,692,233.0 | 234,663,290.0 | 4,665,680.7 | 5 | 31,608 | 28,463 | 26,521 | 0.020 (max is trial 1) | compiled=5 | 3,037,482.0 | 225,167,311.0 | 99,770.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 135,316,920.0 | 129,017,889.0 | 143,636,065.0 | 5,718,442.4 | 5 | 23,184 | 12,945 | 11,234 | 0.042 | compiled=5 | 2,803,262.0 | 132,338,496.0 | 186,661.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 139,545,272.0 | 134,605,034.0 | 140,678,530.0 | 2,193,759.9 | 5 | 23,144 | 12,768 | 11,057 | 0.016 (max is trial 1) | compiled=5 | 2,799,472.0 | 135,867,853.0 | 103,471.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 217,200,280.0 | 202,383,805.0 | 223,164,619.0 | 7,601,173.1 | 5 | 27,360 | 24,351 | 24,120 | 0.035 | compiled=5 | 2,922,449.0 | 214,075,470.0 | 202,361.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 217,241,300.0 | 210,202,684.0 | 227,040,782.0 | 5,815,301.8 | 5 | 27,360 | 24,464 | 24,233 | 0.027 | compiled=5 | 2,873,138.0 | 214,163,411.0 | 193,121.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 218,539,971.0 | 217,023,372.0 | 219,635,427.0 | 1,025,713.5 | 5 | 27,360 | 24,351 | 24,120 | 0.005 | compiled=5 | 2,921,107.0 | 214,125,565.0 | 114,360.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 218,920,462.0 | 209,855,170.0 | 222,902,467.0 | 5,344,296.7 | 5 | 27,360 | 24,464 | 24,233 | 0.024 | compiled=5 | 2,931,307.0 | 215,254,612.0 | 191,711.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 286,874,111.0 | 286,487,259.0 | 290,759,097.0 | 1,632,829.2 | 5 | 27,168 | 22,034 | 22,034 | 0.006 (max is trial 1) | compiled=5 | 2,823,162.0 | 284,934,764.0 | 188,640.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 289,910,704.0 | 282,538,013.0 | 298,684,649.0 | 5,355,054.8 | 5 | 27,168 | 22,147 | 22,147 | 0.018 | compiled=5 | 2,846,541.0 | 286,945,092.0 | 105,940.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 277,539,041.0 | 275,270,063.0 | 288,823,768.0 | 5,012,690.6 | 5 | 27,168 | 22,016 | 22,016 | 0.018 | compiled=5 | 2,894,892.0 | 274,536,028.0 | 108,121.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 280,238,232.0 | 275,899,618.0 | 286,387,690.0 | 3,864,908.9 | 5 | 27,168 | 22,129 | 22,129 | 0.014 (max is trial 1) | compiled=5 | 2,780,731.0 | 278,373,628.0 | 199,332.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 287,564,750.0 | 278,276,981.0 | 288,323,804.0 | 3,852,283.3 | 5 | 27,168 | 22,032 | 22,032 | 0.013 | compiled=5 | 2,838,848.0 | 284,499,861.0 | 105,721.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 287,427,089.0 | 282,434,896.0 | 290,098,195.0 | 3,398,021.4 | 5 | 27,168 | 22,145 | 22,145 | 0.012 | compiled=5 | 2,858,648.0 | 282,495,598.0 | 114,520.0 |
| `phone-palindrome-6` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 288,080,898.0 | 283,511,802.0 | 289,056,925.0 | 1,986,677.2 | 5 | 27,168 | 22,032 | 22,032 | 0.007 | compiled=5 | 2,881,467.0 | 284,993,600.0 | 195,222.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 289,006,213.0 | 287,049,203.0 | 292,220,612.0 | 1,909,898.1 | 5 | 27,168 | 22,145 | 22,145 | 0.007 (max is trial 1) | compiled=5 | 2,873,837.0 | 286,050,806.0 | 100,660.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 252,286,922.0 | 236,384,317.0 | 255,722,146.0 | 7,316,225.3 | 5 | 31,808 | 31,639 | 28,998 | 0.029 | compiled=5 | 4,818,209.0 | 249,005,818.0 | 105,271.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 242,449,601.0 | 237,257,128.0 | 248,846,047.0 | 4,157,821.0 | 5 | 31,808 | 31,567 | 28,926 | 0.017 | compiled=5 | 3,078,732.0 | 237,813,282.0 | 101,000.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 249,805,915.0 | 248,379,422.0 | 255,014,686.0 | 2,458,631.8 | 5 | 31,808 | 31,639 | 28,998 | 0.010 | compiled=5 | 3,109,334.0 | 246,620,850.0 | 105,671.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 240,578,632.0 | 233,499,427.0 | 249,527,001.0 | 5,648,329.0 | 5 | 31,808 | 31,567 | 28,926 | 0.023 (max is trial 1) | compiled=5 | 3,072,404.0 | 237,497,788.0 | 194,511.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 231,244,579.0 | 224,491,427.0 | 232,066,335.0 | 2,828,018.7 | 5 | 27,280 | 25,884 | 25,422 | 0.012 | compiled=5 | 2,930,848.0 | 227,579,466.0 | 191,431.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 231,925,854.0 | 223,934,753.0 | 238,185,115.0 | 4,598,825.0 | 5 | 27,280 | 25,997 | 25,535 | 0.020 | compiled=5 | 2,955,349.0 | 228,728,583.0 | 193,091.0 |
| `pwd-strength-chain` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 233,008,945.0 | 232,049,690.0 | 238,469,797.0 | 2,366,433.9 | 5 | 27,280 | 25,884 | 25,422 | 0.010 (max is trial 1) | compiled=5 | 2,948,348.0 | 229,666,786.0 | 100,790.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 233,204,704.0 | 221,735,530.0 | 239,451,015.0 | 5,796,058.9 | 5 | 27,280 | 25,997 | 25,535 | 0.025 (max is trial 1) | compiled=5 | 3,012,297.0 | 229,460,305.0 | 100,131.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 217,372,880.0 | 208,765,105.0 | 219,349,497.0 | 4,001,566.2 | 5 | 27,488 | 24,862 | 24,169 | 0.018 | compiled=5 | 2,778,711.0 | 213,948,816.0 | 205,700.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 216,305,255.0 | 211,955,708.0 | 217,933,532.0 | 2,068,354.1 | 5 | 27,488 | 24,975 | 24,282 | 0.010 | compiled=5 | 2,921,742.0 | 213,154,853.0 | 102,991.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 217,591,672.0 | 206,715,138.0 | 223,620,108.0 | 6,171,767.3 | 5 | 27,488 | 24,844 | 24,151 | 0.028 | compiled=5 | 2,866,192.0 | 214,523,838.0 | 187,232.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 210,347,187.0 | 199,746,844.0 | 216,674,065.0 | 5,837,360.7 | 5 | 27,488 | 24,957 | 24,264 | 0.028 (max is trial 1) | compiled=5 | 2,726,521.0 | 207,535,444.0 | 98,061.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 215,212,707.0 | 211,663,435.0 | 219,532,435.0 | 2,517,506.7 | 5 | 27,488 | 24,860 | 24,167 | 0.012 | compiled=5 | 2,908,549.0 | 212,137,678.0 | 102,081.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 216,204,113.0 | 212,984,283.0 | 218,277,436.0 | 1,716,446.7 | 5 | 27,488 | 24,973 | 24,280 | 0.008 (max is trial 1) | compiled=5 | 2,883,789.0 | 213,221,194.0 | 108,300.0 |
| `quoted-delim-match` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 217,147,752.0 | 202,996,060.0 | 223,940,193.0 | 7,598,852.1 | 5 | 27,488 | 24,860 | 24,167 | 0.035 | compiled=5 | 2,918,847.0 | 214,027,434.0 | 100,411.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 216,955,451.0 | 209,469,618.0 | 220,001,400.0 | 3,540,666.2 | 5 | 27,488 | 24,973 | 24,280 | 0.016 | compiled=5 | 2,931,827.0 | 213,922,643.0 | 107,871.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 151,088,301.0 | 149,871,777.0 | 154,747,908.0 | 1,797,216.0 | 5 | 27,608 | 19,289 | 13,309 | 0.012 | compiled=5 | 3,170,343.0 | 147,845,789.0 | 104,061.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,009,297.0 | 152,708,369.0 | 162,335,737.0 | 3,599,988.9 | 5 | 27,752 | 21,933 | 15,326 | 0.022 | compiled=5 | 3,175,132.0 | 156,718,305.0 | 115,860.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 151,127,581.0 | 142,843,838.0 | 157,884,845.0 | 5,019,330.4 | 5 | 27,608 | 19,289 | 13,309 | 0.033 | compiled=5 | 3,134,405.0 | 147,299,192.0 | 105,291.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,986,471.0 | 155,967,789.0 | 169,325,954.0 | 4,529,783.9 | 5 | 27,752 | 21,933 | 15,326 | 0.028 | compiled=5 | 3,201,385.0 | 156,589,125.0 | 203,611.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 168,896,171.0 | 162,565,670.0 | 173,575,001.0 | 4,001,278.4 | 5 | 23,104 | 19,150 | 19,150 | 0.024 | compiled=5 | 2,787,548.0 | 166,022,723.0 | 104,981.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 169,813,127.0 | 163,027,024.0 | 182,557,669.0 | 6,525,791.3 | 5 | 23,104 | 19,263 | 19,263 | 0.038 | compiled=5 | 4,322,438.0 | 166,898,768.0 | 115,900.0 |
| `router-prefix-order` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,708,845.0 | 169,624,466.0 | 176,006,112.0 | 2,095,581.7 | 5 | 23,104 | 19,150 | 19,150 | 0.012 | compiled=5 | 2,847,397.0 | 168,783,079.0 | 105,251.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,789,318.0 | 167,069,810.0 | 178,733,317.0 | 3,791,100.8 | 5 | 23,104 | 19,263 | 19,263 | 0.022 | compiled=5 | 2,950,697.0 | 169,868,515.0 | 190,521.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 279,408,392.0 | 263,008,905.0 | 280,377,215.0 | 6,583,032.2 | 5 | 27,488 | 31,532 | 31,070 | 0.024 | compiled=5 | 3,179,223.0 | 276,107,327.0 | 192,271.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 279,332,261.0 | 279,152,301.0 | 281,077,308.0 | 718,186.2 | 5 | 31,584 | 31,645 | 31,183 | 0.003 (max is trial 1) | compiled=5 | 3,065,493.0 | 276,083,507.0 | 108,130.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 282,232,418.0 | 276,222,801.0 | 293,215,624.0 | 5,631,820.0 | 5 | 27,448 | 31,514 | 31,052 | 0.020 | compiled=5 | 3,027,464.0 | 279,101,093.0 | 104,271.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 285,707,495.0 | 266,442,893.0 | 292,408,008.0 | 8,771,596.0 | 5 | 27,448 | 31,627 | 31,165 | 0.031 | compiled=5 | 4,849,818.0 | 280,478,154.0 | 115,871.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 272,764,815.0 | 269,023,521.0 | 285,608,668.0 | 5,964,459.0 | 5 | 27,488 | 31,530 | 31,068 | 0.022 (max is trial 1) | compiled=5 | 3,143,920.0 | 268,575,919.0 | 99,391.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 276,967,402.0 | 270,300,479.0 | 288,472,876.0 | 6,560,638.6 | 5 | 31,584 | 31,643 | 31,181 | 0.024 | compiled=5 | 3,064,479.0 | 273,418,360.0 | 191,301.0 |
| `tag-depth3-bound` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 276,680,671.0 | 270,984,119.0 | 280,654,084.0 | 3,730,481.9 | 5 | 27,488 | 31,530 | 31,068 | 0.013 | compiled=5 | 3,068,218.0 | 274,367,368.0 | 105,090.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 279,019,295.0 | 271,149,189.0 | 289,551,426.0 | 5,967,836.6 | 5 | 31,584 | 31,643 | 31,181 | 0.021 | compiled=5 | 3,091,558.0 | 275,710,616.0 | 188,921.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 225,278,581.0 | 224,408,128.0 | 233,877,137.0 | 3,530,451.8 | 5 | 27,448 | 25,424 | 24,269 | 0.016 (max is trial 1) | compiled=5 | 2,954,521.0 | 222,422,491.0 | 107,631.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 225,592,304.0 | 218,874,976.0 | 229,837,961.0 | 4,490,720.4 | 5 | 27,448 | 25,537 | 24,382 | 0.020 | compiled=5 | 2,994,652.0 | 222,463,531.0 | 189,600.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 217,545,352.0 | 215,755,007.0 | 218,453,208.0 | 919,054.7 | 5 | 27,448 | 25,406 | 24,251 | 0.004 | compiled=5 | 2,773,872.0 | 214,683,169.0 | 100,171.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 224,416,656.0 | 215,513,296.0 | 227,105,567.0 | 4,042,028.5 | 5 | 27,448 | 25,519 | 24,364 | 0.018 | compiled=5 | 2,970,633.0 | 221,252,741.0 | 108,241.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 225,271,791.0 | 224,718,338.0 | 226,743,212.0 | 849,071.4 | 5 | 27,448 | 25,422 | 24,267 | 0.004 (max is trial 1) | compiled=5 | 2,983,749.0 | 222,096,981.0 | 191,061.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 225,901,935.0 | 215,753,401.0 | 229,579,879.0 | 4,652,564.3 | 5 | 27,448 | 25,535 | 24,380 | 0.021 (max is trial 1) | compiled=5 | 3,068,629.0 | 222,725,485.0 | 187,551.0 |
| `tag-pair-match` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 225,348,110.0 | 212,626,066.0 | 229,662,466.0 | 6,091,784.6 | 5 | 27,448 | 25,422 | 24,267 | 0.027 | compiled=5 | 3,005,938.0 | 222,240,052.0 | 111,721.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 226,884,170.0 | 219,439,736.0 | 228,096,776.0 | 3,613,849.0 | 5 | 27,448 | 25,535 | 24,380 | 0.016 | compiled=5 | 2,993,658.0 | 223,708,131.0 | 105,971.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 195,992,643.0 | 192,087,998.0 | 198,894,584.0 | 2,901,501.2 | 5 | 27,360 | 22,410 | 22,179 | 0.015 | compiled=5 | 2,850,781.0 | 192,960,121.0 | 192,171.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 190,716,094.0 | 187,755,820.0 | 202,872,861.0 | 5,848,678.6 | 5 | 27,360 | 22,524 | 22,293 | 0.031 | compiled=5 | 2,857,812.0 | 186,265,804.0 | 99,190.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 132,971,501.0 | 127,284,335.0 | 140,734,361.0 | 5,546,108.2 | 5 | 23,144 | 12,680 | 11,069 | 0.042 | compiled=5 | 2,864,292.0 | 128,641,787.0 | 112,331.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 129,631,854.0 | 125,504,891.0 | 137,094,671.0 | 4,720,977.2 | 5 | 23,104 | 12,504 | 10,893 | 0.036 | compiled=5 | 2,779,262.0 | 125,170,349.0 | 113,501.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 189,492,922.0 | 189,223,891.0 | 207,616,889.0 | 7,126,707.6 | 5 | 27,360 | 22,391 | 22,160 | 0.038 | compiled=5 | 2,864,139.0 | 186,508,994.0 | 195,821.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 195,717,782.0 | 181,912,534.0 | 197,564,454.0 | 5,821,366.6 | 5 | 27,360 | 22,505 | 22,274 | 0.030 (max is trial 1) | compiled=5 | 2,866,438.0 | 192,764,634.0 | 202,631.0 |
| `trim-nested-star` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 196,486,361.0 | 195,173,684.0 | 202,120,094.0 | 2,438,812.5 | 5 | 27,360 | 22,391 | 22,160 | 0.012 | compiled=5 | 2,829,097.0 | 193,550,964.0 | 115,941.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 194,148,098.0 | 189,243,439.0 | 197,765,499.0 | 3,147,112.8 | 5 | 27,360 | 22,505 | 22,274 | 0.016 (max is trial 1) | compiled=5 | 2,872,337.0 | 191,076,630.0 | 189,151.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 187,365,919.0 | 179,788,857.0 | 189,950,139.0 | 3,604,917.9 | 5 | 31,632 | 26,873 | 22,071 | 0.019 | compiled=5 | 3,065,382.0 | 184,197,716.0 | 99,521.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 193,221,022.0 | 178,232,311.0 | 195,110,521.0 | 6,247,493.2 | 5 | 31,728 | 28,449 | 23,433 | 0.032 | compiled=5 | 3,099,653.0 | 190,575,051.0 | 98,170.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 188,175,382.0 | 179,921,157.0 | 190,097,427.0 | 3,574,509.4 | 5 | 31,632 | 26,873 | 22,071 | 0.019 | compiled=5 | 3,103,774.0 | 184,975,537.0 | 107,981.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 187,920,080.0 | 185,924,825.0 | 195,646,621.0 | 3,745,483.6 | 5 | 31,728 | 28,449 | 23,433 | 0.020 | compiled=5 | 3,130,255.0 | 183,852,658.0 | 102,681.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 172,166,092.0 | 155,038,281.0 | 172,563,085.0 | 6,740,680.0 | 5 | 23,104 | 18,794 | 18,794 | 0.039 | compiled=5 | 2,801,177.0 | 169,046,272.0 | 100,151.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 173,900,822.0 | 163,168,765.0 | 177,366,695.0 | 4,939,469.2 | 5 | 23,104 | 18,905 | 18,905 | 0.028 | compiled=5 | 2,863,798.0 | 170,716,772.0 | 101,101.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 170,140,077.0 | 162,783,265.0 | 174,964,774.0 | 5,222,536.6 | 5 | 23,104 | 18,794 | 18,794 | 0.031 | compiled=5 | 2,835,077.0 | 167,216,510.0 | 114,550.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 168,962,960.0 | 162,329,149.0 | 172,864,293.0 | 3,889,282.3 | 5 | 23,104 | 18,905 | 18,905 | 0.023 | compiled=5 | 2,873,897.0 | 165,896,032.0 | 116,280.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 177,949,330.0 | 168,292,491.0 | 191,146,804.0 | 8,057,940.4 | 5 | 36,888 | 22,372 | 16,968 | 0.045 | compiled=5 | 4,727,269.0 | 173,374,192.0 | 213,111.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 178,814,953.0 | 177,257,468.0 | 190,764,622.0 | 5,046,942.0 | 5 | 36,848 | 22,194 | 16,790 | 0.028 (max is trial 1) | compiled=5 | 4,523,298.0 | 174,188,075.0 | 103,580.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 170,059,959.0 | 165,932,573.0 | 175,172,419.0 | 3,127,090.1 | 5 | 36,888 | 22,372 | 16,968 | 0.018 | compiled=5 | 4,416,968.0 | 164,077,205.0 | 131,401.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 176,957,316.0 | 169,449,706.0 | 177,700,370.0 | 3,098,633.2 | 5 | 36,848 | 22,194 | 16,790 | 0.018 (max is trial 1) | compiled=5 | 4,493,758.0 | 171,674,966.0 | 104,920.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 198,126,307.0 | 192,571,631.0 | 201,868,222.0 | 3,400,634.9 | 5 | 23,192 | 22,985 | 22,523 | 0.017 (max is trial 1) | compiled=5 | 5,883,228.0 | 193,126,776.0 | 104,171.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 197,687,926.0 | 189,907,065.0 | 209,518,760.0 | 6,557,367.2 | 5 | 23,192 | 23,098 | 22,636 | 0.033 | compiled=5 | 4,354,437.0 | 192,955,665.0 | 206,161.0 |
| `uuid-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 196,454,231.0 | 188,147,521.0 | 197,962,030.0 | 4,031,406.6 | 5 | 23,192 | 22,985 | 22,523 | 0.021 | compiled=5 | 2,897,217.0 | 192,324,487.0 | 215,641.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 192,850,070.0 | 187,571,780.0 | 199,260,838.0 | 4,605,678.9 | 5 | 23,192 | 23,098 | 22,636 | 0.024 (max is trial 1) | compiled=5 | 2,873,126.0 | 190,850,488.0 | 209,701.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,109,137.0 | 144,484,195.0 | 154,257,324.0 | 3,916,027.8 | 5 | 27,608 | 18,296 | 13,299 | 0.026 | compiled=5 | 3,160,883.0 | 147,013,295.0 | 99,721.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 152,983,309.0 | 146,172,452.0 | 161,545,744.0 | 5,465,168.5 | 5 | 27,752 | 20,639 | 15,316 | 0.036 (max is trial 1) | compiled=5 | 3,179,693.0 | 149,599,555.0 | 198,351.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 142,475,583.0 | 141,368,106.0 | 150,863,071.0 | 3,714,490.5 | 5 | 27,608 | 18,296 | 13,299 | 0.026 | compiled=5 | 3,036,023.0 | 139,241,659.0 | 191,352.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,667,889.0 | 156,490,035.0 | 165,775,016.0 | 3,256,486.1 | 5 | 27,752 | 20,639 | 15,316 | 0.020 (max is trial 1) | compiled=5 | 3,009,993.0 | 156,465,814.0 | 204,302.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 140,289,188.0 | 128,185,660.0 | 141,853,268.0 | 5,073,315.2 | 5 | 23,072 | 17,839 | 17,839 | 0.036 | compiled=5 | 2,724,157.0 | 137,190,708.0 | 188,451.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 143,271,377.0 | 137,606,390.0 | 144,918,558.0 | 2,649,267.4 | 5 | 23,072 | 17,950 | 17,950 | 0.018 (max is trial 1) | compiled=5 | 2,766,078.0 | 140,425,818.0 | 106,101.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 139,498,357.0 | 127,771,159.0 | 142,204,762.0 | 5,507,480.7 | 5 | 23,072 | 17,839 | 17,839 | 0.039 | compiled=5 | 2,908,057.0 | 135,746,905.0 | 97,980.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 131,308,980.0 | 124,239,509.0 | 149,312,376.0 | 9,143,867.5 | 5 | 23,072 | 17,950 | 17,950 | 0.070 | compiled=5 | 2,777,856.0 | 128,438,883.0 | 100,381.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 151,111,592.0 | 149,041,674.0 | 159,150,084.0 | 3,641,318.3 | 5 | 27,936 | 27,250 | 14,985 | 0.024 | compiled=5 | 3,505,204.0 | 146,536,413.0 | 108,051.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,457,935.0 | 158,144,689.0 | 168,918,794.0 | 3,994,904.2 | 5 | 28,080 | 30,113 | 16,960 | 0.025 | compiled=5 | 3,487,634.0 | 155,544,930.0 | 192,230.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,633,220.0 | 142,153,681.0 | 168,137,066.0 | 8,764,586.7 | 5 | 27,936 | 27,250 | 14,985 | 0.055 | compiled=5 | 3,490,047.0 | 154,925,442.0 | 194,731.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 165,903,988.0 | 163,477,080.0 | 172,560,660.0 | 3,303,695.9 | 5 | 28,080 | 30,113 | 16,960 | 0.020 | compiled=5 | 3,623,539.0 | 162,204,329.0 | 184,302.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,450,842.0 | 199,192,894.0 | 208,119,703.0 | 3,860,533.3 | 5 | 23,112 | 20,901 | 20,670 | 0.019 | compiled=5 | 2,830,458.0 | 203,308,071.0 | 191,781.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 208,347,943.0 | 190,718,470.0 | 209,313,369.0 | 7,158,345.3 | 5 | 23,112 | 21,014 | 20,783 | 0.034 | compiled=5 | 2,845,078.0 | 205,287,693.0 | 202,262.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 202,488,087.0 | 200,701,067.0 | 211,724,971.0 | 4,045,731.2 | 5 | 23,112 | 20,901 | 20,670 | 0.020 | compiled=5 | 2,898,077.0 | 198,108,191.0 | 209,572.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 208,538,412.0 | 207,305,196.0 | 211,751,283.0 | 1,819,746.8 | 5 | 23,112 | 21,014 | 20,783 | 0.009 | compiled=5 | 2,863,087.0 | 205,580,524.0 | 98,851.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 149,635,606.0 | 145,848,430.0 | 155,540,879.0 | 3,408,543.9 | 5 | 27,608 | 22,063 | 13,741 | 0.023 | compiled=5 | 3,272,294.0 | 146,173,551.0 | 189,881.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 151,332,173.0 | 144,974,947.0 | 159,388,366.0 | 4,758,323.9 | 5 | 27,744 | 25,414 | 15,655 | 0.031 | compiled=5 | 2,178,129.0 | 149,107,743.0 | 112,720.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 155,279,195.0 | 150,400,857.0 | 155,705,107.0 | 2,204,963.6 | 5 | 27,608 | 22,063 | 13,741 | 0.014 | compiled=5 | 3,266,125.0 | 149,689,111.0 | 189,642.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 157,571,393.0 | 151,985,559.0 | 167,667,232.0 | 5,824,725.5 | 5 | 27,744 | 25,414 | 15,655 | 0.037 (max is trial 1) | compiled=5 | 2,117,797.0 | 155,214,444.0 | 192,881.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 203,096,619.0 | 190,357,169.0 | 206,610,043.0 | 5,630,491.6 | 5 | 31,336 | 23,271 | 23,040 | 0.028 (max is trial 1) | compiled=5 | 2,985,149.0 | 199,995,709.0 | 102,100.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 203,149,679.0 | 190,168,257.0 | 203,877,974.0 | 5,582,037.9 | 5 | 31,336 | 23,386 | 23,155 | 0.027 | compiled=5 | 1,705,361.0 | 201,233,698.0 | 103,101.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 203,424,182.0 | 194,817,872.0 | 213,438,792.0 | 5,904,640.3 | 5 | 31,336 | 23,271 | 23,040 | 0.029 | compiled=5 | 2,969,108.0 | 199,846,051.0 | 189,541.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 202,702,448.0 | 199,865,790.0 | 212,261,534.0 | 4,265,218.0 | 5 | 31,336 | 23,386 | 23,155 | 0.021 | compiled=5 | 1,656,700.0 | 200,979,388.0 | 106,181.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 151,236,263.0 | 144,466,784.0 | 157,585,988.0 | 4,163,576.4 | 5 | 27,608 | 18,297 | 13,300 | 0.028 | compiled=5 | 3,006,273.0 | 148,272,810.0 | 195,551.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 157,402,667.0 | 154,714,377.0 | 161,261,303.0 | 2,476,178.6 | 5 | 27,752 | 20,640 | 15,317 | 0.016 (max is trial 1) | compiled=5 | 3,051,742.0 | 154,190,024.0 | 197,631.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,369,671.0 | 135,249,799.0 | 151,531,995.0 | 5,781,682.6 | 5 | 27,608 | 18,297 | 13,300 | 0.040 (max is trial 1) | compiled=5 | 3,048,424.0 | 140,235,877.0 | 99,031.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 154,651,450.0 | 150,955,942.0 | 167,423,289.0 | 5,877,944.5 | 5 | 27,752 | 20,640 | 15,317 | 0.038 | compiled=5 | 3,024,364.0 | 151,502,825.0 | 188,521.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 130,562,905.0 | 116,227,463.0 | 142,763,113.0 | 11,047,462.1 | 5 | 23,072 | 17,840 | 17,840 | 0.085 | compiled=5 | 2,731,947.0 | 127,639,787.0 | 105,300.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 142,804,624.0 | 135,154,994.0 | 144,798,247.0 | 3,960,956.0 | 5 | 23,072 | 17,951 | 17,951 | 0.028 | compiled=5 | 2,782,658.0 | 138,201,664.0 | 104,421.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 140,819,804.0 | 127,453,056.0 | 146,399,408.0 | 7,857,388.0 | 5 | 23,072 | 17,840 | 17,840 | 0.056 (max is trial 1) | compiled=5 | 2,803,776.0 | 136,296,689.0 | 106,221.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 139,495,898.0 | 136,305,909.0 | 141,354,678.0 | 2,011,799.9 | 5 | 23,072 | 17,951 | 17,951 | 0.014 | compiled=5 | 2,771,216.0 | 136,359,539.0 | 191,671.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 143,649,071.0 | 142,324,557.0 | 153,112,749.0 | 4,378,966.3 | 5 | 27,608 | 19,676 | 13,581 | 0.030 (max is trial 1) | compiled=5 | 3,364,093.0 | 140,089,327.0 | 193,950.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 160,194,219.0 | 150,641,579.0 | 167,461,457.0 | 5,488,681.1 | 5 | 27,752 | 22,318 | 15,600 | 0.034 (max is trial 1) | compiled=5 | 1,862,248.0 | 158,138,950.0 | 193,021.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 148,055,369.0 | 142,659,366.0 | 157,791,974.0 | 5,461,882.6 | 5 | 27,608 | 19,676 | 13,581 | 0.037 (max is trial 1) | compiled=5 | 3,135,514.0 | 145,034,744.0 | 101,451.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 156,054,622.0 | 145,901,491.0 | 162,062,118.0 | 6,022,123.1 | 5 | 27,752 | 22,318 | 15,600 | 0.039 | compiled=5 | 1,736,644.0 | 154,272,997.0 | 101,001.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 179,573,409.0 | 174,971,419.0 | 187,996,673.0 | 4,225,070.8 | 5 | 23,184 | 20,198 | 19,736 | 0.024 | compiled=5 | 2,869,879.0 | 176,500,219.0 | 115,140.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 178,226,321.0 | 165,297,718.0 | 179,733,559.0 | 5,382,142.6 | 5 | 23,184 | 20,311 | 19,849 | 0.030 | compiled=5 | 1,535,030.0 | 176,495,499.0 | 108,010.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 180,072,366.0 | 165,703,290.0 | 189,030,258.0 | 7,497,789.2 | 5 | 23,184 | 20,198 | 19,736 | 0.042 | compiled=5 | 4,140,964.0 | 176,950,537.0 | 192,561.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 179,199,110.0 | 172,601,952.0 | 181,871,855.0 | 4,009,918.6 | 5 | 23,184 | 20,311 | 19,849 | 0.022 (max is trial 1) | compiled=5 | 1,654,999.0 | 177,360,270.0 | 183,841.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 583,982,264.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,484,884,802.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 853,086,664.0 | 850,925,937.0 | 858,884,930.0 | 2,741,780.4 | 5 | 277,312 | 889,527 (warned) | 20,438 | 0.003 | compiled=5 | 567,760,422.0 | 285,102,170.0 | 105,231.0 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,083,381,963.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 27,968,909.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 28,543,713.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 28,013,354.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 27,683,742.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 362,570,027.0 | 357,178,866.0 | 363,272,241.0 | 2,214,717.4 | 5 | 45,648 | 54,260 | 44,337 | 0.006 | compiled=5 | 5,088,510.0 | 355,940,220.0 | 110,520.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 340,159,508.0 | 338,614,530.0 | 352,416,517.0 | 5,181,222.5 | 5 | 45,280 | 52,699 | 42,776 | 0.015 | compiled=5 | 4,777,859.0 | 337,511,106.0 | 112,530.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 186,590,880.0 | 177,673,929.0 | 188,500,964.0 | 3,993,785.5 | 5 | 41,232 | 29,483 | 20,484 | 0.021 | compiled=5 | 4,626,816.0 | 181,903,273.0 | 108,731.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 170,162,882.0 | 159,946,412.0 | 178,203,094.0 | 6,290,366.7 | 5 | 40,864 | 27,817 | 18,818 | 0.037 | compiled=5 | 4,497,695.0 | 165,553,246.0 | 111,941.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 294,976,076.0 | 292,312,470.0 | 296,140,944.0 | 1,445,273.1 | 5 | 27,408 | 33,723 | 32,799 | 0.005 | compiled=5 | 3,219,551.0 | 290,901,271.0 | 108,110.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 298,941,523.0 | 296,750,469.0 | 304,029,985.0 | 2,686,108.3 | 5 | 27,408 | 33,836 | 32,912 | 0.009 | compiled=5 | 3,181,700.0 | 293,860,341.0 | 112,651.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 302,551,803.0 | 291,762,399.0 | 306,055,963.0 | 4,878,592.7 | 5 | 27,408 | 33,723 | 32,799 | 0.016 | compiled=5 | 3,112,379.0 | 299,203,283.0 | 169,941.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 301,027,774.0 | 300,444,270.0 | 331,453,172.0 | 12,241,117.8 | 5 | 27,408 | 33,836 | 32,912 | 0.041 (max is trial 1) | compiled=5 | 3,153,949.0 | 297,746,955.0 | 219,372.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 243,593,025.0 | 233,457,623.0 | 258,160,344.0 | 8,814,094.4 | 5 | 31,800 | 32,766 | 27,256 | 0.036 | compiled=5 | 4,500,338.0 | 239,902,401.0 | 190,620.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 236,790,457.0 | 227,502,701.0 | 239,927,660.0 | 4,521,757.0 | 5 | 31,888 | 33,838 | 27,903 | 0.019 | compiled=5 | 3,318,573.0 | 232,853,543.0 | 195,041.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 240,036,361.0 | 238,852,468.0 | 242,807,774.0 | 1,511,828.4 | 5 | 31,800 | 32,766 | 27,256 | 0.006 (max is trial 1) | compiled=5 | 3,299,343.0 | 236,635,248.0 | 110,200.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 241,232,467.0 | 240,741,314.0 | 246,187,017.0 | 2,035,936.3 | 5 | 31,888 | 33,838 | 27,903 | 0.008 (max is trial 1) | compiled=5 | 3,349,883.0 | 237,541,112.0 | 191,441.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 214,382,283.0 | 210,940,621.0 | 217,415,402.0 | 2,098,145.8 | 5 | 27,328 | 23,345 | 22,883 | 0.010 (max is trial 1) | compiled=5 | 2,929,619.0 | 211,260,192.0 | 192,472.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 210,962,159.0 | 203,837,644.0 | 215,992,573.0 | 4,827,435.6 | 5 | 27,328 | 23,461 | 22,999 | 0.023 (max is trial 1) | compiled=5 | 2,944,629.0 | 206,410,900.0 | 188,972.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 214,212,855.0 | 202,240,135.0 | 214,984,849.0 | 4,841,852.2 | 5 | 27,328 | 23,345 | 22,883 | 0.023 | compiled=5 | 3,097,598.0 | 210,034,740.0 | 202,811.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 214,539,457.0 | 210,443,133.0 | 217,401,744.0 | 2,236,835.8 | 5 | 27,328 | 23,461 | 22,999 | 0.010 | compiled=5 | 2,960,927.0 | 211,485,159.0 | 103,421.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 236,308,177.0 | 235,763,624.0 | 237,749,622.0 | 692,786.6 | 5 | 31,800 | 32,487 | 26,977 | 0.003 (max is trial 1) | compiled=5 | 3,240,964.0 | 232,727,082.0 | 103,120.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 233,400,045.0 | 228,304,285.0 | 238,959,628.0 | 4,095,567.9 | 5 | 31,888 | 33,556 | 27,621 | 0.018 (max is trial 1) | compiled=5 | 3,312,323.0 | 229,876,191.0 | 197,381.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 243,396,145.0 | 234,179,888.0 | 265,544,106.0 | 11,057,069.6 | 5 | 31,800 | 32,487 | 26,977 | 0.045 | compiled=5 | 3,261,833.0 | 237,735,752.0 | 111,030.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 236,945,090.0 | 236,549,548.0 | 238,471,525.0 | 781,771.7 | 5 | 31,888 | 33,556 | 27,621 | 0.003 | compiled=5 | 3,310,123.0 | 233,560,166.0 | 188,540.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 206,604,822.0 | 203,795,873.0 | 209,338,800.0 | 1,794,641.6 | 5 | 27,328 | 23,066 | 22,604 | 0.009 | compiled=5 | 2,908,119.0 | 203,604,513.0 | 187,211.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 210,431,726.0 | 209,669,792.0 | 215,139,957.0 | 1,984,809.2 | 5 | 27,328 | 23,179 | 22,717 | 0.009 (max is trial 1) | compiled=5 | 2,911,358.0 | 207,764,350.0 | 104,070.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 206,957,053.0 | 204,507,790.0 | 207,509,756.0 | 1,091,135.9 | 5 | 27,328 | 23,066 | 22,604 | 0.005 | compiled=5 | 2,936,627.0 | 203,920,925.0 | 105,811.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 209,882,689.0 | 209,108,006.0 | 212,161,463.0 | 1,167,508.2 | 5 | 27,328 | 23,179 | 22,717 | 0.006 (max is trial 1) | compiled=5 | 2,932,117.0 | 206,859,302.0 | 104,861.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 399,742,938.0 | 391,266,653.0 | 419,281,697.0 | 11,748,332.3 | 5 | 40,504 | 60,491 | 40,762 | 0.029 (max is trial 1) | compiled=5 | 11,938,389.0 | 386,635,555.0 | 214,041.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 414,065,076.0 | 403,262,493.0 | 429,158,498.0 | 9,556,110.0 | 5 | 40,592 | 65,134 | 42,262 | 0.023 (max is trial 1) | compiled=5 | 9,394,738.0 | 404,335,067.0 | 123,381.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 398,150,912.0 | 390,209,551.0 | 400,049,711.0 | 4,403,575.9 | 5 | 40,504 | 60,491 | 40,762 | 0.011 | compiled=5 | 6,332,666.0 | 391,677,116.0 | 101,200.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 414,449,288.0 | 412,981,202.0 | 427,457,189.0 | 5,288,399.4 | 5 | 40,592 | 65,134 | 42,262 | 0.013 (max is trial 1) | compiled=5 | 9,453,848.0 | 404,943,780.0 | 210,751.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 356,390,640.0 | 347,399,653.0 | 380,534,304.0 | 11,798,772.8 | 5 | 35,720 | 36,838 | 35,914 | 0.033 (max is trial 1) | compiled=5 | 3,135,260.0 | 353,049,139.0 | 189,941.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 359,419,699.0 | 350,352,992.0 | 371,067,864.0 | 6,797,972.4 | 5 | 35,720 | 36,951 | 36,027 | 0.019 | compiled=5 | 3,168,970.0 | 354,419,568.0 | 188,271.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 356,297,257.0 | 349,973,771.0 | 362,132,201.0 | 4,478,542.7 | 5 | 35,720 | 36,838 | 35,914 | 0.013 (max is trial 1) | compiled=5 | 3,153,138.0 | 352,978,328.0 | 108,030.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 361,182,267.0 | 350,114,142.0 | 361,934,431.0 | 4,444,505.1 | 5 | 35,720 | 36,951 | 36,027 | 0.012 | compiled=5 | 3,268,449.0 | 357,722,317.0 | 107,711.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 359,151,634.0 | 350,586,390.0 | 364,629,576.0 | 4,518,640.2 | 5 | 40,504 | 58,043 | 38,314 | 0.013 (max is trial 1) | compiled=5 | 6,107,804.0 | 352,104,785.0 | 102,050.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 371,314,152.0 | 366,548,563.0 | 379,462,455.0 | 4,178,970.6 | 5 | 40,592 | 62,686 | 39,814 | 0.011 (max is trial 1) | compiled=5 | 9,030,626.0 | 362,173,926.0 | 102,130.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 358,461,101.0 | 351,917,196.0 | 367,690,800.0 | 6,243,741.0 | 5 | 40,504 | 58,043 | 38,314 | 0.017 | compiled=5 | 6,131,455.0 | 350,966,381.0 | 194,430.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 375,122,360.0 | 363,136,840.0 | 380,393,750.0 | 5,691,002.9 | 5 | 40,592 | 62,686 | 39,814 | 0.015 | compiled=5 | 9,035,276.0 | 363,581,862.0 | 189,801.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 317,886,434.0 | 308,118,751.0 | 321,082,224.0 | 4,465,473.9 | 5 | 31,624 | 34,390 | 33,466 | 0.014 | compiled=5 | 3,104,579.0 | 313,682,597.0 | 192,582.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 318,414,158.0 | 316,561,306.0 | 319,307,982.0 | 995,129.7 | 5 | 31,624 | 34,503 | 33,579 | 0.003 | compiled=5 | 3,113,620.0 | 313,991,089.0 | 108,531.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 316,698,717.0 | 315,026,857.0 | 322,262,508.0 | 2,605,443.1 | 5 | 31,624 | 34,390 | 33,466 | 0.008 | compiled=5 | 3,159,058.0 | 314,235,182.0 | 102,461.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 317,701,923.0 | 311,672,396.0 | 327,698,280.0 | 5,746,638.9 | 5 | 31,624 | 34,503 | 33,579 | 0.018 | compiled=5 | 3,471,831.0 | 313,764,889.0 | 206,321.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 5,440,169,870.0 | 5,415,535,980.0 | 5,460,333,612.0 | 16,374,645.6 | 5 | 175,976 | 516,731 (warned) | 298,766 | 0.003 | compiled=5 | 601,581,285.0 | 4,832,288,970.0 | 199,671.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 6,441,714,562.0 | 6,421,374,852.0 | 6,452,491,777.0 | 10,279,879.2 | 5 | 180,168 | 526,348 (warned) | 300,186 | 0.002 (max is trial 1) | compiled=5 | 1,582,348,114.0 | 4,854,801,230.0 | 195,721.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 4,405,913,371.0 | 4,365,698,008.0 | 4,432,914,840.0 | 23,827,153.5 | 5 | 155,456 | 472,988 (warned) | 255,019 | 0.005 | compiled=5 | 592,646,461.0 | 3,805,910,661.0 | 205,561.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 5,429,574,636.0 | 5,408,600,234.0 | 5,566,312,720.0 | 57,611,858.8 | 5 | 159,648 | 482,605 (warned) | 256,439 | 0.011 (max is trial 1) | compiled=5 | 1,583,265,041.0 | 3,846,208,114.0 | 193,152.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 4,777,376,780.0 | 4,761,290,936.0 | 4,781,093,123.0 | 7,954,647.4 | 5 | 105,728 | 296,609 (warned) | 293,814 | 0.002 | compiled=5 | 9,139,639.0 | 4,759,328,544.0 | 199,391.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 4,786,950,391.0 | 4,762,126,902.0 | 4,800,114,532.0 | 13,054,630.9 | 5 | 105,728 | 296,726 (warned) | 293,931 | 0.003 | compiled=5 | 9,203,038.0 | 4,774,342,320.0 | 187,821.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 4,774,649,397.0 | 4,763,450,242.0 | 4,799,452,443.0 | 14,109,768.8 | 5 | 105,728 | 296,609 (warned) | 293,814 | 0.003 | compiled=5 | 8,993,252.0 | 4,765,256,243.0 | 190,061.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 4,790,900,834.0 | 4,761,838,173.0 | 4,799,542,835.0 | 13,890,121.5 | 5 | 105,728 | 296,726 (warned) | 293,931 | 0.003 | compiled=5 | 9,182,744.0 | 4,780,813,384.0 | 186,821.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 244,038,668.0 | 239,897,802.0 | 249,310,890.0 | 3,879,779.7 | 5 | 31,960 | 36,053 | 27,569 | 0.016 (max is trial 1) | compiled=5 | 3,373,263.0 | 240,577,574.0 | 110,381.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 250,855,856.0 | 236,011,395.0 | 252,222,421.0 | 6,179,986.3 | 5 | 32,096 | 39,397 | 29,094 | 0.025 | compiled=5 | 3,455,184.0 | 247,280,871.0 | 119,801.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 242,209,715.0 | 240,118,838.0 | 246,557,070.0 | 2,310,325.4 | 5 | 31,960 | 36,053 | 27,569 | 0.010 | compiled=5 | 4,914,549.0 | 236,850,633.0 | 115,671.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 251,711,870.0 | 244,433,092.0 | 264,002,885.0 | 6,360,477.1 | 5 | 32,096 | 39,397 | 29,094 | 0.025 | compiled=5 | 3,881,140.0 | 247,127,424.0 | 111,501.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 214,498,012.0 | 213,299,975.0 | 215,711,080.0 | 769,963.5 | 5 | 27,400 | 23,991 | 23,529 | 0.004 | compiled=5 | 2,924,128.0 | 211,476,783.0 | 102,431.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 214,231,512.0 | 209,440,181.0 | 219,281,102.0 | 3,274,034.7 | 5 | 27,400 | 24,105 | 23,643 | 0.015 | compiled=5 | 4,581,139.0 | 211,129,011.0 | 104,931.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 212,258,975.0 | 206,022,358.0 | 215,875,465.0 | 3,687,717.0 | 5 | 27,400 | 23,991 | 23,529 | 0.017 | compiled=5 | 4,419,856.0 | 206,120,908.0 | 100,001.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 218,580,060.0 | 208,377,041.0 | 224,951,337.0 | 6,262,408.9 | 5 | 27,400 | 24,105 | 23,643 | 0.029 | compiled=5 | 4,479,746.0 | 212,634,376.0 | 204,061.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 250,961,695.0 | 235,989,705.0 | 256,876,830.0 | 8,302,301.4 | 5 | 36,024 | 46,375 | 29,470 | 0.033 | compiled=5 | 7,038,458.0 | 243,812,487.0 | 110,750.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 255,242,883.0 | 248,519,955.0 | 265,112,382.0 | 5,343,950.6 | 5 | 36,120 | 48,792 | 30,891 | 0.021 | compiled=5 | 6,014,644.0 | 249,125,889.0 | 102,350.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 161,453,014.0 | 146,761,945.0 | 170,501,205.0 | 8,527,832.6 | 5 | 32,032 | 39,301 | 15,035 | 0.053 | compiled=5 | 6,890,694.0 | 153,637,152.0 | 188,642.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 164,883,650.0 | 156,023,581.0 | 176,499,631.0 | 6,882,267.4 | 5 | 32,176 | 42,789 | 17,010 | 0.042 (max is trial 1) | compiled=5 | 6,420,000.0 | 158,525,090.0 | 101,131.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 222,775,225.0 | 205,814,527.0 | 227,291,662.0 | 9,133,861.8 | 5 | 27,280 | 25,437 | 24,975 | 0.041 | compiled=5 | 2,980,669.0 | 219,775,516.0 | 97,180.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 222,065,781.0 | 215,031,236.0 | 224,025,885.0 | 3,126,291.2 | 5 | 27,280 | 25,550 | 25,088 | 0.014 | compiled=5 | 2,957,249.0 | 218,917,251.0 | 191,281.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 225,569,431.0 | 221,156,416.0 | 226,536,098.0 | 1,947,074.2 | 5 | 27,280 | 25,437 | 24,975 | 0.009 | compiled=5 | 4,584,977.0 | 220,430,772.0 | 107,161.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 221,984,032.0 | 210,024,160.0 | 226,721,028.0 | 5,671,935.5 | 5 | 27,280 | 25,550 | 25,088 | 0.026 (max is trial 1) | compiled=5 | 4,480,096.0 | 217,331,924.0 | 183,401.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 392,473,599.0 | 380,773,681.0 | 393,043,082.0 | 4,712,515.9 | 5 | 40,040 | 56,740 | 26,630 | 0.012 | compiled=5 | 7,133,139.0 | 385,185,619.0 | 102,430.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 392,695,239.0 | 390,315,731.0 | 395,289,860.0 | 2,034,505.3 | 5 | 40,136 | 59,994 | 28,051 | 0.005 | compiled=5 | 7,186,779.0 | 384,583,827.0 | 104,950.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 170,048,091.0 | 167,805,742.0 | 182,307,074.0 | 5,231,477.5 | 5 | 40,224 | 61,078 | 15,834 | 0.031 | compiled=5 | 7,161,556.0 | 162,068,808.0 | 187,742.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 186,482,449.0 | 184,001,209.0 | 193,589,084.0 | 3,495,199.3 | 5 | 40,368 | 65,816 | 17,809 | 0.019 | compiled=5 | 6,774,663.0 | 177,217,897.0 | 106,231.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 356,420,962.0 | 353,057,020.0 | 364,842,315.0 | 4,032,493.6 | 5 | 27,160 | 21,526 | 21,295 | 0.011 | compiled=5 | 3,118,260.0 | 351,939,272.0 | 191,741.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 349,586,857.0 | 347,715,425.0 | 352,057,343.0 | 1,438,999.8 | 5 | 27,160 | 21,639 | 21,408 | 0.004 (max is trial 1) | compiled=5 | 2,879,369.0 | 346,498,857.0 | 192,251.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 356,243,537.0 | 354,562,749.0 | 364,410,945.0 | 3,584,264.7 | 5 | 27,160 | 21,526 | 21,295 | 0.010 | compiled=5 | 4,320,625.0 | 350,800,425.0 | 197,661.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 348,865,264.0 | 340,447,955.0 | 368,724,901.0 | 10,004,352.4 | 5 | 27,160 | 21,639 | 21,408 | 0.029 | compiled=5 | 4,332,145.0 | 344,423,358.0 | 193,121.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 276,070,717.0 | 271,171,237.0 | 294,435,501.0 | 9,054,789.3 | 5 | 52,360 | 103,904 | 32,554 | 0.033 | compiled=5 | 8,626,965.0 | 267,383,683.0 | 112,220.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 293,445,927.0 | 284,778,442.0 | 301,736,271.0 | 5,411,568.6 | 5 | 52,456 | 111,143 | 33,982 | 0.018 | compiled=5 | 9,125,546.0 | 282,138,912.0 | 109,370.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 208,147,879.0 | 192,133,113.0 | 215,066,452.0 | 8,488,765.4 | 5 | 52,408 | 109,149 | 17,440 | 0.041 | compiled=5 | 9,522,305.0 | 198,577,224.0 | 192,291.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 218,783,712.0 | 208,800,863.0 | 221,625,854.0 | 4,496,439.0 | 5 | 56,640 | 117,707 | 19,304 | 0.021 | compiled=5 | 9,937,598.0 | 208,528,621.0 | 192,471.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 220,755,532.0 | 216,441,156.0 | 222,024,891.0 | 1,997,040.3 | 5 | 27,280 | 26,996 | 26,533 | 0.009 | compiled=5 | 2,968,749.0 | 217,693,413.0 | 191,681.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 222,372,885.0 | 212,243,499.0 | 222,815,685.0 | 4,566,779.6 | 5 | 27,280 | 27,109 | 26,646 | 0.021 | compiled=5 | 2,992,379.0 | 219,278,623.0 | 195,871.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 222,311,043.0 | 212,969,609.0 | 225,802,013.0 | 4,530,649.4 | 5 | 27,280 | 26,996 | 26,533 | 0.020 | compiled=5 | 4,467,476.0 | 217,657,105.0 | 100,101.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 223,005,178.0 | 215,333,982.0 | 228,274,548.0 | 4,778,318.1 | 5 | 27,280 | 27,109 | 26,646 | 0.021 | compiled=5 | 4,490,966.0 | 216,615,840.0 | 107,711.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 569,504,926.0 | 567,581,387.0 | 583,956,924.0 | 5,964,138.9 | 5 | 208,424 | 552,395 (warned) | 43,128 | 0.010 (max is trial 1) | compiled=5 | 57,909,115.0 | 511,934,392.0 | 101,211.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 579,094,734.0 | 575,303,779.0 | 605,514,711.0 | 11,338,459.5 | 5 | 212,616 | 567,185 (warned) | 44,416 | 0.020 | compiled=5 | 65,168,754.0 | 513,860,710.0 | 196,201.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 372,473,224.0 | 358,002,361.0 | 373,081,088.0 | 5,728,378.1 | 5 | 208,016 | 560,271 (warned) | 16,585 | 0.015 | compiled=5 | 59,249,213.0 | 308,791,136.0 | 98,241.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 392,197,579.0 | 376,754,767.0 | 395,760,747.0 | 6,855,432.3 | 5 | 216,344 | 576,684 (warned) | 18,313 | 0.017 | compiled=5 | 69,987,388.0 | 316,678,968.0 | 94,811.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 348,357,980.0 | 340,686,831.0 | 353,579,422.0 | 4,973,925.9 | 5 | 35,880 | 39,595 | 37,746 | 0.014 | compiled=5 | 3,287,221.0 | 344,205,762.0 | 120,891.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 352,796,248.0 | 343,062,015.0 | 354,980,601.0 | 4,147,749.5 | 5 | 35,880 | 39,708 | 37,859 | 0.012 | compiled=5 | 3,279,611.0 | 346,848,780.0 | 194,561.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 351,756,811.0 | 349,416,157.0 | 359,139,795.0 | 3,332,201.2 | 5 | 35,880 | 39,595 | 37,746 | 0.009 | compiled=5 | 4,733,408.0 | 346,878,683.0 | 197,251.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 351,276,679.0 | 346,362,869.0 | 354,020,675.0 | 2,504,518.2 | 5 | 35,880 | 39,708 | 37,859 | 0.007 | compiled=5 | 3,556,661.0 | 347,255,414.0 | 204,412.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 159,149,073.0 | 148,359,711.0 | 160,663,511.0 | 4,515,601.9 | 5 | 27,608 | 19,872 | 14,165 | 0.028 (max is trial 1) | compiled=5 | 3,128,012.0 | 154,033,334.0 | 136,211.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,928,057.0 | 153,338,590.0 | 162,944,790.0 | 3,739,569.5 | 5 | 27,752 | 21,932 | 15,325 | 0.023 | compiled=5 | 3,157,423.0 | 156,630,753.0 | 108,741.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 158,203,257.0 | 148,743,103.0 | 159,333,116.0 | 3,899,516.1 | 5 | 27,608 | 19,872 | 14,165 | 0.025 | compiled=5 | 3,145,255.0 | 153,008,257.0 | 211,601.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,743,280.0 | 152,100,859.0 | 168,256,036.0 | 6,014,982.9 | 5 | 27,752 | 21,932 | 15,325 | 0.038 | compiled=5 | 3,192,015.0 | 156,157,782.0 | 102,871.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 171,600,459.0 | 169,090,392.0 | 176,316,728.0 | 2,543,752.4 | 5 | 23,104 | 19,147 | 19,147 | 0.015 | compiled=5 | 2,791,858.0 | 168,711,680.0 | 105,241.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 173,479,100.0 | 172,898,196.0 | 187,893,392.0 | 5,746,686.6 | 5 | 23,104 | 19,260 | 19,260 | 0.033 | compiled=5 | 2,839,248.0 | 170,565,011.0 | 109,121.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,412,724.0 | 166,026,904.0 | 172,365,001.0 | 2,441,417.1 | 5 | 23,104 | 19,147 | 19,147 | 0.014 | compiled=5 | 2,917,147.0 | 168,505,677.0 | 100,060.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 171,932,487.0 | 164,037,551.0 | 172,440,420.0 | 3,172,472.6 | 5 | 23,104 | 19,260 | 19,260 | 0.018 | compiled=5 | 2,802,166.0 | 169,005,470.0 | 99,940.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 170,239,179.0 | 161,087,652.0 | 171,882,386.0 | 3,880,350.1 | 5 | 27,752 | 21,931 | 16,150 | 0.023 | compiled=5 | 3,099,222.0 | 166,618,505.0 | 109,800.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 156,352,413.0 | 146,566,733.0 | 165,602,471.0 | 6,447,855.4 | 5 | 27,752 | 21,503 | 15,722 | 0.041 | compiled=5 | 3,109,143.0 | 153,087,960.0 | 198,270.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 169,776,997.0 | 164,625,658.0 | 174,832,649.0 | 3,266,232.1 | 5 | 27,752 | 21,931 | 16,150 | 0.019 | compiled=5 | 3,104,974.0 | 166,476,032.0 | 100,340.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 164,518,847.0 | 155,011,723.0 | 167,072,538.0 | 4,166,739.9 | 5 | 27,752 | 21,503 | 15,722 | 0.025 | compiled=5 | 3,077,664.0 | 159,694,789.0 | 193,702.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 151,879,933.0 | 136,501,603.0 | 153,100,960.0 | 6,414,985.7 | 5 | 23,072 | 18,332 | 18,332 | 0.042 | compiled=5 | 2,785,538.0 | 148,917,403.0 | 201,812.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 151,653,640.0 | 129,578,899.0 | 154,045,945.0 | 9,080,277.3 | 5 | 23,072 | 18,444 | 18,444 | 0.060 | compiled=5 | 2,748,938.0 | 148,805,902.0 | 173,231.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 150,922,275.0 | 139,419,697.0 | 154,700,416.0 | 6,144,183.8 | 5 | 23,072 | 18,332 | 18,332 | 0.041 | compiled=5 | 2,813,776.0 | 147,867,426.0 | 186,611.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 139,064,165.0 | 136,598,431.0 | 150,899,894.0 | 5,943,146.9 | 5 | 23,072 | 18,444 | 18,444 | 0.043 | compiled=5 | 2,892,377.0 | 136,058,167.0 | 192,292.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 221,272,876.0 | 220,729,423.0 | 222,548,340.0 | 759,929.0 | 5 | 31,792 | 30,836 | 26,002 | 0.003 (max is trial 1) | compiled=5 | 3,125,153.0 | 217,775,491.0 | 107,760.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 217,005,479.0 | 215,939,034.0 | 230,666,863.0 | 5,488,017.1 | 5 | 31,880 | 32,315 | 27,251 | 0.025 | compiled=5 | 3,173,613.0 | 213,621,865.0 | 193,521.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 156,163,011.0 | 149,773,913.0 | 161,627,344.0 | 3,995,424.8 | 5 | 27,608 | 20,475 | 13,956 | 0.026 | compiled=5 | 3,193,275.0 | 150,799,200.0 | 100,171.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 163,662,750.0 | 158,064,107.0 | 164,612,888.0 | 2,459,056.1 | 5 | 27,744 | 22,624 | 15,753 | 0.015 | compiled=5 | 3,212,436.0 | 160,260,384.0 | 205,062.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 189,987,875.0 | 177,546,986.0 | 192,885,154.0 | 6,477,143.2 | 5 | 27,320 | 21,614 | 21,614 | 0.034 | compiled=5 | 2,837,938.0 | 187,070,797.0 | 179,942.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 193,065,746.0 | 186,361,482.0 | 196,975,321.0 | 3,866,205.9 | 5 | 27,320 | 21,728 | 21,728 | 0.020 | compiled=5 | 4,478,569.0 | 189,847,724.0 | 104,551.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 191,915,445.0 | 185,668,988.0 | 193,111,172.0 | 3,266,887.7 | 5 | 27,320 | 21,614 | 21,614 | 0.017 | compiled=5 | 2,856,377.0 | 188,878,646.0 | 192,781.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 192,575,497.0 | 188,367,284.0 | 197,693,528.0 | 2,995,445.4 | 5 | 27,320 | 21,728 | 21,728 | 0.016 | compiled=5 | 2,847,786.0 | 189,535,720.0 | 191,731.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 146,257,981.0 | 137,740,078.0 | 152,840,579.0 | 5,647,547.2 | 5 | 27,432 | 14,458 | 12,101 | 0.039 | compiled=5 | 5,821,743.0 | 140,121,557.0 | 107,851.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 141,209,102.0 | 137,906,808.0 | 143,611,992.0 | 2,075,453.4 | 5 | 27,432 | 14,281 | 11,924 | 0.015 (max is trial 1) | compiled=5 | 4,330,628.0 | 136,666,233.0 | 107,580.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 145,051,457.0 | 130,466,098.0 | 147,225,086.0 | 6,172,011.3 | 5 | 27,432 | 14,458 | 12,101 | 0.043 | compiled=5 | 5,938,374.0 | 139,557,975.0 | 102,421.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 143,478,850.0 | 136,129,701.0 | 150,390,949.0 | 5,252,228.0 | 5 | 27,432 | 14,281 | 11,924 | 0.037 (max is trial 1) | compiled=5 | 4,983,410.0 | 138,413,920.0 | 190,131.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 235,926,740.0 | 232,438,397.0 | 244,239,513.0 | 3,887,304.2 | 5 | 27,440 | 26,143 | 25,450 | 0.016 (max is trial 1) | compiled=5 | 4,416,509.0 | 231,322,110.0 | 192,291.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 236,136,471.0 | 235,293,935.0 | 241,284,354.0 | 2,187,484.5 | 5 | 27,440 | 26,256 | 25,563 | 0.009 | compiled=5 | 4,435,259.0 | 231,300,960.0 | 108,450.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 232,942,205.0 | 230,666,822.0 | 234,412,054.0 | 1,203,495.7 | 5 | 27,440 | 26,143 | 25,450 | 0.005 | compiled=5 | 3,008,058.0 | 229,420,884.0 | 100,861.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 232,120,251.0 | 223,798,251.0 | 234,573,764.0 | 4,617,126.0 | 5 | 27,440 | 26,256 | 25,563 | 0.020 | compiled=5 | 2,937,978.0 | 229,074,472.0 | 99,051.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 319,449,223.0 | 312,857,497.0 | 323,983,913.0 | 4,475,166.3 | 5 | 40,776 | 44,485 | 39,457 | 0.014 (max is trial 1) | compiled=5 | 4,763,369.0 | 314,583,853.0 | 102,001.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 317,175,623.0 | 308,967,211.0 | 326,739,452.0 | 6,576,764.5 | 5 | 40,568 | 43,668 | 38,640 | 0.021 | compiled=5 | 4,830,739.0 | 312,135,764.0 | 218,031.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 168,902,904.0 | 159,442,066.0 | 173,521,404.0 | 5,057,672.9 | 5 | 32,424 | 21,844 | 16,816 | 0.030 | compiled=5 | 4,464,428.0 | 164,987,158.0 | 192,351.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 153,111,440.0 | 152,285,977.0 | 161,850,285.0 | 3,636,546.9 | 5 | 32,224 | 20,922 | 15,894 | 0.024 | compiled=5 | 4,706,249.0 | 148,447,742.0 | 103,360.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 278,950,385.0 | 268,262,477.0 | 282,013,826.0 | 4,734,106.8 | 5 | 27,240 | 31,561 | 31,561 | 0.017 | compiled=5 | 4,637,400.0 | 274,149,874.0 | 190,051.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 279,216,916.0 | 274,448,076.0 | 282,932,810.0 | 3,071,931.3 | 5 | 27,240 | 31,674 | 31,674 | 0.011 | compiled=5 | 4,503,238.0 | 274,609,607.0 | 104,071.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 275,767,565.0 | 272,253,266.0 | 288,335,810.0 | 5,493,632.1 | 5 | 27,240 | 31,561 | 31,561 | 0.020 | compiled=5 | 1,806,120.0 | 273,861,175.0 | 106,141.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 277,399,684.0 | 262,612,299.0 | 281,069,667.0 | 6,837,760.7 | 5 | 27,240 | 31,674 | 31,674 | 0.025 | compiled=5 | 3,039,188.0 | 274,168,196.0 | 191,461.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 211,249,816.0 | 194,114,456.0 | 222,907,772.0 | 9,755,109.6 | 5 | 31,888 | 26,794 | 24,250 | 0.046 | compiled=5 | 4,486,819.0 | 206,585,537.0 | 197,391.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 203,272,842.0 | 197,433,149.0 | 214,359,437.0 | 5,722,182.0 | 5 | 31,808 | 26,534 | 23,990 | 0.028 | compiled=5 | 4,658,419.0 | 196,442,775.0 | 210,271.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 146,388,503.0 | 139,030,423.0 | 152,186,105.0 | 5,549,406.5 | 5 | 27,672 | 15,696 | 13,152 | 0.038 | compiled=5 | 4,405,298.0 | 140,637,960.0 | 105,460.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 150,201,559.0 | 137,118,526.0 | 157,235,697.0 | 6,544,801.4 | 5 | 23,496 | 15,333 | 12,789 | 0.044 (max is trial 1) | compiled=5 | 4,461,888.0 | 144,786,736.0 | 210,851.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 189,219,351.0 | 188,933,469.0 | 196,010,504.0 | 2,694,502.6 | 5 | 27,200 | 20,258 | 20,258 | 0.014 | compiled=5 | 4,306,868.0 | 184,814,163.0 | 192,451.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 188,375,524.0 | 183,893,517.0 | 189,558,293.0 | 2,002,197.4 | 5 | 27,200 | 20,369 | 20,369 | 0.011 | compiled=5 | 4,343,837.0 | 183,921,166.0 | 107,471.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 187,847,860.0 | 179,279,731.0 | 191,823,533.0 | 4,546,011.2 | 5 | 27,200 | 20,258 | 20,258 | 0.024 (max is trial 1) | compiled=5 | 2,984,798.0 | 184,643,572.0 | 187,761.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 178,930,889.0 | 175,765,251.0 | 196,870,283.0 | 7,939,083.3 | 5 | 27,200 | 20,369 | 20,369 | 0.044 (max is trial 1) | compiled=5 | 2,871,797.0 | 175,898,231.0 | 189,601.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 247,682,312.0 | 240,481,094.0 | 248,997,578.0 | 3,078,098.7 | 5 | 36,384 | 46,458 | 21,140 | 0.012 | compiled=5 | 5,805,044.0 | 241,534,518.0 | 187,371.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 256,930,891.0 | 249,774,811.0 | 263,726,418.0 | 4,706,615.1 | 5 | 36,528 | 49,319 | 22,728 | 0.018 | compiled=5 | 6,645,247.0 | 250,158,703.0 | 194,881.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 247,233,551.0 | 240,886,345.0 | 250,859,796.0 | 3,354,742.4 | 5 | 36,384 | 46,458 | 21,140 | 0.014 | compiled=5 | 5,819,154.0 | 241,341,748.0 | 119,530.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 253,920,639.0 | 248,532,597.0 | 265,574,554.0 | 5,834,472.7 | 5 | 36,528 | 49,319 | 22,728 | 0.023 (max is trial 1) | compiled=5 | 5,896,864.0 | 247,922,724.0 | 110,411.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 255,968,938.0 | 242,113,439.0 | 259,235,077.0 | 6,257,049.0 | 5 | 27,208 | 20,758 | 20,527 | 0.024 (max is trial 1) | compiled=5 | 4,344,708.0 | 251,479,759.0 | 103,230.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 257,143,275.0 | 252,861,780.0 | 267,977,995.0 | 5,014,966.8 | 5 | 27,208 | 20,869 | 20,638 | 0.020 | compiled=5 | 2,869,018.0 | 254,187,097.0 | 102,240.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 254,496,131.0 | 245,317,408.0 | 257,181,216.0 | 4,904,959.1 | 5 | 27,208 | 20,758 | 20,527 | 0.019 | compiled=5 | 2,867,416.0 | 251,535,714.0 | 192,341.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 257,502,889.0 | 244,746,214.0 | 262,671,969.0 | 6,046,823.5 | 5 | 27,208 | 20,869 | 20,638 | 0.023 | compiled=5 | 2,880,677.0 | 254,540,752.0 | 195,511.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 227,134,130.0 | 223,995,726.0 | 238,869,167.0 | 5,835,510.6 | 5 | 85,552 | 226,458 | 18,492 | 0.026 | compiled=5 | 15,925,814.0 | 208,141,093.0 | 101,211.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 238,651,955.0 | 220,408,663.0 | 258,700,857.0 | 12,457,062.7 | 5 | 89,792 | 236,289 | 20,468 | 0.052 | compiled=5 | 18,250,574.0 | 214,784,340.0 | 186,751.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 228,271,995.0 | 212,596,242.0 | 241,572,701.0 | 9,180,968.4 | 5 | 85,552 | 226,458 | 18,492 | 0.040 | compiled=5 | 15,541,691.0 | 212,564,033.0 | 104,480.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 247,265,545.0 | 235,048,288.0 | 263,025,068.0 | 10,265,440.0 | 5 | 89,792 | 236,289 | 20,468 | 0.042 | compiled=5 | 17,320,966.0 | 225,374,953.0 | 192,472.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 442,791,214.0 | 432,308,266.0 | 458,046,291.0 | 8,825,710.4 | 5 | 31,376 | 59,509 | 59,046 | 0.020 | compiled=5 | 3,608,043.0 | 439,060,230.0 | 192,311.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 445,648,142.0 | 443,114,044.0 | 453,304,289.0 | 3,820,898.4 | 5 | 31,376 | 59,624 | 59,161 | 0.009 | compiled=5 | 3,630,543.0 | 441,771,967.0 | 191,071.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 445,315,330.0 | 436,622,848.0 | 446,236,326.0 | 3,582,616.2 | 5 | 31,376 | 59,509 | 59,046 | 0.008 | compiled=5 | 5,054,220.0 | 440,046,339.0 | 110,531.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 445,959,204.0 | 435,549,912.0 | 459,724,284.0 | 7,778,912.1 | 5 | 31,376 | 59,624 | 59,161 | 0.017 (max is trial 1) | compiled=5 | 3,633,912.0 | 440,768,633.0 | 191,031.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 194,253,466.0 | 185,285,320.0 | 201,328,894.0 | 5,187,369.6 | 5 | 36,248 | 56,740 | 16,340 | 0.027 (max is trial 1) | compiled=5 | 5,688,423.0 | 188,464,763.0 | 192,611.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 203,047,192.0 | 193,550,994.0 | 213,175,603.0 | 8,020,576.6 | 5 | 36,392 | 60,519 | 18,131 | 0.040 (max is trial 1) | compiled=5 | 12,925,443.0 | 189,499,017.0 | 100,860.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 186,364,388.0 | 179,356,982.0 | 194,571,853.0 | 5,359,346.4 | 5 | 36,248 | 56,740 | 16,340 | 0.029 | compiled=5 | 5,676,285.0 | 180,465,312.0 | 101,011.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 202,150,411.0 | 194,821,035.0 | 212,322,291.0 | 6,720,560.4 | 5 | 36,392 | 60,519 | 18,131 | 0.033 | compiled=5 | 6,215,098.0 | 193,265,652.0 | 109,481.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 223,493,731.0 | 218,114,274.0 | 228,575,992.0 | 3,348,409.0 | 5 | 27,280 | 25,397 | 24,935 | 0.015 (max is trial 1) | compiled=5 | 2,916,658.0 | 220,789,733.0 | 192,971.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 222,703,965.0 | 217,408,582.0 | 231,738,932.0 | 5,362,454.3 | 5 | 27,280 | 25,510 | 25,048 | 0.024 | compiled=5 | 2,957,119.0 | 219,099,902.0 | 194,591.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 224,049,353.0 | 217,445,724.0 | 226,502,198.0 | 3,232,118.7 | 5 | 27,280 | 25,397 | 24,935 | 0.014 | compiled=5 | 2,961,417.0 | 220,650,863.0 | 103,361.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 215,874,235.0 | 212,633,956.0 | 236,194,224.0 | 8,692,452.4 | 5 | 27,280 | 25,510 | 25,048 | 0.040 | compiled=5 | 2,975,288.0 | 210,850,406.0 | 206,541.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 162,295,137.0 | 160,284,729.0 | 170,359,200.0 | 3,910,381.5 | 5 | 27,872 | 35,424 | 14,257 | 0.024 | compiled=5 | 4,404,548.0 | 157,677,678.0 | 110,601.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 172,723,969.0 | 164,788,337.0 | 179,331,506.0 | 4,634,686.1 | 5 | 32,112 | 38,448 | 16,269 | 0.027 | compiled=5 | 5,110,051.0 | 167,892,959.0 | 193,761.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 169,684,098.0 | 151,882,308.0 | 172,197,078.0 | 7,406,529.6 | 5 | 27,872 | 35,424 | 14,257 | 0.044 | compiled=5 | 4,467,675.0 | 165,172,032.0 | 187,391.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 177,088,756.0 | 172,318,179.0 | 182,079,694.0 | 3,406,352.0 | 5 | 32,112 | 38,448 | 16,269 | 0.019 | compiled=5 | 4,483,545.0 | 172,505,620.0 | 106,951.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 190,642,249.0 | 185,111,234.0 | 200,585,304.0 | 5,242,280.1 | 5 | 27,240 | 22,695 | 22,464 | 0.027 | compiled=5 | 2,884,909.0 | 187,335,038.0 | 189,851.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 188,466,896.0 | 182,459,608.0 | 191,953,027.0 | 3,952,786.2 | 5 | 27,240 | 22,808 | 22,577 | 0.021 | compiled=5 | 2,869,698.0 | 185,399,536.0 | 106,111.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 191,969,075.0 | 183,844,277.0 | 195,143,983.0 | 3,962,724.9 | 5 | 27,240 | 22,695 | 22,464 | 0.021 | compiled=5 | 2,884,937.0 | 188,884,067.0 | 197,281.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 191,235,920.0 | 190,893,018.0 | 195,937,950.0 | 2,071,549.9 | 5 | 27,240 | 22,808 | 22,577 | 0.011 | compiled=5 | 2,901,287.0 | 188,140,912.0 | 189,322.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 1,464,950,299.0 | 1,454,057,136.0 | 1,474,095,788.0 | 7,069,562.6 | 5 | 680,264 | 393,519 (warned) | 99,039 | 0.005 | compiled=5 | 13,215,754.0 | 1,451,529,785.0 | 293,221.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 1,411,562,384.0 | 1,363,203,538.0 | 1,432,832,771.0 | 24,583,631.6 | 5 | 659,736 | 400,725 (warned) | 101,189 | 0.017 | compiled=5 | 26,158,826.0 | 1,384,871,796.0 | 277,181.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,452,415,171.0 | 1,408,914,032.0 | 1,482,074,916.0 | 25,121,688.7 | 5 | 680,264 | 393,519 (warned) | 99,039 | 0.017 (max is trial 1) | compiled=5 | 14,588,264.0 | 1,439,871,104.0 | 538,204.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,389,513,590.0 | 1,371,933,163.0 | 1,407,704,923.0 | 12,141,888.2 | 5 | 659,736 | 400,725 (warned) | 101,189 | 0.009 | compiled=5 | 26,723,379.0 | 1,361,740,803.0 | 526,394.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 1,664,433,159.0 | 1,662,877,410.0 | 1,667,698,332.0 | 2,003,200.5 | 5 | 60,264 | 182,804 | 181,181 | 0.001 | compiled=5 | 7,296,026.0 | 1,658,555,372.0 | 202,312.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 1,677,455,223.0 | 1,660,815,107.0 | 1,686,051,779.0 | 8,747,362.2 | 5 | 60,264 | 182,919 | 181,296 | 0.005 | compiled=5 | 7,335,697.0 | 1,669,052,890.0 | 193,101.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 1,660,108,428.0 | 1,655,055,748.0 | 1,664,334,354.0 | 3,367,357.7 | 5 | 60,264 | 182,804 | 181,181 | 0.002 (max is trial 1) | compiled=5 | 7,381,674.0 | 1,652,262,632.0 | 199,861.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 1,666,439,324.0 | 1,661,895,488.0 | 1,669,675,345.0 | 2,538,897.3 | 5 | 60,264 | 182,919 | 181,296 | 0.002 | compiled=5 | 7,371,713.0 | 1,659,009,921.0 | 192,551.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 157,345,075.0 | 147,392,996.0 | 162,640,099.0 | 4,955,040.1 | 5 | 27,608 | 19,611 | 13,699 | 0.031 | compiled=5 | 4,688,899.0 | 152,474,617.0 | 126,100.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 165,711,011.0 | 151,455,943.0 | 168,638,522.0 | 6,159,116.4 | 5 | 27,752 | 22,218 | 15,788 | 0.037 | compiled=5 | 4,757,970.0 | 160,760,811.0 | 173,021.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 157,418,490.0 | 147,202,521.0 | 163,616,230.0 | 6,902,630.6 | 5 | 27,608 | 19,611 | 13,699 | 0.044 | compiled=5 | 4,741,638.0 | 152,626,214.0 | 197,572.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 163,520,500.0 | 159,685,469.0 | 174,875,576.0 | 6,325,210.9 | 5 | 27,752 | 22,218 | 15,788 | 0.039 | compiled=5 | 4,860,878.0 | 160,837,389.0 | 191,422.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 186,176,881.0 | 182,096,715.0 | 190,892,542.0 | 3,310,471.2 | 5 | 27,320 | 21,895 | 21,202 | 0.018 | compiled=5 | 4,452,638.0 | 181,620,462.0 | 106,701.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 183,408,423.0 | 182,422,807.0 | 196,470,837.0 | 5,361,918.9 | 5 | 27,320 | 22,008 | 21,315 | 0.029 | compiled=5 | 2,874,449.0 | 180,534,065.0 | 202,201.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 190,393,186.0 | 181,390,872.0 | 194,004,145.0 | 4,354,235.5 | 5 | 27,320 | 21,895 | 21,202 | 0.023 | compiled=5 | 4,394,136.0 | 185,791,999.0 | 98,741.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 186,901,386.0 | 182,118,016.0 | 199,077,517.0 | 5,954,458.5 | 5 | 27,320 | 22,008 | 21,315 | 0.032 | compiled=5 | 4,354,825.0 | 180,722,858.0 | 207,521.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 136,749,004.0 | 132,142,125.0 | 144,604,726.0 | 4,722,919.7 | 5 | 27,392 | 13,845 | 11,762 | 0.035 | compiled=5 | 2,882,501.0 | 132,233,135.0 | 187,911.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 140,782,970.0 | 124,603,954.0 | 144,039,093.0 | 7,941,845.9 | 5 | 23,256 | 13,668 | 11,585 | 0.056 | compiled=5 | 2,736,801.0 | 137,926,148.0 | 195,131.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 136,961,931.0 | 131,124,307.0 | 143,967,626.0 | 5,091,711.2 | 5 | 27,392 | 13,845 | 11,762 | 0.037 | compiled=5 | 2,793,342.0 | 133,950,198.0 | 204,812.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 137,315,412.0 | 132,543,837.0 | 144,526,320.0 | 4,452,634.9 | 5 | 23,256 | 13,668 | 11,585 | 0.032 | compiled=5 | 2,851,982.0 | 132,760,168.0 | 101,181.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 197,480,485.0 | 195,905,003.0 | 207,335,836.0 | 4,125,993.7 | 5 | 27,400 | 23,634 | 23,172 | 0.021 | compiled=5 | 2,908,879.0 | 194,126,152.0 | 107,150.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 204,597,438.0 | 203,853,654.0 | 206,232,689.0 | 936,299.8 | 5 | 27,400 | 23,747 | 23,285 | 0.005 | compiled=5 | 3,102,040.0 | 200,910,596.0 | 103,120.0 |
| `winpath-near-miss` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 204,792,861.0 | 196,818,023.0 | 205,328,423.0 | 3,241,521.9 | 5 | 27,400 | 23,634 | 23,172 | 0.016 | compiled=5 | 4,445,376.0 | 200,228,633.0 | 188,191.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 203,272,571.0 | 196,604,482.0 | 205,843,307.0 | 3,417,540.9 | 5 | 27,400 | 23,747 | 23,285 | 0.017 (max is trial 1) | compiled=5 | 4,387,966.0 | 198,691,824.0 | 187,841.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 116,951.0 | 100,901.0 | 567,473.0 | 177,913.3 | 5 | - | 1.521 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 318,622.0 | 255,431.0 | 1,302,157.0 | 395,348.2 | 5 | - | 1.241 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,601,705.0 | 1,942,811.0 | 2,693,715.0 | 273,747.9 | 5 | 5,896 | 0.105 | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,730,596.0 | 2,653,384.0 | 3,880,552.0 | 469,775.2 | 5 | 6,376 | 0.172 (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `rust_1.13.1_default-caps-simdna` | 189,341.0 | 174,541.0 | 1,140,066.0 | 378,218.3 | 5 | - | 1.998 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 86,161.0 | 66,821.0 | 540,223.0 | 179,424.3 | 5 | - | 2.082 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,341,367.0 | 1,268,857.0 | 2,475,703.0 | 463,672.2 | 5 | 6,088 | 0.346 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,689,789.0 | 1,648,729.0 | 2,804,845.0 | 450,060.8 | 5 | 3,672 | 0.266 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `rust_1.13.1_default-caps-simdna` | 109,320.0 | 84,270.0 | 640,944.0 | 211,272.2 | 5 | - | 1.933 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 113,601.0 | 85,131.0 | 650,093.0 | 216,066.3 | 5 | - | 1.902 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,157,757.0 | 1,134,946.0 | 2,098,662.0 | 376,120.8 | 5 | 6,088 | 0.325 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,500,288.0 | 1,440,538.0 | 2,503,204.0 | 405,724.0 | 5 | 3,672 | 0.270 (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 24,850.0 | 19,540.0 | 239,751.0 | 86,429.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 26,830.0 | 22,331.0 | 224,701.0 | 78,658.8 | 5 | - | 2.932 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,099,016.0 | 1,074,746.0 | 2,083,761.0 | 391,192.5 | 5 | 5,736 | 0.356 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 467,892.0 | 451,462.0 | 969,566.0 | 199,974.1 | 5 | 6,024 | 0.427 (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 21,220.0 | 16,740.0 | 218,281.0 | 78,669.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 24,430.0 | 22,241.0 | 230,431.0 | 81,593.0 | 5 | - | 3.340 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 599,444.0 | 539,453.0 | 1,517,699.0 | 376,219.0 | 5 | 5,784 | 0.628 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 349,952.0 | 327,382.0 | 836,954.0 | 197,287.6 | 5 | 6,232 | 0.564 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `rust_1.13.1_default-caps-simdna` | 28,390.0 | 17,620.0 | 229,392.0 | 82,354.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 55,071.0 | 50,940.0 | 483,683.0 | 170,279.1 | 5 | - | 3.092 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 602,864.0 | 577,933.0 | 1,558,099.0 | 378,850.6 | 5 | 5,704 | 0.628 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 298,931.0 | 288,732.0 | 754,424.0 | 182,045.8 | 5 | 5,992 | 0.609 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 16,471.0 | 14,150.0 | 398,362.0 | 151,686.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 78,881.0 | 56,200.0 | 476,992.0 | 163,751.7 | 5 | - | 2.076 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 453,142.0 | 402,092.0 | 1,281,907.0 | 341,766.9 | 5 | 4,776 | 0.754 (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 513,023.0 | 484,483.0 | 1,314,667.0 | 322,241.3 | 5 | 2,120 | 0.628 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,751.0 | 4,310.0 | 411,842.0 | 161,656.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 14,690.0 | 10,980.0 | 257,632.0 | 96,904.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 85,120.0 | 77,710.0 | 516,753.0 | 173,254.7 | 5 | 936 | 2.035 (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 286,772.0 | 272,441.0 | 1,056,776.0 | 306,837.6 | 5 | 1,704 | 1.070 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `rust_1.13.1_default-caps-simdna` | 87,870.0 | 79,501.0 | 936,965.0 | 335,025.5 | 5 | - | 3.813 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 62,510.0 | 46,390.0 | 525,753.0 | 185,770.8 | 5 | - | 2.972 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 488,073.0 | 466,283.0 | 1,332,437.0 | 336,668.2 | 5 | 5,784 | 0.690 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 447,673.0 | 431,832.0 | 1,247,647.0 | 319,748.8 | 5 | 1,832 | 0.714 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 583,433.0 | 473,893.0 | 1,074,366.0 | 210,207.2 | 5 | - | 0.360 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 598,644.0 | 472,152.0 | 1,089,996.0 | 213,541.8 | 5 | - | 0.357 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,039,206.0 | 1,016,456.0 | 1,673,419.0 | 252,953.5 | 5 | 3,464 | 0.243 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 757,394.0 | 747,324.0 | 1,548,878.0 | 318,325.6 | 5 | 2,824 | 0.420 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 9,761.0 | 6,770.0 | 223,511.0 | 85,518.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 25,630.0 | 21,110.0 | 230,121.0 | 81,842.8 | 5 | - | 3.193 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 486,752.0 | 439,843.0 | 1,280,957.0 | 321,804.7 | 5 | 4,840 | 0.661 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 571,283.0 | 538,633.0 | 1,385,847.0 | 329,286.8 | 5 | 2,504 | 0.576 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `rust_1.13.1_default-caps-simdna` | 178,941.0 | 162,011.0 | 720,064.0 | 213,453.5 | 5 | - | 1.193 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 351,172.0 | 324,992.0 | 1,348,927.0 | 396,177.5 | 5 | - | 1.128 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,743,751.0 | 3,734,911.0 | 4,682,176.0 | 376,525.6 | 5 | 10,168 | 0.101 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,976,852.0 | 3,429,409.0 | 10,170,436.0 | 2,744,430.5 | 5 | 9,496 | 0.690 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `mojibake-curly-quote` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `mojibake-curly-quote` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 643,883.0 | 600,283.0 | 1,547,509.0 | 363,383.5 | 5 | 5,992 | 0.564 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 946,185.0 | 938,515.0 | 1,951,041.0 | 398,843.0 | 5 | 3,352 | 0.422 (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 82,010.0 | 68,211.0 | 512,123.0 | 169,204.8 | 5 | - | 2.063 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 85,571.0 | 74,050.0 | 552,873.0 | 183,994.3 | 5 | - | 2.150 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 831,775.0 | 804,094.0 | 1,808,090.0 | 391,153.3 | 5 | 5,704 | 0.470 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 364,652.0 | 349,032.0 | 821,585.0 | 185,460.6 | 5 | 5,992 | 0.509 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `rust_1.13.1_default-caps-simdna` | 99,941.0 | 78,021.0 | 526,583.0 | 171,140.2 | 5 | - | 1.712 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 230,651.0 | 190,251.0 | 1,172,336.0 | 379,685.7 | 5 | - | 1.646 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 995,555.0 | 920,785.0 | 1,982,391.0 | 400,356.7 | 5 | 5,736 | 0.402 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 409,542.0 | 389,663.0 | 890,635.0 | 192,579.4 | 5 | 5,992 | 0.470 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `rust_1.13.1_default-caps-simdna` | 22,420.0 | 15,900.0 | 465,162.0 | 177,266.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 22,510.0 | 21,330.0 | 220,722.0 | 78,363.8 | 5 | - | 3.481 (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 448,492.0 | 433,263.0 | 1,242,337.0 | 319,634.3 | 5 | 4,776 | 0.713 (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 488,393.0 | 462,462.0 | 1,281,117.0 | 318,088.5 | 5 | 2,120 | 0.651 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `trim-nested-star` | `plain` | `rust_1.13.1_default-caps-simdna` | 138,211.0 | 106,140.0 | 1,061,766.0 | 369,583.2 | 5 | - | 2.674 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 137,910.0 | 107,751.0 | 1,056,606.0 | 369,913.9 | 5 | - | 2.682 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 751,744.0 | 705,894.0 | 1,724,129.0 | 394,470.3 | 5 | 5,736 | 0.525 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,528,538.0 | 1,488,108.0 | 2,599,414.0 | 430,216.7 | 5 | 2,600 | 0.281 (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 54,360.0 | 42,290.0 | 256,322.0 | 82,678.5 | 5 | - | 1.521 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 72,161.0 | 56,980.0 | 315,642.0 | 99,466.2 | 5 | - | 1.378 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 496,452.0 | 491,583.0 | 943,886.0 | 177,907.4 | 5 | 2,216 | 0.358 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,177,797.0 | 1,154,736.0 | 1,476,808.0 | 119,852.4 | 5 | 2,088 | 0.102 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 4,030.0 | 1,600.0 | 182,501.0 | 71,804.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,890.0 | 8,690.0 | 215,041.0 | 80,925.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 47,340.0 | 43,070.0 | 310,071.0 | 105,168.8 | 5 | 936 | 2.222 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 353,372.0 | 329,412.0 | 1,256,017.0 | 361,128.2 | 5 | 1,704 | 1.022 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `rust_1.13.1_default-caps-simdna` | 174,531.0 | 142,660.0 | 628,004.0 | 186,269.4 | 5 | - | 1.067 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 33,900.0 | 27,260.0 | 233,161.0 | 78,810.4 | 5 | - | 2.325 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,197,568.0 | 3,153,447.0 | 4,482,724.0 | 520,855.4 | 5 | 7,928 | 0.163 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 718,854.0 | 673,224.0 | 1,530,249.0 | 332,334.3 | 5 | 2,504 | 0.462 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `rust_1.13.1_default-caps-simdna` | 438,782.0 | 260,701.0 | 774,364.0 | 172,180.9 | 5 | - | 0.392 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 174,291.0 | 151,861.0 | 653,544.0 | 191,382.9 | 5 | - | 1.098 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,608,480.0 | 3,604,380.0 | 4,778,067.0 | 465,877.9 | 5 | 6,504 | 0.129 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,700.0 | 4,250.0 | 369,152.0 | 144,627.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 14,110.0 | 10,470.0 | 242,821.0 | 91,154.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 95,971.0 | 88,571.0 | 549,213.0 | 181,698.2 | 5 | 936 | 1.893 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 126,950.0 | 121,941.0 | 580,423.0 | 180,966.0 | 5 | 1,704 | 1.425 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `rust_1.13.1_default-caps-simdna` | 143,540.0 | 114,000.0 | 523,473.0 | 157,645.0 | 5 | - | 1.098 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 35,520.0 | 29,301.0 | 243,022.0 | 82,909.0 | 5 | - | 2.334 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 267,192.0 | 232,831.0 | 712,134.0 | 184,073.6 | 5 | 2,056 | 0.689 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `rust_1.13.1_default-caps-simdna` | 10,419,848.0 | 9,863,215.0 | 13,502,085.0 | 1,313,707.9 | 5 | - | 0.126 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 10,364,068.0 | 9,786,714.0 | 13,425,294.0 | 1,313,975.4 | 5 | - | 0.127 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,783,817,252.0 | 1,778,505,152.0 | 1,825,940,595.0 | 17,521,944.8 | 5 | 158,072 | 0.010 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,733,371,681.0 | 1,726,046,281.0 | 1,770,429,307.0 | 16,022,676.3 | 5 | 141,928 | 0.009 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `rust_1.13.1_default-caps-simdna` | 2,519,274.0 | 2,385,973.0 | 4,495,445.0 | 793,764.1 | 5 | - | 0.315 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,273,117.0 | 1,225,367.0 | 2,140,242.0 | 345,235.0 | 5 | - | 0.271 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,330,228.0 | 2,978,827.0 | 8,929,459.0 | 2,456,153.5 | 5 | 4,232 | 0.738 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,155,457.0 | 2,973,857.0 | 8,867,840.0 | 2,497,173.1 | 5 | 4,488 | 0.791 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `rust_1.13.1_default-caps-simdna` | 55,520.0 | 52,940.0 | 281,721.0 | 89,610.9 | 5 | - | 1.614 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 52,191.0 | 46,780.0 | 276,232.0 | 89,465.4 | 5 | - | 1.714 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,559,305.0 | 2,242,442.0 | 5,735,332.0 | 1,153,145.1 | 5 | 11,752 | 0.253 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,005,991.0 | 1,737,369.0 | 3,558,630.0 | 655,729.9 | 5 | 3,464 | 0.327 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `rust_1.13.1_default-caps-simdna` | 93,260.0 | 76,080.0 | 308,752.0 | 88,607.6 | 5 | - | 0.950 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 93,131.0 | 75,170.0 | 301,651.0 | 85,434.4 | 5 | - | 0.917 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,152,063.0 | 2,311,273.0 | 5,494,430.0 | 1,020,993.5 | 5 | 7,224 | 0.246 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,028,523.0 | 2,090,832.0 | 5,744,422.0 | 1,195,224.3 | 5 | 2,352 | 0.297 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `rust_1.13.1_default-caps-simdna` | 669,433.0 | 587,454.0 | 1,220,047.0 | 236,028.8 | 5 | - | 0.353 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 998,545.0 | 870,955.0 | 2,039,372.0 | 439,957.6 | 5 | - | 0.441 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,440,639.0 | 2,645,184.0 | 5,062,378.0 | 793,853.5 | 5 | 3,504 | 0.231 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,642,600.0 | 2,697,515.0 | 5,257,349.0 | 834,315.1 | 5 | 5,048 | 0.229 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `rust_1.13.1_default-caps-simdna` | 401,053.0 | 347,012.0 | 930,995.0 | 214,795.3 | 5 | - | 0.536 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 461,663.0 | 391,493.0 | 1,041,346.0 | 242,741.2 | 5 | - | 0.526 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 26,744,138.0 | 26,459,177.0 | 39,956,152.0 | 5,330,614.1 | 5 | 129,576 | 0.199 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,987,098.0 | 4,931,397.0 | 12,615,860.0 | 2,967,324.1 | 5 | 10,072 | 0.595 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `rust_1.13.1_default-caps-simdna` | 7,530.0 | 5,850.0 | 232,401.0 | 89,470.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 34,780.0 | 25,500.0 | 276,041.0 | 97,877.2 | 5 | - | 2.814 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 415,362.0 | 394,702.0 | 1,215,657.0 | 318,221.0 | 5 | 4,776 | 0.766 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 488,953.0 | 459,522.0 | 1,264,947.0 | 312,739.6 | 5 | 2,120 | 0.640 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 31,650.0 | 25,450.0 | 430,782.0 | 158,609.9 | 5 | - | 5.011 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 35,640.0 | 27,461.0 | 448,053.0 | 164,536.4 | 5 | - | 4.617 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 508,223.0 | 471,353.0 | 1,343,867.0 | 337,180.5 | 5 | 5,592 | 0.663 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 313,621.0 | 296,822.0 | 1,053,766.0 | 295,792.5 | 5 | 1,832 | 0.943 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `rust_1.13.1_default-caps-simdna` | 208,511.0 | 179,801.0 | 1,184,176.0 | 389,713.9 | 5 | - | 1.869 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 201,772.0 | 164,891.0 | 1,154,886.0 | 381,874.2 | 5 | - | 1.893 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 513,813.0 | 474,103.0 | 1,334,568.0 | 330,374.9 | 5 | 3,944 | 0.643 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 997,416.0 | 954,666.0 | 1,942,640.0 | 383,172.5 | 5 | 6,056 | 0.384 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 35,701.0 | 31,730.0 | 248,091.0 | 84,062.4 | 5 | - | 2.355 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 42,170.0 | 36,940.0 | 230,421.0 | 74,826.6 | 5 | - | 1.774 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,046,576.0 | 973,676.0 | 2,003,641.0 | 393,529.0 | 5 | 6,104 | 0.376 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,248,197.0 | 1,180,417.0 | 2,277,183.0 | 421,875.7 | 5 | 6,488 | 0.338 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 106,680.0 | 90,211.0 | 366,592.0 | 106,380.3 | 5 | - | 0.997 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 222,701.0 | 194,911.0 | 699,084.0 | 196,319.2 | 5 | - | 0.882 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,680,949.0 | 1,650,830.0 | 2,700,465.0 | 407,604.2 | 5 | 2,984 | 0.242 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,596,089.0 | 1,549,868.0 | 2,625,285.0 | 415,736.7 | 5 | 2,824 | 0.260 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `rust_1.13.1_default-caps-simdna` | 499,283.0 | 416,482.0 | 949,125.0 | 193,057.1 | 5 | - | 0.387 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,226,687.0 | 1,066,495.0 | 2,263,273.0 | 445,963.1 | 5 | - | 0.364 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 597,263.0 | 579,803.0 | 1,455,948.0 | 338,938.6 | 5 | 2,312 | 0.567 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 487,333.0 | 482,153.0 | 1,264,867.0 | 307,355.3 | 5 | 2,088 | 0.631 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `rust_1.13.1_default-caps-simdna` | 117,970.0 | 109,891.0 | 594,333.0 | 189,257.8 | 5 | - | 1.604 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 96,370.0 | 90,330.0 | 517,623.0 | 164,666.5 | 5 | - | 1.709 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,375,474.0 | 2,744,005.0 | 5,783,262.0 | 962,607.2 | 5 | 7,472 | 0.220 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,108,546.0 | 1,088,326.0 | 2,043,591.0 | 374,585.0 | 5 | 1,896 | 0.338 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `rust_1.13.1_default-caps-simdna` | 3,845,702.0 | 1,967,001.0 | 4,761,247.0 | 911,906.5 | 5 | - | 0.237 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,194,667.0 | 824,124.0 | 2,079,432.0 | 426,398.6 | 5 | - | 0.357 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10,733,309.0 | 10,708,090.0 | 21,727,861.0 | 4,398,708.9 | 5 | 31,592 | 0.410 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,449,130.0 | 5,409,120.0 | 14,658,071.0 | 3,604,294.5 | 5 | 19,608 | 0.661 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `rust_1.13.1_default-caps-simdna` | 258,651.0 | 230,791.0 | 719,284.0 | 185,057.9 | 5 | - | 0.715 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 107,971.0 | 92,930.0 | 553,833.0 | 176,134.1 | 5 | - | 1.631 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,691,405.0 | 2,606,195.0 | 4,338,064.0 | 653,139.7 | 5 | 9,144 | 0.243 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,770,566.0 | 2,619,674.0 | 4,688,136.0 | 775,746.7 | 5 | 4,904 | 0.280 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `rust_1.13.1_default-caps-simdna` | 345,502.0 | 160,581.0 | 724,204.0 | 204,540.7 | 5 | - | 0.592 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 97,440.0 | 80,611.0 | 611,814.0 | 202,956.0 | 5 | - | 2.083 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,880,850.0 | 1,647,169.0 | 3,149,888.0 | 558,982.8 | 5 | 11,160 | 0.297 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,967,451.0 | 1,713,530.0 | 2,827,185.0 | 401,353.7 | 5 | 4,936 | 0.204 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `rust_1.13.1_default-caps-simdna` | 3,565,259.0 | 2,662,885.0 | 5,059,788.0 | 801,264.4 | 5 | - | 0.225 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 1,323,607.0 | 1,150,727.0 | 1,977,421.0 | 303,988.2 | 5 | - | 0.230 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 35,379,417.0 | 35,320,136.0 | 40,419,805.0 | 2,013,711.7 | 5 | 99,944 | 0.057 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 38,787,676.0 | 38,723,705.0 | 49,260,374.0 | 4,195,882.4 | 5 | 89,624 | 0.108 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `rust_1.13.1_default-caps-simdna` | 67,970.0 | 66,451.0 | 530,143.0 | 180,076.2 | 5 | - | 2.649 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 77,270.0 | 68,920.0 | 516,042.0 | 171,750.4 | 5 | - | 2.223 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,274,507.0 | 1,086,816.0 | 2,437,884.0 | 484,484.6 | 5 | 6,136 | 0.380 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,267,107.0 | 1,228,437.0 | 2,260,972.0 | 394,181.8 | 5 | 3,496 | 0.311 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `rust_1.13.1_default-caps-simdna` | 76,150.0 | 64,130.0 | 503,152.0 | 168,320.1 | 5 | - | 2.210 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 72,611.0 | 65,170.0 | 531,043.0 | 179,512.8 | 5 | - | 2.472 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,930,131.0 | 1,831,280.0 | 3,408,859.0 | 598,413.7 | 5 | 4,152 | 0.310 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,517,229.0 | 1,455,568.0 | 2,610,535.0 | 446,342.6 | 5 | 4,184 | 0.294 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `balanced-parens-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `base10num-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,601.0 | 6,550.0 | 14,120.0 | 2,900.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 7,770.0 | 7,030.0 | 16,490.0 | 3,611.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,540.0 | 6,120.0 | 21,040.0 | 5,557.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 8,580.0 | 7,170.0 | 22,220.0 | 5,634.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,010.0 | 4,410.0 | 10,660.0 | 2,476.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,260.0 | 5,340.0 | 14,510.0 | 3,500.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,580.0 | 5,870.0 | 17,770.0 | 4,469.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 7,400.0 | 6,500.0 | 18,250.0 | 4,438.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,930.0 | 4,360.0 | 13,470.0 | 3,298.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,620.0 | 5,300.0 | 11,660.0 | 2,353.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,210.0 | 3,570.0 | 11,790.0 | 3,141.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,790.0 | 4,110.0 | 12,800.0 | 3,339.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,410.0 | 4,340.0 | 12,160.0 | 2,875.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,300.0 | 4,600.0 | 15,500.0 | 3,968.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,790.0 | 5,790.0 | 17,200.0 | 4,336.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 7,900.0 | 6,620.0 | 16,830.0 | 3,812.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 3,950.0 | 3,010.0 | 9,610.0 | 2,587.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,380.0 | 3,870.0 | 14,790.0 | 4,144.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,180.0 | 2,700.0 | 10,000.0 | 2,642.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,000.0 | 3,250.0 | 14,120.0 | 3,983.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,820.0 | 3,340.0 | 22,130.0 | 7,105.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 9,160.0 | 7,430.0 | 28,650.0 | 8,145.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,110.0 | 1,790.0 | 8,980.0 | 2,768.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,950.0 | 5,320.0 | 22,160.0 | 6,506.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,800.0 | 5,980.0 | 17,441.0 | 4,213.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 7,010.0 | 6,320.0 | 17,770.0 | 4,322.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 760.0 | 720.0 | 7,090.0 | 2,535.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 940.0 | 860.0 | 6,440.0 | 2,186.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,940.0 | 1,790.0 | 9,700.0 | 3,104.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,790.0 | 1,550.0 | 11,030.0 | 3,696.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 22,601.0 | 19,750.0 | 40,950.0 | 7,764.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 23,411.0 | 20,020.0 | 35,000.0 | 5,413.4 | 5 | - | 0.231 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,980.0 | 1,800.0 | 5,230.0 | 1,301.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,510.0 | 2,300.0 | 19,120.0 | 6,624.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 13,850.0 | 12,690.0 | 25,560.0 | 4,809.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,860.0 | 13,100.0 | 27,971.0 | 5,495.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,940.0 | 12,570.0 | 26,110.0 | 5,013.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,090.0 | 12,920.0 | 25,690.0 | 4,795.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,140.0 | 1,940.0 | 6,770.0 | 1,849.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,560.0 | 2,130.0 | 9,670.0 | 2,873.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,841.0 | 5,790.0 | 13,970.0 | 3,121.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 9,540.0 | 6,810.0 | 22,990.0 | 5,855.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,370.0 | 7,510.0 | 24,380.0 | 6,108.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,280.0 | 8,090.0 | 34,270.0 | 9,682.8 | 5 | - | timer-floor | compiled=5 |
| `phone-list-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,870.0 | 11,330.0 | 33,360.0 | 8,530.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 22,560.0 | 12,240.0 | 42,130.0 | 11,583.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,590.0 | 5,540.0 | 14,870.0 | 3,453.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,850.0 | 5,420.0 | 15,830.0 | 3,795.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,981.0 | 8,430.0 | 20,400.0 | 4,457.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,660.0 | 8,780.0 | 21,121.0 | 4,482.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,760.0 | 3,980.0 | 13,950.0 | 3,750.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,640.0 | 4,620.0 | 17,420.0 | 4,793.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,040.0 | 1,790.0 | 5,370.0 | 1,346.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,720.0 | 2,380.0 | 7,640.0 | 2,000.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,990.0 | 13,630.0 | 31,310.0 | 6,638.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 17,060.0 | 14,250.0 | 34,210.0 | 7,250.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,420.0 | 9,300.0 | 23,730.0 | 5,414.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,340.0 | 10,290.0 | 23,381.0 | 4,744.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,610.0 | 6,980.0 | 24,130.0 | 6,368.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,581.0 | 7,960.0 | 27,500.0 | 7,100.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,590.0 | 1,390.0 | 12,800.0 | 4,435.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,570.0 | 2,050.0 | 11,230.0 | 3,543.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,650.0 | 7,670.0 | 16,670.0 | 3,212.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,200.0 | 8,160.0 | 17,830.0 | 3,468.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 650.0 | 590.0 | 5,071.0 | 1,773.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,050.0 | 930.0 | 6,840.0 | 2,317.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,180.0 | 2,670.0 | 12,590.0 | 3,643.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 3,870.0 | 2,920.0 | 9,691.0 | 2,478.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 15,480.0 | 13,570.0 | 28,130.0 | 5,434.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 15,940.0 | 13,400.0 | 26,090.0 | 4,574.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 590.0 | 520.0 | 5,090.0 | 1,803.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 980.0 | 900.0 | 6,480.0 | 2,194.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,380.0 | 4,810.0 | 14,650.0 | 3,610.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,960.0 | 5,130.0 | 17,000.0 | 4,357.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,146,657.0 | 1,097,806.0 | 1,372,708.0 | 99,595.8 | 5 | - | 0.087 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,156,267.0 | 1,089,766.0 | 1,375,907.0 | 105,071.9 | 5 | - | 0.091 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 51,620.0 | 49,411.0 | 72,320.0 | 8,447.6 | 5 | - | 0.164 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 52,321.0 | 50,420.0 | 88,131.0 | 14,269.7 | 5 | - | 0.273 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,130.0 | 7,110.0 | 20,460.0 | 4,925.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,090.0 | 7,940.0 | 42,360.0 | 12,871.9 | 5 | - | timer-floor | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,030.0 | 5,900.0 | 19,640.0 | 5,152.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 9,300.0 | 6,960.0 | 17,070.0 | 3,638.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 17,570.0 | 14,130.0 | 35,140.0 | 7,760.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 18,140.0 | 15,170.0 | 33,881.0 | 6,937.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 15,650.0 | 12,870.0 | 32,271.0 | 7,129.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 16,150.0 | 13,570.0 | 34,260.0 | 7,686.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 347,322.0 | 329,062.0 | 433,773.0 | 37,689.3 | 5 | - | 0.109 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 358,312.0 | 331,042.0 | 436,452.0 | 36,440.0 | 5 | - | 0.102 (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,100.0 | 4,420.0 | 14,410.0 | 3,777.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,710.0 | 4,810.0 | 14,480.0 | 3,677.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,950.0 | 8,300.0 | 33,280.0 | 9,525.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,720.0 | 8,890.0 | 22,100.0 | 4,840.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,090.0 | 2,890.0 | 12,280.0 | 3,458.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,130.0 | 3,411.0 | 9,660.0 | 2,224.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 23,850.0 | 21,010.0 | 37,750.0 | 6,072.0 | 5 | - | 0.255 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 26,560.0 | 21,910.0 | 42,480.0 | 8,196.2 | 5 | - | 0.309 | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 27,310.0 | 23,440.0 | 43,711.0 | 7,307.5 | 5 | - | 0.268 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 29,010.0 | 25,781.0 | 43,090.0 | 6,209.2 | 5 | - | 0.214 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,910.0 | 1,640.0 | 9,000.0 | 2,860.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,520.0 | 2,190.0 | 10,060.0 | 3,017.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,230.0 | 1,060.0 | 7,711.0 | 2,599.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,330.0 | 1,140.0 | 8,170.0 | 2,732.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,210.0 | 3,390.0 | 17,440.0 | 5,300.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,220.0 | 3,170.0 | 10,850.0 | 2,815.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,520.0 | 7,670.0 | 23,260.0 | 5,665.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,820.0 | 8,300.0 | 23,571.0 | 5,607.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 31,990.0 | 23,850.0 | 43,391.0 | 7,457.3 | 5 | - | 0.233 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 25,560.0 | 25,050.0 | 46,251.0 | 8,127.3 | 5 | - | 0.318 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,400.0 | 3,920.0 | 15,910.0 | 4,461.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,550.0 | 4,960.0 | 11,470.0 | 2,607.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,460.0 | 3,720.0 | 10,950.0 | 2,634.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,800.0 | 4,210.0 | 12,680.0 | 3,241.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 127,301.0 | 116,311.0 | 162,191.0 | 17,088.2 | 5 | - | 0.134 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 124,641.0 | 117,591.0 | 171,191.0 | 19,676.3 | 5 | - | 0.158 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 15,860.0 | 13,690.0 | 29,600.0 | 5,866.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 17,250.0 | 14,700.0 | 31,251.0 | 6,151.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,400.0 | 8,060.0 | 15,850.0 | 2,830.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,271.0 | 8,590.0 | 19,670.0 | 4,079.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 552,533.0 | 520,792.0 | 687,564.0 | 59,732.0 | 5 | - | 0.108 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 543,523.0 | 509,322.0 | 690,034.0 | 64,481.5 | 5 | - | 0.119 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,520.0 | 6,670.0 | 17,410.0 | 3,873.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 20,350.0 | 15,890.0 | 55,650.0 | 14,889.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,120.0 | 4,250.0 | 10,400.0 | 2,449.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,710.0 | 4,710.0 | 12,000.0 | 2,847.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |

