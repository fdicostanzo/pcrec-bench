# pcrec-bench report

## Query

- filters: subbench=email-specimen
- record source: store/index.tsv (11 candidate file(s))
- records included: 11
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T062213Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z` (store/records/email-specimen@0.1/libpcre2_10.46_interp-caps-simdna/email-specimen@0.1__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260825T173402Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z.jsonl)
    - `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z` (store/records/email-specimen@0.1/libpcre2_10.46_jit-caps-simdna/email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T174132Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-caps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-caps-simdna__budu-ryzen1600__20260825T175131Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z` (store/records/email-specimen@0.1/pcrec_692c2e8_auto-nocaps-simdna/email-specimen@0.1__pcrec_692c2e8_auto-nocaps-simdna__budu-ryzen1600__20260825T175534Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-caps-simdna__budu-ryzen1600__20260825T175933Z.jsonl)
    - `email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z` (store/records/email-specimen@0.1/pcrec_692c2e8_vm-in-caps-simdna/email-specimen@0.1__pcrec_692c2e8_vm-in-caps-simdna__budu-ryzen1600__20260825T180451Z.jsonl)
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
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 13,404,326.4 | 13,368,845.5 | 13,576,125.4 | 77,278.4 | 0.257x | 3 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 13,408,225.1 | 13,394,731.7 | 13,572,638.1 | 67,711.1 | 0.257x | 3 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 52,100,169.8 | 51,631,124.3 | 52,291,126.2 | 223,442.3 | 1.000x | 3 | 100% |

### `factored` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 234,045.4 | 233,991.8 | 234,187.7 | 85.3 | 0.127x | 85 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 234,950.9 | 234,809.6 | 235,298.4 | 185.4 | 0.128x | 85 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 464,407.8 | 462,303.1 | 474,574.6 | 4,506.4 | 0.252x | 85 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,833,523.6 | 1,825,603.4 | 1,870,065.7 | 15,610.2 | 0.996x | 85 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,840,011.9 | 1,823,547.2 | 1,875,087.4 | 17,575.6 | 1.000x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 6,136.2 | 6,127.7 | 6,171.5 | 15.6 | 0.044x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 6,284.3 | 6,280.8 | 6,288.0 | 2.7 | 0.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 15,364.2 | 15,306.0 | 15,389.2 | 27.8 | 0.111x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 54,117.6 | 53,402.9 | 54,412.7 | 348.0 | 0.392x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 69,537.5 | 68,685.3 | 69,927.0 | 413.5 | 0.504x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 82,438.7 | 81,501.9 | 82,820.4 | 458.8 | 0.598x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 82,542.8 | 81,246.9 | 84,860.7 | 1,428.5 | 0.599x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 84,075.8 | 81,884.8 | 85,755.1 | 1,234.9 | 0.610x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 137,905.8 | 137,496.3 | 138,120.0 | 246.1 | 1.000x |

### `orig` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 9,124,618.5 | 9,088,777.7 | 9,377,921.3 | 108,199.9 | 0.316x | 3 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 13,393,466.4 | 13,377,567.0 | 13,407,888.5 | 11,788.5 | 0.463x | 3 | 100% |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 13,397,524.5 | 13,376,255.0 | 13,464,852.2 | 34,677.2 | 0.463x | 3 | 100% |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 13,419,602.4 | 13,386,886.3 | 13,487,875.5 | 34,806.9 | 0.464x | 3 | 100% |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 13,419,710.9 | 13,378,803.9 | 13,495,708.0 | 42,286.7 | 0.464x | 3 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 28,909,549.3 | 28,744,453.0 | 29,141,895.9 | 143,612.8 | 1.000x | 3 | 100% |

### `orig` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 62,732.3 | 62,494.7 | 62,927.9 | 152.3 | 0.117x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 80,227.6 | 80,062.2 | 80,517.8 | 159.4 | 0.149x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 100,989.8 | 99,972.5 | 101,276.1 | 455.7 | 0.188x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 234,114.6 | 233,838.7 | 234,203.1 | 131.3 | 0.436x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 234,417.4 | 234,085.6 | 234,598.6 | 174.0 | 0.437x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 234,774.0 | 234,543.1 | 234,978.3 | 179.2 | 0.437x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 235,230.3 | 234,913.4 | 236,508.9 | 586.4 | 0.438x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 535,137.9 | 533,912.7 | 547,816.1 | 5,144.2 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 536,878.8 | 536,089.1 | 538,135.6 | 668.9 | 1.000x |

### `orig` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 6,123.8 | 6,111.3 | 6,274.4 | 61.5 | 0.093x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 6,125.1 | 6,121.6 | 6,139.6 | 6.4 | 0.093x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 6,128.6 | 6,125.4 | 6,155.1 | 11.5 | 0.093x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 6,131.1 | 6,118.3 | 6,148.6 | 11.8 | 0.093x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 6,135.3 | 6,105.5 | 6,151.9 | 16.0 | 0.093x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 12,546.2 | 12,511.8 | 12,629.5 | 43.5 | 0.190x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 28,996.9 | 28,809.3 | 30,001.0 | 431.1 | 0.440x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 30,090.3 | 29,227.9 | 31,144.4 | 610.3 | 0.456x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 65,959.2 | 65,868.6 | 67,749.1 | 708.1 | 1.000x |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 3 | 67% | 0 | 0 | `t-c-long-atom-run` (other) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 85 | 94% | 25 | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 3 | 67% | 5 | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 137,870,986.0 | 131,535,054.0 | 141,303,679.0 | 3,360,140.2 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 151,352,487.0 | 146,828,416.0 | 172,195,634.0 | 9,583,670.9 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 135,825,530.0 | 123,966,752.0 | 150,180,853.0 | 8,917,589.7 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 141,989,216.0 | 125,149,031.0 | 147,678,719.0 | 8,307,974.1 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 535,765,380.0 | 526,468,518.0 | 537,513,576.0 | 4,046,565.0 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 538,961,373.0 | 537,787,867.0 | 542,941,905.0 | 1,841,075.2 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 533,212,035.0 | 528,952,948.0 | 535,271,359.0 | 2,613,095.7 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 542,331,633.0 | 530,896,401.0 | 545,425,863.0 | 5,487,425.3 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 420,465,289.0 | 414,985,073.0 | 428,903,342.0 | 4,893,507.9 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 430,387,601.0 | 417,874,860.0 | 443,938,027.0 | 8,743,376.0 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 427,493,516.0 | 422,008,523.0 | 434,926,485.0 | 4,492,879.1 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 420,974,905.0 | 413,095,565.0 | 432,864,330.0 | 7,311,852.8 | 5 | compiled=5 |
| `factored` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 424,762,944.0 | 423,664,078.0 | 432,708,304.0 | 3,362,545.9 | 5 | compiled=5 |
| `factored` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 427,987,625.0 | 424,012,201.0 | 439,228,106.0 | 5,642,429.0 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_692c2e8_auto-caps-simdna` | 138,059,729.0 | 124,894,261.0 | 149,332,363.0 | 8,629,100.3 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-caps-simdna` | 140,676,166.0 | 139,723,758.0 | 158,223,452.0 | 7,360,641.1 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_692c2e8_auto-nocaps-simdna` | 133,689,958.0 | 120,601,984.0 | 142,934,562.0 | 8,297,236.7 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_692c2e8_auto-nocaps-simdna` | 160,936,575.0 | 140,161,606.0 | 164,819,689.0 | 10,686,048.7 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 406,687,295.0 | 398,252,896.0 | 413,024,068.0 | 5,798,706.7 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 404,607,847.0 | 391,192,410.0 | 416,889,170.0 | 8,332,820.0 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 406,593,912.0 | 392,519,313.0 | 419,969,716.0 | 9,292,650.8 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_692c2e8_vm-in-caps-simdna` | 401,511,589.0 | 398,264,420.0 | 408,501,273.0 | 3,919,558.6 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 118,056,825.0 | 103,621,896.0 | 120,772,314.0 | 6,366,891.3 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 117,555,053.0 | 109,696,744.0 | 130,533,016.0 | 9,212,004.5 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 113,739,182.0 | 110,959,754.0 | 143,108,420.0 | 11,988,842.7 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 135,300,201.0 | 122,043,665.0 | 137,739,956.0 | 6,730,911.2 | 5 | compiled=5 |
| `orig` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 382,875,770.0 | 372,878,556.0 | 389,967,264.0 | 6,557,411.6 | 5 | compiled=5 |
| `orig` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 374,587,618.0 | 362,494,710.0 | 389,369,562.0 | 9,692,150.1 | 5 | compiled=5 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,290.5 | 62,961.0 | 168,531.0 | 39,080.9 | 10 | compiled=10 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 154,441.0 | 133,921.0 | 396,882.0 | 95,859.2 | 10 | compiled=10 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 33,210.5 | 12,870.0 | 101,331.0 | 25,036.8 | 10 | compiled=10 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 31,690.0 | 12,300.0 | 109,651.0 | 27,509.2 | 10 | compiled=10 |

