# pcrec-bench report

## Query

- filters: subbench=email-specimen
- record source: store/index.tsv (5 candidate file(s))
- records included: 5
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-caps-simdna/email-specimen@0.1__pcrec_8da6120_auto-caps-simdna__budu-ryzen1600__20260825T065046Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z` (store/records/email-specimen@0.1/pcrec_8da6120_auto-nocaps-simdna/email-specimen@0.1__pcrec_8da6120_auto-nocaps-simdna__budu-ryzen1600__20260825T063943Z.jsonl)
    - `email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z` (store/records/email-specimen@0.1/pcrec_8da6120_vm-caps-simdna/email-specimen@0.1__pcrec_8da6120_vm-caps-simdna__budu-ryzen1600__20260825T064436Z.jsonl)
- sub-bench version(s): email-specimen@0.1
- machine(s): budu-ryzen1600
- schema version(s): 1.1
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost)

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 51,887,584.9 | 51,715,536.7 | 52,400,309.6 | 237,758.7 | 1.000x | 3 | 100% |

### `factored` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,838,131.4 | 1,834,292.9 | 1,867,343.0 | 12,430.8 | 0.993x | 85 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,851,831.7 | 1,833,210.9 | 1,882,042.5 | 16,258.5 | 1.000x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 15,356.9 | 15,283.3 | 15,555.6 | 93.0 | 0.110x |
| 2 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 82,438.7 | 81,501.9 | 82,820.4 | 458.8 | 0.591x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 82,542.8 | 81,246.9 | 84,860.7 | 1,428.5 | 0.592x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 84,075.8 | 81,884.8 | 85,755.1 | 1,234.9 | 0.603x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 139,473.0 | 137,977.7 | 142,462.1 | 1,654.9 | 1.000x |

### `orig` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 9,080,736.7 | 9,007,571.8 | 9,110,169.7 | 36,680.6 | 0.315x | 3 | 100% |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 13,397,524.5 | 13,376,255.0 | 13,464,852.2 | 34,677.2 | 0.464x | 3 | 100% |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 13,419,710.9 | 13,378,803.9 | 13,495,708.0 | 42,286.7 | 0.465x | 3 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 28,855,145.7 | 28,771,996.2 | 29,202,089.1 | 156,956.7 | 1.000x | 3 | 100% |

### `orig` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 100,989.8 | 99,972.5 | 101,276.1 | 455.7 | 0.188x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 234,774.0 | 234,543.1 | 234,978.3 | 179.2 | 0.437x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 235,230.3 | 234,913.4 | 236,508.9 | 586.4 | 0.438x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 536,225.9 | 535,003.5 | 538,779.0 | 1,231.3 | 0.998x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 537,486.9 | 535,808.3 | 545,853.0 | 3,695.2 | 1.000x |

### `orig` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 6,131.1 | 6,118.3 | 6,148.6 | 11.8 | 0.093x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 6,135.3 | 6,105.5 | 6,151.9 | 16.0 | 0.093x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 6,276.7 | 6,174.2 | 6,828.3 | 242.4 | 0.096x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 30,090.3 | 29,227.9 | 31,144.4 | 610.3 | 0.458x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 65,681.7 | 65,504.1 | 66,190.9 | 292.3 | 1.000x |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 3 | 67% | 0 | 0 | `t-c-long-atom-run` (other) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 | compiled=5 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,630.0 | 64,000.0 | 168,531.0 | 39,793.8 | 5 | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 159,291.0 | 144,641.0 | 396,882.0 | 95,332.9 | 5 | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,510.0 | 12,870.0 | 45,421.0 | 12,460.8 | 5 | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,541.0 | 12,300.0 | 45,080.0 | 12,673.0 | 5 | compiled=5 |

