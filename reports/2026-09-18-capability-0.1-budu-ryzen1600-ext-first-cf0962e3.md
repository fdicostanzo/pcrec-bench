# pcrec-bench report

reporter: v24 (2026-09-26)

## Query

- filters: subbench=capability, version=0.1, since=2026-09-18T03:00:00Z, until=2026-09-18T06:00:00Z, testee=re2_11.0.0_default-caps-simdna, testee=re2_11.0.0_longest-caps-simdna, testee=oniguruma_6.9.10_default-caps-simdna, testee=tre_0.9.0_default-caps-simdna, testee=vectorscan_5.4.11_block-nosom-nocaps-simd
- record source: store/index.tsv (5 record(s) matching this query)
- records included: 5
- worst other-core busy: 76.52% (`vectorscan_5.4.11_block-nosom-nocaps-simd` / `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput`)
    - `capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260918T040233Z` (store/records/capability@0.1/oniguruma_6.9.10_default-caps-simdna/capability@0.1__oniguruma_6.9.10_default-caps-simdna__budu-ryzen1600__20260918T040233Z.jsonl) — agreement: agree (0 of 123 groups; 0 of 4831 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260918T033345Z` (store/records/capability@0.1/re2_11.0.0_default-caps-simdna/capability@0.1__re2_11.0.0_default-caps-simdna__budu-ryzen1600__20260918T033345Z.jsonl) — agreement: agree (0 of 77 groups; 0 of 3037 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__re2_11.0.0_longest-caps-simdna__budu-ryzen1600__20260918T052217Z` (store/records/capability@0.1/re2_11.0.0_longest-caps-simdna/capability@0.1__re2_11.0.0_longest-caps-simdna__budu-ryzen1600__20260918T052217Z.jsonl) — agreement: agree (0 of 77 groups; 0 of 3034 rows; 8 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260918T043931Z` (store/records/capability@0.1/tre_0.9.0_default-caps-simdna/capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__20260918T043931Z.jsonl) — agreement: agree (0 of 79 groups; 0 of 3142 rows; 56 unjudged; k=1.5, 2/3; 5 trials)
    - `capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260918T045924Z` (store/records/capability@0.1/vectorscan_5.4.11_block-nosom-nocaps-simd/capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__budu-ryzen1600__20260918T045924Z.jsonl) — agreement: agree (0 of 80 groups; 1 of 3118 rows; 2 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): capability@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 5 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 98.6 | 0.0001 | 96.2 | 99.6 | 1.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.7 | 0.0002 | 284.4 | 287.5 | 1.2 | 2.886x | 2.886x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.1 | 0.0002 | 284.6 | 286.9 | 0.8 | 2.900x | 2.900x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,845,276.0 | 8.6069 | 11,812,971.8 | 11,862,771.1 | 17,777.9 | 120079.005x | 120079.005x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.1 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,006,526.5 | 8.5893 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.3 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,259,736.6 | 8.6202 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.3 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.6 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 565,736.0 | 8.6324 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,063.2 | 4,060.9 | 4,188.6 | 50.3 | 1.000x | 1.000x | 75 | 54.2 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,074.3 | 4,061.9 | 4,144.1 | 29.9 | 1.003x | 1.003x | 75 | 54.3 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,820.8 | 7,793.4 | 8,921.5 | 439.2 | 1.925x | 1.925x | 75 | 104.3 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,752.6 | 18,606.6 | 19,026.7 | 153.3 | 4.615x | 4.615x | 75 | 250.0 | 27.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.6 | 0.0001 | 93.5 | 94.0 | 0.2 | 1.000x | 1.000x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0001 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,915.5 | 2,905.9 | 2,938.8 | 11.4 | 1.000x | 1.000x | 75 | 38.9 | 58.6 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,236,210.3 | 1.6249 | 2,235,095.1 | 2,247,883.7 | 4,756.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,237,315.8 | 1.6257 | 2,236,202.2 | 2,247,920.8 | 4,278.3 | 1.000x | 1.000x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,735,646.5 | 7.0740 | 9,613,981.1 | 9,806,489.4 | 77,809.8 | 4.354x | 4.354x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,778,404.6 | 46.3420 | 63,649,370.0 | 64,735,844.2 | 406,183.9 | 28.521x | 28.521x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,325.1 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,389.9 | 1.6188 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,449,226.5 | 7.1041 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 48,552,432.6 | 46.3032 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,729.6 | 1.6164 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,926.5 | 1.6172 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,830,389.5 | 6.9824 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,110,604.0 | 46.1983 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,494.5 | 1.7623 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,024.9 | 1.7704 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 457,626.6 | 6.9828 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,049,123.6 | 46.5259 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,640.6 | 5,610.8 | 5,650.8 | 14.9 | 1.000x | 1.000x | 75 | 75.2 | 58.6 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,685.4 | 7,679.8 | 7,790.8 | 41.8 | 1.363x | 1.363x | 75 | 102.5 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,688.0 | 7,684.2 | 7,703.1 | 7.4 | 1.363x | 1.363x | 75 | 102.5 | 100.0 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,944.9 | 23,902.4 | 24,353.1 | 166.8 | 4.245x | 4.245x | 75 | 319.3 | 27.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,728,745.7 | 7.0690 | 9,629,121.1 | 9,805,223.6 | 67,491.8 | 1.000x | 1.000x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,428,697.6 | 7.0846 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,835,720.2 | 7.0027 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 464,327.9 | 7.0851 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,638.2 | 5,613.3 | 5,653.6 | 15.7 | 1.000x | 1.000x | 75 | 75.2 | 58.6 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,600,379.3 | 6.9757 | 9,582,038.1 | 9,607,703.2 | 8,643.7 | 1.000x | 1.000x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,351,415.6 | 7.0109 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,807,749.4 | 6.8960 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 438,464.7 | 6.6904 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,465.4 | 17,375.1 | 18,436.9 | 400.6 | 1.000x | 1.000x | 75 | 232.9 | 58.6 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 93.9 | 95.0 | 0.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 285.2 | 0.0002 | 283.0 | 342.4 | 23.0 | 3.009x | 3.009x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.8 | 291.7 | 2.1 | 3.037x | 3.037x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,686,289.3 | 6.3115 | 8,680,636.3 | 8,713,813.6 | 12,994.9 | 91655.053x | 91655.053x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,620,212.8 | 6.3135 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,652,237.6 | 6.3028 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 106.9 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 414,644.0 | 6.3270 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,733.3 | 5,691.7 | 5,790.2 | 35.1 | 1.000x | 1.000x | 75 | 76.4 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,662.9 | 9,510.4 | 9,937.2 | 146.8 | 1.685x | 1.685x | 75 | 128.8 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,667.3 | 9,546.6 | 9,706.4 | 70.8 | 1.686x | 1.686x | 75 | 128.9 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,726.6 | 13,694.3 | 13,864.7 | 61.4 | 2.394x | 2.394x | 75 | 183.0 | 27.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 80,036,131.5 | 58.1550 | 79,688,787.0 | 80,380,958.5 | 232,715.3 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 216,510,331.5 | 157.3184 | 214,715,651.5 | 220,132,807.5 | 2,159,864.3 | 2.705x | 2.705x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 60,903,021.0 | 58.0816 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 165,042,159.0 | 157.3965 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 15,257,858.0 | 58.2041 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 41,252,118.5 | 157.3643 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,851,262.2 | 58.7656 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 10,231,189.5 | 156.1156 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 89,010.3 | 88,938.4 | 89,450.5 | 207.9 | 1.000x | 1.000x | 75 | 1,186.8 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 210,823.4 | 209,975.6 | 238,061.8 | 10,916.4 | 2.369x | 2.369x | 75 | 2,811.0 | 27.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,794.5 | 1.6195 | 2,227,479.4 | 2,233,759.4 | 2,266.2 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 184,142,654.5 | 133.7997 | 183,038,538.0 | 186,214,666.5 | 1,063,804.1 | 82.620x | 82.620x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,957.5 | 1.6183 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 140,484,082.0 | 133.9761 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,780.4 | 1.6204 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 34,932,582.0 | 133.2572 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,683.3 | 1.6279 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,730,210.5 | 133.2124 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,896.5 | 8,839.2 | 8,934.6 | 35.8 | 1.000x | 1.000x | 75 | 118.6 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 195,786.6 | 195,028.2 | 196,848.3 | 636.8 | 22.007x | 22.007x | 75 | 2,610.5 | 27.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,381.0 | 0.0010 | 1,373.7 | 1,398.2 | 8.7 | 1.000x | 1.000x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 388.3 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 555.8 | 0.0021 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 436.3 | 0.0067 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 18,596.6 | 18,446.5 | 18,750.3 | 99.5 | 1.000x | 1.000x | 75 | 248.0 | 58.6 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 342.5 | 0.0002 | 337.1 | 347.8 | 3.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 343.5 | 0.0002 | 340.7 | 362.3 | 7.7 | 1.003x | 1.003x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,826.3 | 1.6195 | 2,227,226.6 | 2,232,639.0 | 1,937.3 | 6507.930x | 6507.930x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 22,211,467.6 | 16.1391 | 21,620,955.8 | 22,626,074.1 | 325,440.7 | 64855.063x | 64855.063x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 113.1 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 114.1 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,697.9 | 1.6181 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,863,261.7 | 16.0821 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 103.5 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,593.3 | 1.6197 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,261,958.8 | 16.2581 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 125.6 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 126.1 | 0.0019 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,555.7 | 1.6259 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,073,617.1 | 16.3821 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,069.0 | 5,055.9 | 5,084.1 | 11.9 | 1.000x | 1.000x | 75 | 67.6 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 43,685.4 | 43,549.2 | 44,103.8 | 221.5 | 8.618x | 8.618x | 75 | 582.5 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 44,529.2 | 44,338.4 | 44,617.8 | 99.0 | 8.785x | 8.785x | 75 | 593.7 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 205,268.9 | 204,661.5 | 210,778.8 | 2,401.2 | 40.495x | 40.495x | 75 | 2,736.9 | 27.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 310.1 | 0.0002 | 309.6 | 355.0 | 17.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 311.9 | 0.0002 | 309.6 | 313.7 | 1.4 | 1.006x | 1.006x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,638.1 | 0.0128 | 17,557.2 | 17,717.4 | 53.7 | 56.870x | 56.870x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,217,479.4 | 7.4241 | 10,210,376.3 | 10,223,737.2 | 4,636.8 | 32944.023x | 32944.023x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 99.2 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,892.3 | 0.0018 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,783,757.7 | 7.4232 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 87.9 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 297.6 | 0.0011 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,945,327.8 | 7.4208 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 122.7 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 124.4 | 0.0019 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 15,439.1 | 0.2356 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 488,318.6 | 7.4512 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 249,978.4 | 0.1816 | 249,850.7 | 250,581.3 | 256.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 250,174.3 | 0.1818 | 249,698.6 | 250,649.2 | 300.8 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,180,777.2 | 0.8580 | 1,180,653.9 | 1,183,211.5 | 986.9 | 4.724x | 4.724x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,645,312.8 | 18.6341 | 25,626,430.0 | 25,665,305.6 | 14,816.7 | 102.590x | 102.590x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 196,476.5 | 0.1874 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 196,564.2 | 0.1875 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 897,757.5 | 0.8562 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,528,609.3 | 18.6239 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 42,468.6 | 0.1620 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 42,522.2 | 0.1622 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 226,234.7 | 0.8630 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,890,331.9 | 18.6551 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 11,077.3 | 0.1690 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 11,069.3 | 0.1689 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 56,901.5 | 0.8682 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,225,718.9 | 18.7030 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,197.6 | 3,179.9 | 3,198.9 | 7.9 | 1.000x | 1.000x | 75 | 42.6 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,650.8 | 7,635.1 | 7,782.0 | 55.4 | 2.393x | 2.393x | 75 | 102.0 | 100.0 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,300,527.7 | 9.6643 | 13,268,289.0 | 13,388,146.2 | 42,996.0 | 1.000x | 1.000x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 10,194,825.3 | 9.7225 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,505,563.0 | 9.5580 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 604,153.4 | 9.2187 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 20,462.7 | 20,445.9 | 20,744.0 | 111.6 | 1.000x | 1.000x | 75 | 272.8 | 58.6 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,199.2 | 0.0169 | 23,191.3 | 23,318.0 | 47.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,801.6 | 0.0173 | 23,778.5 | 23,892.2 | 39.9 | 1.026x | 1.026x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,936.7 | 0.0174 | 23,910.8 | 24,048.7 | 48.8 | 1.032x | 1.032x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,556.4 | 1.6193 | 2,227,650.2 | 6,262,574.3 | 1,613,659.5 | 96.062x | 96.062x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,650.6 | 0.0168 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,839.7 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,840.8 | 0.0170 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,229.0 | 1.6186 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,408.0 | 0.0168 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,508.8 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,524.3 | 0.0173 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,555.6 | 1.6196 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,136.3 | 0.0173 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,458.3 | 0.0223 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,571.4 | 0.0240 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,356.4 | 1.6229 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,091.6 | 2,091.2 | 2,095.2 | 1.5 | 1.000x | 1.000x | 75 | 27.9 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.0 | 4,389.9 | 4,412.5 | 9.0 | 2.102x | 2.102x | 75 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,501.3 | 7,490.1 | 7,519.2 | 10.3 | 3.586x | 3.586x | 75 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,512.5 | 7,503.6 | 7,522.3 | 6.9 | 3.592x | 3.592x | 75 | 100.2 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,035,195.9 | 1.4788 | 2,034,726.2 | 2,041,089.2 | 2,382.7 | 1.000x | 1.000x | 3 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,795.8 | 1.6267 | 2,230,522.7 | 2,245,104.7 | 5,639.3 | 1.100x | 1.100x | 3 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,737.3 | 1.6303 | 2,242,372.1 | 2,562,583.7 | 127,765.6 | 1.102x | 1.102x | 3 | 100% |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,550,179.3 | 1.4784 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,361.2 | 1.6206 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,703,107.9 | 1.6242 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,601.1 | 1.4786 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,278.2 | 1.6147 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,570.0 | 1.6196 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,429.9 | 1.4867 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,049.9 | 1.7708 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,000.8 | 1.7700 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,195.5 | 5,189.3 | 5,210.9 | 7.9 | 1.000x | 1.000x | 75 | 69.3 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,680.5 | 9,660.9 | 9,833.1 | 63.6 | 1.863x | 1.863x | 75 | 129.1 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,730.8 | 9,702.7 | 9,856.5 | 65.5 | 1.873x | 1.873x | 75 | 129.7 | 100.2 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.7 | 0.0002 | 281.7 | 287.4 | 2.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.3 | 0.0002 | 286.4 | 291.3 | 2.1 | 1.009x | 1.009x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 361.0 | 380.9 | 7.2 | 1.290x | 1.290x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,439,869.0 | 11.2187 | 15,401,899.9 | 15,724,924.6 | 120,366.5 | 54235.058x | 54235.058x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.1 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 302.7 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,753,517.2 | 11.2090 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 87.8 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.8 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,966,689.3 | 11.3170 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0005 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 745,934.3 | 11.3821 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,410.3 | 3,397.7 | 3,444.8 | 16.5 | 1.000x | 1.000x | 75 | 45.5 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,832.1 | 6,812.5 | 6,912.4 | 43.4 | 2.003x | 2.003x | 75 | 91.1 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,848.5 | 6,837.0 | 6,896.7 | 21.9 | 2.008x | 2.008x | 75 | 91.3 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,547.2 | 30,197.3 | 30,913.0 | 267.8 | 8.957x | 8.957x | 75 | 407.3 | 27.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,442,039.1 | 1.7744 | 2,429,228.9 | 2,487,973.9 | 21,518.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,487,038.7 | 1.8071 | 2,475,028.9 | 2,506,509.1 | 10,714.5 | 1.018x | 1.018x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,965,092.1 | 2.8811 | 3,957,525.3 | 3,989,063.6 | 11,202.9 | 1.624x | 1.624x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 29,542,544.1 | 21.4659 | 29,498,658.1 | 29,614,725.7 | 41,323.1 | 12.097x | 12.097x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,866,880.9 | 1.7804 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,899,496.7 | 1.8115 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,023,162.4 | 2.8831 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,494,733.3 | 21.4526 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 456,833.3 | 1.7427 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 465,675.9 | 1.7764 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 755,525.0 | 2.8821 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,635,318.1 | 21.4970 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 119,979.0 | 1.8307 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 121,067.9 | 1.8473 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 185,727.1 | 2.8340 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,413,374.8 | 21.5664 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,042.2 | 4,036.1 | 4,063.9 | 9.9 | 1.000x | 1.000x | 75 | 53.9 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,990.8 | 7,903.9 | 8,199.3 | 112.7 | 1.977x | 1.977x | 75 | 106.5 | 100.0 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.3 | 104.2 | 2.7 | 1.000x | 1.000x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.7 | 0.0005 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,029.4 | 4,984.7 | 5,092.2 | 38.0 | 1.000x | 1.000x | 75 | 67.1 | 58.6 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.4 | 0.0001 | 97.1 | 104.2 | 2.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.8 | 0.0002 | 285.2 | 344.2 | 23.2 | 2.943x | 2.943x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.9 | 291.5 | 2.1 | 2.953x | 2.953x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,159,734.8 | 13.9216 | 19,126,668.1 | 20,247,433.9 | 520,105.0 | 196620.778x | 196620.778x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,567,739.7 | 13.8929 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.3 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,676,688.4 | 14.0255 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 110.1 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.1 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 920,840.3 | 14.0509 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,983.4 | 4,969.5 | 5,066.7 | 36.0 | 1.000x | 1.000x | 75 | 66.4 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,895.6 | 7,872.7 | 8,088.5 | 94.3 | 1.584x | 1.584x | 75 | 105.3 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,028.0 | 7,948.6 | 8,153.9 | 73.3 | 1.611x | 1.611x | 75 | 107.0 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 41,789.1 | 40,846.3 | 41,972.8 | 444.0 | 8.386x | 8.386x | 75 | 557.2 | 27.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,764.4 | 0.0173 | 23,749.0 | 23,788.5 | 13.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,903.0 | 0.0174 | 23,880.3 | 23,910.3 | 11.0 | 1.006x | 1.006x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,965.5 | 1.6196 | 2,228,367.8 | 2,229,892.6 | 527.0 | 93.794x | 93.794x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,626,598.2 | 15.7141 | 20,391,829.5 | 23,439,821.3 | 1,175,032.1 | 910.043x | 910.043x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,797.8 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,822.6 | 0.0170 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,595.4 | 1.6190 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,471,239.3 | 15.7082 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,515.3 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,534.1 | 0.0173 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,823.1 | 1.6206 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,121,533.8 | 15.7224 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,452.2 | 0.0222 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,539.8 | 0.0235 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,805.5 | 1.6297 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,144,597.4 | 17.4652 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,421.8 | 4,415.6 | 4,517.8 | 39.0 | 1.000x | 1.000x | 75 | 59.0 | 58.6 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,528.6 | 7,518.6 | 7,541.8 | 7.6 | 1.703x | 1.703x | 75 | 100.4 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,542.8 | 7,518.7 | 7,553.1 | 12.2 | 1.706x | 1.706x | 75 | 100.6 | 100.0 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,679.7 | 1.0890 | 1,498,478.1 | 1,499,819.6 | 503.0 | 1.000x | 1.000x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,707.7 | 1.0888 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,203.7 | 1.0880 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,686.3 | 1.0938 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,461.8 | 4,452.7 | 4,474.4 | 7.4 | 1.000x | 1.000x | 75 | 59.5 | 58.6 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 95.3 | 0.0001 | 93.7 | 101.3 | 3.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.1 | 0.0002 | 284.4 | 298.2 | 5.3 | 2.991x | 2.991x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 285.9 | 0.0002 | 283.9 | 287.2 | 1.2 | 2.999x | 2.999x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,689,123.8 | 6.3136 | 8,682,341.8 | 8,716,311.4 | 14,626.1 | 91156.047x | 91156.047x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.9 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,619,895.1 | 6.3132 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.8 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,991.8 | 6.3095 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.8 | 0.0016 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,017.9 | 6.3327 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,603.5 | 9,577.6 | 9,792.7 | 79.4 | 1.000x | 1.000x | spread | 75 | 128.0 | 100.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,635.4 | 9,605.8 | 9,701.8 | 37.3 | 1.003x | 1.003x | spread | 75 | 128.5 | 100.0 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,302.4 | 13,248.6 | 13,345.6 | 34.6 | 1.385x | 1.385x | spread | 75 | 177.4 | 27.9 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,590,485.6 | 12,556,989.4 | 12,952,288.1 | 149,711.2 | 1311.029x | 1311.029x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 167,873.1 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.7 | 0.0001 | 93.7 | 95.4 | 0.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.2 | 0.0002 | 283.6 | 295.7 | 4.6 | 2.999x | 2.999x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 284.0 | 289.7 | 1.8 | 3.023x | 3.023x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,686,920.8 | 6.3120 | 8,684,292.5 | 8,719,581.7 | 13,275.6 | 91685.062x | 91685.062x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,616,979.9 | 6.3104 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.1 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,002.2 | 6.3057 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.4 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.4 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 416,018.9 | 6.3479 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,101.6 | 9,991.2 | 10,205.8 | 72.8 | 1.000x | 1.000x | spread | 75 | 134.7 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,105.3 | 10,021.8 | 10,821.2 | 302.4 | 1.000x | 1.000x | spread | 75 | 134.7 | 100.2 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,104.5 | 14,935.7 | 15,156.8 | 89.6 | 1.495x | 1.495x | spread | 75 | 201.4 | 27.9 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 16,693,186.2 | 16,645,155.7 | 17,278,804.8 | 238,231.0 | 1652.522x | 1652.522x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 222,575.8 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 14,477,787.7 | 10.5197 | 14,410,840.5 | 16,677,678.8 | 885,794.3 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,737,655.1 | 20.8810 | 28,699,391.8 | 28,880,049.0 | 67,087.2 | 1.985x | 1.985x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 11,103,596.2 | 10.5892 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,920,060.7 | 20.9046 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,720,979.9 | 10.3797 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,450,709.5 | 20.7928 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 658,196.4 | 10.0433 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,357,390.8 | 20.7121 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,750.7 | 22,734.3 | 22,863.2 | 55.8 | 1.000x | 1.000x | 75 | 303.3 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,351.3 | 29,990.7 | 30,569.7 | 187.1 | 1.334x | 1.334x | 75 | 404.7 | 27.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,048.4 | 0.0029 | 4,037.1 | 4,824.4 | 310.2 | 1.000x | 1.000x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 573.5 | 0.0005 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,841.3 | 0.0070 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,633.7 | 0.0249 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 36,028.0 | 36,023.7 | 38,607.8 | 1,014.2 | 1.000x | 1.000x | 75 | 480.4 | 58.6 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,837,824.3 | 2.7886 | 3,817,923.8 | 3,870,074.1 | 18,863.8 | 1.000x | 1.000x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,936,976.8 | 2.8009 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 718,631.8 | 2.7414 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 180,419.7 | 2.7530 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,095.2 | 7,081.4 | 7,134.8 | 18.7 | 1.000x | 1.000x | 75 | 94.6 | 58.6 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 398,855.6 | 0.2898 | 398,612.9 | 401,866.5 | 1,218.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 400,418.3 | 0.2909 | 399,254.2 | 405,719.5 | 2,441.8 | 1.004x | 1.004x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,361,509.6 | 0.9893 | 1,360,131.0 | 1,366,519.3 | 2,209.7 | 3.414x | 3.414x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 26,472,797.1 | 19.2354 | 26,439,972.9 | 26,536,229.4 | 37,809.2 | 66.372x | 66.372x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 304,403.1 | 0.2903 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 305,168.2 | 0.2910 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,039,087.2 | 0.9910 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 20,178,300.7 | 19.2435 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 74,613.1 | 0.2846 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 74,791.7 | 0.2853 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 259,546.0 | 0.9901 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,039,899.1 | 19.2257 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 19,615.2 | 0.2993 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 19,827.3 | 0.3025 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 62,428.3 | 0.9526 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,260,728.3 | 19.2372 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,808.1 | 2,801.2 | 2,840.1 | 17.2 | 1.000x | 1.000x | 75 | 37.4 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,612.8 | 7,591.2 | 7,887.0 | 112.8 | 2.711x | 2.711x | 75 | 101.5 | 100.0 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,230,556.5 | 1.6207 | 2,228,823.6 | 2,233,826.7 | 1,803.9 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 34,518,744.6 | 25.0816 | 34,494,834.5 | 34,865,714.1 | 140,472.3 | 15.475x | 15.475x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,961.9 | 1.6193 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,291,626.9 | 25.0736 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 425,020.0 | 1.6213 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,569,446.6 | 25.0605 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,562.7 | 1.6260 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,645,550.9 | 25.1091 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,552.2 | 6,546.6 | 6,588.6 | 15.0 | 1.000x | 1.000x | 75 | 87.4 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,397.7 | 47,362.2 | 47,585.5 | 81.5 | 7.234x | 7.234x | 75 | 632.0 | 27.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,027.8 | 1.6196 | 2,228,591.7 | 2,240,708.9 | 4,690.7 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 27,780,021.7 | 20.1852 | 27,713,332.4 | 27,822,273.1 | 38,966.6 | 12.463x | 12.463x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,627.3 | 1.6190 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,122,834.3 | 20.1443 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,700.0 | 1.6201 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,273,562.8 | 20.1170 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,597.8 | 1.6266 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,337,638.9 | 20.4107 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,951.1 | 5,937.2 | 5,964.9 | 11.6 | 1.000x | 1.000x | 75 | 79.3 | 58.6 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.6 | 0.0002 | 282.4 | 286.9 | 1.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 285.7 | 289.0 | 1.1 | 1.007x | 1.007x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 745.0 | 0.0005 | 729.6 | 752.1 | 8.6 | 2.618x | 2.618x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,849,925.9 | 8.6103 | 11,835,794.0 | 21,775,545.9 | 3,958,306.3 | 41637.031x | 41637.031x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 89.6 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 247.1 | 0.0002 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,038,698.3 | 8.6200 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.6 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 247.3 | 0.0009 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,251,950.4 | 8.5905 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 249.8 | 0.0038 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 571,801.6 | 8.7250 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,419.7 | 9,402.9 | 9,560.5 | 59.7 | 1.000x | 1.000x | spread | 75 | 125.6 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,468.1 | 9,446.9 | 9,519.3 | 27.8 | 1.005x | 1.005x | spread | 75 | 126.2 | 100.2 | 100% |
| 3 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,511.4 | 19,426.2 | 19,566.0 | 50.9 | 2.071x | 2.071x | spread | 75 | 260.2 | 27.9 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,536,685.1 | 12,517,587.1 | 12,554,973.7 | 12,607.1 | 1330.900x | 1330.900x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 167,155.8 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,036,374.5 | 1.4796 | 2,035,108.2 | 2,045,770.6 | 3,993.6 | 1.000x | 1.000x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,551,224.2 | 1.4794 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,805.3 | 1.4794 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,542.6 | 1.4884 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,932.3 | 4,926.4 | 5,678.1 | 298.7 | 1.000x | 1.000x | 75 | 65.8 | 58.6 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 92.9 | 0.0001 | 92.5 | 106.5 | 5.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 296.4 | 0.0002 | 295.6 | 297.6 | 0.7 | 3.190x | 3.190x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 298.0 | 0.0002 | 295.2 | 310.9 | 5.5 | 3.207x | 3.207x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,852,271.0 | 8.6120 | 11,798,052.3 | 12,082,103.6 | 126,587.3 | 127549.544x | 127549.544x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,040,378.2 | 8.6216 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.0 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.1 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,249,509.9 | 8.5812 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 119.6 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120.5 | 0.0018 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 568,955.0 | 8.6816 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,795.9 | 2,789.1 | 2,832.6 | 18.3 | 1.000x | 1.000x | 75 | 37.3 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,210.6 | 4,204.9 | 4,219.4 | 4.8 | 1.506x | 1.506x | 75 | 56.1 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,219.0 | 4,206.9 | 4,232.1 | 8.9 | 1.509x | 1.509x | 75 | 56.3 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,317.6 | 35,299.1 | 35,608.2 | 123.4 | 12.632x | 12.632x | 75 | 470.9 | 27.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 700,481.3 | 0.5090 | 699,694.8 | 701,083.4 | 462.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 1,646,513.1 | 1.1964 | 1,636,496.1 | 1,667,335.6 | 10,902.9 | 2.351x | 2.351x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 1,678,588.5 | 1.2197 | 1,676,557.8 | 1,734,706.8 | 23,283.9 | 2.396x | 2.396x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,979,405.4 | 2.8915 | 3,961,213.6 | 4,016,038.8 | 18,735.5 | 5.681x | 5.681x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 536,650.7 | 0.5118 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,253,010.1 | 1.1950 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,278,705.9 | 1.2195 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,036,809.6 | 2.8961 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 129,760.9 | 0.4950 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 303,050.1 | 1.1560 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 309,717.8 | 1.1815 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 749,430.8 | 2.8589 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 34,158.4 | 0.5212 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 89,160.7 | 1.3605 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 91,062.7 | 1.3895 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 192,126.6 | 2.9316 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,188.6 | 2,187.5 | 2,231.6 | 16.9 | 1.000x | 1.000x | 75 | 29.2 | 27.9 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,651.9 | 4,644.8 | 4,670.4 | 10.2 | 2.126x | 2.126x | 75 | 62.0 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,717.5 | 7,679.0 | 7,852.1 | 63.2 | 3.526x | 3.526x | 75 | 102.9 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,762.8 | 7,686.0 | 7,786.5 | 34.1 | 3.547x | 3.547x | 75 | 103.5 | 100.0 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,238,720.3 | 1.6267 | 2,236,559.2 | 2,240,047.1 | 1,298.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,243,644.8 | 1.6303 | 2,239,152.6 | 2,246,551.6 | 2,777.3 | 1.002x | 1.002x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,560,019.1 | 4.7666 | 6,529,638.9 | 6,597,222.3 | 23,928.2 | 2.930x | 2.930x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 65,785,610.4 | 47.8004 | 65,379,510.0 | 66,622,055.2 | 427,936.0 | 29.385x | 29.385x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,698,688.4 | 1.6200 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,138.5 | 1.6223 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 4,983,004.7 | 4.7522 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 49,992,617.0 | 47.6767 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,008.1 | 1.6175 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,564.3 | 1.6196 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,257,637.8 | 4.7975 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,527,788.4 | 47.7897 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 115,557.4 | 1.7633 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,795.3 | 1.7669 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 319,376.6 | 4.8733 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,103,319.8 | 47.3529 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,591.6 | 9,574.0 | 9,786.1 | 79.1 | 1.000x | 1.000x | 75 | 127.9 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,675.3 | 9,629.7 | 9,830.8 | 72.9 | 1.009x | 1.009x | 75 | 129.0 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,350.6 | 13,280.3 | 13,525.0 | 91.5 | 1.392x | 1.392x | 75 | 178.0 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,627.0 | 63,295.5 | 64,097.1 | 321.6 | 6.634x | 6.634x | 75 | 848.4 | 27.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,494,350.5 | 17.0712 | 23,280,290.1 | 23,604,505.3 | 127,658.2 | 1.000x | 1.000x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 17,976,793.7 | 17.1440 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,417,126.2 | 16.8500 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,067,112.0 | 16.2828 |

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,694.2 | 11,660.0 | 11,771.9 | 39.3 | 1.000x | 1.000x | 75 | 155.9 | 58.6 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,248.6 | 0.0169 | 23,221.9 | 23,297.5 | 25.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,758.8 | 0.0173 | 23,741.2 | 23,773.9 | 10.7 | 1.022x | 1.022x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,779.2 | 0.0173 | 23,741.0 | 23,921.2 | 64.8 | 1.023x | 1.023x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,819.3 | 1.6202 | 2,228,441.8 | 2,234,492.3 | 2,111.8 | 95.912x | 95.912x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,668.5 | 0.0168 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,807.7 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,811.9 | 0.0170 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,260.2 | 1.6196 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,425.3 | 0.0169 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,498.6 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,517.5 | 0.0172 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,781.5 | 1.6204 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,142.1 | 0.0174 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,442.1 | 0.0220 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,447.6 | 0.0221 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,412.0 | 1.6237 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,092.1 | 2,090.5 | 2,098.4 | 2.8 | 1.000x | 1.000x | 75 | 27.9 | 27.9 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.9 | 4,392.6 | 4,978.2 | 232.0 | 2.102x | 2.102x | 75 | 58.6 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,514.9 | 7,501.4 | 7,526.1 | 8.4 | 3.592x | 3.592x | 75 | 100.2 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,537.7 | 7,511.6 | 7,601.8 | 34.2 | 3.603x | 3.603x | 75 | 100.5 | 100.2 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,854.5 | 1.6202 | 2,228,571.0 | 2,231,481.9 | 1,163.2 | 1.000x | 1.000x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,142.7 | 1.6195 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,827.6 | 1.6206 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,776.7 | 1.6293 |

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,047.9 | 5,034.5 | 5,145.9 | 43.2 | 1.000x | 1.000x | 75 | 67.3 | 58.6 | 100% |

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 909,418,994.0 | 660.7920 | 907,635,774.0 | 1,039,619,183.0 | 51,272,470.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 915,511,309.0 | 665.2188 | 899,467,753.0 | 951,066,994.0 | 20,860,808.5 | 1.007x | 1.007x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,137,713,544.0 | 1553.2819 | 2,120,757,817.0 | 2,480,947,384.0 | 139,483,497.6 | 2.351x | 2.351x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 692,210,197.0 | 660.1431 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 690,401,889.0 | 658.4185 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,629,609,806.0 | 1554.1170 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 172,709,917.0 | 658.8360 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 177,402,764.0 | 676.7378 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 406,240,412.0 | 1549.6842 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 45,741,747.0 | 697.9637 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 47,559,525.0 | 725.7008 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 102,213,140.0 | 1559.6487 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 181,558.9 | 180,952.8 | 184,663.4 | 1,326.8 | 1.000x | 1.000x | 75 | 2,420.8 | 100.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 182,594.8 | 181,265.1 | 183,247.3 | 661.0 | 1.006x | 1.006x | 75 | 2,434.6 | 100.0 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 765,447.8 | 763,500.9 | 769,117.1 | 1,916.0 | 4.216x | 4.216x | 75 | 10,206.0 | 58.6 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.2 | 0.0002 | 283.5 | 286.2 | 0.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.0 | 0.0002 | 283.6 | 287.3 | 1.5 | 1.006x | 1.006x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,006.4 | 0.0007 | 977.1 | 1,011.4 | 15.1 | 3.541x | 3.541x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,399,163.4 | 11.1892 | 15,380,043.9 | 15,520,233.5 | 50,750.5 | 54176.179x | 54176.179x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 306.0 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,717,792.7 | 11.1750 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 421.2 | 0.0016 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,947,490.3 | 11.2438 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 106.9 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 278.8 | 0.0043 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 741,816.5 | 11.3192 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,707.2 | 9,570.5 | 9,770.3 | 66.1 | 1.000x | 1.000x | 75 | 129.4 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,737.3 | 9,714.3 | 9,793.3 | 28.8 | 1.003x | 1.003x | 75 | 129.8 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,656.5 | 11,611.5 | 11,871.9 | 92.7 | 1.201x | 1.201x | 75 | 155.4 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 42,417.2 | 42,355.6 | 42,457.1 | 37.4 | 4.370x | 4.370x | 75 | 565.6 | 27.9 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 27,178,784.8 | 19.7483 | 27,101,937.3 | 27,960,581.0 | 351,977.7 | 1.000x | 1.000x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 20,814,145.0 | 19.8499 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 5,128,784.7 | 19.5648 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,235,855.1 | 18.8577 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,893.4 | 15,772.3 | 16,188.7 | 147.3 | 1.000x | 1.000x | 75 | 211.9 | 58.6 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 25,776,438.6 | 18.7294 | 25,756,114.0 | 26,331,673.2 | 219,154.1 | 1.000x | 1.000x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 19,738,679.8 | 18.8243 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,865,464.7 | 18.5603 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,176,568.6 | 17.9530 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,951.5 | 15,869.6 | 16,015.9 | 51.1 | 1.000x | 1.000x | 75 | 212.7 | 58.6 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,461,960.6 | 2.5155 | 3,446,127.4 | 3,504,453.5 | 20,710.8 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,646,841.7 | 2.5242 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 651,344.4 | 2.4847 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 163,774.5 | 2.4990 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,263.0 | 6,260.9 | 6,298.7 | 14.1 | 1.000x | 1.000x | 75 | 83.5 | 58.6 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,273,987.7 | 2.3789 | 3,251,490.0 | 3,319,012.3 | 27,398.1 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,503,123.8 | 2.3872 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 616,205.0 | 2.3506 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 154,658.9 | 2.3599 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 290,745.7 | 290,281.8 | 291,145.7 | 305.9 | 1.000x | 1.000x | **dominated**: `waf-sleep` is 98.1% of this set | 75 | 3,876.6 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 69,561,405.2 | 50.5439 | 69,299,673.5 | 69,819,311.8 | 176,101.9 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 52,934,450.8 | 50.4822 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 13,301,012.5 | 50.7393 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,325,942.0 | 50.7498 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,531.8 | 23,414.9 | 29,466.6 | 2,388.1 | 1.000x | 1.000x | 75 | 313.8 | 58.6 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,676.0 | 1.6186 | 2,226,582.6 | 2,229,305.0 | 889.6 | 1.000x | 1.000x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,061.3 | 1.6184 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 423,987.4 | 1.6174 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,228.4 | 1.6209 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,334.2 | 5,319.0 | 5,343.5 | 9.4 | 1.000x | 1.000x | 75 | 71.1 | 58.6 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,170,961.4 | 1.5774 | 2,169,820.1 | 2,179,610.4 | 3,548.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,524.0 | 1.6294 | 2,232,468.3 | 2,249,970.6 | 6,088.5 | 1.033x | 1.033x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,681.0 | 1.6303 | 2,238,273.5 | 2,245,637.6 | 2,513.3 | 1.033x | 1.033x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 171,683,257.0 | 124.7466 | 169,849,352.0 | 175,041,292.0 | 1,713,375.3 | 79.082x | 79.082x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,654,190.0 | 1.5776 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,766.1 | 1.6220 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,702,109.9 | 1.6233 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 129,693,290.0 | 123.6852 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 413,350.2 | 1.5768 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,913.0 | 1.6209 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,936.4 | 1.6210 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 33,407,033.5 | 127.4377 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 103,737.3 | 1.5829 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,840.0 | 1.7676 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,584.6 | 1.7789 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,337,458.5 | 127.2195 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,520.6 | 7,471.6 | 7,646.6 | 60.5 | 1.000x | 1.000x | 75 | 100.3 | 58.6 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,973.3 | 9,874.5 | 10,122.7 | 80.9 | 1.326x | 1.326x | 75 | 133.0 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,979.6 | 9,886.8 | 10,145.8 | 92.6 | 1.327x | 1.327x | 75 | 133.1 | 100.0 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 175,424.2 | 174,489.4 | 176,594.3 | 670.7 | 23.326x | 23.326x | 75 | 2,339.0 | 27.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 414,437.2 | 0.3011 | 414,185.1 | 414,945.7 | 275.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,686.3 | 1.6259 | 2,232,765.2 | 2,248,333.0 | 5,206.9 | 5.399x | 5.399x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,455.1 | 1.6279 | 2,238,769.5 | 2,242,236.5 | 1,165.9 | 5.406x | 5.406x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,061,868.5 | 18.2102 | 25,031,772.0 | 25,097,622.4 | 22,316.5 | 60.472x | 60.472x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 315,240.3 | 0.3006 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,698,287.0 | 1.6196 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,242.0 | 1.6205 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,100,497.7 | 18.2157 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 79,025.4 | 0.3015 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,856.3 | 1.6169 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,936.9 | 1.6172 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,772,654.0 | 18.2062 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 19,967.9 | 0.3047 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,663.1 | 1.7649 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,305.6 | 1.7747 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,195,404.2 | 18.2404 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,946.8 | 2,944.2 | 3,126.5 | 70.6 | 1.000x | 1.000x | 75 | 39.3 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,202.4 | 10,123.6 | 10,894.5 | 280.6 | 3.462x | 3.462x | 75 | 136.0 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,429.3 | 10,391.6 | 10,448.3 | 23.4 | 3.539x | 3.539x | 75 | 139.1 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 56,715.0 | 56,668.7 | 56,810.6 | 46.6 | 19.246x | 19.246x | 75 | 756.2 | 27.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 439,089.5 | 0.3190 | 438,860.0 | 445,543.4 | 2,601.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,271.4 | 0.3192 | 438,875.8 | 440,274.8 | 578.7 | 1.000x | 1.000x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,249,951.7 | 0.9082 | 1,249,354.5 | 1,253,520.1 | 1,534.1 | 2.847x | 2.847x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,318,812.9 | 25.6630 | 35,181,012.1 | 35,437,962.2 | 90,841.4 | 80.436x | 80.436x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,778.6 | 0.3155 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,838.8 | 0.3155 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 952,392.2 | 0.9083 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,877,191.6 | 25.6321 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,050.8 | 0.3168 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,950.5 | 0.3164 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 238,027.7 | 0.9080 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,750,774.0 | 25.7522 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,376.0 | 0.3872 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,396.5 | 0.3875 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 59,189.1 | 0.9032 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,690,847.2 | 25.8003 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,356.6 | 3,349.3 | 3,396.8 | 21.5 | 1.000x | 1.000x | 75 | 44.8 | 58.6 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,973.5 | 8,882.4 | 8,990.2 | 38.4 | 2.673x | 2.673x | 75 | 119.6 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,022.2 | 9,017.5 | 9,109.4 | 35.1 | 2.688x | 2.688x | 75 | 120.3 | 100.0 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 74,743.8 | 74,724.7 | 74,852.3 | 46.4 | 22.267x | 22.267x | 75 | 996.6 | 27.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,062.8 | 1.6291 | 2,235,212.0 | 2,251,360.1 | 5,962.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,243,308.2 | 1.6300 | 2,237,197.2 | 2,243,682.4 | 2,465.7 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,834,438.6 | 3.5127 | 4,831,155.3 | 4,839,506.2 | 2,855.6 | 2.156x | 2.156x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,819.0 | 1.6220 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,257.1 | 1.6215 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,671,783.4 | 3.5017 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,139.2 | 1.6180 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,747.9 | 1.6203 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 926,455.9 | 3.5341 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,104.5 | 1.7869 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 117,670.6 | 1.7955 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 235,656.2 | 3.5958 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,033.7 | 9,020.1 | 9,165.9 | 54.3 | 1.000x | 1.000x | 75 | 120.4 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,284.5 | 10,263.4 | 10,490.6 | 83.2 | 1.138x | 1.138x | 75 | 137.1 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,351.6 | 10,345.8 | 10,484.8 | 53.4 | 1.146x | 1.146x | 75 | 138.0 | 100.2 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 325,587.1 | 0.2366 | 325,329.5 | 329,401.9 | 1,540.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 326,198.2 | 0.2370 | 325,688.2 | 326,461.9 | 269.8 | 1.002x | 1.002x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,342,842.6 | 0.9757 | 1,341,850.0 | 1,343,793.8 | 709.0 | 4.124x | 4.124x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,598,173.3 | 20.7797 | 28,571,082.2 | 28,669,532.7 | 33,751.2 | 87.836x | 87.836x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 256,351.1 | 0.2445 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 256,644.6 | 0.2448 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,021,957.1 | 0.9746 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,772,259.9 | 20.7636 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 54,864.4 | 0.2093 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 54,923.1 | 0.2095 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 256,264.2 | 0.9776 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,458,204.5 | 20.8214 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 14,397.9 | 0.2197 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 14,769.9 | 0.2254 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 64,228.4 | 0.9800 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,371,465.0 | 20.9269 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,986.1 | 2,980.2 | 3,139.4 | 60.7 | 1.000x | 1.000x | 75 | 39.8 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,468.4 | 7,467.8 | 7,469.7 | 0.7 | 2.501x | 2.501x | 75 | 99.6 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,488.0 | 7,485.2 | 8,133.2 | 256.2 | 2.508x | 2.508x | 75 | 99.8 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,912.2 | 30,851.3 | 31,201.5 | 129.0 | 10.352x | 10.352x | 75 | 412.2 | 27.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 151.3 | 0.0001 | 151.1 | 151.4 | 0.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 316.3 | 0.0002 | 314.8 | 317.6 | 0.9 | 2.091x | 2.091x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 316.7 | 0.0002 | 314.8 | 317.9 | 1.1 | 2.093x | 2.093x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,567,140.7 | 13.4911 | 18,541,650.5 | 18,620,515.0 | 27,681.4 | 122732.600x | 122732.600x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 50.3 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 98.9 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,152,979.8 | 13.4973 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 98.6 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 98.5 | 0.0004 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,533,333.7 | 13.4786 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 118.5 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 118.6 | 0.0018 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 887,617.8 | 13.5440 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,474.2 | 3,455.8 | 3,477.2 | 7.8 | 1.000x | 1.000x | 75 | 46.3 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,307.4 | 7,292.6 | 7,337.8 | 17.1 | 2.103x | 2.103x | 75 | 97.4 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,330.5 | 7,308.9 | 7,360.6 | 17.5 | 2.110x | 2.110x | 75 | 97.7 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 12,695.1 | 12,681.5 | 12,722.7 | 14.5 | 3.654x | 3.654x | 75 | 169.3 | 27.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,010,275.2 | 34.1581 | 46,709,688.3 | 48,495,435.3 | 659,963.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 62,962,198.6 | 45.7489 | 62,490,547.6 | 64,109,606.2 | 587,533.6 | 1.339x | 1.339x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 65,721,547.2 | 47.7539 | 65,413,297.6 | 66,673,090.8 | 460,939.9 | 1.398x | 1.398x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 99,913,182.7 | 72.5978 | 99,339,699.3 | 101,624,659.3 | 801,474.7 | 2.125x | 2.125x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 35,802,428.7 | 34.1439 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 48,064,878.0 | 45.8382 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 50,273,919.2 | 47.9449 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 76,132,659.0 | 72.6058 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 8,933,194.8 | 34.0774 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 11,936,399.0 | 45.5337 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 12,335,622.0 | 47.0567 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 18,924,162.3 | 72.1900 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,213,087.8 | 33.7690 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 2,984,221.8 | 45.5356 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 3,112,006.0 | 47.4854 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 4,643,146.7 | 70.8488 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,362.3 | 17,081.7 | 17,567.5 | 185.8 | 1.000x | 1.000x | 75 | 231.5 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 19,842.2 | 19,706.9 | 20,006.7 | 107.8 | 1.143x | 1.143x | 75 | 264.6 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 19,913.7 | 19,739.3 | 20,174.9 | 153.4 | 1.147x | 1.147x | 75 | 265.5 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 31,343.3 | 31,278.0 | 31,451.9 | 63.8 | 1.805x | 1.805x | 75 | 417.9 | 27.9 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 374.4 | 0.0003 | 369.5 | 382.0 | 4.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 384.4 | 0.0003 | 381.4 | 390.1 | 3.3 | 1.027x | 1.027x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,440.6 | 1.6185 | 2,226,539.7 | 2,234,098.7 | 2,758.3 | 5948.722x | 5948.722x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,848,026.8 | 15.8750 | 21,070,678.2 | 22,350,250.6 | 561,505.5 | 58348.513x | 58348.513x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 114.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 112.8 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,947.3 | 1.6183 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,513,572.8 | 15.7486 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 101.2 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,200.4 | 1.6182 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,258,051.2 | 16.2432 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 155.5 | 0.0024 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 170.1 | 0.0026 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,439.2 | 1.6241 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,069,530.3 | 16.3197 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,227.7 | 5,218.6 | 5,288.9 | 25.3 | 1.000x | 1.000x | 75 | 69.7 | 58.6 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,127.5 | 8,103.7 | 8,180.7 | 25.8 | 1.555x | 1.555x | 75 | 108.4 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,136.0 | 8,100.5 | 9,032.2 | 364.7 | 1.556x | 1.556x | 75 | 108.5 | 100.0 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 120,423.0 | 120,382.5 | 120,919.3 | 216.9 | 23.036x | 23.036x | 75 | 1,605.6 | 27.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.8 | 0.0002 | 284.4 | 285.2 | 0.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.8 | 0.0002 | 285.4 | 288.2 | 1.1 | 1.003x | 1.003x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 367.0 | 389.5 | 9.6 | 1.290x | 1.290x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,399,526.6 | 11.1894 | 15,387,074.9 | 15,427,381.2 | 16,185.8 | 54062.865x | 54062.865x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 299.2 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,726,477.1 | 11.1832 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.3 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 34.1 | 0.0001 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,937,226.4 | 11.2046 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 34.6 | 0.0005 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 740,877.6 | 11.3049 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,661.5 | 3,588.6 | 3,824.5 | 85.0 | 1.000x | 1.000x | 75 | 48.8 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,317.1 | 9,277.2 | 9,366.3 | 29.0 | 2.545x | 2.545x | 75 | 124.2 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,420.2 | 9,330.1 | 10,128.7 | 293.5 | 2.573x | 2.573x | 75 | 125.6 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 38,827.5 | 38,585.4 | 39,030.0 | 152.6 | 10.604x | 10.604x | 75 | 517.7 | 27.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 94.3 | 95.0 | 0.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.8 | 0.0002 | 283.4 | 304.4 | 8.0 | 3.003x | 3.003x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.9 | 0.0002 | 283.1 | 291.6 | 3.2 | 3.004x | 3.004x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,693,894.0 | 6.3171 | 8,660,192.5 | 8,703,324.0 | 15,746.7 | 91670.935x | 91670.935x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,621,152.4 | 6.3144 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,652,694.0 | 6.3045 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 414,860.8 | 6.3303 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,038.4 | 2,033.8 | 2,042.1 | 3.0 | 1.000x | 1.000x | 75 | 27.2 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,046.0 | 2,040.1 | 2,094.7 | 20.2 | 1.004x | 1.004x | 75 | 27.3 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,915.5 | 4,906.6 | 4,989.0 | 31.9 | 2.411x | 2.411x | 75 | 65.5 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,921.2 | 13,916.7 | 13,933.6 | 7.2 | 6.830x | 6.830x | 75 | 185.6 | 27.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,235,844.8 | 1.6246 | 2,231,352.6 | 2,251,497.0 | 7,159.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,842.2 | 1.6268 | 2,233,817.2 | 2,242,387.3 | 2,999.4 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,420,629.7 | 1.7589 | 2,415,306.8 | 2,421,702.7 | 2,248.5 | 1.083x | 1.083x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 72,489,213.0 | 52.6713 | 69,753,004.8 | 72,506,743.0 | 1,072,793.8 | 32.421x | 32.421x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,309.3 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,652.9 | 1.6209 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,844,193.1 | 1.7588 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 55,175,180.5 | 52.6192 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,178.7 | 1.6143 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,680.1 | 1.6162 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 459,146.5 | 1.7515 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 13,731,436.5 | 52.3813 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,008.7 | 1.7702 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,210.7 | 1.7732 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 116,148.1 | 1.7723 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,434,615.0 | 52.4081 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,236.0 | 4,226.9 | 4,290.4 | 22.8 | 1.000x | 1.000x | 75 | 56.5 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,815.1 | 9,755.0 | 10,362.4 | 227.8 | 2.317x | 2.317x | 75 | 130.9 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,878.0 | 9,848.5 | 9,913.1 | 25.6 | 2.332x | 2.332x | 75 | 131.7 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 121,919.5 | 119,770.2 | 122,253.0 | 1,004.8 | 28.782x | 28.782x | 75 | 1,625.6 | 27.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,325.2 | 1.6293 | 2,238,906.8 | 2,279,953.9 | 15,483.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,907.8 | 1.6297 | 2,233,106.6 | 2,248,494.0 | 5,092.6 | 1.000x | 1.000x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 65,241,237.2 | 47.4049 | 65,024,447.8 | 65,398,824.0 | 130,718.7 | 29.095x | 29.095x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 285,325,096.0 | 207.3198 | 280,193,756.0 | 292,484,487.0 | 4,023,104.3 | 127.245x | 127.245x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,966.1 | 1.6231 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,838.2 | 1.6220 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 49,703,089.0 | 47.4006 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 218,465,690.0 | 208.3451 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,128.7 | 1.6179 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,466.9 | 1.6192 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 12,403,551.6 | 47.3158 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 52,845,094.0 | 201.5880 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,723.8 | 1.7811 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,046.2 | 1.7860 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,115,774.6 | 47.5429 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 13,182,896.0 | 201.1550 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,646.5 | 9,614.1 | 9,955.4 | 126.6 | 1.000x | 1.000x | 75 | 128.6 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,704.5 | 9,670.3 | 9,716.5 | 19.7 | 1.006x | 1.006x | 75 | 129.4 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 44,816.7 | 44,752.1 | 45,046.3 | 113.0 | 4.646x | 4.646x | 75 | 597.6 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 319,759.1 | 318,703.8 | 327,037.0 | 3,126.0 | 33.148x | 33.148x | 75 | 4,263.5 | 27.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,147.2 | 1.6277 | 2,235,744.2 | 2,248,140.7 | 4,055.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,240,941.6 | 1.6283 | 2,231,147.1 | 2,244,189.0 | 5,263.1 | 1.000x | 1.000x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,911,042.9 | 3.5684 | 4,900,030.2 | 5,814,985.9 | 362,499.5 | 2.192x | 2.192x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 60,079,000.4 | 43.6539 | 60,068,762.4 | 60,187,309.0 | 44,431.7 | 26.819x | 26.819x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,881.0 | 1.6211 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,204.9 | 1.6214 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,729,683.1 | 3.5569 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 45,759,910.0 | 43.6401 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 425,758.3 | 1.6241 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,759.7 | 1.6203 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 934,212.4 | 3.5637 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 11,430,437.8 | 43.6037 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,562.9 | 1.7786 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,976.9 | 1.7697 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 246,550.1 | 3.7621 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,878,786.6 | 43.9268 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,593.2 | 9,575.7 | 9,772.1 | 73.2 | 1.000x | 1.000x | 75 | 127.9 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,839.2 | 9,633.0 | 9,944.0 | 116.6 | 1.026x | 1.026x | 75 | 131.2 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,477.7 | 12,460.1 | 12,509.0 | 18.6 | 1.301x | 1.301x | 75 | 166.4 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 71,099.8 | 71,064.5 | 71,109.6 | 18.5 | 7.411x | 7.411x | 75 | 948.0 | 27.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 438,865.4 | 0.3189 | 438,743.8 | 440,523.7 | 661.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,102.4 | 0.3191 | 438,451.0 | 439,565.5 | 453.0 | 1.001x | 1.001x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,425,857.9 | 2.4893 | 3,423,977.2 | 3,427,078.8 | 1,119.1 | 7.806x | 7.806x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,936,396.2 | 22.4787 | 30,884,965.9 | 30,998,074.3 | 42,965.4 | 70.492x | 70.492x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,714.0 | 0.3154 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,683.7 | 0.3154 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,603,920.7 | 2.4833 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 23,551,311.4 | 22.4603 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,169.4 | 0.3173 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,967.9 | 0.3165 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 655,621.8 | 2.5010 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,897,141.8 | 22.4958 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,110.2 | 0.3832 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 24,987.5 | 0.3813 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 166,324.6 | 2.5379 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,481,358.6 | 22.6037 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,258.9 | 8,245.2 | 8,906.9 | 260.5 | 1.000x | 1.000x | 75 | 110.1 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,310.8 | 8,282.6 | 8,584.9 | 130.5 | 1.006x | 1.006x | 75 | 110.8 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,755.4 | 8,743.4 | 8,820.1 | 28.2 | 1.060x | 1.060x | 75 | 116.7 | 58.6 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 39,239.9 | 39,205.5 | 39,338.8 | 48.7 | 4.751x | 4.751x | 75 | 523.2 | 27.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,245,698.0 | 1.6317 | 2,237,409.5 | 2,249,579.8 | 4,827.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,246,279.2 | 1.6322 | 2,238,966.4 | 2,249,444.7 | 3,694.4 | 1.000x | 1.000x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 138,553,761.5 | 100.6744 | 138,270,549.0 | 153,899,022.5 | 6,138,875.5 | 61.697x | 61.697x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 1,169,517,671.0 | 849.7821 | 1,160,081,936.0 | 1,177,845,858.0 | 7,268,394.2 | 520.781x | 520.781x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,934.9 | 1.6221 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,701,537.2 | 1.6227 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 105,556,164.5 | 100.6662 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 887,301,449.0 | 846.1966 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,753.7 | 1.6203 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,991.9 | 1.6174 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 26,400,943.5 | 100.7116 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 223,480,342.0 | 852.5098 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120,039.4 | 1.8317 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 120,903.2 | 1.8448 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 6,596,653.5 | 100.6569 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 55,721,623.0 | 850.2445 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,560.4 | 9,526.6 | 9,772.6 | 90.6 | 1.000x | 1.000x | 75 | 127.5 | 100.0 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,625.2 | 9,613.1 | 9,639.8 | 9.1 | 1.007x | 1.007x | 75 | 128.3 | 100.2 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 142,711.4 | 142,421.2 | 142,970.4 | 186.6 | 14.927x | 14.927x | 75 | 1,902.8 | 58.6 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,015.7 | 0.3190 | 438,764.7 | 439,629.1 | 303.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 440,033.2 | 0.3197 | 439,026.3 | 440,551.3 | 514.3 | 1.002x | 1.002x |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,130.6 | 1.0886 | 1,497,611.9 | 1,500,676.9 | 1,094.7 | 3.412x | 3.412x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,824.6 | 0.3155 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,973.4 | 0.3156 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,170.5 | 1.0883 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,924.3 | 0.3163 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,098.3 | 0.3170 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,299.8 | 1.0883 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,198.4 | 0.3845 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,263.2 | 0.3855 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,488.8 | 1.0908 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,885.2 | 3,875.5 | 3,914.5 | 13.9 | 1.000x | 1.000x | 75 | 51.8 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,261.6 | 8,228.9 | 8,317.2 | 30.5 | 2.126x | 2.126x | 75 | 110.2 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,296.2 | 8,234.9 | 8,726.7 | 197.1 | 2.135x | 2.135x | 75 | 110.6 | 100.2 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 93.4 | 111.8 | 7.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 294.5 | 0.0002 | 292.2 | 300.8 | 2.9 | 3.126x | 3.126x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 296.9 | 0.0002 | 292.2 | 328.1 | 13.2 | 3.151x | 3.151x |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,188,297.9 | 7.4029 | 10,184,252.9 | 10,202,429.7 | 6,911.6 | 108123.958x | 108123.958x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 91.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,756,780.5 | 7.3974 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 92.1 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 91.3 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,943,261.2 | 7.4130 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.0 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 112.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 485,957.0 | 7.4151 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,927.0 | 2,925.5 | 4,037.8 | 443.9 | 1.000x | 1.000x | 75 | 39.0 | 58.6 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,942.1 | 6,899.2 | 6,954.6 | 20.1 | 2.372x | 2.372x | 75 | 92.6 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,946.4 | 6,875.9 | 6,965.2 | 33.8 | 2.373x | 2.373x | 75 | 92.6 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,964.7 | 25,866.3 | 25,973.8 | 40.3 | 8.871x | 8.871x | 75 | 346.2 | 27.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 75 | 97% | -17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_default-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `file-ext-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `high-byte-run` | `large-subject-throughput` | `plain` | `tre_0.9.0_default-caps-simdna` | 3 | 0% | 0 | 15 | `t-1m` (wrong), `t-256k` (wrong), `t-64k` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 48% | 0 | 195 | `br-dup-param` (wrong), `br-palindrome` (wrong), `cg-number` (wrong), `dt-iso8601` (wrong), `dt-prose-month` (wrong), `la-currency` (wrong), `la-float-bound` (wrong), `la-float-dotted` (wrong), `la-pwd-strong` (wrong), `la-pwd-weak` (wrong), `lp-num-leadzero` (wrong), `lp-num-neg-dec` (wrong), `lp-syslog` (wrong), `lp-winpath` (wrong), `lp-winpath-reserved` (wrong), `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong), `rd-date-hit` (wrong), `rd-email-hit` (wrong), `rd-numeric-id-hit` (wrong), `rd-numeric-id-near-miss` (wrong), `rd-phone-list-hit` (wrong), `rec-array-define` (wrong), `rec-tag-depth3` (wrong), `sec-aws-key` (wrong), `sec-github-pat` (wrong), `sec-slack-webhook` (wrong), `v-ipv4` (wrong), `v-ipv4-oor` (wrong), `v-us-zip` (wrong), `v-us-zip-plus4` (wrong), `v-uuid-badnibble` (wrong), `v-uuid-valid` (wrong), `waf-benign` (wrong), `waf-comment-obfuscation` (wrong), `waf-concat` (wrong), `waf-dbnames` (wrong), `waf-sleep` (wrong), `waf-union` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `tag-pair-match` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `br-tag-pair` (wrong) |
| `wild-waf-crs-942360-concat-sqli` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `waf-union` (wrong) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.8 | 0.0001 | 167.7 | 170.7 | 1.2 | 1.000x | 1.000x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 56.1 | 0.0009 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,045.9 | 2,044.8 | 2,051.3 | 2.5 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,417.2 | 0.0882 | 121,195.4 | 121,618.5 | 137.5 | 1.000x | 1.000x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,621.6 | 0.0883 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,047.8 | 0.0879 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,759.1 | 0.0879 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,464.5 | 2,458.8 | 2,467.1 | 3.3 | 1.000x | 1.000x | 75 | 32.9 | 27.2 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,260.2 | 0.0881 | 120,894.5 | 121,657.3 | 251.3 | 1.000x | 1.000x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,470.3 | 0.0882 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,035.1 | 0.0879 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,754.8 | 0.0878 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,463.2 | 2,453.8 | 2,563.5 | 41.3 | 1.000x | 1.000x | 75 | 32.8 | 27.2 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.7 | 167.2 | 0.2 | 1.000x | 1.000x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0008 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,865.0 | 1,861.9 | 1,867.7 | 1.9 | 1.000x | 1.000x | 75 | 24.9 | 27.2 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,673.8 | 0.0230 | 31,624.3 | 31,707.9 | 26.8 | 1.000x | 1.000x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,115.2 | 0.0230 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,982.9 | 0.0228 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,527.9 | 0.0233 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,847.5 | 1,843.3 | 1,959.4 | 46.1 | 1.000x | 1.000x | 75 | 24.6 | 27.2 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 170.2 | 0.0001 | 169.8 | 174.3 | 1.8 | 1.000x | 1.000x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 58.9 | 0.0009 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 84,638.6 | 0.0615 | 84,550.5 | 84,788.7 | 78.2 | 1.000x | 1.000x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 64,434.3 | 0.0614 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,067.5 | 0.0613 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,119.6 | 0.0629 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,478.9 | 2,477.8 | 2,605.1 | 50.6 | 1.000x | 1.000x | 75 | 33.1 | 27.2 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,335.2 | 0.0235 | 32,332.7 | 32,462.5 | 51.4 | 1.000x | 1.000x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,534.1 | 0.0234 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,143.7 | 0.0234 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,678.0 | 0.0256 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,042.0 | 2,039.4 | 2,073.1 | 12.8 | 1.000x | 1.000x | 75 | 27.2 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 64,081.2 | 0.0466 | 63,973.2 | 64,143.2 | 58.5 | 1.000x | 1.000x |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48,659.0 | 0.0464 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 12,236.1 | 0.0467 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,138.3 | 0.0479 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,639.7 | 2,637.5 | 2,643.7 | 2.6 | 1.000x | 1.000x | 75 | 35.2 | 27.2 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.3 | 30.8 | 0.2 | 1.000x | 1.000x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 949.6 | 948.7 | 950.9 | 0.7 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292.4 | 0.0002 | 292.4 | 293.1 | 0.3 | 1.000x | 1.000x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86.2 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 124.2 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 82.3 | 0.0013 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,687.9 | 2,664.0 | 2,755.3 | 31.8 | 1.000x | 1.000x | 75 | 35.8 | 27.2 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 134.4 | 0.0001 | 133.8 | 134.9 | 0.4 | 1.000x | 1.000x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.4 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45.7 | 0.0007 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,149.8 | 1,144.9 | 1,155.2 | 3.5 | 1.000x | 1.000x | 75 | 15.3 | 27.2 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,656.8 | 0.0230 | 31,637.3 | 31,741.6 | 37.7 | 1.000x | 1.000x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,145.4 | 0.0230 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,978.6 | 0.0228 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.4 | 0.0233 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,048.9 | 2,044.5 | 2,053.2 | 3.0 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.8 | 169.0 | 0.8 | 1.000x | 1.000x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,958.2 | 1,957.7 | 1,975.6 | 6.9 | 1.000x | 1.000x | 75 | 26.1 | 27.2 | 100% |

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.7 | 169.6 | 1.1 | 1.000x | 1.000x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,983.0 | 1,981.7 | 1,983.6 | 0.7 | 1.000x | 1.000x | 75 | 26.4 | 27.2 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,247.3 | 0.0009 | 1,246.8 | 1,251.7 | 2.0 | 1.000x | 1.000x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.9 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 632.2 | 0.0024 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 530.3 | 0.0081 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,296.8 | 2,295.7 | 2,534.7 | 94.7 | 1.000x | 1.000x | 75 | 30.6 | 27.2 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 169.6 | 1.0 | 1.000x | 1.000x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,861.8 | 1,860.9 | 1,864.0 | 1.1 | 1.000x | 1.000x | 75 | 24.8 | 27.2 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.2 | 30.4 | 0.1 | 1.000x | 1.000x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 571.2 | 570.6 | 573.4 | 1.2 | 1.000x | 1.000x | 75 | 7.6 | 27.2 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 123.7 | 0.0001 | 123.3 | 130.7 | 2.8 | 1.000x | 1.000x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 43.4 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 40.8 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 39.6 | 0.0006 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,070.7 | 2,070.5 | 2,091.5 | 8.2 | 1.000x | 1.000x | 75 | 27.6 | 27.2 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 182,372.3 | 0.1325 | 182,184.6 | 182,847.2 | 228.4 | 1.000x | 1.000x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 140,301.4 | 0.1338 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 33,779.6 | 0.1289 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 8,354.1 | 0.1275 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,001.9 | 2,988.6 | 3,184.7 | 75.8 | 1.000x | 1.000x | 75 | 40.0 | 27.2 | 100% |

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,348.7 | 0.0235 | 32,334.6 | 32,456.4 | 45.3 | 1.000x | 1.000x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,530.8 | 0.0234 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,137.7 | 0.0234 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,673.4 | 0.0255 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,039.2 | 2,039.1 | 2,110.8 | 28.5 | 1.000x | 1.000x | 75 | 27.2 | 27.2 | 100% |

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 651.5 | 0.0005 | 650.6 | 688.1 | 14.7 | 1.000x | 1.000x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 209.4 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 214.1 | 0.0008 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 228.4 | 0.0035 |

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,750.1 | 3,746.0 | 3,768.4 | 7.9 | 1.000x | 1.000x | 75 | 50.0 | 27.2 | 100% |

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 147.8 | 0.0001 | 146.9 | 149.4 | 0.8 | 1.000x | 1.000x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.0 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.5 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.4 | 0.0008 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,619.0 | 1,618.0 | 1,627.6 | 4.1 | 1.000x | 1.000x | 75 | 21.6 | 27.2 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292,470.2 | 0.2125 | 292,421.7 | 293,292.6 | 326.1 | 1.000x | 1.000x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 223,226.8 | 0.2129 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55,299.2 | 0.2109 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 14,025.7 | 0.2140 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,103.2 | 2,101.5 | 2,103.9 | 0.8 | 1.000x | 1.000x | 75 | 28.0 | 27.2 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,324.7 | 0.0438 | 60,289.3 | 60,386.9 | 32.2 | 1.000x | 1.000x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,871.9 | 0.0437 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,513.5 | 0.0439 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,943.6 | 0.0449 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 829.8 | 827.8 | 830.7 | 1.2 | 1.000x | 1.000x | 75 | 11.1 | 27.2 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 111,983.2 | 0.0814 | 111,928.7 | 112,443.5 | 193.7 | 1.000x | 1.000x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86,547.2 | 0.0825 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,573.4 | 0.0785 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,869.5 | 0.0743 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 694.3 | 692.5 | 695.1 | 0.9 | 1.000x | 1.000x | 75 | 9.3 | 27.2 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 475,056.4 | 0.3452 | 474,924.7 | 476,086.8 | 498.4 | 1.000x | 1.000x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 377,595.2 | 0.3601 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81,082.5 | 0.3093 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,407.2 | 0.2504 |

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,647.4 | 1,645.7 | 1,683.2 | 14.6 | 1.000x | 1.000x | 75 | 22.0 | 27.2 | 100% |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 153,409.3 | 0.1115 | 153,382.2 | 153,915.9 | 228.1 | 1.000x | 1.000x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 116,853.5 | 0.1114 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 29,184.1 | 0.1113 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,382.0 | 0.1126 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,402.5 | 2,399.7 | 2,406.6 | 2.5 | 1.000x | 1.000x | 75 | 32.0 | 27.2 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 223.3 | 0.0002 | 223.2 | 226.0 | 1.1 | 1.000x | 1.000x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 73.9 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75.1 | 0.0003 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.3 | 0.0011 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,760.9 | 2,757.8 | 2,771.5 | 4.9 | 1.000x | 1.000x | 75 | 36.8 | 27.2 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 241.4 | 0.0002 | 241.2 | 242.3 | 0.4 | 1.000x | 1.000x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 83.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 78.7 | 0.0003 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 79.4 | 0.0012 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,892.4 | 3,886.7 | 4,064.4 | 69.3 | 1.000x | 1.000x | 75 | 51.9 | 27.2 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 199.8 | 0.0001 | 195.6 | 202.2 | 2.3 | 1.000x | 1.000x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 61.3 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 63.3 | 0.0010 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,247.0 | 2,244.2 | 2,268.6 | 9.0 | 1.000x | 1.000x | 75 | 30.0 | 27.2 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 36.4 | 2.9 | 1.000x | 1.000x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 950.7 | 949.6 | 952.6 | 1.1 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.4 | 0.1 | 1.000x | 1.000x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.0 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 986.3 | 984.0 | 1,176.3 | 76.2 | 1.000x | 1.000x | 75 | 13.2 | 27.2 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243,490.9 | 0.1769 | 243,334.2 | 245,883.2 | 970.7 | 1.000x | 1.000x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 185,930.3 | 0.1773 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 46,122.8 | 0.1759 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,429.7 | 0.1744 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,625.9 | 1,623.3 | 1,676.5 | 20.6 | 1.000x | 1.000x | 75 | 21.7 | 27.2 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 600,337.0 | 0.4362 | 600,029.2 | 600,994.4 | 346.0 | 1.000x | 1.000x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 477,905.1 | 0.4558 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 101,807.6 | 0.3884 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,492.4 | 0.3127 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,412.9 | 3,406.4 | 3,884.5 | 185.7 | 1.000x | 1.000x | 75 | 45.5 | 27.2 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 160,217.0 | 0.1164 | 160,176.6 | 160,496.2 | 119.3 | 1.000x | 1.000x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 122,101.2 | 0.1164 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 30,347.6 | 0.1158 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,761.9 | 0.1184 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,420.3 | 2,418.3 | 2,429.3 | 4.3 | 1.000x | 1.000x | 75 | 32.3 | 27.2 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 86,366.8 | 0.0628 | 86,279.7 | 86,983.2 | 253.6 | 1.000x | 1.000x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 65,811.0 | 0.0628 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,405.2 | 0.0626 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,147.7 | 0.0633 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,914.2 | 1,910.3 | 1,918.6 | 3.2 | 1.000x | 1.000x | 75 | 25.5 | 27.2 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 878,263.5 | 0.6382 | 875,941.9 | 880,883.5 | 1,594.2 | 1.000x | 1.000x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 700,812.1 | 0.6683 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 149,157.3 | 0.5690 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 28,185.7 | 0.4301 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 4,575.5 | 4,558.2 | 4,581.3 | 9.6 | 1.000x | 1.000x | 75 | 61.0 | 27.2 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,231.1 | 0.0438 | 60,206.6 | 60,404.6 | 71.4 | 1.000x | 1.000x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,839.1 | 0.0437 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,470.4 | 0.0438 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,937.5 | 0.0448 |

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,358.9 | 2,352.4 | 2,360.9 | 3.5 | 1.000x | 1.000x | 75 | 31.5 | 27.2 | 100% |

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 133.2 | 0.0001 | 133.0 | 135.0 | 0.8 | 1.000x | 1.000x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0000 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0002 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.6 | 0.0007 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,463.5 | 1,462.9 | 1,468.1 | 1.9 | 1.000x | 1.000x | 75 | 19.5 | 27.2 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `base10num-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 98.6 | 0.0001 | 96.2 | 99.6 | 1.4 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.8 | 0.0001 | 167.7 | 170.7 | 1.2 | 1.701x | 1.701x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.7 | 0.0002 | 284.4 | 287.5 | 1.2 | 2.886x | 2.886x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.1 | 0.0002 | 284.6 | 286.9 | 0.8 | 2.900x | 2.900x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,845,276.0 | 8.6069 | 11,812,971.8 | 11,862,771.1 | 17,777.9 | 120079.005x | 120079.005x |

#### `base10num-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.1 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,006,526.5 | 8.5893 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.3 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,259,736.6 | 8.6202 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.3 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 56.1 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.6 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 565,736.0 | 8.6324 |

### `base10num-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,045.9 | 2,044.8 | 2,051.3 | 2.5 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,063.2 | 4,060.9 | 4,188.6 | 50.3 | 1.986x | 1.986x | 75 | 54.2 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,074.3 | 4,061.9 | 4,144.1 | 29.9 | 1.991x | 1.991x | 75 | 54.3 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,820.8 | 7,793.4 | 8,921.5 | 439.2 | 3.823x | 3.823x | 75 | 104.3 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,752.6 | 18,606.6 | 19,026.7 | 153.3 | 9.166x | 9.166x | 75 | 250.0 | 27.9 | 100% |

### `bracket-array-define` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 93.6 | 0.0001 | 93.5 | 94.0 | 0.2 | 1.000x | 1.000x |

#### `bracket-array-define` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0001 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |

### `bracket-array-define` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,915.5 | 2,905.9 | 2,938.8 | 11.4 | 1.000x | 1.000x | 75 | 38.9 | 58.6 | 100% |

### `codegrammar-flat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,417.2 | 0.0882 | 121,195.4 | 121,618.5 | 137.5 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,236,210.3 | 1.6249 | 2,235,095.1 | 2,247,883.7 | 4,756.4 | 18.418x | 18.418x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,237,315.8 | 1.6257 | 2,236,202.2 | 2,247,920.8 | 4,278.3 | 18.427x | 18.427x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,735,646.5 | 7.0740 | 9,613,981.1 | 9,806,489.4 | 77,809.8 | 80.183x | 80.183x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,778,404.6 | 46.3420 | 63,649,370.0 | 64,735,844.2 | 406,183.9 | 525.283x | 525.283x |

#### `codegrammar-flat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,621.6 | 0.0883 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,697,325.1 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,389.9 | 1.6188 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,449,226.5 | 7.1041 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 48,552,432.6 | 46.3032 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,047.8 | 0.0879 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,729.6 | 1.6164 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,926.5 | 1.6172 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,830,389.5 | 6.9824 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,110,604.0 | 46.1983 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,759.1 | 0.0879 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,494.5 | 1.7623 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,024.9 | 1.7704 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 457,626.6 | 6.9828 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,049,123.6 | 46.5259 |

### `codegrammar-flat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,464.5 | 2,458.8 | 2,467.1 | 3.3 | 1.000x | 1.000x | 75 | 32.9 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,640.6 | 5,610.8 | 5,650.8 | 14.9 | 2.289x | 2.289x | 75 | 75.2 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,685.4 | 7,679.8 | 7,790.8 | 41.8 | 3.118x | 3.118x | 75 | 102.5 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,688.0 | 7,684.2 | 7,703.1 | 7.4 | 3.120x | 3.120x | 75 | 102.5 | 100.0 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,944.9 | 23,902.4 | 24,353.1 | 166.8 | 9.716x | 9.716x | 75 | 319.3 | 27.9 | 100% |

### `codegrammar-xflag` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 121,260.2 | 0.0881 | 120,894.5 | 121,657.3 | 251.3 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,728,745.7 | 7.0690 | 9,629,121.1 | 9,805,223.6 | 67,491.8 | 80.230x | 80.230x |

#### `codegrammar-xflag` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 92,470.3 | 0.0882 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,428,697.6 | 7.0846 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 23,035.1 | 0.0879 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,835,720.2 | 7.0027 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,754.8 | 0.0878 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 464,327.9 | 7.0851 |

### `codegrammar-xflag` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,463.2 | 2,453.8 | 2,563.5 | 41.3 | 1.000x | 1.000x | 75 | 32.8 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,638.2 | 5,613.3 | 5,653.6 | 15.7 | 2.289x | 2.289x | 75 | 75.2 | 58.6 | 100% |

### `currency-lookbehind-fixed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,600,379.3 | 6.9757 | 9,582,038.1 | 9,607,703.2 | 8,643.7 | 1.000x | 1.000x |

#### `currency-lookbehind-fixed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 7,351,415.6 | 7.0109 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,807,749.4 | 6.8960 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 438,464.7 | 6.6904 |

### `currency-lookbehind-fixed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,465.4 | 17,375.1 | 18,436.9 | 400.6 | 1.000x | 1.000x | 75 | 232.9 | 58.6 | 100% |

### `date-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 93.9 | 95.0 | 0.4 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.7 | 167.2 | 0.2 | 1.761x | 1.761x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 285.2 | 0.0002 | 283.0 | 342.4 | 23.0 | 3.009x | 3.009x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.8 | 291.7 | 2.1 | 3.037x | 3.037x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,686,289.3 | 6.3115 | 8,680,636.3 | 8,713,813.6 | 12,994.9 | 91655.053x | 91655.053x |

#### `date-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,620,212.8 | 6.3135 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,652,237.6 | 6.3028 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 106.9 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 414,644.0 | 6.3270 |

### `date-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,865.0 | 1,861.9 | 1,867.7 | 1.9 | 1.000x | 1.000x | 75 | 24.9 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,733.3 | 5,691.7 | 5,790.2 | 35.1 | 3.074x | 3.074x | 75 | 76.4 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,662.9 | 9,510.4 | 9,937.2 | 146.8 | 5.181x | 5.181x | 75 | 128.8 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,667.3 | 9,546.6 | 9,706.4 | 70.8 | 5.183x | 5.183x | 75 | 128.9 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,726.6 | 13,694.3 | 13,864.7 | 61.4 | 7.360x | 7.360x | 75 | 183.0 | 27.9 | 100% |

### `doubled-word` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 80,036,131.5 | 58.1550 | 79,688,787.0 | 80,380,958.5 | 232,715.3 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 216,510,331.5 | 157.3184 | 214,715,651.5 | 220,132,807.5 | 2,159,864.3 | 2.705x | 2.705x |

#### `doubled-word` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 60,903,021.0 | 58.0816 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 165,042,159.0 | 157.3965 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 15,257,858.0 | 58.2041 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 41,252,118.5 | 157.3643 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,851,262.2 | 58.7656 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 10,231,189.5 | 156.1156 |

### `doubled-word` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 89,010.3 | 88,938.4 | 89,450.5 | 207.9 | 1.000x | 1.000x | 75 | 1,186.8 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 210,823.4 | 209,975.6 | 238,061.8 | 10,916.4 | 2.369x | 2.369x | 75 | 2,811.0 | 27.9 | 100% |

### `dup-param-detect` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,794.5 | 1.6195 | 2,227,479.4 | 2,233,759.4 | 2,266.2 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 184,142,654.5 | 133.7997 | 183,038,538.0 | 186,214,666.5 | 1,063,804.1 | 82.620x | 82.620x |

#### `dup-param-detect` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,957.5 | 1.6183 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 140,484,082.0 | 133.9761 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,780.4 | 1.6204 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 34,932,582.0 | 133.2572 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,683.3 | 1.6279 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,730,210.5 | 133.2124 |

### `dup-param-detect` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,896.5 | 8,839.2 | 8,934.6 | 35.8 | 1.000x | 1.000x | 75 | 118.6 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 195,786.6 | 195,028.2 | 196,848.3 | 636.8 | 22.007x | 22.007x | 75 | 2,610.5 | 27.9 | 100% |

### `email-local-nodup` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,381.0 | 0.0010 | 1,373.7 | 1,398.2 | 8.7 | 1.000x | 1.000x |

#### `email-local-nodup` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 388.3 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 555.8 | 0.0021 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 436.3 | 0.0067 |

### `email-local-nodup` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 18,596.6 | 18,446.5 | 18,750.3 | 99.5 | 1.000x | 1.000x | 75 | 248.0 | 58.6 | 100% |

### `email-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 342.5 | 0.0002 | 337.1 | 347.8 | 3.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 343.5 | 0.0002 | 340.7 | 362.3 | 7.7 | 1.003x | 1.003x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,673.8 | 0.0230 | 31,624.3 | 31,707.9 | 26.8 | 92.484x | 92.484x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,826.3 | 1.6195 | 2,227,226.6 | 2,232,639.0 | 1,937.3 | 6507.930x | 6507.930x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 22,211,467.6 | 16.1391 | 21,620,955.8 | 22,626,074.1 | 325,440.7 | 64855.063x | 64855.063x |

#### `email-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 113.1 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 114.1 | 0.0001 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,115.2 | 0.0230 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,697.9 | 1.6181 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,863,261.7 | 16.0821 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 103.5 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,982.9 | 0.0228 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,593.3 | 1.6197 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,261,958.8 | 16.2581 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 125.6 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 126.1 | 0.0019 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,527.9 | 0.0233 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,555.7 | 1.6259 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,073,617.1 | 16.3821 |

### `email-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,847.5 | 1,843.3 | 1,959.4 | 46.1 | 1.000x | 1.000x | 75 | 24.6 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,069.0 | 5,055.9 | 5,084.1 | 11.9 | 2.744x | 2.744x | 75 | 67.6 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 43,685.4 | 43,549.2 | 44,103.8 | 221.5 | 23.646x | 23.646x | 75 | 582.5 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 44,529.2 | 44,338.4 | 44,617.8 | 99.0 | 24.103x | 24.103x | 75 | 593.7 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 205,268.9 | 204,661.5 | 210,778.8 | 2,401.2 | 111.109x | 111.109x | 75 | 2,736.9 | 27.9 | 100% |

### `evil-alt-nested` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 170.2 | 0.0001 | 169.8 | 174.3 | 1.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 310.1 | 0.0002 | 309.6 | 355.0 | 17.9 | 1.822x | 1.822x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 311.9 | 0.0002 | 309.6 | 313.7 | 1.4 | 1.833x | 1.833x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,638.1 | 0.0128 | 17,557.2 | 17,717.4 | 53.7 | 103.641x | 103.641x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,217,479.4 | 7.4241 | 10,210,376.3 | 10,223,737.2 | 4,636.8 | 60037.694x | 60037.694x |

#### `evil-alt-nested` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 99.2 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,892.3 | 0.0018 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,783,757.7 | 7.4232 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.7 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 87.9 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 297.6 | 0.0011 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,945,327.8 | 7.4208 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 58.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 122.7 | 0.0019 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 124.4 | 0.0019 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 15,439.1 | 0.2356 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 488,318.6 | 7.4512 |

### `file-ext-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 84,638.6 | 0.0615 | 84,550.5 | 84,788.7 | 78.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 249,978.4 | 0.1816 | 249,850.7 | 250,581.3 | 256.9 | 2.953x | 2.953x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 250,174.3 | 0.1818 | 249,698.6 | 250,649.2 | 300.8 | 2.956x | 2.956x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,180,777.2 | 0.8580 | 1,180,653.9 | 1,183,211.5 | 986.9 | 13.951x | 13.951x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,645,312.8 | 18.6341 | 25,626,430.0 | 25,665,305.6 | 14,816.7 | 302.998x | 302.998x |

#### `file-ext-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 64,434.3 | 0.0614 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 196,476.5 | 0.1874 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 196,564.2 | 0.1875 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 897,757.5 | 0.8562 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,528,609.3 | 18.6239 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,067.5 | 0.0613 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 42,468.6 | 0.1620 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 42,522.2 | 0.1622 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 226,234.7 | 0.8630 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,890,331.9 | 18.6551 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,119.6 | 0.0629 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 11,077.3 | 0.1690 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 11,069.3 | 0.1689 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 56,901.5 | 0.8682 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,225,718.9 | 18.7030 |

### `file-ext-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,478.9 | 2,477.8 | 2,605.1 | 50.6 | 1.000x | 1.000x | 75 | 33.1 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,197.6 | 3,179.9 | 3,198.9 | 7.9 | 1.290x | 1.290x | 75 | 42.6 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,650.8 | 7,635.1 | 7,782.0 | 55.4 | 3.086x | 3.086x | 75 | 102.0 | 100.0 | 100% |

### `float-literal-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,300,527.7 | 9.6643 | 13,268,289.0 | 13,388,146.2 | 42,996.0 | 1.000x | 1.000x |

#### `float-literal-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 10,194,825.3 | 9.7225 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,505,563.0 | 9.5580 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 604,153.4 | 9.2187 |

### `float-literal-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 20,462.7 | 20,445.9 | 20,744.0 | 111.6 | 1.000x | 1.000x | 75 | 272.8 | 58.6 | 100% |

### `floor-byte` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,199.2 | 0.0169 | 23,191.3 | 23,318.0 | 47.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,801.6 | 0.0173 | 23,778.5 | 23,892.2 | 39.9 | 1.026x | 1.026x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,936.7 | 0.0174 | 23,910.8 | 24,048.7 | 48.8 | 1.032x | 1.032x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,335.2 | 0.0235 | 32,332.7 | 32,462.5 | 51.4 | 1.394x | 1.394x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,556.4 | 1.6193 | 2,227,650.2 | 6,262,574.3 | 1,613,659.5 | 96.062x | 96.062x |

#### `floor-byte` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,650.6 | 0.0168 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,839.7 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,840.8 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,534.1 | 0.0234 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,229.0 | 1.6186 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,408.0 | 0.0168 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,508.8 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,524.3 | 0.0173 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,143.7 | 0.0234 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,555.6 | 1.6196 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,136.3 | 0.0173 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,458.3 | 0.0223 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,571.4 | 0.0240 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,678.0 | 0.0256 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,356.4 | 1.6229 |

### `floor-byte` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,042.0 | 2,039.4 | 2,073.1 | 12.8 | 1.000x | 1.000x | 75 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,091.6 | 2,091.2 | 2,095.2 | 1.5 | 1.024x | 1.024x | 75 | 27.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.0 | 4,389.9 | 4,412.5 | 9.0 | 2.153x | 2.153x | 75 | 58.6 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,501.3 | 7,490.1 | 7,519.2 | 10.3 | 3.673x | 3.673x | 75 | 100.0 | 100% |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,512.5 | 7,503.6 | 7,522.3 | 6.9 | 3.679x | 3.679x | 75 | 100.2 | 100% |

### `high-byte-run` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 64,081.2 | 0.0466 | 63,973.2 | 64,143.2 | 58.5 | 1.000x | 1.000x | 3 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,035,195.9 | 1.4788 | 2,034,726.2 | 2,041,089.2 | 2,382.7 | 31.760x | 31.760x | 3 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,795.8 | 1.6267 | 2,230,522.7 | 2,245,104.7 | 5,639.3 | 34.937x | 34.937x | 3 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,737.3 | 1.6303 | 2,242,372.1 | 2,562,583.7 | 127,765.6 | 35.014x | 35.014x | 3 | 100% |

#### `high-byte-run` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 48,659.0 | 0.0464 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,550,179.3 | 1.4784 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,361.2 | 1.6206 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,703,107.9 | 1.6242 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 12,236.1 | 0.0467 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,601.1 | 1.4786 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,278.2 | 1.6147 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,570.0 | 1.6196 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,138.3 | 0.0479 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,429.9 | 1.4867 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,049.9 | 1.7708 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,000.8 | 1.7700 |

### `high-byte-run` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,639.7 | 2,637.5 | 2,643.7 | 2.6 | 1.000x | 1.000x | 75 | 35.2 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,195.5 | 5,189.3 | 5,210.9 | 7.9 | 1.968x | 1.968x | 75 | 69.3 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,680.5 | 9,660.9 | 9,833.1 | 63.6 | 3.667x | 3.667x | 75 | 129.1 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,730.8 | 9,702.7 | 9,856.5 | 65.5 | 3.686x | 3.686x | 75 | 129.7 | 100.2 | 100% |

### `ipv4-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.5 | 0.0000 | 30.3 | 30.8 | 0.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.7 | 0.0002 | 281.7 | 287.4 | 2.0 | 9.344x | 9.344x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.3 | 0.0002 | 286.4 | 291.3 | 2.1 | 9.430x | 9.430x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 361.0 | 380.9 | 7.2 | 12.058x | 12.058x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,439,869.0 | 11.2187 | 15,401,899.9 | 15,724,924.6 | 120,366.5 | 506778.981x | 506778.981x |

#### `ipv4-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.1 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 302.7 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,753,517.2 | 11.2090 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 87.8 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.8 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0001 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,966,689.3 | 11.3170 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.2 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0005 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 745,934.3 | 11.3821 |

### `ipv4-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 949.6 | 948.7 | 950.9 | 0.7 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,410.3 | 3,397.7 | 3,444.8 | 16.5 | 3.591x | 3.591x | 75 | 45.5 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,832.1 | 6,812.5 | 6,912.4 | 43.4 | 7.195x | 7.195x | 75 | 91.1 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,848.5 | 6,837.0 | 6,896.7 | 21.9 | 7.212x | 7.212x | 75 | 91.3 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,547.2 | 30,197.3 | 30,913.0 | 267.8 | 32.168x | 32.168x | 75 | 407.3 | 27.9 | 100% |

### `keyword-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292.4 | 0.0002 | 292.4 | 293.1 | 0.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,442,039.1 | 1.7744 | 2,429,228.9 | 2,487,973.9 | 21,518.6 | 8350.635x | 8350.635x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,487,038.7 | 1.8071 | 2,475,028.9 | 2,506,509.1 | 10,714.5 | 8504.513x | 8504.513x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,965,092.1 | 2.8811 | 3,957,525.3 | 3,989,063.6 | 11,202.9 | 13558.767x | 13558.767x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 29,542,544.1 | 21.4659 | 29,498,658.1 | 29,614,725.7 | 41,323.1 | 101021.729x | 101021.729x |

#### `keyword-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86.2 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,866,880.9 | 1.7804 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,899,496.7 | 1.8115 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,023,162.4 | 2.8831 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 22,494,733.3 | 21.4526 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 124.2 | 0.0005 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 456,833.3 | 1.7427 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 465,675.9 | 1.7764 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 755,525.0 | 2.8821 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,635,318.1 | 21.4970 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 82.3 | 0.0013 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 119,979.0 | 1.8307 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 121,067.9 | 1.8473 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 185,727.1 | 2.8340 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,413,374.8 | 21.5664 |

### `keyword-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,687.9 | 2,664.0 | 2,755.3 | 31.8 | 1.000x | 1.000x | 75 | 35.8 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,042.2 | 4,036.1 | 4,063.9 | 9.9 | 1.504x | 1.504x | 75 | 53.9 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,990.8 | 7,903.9 | 8,199.3 | 112.7 | 2.973x | 2.973x | 75 | 106.5 | 100.0 | 100% |

### `logparse-atomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.7 | 0.0001 | 97.3 | 104.2 | 2.7 | 1.000x | 1.000x |

#### `logparse-atomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.7 | 0.0005 |

### `logparse-atomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,029.4 | 4,984.7 | 5,092.2 | 38.0 | 1.000x | 1.000x | 75 | 67.1 | 58.6 | 100% |

### `logparse-atomic-removed` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 97.4 | 0.0001 | 97.1 | 104.2 | 2.7 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 134.4 | 0.0001 | 133.8 | 134.9 | 0.4 | 1.379x | 1.379x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.8 | 0.0002 | 285.2 | 344.2 | 23.2 | 2.943x | 2.943x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 287.8 | 0.0002 | 285.9 | 291.5 | 2.1 | 2.953x | 2.953x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,159,734.8 | 13.9216 | 19,126,668.1 | 20,247,433.9 | 520,105.0 | 196620.778x | 196620.778x |

#### `logparse-atomic-removed` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 32.5 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.3 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,567,739.7 | 13.8929 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 32.4 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.4 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.3 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.8 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,676,688.4 | 14.0255 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 32.6 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45.7 | 0.0007 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 110.1 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.1 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 920,840.3 | 14.0509 |

### `logparse-atomic-removed` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,149.8 | 1,144.9 | 1,155.2 | 3.5 | 1.000x | 1.000x | 75 | 15.3 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,983.4 | 4,969.5 | 5,066.7 | 36.0 | 4.334x | 4.334x | 75 | 66.4 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,895.6 | 7,872.7 | 8,088.5 | 94.3 | 6.867x | 6.867x | 75 | 105.3 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,028.0 | 7,948.6 | 8,153.9 | 73.3 | 6.982x | 6.982x | 75 | 107.0 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 41,789.1 | 40,846.3 | 41,972.8 | 444.0 | 36.345x | 36.345x | 75 | 557.2 | 27.9 | 100% |

### `mojibake-curly-quote` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: re2_11.0.0_longest-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,764.4 | 0.0173 | 23,749.0 | 23,788.5 | 13.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,903.0 | 0.0174 | 23,880.3 | 23,910.3 | 11.0 | 1.006x | 1.006x |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 31,656.8 | 0.0230 | 31,637.3 | 31,741.6 | 37.7 | 1.332x | 1.332x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,228,965.5 | 1.6196 | 2,228,367.8 | 2,229,892.6 | 527.0 | 93.794x | 93.794x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,626,598.2 | 15.7141 | 20,391,829.5 | 23,439,821.3 | 1,175,032.1 | 910.043x | 910.043x |

#### `mojibake-curly-quote` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,797.8 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,822.6 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,145.4 | 0.0230 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,595.4 | 1.6190 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,471,239.3 | 15.7082 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,515.3 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,534.1 | 0.0173 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,978.6 | 0.0228 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,823.1 | 1.6206 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,121,533.8 | 15.7224 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,452.2 | 0.0222 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,539.8 | 0.0235 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,529.4 | 0.0233 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,805.5 | 1.6297 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,144,597.4 | 17.4652 |

### `mojibake-curly-quote` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,048.9 | 2,044.5 | 2,053.2 | 3.0 | 1.000x | 1.000x | 75 | 27.3 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,421.8 | 4,415.6 | 4,517.8 | 39.0 | 2.158x | 2.158x | 75 | 59.0 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,528.6 | 7,518.6 | 7,541.8 | 7.6 | 3.675x | 3.675x | 75 | 100.4 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,542.8 | 7,518.7 | 7,553.1 | 12.2 | 3.681x | 3.681x | 75 | 100.6 | 100.0 | 100% |

### `nested-comment-rec` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,679.7 | 1.0890 | 1,498,478.1 | 1,499,819.6 | 503.0 | 1.000x | 1.000x |

#### `nested-comment-rec` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,707.7 | 1.0888 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,203.7 | 1.0880 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,686.3 | 1.0938 |

### `nested-comment-rec` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,461.8 | 4,452.7 | 4,474.4 | 7.4 | 1.000x | 1.000x | 75 | 59.5 | 58.6 | 100% |

### `numeric-id-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 95.3 | 0.0001 | 93.7 | 101.3 | 3.2 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.8 | 169.0 | 0.8 | 1.751x | 1.751x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.1 | 0.0002 | 284.4 | 298.2 | 5.3 | 2.991x | 2.991x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 285.9 | 0.0002 | 283.9 | 287.2 | 1.2 | 2.999x | 2.999x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,689,123.8 | 6.3136 | 8,682,341.8 | 8,716,311.4 | 14,626.1 | 91156.047x | 91156.047x |

#### `numeric-id-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.9 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,619,895.1 | 6.3132 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.8 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,991.8 | 6.3095 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.6 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.8 | 0.0016 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 415,017.9 | 6.3327 |

### `numeric-id-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,958.2 | 1,957.7 | 1,975.6 | 6.9 | 1.000x | 1.000x | spread | 75 | 26.1 | 27.2 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,603.5 | 9,577.6 | 9,792.7 | 79.4 | 4.904x | 4.904x | spread | 75 | 128.0 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,635.4 | 9,605.8 | 9,701.8 | 37.3 | 4.921x | 4.921x | spread | 75 | 128.5 | 100.0 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,302.4 | 13,248.6 | 13,345.6 | 34.6 | 6.793x | 6.793x | spread | 75 | 177.4 | 27.9 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,590,485.6 | 12,556,989.4 | 12,952,288.1 | 149,711.2 | 6429.602x | 6429.602x | **dominated**: `rd-numeric-id-near-miss` is 99.9% of this set | 75 | 167,873.1 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-list-nested-plus` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.7 | 0.0001 | 93.7 | 95.4 | 0.7 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 166.9 | 0.0001 | 166.7 | 169.6 | 1.1 | 1.761x | 1.761x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.2 | 0.0002 | 283.6 | 295.7 | 4.6 | 2.999x | 2.999x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.4 | 0.0002 | 284.0 | 289.7 | 1.8 | 3.023x | 3.023x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,686,920.8 | 6.3120 | 8,684,292.5 | 8,719,581.7 | 13,275.6 | 91685.062x | 91685.062x |

#### `phone-list-nested-plus` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.4 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,616,979.9 | 6.3104 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.1 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,653,002.2 | 6.3057 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.8 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.4 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.4 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 416,018.9 | 6.3479 |

### `phone-list-nested-plus` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,983.0 | 1,981.7 | 1,983.6 | 0.7 | 1.000x | 1.000x | spread | 75 | 26.4 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,101.6 | 9,991.2 | 10,205.8 | 72.8 | 5.094x | 5.094x | spread | 75 | 134.7 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,105.3 | 10,021.8 | 10,821.2 | 302.4 | 5.096x | 5.096x | spread | 75 | 134.7 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,104.5 | 14,935.7 | 15,156.8 | 89.6 | 7.617x | 7.617x | spread | 75 | 201.4 | 27.9 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 16,693,186.2 | 16,645,155.7 | 17,278,804.8 | 238,231.0 | 8418.020x | 8418.020x | **dominated**: `rd-numeric-id-near-miss` is 100.0% of this set | 75 | 222,575.8 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `phone-palindrome-6` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 14,477,787.7 | 10.5197 | 14,410,840.5 | 16,677,678.8 | 885,794.3 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,737,655.1 | 20.8810 | 28,699,391.8 | 28,880,049.0 | 67,087.2 | 1.985x | 1.985x |

#### `phone-palindrome-6` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 11,103,596.2 | 10.5892 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,920,060.7 | 20.9046 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 2,720,979.9 | 10.3797 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,450,709.5 | 20.7928 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 658,196.4 | 10.0433 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,357,390.8 | 20.7121 |

### `phone-palindrome-6` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 22,750.7 | 22,734.3 | 22,863.2 | 55.8 | 1.000x | 1.000x | 75 | 303.3 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,351.3 | 29,990.7 | 30,569.7 | 187.1 | 1.334x | 1.334x | 75 | 404.7 | 27.9 | 100% |

### `pwd-strength-chain` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,048.4 | 0.0029 | 4,037.1 | 4,824.4 | 310.2 | 1.000x | 1.000x |

#### `pwd-strength-chain` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 573.5 | 0.0005 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,841.3 | 0.0070 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,633.7 | 0.0249 |

### `pwd-strength-chain` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 36,028.0 | 36,023.7 | 38,607.8 | 1,014.2 | 1.000x | 1.000x | 75 | 480.4 | 58.6 | 100% |

### `quoted-delim-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,837,824.3 | 2.7886 | 3,817,923.8 | 3,870,074.1 | 18,863.8 | 1.000x | 1.000x |

#### `quoted-delim-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,936,976.8 | 2.8009 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 718,631.8 | 2.7414 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 180,419.7 | 2.7530 |

### `quoted-delim-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,095.2 | 7,081.4 | 7,134.8 | 18.7 | 1.000x | 1.000x | 75 | 94.6 | 58.6 | 100% |

### `router-prefix-order` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,247.3 | 0.0009 | 1,246.8 | 1,251.7 | 2.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 398,855.6 | 0.2898 | 398,612.9 | 401,866.5 | 1,218.8 | 319.770x | 319.770x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 400,418.3 | 0.2909 | 399,254.2 | 405,719.5 | 2,441.8 | 321.023x | 321.023x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,361,509.6 | 0.9893 | 1,360,131.0 | 1,366,519.3 | 2,209.7 | 1091.549x | 1091.549x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 26,472,797.1 | 19.2354 | 26,439,972.9 | 26,536,229.4 | 37,809.2 | 21223.758x | 21223.758x |

#### `router-prefix-order` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 84.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 304,403.1 | 0.2903 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 305,168.2 | 0.2910 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,039,087.2 | 0.9910 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 20,178,300.7 | 19.2435 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 632.2 | 0.0024 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 74,613.1 | 0.2846 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 74,791.7 | 0.2853 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 259,546.0 | 0.9901 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,039,899.1 | 19.2257 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 530.3 | 0.0081 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 19,615.2 | 0.2993 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 19,827.3 | 0.3025 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 62,428.3 | 0.9526 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,260,728.3 | 19.2372 |

### `router-prefix-order` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,296.8 | 2,295.7 | 2,534.7 | 94.7 | 1.000x | 1.000x | 75 | 30.6 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,808.1 | 2,801.2 | 2,840.1 | 17.2 | 1.223x | 1.223x | 75 | 37.4 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,612.8 | 7,591.2 | 7,887.0 | 112.8 | 3.315x | 3.315x | 75 | 101.5 | 100.0 | 100% |

### `tag-depth3-bound` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,230,556.5 | 1.6207 | 2,228,823.6 | 2,233,826.7 | 1,803.9 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 34,518,744.6 | 25.0816 | 34,494,834.5 | 34,865,714.1 | 140,472.3 | 15.475x | 15.475x |

#### `tag-depth3-bound` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,961.9 | 1.6193 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,291,626.9 | 25.0736 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 425,020.0 | 1.6213 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,569,446.6 | 25.0605 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,562.7 | 1.6260 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,645,550.9 | 25.1091 |

### `tag-depth3-bound` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,552.2 | 6,546.6 | 6,588.6 | 15.0 | 1.000x | 1.000x | 75 | 87.4 | 58.6 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,397.7 | 47,362.2 | 47,585.5 | 81.5 | 7.234x | 7.234x | 75 | 632.0 | 27.9 | 100% |

### `tag-pair-match` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,027.8 | 1.6196 | 2,228,591.7 | 2,240,708.9 | 4,690.7 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 27,780,021.7 | 20.1852 | 27,713,332.4 | 27,822,273.1 | 38,966.6 | 12.463x | 12.463x |

#### `tag-pair-match` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,627.3 | 1.6190 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,122,834.3 | 20.1443 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,700.0 | 1.6201 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,273,562.8 | 20.1170 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,597.8 | 1.6266 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,337,638.9 | 20.4107 |

### `tag-pair-match` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,951.1 | 5,937.2 | 5,964.9 | 11.6 | 1.000x | 1.000x | 75 | 79.3 | 58.6 | 100% |

### `trim-nested-star` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 167.0 | 0.0001 | 166.9 | 169.6 | 1.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.6 | 0.0002 | 282.4 | 286.9 | 1.5 | 1.704x | 1.704x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 286.6 | 0.0002 | 285.7 | 289.0 | 1.1 | 1.716x | 1.716x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 745.0 | 0.0005 | 729.6 | 752.1 | 8.6 | 4.460x | 4.460x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,849,925.9 | 8.6103 | 11,835,794.0 | 21,775,545.9 | 3,958,306.3 | 70940.967x | 70940.967x |

#### `trim-nested-star` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 87.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 89.6 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 247.1 | 0.0002 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,038,698.3 | 8.6200 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.6 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.6 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 247.3 | 0.0009 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,251,950.4 | 8.5905 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55.9 | 0.0009 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 249.8 | 0.0038 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 571,801.6 | 8.7250 |

### `trim-nested-star` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,861.8 | 1,860.9 | 1,864.0 | 1.1 | 1.000x | 1.000x | spread | 75 | 24.8 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,419.7 | 9,402.9 | 9,560.5 | 59.7 | 5.060x | 5.060x | spread | 75 | 125.6 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,468.1 | 9,446.9 | 9,519.3 | 27.8 | 5.086x | 5.086x | spread | 75 | 126.2 | 100.2 | 100% |
| 4 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 19,511.4 | 19,426.2 | 19,566.0 | 50.9 | 10.480x | 10.480x | spread | 75 | 260.2 | 27.9 | 100% |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,536,685.1 | 12,517,587.1 | 12,554,973.7 | 12,607.1 | 6733.806x | 6733.806x | **dominated**: `rd-trim-near-miss` is 99.9% of this set | 75 | 167,155.8 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `utf8-lead-no-cont` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,036,374.5 | 1.4796 | 2,035,108.2 | 2,045,770.6 | 3,993.6 | 1.000x | 1.000x |

#### `utf8-lead-no-cont` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,551,224.2 | 1.4794 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 387,805.3 | 1.4794 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 97,542.6 | 1.4884 |

### `utf8-lead-no-cont` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,932.3 | 4,926.4 | 5,678.1 | 298.7 | 1.000x | 1.000x | 75 | 65.8 | 58.6 | 100% |

### `uuid-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.2 | 30.4 | 0.1 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 92.9 | 0.0001 | 92.5 | 106.5 | 5.5 | 3.060x | 3.060x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 296.4 | 0.0002 | 295.6 | 297.6 | 0.7 | 9.762x | 9.762x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 298.0 | 0.0002 | 295.2 | 310.9 | 5.5 | 9.814x | 9.814x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 11,852,271.0 | 8.6120 | 11,798,052.3 | 12,082,103.6 | 126,587.3 | 390308.738x | 390308.738x |

#### `uuid-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.8 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 9,040,378.2 | 8.6216 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.0 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.1 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,249,509.9 | 8.5812 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 30.9 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 119.6 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120.5 | 0.0018 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 568,955.0 | 8.6816 |

### `uuid-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 571.2 | 570.6 | 573.4 | 1.2 | 1.000x | 1.000x | 75 | 7.6 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,795.9 | 2,789.1 | 2,832.6 | 18.3 | 4.894x | 4.894x | 75 | 37.3 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 4,210.6 | 4,204.9 | 4,219.4 | 4.8 | 7.371x | 7.371x | 75 | 56.1 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 4,219.0 | 4,206.9 | 4,232.1 | 8.9 | 7.386x | 7.386x | 75 | 56.3 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,317.6 | 35,299.1 | 35,608.2 | 123.4 | 61.825x | 61.825x | 75 | 470.9 | 27.9 | 100% |

### `wild-codegrammar-json-array-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 123.7 | 0.0001 | 123.3 | 130.7 | 2.8 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 700,481.3 | 0.5090 | 699,694.8 | 701,083.4 | 462.3 | 5662.974x | 5662.974x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 1,646,513.1 | 1.1964 | 1,636,496.1 | 1,667,335.6 | 10,902.9 | 13311.078x | 13311.078x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 1,678,588.5 | 1.2197 | 1,676,557.8 | 1,734,706.8 | 23,283.9 | 13570.388x | 13570.388x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,979,405.4 | 2.8915 | 3,961,213.6 | 4,016,038.8 | 18,735.5 | 32171.122x | 32171.122x |

#### `wild-codegrammar-json-array-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 43.4 | 0.0000 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 536,650.7 | 0.5118 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,253,010.1 | 1.1950 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,278,705.9 | 1.2195 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,036,809.6 | 2.8961 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 40.8 | 0.0002 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 129,760.9 | 0.4950 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 303,050.1 | 1.1560 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 309,717.8 | 1.1815 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 749,430.8 | 2.8589 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 39.6 | 0.0006 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 34,158.4 | 0.5212 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 89,160.7 | 1.3605 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 91,062.7 | 1.3895 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 192,126.6 | 2.9316 |

### `wild-codegrammar-json-array-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,070.7 | 2,070.5 | 2,091.5 | 8.2 | 1.000x | 1.000x | 75 | 27.6 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,188.6 | 2,187.5 | 2,231.6 | 16.9 | 1.057x | 1.057x | 75 | 29.2 | 27.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,651.9 | 4,644.8 | 4,670.4 | 10.2 | 2.247x | 2.247x | 75 | 62.0 | 58.6 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,717.5 | 7,679.0 | 7,852.1 | 63.2 | 3.727x | 3.727x | 75 | 102.9 | 100.2 | 100% |
| 5 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,762.8 | 7,686.0 | 7,786.5 | 34.1 | 3.749x | 3.749x | 75 | 103.5 | 100.0 | 100% |

### `wild-codegrammar-json-constant` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 182,372.3 | 0.1325 | 182,184.6 | 182,847.2 | 228.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,238,720.3 | 1.6267 | 2,236,559.2 | 2,240,047.1 | 1,298.8 | 12.276x | 12.276x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,243,644.8 | 1.6303 | 2,239,152.6 | 2,246,551.6 | 2,777.3 | 12.303x | 12.303x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,560,019.1 | 4.7666 | 6,529,638.9 | 6,597,222.3 | 23,928.2 | 35.970x | 35.970x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 65,785,610.4 | 47.8004 | 65,379,510.0 | 66,622,055.2 | 427,936.0 | 360.722x | 360.722x |

#### `wild-codegrammar-json-constant` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 140,301.4 | 0.1338 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,698,688.4 | 1.6200 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,138.5 | 1.6223 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 4,983,004.7 | 4.7522 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 49,992,617.0 | 47.6767 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 33,779.6 | 0.1289 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,008.1 | 1.6175 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,564.3 | 1.6196 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 1,257,637.8 | 4.7975 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 12,527,788.4 | 47.7897 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 8,354.1 | 0.1275 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 115,557.4 | 1.7633 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,795.3 | 1.7669 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 319,376.6 | 4.8733 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,103,319.8 | 47.3529 |

### `wild-codegrammar-json-constant` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,001.9 | 2,988.6 | 3,184.7 | 75.8 | 1.000x | 1.000x | 75 | 40.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,591.6 | 9,574.0 | 9,786.1 | 79.1 | 3.195x | 3.195x | 75 | 127.9 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,675.3 | 9,629.7 | 9,830.8 | 72.9 | 3.223x | 3.223x | 75 | 129.0 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 13,350.6 | 13,280.3 | 13,525.0 | 91.5 | 4.447x | 4.447x | 75 | 178.0 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 63,627.0 | 63,295.5 | 64,097.1 | 321.6 | 21.195x | 21.195x | 75 | 848.4 | 27.9 | 100% |

### `wild-codegrammar-json-number-extended` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,494,350.5 | 17.0712 | 23,280,290.1 | 23,604,505.3 | 127,658.2 | 1.000x | 1.000x |

#### `wild-codegrammar-json-number-extended` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 17,976,793.7 | 17.1440 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,417,126.2 | 16.8500 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,067,112.0 | 16.2828 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-number-extended` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,694.2 | 11,660.0 | 11,771.9 | 39.3 | 1.000x | 1.000x | 75 | 155.9 | 58.6 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-object-begin` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: tre_0.9.0_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 23,248.6 | 0.0169 | 23,221.9 | 23,297.5 | 25.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 23,758.8 | 0.0173 | 23,741.2 | 23,773.9 | 10.7 | 1.022x | 1.022x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 23,779.2 | 0.0173 | 23,741.0 | 23,921.2 | 64.8 | 1.023x | 1.023x |
| 4 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 32,348.7 | 0.0235 | 32,334.6 | 32,456.4 | 45.3 | 1.391x | 1.391x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,819.3 | 1.6202 | 2,228,441.8 | 2,234,492.3 | 2,111.8 | 95.912x | 95.912x |

#### `wild-codegrammar-json-object-begin` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 17,668.5 | 0.0168 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 17,807.7 | 0.0170 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 17,811.9 | 0.0170 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 24,530.8 | 0.0234 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,260.2 | 1.6196 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,425.3 | 0.0169 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 4,498.6 | 0.0172 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 4,517.5 | 0.0172 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 6,137.7 | 0.0234 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,781.5 | 1.6204 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,142.1 | 0.0174 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 1,442.1 | 0.0220 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 1,447.6 | 0.0221 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,673.4 | 0.0255 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,412.0 | 1.6237 |

### `wild-codegrammar-json-object-begin` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,039.2 | 2,039.1 | 2,110.8 | 28.5 | 1.000x | 1.000x | 75 | 27.2 | 27.2 | 100% |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 2,092.1 | 2,090.5 | 2,098.4 | 2.8 | 1.026x | 1.026x | 75 | 27.9 | 27.9 | 100% |
| 3 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,397.9 | 4,392.6 | 4,978.2 | 232.0 | 2.157x | 2.157x | 75 | 58.6 | 58.6 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,514.9 | 7,501.4 | 7,526.1 | 8.4 | 3.685x | 3.685x | 75 | 100.2 | 100.0 | 100% |
| 5 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,537.7 | 7,511.6 | 7,601.8 | 34.2 | 3.696x | 3.696x | 75 | 100.5 | 100.2 | 100% |

### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,229,854.5 | 1.6202 | 2,228,571.0 | 2,231,481.9 | 1,163.2 | 1.000x | 1.000x |

#### `wild-codegrammar-json-stringcontent-escape` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,698,142.7 | 1.6195 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,827.6 | 1.6206 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,776.7 | 1.6293 |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-codegrammar-json-stringcontent-escape` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,047.9 | 5,034.5 | 5,145.9 | 43.2 | 1.000x | 1.000x | 75 | 67.3 | 58.6 | 100% |

- not ranked: `vectorscan_5.4.11_block-nosom-nocaps-simd` — did-not-compile (hs_compile failed (code -4, expression 0): Unterminated comment.)

### `wild-datetime-datefinder-alternation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 651.5 | 0.0005 | 650.6 | 688.1 | 14.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 909,418,994.0 | 660.7920 | 907,635,774.0 | 1,039,619,183.0 | 51,272,470.0 | 1395887.314x | 1395887.314x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 915,511,309.0 | 665.2188 | 899,467,753.0 | 951,066,994.0 | 20,860,808.5 | 1405238.543x | 1405238.543x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,137,713,544.0 | 1553.2819 | 2,120,757,817.0 | 2,480,947,384.0 | 139,483,497.6 | 3281223.768x | 3281223.768x |

#### `wild-datetime-datefinder-alternation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 209.4 | 0.0002 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 692,210,197.0 | 660.1431 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 690,401,889.0 | 658.4185 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,629,609,806.0 | 1554.1170 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 214.1 | 0.0008 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 172,709,917.0 | 658.8360 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 177,402,764.0 | 676.7378 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 406,240,412.0 | 1549.6842 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 228.4 | 0.0035 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 45,741,747.0 | 697.9637 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 47,559,525.0 | 725.7008 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 102,213,140.0 | 1559.6487 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-datefinder-alternation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,750.1 | 3,746.0 | 3,768.4 | 7.9 | 1.000x | 1.000x | 75 | 50.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 181,558.9 | 180,952.8 | 184,663.4 | 1,326.8 | 48.415x | 48.415x | 75 | 2,420.8 | 100.2 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 182,594.8 | 181,265.1 | 183,247.3 | 661.0 | 48.691x | 48.691x | 75 | 2,434.6 | 100.0 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 765,447.8 | 763,500.9 | 769,117.1 | 1,916.0 | 204.114x | 204.114x | 75 | 10,206.0 | 58.6 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-datetime-moment-iso8601` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 147.8 | 0.0001 | 146.9 | 149.4 | 0.8 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.2 | 0.0002 | 283.5 | 286.2 | 0.9 | 1.923x | 1.923x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 286.0 | 0.0002 | 283.6 | 287.3 | 1.5 | 1.935x | 1.935x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,006.4 | 0.0007 | 977.1 | 1,011.4 | 15.1 | 6.809x | 6.809x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,399,163.4 | 11.1892 | 15,380,043.9 | 15,520,233.5 | 50,750.5 | 104180.715x | 104180.715x |

#### `wild-datetime-moment-iso8601` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.0 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.6 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 306.0 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,717,792.7 | 11.1750 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.5 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.9 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 421.2 | 0.0016 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,947,490.3 | 11.2438 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 49.4 | 0.0008 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 106.9 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 108.0 | 0.0016 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 278.8 | 0.0043 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 741,816.5 | 11.3192 |

### `wild-datetime-moment-iso8601` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,619.0 | 1,618.0 | 1,627.6 | 4.1 | 1.000x | 1.000x | 75 | 21.6 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,707.2 | 9,570.5 | 9,770.3 | 66.1 | 5.996x | 5.996x | 75 | 129.4 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,737.3 | 9,714.3 | 9,793.3 | 28.8 | 6.015x | 6.015x | 75 | 129.8 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 11,656.5 | 11,611.5 | 11,871.9 | 92.7 | 7.200x | 7.200x | 75 | 155.4 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 42,417.2 | 42,355.6 | 42,457.1 | 37.4 | 26.200x | 26.200x | 75 | 565.6 | 27.9 | 100% |

### `wild-logparse-base10num-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 27,178,784.8 | 19.7483 | 27,101,937.3 | 27,960,581.0 | 351,977.7 | 1.000x | 1.000x |

#### `wild-logparse-base10num-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 20,814,145.0 | 19.8499 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 5,128,784.7 | 19.5648 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,235,855.1 | 18.8577 |

### `wild-logparse-base10num-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,893.4 | 15,772.3 | 16,188.7 | 147.3 | 1.000x | 1.000x | 75 | 211.9 | 58.6 | 100% |

### `wild-logparse-base10num-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 25,776,438.6 | 18.7294 | 25,756,114.0 | 26,331,673.2 | 219,154.1 | 1.000x | 1.000x |

#### `wild-logparse-base10num-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 19,738,679.8 | 18.8243 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 4,865,464.7 | 18.5603 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 1,176,568.6 | 17.9530 |

### `wild-logparse-base10num-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 15,951.5 | 15,869.6 | 16,015.9 | 51.1 | 1.000x | 1.000x | 75 | 212.7 | 58.6 | 100% |

### `wild-logparse-quotedstring-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,461,960.6 | 2.5155 | 3,446,127.4 | 3,504,453.5 | 20,710.8 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,646,841.7 | 2.5242 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 651,344.4 | 2.4847 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 163,774.5 | 2.4990 |

### `wild-logparse-quotedstring-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 6,263.0 | 6,260.9 | 6,298.7 | 14.1 | 1.000x | 1.000x | 75 | 83.5 | 58.6 | 100% |

### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,273,987.7 | 2.3789 | 3,251,490.0 | 3,319,012.3 | 27,398.1 | 1.000x | 1.000x |

#### `wild-logparse-quotedstring-noatomic` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,503,123.8 | 2.3872 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 616,205.0 | 2.3506 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 154,658.9 | 2.3599 |

### `wild-logparse-quotedstring-noatomic` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | set composition | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 290,745.7 | 290,281.8 | 291,145.7 | 305.9 | 1.000x | 1.000x | **dominated**: `waf-sleep` is 98.1% of this set | 75 | 3,876.6 | 58.6 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; `--grain subject` carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

_per-subject rows: 75 subjects — too many to enumerate here (the cap is 24); `--grain subject` renders them._

### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 69,561,405.2 | 50.5439 | 69,299,673.5 | 69,819,311.8 | 176,101.9 | 1.000x | 1.000x |

#### `wild-logparse-syslogbase-expanded` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 52,934,450.8 | 50.4822 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 13,301,012.5 | 50.7393 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,325,942.0 | 50.7498 |

### `wild-logparse-syslogbase-expanded` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 23,531.8 | 23,414.9 | 29,466.6 | 2,388.1 | 1.000x | 1.000x | 75 | 313.8 | 58.6 | 100% |

### `wild-logparse-winpath-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,676.0 | 1.6186 | 2,226,582.6 | 2,229,305.0 | 889.6 | 1.000x | 1.000x |

#### `wild-logparse-winpath-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,697,061.3 | 1.6184 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 423,987.4 | 1.6174 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,228.4 | 1.6209 |

### `wild-logparse-winpath-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,334.2 | 5,319.0 | 5,343.5 | 9.4 | 1.000x | 1.000x | 75 | 71.1 | 58.6 | 100% |

### `wild-secrets-aws-access-key-id` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 292,470.2 | 0.2125 | 292,421.7 | 293,292.6 | 326.1 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,170,961.4 | 1.5774 | 2,169,820.1 | 2,179,610.4 | 3,548.2 | 7.423x | 7.423x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,524.0 | 1.6294 | 2,232,468.3 | 2,249,970.6 | 6,088.5 | 7.668x | 7.668x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,243,681.0 | 1.6303 | 2,238,273.5 | 2,245,637.6 | 2,513.3 | 7.671x | 7.671x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 171,683,257.0 | 124.7466 | 169,849,352.0 | 175,041,292.0 | 1,713,375.3 | 587.011x | 587.011x |

#### `wild-secrets-aws-access-key-id` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 223,226.8 | 0.2129 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,654,190.0 | 1.5776 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,766.1 | 1.6220 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,702,109.9 | 1.6233 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 129,693,290.0 | 123.6852 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 55,299.2 | 0.2109 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 413,350.2 | 1.5768 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,913.0 | 1.6209 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,936.4 | 1.6210 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 33,407,033.5 | 127.4377 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 14,025.7 | 0.2140 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 103,737.3 | 1.5829 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,840.0 | 1.7676 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,584.6 | 1.7789 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 8,337,458.5 | 127.2195 |

### `wild-secrets-aws-access-key-id` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,103.2 | 2,101.5 | 2,103.9 | 0.8 | 1.000x | 1.000x | 75 | 28.0 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 7,520.6 | 7,471.6 | 7,646.6 | 60.5 | 3.576x | 3.576x | 75 | 100.3 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,973.3 | 9,874.5 | 10,122.7 | 80.9 | 4.742x | 4.742x | 75 | 133.0 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,979.6 | 9,886.8 | 10,145.8 | 92.6 | 4.745x | 4.745x | 75 | 133.1 | 100.0 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 175,424.2 | 174,489.4 | 176,594.3 | 670.7 | 83.409x | 83.409x | 75 | 2,339.0 | 27.9 | 100% |

### `wild-secrets-github-pat` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,324.7 | 0.0438 | 60,289.3 | 60,386.9 | 32.2 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 414,437.2 | 0.3011 | 414,185.1 | 414,945.7 | 275.2 | 6.870x | 6.870x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,237,686.3 | 1.6259 | 2,232,765.2 | 2,248,333.0 | 5,206.9 | 37.094x | 37.094x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,455.1 | 1.6279 | 2,238,769.5 | 2,242,236.5 | 1,165.9 | 37.140x | 37.140x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,061,868.5 | 18.2102 | 25,031,772.0 | 25,097,622.4 | 22,316.5 | 415.450x | 415.450x |

#### `wild-secrets-github-pat` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,871.9 | 0.0437 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 315,240.3 | 0.3006 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,698,287.0 | 1.6196 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,242.0 | 1.6205 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 19,100,497.7 | 18.2157 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,513.5 | 0.0439 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 79,025.4 | 0.3015 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,856.3 | 1.6169 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,936.9 | 1.6172 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,772,654.0 | 18.2062 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,943.6 | 0.0449 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 19,967.9 | 0.3047 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,663.1 | 1.7649 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,305.6 | 1.7747 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,195,404.2 | 18.2404 |

### `wild-secrets-github-pat` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 829.8 | 827.8 | 830.7 | 1.2 | 1.000x | 1.000x | 75 | 11.1 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,946.8 | 2,944.2 | 3,126.5 | 70.6 | 3.551x | 3.551x | 75 | 39.3 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,202.4 | 10,123.6 | 10,894.5 | 280.6 | 12.296x | 12.296x | 75 | 136.0 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,429.3 | 10,391.6 | 10,448.3 | 23.4 | 12.569x | 12.569x | 75 | 139.1 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 56,715.0 | 56,668.7 | 56,810.6 | 46.6 | 68.351x | 68.351x | 75 | 756.2 | 27.9 | 100% |

### `wild-secrets-slack-webhook-url` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 111,983.2 | 0.0814 | 111,928.7 | 112,443.5 | 193.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 439,089.5 | 0.3190 | 438,860.0 | 445,543.4 | 2,601.3 | 3.921x | 3.921x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,271.4 | 0.3192 | 438,875.8 | 440,274.8 | 578.7 | 3.923x | 3.923x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,249,951.7 | 0.9082 | 1,249,354.5 | 1,253,520.1 | 1,534.1 | 11.162x | 11.162x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 35,318,812.9 | 25.6630 | 35,181,012.1 | 35,437,962.2 | 90,841.4 | 315.394x | 315.394x |

#### `wild-secrets-slack-webhook-url` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 86,547.2 | 0.0825 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,778.6 | 0.3155 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,838.8 | 0.3155 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 952,392.2 | 0.9083 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 26,877,191.6 | 25.6321 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,573.4 | 0.0785 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,050.8 | 0.3168 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,950.5 | 0.3164 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 238,027.7 | 0.9080 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 6,750,774.0 | 25.7522 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,869.5 | 0.0743 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,376.0 | 0.3872 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,396.5 | 0.3875 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 59,189.1 | 0.9032 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,690,847.2 | 25.8003 |

### `wild-secrets-slack-webhook-url` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 694.3 | 692.5 | 695.1 | 0.9 | 1.000x | 1.000x | 75 | 9.3 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,356.6 | 3,349.3 | 3,396.8 | 21.5 | 4.835x | 4.835x | 75 | 44.8 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,973.5 | 8,882.4 | 8,990.2 | 38.4 | 12.925x | 12.925x | 75 | 119.6 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,022.2 | 9,017.5 | 9,109.4 | 35.1 | 12.995x | 12.995x | 75 | 120.3 | 100.0 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 74,743.8 | 74,724.7 | 74,852.3 | 46.4 | 107.654x | 107.654x | 75 | 996.6 | 27.9 | 100% |

### `wild-secrets-username-password-pair` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 475,056.4 | 0.3452 | 474,924.7 | 476,086.8 | 498.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,062.8 | 1.6291 | 2,235,212.0 | 2,251,360.1 | 5,962.2 | 4.720x | 4.720x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,243,308.2 | 1.6300 | 2,237,197.2 | 2,243,682.4 | 2,465.7 | 4.722x | 4.722x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,834,438.6 | 3.5127 | 4,831,155.3 | 4,839,506.2 | 2,855.6 | 10.177x | 10.177x |

#### `wild-secrets-username-password-pair` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 377,595.2 | 0.3601 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,819.0 | 1.6220 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,257.1 | 1.6215 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,671,783.4 | 3.5017 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 81,082.5 | 0.3093 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,139.2 | 1.6180 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,747.9 | 1.6203 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 926,455.9 | 3.5341 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,407.2 | 0.2504 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,104.5 | 1.7869 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 117,670.6 | 1.7955 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 235,656.2 | 3.5958 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-secrets-username-password-pair` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,647.4 | 1,645.7 | 1,683.2 | 14.6 | 1.000x | 1.000x | 75 | 22.0 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 9,033.7 | 9,020.1 | 9,165.9 | 54.3 | 5.484x | 5.484x | 75 | 120.4 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 10,284.5 | 10,263.4 | 10,490.6 | 83.2 | 6.243x | 6.243x | 75 | 137.1 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 10,351.6 | 10,345.8 | 10,484.8 | 53.4 | 6.284x | 6.284x | 75 | 138.0 | 100.2 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 153,409.3 | 0.1115 | 153,382.2 | 153,915.9 | 228.1 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 325,587.1 | 0.2366 | 325,329.5 | 329,401.9 | 1,540.9 | 2.122x | 2.122x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 326,198.2 | 0.2370 | 325,688.2 | 326,461.9 | 269.8 | 2.126x | 2.126x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,342,842.6 | 0.9757 | 1,341,850.0 | 1,343,793.8 | 709.0 | 8.753x | 8.753x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 28,598,173.3 | 20.7797 | 28,571,082.2 | 28,669,532.7 | 33,751.2 | 186.417x | 186.417x |

#### `wild-semdiv-altorder-foo-foobar-rustregex` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 116,853.5 | 0.1114 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 256,351.1 | 0.2445 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 256,644.6 | 0.2448 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,021,957.1 | 0.9746 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 21,772,259.9 | 20.7636 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 29,184.1 | 0.1113 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 54,864.4 | 0.2093 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 54,923.1 | 0.2095 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 256,264.2 | 0.9776 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,458,204.5 | 20.8214 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,382.0 | 0.1126 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 14,397.9 | 0.2197 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 14,769.9 | 0.2254 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 64,228.4 | 0.9800 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,371,465.0 | 20.9269 |

### `wild-semdiv-altorder-foo-foobar-rustregex` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,402.5 | 2,399.7 | 2,406.6 | 2.5 | 1.000x | 1.000x | 75 | 32.0 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,986.1 | 2,980.2 | 3,139.4 | 60.7 | 1.243x | 1.243x | 75 | 39.8 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,468.4 | 7,467.8 | 7,469.7 | 0.7 | 3.109x | 3.109x | 75 | 99.6 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,488.0 | 7,485.2 | 8,133.2 | 256.2 | 3.117x | 3.117x | 75 | 99.8 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,912.2 | 30,851.3 | 31,201.5 | 129.0 | 12.867x | 12.867x | 75 | 412.2 | 27.9 | 100% |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 151.3 | 0.0001 | 151.1 | 151.4 | 0.1 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 223.3 | 0.0002 | 223.2 | 226.0 | 1.1 | 1.476x | 1.476x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 316.3 | 0.0002 | 314.8 | 317.6 | 0.9 | 2.091x | 2.091x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 316.7 | 0.0002 | 314.8 | 317.9 | 1.1 | 2.093x | 2.093x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 18,567,140.7 | 13.4911 | 18,541,650.5 | 18,620,515.0 | 27,681.4 | 122732.600x | 122732.600x |

#### `wild-semdiv-dollar-trailing-newline-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 50.3 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 73.9 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 99.3 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 98.9 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 14,152,979.8 | 13.4973 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0002 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75.1 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 98.6 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 98.5 | 0.0004 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 3,533,333.7 | 13.4786 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 50.4 | 0.0008 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.3 | 0.0011 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 118.5 | 0.0018 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 118.6 | 0.0018 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 887,617.8 | 13.5440 |

### `wild-semdiv-dollar-trailing-newline-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,760.9 | 2,757.8 | 2,771.5 | 4.9 | 1.000x | 1.000x | 75 | 36.8 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,474.2 | 3,455.8 | 3,477.2 | 7.8 | 1.258x | 1.258x | 75 | 46.3 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 7,307.4 | 7,292.6 | 7,337.8 | 17.1 | 2.647x | 2.647x | 75 | 97.4 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 7,330.5 | 7,308.9 | 7,360.6 | 17.5 | 2.655x | 2.655x | 75 | 97.7 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 12,695.1 | 12,681.5 | 12,722.7 | 14.5 | 4.598x | 4.598x | 75 | 169.3 | 27.9 | 100% |

### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 241.4 | 0.0002 | 241.2 | 242.3 | 0.4 | 1.000x | 1.000x |
| 2 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 47,010,275.2 | 34.1581 | 46,709,688.3 | 48,495,435.3 | 659,963.6 | 194725.238x | 194725.238x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 62,962,198.6 | 45.7489 | 62,490,547.6 | 64,109,606.2 | 587,533.6 | 260801.049x | 260801.049x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 65,721,547.2 | 47.7539 | 65,413,297.6 | 66,673,090.8 | 460,939.9 | 272230.780x | 272230.780x |
| 5 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 99,913,182.7 | 72.5978 | 99,339,699.3 | 101,624,659.3 | 801,474.7 | 413858.846x | 413858.846x |

#### `wild-semdiv-empty-alt-repeat-pcre2` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 83.5 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 35,802,428.7 | 34.1439 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 48,064,878.0 | 45.8382 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 50,273,919.2 | 47.9449 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 76,132,659.0 | 72.6058 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 78.7 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 8,933,194.8 | 34.0774 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 11,936,399.0 | 45.5337 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 12,335,622.0 | 47.0567 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 18,924,162.3 | 72.1900 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 79.4 | 0.0012 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,213,087.8 | 33.7690 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 2,984,221.8 | 45.5356 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 3,112,006.0 | 47.4854 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 4,643,146.7 | 70.8488 |

### `wild-semdiv-empty-alt-repeat-pcre2` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,892.4 | 3,886.7 | 4,064.4 | 69.3 | 1.000x | 1.000x | 75 | 51.9 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 17,362.3 | 17,081.7 | 17,567.5 | 185.8 | 4.461x | 4.461x | 75 | 231.5 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 19,842.2 | 19,706.9 | 20,006.7 | 107.8 | 5.098x | 5.098x | 75 | 264.6 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 19,913.7 | 19,739.3 | 20,174.9 | 153.4 | 5.116x | 5.116x | 75 | 265.5 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 31,343.3 | 31,278.0 | 31,451.9 | 63.8 | 8.052x | 8.052x | 75 | 417.9 | 27.9 | 100% |

### `wild-validator-email-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 199.8 | 0.0001 | 195.6 | 202.2 | 2.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 374.4 | 0.0003 | 369.5 | 382.0 | 4.1 | 1.874x | 1.874x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 384.4 | 0.0003 | 381.4 | 390.1 | 3.3 | 1.924x | 1.924x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,227,440.6 | 1.6185 | 2,226,539.7 | 2,234,098.7 | 2,758.3 | 11150.138x | 11150.138x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 21,848,026.8 | 15.8750 | 21,070,678.2 | 22,350,250.6 | 561,505.5 | 109367.009x | 109367.009x |

#### `wild-validator-email-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 74.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 114.4 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 112.8 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,696,947.3 | 1.6183 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 16,513,572.8 | 15.7486 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 61.3 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 101.2 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 102.7 | 0.0004 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 424,200.4 | 1.6182 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 4,258,051.2 | 16.2432 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 63.3 | 0.0010 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 155.5 | 0.0024 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 170.1 | 0.0026 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 106,439.2 | 1.6241 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,069,530.3 | 16.3197 |

### `wild-validator-email-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,247.0 | 2,244.2 | 2,268.6 | 9.0 | 1.000x | 1.000x | 75 | 30.0 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 5,227.7 | 5,218.6 | 5,288.9 | 25.3 | 2.327x | 2.327x | 75 | 69.7 | 58.6 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,127.5 | 8,103.7 | 8,180.7 | 25.8 | 3.617x | 3.617x | 75 | 108.4 | 100.2 | 100% |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,136.0 | 8,100.5 | 9,032.2 | 364.7 | 3.621x | 3.621x | 75 | 108.5 | 100.0 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 120,423.0 | 120,382.5 | 120,919.3 | 216.9 | 53.592x | 53.592x | 75 | 1,605.6 | 27.9 | 100% |

### `wild-validator-ipv4-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.4 | 0.0000 | 30.3 | 36.4 | 2.9 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.8 | 0.0002 | 284.4 | 285.2 | 0.3 | 9.376x | 9.376x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 285.8 | 0.0002 | 285.4 | 288.2 | 1.1 | 9.406x | 9.406x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 367.4 | 0.0003 | 367.0 | 389.5 | 9.6 | 12.093x | 12.093x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 15,399,526.6 | 11.1894 | 15,387,074.9 | 15,427,381.2 | 16,185.8 | 506887.114x | 506887.114x |

#### `wild-validator-ipv4-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 89.0 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 299.2 | 0.0003 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 11,726,477.1 | 11.1832 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0000 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 88.4 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 89.3 | 0.0003 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 34.1 | 0.0001 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 2,937,226.4 | 11.2046 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0002 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 109.0 | 0.0017 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 34.6 | 0.0005 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 740,877.6 | 11.3049 |

### `wild-validator-ipv4-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 950.7 | 949.6 | 952.6 | 1.1 | 1.000x | 1.000x | 75 | 12.7 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,661.5 | 3,588.6 | 3,824.5 | 85.0 | 3.851x | 3.851x | 75 | 48.8 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,317.1 | 9,277.2 | 9,366.3 | 29.0 | 9.801x | 9.801x | 75 | 124.2 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,420.2 | 9,330.1 | 10,128.7 | 293.5 | 9.909x | 9.909x | 75 | 125.6 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 38,827.5 | 38,585.4 | 39,030.0 | 152.6 | 40.842x | 40.842x | 75 | 517.7 | 27.9 | 100% |

### `wild-validator-us-zip-owasp` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 30.3 | 0.0000 | 30.3 | 30.4 | 0.1 | 1.000x | 1.000x |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.8 | 0.0001 | 94.3 | 95.0 | 0.3 | 3.130x | 3.130x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 284.8 | 0.0002 | 283.4 | 304.4 | 8.0 | 9.400x | 9.400x |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 284.9 | 0.0002 | 283.1 | 291.6 | 3.2 | 9.404x | 9.404x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 8,693,894.0 | 6.3171 | 8,660,192.5 | 8,703,324.0 | 15,746.7 | 286943.036x | 286943.036x |

#### `wild-validator-us-zip-owasp` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.0 | 0.0000 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 88.5 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 88.1 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 6,621,152.4 | 6.3144 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.1 | 0.0000 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0001 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 89.2 | 0.0003 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 88.2 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,652,694.0 | 6.3045 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10.2 | 0.0002 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.7 | 0.0005 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 107.5 | 0.0016 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 108.5 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 414,860.8 | 6.3303 |

### `wild-validator-us-zip-owasp` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 986.3 | 984.0 | 1,176.3 | 76.2 | 1.000x | 1.000x | 75 | 13.2 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,038.4 | 2,033.8 | 2,042.1 | 3.0 | 2.067x | 2.067x | 75 | 27.2 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,046.0 | 2,040.1 | 2,094.7 | 20.2 | 2.074x | 2.074x | 75 | 27.3 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,915.5 | 4,906.6 | 4,989.0 | 31.9 | 4.984x | 4.984x | 75 | 65.5 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 13,921.2 | 13,916.7 | 13,933.6 | 7.2 | 14.114x | 14.114x | 75 | 185.6 | 27.9 | 100% |

### `wild-validator-uuid-grok` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 243,490.9 | 0.1769 | 243,334.2 | 245,883.2 | 970.7 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,235,844.8 | 1.6246 | 2,231,352.6 | 2,251,497.0 | 7,159.8 | 9.182x | 9.182x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,238,842.2 | 1.6268 | 2,233,817.2 | 2,242,387.3 | 2,999.4 | 9.195x | 9.195x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,420,629.7 | 1.7589 | 2,415,306.8 | 2,421,702.7 | 2,248.5 | 9.941x | 9.941x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 72,489,213.0 | 52.6713 | 69,753,004.8 | 72,506,743.0 | 1,072,793.8 | 297.708x | 297.708x |

#### `wild-validator-uuid-grok` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 185,930.3 | 0.1773 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,697,309.3 | 1.6187 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,699,652.9 | 1.6209 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,844,193.1 | 1.7588 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 55,175,180.5 | 52.6192 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 46,122.8 | 0.1759 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,178.7 | 1.6143 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 423,680.1 | 1.6162 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 459,146.5 | 1.7515 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 13,731,436.5 | 52.3813 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,429.7 | 0.1744 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,008.7 | 1.7702 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,210.7 | 1.7732 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 116,148.1 | 1.7723 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 3,434,615.0 | 52.4081 |

### `wild-validator-uuid-grok` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,625.9 | 1,623.3 | 1,676.5 | 20.6 | 1.000x | 1.000x | 75 | 21.7 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,236.0 | 4,226.9 | 4,290.4 | 22.8 | 2.605x | 2.605x | 75 | 56.5 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,815.1 | 9,755.0 | 10,362.4 | 227.8 | 6.037x | 6.037x | 75 | 130.9 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,878.0 | 9,848.5 | 9,913.1 | 25.6 | 6.075x | 6.075x | 75 | 131.7 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 121,919.5 | 119,770.2 | 122,253.0 | 1,004.8 | 74.985x | 74.985x | 75 | 1,625.6 | 27.9 | 100% |

### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 600,337.0 | 0.4362 | 600,029.2 | 600,994.4 | 346.0 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,242,325.2 | 1.6293 | 2,238,906.8 | 2,279,953.9 | 15,483.7 | 3.735x | 3.735x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,242,907.8 | 1.6297 | 2,233,106.6 | 2,248,494.0 | 5,092.6 | 3.736x | 3.736x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 65,241,237.2 | 47.4049 | 65,024,447.8 | 65,398,824.0 | 130,718.7 | 108.674x | 108.674x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 285,325,096.0 | 207.3198 | 280,193,756.0 | 292,484,487.0 | 4,023,104.3 | 475.275x | 475.275x |

#### `wild-waf-crs-942140-dbnames` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 477,905.1 | 0.4558 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,701,966.1 | 1.6231 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,700,838.2 | 1.6220 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 49,703,089.0 | 47.4006 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 218,465,690.0 | 208.3451 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 101,807.6 | 0.3884 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,128.7 | 1.6179 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 424,466.9 | 1.6192 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 12,403,551.6 | 47.3158 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 52,845,094.0 | 201.5880 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 20,492.4 | 0.3127 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 116,723.8 | 1.7811 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 117,046.2 | 1.7860 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 3,115,774.6 | 47.5429 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 13,182,896.0 | 201.1550 |

### `wild-waf-crs-942140-dbnames` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 3,412.9 | 3,406.4 | 3,884.5 | 185.7 | 1.000x | 1.000x | 75 | 45.5 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,646.5 | 9,614.1 | 9,955.4 | 126.6 | 2.827x | 2.827x | 75 | 128.6 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,704.5 | 9,670.3 | 9,716.5 | 19.7 | 2.844x | 2.844x | 75 | 129.4 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 44,816.7 | 44,752.1 | 45,046.3 | 113.0 | 13.132x | 13.132x | 75 | 597.6 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 319,759.1 | 318,703.8 | 327,037.0 | 3,126.0 | 93.692x | 93.692x | 75 | 4,263.5 | 27.9 | 100% |

### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 160,217.0 | 0.1164 | 160,176.6 | 160,496.2 | 119.3 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,240,147.2 | 1.6277 | 2,235,744.2 | 2,248,140.7 | 4,055.5 | 13.982x | 13.982x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,240,941.6 | 1.6283 | 2,231,147.1 | 2,244,189.0 | 5,263.1 | 13.987x | 13.987x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 4,911,042.9 | 3.5684 | 4,900,030.2 | 5,814,985.9 | 362,499.5 | 30.652x | 30.652x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 60,079,000.4 | 43.6539 | 60,068,762.4 | 60,187,309.0 | 44,431.7 | 374.985x | 374.985x |

#### `wild-waf-crs-942160-sleep-benchmark` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 122,101.2 | 0.1164 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,699,881.0 | 1.6211 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,204.9 | 1.6214 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 3,729,683.1 | 3.5569 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 45,759,910.0 | 43.6401 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 30,347.6 | 0.1158 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 425,758.3 | 1.6241 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,759.7 | 1.6203 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 934,212.4 | 3.5637 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 11,430,437.8 | 43.6037 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 7,761.9 | 0.1184 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 116,562.9 | 1.7786 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 115,976.9 | 1.7697 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 246,550.1 | 3.7621 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 2,878,786.6 | 43.9268 |

### `wild-waf-crs-942160-sleep-benchmark` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,420.3 | 2,418.3 | 2,429.3 | 4.3 | 1.000x | 1.000x | 75 | 32.3 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,593.2 | 9,575.7 | 9,772.1 | 73.2 | 3.964x | 3.964x | 75 | 127.9 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,839.2 | 9,633.0 | 9,944.0 | 116.6 | 4.065x | 4.065x | 75 | 131.2 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 12,477.7 | 12,460.1 | 12,509.0 | 18.6 | 5.156x | 5.156x | 75 | 166.4 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 71,099.8 | 71,064.5 | 71,109.6 | 18.5 | 29.377x | 29.377x | 75 | 948.0 | 27.9 | 100% |

### `wild-waf-crs-942270-union-select` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 86,366.8 | 0.0628 | 86,279.7 | 86,983.2 | 253.6 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 438,865.4 | 0.3189 | 438,743.8 | 440,523.7 | 661.7 | 5.081x | 5.081x |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,102.4 | 0.3191 | 438,451.0 | 439,565.5 | 453.0 | 5.084x | 5.084x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,425,857.9 | 2.4893 | 3,423,977.2 | 3,427,078.8 | 1,119.1 | 39.666x | 39.666x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 30,936,396.2 | 22.4787 | 30,884,965.9 | 30,998,074.3 | 42,965.4 | 358.198x | 358.198x |

#### `wild-waf-crs-942270-union-select` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 65,811.0 | 0.0628 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,714.0 | 0.3154 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,683.7 | 0.3154 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 2,603,920.7 | 2.4833 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 23,551,311.4 | 22.4603 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 16,405.2 | 0.0626 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,169.4 | 0.3173 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,967.9 | 0.3165 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 655,621.8 | 2.5010 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 5,897,141.8 | 22.4958 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,147.7 | 0.0633 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,110.2 | 0.3832 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 24,987.5 | 0.3813 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 166,324.6 | 2.5379 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 1,481,358.6 | 22.6037 |

### `wild-waf-crs-942270-union-select` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,914.2 | 1,910.3 | 1,918.6 | 3.2 | 1.000x | 1.000x | 75 | 25.5 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,258.9 | 8,245.2 | 8,906.9 | 260.5 | 4.314x | 4.314x | 75 | 110.1 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,310.8 | 8,282.6 | 8,584.9 | 130.5 | 4.342x | 4.342x | 75 | 110.8 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 8,755.4 | 8,743.4 | 8,820.1 | 28.2 | 4.574x | 4.574x | 75 | 116.7 | 58.6 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 39,239.9 | 39,205.5 | 39,338.8 | 48.7 | 20.499x | 20.499x | 75 | 523.2 | 27.9 | 100% |

### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 878,263.5 | 0.6382 | 875,941.9 | 880,883.5 | 1,594.2 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 2,245,698.0 | 1.6317 | 2,237,409.5 | 2,249,579.8 | 4,827.9 | 2.557x | 2.557x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 2,246,279.2 | 1.6322 | 2,238,966.4 | 2,249,444.7 | 3,694.4 | 2.558x | 2.558x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 138,553,761.5 | 100.6744 | 138,270,549.0 | 153,899,022.5 | 6,138,875.5 | 157.759x | 157.759x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 1,169,517,671.0 | 849.7821 | 1,160,081,936.0 | 1,177,845,858.0 | 7,268,394.2 | 1331.625x | 1331.625x |

#### `wild-waf-crs-942360-concat-sqli` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 700,812.1 | 0.6683 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 1,700,934.9 | 1.6221 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 1,701,537.2 | 1.6227 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 105,556,164.5 | 100.6662 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 887,301,449.0 | 846.1966 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 149,157.3 | 0.5690 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 424,753.7 | 1.6203 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 423,991.9 | 1.6174 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 26,400,943.5 | 100.7116 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 223,480,342.0 | 852.5098 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 28,185.7 | 0.4301 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 120,039.4 | 1.8317 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 120,903.2 | 1.8448 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 6,596,653.5 | 100.6569 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 55,721,623.0 | 850.2445 |

### `wild-waf-crs-942360-concat-sqli` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 4,575.5 | 4,558.2 | 4,581.3 | 9.6 | 1.000x | 1.000x | 75 | 61.0 | 27.2 | 100% |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 9,560.4 | 9,526.6 | 9,772.6 | 90.6 | 2.089x | 2.089x | 75 | 127.5 | 100.0 | 100% |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 9,625.2 | 9,613.1 | 9,639.8 | 9.1 | 2.104x | 2.104x | 75 | 128.3 | 100.2 | 100% |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 142,711.4 | 142,421.2 | 142,970.4 | 186.6 | 31.191x | 31.191x | 75 | 1,902.8 | 58.6 | 100% |

### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 60,231.1 | 0.0438 | 60,206.6 | 60,404.6 | 71.4 | 1.000x | 1.000x |
| 2 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 439,015.7 | 0.3190 | 438,764.7 | 439,629.1 | 303.0 | 7.289x | 7.289x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 440,033.2 | 0.3197 | 439,026.3 | 440,551.3 | 514.3 | 7.306x | 7.306x |
| 4 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 1,498,130.6 | 1.0886 | 1,497,611.9 | 1,500,676.9 | 1,094.7 | 24.873x | 24.873x |

#### `wild-waf-crs-942500-comment-obfuscation` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 45,839.1 | 0.0437 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 330,824.6 | 0.3155 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 330,973.4 | 0.3156 |
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 1,141,170.5 | 1.0883 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 11,470.4 | 0.0438 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 82,924.3 | 0.3163 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 83,098.3 | 0.3170 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 285,299.8 | 1.0883 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,937.5 | 0.0448 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 25,198.4 | 0.3845 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 25,263.2 | 0.3855 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 71,488.8 | 1.0908 |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `wild-waf-crs-942500-comment-obfuscation` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 2,358.9 | 2,352.4 | 2,360.9 | 3.5 | 1.000x | 1.000x | 75 | 31.5 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 3,885.2 | 3,875.5 | 3,914.5 | 13.9 | 1.647x | 1.647x | 75 | 51.8 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 8,261.6 | 8,228.9 | 8,317.2 | 30.5 | 3.502x | 3.502x | 75 | 110.2 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 8,296.2 | 8,234.9 | 8,726.7 | 197.1 | 3.517x | 3.517x | 75 | 110.6 | 100.2 | 100% |

- not ranked: `tre_0.9.0_default-caps-simdna` — did-not-compile (tre_regncompb failed (code 11): Invalid character range)

### `winpath-near-miss` / `large-subject-throughput` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: oniguruma_6.9.10_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 94.2 | 0.0001 | 93.4 | 111.8 | 7.1 | 1.000x | 1.000x |
| 2 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 133.2 | 0.0001 | 133.0 | 135.0 | 0.8 | 1.414x | 1.414x |
| 3 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 294.5 | 0.0002 | 292.2 | 300.8 | 2.9 | 3.126x | 3.126x |
| 4 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 296.9 | 0.0002 | 292.2 | 328.1 | 13.2 | 3.151x | 3.151x |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 10,188,297.9 | 7.4029 | 10,184,252.9 | 10,202,429.7 | 6,911.6 | 108123.958x | 108123.958x |

#### `winpath-near-miss` / `large-subject-throughput` per-subject (capability@0.1)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-1m` | 1,048,576 | `oniguruma_6.9.10_default-caps-simdna` | 31.5 | 0.0000 |
| `t-1m` | 1,048,576 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0000 |
| `t-1m` | 1,048,576 | `re2_11.0.0_longest-caps-simdna` | 90.8 | 0.0001 |
| `t-1m` | 1,048,576 | `re2_11.0.0_default-caps-simdna` | 91.2 | 0.0001 |
| `t-1m` | 1,048,576 | `tre_0.9.0_default-caps-simdna` | 7,756,780.5 | 7.3974 |
| `t-256k` | 262,144 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0001 |
| `t-256k` | 262,144 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.3 | 0.0002 |
| `t-256k` | 262,144 | `re2_11.0.0_longest-caps-simdna` | 92.1 | 0.0004 |
| `t-256k` | 262,144 | `re2_11.0.0_default-caps-simdna` | 91.3 | 0.0003 |
| `t-256k` | 262,144 | `tre_0.9.0_default-caps-simdna` | 1,943,261.2 | 7.4130 |
| `t-64k` | 65,536 | `oniguruma_6.9.10_default-caps-simdna` | 31.2 | 0.0005 |
| `t-64k` | 65,536 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 44.6 | 0.0007 |
| `t-64k` | 65,536 | `re2_11.0.0_longest-caps-simdna` | 112.0 | 0.0017 |
| `t-64k` | 65,536 | `re2_11.0.0_default-caps-simdna` | 112.2 | 0.0017 |
| `t-64k` | 65,536 | `tre_0.9.0_default-caps-simdna` | 485,957.0 | 7.4151 |

### `winpath-near-miss` / `short-subject-search` (capability@0.1) — baseline: libpcre2 engine_mode=interp

- baseline: vectorscan_5.4.11_block-nosom-nocaps-simd (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | measured | `plain` | same program | 1,463.5 | 1,462.9 | 1,468.1 | 1.9 | 1.000x | 1.000x | 75 | 19.5 | 27.2 | 100% |
| 2 | `oniguruma_6.9.10_default-caps-simdna` | measured | `plain` | same program | 2,927.0 | 2,925.5 | 4,037.8 | 443.9 | 2.000x | 2.000x | 75 | 39.0 | 58.6 | 100% |
| 3 | `re2_11.0.0_default-caps-simdna` | measured | `plain` | same program | 6,942.1 | 6,899.2 | 6,954.6 | 20.1 | 4.743x | 4.743x | 75 | 92.6 | 100.0 | 100% |
| 4 | `re2_11.0.0_longest-caps-simdna` | measured | `plain` | same program | 6,946.4 | 6,875.9 | 6,965.2 | 33.8 | 4.746x | 4.746x | 75 | 92.6 | 100.2 | 100% |
| 5 | `tre_0.9.0_default-caps-simdna` | measured | `plain` | same program | 25,964.7 | 25,866.3 | 25,973.8 | 40.3 | 17.741x | 17.741x | 75 | 346.2 | 27.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `evil-alt-nested` | `short-subject-search` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 75 | 97% | -17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B) | 0 | `rd-evil-alt-near-miss` (gave-up), `sd-empty-alt-hit` (gave-up) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_default-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `evil-alt-nested` | `short-subject-search` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 75 | 97% | 0 | 0 | `rd-evil-alt-near-miss` (no-expectation), `sd-empty-alt-hit` (no-expectation) |
| `file-ext-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `file-ext-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-fileext-short` (wrong) |
| `high-byte-run` | `large-subject-throughput` | `plain` | `tre_0.9.0_default-caps-simdna` | 3 | 0% | 0 | 15 | `t-1m` (wrong), `t-256k` (wrong), `t-64k` (wrong) |
| `high-byte-run` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 48% | 0 | 195 | `br-dup-param` (wrong), `br-palindrome` (wrong), `cg-number` (wrong), `dt-iso8601` (wrong), `dt-prose-month` (wrong), `la-currency` (wrong), `la-float-bound` (wrong), `la-float-dotted` (wrong), `la-pwd-strong` (wrong), `la-pwd-weak` (wrong), `lp-num-leadzero` (wrong), `lp-num-neg-dec` (wrong), `lp-syslog` (wrong), `lp-winpath` (wrong), `lp-winpath-reserved` (wrong), `nu-high-byte` (wrong), `nu-lead-with-cont` (wrong), `rd-date-hit` (wrong), `rd-email-hit` (wrong), `rd-numeric-id-hit` (wrong), `rd-numeric-id-near-miss` (wrong), `rd-phone-list-hit` (wrong), `rec-array-define` (wrong), `rec-tag-depth3` (wrong), `sec-aws-key` (wrong), `sec-github-pat` (wrong), `sec-slack-webhook` (wrong), `v-ipv4` (wrong), `v-ipv4-oor` (wrong), `v-us-zip` (wrong), `v-us-zip-plus4` (wrong), `v-uuid-badnibble` (wrong), `v-uuid-valid` (wrong), `waf-benign` (wrong), `waf-comment-obfuscation` (wrong), `waf-concat` (wrong), `waf-dbnames` (wrong), `waf-sleep` (wrong), `waf-union` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `keyword-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-keyword-short` (wrong) |
| `mojibake-curly-quote` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `nu-mojibake` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `re2_11.0.0_longest-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `router-prefix-order` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `sd-router-short` (wrong) |
| `tag-pair-match` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `br-tag-pair` (wrong) |
| `wild-waf-crs-942360-concat-sqli` | `short-subject-search` | `plain` | `tre_0.9.0_default-caps-simdna` | 75 | 99% | 0 | 5 | `waf-union` (wrong) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `balanced-parens-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 24,610.0 | 19,340.0 | 133,480.0 | 44,048.9 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 25,250.0 | 19,031.0 | 139,081.0 | 46,269.9 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,194,337.0 | 1,166,216.0 | 1,725,750.0 | 216,201.7 | 5 | 5,896 | 0.181 (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,169,149.0 | 3,050,348.0 | 4,332,666.0 | 481,935.2 | 5 | 6,376 | 0.152 (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `bracket-array-define` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `re2_11.0.0_default-caps-simdna` | 11,460.0 | 8,670.0 | 64,971.0 | 21,685.9 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `re2_11.0.0_longest-caps-simdna` | 11,420.0 | 8,470.0 | 68,121.0 | 22,619.6 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,413,448.0 | 1,351,818.0 | 2,562,365.0 | 470,035.8 | 5 | 6,088 | 0.333 (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,807,461.0 | 1,796,850.0 | 2,968,267.0 | 464,156.2 | 5 | 3,672 | 0.257 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-xflag` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-xflag` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,422,798.0 | 1,385,668.0 | 2,551,535.0 | 455,208.7 | 5 | 6,088 | 0.320 (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,831,490.0 | 1,773,290.0 | 3,006,588.0 | 479,838.3 | 5 | 3,672 | 0.262 (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,620.0 | 14,490.0 | 113,791.0 | 38,073.1 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 18,861.0 | 14,570.0 | 119,600.0 | 40,228.5 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,096,036.0 | 1,051,396.0 | 2,110,532.0 | 407,941.7 | 5 | 5,736 | 0.372 (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 469,693.0 | 447,242.0 | 948,615.0 | 191,335.9 | 5 | 6,024 | 0.407 (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `doubled-word` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `dup-param-detect` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-local-nodup` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 22,140.0 | 16,380.0 | 126,071.0 | 42,139.4 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 21,780.0 | 15,990.0 | 129,080.0 | 43,309.4 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 578,563.0 | 538,383.0 | 1,525,299.0 | 383,394.6 | 5 | 5,784 | 0.663 (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 361,253.0 | 328,151.0 | 833,125.0 | 193,562.5 | 5 | 6,232 | 0.536 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `re2_11.0.0_default-caps-simdna` | 13,140.0 | 10,590.0 | 123,710.0 | 43,865.0 | 5 | 9 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `re2_11.0.0_longest-caps-simdna` | 13,930.0 | 10,670.0 | 100,461.0 | 34,470.2 | 5 | 9 | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 608,863.0 | 574,464.0 | 1,535,579.0 | 371,526.6 | 5 | 5,704 | 0.610 (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 291,391.0 | 280,012.0 | 750,635.0 | 182,093.3 | 5 | 5,992 | 0.625 (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 15,890.0 | 12,460.0 | 142,391.0 | 50,685.9 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,041.0 | 11,110.0 | 88,960.0 | 30,220.4 | 5 | 12 | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 494,503.0 | 455,283.0 | 1,387,608.0 | 359,149.4 | 5 | 4,776 | 0.726 (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 237,622.0 | 221,851.0 | 634,834.0 | 161,485.6 | 5 | 2,120 | 0.680 (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `float-literal-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `re2_11.0.0_default-caps-simdna` | 4,900.0 | 4,060.0 | 98,990.0 | 37,644.8 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `re2_11.0.0_longest-caps-simdna` | 4,760.0 | 4,030.0 | 91,811.0 | 34,805.4 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 103,731.0 | 91,981.0 | 522,643.0 | 169,018.2 | 5 | 936 | 1.629 (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 133,121.0 | 124,381.0 | 511,173.0 | 152,157.8 | 5 | 1,704 | 1.143 (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `re2_11.0.0_default-caps-simdna` | 12,180.0 | 9,740.0 | 100,651.0 | 35,508.4 | 5 | 10 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `re2_11.0.0_longest-caps-simdna` | 12,360.0 | 9,840.0 | 100,701.0 | 35,432.9 | 5 | 10 | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 568,943.0 | 520,854.0 | 1,469,139.0 | 365,859.2 | 5 | 5,784 | 0.643 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 203,131.0 | 190,371.0 | 583,713.0 | 153,104.9 | 5 | 1,832 | 0.754 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 26,890.0 | 24,000.0 | 92,910.0 | 26,532.2 | 5 | 49 | 0.987 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 67,901.0 | 59,880.0 | 218,232.0 | 60,658.9 | 5 | 49 | 0.893 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,184,652.0 | 2,134,743.0 | 3,340,609.0 | 465,884.8 | 5 | 3,464 | 0.213 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 906,435.0 | 890,285.0 | 1,452,788.0 | 219,242.3 | 5 | 2,824 | 0.242 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 20,700.0 | 13,600.0 | 108,050.0 | 35,478.1 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,800.0 | 12,190.0 | 101,851.0 | 34,893.8 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 549,553.0 | 518,183.0 | 1,443,219.0 | 360,503.0 | 5 | 4,840 | 0.656 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 249,611.0 | 244,421.0 | 650,434.0 | 158,955.0 | 5 | 2,504 | 0.637 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `re2_11.0.0_default-caps-simdna` | 66,741.0 | 59,501.0 | 200,041.0 | 53,703.5 | 5 | 80 | 0.805 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `re2_11.0.0_longest-caps-simdna` | 66,010.0 | 58,090.0 | 201,821.0 | 54,787.5 | 5 | 80 | 0.830 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,763,782.0 | 3,727,402.0 | 4,499,836.0 | 299,987.3 | 5 | 10,168 | 0.080 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,838,233.0 | 3,421,549.0 | 10,199,788.0 | 2,816,437.9 | 5 | 9,496 | 0.734 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `re2_11.0.0_default-caps-simdna` | 10,830.0 | 8,540.0 | 95,831.0 | 34,142.5 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `re2_11.0.0_longest-caps-simdna` | 10,620.0 | 8,510.0 | 100,841.0 | 36,192.8 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 734,115.0 | 710,004.0 | 1,750,660.0 | 406,865.8 | 5 | 5,992 | 0.554 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 439,453.0 | 417,652.0 | 943,926.0 | 204,685.6 | 5 | 3,352 | 0.466 (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 11,860.0 | 8,790.0 | 98,441.0 | 34,907.9 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 10,890.0 | 8,190.0 | 99,711.0 | 35,703.5 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 816,645.0 | 807,305.0 | 1,876,080.0 | 421,777.9 | 5 | 5,704 | 0.516 (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 365,082.0 | 349,612.0 | 819,465.0 | 184,524.5 | 5 | 5,992 | 0.505 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `re2_11.0.0_default-caps-simdna` | 18,190.0 | 14,150.0 | 111,240.0 | 37,114.8 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `re2_11.0.0_longest-caps-simdna` | 17,700.0 | 13,260.0 | 106,140.0 | 35,403.9 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 967,505.0 | 951,206.0 | 1,969,511.0 | 398,173.3 | 5 | 5,736 | 0.412 (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 407,172.0 | 387,562.0 | 893,815.0 | 194,434.6 | 5 | 5,992 | 0.478 (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `phone-palindrome-6` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `pwd-strength-chain` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `re2_11.0.0_default-caps-simdna` | 15,170.0 | 11,730.0 | 98,200.0 | 33,493.2 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,990.0 | 4,630.0 | 48,230.0 | 16,963.0 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 489,742.0 | 478,362.0 | 1,378,707.0 | 354,642.1 | 5 | 4,776 | 0.724 (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 217,191.0 | 212,031.0 | 614,163.0 | 156,921.7 | 5 | 2,120 | 0.723 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-depth3-bound` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `tag-pair-match` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `trim-nested-star` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,400.0 | 10,770.0 | 100,521.0 | 34,775.9 | 5 | 8 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,120.0 | 10,450.0 | 101,491.0 | 35,291.2 | 5 | 8 | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 751,174.0 | 716,064.0 | 1,698,710.0 | 381,824.3 | 5 | 5,736 | 0.508 (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 687,564.0 | 673,774.0 | 1,216,257.0 | 210,611.1 | 5 | 2,600 | 0.306 (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `utf8-lead-no-cont` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 26,060.0 | 23,791.0 | 87,681.0 | 24,704.0 | 5 | 69 | 0.948 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 64,380.0 | 58,231.0 | 199,471.0 | 54,127.0 | 5 | 69 | 0.841 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,373,638.0 | 1,344,417.0 | 2,408,794.0 | 415,896.8 | 5 | 2,216 | 0.303 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 569,023.0 | 552,583.0 | 1,087,826.0 | 209,510.6 | 5 | 2,088 | 0.368 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,030.0 | 1,580.0 | 45,570.0 | 17,431.6 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,370.0 | 4,440.0 | 89,071.0 | 33,535.1 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 103,110.0 | 95,430.0 | 582,974.0 | 192,328.5 | 5 | 936 | 1.865 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 348,552.0 | 328,652.0 | 1,241,547.0 | 356,341.1 | 5 | 1,704 | 1.022 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `re2_11.0.0_default-caps-simdna` | 11,250.0 | 9,190.0 | 69,040.0 | 23,178.7 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `re2_11.0.0_longest-caps-simdna` | 9,170.0 | 7,370.0 | 55,920.0 | 18,799.3 | 5 | 19 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,175,269.0 | 1,440,168.0 | 4,507,256.0 | 976,940.6 | 5 | 7,928 | 0.308 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 805,665.0 | 746,504.0 | 1,719,940.0 | 371,972.1 | 5 | 2,504 | 0.462 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `re2_11.0.0_default-caps-simdna` | 2,490.0 | 2,200.0 | 48,741.0 | 18,485.2 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,140.0 | 4,180.0 | 82,541.0 | 30,991.5 | 5 | 5 | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 103,231.0 | 94,071.0 | 529,113.0 | 168,072.4 | 5 | 936 | 1.628 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 134,951.0 | 123,810.0 | 522,883.0 | 156,606.4 | 5 | 1,704 | 1.160 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `re2_11.0.0_default-caps-simdna` | 3,224,718.0 | 1,393,798.0 | 4,755,247.0 | 1,315,317.3 | 5 | 3,248 | 0.408 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `re2_11.0.0_longest-caps-simdna` | 2,872,367.0 | 1,377,028.0 | 4,437,856.0 | 1,175,916.5 | 5 | 3,248 | 0.409 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,785,550,151.0 | 1,777,019,042.0 | 1,807,409,028.0 | 11,259,886.4 | 5 | 158,072 | 0.006 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,728,347,520.0 | 1,717,510,868.0 | 1,771,323,079.0 | 18,939,751.3 | 5 | 141,928 | 0.011 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `re2_11.0.0_default-caps-simdna` | 47,780.0 | 42,641.0 | 119,940.0 | 29,363.7 | 5 | 75 | 0.615 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `re2_11.0.0_longest-caps-simdna` | 146,961.0 | 115,861.0 | 283,122.0 | 61,555.3 | 5 | 75 | 0.419 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,007,218.0 | 2,987,168.0 | 3,594,670.0 | 237,286.9 | 5 | 4,232 | 0.079 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,744,492.0 | 3,391,669.0 | 4,414,735.0 | 341,345.5 | 5 | 4,488 | 0.091 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `re2_11.0.0_default-caps-simdna` | 31,280.0 | 25,360.0 | 99,990.0 | 28,410.3 | 5 | 68 | 0.908 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `re2_11.0.0_longest-caps-simdna` | 31,060.0 | 24,950.0 | 89,751.0 | 24,387.9 | 5 | 68 | 0.785 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,499,965.0 | 2,491,984.0 | 3,227,149.0 | 288,687.0 | 5 | 11,752 | 0.115 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 792,955.0 | 780,535.0 | 1,265,817.0 | 189,257.8 | 5 | 3,464 | 0.239 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `re2_11.0.0_default-caps-simdna` | 76,550.0 | 71,670.0 | 157,461.0 | 32,586.8 | 5 | 265 | 0.426 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `re2_11.0.0_longest-caps-simdna` | 202,871.0 | 183,211.0 | 355,603.0 | 63,505.4 | 5 | 265 | 0.313 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,889,101.0 | 1,869,411.0 | 2,594,005.0 | 281,138.9 | 5 | 7,224 | 0.149 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,145,734.0 | 2,011,852.0 | 5,551,962.0 | 1,143,848.4 | 5 | 2,352 | 0.276 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `re2_11.0.0_default-caps-simdna` | 253,121.0 | 234,341.0 | 404,492.0 | 64,573.0 | 5 | 181 | 0.255 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `re2_11.0.0_longest-caps-simdna` | 251,801.0 | 217,511.0 | 401,152.0 | 67,902.7 | 5 | 181 | 0.270 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,549,409.0 | 1,534,229.0 | 2,105,822.0 | 224,991.9 | 5 | 3,504 | 0.145 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,145,274.0 | 2,085,612.0 | 5,242,620.0 | 1,022,622.3 | 5 | 5,048 | 0.247 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `re2_11.0.0_default-caps-simdna` | 408,572.0 | 353,152.0 | 616,374.0 | 95,697.4 | 5 | 412 | 0.234 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `re2_11.0.0_longest-caps-simdna` | 373,013.0 | 352,742.0 | 605,533.0 | 94,393.8 | 5 | 412 | 0.253 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 26,649,604.0 | 26,487,913.0 | 29,390,040.0 | 1,124,103.2 | 5 | 129,576 | 0.042 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,972,168.0 | 4,911,268.0 | 13,899,320.0 | 3,485,623.8 | 5 | 10,072 | 0.701 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,450.0 | 11,430.0 | 97,801.0 | 33,534.9 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `re2_11.0.0_longest-caps-simdna` | 5,890.0 | 4,750.0 | 48,601.0 | 17,143.8 | 5 | 11 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 488,663.0 | 447,183.0 | 1,358,938.0 | 355,466.9 | 5 | 4,776 | 0.727 (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 210,161.0 | 206,022.0 | 595,613.0 | 152,598.9 | 5 | 2,120 | 0.726 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 8,380.0 | 6,940.0 | 90,150.0 | 32,740.8 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `re2_11.0.0_longest-caps-simdna` | 4,140.0 | 3,280.0 | 52,770.0 | 19,508.7 | 5 | 7 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 577,564.0 | 534,483.0 | 1,496,379.0 | 370,713.5 | 5 | 5,592 | 0.642 (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 137,061.0 | 132,801.0 | 521,103.0 | 153,078.3 | 5 | 1,832 | 1.117 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `re2_11.0.0_default-caps-simdna` | 14,140.0 | 11,050.0 | 100,601.0 | 34,737.2 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `re2_11.0.0_longest-caps-simdna` | 14,281.0 | 10,670.0 | 121,610.0 | 43,189.5 | 5 | 13 | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 573,983.0 | 553,114.0 | 1,487,409.0 | 366,410.6 | 5 | 3,944 | 0.638 (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 449,603.0 | 432,083.0 | 941,576.0 | 198,012.9 | 5 | 6,056 | 0.440 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 19,030.0 | 15,870.0 | 77,420.0 | 23,437.6 | 5 | 29 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 18,930.0 | 15,590.0 | 80,781.0 | 24,869.2 | 5 | 29 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,216,977.0 | 1,197,287.0 | 5,204,090.0 | 1,593,992.2 | 5 | 6,104 | 1.310 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,418,258.0 | 1,327,037.0 | 2,550,485.0 | 469,295.6 | 5 | 6,488 | 0.331 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 82,141.0 | 74,961.0 | 210,031.0 | 51,441.4 | 5 | 53 | 0.626 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 95,171.0 | 74,870.0 | 212,131.0 | 50,733.7 | 5 | 53 | 0.533 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,935,881.0 | 1,894,281.0 | 2,989,458.0 | 426,172.2 | 5 | 2,984 | 0.220 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,777,140.0 | 1,747,830.0 | 2,811,356.0 | 414,301.7 | 5 | 2,824 | 0.233 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `re2_11.0.0_default-caps-simdna` | 21,960.0 | 18,010.0 | 133,821.0 | 44,737.7 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `re2_11.0.0_longest-caps-simdna` | 30,610.0 | 17,800.0 | 121,301.0 | 38,342.3 | 5 | 15 | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 679,304.0 | 649,094.0 | 1,586,469.0 | 361,501.9 | 5 | 2,312 | 0.532 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 567,824.0 | 519,093.0 | 1,421,289.0 | 343,672.8 | 5 | 2,088 | 0.605 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `re2_11.0.0_default-caps-simdna` | 56,081.0 | 51,670.0 | 192,951.0 | 54,600.9 | 5 | 72 | 0.974 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `re2_11.0.0_longest-caps-simdna` | 54,460.0 | 53,260.0 | 173,661.0 | 47,036.6 | 5 | 72 | 0.864 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 4,849,558.0 | 3,194,898.0 | 9,195,773.0 | 2,008,299.7 | 5 | 7,472 | 0.414 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,129,117.0 | 1,052,886.0 | 2,032,982.0 | 367,675.3 | 5 | 1,896 | 0.326 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `re2_11.0.0_default-caps-simdna` | 288,411.0 | 275,972.0 | 470,112.0 | 73,297.8 | 5 | 221 | 0.254 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `re2_11.0.0_longest-caps-simdna` | 117,211.0 | 105,610.0 | 213,622.0 | 40,220.7 | 5 | 221 | 0.343 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 10,763,282.0 | 10,731,622.0 | 11,556,046.0 | 322,653.2 | 5 | 31,592 | 0.030 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 5,438,261.0 | 5,430,341.0 | 6,158,885.0 | 285,476.6 | 5 | 19,608 | 0.052 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `re2_11.0.0_default-caps-simdna` | 68,700.0 | 45,410.0 | 180,251.0 | 49,760.5 | 5 | 35 | 0.724 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `re2_11.0.0_longest-caps-simdna` | 21,461.0 | 17,990.0 | 96,880.0 | 30,298.2 | 5 | 35 | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,994,587.0 | 1,824,011.0 | 4,334,755.0 | 795,400.1 | 5 | 9,144 | 0.266 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 3,057,637.0 | 3,035,348.0 | 4,340,475.0 | 508,756.2 | 5 | 4,904 | 0.166 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `re2_11.0.0_default-caps-simdna` | 33,260.0 | 27,400.0 | 136,671.0 | 41,634.1 | 5 | 23 | 1.252 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `re2_11.0.0_longest-caps-simdna` | 33,430.0 | 27,690.0 | 138,031.0 | 41,950.4 | 5 | 23 | 1.255 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,072,762.0 | 1,915,621.0 | 3,367,719.0 | 536,363.3 | 5 | 11,160 | 0.259 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 1,898,701.0 | 1,867,821.0 | 3,117,947.0 | 485,113.6 | 5 | 4,936 | 0.255 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `re2_11.0.0_default-caps-simdna` | 429,732.0 | 416,283.0 | 597,133.0 | 67,963.9 | 5 | 859 | 0.158 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `re2_11.0.0_longest-caps-simdna` | 430,713.0 | 417,352.0 | 597,033.0 | 66,913.5 | 5 | 859 | 0.155 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 35,517,405.0 | 35,468,485.0 | 48,025,158.0 | 4,994,309.7 | 5 | 99,944 | 0.141 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 38,656,033.0 | 38,652,404.0 | 49,270,935.0 | 4,239,579.4 | 5 | 89,624 | 0.110 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `re2_11.0.0_default-caps-simdna` | 46,800.0 | 39,001.0 | 168,611.0 | 49,009.3 | 5 | 20 | 1.047 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `re2_11.0.0_longest-caps-simdna` | 45,130.0 | 38,440.0 | 164,191.0 | 47,947.1 | 5 | 20 | 1.062 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 591,194.0 | 523,293.0 | 1,070,266.0 | 205,529.7 | 5 | 6,136 | 0.348 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 696,464.0 | 653,594.0 | 1,429,008.0 | 295,819.0 | 5 | 3,496 | 0.425 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `re2_11.0.0_default-caps-simdna` | 17,611.0 | 14,220.0 | 80,750.0 | 25,535.5 | 5 | 28 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `re2_11.0.0_longest-caps-simdna` | 17,960.0 | 14,410.0 | 78,561.0 | 24,623.5 | 5 | 28 | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2,097,402.0 | 2,038,802.0 | 3,365,109.0 | 513,896.6 | 5 | 4,152 | 0.245 (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 674,574.0 | 649,413.0 | 1,558,809.0 | 355,224.2 | 5 | 4,184 | 0.527 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `balanced-parens-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `balanced-parens-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `balanced-parens-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `base10num-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,411.0 | 7,580.0 | 25,140.0 | 6,658.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 20,720.0 | 18,360.0 | 49,360.0 | 11,696.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 10,350.0 | 8,750.0 | 31,220.0 | 8,467.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `base10num-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 11,400.0 | 9,800.0 | 30,110.0 | 7,589.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 9,280.0 | 7,530.0 | 23,700.0 | 6,041.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 22,220.0 | 18,510.0 | 48,370.0 | 11,179.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `bracket-array-define` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `codegrammar-flat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,050.0 | 9,570.0 | 22,340.0 | 5,098.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 13,510.0 | 11,250.0 | 34,821.0 | 8,872.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `plain` | `tre_0.9.0_default-caps-simdna` | 11,180.0 | 9,500.0 | 31,840.0 | 8,436.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-flat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 12,480.0 | 10,700.0 | 33,170.0 | 8,419.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,580.0 | 13,090.0 | 38,370.0 | 9,507.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 16,250.0 | 14,050.0 | 39,350.0 | 9,475.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `codegrammar-xflag` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `currency-lookbehind-fixed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,900.0 | 9,700.0 | 29,150.0 | 7,066.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,970.0 | 10,980.0 | 30,850.0 | 7,216.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `currency-lookbehind-fixed` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `date-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,150.0 | 4,480.0 | 19,970.0 | 5,865.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,720.0 | 5,030.0 | 18,250.0 | 5,030.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,250.0 | 5,031.0 | 23,570.0 | 7,020.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `date-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,260.0 | 6,010.0 | 19,640.0 | 5,094.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,710.0 | 9,140.0 | 30,380.0 | 7,831.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,010.0 | 10,740.0 | 31,710.0 | 9,591.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `plain` | `tre_0.9.0_default-caps-simdna` | 11,430.0 | 9,880.0 | 33,800.0 | 8,990.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `doubled-word` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 12,670.0 | 10,860.0 | 33,941.0 | 8,685.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 14,580.0 | 12,580.0 | 35,520.0 | 8,799.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 25,510.0 | 14,360.0 | 36,220.0 | 8,578.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `plain` | `tre_0.9.0_default-caps-simdna` | 15,320.0 | 11,520.0 | 36,610.0 | 9,216.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `dup-param-detect` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 16,810.0 | 12,520.0 | 36,410.0 | 8,741.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,690.0 | 4,360.0 | 24,020.0 | 7,398.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 11,070.0 | 9,420.0 | 29,380.0 | 7,585.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-local-nodup` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `email-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,960.0 | 3,200.0 | 13,020.0 | 3,572.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,000.0 | 3,930.0 | 14,240.0 | 3,734.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,221.0 | 12,500.0 | 38,260.0 | 9,373.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `email-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 15,161.0 | 13,360.0 | 39,810.0 | 10,067.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 3,810.0 | 2,560.0 | 9,360.0 | 2,493.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,290.0 | 3,490.0 | 16,120.0 | 4,802.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `plain` | `tre_0.9.0_default-caps-simdna` | 5,800.0 | 4,650.0 | 16,850.0 | 4,574.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `evil-alt-nested` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,310.0 | 6,401.0 | 20,260.0 | 5,227.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,220.0 | 3,870.0 | 11,960.0 | 3,079.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,790.0 | 2,440.0 | 12,510.0 | 3,905.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,120.0 | 5,340.0 | 18,900.0 | 5,128.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `file-ext-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,050.0 | 6,070.0 | 20,850.0 | 6,308.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 15,230.0 | 14,050.0 | 34,781.0 | 7,937.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `float-literal-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 25,420.0 | 16,120.0 | 70,061.0 | 19,843.0 | 5 | - | timer-floor | compiled=5 |
| `float-literal-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `floor-byte` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 750.0 | 650.0 | 5,810.0 | 2,027.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,230.0 | 1,070.0 | 7,600.0 | 2,547.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `plain` | `tre_0.9.0_default-caps-simdna` | 3,990.0 | 3,030.0 | 22,630.0 | 7,480.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor-byte` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 2,950.0 | 2,270.0 | 11,440.0 | 3,453.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,820.0 | 1,750.0 | 9,490.0 | 3,047.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,280.0 | 2,020.0 | 9,060.0 | 2,713.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `high-byte-run` | `plain` | `tre_0.9.0_default-caps-simdna` | 36,680.0 | 32,460.0 | 121,491.0 | 33,847.1 | 5 | - | 0.923 (max is trial 1) | compiled=5 |
| `high-byte-run` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 16,631.0 | 14,420.0 | 64,440.0 | 18,962.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 59,200.0 | 52,951.0 | 117,041.0 | 23,797.8 | 5 | - | 0.402 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 29,830.0 | 26,340.0 | 40,130.0 | 5,089.7 | 5 | - | 0.171 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 35,550.0 | 29,780.0 | 78,601.0 | 18,380.0 | 5 | - | 0.517 (max is trial 1) | compiled=5 |
| `ipv4-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 33,520.0 | 31,750.0 | 72,690.0 | 15,566.6 | 5 | - | 0.464 (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,130.0 | 3,730.0 | 15,520.0 | 4,557.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,590.0 | 2,360.0 | 12,401.0 | 3,907.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,120.0 | 5,491.0 | 18,500.0 | 4,933.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `keyword-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,130.0 | 6,250.0 | 18,810.0 | 4,728.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 20,790.0 | 15,030.0 | 29,410.0 | 6,007.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `logparse-atomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 39,610.0 | 34,890.0 | 63,840.0 | 10,716.9 | 5 | - | 0.271 (max is trial 1) | compiled=5 |
| `logparse-atomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `logparse-atomic-removed` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 37,950.0 | 33,670.0 | 60,680.0 | 10,033.5 | 5 | - | 0.264 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 34,780.0 | 32,030.0 | 63,411.0 | 11,773.1 | 5 | - | 0.339 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `plain` | `tre_0.9.0_default-caps-simdna` | 40,860.0 | 35,020.0 | 84,590.0 | 18,487.4 | 5 | - | 0.452 (max is trial 1) | compiled=5 |
| `logparse-atomic-removed` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 37,851.0 | 35,910.0 | 80,650.0 | 17,024.1 | 5 | - | 0.450 (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,720.0 | 2,420.0 | 10,800.0 | 3,245.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,910.0 | 2,630.0 | 8,330.0 | 2,164.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,450.0 | 15,680.0 | 56,740.0 | 15,973.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `mojibake-curly-quote` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,400.0 | 7,210.0 | 28,530.0 | 8,075.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `negation-scope-lookbehind-var` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `negation-scope-lookbehind-var` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `nested-comment-rec` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,220.0 | 6,840.0 | 19,010.0 | 4,568.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 26,040.0 | 21,281.0 | 58,510.0 | 13,383.7 | 5 | - | 0.514 (max is trial 1) | compiled=5 |
| `nested-comment-rec` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `numeric-id-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,110.0 | 2,810.0 | 12,500.0 | 3,587.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,930.0 | 4,660.0 | 27,090.0 | 8,432.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 5,200.0 | 4,330.0 | 17,140.0 | 4,827.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `numeric-id-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,700.0 | 5,350.0 | 20,010.0 | 5,356.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,320.0 | 10,610.0 | 34,250.0 | 8,957.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 6,280.0 | 5,550.0 | 15,410.0 | 3,777.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `plain` | `tre_0.9.0_default-caps-simdna` | 8,410.0 | 7,150.0 | 25,670.0 | 6,987.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-list-nested-plus` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,670.0 | 7,960.0 | 27,470.0 | 7,274.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 13,100.0 | 10,640.0 | 25,160.0 | 5,302.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,750.0 | 11,850.0 | 29,460.0 | 6,381.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,880.0 | 7,170.0 | 25,491.0 | 7,051.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `phone-palindrome-6` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,270.0 | 8,260.0 | 28,230.0 | 7,634.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,390.0 | 10,440.0 | 26,610.0 | 6,009.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,940.0 | 21,770.0 | 85,361.0 | 24,136.3 | 5 | - | 0.864 (max is trial 1) | compiled=5 |
| `pwd-strength-chain` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `quoted-delim-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,510.0 | 8,700.0 | 30,220.0 | 9,855.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,220.0 | 10,180.0 | 29,500.0 | 7,215.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `quoted-delim-match` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `router-prefix-order` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,550.0 | 2,340.0 | 15,200.0 | 5,053.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,740.0 | 2,390.0 | 12,370.0 | 3,869.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `plain` | `tre_0.9.0_default-caps-simdna` | 6,090.0 | 5,340.0 | 18,300.0 | 4,888.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `router-prefix-order` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 6,790.0 | 6,150.0 | 18,290.0 | 4,609.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 17,830.0 | 16,180.0 | 44,510.0 | 10,747.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,120.0 | 20,841.0 | 80,371.0 | 22,576.7 | 5 | - | 0.832 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `plain` | `tre_0.9.0_default-caps-simdna` | 39,540.0 | 27,140.0 | 71,161.0 | 16,111.4 | 5 | - | 0.407 (max is trial 1) | compiled=5 |
| `tag-depth3-bound` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 37,080.0 | 28,710.0 | 82,980.0 | 20,150.3 | 5 | - | 0.543 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 22,440.0 | 20,000.0 | 43,800.0 | 8,778.4 | 5 | - | 0.391 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,230.0 | 23,360.0 | 46,871.0 | 8,485.7 | 5 | - | 0.312 (max is trial 1) | compiled=5 |
| `tag-pair-match` | `plain` | `tre_0.9.0_default-caps-simdna` | 22,370.0 | 16,060.0 | 46,931.0 | 11,217.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `tag-pair-match` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,810.0 | 17,780.0 | 50,090.0 | 12,227.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 8,700.0 | 6,950.0 | 21,361.0 | 5,311.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,870.0 | 3,530.0 | 15,040.0 | 4,235.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,700.0 | 6,130.0 | 23,610.0 | 6,508.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `trim-nested-star` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,240.0 | 7,540.0 | 24,670.0 | 6,396.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,960.0 | 1,670.0 | 11,620.0 | 3,867.2 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 3,210.0 | 2,500.0 | 7,140.0 | 1,705.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `utf8-lead-no-cont` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `uuid-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 25,470.0 | 20,450.0 | 41,891.0 | 7,640.4 | 5 | - | 0.300 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 10,340.0 | 8,260.0 | 31,180.0 | 8,701.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 38,890.0 | 36,460.0 | 103,470.0 | 25,522.5 | 5 | - | 0.656 (max is trial 1) | compiled=5 |
| `uuid-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 39,421.0 | 38,200.0 | 98,311.0 | 23,385.2 | 5 | - | 0.593 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,360.0 | 1,240.0 | 11,900.0 | 4,222.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,290.0 | 2,050.0 | 19,450.0 | 6,868.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,640.0 | 1,220.0 | 9,780.0 | 3,261.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-array-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 2,850.0 | 2,290.0 | 12,680.0 | 3,954.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 7,390.0 | 5,810.0 | 20,750.0 | 5,487.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 8,670.0 | 6,400.0 | 55,740.0 | 18,959.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `plain` | `tre_0.9.0_default-caps-simdna` | 9,920.0 | 7,260.0 | 24,100.0 | 6,191.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-constant` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 23,711.0 | 19,900.0 | 78,080.0 | 21,911.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,940.0 | 29,240.0 | 66,640.0 | 13,993.5 | 5 | - | 0.412 (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-number-extended` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-number-extended` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-codegrammar-json-object-begin` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,370.0 | 1,200.0 | 26,100.0 | 9,910.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,260.0 | 2,020.0 | 8,360.0 | 2,440.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,620.0 | 1,290.0 | 15,660.0 | 5,586.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-object-begin` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 2,980.0 | 2,370.0 | 17,540.0 | 5,846.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 13,360.0 | 10,380.0 | 46,361.0 | 13,602.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-codegrammar-json-stringcontent-escape` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-codegrammar-json-stringcontent-escape` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-datetime-datefinder-alternation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,536,937.0 | 2,406,686.0 | 2,993,639.0 | 214,385.3 | 5 | - | 0.085 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,512,887.0 | 2,440,106.0 | 3,000,739.0 | 209,918.4 | 5 | - | 0.084 (max is trial 1) | compiled=5 |
| `wild-datetime-datefinder-alternation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-datefinder-alternation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-datetime-moment-iso8601` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 123,090.0 | 111,511.0 | 173,702.0 | 22,869.3 | 5 | - | 0.186 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 122,390.0 | 109,851.0 | 161,761.0 | 18,882.6 | 5 | - | 0.154 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `plain` | `tre_0.9.0_default-caps-simdna` | 71,830.0 | 68,800.0 | 127,670.0 | 22,061.2 | 5 | - | 0.307 (max is trial 1) | compiled=5 |
| `wild-datetime-moment-iso8601` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 81,021.0 | 70,270.0 | 121,110.0 | 18,277.9 | 5 | - | 0.226 (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 21,790.0 | 17,460.0 | 46,260.0 | 10,643.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 23,540.0 | 18,660.0 | 46,470.0 | 10,149.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-base10num-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 17,170.0 | 14,440.0 | 44,231.0 | 11,213.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 21,570.0 | 17,230.0 | 39,900.0 | 8,277.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-base10num-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 42,270.0 | 35,301.0 | 75,601.0 | 14,924.7 | 5 | - | 0.353 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 44,911.0 | 36,840.0 | 72,381.0 | 13,000.0 | 5 | - | 0.289 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,990.0 | 28,240.0 | 67,790.0 | 14,545.4 | 5 | - | 0.428 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 35,870.0 | 30,500.0 | 66,800.0 | 13,412.1 | 5 | - | 0.374 (max is trial 1) | compiled=5 |
| `wild-logparse-quotedstring-noatomic` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-syslogbase-expanded` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 790,795.0 | 728,345.0 | 935,566.0 | 70,721.8 | 5 | - | 0.089 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 958,736.0 | 941,876.0 | 1,139,188.0 | 74,375.3 | 5 | - | 0.078 (max is trial 1) | compiled=5 |
| `wild-logparse-syslogbase-expanded` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-logparse-winpath-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,790.0 | 5,330.0 | 20,140.0 | 5,667.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 15,430.0 | 12,720.0 | 36,610.0 | 9,008.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-logparse-winpath-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | unsupported-by-declaration=1 |
| `wild-secrets-aws-access-key-id` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 12,150.0 | 9,920.0 | 36,241.0 | 9,949.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 17,220.0 | 12,710.0 | 52,180.0 | 14,784.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `plain` | `tre_0.9.0_default-caps-simdna` | 35,200.0 | 27,070.0 | 70,810.0 | 16,023.8 | 5 | - | 0.455 (max is trial 1) | compiled=5 |
| `wild-secrets-aws-access-key-id` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 40,920.0 | 28,610.0 | 73,801.0 | 16,272.3 | 5 | - | 0.398 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,070.0 | 3,730.0 | 9,800.0 | 2,189.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 5,870.0 | 3,770.0 | 13,731.0 | 3,571.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `plain` | `tre_0.9.0_default-caps-simdna` | 94,250.0 | 92,160.0 | 300,872.0 | 81,424.9 | 5 | - | 0.864 (max is trial 1) | compiled=5 |
| `wild-secrets-github-pat` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 96,700.0 | 95,121.0 | 336,702.0 | 93,744.9 | 5 | - | 0.969 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 28,770.0 | 25,370.0 | 42,650.0 | 6,145.9 | 5 | - | 0.214 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 29,320.0 | 25,830.0 | 42,480.0 | 5,912.0 | 5 | - | 0.202 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `plain` | `tre_0.9.0_default-caps-simdna` | 115,371.0 | 83,431.0 | 227,101.0 | 53,712.3 | 5 | - | 0.466 (max is trial 1) | compiled=5 |
| `wild-secrets-slack-webhook-url` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 131,210.0 | 84,621.0 | 234,242.0 | 54,675.6 | 5 | - | 0.417 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 33,400.0 | 28,590.0 | 57,871.0 | 10,662.4 | 5 | - | 0.319 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 36,800.0 | 31,160.0 | 53,711.0 | 8,246.6 | 5 | - | 0.224 (max is trial 1) | compiled=5 |
| `wild-secrets-username-password-pair` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-secrets-username-password-pair` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 2,070.0 | 1,810.0 | 5,160.0 | 1,258.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 2,520.0 | 2,330.0 | 10,420.0 | 3,148.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `plain` | `tre_0.9.0_default-caps-simdna` | 8,790.0 | 5,000.0 | 18,930.0 | 5,171.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-altorder-foo-foobar-rustregex` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 7,710.0 | 6,290.0 | 25,700.0 | 7,309.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 1,280.0 | 1,140.0 | 4,310.0 | 1,212.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,600.0 | 1,460.0 | 8,790.0 | 2,862.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 7,170.0 | 6,290.0 | 29,390.0 | 8,873.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-dollar-trailing-newline-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 4,110.0 | 3,480.0 | 21,230.0 | 6,865.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 4,170.0 | 3,560.0 | 13,741.0 | 3,830.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 4,990.0 | 3,940.0 | 12,430.0 | 3,143.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `plain` | `tre_0.9.0_default-caps-simdna` | 16,990.0 | 13,880.0 | 73,811.0 | 22,871.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-semdiv-empty-alt-repeat-pcre2` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 8,051.0 | 6,760.0 | 26,400.0 | 7,425.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,400.0 | 7,650.0 | 19,060.0 | 4,068.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 27,380.0 | 20,460.0 | 59,180.0 | 14,148.9 | 5 | - | 0.517 (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 21,780.0 | 19,480.0 | 66,621.0 | 17,876.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-email-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 33,170.0 | 22,430.0 | 60,310.0 | 13,551.5 | 5 | - | 0.409 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 26,281.0 | 23,320.0 | 56,830.0 | 12,660.3 | 5 | - | 0.482 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 71,370.0 | 59,191.0 | 114,281.0 | 21,350.2 | 5 | - | 0.299 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 35,021.0 | 29,670.0 | 76,970.0 | 17,711.7 | 5 | - | 0.506 (max is trial 1) | compiled=5 |
| `wild-validator-ipv4-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 35,060.0 | 31,561.0 | 81,121.0 | 18,683.6 | 5 | - | 0.533 (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,590.0 | 3,990.0 | 12,300.0 | 3,037.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 13,820.0 | 11,960.0 | 38,250.0 | 9,927.6 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `plain` | `tre_0.9.0_default-caps-simdna` | 9,000.0 | 7,530.0 | 26,080.0 | 6,943.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-us-zip-owasp` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 9,940.0 | 8,650.0 | 28,301.0 | 7,390.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 5,310.0 | 3,660.0 | 12,361.0 | 3,168.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 12,850.0 | 11,540.0 | 25,080.0 | 5,689.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `plain` | `tre_0.9.0_default-caps-simdna` | 33,700.0 | 31,940.0 | 99,320.0 | 25,907.5 | 5 | - | 0.769 (max is trial 1) | compiled=5 |
| `wild-validator-uuid-grok` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 36,790.0 | 34,480.0 | 102,480.0 | 25,931.0 | 5 | - | 0.705 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 145,391.0 | 141,191.0 | 196,671.0 | 20,797.4 | 5 | - | 0.143 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 336,712.0 | 315,563.0 | 464,203.0 | 55,035.8 | 5 | - | 0.163 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `plain` | `tre_0.9.0_default-caps-simdna` | 230,061.0 | 187,481.0 | 409,132.0 | 81,858.7 | 5 | - | 0.356 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942140-dbnames` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 229,631.0 | 191,482.0 | 424,372.0 | 85,620.6 | 5 | - | 0.373 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 19,550.0 | 16,620.0 | 34,750.0 | 6,673.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 45,530.0 | 37,740.0 | 79,250.0 | 15,970.7 | 5 | - | 0.351 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `plain` | `tre_0.9.0_default-caps-simdna` | 33,830.0 | 30,590.0 | 72,250.0 | 15,597.4 | 5 | - | 0.461 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942160-sleep-benchmark` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 35,230.0 | 31,500.0 | 76,030.0 | 16,698.9 | 5 | - | 0.474 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 11,661.0 | 9,740.0 | 21,550.0 | 4,314.0 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 28,001.0 | 22,970.0 | 53,390.0 | 11,170.3 | 5 | - | 0.399 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `plain` | `tre_0.9.0_default-caps-simdna` | 16,370.0 | 14,980.0 | 44,690.0 | 11,268.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942270-union-select` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 17,550.0 | 16,340.0 | 45,650.0 | 11,159.1 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 662,274.0 | 629,374.0 | 835,896.0 | 75,166.1 | 5 | - | 0.113 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 1,427,550.0 | 1,383,830.0 | 1,798,132.0 | 154,340.1 | 5 | - | 0.108 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `plain` | `tre_0.9.0_default-caps-simdna` | 1,307,378.0 | 906,415.0 | 2,238,003.0 | 439,994.2 | 5 | - | 0.337 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942360-concat-sqli` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 1,302,367.0 | 911,756.0 | 2,258,453.0 | 445,916.3 | 5 | - | 0.342 (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 10,350.0 | 8,180.0 | 17,040.0 | 3,143.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 20,870.0 | 15,850.0 | 45,140.0 | 10,638.4 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `wild-waf-crs-942500-comment-obfuscation` | `plain` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `wild-waf-crs-942500-comment-obfuscation` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `winpath-near-miss` | `plain` | `oniguruma_6.9.10_default-caps-simdna` | 6,380.0 | 5,090.0 | 18,980.0 | 5,152.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `oniguruma_6.9.10_default-caps-simdna` | 14,970.0 | 12,690.0 | 55,850.0 | 16,383.5 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `plain` | `tre_0.9.0_default-caps-simdna` | 18,470.0 | 16,670.0 | 53,630.0 | 14,152.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `winpath-near-miss` | `whole-subject` | `tre_0.9.0_default-caps-simdna` | 19,420.0 | 17,340.0 | 57,370.0 | 15,214.7 | 5 | - | timer-floor (max is trial 1) | compiled=5 |

