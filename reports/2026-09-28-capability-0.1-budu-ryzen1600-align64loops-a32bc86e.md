# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, machine=budu-ryzen1600, testee=pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64, testee=pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 38.1% (`pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-datetime-moment-iso8601` / `large-subject-throughput`)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64__budu-ryzen1600__20260928T101609Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64/capability@0.1__pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64__budu-ryzen1600__20260928T101609Z.jsonl) — agreement: agree (0 of 72 groups; 0 of 2806 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64__budu-ryzen1600__20260928T103722Z` (store/records/capability@0.1/pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64/capability@0.1__pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64__budu-ryzen1600__20260928T103722Z.jsonl) — agreement: agree (0 of 72 groups; 0 of 2806 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
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

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 17.8 | 0.0000 | 17.8 | 18.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 17.8 | 0.0000 | 17.8 | 17.9 | 0.0 | 1.000x | 1.000x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 6.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.9 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.9 | 0.0001 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 515.9 | 514.6 | 530.0 | 6.0 | 1.000x | 1.000x | 75 | 6.9 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 528.0 | 511.2 | 530.2 | 7.1 | 1.023x | 1.023x | 75 | 7.0 | 8.8 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 605,440.7 | 0.4399 | 594,999.2 | 617,175.7 | 7,904.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 617,461.5 | 0.4487 | 605,348.4 | 623,333.4 | 7,477.2 | 1.020x | 1.020x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 464,981.1 | 0.4434 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 467,640.9 | 0.4460 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 113,332.6 | 0.4323 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 117,476.2 | 0.4481 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 28,287.9 | 0.4316 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 28,224.8 | 0.4307 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 891.8 | 890.9 | 902.4 | 4.3 | 1.000x | 1.000x | 75 | 11.9 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 892.8 | 891.9 | 901.0 | 3.4 | 1.001x | 1.001x | 75 | 11.9 | 8.8 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 29.6 | 0.0000 | 29.3 | 31.6 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 30.3 | 0.0000 | 29.4 | 31.7 | 0.8 | 1.022x | 1.022x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9.8 | 0.0001 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 801.0 | 800.3 | 801.9 | 0.5 | 1.000x | 1.000x | 75 | 10.7 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 801.9 | 800.9 | 803.9 | 1.0 | 1.001x | 1.001x | 75 | 10.7 | 8.8 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 48.7 | 0.0000 | 46.9 | 50.7 | 1.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 50.6 | 0.0000 | 48.3 | 51.6 | 1.4 | 1.039x | 1.039x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 17.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 18.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15.5 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15.5 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15.8 | 0.0002 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,360.8 | 1,355.7 | 1,387.2 | 11.5 | 1.000x | 1.000x | 75 | 18.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,365.3 | 1,363.9 | 1,370.7 | 2.3 | 1.003x | 1.003x | 75 | 18.2 | 8.8 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 11,871.8 | 0.0086 | 11,785.1 | 12,284.2 | 203.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 12,197.5 | 0.0089 | 11,796.6 | 12,223.0 | 177.3 | 1.027x | 1.027x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,214.4 | 0.0012 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,268.7 | 0.0012 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 46.5 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 45.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10,610.9 | 0.1619 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10,876.9 | 0.1660 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 255,601.5 | 0.1857 | 255,391.7 | 255,770.9 | 125.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 255,804.8 | 0.1859 | 255,481.3 | 256,021.8 | 199.0 | 1.001x | 1.001x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 203,025.0 | 0.1936 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 203,024.3 | 0.1936 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 43,978.3 | 0.1678 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 44,115.8 | 0.1683 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 8,642.4 | 0.1319 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 8,630.2 | 0.1317 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 693.6 | 693.1 | 694.0 | 0.4 | 1.000x | 1.000x | 75 | 9.2 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 695.1 | 694.2 | 699.2 | 1.7 | 1.002x | 1.002x | 75 | 9.3 | 8.8 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,135.3 | 0.0168 | 23,120.3 | 23,157.1 | 12.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,156.4 | 0.0168 | 23,129.7 | 23,206.8 | 25.2 | 1.001x | 1.001x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 17,634.9 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 17,649.2 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 4,383.9 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 4,400.3 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,107.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,106.9 | 0.0169 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 663.5 | 662.2 | 667.3 | 1.9 | 1.000x | 1.000x | 75 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 663.7 | 661.8 | 671.2 | 3.3 | 1.000x | 1.000x | 75 | 8.8 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 15.6 | 0.0000 | 15.4 | 16.9 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 15.8 | 0.0000 | 15.7 | 16.0 | 0.1 | 1.011x | 1.011x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.2 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.4 | 0.0001 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 437.2 | 436.8 | 438.9 | 0.8 | 1.000x | 1.000x | 75 | 5.8 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 438.2 | 437.8 | 440.4 | 0.9 | 1.002x | 1.002x | 75 | 5.8 | 8.8 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 686,705.4 | 0.4990 | 686,564.5 | 688,079.4 | 566.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 687,172.0 | 0.4993 | 686,783.2 | 687,723.1 | 340.1 | 1.001x | 1.001x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 530,832.5 | 0.5062 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 531,197.3 | 0.5066 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 126,817.0 | 0.4838 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 126,824.9 | 0.4838 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 29,042.7 | 0.4432 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 29,069.2 | 0.4436 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 792.6 | 788.7 | 793.7 | 1.7 | 1.000x | 1.000x | 75 | 10.6 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 793.4 | 791.1 | 794.0 | 1.0 | 1.001x | 1.001x | 75 | 10.6 | 8.8 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 32.1 | 0.0000 | 32.0 | 32.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 33.0 | 0.0000 | 32.9 | 33.0 | 0.0 | 1.029x | 1.029x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 11.3 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 11.6 | 0.0002 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 795.1 | 794.7 | 796.1 | 0.5 | 1.000x | 1.000x | 75 | 10.6 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 822.2 | 821.7 | 826.1 | 1.7 | 1.034x | 1.034x | 75 | 11.0 | 8.8 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 30.7 | 0.0000 | 30.3 | 31.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 30.9 | 0.0000 | 30.7 | 30.9 | 0.0 | 1.004x | 1.004x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.2 | 0.0002 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 834.0 | 830.1 | 846.3 | 6.9 | 1.000x | 1.000x | 75 | 11.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 845.0 | 837.3 | 854.4 | 6.2 | 1.013x | 1.013x | 75 | 11.3 | 8.8 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 32.2 | 0.0000 | 32.2 | 32.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 32.4 | 0.0000 | 32.3 | 32.6 | 0.1 | 1.005x | 1.005x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.8 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.8 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.9 | 0.0002 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 918.7 | 915.3 | 932.1 | 5.8 | 1.000x | 1.000x | 75 | 12.2 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 926.0 | 915.9 | 932.3 | 6.0 | 1.008x | 1.008x | 75 | 12.3 | 8.8 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 340,305.9 | 0.2473 | 340,149.8 | 340,554.9 | 144.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 340,455.8 | 0.2474 | 340,229.7 | 340,475.0 | 106.0 | 1.000x | 1.000x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 261,785.6 | 0.2497 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 261,635.5 | 0.2495 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 64,167.2 | 0.2448 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 64,182.4 | 0.2448 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 14,450.3 | 0.2205 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 14,577.9 | 0.2224 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 708.5 | 708.2 | 709.2 | 0.4 | 1.000x | 1.000x | 75 | 9.4 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 710.2 | 708.6 | 829.6 | 48.0 | 1.002x | 1.002x | 75 | 9.5 | 8.8 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 47.1 | 0.0000 | 46.9 | 47.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 47.2 | 0.0000 | 47.1 | 47.5 | 0.1 | 1.001x | 1.001x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15.7 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15.8 | 0.0002 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 10,117,323.2 | 10,110,352.1 | 10,119,605.8 | 3,243.3 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 134,897.6 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 10,121,077.5 | 10,117,825.6 | 10,126,413.6 | 2,930.5 | 1.000x | 1.000x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 134,947.7 | 8.8 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 16.0 | 0.0000 | 16.0 | 18.7 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 16.0 | 0.0000 | 16.0 | 16.1 | 0.0 | 1.001x | 1.001x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5.4 | 0.0001 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 535.4 | 532.9 | 540.2 | 2.8 | 1.000x | 1.000x | 75 | 7.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 536.9 | 535.0 | 537.9 | 1.1 | 1.003x | 1.003x | 75 | 7.2 | 8.8 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 219,093.1 | 0.1592 | 218,850.1 | 220,235.2 | 495.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 219,132.8 | 0.1592 | 218,915.7 | 219,519.5 | 196.6 | 1.000x | 1.000x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 168,281.1 | 0.1605 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 168,458.9 | 0.1607 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 40,505.6 | 0.1545 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 40,323.3 | 0.1538 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10,282.6 | 0.1569 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10,324.0 | 0.1575 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 690.6 | 681.5 | 704.6 | 8.5 | 1.000x | 1.000x | 75 | 9.2 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 695.2 | 685.5 | 706.3 | 6.8 | 1.007x | 1.007x | 75 | 9.3 | 8.8 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 4,194,807.0 | 3.0480 | 4,194,451.3 | 4,199,184.0 | 1,828.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 4,194,954.4 | 3.0481 | 4,194,408.1 | 4,200,605.7 | 2,286.4 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 3,196,281.3 | 3.0482 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 3,197,724.8 | 3.0496 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 800,049.8 | 3.0519 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 799,352.2 | 3.0493 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 198,810.9 | 3.0336 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 198,010.9 | 3.0214 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,447.6 | 2,437.3 | 2,452.9 | 5.4 | 1.000x | 1.000x | 75 | 32.6 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,452.1 | 2,448.2 | 2,455.8 | 2.6 | 1.002x | 1.002x | 75 | 32.7 | 8.8 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,100.0 | 0.0168 | 23,094.8 | 23,134.1 | 14.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,116.8 | 0.0168 | 23,108.0 | 23,250.3 | 53.8 | 1.001x | 1.001x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 17,610.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 17,629.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 4,380.1 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 4,380.2 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,109.1 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,108.3 | 0.0169 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 683.6 | 671.4 | 686.1 | 5.3 | 1.000x | 1.000x | 75 | 9.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 684.8 | 675.3 | 699.0 | 8.8 | 1.002x | 1.002x | 75 | 9.1 | 8.8 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 38.0 | 0.0000 | 37.5 | 38.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 38.1 | 0.0000 | 37.9 | 38.2 | 0.1 | 1.002x | 1.002x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 12.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 12.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 12.7 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 12.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 12.7 | 0.0002 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,026.8 | 1,025.9 | 1,032.6 | 2.5 | 1.000x | 1.000x | 75 | 13.7 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,028.1 | 1,025.0 | 1,030.4 | 1.9 | 1.001x | 1.001x | 75 | 13.7 | 8.8 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 3,937,452.0 | 2.8610 | 3,934,727.6 | 3,939,435.7 | 1,602.8 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 3,994,295.9 | 2.9023 | 3,990,364.0 | 3,997,071.7 | 2,152.7 | 1.014x | 1.014x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 2,999,081.8 | 2.8601 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 3,042,978.7 | 2.9020 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 750,279.5 | 2.8621 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 761,629.6 | 2.9054 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 187,787.2 | 2.8654 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 189,445.1 | 2.8907 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,148.4 | 1,146.9 | 1,151.9 | 1.7 | 1.000x | 1.000x | 75 | 15.3 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,158.6 | 1,153.2 | 1,162.3 | 3.0 | 1.009x | 1.009x | 75 | 15.4 | 8.8 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 125,302.8 | 0.0910 | 125,172.9 | 125,440.0 | 89.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 125,389.3 | 0.0911 | 125,303.6 | 125,624.8 | 111.5 | 1.001x | 1.001x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 102,872.5 | 0.0981 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 102,838.0 | 0.0981 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 18,917.3 | 0.0722 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 19,057.5 | 0.0727 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 3,467.0 | 0.0529 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 3,542.3 | 0.0541 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,578.3 | 1,571.0 | 1,586.7 | 5.0 | 1.000x | 1.000x | 75 | 21.0 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,598.8 | 1,595.7 | 1,602.8 | 2.7 | 1.013x | 1.013x | 75 | 21.3 | 8.8 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 354,924.0 | 0.2579 | 354,686.2 | 383,140.5 | 11,317.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 357,734.6 | 0.2599 | 357,657.2 | 357,998.6 | 128.4 | 1.008x | 1.008x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 272,476.3 | 0.2599 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 274,761.6 | 0.2620 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 67,191.0 | 0.2563 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 67,557.1 | 0.2577 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 15,250.3 | 0.2327 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 15,471.3 | 0.2361 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,306.8 | 1,297.2 | 1,313.1 | 5.9 | 1.000x | 1.000x | 75 | 17.4 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,307.3 | 1,299.6 | 1,311.7 | 4.2 | 1.000x | 1.000x | 75 | 17.4 | 8.8 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,136.6 | 0.0168 | 23,127.9 | 23,157.0 | 9.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,160.3 | 0.0168 | 23,111.5 | 23,195.2 | 32.6 | 1.001x | 1.001x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 17,652.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 17,630.3 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 4,377.6 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 4,402.8 | 0.0168 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,109.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,109.0 | 0.0169 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,049.6 | 1,048.2 | 1,055.2 | 2.5 | 1.000x | 1.000x | 75 | 14.0 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,067.8 | 1,062.8 | 1,069.1 | 2.4 | 1.017x | 1.017x | 75 | 14.2 | 8.8 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 352,078.2 | 0.2558 | 351,662.9 | 352,788.8 | 376.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 352,201.4 | 0.2559 | 351,517.7 | 353,190.9 | 570.4 | 1.000x | 1.000x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 282,884.6 | 0.2698 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 282,840.0 | 0.2697 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 58,189.0 | 0.2220 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 58,325.7 | 0.2225 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 11,079.8 | 0.1691 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 11,023.2 | 0.1682 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 684.1 | 681.7 | 686.4 | 1.6 | 1.000x | 1.000x | 75 | 9.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 684.7 | 680.3 | 687.9 | 2.8 | 1.001x | 1.001x | 75 | 9.1 | 8.8 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 41.8 | 0.0000 | 41.7 | 45.0 | 1.3 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 42.1 | 0.0000 | 41.7 | 45.3 | 1.3 | 1.008x | 1.008x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 13.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 13.9 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 13.9 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 13.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 14.0 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 14.3 | 0.0002 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 959.3 | 958.4 | 963.8 | 2.1 | 1.000x | 1.000x | 75 | 12.8 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 962.1 | 958.9 | 962.7 | 1.4 | 1.003x | 1.003x | 75 | 12.8 | 8.8 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 6,981,572.9 | 5.0729 | 6,968,598.3 | 7,018,408.5 | 17,227.6 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 7,006,321.1 | 5.0909 | 6,979,550.2 | 7,025,559.1 | 16,137.3 | 1.004x | 1.004x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 5,362,230.0 | 5.1138 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 5,383,119.5 | 5.1337 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,308,545.8 | 4.9917 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,313,739.4 | 5.0115 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 314,559.9 | 4.7998 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 317,194.8 | 4.8400 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,921.5 | 2,907.3 | 2,962.2 | 18.9 | 1.000x | 1.000x | 75 | 39.0 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,929.2 | 2,906.1 | 2,937.2 | 11.3 | 1.003x | 1.003x | 75 | 39.1 | 8.8 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 38.0 | 0.0000 | 36.6 | 39.1 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 38.0 | 0.0000 | 35.6 | 41.7 | 2.0 | 1.001x | 1.001x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 14.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 14.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 12.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 12.0 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 12.1 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 11.8 | 0.0002 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 986.6 | 980.3 | 989.2 | 3.5 | 1.000x | 1.000x | 75 | 13.2 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 989.1 | 988.1 | 994.1 | 2.2 | 1.003x | 1.003x | 75 | 13.2 | 8.8 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 27.8 | 0.0000 | 27.7 | 28.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 27.9 | 0.0000 | 27.8 | 28.0 | 0.1 | 1.002x | 1.002x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9.3 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9.3 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9.3 | 0.0001 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 816.3 | 815.7 | 817.6 | 0.8 | 1.000x | 1.000x | 75 | 10.9 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 816.9 | 816.0 | 828.8 | 4.9 | 1.001x | 1.001x | 75 | 10.9 | 8.8 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 31.8 | 0.0000 | 30.3 | 32.0 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 31.9 | 0.0000 | 31.8 | 32.0 | 0.1 | 1.003x | 1.003x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.6 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 10.7 | 0.0002 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 785.0 | 783.6 | 785.5 | 0.7 | 1.000x | 1.000x | 75 | 10.5 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 786.4 | 783.7 | 793.8 | 4.0 | 1.002x | 1.002x | 75 | 10.5 | 8.8 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 82,121.6 | 0.0597 | 82,024.1 | 82,255.5 | 88.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 82,787.1 | 0.0602 | 82,136.8 | 82,920.4 | 280.1 | 1.008x | 1.008x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 68,242.5 | 0.0651 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 68,756.2 | 0.0656 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 11,462.9 | 0.0437 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 11,587.8 | 0.0442 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 2,420.4 | 0.0369 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 2,466.8 | 0.0376 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 747.1 | 742.3 | 755.9 | 5.1 | 1.000x | 1.000x | 75 | 10.0 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 750.5 | 746.2 | 754.9 | 3.0 | 1.004x | 1.004x | 75 | 10.0 | 8.8 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 4,081,389.2 | 2.9656 | 4,077,098.2 | 4,082,420.5 | 2,037.1 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 4,081,732.8 | 2.9658 | 4,079,683.3 | 4,081,949.5 | 900.4 | 1.000x | 1.000x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 3,114,334.0 | 2.9701 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 3,113,885.8 | 2.9696 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 775,773.9 | 2.9593 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 775,957.8 | 2.9600 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 191,537.7 | 2.9226 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 191,439.4 | 2.9211 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,693.5 | 2,687.3 | 2,696.7 | 3.6 | 1.000x | 1.000x | 75 | 35.9 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 2,695.4 | 2,690.1 | 2,698.1 | 3.2 | 1.001x | 1.001x | 75 | 35.9 | 8.8 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,328,222.1 | 0.9651 | 1,320,444.3 | 1,338,123.4 | 6,506.9 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,339,654.4 | 0.9734 | 1,328,042.6 | 1,345,143.2 | 5,895.8 | 1.009x | 1.009x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,007,790.3 | 0.9611 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,009,155.0 | 0.9624 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 251,508.1 | 0.9594 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 258,822.1 | 0.9873 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 66,371.7 | 1.0128 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 67,906.4 | 1.0362 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 705.4 | 703.4 | 723.2 | 7.2 | 1.000x | 1.000x | 75 | 9.4 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 706.6 | 701.5 | 708.5 | 2.3 | 1.002x | 1.002x | 75 | 9.4 | 8.8 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,001,409.7 | 0.7276 | 993,409.7 | 1,020,310.0 | 9,073.2 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,001,641.9 | 0.7278 | 996,138.7 | 1,008,672.7 | 4,350.4 | 1.000x | 1.000x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 758,573.6 | 0.7234 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 757,658.7 | 0.7226 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 193,341.4 | 0.7375 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 193,800.2 | 0.7393 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 48,526.4 | 0.7405 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 49,074.1 | 0.7488 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,151.5 | 1,150.4 | 1,153.6 | 1.1 | 1.000x | 1.000x | 75 | 15.4 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 1,152.7 | 1,146.8 | 1,165.4 | 6.2 | 1.001x | 1.001x | 75 | 15.4 | 8.8 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 12,003,362.2 | 8.7218 | 11,817,233.2 | 12,121,664.4 | 119,154.5 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 12,105,026.5 | 8.7956 | 11,813,547.8 | 12,110,112.9 | 143,325.3 | 1.008x | 1.008x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 9,149,356.8 | 8.7255 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 9,227,686.3 | 8.8002 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 2,283,237.0 | 8.7099 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 2,299,714.7 | 8.7727 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 570,768.3 | 8.7092 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 575,111.3 | 8.7755 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 7,734.0 | 7,727.4 | 7,808.4 | 36.0 | 1.000x | 1.000x | 75 | 103.1 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 7,735.7 | 7,726.6 | 7,775.1 | 19.4 | 1.000x | 1.000x | 75 | 103.1 | 8.8 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,114.4 | 0.0168 | 23,102.0 | 23,166.9 | 23.4 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 23,117.6 | 0.0168 | 23,114.0 | 23,132.8 | 6.7 | 1.000x | 1.000x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 17,629.7 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 17,632.6 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 4,379.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 4,376.5 | 0.0167 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,106.5 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,109.3 | 0.0169 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 710.7 | 710.3 | 713.6 | 1.3 | 1.000x | 1.000x | 75 | 9.5 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 712.9 | 709.7 | 720.9 | 4.1 | 1.003x | 1.003x | 75 | 9.5 | 8.8 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 21.3 | 0.0000 | 21.3 | 21.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 21.4 | 0.0000 | 21.4 | 21.5 | 0.0 | 1.003x | 1.003x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 7.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 7.2 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 7.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 7.1 | 0.0000 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 7.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 7.1 | 0.0001 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64 (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 510.1 | 509.9 | 510.8 | 0.3 | 1.000x | 1.000x | 75 | 6.8 | 8.8 | 100% |
| 2 | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | measured | `plain` | same program | 510.3 | 506.6 | 510.5 | 1.8 | 1.000x | 1.000x | 75 | 6.8 | 8.8 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 75 | 97% | -2:PCREC_ERR_STEPS×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,277 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 9,382 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-datetime-datefinder-alternation` / `whole-subject`: engine=vm, sel=overflowed-prefilter (DFA fallback tripped), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 508,522 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=49/74 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 5,475 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 5,580 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,770 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 1,873 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,326 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,431 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,307 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 16,412 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2,3,4, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,3,4,5,6*,7,8,9,10, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,5,6*,7, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned table=premultiplied offsets=0*,1,2, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0*,1,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=run-pinned-bounded table=premultiplied offsets=0,1*,2, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
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
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `balanced-parens-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 147,637,025.0 | 143,240,676.0 | 154,326,022.0 | 3,975,719.0 | 5 | 31,832 | 16,705 | 14,320 | 0.027 | compiled=5 | 1,561,546.0 | 146,156,728.0 | 106,410.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 142,132,161.0 | 137,974,816.0 | 150,428,226.0 | 4,411,353.1 | 5 | 31,752 | 16,158 | 13,773 | 0.031 | compiled=5 | 1,535,666.0 | 140,378,115.0 | 192,631.0 |
| `base10num-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 151,784,751.0 | 145,412,491.0 | 152,867,145.0 | 2,963,721.7 | 5 | 31,832 | 16,705 | 14,320 | 0.020 | compiled=5 | 1,522,517.0 | 150,326,564.0 | 101,330.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 137,407,306.0 | 136,153,299.0 | 149,102,688.0 | 5,708,610.8 | 5 | 31,752 | 16,158 | 13,773 | 0.042 | compiled=5 | 1,591,687.0 | 134,542,492.0 | 98,510.0 |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `bracket-array-define` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 348,217,030.0 | 336,371,494.0 | 353,540,242.0 | 5,949,879.0 | 5 | 36,168 | 35,699 | 27,100 | 0.017 | compiled=5 | 2,088,328.0 | 346,027,172.0 | 99,481.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 358,414,002.0 | 341,900,525.0 | 364,484,296.0 | 7,702,597.5 | 5 | 36,216 | 35,420 | 27,908 | 0.021 (max is trial 1) | compiled=5 | 2,145,939.0 | 356,170,093.0 | 207,571.0 |
| `codegrammar-flat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 351,083,577.0 | 343,562,274.0 | 355,448,577.0 | 3,903,345.1 | 5 | 36,168 | 35,699 | 27,100 | 0.011 | compiled=5 | 2,120,790.0 | 348,784,417.0 | 112,781.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 358,282,691.0 | 355,022,525.0 | 359,399,936.0 | 1,618,572.5 | 5 | 36,216 | 35,420 | 27,908 | 0.005 | compiled=5 | 2,058,390.0 | 356,089,050.0 | 97,700.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `codegrammar-xflag` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 259,538,735.0 | 252,181,405.0 | 259,747,627.0 | 3,069,779.9 | 5 | 36,048 | 33,849 | 31,823 | 0.012 | compiled=5 | 1,790,618.0 | 257,531,116.0 | 204,951.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 258,129,088.0 | 243,936,862.0 | 260,582,418.0 | 6,734,583.4 | 5 | 36,048 | 33,777 | 31,751 | 0.026 (max is trial 1) | compiled=5 | 1,814,467.0 | 256,211,521.0 | 199,531.0 |
| `date-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 260,490,015.0 | 244,584,254.0 | 261,640,331.0 | 6,686,562.6 | 5 | 36,048 | 33,849 | 31,823 | 0.026 | compiled=5 | 1,814,148.0 | 258,566,967.0 | 188,471.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 248,357,941.0 | 242,801,545.0 | 259,103,249.0 | 5,371,328.0 | 5 | 36,048 | 33,777 | 31,751 | 0.022 | compiled=5 | 1,790,908.0 | 246,377,722.0 | 99,050.0 |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `doubled-word` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `dup-param-detect` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `email-local-nodup` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 219,693,814.0 | 216,038,239.0 | 231,137,739.0 | 6,376,368.9 | 5 | 36,008 | 29,236 | 27,290 | 0.029 | compiled=5 | 1,948,018.0 | 216,045,490.0 | 190,291.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 224,118,952.0 | 218,234,828.0 | 227,692,455.0 | 3,046,589.1 | 5 | 36,008 | 29,667 | 27,637 | 0.014 | compiled=5 | 1,727,026.0 | 222,302,874.0 | 109,201.0 |
| `email-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 223,313,696.0 | 218,055,883.0 | 224,791,014.0 | 2,339,375.1 | 5 | 36,008 | 29,236 | 27,290 | 0.010 | compiled=5 | 1,712,308.0 | 221,506,668.0 | 100,170.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 221,739,911.0 | 216,934,358.0 | 225,366,766.0 | 3,198,411.7 | 5 | 36,008 | 29,667 | 27,637 | 0.014 | compiled=5 | 1,782,749.0 | 219,882,101.0 | 104,890.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 215,789,590.0 | 207,447,294.0 | 216,161,320.0 | 3,368,510.4 | 5 | 35,824 | 25,768 | 25,768 | 0.016 | compiled=5 | 1,615,236.0 | 214,084,721.0 | 105,741.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 210,263,076.0 | 208,468,568.0 | 215,625,047.0 | 2,524,880.6 | 5 | 35,824 | 25,881 | 25,881 | 0.012 | compiled=5 | 1,644,357.0 | 207,500,855.0 | 102,221.0 |
| `evil-alt-nested` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 216,117,834.0 | 206,856,782.0 | 222,642,543.0 | 5,269,547.3 | 5 | 35,824 | 25,768 | 25,768 | 0.024 | compiled=5 | 1,585,107.0 | 214,301,586.0 | 193,121.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 215,581,791.0 | 210,925,319.0 | 219,928,791.0 | 3,394,515.4 | 5 | 35,824 | 25,881 | 25,881 | 0.016 | compiled=5 | 1,607,047.0 | 213,870,423.0 | 103,501.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 155,696,238.0 | 151,797,712.0 | 161,971,572.0 | 3,996,263.2 | 5 | 31,968 | 21,280 | 15,157 | 0.026 | compiled=5 | 1,920,588.0 | 153,479,108.0 | 116,231.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 165,683,047.0 | 161,076,318.0 | 168,191,987.0 | 2,602,483.6 | 5 | 32,112 | 24,424 | 17,358 | 0.016 | compiled=5 | 1,980,178.0 | 161,277,229.0 | 100,560.0 |
| `file-ext-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 149,721,252.0 | 147,956,093.0 | 160,220,850.0 | 5,518,314.8 | 5 | 31,968 | 21,280 | 15,157 | 0.037 | compiled=5 | 1,924,669.0 | 147,152,180.0 | 190,461.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 168,075,625.0 | 162,068,117.0 | 172,196,614.0 | 3,678,790.9 | 5 | 32,112 | 24,424 | 17,358 | 0.022 | compiled=5 | 1,978,649.0 | 165,904,975.0 | 188,640.0 |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `float-literal-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 145,513,825.0 | 145,273,075.0 | 157,985,326.0 | 4,905,112.2 | 5 | 31,968 | 19,793 | 14,796 | 0.034 | compiled=5 | 1,716,697.0 | 143,721,548.0 | 99,641.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 155,947,447.0 | 151,627,429.0 | 171,993,633.0 | 7,906,953.9 | 5 | 32,112 | 22,248 | 16,925 | 0.051 | compiled=5 | 1,757,437.0 | 152,339,793.0 | 172,410.0 |
| `floor-byte` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 146,905,409.0 | 134,449,092.0 | 158,829,383.0 | 7,867,713.9 | 5 | 31,968 | 19,793 | 14,796 | 0.054 | compiled=5 | 1,731,948.0 | 144,682,129.0 | 188,481.0 |
| `floor-byte` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 155,186,257.0 | 149,123,869.0 | 156,470,493.0 | 2,777,075.0 | 5 | 32,112 | 22,248 | 16,925 | 0.018 | compiled=5 | 2,001,030.0 | 153,330,358.0 | 169,121.0 |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `high-byte-run` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 164,062,750.0 | 161,386,890.0 | 176,448,409.0 | 5,389,282.7 | 5 | 36,784 | 23,670 | 18,354 | 0.033 | compiled=5 | 2,022,538.0 | 161,259,729.0 | 114,931.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 156,634,560.0 | 154,548,382.0 | 167,928,586.0 | 5,346,846.2 | 5 | 36,576 | 22,748 | 17,432 | 0.034 | compiled=5 | 1,734,157.0 | 154,703,252.0 | 104,540.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 171,724,622.0 | 169,481,682.0 | 173,391,729.0 | 1,408,523.6 | 5 | 36,784 | 23,670 | 18,354 | 0.008 | compiled=5 | 1,750,488.0 | 169,872,334.0 | 105,721.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 166,167,066.0 | 163,244,813.0 | 168,660,678.0 | 1,968,414.4 | 5 | 36,576 | 22,748 | 17,432 | 0.012 | compiled=5 | 1,843,319.0 | 164,221,847.0 | 191,031.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 158,021,086.0 | 148,193,187.0 | 160,911,086.0 | 4,356,628.6 | 5 | 31,968 | 21,758 | 15,144 | 0.028 | compiled=5 | 1,875,457.0 | 156,010,138.0 | 190,841.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 162,068,952.0 | 160,618,315.0 | 170,395,935.0 | 4,335,162.5 | 5 | 32,112 | 26,179 | 17,353 | 0.027 | compiled=5 | 2,035,738.0 | 159,604,623.0 | 99,890.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 149,502,920.0 | 139,731,956.0 | 163,025,002.0 | 8,387,864.9 | 5 | 31,968 | 21,758 | 15,144 | 0.056 | compiled=5 | 3,661,157.0 | 147,386,261.0 | 105,540.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 170,396,807.0 | 169,327,671.0 | 177,915,540.0 | 3,177,632.9 | 5 | 32,112 | 26,179 | 17,353 | 0.019 | compiled=5 | 2,059,759.0 | 167,571,733.0 | 171,061.0 |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `logparse-atomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 279,526,455.0 | 278,928,372.0 | 284,304,535.0 | 1,981,777.8 | 5 | 83,104 | 57,232 | 37,299 | 0.007 (max is trial 1) | compiled=5 | 2,456,160.0 | 276,813,154.0 | 227,091.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 283,546,281.0 | 278,547,671.0 | 293,414,570.0 | 5,334,725.5 | 5 | 83,064 | 57,159 | 37,226 | 0.019 | compiled=5 | 5,263,292.0 | 280,754,670.0 | 130,641.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 315,400,186.0 | 310,011,160.0 | 317,919,896.0 | 2,633,783.7 | 5 | 87,200 | 63,692 | 43,759 | 0.008 | compiled=5 | 2,601,582.0 | 312,681,923.0 | 115,841.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 318,441,120.0 | 314,796,673.0 | 319,888,006.0 | 1,743,294.5 | 5 | 87,160 | 63,619 | 43,686 | 0.005 | compiled=5 | 2,589,851.0 | 315,602,326.0 | 134,301.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `mojibake-curly-quote` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 218,249,268.0 | 213,079,408.0 | 228,953,111.0 | 5,526,598.0 | 5 | 35,928 | 28,898 | 27,216 | 0.025 | compiled=5 | 1,737,547.0 | 216,413,290.0 | 100,501.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 216,760,093.0 | 210,280,736.0 | 222,673,746.0 | 3,930,123.4 | 5 | 35,928 | 28,827 | 27,145 | 0.018 (max is trial 1) | compiled=5 | 1,705,787.0 | 214,896,515.0 | 189,391.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 218,202,623.0 | 212,713,598.0 | 220,053,212.0 | 2,892,694.3 | 5 | 35,928 | 28,898 | 27,216 | 0.013 | compiled=5 | 1,711,278.0 | 216,402,575.0 | 104,811.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 216,711,477.0 | 203,745,808.0 | 218,269,424.0 | 5,584,782.5 | 5 | 35,928 | 28,827 | 27,145 | 0.026 | compiled=5 | 1,694,357.0 | 214,820,098.0 | 191,911.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 224,451,092.0 | 223,782,801.0 | 231,054,249.0 | 2,701,001.6 | 5 | 36,008 | 30,126 | 28,184 | 0.012 | compiled=5 | 1,775,047.0 | 222,300,645.0 | 194,381.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 230,234,506.0 | 226,528,772.0 | 231,818,063.0 | 1,847,406.7 | 5 | 35,968 | 30,054 | 28,112 | 0.008 | compiled=5 | 1,771,048.0 | 228,315,029.0 | 107,611.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 230,297,938.0 | 218,996,287.0 | 236,563,266.0 | 5,962,672.9 | 5 | 36,008 | 30,126 | 28,184 | 0.026 | compiled=5 | 1,787,348.0 | 228,432,180.0 | 103,041.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 230,708,591.0 | 226,749,623.0 | 231,030,421.0 | 1,601,760.9 | 5 | 35,968 | 30,054 | 28,112 | 0.007 | compiled=5 | 1,821,059.0 | 228,774,531.0 | 105,301.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `phone-palindrome-6` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `pwd-strength-chain` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `quoted-delim-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 157,047,531.0 | 142,154,322.0 | 165,331,415.0 | 8,119,113.9 | 5 | 31,968 | 21,136 | 15,156 | 0.052 | compiled=5 | 1,901,697.0 | 154,944,293.0 | 134,180.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 168,132,946.0 | 164,098,131.0 | 172,840,496.0 | 2,845,927.5 | 5 | 32,112 | 23,964 | 17,357 | 0.017 | compiled=5 | 2,002,078.0 | 166,060,118.0 | 99,140.0 |
| `router-prefix-order` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 159,031,724.0 | 141,609,684.0 | 160,939,282.0 | 7,150,610.7 | 5 | 31,968 | 21,136 | 15,156 | 0.045 | compiled=5 | 1,912,149.0 | 157,017,955.0 | 117,550.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 169,998,293.0 | 154,051,551.0 | 172,573,147.0 | 6,899,162.2 | 5 | 32,112 | 23,964 | 17,357 | 0.041 | compiled=5 | 1,979,449.0 | 167,921,604.0 | 106,811.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `tag-depth3-bound` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `tag-pair-match` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 202,290,334.0 | 198,308,138.0 | 208,520,930.0 | 3,677,991.1 | 5 | 31,696 | 24,001 | 23,770 | 0.018 | compiled=5 | 1,578,476.0 | 200,351,576.0 | 103,981.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 204,906,245.0 | 189,265,743.0 | 206,161,100.0 | 6,398,318.7 | 5 | 35,792 | 24,115 | 23,884 | 0.031 | compiled=5 | 1,568,316.0 | 203,178,717.0 | 182,101.0 |
| `trim-nested-star` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 205,946,357.0 | 199,685,349.0 | 213,686,353.0 | 4,453,320.7 | 5 | 31,696 | 24,001 | 23,770 | 0.022 | compiled=5 | 1,591,687.0 | 204,208,329.0 | 206,801.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 205,006,963.0 | 197,487,239.0 | 212,076,696.0 | 5,081,495.4 | 5 | 35,792 | 24,115 | 23,884 | 0.025 | compiled=5 | 1,634,217.0 | 203,260,326.0 | 189,471.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `utf8-lead-no-cont` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 175,005,163.0 | 168,870,779.0 | 180,737,308.0 | 3,903,877.4 | 5 | 41,248 | 23,987 | 18,583 | 0.022 | compiled=5 | 2,279,419.0 | 172,523,584.0 | 202,131.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 170,780,228.0 | 161,755,010.0 | 173,835,719.0 | 4,129,046.7 | 5 | 41,208 | 23,809 | 18,405 | 0.024 | compiled=5 | 1,670,666.0 | 169,241,091.0 | 98,130.0 |
| `uuid-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 171,543,311.0 | 169,086,480.0 | 177,684,578.0 | 3,309,960.0 | 5 | 41,248 | 23,987 | 18,583 | 0.019 | compiled=5 | 1,650,568.0 | 169,272,381.0 | 189,501.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 178,336,532.0 | 163,269,003.0 | 181,684,737.0 | 6,653,268.7 | 5 | 41,208 | 23,809 | 18,405 | 0.037 | compiled=5 | 1,665,358.0 | 176,482,313.0 | 183,581.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 142,205,462.0 | 134,913,753.0 | 152,194,682.0 | 6,058,292.8 | 5 | 31,968 | 19,793 | 14,796 | 0.043 | compiled=5 | 1,724,367.0 | 140,272,765.0 | 183,971.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 165,287,495.0 | 147,551,533.0 | 169,768,283.0 | 7,694,018.1 | 5 | 32,112 | 22,248 | 16,925 | 0.047 | compiled=5 | 3,682,475.0 | 162,191,572.0 | 100,891.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 146,299,506.0 | 141,814,845.0 | 165,039,951.0 | 8,131,959.1 | 5 | 31,968 | 19,793 | 14,796 | 0.056 | compiled=5 | 1,744,718.0 | 144,424,997.0 | 111,760.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 161,726,386.0 | 145,759,314.0 | 166,741,479.0 | 7,561,047.1 | 5 | 32,112 | 22,248 | 16,925 | 0.047 | compiled=5 | 1,759,478.0 | 159,867,608.0 | 109,130.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 161,671,700.0 | 142,882,425.0 | 163,331,097.0 | 8,017,347.1 | 5 | 32,296 | 28,744 | 16,479 | 0.050 | compiled=5 | 2,243,729.0 | 159,308,381.0 | 115,840.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 169,416,242.0 | 166,139,678.0 | 177,324,023.0 | 3,721,980.5 | 5 | 32,432 | 31,719 | 18,566 | 0.022 | compiled=5 | 2,374,150.0 | 166,896,982.0 | 188,931.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 151,330,310.0 | 145,067,260.0 | 166,292,388.0 | 7,002,777.7 | 5 | 32,296 | 28,744 | 16,479 | 0.046 | compiled=5 | 2,291,110.0 | 148,945,868.0 | 194,011.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 163,270,553.0 | 159,321,065.0 | 172,857,357.0 | 5,474,102.4 | 5 | 32,432 | 31,719 | 18,566 | 0.034 | compiled=5 | 2,463,961.0 | 160,708,212.0 | 183,910.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 155,278,664.0 | 143,834,158.0 | 159,570,972.0 | 5,716,495.1 | 5 | 31,968 | 19,795 | 14,798 | 0.037 | compiled=5 | 1,738,377.0 | 153,467,657.0 | 191,100.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 163,690,089.0 | 155,393,675.0 | 166,586,909.0 | 4,576,336.3 | 5 | 32,112 | 22,250 | 16,927 | 0.028 (max is trial 1) | compiled=5 | 1,758,957.0 | 161,746,841.0 | 193,560.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 151,669,610.0 | 145,899,035.0 | 166,369,676.0 | 7,071,666.8 | 5 | 31,968 | 19,795 | 14,798 | 0.047 | compiled=5 | 1,747,738.0 | 149,731,731.0 | 189,361.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 160,693,512.0 | 150,695,745.0 | 171,406,331.0 | 7,336,523.7 | 5 | 32,112 | 22,250 | 16,927 | 0.046 | compiled=5 | 1,772,128.0 | 158,734,823.0 | 186,561.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 598,464,358.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 16,237,105,868.0 | 16,160,855,071.0 | 16,328,483,054.0 | 69,412,009.0 | 5 | 154,944 | 484,520 (warned) | 482,896 | 0.004 | compiled=5 | 9,382,286,188.0 | 6,887,774,372.0 | 98,420.0 |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 585,385,094.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,242,282,476.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 362,851,010.0 | 354,098,834.0 | 373,708,973.0 | 7,510,059.5 | 5 | 50,008 | 55,856 | 45,933 | 0.021 | compiled=5 | 2,298,619.0 | 360,486,641.0 | 98,030.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 346,267,733.0 | 340,290,230.0 | 350,411,089.0 | 3,825,641.8 | 5 | 49,640 | 54,295 | 44,372 | 0.011 | compiled=5 | 2,310,359.0 | 341,518,164.0 | 102,100.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 360,929,372.0 | 354,661,745.0 | 366,630,029.0 | 3,974,951.8 | 5 | 50,008 | 55,856 | 45,933 | 0.011 | compiled=5 | 2,324,661.0 | 358,559,092.0 | 102,040.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 351,004,607.0 | 345,993,425.0 | 351,437,560.0 | 2,430,976.3 | 5 | 49,640 | 54,295 | 44,372 | 0.007 | compiled=5 | 2,335,320.0 | 348,551,687.0 | 103,001.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 246,619,922.0 | 240,212,366.0 | 247,664,696.0 | 2,808,417.0 | 5 | 40,432 | 46,133 | 29,228 | 0.011 | compiled=5 | 3,221,113.0 | 243,301,959.0 | 102,500.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 250,449,216.0 | 244,865,595.0 | 260,170,066.0 | 6,859,551.1 | 5 | 40,528 | 48,666 | 30,765 | 0.027 | compiled=5 | 7,128,098.0 | 243,118,618.0 | 181,690.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 255,334,991.0 | 251,503,564.0 | 256,986,430.0 | 1,811,771.3 | 5 | 40,432 | 48,061 | 31,156 | 0.007 | compiled=5 | 3,186,995.0 | 251,948,887.0 | 114,750.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 257,534,712.0 | 255,766,805.0 | 265,495,049.0 | 4,108,479.6 | 5 | 40,528 | 50,594 | 32,693 | 0.016 | compiled=5 | 6,690,690.0 | 254,033,956.0 | 186,840.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 336,002,512.0 | 328,856,823.0 | 341,915,306.0 | 4,607,956.9 | 5 | 44,400 | 56,824 | 26,714 | 0.014 | compiled=5 | 4,466,798.0 | 331,277,873.0 | 200,201.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 337,775,731.0 | 330,486,170.0 | 339,174,245.0 | 3,659,756.5 | 5 | 44,496 | 60,192 | 28,249 | 0.011 | compiled=5 | 4,594,819.0 | 327,067,026.0 | 108,171.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 394,919,877.0 | 386,399,679.0 | 396,992,296.0 | 3,903,406.5 | 5 | 48,496 | 58,384 | 28,274 | 0.010 | compiled=5 | 4,673,022.0 | 386,345,188.0 | 190,381.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 399,142,657.0 | 391,433,392.0 | 422,202,002.0 | 10,514,370.4 | 5 | 44,496 | 61,754 | 29,811 | 0.026 | compiled=5 | 4,594,141.0 | 387,539,964.0 | 191,641.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 287,572,887.0 | 285,741,009.0 | 289,713,305.0 | 1,396,171.4 | 5 | 56,720 | 105,222 | 33,872 | 0.005 (max is trial 1) | compiled=5 | 7,603,391.0 | 278,503,751.0 | 194,071.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 295,011,477.0 | 289,599,936.0 | 301,055,151.0 | 4,234,027.3 | 5 | 56,816 | 112,577 | 35,416 | 0.014 | compiled=5 | 8,019,252.0 | 282,966,399.0 | 100,521.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 285,392,879.0 | 278,912,740.0 | 298,266,048.0 | 6,323,727.6 | 5 | 56,720 | 105,520 | 34,170 | 0.022 | compiled=5 | 8,594,410.0 | 277,735,044.0 | 102,090.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 295,470,065.0 | 288,717,665.0 | 300,119,935.0 | 3,683,253.0 | 5 | 56,816 | 112,875 | 35,714 | 0.012 (max is trial 1) | compiled=5 | 8,024,856.0 | 287,262,627.0 | 194,951.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 552,196,852.0 | 542,883,744.0 | 565,368,775.0 | 7,297,799.5 | 5 | 212,832 | 550,723 (warned) | 41,457 | 0.013 (max is trial 1) | compiled=5 | 64,033,297.0 | 485,673,274.0 | 180,230.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 568,486,957.0 | 558,838,068.0 | 592,398,423.0 | 12,429,040.3 | 5 | 217,024 | 565,513 (warned) | 42,745 | 0.022 | compiled=5 | 65,023,422.0 | 503,488,306.0 | 194,281.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 571,225,301.0 | 562,128,849.0 | 593,053,709.0 | 10,204,651.5 | 5 | 212,832 | 554,081 (warned) | 44,814 | 0.018 (max is trial 1) | compiled=5 | 57,753,283.0 | 513,595,168.0 | 96,440.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 587,990,728.0 | 576,847,866.0 | 601,549,278.0 | 9,808,400.1 | 5 | 217,024 | 568,871 (warned) | 46,102 | 0.017 (max is trial 1) | compiled=5 | 64,956,986.0 | 522,936,430.0 | 101,900.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 163,953,701.0 | 155,321,995.0 | 164,647,173.0 | 3,502,734.7 | 5 | 31,968 | 21,710 | 16,003 | 0.021 | compiled=5 | 1,861,687.0 | 161,991,172.0 | 99,921.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 163,972,901.0 | 160,325,195.0 | 177,205,513.0 | 6,562,934.8 | 5 | 32,112 | 23,954 | 17,347 | 0.040 | compiled=5 | 1,933,198.0 | 159,881,103.0 | 191,211.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 155,012,536.0 | 151,577,510.0 | 155,692,487.0 | 1,482,773.6 | 5 | 31,968 | 21,710 | 16,003 | 0.010 | compiled=5 | 2,147,880.0 | 152,767,015.0 | 185,441.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 162,453,090.0 | 161,831,257.0 | 171,593,801.0 | 4,503,202.6 | 5 | 32,112 | 23,954 | 17,347 | 0.028 | compiled=5 | 2,216,590.0 | 160,404,560.0 | 193,641.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 172,780,084.0 | 165,863,897.0 | 177,210,672.0 | 3,809,334.8 | 5 | 32,112 | 23,560 | 17,779 | 0.022 | compiled=5 | 1,989,118.0 | 170,832,347.0 | 193,340.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 161,863,902.0 | 157,113,092.0 | 171,070,037.0 | 5,647,029.6 | 5 | 32,112 | 23,132 | 17,351 | 0.035 (max is trial 1) | compiled=5 | 1,852,658.0 | 160,090,474.0 | 100,001.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 166,005,735.0 | 158,667,273.0 | 182,771,932.0 | 8,709,235.3 | 5 | 32,112 | 23,560 | 17,779 | 0.052 | compiled=5 | 2,116,090.0 | 164,247,338.0 | 192,391.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 164,724,390.0 | 160,576,879.0 | 169,710,633.0 | 3,239,741.0 | 5 | 32,112 | 23,132 | 17,351 | 0.020 | compiled=5 | 1,841,759.0 | 162,948,932.0 | 98,971.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 223,010,668.0 | 215,581,629.0 | 223,275,788.0 | 3,185,134.8 | 5 | 36,144 | 32,388 | 27,554 | 0.014 | compiled=5 | 1,875,037.0 | 220,934,669.0 | 104,020.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 225,421,228.0 | 219,369,061.0 | 228,065,888.0 | 3,504,466.2 | 5 | 36,240 | 33,867 | 28,803 | 0.016 | compiled=5 | 1,907,198.0 | 221,259,041.0 | 106,730.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 213,490,771.0 | 204,906,351.0 | 225,134,316.0 | 7,322,632.5 | 5 | 36,144 | 32,388 | 27,554 | 0.034 | compiled=5 | 1,800,148.0 | 211,486,662.0 | 108,630.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 228,473,910.0 | 220,159,932.0 | 238,815,166.0 | 8,010,435.9 | 5 | 36,240 | 33,867 | 28,803 | 0.035 | compiled=5 | 1,913,489.0 | 226,359,210.0 | 202,011.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 145,514,646.0 | 137,172,062.0 | 152,111,612.0 | 6,116,082.8 | 5 | 31,792 | 15,957 | 13,600 | 0.042 | compiled=5 | 1,546,007.0 | 143,889,929.0 | 190,020.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 148,728,149.0 | 130,641,656.0 | 149,877,493.0 | 7,212,248.4 | 5 | 31,792 | 15,780 | 13,423 | 0.048 | compiled=5 | 1,583,966.0 | 146,970,601.0 | 185,621.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 143,573,072.0 | 131,393,338.0 | 151,377,409.0 | 7,177,790.9 | 5 | 31,792 | 15,957 | 13,600 | 0.050 | compiled=5 | 1,371,146.0 | 141,912,236.0 | 101,590.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 139,528,746.0 | 134,199,890.0 | 154,693,835.0 | 7,895,393.1 | 5 | 31,792 | 15,780 | 13,423 | 0.057 (max is trial 1) | compiled=5 | 1,650,767.0 | 137,769,467.0 | 194,771.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 320,825,160.0 | 313,314,300.0 | 323,646,393.0 | 3,848,527.8 | 5 | 45,136 | 46,197 | 41,169 | 0.012 | compiled=5 | 2,194,158.0 | 318,667,102.0 | 109,481.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 315,141,278.0 | 300,153,178.0 | 325,953,622.0 | 8,255,125.4 | 5 | 44,928 | 45,380 | 40,352 | 0.026 | compiled=5 | 2,081,539.0 | 312,834,358.0 | 106,970.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 320,446,150.0 | 313,552,068.0 | 322,358,496.0 | 3,231,882.2 | 5 | 45,136 | 46,197 | 41,169 | 0.010 (max is trial 1) | compiled=5 | 2,069,389.0 | 317,491,685.0 | 105,681.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 315,391,736.0 | 311,088,747.0 | 318,627,420.0 | 2,404,944.9 | 5 | 44,928 | 45,380 | 40,352 | 0.008 | compiled=5 | 2,238,710.0 | 313,118,105.0 | 205,311.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 211,087,580.0 | 210,140,765.0 | 213,443,829.0 | 1,222,779.9 | 5 | 36,248 | 28,501 | 25,957 | 0.006 (max is trial 1) | compiled=5 | 1,713,897.0 | 208,486,449.0 | 206,501.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 208,900,040.0 | 198,706,730.0 | 212,197,793.0 | 5,383,073.7 | 5 | 36,160 | 28,241 | 25,697 | 0.026 | compiled=5 | 1,732,287.0 | 206,968,783.0 | 120,220.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 210,094,836.0 | 206,106,897.0 | 210,216,127.0 | 1,601,518.3 | 5 | 36,248 | 28,501 | 25,957 | 0.008 | compiled=5 | 1,716,838.0 | 208,210,458.0 | 189,401.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 207,401,554.0 | 202,997,224.0 | 207,910,925.0 | 1,843,619.4 | 5 | 36,160 | 28,241 | 25,697 | 0.009 | compiled=5 | 1,716,948.0 | 205,498,376.0 | 211,131.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 242,014,414.0 | 240,471,417.0 | 248,713,370.0 | 3,107,646.1 | 5 | 40,736 | 47,955 | 22,637 | 0.013 | compiled=5 | 3,182,883.0 | 238,083,358.0 | 102,700.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 254,588,484.0 | 251,946,923.0 | 255,512,309.0 | 1,243,950.9 | 5 | 40,880 | 50,932 | 24,341 | 0.005 | compiled=5 | 3,281,423.0 | 251,208,760.0 | 100,061.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 248,870,482.0 | 241,301,488.0 | 250,073,449.0 | 3,344,133.2 | 5 | 40,736 | 47,955 | 22,637 | 0.013 | compiled=5 | 3,189,285.0 | 245,594,917.0 | 210,551.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 255,406,972.0 | 252,187,140.0 | 261,543,721.0 | 3,038,093.1 | 5 | 40,880 | 50,932 | 24,341 | 0.012 | compiled=5 | 3,247,955.0 | 252,043,808.0 | 116,310.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 230,548,828.0 | 222,259,265.0 | 233,698,349.0 | 3,843,605.3 | 5 | 89,912 | 227,952 | 19,986 | 0.017 (max is trial 1) | compiled=5 | 14,321,558.0 | 216,024,099.0 | 101,331.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 237,220,474.0 | 236,476,250.0 | 243,577,181.0 | 3,231,989.9 | 5 | 98,248 | 237,783 | 21,962 | 0.014 | compiled=5 | 15,688,323.0 | 221,562,161.0 | 106,321.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 230,600,820.0 | 222,982,225.0 | 237,975,203.0 | 4,748,499.3 | 5 | 89,912 | 227,952 | 19,986 | 0.021 | compiled=5 | 14,463,246.0 | 215,929,333.0 | 191,610.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 243,172,506.0 | 234,427,317.0 | 253,825,825.0 | 6,925,325.5 | 5 | 98,248 | 237,783 | 21,962 | 0.028 (max is trial 1) | compiled=5 | 15,728,081.0 | 220,261,993.0 | 99,480.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 190,270,275.0 | 189,818,044.0 | 196,344,751.0 | 2,880,077.6 | 5 | 40,656 | 58,368 | 17,968 | 0.015 | compiled=5 | 4,887,589.0 | 184,739,694.0 | 183,830.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 200,714,787.0 | 200,009,424.0 | 207,951,747.0 | 3,512,320.5 | 5 | 44,896 | 62,147 | 19,759 | 0.017 | compiled=5 | 4,997,510.0 | 195,170,005.0 | 117,490.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 189,125,631.0 | 187,206,370.0 | 197,488,458.0 | 4,350,109.7 | 5 | 40,656 | 58,368 | 17,968 | 0.023 | compiled=5 | 4,497,321.0 | 184,440,919.0 | 100,560.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 207,761,146.0 | 193,048,249.0 | 220,113,292.0 | 8,638,630.8 | 5 | 44,896 | 62,147 | 19,759 | 0.042 | compiled=5 | 5,085,823.0 | 202,507,902.0 | 188,501.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 163,595,269.0 | 155,636,027.0 | 175,175,475.0 | 7,513,629.2 | 5 | 36,328 | 36,918 | 15,751 | 0.046 | compiled=5 | 3,219,083.0 | 160,185,325.0 | 107,631.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 175,650,796.0 | 174,710,092.0 | 188,331,998.0 | 5,801,832.1 | 5 | 36,472 | 39,942 | 17,763 | 0.033 | compiled=5 | 4,005,786.0 | 172,287,733.0 | 203,081.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 170,979,928.0 | 162,347,608.0 | 173,275,939.0 | 3,771,695.6 | 5 | 36,328 | 36,918 | 15,751 | 0.022 | compiled=5 | 3,790,158.0 | 165,805,375.0 | 99,450.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 174,606,675.0 | 174,132,753.0 | 178,895,014.0 | 1,784,149.1 | 5 | 36,472 | 39,942 | 17,763 | 0.010 (max is trial 1) | compiled=5 | 3,320,145.0 | 171,089,919.0 | 104,311.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,468,029,526.0 | 1,432,311,683.0 | 1,479,020,801.0 | 15,858,436.1 | 5 | 684,624 | 395,013 (warned) | 100,533 | 0.011 | compiled=5 | 12,718,201.0 | 1,454,845,623.0 | 539,092.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 1,380,123,403.0 | 1,373,744,747.0 | 1,398,153,234.0 | 9,920,647.6 | 5 | 664,088 | 402,219 (warned) | 102,683 | 0.007 | compiled=5 | 12,981,212.0 | 1,365,878,586.0 | 530,802.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,457,532,895.0 | 1,422,837,226.0 | 1,474,106,489.0 | 20,168,995.7 | 5 | 684,624 | 395,013 (warned) | 100,533 | 0.014 | compiled=5 | 12,705,338.0 | 1,444,544,725.0 | 290,711.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 1,383,376,777.0 | 1,363,869,928.0 | 1,405,548,048.0 | 15,345,462.7 | 5 | 664,088 | 402,219 (warned) | 102,683 | 0.011 | compiled=5 | 24,474,002.0 | 1,360,206,651.0 | 523,523.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 156,921,380.0 | 153,078,955.0 | 163,799,469.0 | 4,208,153.5 | 5 | 31,968 | 21,615 | 15,703 | 0.027 | compiled=5 | 2,072,229.0 | 154,634,542.0 | 193,101.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 172,728,745.0 | 171,994,681.0 | 185,025,685.0 | 4,972,403.1 | 5 | 32,112 | 24,222 | 17,792 | 0.029 (max is trial 1) | compiled=5 | 2,139,479.0 | 170,065,804.0 | 187,530.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 159,528,746.0 | 144,734,977.0 | 163,786,815.0 | 7,212,481.7 | 5 | 31,968 | 21,615 | 15,703 | 0.045 | compiled=5 | 2,034,989.0 | 155,090,766.0 | 194,531.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 169,242,841.0 | 163,538,304.0 | 172,902,768.0 | 3,750,849.1 | 5 | 32,112 | 24,222 | 17,792 | 0.022 | compiled=5 | 2,130,920.0 | 164,552,309.0 | 183,631.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 137,337,682.0 | 133,972,710.0 | 147,857,985.0 | 5,033,131.4 | 5 | 31,752 | 15,346 | 13,263 | 0.037 | compiled=5 | 1,532,137.0 | 135,625,366.0 | 100,300.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_cf-align-functions-64-align-loops-64` | 138,124,715.0 | 127,800,645.0 | 147,511,853.0 | 7,295,263.2 | 5 | 31,712 | 15,169 | 13,086 | 0.053 | compiled=5 | 1,571,027.0 | 136,375,849.0 | 107,690.0 |
| `winpath-near-miss` | `plain` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 137,714,696.0 | 136,054,810.0 | 149,117,559.0 | 4,938,670.4 | 5 | 31,752 | 15,346 | 13,263 | 0.036 | compiled=5 | 1,523,967.0 | 134,543,662.0 | 191,821.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a32bc86e_auto-caps-simdna_nolitrun-cf-align-functions-64-align-loops-64` | 145,882,494.0 | 133,838,069.0 | 148,811,577.0 | 5,331,935.9 | 5 | 31,712 | 15,169 | 13,086 | 0.037 | compiled=5 | 1,536,767.0 | 144,143,196.0 | 188,091.0 |

