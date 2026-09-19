# pcrec-bench report

reporter: v18 (2026-09-18)

## Query

- filters: subbench=capability, version=0.1, machine=budu-ryzen1600, since=2026-09-17T00:00:00Z, until=2026-09-17T08:00:00Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=libpcre2_10.46_dfa-nocaps-simdna, testee=pcrec_a770139e_auto-caps-simdna, testee=pcrec_a770139e_auto-nocaps-simdna, testee=pcrec_a770139e_vm-caps-simdna, testee=pcrec_a770139e_vm-in-caps-simdna
- record source: store/index.tsv (8 record(s) matching this query)
- records included: 7
- worst other-core busy: 48.39% (`libpcre2_10.46_dfa-nocaps-simdna` / `email-local-nodup` / `large-subject-throughput`)
    - `capability@0.1__libpcre2_10.46_dfa-nocaps-simdna__budu-ryzen1600__20260917T062345Z` (store/records/capability@0.1/libpcre2_10.46_dfa-nocaps-simdna/capability@0.1__libpcre2_10.46_dfa-nocaps-simdna__budu-ryzen1600__20260917T062345Z.jsonl) — agreement: agree (0 of 116 groups; 5 of 4572 rows; 30 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260917T005053Z` (store/records/capability@0.1/libpcre2_10.46_interp-caps-simdna/capability@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260917T005053Z.jsonl) — agreement: agree (0 of 126 groups; 52 of 4984 rows; 8 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260917T013333Z` (store/records/capability@0.1/libpcre2_10.46_jit-caps-simdna/capability@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260917T013333Z.jsonl) — agreement: agree (0 of 128 groups; 0 of 4990 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a770139e_auto-caps-simdna__budu-ryzen1600__20260917T020152Z` (store/records/capability@0.1/pcrec_a770139e_auto-caps-simdna/capability@0.1__pcrec_a770139e_auto-caps-simdna__budu-ryzen1600__20260917T020152Z.jsonl) — agreement: agree (0 of 122 groups; 6 of 4755 rows; 3 unjudged (2 all-timed-out); k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a770139e_auto-nocaps-simdna__budu-ryzen1600__20260917T024324Z` (store/records/capability@0.1/pcrec_a770139e_auto-nocaps-simdna/capability@0.1__pcrec_a770139e_auto-nocaps-simdna__budu-ryzen1600__20260917T024324Z.jsonl) — agreement: agree (0 of 124 groups; 4 of 4833 rows; 3 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a770139e_vm-caps-simdna__budu-ryzen1600__20260917T030830Z` (store/records/capability@0.1/pcrec_a770139e_vm-caps-simdna/capability@0.1__pcrec_a770139e_vm-caps-simdna__budu-ryzen1600__20260917T030830Z.jsonl) — agreement: agree (0 of 124 groups; 5 of 4828 rows; 8 unjudged (7 all-timed-out); k=1.5, 2/3; 5 trials)
    - `capability@0.1__pcrec_a770139e_vm-in-caps-simdna__budu-ryzen1600__20260917T042856Z` (store/records/capability@0.1/pcrec_a770139e_vm-in-caps-simdna/capability@0.1__pcrec_a770139e_vm-in-caps-simdna__budu-ryzen1600__20260917T042856Z.jsonl) — agreement: agree (0 of 124 groups; 7 of 4828 rows; 8 unjudged (7 all-timed-out); k=1.5, 2/3; 5 trials)
- superseded: 1 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.5
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

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 562,266.0 | 0.4085 | 557,095.6 | 568,518.6 | 3,824.2 | 0.194x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,903,815.8 | 2.1099 | 2,887,176.7 | 2,933,939.2 | 15,780.3 | 1.000x | 5.164x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,705,332.8 | 3.4189 | 4,688,470.7 | 4,789,755.6 | 36,667.1 | 1.620x | 8.369x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,478,129.3 | 3.9805 | 5,471,485.6 | 5,498,133.0 | 9,399.6 | 1.887x | 9.743x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 5,483,768.4 | 3.9846 | 5,480,698.6 | 5,488,332.0 | 3,059.8 | 1.888x | 9.753x |
| 6 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 5,484,126.5 | 3.9848 | 5,482,435.4 | 5,496,093.6 | 4,953.9 | 1.889x | 9.754x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,495,730.3 | 3.9932 | 5,492,313.0 | 5,506,002.9 | 5,536.7 | 1.893x | 9.774x |

#### `balanced-parens-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 432,269.1 | 0.4122 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,233,889.5 | 2.1304 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 3,624,544.2 | 3.4566 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 4,173,983.8 | 3.9806 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 4,180,414.9 | 3.9868 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 4,177,732.9 | 3.9842 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 4,189,440.1 | 3.9954 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 105,140.3 | 0.4011 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 534,267.8 | 2.0381 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 865,887.4 | 3.3031 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,041,992.7 | 3.9749 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 1,042,028.7 | 3.9750 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 1,044,987.4 | 3.9863 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,044,164.4 | 3.9832 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 25,209.9 | 0.3847 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 132,966.6 | 2.0289 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 214,986.9 | 3.2804 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 261,009.3 | 3.9827 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 260,771.0 | 3.9791 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 261,316.0 | 3.9874 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 261,652.1 | 3.9925 |

### `balanced-parens-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,959.0 | 2,846.1 | 3,284.2 | 159.3 | 0.765x | 1.000x | 75 | 39.5 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,866.5 | 3,838.5 | 4,063.9 | 83.3 | 1.000x | 1.307x | 75 | 51.6 | 34.4 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,585.5 | 4,567.7 | 5,362.7 | 312.8 | 1.186x | 1.550x | 75 | 61.1 | 30.4 | 100% |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 6,418.6 | 6,310.9 | 6,654.3 | 123.9 | 1.660x | 2.169x | 75 | 85.6 | 8.9 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,558.1 | 6,506.5 | 6,621.0 | 44.5 | 1.696x | 2.216x | 75 | 87.4 | 18.1 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,606.1 | 6,513.8 | 6,714.9 | 74.0 | 1.709x | 2.233x | 75 | 88.1 | 17.3 | 100% |
| 7 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 6,643.2 | 6,495.2 | 6,691.9 | 67.6 | 1.718x | 2.245x | 75 | 88.6 | 8.9 | 100% |

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.8 | 17.3 | 0.2 | 0.182x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 16.9 | 0.0000 | 16.9 | 16.9 | 0.0 | 0.183x | 1.001x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.9 | 0.0001 | 80.5 | 81.2 | 0.2 | 0.874x | 4.793x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 92.6 | 0.0001 | 92.5 | 93.1 | 0.2 | 1.000x | 5.485x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 118.9 | 0.0001 | 114.6 | 123.1 | 3.2 | 1.284x | 7.042x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,067,311.7 | 2.9553 | 4,064,620.3 | 4,075,092.8 | 3,549.5 | 43919.122x | 240916.748x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,071,138.8 | 2.9581 | 4,066,654.6 | 4,074,917.6 | 3,407.7 | 43960.448x | 241143.437x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.0 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,098,414.0 | 2.9549 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,102,121.9 | 2.9584 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 5.6 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 38.7 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 774,757.8 | 2.9555 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 774,807.8 | 2.9557 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.6 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 30.9 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 38.6 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 194,286.3 | 2.9646 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 194,898.1 | 2.9739 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 548.7 | 537.3 | 553.7 | 6.6 | 0.121x | 1.000x | 75 | 7.3 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 551.9 | 550.1 | 556.2 | 2.3 | 0.122x | 1.006x | 75 | 7.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,177.4 | 3,042.0 | 3,412.1 | 141.1 | 0.700x | 5.790x | 75 | 42.4 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,536.7 | 4,476.0 | 4,546.8 | 29.2 | 1.000x | 8.268x | 75 | 60.5 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,930.6 | 4,891.8 | 5,638.0 | 290.0 | 1.087x | 8.985x | 75 | 65.7 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,654.0 | 5,636.3 | 5,675.2 | 13.4 | 1.246x | 10.304x | 75 | 75.4 | 17.3 | 100% |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,710.8 | 5,700.0 | 5,715.4 | 5.3 | 1.259x | 10.407x | 75 | 76.1 | 18.1 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.3 | 0.0001 | 122.2 | 132.0 | 4.1 | 0.387x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 311.0 | 0.0002 | 310.6 | 313.0 | 0.9 | 0.938x | 2.424x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 331.4 | 0.0002 | 330.9 | 342.2 | 4.3 | 1.000x | 2.583x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,881,550.9 | 3.5470 | 4,880,576.7 | 4,920,304.1 | 17,805.2 | 14728.451x | 38040.015x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,881,816.8 | 3.5472 | 4,878,417.5 | 4,883,952.9 | 2,292.4 | 14729.253x | 38042.087x |
| 6 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,882,439.1 | 3.5476 | 4,879,169.3 | 4,888,963.2 | 4,371.2 | 14731.131x | 38046.937x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,895,988.6 | 3.5575 | 4,887,297.6 | 4,928,819.5 | 14,305.7 | 14772.012x | 38152.523x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 103.8 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 110.3 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,717,424.8 | 3.5452 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,716,801.5 | 3.5446 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,719,237.8 | 3.5469 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,729,802.8 | 3.5570 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 42.8 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 103.5 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 110.3 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 930,720.8 | 3.5504 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 930,726.0 | 3.5504 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 929,771.8 | 3.5468 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 932,266.5 | 3.5563 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42.2 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 104.1 | 0.0016 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 111.0 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 233,352.8 | 3.5607 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 233,797.3 | 3.5675 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 233,429.6 | 3.5619 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 234,854.2 | 3.5836 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,233.6 | 3,109.3 | 3,400.1 | 106.3 | 0.366x | 1.000x | 75 | 43.1 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 6,822.0 | 6,819.7 | 6,836.8 | 7.6 | 0.773x | 2.110x | 75 | 91.0 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,843.4 | 6,819.9 | 6,848.1 | 10.8 | 0.775x | 2.116x | 75 | 91.2 | 18.1 | 100% |
| 4 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 6,870.6 | 6,859.7 | 6,886.8 | 8.7 | 0.779x | 2.125x | 75 | 91.6 | 8.9 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,093.4 | 7,077.9 | 7,132.1 | 19.0 | 0.804x | 2.194x | 75 | 94.6 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 8,824.7 | 8,806.4 | 8,920.4 | 41.8 | 1.000x | 2.729x | 75 | 117.7 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,881.9 | 8,868.2 | 9,058.8 | 70.9 | 1.006x | 2.747x | 75 | 118.4 | 30.4 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 610,465.6 | 0.4436 | 597,417.5 | 627,408.9 | 9,770.8 | 0.288x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 645,342.6 | 0.4689 | 639,094.1 | 657,120.2 | 6,231.3 | 0.305x | 1.057x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 907,844.0 | 0.6596 | 900,359.0 | 923,453.5 | 8,149.8 | 0.429x | 1.487x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,999,677.3 | 1.4530 | 1,992,256.1 | 2,009,290.8 | 6,227.4 | 0.945x | 3.276x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,116,040.6 | 1.5375 | 2,112,873.8 | 2,117,247.5 | 1,552.2 | 1.000x | 3.466x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,446,367.4 | 3.2308 | 4,434,590.5 | 4,452,969.5 | 6,751.6 | 2.101x | 7.284x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,415,823.9 | 11.2013 | 14,303,071.9 | 15,973,547.6 | 684,334.2 | 7.285x | 25.253x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 469,445.4 | 0.4477 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 499,967.6 | 0.4768 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 696,379.5 | 0.6641 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 1,522,179.3 | 1.4517 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,620,049.8 | 1.5450 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,394,020.2 | 3.2368 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 11,712,969.9 | 11.1704 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 111,990.1 | 0.4272 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 114,638.5 | 0.4373 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 166,476.6 | 0.6351 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 381,412.7 | 1.4550 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 397,465.0 | 1.5162 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 838,436.7 | 3.1984 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,958,583.6 | 11.2861 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 27,433.1 | 0.4186 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 30,678.8 | 0.4681 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42,012.8 | 0.6411 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 95,366.5 | 1.4552 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,035.3 | 1.5112 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 212,402.2 | 3.2410 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 735,328.1 | 11.2202 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 726.5 | 723.9 | 729.1 | 1.8 | 0.266x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 938.3 | 929.2 | 939.6 | 3.8 | 0.343x | 1.291x | 75 | 12.5 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,556.0 | 1,552.0 | 1,556.5 | 1.7 | 0.569x | 2.142x | 75 | 20.7 | 18.1 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,456.6 | 2,444.0 | 3,121.7 | 289.8 | 0.898x | 3.381x | 75 | 32.8 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,734.4 | 2,668.6 | 2,961.0 | 111.7 | 1.000x | 3.764x | 75 | 36.5 | 34.4 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,299.6 | 3,188.9 | 3,535.2 | 126.6 | 1.207x | 4.542x | 75 | 44.0 | 40.4 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,782.0 | 3,773.0 | 3,796.7 | 7.8 | 1.383x | 5.206x | 75 | 50.4 | 17.3 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 614,392.3 | 0.4464 | 612,213.3 | 634,295.6 | 8,125.8 | 0.290x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 646,193.8 | 0.4695 | 640,548.0 | 664,055.3 | 8,286.5 | 0.305x | 1.052x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 904,180.0 | 0.6570 | 892,724.8 | 919,160.0 | 9,340.3 | 0.426x | 1.472x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,003,777.1 | 1.4560 | 1,995,876.4 | 2,004,950.9 | 3,668.1 | 0.945x | 3.261x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,121,186.4 | 1.5413 | 2,111,247.3 | 2,122,007.5 | 4,547.1 | 1.000x | 3.452x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,413,243.3 | 3.2067 | 4,410,760.2 | 4,443,849.5 | 12,643.0 | 2.081x | 7.183x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 14,814,920.1 | 10.7647 | 14,530,742.7 | 16,280,473.3 | 633,152.7 | 6.984x | 24.113x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 469,842.7 | 0.4481 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 494,702.7 | 0.4718 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 696,904.6 | 0.6646 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 1,525,189.7 | 1.4545 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,623,317.2 | 1.5481 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,360,914.6 | 3.2052 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 11,384,958.4 | 10.8575 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 117,506.0 | 0.4482 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 125,937.0 | 0.4804 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 164,878.2 | 0.6290 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 379,639.8 | 1.4482 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 397,016.3 | 1.5145 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 841,125.6 | 3.2086 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,782,399.1 | 10.6140 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 27,320.0 | 0.4169 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 28,425.5 | 0.4337 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42,222.4 | 0.6443 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 95,955.7 | 1.4642 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,221.0 | 1.5140 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 211,441.0 | 3.2263 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 691,448.7 | 10.5507 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 726.2 | 724.0 | 732.4 | 2.9 | 0.262x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 940.6 | 936.3 | 941.5 | 1.8 | 0.339x | 1.295x | 75 | 12.5 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,559.4 | 1,546.2 | 1,561.2 | 5.6 | 0.562x | 2.147x | 75 | 20.8 | 18.1 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,477.9 | 2,446.8 | 3,469.5 | 446.7 | 0.894x | 3.412x | 75 | 33.0 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,772.8 | 2,672.9 | 2,889.0 | 76.0 | 1.000x | 3.818x | 75 | 37.0 | 34.4 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,154.0 | 3,149.6 | 3,191.9 | 15.7 | 1.137x | 4.343x | 75 | 42.1 | 40.4 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,774.5 | 3,772.5 | 3,782.0 | 3.4 | 1.361x | 5.197x | 75 | 50.3 | 17.3 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,723,358.9 | 1.2522 | 1,722,608.4 | 1,727,284.7 | 1,688.1 | 0.152x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 10,819,260.4 | 7.8614 | 10,792,630.6 | 10,874,233.5 | 28,319.1 | 0.953x | 6.278x |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 11,101,888.3 | 8.0667 | 11,085,158.6 | 11,185,193.3 | 37,762.5 | 0.978x | 6.442x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 11,120,743.5 | 8.0804 | 11,114,940.9 | 11,122,443.5 | 2,979.1 | 0.979x | 6.453x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 11,207,587.8 | 8.1435 | 11,192,443.2 | 11,250,211.8 | 19,515.2 | 0.987x | 6.503x |
| 6 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 11,237,220.0 | 8.1651 | 11,210,957.3 | 11,257,968.9 | 17,500.8 | 0.989x | 6.521x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 11,356,965.2 | 8.2521 | 11,329,033.5 | 12,285,092.4 | 370,864.9 | 1.000x | 6.590x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,318,109.5 | 1.2570 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 8,291,377.1 | 7.9073 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 8,465,042.8 | 8.0729 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 8,470,009.2 | 8.0776 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 8,525,461.5 | 8.1305 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 8,561,314.5 | 8.1647 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,710,549.0 | 8.3070 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 325,054.6 | 1.2400 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,046,429.3 | 7.8065 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 2,114,446.8 | 8.0660 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 2,119,758.0 | 8.0862 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 2,140,164.6 | 8.1641 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 2,137,246.0 | 8.1529 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,132,165.0 | 8.1336 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 80,898.6 | 1.2344 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 491,307.6 | 7.4968 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 527,758.8 | 8.0530 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 532,120.9 | 8.1195 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 536,346.4 | 8.1840 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 537,187.5 | 8.1968 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 514,251.2 | 7.8469 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,033.4 | 4,026.7 | 4,335.2 | 149.7 | 0.253x | 1.000x | 75 | 53.8 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 5,149.7 | 5,142.8 | 5,161.7 | 6.7 | 0.323x | 1.277x | 75 | 68.7 | 8.9 | 100% |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 5,157.2 | 5,150.4 | 5,404.7 | 99.6 | 0.323x | 1.279x | 75 | 68.8 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 12,381.1 | 12,319.8 | 12,421.1 | 32.5 | 0.776x | 3.070x | 75 | 165.1 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 12,613.5 | 12,588.8 | 12,626.3 | 12.7 | 0.791x | 3.127x | 75 | 168.2 | 17.3 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,324.1 | 15,262.1 | 15,399.9 | 44.0 | 0.961x | 3.799x | 75 | 204.3 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 15,949.0 | 15,914.0 | 15,982.4 | 25.3 | 1.000x | 3.954x | 75 | 212.7 | 34.4 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 16.1 | 0.0000 | 16.1 | 16.2 | 0.0 | 0.165x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 30.7 | 0.0000 | 30.6 | 30.9 | 0.1 | 0.314x | 1.908x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.8 | 0.0001 | 97.8 | 105.0 | 2.9 | 1.000x | 6.070x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 103.4 | 0.0001 | 102.9 | 157.6 | 22.7 | 1.058x | 6.419x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 140.5 | 0.0001 | 132.2 | 144.3 | 4.5 | 1.436x | 8.719x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,863,616.8 | 2.8073 | 3,862,462.8 | 3,871,978.1 | 4,201.6 | 39501.094x | 239760.394x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,865,776.8 | 2.8089 | 3,864,355.7 | 3,871,712.7 | 3,230.7 | 39523.178x | 239894.435x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 10.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 46.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,942,717.2 | 2.8064 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,944,835.2 | 2.8084 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 5.4 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 10.3 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.3 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 46.1 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 736,023.2 | 2.8077 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 735,888.5 | 2.8072 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.4 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 34.4 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 47.3 | 0.0007 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 184,801.6 | 2.8198 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 185,053.1 | 2.8237 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 492.3 | 488.8 | 498.8 | 3.6 | 0.114x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 868.8 | 867.9 | 870.8 | 1.0 | 0.200x | 1.765x | 75 | 11.6 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,371.9 | 3,356.8 | 3,508.4 | 58.0 | 0.778x | 6.849x | 75 | 45.0 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,237.3 | 4,079.8 | 4,808.2 | 274.3 | 0.977x | 8.607x | 75 | 56.5 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,336.8 | 4,332.3 | 4,406.6 | 28.2 | 1.000x | 8.809x | 75 | 57.8 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,115.9 | 6,094.5 | 6,158.1 | 21.0 | 1.410x | 12.423x | 75 | 81.5 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,328.8 | 6,310.7 | 6,355.5 | 16.2 | 1.459x | 12.855x | 75 | 84.4 | 17.3 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,111,656.5 | 9.5270 | 13,083,420.8 | 13,188,114.4 | 36,229.7 | 0.146x | 1.000x |
| 2 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 25,436,977.5 | 18.4827 | 25,305,794.1 | 26,044,406.5 | 270,508.9 | 0.284x | 1.940x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 25,439,488.4 | 18.4846 | 25,384,436.2 | 25,860,358.3 | 172,843.9 | 0.284x | 1.940x |
| 4 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 25,467,482.8 | 18.5049 | 25,339,936.6 | 25,483,010.2 | 52,246.1 | 0.284x | 1.942x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 25,520,680.9 | 18.5436 | 25,330,925.3 | 25,866,862.7 | 185,070.8 | 0.285x | 1.946x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 89,645,403.0 | 65.1372 | 89,456,335.7 | 90,437,164.0 | 405,966.8 | 1.000x | 6.837x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 10,002,109.4 | 9.5388 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 19,403,316.5 | 18.5044 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 19,386,047.7 | 18.4880 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 19,433,816.9 | 18.5335 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 19,425,253.4 | 18.5254 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 68,224,564.7 | 65.0640 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 2,496,474.4 | 9.5233 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 4,837,158.0 | 18.4523 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 4,842,061.5 | 18.4710 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4,830,423.6 | 18.4266 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 4,821,813.2 | 18.3938 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 17,133,327.7 | 65.3585 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 625,940.8 | 9.5511 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,206,972.2 | 18.4169 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 1,205,424.6 | 18.3933 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 1,202,788.6 | 18.3531 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,203,240.3 | 18.3600 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 4,296,641.0 | 65.5615 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,186.3 | 13,148.2 | 13,216.7 | 27.3 | 0.158x | 1.000x | 75 | 175.8 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 20,804.0 | 20,751.6 | 20,855.9 | 42.1 | 0.250x | 1.578x | 75 | 277.4 | 8.9 | 100% |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 20,864.8 | 20,775.3 | 20,934.0 | 52.7 | 0.251x | 1.582x | 75 | 278.2 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 20,909.7 | 20,829.4 | 20,941.6 | 43.4 | 0.251x | 1.586x | 75 | 278.8 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 21,085.2 | 21,033.4 | 21,623.5 | 224.6 | 0.253x | 1.599x | 75 | 281.1 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 83,264.2 | 83,130.5 | 83,734.5 | 210.4 | 1.000x | 6.314x | 75 | 1,110.2 | 34.4 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,240.8 | 0.0169 | 23,212.8 | 23,259.9 | 15.5 | 1.000x | 1.000x | spread |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,301,139.6 | 2.3986 | 3,300,435.1 | 3,312,472.0 | 5,023.6 | 142.041x | 142.041x | **dominated**: `t-1m` is 99.6% of this set |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 13,401,591.7 | 9.7377 | 13,397,411.1 | 13,405,874.1 | 2,816.9 | 576.641x | 576.641x | spread |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 13,443,293.2 | 9.7680 | 13,431,092.6 | 13,499,898.6 | 25,054.2 | 578.436x | 578.436x | spread |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 13,444,931.7 | 9.7692 | 13,426,054.0 | 13,461,909.2 | 14,891.3 | 578.506x | 578.506x | spread |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 13,448,825.7 | 9.7720 | 13,415,055.5 | 13,468,689.8 | 18,725.6 | 578.674x | 578.674x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,685.5 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,288,704.7 | 3.1364 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 10,216,137.7 | 9.7429 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 10,254,203.8 | 9.7792 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 10,252,156.3 | 9.7772 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 10,257,272.5 | 9.7821 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,409.7 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,776.0 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 2,555,190.0 | 9.7473 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 2,558,301.6 | 9.7591 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 2,558,094.8 | 9.7584 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 2,560,786.8 | 9.7686 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.1 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,509.3 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 629,879.1 | 9.6112 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 632,382.3 | 9.6494 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 623,768.0 | 9.5179 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 629,690.5 | 9.6083 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,338.5 | 3,286.2 | 3,449.9 | 64.2 | 0.575x | 1.000x | 75 | 44.5 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,805.1 | 5,723.5 | 5,906.3 | 62.9 | 1.000x | 1.739x | 75 | 77.4 | 34.4 | 100% |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 10,840.2 | 10,826.8 | 10,999.1 | 65.4 | 1.867x | 3.247x | 75 | 144.5 | 18.1 | 100% |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 10,851.9 | 10,821.8 | 10,905.8 | 30.4 | 1.869x | 3.251x | 75 | 144.7 | 8.9 | 100% |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 10,864.5 | 10,818.1 | 10,871.9 | 19.7 | 1.872x | 3.254x | 75 | 144.9 | 8.9 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 10,956.9 | 10,916.6 | 10,985.1 | 27.3 | 1.887x | 3.282x | 75 | 146.1 | 17.3 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 258.8 | 0.0002 | 258.1 | 262.6 | 1.7 | 0.094x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 977.7 | 0.0007 | 974.6 | 986.9 | 4.2 | 0.354x | 3.777x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 979.1 | 0.0007 | 977.3 | 987.2 | 3.7 | 0.354x | 3.783x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,763.3 | 0.0020 | 2,747.3 | 2,792.8 | 14.8 | 1.000x | 10.677x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,885.6 | 0.0028 | 3,873.6 | 4,619.0 | 292.4 | 1.406x | 15.013x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,864,297.6 | 2.8078 | 3,863,357.1 | 3,875,975.9 | 4,789.6 | 1398.456x | 14930.646x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,865,785.0 | 2.8089 | 3,863,500.4 | 3,873,060.1 | 3,642.9 | 1398.994x | 14936.392x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 70.1 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 228.3 | 0.0002 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 230.0 | 0.0002 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 653.9 | 0.0006 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 877.4 | 0.0008 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,942,127.7 | 2.8058 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,942,212.9 | 2.8059 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 105.2 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 458.2 | 0.0017 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 456.9 | 0.0017 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,279.0 | 0.0049 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,873.9 | 0.0071 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 736,648.2 | 2.8101 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 737,081.3 | 2.8117 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 85.3 | 0.0013 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 290.6 | 0.0044 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 290.5 | 0.0044 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 831.1 | 0.0127 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,137.5 | 0.0174 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 185,521.8 | 2.8308 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 185,269.8 | 2.8270 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,321.7 | 5,132.7 | 5,597.3 | 163.0 | 0.159x | 1.000x | 75 | 71.0 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 10,632.5 | 10,605.5 | 10,661.1 | 19.6 | 0.318x | 1.998x | 75 | 141.8 | 8.9 | 100% |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 10,649.7 | 10,574.8 | 10,676.2 | 41.8 | 0.318x | 2.001x | 75 | 142.0 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 15,935.3 | 15,888.9 | 16,215.7 | 119.4 | 0.476x | 2.994x | 75 | 212.5 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 16,176.7 | 16,155.1 | 16,196.4 | 15.4 | 0.483x | 3.040x | 75 | 215.7 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33,485.1 | 33,447.6 | 33,582.3 | 53.9 | 1.000x | 6.292x | 75 | 446.5 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 42,500.9 | 42,084.8 | 43,084.4 | 344.1 | 1.269x | 7.986x | 75 | 566.7 | 30.4 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 33.3 | 0.0000 | 31.4 | 33.8 | 1.0 | 0.001x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 48.5 | 0.0000 | 47.3 | 49.5 | 0.8 | 0.002x | 1.456x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,522.1 | 0.0018 | 2,494.7 | 2,535.3 | 13.7 | 0.091x | 75.652x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 13,928.0 | 0.0101 | 13,918.0 | 13,974.4 | 20.8 | 0.504x | 417.775x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 27,657.6 | 0.0201 | 27,580.1 | 27,846.8 | 114.6 | 1.000x | 829.598x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,484,155.0 | 3.2582 | 4,480,660.9 | 4,491,520.8 | 4,198.7 | 162.131x | 134503.608x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,486,396.9 | 3.2599 | 4,480,276.6 | 4,498,113.6 | 6,700.0 | 162.212x | 134570.856x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 11.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 17.4 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,133.7 | 0.0011 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,594.6 | 0.0015 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 16,991.2 | 0.0162 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,410,773.2 | 3.2528 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,411,027.4 | 3.2530 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 15.3 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 504.3 | 0.0019 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,808.5 | 0.0374 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,120.7 | 0.0081 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 852,633.6 | 3.2525 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 853,632.8 | 3.2564 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 10.9 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 15.6 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 889.2 | 0.0136 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,528.0 | 0.0386 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 8,563.5 | 0.1307 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 218,630.2 | 3.3360 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 219,392.9 | 3.3477 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 974.9 | 971.6 | 980.2 | 3.2 | 0.307x | 1.000x | 75 | 13.0 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,433.7 | 1,427.8 | 1,448.7 | 7.5 | 0.452x | 1.471x | 75 | 19.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,079.6 | 3,036.4 | 3,207.5 | 61.1 | 0.971x | 3.159x | 75 | 41.1 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,172.3 | 3,162.7 | 3,292.8 | 49.6 | 1.000x | 3.254x | 75 | 42.3 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,805.2 | 8,711.2 | 9,628.5 | 345.8 | 2.776x | 9.032x | 75 | 117.4 | 30.4 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 27.0 | 0.0000 | 26.9 | 28.3 | 0.5 | 0.001x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,579.0 | 0.0011 | 1,573.0 | 1,591.3 | 6.2 | 0.074x | 58.437x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,948.7 | 0.0014 | 1,941.2 | 1,963.2 | 7.8 | 0.092x | 72.122x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 21,266.4 | 0.0155 | 21,161.3 | 21,375.8 | 70.6 | 1.000x | 787.073x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,283,772.5 | 3.1126 | 4,282,903.9 | 4,290,199.8 | 2,648.0 | 201.434x | 158542.908x |
| 6 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,285,766.2 | 3.1141 | 4,284,531.1 | 5,091,458.5 | 322,207.7 | 201.527x | 158616.694x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,286,372.3 | 3.1145 | 4,281,098.7 | 5,041,431.4 | 302,490.8 | 201.556x | 158639.125x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 10.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 501.8 | 0.0005 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 225.0 | 0.0002 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,218.3 | 0.0021 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,255,611.2 | 3.1048 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,254,395.1 | 3.1036 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,253,459.8 | 3.1027 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4.7 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 118.6 | 0.0005 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 49.0 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 133.7 | 0.0005 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 813,447.5 | 3.1031 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 814,112.8 | 3.1056 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 814,302.1 | 3.1063 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 11.9 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 960.4 | 0.0147 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,675.4 | 0.0256 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 18,910.9 | 0.2886 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 215,065.9 | 3.2816 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 217,307.7 | 3.3159 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 215,543.7 | 3.2889 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 76,758.0 | 0.0558 | 76,711.6 | 76,820.3 | 37.7 | 0.063x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 292,601.7 | 0.2126 | 292,416.2 | 293,102.8 | 249.8 | 0.239x | 3.812x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 292,646.0 | 0.2126 | 292,570.6 | 293,156.6 | 217.1 | 0.239x | 3.813x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,134,876.5 | 0.8246 | 1,133,682.1 | 1,153,975.3 | 7,620.5 | 0.928x | 14.785x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,222,845.7 | 0.8885 | 1,217,124.1 | 1,225,350.1 | 2,917.4 | 1.000x | 15.931x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,855,486.9 | 2.8014 | 3,334,356.0 | 3,866,372.2 | 208,796.6 | 3.153x | 50.229x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,856,595.2 | 2.8022 | 3,848,142.2 | 3,862,138.4 | 4,495.2 | 3.154x | 50.244x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 58,408.2 | 0.0557 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 228,518.7 | 0.2179 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 228,703.0 | 0.2181 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 864,092.8 | 0.8241 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 933,086.3 | 0.8899 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,936,775.4 | 2.8007 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,937,885.9 | 2.8018 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 14,607.1 | 0.0557 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 52,643.3 | 0.2008 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 52,625.6 | 0.2008 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 216,457.2 | 0.8257 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 232,123.8 | 0.8855 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 734,423.1 | 2.8016 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 735,055.1 | 2.8040 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 3,716.4 | 0.0567 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 11,341.7 | 0.1731 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 11,350.0 | 0.1732 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 54,368.5 | 0.8296 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 57,624.7 | 0.8793 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 183,755.0 | 2.8039 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 183,717.6 | 2.8033 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 833.5 | 817.8 | 867.7 | 16.7 | 0.205x | 1.000x | 75 | 11.1 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 837.4 | 823.3 | 867.7 | 18.3 | 0.205x | 1.005x | 75 | 11.2 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,807.2 | 2,778.4 | 2,976.4 | 89.5 | 0.689x | 3.368x | 75 | 37.4 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,075.2 | 4,067.7 | 4,444.4 | 145.3 | 1.000x | 4.889x | 75 | 54.3 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,600.8 | 4,518.4 | 4,722.7 | 68.6 | 1.129x | 5.520x | 75 | 61.3 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,784.7 | 4,518.0 | 4,912.8 | 143.3 | 1.174x | 5.741x | 75 | 63.8 | 18.1 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,789,624.2 | 1.3004 | 1,787,196.2 | 1,793,163.1 | 2,214.9 | 0.118x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,790,446.7 | 1.3010 | 1,787,422.3 | 1,802,571.9 | 5,505.8 | 0.118x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,128,191.0 | 1.5464 | 2,118,594.6 | 2,136,797.6 | 5,913.3 | 0.140x | 1.189x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 15,150,346.6 | 11.0084 | 15,124,920.9 | 15,187,452.8 | 24,785.4 | 1.000x | 8.466x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 18,611,391.9 | 13.5232 | 18,590,070.5 | 18,739,437.3 | 54,460.5 | 1.228x | 10.400x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 18,862,693.4 | 13.7058 | 18,840,031.1 | 18,976,659.6 | 48,009.1 | 1.245x | 10.540x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 19,104,177.5 | 13.8813 | 18,992,667.6 | 19,663,333.4 | 249,016.4 | 1.261x | 10.675x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 1,368,887.9 | 1.3055 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 1,368,435.2 | 1.3050 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,610,952.2 | 1.5363 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 11,628,427.6 | 11.0897 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 14,263,633.7 | 13.6029 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 14,385,291.4 | 13.7189 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 14,580,170.1 | 13.9047 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 338,356.8 | 1.2907 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 339,200.2 | 1.2939 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 415,597.8 | 1.5854 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,845,806.2 | 10.8559 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 3,504,517.4 | 13.3687 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 3,583,979.9 | 13.6718 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 3,652,025.4 | 13.9314 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 82,522.9 | 1.2592 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 82,709.8 | 1.2621 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 100,743.8 | 1.5372 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 677,376.7 | 10.3359 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 839,490.2 | 12.8096 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 897,594.9 | 13.6962 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 910,934.4 | 13.8998 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,482.1 | 2,476.2 | 2,513.6 | 13.7 | 0.452x | 1.000x | 75 | 33.1 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,484.1 | 2,482.9 | 2,492.1 | 3.4 | 0.452x | 1.001x | 75 | 33.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,482.3 | 3,390.8 | 3,561.0 | 62.3 | 0.634x | 1.403x | 75 | 46.4 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,490.3 | 5,449.0 | 5,499.0 | 18.0 | 1.000x | 2.212x | 75 | 73.2 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,858.8 | 5,825.5 | 6,555.7 | 284.1 | 1.067x | 2.360x | 75 | 78.1 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 19,852.9 | 19,786.9 | 19,919.0 | 45.9 | 3.616x | 7.999x | 75 | 264.7 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 20,087.9 | 20,058.1 | 21,834.7 | 700.4 | 3.659x | 8.093x | 75 | 267.8 | 17.3 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 23,144.2 | 0.0168 | 23,114.0 | 23,198.1 | 29.5 | 0.996x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 23,166.1 | 0.0168 | 23,123.5 | 23,248.0 | 52.5 | 0.997x | 1.001x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,242.8 | 0.0169 | 23,224.7 | 23,278.7 | 20.8 | 1.000x | 1.004x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,243.4 | 0.0169 | 23,228.8 | 25,906.0 | 1,066.4 | 1.000x | 1.004x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,954.9 | 0.0378 | 51,548.6 | 52,169.7 | 212.0 | 2.235x | 2.245x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 814,107.8 | 0.5915 | 813,968.4 | 816,930.0 | 1,120.8 | 35.025x | 35.175x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 814,682.8 | 0.5920 | 814,010.9 | 816,159.4 | 753.3 | 35.050x | 35.200x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 17,646.4 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 17,662.2 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,696.6 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,693.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,663.5 | 0.0378 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 620,080.6 | 0.5914 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 620,313.5 | 0.5916 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4,390.9 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 4,388.2 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,419.9 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,409.5 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,794.2 | 0.0374 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 155,159.2 | 0.5919 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 155,273.4 | 0.5923 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 1,107.0 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 1,112.1 | 0.0170 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,143.7 | 0.0175 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,138.2 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,508.6 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 38,901.3 | 0.5936 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 38,969.5 | 0.5946 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 667.1 | 664.6 | 668.4 | 1.4 | 0.258x | 1.000x | 75 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 669.1 | 664.8 | 700.6 | 13.1 | 0.259x | 1.003x | 75 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 1,300.7 | 1,298.8 | 1,306.0 | 2.5 | 0.504x | 1.950x | 75 | 17.3 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,354.5 | 1,352.4 | 1,358.5 | 2.1 | 0.524x | 2.030x | 75 | 18.1 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,277.3 | 2,271.3 | 2,472.5 | 80.6 | 0.882x | 3.414x | 75 | 30.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,582.7 | 2,581.7 | 2,612.8 | 14.6 | 1.000x | 3.871x | 75 | 34.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,031.9 | 2,822.9 | 3,197.0 | 143.2 | 1.174x | 4.545x | 75 | 40.4 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 407,488.7 | 0.2961 | 407,448.7 | 408,044.4 | 224.4 | 0.400x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 483,151.7 | 0.3511 | 482,871.3 | 486,633.1 | 1,489.1 | 0.475x | 1.186x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 483,331.5 | 0.3512 | 483,155.1 | 483,836.5 | 247.4 | 0.475x | 1.186x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,012,634.2 | 0.7358 | 1,010,832.0 | 1,015,461.7 | 1,698.9 | 0.995x | 2.485x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,017,809.1 | 0.7395 | 1,015,898.4 | 1,019,696.4 | 1,273.6 | 1.000x | 2.498x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,034,760.3 | 1.4785 | 2,034,351.7 | 2,038,315.5 | 1,451.8 | 1.999x | 4.993x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 2,034,784.8 | 1.4785 | 2,034,136.9 | 2,040,434.8 | 2,343.8 | 1.999x | 4.993x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 310,296.3 | 0.2959 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 368,308.0 | 0.3512 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 368,351.6 | 0.3513 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 777,399.7 | 0.7414 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 776,432.5 | 0.7405 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 1,550,217.8 | 1.4784 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 1,549,781.0 | 1.4780 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 77,676.8 | 0.2963 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 91,814.6 | 0.3502 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 91,860.2 | 0.3504 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 191,525.2 | 0.7306 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 193,387.6 | 0.7377 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 387,389.8 | 1.4778 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 387,501.0 | 1.4782 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 19,590.5 | 0.2989 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 23,074.0 | 0.3521 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 23,044.7 | 0.3516 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 46,071.8 | 0.7030 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 47,518.4 | 0.7251 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 97,297.9 | 1.4846 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 97,293.0 | 1.4846 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,106.7 | 1,102.9 | 1,110.0 | 2.3 | 0.314x | 1.000x | 75 | 14.8 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,107.7 | 1,105.5 | 1,111.4 | 2.3 | 0.314x | 1.001x | 75 | 14.8 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 2,784.7 | 2,775.1 | 2,802.9 | 9.7 | 0.789x | 2.516x | 75 | 37.1 | 17.3 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,866.9 | 2,842.7 | 2,874.1 | 10.9 | 0.812x | 2.591x | 75 | 38.2 | 18.1 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,272.4 | 3,262.6 | 4,071.7 | 319.8 | 0.927x | 2.957x | 75 | 43.6 | 30.4 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,364.8 | 3,344.3 | 3,413.9 | 24.1 | 0.953x | 3.041x | 75 | 44.9 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,529.1 | 3,494.0 | 3,552.3 | 22.2 | 1.000x | 3.189x | 75 | 47.1 | 34.4 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.8 | 0.0 | 0.203x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 0.0000 | 18.8 | 19.8 | 0.4 | 0.204x | 1.007x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 81.7 | 0.0001 | 81.3 | 120.6 | 15.2 | 0.885x | 4.358x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 92.4 | 0.0001 | 92.3 | 92.5 | 0.0 | 1.000x | 4.927x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 144.0 | 0.0001 | 142.0 | 150.7 | 3.0 | 1.559x | 7.680x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,069,161.0 | 2.9567 | 4,065,874.3 | 4,073,821.3 | 2,602.5 | 44047.324x | 217034.037x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,069,526.5 | 2.9570 | 4,067,823.4 | 4,070,503.6 | 1,017.5 | 44051.281x | 217053.535x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 6.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 44.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,098,782.4 | 2.9552 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,098,435.3 | 2.9549 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 48.4 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 774,611.1 | 2.9549 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 775,477.6 | 2.9582 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 6.4 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 30.8 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.1 | 0.0008 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 194,543.4 | 2.9685 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 194,768.3 | 2.9719 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 492.2 | 491.1 | 495.2 | 1.4 | 0.166x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 494.8 | 492.8 | 498.4 | 2.1 | 0.167x | 1.005x | 75 | 6.6 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,742.5 | 2,724.2 | 2,784.6 | 22.0 | 0.925x | 5.572x | 75 | 36.6 | 30.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,964.6 | 2,940.5 | 2,993.8 | 18.0 | 1.000x | 6.023x | 75 | 39.5 | 34.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,016.1 | 2,910.2 | 3,308.9 | 140.4 | 1.017x | 6.128x | 75 | 40.2 | 40.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,403.4 | 6,359.2 | 6,422.9 | 21.9 | 2.160x | 13.009x | 75 | 85.4 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,430.9 | 6,414.0 | 6,529.3 | 42.0 | 2.169x | 13.065x | 75 | 85.7 | 17.3 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 511,780.6 | 0.3719 | 502,082.3 | 518,020.7 | 5,713.5 | 0.154x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 730,648.8 | 0.5309 | 730,478.9 | 1,150,804.0 | 168,020.8 | 0.220x | 1.428x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 731,770.2 | 0.5317 | 731,118.9 | 737,121.1 | 2,243.5 | 0.221x | 1.430x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,143,025.6 | 2.2838 | 3,135,065.3 | 3,164,269.1 | 11,602.0 | 0.948x | 6.141x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,316,797.1 | 2.4100 | 3,295,097.3 | 3,389,636.2 | 33,969.5 | 1.000x | 6.481x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,180,219.3 | 3.0374 | 4,163,278.2 | 4,188,703.6 | 8,654.8 | 1.260x | 8.168x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,198,086.5 | 3.0504 | 4,195,117.0 | 4,205,180.4 | 3,374.4 | 1.266x | 8.203x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 391,236.3 | 0.3731 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 564,430.7 | 0.5383 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 564,649.8 | 0.5385 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,397,249.4 | 2.2862 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,520,617.0 | 2.4038 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,184,249.7 | 3.0367 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,197,376.1 | 3.0493 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 96,555.6 | 0.3683 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 135,144.1 | 0.5155 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 135,402.3 | 0.5165 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 602,096.1 | 2.2968 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 633,885.2 | 2.4181 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 796,813.5 | 3.0396 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 800,184.2 | 3.0525 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 23,746.1 | 0.3623 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 31,106.5 | 0.4746 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 31,240.6 | 0.4767 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 151,118.0 | 2.3059 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 158,274.1 | 2.4151 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 199,534.7 | 3.0447 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 200,658.1 | 3.0618 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 776.7 | 775.1 | 778.0 | 1.1 | 0.194x | 1.000x | 75 | 10.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 778.2 | 776.8 | 784.1 | 2.6 | 0.194x | 1.002x | 75 | 10.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,873.5 | 2,816.5 | 3,149.4 | 118.3 | 0.716x | 3.700x | 75 | 38.3 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,014.0 | 3,958.3 | 4,104.4 | 57.3 | 1.000x | 5.168x | 75 | 53.5 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,678.4 | 4,600.9 | 4,715.4 | 41.6 | 1.166x | 6.023x | 75 | 62.4 | 18.1 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,764.6 | 4,446.5 | 4,772.4 | 128.2 | 1.187x | 6.134x | 75 | 63.5 | 17.3 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 30.0 | 0.0000 | 30.0 | 33.5 | 1.4 | 0.115x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 30.2 | 0.0000 | 30.1 | 30.2 | 0.0 | 0.115x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.9 | 0.0001 | 125.3 | 136.9 | 3.9 | 0.493x | 4.294x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 245.3 | 0.0002 | 243.6 | 246.1 | 0.9 | 0.938x | 8.171x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 261.4 | 0.0002 | 258.6 | 262.3 | 1.4 | 1.000x | 8.706x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,845,825.0 | 2.0678 | 2,845,290.9 | 2,884,651.2 | 15,303.8 | 10886.078x | 94777.357x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 2,846,428.6 | 2.0682 | 2,845,914.2 | 2,851,964.4 | 2,225.3 | 10888.387x | 94797.461x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,167,252.3 | 2.0669 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,168,023.2 | 2.0676 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 9.9 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 43.1 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 542,374.2 | 2.0690 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 542,149.5 | 2.0681 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 10.4 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 42.5 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 191.4 | 0.0029 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 198.7 | 0.0030 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 136,087.7 | 2.0765 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 136,168.3 | 2.0778 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 839.4 | 837.4 | 841.6 | 1.4 | 0.169x | 1.000x | 75 | 11.2 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 850.7 | 843.0 | 860.8 | 6.4 | 0.172x | 1.013x | 75 | 11.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,219.1 | 3,189.0 | 3,720.7 | 199.1 | 0.649x | 3.835x | 75 | 42.9 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,120.3 | 4,110.1 | 4,126.5 | 5.4 | 0.831x | 4.909x | 75 | 54.9 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,128.4 | 4,120.5 | 4,139.4 | 6.1 | 0.833x | 4.918x | 75 | 55.0 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,959.0 | 4,930.1 | 4,986.6 | 19.2 | 1.000x | 5.908x | 75 | 66.1 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,239.9 | 5,211.4 | 5,701.0 | 189.0 | 1.057x | 6.242x | 75 | 69.9 | 30.4 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 18.7 | 0.0000 | 18.7 | 18.8 | 0.0 | 0.075x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 30.3 | 0.0000 | 30.2 | 30.3 | 0.0 | 0.121x | 1.616x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128.9 | 0.0001 | 126.0 | 144.5 | 7.2 | 0.514x | 6.879x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 194.1 | 0.0001 | 191.9 | 218.3 | 9.9 | 0.773x | 10.356x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 251.0 | 0.0002 | 250.2 | 256.7 | 2.4 | 1.000x | 13.393x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,659,912.9 | 2.6593 | 3,658,350.7 | 3,671,351.1 | 4,804.0 | 14578.898x | 195249.101x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,661,361.5 | 2.6604 | 3,658,009.7 | 3,668,018.2 | 4,214.3 | 14584.668x | 195326.379x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,786,019.3 | 2.6570 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,789,643.6 | 2.6604 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 9.8 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 43.1 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 697,099.5 | 2.6592 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 697,261.0 | 2.6598 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 6.8 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 43.0 | 0.0007 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 139.8 | 0.0021 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 188.4 | 0.0029 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 175,185.1 | 2.6731 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 174,987.5 | 2.6701 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 493.6 | 492.4 | 496.5 | 1.5 | 0.102x | 1.000x | 75 | 6.6 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 808.7 | 807.8 | 809.5 | 0.6 | 0.167x | 1.638x | 75 | 10.8 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,218.8 | 3,116.9 | 3,272.9 | 53.0 | 0.666x | 6.522x | 75 | 42.9 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,582.1 | 4,533.2 | 5,174.9 | 245.7 | 0.948x | 9.284x | 75 | 61.1 | 30.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,802.2 | 4,796.5 | 4,806.2 | 3.2 | 0.993x | 9.730x | 75 | 64.0 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,812.7 | 4,806.5 | 4,819.2 | 4.1 | 0.996x | 9.751x | 75 | 64.2 | 18.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,833.8 | 4,814.9 | 4,875.8 | 20.5 | 1.000x | 9.794x | 75 | 64.5 | 34.4 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 23,156.9 | 0.0168 | 23,117.9 | 23,329.8 | 77.6 | 0.997x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 23,166.7 | 0.0168 | 23,142.1 | 23,239.0 | 34.3 | 0.997x | 1.000x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,237.7 | 0.0169 | 23,225.5 | 23,329.3 | 38.2 | 1.000x | 1.003x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,264.9 | 0.0169 | 23,240.8 | 23,268.0 | 11.8 | 1.001x | 1.005x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,046.1 | 0.0291 | 40,002.1 | 40,176.4 | 65.6 | 1.723x | 1.729x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 407,415.6 | 0.2960 | 407,342.9 | 408,748.6 | 538.1 | 17.533x | 17.594x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 407,560.4 | 0.2961 | 407,480.0 | 408,291.4 | 308.0 | 17.539x | 17.600x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 17,655.6 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 17,659.8 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,689.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,706.7 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,515.2 | 0.0291 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 310,239.5 | 0.2959 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 310,455.2 | 0.2961 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4,392.4 | 0.0168 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 4,388.7 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,413.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,420.6 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,596.8 | 0.0290 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 77,620.7 | 0.2961 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 77,620.8 | 0.2961 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 1,106.8 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 1,112.4 | 0.0170 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.7 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,139.7 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,968.0 | 0.0300 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 19,511.1 | 0.2977 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 19,495.6 | 0.2975 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,824.7 | 2,603.4 | 2,868.0 | 97.6 | 1.000x | 1.000x | 75 | 37.7 | 34.4 | 100% |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,857.5 | 2,392.8 | 3,311.4 | 408.0 | 1.012x | 1.012x | 75 | 38.1 | 30.4 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,954.5 | 2,886.8 | 3,110.9 | 96.1 | 1.046x | 1.046x | 75 | 39.4 | 40.4 | 100% |

### `negation-scope-lookbehind-var` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,588.5 | 0.0375 | 51,453.5 | 51,633.3 | 65.0 | 0.001x | 1.000x | 3 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 48,746,190.7 | 35.4194 | 48,512,426.3 | 49,830,534.8 | 466,084.7 | 1.000x | 944.904x | 3 | 100% |

#### `negation-scope-lookbehind-var` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,262.0 | 0.0374 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 37,150,551.2 | 35.4295 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,822.3 | 0.0375 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 9,203,447.3 | 35.1084 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,516.1 | 0.0384 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 2,400,179.0 | 36.6238 |

### `negation-scope-lookbehind-var` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,119.1 | 2,903.3 | 3,338.9 | 168.9 | 0.340x | 1.000x | 75 | 41.6 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,184.3 | 9,118.4 | 9,435.0 | 111.2 | 1.000x | 2.944x | 75 | 122.5 | 34.4 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 52,006.5 | 0.0378 | 51,639.2 | 52,337.3 | 269.0 | 0.019x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,105,602.6 | 1.5299 | 2,087,963.4 | 2,133,077.5 | 18,485.1 | 0.784x | 40.487x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,685,331.9 | 1.9512 | 2,684,786.5 | 2,685,986.6 | 418.9 | 1.000x | 51.635x |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 7,798,118.9 | 5.6662 | 7,790,698.3 | 7,827,975.6 | 13,612.8 | 2.904x | 149.945x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 7,806,477.4 | 5.6723 | 7,798,899.2 | 7,813,450.8 | 4,721.6 | 2.907x | 150.106x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 7,807,349.7 | 5.6729 | 7,798,246.3 | 7,819,582.8 | 7,391.1 | 2.907x | 150.122x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,814,250.3 | 5.6779 | 7,793,241.1 | 7,829,126.3 | 12,465.2 | 2.910x | 150.255x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,669.7 | 0.0378 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,609,287.0 | 1.5347 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,057,363.9 | 1.9621 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 5,941,217.2 | 5.6660 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5,949,472.1 | 5.6739 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 5,943,003.0 | 5.6677 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 5,950,497.4 | 5.6748 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,835.9 | 0.0375 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 402,915.4 | 1.5370 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 508,962.3 | 1.9415 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 1,484,310.6 | 5.6622 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 1,486,640.8 | 5.6711 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,489,064.6 | 5.6803 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,485,995.8 | 5.6686 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,516.2 | 0.0384 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 95,215.2 | 1.4529 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 119,191.7 | 1.8187 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 370,845.8 | 5.6587 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 372,321.2 | 5.6812 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 372,814.2 | 5.6887 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 372,521.8 | 5.6842 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,232.4 | 3,102.1 | 3,324.3 | 85.7 | 0.618x | 1.000x | 75 | 43.1 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,231.5 | 5,204.9 | 5,257.8 | 19.5 | 1.000x | 1.618x | 75 | 69.8 | 34.4 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 6,937.2 | 6,911.7 | 7,571.7 | 256.5 | 1.326x | 2.146x | 75 | 92.5 | 30.4 | 100% |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 9,078.4 | 9,069.9 | 9,118.2 | 18.1 | 1.735x | 2.809x | 75 | 121.0 | 17.3 | 100% |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 9,268.7 | 9,252.0 | 9,296.4 | 19.0 | 1.772x | 2.867x | 75 | 123.6 | 8.9 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,283.3 | 9,279.9 | 9,313.2 | 12.6 | 1.774x | 2.872x | 75 | 123.8 | 18.1 | 100% |
| 7 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 9,304.4 | 9,280.4 | 9,324.5 | 17.1 | 1.779x | 2.878x | 75 | 124.1 | 8.9 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.7 | 0.2 | 0.161x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 27.8 | 0.0000 | 27.6 | 29.5 | 0.7 | 0.295x | 1.832x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.3 | 0.0001 | 80.2 | 91.4 | 4.4 | 0.852x | 5.291x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 94.2 | 144.8 | 20.2 | 1.000x | 6.207x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 124.1 | 0.0001 | 123.0 | 152.3 | 11.4 | 1.317x | 8.173x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,068,098.9 | 2.9559 | 4,066,453.5 | 4,094,024.6 | 10,405.6 | 43183.104x | 268024.853x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,075,160.6 | 2.9610 | 4,065,832.4 | 4,133,943.6 | 25,356.4 | 43258.065x | 268490.111x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 9.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,098,235.5 | 2.9547 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,097,046.7 | 2.9536 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 9.3 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.7 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 775,474.7 | 2.9582 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 774,192.3 | 2.9533 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 9.2 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.3 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 194,969.9 | 2.9750 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 194,646.7 | 2.9701 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 470.6 | 469.3 | 474.2 | 1.8 | 0.000x | 1.000x | spread | 75 | 6.3 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 847.1 | 834.4 | 850.7 | 5.7 | 0.000x | 1.800x | spread | 75 | 11.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,240.3 | 13,222.2 | 13,672.8 | 173.9 | 0.000x | 28.136x | spread | 75 | 176.5 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,113,242.7 | 3,103,890.7 | 3,125,062.7 | 8,232.5 | 0.091x | 6615.701x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 41,509.9 | 40.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 9,233,657.0 | 9,227,985.8 | 9,236,055.7 | 2,914.3 | 0.271x | 19621.701x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 123,115.4 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,240,914.6 | 9,233,143.2 | 9,254,568.0 | 7,752.4 | 0.272x | 19637.124x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 123,212.2 | 18.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 34,025,624.1 | 34,003,935.4 | 34,195,102.5 | 82,077.0 | 1.000x | 72305.115x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 453,675.0 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.2 | 0.0 | 0.161x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 28.5 | 0.0000 | 28.5 | 28.7 | 0.1 | 0.303x | 1.879x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 81.0 | 0.0001 | 80.8 | 92.9 | 4.8 | 0.860x | 5.341x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 94.1 | 94.2 | 0.0 | 1.000x | 6.210x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 124.2 | 0.0001 | 120.2 | 129.1 | 2.9 | 1.319x | 8.189x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,864,125.9 | 2.8077 | 3,862,983.8 | 3,866,301.6 | 1,286.7 | 41033.773x | 254820.817x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,866,744.1 | 2.8096 | 3,862,688.9 | 3,873,923.5 | 3,789.8 | 41061.577x | 254993.476x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.0 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,942,852.3 | 2.8065 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,943,820.8 | 2.8074 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 9.5 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 41.0 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 736,482.6 | 2.8095 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 736,366.9 | 2.8090 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 9.5 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.5 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.0 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 184,915.6 | 2.8216 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 185,112.7 | 2.8246 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 481.2 | 479.9 | 481.2 | 0.6 | 0.000x | 1.000x | spread | 75 | 6.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 892.2 | 890.5 | 895.0 | 1.7 | 0.000x | 1.854x | spread | 75 | 11.9 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 15,202.4 | 15,145.8 | 15,902.2 | 286.2 | 0.000x | 31.593x | spread | 75 | 202.7 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,895,514.6 | 3,887,027.4 | 3,903,410.1 | 5,891.8 | 0.097x | 8095.595x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 51,940.2 | 40.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 9,976,542.2 | 9,966,951.9 | 9,980,523.0 | 4,550.2 | 0.250x | 20733.087x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 133,020.6 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,984,573.4 | 9,969,651.9 | 10,000,208.6 | 9,960.3 | 0.250x | 20749.778x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 133,127.6 | 18.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 39,975,369.4 | 39,647,313.1 | 40,435,170.8 | 273,984.8 | 1.000x | 83076.161x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 533,004.9 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,212,527.9 | 1.6076 | 2,209,209.6 | 2,232,888.8 | 10,232.8 | 0.109x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 6,629,620.6 | 4.8171 | 6,592,300.9 | 7,274,319.5 | 259,147.5 | 0.326x | 2.996x |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,679,320.2 | 4.8533 | 6,581,427.3 | 7,218,087.5 | 231,393.8 | 0.329x | 3.019x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,089,853.0 | 5.1516 | 6,592,797.4 | 7,552,837.9 | 334,732.3 | 0.349x | 3.204x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 7,525,843.5 | 5.4683 | 6,948,695.4 | 7,633,181.1 | 244,496.0 | 0.370x | 3.401x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,329,662.6 | 14.7717 | 20,269,516.6 | 20,396,375.1 | 40,808.9 | 1.000x | 9.188x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,691,442.6 | 1.6131 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 5,086,488.6 | 4.8509 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 5,120,186.7 | 4.8830 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 5,523,980.3 | 5.2681 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5,855,910.5 | 5.5846 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,606,478.0 | 14.8835 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 419,310.5 | 1.5995 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 1,249,493.2 | 4.7664 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,250,092.8 | 4.7687 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,255,159.0 | 4.7881 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 1,340,985.8 | 5.1155 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,807,524.4 | 14.5246 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 101,854.8 | 1.5542 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 311,165.8 | 4.7480 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 309,580.7 | 4.7238 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 312,603.8 | 4.7700 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 314,174.5 | 4.7939 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 915,617.4 | 13.9712 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,545.7 | 4,519.9 | 4,704.0 | 68.3 | 0.259x | 1.000x | 75 | 60.6 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 7,357.3 | 7,093.0 | 7,617.3 | 167.6 | 0.420x | 1.619x | 75 | 98.1 | 8.9 | 100% |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 7,378.2 | 7,147.8 | 7,622.4 | 152.2 | 0.421x | 1.623x | 75 | 98.4 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 7,665.5 | 7,156.8 | 7,680.3 | 204.9 | 0.437x | 1.686x | 75 | 102.2 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,694.1 | 7,572.3 | 7,841.2 | 97.1 | 0.439x | 1.693x | 75 | 102.6 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 17,534.3 | 17,496.5 | 17,734.1 | 85.0 | 1.000x | 3.857x | 75 | 233.8 | 34.4 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 221.7 | 0.0002 | 220.9 | 223.2 | 0.8 | 0.043x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 222.3 | 0.0002 | 221.6 | 223.5 | 0.6 | 0.043x | 1.003x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,132.0 | 0.0008 | 1,130.0 | 1,134.7 | 1.6 | 0.219x | 5.106x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,172.1 | 0.0038 | 5,158.0 | 5,211.6 | 20.2 | 1.000x | 23.330x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 12,106.1 | 0.0088 | 12,090.6 | 12,134.5 | 16.6 | 2.341x | 54.607x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,684,824.0 | 2.6774 | 3,682,041.3 | 3,690,920.6 | 3,308.7 | 712.445x | 16621.122x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,691,855.6 | 2.6825 | 3,677,710.6 | 3,694,470.2 | 6,675.7 | 713.804x | 16652.839x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 58.2 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 58.1 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 131.0 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 637.8 | 0.0006 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,280.7 | 0.0012 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,802,101.5 | 2.6723 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,813,120.7 | 2.6828 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 94.7 | 0.0004 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 95.3 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 596.7 | 0.0023 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 2,638.5 | 0.0101 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,972.6 | 0.0228 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 704,813.5 | 2.6887 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 701,965.9 | 2.6778 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 68.8 | 0.0011 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 69.1 | 0.0011 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 405.9 | 0.0062 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,893.4 | 0.0289 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,865.6 | 0.0742 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 177,183.1 | 2.7036 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 176,643.1 | 2.6954 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,323.2 | 8,289.4 | 8,370.7 | 30.8 | 0.231x | 1.000x | 75 | 111.0 | 40.4 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 12,361.7 | 12,348.9 | 12,713.7 | 141.8 | 0.342x | 1.485x | 75 | 164.8 | 8.9 | 100% |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 12,363.2 | 12,344.0 | 12,420.4 | 25.8 | 0.342x | 1.485x | 75 | 164.8 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 14,475.2 | 14,458.9 | 14,646.8 | 69.5 | 0.401x | 1.739x | 75 | 193.0 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 14,773.7 | 14,732.2 | 14,774.1 | 19.4 | 0.409x | 1.775x | 75 | 197.0 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 36,107.0 | 35,957.5 | 36,313.1 | 129.7 | 1.000x | 4.338x | 75 | 481.4 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 95,501.0 | 94,995.6 | 99,228.5 | 1,574.2 | 2.645x | 11.474x | 75 | 1,273.3 | 30.4 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 460,903.3 | 0.3349 | 458,315.3 | 467,298.6 | 2,981.1 | 0.110x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,205,744.4 | 3.0559 | 4,190,894.0 | 4,227,034.9 | 12,261.6 | 1.000x | 9.125x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 9,758,197.6 | 7.0904 | 9,729,834.9 | 9,826,299.0 | 31,806.4 | 2.320x | 21.172x |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 9,877,485.3 | 7.1771 | 9,808,855.2 | 10,047,638.9 | 82,956.7 | 2.349x | 21.431x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 10,059,067.3 | 7.3090 | 10,006,597.0 | 10,100,860.7 | 34,568.8 | 2.392x | 21.825x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 10,075,056.7 | 7.3206 | 10,034,361.8 | 10,086,609.6 | 19,038.5 | 2.396x | 21.859x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 354,469.1 | 0.3380 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,222,438.0 | 3.0732 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 7,466,247.1 | 7.1204 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 7,565,966.3 | 7.2155 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 7,695,556.6 | 7.3391 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 7,705,233.5 | 7.3483 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 84,999.4 | 0.3242 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 779,383.7 | 2.9731 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 1,822,193.5 | 6.9511 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 1,851,750.2 | 7.0639 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,887,680.5 | 7.2009 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,906,860.6 | 7.2741 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 21,429.7 | 0.3270 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 199,603.8 | 3.0457 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 451,692.6 | 6.8923 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 463,034.7 | 7.0653 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 463,183.3 | 7.0676 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 462,548.3 | 7.0579 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,317.1 | 3,229.2 | 3,490.4 | 106.7 | 0.396x | 1.000x | 75 | 44.2 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 8,370.4 | 8,299.1 | 8,577.6 | 101.5 | 1.000x | 2.523x | 75 | 111.6 | 34.4 | 100% |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 11,131.2 | 10,685.3 | 11,234.3 | 204.0 | 1.330x | 3.356x | 75 | 148.4 | 8.9 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 11,335.1 | 11,258.2 | 11,480.0 | 73.9 | 1.354x | 3.417x | 75 | 151.1 | 18.1 | 100% |
| 5 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 11,406.2 | 11,348.5 | 11,452.7 | 35.0 | 1.363x | 3.439x | 75 | 152.1 | 8.9 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 11,475.8 | 11,438.2 | 11,593.3 | 53.2 | 1.371x | 3.460x | 75 | 153.0 | 17.3 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91,706.5 | 0.0666 | 91,687.8 | 92,376.7 | 268.9 | 0.041x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 393,633.9 | 0.2860 | 393,468.8 | 393,818.1 | 131.2 | 0.176x | 4.292x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 393,753.9 | 0.2861 | 393,635.7 | 393,882.8 | 97.5 | 0.176x | 4.294x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,182,520.9 | 1.5858 | 2,166,544.3 | 2,186,450.1 | 7,059.5 | 0.977x | 23.799x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,233,113.3 | 1.6226 | 2,227,974.7 | 2,235,032.1 | 2,816.5 | 1.000x | 24.351x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,061,202.6 | 2.9509 | 4,052,828.1 | 4,073,747.0 | 7,126.6 | 1.819x | 44.285x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,064,526.8 | 2.9533 | 4,055,245.8 | 4,068,277.4 | 4,721.9 | 1.820x | 44.321x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 70,166.1 | 0.0669 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 302,116.9 | 0.2881 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 302,063.5 | 0.2881 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,671,958.0 | 1.5945 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,711,559.9 | 1.6323 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,094,161.9 | 2.9508 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,097,134.5 | 2.9537 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 17,397.9 | 0.0664 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 74,512.0 | 0.2842 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 74,511.2 | 0.2842 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 414,660.2 | 1.5818 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 421,609.2 | 1.6083 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 775,333.6 | 2.9577 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 773,871.8 | 2.9521 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 4,148.9 | 0.0633 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 17,099.6 | 0.2609 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 17,238.0 | 0.2630 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 95,585.7 | 1.4585 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 98,386.7 | 1.5013 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 192,776.8 | 2.9415 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 192,540.8 | 2.9379 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 779.5 | 772.5 | 794.6 | 7.3 | 0.211x | 1.000x | 75 | 10.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 781.2 | 771.4 | 794.3 | 9.9 | 0.211x | 1.002x | 75 | 10.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,822.7 | 2,768.2 | 3,121.6 | 126.2 | 0.762x | 3.621x | 75 | 37.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,703.0 | 3,595.6 | 3,729.1 | 51.8 | 1.000x | 4.750x | 75 | 49.4 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,521.2 | 4,477.3 | 4,569.2 | 31.9 | 1.221x | 5.800x | 75 | 60.3 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,617.5 | 4,353.8 | 4,714.2 | 150.4 | 1.247x | 5.924x | 75 | 61.6 | 18.1 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,238.0 | 0.0169 | 23,223.2 | 23,268.6 | 17.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,252.3 | 0.0169 | 23,229.1 | 23,335.8 | 40.0 | 1.001x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,177.5 | 0.0292 | 40,096.1 | 40,344.8 | 91.6 | 1.729x | 1.729x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,491,353.6 | 3.2635 | 4,488,321.2 | 4,502,529.6 | 4,962.3 | 193.276x | 193.276x |
| 5 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,493,504.7 | 3.2650 | 4,484,995.4 | 4,532,849.3 | 16,839.1 | 193.369x | 193.369x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,494,626.2 | 3.2658 | 4,483,186.5 | 4,519,438.4 | 12,095.5 | 193.417x | 193.417x |
| 7 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,683,683.2 | 3.4032 | 4,677,685.7 | 4,695,932.2 | 6,303.2 | 201.553x | 201.553x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,694.1 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,704.0 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,532.9 | 0.0291 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,414,586.9 | 3.2564 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,414,992.1 | 3.2568 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,412,940.9 | 3.2548 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,568,244.6 | 3.4029 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,404.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,418.7 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,615.8 | 0.0291 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 853,668.9 | 3.2565 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 855,384.2 | 3.2630 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 854,346.8 | 3.2591 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 891,301.6 | 3.4000 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,133.2 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,133.8 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,964.5 | 0.0300 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 222,764.5 | 3.3991 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 223,128.4 | 3.4047 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 225,442.8 | 3.4400 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 223,871.1 | 3.4160 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,585.2 | 3,504.7 | 3,840.9 | 116.1 | 0.501x | 1.000x | 75 | 47.8 | 40.4 | 100% |
| 2 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,898.1 | 6,855.1 | 7,034.4 | 71.6 | 0.965x | 1.924x | 75 | 92.0 | 17.3 | 100% |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 6,969.6 | 6,912.0 | 7,054.1 | 46.2 | 0.975x | 1.944x | 75 | 92.9 | 8.9 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,152.0 | 7,106.6 | 7,167.1 | 21.4 | 1.000x | 1.995x | 75 | 95.4 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 7,155.6 | 7,011.5 | 7,320.2 | 114.5 | 1.001x | 1.996x | 75 | 95.4 | 18.1 | 100% |
| 6 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 7,178.0 | 6,906.6 | 7,310.5 | 145.3 | 1.004x | 2.002x | 75 | 95.7 | 8.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,229.8 | 0.0169 | 23,196.0 | 23,251.0 | 19.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 39,993.9 | 0.0291 | 39,889.5 | 40,218.9 | 124.6 | 1.722x | 1.722x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,633,754.3 | 3.3669 | 4,628,456.8 | 4,643,316.8 | 4,865.8 | 199.475x | 199.475x |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,644,013.0 | 3.3744 | 4,635,412.6 | 4,649,425.8 | 4,600.3 | 199.916x | 199.916x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,650,573.7 | 3.3791 | 4,639,324.2 | 4,654,185.1 | 5,635.3 | 200.199x | 200.199x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,650,851.0 | 3.3794 | 4,632,399.4 | 4,663,714.6 | 12,627.1 | 200.211x | 200.211x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,672.3 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,463.7 | 0.0291 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,529,277.9 | 3.3658 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,535,399.3 | 3.3716 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,541,751.7 | 3.3777 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,544,943.4 | 3.3807 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,423.7 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,568.8 | 0.0289 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 882,876.4 | 3.3679 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 885,232.2 | 3.3769 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 885,012.8 | 3.3761 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 884,980.5 | 3.3759 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,135.1 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,964.8 | 0.0300 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 222,872.7 | 3.4008 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 222,472.2 | 3.3947 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 222,237.7 | 3.3911 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 222,354.8 | 3.3929 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,274.2 | 3,177.9 | 3,313.0 | 57.3 | 0.754x | 1.000x | 75 | 43.7 | 40.4 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,343.7 | 4,283.8 | 4,474.8 | 67.5 | 1.000x | 1.327x | 75 | 57.9 | 34.4 | 100% |
| 3 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,002.7 | 5,978.8 | 6,103.4 | 44.7 | 1.382x | 1.833x | 75 | 80.0 | 18.1 | 100% |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 6,037.7 | 5,966.7 | 6,172.3 | 68.5 | 1.390x | 1.844x | 75 | 80.5 | 8.9 | 100% |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 6,129.5 | 6,122.6 | 6,137.0 | 5.2 | 1.411x | 1.872x | 75 | 81.7 | 8.9 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,281.4 | 6,263.2 | 6,339.5 | 27.8 | 1.446x | 1.918x | 75 | 83.8 | 17.3 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 15.2 | 0.0000 | 15.1 | 15.3 | 0.0 | 0.043x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 126.8 | 0.0001 | 122.7 | 132.4 | 3.3 | 0.356x | 8.348x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 253.4 | 0.0002 | 243.9 | 256.5 | 5.1 | 0.712x | 16.686x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 356.1 | 0.0003 | 354.5 | 358.8 | 1.5 | 1.000x | 23.446x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,252,796.9 | 2.3635 | 3,251,998.2 | 3,263,344.9 | 4,593.8 | 9134.067x | 214157.689x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,254,903.8 | 2.3650 | 3,253,984.1 | 3,263,642.6 | 4,370.9 | 9139.984x | 214296.405x |
| 7 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 3,255,807.7 | 2.3657 | 3,252,238.9 | 3,262,034.1 | 3,354.5 | 9142.522x | 214355.916x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 42.4 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.1 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 118.3 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,477,640.8 | 2.3629 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,479,355.7 | 2.3645 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 2,477,985.2 | 2.3632 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 5.1 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 42.5 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.2 | 0.0003 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 118.9 | 0.0005 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 619,408.6 | 2.3629 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 620,089.5 | 2.3655 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 620,527.0 | 2.3671 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.0 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.8 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 84.9 | 0.0013 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 118.9 | 0.0018 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 155,709.1 | 2.3759 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 155,822.5 | 2.3777 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 156,541.1 | 2.3886 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 427.8 | 426.7 | 446.7 | 7.5 | 0.000x | 1.000x | spread | 75 | 5.7 | 8.9 | 100% |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,638.5 | 12,948.0 | 13,659.8 | 341.3 | 0.000x | 31.879x | spread | 75 | 181.8 | 30.4 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,390,462.6 | 3,381,540.0 | 3,417,180.1 | 12,931.8 | 0.100x | 7924.931x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 45,206.2 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 8,954,916.9 | 8,937,896.3 | 8,964,864.6 | 9,116.5 | 0.264x | 20931.391x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,398.9 | 18.1 | 100% |
| 5 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 8,965,504.0 | 8,958,886.0 | 8,995,654.1 | 13,805.7 | 0.265x | 20956.137x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,540.1 | 8.9 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 8,997,242.1 | 8,991,413.7 | 9,010,177.9 | 6,507.7 | 0.265x | 21030.322x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 119,963.2 | 17.3 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 33,894,166.4 | 33,845,989.1 | 33,977,605.1 | 46,589.8 | 1.000x | 79224.860x | **dominated**: `rd-trim-near-miss` is 100.0% of this set | 75 | 451,922.2 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 480,467.4 | 0.3491 | 479,368.1 | 481,800.7 | 783.8 | 0.472x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 480,493.7 | 0.3491 | 436,276.7 | 487,659.5 | 19,458.1 | 0.472x | 1.000x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 480,739.0 | 0.3493 | 480,320.7 | 486,507.5 | 2,314.6 | 0.473x | 1.001x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,017,026.6 | 0.7390 | 1,015,014.3 | 1,020,194.6 | 1,692.2 | 1.000x | 2.117x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,017,211.2 | 0.7391 | 1,016,790.2 | 1,017,792.3 | 323.3 | 1.000x | 2.117x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,661,665.6 | 2.6606 | 3,660,901.7 | 3,663,810.7 | 1,062.8 | 3.600x | 7.621x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,664,092.1 | 2.6624 | 3,663,452.3 | 3,693,198.1 | 11,692.4 | 3.603x | 7.626x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 366,487.4 | 0.3495 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 334,475.0 | 0.3190 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 366,693.9 | 0.3497 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 776,660.9 | 0.7407 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 777,018.6 | 0.7410 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,788,929.0 | 2.6597 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,790,195.0 | 2.6609 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 91,164.1 | 0.3478 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 114,760.0 | 0.4378 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 91,440.2 | 0.3488 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 194,288.9 | 0.7412 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 194,401.7 | 0.7416 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 697,631.2 | 2.6613 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 698,344.7 | 2.6640 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 22,582.6 | 0.3446 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 30,747.9 | 0.4692 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 22,570.6 | 0.3444 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 46,082.2 | 0.7032 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 46,100.1 | 0.7034 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 175,097.0 | 2.6718 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 175,475.6 | 2.6775 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,251.0 | 1,249.0 | 1,251.4 | 0.9 | 0.362x | 1.000x | 75 | 16.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,251.7 | 1,249.1 | 1,252.5 | 1.3 | 0.362x | 1.001x | 75 | 16.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,120.5 | 3,109.4 | 3,816.6 | 276.2 | 0.902x | 2.494x | 75 | 41.6 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,422.4 | 3,421.4 | 3,503.3 | 31.6 | 0.989x | 2.736x | 75 | 45.6 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,459.6 | 3,416.1 | 3,607.6 | 65.9 | 1.000x | 2.765x | 75 | 46.1 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,943.6 | 4,938.8 | 4,947.4 | 3.0 | 1.429x | 3.952x | 75 | 65.9 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,060.7 | 5,037.3 | 5,068.7 | 13.0 | 1.463x | 4.045x | 75 | 67.5 | 17.3 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 20.0 | 0.0000 | 19.9 | 20.3 | 0.1 | 0.129x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 20.1 | 0.0000 | 19.9 | 20.5 | 0.2 | 0.130x | 1.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 117.3 | 0.0001 | 116.5 | 123.1 | 2.4 | 0.758x | 5.869x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 154.7 | 0.0001 | 152.1 | 170.6 | 8.1 | 1.000x | 7.743x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 167.8 | 0.0001 | 167.3 | 174.6 | 2.8 | 1.084x | 8.394x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 2,440,259.7 | 1.7731 | 2,439,980.3 | 3,142,560.7 | 280,540.1 | 15769.378x | 122098.920x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,448,611.5 | 1.7792 | 2,441,689.5 | 2,572,702.0 | 52,300.9 | 15823.348x | 122516.803x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 37.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 1,857,811.0 | 1.7717 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 1,863,205.2 | 1.7769 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 38.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 30.7 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.0 | 0.0001 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 465,142.5 | 1.7744 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 467,489.9 | 1.7833 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 8.1 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 8.1 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 41.3 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 93.3 | 0.0014 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 113.7 | 0.0017 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 117,503.0 | 1.7930 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 116,570.5 | 1.7787 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 560.7 | 560.5 | 565.2 | 1.8 | 0.198x | 1.000x | 75 | 7.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 563.6 | 559.7 | 958.3 | 157.5 | 0.199x | 1.005x | 75 | 7.5 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,809.2 | 2,800.1 | 3,197.9 | 177.0 | 0.993x | 5.010x | 75 | 37.5 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,830.2 | 2,769.1 | 2,834.9 | 24.7 | 1.000x | 5.048x | 75 | 37.7 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,168.4 | 3,147.8 | 3,974.4 | 325.5 | 1.120x | 5.651x | 75 | 42.2 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,565.5 | 4,065.0 | 4,670.2 | 265.0 | 1.613x | 8.143x | 75 | 60.9 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,717.8 | 4,609.5 | 4,946.0 | 127.2 | 1.667x | 8.414x | 75 | 62.9 | 17.3 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 263,510.2 | 0.1915 | 263,410.0 | 264,235.1 | 307.7 | 0.310x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 263,619.4 | 0.1915 | 263,421.5 | 264,445.3 | 384.4 | 0.310x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 395,185.4 | 0.2871 | 391,923.5 | 415,245.6 | 8,387.9 | 0.464x | 1.500x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 770,173.9 | 0.5596 | 764,904.0 | 793,611.2 | 10,324.2 | 0.905x | 2.923x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 851,233.8 | 0.6185 | 832,894.7 | 859,398.3 | 9,423.7 | 1.000x | 3.230x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 955,143.1 | 0.6940 | 954,623.7 | 960,090.5 | 2,079.5 | 1.122x | 3.625x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 955,325.0 | 0.6941 | 954,240.0 | 990,032.9 | 13,963.3 | 1.122x | 3.625x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 202,474.6 | 0.1931 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 202,479.7 | 0.1931 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 302,608.1 | 0.2886 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 594,301.4 | 0.5668 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 651,279.8 | 0.6211 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 727,241.0 | 0.6936 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 728,025.1 | 0.6943 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 48,651.9 | 0.1856 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 48,683.4 | 0.1857 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 73,504.6 | 0.2804 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 140,223.4 | 0.5349 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 158,303.6 | 0.6039 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 181,517.9 | 0.6924 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 181,468.9 | 0.6922 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 12,377.8 | 0.1889 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 12,396.9 | 0.1892 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 19,242.1 | 0.2936 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 37,005.0 | 0.5647 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 42,170.1 | 0.6435 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 45,981.8 | 0.7016 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 45,844.3 | 0.6995 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 689.8 | 683.2 | 705.2 | 8.2 | 0.245x | 1.000x | 75 | 9.2 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 710.3 | 695.3 | 713.2 | 6.7 | 0.252x | 1.030x | 75 | 9.5 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 1,276.7 | 1,271.4 | 1,278.2 | 2.5 | 0.453x | 1.851x | 75 | 17.0 | 17.3 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,332.7 | 1,329.5 | 1,334.1 | 2.0 | 0.473x | 1.932x | 75 | 17.8 | 18.1 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,396.7 | 2,394.1 | 2,427.1 | 13.5 | 0.851x | 3.474x | 75 | 32.0 | 30.4 | 100% |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,787.1 | 2,773.0 | 3,005.0 | 86.7 | 0.990x | 4.040x | 75 | 37.2 | 40.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,815.2 | 2,742.1 | 2,921.6 | 69.6 | 1.000x | 4.081x | 75 | 37.5 | 34.4 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,983,449.3 | 1.4412 | 1,981,109.6 | 1,983,924.2 | 1,069.8 | 0.278x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,196,737.5 | 3.0494 | 4,196,447.8 | 4,199,448.2 | 1,205.4 | 0.589x | 2.116x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,198,921.6 | 3.0510 | 4,194,758.7 | 4,201,999.5 | 2,446.1 | 0.589x | 2.117x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,720,534.9 | 3.4300 | 4,699,195.5 | 4,744,680.8 | 19,216.8 | 0.662x | 2.380x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,723,124.6 | 3.4319 | 4,696,329.7 | 4,747,684.2 | 16,368.5 | 0.663x | 2.381x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 6,207,305.8 | 4.5103 | 6,190,032.8 | 6,216,321.1 | 8,544.6 | 0.871x | 3.130x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,128,347.8 | 5.1795 | 7,083,949.5 | 7,164,913.2 | 28,873.7 | 1.000x | 3.594x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,518,907.7 | 1.4485 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,197,402.4 | 3.0493 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,199,884.8 | 3.0516 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,582,653.9 | 3.4167 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,599,003.6 | 3.4323 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,703,205.7 | 4.4853 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 5,392,917.9 | 5.1431 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 375,627.1 | 1.4329 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 800,551.3 | 3.0539 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 800,894.0 | 3.0552 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 897,466.3 | 3.4236 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 899,439.8 | 3.4311 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,198,818.0 | 4.5731 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,383,127.6 | 5.2762 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 88,388.9 | 1.3487 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 198,871.5 | 3.0345 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 198,639.8 | 3.0310 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 228,977.7 | 3.4939 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 228,113.2 | 3.4807 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 305,282.0 | 4.6582 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 354,463.7 | 5.4087 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,446.9 | 2,441.6 | 2,451.8 | 3.8 | 0.319x | 1.000x | 75 | 32.6 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,453.6 | 2,449.5 | 2,461.6 | 4.6 | 0.320x | 1.003x | 75 | 32.7 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,385.1 | 3,306.2 | 3,416.4 | 37.4 | 0.442x | 1.383x | 75 | 45.1 | 17.3 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,420.2 | 3,410.5 | 3,487.9 | 28.3 | 0.446x | 1.398x | 75 | 45.6 | 40.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,421.9 | 3,408.9 | 3,428.2 | 7.3 | 0.446x | 1.398x | 75 | 45.6 | 18.1 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,078.3 | 7,063.5 | 7,539.3 | 185.5 | 0.924x | 2.893x | 75 | 94.4 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,664.2 | 7,636.8 | 8,474.2 | 321.2 | 1.000x | 3.132x | 75 | 102.2 | 34.4 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,456,363.4 | 1.7848 | 2,438,855.7 | 2,477,195.3 | 13,373.4 | 0.130x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,465,677.2 | 1.7916 | 2,455,005.5 | 2,487,748.1 | 12,655.8 | 0.131x | 1.004x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,476,937.3 | 3.2530 | 4,396,172.3 | 4,564,955.5 | 53,447.5 | 0.237x | 1.823x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,960,875.3 | 7.2377 | 9,919,626.7 | 10,060,366.3 | 46,817.7 | 0.528x | 4.055x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 10,054,962.0 | 7.3060 | 10,012,898.7 | 10,336,762.0 | 117,166.2 | 0.533x | 4.093x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 18,862,675.2 | 13.7058 | 18,462,520.6 | 18,996,780.5 | 226,398.0 | 1.000x | 7.679x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 21,848,582.0 | 15.8754 | 21,824,088.1 | 21,916,181.7 | 31,431.8 | 1.158x | 8.895x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 1,885,171.6 | 1.7978 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 1,882,847.9 | 1.7956 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,428,091.4 | 3.2693 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 7,579,562.9 | 7.2284 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 7,674,607.9 | 7.3191 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 14,472,591.7 | 13.8021 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 16,751,286.8 | 15.9753 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 457,159.0 | 1.7439 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 467,072.0 | 1.7817 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 842,909.3 | 3.2154 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,893,121.7 | 7.2217 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,903,793.7 | 7.2624 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,536,128.7 | 13.4893 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,109,805.8 | 15.6777 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 113,714.7 | 1.7351 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 113,093.7 | 1.7257 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 204,260.2 | 3.1168 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 467,055.3 | 7.1267 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 476,724.6 | 7.2742 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 853,954.9 | 13.0303 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 996,303.4 | 15.2024 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,411.5 | 1,398.8 | 1,417.0 | 6.2 | 0.142x | 1.000x | 75 | 18.8 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,415.5 | 1,407.4 | 1,425.0 | 5.7 | 0.142x | 1.003x | 75 | 18.9 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,666.6 | 3,661.0 | 3,700.6 | 14.7 | 0.369x | 2.598x | 75 | 48.9 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 7,327.1 | 7,318.2 | 7,344.1 | 10.2 | 0.737x | 5.191x | 75 | 97.7 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,434.1 | 7,416.5 | 7,446.8 | 10.2 | 0.748x | 5.267x | 75 | 99.1 | 17.3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,943.9 | 9,912.4 | 10,194.8 | 106.3 | 1.000x | 7.045x | 75 | 132.6 | 34.4 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 12,446.2 | 12,376.3 | 12,921.7 | 217.8 | 1.252x | 8.818x | 75 | 165.9 | 30.4 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 23,152.7 | 0.0168 | 23,150.3 | 23,175.3 | 10.3 | 0.997x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 23,172.6 | 0.0168 | 23,142.7 | 23,322.5 | 63.0 | 0.998x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,229.7 | 0.0169 | 23,220.0 | 23,357.2 | 50.9 | 1.000x | 1.003x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,287.6 | 0.0169 | 23,256.4 | 23,306.2 | 17.2 | 1.002x | 1.006x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,850.2 | 0.0377 | 51,685.7 | 52,279.1 | 210.6 | 2.232x | 2.239x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 814,178.4 | 0.5916 | 814,100.6 | 816,293.4 | 1,041.2 | 35.049x | 35.166x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 814,593.5 | 0.5919 | 814,050.0 | 816,741.3 | 1,048.6 | 35.067x | 35.184x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 17,656.2 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 17,650.4 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,690.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,729.1 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,544.8 | 0.0377 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 620,124.8 | 0.5914 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 620,069.7 | 0.5913 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 4,389.5 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4,428.6 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,411.8 | 0.0168 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,422.1 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,790.9 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 155,090.9 | 0.5916 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 155,163.0 | 0.5919 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 1,113.6 | 0.0170 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 1,108.9 | 0.0169 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,130.9 | 0.0173 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,137.2 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,519.5 | 0.0384 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 38,980.2 | 0.5948 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 39,016.8 | 0.5953 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 662.8 | 661.2 | 689.4 | 10.9 | 0.244x | 1.000x | 75 | 8.8 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 680.4 | 666.7 | 689.1 | 9.9 | 0.250x | 1.027x | 75 | 9.1 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 1,299.3 | 1,295.1 | 1,305.7 | 3.5 | 0.478x | 1.961x | 75 | 17.3 | 17.3 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,357.0 | 1,355.5 | 1,362.3 | 2.4 | 0.499x | 2.048x | 75 | 18.1 | 18.1 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,290.0 | 2,256.0 | 3,162.6 | 360.4 | 0.843x | 3.455x | 75 | 30.5 | 30.4 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,717.4 | 2,584.1 | 2,815.8 | 91.5 | 1.000x | 4.100x | 75 | 36.2 | 34.4 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,999.4 | 2,744.8 | 3,352.7 | 206.5 | 1.104x | 4.526x | 75 | 40.0 | 40.4 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 23,146.1 | 0.0168 | 23,107.9 | 23,152.8 | 17.1 | 0.997x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 23,162.8 | 0.0168 | 23,151.0 | 23,199.9 | 16.6 | 0.998x | 1.001x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,214.4 | 0.0169 | 23,191.0 | 23,344.0 | 54.7 | 1.000x | 1.003x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,343.9 | 0.0170 | 23,295.3 | 23,445.5 | 52.5 | 1.006x | 1.009x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 40,217.6 | 0.0292 | 40,037.7 | 40,315.2 | 104.4 | 1.732x | 1.738x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,915,919.8 | 2.8453 | 3,915,329.9 | 3,925,884.8 | 4,056.4 | 168.685x | 169.183x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,917,365.9 | 2.8464 | 3,916,191.1 | 3,938,026.3 | 8,349.7 | 168.747x | 169.245x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 17,644.1 | 0.0168 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 17,666.6 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,659.1 | 0.0168 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,750.7 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 30,730.6 | 0.0293 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,981,872.0 | 2.8437 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,982,814.3 | 2.8446 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 4,388.4 | 0.0167 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 4,385.0 | 0.0167 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,420.4 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,428.3 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 7,530.0 | 0.0287 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 746,283.0 | 2.8468 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 746,603.0 | 2.8481 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 1,107.1 | 0.0169 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 1,112.8 | 0.0170 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,138.4 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,141.0 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 1,978.9 | 0.0302 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 187,454.4 | 2.8603 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 187,614.5 | 2.8628 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 727.5 | 722.4 | 738.4 | 6.1 | 0.231x | 1.000x | 75 | 9.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 743.6 | 735.4 | 749.5 | 5.9 | 0.236x | 1.022x | 75 | 9.9 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,839.0 | 2,816.0 | 2,855.6 | 12.7 | 0.902x | 3.902x | 75 | 37.9 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,845.8 | 2,780.9 | 3,353.3 | 231.7 | 0.904x | 3.912x | 75 | 37.9 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,147.0 | 3,088.8 | 3,325.4 | 85.6 | 1.000x | 4.326x | 75 | 42.0 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,304.7 | 5,212.3 | 5,599.6 | 138.8 | 1.686x | 7.292x | 75 | 70.7 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,585.7 | 5,370.6 | 5,670.2 | 113.8 | 1.775x | 7.678x | 75 | 74.5 | 17.3 | 100% |

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 10,425,108.0 | 7.5750 | 10,415,343.2 | 10,527,435.4 | 42,536.1 | 0.002x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 259,150,804.0 | 188.3013 | 253,743,791.0 | 264,815,748.0 | 3,655,172.5 | 0.057x | 24.858x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,514,881,080.0 | 3280.5532 | 4,511,883,135.0 | 4,520,715,052.0 | 3,119,805.8 | 1.000x | 433.078x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 10,046,355,001.0 | 7299.7720 | 10,033,667,338.0 | 10,084,410,115.0 | 17,585,039.0 | 2.225x | 963.669x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 7,942,077.2 | 7.5742 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 196,725,747.5 | 187.6123 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,432,521,569.0 | 3273.5077 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 7,642,894,838.0 | 7288.8325 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 1,987,280.4 | 7.5809 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 49,474,310.0 | 188.7295 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 863,848,207.0 | 3295.3194 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,920,216,335.0 | 7325.0440 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 497,000.0 | 7.5836 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 12,268,893.0 | 187.2085 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 217,769,561.0 | 3322.8998 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 483,867,260.0 | 7383.2285 |

- not ranked: `pcrec_a770139e_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670132 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_a770139e_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665080 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_a770139e_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665080 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,018.8 | 2,012.1 | 2,033.2 | 7.0 | 0.001x | 1.000x | 75 | 26.9 | 8.9 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 88,206.3 | 86,270.0 | 88,708.9 | 937.6 | 0.050x | 43.692x | 75 | 1,176.1 | 40.4 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,750,980.9 | 1,750,262.0 | 1,751,305.2 | 375.5 | 1.000x | 867.329x | 75 | 23,346.4 | 34.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,958,526.1 | 3,909,930.7 | 4,013,833.0 | 36,965.7 | 2.261x | 1960.813x | 75 | 52,780.3 | 30.4 | 100% |

- not ranked: `pcrec_a770139e_auto-caps-simdna` — did-not-compile (pcrec: pattern too large: 670132 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_a770139e_vm-caps-simdna` — did-not-compile (pcrec: pattern too large: 665080 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))
- not ranked: `pcrec_a770139e_vm-in-caps-simdna` — did-not-compile (pcrec: pattern too large: 665080 bytes of emitted code (limit 500000), which gcc cannot compile in reasonable time. A repeat's body is replicated and counts MULTIPLY through nesting -- lower a count, try --unroll=1, or raise --max-emit-code-bytes (pattern offset 0))

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 19.8 | 0.0000 | 19.6 | 20.0 | 0.2 | 0.203x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 33.1 | 0.0000 | 32.9 | 33.4 | 0.2 | 0.338x | 1.671x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.6 | 110.3 | 5.0 | 1.000x | 4.937x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 116.6 | 0.0001 | 81.5 | 126.6 | 19.2 | 1.192x | 5.888x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 174.9 | 0.0001 | 151.7 | 175.3 | 9.3 | 1.789x | 8.832x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,276,574.4 | 3.1074 | 4,267,597.9 | 4,280,729.4 | 5,214.7 | 43752.424x | 216021.634x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,285,218.4 | 3.1137 | 4,273,479.8 | 4,294,894.2 | 7,336.2 | 43840.858x | 216458.268x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 6.6 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 11.0 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 37.9 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 55.6 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,256,693.4 | 3.1058 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,260,102.2 | 3.1091 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.6 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 11.0 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 37.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 63.1 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 813,530.5 | 3.1034 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 814,428.4 | 3.1068 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 6.5 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 11.0 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 39.0 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 204,181.3 | 3.1156 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 205,668.1 | 3.1382 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 592.4 | 588.5 | 625.8 | 14.0 | 0.168x | 1.000x | 75 | 7.9 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 982.0 | 980.7 | 999.0 | 7.0 | 0.278x | 1.658x | 75 | 13.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,263.8 | 3,056.3 | 3,433.6 | 141.8 | 0.923x | 5.509x | 75 | 43.5 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,535.6 | 3,524.6 | 3,536.8 | 4.6 | 1.000x | 5.968x | 75 | 47.1 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,795.1 | 3,727.7 | 4,492.0 | 283.9 | 1.073x | 6.406x | 75 | 50.6 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,324.7 | 6,311.7 | 6,334.4 | 8.6 | 1.789x | 10.676x | 75 | 84.3 | 17.3 | 100% |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,324.7 | 6,304.5 | 6,328.2 | 8.9 | 1.789x | 10.676x | 75 | 84.3 | 18.1 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,022,098.6 | 2.9225 | 4,020,812.9 | 4,038,906.7 | 6,793.4 | 0.203x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,030,440.3 | 2.9286 | 4,025,839.8 | 4,046,359.5 | 7,222.7 | 0.203x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,760,420.5 | 3.4590 | 4,720,910.0 | 4,886,668.8 | 68,697.2 | 0.240x | 1.184x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 19,807,034.2 | 14.3920 | 19,698,062.2 | 19,870,715.9 | 66,274.9 | 1.000x | 4.925x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 23,307,778.8 | 16.9356 | 23,252,521.2 | 23,411,549.4 | 51,558.0 | 1.177x | 5.795x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 23,665,758.6 | 17.1958 | 23,651,524.9 | 23,689,126.0 | 15,049.9 | 1.195x | 5.884x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 27,306,139.6 | 19.8409 | 27,252,933.3 | 27,426,661.2 | 74,654.1 | 1.379x | 6.789x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,079,860.0 | 2.9372 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,085,943.3 | 2.9430 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,648,821.5 | 3.4798 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,176,917.7 | 14.4738 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 17,741,424.6 | 16.9195 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 18,012,723.4 | 17.1783 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 20,893,195.4 | 19.9253 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 758,390.8 | 2.8930 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 759,841.3 | 2.8986 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 894,895.3 | 3.4138 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,723,503.6 | 14.2040 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 4,425,655.9 | 16.8825 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 4,507,006.1 | 17.1929 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,129,382.9 | 19.5670 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 184,042.5 | 2.8083 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 184,319.7 | 2.8125 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 217,340.4 | 3.3164 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 901,062.9 | 13.7491 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,123,275.4 | 17.1398 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,142,501.9 | 17.4332 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,241,249.0 | 18.9400 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,509.7 | 2,482.2 | 2,586.3 | 40.6 | 0.210x | 1.000x | 75 | 33.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,524.2 | 2,491.6 | 2,604.9 | 42.2 | 0.212x | 1.006x | 75 | 33.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,247.8 | 4,077.9 | 4,515.1 | 167.5 | 0.356x | 1.693x | 75 | 56.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 11,930.4 | 11,917.0 | 12,007.9 | 34.5 | 1.000x | 4.754x | 75 | 159.1 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 16,435.0 | 16,285.1 | 16,519.2 | 89.5 | 1.378x | 6.548x | 75 | 219.1 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 18,314.2 | 18,287.5 | 18,409.1 | 41.5 | 1.535x | 7.297x | 75 | 244.2 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 18,627.5 | 18,592.3 | 18,650.8 | 20.3 | 1.561x | 7.422x | 75 | 248.4 | 17.3 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 3,984,108.3 | 2.8949 | 3,977,056.0 | 3,992,583.6 | 5,911.9 | 0.193x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 3,990,438.3 | 2.8995 | 3,983,988.5 | 4,119,297.8 | 52,743.4 | 0.193x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,787,801.8 | 3.4789 | 4,715,663.1 | 4,883,608.9 | 55,695.9 | 0.232x | 1.202x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,669,190.5 | 15.0184 | 20,463,615.0 | 21,383,631.7 | 332,619.1 | 1.000x | 5.188x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 22,242,282.8 | 16.1614 | 22,214,077.9 | 22,310,617.0 | 36,478.5 | 1.076x | 5.583x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 23,205,821.8 | 16.8616 | 23,116,901.4 | 23,313,368.8 | 66,899.0 | 1.123x | 5.825x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 23,413,994.8 | 17.0128 | 23,287,935.1 | 23,740,362.6 | 172,439.7 | 1.133x | 5.877x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,052,740.4 | 2.9113 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,057,011.7 | 2.9154 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,665,928.1 | 3.4961 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 15,838,258.2 | 15.1045 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,044,377.4 | 16.2548 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 17,672,659.7 | 16.8540 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 17,884,876.6 | 17.0563 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 749,422.4 | 2.8588 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 751,783.8 | 2.8678 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 903,839.4 | 3.4479 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 3,890,962.5 | 14.8428 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,187,288.9 | 15.9732 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 4,408,384.9 | 16.8167 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 4,434,151.5 | 16.9149 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 181,307.0 | 2.7665 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 181,564.2 | 2.7705 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 221,484.2 | 3.3796 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 939,969.8 | 14.3428 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,012,041.1 | 15.4425 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,118,711.8 | 17.0702 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,116,029.5 | 17.0293 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,476.4 | 2,468.7 | 2,557.5 | 38.4 | 0.203x | 1.000x | 75 | 33.0 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,556.0 | 2,461.5 | 2,574.4 | 40.4 | 0.209x | 1.032x | 75 | 34.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,146.7 | 4,078.2 | 4,580.9 | 179.4 | 0.340x | 1.674x | 75 | 55.3 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 12,206.1 | 12,141.1 | 12,217.6 | 29.0 | 1.000x | 4.929x | 75 | 162.7 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 13,874.3 | 13,741.8 | 14,189.2 | 151.7 | 1.137x | 5.603x | 75 | 185.0 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 17,905.5 | 17,854.8 | 18,223.3 | 135.1 | 1.467x | 7.230x | 75 | 238.7 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 18,047.0 | 17,860.1 | 20,239.2 | 901.5 | 1.479x | 7.288x | 75 | 240.6 | 17.3 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,008,804.3 | 0.7330 | 1,008,359.5 | 1,017,389.7 | 3,436.4 | 0.487x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,009,215.2 | 0.7333 | 1,008,225.9 | 1,010,164.9 | 798.1 | 0.487x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,449,818.5 | 1.0535 | 1,446,924.9 | 1,454,534.3 | 2,571.3 | 0.700x | 1.437x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,071,041.1 | 1.5048 | 2,061,918.5 | 2,090,422.0 | 9,725.1 | 1.000x | 2.053x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,853,300.1 | 2.7998 | 3,841,783.2 | 4,903,298.0 | 420,748.5 | 1.861x | 3.820x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 46,653,312.3 | 33.8987 | 46,645,014.0 | 46,763,064.7 | 44,984.7 | 22.527x | 46.246x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 46,736,253.7 | 33.9590 | 46,611,984.7 | 46,781,947.3 | 60,288.1 | 22.567x | 46.328x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 772,300.0 | 0.7365 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 772,334.2 | 0.7366 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,106,018.4 | 1.0548 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,585,961.1 | 1.5125 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 2,953,625.2 | 2.8168 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 35,524,921.8 | 33.8792 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 35,578,294.2 | 33.9301 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 188,549.7 | 0.7193 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 188,476.0 | 0.7190 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 274,750.9 | 1.0481 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 387,079.3 | 1.4766 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 718,614.9 | 2.7413 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 8,897,299.8 | 33.9405 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 8,910,872.0 | 33.9923 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 47,729.6 | 0.7283 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 47,702.8 | 0.7279 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 69,072.9 | 1.0540 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 98,000.6 | 1.4954 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 181,060.0 | 2.7628 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 2,235,720.8 | 34.1144 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 2,233,201.0 | 34.0759 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,954.2 | 1,952.7 | 1,966.4 | 5.5 | 0.396x | 1.000x | 75 | 26.1 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,958.6 | 1,952.5 | 1,968.6 | 6.1 | 0.397x | 1.002x | 75 | 26.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,185.1 | 4,093.4 | 4,418.8 | 109.0 | 0.847x | 2.142x | 75 | 55.8 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,938.3 | 4,890.4 | 4,940.9 | 19.2 | 1.000x | 2.527x | 75 | 65.8 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 48,969.7 | 48,891.0 | 49,001.2 | 37.8 | 9.916x | 25.058x | 75 | 652.9 | 18.1 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 49,150.0 | 49,117.2 | 49,491.4 | 139.9 | 9.953x | 25.150x | 75 | 655.3 | 17.3 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 928,957.6 | 0.6750 | 927,913.5 | 931,480.5 | 1,189.8 | 0.440x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 931,208.3 | 0.6766 | 928,439.8 | 936,867.1 | 2,845.7 | 0.441x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,442,083.7 | 1.0478 | 1,441,378.5 | 1,448,881.2 | 3,525.7 | 0.683x | 1.552x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,111,987.7 | 1.5346 | 2,104,629.4 | 2,132,996.9 | 10,474.1 | 1.000x | 2.274x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 8,795,923.3 | 6.3912 | 8,750,426.3 | 8,851,875.6 | 32,363.8 | 4.165x | 9.469x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 23,030,277.0 | 16.7340 | 22,994,405.1 | 23,061,888.1 | 22,259.7 | 10.905x | 24.792x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 23,115,237.2 | 16.7957 | 22,965,332.9 | 49,483,085.9 | 10,569,536.6 | 10.945x | 24.883x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 710,714.9 | 0.6778 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 712,084.4 | 0.6791 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,099,749.4 | 1.0488 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,619,412.0 | 1.5444 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 6,762,335.8 | 6.4491 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 17,540,414.7 | 16.7278 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 17,597,369.3 | 16.7822 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 174,081.1 | 0.6641 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 174,287.0 | 0.6649 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 273,600.3 | 1.0437 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 394,629.6 | 1.5054 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,620,181.0 | 6.1805 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 4,382,750.3 | 16.7189 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 4,411,799.1 | 16.8297 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 44,080.8 | 0.6726 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 44,061.9 | 0.6723 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 68,700.2 | 1.0483 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 99,248.9 | 1.5144 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 415,827.8 | 6.3450 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,100,007.0 | 16.7848 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,106,068.8 | 16.8773 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,850.7 | 1,846.9 | 1,855.4 | 3.1 | 0.002x | 1.000x | spread | 75 | 24.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,851.9 | 1,849.2 | 1,862.5 | 5.5 | 0.002x | 1.001x | spread | 75 | 24.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 14,952.3 | 14,723.6 | 15,350.1 | 220.4 | 0.014x | 8.079x | spread | 75 | 199.4 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 104,871.2 | 104,816.5 | 104,887.4 | 26.7 | 0.100x | 56.667x | **dominated**: `waf-sleep` is 96.0% of this set | 75 | 1,398.3 | 40.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 114,178.1 | 114,045.8 | 114,363.1 | 102.1 | 0.109x | 61.696x | spread | 75 | 1,522.4 | 18.1 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 114,418.8 | 114,203.1 | 114,666.2 | 176.0 | 0.109x | 61.826x | spread | 75 | 1,525.6 | 17.3 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,045,384.5 | 1,037,774.2 | 1,107,117.1 | 25,649.9 | 1.000x | 564.869x | **dominated**: `waf-sleep` is 99.6% of this set | 75 | 13,938.5 | 34.4 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 3,987,494.3 | 2.8973 | 3,987,045.3 | 3,994,479.6 | 3,009.5 | 0.054x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 3,988,987.3 | 2.8984 | 3,986,121.1 | 3,990,405.9 | 1,615.6 | 0.054x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,319,504.7 | 4.5918 | 6,307,496.2 | 6,328,377.8 | 7,660.1 | 0.086x | 1.585x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 30,190,616.4 | 21.9368 | 30,086,109.2 | 30,583,026.4 | 177,326.5 | 0.410x | 7.571x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 40,051,375.3 | 29.1017 | 40,017,606.4 | 40,129,929.9 | 39,411.1 | 0.544x | 10.044x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 40,277,665.9 | 29.2661 | 40,066,281.9 | 40,921,355.1 | 319,709.3 | 0.547x | 10.101x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 73,681,100.2 | 53.5374 | 73,571,742.2 | 74,819,146.2 | 469,548.0 | 1.000x | 18.478x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,036,349.9 | 2.8957 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,036,477.2 | 2.8958 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 4,802,529.0 | 4.5800 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 22,912,127.7 | 21.8507 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 30,545,529.3 | 29.1305 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 30,690,968.9 | 29.2692 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 56,068,438.8 | 53.4710 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 761,287.5 | 2.9041 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 760,814.5 | 2.9023 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,209,442.4 | 4.6137 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,756,851.2 | 21.9606 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 7,610,341.1 | 29.0311 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 7,660,020.3 | 29.2207 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 13,979,687.5 | 53.3283 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 189,982.6 | 2.8989 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 190,413.7 | 2.9055 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 305,205.9 | 4.6571 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,499,558.4 | 22.8814 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,895,222.0 | 28.9188 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,911,492.1 | 29.1671 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 3,654,289.0 | 55.7600 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 3,586.5 | 3,564.8 | 3,625.2 | 19.5 | 0.393x | 1.000x | 75 | 47.8 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 3,752.7 | 3,734.9 | 3,787.1 | 20.5 | 0.411x | 1.046x | 75 | 50.0 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,132.3 | 7,079.6 | 7,770.8 | 263.8 | 0.781x | 1.989x | 75 | 95.1 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 8,929.1 | 8,853.9 | 8,995.1 | 47.0 | 0.978x | 2.490x | 75 | 119.1 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 9,134.2 | 9,114.4 | 9,150.9 | 13.1 | 1.000x | 2.547x | 75 | 121.8 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 38,479.4 | 38,411.5 | 38,786.4 | 144.1 | 4.213x | 10.729x | 75 | 513.1 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 38,517.8 | 38,315.2 | 38,555.7 | 90.1 | 4.217x | 10.740x | 75 | 513.6 | 17.3 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,249.3 | 0.0169 | 23,242.5 | 23,277.4 | 13.2 | 1.000x | 1.000x | spread |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,338.3 | 0.0170 | 23,288.1 | 23,524.8 | 81.2 | 1.004x | 1.004x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,947,563.9 | 2.1417 | 2,945,603.9 | 2,949,678.6 | 1,466.2 | 126.781x | 126.781x | **dominated**: `t-1m` is 99.6% of this set |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 3,470,134.4 | 2.5214 | 3,466,692.9 | 3,481,530.7 | 5,098.8 | 149.258x | 149.258x | spread |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 3,471,678.0 | 2.5226 | 3,469,341.5 | 3,495,389.0 | 9,764.0 | 149.324x | 149.324x | spread |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 19,563,739.6 | 14.2152 | 18,739,131.4 | 19,636,317.9 | 341,032.3 | 841.477x | 841.477x | spread |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 20,427,146.8 | 14.8425 | 19,637,753.1 | 20,631,527.3 | 356,509.1 | 878.614x | 878.614x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,695.1 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,764.4 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,935,205.7 | 2.7992 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 2,644,685.0 | 2.5222 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 2,644,809.3 | 2.5223 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 14,956,280.8 | 14.2634 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 15,686,892.3 | 14.9602 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,425.1 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,438.3 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,768.6 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 662,117.3 | 2.5258 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 664,918.0 | 2.5365 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 3,728,280.3 | 14.2223 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 3,890,631.1 | 14.8416 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,139.0 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,139.4 | 0.0174 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,586.2 | 0.0395 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 164,415.5 | 2.5088 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 165,412.9 | 2.5240 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 875,232.1 | 13.3550 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 909,438.4 | 13.8769 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,643.9 | 2,643.7 | 2,653.0 | 3.6 | 0.663x | 1.000x | 75 | 35.3 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,646.4 | 2,640.6 | 2,663.1 | 7.7 | 0.663x | 1.001x | 75 | 35.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,303.3 | 3,134.5 | 3,814.9 | 241.3 | 0.828x | 1.249x | 75 | 44.0 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,989.5 | 3,966.6 | 4,024.6 | 22.8 | 1.000x | 1.509x | 75 | 53.2 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,810.4 | 5,739.5 | 6,445.4 | 262.6 | 1.456x | 2.198x | 75 | 77.5 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 22,969.3 | 22,958.0 | 23,508.6 | 261.3 | 5.757x | 8.688x | 75 | 306.3 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 23,704.5 | 23,695.5 | 23,730.7 | 12.6 | 5.942x | 8.966x | 75 | 316.1 | 17.3 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 91,325.3 | 0.0664 | 91,282.2 | 91,632.8 | 156.5 | 0.419x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 211,881.9 | 0.1540 | 207,439.4 | 212,102.6 | 2,179.1 | 0.972x | 2.320x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 217,909.0 | 0.1583 | 216,134.1 | 220,853.1 | 1,573.5 | 1.000x | 2.386x |
| 4 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,009,346.3 | 2.9132 | 4,007,837.4 | 4,011,094.6 | 1,174.0 | 18.399x | 43.902x |
| 5 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,205,867.9 | 3.0560 | 4,202,262.4 | 4,209,133.0 | 2,673.9 | 19.301x | 46.054x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 9,315,481.0 | 6.7687 | 9,309,541.3 | 9,370,808.2 | 22,611.8 | 42.749x | 102.003x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,343,953.5 | 6.7894 | 9,325,188.0 | 9,359,705.3 | 11,416.7 | 42.880x | 102.315x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,790.6 | 0.0666 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 162,635.9 | 0.1551 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 167,640.1 | 0.1599 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,053,474.5 | 2.9120 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,201,964.2 | 3.0536 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 7,103,576.2 | 6.7745 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 7,124,343.8 | 6.7943 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 17,165.0 | 0.0655 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 39,253.1 | 0.1497 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 39,923.0 | 0.1523 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 765,674.2 | 2.9208 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 801,936.3 | 3.0591 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,768,598.2 | 6.7467 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,774,332.9 | 6.7685 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 4,377.4 | 0.0668 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 9,852.1 | 0.1503 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 10,337.5 | 0.1577 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 190,722.3 | 2.9102 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 199,135.6 | 3.0386 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 440,776.6 | 6.7257 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 441,431.8 | 6.7357 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,470.7 | 2,450.3 | 2,472.6 | 8.3 | 0.543x | 1.000x | 75 | 32.9 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,728.2 | 2,717.2 | 2,736.5 | 6.9 | 0.600x | 1.104x | 75 | 36.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,507.2 | 3,300.7 | 3,811.8 | 163.7 | 0.771x | 1.420x | 75 | 46.8 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,262.7 | 4,240.7 | 4,289.8 | 18.0 | 0.937x | 1.725x | 75 | 56.8 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,549.6 | 4,512.2 | 4,723.9 | 78.8 | 1.000x | 1.841x | 75 | 60.7 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 7,732.8 | 7,708.3 | 7,917.5 | 76.9 | 1.700x | 3.130x | 75 | 103.1 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 7,926.8 | 7,874.1 | 7,938.4 | 23.3 | 1.742x | 3.208x | 75 | 105.7 | 17.3 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 98,609.1 | 0.0717 | 97,923.4 | 98,734.9 | 291.8 | 0.092x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 124,515.3 | 0.0905 | 124,214.1 | 124,568.0 | 130.3 | 0.116x | 1.263x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 124,556.3 | 0.0905 | 124,437.8 | 184,608.9 | 24,038.4 | 0.116x | 1.263x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,043,729.0 | 0.7584 | 1,043,165.9 | 1,053,385.5 | 3,888.9 | 0.969x | 10.585x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,077,130.4 | 0.7827 | 1,076,043.9 | 1,081,354.1 | 1,997.5 | 1.000x | 10.923x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,771,121.2 | 3.4667 | 4,758,394.2 | 4,787,174.4 | 9,463.3 | 4.429x | 48.384x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,229,721.7 | 3.8000 | 5,228,164.2 | 5,239,882.5 | 4,960.3 | 4.855x | 53.035x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 73,034.4 | 0.0697 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 102,388.9 | 0.0976 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 102,429.1 | 0.0977 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 797,833.9 | 0.7609 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 822,176.7 | 0.7841 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,637,014.7 | 3.4685 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,986,161.9 | 3.8015 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 20,337.2 | 0.0776 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 18,646.3 | 0.0711 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 18,636.6 | 0.0711 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 196,153.9 | 0.7483 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 202,864.3 | 0.7739 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 908,474.0 | 3.4656 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 993,644.4 | 3.7905 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 5,237.5 | 0.0799 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 3,443.3 | 0.0525 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 3,444.7 | 0.0526 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 50,201.8 | 0.7660 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 51,696.2 | 0.7888 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 226,131.8 | 3.4505 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 248,797.1 | 3.7963 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,377.9 | 1,375.3 | 1,385.1 | 3.7 | 0.459x | 1.000x | 75 | 18.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,712.4 | 1,699.7 | 1,729.6 | 10.9 | 0.571x | 1.243x | 75 | 22.8 | 8.9 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,999.4 | 2,915.2 | 3,155.7 | 91.4 | 1.000x | 2.177x | 75 | 40.0 | 34.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,111.6 | 3,082.9 | 3,389.4 | 114.9 | 1.037x | 2.258x | 75 | 41.5 | 40.4 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,145.5 | 3,140.9 | 3,156.0 | 5.0 | 1.049x | 2.283x | 75 | 41.9 | 18.1 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,377.2 | 3,364.8 | 3,401.1 | 12.8 | 1.126x | 2.451x | 75 | 45.0 | 30.4 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,653.7 | 3,631.2 | 3,665.5 | 13.4 | 1.218x | 2.652x | 75 | 48.7 | 17.3 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,806.5 | 0.0376 | 51,762.3 | 52,848.7 | 416.8 | 0.029x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 338,348.6 | 0.2458 | 338,316.5 | 338,937.3 | 234.5 | 0.191x | 6.531x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 341,140.5 | 0.2479 | 341,029.1 | 341,827.8 | 296.4 | 0.192x | 6.585x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,776,019.1 | 1.2905 | 1,773,741.4 | 1,780,103.0 | 2,146.9 | 1.000x | 34.282x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,846,587.7 | 1.3417 | 1,844,352.2 | 1,852,998.8 | 2,995.1 | 1.040x | 35.644x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,789,670.0 | 3.4802 | 4,783,559.8 | 4,822,488.2 | 17,541.0 | 2.697x | 92.453x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,793,034.7 | 3.4827 | 4,784,840.3 | 4,798,741.6 | 4,647.4 | 2.699x | 92.518x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,445.4 | 0.0376 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 259,772.8 | 0.2477 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 262,007.9 | 0.2499 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,351,745.3 | 1.2891 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,407,577.0 | 1.3424 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,648,890.9 | 3.4799 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,651,299.1 | 3.4822 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,839.5 | 0.0375 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 63,917.1 | 0.2438 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 64,344.3 | 0.2455 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 339,658.5 | 1.2957 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 352,529.8 | 1.3448 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 912,328.2 | 3.4803 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 910,901.7 | 3.4748 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,562.0 | 0.0391 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 14,682.2 | 0.2240 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 14,750.2 | 0.2251 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 84,027.3 | 1.2822 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 86,377.5 | 1.3180 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 228,450.9 | 3.4859 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 227,836.4 | 3.4765 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 927.7 | 927.2 | 969.7 | 16.7 | 0.193x | 1.000x | 75 | 12.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,304.2 | 1,303.5 | 1,305.2 | 0.7 | 0.271x | 1.406x | 75 | 17.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,087.0 | 3,043.5 | 3,602.5 | 212.4 | 0.641x | 3.328x | 75 | 41.2 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,956.7 | 3,922.7 | 4,960.9 | 405.6 | 0.822x | 4.265x | 75 | 52.8 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,815.8 | 4,813.6 | 4,871.7 | 22.1 | 1.000x | 5.191x | 75 | 64.2 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,610.5 | 5,602.3 | 5,612.6 | 4.2 | 1.165x | 6.048x | 75 | 74.8 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,737.3 | 5,697.5 | 5,757.8 | 24.0 | 1.191x | 6.185x | 75 | 76.5 | 17.3 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 23,276.3 | 0.0169 | 23,260.8 | 23,309.7 | 16.6 | 1.000x | 1.000x | spread |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,326.7 | 0.0169 | 23,306.2 | 23,381.2 | 25.4 | 1.002x | 1.002x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 134,167.5 | 0.0975 | 133,810.5 | 134,646.8 | 284.4 | 5.764x | 5.764x | **dominated**: `t-1m` is 90.8% of this set |
| 4 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,281,791.7 | 0.9314 | 1,276,393.1 | 1,284,580.4 | 2,863.4 | 55.068x | 55.068x | spread |
| 5 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,288,581.3 | 0.9363 | 1,283,850.9 | 1,290,266.1 | 2,609.0 | 55.360x | 55.360x | spread |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,882,751.8 | 4.2745 | 5,880,815.4 | 5,886,253.0 | 1,900.8 | 252.735x | 252.735x | spread |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,884,801.5 | 4.2759 | 5,855,971.8 | 5,887,486.0 | 11,844.8 | 252.823x | 252.823x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,692.9 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,723.0 | 0.0169 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 121,727.6 | 0.1161 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 971,614.7 | 0.9266 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 973,785.5 | 0.9287 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 4,477,106.3 | 4.2697 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 4,480,407.9 | 4.2728 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,425.5 | 0.0169 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,451.0 | 0.0170 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,787.9 | 0.0373 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 246,713.5 | 0.9411 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 249,073.2 | 0.9501 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,123,247.6 | 4.2848 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,121,682.3 | 4.2789 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,160.1 | 0.0177 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,157.8 | 0.0177 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,616.1 | 0.0399 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 63,463.5 | 0.9684 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 63,923.3 | 0.9754 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 281,700.0 | 4.2984 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 282,451.1 | 4.3099 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,367.6 | 1,358.4 | 1,536.5 | 68.8 | 0.282x | 1.000x | 75 | 18.2 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,880.0 | 1,860.7 | 1,884.3 | 8.2 | 0.388x | 1.375x | 75 | 25.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,330.5 | 3,136.4 | 3,792.1 | 227.4 | 0.687x | 2.435x | 75 | 44.4 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,835.9 | 3,811.4 | 3,860.8 | 18.2 | 0.791x | 2.805x | 75 | 51.1 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,847.0 | 4,842.4 | 4,879.5 | 13.6 | 1.000x | 3.544x | 75 | 64.6 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,393.8 | 6,370.1 | 6,537.5 | 60.3 | 1.319x | 4.675x | 75 | 85.3 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,549.0 | 6,532.8 | 6,664.7 | 56.1 | 1.351x | 4.789x | 75 | 87.3 | 17.3 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 128,335.2 | 0.0932 | 128,118.9 | 128,514.9 | 145.2 | 0.078x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 408,974.2 | 0.2972 | 408,805.7 | 411,136.7 | 880.4 | 0.249x | 3.187x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 409,654.4 | 0.2977 | 408,388.1 | 411,591.3 | 1,116.8 | 0.249x | 3.192x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,586,698.5 | 1.1529 | 1,563,495.8 | 1,591,292.1 | 11,976.9 | 0.965x | 12.364x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,643,819.0 | 1.1944 | 1,634,173.4 | 1,684,813.7 | 18,345.1 | 1.000x | 12.809x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,942,787.0 | 2.8649 | 3,925,210.4 | 3,974,141.8 | 17,448.3 | 2.399x | 30.723x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,943,797.7 | 2.8656 | 3,934,661.0 | 3,950,399.7 | 6,037.4 | 2.399x | 30.730x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 98,269.1 | 0.0937 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 325,812.7 | 0.3107 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 326,044.8 | 0.3109 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,198,891.6 | 1.1434 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,246,333.5 | 1.1886 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,995,667.0 | 2.8569 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,004,085.8 | 2.8649 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 23,980.4 | 0.0915 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 69,980.2 | 0.2670 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 70,067.2 | 0.2673 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 306,458.9 | 1.1690 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 315,828.8 | 1.2048 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 752,021.0 | 2.8687 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 751,654.6 | 2.8673 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 5,955.9 | 0.0909 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 13,255.2 | 0.2023 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 13,238.7 | 0.2020 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 79,733.8 | 1.2166 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 81,656.7 | 1.2460 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 188,940.5 | 2.8830 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 188,344.2 | 2.8739 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 709.5 | 708.4 | 714.5 | 2.2 | 0.231x | 1.000x | 75 | 9.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 712.0 | 708.1 | 713.7 | 1.9 | 0.232x | 1.004x | 75 | 9.5 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,017.7 | 2,819.6 | 3,254.2 | 189.0 | 0.984x | 4.253x | 75 | 40.2 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,067.8 | 3,053.0 | 3,243.7 | 74.7 | 1.000x | 4.324x | 75 | 40.9 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,072.1 | 2,762.0 | 3,249.2 | 195.3 | 1.001x | 4.330x | 75 | 41.0 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,601.5 | 4,518.0 | 4,803.4 | 107.5 | 1.500x | 6.486x | 75 | 61.4 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,802.4 | 4,629.6 | 5,362.8 | 250.1 | 1.565x | 6.769x | 75 | 64.0 | 17.3 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,579.8 | 0.0375 | 51,399.1 | 51,870.1 | 169.2 | 0.019x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 109,601.6 | 0.0796 | 109,535.3 | 109,918.2 | 148.4 | 0.040x | 2.125x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 109,613.0 | 0.0796 | 109,515.9 | 109,815.4 | 125.2 | 0.040x | 2.125x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 1,672,132.5 | 1.2150 | 1,671,697.5 | 1,673,054.0 | 551.7 | 0.614x | 32.418x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 1,673,031.7 | 1.2156 | 1,671,180.6 | 1,676,032.4 | 1,590.5 | 0.614x | 32.436x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,607,795.8 | 1.8948 | 2,599,348.2 | 3,126,014.0 | 204,021.7 | 0.958x | 50.558x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,722,879.4 | 1.9785 | 2,716,636.8 | 2,726,864.5 | 3,280.2 | 1.000x | 52.790x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,232.4 | 0.0374 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 89,361.5 | 0.0852 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 89,315.7 | 0.0852 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 1,273,145.6 | 1.2142 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 1,273,085.5 | 1.2141 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,981,863.9 | 1.8901 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,071,176.6 | 1.9752 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,847.1 | 0.0376 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 16,754.8 | 0.0639 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 16,788.6 | 0.0640 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 318,135.0 | 1.2136 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 318,211.5 | 1.2139 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 495,539.6 | 1.8903 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 517,002.9 | 1.9722 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,511.5 | 0.0383 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 3,477.0 | 0.0531 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 3,465.2 | 0.0529 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 80,785.1 | 1.2327 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 80,804.4 | 1.2330 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 130,509.1 | 1.9914 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 135,064.2 | 2.0609 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,184.5 | 1,180.1 | 1,188.6 | 2.8 | 0.315x | 1.000x | 75 | 15.8 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,186.2 | 1,182.1 | 1,194.1 | 4.0 | 0.315x | 1.001x | 75 | 15.8 | 8.9 | 100% |
| 3 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 2,015.2 | 2,005.5 | 2,029.4 | 8.1 | 0.535x | 1.701x | 75 | 26.9 | 17.3 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 2,138.3 | 2,133.9 | 2,148.9 | 5.5 | 0.568x | 1.805x | 75 | 28.5 | 18.1 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,929.9 | 2,904.7 | 3,067.8 | 60.0 | 0.778x | 2.474x | 75 | 39.1 | 40.4 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,546.4 | 3,531.9 | 3,602.2 | 31.5 | 0.942x | 2.994x | 75 | 47.3 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,765.5 | 3,753.0 | 3,967.9 | 80.7 | 1.000x | 3.179x | 75 | 50.2 | 34.4 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 3,803,399.2 | 2.7636 | 3,793,866.4 | 3,817,143.3 | 8,062.5 | 0.081x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 7,002,218.5 | 5.0879 | 6,992,783.7 | 7,014,650.7 | 7,628.3 | 0.150x | 1.841x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 10,520,381.9 | 7.6442 | 10,459,895.4 | 10,621,557.4 | 52,565.1 | 0.225x | 2.766x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 25,381,662.2 | 18.4425 | 25,249,636.0 | 26,171,002.0 | 331,477.3 | 0.544x | 6.673x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 25,960,135.6 | 18.8629 | 25,819,433.0 | 27,847,368.1 | 770,958.2 | 0.556x | 6.826x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 28,152,731.3 | 20.4560 | 28,086,400.9 | 28,703,777.5 | 257,321.0 | 0.603x | 7.402x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 46,692,370.3 | 33.9271 | 46,170,189.3 | 47,246,026.5 | 355,737.3 | 1.000x | 12.276x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 2,924,404.6 | 2.7889 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 5,375,563.4 | 5.1265 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 8,048,863.1 | 7.6760 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 19,359,712.7 | 18.4629 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 19,800,676.1 | 18.8834 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 21,566,760.1 | 20.5677 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 35,724,093.8 | 34.0692 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 705,469.6 | 2.6912 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 1,307,768.8 | 4.9887 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,982,484.1 | 7.5626 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 4,808,410.0 | 18.3426 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 4,916,047.0 | 18.7532 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,327,712.9 | 20.3236 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 8,795,872.0 | 33.5536 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 174,800.6 | 2.6672 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 316,927.8 | 4.8359 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 482,588.5 | 7.3637 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 1,203,725.6 | 18.3674 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 1,243,412.5 | 18.9730 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,301,005.6 | 19.8518 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 2,171,424.7 | 33.1333 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,235.2 | 1,227.2 | 1,245.7 | 6.8 | 0.006x | 1.000x | 75 | 16.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,900.4 | 2,881.7 | 2,904.8 | 8.3 | 0.013x | 2.348x | 75 | 38.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 22,433.1 | 22,339.1 | 22,578.1 | 84.8 | 0.104x | 18.161x | 75 | 299.1 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 101,891.1 | 101,644.4 | 102,191.0 | 191.5 | 0.474x | 82.489x | 75 | 1,358.5 | 17.3 | 100% |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 104,231.5 | 104,093.2 | 104,541.5 | 157.7 | 0.485x | 84.383x | 75 | 1,389.8 | 18.1 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 119,950.2 | 119,601.6 | 150,820.1 | 12,375.0 | 0.558x | 97.109x | 75 | 1,599.3 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 214,887.8 | 213,786.3 | 216,740.5 | 1,171.2 | 1.000x | 173.968x | 75 | 2,865.2 | 34.4 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 38.5 | 0.0000 | 38.2 | 39.0 | 0.3 | 0.076x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 38.7 | 0.0000 | 36.2 | 40.3 | 1.5 | 0.076x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 164.4 | 0.0001 | 162.8 | 168.3 | 2.0 | 0.324x | 4.269x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 507.9 | 0.0004 | 504.5 | 518.8 | 5.2 | 1.000x | 13.184x |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 695.3 | 0.0005 | 693.0 | 699.6 | 2.7 | 1.369x | 18.049x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,479,297.3 | 3.2547 | 4,477,760.2 | 4,504,660.0 | 10,211.1 | 8819.157x | 116269.004x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,479,974.4 | 3.2552 | 4,470,907.6 | 4,584,037.7 | 42,412.6 | 8820.490x | 116286.579x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 14.3 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 14.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 60.7 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 284.0 | 0.0003 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 329.1 | 0.0003 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,409,750.2 | 3.2518 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,405,675.4 | 3.2479 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 11.7 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 12.0 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 51.0 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 109.9 | 0.0004 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 171.0 | 0.0007 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 855,486.1 | 3.2634 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 855,086.5 | 3.2619 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 12.6 | 0.0002 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 12.1 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.4 | 0.0008 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 114.0 | 0.0017 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 194.8 | 0.0030 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 214,495.6 | 3.2729 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 213,892.1 | 3.2637 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,058.6 | 1,052.5 | 1,072.1 | 7.4 | 0.175x | 1.000x | 75 | 14.1 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,063.4 | 1,061.0 | 1,069.5 | 3.0 | 0.176x | 1.005x | 75 | 14.2 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,273.1 | 3,118.7 | 3,644.4 | 190.6 | 0.543x | 3.092x | 75 | 43.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,032.0 | 6,007.6 | 6,058.8 | 18.1 | 1.000x | 5.698x | 75 | 80.4 | 34.4 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,430.1 | 6,421.2 | 6,474.6 | 19.1 | 1.066x | 6.074x | 75 | 85.7 | 17.3 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,486.4 | 6,481.7 | 6,491.8 | 3.7 | 1.075x | 6.127x | 75 | 86.5 | 18.1 | 100% |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 7,240.1 | 7,187.1 | 7,854.1 | 253.0 | 1.200x | 6.839x | 75 | 96.5 | 30.4 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 18.9 | 0.0000 | 18.7 | 18.9 | 0.1 | 0.193x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 32.1 | 0.0000 | 32.0 | 32.1 | 0.0 | 0.328x | 1.698x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 82.2 | 0.0001 | 81.5 | 83.3 | 0.6 | 0.841x | 4.355x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 97.8 | 0.0001 | 97.7 | 98.3 | 0.2 | 1.000x | 5.180x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 146.3 | 0.0001 | 145.5 | 151.1 | 2.1 | 1.495x | 7.746x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,269,921.5 | 3.1026 | 4,268,904.0 | 4,272,392.7 | 1,340.7 | 43645.975x | 226106.502x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,273,066.5 | 3.1048 | 4,269,291.7 | 4,459,484.5 | 74,495.1 | 43678.122x | 226273.041x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 6.2 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 45.5 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,251,150.8 | 3.1005 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,254,689.2 | 3.1039 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.3 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 10.7 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.5 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 32.6 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 50.1 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 813,894.6 | 3.1048 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 813,697.2 | 3.1040 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 6.2 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 10.7 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.6 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 32.7 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 52.0 | 0.0008 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 204,391.1 | 3.1188 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 204,649.5 | 3.1227 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 500.2 | 498.2 | 502.8 | 1.8 | 0.157x | 1.000x | 75 | 6.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 871.9 | 870.6 | 874.5 | 1.4 | 0.273x | 1.743x | 75 | 11.6 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,705.8 | 2,689.0 | 3,919.9 | 488.2 | 0.847x | 5.409x | 75 | 36.1 | 30.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,196.0 | 3,177.3 | 5,002.4 | 713.2 | 1.000x | 6.389x | 75 | 42.6 | 34.4 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,318.4 | 3,213.7 | 3,852.9 | 224.3 | 1.038x | 6.634x | 75 | 44.2 | 40.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,405.9 | 6,367.6 | 6,428.1 | 22.3 | 2.004x | 12.806x | 75 | 85.4 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,717.8 | 6,679.0 | 6,738.9 | 20.1 | 2.102x | 13.430x | 75 | 89.6 | 17.3 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 18.0 | 0.0000 | 17.8 | 19.6 | 0.7 | 0.192x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 30.4 | 0.0 | 0.323x | 1.683x |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 80.7 | 0.0001 | 79.9 | 119.8 | 16.8 | 0.858x | 4.471x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 94.1 | 0.0001 | 94.0 | 94.2 | 0.1 | 1.000x | 5.211x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 122.6 | 0.0001 | 111.7 | 127.2 | 6.4 | 1.303x | 6.792x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 3,560,239.2 | 2.5869 | 3,554,729.2 | 3,585,919.1 | 10,957.5 | 37850.648x | 197254.915x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 3,567,581.4 | 2.5922 | 3,564,682.6 | 3,572,748.8 | 2,885.8 | 37928.706x | 197661.708x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 5.9 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 40.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 2,710,326.1 | 2.5848 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 2,714,910.7 | 2.5891 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.0 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 27.1 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 31.3 | 0.0001 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 40.5 | 0.0002 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 678,399.5 | 2.5879 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 681,154.4 | 2.5984 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 5.9 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 26.8 | 0.0004 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 39.4 | 0.0006 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 170,393.6 | 2.6000 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 171,051.0 | 2.6100 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 485.4 | 484.2 | 486.8 | 0.9 | 0.153x | 1.000x | 75 | 6.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 808.5 | 806.7 | 843.8 | 14.3 | 0.254x | 1.665x | 75 | 10.8 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,079.4 | 2,961.1 | 3,492.1 | 216.8 | 0.969x | 6.343x | 75 | 41.1 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,177.8 | 3,173.6 | 3,270.3 | 37.4 | 1.000x | 6.546x | 75 | 42.4 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,353.4 | 3,320.3 | 3,366.8 | 16.1 | 1.055x | 6.908x | 75 | 44.7 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,894.6 | 4,890.4 | 5,215.3 | 128.5 | 1.540x | 10.083x | 75 | 65.3 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,127.9 | 5,112.5 | 5,133.0 | 8.0 | 1.614x | 10.563x | 75 | 68.4 | 17.3 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 82,442.8 | 0.0599 | 82,404.3 | 82,779.8 | 143.3 | 0.003x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 82,594.4 | 0.0600 | 81,806.0 | 82,774.9 | 378.7 | 0.003x | 1.002x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 134,578.1 | 0.0978 | 134,283.8 | 134,658.9 | 137.3 | 0.005x | 1.632x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 8,122,808.4 | 5.9021 | 8,115,114.7 | 8,142,948.8 | 9,359.8 | 0.311x | 98.527x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 8,139,105.6 | 5.9139 | 8,113,363.1 | 8,188,091.3 | 29,763.9 | 0.312x | 98.724x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 26,121,044.2 | 18.9798 | 26,088,628.6 | 26,127,729.7 | 14,582.2 | 1.000x | 316.838x |
| 7 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 28,647,224.1 | 20.8153 | 28,569,891.7 | 28,742,575.6 | 55,218.1 | 1.097x | 347.480x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 68,475.7 | 0.0653 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 68,460.9 | 0.0653 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 102,549.8 | 0.0978 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 6,197,102.8 | 5.9100 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 6,216,365.1 | 5.9284 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,930,940.9 | 19.0076 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 21,854,208.9 | 20.8418 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 11,711.1 | 0.0447 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 11,731.0 | 0.0448 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 25,762.1 | 0.0983 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,536,125.5 | 5.8599 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,535,880.8 | 5.8589 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 4,952,782.8 | 18.8934 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 5,421,512.5 | 20.6814 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 2,412.7 | 0.0368 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 2,402.5 | 0.0367 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 6,170.6 | 0.0942 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 386,493.1 | 5.8974 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 386,859.8 | 5.9030 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,236,205.0 | 18.8630 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,354,918.6 | 20.6744 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 712.6 | 711.6 | 715.9 | 1.6 | 0.242x | 1.000x | 75 | 9.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 720.9 | 713.6 | 726.3 | 4.8 | 0.245x | 1.012x | 75 | 9.6 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,893.0 | 2,869.5 | 2,971.3 | 35.6 | 0.981x | 4.060x | 75 | 38.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,947.9 | 2,924.3 | 2,956.6 | 12.3 | 1.000x | 4.137x | 75 | 39.3 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,409.3 | 3,393.2 | 3,461.1 | 25.0 | 1.157x | 4.784x | 75 | 45.5 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,741.2 | 6,705.1 | 6,770.6 | 25.4 | 2.287x | 9.459x | 75 | 89.9 | 17.3 | 100% |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,901.9 | 6,801.1 | 6,933.0 | 47.1 | 2.341x | 9.685x | 75 | 92.0 | 18.1 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 4,081,401.6 | 2.9656 | 4,079,378.7 | 4,092,301.8 | 5,071.7 | 0.136x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 4,082,918.2 | 2.9667 | 4,078,569.3 | 4,084,025.3 | 2,167.5 | 0.136x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 5,402,673.4 | 3.9256 | 5,399,299.7 | 5,466,254.6 | 31,026.6 | 0.180x | 1.324x |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 20,840,691.4 | 15.1430 | 20,782,768.7 | 20,873,255.5 | 35,731.5 | 0.693x | 5.106x |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 21,363,647.7 | 15.5230 | 20,835,164.9 | 21,506,251.7 | 238,860.6 | 0.710x | 5.234x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 23,532,100.3 | 17.0986 | 23,513,965.2 | 26,187,735.2 | 1,057,537.6 | 0.782x | 5.766x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 30,086,298.6 | 21.8610 | 30,049,413.9 | 30,111,953.1 | 22,366.6 | 1.000x | 7.372x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 3,112,023.6 | 2.9679 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 3,113,456.2 | 2.9692 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 4,116,028.1 | 3.9254 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 15,892,805.1 | 15.1566 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 16,354,535.2 | 15.5969 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 17,903,606.9 | 17.0742 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 22,873,496.7 | 21.8139 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 776,763.9 | 2.9631 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 776,575.9 | 2.9624 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 1,030,705.9 | 3.9318 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 3,956,328.5 | 15.0922 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 3,997,006.9 | 15.2474 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,481,656.2 | 17.0962 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 5,728,266.4 | 21.8516 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 191,886.5 | 2.9280 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 191,710.1 | 2.9253 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 257,015.1 | 3.9217 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 987,155.6 | 15.0628 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 991,646.3 | 15.1313 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,151,513.2 | 17.5707 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 1,471,126.6 | 22.4476 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 2,703.5 | 2,701.8 | 2,709.7 | 3.0 | 0.133x | 1.000x | 75 | 36.0 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 2,704.2 | 2,700.2 | 2,710.0 | 3.5 | 0.133x | 1.000x | 75 | 36.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 4,794.5 | 4,707.3 | 4,828.3 | 46.1 | 0.236x | 1.773x | 75 | 63.9 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 16,462.9 | 16,332.6 | 16,568.5 | 86.6 | 0.811x | 6.089x | 75 | 219.5 | 18.1 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 16,470.1 | 16,463.5 | 16,508.0 | 16.3 | 0.812x | 6.092x | 75 | 219.6 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 16,488.3 | 16,444.2 | 16,947.0 | 190.1 | 0.813x | 6.099x | 75 | 219.8 | 17.3 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,292.4 | 20,225.6 | 20,644.2 | 154.1 | 1.000x | 7.506x | 75 | 270.6 | 34.4 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,051,200.3 | 0.7638 | 1,050,835.9 | 1,053,165.3 | 888.4 | 0.157x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,267,983.1 | 0.9213 | 1,266,928.6 | 1,269,634.9 | 870.6 | 0.190x | 1.206x |
| 3 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,269,658.2 | 0.9225 | 1,264,594.5 | 1,272,641.5 | 2,716.9 | 0.190x | 1.208x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,570,651.2 | 4.0477 | 5,552,794.1 | 5,706,381.4 | 58,098.5 | 0.834x | 5.299x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 6,681,609.1 | 4.8549 | 6,653,379.7 | 6,695,199.9 | 15,895.0 | 1.000x | 6.356x |
| 6 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 9,942,510.7 | 7.2243 | 9,920,138.7 | 10,136,553.7 | 81,436.0 | 1.488x | 9.458x |
| 7 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 9,972,898.1 | 7.2464 | 9,944,468.0 | 10,024,031.4 | 26,844.7 | 1.493x | 9.487x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 792,469.1 | 0.7558 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 962,612.0 | 0.9180 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 963,900.7 | 0.9192 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 4,222,246.4 | 4.0266 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 5,067,071.7 | 4.8323 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 7,553,511.1 | 7.2036 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 7,607,445.9 | 7.2550 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 207,111.4 | 0.7901 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 240,623.6 | 0.9179 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 240,847.5 | 0.9188 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,060,747.7 | 4.0464 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 1,266,346.3 | 4.8307 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 1,889,302.0 | 7.2071 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 1,900,394.0 | 7.2494 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 51,618.6 | 0.7876 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 64,122.5 | 0.9784 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 64,114.0 | 0.9783 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 286,496.5 | 4.3716 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 340,268.2 | 5.1921 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 477,359.3 | 7.2839 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 478,564.9 | 7.3023 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,303.3 | 1,293.5 | 1,325.4 | 12.1 | 0.359x | 1.000x | 75 | 17.4 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,308.4 | 1,307.0 | 1,325.1 | 7.2 | 0.360x | 1.004x | 75 | 17.4 | 8.9 | 100% |
| 3 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,182.7 | 3,170.6 | 3,186.3 | 6.3 | 0.876x | 2.442x | 75 | 42.4 | 30.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,420.5 | 3,410.0 | 3,585.0 | 66.9 | 0.942x | 2.624x | 75 | 45.6 | 40.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,631.6 | 3,577.7 | 3,706.2 | 47.2 | 1.000x | 2.786x | 75 | 48.4 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 11,083.3 | 11,067.8 | 11,133.3 | 23.3 | 3.052x | 8.504x | 75 | 147.8 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 11,275.2 | 11,263.9 | 11,292.5 | 10.3 | 3.105x | 8.651x | 75 | 150.3 | 17.3 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 60,156.2 | 0.0437 | 59,831.1 | 60,764.7 | 306.2 | 0.021x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 994,646.2 | 0.7227 | 993,472.1 | 997,234.8 | 1,378.6 | 0.351x | 16.534x |
| 3 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,006,824.5 | 0.7316 | 995,346.0 | 1,017,357.4 | 8,793.6 | 0.355x | 16.737x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 2,440,748.2 | 1.7735 | 2,438,170.8 | 2,637,764.5 | 78,609.1 | 0.860x | 40.574x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,836,522.1 | 2.0610 | 2,835,421.7 | 2,837,841.7 | 876.8 | 1.000x | 47.153x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,311,128.2 | 3.1325 | 4,310,108.2 | 4,326,406.2 | 6,116.3 | 1.520x | 71.666x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,312,509.8 | 3.1335 | 4,309,180.0 | 4,313,250.5 | 1,439.1 | 1.520x | 71.689x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 45,835.2 | 0.0437 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 757,131.9 | 0.7221 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 758,140.9 | 0.7230 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,854,898.8 | 1.7690 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 2,155,494.3 | 2.0556 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,283,124.5 | 3.1310 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,283,515.1 | 3.1314 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 11,429.6 | 0.0436 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 189,159.3 | 0.7216 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 201,192.0 | 0.7675 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 465,542.7 | 1.7759 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 542,450.0 | 2.0693 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 822,729.0 | 3.1385 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 821,976.1 | 3.1356 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,925.8 | 0.0446 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 48,240.4 | 0.7361 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 48,453.0 | 0.7393 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 118,749.7 | 1.8120 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 138,428.8 | 2.1123 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 206,915.0 | 3.1573 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 206,938.4 | 3.1576 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 1,147.7 | 1,138.7 | 1,155.8 | 5.5 | 0.220x | 1.000x | 75 | 15.3 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 1,149.1 | 1,133.6 | 1,150.8 | 6.4 | 0.220x | 1.001x | 75 | 15.3 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,117.6 | 3,055.8 | 3,575.8 | 190.8 | 0.597x | 2.716x | 75 | 41.6 | 40.4 | 100% |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 4,769.2 | 4,733.6 | 5,473.2 | 280.2 | 0.914x | 4.155x | 75 | 63.6 | 30.4 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 5,218.0 | 5,200.5 | 5,233.4 | 12.2 | 1.000x | 4.546x | 75 | 69.6 | 34.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 5,253.5 | 5,240.8 | 5,256.0 | 6.7 | 1.007x | 4.577x | 75 | 70.0 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 5,305.8 | 5,292.5 | 5,318.0 | 8.9 | 1.017x | 4.623x | 75 | 70.7 | 17.3 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 12,110,526.0 | 8.7996 | 12,105,147.0 | 13,002,819.7 | 405,608.2 | 0.043x | 1.000x |
| 2 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 12,171,744.1 | 8.8441 | 12,140,474.0 | 12,819,261.0 | 257,574.5 | 0.044x | 1.005x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,215,396.8 | 12.5089 | 17,129,482.5 | 17,236,671.2 | 39,452.1 | 0.062x | 1.422x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 48,404,817.2 | 35.1714 | 48,281,649.5 | 53,994,198.3 | 2,215,387.1 | 0.174x | 3.997x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 48,463,420.2 | 35.2140 | 48,281,972.3 | 49,875,024.7 | 599,052.1 | 0.174x | 4.002x |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 227,773,600.5 | 165.5023 | 227,381,168.0 | 228,528,644.5 | 422,175.6 | 0.816x | 18.808x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 278,963,869.0 | 202.6977 | 278,287,376.0 | 279,643,673.0 | 430,615.4 | 1.000x | 23.035x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 9,238,754.9 | 8.8108 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 9,274,272.1 | 8.8446 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 13,147,462.7 | 12.5384 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 36,915,243.0 | 35.2051 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 36,878,548.0 | 35.1701 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 173,570,529.5 | 165.5298 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 212,573,634.0 | 202.7260 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 2,300,781.6 | 8.7768 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 2,315,057.3 | 8.8312 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 3,260,497.4 | 12.4378 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 9,220,594.8 | 35.1738 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 9,167,120.2 | 34.9698 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 43,361,729.5 | 165.4119 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 53,060,016.0 | 202.4079 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 575,172.8 | 8.7764 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 585,320.6 | 8.9313 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 809,212.9 | 12.3476 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 2,309,291.3 | 35.2370 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 2,289,529.5 | 34.9354 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 10,841,341.5 | 165.4257 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 13,330,219.0 | 203.4030 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 7,384.2 | 7,375.2 | 7,449.9 | 30.9 | 0.033x | 1.000x | 75 | 98.5 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 7,428.9 | 7,384.3 | 7,508.7 | 42.3 | 0.033x | 1.006x | 75 | 99.1 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 17,073.0 | 17,050.5 | 17,185.9 | 48.4 | 0.077x | 2.312x | 75 | 227.6 | 40.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 48,562.7 | 48,494.6 | 48,761.9 | 94.0 | 0.219x | 6.577x | 75 | 647.5 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 48,624.9 | 48,475.1 | 48,683.8 | 71.1 | 0.219x | 6.585x | 75 | 648.3 | 17.3 | 100% |
| 6 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 182,782.9 | 182,597.5 | 189,777.2 | 2,801.2 | 0.823x | 24.753x | 75 | 2,437.1 | 30.4 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 222,001.6 | 220,391.7 | 233,793.2 | 4,999.2 | 1.000x | 30.065x | 75 | 2,960.0 | 34.4 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 51,801.2 | 0.0376 | 51,769.8 | 52,147.3 | 145.0 | 0.022x | 1.000x |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 1,949,356.0 | 1.4164 | 1,946,978.9 | 2,139,020.4 | 75,884.2 | 0.828x | 37.631x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,354,099.0 | 1.7105 | 2,353,756.3 | 2,354,931.7 | 462.2 | 1.000x | 45.445x |
| 4 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,084,577.9 | 2.9679 | 4,078,008.5 | 4,088,273.2 | 3,337.1 | 1.735x | 78.851x |
| 5 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,085,762.0 | 2.9688 | 4,082,698.4 | 4,087,870.3 | 1,799.5 | 1.736x | 78.874x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,482.4 | 0.0377 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 1,491,673.6 | 1.4226 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,802,863.1 | 1.7193 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,112,937.5 | 2.9687 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,115,413.9 | 2.9711 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 9,807.9 | 0.0374 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 369,613.0 | 1.4100 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 446,632.5 | 1.7038 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 777,684.0 | 2.9666 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 777,598.7 | 2.9663 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 2,512.8 | 0.0383 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 86,656.1 | 1.3223 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 104,594.7 | 1.5960 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 192,949.4 | 2.9442 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 193,311.7 | 2.9497 |

- not ranked: `pcrec_a770139e_auto-caps-simdna` — did-not-compile (the artifact did not build:\ngcc -O2 -std=gnu11 -fPIC -shared -o /home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact-1.so /home/duxevents/pcrec-bench/testees/pcrec/shim.c -DPB_ARTIFACT="/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c" -I /home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1\nIn file included from /home/duxevents/pcrec-bench/testees/pcrec/shim.c:308:\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_search':\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: warning: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: error: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:201:7: error: expected expression before '/' token\n  201 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: warning: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: error: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:261:7: error: expected expression before '/' token\n  261 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: error: 'rx_forward_next_state' undeclared (first use in this function); did you mean 'rx_forward_state'?\n  295 |         forward_state = rx_forward_step(rx_forward_next_state, forward_state, rx_forward_byte_class[subject[scan_position++]]);\n      |                                         ^~~~~~~~~~~~~~~~~~~~~\n      |                                         rx_forward_state\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: note: each undeclared identifier is reported only once for each function it appears in\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:307:45: error: 'rx_reverse_next_state' undeclared (first use in this function); did you mean 'rx_reverse_state'?\n  307 |             reverse_state = rx_reverse_step(rx_reverse_next_state, reverse_state, rx_reverse_byte_class[subject[--rewind_position]]);\n      |                                             ^~~~~~~~~~~~~~~~~~~~~\n      |                                             rx_reverse_state\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_match':\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: warning: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: error: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:395:7: error: expected expression before '/' token\n  395 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:421:43: error: 'rx_anchored_next_state' undeclared (first use in this function); did you mean 'rx_anchored_state'?\n  421 |         anchored_state = rx_anchored_step(rx_anchored_next_state, anchored_state, rx_anchored_byte_class[subject[scan_position++]]);\n      |                                           ^~~~~~~~~~~~~~~~~~~~~~\n      |                                           rx_anchored_state\n)
- not ranked: `pcrec_a770139e_auto-nocaps-simdna` — did-not-compile (the artifact did not build:\ngcc -O2 -std=gnu11 -fPIC -shared -o /home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact-1.so /home/duxevents/pcrec-bench/testees/pcrec/shim.c -DPB_ARTIFACT="/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c" -I /home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1\nIn file included from /home/duxevents/pcrec-bench/testees/pcrec/shim.c:308:\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_search':\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: warning: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: error: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:201:7: error: expected expression before '/' token\n  201 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: warning: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: error: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:261:7: error: expected expression before '/' token\n  261 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: error: 'rx_forward_next_state' undeclared (first use in this function); did you mean 'rx_forward_state'?\n  295 |         forward_state = rx_forward_step(rx_forward_next_state, forward_state, rx_forward_byte_class[subject[scan_position++]]);\n      |                                         ^~~~~~~~~~~~~~~~~~~~~\n      |                                         rx_forward_state\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: note: each undeclared identifier is reported only once for each function it appears in\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:307:45: error: 'rx_reverse_next_state' undeclared (first use in this function); did you mean 'rx_reverse_state'?\n  307 |             reverse_state = rx_reverse_step(rx_reverse_next_state, reverse_state, rx_reverse_byte_class[subject[--rewind_position]]);\n      |                                             ^~~~~~~~~~~~~~~~~~~~~\n      |                                             rx_reverse_state\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_match':\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: warning: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: error: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:395:7: error: expected expression before '/' token\n  395 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:421:43: error: 'rx_anchored_next_state' undeclared (first use in this function); did you mean 'rx_anchored_state'?\n  421 |         anchored_state = rx_anchored_step(rx_anchored_next_state, anchored_state, rx_anchored_byte_class[subject[scan_position++]]);\n      |                                           ^~~~~~~~~~~~~~~~~~~~~~\n      |                                           rx_anchored_state\n)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,811.0 | 2,805.6 | 3,107.5 | 143.4 | 0.840x | 1.000x | 75 | 37.5 | 40.4 | 100% |
| 2 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 3,237.0 | 3,212.2 | 4,395.7 | 458.3 | 0.967x | 1.152x | 75 | 43.2 | 30.4 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,347.3 | 3,337.3 | 3,365.6 | 11.8 | 1.000x | 1.191x | 75 | 44.6 | 34.4 | 100% |
| 4 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,757.0 | 4,588.3 | 4,800.6 | 84.9 | 1.421x | 1.692x | 75 | 63.4 | 18.1 | 100% |
| 5 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,831.2 | 4,656.0 | 4,890.2 | 96.2 | 1.443x | 1.719x | 75 | 64.4 | 17.3 | 100% |

- not ranked: `pcrec_a770139e_auto-caps-simdna` — did-not-compile (the artifact did not build:\ngcc -O2 -std=gnu11 -fPIC -shared -o /home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact-1.so /home/duxevents/pcrec-bench/testees/pcrec/shim.c -DPB_ARTIFACT="/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c" -I /home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1\nIn file included from /home/duxevents/pcrec-bench/testees/pcrec/shim.c:308:\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_search':\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: warning: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: error: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:201:7: error: expected expression before '/' token\n  201 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: warning: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: error: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:261:7: error: expected expression before '/' token\n  261 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: error: 'rx_forward_next_state' undeclared (first use in this function); did you mean 'rx_forward_state'?\n  295 |         forward_state = rx_forward_step(rx_forward_next_state, forward_state, rx_forward_byte_class[subject[scan_position++]]);\n      |                                         ^~~~~~~~~~~~~~~~~~~~~\n      |                                         rx_forward_state\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: note: each undeclared identifier is reported only once for each function it appears in\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:307:45: error: 'rx_reverse_next_state' undeclared (first use in this function); did you mean 'rx_reverse_state'?\n  307 |             reverse_state = rx_reverse_step(rx_reverse_next_state, reverse_state, rx_reverse_byte_class[subject[--rewind_position]]);\n      |                                             ^~~~~~~~~~~~~~~~~~~~~\n      |                                             rx_reverse_state\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_match':\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: warning: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: error: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:395:7: error: expected expression before '/' token\n  395 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-auto/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:421:43: error: 'rx_anchored_next_state' undeclared (first use in this function); did you mean 'rx_anchored_state'?\n  421 |         anchored_state = rx_anchored_step(rx_anchored_next_state, anchored_state, rx_anchored_byte_class[subject[scan_position++]]);\n      |                                           ^~~~~~~~~~~~~~~~~~~~~~\n      |                                           rx_anchored_state\n)
- not ranked: `pcrec_a770139e_auto-nocaps-simdna` — did-not-compile (the artifact did not build:\ngcc -O2 -std=gnu11 -fPIC -shared -o /home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact-1.so /home/duxevents/pcrec-bench/testees/pcrec/shim.c -DPB_ARTIFACT="/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c" -I /home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1\nIn file included from /home/duxevents/pcrec-bench/testees/pcrec/shim.c:308:\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_search':\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: warning: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:200:20: error: missing terminating " character\n  200 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:201:7: error: expected expression before '/' token\n  201 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: warning: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:260:20: error: missing terminating " character\n  260 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:261:7: error: expected expression before '/' token\n  261 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: error: 'rx_forward_next_state' undeclared (first use in this function); did you mean 'rx_forward_state'?\n  295 |         forward_state = rx_forward_step(rx_forward_next_state, forward_state, rx_forward_byte_class[subject[scan_position++]]);\n      |                                         ^~~~~~~~~~~~~~~~~~~~~\n      |                                         rx_forward_state\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:295:41: note: each undeclared identifier is reported only once for each function it appears in\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:307:45: error: 'rx_reverse_next_state' undeclared (first use in this function); did you mean 'rx_reverse_state'?\n  307 |             reverse_state = rx_reverse_step(rx_reverse_next_state, reverse_state, rx_reverse_byte_class[subject[--rewind_position]]);\n      |                                             ^~~~~~~~~~~~~~~~~~~~~\n      |                                             rx_reverse_state\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c: In function 'rx_match':\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: warning: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:394:20: error: missing terminating " character\n  394 |      *    5  "/*!*/"   ACCEPTING\n      |                    ^~~~~~~~~~~~~\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:395:7: error: expected expression before '/' token\n  395 |      */\n      |       ^\n/home/duxevents/pcrec-bench/build/work/pcrec-nocaps/p-wild-waf-crs-942500-comment-obfuscation/plain/t1/artifact.c:421:43: error: 'rx_anchored_next_state' undeclared (first use in this function); did you mean 'rx_anchored_state'?\n  421 |         anchored_state = rx_anchored_step(rx_anchored_next_state, anchored_state, rx_anchored_byte_class[subject[scan_position++]]);\n      |                                           ^~~~~~~~~~~~~~~~~~~~~~\n      |                                           rx_anchored_state\n)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 20.2 | 0.0000 | 20.2 | 20.3 | 0.1 | 0.076x | 1.000x |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 20.3 | 0.0000 | 20.0 | 20.3 | 0.1 | 0.076x | 1.001x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 119.8 | 0.0001 | 109.8 | 123.4 | 5.2 | 0.447x | 5.917x |
| 4 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 265.1 | 0.0002 | 264.5 | 269.7 | 1.9 | 0.989x | 13.094x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 268.0 | 0.0002 | 266.9 | 268.8 | 0.8 | 1.000x | 13.239x |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 4,908,974.8 | 3.5669 | 4,901,583.1 | 4,948,009.4 | 16,656.1 | 18315.774x | 242483.229x |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 4,942,042.7 | 3.5909 | 4,922,371.5 | 4,955,452.8 | 12,998.1 | 18439.153x | 244116.647x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 41.2 | 0.0000 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_dfa-nocaps-simdna` | 88.1 | 0.0001 |
| `t-1m` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 89.3 | 0.0001 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-caps-simdna` | 3,741,225.2 | 3.5679 |
| `t-1m` | 1,048,576 | `pcrec_a770139e_vm-in-caps-simdna` | 3,769,994.7 | 3.5953 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-caps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `pcrec_a770139e_auto-nocaps-simdna` | 6.8 | 0.0000 |
| `t-256k` | 262,144 | `libpcre2_10.46_jit-caps-simdna` | 39.4 | 0.0002 |
| `t-256k` | 262,144 | `libpcre2_10.46_dfa-nocaps-simdna` | 87.9 | 0.0003 |
| `t-256k` | 262,144 | `libpcre2_10.46_interp-caps-simdna` | 89.4 | 0.0003 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-caps-simdna` | 931,947.9 | 3.5551 |
| `t-256k` | 262,144 | `pcrec_a770139e_vm-in-caps-simdna` | 934,711.6 | 3.5656 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-caps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `pcrec_a770139e_auto-nocaps-simdna` | 6.7 | 0.0001 |
| `t-64k` | 65,536 | `libpcre2_10.46_jit-caps-simdna` | 39.0 | 0.0006 |
| `t-64k` | 65,536 | `libpcre2_10.46_dfa-nocaps-simdna` | 89.3 | 0.0014 |
| `t-64k` | 65,536 | `libpcre2_10.46_interp-caps-simdna` | 89.6 | 0.0014 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-caps-simdna` | 234,545.2 | 3.5789 |
| `t-64k` | 65,536 | `pcrec_a770139e_vm-in-caps-simdna` | 238,928.8 | 3.6458 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_a770139e_auto-caps-simdna` | measured | `plain` | same program | 498.9 | 498.6 | 499.7 | 0.4 | 0.108x | 1.000x | 75 | 6.7 | 8.9 | 100% |
| 2 | `pcrec_a770139e_auto-nocaps-simdna` | measured | `plain` | same program | 500.0 | 498.9 | 500.2 | 0.6 | 0.108x | 1.002x | 75 | 6.7 | 8.9 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,848.0 | 2,779.5 | 3,490.7 | 304.5 | 0.615x | 5.709x | 75 | 38.0 | 40.4 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 4,634.3 | 4,604.7 | 4,664.7 | 19.9 | 1.000x | 9.290x | 75 | 61.8 | 34.4 | 100% |
| 5 | `libpcre2_10.46_dfa-nocaps-simdna` | measured | `plain` | same program | 5,444.9 | 5,403.3 | 5,916.1 | 193.1 | 1.175x | 10.915x | 75 | 72.6 | 30.4 | 100% |
| 6 | `pcrec_a770139e_vm-caps-simdna` | measured | `plain` | same program | 6,165.8 | 6,163.9 | 6,171.9 | 3.2 | 1.330x | 12.360x | 75 | 82.2 | 18.1 | 100% |
| 7 | `pcrec_a770139e_vm-in-caps-simdna` | measured | `plain` | same program | 6,189.7 | 6,180.8 | 6,206.9 | 9.0 | 1.336x | 12.408x | 75 | 82.5 | 17.3 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 75 | 93% | 0 | 0 | `sd-empty-alt-hit` (timed-out), `sd-empty-alt-miss` (timed-out), `sec-github-pat` (timed-out), `v-uuid-badnibble` (timed-out), `v-uuid-valid` (timed-out) |
| `email-nested-plus` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 75 | 93% | 0 | 0 | `sd-empty-alt-hit` (timed-out), `sd-empty-alt-miss` (timed-out), `sec-github-pat` (timed-out), `v-uuid-badnibble` (timed-out), `v-uuid-valid` (timed-out) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 75 | 97% | -47:match×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 75 | 97% | -47:match×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (timed-out), `sd-empty-alt-hit` (timed-out) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 75 | 97% | 0 | 10 | `rd-evil-alt-near-miss` (wrong), `sd-empty-alt-hit` (wrong) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (timed-out), `sd-empty-alt-hit` (timed-out) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (timed-out), `sd-empty-alt-hit` (timed-out) |
| `file-ext-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `negation-scope-lookbehind-var` | `large-subject-throughput` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3 | 0% | -42:pattern×3 (smallest: t-64k, 65,536 B) | 0 | `t-1m` (gave-up), `t-256k` (gave-up), `t-64k` (gave-up) |
| `negation-scope-lookbehind-var` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 80% | -42:pattern×15 (smallest: sd-fileext-short, 14 B) | 0 | `la-negation-hit` (gave-up), `la-negation-miss` (gave-up), `lp-atomic-hit` (gave-up), `lp-atomic-nonmatch` (gave-up), `lp-syslog` (gave-up), `sd-fileext-short` (gave-up), `sec-slack-webhook` (gave-up), `sec-userpass` (gave-up), `v-email` (gave-up), `v-uuid-badnibble` (gave-up), `v-uuid-valid` (gave-up), `waf-benign` (gave-up), `waf-concat` (gave-up), `waf-dbnames` (gave-up), `waf-union` (gave-up) |
| `router-prefix-order` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `tag-depth3-bound` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 96% | -42:pattern×3 (smallest: br-tag-pair, 18 B) | 0 | `br-tag-mismatch` (gave-up), `br-tag-pair` (gave-up), `rec-tag-depth3` (gave-up) |
| `wild-logparse-quotedstring-grok` | `short-subject-search` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 75 | 99% | 0 | 5 | `lp-quoted-escaped` (wrong) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_a770139e_auto-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=declined-nullable-default (prefilter declined, no cap hit), entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1497877 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 301,737 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1519458 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 301,846 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `base10num-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `base10num-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `codegrammar-flat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `codegrammar-flat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `codegrammar-xflag` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `date-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `date-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `doubled-word` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `email-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `email-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `evil-alt-nested` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `evil-alt-nested` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `file-ext-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `file-ext-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `floor-byte` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `floor-byte` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `high-byte-run` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=4 (match: 2), start=reverse-pass, folds=2, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `high-byte-run` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `ipv4-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `keyword-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 15,914 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=1, islands=2, shape=plain (prog: 16,019 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/2 == stamped default (single tier), buffers=1/2 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `logparse-atomic-removed` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `mojibake-curly-quote` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_auto-nocaps-simdna` / `numeric-id-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `phone-list-nested-plus` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (exact), dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `router-prefix-order` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `router-prefix-order` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `trim-nested-star` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `trim-nested-star` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `uuid-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `uuid-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-datetime-datefinder-alternation` / `plain`: engine=dfa, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=2 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1454134 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 258,593 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=size-cap-retry (DFA fallback tripped), entry=plain entry, vm_prefilter=hybrid, lang=count-collapsed (size cap retry, exact 1475715 > 1000000), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=1, shape=plain (prog: 258,702 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=47/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=selected, entry=plain entry, vm_prefilter=hybrid, lang=exact (no counted repeat), dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-github-pat` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,6*, edge=mixed, edges=3 (match: 3), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=mixed offsets=none, edge=range, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=range, edges=0 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,1*, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-email-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=offset-set-bounded table=premultiplied offsets=0,8*,13, edge=bitmap, edges=8 (match: 4), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=mixed, edges=2 (match: 2), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=bitmap, edges=1 (match: 1), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `winpath-near-miss` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_auto-nocaps-simdna` / `winpath-near-miss` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=attempt prefilter=none table=none offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=search-filter, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_a770139e_vm-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=3/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=5/5 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=3/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=5/7 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=5/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=13/5 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=1/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,286 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,389 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=40
- `pcrec_a770139e_vm-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=1/10 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=4/6 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=2/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=5/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=14/11 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=5/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=5/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 301,737 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 301,846 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=8/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=1/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=2/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=9/13 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=2/4 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=15/2 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=4/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=3/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=29/3 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=3/2 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `balanced-parens-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,049 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `balanced-parens-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,259 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `base10num-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,040 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `base10num-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,145 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `bracket-array-define` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,395 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `bracket-array-define` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,500 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=47/71 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `codegrammar-flat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,601 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `codegrammar-flat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,704 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `codegrammar-xflag` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,658 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `codegrammar-xflag` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 2,763 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,586 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `currency-lookbehind-fixed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,691 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `date-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,024 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `date-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 8,129 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `doubled-word` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,982 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `doubled-word` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,087 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `dup-param-detect` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `dup-param-detect` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,826 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `email-local-nodup` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,816 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `email-local-nodup` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,921 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/7 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `email-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,299 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `email-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,404 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `evil-alt-nested` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,147 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `evil-alt-nested` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,252 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `file-ext-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,449 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `file-ext-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,554 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `float-literal-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,425 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `float-literal-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,530 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=5/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `floor-byte` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `floor-byte` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `high-byte-run` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 647 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `high-byte-run` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 750 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `ipv4-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,695 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `ipv4-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 13,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=13/5 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `keyword-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,930 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `keyword-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,035 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `logparse-atomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,167 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `logparse-atomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 16,272 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `logparse-atomic-removed` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,757 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `logparse-atomic-removed` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=2, shape=plain (prog: 15,862 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `mojibake-curly-quote` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,286 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `mojibake-curly-quote` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 1,389 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `nested-comment-rec` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,432 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `nested-comment-rec` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,537 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=46/70 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=40
- `pcrec_a770139e_vm-in-caps-simdna` / `numeric-id-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,986 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `numeric-id-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,091 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `phone-list-nested-plus` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,110 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `phone-list-nested-plus` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,215 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `phone-palindrome-6` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,952 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `phone-palindrome-6` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 4,057 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/10 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `pwd-strength-chain` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,830 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `pwd-strength-chain` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,935 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `quoted-delim-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,139 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `quoted-delim-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,244 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `router-prefix-order` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,291 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `router-prefix-order` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,396 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `tag-depth3-bound` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 10,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `tag-depth3-bound` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 11,054 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `tag-pair-match` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,740 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `tag-pair-match` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,845 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=4/6 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `trim-nested-star` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,800 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `trim-nested-star` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,905 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `utf8-lead-no-cont` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,206 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `utf8-lead-no-cont` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,309 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `uuid-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,685 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `uuid-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=shared (prog: 4,790 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-array-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,481 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-constant` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=1, shape=forward (prog: 3,586 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-number-extended` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,852 B), clsfolds=1, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 237 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-object-begin` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 340 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-codegrammar-json-stringcontent-escape` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,487 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,575 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-datetime-moment-iso8601` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,680 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=14/11 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,399 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-base10num-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,507 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,989 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-base10num-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,094 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=5/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,844 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-quotedstring-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 18,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=60/91 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,216 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-quotedstring-noatomic` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 15,321 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 301,737 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-syslogbase-expanded` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 301,846 B), clsfolds=8, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED|PCREC_VM_RUNG_REVDET, K=8/default, caps=500,000/1,000,000, fast tier=19/29 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,590 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-logparse-winpath-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,696 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,403 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-aws-access-key-id` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=1, shape=plain (prog: 7,508 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=8/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-github-pat` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,330 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-github-pat` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=inline (prog: 3,435 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,624 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-slack-webhook-url` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=plain (prog: 8,729 B), clsfolds=15, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,664 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-secrets-username-password-pair` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=2, shape=plain (prog: 19,769 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=62/93 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,290 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-altorder-foo-foobar-rustregex` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,395 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=2/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 728 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-dollar-trailing-newline-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 831 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,439 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-semdiv-empty-alt-repeat-pcre2` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 1,544 B), clsfolds=0, rungs=PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/94 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-email-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,616 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-email-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 5,721 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,007 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-ipv4-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 14,112 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=9/13 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,173 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-us-zip-owasp` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,276 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=2/4 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,549 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-validator-uuid-grok` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 2,652 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 41,952 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942140-dbnames` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 42,059 B), clsfolds=23, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=15/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 6,899 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942160-sleep-benchmark` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 7,004 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=4/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,138 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942270-union-select` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 4,243 B), clsfolds=12, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=3/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,600 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942360-concat-sqli` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 170,707 B), clsfolds=26, rungs=PCREC_VM_RUNG_CURSOR, K=8/default, caps=500,000/1,000,000, fast tier=29/3 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,934 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `wild-waf-crs-942500-comment-obfuscation` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,039 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=3/2 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `winpath-near-miss` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 2,925 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_a770139e_vm-in-caps-simdna` / `winpath-near-miss` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 3,030 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=63/95 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
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
| `balanced-parens-rec` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 205,769,279.0 | 198,214,227.0 | 210,278,785.0 | 4,008,486.7 | 5 | 27,360 | 24,136 | 23,905 | 0.019 | compiled=5 | 1,540,009.0 | 204,142,341.0 | 101,431.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 199,479,653.0 | 198,232,017.0 | 211,704,034.0 | 5,162,911.6 | 5 | 27,360 | 24,354 | 24,123 | 0.026 | compiled=5 | 1,518,798.0 | 197,071,870.0 | 192,531.0 |
| `balanced-parens-rec` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 198,590,030.0 | 194,674,858.0 | 204,379,771.0 | 3,686,466.6 | 5 | 27,360 | 24,136 | 23,905 | 0.019 | compiled=5 | 1,510,868.0 | 196,888,940.0 | 196,441.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 205,555,009.0 | 197,561,324.0 | 214,228,495.0 | 6,103,978.5 | 5 | 27,360 | 24,354 | 24,123 | 0.030 | compiled=5 | 1,518,209.0 | 202,335,441.0 | 99,761.0 |
| `balanced-parens-rec` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 206,407,596.0 | 203,755,860.0 | 208,945,558.0 | 1,794,422.5 | 5 | 27,360 | 24,134 | 23,903 | 0.009 (max is trial 1) | compiled=5 | 1,521,949.0 | 204,637,715.0 | 188,901.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 206,611,816.0 | 196,483,629.0 | 208,057,114.0 | 5,097,142.7 | 5 | 27,360 | 24,352 | 24,121 | 0.025 | compiled=5 | 1,547,148.0 | 204,475,314.0 | 188,051.0 |
| `balanced-parens-rec` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 202,595,873.0 | 195,029,862.0 | 208,411,526.0 | 4,796,294.2 | 5 | 27,360 | 24,134 | 23,903 | 0.024 | compiled=5 | 1,546,568.0 | 201,157,266.0 | 204,011.0 |
| `balanced-parens-rec` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 205,140,568.0 | 197,926,878.0 | 209,575,992.0 | 3,765,894.5 | 5 | 27,360 | 24,352 | 24,121 | 0.018 (max is trial 1) | compiled=5 | 1,537,629.0 | 203,501,799.0 | 98,961.0 |
| `base10num-near-miss` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 137,433,708.0 | 136,196,942.0 | 146,262,798.0 | 3,731,127.8 | 5 | 23,376 | 15,184 | 12,799 | 0.027 (max is trial 1) | compiled=5 | 1,303,427.0 | 135,757,048.0 | 99,771.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 128,835,777.0 | 128,257,486.0 | 129,350,222.0 | 385,974.4 | 5 | 23,296 | 14,637 | 12,252 | 0.003 (max is trial 1) | compiled=5 | 1,481,559.0 | 126,979,778.0 | 107,230.0 |
| `base10num-near-miss` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 148,454,912.0 | 134,338,864.0 | 149,495,128.0 | 5,687,586.6 | 5 | 23,376 | 15,184 | 12,799 | 0.038 | compiled=5 | 1,499,918.0 | 146,809,653.0 | 190,271.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 144,308,509.0 | 139,099,861.0 | 151,140,648.0 | 3,884,297.0 | 5 | 23,296 | 14,637 | 12,252 | 0.027 | compiled=5 | 1,488,578.0 | 142,743,291.0 | 197,201.0 |
| `base10num-near-miss` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 178,097,805.0 | 177,160,179.0 | 187,709,119.0 | 3,908,553.8 | 5 | 27,200 | 21,115 | 21,115 | 0.022 (max is trial 1) | compiled=5 | 1,609,629.0 | 175,811,402.0 | 185,041.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 177,324,911.0 | 176,801,057.0 | 184,454,811.0 | 2,859,762.3 | 5 | 27,200 | 21,228 | 21,228 | 0.016 | compiled=5 | 1,489,519.0 | 175,860,162.0 | 104,421.0 |
| `base10num-near-miss` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 177,824,208.0 | 175,236,684.0 | 185,151,918.0 | 3,514,915.4 | 5 | 27,200 | 21,115 | 21,115 | 0.020 | compiled=5 | 1,505,499.0 | 176,113,408.0 | 110,761.0 |
| `base10num-near-miss` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 184,087,511.0 | 173,708,246.0 | 189,954,205.0 | 6,658,801.8 | 5 | 27,200 | 21,228 | 21,228 | 0.036 | compiled=5 | 2,993,067.0 | 180,883,114.0 | 108,450.0 |
| `bracket-array-define` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 216,755,481.0 | 208,529,086.0 | 218,046,652.0 | 3,433,876.9 | 5 | 27,400 | 24,931 | 24,616 | 0.016 | compiled=5 | 1,539,409.0 | 214,554,640.0 | 107,530.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 216,983,895.0 | 205,723,289.0 | 226,150,646.0 | 6,697,540.7 | 5 | 27,400 | 25,044 | 24,729 | 0.031 | compiled=5 | 2,923,757.0 | 215,345,395.0 | 182,881.0 |
| `bracket-array-define` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 206,721,294.0 | 199,748,937.0 | 214,486,017.0 | 4,676,550.7 | 5 | 27,400 | 24,932 | 24,616 | 0.023 (max is trial 1) | compiled=5 | 1,616,149.0 | 204,520,172.0 | 100,521.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 213,573,673.0 | 204,917,225.0 | 215,454,884.0 | 3,895,698.1 | 5 | 27,400 | 25,045 | 24,729 | 0.018 | compiled=5 | 1,553,909.0 | 211,851,533.0 | 109,731.0 |
| `bracket-array-define` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 214,395,099.0 | 207,420,930.0 | 216,963,095.0 | 3,306,490.2 | 5 | 27,400 | 24,929 | 24,614 | 0.015 | compiled=5 | 1,555,189.0 | 212,717,331.0 | 108,041.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 208,804,248.0 | 201,432,487.0 | 215,609,987.0 | 4,961,822.3 | 5 | 27,400 | 25,042 | 24,727 | 0.024 | compiled=5 | 1,539,149.0 | 207,036,438.0 | 110,731.0 |
| `bracket-array-define` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 215,855,427.0 | 209,589,662.0 | 217,561,436.0 | 2,926,942.2 | 5 | 27,400 | 24,929 | 24,614 | 0.014 | compiled=5 | 1,568,648.0 | 214,179,218.0 | 198,621.0 |
| `bracket-array-define` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 215,383,613.0 | 214,966,482.0 | 218,244,949.0 | 1,202,914.1 | 5 | 27,400 | 25,042 | 24,727 | 0.006 | compiled=5 | 1,585,099.0 | 213,733,905.0 | 104,100.0 |
| `codegrammar-flat` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 347,661,904.0 | 346,954,890.0 | 358,868,188.0 | 4,520,025.9 | 5 | 31,808 | 34,117 | 25,518 | 0.013 | compiled=5 | 1,998,191.0 | 345,519,392.0 | 195,721.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 347,295,360.0 | 344,886,278.0 | 353,462,897.0 | 3,013,039.8 | 5 | 31,856 | 33,838 | 26,326 | 0.009 | compiled=5 | 2,039,032.0 | 344,220,744.0 | 193,511.0 |
| `codegrammar-flat` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 173,105,680.0 | 171,673,430.0 | 175,800,954.0 | 1,631,873.0 | 5 | 27,832 | 28,158 | 15,208 | 0.009 | compiled=5 | 2,096,302.0 | 170,150,683.0 | 112,340.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 168,705,563.0 | 162,387,419.0 | 172,770,507.0 | 3,404,101.6 | 5 | 27,888 | 26,408 | 15,857 | 0.020 | compiled=5 | 2,440,923.0 | 166,048,589.0 | 191,521.0 |
| `codegrammar-flat` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 310,312,292.0 | 304,330,227.0 | 313,885,051.0 | 3,348,969.9 | 5 | 27,200 | 21,203 | 20,741 | 0.011 | compiled=5 | 1,524,098.0 | 308,628,822.0 | 107,051.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 312,821,345.0 | 309,785,228.0 | 317,716,833.0 | 2,884,106.7 | 5 | 27,200 | 21,314 | 20,852 | 0.009 | compiled=5 | 1,521,589.0 | 309,678,937.0 | 189,351.0 |
| `codegrammar-flat` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 310,799,648.0 | 303,272,108.0 | 312,789,070.0 | 3,471,394.1 | 5 | 27,200 | 21,203 | 20,741 | 0.011 (max is trial 1) | compiled=5 | 1,499,399.0 | 309,187,139.0 | 113,110.0 |
| `codegrammar-flat` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 317,342,674.0 | 301,922,289.0 | 319,659,678.0 | 7,785,572.6 | 5 | 27,200 | 21,314 | 20,852 | 0.025 (max is trial 1) | compiled=5 | 1,534,269.0 | 315,704,535.0 | 114,931.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 346,833,520.0 | 339,148,124.0 | 347,569,403.0 | 3,199,213.7 | 5 | 31,848 | 34,443 | 25,765 | 0.009 | compiled=5 | 1,996,022.0 | 344,728,957.0 | 206,951.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 353,321,916.0 | 348,375,089.0 | 366,739,513.0 | 6,459,013.7 | 5 | 31,896 | 34,166 | 26,575 | 0.018 | compiled=5 | 1,982,952.0 | 351,145,623.0 | 201,481.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 167,626,348.0 | 165,555,316.0 | 175,657,874.0 | 4,153,183.9 | 5 | 27,872 | 28,435 | 15,405 | 0.025 | compiled=5 | 2,088,092.0 | 165,347,855.0 | 101,480.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 168,135,031.0 | 164,821,153.0 | 170,791,146.0 | 1,981,546.5 | 5 | 27,928 | 26,685 | 16,054 | 0.012 | compiled=5 | 2,046,671.0 | 165,985,649.0 | 110,591.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 309,462,007.0 | 302,536,287.0 | 312,345,352.0 | 4,076,074.5 | 5 | 27,240 | 21,529 | 20,988 | 0.013 | compiled=5 | 1,535,238.0 | 307,378,055.0 | 100,511.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 316,849,389.0 | 303,499,072.0 | 319,401,571.0 | 5,775,578.7 | 5 | 27,240 | 21,642 | 21,101 | 0.018 (max is trial 1) | compiled=5 | 1,539,608.0 | 314,845,736.0 | 99,751.0 |
| `codegrammar-xflag` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 309,930,744.0 | 292,907,641.0 | 311,734,304.0 | 6,936,945.7 | 5 | 27,240 | 21,529 | 20,988 | 0.022 | compiled=5 | 1,535,639.0 | 308,287,074.0 | 100,991.0 |
| `codegrammar-xflag` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 314,331,887.0 | 310,242,285.0 | 323,957,041.0 | 4,989,091.4 | 5 | 27,240 | 21,642 | 21,101 | 0.016 | compiled=5 | 1,418,938.0 | 311,271,720.0 | 201,271.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 219,180,277.0 | 212,415,658.0 | 222,151,372.0 | 3,288,440.9 | 5 | 31,824 | 31,405 | 25,774 | 0.015 | compiled=5 | 1,863,750.0 | 217,224,336.0 | 107,780.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 225,463,403.0 | 219,159,637.0 | 227,028,721.0 | 3,023,907.9 | 5 | 31,920 | 33,431 | 27,182 | 0.013 | compiled=5 | 1,946,952.0 | 223,399,022.0 | 109,810.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 220,044,230.0 | 211,554,772.0 | 226,863,637.0 | 4,860,130.8 | 5 | 31,824 | 31,405 | 25,774 | 0.022 | compiled=5 | 1,869,251.0 | 217,539,344.0 | 111,461.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 224,922,955.0 | 217,732,176.0 | 226,947,936.0 | 3,855,502.6 | 5 | 31,920 | 33,431 | 27,182 | 0.017 | compiled=5 | 1,939,580.0 | 222,775,854.0 | 102,021.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 188,481,314.0 | 187,108,346.0 | 197,529,984.0 | 4,675,145.1 | 5 | 27,288 | 21,594 | 21,363 | 0.025 | compiled=5 | 1,534,748.0 | 187,043,615.0 | 107,331.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 195,091,901.0 | 194,262,666.0 | 195,864,165.0 | 553,794.6 | 5 | 27,288 | 21,707 | 21,476 | 0.003 (max is trial 1) | compiled=5 | 1,537,929.0 | 193,205,040.0 | 188,771.0 |
| `currency-lookbehind-fixed` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 194,280,409.0 | 193,859,686.0 | 203,086,457.0 | 3,486,123.3 | 5 | 27,288 | 21,594 | 21,363 | 0.018 | compiled=5 | 1,567,629.0 | 192,645,499.0 | 102,741.0 |
| `currency-lookbehind-fixed` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 194,804,881.0 | 188,731,427.0 | 200,168,520.0 | 3,645,045.9 | 5 | 27,288 | 21,707 | 21,476 | 0.019 (max is trial 1) | compiled=5 | 1,567,869.0 | 192,940,591.0 | 189,601.0 |
| `date-nested-plus` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 255,407,744.0 | 252,215,597.0 | 256,549,441.0 | 1,461,495.4 | 5 | 31,696 | 32,231 | 30,205 | 0.006 | compiled=5 | 1,715,879.0 | 253,556,414.0 | 106,911.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 253,314,234.0 | 246,915,126.0 | 261,581,501.0 | 4,894,061.3 | 5 | 31,696 | 32,159 | 30,133 | 0.019 | compiled=5 | 1,732,410.0 | 251,510,603.0 | 193,581.0 |
| `date-nested-plus` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 135,931,503.0 | 128,762,863.0 | 141,972,506.0 | 4,465,175.1 | 5 | 23,184 | 13,167 | 11,372 | 0.033 | compiled=5 | 1,442,808.0 | 134,386,495.0 | 107,831.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 140,164,256.0 | 127,754,987.0 | 149,258,737.0 | 7,023,767.8 | 5 | 23,184 | 12,990 | 11,195 | 0.050 (max is trial 1) | compiled=5 | 1,453,128.0 | 138,643,918.0 | 119,120.0 |
| `date-nested-plus` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 241,964,096.0 | 235,245,447.0 | 242,757,740.0 | 2,802,090.1 | 5 | 27,400 | 27,803 | 27,572 | 0.012 | compiled=5 | 1,613,539.0 | 240,246,176.0 | 98,980.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 235,433,709.0 | 233,087,884.0 | 244,307,399.0 | 4,453,816.2 | 5 | 27,400 | 27,916 | 27,685 | 0.019 (max is trial 1) | compiled=5 | 1,602,119.0 | 233,637,998.0 | 111,401.0 |
| `date-nested-plus` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 243,224,247.0 | 242,343,463.0 | 244,581,575.0 | 797,403.4 | 5 | 27,400 | 27,803 | 27,572 | 0.003 | compiled=5 | 1,627,629.0 | 241,422,227.0 | 110,271.0 |
| `date-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 244,688,514.0 | 242,732,853.0 | 247,074,628.0 | 1,523,250.4 | 5 | 27,400 | 27,916 | 27,685 | 0.006 | compiled=5 | 1,686,090.0 | 242,343,162.0 | 102,631.0 |
| `doubled-word` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 212,922,481.0 | 203,558,808.0 | 217,000,134.0 | 5,044,880.0 | 5 | 27,328 | 23,193 | 22,731 | 0.024 (max is trial 1) | compiled=5 | 1,522,959.0 | 211,296,622.0 | 108,451.0 |
| `doubled-word` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 211,764,734.0 | 208,263,524.0 | 221,473,860.0 | 4,455,832.0 | 5 | 27,328 | 23,306 | 22,844 | 0.021 | compiled=5 | 1,575,739.0 | 210,010,394.0 | 118,661.0 |
| `doubled-word` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 214,907,020.0 | 210,856,078.0 | 218,153,658.0 | 2,703,784.4 | 5 | 27,328 | 23,175 | 22,713 | 0.013 | compiled=5 | 1,524,399.0 | 213,220,631.0 | 192,691.0 |
| `doubled-word` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 210,040,034.0 | 203,571,168.0 | 213,763,794.0 | 3,985,800.4 | 5 | 27,328 | 23,288 | 22,826 | 0.019 | compiled=5 | 1,531,629.0 | 208,427,954.0 | 184,661.0 |
| `doubled-word` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 207,031,068.0 | 204,530,634.0 | 213,125,183.0 | 3,506,131.2 | 5 | 27,328 | 23,191 | 22,729 | 0.017 | compiled=5 | 1,846,580.0 | 204,101,812.0 | 106,521.0 |
| `doubled-word` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 213,525,795.0 | 209,520,572.0 | 216,650,642.0 | 2,423,287.1 | 5 | 27,328 | 23,304 | 22,842 | 0.011 | compiled=5 | 1,598,029.0 | 211,871,246.0 | 120,131.0 |
| `doubled-word` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 208,654,256.0 | 200,742,494.0 | 212,854,151.0 | 4,582,172.8 | 5 | 27,328 | 23,191 | 22,729 | 0.022 (max is trial 1) | compiled=5 | 1,639,338.0 | 205,364,179.0 | 198,631.0 |
| `doubled-word` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 212,292,946.0 | 204,987,607.0 | 218,874,343.0 | 4,703,833.1 | 5 | 27,328 | 23,304 | 22,842 | 0.022 | compiled=5 | 1,530,118.0 | 210,559,877.0 | 108,111.0 |
| `dup-param-detect` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 227,313,583.0 | 225,131,582.0 | 231,844,949.0 | 2,320,710.5 | 5 | 27,448 | 25,747 | 25,285 | 0.010 (max is trial 1) | compiled=5 | 1,630,709.0 | 225,476,723.0 | 113,021.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 225,362,192.0 | 221,157,518.0 | 227,375,754.0 | 2,122,674.6 | 5 | 27,448 | 25,860 | 25,398 | 0.009 | compiled=5 | 1,583,519.0 | 223,675,242.0 | 204,481.0 |
| `dup-param-detect` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 225,218,477.0 | 222,728,884.0 | 231,095,858.0 | 2,952,074.9 | 5 | 27,448 | 25,729 | 25,267 | 0.013 | compiled=5 | 1,635,229.0 | 223,269,156.0 | 101,230.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 227,794,982.0 | 224,677,814.0 | 236,811,702.0 | 4,672,252.0 | 5 | 27,448 | 25,842 | 25,380 | 0.021 (max is trial 1) | compiled=5 | 1,614,118.0 | 224,474,943.0 | 108,650.0 |
| `dup-param-detect` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 220,226,962.0 | 219,153,646.0 | 227,317,903.0 | 3,043,875.3 | 5 | 27,448 | 25,745 | 25,283 | 0.014 | compiled=5 | 1,583,999.0 | 217,730,779.0 | 191,571.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 226,370,477.0 | 223,315,739.0 | 227,897,907.0 | 1,617,423.2 | 5 | 27,448 | 25,858 | 25,396 | 0.007 | compiled=5 | 1,564,259.0 | 224,690,848.0 | 115,370.0 |
| `dup-param-detect` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 226,162,683.0 | 216,708,371.0 | 239,766,887.0 | 7,884,806.0 | 5 | 27,448 | 25,745 | 25,283 | 0.035 | compiled=5 | 1,600,569.0 | 224,506,164.0 | 121,780.0 |
| `dup-param-detect` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 226,684,676.0 | 215,371,354.0 | 228,357,835.0 | 5,347,054.0 | 5 | 27,448 | 25,858 | 25,396 | 0.024 | compiled=5 | 1,604,999.0 | 224,990,746.0 | 188,991.0 |
| `email-local-nodup` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 192,910,726.0 | 190,687,893.0 | 202,873,824.0 | 4,301,953.2 | 5 | 31,536 | 25,737 | 23,664 | 0.022 | compiled=5 | 1,625,029.0 | 191,094,496.0 | 191,201.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 190,115,011.0 | 183,760,754.0 | 215,956,008.0 | 11,386,735.8 | 5 | 31,536 | 26,155 | 24,011 | 0.060 | compiled=5 | 1,612,989.0 | 188,420,551.0 | 196,211.0 |
| `email-local-nodup` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 201,581,766.0 | 190,103,373.0 | 206,693,054.0 | 5,503,087.0 | 5 | 31,536 | 25,737 | 23,664 | 0.027 | compiled=5 | 1,610,189.0 | 199,795,877.0 | 109,191.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 197,102,242.0 | 193,165,920.0 | 197,515,623.0 | 1,613,037.6 | 5 | 31,536 | 26,155 | 24,011 | 0.008 | compiled=5 | 1,620,849.0 | 195,368,632.0 | 185,501.0 |
| `email-local-nodup` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 190,142,444.0 | 180,295,479.0 | 196,727,750.0 | 6,264,194.3 | 5 | 27,280 | 22,077 | 21,615 | 0.033 | compiled=5 | 1,582,099.0 | 188,419,753.0 | 110,841.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 195,047,400.0 | 187,513,198.0 | 195,457,203.0 | 3,080,534.8 | 5 | 27,240 | 22,190 | 21,728 | 0.016 | compiled=5 | 1,541,389.0 | 193,399,162.0 | 106,651.0 |
| `email-local-nodup` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 186,392,964.0 | 178,959,854.0 | 195,173,162.0 | 5,697,805.6 | 5 | 27,280 | 22,077 | 21,615 | 0.031 (max is trial 1) | compiled=5 | 1,539,269.0 | 184,858,186.0 | 190,541.0 |
| `email-local-nodup` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 188,288,505.0 | 185,329,418.0 | 197,460,695.0 | 4,522,060.1 | 5 | 27,240 | 22,190 | 21,728 | 0.024 (max is trial 1) | compiled=5 | 1,525,559.0 | 186,409,665.0 | 189,891.0 |
| `email-nested-plus` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 219,240,296.0 | 218,983,855.0 | 225,794,876.0 | 2,620,133.4 | 5 | 31,648 | 27,613 | 25,667 | 0.012 | compiled=5 | 1,635,620.0 | 217,394,296.0 | 101,911.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 219,482,949.0 | 218,851,725.0 | 224,389,697.0 | 2,074,897.8 | 5 | 31,648 | 28,044 | 26,014 | 0.009 (max is trial 1) | compiled=5 | 1,640,969.0 | 217,609,227.0 | 102,131.0 |
| `email-nested-plus` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 139,685,254.0 | 129,849,328.0 | 142,325,099.0 | 4,376,982.8 | 5 | 23,184 | 12,672 | 10,957 | 0.031 | compiled=5 | 1,528,628.0 | 138,006,864.0 | 101,671.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 129,664,719.0 | 127,473,566.0 | 143,395,534.0 | 5,878,610.5 | 5 | 23,184 | 12,998 | 11,199 | 0.045 | compiled=5 | 1,468,458.0 | 126,991,963.0 | 106,691.0 |
| `email-nested-plus` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 208,540,107.0 | 202,885,375.0 | 209,995,664.0 | 2,550,194.4 | 5 | 27,360 | 23,684 | 23,453 | 0.012 | compiled=5 | 1,542,839.0 | 206,902,917.0 | 100,891.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 209,117,520.0 | 201,448,565.0 | 213,064,722.0 | 4,079,442.5 | 5 | 27,360 | 23,797 | 23,566 | 0.020 (max is trial 1) | compiled=5 | 1,541,578.0 | 207,408,870.0 | 195,682.0 |
| `email-nested-plus` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 207,416,750.0 | 203,600,639.0 | 210,919,559.0 | 2,639,821.5 | 5 | 27,360 | 23,684 | 23,453 | 0.013 | compiled=5 | 1,600,059.0 | 205,793,992.0 | 106,181.0 |
| `email-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 202,898,955.0 | 197,494,254.0 | 209,900,154.0 | 4,686,146.0 | 5 | 27,360 | 23,797 | 23,566 | 0.023 | compiled=5 | 1,550,148.0 | 201,257,446.0 | 189,351.0 |
| `evil-alt-nested` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 212,886,150.0 | 205,844,731.0 | 214,159,997.0 | 3,011,927.2 | 5 | 27,360 | 24,150 | 24,150 | 0.014 (max is trial 1) | compiled=5 | 1,526,479.0 | 210,926,469.0 | 104,370.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 211,487,894.0 | 203,224,876.0 | 213,466,934.0 | 3,562,098.0 | 5 | 27,360 | 24,263 | 24,263 | 0.017 | compiled=5 | 1,531,629.0 | 209,855,803.0 | 188,131.0 |
| `evil-alt-nested` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 132,950,886.0 | 126,641,801.0 | 140,234,027.0 | 5,044,250.2 | 5 | 23,144 | 12,659 | 11,048 | 0.038 | compiled=5 | 1,410,418.0 | 131,279,707.0 | 193,861.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 132,606,954.0 | 124,524,040.0 | 136,905,909.0 | 4,943,832.4 | 5 | 23,104 | 12,482 | 10,871 | 0.037 | compiled=5 | 1,451,408.0 | 130,964,825.0 | 184,451.0 |
| `evil-alt-nested` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 213,407,464.0 | 210,426,197.0 | 221,861,492.0 | 4,034,447.4 | 5 | 27,360 | 24,131 | 24,131 | 0.019 | compiled=5 | 1,567,639.0 | 210,207,066.0 | 192,591.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 210,388,498.0 | 203,045,415.0 | 212,749,052.0 | 3,479,090.6 | 5 | 27,360 | 24,244 | 24,244 | 0.017 (max is trial 1) | compiled=5 | 1,707,549.0 | 208,683,908.0 | 191,511.0 |
| `evil-alt-nested` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 212,809,019.0 | 206,117,603.0 | 216,731,901.0 | 3,580,355.0 | 5 | 27,360 | 24,131 | 24,131 | 0.017 (max is trial 1) | compiled=5 | 1,557,398.0 | 211,156,711.0 | 205,191.0 |
| `evil-alt-nested` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 210,557,119.0 | 202,988,026.0 | 212,622,118.0 | 3,801,797.9 | 5 | 27,360 | 24,244 | 24,244 | 0.018 | compiled=5 | 1,547,289.0 | 208,818,578.0 | 187,821.0 |
| `file-ext-order` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 146,970,911.0 | 140,957,149.0 | 153,080,207.0 | 4,022,100.9 | 5 | 27,608 | 19,411 | 13,288 | 0.027 | compiled=5 | 1,776,540.0 | 145,093,661.0 | 174,881.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 159,880,117.0 | 151,467,329.0 | 162,028,538.0 | 3,867,160.0 | 5 | 27,752 | 22,371 | 15,305 | 0.024 | compiled=5 | 1,856,591.0 | 157,832,935.0 | 191,101.0 |
| `file-ext-order` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 153,754,861.0 | 141,031,932.0 | 153,959,232.0 | 5,030,558.0 | 5 | 27,608 | 19,411 | 13,288 | 0.033 | compiled=5 | 1,793,590.0 | 151,758,730.0 | 184,661.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 162,118,378.0 | 161,131,442.0 | 163,209,984.0 | 829,259.0 | 5 | 27,752 | 22,371 | 15,305 | 0.005 | compiled=5 | 1,858,780.0 | 160,057,687.0 | 200,171.0 |
| `file-ext-order` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 162,958,130.0 | 162,644,598.0 | 172,713,115.0 | 4,361,866.7 | 5 | 23,104 | 19,287 | 19,287 | 0.027 (max is trial 1) | compiled=5 | 1,475,509.0 | 161,577,402.0 | 118,271.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 171,712,498.0 | 159,257,579.0 | 172,043,531.0 | 4,894,463.9 | 5 | 23,104 | 19,400 | 19,400 | 0.029 | compiled=5 | 1,459,478.0 | 168,711,352.0 | 190,051.0 |
| `file-ext-order` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 171,459,911.0 | 155,780,236.0 | 173,722,335.0 | 6,605,493.2 | 5 | 23,104 | 19,287 | 19,287 | 0.039 | compiled=5 | 1,480,518.0 | 169,676,942.0 | 199,421.0 |
| `file-ext-order` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 172,571,128.0 | 162,930,936.0 | 174,772,591.0 | 4,362,859.6 | 5 | 23,104 | 19,400 | 19,400 | 0.025 | compiled=5 | 1,485,928.0 | 170,981,189.0 | 186,691.0 |
| `float-literal-bound` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 232,847,496.0 | 226,702,790.0 | 234,673,914.0 | 2,722,748.5 | 5 | 31,752 | 32,187 | 27,038 | 0.012 | compiled=5 | 1,901,441.0 | 230,836,524.0 | 113,801.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 236,207,964.0 | 227,830,996.0 | 243,768,529.0 | 5,280,704.1 | 5 | 31,848 | 33,029 | 27,571 | 0.022 (max is trial 1) | compiled=5 | 3,700,201.0 | 232,420,693.0 | 198,642.0 |
| `float-literal-bound` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 233,677,933.0 | 225,655,759.0 | 234,515,419.0 | 3,995,752.6 | 5 | 31,752 | 32,187 | 27,038 | 0.017 | compiled=5 | 1,988,361.0 | 231,634,922.0 | 104,140.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 232,764,058.0 | 227,856,612.0 | 233,102,152.0 | 2,016,848.6 | 5 | 31,848 | 33,029 | 27,571 | 0.009 | compiled=5 | 1,931,731.0 | 230,759,638.0 | 107,591.0 |
| `float-literal-bound` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 195,343,102.0 | 190,457,164.0 | 198,892,823.0 | 2,755,193.1 | 5 | 27,288 | 22,127 | 21,896 | 0.014 | compiled=5 | 1,701,850.0 | 192,245,135.0 | 102,100.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 193,886,974.0 | 193,637,613.0 | 200,114,099.0 | 2,621,637.5 | 5 | 27,288 | 22,240 | 22,009 | 0.014 | compiled=5 | 1,547,399.0 | 192,233,265.0 | 106,310.0 |
| `float-literal-bound` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 197,712,126.0 | 195,488,694.0 | 199,420,026.0 | 1,442,537.7 | 5 | 27,288 | 22,127 | 21,896 | 0.007 | compiled=5 | 1,528,408.0 | 195,861,906.0 | 209,431.0 |
| `float-literal-bound` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 201,044,635.0 | 194,127,276.0 | 202,178,140.0 | 3,559,743.0 | 5 | 27,288 | 22,240 | 22,009 | 0.018 (max is trial 1) | compiled=5 | 1,547,478.0 | 198,930,613.0 | 185,411.0 |
| `floor-byte` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 140,792,388.0 | 138,291,042.0 | 152,334,334.0 | 5,591,134.1 | 5 | 27,608 | 18,268 | 13,271 | 0.040 | compiled=5 | 1,794,040.0 | 138,922,137.0 | 202,031.0 |
| `floor-byte` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 152,365,955.0 | 150,328,813.0 | 161,121,105.0 | 4,045,846.3 | 5 | 27,752 | 20,611 | 15,288 | 0.027 | compiled=5 | 1,705,100.0 | 150,707,274.0 | 106,551.0 |
| `floor-byte` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 147,166,245.0 | 145,756,798.0 | 150,963,515.0 | 2,044,692.0 | 5 | 27,608 | 18,268 | 13,271 | 0.014 | compiled=5 | 1,662,549.0 | 145,407,515.0 | 101,111.0 |
| `floor-byte` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 159,278,133.0 | 148,393,072.0 | 164,114,059.0 | 5,976,071.1 | 5 | 27,752 | 20,611 | 15,288 | 0.038 | compiled=5 | 1,681,380.0 | 157,422,562.0 | 195,581.0 |
| `floor-byte` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 141,481,758.0 | 126,745,595.0 | 142,731,315.0 | 6,217,796.6 | 5 | 23,072 | 17,811 | 17,811 | 0.044 | compiled=5 | 1,461,528.0 | 139,860,749.0 | 183,941.0 |
| `floor-byte` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 141,060,166.0 | 127,127,267.0 | 142,405,663.0 | 6,754,553.5 | 5 | 23,072 | 17,922 | 17,922 | 0.048 | compiled=5 | 1,443,628.0 | 139,516,557.0 | 108,891.0 |
| `floor-byte` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 134,304,958.0 | 131,278,842.0 | 138,813,343.0 | 2,677,151.0 | 5 | 23,072 | 17,811 | 17,811 | 0.020 | compiled=5 | 1,447,048.0 | 131,361,982.0 | 99,090.0 |
| `floor-byte` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 142,031,450.0 | 131,354,712.0 | 146,808,797.0 | 6,044,077.4 | 5 | 23,072 | 17,922 | 17,922 | 0.043 (max is trial 1) | compiled=5 | 1,448,118.0 | 140,501,502.0 | 100,340.0 |
| `high-byte-run` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 160,713,003.0 | 156,845,169.0 | 163,927,570.0 | 2,650,867.0 | 5 | 23,216 | 24,517 | 18,211 | 0.016 | compiled=5 | 1,834,730.0 | 156,686,359.0 | 205,801.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 162,428,112.0 | 157,343,703.0 | 162,796,445.0 | 2,059,415.3 | 5 | 27,744 | 23,219 | 16,092 | 0.013 | compiled=5 | 1,816,500.0 | 159,406,984.0 | 104,030.0 |
| `high-byte-run` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 168,383,872.0 | 157,281,551.0 | 171,273,099.0 | 4,814,835.6 | 5 | 23,216 | 24,517 | 18,211 | 0.029 | compiled=5 | 1,797,030.0 | 166,383,491.0 | 194,201.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 165,369,067.0 | 152,509,345.0 | 166,337,362.0 | 5,256,515.0 | 5 | 27,744 | 23,219 | 16,092 | 0.032 | compiled=5 | 1,809,420.0 | 163,438,226.0 | 115,791.0 |
| `high-byte-run` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 158,191,082.0 | 152,271,759.0 | 164,210,686.0 | 4,654,472.5 | 5 | 23,072 | 18,356 | 18,356 | 0.029 | compiled=5 | 1,583,479.0 | 156,368,952.0 | 191,291.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 167,551,675.0 | 160,557,076.0 | 169,110,095.0 | 3,019,373.4 | 5 | 23,072 | 18,467 | 18,467 | 0.018 (max is trial 1) | compiled=5 | 1,473,578.0 | 165,901,976.0 | 206,621.0 |
| `high-byte-run` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 160,377,022.0 | 149,972,045.0 | 163,942,911.0 | 5,003,103.6 | 5 | 23,072 | 18,356 | 18,356 | 0.031 | compiled=5 | 1,481,799.0 | 158,822,433.0 | 187,081.0 |
| `high-byte-run` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 166,691,556.0 | 155,398,165.0 | 171,901,046.0 | 5,460,890.5 | 5 | 23,072 | 18,467 | 18,467 | 0.033 (max is trial 1) | compiled=5 | 1,482,409.0 | 165,125,527.0 | 111,610.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 165,536,208.0 | 144,881,761.0 | 168,201,655.0 | 8,549,039.6 | 5 | 32,424 | 22,028 | 16,712 | 0.052 | compiled=5 | 1,687,819.0 | 163,726,199.0 | 168,481.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 164,295,363.0 | 150,576,884.0 | 166,153,054.0 | 5,714,252.5 | 5 | 32,224 | 21,106 | 15,790 | 0.035 (max is trial 1) | compiled=5 | 1,675,489.0 | 161,498,246.0 | 204,042.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 159,180,661.0 | 152,439,544.0 | 169,399,778.0 | 6,492,627.4 | 5 | 32,424 | 22,028 | 16,712 | 0.041 | compiled=5 | 1,792,370.0 | 155,012,158.0 | 109,061.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 154,281,375.0 | 142,441,009.0 | 162,172,468.0 | 6,813,408.1 | 5 | 32,224 | 21,106 | 15,790 | 0.044 | compiled=5 | 1,906,820.0 | 150,800,115.0 | 96,330.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 258,961,901.0 | 248,336,011.0 | 261,186,873.0 | 4,538,341.3 | 5 | 27,200 | 30,877 | 30,877 | 0.018 | compiled=5 | 1,674,300.0 | 257,096,930.0 | 118,041.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 259,615,504.0 | 249,194,515.0 | 260,269,429.0 | 4,213,933.8 | 5 | 27,200 | 30,990 | 30,990 | 0.016 | compiled=5 | 1,909,831.0 | 256,461,357.0 | 108,330.0 |
| `ipv4-near-miss` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 257,177,624.0 | 255,119,052.0 | 261,997,960.0 | 2,506,269.4 | 5 | 27,200 | 30,877 | 30,877 | 0.010 | compiled=5 | 1,752,940.0 | 255,393,344.0 | 190,561.0 |
| `ipv4-near-miss` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 251,508,342.0 | 249,153,959.0 | 258,661,800.0 | 4,031,258.9 | 5 | 27,200 | 30,990 | 30,990 | 0.016 (max is trial 1) | compiled=5 | 1,677,459.0 | 249,903,304.0 | 105,631.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 155,003,098.0 | 143,451,273.0 | 156,065,115.0 | 4,665,602.4 | 5 | 27,608 | 20,231 | 13,617 | 0.030 (max is trial 1) | compiled=5 | 1,821,780.0 | 152,062,532.0 | 197,301.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 163,075,295.0 | 155,210,060.0 | 166,880,567.0 | 3,877,927.9 | 5 | 27,752 | 24,536 | 15,710 | 0.024 | compiled=5 | 1,955,892.0 | 161,021,124.0 | 191,541.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 152,418,594.0 | 146,929,385.0 | 155,151,909.0 | 2,779,680.8 | 5 | 27,608 | 20,231 | 13,617 | 0.018 | compiled=5 | 1,928,490.0 | 149,939,491.0 | 106,101.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 158,529,547.0 | 153,534,051.0 | 166,738,704.0 | 5,243,004.0 | 5 | 27,752 | 24,536 | 15,710 | 0.033 | compiled=5 | 1,961,251.0 | 156,026,934.0 | 98,671.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 170,310,911.0 | 159,708,952.0 | 174,361,834.0 | 5,570,729.6 | 5 | 23,104 | 19,763 | 19,763 | 0.033 (max is trial 1) | compiled=5 | 1,465,979.0 | 168,665,872.0 | 184,621.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 172,348,353.0 | 167,302,594.0 | 174,760,786.0 | 2,509,389.5 | 5 | 23,104 | 19,876 | 19,876 | 0.015 | compiled=5 | 1,470,958.0 | 170,762,944.0 | 100,360.0 |
| `keyword-prefix-order` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 171,761,745.0 | 156,443,379.0 | 173,331,462.0 | 6,755,922.5 | 5 | 23,104 | 19,763 | 19,763 | 0.039 | compiled=5 | 1,510,268.0 | 169,961,374.0 | 99,160.0 |
| `keyword-prefix-order` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 163,061,456.0 | 160,781,534.0 | 172,875,690.0 | 5,355,309.0 | 5 | 23,104 | 19,876 | 19,876 | 0.033 | compiled=5 | 1,467,688.0 | 161,436,538.0 | 187,781.0 |
| `logparse-atomic` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 311,569,557.0 | 303,194,898.0 | 316,586,767.0 | 4,365,882.6 | 5 | 82,840 | 62,348 | 42,415 | 0.014 (max is trial 1) | compiled=5 | 2,425,264.0 | 309,021,082.0 | 123,211.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 313,232,566.0 | 299,711,909.0 | 315,471,368.0 | 5,951,249.2 | 5 | 82,800 | 62,275 | 42,342 | 0.019 | compiled=5 | 2,527,154.0 | 307,933,376.0 | 118,851.0 |
| `logparse-atomic` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 301,600,680.0 | 298,983,376.0 | 307,809,544.0 | 3,613,096.7 | 5 | 82,840 | 62,040 | 42,107 | 0.012 | compiled=5 | 2,428,843.0 | 298,953,076.0 | 217,461.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 312,176,090.0 | 309,710,295.0 | 324,770,330.0 | 6,204,654.0 | 5 | 82,800 | 61,967 | 42,034 | 0.020 (max is trial 1) | compiled=5 | 2,425,293.0 | 309,506,504.0 | 127,121.0 |
| `logparse-atomic` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 244,459,080.0 | 240,398,095.0 | 246,003,418.0 | 2,110,537.1 | 5 | 27,240 | 31,981 | 31,750 | 0.009 | compiled=5 | 1,779,640.0 | 242,554,659.0 | 190,741.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 245,585,205.0 | 244,478,500.0 | 246,631,212.0 | 840,214.0 | 5 | 27,240 | 32,094 | 31,863 | 0.003 | compiled=5 | 1,771,720.0 | 243,443,553.0 | 191,181.0 |
| `logparse-atomic` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 246,306,134.0 | 241,296,525.0 | 247,742,982.0 | 2,293,647.4 | 5 | 27,240 | 31,981 | 31,750 | 0.009 | compiled=5 | 1,774,070.0 | 244,320,143.0 | 100,380.0 |
| `logparse-atomic` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 244,292,044.0 | 241,283,458.0 | 247,359,539.0 | 1,986,583.3 | 5 | 27,240 | 32,094 | 31,863 | 0.008 | compiled=5 | 1,753,529.0 | 242,435,593.0 | 115,611.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 310,574,672.0 | 307,704,335.0 | 311,094,623.0 | 1,237,829.5 | 5 | 82,840 | 62,067 | 42,134 | 0.004 | compiled=5 | 2,427,913.0 | 308,025,507.0 | 121,251.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 314,293,571.0 | 309,913,128.0 | 315,619,151.0 | 2,336,858.8 | 5 | 82,800 | 61,994 | 42,061 | 0.007 | compiled=5 | 2,458,544.0 | 311,714,277.0 | 120,750.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 196,387,386.0 | 195,879,695.0 | 199,106,512.0 | 1,376,857.7 | 5 | 74,496 | 39,580 | 19,878 | 0.007 | compiled=5 | 1,979,941.0 | 194,084,485.0 | 219,261.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 201,315,404.0 | 191,757,460.0 | 204,441,293.0 | 4,283,510.0 | 5 | 74,448 | 39,402 | 19,700 | 0.021 | compiled=5 | 2,031,831.0 | 197,826,926.0 | 115,381.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 244,193,628.0 | 240,114,876.0 | 251,248,568.0 | 3,608,987.4 | 5 | 27,240 | 31,700 | 31,469 | 0.015 | compiled=5 | 1,736,940.0 | 242,357,528.0 | 107,821.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 244,328,279.0 | 241,208,181.0 | 245,347,805.0 | 1,573,771.7 | 5 | 27,240 | 31,813 | 31,582 | 0.006 | compiled=5 | 1,839,140.0 | 242,448,708.0 | 107,121.0 |
| `logparse-atomic-removed` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 244,759,136.0 | 237,077,004.0 | 253,169,293.0 | 5,102,125.0 | 5 | 27,240 | 31,700 | 31,469 | 0.021 | compiled=5 | 1,751,970.0 | 242,887,586.0 | 115,381.0 |
| `logparse-atomic-removed` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 243,924,331.0 | 239,933,628.0 | 248,212,965.0 | 2,688,983.7 | 5 | 27,240 | 31,813 | 31,582 | 0.011 | compiled=5 | 1,779,610.0 | 241,831,839.0 | 190,421.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 142,371,046.0 | 139,251,799.0 | 151,683,441.0 | 4,481,501.8 | 5 | 27,608 | 18,891 | 13,301 | 0.031 | compiled=5 | 1,867,401.0 | 139,045,777.0 | 188,061.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 160,452,551.0 | 157,746,184.0 | 161,650,607.0 | 1,400,522.5 | 5 | 27,752 | 21,378 | 15,318 | 0.009 | compiled=5 | 1,821,551.0 | 158,374,878.0 | 200,791.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 146,244,530.0 | 141,154,152.0 | 154,220,205.0 | 4,753,778.6 | 5 | 27,608 | 18,891 | 13,301 | 0.033 | compiled=5 | 1,783,130.0 | 144,388,900.0 | 192,511.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 148,900,974.0 | 146,702,302.0 | 165,713,778.0 | 8,145,554.9 | 5 | 27,752 | 21,378 | 15,318 | 0.055 | compiled=5 | 1,836,020.0 | 146,870,133.0 | 189,881.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 170,341,451.0 | 160,188,913.0 | 173,956,161.0 | 5,754,768.7 | 5 | 23,072 | 19,380 | 19,380 | 0.034 | compiled=5 | 1,473,968.0 | 168,784,133.0 | 188,391.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 173,727,261.0 | 165,792,966.0 | 174,310,083.0 | 3,677,609.0 | 5 | 23,072 | 19,491 | 19,491 | 0.021 | compiled=5 | 1,485,578.0 | 171,991,931.0 | 203,642.0 |
| `mojibake-curly-quote` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 170,868,800.0 | 166,081,941.0 | 172,849,149.0 | 2,245,622.8 | 5 | 23,072 | 19,380 | 19,380 | 0.013 | compiled=5 | 1,497,708.0 | 167,940,993.0 | 108,221.0 |
| `mojibake-curly-quote` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 173,003,160.0 | 164,950,876.0 | 175,029,683.0 | 3,679,479.7 | 5 | 23,072 | 19,491 | 19,491 | 0.021 | compiled=5 | 1,615,819.0 | 169,585,002.0 | 190,271.0 |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a770139e_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `negation-scope-lookbehind-var` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | unsupported-by-declaration=1 | - | - | - |
| `nested-comment-rec` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 280,996,991.0 | 266,486,928.0 | 285,490,267.0 | 7,084,794.1 | 5 | 27,360 | 29,822 | 29,591 | 0.025 | compiled=5 | 1,650,610.0 | 279,270,991.0 | 196,801.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 281,999,998.0 | 272,119,960.0 | 283,406,266.0 | 4,114,656.4 | 5 | 27,360 | 29,935 | 29,704 | 0.015 | compiled=5 | 1,626,020.0 | 280,272,847.0 | 101,131.0 |
| `nested-comment-rec` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 278,263,052.0 | 265,061,089.0 | 280,961,706.0 | 5,854,368.2 | 5 | 27,360 | 29,808 | 29,577 | 0.021 | compiled=5 | 1,631,079.0 | 276,355,021.0 | 106,761.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 282,398,286.0 | 276,622,731.0 | 283,161,568.0 | 2,359,924.4 | 5 | 27,360 | 29,921 | 29,690 | 0.008 | compiled=5 | 2,925,116.0 | 279,402,957.0 | 206,752.0 |
| `nested-comment-rec` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 278,344,670.0 | 274,003,257.0 | 285,208,850.0 | 4,304,444.7 | 5 | 27,360 | 29,820 | 29,589 | 0.015 | compiled=5 | 1,639,899.0 | 276,608,600.0 | 187,801.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 282,600,185.0 | 274,635,139.0 | 289,406,933.0 | 5,208,250.2 | 5 | 27,360 | 29,933 | 29,702 | 0.018 (max is trial 1) | compiled=5 | 3,233,338.0 | 280,343,502.0 | 99,270.0 |
| `nested-comment-rec` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 281,544,677.0 | 273,421,223.0 | 282,689,454.0 | 3,376,594.6 | 5 | 27,360 | 29,820 | 29,589 | 0.012 | compiled=5 | 1,653,629.0 | 279,482,446.0 | 189,071.0 |
| `nested-comment-rec` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 282,076,281.0 | 276,513,851.0 | 283,993,500.0 | 2,943,558.5 | 5 | 27,360 | 29,933 | 29,702 | 0.010 | compiled=5 | 1,673,969.0 | 280,314,931.0 | 119,011.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 215,230,295.0 | 212,576,458.0 | 216,818,323.0 | 1,395,433.3 | 5 | 31,568 | 27,280 | 25,598 | 0.006 | compiled=5 | 1,646,430.0 | 213,481,914.0 | 189,441.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 213,860,888.0 | 205,878,061.0 | 220,869,656.0 | 5,360,505.9 | 5 | 31,568 | 27,209 | 25,527 | 0.025 | compiled=5 | 1,614,869.0 | 212,125,567.0 | 189,031.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 128,367,561.0 | 125,084,452.0 | 138,517,657.0 | 4,878,494.5 | 5 | 23,144 | 12,884 | 11,202 | 0.038 | compiled=5 | 1,587,018.0 | 125,213,293.0 | 96,920.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 126,597,861.0 | 125,865,697.0 | 140,383,758.0 | 5,919,435.8 | 5 | 23,144 | 12,708 | 11,026 | 0.047 | compiled=5 | 1,451,208.0 | 125,035,863.0 | 100,071.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 203,613,418.0 | 194,090,865.0 | 208,280,545.0 | 5,374,310.3 | 5 | 27,320 | 23,125 | 23,125 | 0.026 | compiled=5 | 1,536,569.0 | 201,996,770.0 | 100,380.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 203,076,736.0 | 200,281,410.0 | 213,763,405.0 | 5,115,618.1 | 5 | 27,320 | 23,239 | 23,239 | 0.025 | compiled=5 | 1,539,498.0 | 201,449,187.0 | 106,561.0 |
| `numeric-id-nested-plus` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 204,496,814.0 | 189,327,170.0 | 206,864,627.0 | 6,500,457.9 | 5 | 27,320 | 23,125 | 23,125 | 0.032 | compiled=5 | 2,848,635.0 | 201,880,789.0 | 185,621.0 |
| `numeric-id-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 203,555,739.0 | 194,744,340.0 | 206,057,063.0 | 4,719,252.3 | 5 | 27,320 | 23,239 | 23,239 | 0.023 (max is trial 1) | compiled=5 | 1,548,438.0 | 201,911,070.0 | 99,861.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 221,372,800.0 | 221,053,208.0 | 232,152,411.0 | 4,489,343.3 | 5 | 31,648 | 28,508 | 26,566 | 0.020 (max is trial 1) | compiled=5 | 1,533,719.0 | 219,745,550.0 | 102,111.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 222,415,626.0 | 219,333,778.0 | 226,545,731.0 | 2,792,477.2 | 5 | 31,608 | 28,436 | 26,494 | 0.013 | compiled=5 | 1,706,389.0 | 220,536,315.0 | 187,481.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 129,957,520.0 | 117,925,783.0 | 137,440,422.0 | 7,630,432.9 | 5 | 23,184 | 12,918 | 11,207 | 0.059 | compiled=5 | 1,686,270.0 | 128,178,210.0 | 106,371.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 140,044,236.0 | 133,436,969.0 | 140,269,467.0 | 2,640,237.6 | 5 | 23,144 | 12,741 | 11,030 | 0.019 | compiled=5 | 1,480,908.0 | 138,373,696.0 | 184,361.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 215,945,678.0 | 208,125,084.0 | 217,270,657.0 | 3,911,482.3 | 5 | 27,360 | 24,324 | 24,093 | 0.018 | compiled=5 | 1,562,499.0 | 214,261,489.0 | 105,611.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 215,878,129.0 | 206,545,618.0 | 217,381,447.0 | 3,959,502.9 | 5 | 27,360 | 24,437 | 24,206 | 0.018 | compiled=5 | 1,577,759.0 | 214,237,029.0 | 108,191.0 |
| `phone-list-nested-plus` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 214,599,979.0 | 209,068,469.0 | 217,043,234.0 | 3,215,366.5 | 5 | 27,360 | 24,324 | 24,093 | 0.015 | compiled=5 | 1,583,699.0 | 212,835,380.0 | 102,910.0 |
| `phone-list-nested-plus` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 216,535,429.0 | 201,231,656.0 | 223,017,536.0 | 7,395,093.3 | 5 | 27,360 | 24,437 | 24,206 | 0.034 | compiled=5 | 1,567,088.0 | 214,760,300.0 | 191,941.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 284,035,768.0 | 277,287,600.0 | 285,721,218.0 | 2,929,624.1 | 5 | 27,168 | 22,007 | 22,007 | 0.010 | compiled=5 | 1,761,810.0 | 281,271,303.0 | 196,671.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 288,039,982.0 | 279,139,681.0 | 288,853,677.0 | 4,372,071.9 | 5 | 27,168 | 22,120 | 22,120 | 0.015 | compiled=5 | 1,495,668.0 | 286,459,323.0 | 196,982.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 275,133,894.0 | 272,348,087.0 | 275,780,757.0 | 1,199,457.0 | 5 | 27,168 | 21,989 | 21,989 | 0.004 | compiled=5 | 1,480,448.0 | 273,541,595.0 | 213,511.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 280,112,951.0 | 279,595,748.0 | 280,340,384.0 | 283,904.0 | 5 | 27,168 | 22,102 | 22,102 | 0.001 | compiled=5 | 1,499,959.0 | 278,100,140.0 | 110,130.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 284,485,825.0 | 278,425,202.0 | 287,839,973.0 | 3,616,858.5 | 5 | 27,168 | 22,005 | 22,005 | 0.013 | compiled=5 | 1,508,529.0 | 282,877,436.0 | 190,691.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 287,423,293.0 | 281,837,430.0 | 287,995,196.0 | 2,632,311.6 | 5 | 27,168 | 22,118 | 22,118 | 0.009 | compiled=5 | 1,508,759.0 | 285,697,232.0 | 192,951.0 |
| `phone-palindrome-6` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 284,876,337.0 | 284,120,171.0 | 285,160,377.0 | 435,345.1 | 5 | 27,168 | 22,005 | 22,005 | 0.002 | compiled=5 | 1,533,948.0 | 283,221,497.0 | 109,540.0 |
| `phone-palindrome-6` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 288,423,636.0 | 286,821,247.0 | 290,137,583.0 | 1,227,548.7 | 5 | 27,168 | 22,118 | 22,118 | 0.004 | compiled=5 | 1,580,859.0 | 285,524,469.0 | 105,881.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 246,770,106.0 | 240,258,747.0 | 255,264,194.0 | 5,719,890.7 | 5 | 31,808 | 31,612 | 28,971 | 0.023 | compiled=5 | 1,853,430.0 | 244,931,365.0 | 191,211.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 246,029,321.0 | 239,317,702.0 | 251,133,970.0 | 4,919,806.3 | 5 | 31,808 | 31,540 | 28,899 | 0.020 (max is trial 1) | compiled=5 | 1,922,641.0 | 242,371,890.0 | 206,211.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 247,295,218.0 | 241,366,027.0 | 250,924,200.0 | 3,078,557.3 | 5 | 31,808 | 31,612 | 28,971 | 0.012 (max is trial 1) | compiled=5 | 1,775,530.0 | 245,061,857.0 | 202,921.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 245,249,388.0 | 239,140,344.0 | 248,754,877.0 | 3,099,684.8 | 5 | 31,808 | 31,540 | 28,899 | 0.013 | compiled=5 | 1,756,640.0 | 242,998,026.0 | 103,090.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 229,032,972.0 | 223,724,071.0 | 232,168,260.0 | 2,723,645.3 | 5 | 27,280 | 25,857 | 25,395 | 0.012 | compiled=5 | 1,593,339.0 | 227,340,852.0 | 111,021.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 229,743,907.0 | 229,231,793.0 | 230,405,490.0 | 441,666.6 | 5 | 27,280 | 25,970 | 25,508 | 0.002 (max is trial 1) | compiled=5 | 1,592,689.0 | 227,571,394.0 | 105,861.0 |
| `pwd-strength-chain` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 230,506,447.0 | 220,838,085.0 | 230,727,518.0 | 3,796,702.3 | 5 | 27,280 | 25,857 | 25,395 | 0.016 | compiled=5 | 1,594,539.0 | 227,423,460.0 | 110,830.0 |
| `pwd-strength-chain` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 230,457,896.0 | 213,490,864.0 | 234,257,928.0 | 8,150,544.3 | 5 | 27,280 | 25,970 | 25,508 | 0.035 | compiled=5 | 1,937,031.0 | 228,674,517.0 | 196,101.0 |
| `quoted-delim-match` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 207,922,793.0 | 205,644,660.0 | 217,826,889.0 | 5,150,133.0 | 5 | 27,488 | 24,835 | 24,142 | 0.025 | compiled=5 | 1,562,029.0 | 206,142,002.0 | 192,591.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 215,008,643.0 | 207,686,742.0 | 215,998,718.0 | 3,110,179.3 | 5 | 27,488 | 24,948 | 24,255 | 0.014 (max is trial 1) | compiled=5 | 1,559,579.0 | 212,754,500.0 | 101,071.0 |
| `quoted-delim-match` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 212,319,055.0 | 208,136,583.0 | 214,295,125.0 | 2,016,597.7 | 5 | 27,488 | 24,817 | 24,124 | 0.009 | compiled=5 | 1,597,359.0 | 210,621,206.0 | 107,221.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 208,585,825.0 | 204,986,875.0 | 212,154,975.0 | 2,762,202.1 | 5 | 27,488 | 24,930 | 24,237 | 0.013 | compiled=5 | 1,574,669.0 | 204,985,105.0 | 210,911.0 |
| `quoted-delim-match` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 213,769,656.0 | 207,232,360.0 | 214,380,849.0 | 3,123,748.4 | 5 | 27,488 | 24,833 | 24,140 | 0.015 (max is trial 1) | compiled=5 | 1,582,459.0 | 211,995,046.0 | 107,541.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 209,712,924.0 | 199,594,366.0 | 215,791,368.0 | 5,746,985.2 | 5 | 27,488 | 24,946 | 24,253 | 0.027 | compiled=5 | 1,550,519.0 | 208,062,524.0 | 114,841.0 |
| `quoted-delim-match` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 214,246,568.0 | 214,072,896.0 | 216,837,101.0 | 1,121,552.3 | 5 | 27,488 | 24,833 | 24,140 | 0.005 | compiled=5 | 1,648,449.0 | 212,571,429.0 | 112,151.0 |
| `quoted-delim-match` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 214,619,019.0 | 197,217,485.0 | 219,173,865.0 | 8,535,651.1 | 5 | 27,488 | 24,946 | 24,253 | 0.040 | compiled=5 | 1,596,318.0 | 212,923,120.0 | 99,581.0 |
| `router-prefix-order` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 148,628,591.0 | 138,010,331.0 | 152,978,858.0 | 5,411,612.8 | 5 | 27,608 | 19,262 | 13,282 | 0.036 | compiled=5 | 1,854,811.0 | 146,622,910.0 | 193,851.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 158,054,795.0 | 148,378,491.0 | 167,696,542.0 | 6,556,482.2 | 5 | 27,752 | 21,906 | 15,299 | 0.041 | compiled=5 | 1,935,561.0 | 155,496,762.0 | 101,511.0 |
| `router-prefix-order` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 142,000,136.0 | 137,879,933.0 | 148,389,382.0 | 4,131,793.9 | 5 | 27,608 | 19,262 | 13,282 | 0.029 | compiled=5 | 1,820,060.0 | 138,569,738.0 | 190,291.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 157,931,375.0 | 154,862,538.0 | 159,786,785.0 | 1,740,597.3 | 5 | 27,752 | 21,906 | 15,299 | 0.011 | compiled=5 | 1,833,690.0 | 155,915,554.0 | 192,911.0 |
| `router-prefix-order` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 169,825,919.0 | 165,557,104.0 | 170,730,513.0 | 1,912,017.7 | 5 | 23,104 | 19,123 | 19,123 | 0.011 | compiled=5 | 1,495,548.0 | 168,207,909.0 | 102,681.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 169,741,398.0 | 160,403,515.0 | 170,532,883.0 | 3,848,403.5 | 5 | 23,104 | 19,236 | 19,236 | 0.023 | compiled=5 | 1,482,149.0 | 167,877,847.0 | 188,771.0 |
| `router-prefix-order` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 170,044,085.0 | 167,769,702.0 | 175,234,513.0 | 2,651,139.3 | 5 | 23,104 | 19,123 | 19,123 | 0.016 | compiled=5 | 1,476,698.0 | 168,387,496.0 | 99,611.0 |
| `router-prefix-order` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 170,041,504.0 | 168,874,999.0 | 177,335,415.0 | 3,058,725.3 | 5 | 23,104 | 19,236 | 19,236 | 0.018 | compiled=5 | 1,482,018.0 | 168,459,226.0 | 185,921.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 276,004,783.0 | 268,791,701.0 | 276,830,878.0 | 3,105,135.8 | 5 | 27,488 | 31,505 | 31,043 | 0.011 | compiled=5 | 1,716,540.0 | 269,473,895.0 | 187,911.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 278,210,165.0 | 273,729,270.0 | 279,057,081.0 | 1,917,297.8 | 5 | 31,584 | 31,618 | 31,156 | 0.007 (max is trial 1) | compiled=5 | 1,692,359.0 | 275,394,069.0 | 108,961.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 281,382,079.0 | 274,680,082.0 | 283,236,769.0 | 3,197,267.8 | 5 | 27,448 | 31,487 | 31,025 | 0.011 | compiled=5 | 1,723,899.0 | 279,422,968.0 | 107,781.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 282,571,894.0 | 274,118,859.0 | 285,744,312.0 | 3,937,555.1 | 5 | 27,448 | 31,600 | 31,138 | 0.014 (max is trial 1) | compiled=5 | 1,692,500.0 | 280,791,825.0 | 191,591.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 277,106,143.0 | 276,225,079.0 | 285,489,950.0 | 3,567,043.7 | 5 | 27,488 | 31,503 | 31,041 | 0.013 | compiled=5 | 1,683,400.0 | 275,203,922.0 | 190,391.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 276,968,893.0 | 267,292,068.0 | 280,012,170.0 | 4,465,689.7 | 5 | 31,584 | 31,616 | 31,154 | 0.016 (max is trial 1) | compiled=5 | 1,701,869.0 | 275,087,842.0 | 108,121.0 |
| `tag-depth3-bound` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 265,623,260.0 | 265,434,579.0 | 280,219,150.0 | 6,895,241.3 | 5 | 27,488 | 31,503 | 31,041 | 0.026 | compiled=5 | 1,682,529.0 | 263,715,730.0 | 187,951.0 |
| `tag-depth3-bound` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 270,293,016.0 | 268,798,127.0 | 279,288,285.0 | 4,633,446.4 | 5 | 31,584 | 31,616 | 31,154 | 0.017 | compiled=5 | 1,751,730.0 | 268,442,906.0 | 98,800.0 |
| `tag-pair-match` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 224,013,464.0 | 217,995,130.0 | 227,319,684.0 | 3,070,642.8 | 5 | 27,448 | 25,397 | 24,242 | 0.014 (max is trial 1) | compiled=5 | 1,640,500.0 | 222,215,454.0 | 189,761.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 218,293,111.0 | 215,560,836.0 | 235,595,811.0 | 7,313,189.1 | 5 | 27,448 | 25,510 | 24,355 | 0.034 | compiled=5 | 1,625,890.0 | 216,767,793.0 | 203,551.0 |
| `tag-pair-match` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 222,048,340.0 | 215,929,727.0 | 231,063,280.0 | 5,467,364.1 | 5 | 27,448 | 25,379 | 24,224 | 0.025 | compiled=5 | 1,627,459.0 | 220,329,280.0 | 119,691.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 221,705,498.0 | 208,900,908.0 | 242,032,380.0 | 11,111,841.3 | 5 | 27,448 | 25,492 | 24,337 | 0.050 | compiled=5 | 1,601,629.0 | 219,930,849.0 | 192,022.0 |
| `tag-pair-match` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 224,177,206.0 | 217,910,069.0 | 226,128,547.0 | 3,248,358.7 | 5 | 27,448 | 25,395 | 24,240 | 0.014 | compiled=5 | 1,618,789.0 | 222,441,956.0 | 116,461.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 224,052,164.0 | 216,576,322.0 | 225,449,933.0 | 3,218,815.6 | 5 | 27,448 | 25,508 | 24,353 | 0.014 | compiled=5 | 1,613,259.0 | 222,245,874.0 | 102,421.0 |
| `tag-pair-match` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 223,601,009.0 | 218,331,770.0 | 235,660,746.0 | 5,719,992.2 | 5 | 27,448 | 25,395 | 24,240 | 0.026 | compiled=5 | 1,606,818.0 | 221,920,710.0 | 116,121.0 |
| `tag-pair-match` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 219,142,125.0 | 214,060,696.0 | 224,005,202.0 | 4,060,986.7 | 5 | 27,448 | 25,508 | 24,353 | 0.019 | compiled=5 | 1,616,539.0 | 217,344,415.0 | 190,471.0 |
| `trim-nested-star` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 195,466,420.0 | 194,682,117.0 | 196,496,416.0 | 687,127.0 | 5 | 27,360 | 22,383 | 22,152 | 0.004 (max is trial 1) | compiled=5 | 1,524,809.0 | 193,596,910.0 | 209,211.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 194,458,174.0 | 184,840,771.0 | 197,918,654.0 | 4,558,751.1 | 5 | 27,360 | 22,497 | 22,266 | 0.023 | compiled=5 | 1,513,228.0 | 192,862,636.0 | 99,830.0 |
| `trim-nested-star` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 128,518,952.0 | 124,371,599.0 | 142,292,686.0 | 7,065,193.1 | 5 | 23,144 | 12,653 | 11,042 | 0.055 | compiled=5 | 1,499,369.0 | 126,681,412.0 | 187,021.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 137,519,402.0 | 131,229,708.0 | 138,507,947.0 | 2,659,822.5 | 5 | 23,104 | 12,477 | 10,866 | 0.019 | compiled=5 | 1,448,638.0 | 135,332,489.0 | 99,401.0 |
| `trim-nested-star` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 195,221,462.0 | 187,947,140.0 | 197,201,763.0 | 3,160,732.8 | 5 | 27,360 | 22,364 | 22,133 | 0.016 (max is trial 1) | compiled=5 | 1,502,379.0 | 193,537,082.0 | 200,151.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 193,889,045.0 | 187,272,257.0 | 195,349,003.0 | 2,842,837.1 | 5 | 27,360 | 22,478 | 22,247 | 0.015 | compiled=5 | 1,502,949.0 | 192,179,734.0 | 101,840.0 |
| `trim-nested-star` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 195,409,834.0 | 194,781,290.0 | 202,886,875.0 | 3,152,373.8 | 5 | 27,360 | 22,364 | 22,133 | 0.016 | compiled=5 | 1,526,648.0 | 193,789,995.0 | 100,270.0 |
| `trim-nested-star` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 194,850,121.0 | 193,524,303.0 | 195,166,102.0 | 579,730.1 | 5 | 27,360 | 22,478 | 22,247 | 0.003 (max is trial 1) | compiled=5 | 1,511,188.0 | 193,084,761.0 | 192,321.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 184,716,460.0 | 177,924,901.0 | 187,957,128.0 | 3,349,523.7 | 5 | 31,632 | 26,846 | 22,044 | 0.018 | compiled=5 | 1,712,970.0 | 182,810,459.0 | 203,551.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 187,136,022.0 | 178,556,804.0 | 191,012,256.0 | 4,683,339.0 | 5 | 31,728 | 28,422 | 23,406 | 0.025 | compiled=5 | 1,752,010.0 | 183,502,352.0 | 105,460.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 184,842,033.0 | 184,245,002.0 | 185,138,935.0 | 300,237.6 | 5 | 31,632 | 26,846 | 22,044 | 0.002 | compiled=5 | 1,752,900.0 | 182,974,103.0 | 99,471.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 192,699,467.0 | 183,911,788.0 | 200,925,972.0 | 6,119,613.7 | 5 | 31,728 | 28,422 | 23,406 | 0.032 (max is trial 1) | compiled=5 | 1,819,980.0 | 190,859,387.0 | 99,180.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 167,873,247.0 | 166,341,207.0 | 170,914,464.0 | 1,623,912.4 | 5 | 23,104 | 18,767 | 18,767 | 0.010 | compiled=5 | 1,460,388.0 | 166,314,719.0 | 98,550.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 161,223,890.0 | 154,872,264.0 | 171,618,088.0 | 6,151,303.8 | 5 | 23,104 | 18,878 | 18,878 | 0.038 | compiled=5 | 1,450,878.0 | 159,563,090.0 | 106,261.0 |
| `utf8-lead-no-cont` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 167,905,423.0 | 157,927,518.0 | 170,019,785.0 | 4,995,414.8 | 5 | 23,104 | 18,767 | 18,767 | 0.030 | compiled=5 | 1,542,389.0 | 166,237,904.0 | 189,031.0 |
| `utf8-lead-no-cont` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 168,618,446.0 | 160,924,624.0 | 172,330,396.0 | 3,743,665.7 | 5 | 23,104 | 18,878 | 18,878 | 0.022 | compiled=5 | 1,474,188.0 | 166,679,226.0 | 170,201.0 |
| `uuid-near-miss` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 172,821,300.0 | 162,716,103.0 | 175,544,547.0 | 4,536,994.7 | 5 | 36,888 | 22,345 | 16,941 | 0.026 | compiled=5 | 1,636,340.0 | 170,992,280.0 | 112,471.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 175,977,369.0 | 167,479,640.0 | 182,394,507.0 | 5,345,331.9 | 5 | 36,848 | 22,167 | 16,763 | 0.030 | compiled=5 | 1,732,600.0 | 172,436,539.0 | 100,760.0 |
| `uuid-near-miss` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 173,195,568.0 | 170,517,944.0 | 180,303,999.0 | 3,607,589.2 | 5 | 36,888 | 22,345 | 16,941 | 0.021 | compiled=5 | 1,654,459.0 | 171,438,279.0 | 109,541.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 166,769,074.0 | 165,065,775.0 | 174,295,975.0 | 3,870,888.9 | 5 | 36,848 | 22,167 | 16,763 | 0.023 | compiled=5 | 1,639,019.0 | 163,559,606.0 | 190,831.0 |
| `uuid-near-miss` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 187,181,647.0 | 186,062,060.0 | 189,301,049.0 | 1,070,045.3 | 5 | 23,192 | 22,958 | 22,496 | 0.006 | compiled=5 | 1,510,709.0 | 185,173,025.0 | 191,681.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 193,916,994.0 | 185,214,955.0 | 204,196,633.0 | 6,060,634.8 | 5 | 23,192 | 23,071 | 22,609 | 0.031 (max is trial 1) | compiled=5 | 1,509,698.0 | 192,298,485.0 | 176,511.0 |
| `uuid-near-miss` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 194,545,859.0 | 187,692,441.0 | 197,313,595.0 | 3,289,171.3 | 5 | 23,192 | 22,958 | 22,496 | 0.017 (max is trial 1) | compiled=5 | 1,551,349.0 | 192,888,010.0 | 100,490.0 |
| `uuid-near-miss` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 193,755,846.0 | 187,165,289.0 | 202,544,214.0 | 5,090,056.7 | 5 | 23,192 | 23,071 | 22,609 | 0.026 | compiled=5 | 1,552,769.0 | 192,101,456.0 | 99,441.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 140,456,746.0 | 131,277,083.0 | 151,701,489.0 | 7,924,500.0 | 5 | 27,608 | 18,269 | 13,272 | 0.056 | compiled=5 | 1,657,840.0 | 138,631,245.0 | 197,321.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 156,797,529.0 | 148,200,410.0 | 161,062,224.0 | 4,672,881.7 | 5 | 27,752 | 20,612 | 15,289 | 0.030 | compiled=5 | 1,688,709.0 | 154,892,608.0 | 99,851.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 148,588,013.0 | 143,660,985.0 | 149,960,800.0 | 2,214,474.9 | 5 | 27,608 | 18,269 | 13,272 | 0.015 | compiled=5 | 1,657,429.0 | 146,577,472.0 | 190,071.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 157,338,071.0 | 156,937,267.0 | 158,263,916.0 | 490,733.6 | 5 | 27,752 | 20,612 | 15,289 | 0.003 | compiled=5 | 1,691,159.0 | 155,457,141.0 | 189,001.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 132,514,478.0 | 127,267,549.0 | 144,683,156.0 | 6,320,717.8 | 5 | 23,072 | 17,812 | 17,812 | 0.048 | compiled=5 | 1,423,988.0 | 130,929,669.0 | 192,341.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 142,215,472.0 | 130,517,817.0 | 147,139,790.0 | 6,069,647.8 | 5 | 23,072 | 17,923 | 17,923 | 0.043 (max is trial 1) | compiled=5 | 1,605,649.0 | 140,691,934.0 | 123,550.0 |
| `wild-codegrammar-json-array-begin` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 140,145,910.0 | 133,071,312.0 | 142,076,401.0 | 3,969,087.7 | 5 | 23,072 | 17,812 | 17,812 | 0.028 | compiled=5 | 2,620,714.0 | 138,534,602.0 | 184,541.0 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 136,848,981.0 | 129,805,083.0 | 143,480,789.0 | 4,603,512.7 | 5 | 23,072 | 17,923 | 17,923 | 0.034 | compiled=5 | 1,479,458.0 | 135,268,773.0 | 100,750.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 148,879,514.0 | 143,712,294.0 | 157,465,904.0 | 5,660,150.3 | 5 | 27,936 | 27,223 | 14,958 | 0.038 | compiled=5 | 2,160,213.0 | 146,598,361.0 | 110,911.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 165,868,583.0 | 161,036,083.0 | 177,867,069.0 | 6,703,597.6 | 5 | 28,080 | 30,086 | 16,933 | 0.040 | compiled=5 | 2,338,704.0 | 163,336,807.0 | 191,081.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 155,984,045.0 | 151,046,957.0 | 159,435,953.0 | 2,780,837.3 | 5 | 27,936 | 27,223 | 14,958 | 0.018 (max is trial 1) | compiled=5 | 2,155,202.0 | 153,743,732.0 | 189,811.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 163,122,113.0 | 156,285,885.0 | 170,492,486.0 | 4,501,586.7 | 5 | 28,080 | 30,086 | 16,933 | 0.028 (max is trial 1) | compiled=5 | 2,268,432.0 | 160,755,320.0 | 102,610.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 206,354,344.0 | 196,527,889.0 | 208,777,908.0 | 4,321,204.8 | 5 | 23,112 | 20,874 | 20,643 | 0.021 | compiled=5 | 1,510,088.0 | 204,744,946.0 | 99,931.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 208,133,255.0 | 200,587,542.0 | 214,412,250.0 | 4,928,313.1 | 5 | 23,112 | 20,987 | 20,756 | 0.024 | compiled=5 | 1,523,599.0 | 206,514,465.0 | 109,581.0 |
| `wild-codegrammar-json-constant` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 199,452,216.0 | 198,060,679.0 | 205,901,952.0 | 2,891,676.2 | 5 | 23,112 | 20,874 | 20,643 | 0.014 | compiled=5 | 1,606,689.0 | 197,575,716.0 | 187,091.0 |
| `wild-codegrammar-json-constant` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 203,733,150.0 | 198,930,753.0 | 210,690,017.0 | 4,456,691.7 | 5 | 23,112 | 20,987 | 20,756 | 0.022 (max is trial 1) | compiled=5 | 1,512,268.0 | 202,086,501.0 | 187,801.0 |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 147,982,869.0 | 141,191,960.0 | 153,306,408.0 | 5,368,910.4 | 5 | 27,608 | 22,036 | 13,714 | 0.036 | compiled=5 | 1,944,592.0 | 143,380,902.0 | 210,392.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,252,523.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 148,014,479.0 | 145,254,094.0 | 151,988,302.0 | 2,213,309.0 | 5 | 27,608 | 22,036 | 13,714 | 0.015 | compiled=5 | 1,966,031.0 | 145,713,297.0 | 203,101.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,218,442.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 202,571,713.0 | 195,925,906.0 | 207,808,023.0 | 3,818,757.8 | 5 | 31,336 | 23,244 | 23,013 | 0.019 | compiled=5 | 1,581,339.0 | 199,283,824.0 | 196,152.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,231,592.0 | - | - |
| `wild-codegrammar-json-number-extended` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 200,759,482.0 | 199,910,930.0 | 201,205,777.0 | 550,386.0 | 5 | 31,336 | 23,244 | 23,013 | 0.003 (max is trial 1) | compiled=5 | 1,605,759.0 | 198,330,850.0 | 108,320.0 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,109,182.0 | - | - |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 152,032,553.0 | 140,274,274.0 | 158,366,338.0 | 6,041,910.8 | 5 | 27,608 | 18,270 | 13,273 | 0.040 | compiled=5 | 1,653,430.0 | 150,195,532.0 | 195,782.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 162,020,749.0 | 150,969,855.0 | 177,532,999.0 | 8,653,484.5 | 5 | 27,752 | 20,613 | 15,290 | 0.053 | compiled=5 | 1,714,470.0 | 160,103,468.0 | 204,321.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 146,671,802.0 | 140,579,199.0 | 154,820,348.0 | 4,890,063.1 | 5 | 27,608 | 18,270 | 13,273 | 0.033 | compiled=5 | 1,641,869.0 | 144,855,842.0 | 184,131.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 158,337,336.0 | 149,122,987.0 | 161,464,025.0 | 5,206,286.1 | 5 | 27,752 | 20,613 | 15,290 | 0.033 | compiled=5 | 1,729,680.0 | 155,455,811.0 | 109,721.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 129,900,604.0 | 117,659,804.0 | 137,835,836.0 | 7,992,761.0 | 5 | 23,072 | 17,813 | 17,813 | 0.062 | compiled=5 | 1,397,968.0 | 128,180,533.0 | 190,731.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 140,775,894.0 | 129,849,843.0 | 145,259,550.0 | 5,572,007.7 | 5 | 23,072 | 17,924 | 17,924 | 0.040 | compiled=5 | 1,486,608.0 | 139,134,035.0 | 101,590.0 |
| `wild-codegrammar-json-object-begin` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 128,282,225.0 | 127,888,603.0 | 137,765,207.0 | 3,787,914.9 | 5 | 23,072 | 17,813 | 17,813 | 0.030 | compiled=5 | 1,637,889.0 | 126,737,217.0 | 189,371.0 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 137,124,264.0 | 128,743,957.0 | 142,557,503.0 | 5,768,282.0 | 5 | 23,072 | 17,924 | 17,924 | 0.042 | compiled=5 | 1,410,168.0 | 134,159,537.0 | 107,570.0 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 153,359,370.0 | 133,262,713.0 | 160,496,792.0 | 9,232,417.0 | 5 | 27,608 | 19,649 | 13,554 | 0.060 | compiled=5 | 1,821,700.0 | 151,416,299.0 | 189,642.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,109,452.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 150,945,865.0 | 133,075,137.0 | 156,867,108.0 | 8,831,295.5 | 5 | 27,608 | 19,649 | 13,554 | 0.059 | compiled=5 | 1,789,510.0 | 149,049,615.0 | 192,751.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 1,096,106.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 178,124,795.0 | 177,051,610.0 | 180,662,419.0 | 1,274,507.8 | 5 | 23,184 | 20,171 | 19,709 | 0.007 (max is trial 1) | compiled=5 | 1,794,770.0 | 176,416,585.0 | 108,071.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 1,228,867.0 | - | - |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 178,996,474.0 | 175,424,025.0 | 182,416,832.0 | 2,390,549.6 | 5 | 23,184 | 20,171 | 19,709 | 0.013 | compiled=5 | 1,506,188.0 | 176,587,510.0 | 201,871.0 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,118,551.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 564,032,335.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,151,600,629.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 852,520,361.0 | 845,321,643.0 | 874,783,965.0 | 10,002,241.5 | 5 | 277,312 | 889,500 (warned) | 20,411 | 0.012 (max is trial 1) | compiled=5 | 564,049,864.0 | 288,135,916.0 | 189,312.0 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 9,886,341,184.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a770139e_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 17,170,617.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 20,505,766.0 | - | - |
| `wild-datetime-datefinder-alternation` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 18,957,314.0 | - | - |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 26,018,044.0 | - | - |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 357,634,431.0 | 356,551,405.0 | 359,966,654.0 | 1,162,361.3 | 5 | 45,648 | 54,233 | 44,310 | 0.003 | compiled=5 | 2,283,794.0 | 354,997,186.0 | 105,661.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 346,014,165.0 | 338,888,203.0 | 349,298,002.0 | 3,466,310.7 | 5 | 45,280 | 52,672 | 42,749 | 0.010 (max is trial 1) | compiled=5 | 2,237,543.0 | 343,665,291.0 | 111,331.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 177,211,192.0 | 173,910,633.0 | 185,691,879.0 | 4,774,474.8 | 5 | 41,232 | 29,456 | 20,457 | 0.027 | compiled=5 | 1,802,970.0 | 175,306,741.0 | 101,481.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 173,068,039.0 | 156,456,827.0 | 176,180,256.0 | 6,996,681.3 | 5 | 40,864 | 27,790 | 18,791 | 0.040 | compiled=5 | 1,825,850.0 | 169,153,027.0 | 110,131.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 300,026,003.0 | 291,420,653.0 | 305,790,446.0 | 5,594,437.4 | 5 | 27,408 | 33,696 | 32,772 | 0.019 | compiled=5 | 1,818,981.0 | 298,008,721.0 | 198,301.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 297,937,360.0 | 291,522,195.0 | 302,839,420.0 | 4,016,703.1 | 5 | 27,408 | 33,809 | 32,885 | 0.013 (max is trial 1) | compiled=5 | 1,806,110.0 | 296,054,451.0 | 191,981.0 |
| `wild-datetime-moment-iso8601` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 295,387,684.0 | 287,755,302.0 | 300,338,713.0 | 4,186,503.9 | 5 | 27,408 | 33,696 | 32,772 | 0.014 (max is trial 1) | compiled=5 | 1,917,451.0 | 293,252,332.0 | 110,351.0 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 300,101,499.0 | 296,005,607.0 | 303,271,587.0 | 2,357,809.9 | 5 | 27,408 | 33,809 | 32,885 | 0.008 | compiled=5 | 2,088,482.0 | 298,088,588.0 | 199,502.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 237,966,245.0 | 227,730,216.0 | 239,171,671.0 | 4,340,235.2 | 5 | 31,800 | 32,739 | 27,229 | 0.018 | compiled=5 | 1,940,241.0 | 235,930,513.0 | 108,081.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 238,292,317.0 | 235,010,417.0 | 239,536,163.0 | 1,557,460.7 | 5 | 31,888 | 33,811 | 27,876 | 0.007 | compiled=5 | 2,002,561.0 | 236,243,845.0 | 101,001.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 231,920,974.0 | 231,065,850.0 | 241,365,607.0 | 4,644,213.1 | 5 | 31,800 | 32,739 | 27,229 | 0.020 | compiled=5 | 2,033,901.0 | 229,727,382.0 | 185,471.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 239,586,856.0 | 230,261,514.0 | 240,352,670.0 | 4,002,043.3 | 5 | 31,888 | 33,811 | 27,876 | 0.017 | compiled=5 | 2,055,451.0 | 237,389,424.0 | 192,481.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 209,149,969.0 | 206,578,546.0 | 210,689,389.0 | 1,329,230.6 | 5 | 27,328 | 23,318 | 22,856 | 0.006 | compiled=5 | 1,609,530.0 | 207,443,401.0 | 105,790.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 205,091,367.0 | 203,193,307.0 | 215,631,118.0 | 4,456,611.9 | 5 | 27,328 | 23,434 | 22,972 | 0.022 (max is trial 1) | compiled=5 | 1,599,739.0 | 203,171,206.0 | 193,591.0 |
| `wild-logparse-base10num-grok` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 202,802,474.0 | 201,242,916.0 | 211,017,120.0 | 4,061,460.0 | 5 | 27,328 | 23,318 | 22,856 | 0.020 | compiled=5 | 1,605,889.0 | 200,929,264.0 | 206,071.0 |
| `wild-logparse-base10num-grok` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 213,870,445.0 | 199,725,887.0 | 222,752,144.0 | 8,645,758.7 | 5 | 27,328 | 23,434 | 22,972 | 0.040 | compiled=5 | 1,918,860.0 | 211,992,725.0 | 100,620.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 233,409,189.0 | 227,600,166.0 | 234,709,526.0 | 2,999,237.2 | 5 | 31,800 | 32,460 | 26,950 | 0.013 (max is trial 1) | compiled=5 | 1,898,721.0 | 231,393,977.0 | 115,821.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 233,252,099.0 | 233,062,367.0 | 244,660,713.0 | 4,458,315.5 | 5 | 31,888 | 33,529 | 27,594 | 0.019 | compiled=5 | 1,958,861.0 | 231,033,655.0 | 111,081.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 234,216,267.0 | 227,179,638.0 | 236,190,316.0 | 3,463,299.2 | 5 | 31,800 | 32,460 | 26,950 | 0.015 (max is trial 1) | compiled=5 | 1,894,560.0 | 232,051,295.0 | 189,461.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 235,238,193.0 | 226,506,815.0 | 239,907,988.0 | 4,574,329.1 | 5 | 31,888 | 33,529 | 27,594 | 0.019 | compiled=5 | 1,959,311.0 | 232,470,117.0 | 169,761.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 204,948,256.0 | 198,100,537.0 | 208,085,935.0 | 3,297,017.6 | 5 | 27,328 | 23,039 | 22,577 | 0.016 (max is trial 1) | compiled=5 | 1,564,869.0 | 203,170,126.0 | 187,171.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 208,245,684.0 | 201,511,837.0 | 210,215,937.0 | 2,992,456.3 | 5 | 27,328 | 23,152 | 22,690 | 0.014 | compiled=5 | 1,558,339.0 | 206,174,833.0 | 114,441.0 |
| `wild-logparse-base10num-noatomic` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 205,180,368.0 | 189,969,024.0 | 211,443,133.0 | 7,484,086.9 | 5 | 27,328 | 23,039 | 22,577 | 0.036 | compiled=5 | 1,580,919.0 | 203,364,648.0 | 103,560.0 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 208,349,535.0 | 207,509,621.0 | 209,163,590.0 | 692,911.8 | 5 | 27,328 | 23,152 | 22,690 | 0.003 (max is trial 1) | compiled=5 | 1,580,679.0 | 206,022,072.0 | 109,121.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 397,750,092.0 | 391,820,127.0 | 402,195,357.0 | 3,439,739.7 | 5 | 40,504 | 60,464 | 40,735 | 0.009 (max is trial 1) | compiled=5 | 4,932,998.0 | 390,546,840.0 | 192,591.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 410,454,743.0 | 403,536,895.0 | 411,784,171.0 | 2,973,700.4 | 5 | 40,592 | 65,107 | 42,235 | 0.007 | compiled=5 | 8,048,556.0 | 402,058,335.0 | 195,491.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 395,998,003.0 | 389,007,235.0 | 398,351,156.0 | 3,956,345.2 | 5 | 40,504 | 60,464 | 40,735 | 0.010 (max is trial 1) | compiled=5 | 4,944,918.0 | 386,841,422.0 | 188,471.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 416,419,797.0 | 405,759,607.0 | 419,780,054.0 | 4,943,318.3 | 5 | 40,592 | 65,107 | 42,235 | 0.012 (max is trial 1) | compiled=5 | 9,821,375.0 | 404,479,550.0 | 101,351.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 355,239,445.0 | 346,946,698.0 | 358,977,147.0 | 4,643,325.0 | 5 | 35,720 | 36,811 | 35,887 | 0.013 (max is trial 1) | compiled=5 | 1,787,420.0 | 353,220,723.0 | 108,041.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 356,650,652.0 | 350,310,886.0 | 365,528,243.0 | 4,947,811.7 | 5 | 35,720 | 36,924 | 36,000 | 0.014 | compiled=5 | 1,702,570.0 | 354,652,261.0 | 187,071.0 |
| `wild-logparse-quotedstring-grok` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 356,779,050.0 | 354,707,869.0 | 364,071,001.0 | 3,334,052.6 | 5 | 35,720 | 36,811 | 35,887 | 0.009 (max is trial 1) | compiled=5 | 1,922,160.0 | 354,868,660.0 | 104,341.0 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 354,794,081.0 | 349,241,290.0 | 367,969,523.0 | 6,769,356.9 | 5 | 35,720 | 36,924 | 36,000 | 0.019 | compiled=5 | 2,169,912.0 | 351,035,140.0 | 199,141.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 357,280,669.0 | 347,491,852.0 | 358,053,163.0 | 4,002,546.0 | 5 | 40,504 | 58,016 | 38,287 | 0.011 | compiled=5 | 4,781,607.0 | 352,332,921.0 | 108,130.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 369,529,388.0 | 361,937,205.0 | 374,481,267.0 | 5,044,106.5 | 5 | 40,592 | 62,659 | 39,787 | 0.014 | compiled=5 | 7,739,644.0 | 354,247,382.0 | 191,551.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 357,753,432.0 | 348,578,389.0 | 361,251,192.0 | 5,215,789.2 | 5 | 40,504 | 58,016 | 38,287 | 0.015 (max is trial 1) | compiled=5 | 4,771,557.0 | 349,942,708.0 | 198,311.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 372,582,163.0 | 370,040,119.0 | 390,577,243.0 | 7,612,203.4 | 5 | 40,592 | 62,659 | 39,787 | 0.020 (max is trial 1) | compiled=5 | 17,782,438.0 | 361,453,782.0 | 192,001.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 315,565,829.0 | 305,174,112.0 | 324,187,380.0 | 6,063,978.5 | 5 | 31,624 | 34,363 | 33,439 | 0.019 (max is trial 1) | compiled=5 | 1,760,879.0 | 313,601,579.0 | 102,060.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 316,203,993.0 | 310,570,472.0 | 320,191,487.0 | 3,346,228.6 | 5 | 31,624 | 34,476 | 33,552 | 0.011 (max is trial 1) | compiled=5 | 1,803,450.0 | 314,219,613.0 | 112,391.0 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 317,574,515.0 | 314,704,661.0 | 319,967,239.0 | 1,695,074.5 | 5 | 31,624 | 34,363 | 33,439 | 0.005 | compiled=5 | 1,766,850.0 | 315,670,386.0 | 105,320.0 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 314,804,300.0 | 310,847,568.0 | 316,214,458.0 | 2,212,843.3 | 5 | 31,624 | 34,476 | 33,552 | 0.007 | compiled=5 | 1,770,719.0 | 312,853,229.0 | 98,871.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 5,427,336,223.0 | 5,405,925,600.0 | 5,443,278,685.0 | 12,491,427.7 | 5 | 180,072 | 526,377 (warned) | 299,133 | 0.002 (max is trial 1) | compiled=5 | 604,298,605.0 | 4,813,307,172.0 | 99,941.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 6,471,409,690.0 | 6,463,759,377.0 | 6,482,908,965.0 | 7,108,981.4 | 5 | 180,168 | 536,222 (warned) | 300,553 | 0.001 | compiled=5 | 1,630,019,477.0 | 4,841,809,775.0 | 100,730.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 4,370,351,455.0 | 4,331,821,091.0 | 4,403,194,266.0 | 22,720,899.0 | 5 | 159,552 | 482,634 (warned) | 255,386 | 0.005 | compiled=5 | 606,063,727.0 | 3,761,886,675.0 | 105,561.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 5,393,671,072.0 | 5,375,130,110.0 | 5,423,927,982.0 | 18,019,710.7 | 5 | 159,648 | 492,479 (warned) | 256,806 | 0.003 (max is trial 1) | compiled=5 | 1,643,316,071.0 | 3,763,374,393.0 | 104,781.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 4,763,196,297.0 | 4,737,960,634.0 | 4,771,869,695.0 | 13,872,061.5 | 5 | 105,728 | 296,976 (warned) | 294,181 | 0.003 | compiled=5 | 6,179,364.0 | 4,749,011,777.0 | 107,730.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 4,779,490,508.0 | 4,742,227,968.0 | 4,795,276,548.0 | 19,069,487.3 | 5 | 105,728 | 297,093 (warned) | 294,298 | 0.004 | compiled=5 | 7,388,262.0 | 4,765,609,800.0 | 192,501.0 |
| `wild-logparse-syslogbase-expanded` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 4,747,965,348.0 | 4,739,947,194.0 | 4,762,386,039.0 | 8,915,365.6 | 5 | 105,728 | 296,976 (warned) | 294,181 | 0.002 | compiled=5 | 6,191,704.0 | 4,741,836,785.0 | 99,630.0 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 4,762,426,887.0 | 4,736,166,703.0 | 4,806,721,110.0 | 23,778,252.1 | 5 | 105,728 | 297,093 (warned) | 294,298 | 0.005 | compiled=5 | 6,030,953.0 | 4,752,059,401.0 | 204,321.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 240,633,809.0 | 232,292,221.0 | 244,025,529.0 | 4,037,538.7 | 5 | 31,960 | 36,026 | 27,542 | 0.017 | compiled=5 | 2,120,192.0 | 238,394,037.0 | 108,710.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 249,826,414.0 | 243,878,008.0 | 259,120,446.0 | 4,888,438.2 | 5 | 32,096 | 39,370 | 29,067 | 0.020 | compiled=5 | 4,261,674.0 | 246,804,286.0 | 190,331.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 239,410,566.0 | 227,563,750.0 | 241,927,871.0 | 5,233,485.1 | 5 | 31,960 | 36,026 | 27,542 | 0.022 | compiled=5 | 4,189,153.0 | 237,285,004.0 | 98,920.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 244,147,012.0 | 240,210,801.0 | 251,806,913.0 | 4,588,202.2 | 5 | 32,096 | 39,370 | 29,067 | 0.019 | compiled=5 | 2,227,352.0 | 239,015,104.0 | 110,760.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 202,750,844.0 | 200,293,801.0 | 213,022,881.0 | 5,301,308.7 | 5 | 27,400 | 23,964 | 23,502 | 0.026 | compiled=5 | 1,587,829.0 | 200,990,764.0 | 191,721.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 212,727,101.0 | 211,686,654.0 | 221,911,432.0 | 3,807,087.6 | 5 | 27,400 | 24,078 | 23,616 | 0.018 | compiled=5 | 1,592,089.0 | 210,446,238.0 | 115,181.0 |
| `wild-logparse-winpath-grok` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 212,204,456.0 | 205,429,978.0 | 222,058,041.0 | 6,074,157.3 | 5 | 27,400 | 23,964 | 23,502 | 0.029 | compiled=5 | 1,581,729.0 | 210,497,298.0 | 183,631.0 |
| `wild-logparse-winpath-grok` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 211,874,494.0 | 198,159,539.0 | 216,001,878.0 | 6,088,664.6 | 5 | 27,400 | 24,078 | 23,616 | 0.029 | compiled=5 | 1,576,018.0 | 210,204,495.0 | 115,011.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 247,180,237.0 | 240,728,161.0 | 250,104,363.0 | 3,153,444.8 | 5 | 36,024 | 46,348 | 29,443 | 0.013 (max is trial 1) | compiled=5 | 3,067,478.0 | 243,774,458.0 | 100,540.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 252,339,927.0 | 250,444,937.0 | 261,154,437.0 | 3,770,412.5 | 5 | 36,120 | 48,765 | 30,864 | 0.015 | compiled=5 | 3,176,319.0 | 248,699,486.0 | 111,560.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 149,542,448.0 | 144,940,473.0 | 153,744,241.0 | 2,840,577.2 | 5 | 32,032 | 39,274 | 15,008 | 0.019 | compiled=5 | 3,453,219.0 | 145,908,278.0 | 188,121.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 159,449,104.0 | 157,410,642.0 | 175,291,181.0 | 6,602,204.1 | 5 | 32,176 | 42,762 | 16,983 | 0.041 | compiled=5 | 3,560,740.0 | 155,801,333.0 | 101,881.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 221,392,790.0 | 213,709,195.0 | 228,531,400.0 | 5,539,513.8 | 5 | 27,280 | 25,410 | 24,948 | 0.025 | compiled=5 | 1,652,429.0 | 219,624,550.0 | 115,811.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 218,547,714.0 | 214,358,000.0 | 220,543,054.0 | 2,594,273.0 | 5 | 27,280 | 25,523 | 25,061 | 0.012 | compiled=5 | 1,632,039.0 | 216,831,764.0 | 111,290.0 |
| `wild-secrets-aws-access-key-id` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 220,792,674.0 | 220,435,292.0 | 222,268,832.0 | 649,654.6 | 5 | 27,280 | 25,410 | 24,948 | 0.003 (max is trial 1) | compiled=5 | 1,643,969.0 | 218,827,973.0 | 105,211.0 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 218,114,078.0 | 212,126,676.0 | 228,508,916.0 | 6,515,337.5 | 5 | 27,280 | 25,523 | 25,061 | 0.030 | compiled=5 | 1,449,098.0 | 216,554,090.0 | 110,890.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 394,062,480.0 | 388,732,049.0 | 396,580,345.0 | 3,385,474.0 | 5 | 40,040 | 56,713 | 26,603 | 0.009 | compiled=5 | 9,968,137.0 | 384,571,155.0 | 98,350.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 391,940,728.0 | 389,662,554.0 | 404,459,949.0 | 5,411,528.6 | 5 | 40,136 | 59,967 | 28,024 | 0.014 | compiled=5 | 10,043,598.0 | 386,056,563.0 | 194,661.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 171,312,729.0 | 158,413,938.0 | 175,024,869.0 | 5,914,584.7 | 5 | 40,224 | 61,051 | 15,807 | 0.035 | compiled=5 | 5,376,200.0 | 158,863,650.0 | 108,381.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 182,126,348.0 | 175,238,030.0 | 204,206,031.0 | 10,492,301.0 | 5 | 40,368 | 65,789 | 17,782 | 0.058 (max is trial 1) | compiled=5 | 5,537,900.0 | 176,383,326.0 | 194,301.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 351,810,505.0 | 343,327,467.0 | 354,165,927.0 | 3,818,997.8 | 5 | 27,160 | 21,499 | 21,268 | 0.011 (max is trial 1) | compiled=5 | 1,546,298.0 | 350,179,916.0 | 104,381.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 347,902,793.0 | 339,586,596.0 | 353,998,107.0 | 4,646,651.7 | 5 | 27,160 | 21,612 | 21,381 | 0.013 (max is trial 1) | compiled=5 | 1,499,629.0 | 346,200,173.0 | 188,721.0 |
| `wild-secrets-github-pat` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 345,704,500.0 | 342,398,893.0 | 352,856,219.0 | 3,881,061.7 | 5 | 27,160 | 21,499 | 21,268 | 0.011 | compiled=5 | 1,516,298.0 | 342,567,573.0 | 192,071.0 |
| `wild-secrets-github-pat` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 350,885,768.0 | 346,638,785.0 | 358,429,681.0 | 4,335,410.0 | 5 | 27,160 | 21,612 | 21,381 | 0.012 | compiled=5 | 1,579,719.0 | 347,669,631.0 | 189,181.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 272,511,502.0 | 261,936,822.0 | 279,756,664.0 | 6,434,041.2 | 5 | 52,360 | 103,877 | 32,527 | 0.024 | compiled=5 | 7,385,742.0 | 256,643,642.0 | 105,181.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 288,923,637.0 | 284,905,163.0 | 302,365,143.0 | 5,930,979.4 | 5 | 52,456 | 111,116 | 33,955 | 0.021 | compiled=5 | 7,760,084.0 | 281,013,062.0 | 196,961.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 204,147,320.0 | 196,273,207.0 | 209,606,080.0 | 4,274,064.0 | 5 | 52,408 | 109,122 | 17,413 | 0.021 (max is trial 1) | compiled=5 | 8,207,105.0 | 194,711,478.0 | 119,790.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 206,917,846.0 | 206,409,154.0 | 208,948,528.0 | 927,576.4 | 5 | 56,640 | 117,680 | 19,277 | 0.004 (max is trial 1) | compiled=5 | 8,609,448.0 | 198,083,187.0 | 198,901.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 221,055,317.0 | 220,919,966.0 | 224,816,459.0 | 1,510,716.8 | 5 | 27,280 | 26,969 | 26,506 | 0.007 | compiled=5 | 1,754,760.0 | 219,218,637.0 | 203,331.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 219,915,501.0 | 208,241,496.0 | 229,208,834.0 | 6,929,032.3 | 5 | 27,280 | 27,082 | 26,619 | 0.032 | compiled=5 | 1,750,830.0 | 218,175,101.0 | 191,351.0 |
| `wild-secrets-slack-webhook-url` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 222,112,101.0 | 219,971,508.0 | 228,719,746.0 | 3,230,894.3 | 5 | 27,280 | 26,969 | 26,506 | 0.015 | compiled=5 | 1,734,199.0 | 220,190,421.0 | 190,302.0 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 220,220,060.0 | 207,198,949.0 | 221,232,166.0 | 5,549,447.3 | 5 | 27,280 | 27,082 | 26,619 | 0.025 | compiled=5 | 1,666,309.0 | 218,389,360.0 | 190,091.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 566,348,587.0 | 549,074,169.0 | 569,079,433.0 | 7,785,141.0 | 5 | 208,424 | 552,368 (warned) | 43,101 | 0.014 | compiled=5 | 56,869,586.0 | 502,874,424.0 | 189,461.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 584,513,932.0 | 579,481,332.0 | 587,455,298.0 | 2,691,592.3 | 5 | 212,616 | 567,158 (warned) | 44,389 | 0.005 | compiled=5 | 63,726,386.0 | 520,691,186.0 | 96,360.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 358,663,068.0 | 357,289,009.0 | 371,226,876.0 | 5,966,071.8 | 5 | 208,016 | 560,244 (warned) | 16,558 | 0.017 (max is trial 1) | compiled=5 | 58,403,604.0 | 300,192,433.0 | 196,002.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 385,952,857.0 | 367,903,256.0 | 391,218,997.0 | 8,138,851.2 | 5 | 216,344 | 576,657 (warned) | 18,286 | 0.021 | compiled=5 | 65,529,033.0 | 313,719,738.0 | 99,731.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 348,228,416.0 | 341,297,056.0 | 349,546,031.0 | 3,042,016.3 | 5 | 35,880 | 39,568 | 37,719 | 0.009 | compiled=5 | 1,906,431.0 | 345,491,460.0 | 189,781.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 347,981,223.0 | 338,438,370.0 | 350,042,695.0 | 4,104,731.6 | 5 | 35,880 | 39,681 | 37,832 | 0.012 | compiled=5 | 1,923,461.0 | 346,005,423.0 | 189,111.0 |
| `wild-secrets-username-password-pair` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 347,887,902.0 | 339,145,884.0 | 359,771,097.0 | 6,973,227.9 | 5 | 35,880 | 39,568 | 37,719 | 0.020 (max is trial 1) | compiled=5 | 1,938,931.0 | 345,866,511.0 | 193,401.0 |
| `wild-secrets-username-password-pair` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 342,331,433.0 | 341,242,146.0 | 349,807,012.0 | 3,779,507.4 | 5 | 35,880 | 39,681 | 37,832 | 0.011 | compiled=5 | 1,923,730.0 | 340,241,230.0 | 191,901.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 152,350,103.0 | 146,360,049.0 | 154,948,867.0 | 3,577,509.3 | 5 | 27,608 | 19,845 | 14,138 | 0.023 | compiled=5 | 1,784,161.0 | 150,004,060.0 | 186,671.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 155,314,421.0 | 145,087,002.0 | 161,767,148.0 | 5,571,192.2 | 5 | 27,752 | 21,905 | 15,298 | 0.036 | compiled=5 | 1,736,870.0 | 153,567,131.0 | 105,481.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 155,694,792.0 | 147,594,727.0 | 158,422,056.0 | 4,343,709.4 | 5 | 27,608 | 19,845 | 14,138 | 0.028 | compiled=5 | 1,765,169.0 | 151,997,722.0 | 197,441.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 161,007,741.0 | 142,746,500.0 | 163,721,628.0 | 7,574,487.5 | 5 | 27,752 | 21,905 | 15,298 | 0.047 (max is trial 1) | compiled=5 | 1,799,590.0 | 159,107,591.0 | 109,640.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 173,468,759.0 | 167,782,236.0 | 176,733,818.0 | 3,523,111.9 | 5 | 23,104 | 19,120 | 19,120 | 0.020 | compiled=5 | 1,456,868.0 | 169,054,054.0 | 190,041.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 172,277,881.0 | 155,990,551.0 | 172,915,206.0 | 6,506,003.4 | 5 | 23,104 | 19,233 | 19,233 | 0.038 | compiled=5 | 1,449,198.0 | 170,621,842.0 | 186,061.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 161,055,595.0 | 160,799,644.0 | 171,315,331.0 | 4,380,913.7 | 5 | 23,104 | 19,120 | 19,120 | 0.027 | compiled=5 | 1,482,388.0 | 159,471,326.0 | 187,621.0 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 170,670,128.0 | 159,957,489.0 | 180,391,232.0 | 7,088,680.9 | 5 | 23,104 | 19,233 | 19,233 | 0.042 | compiled=5 | 1,462,488.0 | 169,113,379.0 | 109,411.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 168,942,348.0 | 156,913,299.0 | 174,344,490.0 | 5,821,757.7 | 5 | 27,752 | 21,904 | 16,123 | 0.034 | compiled=5 | 1,751,110.0 | 165,626,850.0 | 197,511.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 163,468,267.0 | 152,712,215.0 | 165,126,897.0 | 4,618,184.7 | 5 | 27,752 | 21,476 | 15,695 | 0.028 | compiled=5 | 1,782,231.0 | 161,604,077.0 | 191,401.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 167,336,106.0 | 159,028,111.0 | 169,534,980.0 | 4,203,234.9 | 5 | 27,752 | 21,904 | 16,123 | 0.025 | compiled=5 | 1,777,160.0 | 165,453,416.0 | 101,971.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 159,788,416.0 | 146,307,840.0 | 164,673,022.0 | 6,826,015.5 | 5 | 27,752 | 21,476 | 15,695 | 0.043 | compiled=5 | 1,747,629.0 | 157,914,045.0 | 190,041.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 151,495,346.0 | 141,726,578.0 | 152,647,211.0 | 5,081,577.5 | 5 | 23,072 | 18,305 | 18,305 | 0.034 | compiled=5 | 1,448,768.0 | 149,964,367.0 | 102,591.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 145,755,303.0 | 138,096,530.0 | 152,348,840.0 | 4,991,087.1 | 5 | 23,072 | 18,417 | 18,417 | 0.034 | compiled=5 | 1,451,579.0 | 143,821,122.0 | 108,201.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 142,667,645.0 | 139,695,798.0 | 151,835,165.0 | 4,744,247.9 | 5 | 23,072 | 18,305 | 18,305 | 0.033 | compiled=5 | 1,450,908.0 | 141,212,016.0 | 190,511.0 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 145,753,102.0 | 139,207,006.0 | 150,707,458.0 | 3,924,561.9 | 5 | 23,072 | 18,417 | 18,417 | 0.027 | compiled=5 | 1,537,578.0 | 144,101,042.0 | 100,000.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 218,354,202.0 | 217,620,778.0 | 222,741,067.0 | 1,836,958.9 | 5 | 31,792 | 30,809 | 25,975 | 0.008 | compiled=5 | 1,816,790.0 | 216,283,400.0 | 198,621.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 222,771,768.0 | 211,548,443.0 | 223,271,169.0 | 4,696,083.8 | 5 | 31,880 | 32,288 | 27,224 | 0.021 | compiled=5 | 1,846,171.0 | 220,610,385.0 | 190,771.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 148,633,734.0 | 146,206,800.0 | 158,295,547.0 | 4,657,018.5 | 5 | 27,608 | 20,448 | 13,929 | 0.031 | compiled=5 | 1,761,979.0 | 145,719,677.0 | 189,481.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 164,036,468.0 | 150,616,844.0 | 165,435,865.0 | 6,256,106.1 | 5 | 27,744 | 22,597 | 15,726 | 0.038 | compiled=5 | 1,769,419.0 | 162,085,207.0 | 188,771.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 190,070,842.0 | 182,980,932.0 | 195,095,151.0 | 4,447,712.5 | 5 | 27,320 | 21,587 | 21,587 | 0.023 (max is trial 1) | compiled=5 | 1,484,288.0 | 188,485,524.0 | 101,620.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 184,476,251.0 | 182,753,060.0 | 191,824,542.0 | 3,771,034.9 | 5 | 27,320 | 21,701 | 21,701 | 0.020 | compiled=5 | 1,494,888.0 | 182,949,202.0 | 187,781.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 186,767,737.0 | 182,792,024.0 | 193,732,635.0 | 4,237,193.5 | 5 | 27,320 | 21,587 | 21,587 | 0.023 | compiled=5 | 1,557,908.0 | 185,238,348.0 | 207,421.0 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 193,527,634.0 | 182,510,073.0 | 195,502,656.0 | 4,593,743.7 | 5 | 27,320 | 21,701 | 21,701 | 0.024 | compiled=5 | 3,094,127.0 | 190,232,446.0 | 100,551.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 138,661,656.0 | 132,947,972.0 | 146,028,847.0 | 5,438,384.7 | 5 | 27,432 | 14,431 | 12,074 | 0.039 | compiled=5 | 1,508,229.0 | 136,917,045.0 | 104,670.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 135,625,249.0 | 125,089,398.0 | 143,828,884.0 | 6,695,294.9 | 5 | 27,432 | 14,254 | 11,897 | 0.049 | compiled=5 | 1,536,538.0 | 132,608,091.0 | 98,911.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 137,976,244.0 | 136,048,053.0 | 144,371,820.0 | 3,169,357.7 | 5 | 27,432 | 14,431 | 12,074 | 0.023 | compiled=5 | 1,493,849.0 | 136,493,146.0 | 109,841.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 140,267,986.0 | 135,152,079.0 | 146,521,331.0 | 4,405,413.2 | 5 | 27,432 | 14,254 | 11,897 | 0.031 | compiled=5 | 1,494,588.0 | 138,569,147.0 | 198,221.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 231,881,539.0 | 223,608,832.0 | 233,852,071.0 | 4,115,708.7 | 5 | 27,440 | 26,116 | 25,423 | 0.018 | compiled=5 | 1,586,349.0 | 230,114,528.0 | 101,441.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 231,516,536.0 | 225,056,460.0 | 232,307,781.0 | 2,706,014.2 | 5 | 27,440 | 26,229 | 25,536 | 0.012 | compiled=5 | 1,610,100.0 | 229,702,256.0 | 105,890.0 |
| `wild-validator-email-owasp` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 231,134,100.0 | 224,032,060.0 | 232,098,476.0 | 3,554,445.0 | 5 | 27,440 | 26,116 | 25,423 | 0.015 | compiled=5 | 1,598,858.0 | 229,428,391.0 | 98,431.0 |
| `wild-validator-email-owasp` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 232,628,947.0 | 222,720,196.0 | 234,217,958.0 | 4,290,884.1 | 5 | 27,440 | 26,229 | 25,536 | 0.018 | compiled=5 | 1,645,448.0 | 230,666,738.0 | 114,871.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 315,594,239.0 | 298,585,852.0 | 318,135,703.0 | 7,433,807.8 | 5 | 40,776 | 44,458 | 39,430 | 0.024 (max is trial 1) | compiled=5 | 1,961,161.0 | 313,430,097.0 | 102,101.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 310,833,843.0 | 302,739,466.0 | 322,732,022.0 | 6,415,713.7 | 5 | 40,568 | 43,641 | 38,613 | 0.021 (max is trial 1) | compiled=5 | 1,989,661.0 | 308,290,749.0 | 116,170.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 166,272,761.0 | 157,333,461.0 | 171,647,841.0 | 4,880,503.6 | 5 | 32,424 | 21,817 | 16,789 | 0.029 | compiled=5 | 1,771,140.0 | 162,715,411.0 | 196,041.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 160,721,231.0 | 153,198,668.0 | 164,006,178.0 | 3,675,198.3 | 5 | 32,224 | 20,895 | 15,867 | 0.023 | compiled=5 | 1,748,659.0 | 158,641,619.0 | 103,440.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 276,581,400.0 | 274,485,559.0 | 292,338,959.0 | 6,497,267.0 | 5 | 27,240 | 31,534 | 31,534 | 0.023 | compiled=5 | 1,688,490.0 | 274,818,670.0 | 100,090.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 275,491,495.0 | 269,294,539.0 | 276,253,558.0 | 2,813,711.1 | 5 | 27,240 | 31,647 | 31,647 | 0.010 | compiled=5 | 1,697,149.0 | 273,695,854.0 | 101,761.0 |
| `wild-validator-ipv4-owasp` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 275,115,141.0 | 269,101,580.0 | 279,120,065.0 | 3,230,655.7 | 5 | 27,240 | 31,534 | 31,534 | 0.012 (max is trial 1) | compiled=5 | 1,698,689.0 | 273,307,782.0 | 186,901.0 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 273,815,805.0 | 268,398,805.0 | 276,210,897.0 | 3,080,470.2 | 5 | 27,240 | 31,647 | 31,647 | 0.011 | compiled=5 | 1,718,999.0 | 269,928,264.0 | 106,870.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 205,549,980.0 | 198,018,965.0 | 208,052,832.0 | 3,515,397.8 | 5 | 31,888 | 26,767 | 24,223 | 0.017 | compiled=5 | 1,620,400.0 | 203,659,788.0 | 102,201.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 204,586,934.0 | 193,319,639.0 | 206,843,697.0 | 4,891,057.8 | 5 | 31,808 | 26,507 | 23,963 | 0.024 | compiled=5 | 1,734,920.0 | 202,678,962.0 | 211,992.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 147,706,118.0 | 139,079,611.0 | 149,616,709.0 | 4,562,178.1 | 5 | 27,672 | 15,669 | 13,125 | 0.031 | compiled=5 | 1,474,908.0 | 144,503,160.0 | 115,871.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 137,154,900.0 | 129,516,107.0 | 147,658,717.0 | 5,986,149.8 | 5 | 23,496 | 15,306 | 12,762 | 0.044 | compiled=5 | 1,601,739.0 | 135,286,689.0 | 123,130.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 187,085,906.0 | 177,414,120.0 | 189,208,119.0 | 4,934,784.7 | 5 | 27,200 | 20,231 | 20,231 | 0.026 | compiled=5 | 1,491,088.0 | 184,763,602.0 | 189,511.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 181,954,426.0 | 177,233,849.0 | 192,569,278.0 | 5,922,972.0 | 5 | 27,200 | 20,342 | 20,342 | 0.033 | compiled=5 | 1,714,790.0 | 180,261,267.0 | 196,041.0 |
| `wild-validator-us-zip-owasp` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 187,966,683.0 | 176,400,249.0 | 210,422,717.0 | 11,579,352.7 | 5 | 27,200 | 20,231 | 20,231 | 0.062 | compiled=5 | 2,974,326.0 | 184,676,755.0 | 191,401.0 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 184,945,276.0 | 178,219,350.0 | 186,230,284.0 | 2,963,092.1 | 5 | 27,200 | 20,342 | 20,342 | 0.016 | compiled=5 | 1,519,008.0 | 183,192,687.0 | 191,961.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 237,956,934.0 | 235,145,529.0 | 250,340,844.0 | 5,697,957.4 | 5 | 36,384 | 46,431 | 21,113 | 0.024 (max is trial 1) | compiled=5 | 3,098,478.0 | 234,653,215.0 | 107,680.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 242,521,171.0 | 241,595,655.0 | 256,982,703.0 | 6,214,711.5 | 5 | 36,528 | 49,292 | 22,701 | 0.026 (max is trial 1) | compiled=5 | 3,157,309.0 | 239,172,441.0 | 191,421.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 243,325,487.0 | 234,648,620.0 | 249,193,630.0 | 5,183,392.9 | 5 | 36,384 | 46,431 | 21,113 | 0.021 (max is trial 1) | compiled=5 | 3,103,337.0 | 240,105,810.0 | 117,611.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 255,234,264.0 | 242,917,785.0 | 267,131,979.0 | 8,955,084.1 | 5 | 36,528 | 49,292 | 22,701 | 0.035 | compiled=5 | 3,685,411.0 | 247,502,001.0 | 204,211.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 253,615,581.0 | 244,364,940.0 | 254,330,865.0 | 4,581,012.0 | 5 | 27,208 | 20,731 | 20,500 | 0.018 | compiled=5 | 1,594,969.0 | 251,758,491.0 | 115,221.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 256,015,265.0 | 248,550,583.0 | 257,679,874.0 | 3,179,293.5 | 5 | 27,208 | 20,842 | 20,611 | 0.012 (max is trial 1) | compiled=5 | 1,520,989.0 | 254,257,675.0 | 99,881.0 |
| `wild-validator-uuid-grok` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 252,678,750.0 | 239,408,477.0 | 253,310,673.0 | 5,405,004.9 | 5 | 27,208 | 20,731 | 20,500 | 0.021 | compiled=5 | 1,516,298.0 | 251,062,371.0 | 101,850.0 |
| `wild-validator-uuid-grok` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 251,306,811.0 | 248,227,515.0 | 255,987,968.0 | 3,087,906.0 | 5 | 27,208 | 20,842 | 20,611 | 0.012 | compiled=5 | 1,515,238.0 | 248,279,894.0 | 196,421.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 218,216,571.0 | 215,833,438.0 | 225,889,876.0 | 3,479,611.4 | 5 | 85,552 | 226,431 | 18,465 | 0.016 | compiled=5 | 13,870,289.0 | 204,120,081.0 | 215,811.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 232,701,405.0 | 231,767,429.0 | 238,502,898.0 | 3,005,584.1 | 5 | 89,792 | 236,262 | 20,441 | 0.013 | compiled=5 | 15,453,158.0 | 217,288,176.0 | 205,271.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 224,934,046.0 | 210,237,773.0 | 236,848,993.0 | 8,920,458.8 | 5 | 85,552 | 226,431 | 18,465 | 0.040 (max is trial 1) | compiled=5 | 14,062,398.0 | 203,214,036.0 | 220,551.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 243,627,209.0 | 223,870,351.0 | 261,475,368.0 | 12,381,799.0 | 5 | 89,792 | 236,262 | 20,441 | 0.051 | compiled=5 | 24,984,909.0 | 223,230,706.0 | 197,191.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 440,611,676.0 | 431,434,584.0 | 448,410,630.0 | 5,679,423.9 | 5 | 31,376 | 59,482 | 59,019 | 0.013 | compiled=5 | 2,245,243.0 | 438,294,613.0 | 104,521.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 438,925,976.0 | 435,586,798.0 | 442,943,119.0 | 2,440,004.2 | 5 | 31,376 | 59,597 | 59,134 | 0.006 | compiled=5 | 2,247,042.0 | 434,144,389.0 | 116,500.0 |
| `wild-waf-crs-942140-dbnames` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 440,900,844.0 | 438,469,010.0 | 444,496,954.0 | 1,985,974.3 | 5 | 31,376 | 59,482 | 59,019 | 0.005 | compiled=5 | 2,290,122.0 | 438,529,381.0 | 204,321.0 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 442,683,734.0 | 438,853,243.0 | 445,996,471.0 | 2,496,064.0 | 5 | 31,376 | 59,597 | 59,134 | 0.006 | compiled=5 | 2,380,963.0 | 440,234,330.0 | 109,021.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 191,468,978.0 | 182,435,925.0 | 191,846,820.0 | 3,559,515.6 | 5 | 36,248 | 56,713 | 16,313 | 0.019 | compiled=5 | 4,368,135.0 | 186,833,671.0 | 193,551.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 200,318,939.0 | 186,811,242.0 | 211,003,219.0 | 8,260,172.7 | 5 | 36,392 | 60,492 | 18,104 | 0.041 (max is trial 1) | compiled=5 | 4,875,688.0 | 195,402,661.0 | 199,681.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 190,502,815.0 | 190,168,014.0 | 195,507,761.0 | 1,997,773.5 | 5 | 36,248 | 56,713 | 16,313 | 0.010 (max is trial 1) | compiled=5 | 4,377,825.0 | 185,810,629.0 | 106,640.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 200,423,621.0 | 200,184,068.0 | 208,824,596.0 | 3,395,128.0 | 5 | 36,392 | 60,492 | 18,104 | 0.017 | compiled=5 | 4,882,257.0 | 195,441,073.0 | 101,201.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 221,989,723.0 | 214,553,879.0 | 222,513,667.0 | 3,003,155.6 | 5 | 27,280 | 25,370 | 24,908 | 0.014 | compiled=5 | 1,602,689.0 | 220,211,912.0 | 187,231.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 219,977,991.0 | 213,796,126.0 | 224,407,267.0 | 4,253,356.3 | 5 | 27,280 | 25,483 | 25,021 | 0.019 | compiled=5 | 1,640,240.0 | 216,460,092.0 | 189,261.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 221,488,278.0 | 213,725,906.0 | 223,460,948.0 | 3,428,653.5 | 5 | 27,280 | 25,370 | 24,908 | 0.015 | compiled=5 | 1,612,999.0 | 219,696,348.0 | 107,420.0 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 223,549,838.0 | 217,279,324.0 | 224,213,531.0 | 2,558,564.6 | 5 | 27,280 | 25,483 | 25,021 | 0.011 | compiled=5 | 1,638,889.0 | 221,808,939.0 | 102,010.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 166,219,353.0 | 159,098,203.0 | 169,880,154.0 | 3,573,699.3 | 5 | 27,872 | 35,397 | 14,230 | 0.021 | compiled=5 | 3,087,688.0 | 162,282,690.0 | 107,461.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 177,119,687.0 | 170,724,550.0 | 182,162,593.0 | 3,656,849.2 | 5 | 32,112 | 38,421 | 16,242 | 0.021 | compiled=5 | 3,179,128.0 | 173,725,256.0 | 196,191.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 165,086,465.0 | 158,964,390.0 | 166,369,281.0 | 3,107,935.0 | 5 | 27,872 | 35,397 | 14,230 | 0.019 | compiled=5 | 3,093,767.0 | 161,904,997.0 | 98,991.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 182,435,482.0 | 179,271,002.0 | 183,422,186.0 | 1,760,137.3 | 5 | 32,112 | 38,421 | 16,242 | 0.010 | compiled=5 | 7,175,960.0 | 175,960,185.0 | 208,671.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 189,788,862.0 | 175,436,080.0 | 192,934,338.0 | 6,447,602.0 | 5 | 27,240 | 22,668 | 22,437 | 0.034 | compiled=5 | 1,775,300.0 | 188,136,662.0 | 191,031.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 190,864,547.0 | 180,698,139.0 | 191,217,399.0 | 4,108,300.2 | 5 | 27,240 | 22,781 | 22,550 | 0.022 | compiled=5 | 1,568,109.0 | 189,153,057.0 | 108,570.0 |
| `wild-waf-crs-942270-union-select` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 189,770,882.0 | 181,893,880.0 | 195,069,091.0 | 5,069,561.5 | 5 | 27,240 | 22,668 | 22,437 | 0.027 | compiled=5 | 1,563,179.0 | 187,966,883.0 | 100,300.0 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 181,194,936.0 | 173,612,466.0 | 193,856,086.0 | 7,247,460.8 | 5 | 27,240 | 22,781 | 22,550 | 0.040 | compiled=5 | 1,532,448.0 | 179,655,128.0 | 197,602.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 1,438,672,310.0 | 1,432,962,787.0 | 1,443,932,150.0 | 4,203,645.0 | 5 | 680,264 | 393,492 (warned) | 99,012 | 0.003 | compiled=5 | 11,728,217.0 | 1,426,285,749.0 | 520,053.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 1,369,454,394.0 | 1,365,376,499.0 | 1,382,138,676.0 | 7,317,590.3 | 5 | 659,736 | 400,698 (warned) | 101,162 | 0.005 (max is trial 1) | compiled=5 | 12,418,691.0 | 1,356,476,009.0 | 289,721.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 1,433,276,077.0 | 1,423,942,846.0 | 1,439,115,490.0 | 6,231,497.1 | 5 | 680,264 | 393,492 (warned) | 99,012 | 0.004 | compiled=5 | 11,815,085.0 | 1,415,190,608.0 | 504,123.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 1,405,201,263.0 | 1,365,734,414.0 | 1,426,091,089.0 | 23,994,443.3 | 5 | 659,736 | 400,698 (warned) | 101,162 | 0.017 | compiled=5 | 12,529,700.0 | 1,392,124,750.0 | 546,813.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 1,649,976,129.0 | 1,648,203,898.0 | 1,654,164,693.0 | 2,234,896.9 | 5 | 60,264 | 182,777 | 181,154 | 0.001 (max is trial 1) | compiled=5 | 4,442,705.0 | 1,645,438,844.0 | 107,030.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 1,661,395,705.0 | 1,659,971,358.0 | 1,663,037,794.0 | 1,004,372.2 | 5 | 60,264 | 182,892 | 181,269 | 0.001 | compiled=5 | 4,455,805.0 | 1,656,832,209.0 | 107,691.0 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 1,654,265,342.0 | 1,647,666,868.0 | 1,656,161,623.0 | 3,059,089.9 | 5 | 60,264 | 182,777 | 181,154 | 0.002 | compiled=5 | 4,447,354.0 | 1,649,644,548.0 | 196,261.0 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 1,662,964,961.0 | 1,661,276,402.0 | 1,669,127,934.0 | 2,919,869.3 | 5 | 60,264 | 182,892 | 181,269 | 0.002 | compiled=5 | 4,407,984.0 | 1,658,621,138.0 | 102,040.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 2,182,202.0 | - | - |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 4,000,323.0 | - | - |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 4,074,833.0 | - | - |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | - | - | - | - | 0 | - | - | - |  | did-not-compile=1 | 3,950,952.0 | - | - |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 185,991,340.0 | 172,197,042.0 | 187,952,461.0 | 5,918,184.3 | 5 | 27,320 | 21,868 | 21,175 | 0.032 | compiled=5 | 1,549,799.0 | 184,343,100.0 | 108,331.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 182,510,141.0 | 181,468,984.0 | 188,270,974.0 | 3,128,585.5 | 5 | 27,320 | 21,981 | 21,288 | 0.017 | compiled=5 | 1,574,629.0 | 180,697,630.0 | 110,990.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 187,731,661.0 | 181,376,157.0 | 189,237,560.0 | 2,756,659.5 | 5 | 27,320 | 21,868 | 21,175 | 0.015 | compiled=5 | 1,556,289.0 | 185,964,112.0 | 106,191.0 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 188,916,698.0 | 175,793,887.0 | 192,204,276.0 | 5,750,003.9 | 5 | 27,320 | 21,981 | 21,288 | 0.030 | compiled=5 | 1,599,269.0 | 187,208,769.0 | 108,660.0 |
| `winpath-near-miss` | `plain` | `pcrec_a770139e_auto-caps-simdna` | 130,977,040.0 | 130,213,996.0 | 140,501,366.0 | 3,896,909.4 | 5 | 27,392 | 13,818 | 11,735 | 0.030 | compiled=5 | 1,466,798.0 | 128,768,088.0 | 192,131.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a770139e_auto-caps-simdna` | 141,394,501.0 | 133,050,893.0 | 143,237,712.0 | 3,839,310.4 | 5 | 23,256 | 13,641 | 11,558 | 0.027 | compiled=5 | 1,503,849.0 | 138,304,753.0 | 124,361.0 |
| `winpath-near-miss` | `plain` | `pcrec_a770139e_auto-nocaps-simdna` | 143,039,512.0 | 139,874,875.0 | 143,363,173.0 | 1,397,474.2 | 5 | 27,392 | 13,818 | 11,735 | 0.010 | compiled=5 | 1,483,118.0 | 141,432,984.0 | 114,890.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a770139e_auto-nocaps-simdna` | 138,097,515.0 | 123,393,523.0 | 143,059,852.0 | 7,481,886.7 | 5 | 23,256 | 13,641 | 11,558 | 0.054 | compiled=5 | 1,471,928.0 | 136,526,536.0 | 186,781.0 |
| `winpath-near-miss` | `plain` | `pcrec_a770139e_vm-caps-simdna` | 204,609,205.0 | 194,176,196.0 | 210,673,589.0 | 6,178,740.2 | 5 | 27,400 | 23,607 | 23,145 | 0.030 | compiled=5 | 1,592,529.0 | 201,380,737.0 | 107,471.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a770139e_vm-caps-simdna` | 196,052,446.0 | 183,482,296.0 | 201,053,674.0 | 6,390,104.2 | 5 | 27,400 | 23,720 | 23,258 | 0.033 | compiled=5 | 1,544,979.0 | 193,726,573.0 | 102,520.0 |
| `winpath-near-miss` | `plain` | `pcrec_a770139e_vm-in-caps-simdna` | 201,671,237.0 | 197,364,795.0 | 208,749,777.0 | 3,818,667.2 | 5 | 27,400 | 23,607 | 23,145 | 0.019 | compiled=5 | 1,605,798.0 | 199,855,738.0 | 206,311.0 |
| `winpath-near-miss` | `whole-subject` | `pcrec_a770139e_vm-in-caps-simdna` | 200,537,923.0 | 191,041,759.0 | 204,785,335.0 | 5,089,963.0 | 5 | 27,400 | 23,720 | 23,258 | 0.025 | compiled=5 | 1,553,529.0 | 198,394,761.0 | 116,930.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23,940.0 | 20,160.0 | 95,441.0 | 28,746.8 | 5 | 209 | 1.201 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,050.0 | 10,880.0 | 83,390.0 | 28,190.1 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,590.0 | 17,020.0 | 97,961.0 | 30,721.3 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 18,410.0 | 16,670.0 | 89,860.0 | 28,558.1 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,320.0 | 16,260.0 | 92,580.0 | 29,454.5 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,160.0 | 13,260.0 | 92,280.0 | 30,624.9 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,040.0 | 11,560.0 | 80,251.0 | 26,596.0 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,310.0 | 11,050.0 | 79,670.0 | 26,696.2 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 48,060.0 | 39,100.0 | 199,141.0 | 60,526.2 | 5 | 192 | 1.259 (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 15,140.0 | 12,260.0 | 97,400.0 | 33,049.8 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 22,260.0 | 19,410.0 | 159,721.0 | 54,857.0 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,440.0 | 12,210.0 | 86,920.0 | 29,069.7 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 25,360.0 | 20,401.0 | 149,391.0 | 49,970.6 | 5 | 184 | 1.970 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 18,070.0 | 15,250.0 | 87,301.0 | 27,830.5 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,370.0 | 5,980.0 | 78,090.0 | 28,326.6 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,820.0 | 6,410.0 | 70,170.0 | 24,949.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 62,290.0 | 54,260.0 | 228,532.0 | 66,990.6 | 5 | 693 | 1.075 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 15,020.0 | 12,310.0 | 151,091.0 | 54,584.1 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 30,550.0 | 25,050.0 | 109,910.0 | 32,655.9 | 5 | 376 | 1.069 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 29,761.0 | 23,300.0 | 102,310.0 | 29,894.1 | 5 | 376 | 1.004 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,301.0 | 9,940.0 | 70,310.0 | 23,341.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 30,080.0 | 26,050.0 | 109,620.0 | 32,029.8 | 5 | 265 | 1.065 (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 38,170.0 | 33,201.0 | 123,141.0 | 34,252.6 | 5 | 247 | 0.897 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 23,660.0 | 18,680.0 | 158,520.0 | 54,254.1 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 35,220.0 | 25,750.0 | 170,631.0 | 54,919.7 | 5 | 173 | 1.559 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,101.0 | 11,200.0 | 68,610.0 | 22,297.2 | 5 | 195 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 28,250.0 | 18,880.0 | 112,710.0 | 35,564.9 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 21,440.0 | 17,981.0 | 100,751.0 | 31,909.8 | 5 | 227 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,700.0 | 10,390.0 | 72,851.0 | 24,210.8 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,820.0 | 29,950.0 | 116,740.0 | 33,216.8 | 5 | 254 | 0.982 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 21,150.0 | 17,740.0 | 81,281.0 | 24,265.4 | 5 | 261 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,581.0 | 19,550.0 | 160,690.0 | 54,754.7 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9,270.0 | 7,690.0 | 69,811.0 | 24,221.2 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,400.0 | 30,250.0 | 175,211.0 | 56,640.6 | 5 | 425 | 1.696 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,690.0 | 6,170.0 | 66,851.0 | 23,726.1 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,040.0 | 12,870.0 | 77,390.0 | 24,615.1 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 27,480.0 | 22,340.0 | 107,671.0 | 32,673.3 | 5 | 270 | 1.189 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 7,980.0 | 6,450.0 | 66,771.0 | 23,617.7 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 17,740.0 | 13,860.0 | 97,390.0 | 32,115.2 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 1,970,240.0 | 1,872,820.0 | 2,127,901.0 | 91,842.6 | 5 | 16,813 | 0.047 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 65,950.0 | 59,521.0 | 271,041.0 | 82,129.1 | 5 | 421 | 1.245 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 24,250.0 | 17,620.0 | 108,151.0 | 34,609.8 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,100.0 | 15,770.0 | 103,661.0 | 34,008.5 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 34,450.0 | 26,670.0 | 122,381.0 | 36,615.9 | 5 | 371 | 1.063 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 33,800.0 | 25,420.0 | 115,071.0 | 33,329.1 | 5 | 371 | 0.986 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 577,973.0 | 558,943.0 | 749,784.0 | 70,790.1 | 5 | 10,481 | 0.122 (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,360.0 | 13,470.0 | 100,580.0 | 33,886.7 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 22,540.0 | 19,240.0 | 106,451.0 | 33,774.7 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,140.0 | 13,180.0 | 92,991.0 | 30,948.5 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 29,590.0 | 27,270.0 | 109,070.0 | 31,746.1 | 5 | 353 | 1.073 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 48,450.0 | 43,400.0 | 127,270.0 | 31,719.4 | 5 | 778 | 0.655 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,550.0 | 10,160.0 | 74,621.0 | 24,956.4 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 11,990.0 | 9,610.0 | 75,051.0 | 25,373.7 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 12,080.0 | 10,140.0 | 76,170.0 | 25,698.5 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,400.0 | 16,270.0 | 103,871.0 | 33,935.7 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 86,791.0 | 79,180.0 | 262,821.0 | 70,490.7 | 5 | 1,047 | 0.812 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 9,830.0 | 7,960.0 | 68,160.0 | 23,427.2 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,880.0 | 12,490.0 | 97,080.0 | 32,967.5 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 73,570.0 | 68,960.0 | 180,851.0 | 42,863.1 | 5 | 788 | 0.583 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 20,130.0 | 17,450.0 | 101,721.0 | 32,685.5 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 14,090.0 | 11,700.0 | 86,911.0 | 29,289.8 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 386,192.0 | 370,512.0 | 560,423.0 | 71,007.3 | 5 | 3,459 | 0.184 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 16,541.0 | 13,700.0 | 95,000.0 | 31,506.6 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 13,250.0 | 10,870.0 | 88,231.0 | 30,074.8 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,660.0 | 2,840.0 | 44,281.0 | 16,305.7 | 5 | 209 | timer-floor (max is trial 1) | compiled=5 |
| `balanced-parens-rec` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,820.0 | 1,360.0 | 21,120.0 | 7,763.8 | 5 | 209 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,730.0 | 2,530.0 | 21,710.0 | 7,544.2 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,760.0 | 2,860.0 | 33,470.0 | 11,937.4 | 5 | 220 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,260.0 | 2,620.0 | 30,471.0 | 10,903.4 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,310.0 | 2,620.0 | 27,400.0 | 9,678.7 | 5 | 240 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,670.0 | 1,320.0 | 19,780.0 | 7,261.1 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,040.0 | 3,180.0 | 51,540.0 | 19,040.6 | 5 | 211 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,290.0 | 1,910.0 | 21,891.0 | 7,847.7 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,570.0 | 4,590.0 | 47,891.0 | 16,954.4 | 5 | 217 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,020.0 | 1,580.0 | 21,050.0 | 7,642.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,430.0 | 1,860.0 | 24,930.0 | 9,042.8 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,140.0 | 1,720.0 | 26,560.0 | 9,798.1 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,720.0 | 1,370.0 | 26,750.0 | 10,025.5 | 5 | 244 | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,750.0 | 1,470.0 | 27,350.0 | 10,231.0 | 5 | 177 | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,950.0 | 2,420.0 | 28,750.0 | 10,339.9 | 5 | 192 | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,950.0 | 1,580.0 | 20,590.0 | 7,451.4 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,430.0 | 2,700.0 | 37,540.0 | 13,649.4 | 5 | 214 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,920.0 | 1,560.0 | 22,310.0 | 8,166.5 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,530.0 | 3,140.0 | 46,020.0 | 16,946.4 | 5 | 204 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,730.0 | 1,440.0 | 26,000.0 | 9,692.9 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,540.0 | 1,180.0 | 19,860.0 | 7,344.9 | 5 | 212 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,240.0 | 1,170.0 | 17,880.0 | 6,641.1 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,040.0 | 930.0 | 16,370.0 | 6,132.0 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,570.0 | 3,790.0 | 51,871.0 | 18,907.1 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,560.0 | 2,100.0 | 24,400.0 | 8,733.7 | 5 | 246 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 970.0 | 870.0 | 37,891.0 | 14,759.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 450.0 | 380.0 | 20,270.0 | 7,920.5 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,090.0 | 970.0 | 23,350.0 | 8,898.0 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 890.0 | 780.0 | 19,550.0 | 7,454.1 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 10,990.0 | 9,530.0 | 63,711.0 | 21,103.7 | 5 | 693 | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,440.0 | 3,810.0 | 34,630.0 | 12,077.5 | 5 | 693 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,250.0 | 1,140.0 | 20,790.0 | 7,803.4 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,500.0 | 2,250.0 | 39,140.0 | 14,630.2 | 5 | 186 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,140.0 | 5,590.0 | 23,970.0 | 7,139.8 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,140.0 | 5,670.0 | 23,681.0 | 7,032.3 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,140.0 | 5,620.0 | 23,130.0 | 6,815.2 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,700.0 | 7,130.0 | 31,090.0 | 9,353.1 | 5 | 376 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,600.0 | 2,080.0 | 49,411.0 | 18,752.8 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,090.0 | 890.0 | 21,330.0 | 8,103.5 | 5 | 197 | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 7,870.0 | 6,540.0 | 56,460.0 | 19,545.9 | 5 | 265 | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,720.0 | 3,200.0 | 26,670.0 | 9,199.0 | 5 | 265 | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,830.0 | 5,430.0 | 54,961.0 | 19,332.4 | 5 | 247 | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,340.0 | 2,750.0 | 28,620.0 | 10,131.0 | 5 | 247 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,310.0 | 1,040.0 | 21,440.0 | 8,055.4 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,670.0 | 2,230.0 | 42,180.0 | 15,792.0 | 5 | 171 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,680.0 | 1,330.0 | 21,510.0 | 7,960.6 | 5 | 173 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,310.0 | 1,040.0 | 17,700.0 | 6,568.1 | 5 | 173 | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,600.0 | 2,370.0 | 25,711.0 | 9,267.0 | 5 | 195 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,320.0 | 2,840.0 | 27,560.0 | 9,691.6 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,400.0 | 2,800.0 | 31,810.0 | 11,391.6 | 5 | 299 | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,920.0 | 2,230.0 | 28,830.0 | 10,428.8 | 5 | 227 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,190.0 | 1,050.0 | 20,190.0 | 7,591.2 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,040.0 | 900.0 | 21,680.0 | 8,258.9 | 5 | 184 | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,611.0 | 3,920.0 | 31,270.0 | 10,716.3 | 5 | 254 | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,360.0 | 3,770.0 | 30,250.0 | 10,347.4 | 5 | 254 | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,130.0 | 3,160.0 | 30,540.0 | 10,651.9 | 5 | 261 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,390.0 | 1,140.0 | 22,240.0 | 8,342.6 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,620.0 | 2,010.0 | 41,431.0 | 15,537.3 | 5 | 172 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,420.0 | 1,240.0 | 22,070.0 | 8,253.5 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,380.0 | 1,200.0 | 30,010.0 | 11,441.2 | 5 | 231 | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 7,620.0 | 7,060.0 | 49,290.0 | 16,612.0 | 5 | 425 | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,090.0 | 2,850.0 | 21,801.0 | 7,468.5 | 5 | 425 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 350.0 | 310.0 | 14,440.0 | 5,632.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 940.0 | 800.0 | 38,190.0 | 14,891.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,830.0 | 1,630.0 | 21,920.0 | 8,030.8 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,610.0 | 2,200.0 | 44,640.0 | 16,811.0 | 5 | 199 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,370.0 | 4,580.0 | 59,800.0 | 21,748.6 | 5 | 270 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 7,630.0 | 6,410.0 | 47,420.0 | 15,970.1 | 5 | 270 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 350.0 | 320.0 | 15,340.0 | 5,989.2 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 470.0 | 420.0 | 18,960.0 | 7,389.4 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,780.0 | 2,340.0 | 21,340.0 | 7,431.2 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,340.0 | 2,890.0 | 26,150.0 | 9,117.0 | 5 | 243 | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 289,142.0 | 272,832.0 | 330,232.0 | 21,213.3 | 5 | 16,813 | 0.073 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 282,442.0 | 275,561.0 | 336,012.0 | 22,291.8 | 5 | 16,813 | 0.079 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 8,010.0 | 6,840.0 | 27,760.0 | 7,980.6 | 5 | 421 | timer-floor (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 8,010.0 | 6,950.0 | 27,880.0 | 8,019.1 | 5 | 421 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,300.0 | 3,340.0 | 30,780.0 | 10,649.7 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,030.0 | 3,400.0 | 32,430.0 | 11,357.3 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,350.0 | 3,500.0 | 25,781.0 | 8,620.4 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,300.0 | 3,430.0 | 27,570.0 | 9,371.1 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,290.0 | 4,550.0 | 25,140.0 | 7,951.8 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,200.0 | 4,410.0 | 25,600.0 | 8,196.7 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 5,380.0 | 4,580.0 | 32,440.0 | 10,846.3 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,230.0 | 4,510.0 | 26,790.0 | 8,618.7 | 5 | 371 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 107,590.0 | 93,530.0 | 153,791.0 | 21,968.4 | 5 | 10,481 | 0.204 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 104,170.0 | 91,420.0 | 151,560.0 | 21,955.5 | 5 | 10,481 | 0.211 (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,490.0 | 1,990.0 | 20,280.0 | 7,141.3 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,440.0 | 1,930.0 | 20,510.0 | 7,261.2 | 5 | 248 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 4,040.0 | 3,610.0 | 25,330.0 | 8,507.4 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,100.0 | 3,620.0 | 21,260.0 | 6,872.6 | 5 | 340 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,940.0 | 1,670.0 | 19,660.0 | 7,079.1 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,610.0 | 3,940.0 | 46,580.0 | 16,807.6 | 5 | 229 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,830.0 | 3,600.0 | 22,200.0 | 7,329.3 | 5 | 353 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 4,020.0 | 3,670.0 | 22,551.0 | 7,408.1 | 5 | 353 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 10,010.0 | 8,740.0 | 32,980.0 | 9,280.6 | 5 | 778 | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 10,130.0 | 8,930.0 | 34,900.0 | 9,993.0 | 5 | 778 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,170.0 | 1,040.0 | 22,030.0 | 8,327.9 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,130.0 | 1,020.0 | 16,700.0 | 6,217.5 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 720.0 | 620.0 | 16,830.0 | 6,441.8 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 610.0 | 530.0 | 15,740.0 | 6,050.7 | 5 | 166 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,120.0 | 850.0 | 19,760.0 | 7,472.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,340.0 | 1,030.0 | 32,631.0 | 12,537.1 | 5 | 174 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 3,540.0 | 3,040.0 | 22,970.0 | 7,786.7 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,490.0 | 2,960.0 | 23,960.0 | 8,207.6 | 5 | 320 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 6,510.0 | 6,240.0 | 29,860.0 | 9,293.8 | 5 | 1,047 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 6,440.0 | 6,070.0 | 29,090.0 | 8,997.6 | 5 | 1,047 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,360.0 | 1,060.0 | 19,110.0 | 7,114.6 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 3,500.0 | 2,680.0 | 48,831.0 | 18,178.9 | 5 | 180 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,260.0 | 2,060.0 | 20,960.0 | 7,459.0 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,180.0 | 2,020.0 | 23,250.0 | 8,415.4 | 5 | 375 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 16,350.0 | 15,360.0 | 39,960.0 | 9,510.4 | 5 | 788 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 16,520.0 | 15,300.0 | 40,660.0 | 9,739.2 | 5 | 788 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,680.0 | 2,400.0 | 21,020.0 | 7,331.6 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,640.0 | 2,340.0 | 19,560.0 | 6,775.5 | 5 | 216 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 1,480.0 | 1,310.0 | 15,860.0 | 5,753.0 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 1,500.0 | 1,340.0 | 15,910.0 | 5,767.0 | 5 | 193 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 68,260.0 | 67,061.0 | 101,170.0 | 13,114.6 | 5 | 3,459 | 0.192 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 73,020.0 | 67,181.0 | 105,251.0 | 14,053.5 | 5 | 3,459 | 0.192 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,870.0 | 2,420.0 | 23,210.0 | 8,142.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,830.0 | 2,310.0 | 24,250.0 | 8,603.8 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_dfa-nocaps-simdna` | 2,470.0 | 2,100.0 | 20,550.0 | 7,240.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 2,410.0 | 2,040.0 | 21,711.0 | 7,735.0 | 5 | 275 | timer-floor (max is trial 1) | compiled=5 |

