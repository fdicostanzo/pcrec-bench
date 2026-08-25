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
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost)

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 111.9 | 111.2 | 113.8 | 0.9 | 0.129x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.6 | 130.2 | 137.7 | 2.9 | 0.150x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 148.9 | 147.4 | 149.6 | 0.9 | 0.171x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 320.6 | 307.5 | 329.7 | 9.4 | 0.369x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 466.9 | 421.0 | 495.7 | 25.2 | 0.537x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 490.2 | 483.1 | 536.9 | 20.1 | 0.564x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 500.9 | 494.5 | 502.4 | 3.0 | 0.576x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 868.5 | 859.8 | 888.2 | 8.9 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 869.0 | 852.9 | 883.2 | 9.2 | 1.000x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.7 | 103.2 | 104.0 | 0.3 | 0.120x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.8 | 106.7 | 107.3 | 0.2 | 0.124x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 153.1 | 152.2 | 153.3 | 0.4 | 0.178x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 154.9 | 154.2 | 156.5 | 0.8 | 0.180x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 330.5 | 321.2 | 338.9 | 6.4 | 0.384x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 430.7 | 416.6 | 504.6 | 31.6 | 0.500x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 464.5 | 445.4 | 495.6 | 17.8 | 0.539x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 467.6 | 450.4 | 488.3 | 13.3 | 0.543x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 861.1 | 849.3 | 878.9 | 8.1 | 1.000x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 144.2 | 143.5 | 144.7 | 0.4 | 0.117x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 163.7 | 163.4 | 171.3 | 3.0 | 0.133x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 203.5 | 201.8 | 207.1 | 1.8 | 0.166x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 379.2 | 369.0 | 402.7 | 13.0 | 0.309x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 506.6 | 493.4 | 538.1 | 15.3 | 0.413x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 584.4 | 572.0 | 619.1 | 16.2 | 0.476x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 600.3 | 562.6 | 692.0 | 46.5 | 0.489x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,225.4 | 1,212.4 | 1,234.3 | 7.6 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,228.0 | 1,214.2 | 1,234.8 | 7.0 | 1.000x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 135.5 | 135.2 | 138.7 | 1.3 | 0.111x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 139.1 | 138.9 | 139.2 | 0.1 | 0.114x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 175.7 | 175.4 | 177.3 | 0.6 | 0.144x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 208.4 | 208.0 | 210.5 | 1.1 | 0.170x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 392.5 | 374.8 | 402.2 | 10.5 | 0.321x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 520.6 | 492.6 | 536.5 | 19.3 | 0.426x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 551.7 | 511.9 | 579.7 | 29.3 | 0.451x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 563.7 | 533.3 | 597.8 | 26.8 | 0.461x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,222.6 | 1,204.6 | 1,256.0 | 15.0 | 1.000x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 46.1 | 45.8 | 46.5 | 0.2 | 0.061x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 66.7 | 66.6 | 72.2 | 2.2 | 0.088x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 103.0 | 102.8 | 103.7 | 0.3 | 0.136x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 279.0 | 274.8 | 302.6 | 12.1 | 0.368x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 430.1 | 380.9 | 443.6 | 22.1 | 0.568x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 431.3 | 408.0 | 454.4 | 17.8 | 0.569x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 452.3 | 402.1 | 485.4 | 31.1 | 0.597x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 752.4 | 742.3 | 759.8 | 6.1 | 0.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 757.8 | 746.0 | 768.9 | 6.7 | 1.000x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 38.8 | 37.8 | 57.9 | 7.8 | 0.052x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 42.2 | 41.9 | 42.8 | 0.3 | 0.056x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 106.5 | 106.4 | 109.6 | 1.3 | 0.141x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 122.3 | 119.9 | 125.7 | 1.7 | 0.162x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 269.7 | 264.1 | 292.4 | 10.0 | 0.358x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 350.0 | 299.7 | 478.7 | 64.0 | 0.465x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 375.7 | 371.4 | 488.0 | 48.1 | 0.499x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 390.2 | 355.6 | 453.4 | 33.1 | 0.518x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 753.0 | 743.5 | 776.2 | 9.5 | 1.000x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 156.9 | 156.6 | 163.1 | 2.5 | 0.118x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 176.5 | 175.9 | 182.8 | 2.6 | 0.133x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 215.8 | 214.2 | 219.0 | 1.6 | 0.163x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 428.8 | 379.5 | 445.9 | 23.3 | 0.323x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 590.8 | 545.4 | 621.1 | 27.6 | 0.446x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 652.5 | 596.4 | 727.2 | 43.3 | 0.492x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 660.6 | 595.4 | 709.3 | 47.2 | 0.498x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,325.9 | 1,315.1 | 1,348.5 | 9.6 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,326.8 | 1,315.1 | 1,340.3 | 8.6 | 1.001x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 148.1 | 147.5 | 148.8 | 0.4 | 0.111x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 151.7 | 151.4 | 151.9 | 0.1 | 0.114x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 185.2 | 183.6 | 187.4 | 1.0 | 0.139x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 219.0 | 218.6 | 223.6 | 1.9 | 0.165x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 411.6 | 381.9 | 425.4 | 14.3 | 0.309x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 566.9 | 558.6 | 680.0 | 46.1 | 0.426x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 581.7 | 557.8 | 636.4 | 27.8 | 0.437x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 626.4 | 601.0 | 665.6 | 22.0 | 0.471x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,331.2 | 1,316.8 | 1,440.4 | 34.4 | 1.000x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 167.3 | 167.1 | 168.1 | 0.4 | 0.190x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 222.0 | 221.8 | 223.3 | 0.5 | 0.252x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 241.9 | 241.0 | 247.8 | 2.5 | 0.274x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 375.5 | 369.8 | 378.2 | 2.7 | 0.426x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 529.9 | 476.0 | 572.3 | 34.4 | 0.601x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 572.3 | 517.2 | 584.7 | 27.5 | 0.649x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 611.8 | 531.7 | 657.6 | 46.0 | 0.694x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 880.2 | 870.4 | 892.6 | 7.6 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 881.4 | 875.5 | 898.3 | 7.1 | 1.000x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 167.9 | 166.6 | 175.7 | 2.5 | 0.191x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 171.9 | 171.3 | 172.2 | 0.4 | 0.195x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 214.1 | 213.7 | 214.9 | 0.4 | 0.243x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 217.3 | 217.0 | 217.9 | 0.3 | 0.247x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 365.7 | 346.7 | 371.5 | 11.0 | 0.415x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 508.5 | 458.7 | 540.8 | 31.9 | 0.577x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 511.9 | 467.4 | 559.7 | 31.3 | 0.581x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 544.3 | 524.8 | 550.2 | 10.3 | 0.618x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 881.2 | 861.9 | 899.0 | 12.4 | 1.000x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 46.0 | 45.3 | 46.6 | 0.4 | 0.061x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 66.5 | 65.7 | 71.9 | 2.2 | 0.088x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 102.8 | 102.7 | 103.1 | 0.1 | 0.137x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 299.0 | 270.4 | 325.7 | 17.7 | 0.398x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 429.2 | 380.7 | 544.8 | 55.3 | 0.571x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 451.3 | 416.5 | 483.3 | 24.7 | 0.600x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 453.9 | 404.4 | 469.4 | 22.6 | 0.604x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 748.1 | 740.7 | 764.2 | 6.3 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 751.9 | 743.5 | 760.3 | 5.3 | 1.000x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 38.7 | 38.7 | 38.9 | 0.1 | 0.052x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 42.0 | 41.9 | 42.0 | 0.1 | 0.056x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 106.7 | 106.3 | 107.1 | 0.3 | 0.142x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 122.0 | 120.0 | 126.1 | 1.7 | 0.163x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 298.4 | 283.9 | 327.3 | 14.3 | 0.398x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 384.6 | 316.6 | 486.6 | 54.4 | 0.512x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 398.4 | 358.1 | 585.4 | 82.4 | 0.531x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 413.5 | 346.1 | 452.2 | 36.5 | 0.551x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 750.5 | 740.4 | 775.1 | 11.7 | 1.000x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 104.1 | 103.6 | 107.8 | 1.6 | 0.077x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 124.0 | 123.8 | 130.1 | 2.5 | 0.092x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 221.4 | 220.5 | 250.1 | 11.4 | 0.164x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 442.7 | 424.2 | 443.0 | 7.2 | 0.328x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 610.4 | 599.5 | 768.3 | 64.3 | 0.453x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 643.7 | 620.7 | 699.9 | 29.3 | 0.478x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 681.0 | 603.5 | 692.3 | 32.1 | 0.505x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,347.7 | 1,330.8 | 1,367.6 | 11.2 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,354.3 | 1,344.2 | 1,453.0 | 30.1 | 1.005x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 96.8 | 96.2 | 97.1 | 0.3 | 0.072x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 99.7 | 99.4 | 100.3 | 0.3 | 0.074x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 165.8 | 164.5 | 173.6 | 2.5 | 0.123x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 227.7 | 226.7 | 229.3 | 1.0 | 0.169x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 440.5 | 410.8 | 444.6 | 12.6 | 0.327x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 603.5 | 597.0 | 676.6 | 36.1 | 0.448x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 618.0 | 585.7 | 699.6 | 37.9 | 0.459x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 671.0 | 665.0 | 695.0 | 12.3 | 0.498x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,346.2 | 1,332.7 | 1,372.3 | 10.8 | 1.000x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 168.0 | 167.8 | 168.4 | 0.2 | 0.173x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 169.9 | 169.6 | 171.3 | 0.6 | 0.175x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 190.1 | 189.5 | 196.5 | 2.6 | 0.196x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 387.9 | 332.0 | 398.3 | 23.9 | 0.400x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 517.4 | 491.2 | 596.9 | 36.0 | 0.533x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 582.5 | 531.6 | 641.0 | 35.6 | 0.600x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 609.1 | 544.9 | 655.3 | 42.1 | 0.627x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 970.8 | 952.5 | 978.5 | 7.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 972.2 | 962.8 | 1,010.9 | 12.5 | 1.001x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 161.8 | 161.5 | 162.4 | 0.3 | 0.165x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 165.4 | 165.3 | 165.9 | 0.2 | 0.169x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 172.7 | 170.9 | 198.5 | 9.1 | 0.176x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 172.8 | 172.3 | 175.4 | 1.1 | 0.176x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 383.4 | 370.8 | 388.9 | 6.5 | 0.391x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 512.1 | 492.5 | 573.0 | 30.3 | 0.523x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 567.2 | 546.3 | 586.4 | 14.4 | 0.579x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 576.3 | 496.7 | 595.9 | 41.2 | 0.588x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 979.5 | 959.7 | 997.8 | 12.6 | 1.000x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 129.8 | 129.4 | 130.1 | 0.2 | 0.150x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 149.7 | 148.5 | 150.0 | 0.6 | 0.173x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 149.9 | 149.8 | 155.9 | 2.4 | 0.173x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 354.2 | 310.7 | 375.8 | 22.9 | 0.409x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 512.8 | 495.3 | 524.7 | 11.8 | 0.593x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 570.0 | 494.9 | 615.3 | 40.3 | 0.659x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 602.6 | 525.3 | 629.6 | 35.5 | 0.696x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 865.3 | 846.3 | 898.3 | 14.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 866.7 | 853.5 | 870.6 | 5.0 | 1.002x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 122.9 | 122.4 | 124.3 | 0.7 | 0.141x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 126.4 | 126.3 | 128.5 | 0.9 | 0.145x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 154.6 | 153.9 | 154.9 | 0.3 | 0.178x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 158.5 | 157.6 | 165.6 | 2.4 | 0.182x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 368.2 | 357.5 | 382.3 | 8.3 | 0.423x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 486.7 | 461.1 | 548.0 | 29.5 | 0.559x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 499.0 | 440.8 | 545.0 | 39.9 | 0.573x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 531.7 | 460.3 | 603.6 | 50.1 | 0.611x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 870.1 | 851.0 | 896.9 | 13.3 | 1.000x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.8 | 96.7 | 99.3 | 1.0 | 0.113x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 118.2 | 118.2 | 123.8 | 2.2 | 0.137x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 146.1 | 145.3 | 153.7 | 3.1 | 0.170x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 352.7 | 320.6 | 370.9 | 16.9 | 0.410x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 484.3 | 472.8 | 535.7 | 27.8 | 0.563x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 557.6 | 496.0 | 607.5 | 38.4 | 0.649x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 582.2 | 541.5 | 597.9 | 21.1 | 0.677x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 859.7 | 844.4 | 873.4 | 9.3 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 859.8 | 857.3 | 870.4 | 3.6 | 1.000x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 90.1 | 89.8 | 90.4 | 0.2 | 0.104x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 93.4 | 93.4 | 93.7 | 0.1 | 0.108x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 148.6 | 147.3 | 151.4 | 1.5 | 0.172x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 150.4 | 150.2 | 152.1 | 0.7 | 0.174x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 362.6 | 353.5 | 374.8 | 7.5 | 0.420x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 469.9 | 421.4 | 507.0 | 32.2 | 0.544x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 472.8 | 462.0 | 541.1 | 29.7 | 0.548x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 529.4 | 501.8 | 566.8 | 22.6 | 0.613x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 863.2 | 843.7 | 886.0 | 14.6 | 1.000x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.8 | 96.6 | 100.6 | 1.5 | 0.136x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 100.6 | 100.3 | 107.6 | 2.8 | 0.142x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 118.2 | 117.8 | 124.4 | 2.5 | 0.167x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 314.1 | 291.6 | 318.1 | 9.8 | 0.443x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 446.3 | 387.6 | 452.9 | 23.9 | 0.629x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 460.8 | 410.4 | 488.6 | 26.1 | 0.649x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 465.9 | 444.5 | 501.5 | 20.7 | 0.657x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 709.6 | 703.6 | 716.9 | 4.3 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 712.4 | 698.2 | 723.8 | 6.9 | 1.004x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 90.0 | 89.8 | 90.3 | 0.2 | 0.126x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 93.6 | 93.3 | 94.0 | 0.3 | 0.131x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 106.4 | 106.3 | 106.7 | 0.1 | 0.149x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 120.5 | 118.5 | 121.7 | 1.1 | 0.169x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 296.5 | 252.0 | 332.4 | 26.5 | 0.416x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 388.8 | 361.6 | 476.7 | 40.5 | 0.545x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 417.0 | 340.2 | 472.0 | 44.3 | 0.584x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 428.2 | 406.4 | 516.4 | 38.8 | 0.600x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 713.4 | 705.1 | 731.7 | 9.4 | 1.000x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 69.7 | 69.2 | 71.3 | 0.7 | 0.112x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 71.1 | 70.4 | 72.1 | 0.5 | 0.115x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 224.5 | 218.0 | 225.8 | 2.7 | 0.362x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 431.8 | 408.2 | 435.5 | 10.3 | 0.697x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 531.0 | 469.5 | 594.4 | 44.2 | 0.857x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 555.3 | 516.0 | 609.9 | 29.9 | 0.896x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 568.9 | 535.2 | 597.2 | 22.3 | 0.918x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 616.8 | 609.4 | 641.4 | 9.3 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 619.8 | 611.0 | 642.2 | 10.5 | 1.000x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 63.8 | 63.7 | 64.0 | 0.1 | 0.014x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 64.1 | 64.0 | 64.3 | 0.1 | 0.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 441.3 | 434.7 | 459.2 | 6.8 | 0.094x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 2,031.7 | 2,008.1 | 2,256.0 | 92.0 | 0.431x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 2,223.9 | 2,184.4 | 2,277.3 | 31.4 | 0.472x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 2,346.9 | 2,332.0 | 2,382.0 | 17.9 | 0.498x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 2,380.1 | 2,342.9 | 2,515.8 | 60.6 | 0.505x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 2,383.6 | 2,352.9 | 2,427.3 | 26.6 | 0.506x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 4,710.9 | 4,664.2 | 4,804.0 | 40.3 | 1.000x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.2 | 122.7 | 125.1 | 0.8 | 0.112x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 143.6 | 143.5 | 149.6 | 2.4 | 0.131x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 204.2 | 203.6 | 205.7 | 0.7 | 0.186x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 421.3 | 394.7 | 436.5 | 13.8 | 0.383x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 580.5 | 563.8 | 604.2 | 13.2 | 0.528x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 640.8 | 603.9 | 662.7 | 22.2 | 0.583x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 650.6 | 601.5 | 696.0 | 30.1 | 0.592x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,089.6 | 1,074.0 | 1,117.1 | 10.9 | 0.992x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,098.8 | 1,084.7 | 1,119.9 | 11.3 | 1.000x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.6 | 115.5 | 115.8 | 0.1 | 0.105x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 119.6 | 119.4 | 119.9 | 0.1 | 0.109x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 172.3 | 170.0 | 179.2 | 2.7 | 0.157x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 208.9 | 208.8 | 210.1 | 0.5 | 0.191x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 425.9 | 405.3 | 471.0 | 22.7 | 0.389x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 612.3 | 519.2 | 639.6 | 42.7 | 0.559x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 615.4 | 573.0 | 630.7 | 19.7 | 0.561x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 629.0 | 607.1 | 659.4 | 20.2 | 0.574x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,096.0 | 1,091.4 | 1,128.6 | 11.6 | 1.000x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.2 | 122.6 | 124.0 | 0.4 | 0.111x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 143.5 | 143.3 | 150.2 | 2.7 | 0.130x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 204.2 | 203.2 | 206.9 | 1.7 | 0.185x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 422.4 | 410.8 | 451.5 | 14.0 | 0.382x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 602.2 | 554.6 | 609.6 | 20.3 | 0.545x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 619.7 | 594.1 | 649.6 | 20.0 | 0.560x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 647.5 | 605.1 | 716.7 | 37.1 | 0.586x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,095.5 | 1,086.6 | 1,129.2 | 14.6 | 0.991x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,105.6 | 1,075.2 | 1,129.3 | 13.8 | 1.000x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.5 | 115.5 | 115.8 | 0.1 | 0.105x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 119.5 | 119.4 | 119.8 | 0.1 | 0.108x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 170.8 | 170.1 | 179.2 | 3.0 | 0.155x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 209.3 | 208.7 | 212.1 | 1.2 | 0.190x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 429.8 | 412.8 | 465.6 | 17.4 | 0.389x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 604.9 | 430.6 | 636.1 | 73.8 | 0.548x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 610.4 | 569.7 | 661.0 | 32.1 | 0.553x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 622.1 | 602.8 | 651.4 | 16.2 | 0.564x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,103.5 | 1,086.6 | 1,124.6 | 11.5 | 1.000x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.9 | 96.7 | 97.3 | 0.2 | 0.111x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 118.2 | 117.7 | 123.8 | 2.3 | 0.135x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 159.5 | 158.1 | 163.6 | 2.0 | 0.182x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 377.4 | 376.8 | 394.5 | 7.4 | 0.431x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 595.0 | 591.5 | 625.5 | 12.9 | 0.679x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 597.9 | 544.4 | 703.5 | 56.9 | 0.682x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 608.4 | 574.9 | 634.0 | 21.6 | 0.694x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 876.1 | 858.3 | 906.7 | 14.3 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 878.2 | 857.1 | 959.9 | 28.4 | 1.002x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.9 | 89.7 | 90.4 | 0.3 | 0.103x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 93.4 | 93.3 | 93.7 | 0.2 | 0.107x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 155.5 | 153.6 | 158.8 | 1.3 | 0.178x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 169.2 | 168.5 | 169.4 | 0.3 | 0.194x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 383.1 | 368.1 | 397.5 | 12.5 | 0.438x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 517.3 | 497.5 | 575.7 | 27.6 | 0.592x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 523.7 | 502.5 | 563.8 | 20.4 | 0.599x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 547.2 | 531.0 | 629.9 | 35.6 | 0.626x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 873.8 | 862.5 | 894.3 | 9.3 | 1.000x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 117.2 | 116.8 | 117.5 | 0.3 | 0.110x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 137.9 | 137.5 | 143.4 | 2.3 | 0.129x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 201.7 | 201.3 | 202.4 | 0.5 | 0.189x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 426.5 | 399.5 | 436.7 | 12.5 | 0.400x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 623.6 | 592.9 | 715.3 | 45.2 | 0.585x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 629.7 | 586.1 | 643.4 | 20.6 | 0.590x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 639.8 | 577.5 | 700.2 | 42.0 | 0.600x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,066.7 | 1,051.3 | 1,086.3 | 12.7 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,066.8 | 1,055.8 | 1,113.6 | 15.9 | 1.000x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 109.8 | 109.5 | 111.2 | 0.6 | 0.104x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 113.5 | 113.2 | 118.6 | 2.1 | 0.107x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 175.0 | 172.3 | 178.4 | 2.1 | 0.165x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 208.0 | 207.9 | 208.8 | 0.4 | 0.196x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 430.2 | 410.6 | 438.8 | 10.2 | 0.406x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 601.7 | 596.6 | 639.3 | 18.7 | 0.568x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 609.7 | 509.9 | 644.2 | 47.3 | 0.576x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 641.3 | 613.6 | 661.5 | 17.4 | 0.606x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,058.8 | 1,052.5 | 1,070.7 | 5.6 | 1.000x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.2 | 52.9 | 53.4 | 0.2 | 0.147x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 54.7 | 54.6 | 55.0 | 0.1 | 0.151x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 107.9 | 107.4 | 110.4 | 1.1 | 0.299x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 333.0 | 316.8 | 350.3 | 11.3 | 0.922x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 361.0 | 357.5 | 377.3 | 6.6 | 1.000x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 363.7 | 359.0 | 383.4 | 6.7 | 1.007x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 450.0 | 420.2 | 506.3 | 29.4 | 1.247x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 467.6 | 453.0 | 511.3 | 22.5 | 1.296x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 479.7 | 424.5 | 532.7 | 39.7 | 1.329x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.4 | 47.3 | 47.6 | 0.1 | 0.020x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.8 | 47.7 | 47.9 | 0.1 | 0.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 259.9 | 259.0 | 267.4 | 2.9 | 0.108x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,440.2 | 1,414.0 | 1,513.6 | 35.2 | 0.599x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,671.5 | 1,643.5 | 1,736.4 | 32.8 | 0.696x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,806.7 | 1,778.3 | 1,866.6 | 30.2 | 0.752x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,813.5 | 1,752.2 | 1,835.7 | 34.2 | 0.755x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,829.7 | 1,768.5 | 1,867.0 | 34.1 | 0.761x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,403.0 | 2,371.5 | 2,460.6 | 25.9 | 1.000x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.3 | 122.9 | 123.4 | 0.2 | 0.112x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 143.5 | 143.2 | 149.7 | 2.5 | 0.130x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 205.1 | 203.5 | 206.5 | 1.2 | 0.186x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 428.6 | 419.3 | 447.7 | 9.7 | 0.388x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 597.0 | 548.2 | 657.6 | 39.2 | 0.541x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 615.4 | 566.5 | 726.4 | 62.4 | 0.557x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 648.3 | 610.7 | 698.3 | 31.9 | 0.587x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,094.7 | 1,084.8 | 1,118.6 | 10.3 | 0.992x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,104.0 | 1,078.9 | 1,348.0 | 74.8 | 1.000x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.6 | 115.4 | 116.2 | 0.3 | 0.105x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 119.3 | 119.1 | 119.9 | 0.3 | 0.109x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 170.8 | 170.3 | 184.1 | 4.0 | 0.156x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 209.3 | 208.9 | 214.5 | 2.2 | 0.191x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 414.0 | 402.2 | 425.9 | 8.7 | 0.377x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 576.3 | 545.8 | 654.8 | 41.2 | 0.525x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 614.3 | 592.7 | 638.0 | 16.3 | 0.560x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 643.5 | 590.7 | 700.1 | 36.5 | 0.587x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,096.8 | 1,091.6 | 1,116.2 | 8.6 | 1.000x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 116.9 | 116.8 | 120.1 | 1.3 | 0.110x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 137.7 | 137.5 | 143.4 | 2.3 | 0.129x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 201.8 | 200.8 | 202.6 | 0.7 | 0.190x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 432.5 | 415.5 | 436.0 | 7.4 | 0.406x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 618.1 | 592.2 | 657.7 | 27.5 | 0.581x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 620.8 | 587.8 | 708.5 | 41.0 | 0.583x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 651.0 | 622.5 | 698.6 | 25.1 | 0.611x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,061.1 | 1,046.4 | 1,077.5 | 9.0 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,064.7 | 1,052.4 | 1,103.3 | 16.6 | 1.000x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 110.0 | 109.8 | 116.9 | 2.7 | 0.104x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 113.2 | 113.1 | 113.4 | 0.1 | 0.107x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 173.6 | 172.6 | 178.5 | 2.0 | 0.164x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 208.2 | 207.9 | 208.9 | 0.4 | 0.196x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 416.4 | 403.8 | 432.7 | 9.9 | 0.393x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 588.0 | 558.4 | 608.3 | 18.4 | 0.554x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 623.8 | 609.8 | 660.7 | 18.9 | 0.588x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 638.6 | 610.8 | 662.3 | 17.7 | 0.602x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,060.6 | 1,050.8 | 1,073.5 | 6.7 | 1.000x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 56.7 | 56.5 | 56.9 | 0.2 | 0.145x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 57.5 | 56.8 | 58.0 | 0.4 | 0.147x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 109.4 | 109.0 | 111.5 | 0.9 | 0.279x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 336.1 | 315.7 | 355.8 | 13.6 | 0.858x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 387.3 | 382.4 | 398.6 | 4.3 | 0.989x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 391.7 | 385.9 | 414.8 | 7.7 | 1.000x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 481.4 | 472.2 | 528.3 | 20.0 | 1.229x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 490.3 | 475.9 | 497.3 | 8.7 | 1.252x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 506.0 | 462.8 | 519.1 | 21.4 | 1.292x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 50.6 | 50.4 | 50.6 | 0.1 | 0.020x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 51.0 | 51.0 | 51.3 | 0.1 | 0.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 265.4 | 264.2 | 268.1 | 1.3 | 0.104x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,450.3 | 1,410.7 | 1,532.1 | 41.0 | 0.569x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,641.1 | 1,553.6 | 1,748.0 | 62.4 | 0.644x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,834.6 | 1,767.6 | 1,853.1 | 30.6 | 0.720x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,856.0 | 1,805.3 | 1,875.9 | 25.1 | 0.728x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,865.9 | 1,816.2 | 1,885.9 | 27.0 | 0.732x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,548.9 | 2,534.5 | 2,622.8 | 24.7 | 1.000x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 136.8 | 136.3 | 137.0 | 0.2 | 0.123x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 157.4 | 157.1 | 166.4 | 3.6 | 0.141x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 224.2 | 223.3 | 235.1 | 4.4 | 0.201x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 452.2 | 438.9 | 466.1 | 8.6 | 0.405x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 619.6 | 606.8 | 763.4 | 58.8 | 0.556x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 665.6 | 612.3 | 700.1 | 31.2 | 0.597x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 669.1 | 631.5 | 675.1 | 16.6 | 0.600x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,112.6 | 1,099.7 | 1,148.2 | 13.5 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,115.4 | 1,100.9 | 1,173.1 | 20.2 | 1.000x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 129.3 | 129.1 | 129.4 | 0.1 | 0.117x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 132.8 | 132.5 | 133.3 | 0.3 | 0.120x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 175.5 | 174.7 | 179.2 | 1.7 | 0.158x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 214.2 | 213.6 | 223.5 | 3.8 | 0.193x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 419.1 | 410.0 | 424.4 | 5.2 | 0.378x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 623.3 | 562.9 | 634.5 | 26.2 | 0.562x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 650.8 | 638.1 | 670.9 | 10.6 | 0.587x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 654.1 | 599.2 | 682.5 | 27.6 | 0.590x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,109.4 | 1,103.4 | 1,165.7 | 17.2 | 1.000x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.9 | 96.7 | 97.5 | 0.3 | 0.084x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 118.3 | 118.1 | 123.6 | 2.1 | 0.103x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 169.9 | 169.3 | 173.8 | 1.7 | 0.148x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 387.5 | 337.2 | 400.6 | 22.8 | 0.337x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 573.8 | 555.6 | 624.5 | 23.4 | 0.499x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 587.3 | 502.4 | 627.7 | 41.2 | 0.511x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 589.7 | 587.4 | 643.0 | 21.4 | 0.513x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,145.6 | 1,130.0 | 1,167.5 | 9.4 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,149.7 | 1,132.6 | 1,167.0 | 9.8 | 1.000x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.9 | 89.6 | 90.1 | 0.2 | 0.079x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 93.5 | 93.2 | 93.8 | 0.2 | 0.082x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 110.8 | 109.0 | 113.1 | 1.2 | 0.097x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 171.9 | 171.5 | 172.4 | 0.3 | 0.150x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 378.7 | 356.0 | 421.3 | 21.7 | 0.331x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 579.0 | 549.3 | 615.6 | 24.9 | 0.506x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 590.9 | 574.4 | 612.8 | 14.8 | 0.516x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 603.5 | 560.5 | 682.1 | 44.6 | 0.527x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,144.9 | 1,133.1 | 1,196.9 | 19.8 | 1.000x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 138.8 | 137.3 | 154.1 | 6.2 | 0.204x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.2 | 149.5 | 150.4 | 0.3 | 0.221x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 169.6 | 169.6 | 176.7 | 2.8 | 0.250x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 333.5 | 295.2 | 368.3 | 24.5 | 0.491x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 537.8 | 458.9 | 584.8 | 45.2 | 0.792x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 564.8 | 520.9 | 693.4 | 58.5 | 0.831x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 572.4 | 525.2 | 628.4 | 32.9 | 0.843x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 679.4 | 672.6 | 692.7 | 5.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 683.1 | 677.8 | 695.0 | 5.3 | 1.005x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 99.3 | 98.3 | 106.5 | 2.3 | 0.146x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 141.4 | 141.1 | 141.8 | 0.2 | 0.207x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.1 | 142.0 | 143.1 | 0.4 | 0.208x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 145.5 | 145.2 | 146.4 | 0.5 | 0.213x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 355.9 | 324.9 | 366.3 | 15.2 | 0.522x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 530.8 | 480.7 | 583.3 | 34.9 | 0.778x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 538.2 | 516.9 | 640.6 | 43.6 | 0.789x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 548.8 | 493.2 | 585.9 | 32.8 | 0.805x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 681.9 | 672.2 | 708.9 | 9.9 | 1.000x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.2 | 123.2 | 123.8 | 0.2 | 0.109x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 143.3 | 143.2 | 149.5 | 2.5 | 0.126x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 170.6 | 170.0 | 172.0 | 0.7 | 0.150x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 390.9 | 344.7 | 402.3 | 20.3 | 0.345x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 552.4 | 443.6 | 577.8 | 47.0 | 0.487x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 555.0 | 467.7 | 571.8 | 37.9 | 0.489x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 558.7 | 550.1 | 630.6 | 31.3 | 0.493x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,128.0 | 1,121.4 | 1,138.2 | 5.6 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,134.2 | 1,124.5 | 1,173.3 | 12.9 | 1.000x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 107.2 | 106.5 | 112.4 | 2.0 | 0.095x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.5 | 115.3 | 116.2 | 0.3 | 0.102x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 119.4 | 119.3 | 119.4 | 0.0 | 0.106x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 172.7 | 172.4 | 172.9 | 0.2 | 0.153x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 380.0 | 356.2 | 422.4 | 21.7 | 0.336x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 570.7 | 560.1 | 621.0 | 22.0 | 0.505x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 576.8 | 558.3 | 691.1 | 51.8 | 0.511x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 589.0 | 541.4 | 613.1 | 24.1 | 0.522x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,129.3 | 1,115.4 | 1,201.5 | 24.0 | 1.000x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 97.0 | 96.6 | 100.9 | 1.6 | 0.084x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 118.1 | 118.1 | 123.8 | 2.3 | 0.103x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 173.4 | 173.4 | 173.5 | 0.1 | 0.151x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 393.4 | 377.5 | 401.0 | 8.4 | 0.343x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 512.9 | 466.1 | 545.4 | 28.4 | 0.447x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 546.5 | 512.8 | 605.9 | 36.6 | 0.476x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 560.5 | 504.1 | 594.4 | 29.7 | 0.488x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,147.8 | 1,138.9 | 1,160.3 | 6.7 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,151.9 | 1,139.1 | 1,167.6 | 7.5 | 1.004x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.7 | 89.5 | 90.5 | 0.4 | 0.078x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 93.5 | 93.1 | 95.3 | 0.8 | 0.081x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 109.2 | 108.4 | 111.9 | 1.1 | 0.095x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 176.0 | 175.7 | 176.5 | 0.3 | 0.153x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 381.7 | 360.1 | 387.5 | 9.7 | 0.332x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 590.9 | 518.2 | 645.9 | 41.9 | 0.514x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 591.3 | 513.3 | 631.4 | 48.7 | 0.515x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 612.6 | 565.1 | 690.5 | 46.0 | 0.533x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,149.1 | 1,139.4 | 1,181.1 | 14.8 | 1.000x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.4 | 123.1 | 123.9 | 0.3 | 0.108x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 143.3 | 143.2 | 153.4 | 4.0 | 0.126x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 175.9 | 175.6 | 176.1 | 0.2 | 0.154x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 418.7 | 388.7 | 429.4 | 15.5 | 0.367x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 486.9 | 432.4 | 528.0 | 35.4 | 0.427x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 526.1 | 455.2 | 655.5 | 65.1 | 0.461x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 529.2 | 486.7 | 539.9 | 21.3 | 0.464x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,138.9 | 1,123.3 | 1,172.7 | 15.4 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,141.0 | 1,126.8 | 1,154.0 | 7.3 | 1.000x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 107.1 | 106.3 | 108.1 | 0.5 | 0.094x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.8 | 115.8 | 116.2 | 0.2 | 0.102x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 119.3 | 119.1 | 119.5 | 0.1 | 0.105x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 178.4 | 178.0 | 180.2 | 0.8 | 0.157x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 390.7 | 370.1 | 412.0 | 13.3 | 0.344x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 562.2 | 499.5 | 618.4 | 42.4 | 0.496x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 581.4 | 524.1 | 658.0 | 48.5 | 0.513x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 585.1 | 561.8 | 643.9 | 32.6 | 0.516x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,134.4 | 1,124.9 | 1,177.2 | 16.9 | 1.000x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 138.6 | 137.6 | 141.0 | 1.3 | 0.204x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.0 | 149.8 | 156.1 | 2.4 | 0.221x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 173.4 | 169.6 | 175.9 | 2.5 | 0.256x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 354.9 | 297.0 | 387.5 | 29.8 | 0.524x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 509.5 | 453.8 | 571.6 | 40.5 | 0.752x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 535.4 | 448.0 | 648.9 | 67.3 | 0.790x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 546.9 | 527.9 | 624.2 | 33.8 | 0.807x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 677.8 | 673.6 | 691.4 | 6.2 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 678.9 | 672.5 | 751.0 | 22.4 | 1.002x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 98.7 | 98.3 | 100.3 | 0.6 | 0.145x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 141.8 | 141.1 | 142.1 | 0.3 | 0.209x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.1 | 142.1 | 148.3 | 2.5 | 0.209x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 145.9 | 145.3 | 146.2 | 0.4 | 0.215x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 357.5 | 299.8 | 403.2 | 35.3 | 0.526x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 530.1 | 509.0 | 601.9 | 34.5 | 0.780x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 552.1 | 525.9 | 582.3 | 18.9 | 0.812x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 562.1 | 522.0 | 615.9 | 35.9 | 0.827x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 679.8 | 673.5 | 694.0 | 7.2 | 1.000x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.3 | 149.6 | 153.8 | 1.5 | 0.140x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 169.6 | 169.5 | 175.7 | 2.5 | 0.158x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 171.5 | 170.9 | 175.8 | 1.8 | 0.159x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 410.1 | 384.3 | 428.0 | 16.3 | 0.381x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 504.7 | 477.0 | 568.0 | 30.5 | 0.469x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 527.4 | 484.3 | 556.5 | 26.6 | 0.490x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 538.0 | 515.0 | 628.3 | 39.8 | 0.500x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,074.3 | 1,059.0 | 1,093.0 | 10.8 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,076.2 | 1,056.1 | 1,089.9 | 10.0 | 1.000x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 104.3 | 103.9 | 105.4 | 0.5 | 0.097x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.2 | 141.7 | 143.9 | 0.8 | 0.132x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 145.4 | 145.3 | 145.9 | 0.2 | 0.135x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 173.4 | 172.9 | 173.6 | 0.2 | 0.161x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 385.5 | 377.2 | 405.5 | 9.4 | 0.358x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 560.5 | 520.8 | 609.5 | 30.4 | 0.521x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 564.4 | 548.6 | 590.6 | 17.5 | 0.525x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 609.1 | 551.0 | 681.8 | 45.6 | 0.566x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,075.4 | 1,069.8 | 1,106.4 | 11.8 | 1.000x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 44.0 | 43.6 | 44.3 | 0.2 | 0.057x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 45.2 | 45.0 | 45.5 | 0.2 | 0.058x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 187.9 | 185.9 | 189.9 | 1.4 | 0.241x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 430.1 | 412.8 | 448.3 | 11.6 | 0.552x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 554.4 | 542.5 | 581.7 | 15.3 | 0.712x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 555.1 | 534.4 | 604.5 | 23.8 | 0.713x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 572.6 | 555.8 | 622.2 | 22.7 | 0.735x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 778.6 | 772.5 | 816.0 | 11.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 779.0 | 770.9 | 797.4 | 7.4 | 1.000x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 37.8 | 37.6 | 37.9 | 0.1 | 0.014x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 38.2 | 38.1 | 38.3 | 0.1 | 0.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 220.7 | 211.0 | 229.5 | 4.6 | 0.082x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 934.3 | 902.9 | 1,079.8 | 62.5 | 0.348x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,103.3 | 1,076.8 | 1,138.0 | 20.0 | 0.411x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,419.9 | 1,409.4 | 1,436.4 | 10.9 | 0.529x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,427.2 | 1,379.3 | 1,448.9 | 23.6 | 0.532x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,429.5 | 1,392.0 | 1,528.8 | 45.9 | 0.533x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,684.2 | 2,657.5 | 2,824.8 | 48.7 | 1.000x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 89.6 | 89.3 | 89.9 | 0.2 | 0.115x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 91.0 | 90.7 | 91.3 | 0.2 | 0.116x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 189.4 | 183.2 | 190.8 | 2.9 | 0.242x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 428.7 | 419.7 | 438.6 | 7.5 | 0.549x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 553.4 | 540.8 | 592.4 | 20.1 | 0.709x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 553.9 | 531.4 | 563.7 | 13.2 | 0.709x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 564.8 | 555.1 | 613.9 | 20.9 | 0.723x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 779.4 | 763.3 | 805.4 | 10.8 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 781.0 | 774.9 | 789.3 | 5.1 | 1.000x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 83.2 | 83.1 | 83.6 | 0.2 | 0.031x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 83.6 | 83.3 | 83.7 | 0.1 | 0.031x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 233.2 | 231.4 | 237.8 | 2.3 | 0.087x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,675.6 | 2,648.7 | 2,794.6 | 43.5 | 1.000x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 3,330.5 | 3,291.4 | 3,432.4 | 57.7 | 1.245x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 3,345.6 | 3,284.5 | 3,384.5 | 32.4 | 1.250x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 4,412.9 | 4,402.6 | 4,447.4 | 15.7 | 1.649x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 4,423.8 | 4,355.4 | 4,445.3 | 33.3 | 1.653x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 4,456.4 | 4,346.2 | 4,548.4 | 71.4 | 1.666x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 43.7 | 43.5 | 44.0 | 0.2 | 0.056x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 44.9 | 44.8 | 45.2 | 0.2 | 0.058x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 186.9 | 186.4 | 188.5 | 0.8 | 0.240x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 426.7 | 416.0 | 429.9 | 5.0 | 0.548x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 557.0 | 531.4 | 570.4 | 15.1 | 0.716x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 568.4 | 554.5 | 589.5 | 14.4 | 0.730x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 574.6 | 550.8 | 616.8 | 26.0 | 0.738x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 778.4 | 772.1 | 801.7 | 7.8 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 778.6 | 770.3 | 804.2 | 9.8 | 1.000x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 37.6 | 37.5 | 39.0 | 0.6 | 0.014x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 38.0 | 38.0 | 38.1 | 0.0 | 0.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 218.8 | 213.3 | 228.9 | 4.0 | 0.082x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 872.6 | 842.3 | 902.4 | 20.0 | 0.326x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,047.5 | 962.9 | 1,095.6 | 45.5 | 0.391x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,447.1 | 1,409.9 | 1,531.8 | 41.7 | 0.541x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,450.7 | 1,440.5 | 1,503.3 | 23.9 | 0.542x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,488.1 | 1,340.5 | 1,520.2 | 64.8 | 0.556x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,675.7 | 2,650.7 | 2,785.1 | 45.3 | 1.000x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 60.0 | 59.5 | 60.2 | 0.2 | 0.077x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 61.7 | 61.6 | 68.9 | 2.9 | 0.079x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 189.6 | 187.0 | 190.6 | 1.3 | 0.243x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 423.7 | 411.5 | 433.4 | 8.0 | 0.543x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 554.7 | 546.4 | 563.4 | 6.2 | 0.711x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 567.0 | 553.3 | 617.6 | 25.9 | 0.726x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 577.4 | 553.8 | 584.0 | 11.1 | 0.740x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 780.6 | 774.7 | 800.8 | 7.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 781.2 | 770.2 | 816.8 | 14.3 | 1.001x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 53.8 | 53.6 | 53.9 | 0.1 | 0.020x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 54.1 | 54.0 | 54.8 | 0.3 | 0.020x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 233.4 | 229.7 | 238.3 | 2.6 | 0.087x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,410.3 | 1,381.0 | 1,550.0 | 60.5 | 0.528x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,558.2 | 1,539.8 | 1,605.6 | 22.2 | 0.583x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 2,029.2 | 1,989.0 | 2,113.6 | 44.2 | 0.759x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 2,051.3 | 1,992.1 | 2,109.4 | 38.1 | 0.767x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 2,079.6 | 1,997.4 | 2,176.5 | 58.9 | 0.778x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,673.5 | 2,654.2 | 2,807.1 | 46.1 | 1.000x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.6 | 50.4 | 50.9 | 0.2 | 0.055x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 52.1 | 51.6 | 52.4 | 0.3 | 0.056x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 303.9 | 266.3 | 321.7 | 19.6 | 0.328x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 527.3 | 490.7 | 560.8 | 23.1 | 0.570x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 594.5 | 564.5 | 639.2 | 24.7 | 0.643x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 610.8 | 597.9 | 615.1 | 7.2 | 0.660x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 634.0 | 591.0 | 647.5 | 20.4 | 0.685x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 925.1 | 915.9 | 953.5 | 10.6 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 931.6 | 912.3 | 966.5 | 16.9 | 1.007x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.2 | 44.1 | 44.3 | 0.1 | 0.013x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.8 | 44.6 | 45.0 | 0.1 | 0.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 324.3 | 314.0 | 332.2 | 6.4 | 0.099x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,742.4 | 1,735.8 | 1,750.6 | 5.0 | 0.532x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,746.4 | 1,722.4 | 1,856.2 | 52.7 | 0.533x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,771.6 | 1,739.3 | 1,793.5 | 20.2 | 0.541x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,786.6 | 1,707.7 | 1,827.8 | 45.8 | 0.546x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,930.6 | 1,920.3 | 1,943.1 | 8.0 | 0.590x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,274.3 | 3,255.3 | 3,414.3 | 47.3 | 1.000x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.4 | 50.0 | 50.7 | 0.2 | 0.058x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 51.3 | 51.2 | 52.3 | 0.4 | 0.059x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 268.8 | 255.5 | 298.7 | 15.9 | 0.309x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 513.0 | 507.4 | 551.9 | 16.7 | 0.589x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 600.9 | 574.8 | 621.8 | 17.5 | 0.690x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 610.4 | 577.4 | 638.2 | 20.1 | 0.701x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 611.1 | 590.1 | 637.0 | 16.7 | 0.702x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 870.5 | 864.0 | 913.9 | 14.1 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 872.5 | 861.9 | 896.1 | 10.0 | 1.002x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.0 | 43.9 | 44.6 | 0.3 | 0.014x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.7 | 44.5 | 44.8 | 0.1 | 0.015x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 329.1 | 316.7 | 346.8 | 8.7 | 0.108x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,726.9 | 1,719.7 | 1,740.3 | 7.3 | 0.568x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,756.7 | 1,714.1 | 1,781.6 | 25.9 | 0.578x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,767.7 | 1,715.8 | 1,805.5 | 31.6 | 0.582x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,780.4 | 1,716.8 | 1,802.8 | 35.0 | 0.586x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,924.4 | 1,898.8 | 1,977.8 | 26.4 | 0.633x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,038.6 | 3,012.1 | 3,186.7 | 61.0 | 1.000x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 37.0 | 37.0 | 37.1 | 0.1 | 0.029x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 39.1 | 38.6 | 39.4 | 0.3 | 0.031x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.4 | 152.1 | 153.7 | 0.6 | 0.122x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 375.4 | 348.9 | 380.0 | 11.4 | 0.298x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 520.4 | 488.8 | 579.5 | 29.7 | 0.414x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 535.8 | 504.5 | 568.8 | 22.2 | 0.426x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 536.8 | 500.6 | 557.1 | 20.5 | 0.427x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,252.4 | 1,245.3 | 1,311.8 | 20.8 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,257.9 | 1,242.9 | 1,286.5 | 11.4 | 1.000x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.2 | 31.1 | 31.2 | 0.0 | 0.007x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 31.8 | 31.8 | 31.9 | 0.1 | 0.007x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 387.9 | 377.1 | 390.7 | 4.1 | 0.083x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 682.7 | 664.0 | 728.8 | 24.9 | 0.147x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 860.2 | 810.2 | 901.9 | 31.9 | 0.185x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,034.4 | 1,006.6 | 1,133.9 | 47.1 | 0.223x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,045.1 | 998.1 | 1,076.8 | 29.7 | 0.225x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,065.5 | 1,032.4 | 1,091.0 | 20.1 | 0.229x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 4,647.2 | 4,611.0 | 4,784.4 | 57.3 | 1.000x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.3 | 50.1 | 50.4 | 0.1 | 0.032x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 51.7 | 51.5 | 52.4 | 0.3 | 0.033x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 387.6 | 385.4 | 391.0 | 2.0 | 0.245x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 708.9 | 703.6 | 712.0 | 2.8 | 0.449x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 731.3 | 707.9 | 793.0 | 29.1 | 0.463x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 752.5 | 739.4 | 831.3 | 33.6 | 0.476x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 767.8 | 698.3 | 793.0 | 31.8 | 0.486x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,580.1 | 1,569.0 | 1,612.0 | 14.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,584.9 | 1,567.9 | 1,618.9 | 15.0 | 1.003x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.0 | 43.9 | 44.0 | 0.0 | 0.007x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.4 | 44.3 | 44.4 | 0.0 | 0.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 487.2 | 472.9 | 523.3 | 13.5 | 0.083x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,776.0 | 1,763.2 | 1,791.0 | 8.8 | 0.301x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,966.7 | 1,949.6 | 2,006.1 | 21.2 | 0.333x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 2,285.0 | 2,243.8 | 2,352.5 | 36.6 | 0.387x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 2,289.2 | 2,218.5 | 2,367.3 | 58.8 | 0.388x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 2,291.2 | 2,217.7 | 2,301.8 | 31.6 | 0.388x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 5,900.8 | 5,878.7 | 6,023.9 | 50.7 | 1.000x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.2 | 53.1 | 53.3 | 0.1 | 0.084x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 54.3 | 53.6 | 60.2 | 2.4 | 0.086x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.3 | 152.0 | 156.2 | 1.5 | 0.243x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 377.2 | 363.4 | 383.3 | 6.8 | 0.599x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 545.2 | 524.6 | 568.4 | 16.6 | 0.866x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 549.7 | 535.4 | 561.7 | 9.8 | 0.873x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 564.2 | 538.7 | 618.5 | 26.6 | 0.896x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 629.9 | 622.7 | 643.5 | 6.7 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 631.3 | 622.0 | 652.4 | 8.2 | 1.002x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.7 | 47.7 | 47.8 | 0.0 | 0.023x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 48.3 | 48.1 | 48.7 | 0.2 | 0.023x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 195.2 | 194.4 | 197.7 | 0.9 | 0.094x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,506.0 | 1,491.2 | 1,601.6 | 39.5 | 0.722x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,682.0 | 1,621.0 | 1,767.1 | 47.5 | 0.806x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,964.5 | 1,947.4 | 2,031.3 | 29.0 | 0.942x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,970.7 | 1,967.2 | 2,012.3 | 19.0 | 0.945x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,983.5 | 1,906.7 | 2,002.5 | 35.9 | 0.951x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,085.7 | 2,062.7 | 2,171.6 | 34.2 | 1.000x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.3 | 40.3 | 40.5 | 0.1 | 0.048x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 41.8 | 41.7 | 42.2 | 0.2 | 0.049x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 214.9 | 213.6 | 216.1 | 0.9 | 0.254x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 438.4 | 431.9 | 455.9 | 8.4 | 0.518x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 585.7 | 569.5 | 630.3 | 21.3 | 0.692x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 589.5 | 571.7 | 640.2 | 26.9 | 0.696x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 608.1 | 526.8 | 642.4 | 39.7 | 0.718x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 843.1 | 834.8 | 850.2 | 4.7 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 846.7 | 834.7 | 859.4 | 7.2 | 1.000x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.9 | 34.7 | 35.6 | 0.3 | 0.012x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 36.3 | 36.1 | 36.5 | 0.1 | 0.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 286.6 | 281.1 | 316.1 | 9.2 | 0.098x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,226.7 | 1,155.4 | 1,242.3 | 31.9 | 0.419x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,503.4 | 1,446.5 | 1,570.2 | 40.8 | 0.513x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,510.7 | 1,461.9 | 1,558.1 | 32.8 | 0.516x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,514.4 | 1,433.5 | 1,521.9 | 37.0 | 0.517x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,524.5 | 1,483.7 | 1,532.7 | 17.9 | 0.520x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,930.0 | 2,908.2 | 3,070.2 | 46.2 | 1.000x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.1 | 52.8 | 53.2 | 0.2 | 0.053x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 55.1 | 54.1 | 55.3 | 0.4 | 0.055x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 473.1 | 354.4 | 493.9 | 50.8 | 0.470x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 645.7 | 614.6 | 665.0 | 17.4 | 0.641x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 676.8 | 623.7 | 687.6 | 25.1 | 0.672x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 697.9 | 637.7 | 727.9 | 34.3 | 0.693x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 698.6 | 692.3 | 732.6 | 14.8 | 0.694x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,002.7 | 995.7 | 1,043.2 | 14.3 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,007.3 | 995.2 | 1,056.9 | 16.4 | 1.000x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.8 | 47.6 | 47.8 | 0.1 | 0.013x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 48.3 | 48.1 | 48.4 | 0.1 | 0.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 569.6 | 565.0 | 581.0 | 4.4 | 0.159x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 2,453.6 | 2,449.3 | 2,520.2 | 32.4 | 0.683x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 2,501.9 | 2,481.9 | 2,548.1 | 24.7 | 0.697x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 2,507.4 | 2,486.5 | 2,517.1 | 11.1 | 0.698x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 2,869.1 | 2,862.9 | 2,924.6 | 22.7 | 0.799x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 3,089.5 | 3,049.7 | 3,169.4 | 41.6 | 0.861x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,590.0 | 3,562.9 | 4,022.8 | 131.5 | 1.000x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 108.0 | 107.3 | 110.1 | 1.0 | 0.284x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.7 | 110.4 | 110.8 | 0.2 | 0.291x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 112.1 | 111.9 | 112.3 | 0.1 | 0.295x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 325.8 | 311.8 | 340.1 | 10.8 | 0.858x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 379.9 | 374.7 | 395.1 | 5.5 | 1.000x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 380.9 | 372.3 | 420.9 | 14.1 | 1.003x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 473.6 | 436.1 | 493.7 | 19.2 | 1.247x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 480.7 | 444.8 | 524.4 | 31.9 | 1.265x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 500.0 | 436.8 | 515.3 | 28.6 | 1.316x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 105.5 | 105.3 | 106.0 | 0.2 | 0.068x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 109.0 | 108.8 | 109.1 | 0.1 | 0.070x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 211.8 | 210.0 | 216.7 | 1.8 | 0.136x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 305.2 | 299.9 | 346.0 | 17.1 | 0.196x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 496.5 | 486.9 | 500.7 | 4.9 | 0.319x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 698.7 | 671.1 | 719.9 | 16.6 | 0.450x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 706.4 | 656.3 | 759.8 | 36.0 | 0.455x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 748.1 | 672.6 | 775.8 | 35.7 | 0.481x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,554.2 | 1,527.7 | 1,637.2 | 28.7 | 1.000x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 33.6 | 32.7 | 35.3 | 0.8 | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 34.5 | 33.5 | 35.3 | 0.6 | 1.027x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 46.9 | 46.8 | 48.0 | 0.5 | 1.398x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 48.4 | 48.3 | 48.6 | 0.1 | 1.443x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 262.8 | 258.8 | 273.7 | 5.0 | 7.829x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 482.7 | 480.2 | 484.0 | 1.4 | 14.382x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 644.3 | 623.7 | 682.0 | 22.5 | 19.199x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 668.5 | 645.5 | 690.6 | 17.5 | 19.917x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 707.1 | 638.4 | 724.9 | 37.0 | 21.069x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.1 | 34.0 | 52.3 | 5.2 | 1.000x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 40.9 | 40.6 | 41.1 | 0.2 | 1.168x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 41.0 | 40.9 | 41.1 | 0.1 | 1.169x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 44.4 | 44.3 | 48.5 | 1.2 | 1.266x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,827.1 | 1,752.0 | 1,865.2 | 39.7 | 52.127x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,965.6 | 1,848.9 | 2,066.3 | 87.9 | 56.080x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 2,193.6 | 2,189.2 | 2,204.8 | 5.9 | 62.586x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 2,214.4 | 2,211.8 | 2,245.4 | 13.1 | 63.177x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 2,224.4 | 2,124.1 | 2,352.7 | 89.9 | 63.464x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 34.3 | 33.5 | 34.7 | 0.5 | 0.212x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 35.6 | 35.4 | 35.7 | 0.1 | 0.220x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 54.8 | 54.5 | 54.9 | 0.2 | 0.338x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 162.1 | 159.3 | 165.8 | 1.8 | 1.000x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 163.2 | 159.3 | 168.9 | 2.6 | 1.007x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 277.7 | 270.0 | 293.1 | 8.0 | 1.714x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 418.1 | 401.8 | 456.7 | 21.1 | 2.580x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 428.8 | 422.0 | 455.5 | 13.9 | 2.646x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 429.6 | 409.5 | 451.9 | 14.6 | 2.651x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 29.6 | 29.5 | 30.2 | 0.2 | 0.164x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 29.8 | 29.7 | 30.6 | 0.3 | 0.165x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 54.8 | 54.6 | 64.6 | 2.9 | 0.304x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 180.2 | 177.5 | 197.2 | 6.8 | 1.000x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 949.6 | 924.5 | 1,024.5 | 38.4 | 5.270x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,183.8 | 1,079.5 | 1,246.3 | 64.5 | 6.569x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,342.9 | 1,289.5 | 1,407.5 | 40.5 | 7.451x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,359.6 | 1,344.5 | 1,379.8 | 12.6 | 7.544x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,371.7 | 1,359.5 | 1,408.8 | 16.9 | 7.612x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 17.6 | 17.6 | 17.7 | 0.1 | 0.029x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 18.8 | 18.5 | 18.9 | 0.1 | 0.031x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 82.9 | 79.7 | 103.2 | 10.6 | 0.136x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 291.5 | 283.9 | 320.4 | 13.3 | 0.477x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 504.3 | 485.4 | 581.2 | 35.2 | 0.825x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 517.4 | 415.0 | 536.9 | 46.7 | 0.847x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 530.1 | 471.9 | 549.7 | 27.1 | 0.868x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 611.1 | 602.7 | 624.2 | 5.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 613.1 | 603.8 | 623.7 | 6.0 | 1.003x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 12.6 | 12.5 | 12.9 | 0.1 | 0.020x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 12.9 | 12.9 | 13.1 | 0.1 | 0.021x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 84.4 | 83.2 | 129.7 | 13.5 | 0.135x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 176.5 | 174.1 | 180.6 | 2.1 | 0.283x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 370.1 | 369.0 | 383.3 | 5.5 | 0.594x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 623.5 | 614.2 | 1,078.8 | 136.7 | 1.000x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 712.9 | 705.4 | 802.1 | 35.9 | 1.143x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 737.3 | 704.8 | 742.0 | 15.3 | 1.183x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 740.5 | 695.8 | 772.1 | 25.4 | 1.188x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 130.4 | 130.3 | 131.6 | 0.5 | 0.226x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 132.3 | 132.1 | 132.6 | 0.2 | 0.230x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 151.6 | 150.7 | 153.4 | 0.9 | 0.263x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 379.8 | 369.3 | 417.5 | 17.5 | 0.659x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 522.2 | 506.5 | 566.0 | 20.3 | 0.906x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 562.0 | 503.7 | 574.5 | 25.7 | 0.975x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 571.1 | 463.8 | 584.6 | 49.9 | 0.991x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 575.4 | 567.6 | 584.8 | 5.9 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 576.1 | 569.9 | 600.1 | 9.2 | 1.000x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 124.9 | 124.6 | 131.7 | 2.7 | 0.045x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 127.9 | 127.6 | 128.1 | 0.2 | 0.046x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 290.5 | 285.7 | 293.5 | 2.0 | 0.104x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 722.6 | 668.4 | 751.2 | 29.4 | 0.258x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 955.0 | 924.2 | 988.0 | 20.8 | 0.342x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 998.8 | 945.8 | 1,026.1 | 28.5 | 0.357x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,001.7 | 980.7 | 1,040.1 | 22.7 | 0.358x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,012.3 | 969.5 | 1,046.1 | 27.2 | 0.362x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,796.2 | 2,772.4 | 2,875.0 | 34.1 | 1.000x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 54.6 | 54.5 | 55.3 | 0.3 | 0.335x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 112.2 | 111.6 | 114.4 | 1.0 | 0.688x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 113.1 | 113.1 | 113.2 | 0.1 | 0.693x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 161.8 | 158.6 | 168.8 | 2.5 | 0.991x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 163.2 | 160.8 | 165.8 | 1.8 | 1.000x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 287.0 | 280.3 | 306.7 | 9.8 | 1.759x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 419.6 | 389.7 | 467.6 | 26.1 | 2.572x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 424.5 | 371.3 | 432.2 | 22.1 | 2.602x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 428.1 | 392.2 | 459.5 | 22.8 | 2.624x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 107.4 | 107.0 | 107.9 | 0.3 | 0.106x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 110.5 | 110.3 | 111.2 | 0.3 | 0.109x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 159.7 | 158.0 | 166.0 | 2.1 | 0.158x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 172.2 | 171.8 | 173.8 | 0.7 | 0.170x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 385.4 | 366.2 | 398.8 | 12.2 | 0.380x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 533.0 | 472.7 | 583.9 | 37.9 | 0.526x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 549.5 | 501.4 | 566.0 | 23.0 | 0.542x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 568.6 | 535.4 | 640.6 | 38.5 | 0.561x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,013.9 | 997.2 | 1,038.0 | 9.9 | 1.000x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 49.8 | 49.5 | 50.1 | 0.2 | 0.087x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 51.8 | 51.1 | 51.8 | 0.3 | 0.090x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 150.9 | 149.8 | 152.1 | 0.9 | 0.262x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 368.1 | 363.8 | 418.1 | 20.3 | 0.640x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 530.6 | 460.8 | 573.5 | 40.4 | 0.923x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 542.5 | 521.8 | 601.5 | 27.0 | 0.943x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 565.8 | 537.6 | 607.1 | 23.8 | 0.984x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 575.1 | 569.5 | 653.3 | 23.7 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 577.9 | 572.4 | 602.9 | 8.8 | 1.005x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.1 | 44.0 | 44.3 | 0.1 | 0.022x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.6 | 44.3 | 45.7 | 0.5 | 0.022x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 199.5 | 196.0 | 201.8 | 1.8 | 0.100x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,405.0 | 1,296.7 | 1,600.0 | 104.9 | 0.706x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,596.6 | 1,501.8 | 1,783.2 | 108.5 | 0.802x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,804.6 | 1,790.8 | 1,828.1 | 13.0 | 0.906x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,819.9 | 1,796.6 | 1,844.0 | 15.9 | 0.914x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,823.7 | 1,798.6 | 1,844.7 | 16.1 | 0.916x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,991.3 | 1,977.0 | 2,259.9 | 86.8 | 1.000x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 36.7 | 36.5 | 36.9 | 0.1 | 0.037x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 38.6 | 38.6 | 39.0 | 0.2 | 0.039x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 378.2 | 354.2 | 414.8 | 21.3 | 0.378x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 597.5 | 585.8 | 633.8 | 17.3 | 0.597x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 666.3 | 641.0 | 687.0 | 15.1 | 0.666x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 671.0 | 637.4 | 705.9 | 27.3 | 0.671x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 688.3 | 638.3 | 707.5 | 27.9 | 0.688x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 998.1 | 987.6 | 1,018.2 | 8.7 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,000.6 | 991.0 | 1,009.0 | 5.7 | 1.000x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.1 | 31.0 | 31.2 | 0.0 | 0.009x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 31.8 | 31.6 | 31.9 | 0.1 | 0.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 538.1 | 535.8 | 543.8 | 2.8 | 0.152x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,731.2 | 1,717.7 | 1,776.5 | 21.3 | 0.491x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,908.3 | 1,889.9 | 1,944.9 | 19.2 | 0.541x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,967.0 | 1,883.7 | 2,010.0 | 45.3 | 0.557x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,969.6 | 1,960.7 | 1,982.3 | 8.0 | 0.558x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,971.3 | 1,927.4 | 1,996.9 | 29.1 | 0.559x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,528.6 | 3,496.4 | 3,605.1 | 35.2 | 1.000x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.1 | 39.9 | 40.6 | 0.3 | 0.025x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 42.4 | 42.1 | 42.6 | 0.1 | 0.026x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 152.6 | 151.7 | 154.6 | 1.0 | 0.094x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 387.1 | 380.6 | 389.5 | 3.1 | 0.239x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 524.4 | 493.6 | 564.7 | 24.8 | 0.323x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 527.0 | 499.6 | 570.7 | 29.9 | 0.325x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 562.0 | 518.5 | 587.1 | 23.9 | 0.346x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,616.2 | 1,598.4 | 1,660.0 | 17.6 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,622.0 | 1,606.5 | 2,287.1 | 199.0 | 1.000x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.7 | 34.3 | 35.1 | 0.3 | 0.006x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 34.9 | 34.9 | 35.2 | 0.1 | 0.006x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 472.6 | 464.6 | 485.2 | 6.4 | 0.078x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 716.3 | 715.3 | 795.3 | 33.6 | 0.119x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 981.5 | 929.3 | 1,039.0 | 40.0 | 0.163x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,127.6 | 1,077.0 | 1,158.3 | 27.4 | 0.187x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,130.6 | 1,122.5 | 1,163.5 | 15.6 | 0.187x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,133.5 | 1,108.0 | 1,196.4 | 31.0 | 0.188x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 6,039.8 | 6,006.5 | 6,262.3 | 83.8 | 1.000x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 22.4 | 22.1 | 22.7 | 0.2 | 0.029x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 23.9 | 23.6 | 24.0 | 0.1 | 0.031x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 110.0 | 109.7 | 111.4 | 0.6 | 0.141x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 345.5 | 342.6 | 347.4 | 2.0 | 0.444x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 494.5 | 427.4 | 527.2 | 34.1 | 0.636x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 528.8 | 495.9 | 559.5 | 23.3 | 0.680x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 529.7 | 480.2 | 550.1 | 23.9 | 0.681x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 777.8 | 774.3 | 1,213.4 | 130.1 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 779.3 | 773.4 | 806.5 | 9.2 | 1.002x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 18.2 | 18.2 | 18.6 | 0.2 | 0.009x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 18.7 | 18.6 | 18.8 | 0.1 | 0.009x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 186.8 | 178.9 | 191.5 | 3.4 | 0.092x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 312.3 | 310.8 | 325.1 | 5.3 | 0.154x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 555.3 | 528.5 | 599.0 | 24.8 | 0.274x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 751.4 | 750.3 | 777.4 | 11.8 | 0.371x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 773.0 | 744.6 | 847.8 | 35.4 | 0.381x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 791.9 | 753.2 | 810.8 | 19.4 | 0.391x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,027.2 | 2,008.6 | 2,116.1 | 31.4 | 1.000x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 126.8 | 126.6 | 129.0 | 0.9 | 0.232x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 128.6 | 128.5 | 129.4 | 0.3 | 0.235x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 134.8 | 132.9 | 137.0 | 1.3 | 0.246x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 368.1 | 348.5 | 375.8 | 9.5 | 0.673x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 516.9 | 464.7 | 539.4 | 25.4 | 0.945x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 528.4 | 494.5 | 632.1 | 56.5 | 0.966x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 547.0 | 541.9 | 855.6 | 92.9 | 1.000x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 547.0 | 537.9 | 554.8 | 4.1 | 1.000x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 559.4 | 541.4 | 584.5 | 15.4 | 1.023x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 121.8 | 121.5 | 122.2 | 0.3 | 0.047x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 125.2 | 124.8 | 126.6 | 0.7 | 0.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 272.3 | 270.0 | 275.9 | 1.7 | 0.106x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 591.0 | 587.3 | 608.8 | 7.8 | 0.229x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 802.6 | 787.6 | 836.3 | 16.7 | 0.312x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 836.5 | 794.4 | 867.2 | 25.7 | 0.325x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 872.4 | 839.7 | 932.8 | 31.6 | 0.339x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 896.6 | 837.1 | 901.7 | 26.0 | 0.348x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,576.6 | 2,545.5 | 2,632.3 | 29.9 | 1.000x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 100.9 | 100.6 | 101.3 | 0.3 | 0.132x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 102.6 | 102.5 | 102.8 | 0.1 | 0.134x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 247.5 | 232.8 | 262.6 | 10.1 | 0.323x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 483.7 | 473.0 | 529.5 | 20.9 | 0.632x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 546.5 | 510.6 | 619.4 | 41.9 | 0.714x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 572.6 | 526.5 | 591.2 | 24.1 | 0.748x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 601.6 | 551.0 | 655.7 | 39.6 | 0.786x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 765.6 | 755.4 | 937.8 | 52.0 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 766.2 | 758.2 | 785.3 | 8.4 | 1.001x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 95.6 | 95.4 | 97.8 | 0.9 | 0.027x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 99.3 | 99.1 | 100.0 | 0.4 | 0.028x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 380.8 | 374.5 | 392.7 | 5.4 | 0.108x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,035.9 | 1,023.5 | 1,043.6 | 7.7 | 0.294x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,164.0 | 1,076.4 | 1,177.1 | 41.3 | 0.331x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,194.0 | 1,146.4 | 1,201.8 | 23.6 | 0.339x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,199.4 | 1,084.9 | 1,229.9 | 49.7 | 0.341x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,203.9 | 1,186.7 | 1,246.7 | 21.5 | 0.342x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,519.9 | 3,492.4 | 3,625.9 | 44.4 | 1.000x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 126.6 | 126.5 | 130.0 | 1.3 | 0.231x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 128.3 | 128.3 | 128.6 | 0.2 | 0.234x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 133.0 | 131.1 | 135.2 | 1.3 | 0.243x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 365.7 | 362.1 | 383.5 | 7.6 | 0.667x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 504.6 | 478.3 | 556.9 | 31.1 | 0.921x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 547.4 | 518.0 | 575.6 | 21.9 | 0.999x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 548.0 | 540.1 | 894.6 | 104.4 | 1.000x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 549.1 | 544.4 | 605.7 | 17.3 | 1.002x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 558.9 | 482.5 | 613.8 | 44.5 | 1.020x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 122.3 | 121.5 | 123.7 | 0.7 | 0.048x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 125.0 | 124.7 | 125.7 | 0.4 | 0.049x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 274.3 | 272.6 | 277.9 | 1.9 | 0.107x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 593.9 | 549.8 | 602.7 | 21.1 | 0.232x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 814.2 | 802.1 | 820.9 | 6.6 | 0.317x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 825.8 | 751.8 | 855.8 | 35.1 | 0.322x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 883.0 | 822.9 | 888.7 | 24.9 | 0.344x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 886.3 | 843.0 | 892.6 | 18.8 | 0.346x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,565.2 | 2,554.3 | 2,639.2 | 27.3 | 1.000x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 37.8 | 37.5 | 37.9 | 0.1 | 0.048x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 39.1 | 38.9 | 39.7 | 0.3 | 0.050x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.0 | 151.3 | 154.4 | 1.2 | 0.196x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 384.9 | 376.8 | 397.6 | 7.3 | 0.494x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 521.4 | 495.6 | 536.5 | 18.0 | 0.669x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 526.5 | 505.2 | 577.8 | 28.3 | 0.676x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 532.4 | 482.6 | 552.4 | 23.7 | 0.683x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 779.4 | 772.5 | 808.0 | 12.2 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 781.8 | 771.6 | 792.0 | 7.1 | 1.003x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.8 | 31.5 | 32.0 | 0.2 | 0.012x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 32.6 | 32.5 | 32.7 | 0.1 | 0.012x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 217.5 | 213.5 | 221.2 | 2.8 | 0.081x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 666.9 | 613.8 | 722.7 | 40.8 | 0.249x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 843.2 | 820.2 | 941.9 | 48.7 | 0.314x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,037.6 | 980.6 | 1,059.1 | 28.7 | 0.387x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,054.8 | 1,036.4 | 1,095.0 | 20.1 | 0.393x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,069.2 | 1,015.0 | 1,077.0 | 23.1 | 0.399x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,681.8 | 2,654.8 | 2,807.6 | 48.1 | 1.000x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 28.1 | 27.9 | 28.6 | 0.2 | 0.036x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 29.3 | 28.9 | 29.5 | 0.2 | 0.038x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.4 | 151.7 | 156.3 | 1.5 | 0.197x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 380.2 | 377.6 | 393.2 | 5.7 | 0.489x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 521.8 | 479.2 | 530.7 | 18.7 | 0.671x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 538.6 | 507.1 | 556.7 | 20.0 | 0.692x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 544.6 | 519.3 | 564.2 | 18.0 | 0.700x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 776.9 | 772.6 | 782.4 | 2.9 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 777.9 | 769.7 | 799.0 | 7.8 | 1.000x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.4 | 21.3 | 21.9 | 0.3 | 0.008x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.7 | 21.6 | 21.7 | 0.1 | 0.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 218.1 | 212.6 | 221.0 | 2.3 | 0.082x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 626.1 | 559.4 | 645.1 | 30.2 | 0.234x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 866.7 | 807.3 | 885.9 | 35.6 | 0.324x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 963.8 | 949.9 | 1,000.8 | 17.5 | 0.361x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 987.0 | 925.0 | 1,004.0 | 28.9 | 0.369x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,026.6 | 951.7 | 1,145.8 | 72.1 | 0.384x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,671.6 | 2,655.5 | 2,804.0 | 44.6 | 1.000x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 27.8 | 27.7 | 29.1 | 0.5 | 0.036x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 29.0 | 29.0 | 29.7 | 0.3 | 0.037x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.0 | 151.9 | 154.7 | 1.0 | 0.197x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 384.5 | 366.1 | 417.1 | 16.6 | 0.494x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 517.0 | 492.4 | 517.5 | 10.2 | 0.664x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 542.4 | 497.5 | 574.1 | 30.9 | 0.697x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 550.3 | 522.8 | 567.2 | 14.4 | 0.707x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 778.0 | 769.0 | 806.3 | 11.8 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 780.8 | 769.1 | 900.7 | 36.9 | 1.004x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.4 | 21.3 | 21.5 | 0.1 | 0.008x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.6 | 21.5 | 21.7 | 0.1 | 0.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 217.4 | 214.8 | 226.9 | 3.4 | 0.081x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 618.0 | 539.0 | 634.2 | 37.7 | 0.231x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 830.2 | 777.7 | 898.4 | 40.1 | 0.310x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 956.6 | 939.0 | 975.3 | 12.8 | 0.357x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 993.6 | 939.4 | 1,021.4 | 27.6 | 0.371x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 999.8 | 915.6 | 1,021.5 | 38.8 | 0.373x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,678.2 | 2,658.3 | 2,807.3 | 44.4 | 1.000x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 27.9 | 27.8 | 28.2 | 0.2 | 0.036x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 29.4 | 29.4 | 29.7 | 0.1 | 0.038x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.0 | 151.6 | 154.0 | 0.9 | 0.197x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 389.6 | 372.6 | 403.8 | 10.6 | 0.501x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 514.4 | 459.1 | 541.2 | 27.7 | 0.662x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 532.3 | 499.1 | 568.8 | 22.3 | 0.685x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 546.2 | 510.3 | 582.1 | 26.8 | 0.703x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 777.0 | 774.0 | 792.4 | 5.5 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 780.1 | 771.0 | 790.7 | 5.8 | 1.004x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.4 | 21.3 | 22.1 | 0.4 | 0.008x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.7 | 21.6 | 21.9 | 0.1 | 0.008x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 220.2 | 212.4 | 224.4 | 3.4 | 0.082x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 634.7 | 620.1 | 650.7 | 11.0 | 0.237x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 849.2 | 838.2 | 934.0 | 34.9 | 0.317x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 980.4 | 924.3 | 1,062.0 | 45.1 | 0.366x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 981.3 | 957.7 | 1,016.7 | 19.8 | 0.366x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 994.7 | 950.2 | 1,014.5 | 23.6 | 0.371x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,679.8 | 2,664.7 | 2,783.2 | 37.4 | 1.000x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 31.0 | 30.8 | 31.2 | 0.1 | 0.040x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 32.4 | 31.8 | 32.6 | 0.3 | 0.042x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.1 | 151.6 | 153.7 | 0.7 | 0.197x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 385.0 | 357.9 | 389.0 | 11.2 | 0.496x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 523.5 | 511.5 | 552.9 | 15.6 | 0.674x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 523.7 | 490.4 | 559.6 | 23.3 | 0.675x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 552.5 | 525.7 | 559.0 | 11.6 | 0.712x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 776.4 | 772.4 | 786.9 | 4.0 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 779.6 | 768.5 | 836.1 | 20.4 | 1.004x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 25.7 | 25.4 | 26.1 | 0.3 | 0.010x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 25.8 | 25.8 | 26.0 | 0.1 | 0.010x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 219.9 | 212.0 | 223.2 | 3.1 | 0.082x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 631.8 | 592.5 | 680.3 | 31.1 | 0.236x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 871.3 | 790.0 | 885.4 | 35.4 | 0.326x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 963.0 | 955.7 | 1,035.0 | 29.8 | 0.360x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 979.1 | 965.2 | 1,013.2 | 17.5 | 0.366x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 994.4 | 971.7 | 1,031.0 | 21.8 | 0.372x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,676.3 | 2,660.0 | 2,799.8 | 41.9 | 1.000x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 7,760.7 | 7,745.9 | 7,830.2 | 31.7 | 0.762x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 7,956.4 | 7,935.7 | 8,054.4 | 43.8 | 0.781x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 8,184.1 | 8,180.3 | 8,248.8 | 28.3 | 0.803x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 8,202.1 | 8,134.9 | 8,275.5 | 44.9 | 0.805x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 8,249.6 | 8,134.0 | 8,379.3 | 89.4 | 0.810x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 10,168.6 | 10,140.6 | 10,337.4 | 75.3 | 0.998x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 10,190.1 | 10,133.1 | 12,308.1 | 630.7 | 1.000x |
| 8 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 67,112.4 | 67,072.0 | 67,355.6 | 102.4 | 6.586x |
| 9 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 67,152.5 | 67,079.1 | 67,271.9 | 62.1 | 6.590x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 26,262.1 | 26,253.5 | 26,452.6 | 76.4 | 0.144x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 26,281.2 | 26,263.3 | 26,305.9 | 14.8 | 0.144x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 29,394.6 | 29,113.7 | 29,479.6 | 143.2 | 0.161x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 182,237.1 | 180,436.3 | 184,232.2 | 1,167.2 | 1.000x | 10 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 182,322.0 | 181,127.7 | 188,510.3 | 2,244.9 | 1.000x | 10 | 100% |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 33,608.2 | 33,597.6 | 33,621.4 | 9.4 | 0.115x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 33,634.5 | 33,567.7 | 33,716.8 | 48.8 | 0.115x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 72,651.8 | 71,878.3 | 73,309.0 | 508.4 | 0.249x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 291,684.5 | 289,946.2 | 295,500.6 | 1,592.9 | 1.000x | 10 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 291,698.9 | 290,416.5 | 294,468.6 | 1,275.8 | 1.000x | 10 | 100% |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 33,349.5 | 33,336.0 | 33,495.3 | 60.9 | 0.039x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 33,360.5 | 33,343.1 | 33,405.8 | 25.2 | 0.039x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 194,929.3 | 194,669.2 | 195,582.5 | 342.7 | 0.227x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 195,025.4 | 194,449.5 | 206,100.3 | 4,460.5 | 0.227x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 199,473.7 | 198,611.8 | 199,797.7 | 414.8 | 0.232x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 199,566.3 | 198,383.9 | 203,457.6 | 1,727.6 | 0.232x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 200,221.4 | 199,199.0 | 201,995.0 | 1,009.4 | 0.233x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 851,077.1 | 845,906.9 | 880,374.1 | 11,681.8 | 0.990x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 859,647.1 | 841,286.8 | 887,969.5 | 15,375.5 | 1.000x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 10,994.4 | 10,961.8 | 11,270.8 | 117.0 | 0.151x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 13,156.6 | 13,142.7 | 13,160.7 | 7.4 | 0.181x | 5 | 100% |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13,172.2 | 13,157.7 | 13,191.6 | 11.6 | 0.181x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 72,570.8 | 72,186.8 | 74,111.1 | 535.0 | 0.997x | 10 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 72,796.1 | 72,414.1 | 75,219.3 | 817.4 | 1.000x | 10 | 100% |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 315.4 | 298.4 | 324.5 | 10.6 | 0.354x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 482.2 | 471.4 | 518.2 | 16.4 | 0.541x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 510.9 | 497.2 | 544.4 | 16.3 | 0.574x |
| 4 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 516.0 | 495.3 | 549.3 | 17.3 | 0.579x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 525.2 | 492.2 | 559.7 | 28.9 | 0.590x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 882.2 | 872.7 | 895.2 | 7.0 | 0.991x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 890.5 | 869.8 | 917.0 | 15.6 | 1.000x |
| 8 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 1,684.9 | 1,680.6 | 1,707.2 | 11.9 | 1.892x |
| 9 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 1,686.0 | 1,682.1 | 1,687.0 | 1.7 | 1.893x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 25,206.4 | 25,201.3 | 25,395.5 | 75.3 | 0.118x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 25,221.0 | 25,186.8 | 25,348.8 | 57.9 | 0.118x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 101,057.8 | 99,678.4 | 101,371.7 | 596.2 | 0.475x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 212,976.0 | 211,032.0 | 215,032.2 | 1,405.7 | 1.000x | 10 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 213,719.8 | 211,742.0 | 214,359.5 | 874.7 | 1.003x | 10 | 100% |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 26,896.6 | 26,891.2 | 26,924.7 | 13.5 | 0.180x | 5 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 26,924.4 | 26,903.4 | 27,133.0 | 105.7 | 0.180x | 5 | 100% |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 33,003.8 | 32,878.4 | 33,105.0 | 84.6 | 0.221x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 149,400.0 | 148,969.0 | 150,677.2 | 695.3 | 1.000x | 10 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 149,679.5 | 148,436.4 | 150,779.1 | 717.0 | 1.002x | 10 | 100% |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 41.3 | 41.1 | 41.4 | 0.1 | 0.247x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 42.6 | 42.5 | 43.9 | 0.6 | 0.254x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 55.1 | 54.9 | 55.3 | 0.1 | 0.329x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 164.1 | 159.4 | 170.9 | 3.5 | 0.980x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 167.5 | 162.3 | 175.5 | 4.7 | 1.000x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 245.8 | 222.1 | 275.8 | 17.3 | 1.467x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 353.9 | 264.6 | 395.1 | 43.8 | 2.113x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 365.8 | 316.0 | 395.3 | 29.1 | 2.184x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 391.5 | 302.8 | 447.7 | 47.2 | 2.337x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.0 | 33.5 | 34.4 | 0.3 | 0.021x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 34.2 | 34.1 | 34.4 | 0.1 | 0.021x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 142.2 | 140.5 | 145.1 | 1.2 | 0.087x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,148.4 | 1,084.9 | 1,216.1 | 48.8 | 0.705x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,396.9 | 1,372.0 | 1,473.7 | 34.5 | 0.858x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,406.4 | 1,316.2 | 1,441.6 | 44.1 | 0.864x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,437.8 | 1,395.7 | 1,498.3 | 33.2 | 0.883x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,438.1 | 1,373.1 | 1,475.3 | 37.9 | 0.883x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,628.4 | 1,601.3 | 1,683.4 | 23.1 | 1.000x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 117.5 | 117.0 | 120.4 | 1.3 | 0.110x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 137.9 | 137.3 | 142.7 | 2.0 | 0.129x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 203.5 | 203.1 | 205.1 | 0.8 | 0.190x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 399.4 | 370.0 | 429.1 | 23.1 | 0.373x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 540.4 | 533.0 | 593.1 | 22.4 | 0.505x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 552.5 | 541.8 | 651.9 | 41.2 | 0.516x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 586.4 | 543.1 | 617.0 | 24.6 | 0.547x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,067.2 | 1,059.6 | 1,083.1 | 7.5 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,071.2 | 1,049.0 | 1,091.1 | 11.0 | 1.000x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 109.8 | 109.6 | 110.3 | 0.2 | 0.103x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 113.6 | 113.3 | 113.8 | 0.2 | 0.106x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 173.5 | 172.6 | 178.2 | 1.7 | 0.162x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 208.7 | 208.1 | 209.5 | 0.5 | 0.195x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 424.2 | 409.7 | 431.0 | 7.4 | 0.397x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 618.3 | 596.3 | 639.4 | 14.4 | 0.578x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 623.1 | 593.0 | 634.7 | 14.6 | 0.583x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 638.0 | 592.8 | 658.0 | 27.1 | 0.597x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,069.0 | 1,057.3 | 1,083.2 | 8.6 | 1.000x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.6 | 110.6 | 110.7 | 0.1 | 0.109x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.2 | 129.9 | 136.4 | 2.5 | 0.129x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 165.7 | 165.4 | 169.7 | 1.6 | 0.164x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 361.7 | 333.8 | 385.0 | 16.7 | 0.357x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 540.3 | 509.9 | 592.2 | 28.1 | 0.534x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 545.8 | 511.7 | 562.7 | 16.9 | 0.540x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 551.9 | 528.7 | 627.2 | 33.5 | 0.546x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,011.4 | 996.8 | 1,219.4 | 63.4 | 1.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,011.6 | 1,004.3 | 1,023.5 | 6.1 | 1.000x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.3 | 103.0 | 103.5 | 0.2 | 0.102x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.5 | 106.1 | 106.7 | 0.2 | 0.105x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 161.0 | 159.5 | 163.1 | 0.9 | 0.159x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 176.3 | 175.7 | 178.5 | 1.0 | 0.174x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 392.3 | 378.6 | 425.9 | 15.9 | 0.387x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 542.0 | 539.2 | 549.2 | 3.7 | 0.535x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 542.0 | 519.4 | 559.0 | 12.7 | 0.535x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 579.4 | 542.7 | 595.0 | 18.3 | 0.572x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,013.2 | 1,001.9 | 1,049.0 | 15.4 | 1.000x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 39.9 | 39.6 | 40.2 | 0.2 | 0.058x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 58.4 | 57.8 | 66.3 | 3.2 | 0.084x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 84.7 | 84.0 | 85.9 | 0.7 | 0.122x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 278.1 | 243.7 | 293.8 | 20.7 | 0.401x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 401.1 | 377.4 | 435.4 | 19.6 | 0.579x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 423.2 | 415.2 | 507.5 | 37.9 | 0.611x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 449.3 | 366.1 | 472.1 | 41.8 | 0.648x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 688.6 | 685.7 | 699.0 | 4.6 | 0.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 693.2 | 677.9 | 707.8 | 7.3 | 1.000x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 32.5 | 32.5 | 32.7 | 0.1 | 0.047x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 35.4 | 35.1 | 35.5 | 0.2 | 0.051x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 84.5 | 84.3 | 84.7 | 0.1 | 0.123x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 104.5 | 103.9 | 107.3 | 0.9 | 0.152x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 289.1 | 282.1 | 302.3 | 7.2 | 0.420x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 419.2 | 375.9 | 580.3 | 71.5 | 0.609x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 425.0 | 329.7 | 460.3 | 51.4 | 0.617x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 450.7 | 434.1 | 477.5 | 14.2 | 0.654x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 688.7 | 681.7 | 720.6 | 12.7 | 1.000x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.2 | 53.0 | 53.4 | 0.2 | 0.082x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 54.9 | 54.7 | 54.9 | 0.1 | 0.085x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 152.6 | 152.2 | 155.0 | 1.1 | 0.237x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 361.3 | 328.0 | 369.1 | 16.1 | 0.560x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 504.4 | 491.5 | 518.9 | 10.0 | 0.782x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 511.4 | 429.4 | 534.4 | 39.5 | 0.793x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 533.2 | 493.2 | 540.6 | 18.8 | 0.826x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 641.3 | 632.7 | 655.4 | 6.8 | 0.994x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 645.2 | 631.2 | 660.0 | 9.5 | 1.000x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.3 | 47.2 | 47.3 | 0.0 | 0.021x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.7 | 47.5 | 52.8 | 2.0 | 0.021x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 203.3 | 201.2 | 203.8 | 0.9 | 0.090x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,460.0 | 1,348.8 | 1,512.5 | 66.8 | 0.650x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,626.2 | 1,589.7 | 1,695.0 | 34.6 | 0.723x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,817.7 | 1,757.4 | 1,839.1 | 27.5 | 0.809x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,819.6 | 1,773.2 | 1,847.9 | 24.2 | 0.810x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,820.6 | 1,804.2 | 1,848.9 | 16.4 | 0.810x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,247.7 | 2,211.4 | 2,316.2 | 32.1 | 1.000x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 90.8 | 90.6 | 91.4 | 0.3 | 0.105x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 111.1 | 110.9 | 117.4 | 2.5 | 0.129x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 144.2 | 143.8 | 148.9 | 1.9 | 0.167x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 372.9 | 323.4 | 384.1 | 21.7 | 0.431x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 525.4 | 516.7 | 544.9 | 11.9 | 0.608x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 565.7 | 497.5 | 598.6 | 38.4 | 0.655x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 568.6 | 514.9 | 679.0 | 53.7 | 0.658x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 857.4 | 848.0 | 869.0 | 7.1 | 0.992x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 864.2 | 849.1 | 922.0 | 19.1 | 1.000x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 83.5 | 83.2 | 84.0 | 0.3 | 0.097x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 86.6 | 86.4 | 88.5 | 0.8 | 0.100x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 148.4 | 147.4 | 153.2 | 1.5 | 0.172x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 149.5 | 149.1 | 149.7 | 0.2 | 0.173x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 355.8 | 350.6 | 372.7 | 8.1 | 0.412x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 506.7 | 432.6 | 563.6 | 42.9 | 0.587x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 512.7 | 478.9 | 567.1 | 29.8 | 0.594x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 514.3 | 470.9 | 527.5 | 23.7 | 0.596x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 863.3 | 847.1 | 886.1 | 12.3 | 1.000x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 159.8 | 159.3 | 160.1 | 0.3 | 0.180x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 202.1 | 201.6 | 202.9 | 0.5 | 0.228x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 221.7 | 221.4 | 228.9 | 2.9 | 0.250x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 379.2 | 344.5 | 404.5 | 19.1 | 0.428x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 552.9 | 481.5 | 567.5 | 31.3 | 0.624x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 588.7 | 496.5 | 621.3 | 46.4 | 0.665x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 611.8 | 552.8 | 650.3 | 32.0 | 0.691x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 882.9 | 865.4 | 888.0 | 6.7 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 885.7 | 865.0 | 900.3 | 10.8 | 1.000x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 164.3 | 163.9 | 164.6 | 0.2 | 0.186x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 165.2 | 164.1 | 175.3 | 3.2 | 0.187x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 198.0 | 197.7 | 199.2 | 0.6 | 0.224x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 201.0 | 200.2 | 201.6 | 0.5 | 0.227x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 379.6 | 370.2 | 392.5 | 8.8 | 0.429x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 488.5 | 462.7 | 514.9 | 16.6 | 0.552x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 525.8 | 460.2 | 544.4 | 31.0 | 0.594x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 526.6 | 473.0 | 570.9 | 37.7 | 0.595x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 884.5 | 867.2 | 900.2 | 10.7 | 1.000x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 166.1 | 165.9 | 166.4 | 0.2 | 0.073x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 168.3 | 167.9 | 168.7 | 0.3 | 0.074x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 739.7 | 729.6 | 744.7 | 5.2 | 0.326x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 949.5 | 933.9 | 958.6 | 8.9 | 0.419x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 962.9 | 934.7 | 987.9 | 22.4 | 0.425x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 974.6 | 926.1 | 1,119.7 | 67.3 | 0.430x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 987.3 | 944.4 | 1,014.1 | 23.3 | 0.435x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 2,236.3 | 2,215.8 | 2,270.6 | 16.5 | 0.986x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,267.0 | 2,225.1 | 2,300.4 | 24.7 | 1.000x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 160.8 | 160.6 | 161.8 | 0.4 | 0.051x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 164.6 | 164.1 | 165.1 | 0.4 | 0.053x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 407.7 | 406.2 | 415.3 | 2.5 | 0.131x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 912.1 | 862.8 | 919.3 | 20.6 | 0.292x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,123.3 | 1,103.8 | 1,135.1 | 10.7 | 0.360x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,176.2 | 1,140.1 | 1,215.7 | 24.1 | 0.377x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,201.6 | 1,178.0 | 1,249.2 | 23.2 | 0.385x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,205.6 | 1,185.0 | 1,263.4 | 27.0 | 0.386x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,122.4 | 3,099.6 | 3,181.5 | 23.3 | 1.000x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.1 | 40.0 | 40.5 | 0.2 | 0.050x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 41.9 | 41.9 | 42.3 | 0.2 | 0.052x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 153.2 | 150.3 | 155.1 | 1.9 | 0.192x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 382.0 | 373.1 | 393.2 | 7.9 | 0.478x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 499.6 | 456.5 | 538.5 | 30.1 | 0.625x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 514.7 | 465.9 | 565.8 | 33.4 | 0.644x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 543.9 | 497.0 | 576.1 | 25.7 | 0.680x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 793.9 | 769.1 | 983.4 | 68.0 | 0.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 799.5 | 770.5 | 825.5 | 16.1 | 1.000x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.6 | 34.5 | 35.1 | 0.2 | 0.013x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 35.2 | 35.0 | 35.7 | 0.2 | 0.013x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 217.8 | 213.9 | 223.6 | 3.0 | 0.081x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 914.3 | 802.0 | 948.9 | 54.9 | 0.341x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,069.3 | 941.4 | 1,127.9 | 77.4 | 0.399x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,396.4 | 1,376.5 | 1,415.7 | 12.6 | 0.521x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,418.5 | 1,384.2 | 1,434.9 | 17.7 | 0.529x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,423.8 | 1,407.5 | 1,448.9 | 14.3 | 0.531x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,681.5 | 2,652.9 | 3,291.5 | 183.1 | 1.000x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.5 | 53.2 | 53.7 | 0.2 | 0.067x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 55.0 | 54.9 | 55.7 | 0.3 | 0.069x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 199.9 | 184.6 | 205.6 | 7.1 | 0.250x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 425.8 | 410.0 | 443.4 | 11.7 | 0.533x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 526.9 | 505.2 | 569.0 | 20.9 | 0.659x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 551.7 | 490.5 | 582.4 | 32.2 | 0.690x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 558.8 | 539.2 | 601.2 | 24.0 | 0.699x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 785.9 | 767.8 | 807.6 | 12.4 | 0.983x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 799.2 | 768.6 | 807.5 | 13.7 | 1.000x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.5 | 47.4 | 47.6 | 0.1 | 0.018x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.8 | 47.8 | 47.9 | 0.1 | 0.018x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 232.0 | 228.8 | 238.6 | 2.8 | 0.087x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,185.1 | 1,108.3 | 1,267.1 | 52.0 | 0.443x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,299.3 | 1,270.4 | 1,381.2 | 43.7 | 0.486x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,781.8 | 1,732.5 | 1,794.4 | 23.3 | 0.666x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,782.2 | 1,685.6 | 1,823.5 | 48.2 | 0.666x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,790.7 | 1,739.1 | 1,812.7 | 26.5 | 0.670x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,674.5 | 2,663.4 | 2,804.9 | 45.4 | 1.000x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.7 | 110.0 | 111.1 | 0.4 | 0.107x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.5 | 130.2 | 141.3 | 4.3 | 0.126x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 176.0 | 175.9 | 180.0 | 1.7 | 0.170x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 381.1 | 360.8 | 413.1 | 20.6 | 0.369x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 509.1 | 491.3 | 519.3 | 11.1 | 0.493x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 521.6 | 509.9 | 561.4 | 17.6 | 0.505x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 607.9 | 563.0 | 617.8 | 19.9 | 0.588x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,033.6 | 1,024.2 | 1,067.8 | 14.5 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,038.7 | 1,026.1 | 1,074.3 | 15.4 | 1.005x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.7 | 103.3 | 110.9 | 2.9 | 0.100x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.6 | 106.5 | 106.8 | 0.1 | 0.103x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 107.8 | 106.6 | 111.1 | 1.5 | 0.104x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 177.2 | 177.0 | 179.8 | 1.1 | 0.171x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 385.3 | 362.7 | 394.7 | 10.7 | 0.371x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 553.5 | 466.5 | 619.4 | 49.2 | 0.534x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 579.0 | 545.5 | 701.5 | 54.8 | 0.558x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 619.7 | 601.6 | 626.1 | 9.8 | 0.597x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,037.3 | 1,020.9 | 1,084.3 | 20.8 | 1.000x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.5 | 110.0 | 110.9 | 0.3 | 0.106x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.0 | 129.9 | 136.4 | 2.5 | 0.125x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 176.2 | 176.0 | 187.5 | 4.5 | 0.169x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 391.7 | 357.6 | 425.2 | 26.9 | 0.376x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 510.7 | 491.5 | 519.1 | 11.5 | 0.491x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 516.7 | 502.2 | 561.6 | 21.0 | 0.497x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 607.5 | 559.6 | 629.2 | 24.4 | 0.584x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,040.3 | 1,019.2 | 1,078.0 | 16.5 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,043.1 | 1,027.6 | 1,072.1 | 14.4 | 1.003x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.4 | 103.1 | 109.6 | 2.5 | 0.100x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.7 | 106.2 | 107.3 | 0.3 | 0.104x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 106.8 | 106.3 | 110.2 | 1.1 | 0.104x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 177.4 | 177.1 | 179.5 | 0.9 | 0.172x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 386.3 | 374.9 | 400.5 | 9.8 | 0.375x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 535.0 | 522.5 | 634.4 | 40.9 | 0.520x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 598.3 | 542.1 | 627.2 | 35.0 | 0.581x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 601.4 | 569.4 | 643.6 | 24.6 | 0.584x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,029.5 | 1,021.1 | 1,068.6 | 13.4 | 1.000x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.4 | 109.9 | 112.2 | 0.8 | 0.097x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.1 | 129.8 | 136.3 | 2.5 | 0.114x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 170.2 | 169.5 | 174.6 | 1.9 | 0.149x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 380.8 | 364.9 | 418.5 | 18.9 | 0.333x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 501.3 | 460.0 | 513.3 | 19.5 | 0.439x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 513.0 | 489.1 | 536.4 | 16.6 | 0.449x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 565.6 | 534.6 | 592.0 | 19.9 | 0.495x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,138.4 | 1,133.8 | 1,175.7 | 17.5 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,142.2 | 1,127.2 | 1,165.4 | 15.2 | 1.000x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.3 | 103.1 | 104.6 | 0.6 | 0.091x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.5 | 106.3 | 107.0 | 0.3 | 0.094x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 108.1 | 107.2 | 116.0 | 2.4 | 0.095x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 172.5 | 172.4 | 172.7 | 0.1 | 0.152x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 374.6 | 350.8 | 412.7 | 24.3 | 0.331x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 576.2 | 535.9 | 597.6 | 23.6 | 0.509x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 593.0 | 514.6 | 686.8 | 58.2 | 0.523x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 605.3 | 548.6 | 611.3 | 23.5 | 0.534x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,132.9 | 1,123.6 | 1,160.7 | 11.5 | 1.000x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.3 | 109.7 | 110.6 | 0.4 | 0.101x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.4 | 129.9 | 136.5 | 2.5 | 0.119x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 160.1 | 159.9 | 165.0 | 2.0 | 0.147x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 374.9 | 334.9 | 420.4 | 31.9 | 0.344x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 543.2 | 511.1 | 572.1 | 22.5 | 0.498x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 558.2 | 528.3 | 563.0 | 13.4 | 0.512x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 579.3 | 550.0 | 601.1 | 17.8 | 0.531x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,081.7 | 1,067.2 | 1,108.3 | 14.1 | 0.991x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,091.0 | 1,071.9 | 1,108.2 | 11.1 | 1.000x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.2 | 103.1 | 104.2 | 0.4 | 0.096x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.7 | 106.6 | 107.1 | 0.2 | 0.099x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 107.4 | 107.0 | 109.8 | 0.9 | 0.100x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 163.1 | 162.8 | 164.4 | 0.6 | 0.152x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 365.5 | 346.9 | 432.1 | 31.1 | 0.340x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 563.9 | 500.6 | 661.2 | 57.8 | 0.525x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 572.8 | 545.5 | 594.7 | 16.0 | 0.533x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 589.9 | 562.7 | 598.4 | 15.5 | 0.549x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,074.3 | 1,064.6 | 1,100.7 | 11.2 | 1.000x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.4 | 110.4 | 110.9 | 0.2 | 0.102x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.2 | 129.9 | 136.6 | 2.6 | 0.120x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 160.5 | 160.0 | 169.2 | 3.6 | 0.148x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 380.2 | 329.8 | 401.0 | 25.2 | 0.350x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 528.9 | 504.6 | 569.7 | 22.2 | 0.487x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 557.9 | 549.7 | 578.3 | 10.9 | 0.513x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 584.7 | 564.4 | 589.4 | 9.8 | 0.538x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,081.1 | 1,070.8 | 1,106.9 | 14.6 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,087.0 | 1,071.6 | 1,116.2 | 12.9 | 1.000x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.4 | 103.1 | 106.8 | 1.4 | 0.096x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 106.5 | 106.3 | 106.7 | 0.1 | 0.099x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 107.5 | 107.1 | 114.6 | 2.2 | 0.100x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 163.5 | 162.9 | 163.8 | 0.4 | 0.152x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 370.1 | 341.4 | 436.2 | 33.3 | 0.344x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 564.4 | 492.7 | 650.0 | 52.6 | 0.524x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 582.8 | 536.7 | 619.4 | 29.0 | 0.541x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 593.3 | 570.9 | 612.5 | 14.1 | 0.551x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,076.5 | 1,067.8 | 1,098.1 | 9.9 | 1.000x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.5 | 49.5 | 50.7 | 0.5 | 0.055x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 52.1 | 51.6 | 53.7 | 0.7 | 0.057x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 279.1 | 261.0 | 306.7 | 16.4 | 0.303x |
| 4 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 534.0 | 520.3 | 552.8 | 12.5 | 0.580x |
| 5 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 581.7 | 569.8 | 628.6 | 20.8 | 0.631x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 604.8 | 559.0 | 622.7 | 21.4 | 0.656x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 626.0 | 574.3 | 663.2 | 33.9 | 0.679x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 917.7 | 902.3 | 947.6 | 13.8 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 921.5 | 905.9 | 942.7 | 10.9 | 1.000x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.3 | 44.0 | 44.4 | 0.1 | 0.014x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 45.0 | 44.6 | 46.4 | 0.6 | 0.014x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 319.5 | 306.2 | 335.3 | 8.8 | 0.100x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 1,745.3 | 1,732.9 | 1,788.3 | 19.6 | 0.549x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,756.0 | 1,728.4 | 1,842.0 | 39.1 | 0.552x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,771.1 | 1,713.9 | 2,167.9 | 165.0 | 0.557x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,782.9 | 1,726.8 | 1,866.7 | 44.9 | 0.560x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 1,939.2 | 1,936.5 | 1,958.0 | 9.3 | 0.609x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,181.8 | 3,161.0 | 3,564.8 | 116.3 | 1.000x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 12.4 | 12.2 | 12.4 | 0.1 | 0.401x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13.2 | 13.0 | 13.3 | 0.1 | 0.427x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 30.5 | 30.3 | 33.6 | 1.1 | 0.987x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 30.9 | 30.3 | 32.5 | 0.8 | 1.000x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 51.4 | 51.1 | 52.4 | 0.5 | 1.665x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 290.7 | 258.9 | 292.4 | 13.1 | 9.410x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 387.3 | 365.4 | 417.4 | 20.1 | 12.537x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 432.8 | 415.7 | 454.5 | 13.4 | 14.009x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 436.3 | 390.0 | 482.8 | 30.0 | 14.122x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 4.9 | 4.7 | 5.0 | 0.1 | 0.160x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 5.2 | 5.1 | 5.4 | 0.1 | 0.170x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 30.6 | 30.4 | 33.9 | 1.2 | 1.000x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 41.2 | 40.1 | 51.4 | 3.3 | 1.347x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 50.2 | 49.9 | 50.5 | 0.2 | 1.641x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 270.0 | 263.9 | 291.2 | 9.7 | 8.820x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 434.6 | 410.8 | 467.6 | 22.7 | 14.197x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 440.4 | 417.8 | 471.3 | 18.6 | 14.388x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 445.0 | 392.8 | 491.2 | 36.1 | 14.538x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13.9 | 13.9 | 15.0 | 0.5 | 0.453x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 14.0 | 13.2 | 14.2 | 0.4 | 0.458x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 30.6 | 30.3 | 31.4 | 0.4 | 1.000x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 30.7 | 30.3 | 35.2 | 1.5 | 1.004x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 51.3 | 51.2 | 52.8 | 0.6 | 1.674x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 284.2 | 266.3 | 306.3 | 13.1 | 9.281x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 412.8 | 306.7 | 437.7 | 45.9 | 13.482x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 438.8 | 405.0 | 455.1 | 16.7 | 14.331x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 449.1 | 415.6 | 459.2 | 15.0 | 14.666x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 5.5 | 5.3 | 5.6 | 0.1 | 0.179x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 5.8 | 5.6 | 5.9 | 0.1 | 0.189x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 30.6 | 30.4 | 34.3 | 1.3 | 1.000x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 40.9 | 40.1 | 49.8 | 2.8 | 1.338x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 67.8 | 67.5 | 69.3 | 0.8 | 2.216x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 286.9 | 278.9 | 305.7 | 9.6 | 9.374x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 454.5 | 450.9 | 473.3 | 8.1 | 14.852x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 456.9 | 412.6 | 512.6 | 32.1 | 14.933x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 468.2 | 430.4 | 496.4 | 27.4 | 15.301x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 34.2 | 33.5 | 39.6 | 1.8 | 0.997x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 34.3 | 33.8 | 35.8 | 0.7 | 1.000x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 115.4 | 113.3 | 116.1 | 0.9 | 3.361x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 138.1 | 138.1 | 138.2 | 0.0 | 4.023x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 139.6 | 139.4 | 140.0 | 0.2 | 4.065x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 340.2 | 334.1 | 350.5 | 5.7 | 9.908x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 476.3 | 445.6 | 616.2 | 59.8 | 13.873x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 495.6 | 451.7 | 523.8 | 24.0 | 14.435x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 530.0 | 459.6 | 571.3 | 37.8 | 15.437x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.0 | 34.6 | 40.3 | 2.1 | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 46.4 | 46.1 | 48.4 | 0.7 | 1.324x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 132.3 | 132.1 | 132.8 | 0.2 | 3.778x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 132.7 | 132.6 | 132.8 | 0.1 | 3.790x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 2,889.6 | 2,868.4 | 3,035.0 | 62.0 | 82.518x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 3,129.7 | 3,018.7 | 3,181.6 | 57.1 | 89.373x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 3,395.1 | 3,371.3 | 3,485.3 | 41.6 | 96.952x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 3,402.5 | 3,328.7 | 3,482.9 | 48.9 | 97.166x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 3,437.5 | 3,405.4 | 3,452.8 | 19.5 | 98.164x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 30.4 | 30.1 | 31.1 | 0.4 | 0.913x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 32.0 | 31.5 | 32.0 | 0.2 | 0.959x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 33.3 | 32.7 | 34.6 | 0.6 | 1.000x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 34.7 | 33.6 | 37.1 | 0.9 | 1.040x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 169.6 | 164.6 | 175.9 | 3.8 | 5.087x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 392.6 | 389.3 | 402.1 | 5.0 | 11.774x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 596.3 | 570.5 | 655.3 | 31.9 | 17.883x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 622.9 | 611.6 | 646.8 | 12.4 | 18.679x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 636.2 | 568.5 | 662.4 | 33.0 | 19.079x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 25.2 | 25.2 | 26.3 | 0.4 | 0.737x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 25.5 | 25.5 | 26.5 | 0.4 | 0.746x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 34.2 | 33.9 | 40.7 | 2.4 | 1.000x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 44.4 | 44.3 | 48.7 | 1.3 | 1.297x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 811.1 | 763.1 | 839.1 | 25.9 | 23.686x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 998.5 | 971.7 | 1,048.5 | 25.3 | 29.159x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 1,581.2 | 1,541.0 | 1,659.0 | 42.0 | 46.177x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 1,632.7 | 1,596.8 | 1,697.4 | 35.4 | 47.678x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 1,636.8 | 1,579.9 | 1,672.1 | 32.8 | 47.799x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 6,546,906.3 | 6,535,788.9 | 6,704,786.6 | 64,500.5 | 0.126x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 6,562,782.4 | 6,553,636.4 | 6,638,556.9 | 31,574.4 | 0.126x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 7,039,070.7 | 6,964,179.7 | 7,512,686.3 | 156,152.5 | 0.136x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 10,975,556.0 | 10,898,005.0 | 11,025,015.0 | 46,442.2 | 0.211x |
| 5 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 18,612,288.0 | 17,644,272.0 | 19,618,594.0 | 627,811.6 | 0.358x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 23,646,430.0 | 22,861,735.0 | 26,823,629.0 | 1,442,212.7 | 0.455x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 24,010,552.0 | 22,722,773.0 | 25,261,380.0 | 825,072.6 | 0.462x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 24,014,597.0 | 22,956,700.0 | 26,418,041.0 | 1,195,438.1 | 0.462x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 51,944,378.6 | 51,595,473.4 | 52,364,619.8 | 231,159.8 | 1.000x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 17,809.7 | 17,772.2 | 17,873.5 | 28.8 | 1.000x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 3,421,600.3 | 3,420,775.0 | 3,451,781.9 | 13,451.0 | 192.120x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 3,422,915.7 | 3,417,224.3 | 3,432,375.1 | 6,155.3 | 192.194x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 17,697,835.8 | 17,644,885.3 | 17,781,863.7 | 36,072.4 | 993.718x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 84,138,418.0 | 83,753,954.0 | 84,516,340.0 | 281,935.0 | 4724.299x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 87,151,691.0 | 87,056,790.0 | 87,870,905.0 | 296,577.9 | 4893.491x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 88,138,127.0 | 87,017,010.0 | 91,290,196.0 | 1,439,973.1 | 4948.879x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 88,760,543.0 | 87,217,943.0 | 92,820,847.0 | 1,915,173.9 | 4983.827x |
| 9 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 89,148,076.0 | 82,492,434.0 | 90,456,955.0 | 3,365,895.9 | 5005.587x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 17,815.4 | 17,746.7 | 18,020.3 | 76.5 | 1.000x | 10 | 100% |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 3,423,842.4 | 3,414,307.6 | 3,482,299.3 | 24,784.0 | 192.185x | 5 | 100% |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 3,429,171.1 | 3,415,012.9 | 3,527,893.0 | 42,089.9 | 192.484x | 5 | 100% |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 47.2 | 46.6 | 48.7 | 0.8 | 0.085x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 111.2 | 110.8 | 112.9 | 0.7 | 0.201x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 111.2 | 110.0 | 112.4 | 0.9 | 0.201x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 111.7 | 110.8 | 114.5 | 1.3 | 0.202x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 111.7 | 110.8 | 120.8 | 3.7 | 0.202x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 236.1 | 223.8 | 252.6 | 10.6 | 0.427x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 244.1 | 220.6 | 275.8 | 17.7 | 0.441x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 549.0 | 541.5 | 588.1 | 12.5 | 0.992x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 553.3 | 540.1 | 556.9 | 5.9 | 1.000x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 54.4 | 54.1 | 55.2 | 0.4 | 0.098x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 77.9 | 76.8 | 84.3 | 2.2 | 0.141x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.1 | 102.7 | 103.7 | 0.4 | 0.186x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.4 | 103.3 | 104.0 | 0.3 | 0.187x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.5 | 103.3 | 110.1 | 2.7 | 0.187x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.5 | 103.3 | 103.7 | 0.2 | 0.187x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 230.2 | 223.7 | 244.6 | 7.4 | 0.416x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 254.2 | 250.8 | 258.6 | 2.6 | 0.460x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 553.1 | 545.9 | 595.4 | 13.4 | 1.000x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 97.3 | 97.2 | 105.6 | 3.3 | 0.128x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 143.8 | 143.5 | 153.3 | 3.8 | 0.189x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 143.9 | 143.8 | 144.8 | 0.4 | 0.189x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 144.3 | 143.9 | 158.1 | 5.6 | 0.190x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 144.4 | 143.9 | 144.5 | 0.2 | 0.190x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 271.7 | 251.3 | 306.7 | 19.4 | 0.357x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 281.3 | 260.5 | 307.1 | 15.4 | 0.370x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 761.1 | 753.8 | 779.7 | 8.0 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 764.3 | 757.5 | 810.7 | 15.0 | 1.004x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 92.4 | 92.3 | 92.5 | 0.1 | 0.120x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 93.1 | 92.2 | 99.4 | 2.0 | 0.121x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 135.3 | 135.0 | 135.9 | 0.3 | 0.176x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 135.4 | 135.2 | 135.7 | 0.2 | 0.176x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 135.9 | 135.4 | 136.3 | 0.3 | 0.177x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 136.0 | 135.7 | 138.5 | 1.1 | 0.177x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 243.6 | 217.8 | 284.7 | 24.0 | 0.317x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 265.5 | 237.4 | 280.0 | 14.8 | 0.346x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 768.2 | 746.7 | 825.0 | 19.9 | 1.000x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 33.4 | 33.1 | 35.0 | 0.7 | 0.070x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 46.0 | 45.6 | 46.2 | 0.2 | 0.096x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 46.1 | 45.6 | 53.7 | 3.1 | 0.096x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 46.2 | 46.0 | 55.8 | 3.8 | 0.096x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 46.2 | 46.2 | 46.7 | 0.2 | 0.096x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 235.6 | 220.9 | 251.2 | 11.4 | 0.492x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 241.2 | 221.1 | 266.4 | 16.5 | 0.503x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 479.2 | 474.7 | 489.2 | 4.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 483.5 | 475.8 | 503.8 | 8.8 | 1.009x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 38.5 | 38.4 | 39.0 | 0.2 | 0.079x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 38.5 | 38.4 | 38.8 | 0.2 | 0.079x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 38.6 | 38.3 | 38.8 | 0.1 | 0.080x |
| 4 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 38.6 | 38.4 | 38.6 | 0.1 | 0.080x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 38.9 | 38.7 | 39.4 | 0.2 | 0.080x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 64.2 | 61.4 | 71.0 | 2.6 | 0.132x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 228.4 | 206.3 | 259.3 | 16.9 | 0.471x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 246.9 | 238.6 | 297.3 | 21.9 | 0.509x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 485.0 | 473.0 | 502.2 | 10.1 | 1.000x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 60.9 | 60.1 | 76.4 | 6.2 | 0.080x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 157.2 | 156.7 | 158.0 | 0.5 | 0.205x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 157.2 | 156.7 | 157.6 | 0.3 | 0.206x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 157.5 | 157.1 | 170.6 | 5.2 | 0.206x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 157.5 | 156.6 | 166.9 | 3.9 | 0.206x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 247.4 | 244.9 | 301.2 | 22.1 | 0.323x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 258.5 | 251.3 | 276.4 | 10.0 | 0.338x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 764.9 | 757.4 | 835.3 | 21.8 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 772.7 | 761.8 | 796.8 | 9.9 | 1.010x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 67.9 | 67.1 | 68.5 | 0.5 | 0.089x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 93.7 | 90.6 | 102.2 | 3.3 | 0.122x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 147.6 | 146.9 | 147.7 | 0.3 | 0.193x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 147.8 | 147.6 | 150.9 | 1.2 | 0.193x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 147.9 | 147.8 | 148.1 | 0.1 | 0.193x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 148.0 | 147.6 | 148.5 | 0.4 | 0.193x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 255.5 | 236.4 | 295.6 | 21.3 | 0.334x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 277.2 | 254.3 | 337.0 | 27.6 | 0.362x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 766.0 | 759.1 | 806.2 | 15.6 | 1.000x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 61.8 | 60.7 | 76.6 | 6.1 | 0.110x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 222.2 | 222.1 | 223.1 | 0.4 | 0.394x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 222.3 | 221.8 | 224.5 | 1.0 | 0.394x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 222.4 | 221.6 | 231.5 | 3.7 | 0.394x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 222.4 | 221.9 | 223.3 | 0.5 | 0.394x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 256.1 | 228.2 | 280.4 | 17.0 | 0.454x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 261.4 | 252.2 | 274.1 | 8.8 | 0.463x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 564.2 | 557.8 | 882.0 | 95.1 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 565.4 | 557.0 | 585.3 | 7.8 | 1.002x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 68.1 | 67.2 | 69.1 | 0.6 | 0.121x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 92.8 | 91.0 | 99.3 | 2.4 | 0.165x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 213.5 | 213.0 | 214.2 | 0.4 | 0.380x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 213.7 | 213.3 | 217.8 | 1.7 | 0.380x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 214.0 | 213.8 | 214.5 | 0.3 | 0.381x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 214.2 | 214.0 | 215.2 | 0.5 | 0.381x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 272.8 | 245.9 | 318.3 | 24.1 | 0.486x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 276.1 | 232.0 | 295.0 | 22.4 | 0.492x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 561.8 | 559.6 | 577.8 | 5.3 | 1.000x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 33.5 | 33.3 | 33.9 | 0.2 | 0.070x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 45.9 | 45.9 | 48.4 | 1.0 | 0.096x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 46.0 | 45.4 | 46.5 | 0.4 | 0.096x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 46.1 | 45.8 | 46.6 | 0.3 | 0.096x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 46.2 | 46.1 | 55.6 | 3.8 | 0.097x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 242.7 | 232.2 | 250.0 | 6.5 | 0.508x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 253.0 | 221.8 | 279.5 | 23.4 | 0.529x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 478.1 | 470.7 | 540.5 | 19.2 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 479.5 | 471.5 | 503.3 | 8.2 | 1.003x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 38.3 | 38.2 | 38.5 | 0.1 | 0.080x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 38.6 | 38.3 | 49.8 | 4.4 | 0.080x |
| 3 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 38.7 | 38.5 | 38.8 | 0.1 | 0.080x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 38.7 | 38.7 | 38.8 | 0.1 | 0.080x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 38.7 | 38.6 | 38.8 | 0.1 | 0.080x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 65.1 | 63.0 | 71.2 | 2.6 | 0.135x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 263.8 | 211.1 | 282.8 | 27.5 | 0.548x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 275.7 | 250.2 | 289.2 | 15.2 | 0.572x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 481.7 | 469.4 | 491.4 | 7.1 | 1.000x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 103.7 | 103.5 | 104.2 | 0.3 | 0.133x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 103.8 | 103.5 | 104.0 | 0.2 | 0.133x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 104.0 | 104.0 | 115.5 | 4.5 | 0.133x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 104.3 | 104.1 | 104.5 | 0.1 | 0.133x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 121.5 | 121.1 | 122.5 | 0.4 | 0.156x |
| 6 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 303.6 | 282.5 | 315.6 | 10.9 | 0.389x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 314.0 | 300.3 | 316.2 | 5.7 | 0.402x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 779.6 | 772.4 | 829.0 | 15.9 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 781.5 | 770.2 | 788.2 | 6.0 | 1.000x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 85.2 | 83.7 | 91.3 | 2.6 | 0.108x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 96.4 | 96.4 | 98.4 | 0.8 | 0.123x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 96.6 | 96.4 | 96.8 | 0.2 | 0.123x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 96.7 | 96.5 | 97.3 | 0.3 | 0.123x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 96.9 | 96.4 | 98.8 | 0.9 | 0.123x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 133.1 | 131.7 | 133.2 | 0.6 | 0.170x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 335.9 | 296.4 | 364.4 | 23.7 | 0.428x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 352.6 | 293.4 | 396.7 | 33.3 | 0.449x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 785.3 | 777.1 | 795.7 | 5.4 | 1.000x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 55.6 | 55.4 | 59.7 | 1.6 | 0.090x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 169.9 | 169.2 | 179.1 | 3.7 | 0.274x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 169.9 | 169.8 | 170.2 | 0.1 | 0.275x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 169.9 | 169.5 | 174.0 | 1.7 | 0.275x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 170.1 | 170.0 | 170.5 | 0.2 | 0.275x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 261.1 | 258.3 | 270.6 | 4.6 | 0.422x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.1 | 242.7 | 288.7 | 18.4 | 0.457x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 618.3 | 613.0 | 641.3 | 7.7 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 618.8 | 611.3 | 643.8 | 9.0 | 1.000x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 65.0 | 63.7 | 65.8 | 0.7 | 0.105x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 92.9 | 89.7 | 100.3 | 3.1 | 0.150x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 161.6 | 161.5 | 161.7 | 0.1 | 0.262x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 161.9 | 161.4 | 166.8 | 2.0 | 0.262x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 162.0 | 161.7 | 164.0 | 0.8 | 0.262x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 162.1 | 161.2 | 162.8 | 0.5 | 0.262x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 279.9 | 234.4 | 291.7 | 19.8 | 0.453x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 302.5 | 275.2 | 323.3 | 16.4 | 0.490x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 617.8 | 610.3 | 628.0 | 5.5 | 1.000x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 49.5 | 48.9 | 53.7 | 1.8 | 0.091x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 129.7 | 129.3 | 130.3 | 0.3 | 0.238x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 129.8 | 129.2 | 131.4 | 0.7 | 0.238x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 130.0 | 129.8 | 143.8 | 5.5 | 0.239x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 130.2 | 129.6 | 130.6 | 0.4 | 0.239x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 262.0 | 260.4 | 268.0 | 2.8 | 0.481x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 293.5 | 267.5 | 298.2 | 12.4 | 0.539x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 543.9 | 534.1 | 566.6 | 10.6 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 544.8 | 540.9 | 595.0 | 15.4 | 1.000x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 56.4 | 56.1 | 57.2 | 0.4 | 0.104x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 80.4 | 78.7 | 87.1 | 2.4 | 0.148x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 122.4 | 122.0 | 122.7 | 0.3 | 0.226x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 122.5 | 122.2 | 123.1 | 0.3 | 0.226x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 122.8 | 122.4 | 130.1 | 2.9 | 0.227x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 123.2 | 122.0 | 131.8 | 3.6 | 0.227x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 282.0 | 230.1 | 290.5 | 21.6 | 0.520x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 285.1 | 261.1 | 313.0 | 18.8 | 0.526x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 542.3 | 538.5 | 553.7 | 4.4 | 1.000x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 45.5 | 45.2 | 61.0 | 6.1 | 0.084x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 97.0 | 96.7 | 111.8 | 6.0 | 0.180x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 97.2 | 96.8 | 98.9 | 0.8 | 0.181x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 97.3 | 96.5 | 98.1 | 0.6 | 0.181x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 97.5 | 97.3 | 98.0 | 0.3 | 0.181x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 258.5 | 255.3 | 259.8 | 1.6 | 0.480x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 288.4 | 262.1 | 296.1 | 12.4 | 0.536x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 538.2 | 531.7 | 553.9 | 6.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 539.1 | 533.2 | 567.6 | 11.6 | 1.002x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 52.6 | 51.8 | 52.9 | 0.4 | 0.098x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 76.2 | 72.4 | 83.0 | 2.9 | 0.141x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 89.8 | 89.5 | 90.2 | 0.3 | 0.167x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 89.9 | 89.8 | 90.4 | 0.2 | 0.167x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.9 | 89.9 | 90.2 | 0.1 | 0.167x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 90.2 | 89.8 | 90.8 | 0.3 | 0.167x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 277.0 | 228.1 | 282.1 | 20.2 | 0.514x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 284.9 | 255.7 | 308.0 | 16.7 | 0.529x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 538.9 | 531.6 | 584.2 | 14.7 | 1.000x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 32.9 | 32.4 | 34.3 | 0.7 | 0.075x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 97.0 | 96.8 | 98.8 | 0.7 | 0.222x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 97.3 | 96.9 | 107.5 | 4.2 | 0.222x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 97.3 | 96.6 | 100.2 | 1.3 | 0.222x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 97.7 | 97.2 | 102.7 | 2.5 | 0.223x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 247.6 | 240.4 | 252.1 | 4.3 | 0.566x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 264.9 | 258.3 | 270.5 | 4.0 | 0.605x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 437.6 | 432.8 | 441.5 | 2.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 438.7 | 433.5 | 454.6 | 5.4 | 1.002x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 37.7 | 37.2 | 38.0 | 0.3 | 0.086x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.4 | 68.2 | 75.5 | 2.3 | 0.161x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 89.6 | 89.5 | 90.0 | 0.2 | 0.205x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 90.0 | 89.8 | 90.1 | 0.1 | 0.206x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 90.0 | 89.9 | 90.7 | 0.3 | 0.206x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 90.8 | 89.3 | 91.6 | 0.8 | 0.208x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 244.4 | 232.4 | 253.7 | 9.1 | 0.559x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 254.4 | 213.4 | 266.8 | 18.7 | 0.582x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 437.2 | 430.2 | 451.0 | 6.3 | 1.000x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 33.8 | 33.6 | 35.6 | 0.7 | 0.097x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 69.5 | 69.4 | 70.1 | 0.3 | 0.200x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 69.6 | 69.3 | 81.9 | 4.9 | 0.200x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 69.6 | 69.5 | 69.8 | 0.1 | 0.201x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 69.8 | 69.6 | 70.2 | 0.2 | 0.201x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 255.3 | 254.0 | 262.3 | 3.0 | 0.735x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 308.4 | 273.8 | 328.8 | 18.1 | 0.888x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 342.9 | 338.4 | 358.9 | 6.7 | 0.988x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 347.1 | 341.5 | 351.3 | 3.0 | 1.000x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 63.6 | 63.4 | 64.9 | 0.6 | 0.036x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 63.7 | 63.4 | 64.7 | 0.5 | 0.036x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 63.8 | 63.7 | 64.0 | 0.1 | 0.036x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 63.9 | 63.8 | 64.5 | 0.3 | 0.036x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 140.5 | 138.7 | 153.3 | 4.7 | 0.079x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 317.0 | 315.4 | 320.7 | 2.2 | 0.179x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 536.4 | 493.8 | 547.9 | 19.2 | 0.303x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 583.5 | 550.3 | 590.8 | 14.8 | 0.330x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,769.7 | 1,752.3 | 1,823.6 | 20.2 | 1.000x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 80.3 | 80.1 | 81.0 | 0.3 | 0.117x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 123.2 | 123.0 | 123.4 | 0.2 | 0.180x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.4 | 123.2 | 124.0 | 0.3 | 0.180x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 123.6 | 123.4 | 126.9 | 1.3 | 0.180x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 123.8 | 123.3 | 134.5 | 5.0 | 0.181x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 279.3 | 274.8 | 283.3 | 3.1 | 0.408x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 306.5 | 274.5 | 356.2 | 27.4 | 0.447x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 679.2 | 665.0 | 699.7 | 10.3 | 0.991x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 685.2 | 672.8 | 697.5 | 6.8 | 1.000x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 82.6 | 82.1 | 85.1 | 1.1 | 0.121x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 83.7 | 81.1 | 92.3 | 3.2 | 0.122x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 115.1 | 114.9 | 120.2 | 2.0 | 0.168x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 115.3 | 115.2 | 115.9 | 0.3 | 0.169x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.5 | 115.5 | 116.6 | 0.4 | 0.169x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 115.7 | 115.6 | 115.8 | 0.1 | 0.169x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 296.0 | 270.1 | 333.2 | 20.4 | 0.433x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 307.5 | 286.1 | 329.4 | 14.5 | 0.450x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 683.7 | 675.5 | 702.7 | 7.5 | 1.000x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 80.5 | 80.4 | 80.7 | 0.1 | 0.118x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 123.1 | 123.0 | 135.8 | 5.1 | 0.180x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.5 | 123.0 | 124.0 | 0.4 | 0.180x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 123.5 | 123.4 | 134.2 | 4.3 | 0.180x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 123.6 | 123.5 | 123.7 | 0.1 | 0.180x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 278.5 | 274.2 | 284.6 | 3.5 | 0.406x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 306.7 | 268.7 | 348.1 | 25.9 | 0.448x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 682.0 | 676.5 | 699.7 | 6.2 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 685.3 | 674.6 | 697.9 | 7.7 | 1.000x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 82.2 | 82.0 | 82.5 | 0.2 | 0.120x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 82.5 | 80.9 | 96.6 | 4.5 | 0.120x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 115.2 | 114.9 | 116.8 | 0.7 | 0.168x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.4 | 115.3 | 116.4 | 0.4 | 0.168x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 115.5 | 115.3 | 119.5 | 1.6 | 0.169x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 115.7 | 115.5 | 118.0 | 1.2 | 0.169x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 299.2 | 291.3 | 312.3 | 6.9 | 0.437x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 309.6 | 278.9 | 332.4 | 17.2 | 0.452x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 685.3 | 675.9 | 704.8 | 6.9 | 1.000x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 50.2 | 50.1 | 50.5 | 0.1 | 0.093x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 96.7 | 96.6 | 183.2 | 34.5 | 0.180x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 97.2 | 97.1 | 98.0 | 0.3 | 0.181x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 97.3 | 97.0 | 113.6 | 6.5 | 0.181x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 97.7 | 96.9 | 99.3 | 1.0 | 0.182x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 265.8 | 262.8 | 275.2 | 4.4 | 0.495x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 293.9 | 267.8 | 298.7 | 11.3 | 0.547x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 537.2 | 529.1 | 545.8 | 5.1 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 538.9 | 533.9 | 552.2 | 5.7 | 1.003x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 66.3 | 66.1 | 67.3 | 0.4 | 0.123x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 77.4 | 75.0 | 87.7 | 3.6 | 0.144x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.9 | 89.9 | 90.1 | 0.1 | 0.167x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 89.9 | 89.7 | 93.5 | 1.4 | 0.167x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 89.9 | 89.8 | 90.8 | 0.4 | 0.167x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 89.9 | 89.8 | 90.9 | 0.4 | 0.167x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 287.4 | 282.0 | 290.4 | 2.8 | 0.535x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 327.4 | 292.0 | 372.6 | 26.6 | 0.609x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 537.3 | 528.3 | 554.7 | 6.5 | 1.000x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 74.7 | 74.6 | 75.8 | 0.5 | 0.114x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 117.1 | 116.6 | 207.7 | 36.2 | 0.178x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 117.1 | 116.6 | 117.6 | 0.4 | 0.178x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 117.2 | 116.9 | 118.5 | 0.6 | 0.178x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 118.5 | 117.0 | 128.2 | 5.1 | 0.180x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 276.0 | 275.5 | 294.5 | 7.3 | 0.420x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 301.6 | 285.1 | 323.9 | 14.6 | 0.459x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 657.0 | 651.5 | 690.0 | 10.9 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 657.6 | 646.9 | 688.3 | 11.2 | 1.000x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 80.3 | 80.2 | 80.6 | 0.2 | 0.122x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 81.1 | 79.3 | 90.8 | 3.5 | 0.124x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 109.7 | 109.4 | 110.0 | 0.2 | 0.167x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 109.8 | 109.5 | 110.1 | 0.2 | 0.167x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 109.8 | 109.6 | 109.9 | 0.1 | 0.167x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 109.8 | 109.6 | 110.4 | 0.3 | 0.167x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 293.9 | 288.9 | 305.8 | 6.0 | 0.448x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 303.2 | 281.3 | 325.2 | 14.8 | 0.462x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 656.6 | 648.5 | 673.0 | 6.0 | 1.000x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.0 | 25.8 | 27.4 | 0.6 | 0.140x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 52.9 | 52.7 | 58.9 | 2.4 | 0.285x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 53.0 | 52.4 | 54.9 | 0.9 | 0.286x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.2 | 53.0 | 53.4 | 0.1 | 0.286x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 53.3 | 52.9 | 64.4 | 4.5 | 0.287x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 185.4 | 183.0 | 199.7 | 5.1 | 0.998x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 185.8 | 181.7 | 189.9 | 2.1 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 248.5 | 246.9 | 255.3 | 3.1 | 1.337x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 291.5 | 271.4 | 307.1 | 11.6 | 1.569x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.3 | 47.3 | 47.4 | 0.1 | 0.044x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 47.3 | 47.1 | 48.0 | 0.3 | 0.044x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 47.4 | 47.2 | 48.2 | 0.4 | 0.044x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.4 | 47.3 | 47.6 | 0.1 | 0.044x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 109.9 | 106.6 | 121.2 | 4.3 | 0.101x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 226.9 | 226.3 | 229.9 | 1.3 | 0.209x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 446.4 | 431.5 | 453.3 | 7.2 | 0.412x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 470.8 | 447.0 | 490.7 | 14.2 | 0.434x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,083.6 | 1,074.3 | 1,136.6 | 16.7 | 1.000x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 80.6 | 80.2 | 80.7 | 0.2 | 0.119x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 123.4 | 123.0 | 124.0 | 0.3 | 0.182x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 123.7 | 123.3 | 124.5 | 0.4 | 0.183x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 123.7 | 123.2 | 139.4 | 6.3 | 0.183x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.9 | 123.1 | 124.4 | 0.4 | 0.183x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 284.3 | 279.1 | 285.5 | 2.3 | 0.420x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 321.5 | 292.8 | 339.6 | 17.6 | 0.475x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 672.2 | 665.8 | 709.9 | 12.8 | 0.994x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 676.2 | 669.5 | 690.6 | 6.3 | 1.000x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 82.1 | 82.0 | 82.8 | 0.3 | 0.120x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 83.6 | 81.3 | 91.9 | 3.2 | 0.122x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 115.2 | 115.1 | 116.1 | 0.4 | 0.168x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.4 | 115.3 | 115.9 | 0.3 | 0.169x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 115.5 | 115.4 | 116.1 | 0.2 | 0.169x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 115.8 | 115.2 | 116.9 | 0.6 | 0.169x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 305.8 | 286.8 | 319.2 | 11.4 | 0.447x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 307.6 | 295.2 | 325.7 | 10.5 | 0.450x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 683.5 | 674.6 | 698.7 | 6.0 | 1.000x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 74.4 | 74.3 | 74.8 | 0.2 | 0.113x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 117.0 | 116.7 | 120.4 | 1.4 | 0.178x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 117.0 | 116.7 | 118.6 | 0.7 | 0.178x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 117.5 | 117.3 | 140.9 | 9.3 | 0.179x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 117.8 | 116.9 | 123.8 | 2.6 | 0.179x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 281.2 | 280.4 | 283.8 | 1.2 | 0.428x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 312.3 | 268.1 | 331.3 | 21.9 | 0.476x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 653.1 | 644.5 | 665.3 | 5.8 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 656.5 | 651.9 | 667.6 | 4.5 | 1.000x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 80.6 | 80.3 | 80.9 | 0.2 | 0.123x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 81.5 | 79.0 | 89.9 | 3.2 | 0.124x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 109.6 | 109.5 | 112.4 | 1.1 | 0.167x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 109.7 | 109.6 | 110.3 | 0.2 | 0.167x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 109.7 | 109.6 | 111.2 | 0.6 | 0.167x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 109.9 | 109.5 | 110.4 | 0.3 | 0.168x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 291.5 | 287.3 | 301.9 | 5.9 | 0.445x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 306.0 | 279.9 | 323.8 | 14.3 | 0.467x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 655.7 | 646.7 | 673.3 | 7.1 | 1.000x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.6 | 26.5 | 27.4 | 0.4 | 0.138x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 56.3 | 56.2 | 57.0 | 0.3 | 0.292x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 56.4 | 56.2 | 56.7 | 0.1 | 0.293x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 56.6 | 56.3 | 62.4 | 2.3 | 0.294x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 56.7 | 56.5 | 56.9 | 0.2 | 0.295x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 192.6 | 191.0 | 195.5 | 1.5 | 1.000x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 193.2 | 190.1 | 206.7 | 4.4 | 1.003x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 253.8 | 244.3 | 254.3 | 4.1 | 1.318x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 288.9 | 241.3 | 310.6 | 24.4 | 1.500x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 50.5 | 50.4 | 50.6 | 0.1 | 0.046x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 50.6 | 50.6 | 51.4 | 0.3 | 0.047x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 50.7 | 50.3 | 52.1 | 0.7 | 0.047x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 50.8 | 50.4 | 51.3 | 0.3 | 0.047x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 110.7 | 109.1 | 115.6 | 1.9 | 0.102x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 236.6 | 235.3 | 238.6 | 1.2 | 0.217x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 451.8 | 444.5 | 466.9 | 7.7 | 0.415x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 483.1 | 474.1 | 498.5 | 8.8 | 0.444x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,088.7 | 1,082.7 | 1,142.1 | 16.6 | 1.000x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 87.6 | 87.3 | 87.9 | 0.2 | 0.128x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 136.5 | 136.2 | 137.2 | 0.3 | 0.200x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 136.6 | 136.0 | 137.3 | 0.4 | 0.200x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 136.9 | 136.5 | 138.2 | 0.6 | 0.200x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 136.9 | 136.7 | 146.5 | 3.9 | 0.200x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 287.6 | 286.3 | 290.7 | 1.7 | 0.421x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 333.3 | 318.0 | 351.2 | 11.4 | 0.487x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 683.7 | 679.1 | 707.2 | 7.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 685.8 | 677.0 | 698.1 | 5.3 | 1.003x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 87.2 | 84.0 | 96.0 | 3.4 | 0.127x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 93.5 | 93.2 | 95.1 | 0.7 | 0.136x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 129.1 | 129.0 | 130.3 | 0.5 | 0.187x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 129.2 | 129.0 | 138.2 | 3.6 | 0.187x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 129.3 | 129.1 | 129.7 | 0.2 | 0.188x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 129.3 | 129.0 | 131.3 | 1.0 | 0.188x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 303.1 | 290.1 | 310.5 | 7.2 | 0.440x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 324.7 | 286.3 | 331.9 | 16.8 | 0.471x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 689.1 | 673.2 | 697.4 | 6.4 | 1.000x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 85.7 | 85.6 | 87.1 | 0.6 | 0.121x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.7 | 96.3 | 97.3 | 0.3 | 0.137x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 97.1 | 96.9 | 111.9 | 5.9 | 0.137x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 97.1 | 96.9 | 97.7 | 0.3 | 0.137x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 97.2 | 96.4 | 107.3 | 4.1 | 0.138x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 274.1 | 262.1 | 283.1 | 6.8 | 0.388x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 294.0 | 268.5 | 307.8 | 12.9 | 0.416x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 705.0 | 696.4 | 734.3 | 11.1 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 706.4 | 698.1 | 733.4 | 9.4 | 1.000x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 62.8 | 62.2 | 64.1 | 0.7 | 0.089x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 89.7 | 89.4 | 90.4 | 0.4 | 0.127x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 89.8 | 89.6 | 90.0 | 0.1 | 0.127x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 89.8 | 89.7 | 90.1 | 0.1 | 0.127x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 90.0 | 89.9 | 90.8 | 0.4 | 0.128x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 90.5 | 90.0 | 101.0 | 3.6 | 0.128x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 279.4 | 275.7 | 288.5 | 4.5 | 0.396x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 286.2 | 261.8 | 307.7 | 15.5 | 0.406x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 705.6 | 699.9 | 718.7 | 5.1 | 1.000x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 37.8 | 37.6 | 39.7 | 0.8 | 0.084x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 149.9 | 149.8 | 163.8 | 5.5 | 0.334x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 150.0 | 149.8 | 150.8 | 0.4 | 0.334x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.3 | 149.5 | 150.4 | 0.3 | 0.335x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 150.4 | 150.0 | 155.6 | 2.1 | 0.335x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 250.3 | 242.6 | 260.3 | 6.2 | 0.557x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 286.9 | 254.5 | 296.4 | 14.4 | 0.639x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 448.5 | 444.3 | 466.4 | 5.9 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 449.1 | 447.0 | 455.3 | 2.4 | 1.000x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 42.0 | 41.4 | 42.2 | 0.3 | 0.093x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 71.8 | 70.4 | 79.0 | 2.8 | 0.159x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.0 | 141.9 | 143.4 | 0.6 | 0.315x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 142.1 | 141.9 | 142.9 | 0.4 | 0.315x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 142.4 | 142.3 | 143.1 | 0.3 | 0.315x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 142.5 | 142.1 | 142.8 | 0.2 | 0.316x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 263.2 | 256.0 | 274.4 | 6.8 | 0.583x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 283.2 | 250.2 | 287.8 | 16.0 | 0.627x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 451.5 | 446.4 | 472.7 | 7.2 | 1.000x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 86.6 | 86.2 | 90.1 | 1.5 | 0.130x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.3 | 123.2 | 123.9 | 0.3 | 0.184x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 123.7 | 123.0 | 124.2 | 0.4 | 0.185x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 124.5 | 123.5 | 132.9 | 3.6 | 0.186x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 124.9 | 123.4 | 128.6 | 1.8 | 0.187x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 281.4 | 268.3 | 288.5 | 6.7 | 0.421x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 293.2 | 267.8 | 296.2 | 10.9 | 0.438x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 668.7 | 662.2 | 689.2 | 6.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 669.7 | 663.2 | 684.1 | 5.9 | 1.001x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 64.6 | 62.5 | 70.0 | 2.8 | 0.096x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 84.7 | 82.9 | 95.2 | 4.1 | 0.126x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.4 | 115.0 | 115.4 | 0.2 | 0.172x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 115.4 | 115.0 | 119.5 | 1.7 | 0.172x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 115.6 | 114.9 | 116.8 | 0.7 | 0.172x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 115.7 | 115.0 | 116.3 | 0.5 | 0.173x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 281.9 | 273.3 | 292.4 | 7.1 | 0.421x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 304.3 | 287.9 | 310.1 | 8.2 | 0.454x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 669.9 | 662.5 | 679.3 | 5.3 | 1.000x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 90.6 | 87.7 | 91.2 | 1.5 | 0.127x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 96.9 | 96.7 | 97.4 | 0.3 | 0.136x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 97.0 | 96.8 | 97.4 | 0.2 | 0.136x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 97.4 | 96.9 | 111.4 | 5.6 | 0.136x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 97.8 | 96.8 | 106.6 | 3.6 | 0.137x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 278.9 | 262.3 | 289.4 | 9.3 | 0.390x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 292.5 | 270.0 | 294.8 | 9.2 | 0.409x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 712.7 | 706.3 | 724.7 | 6.0 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 715.0 | 706.7 | 742.6 | 10.1 | 1.000x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 87.5 | 87.5 | 90.8 | 1.3 | 0.123x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 89.5 | 88.9 | 97.4 | 2.5 | 0.126x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 89.9 | 89.8 | 90.5 | 0.3 | 0.126x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 89.9 | 89.6 | 90.3 | 0.2 | 0.126x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 90.1 | 89.3 | 94.1 | 1.7 | 0.127x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 90.3 | 89.6 | 93.6 | 1.4 | 0.127x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 306.6 | 295.5 | 323.1 | 10.0 | 0.431x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 313.9 | 264.9 | 325.1 | 21.9 | 0.441x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 711.0 | 699.3 | 735.3 | 9.1 | 1.000x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 88.4 | 88.2 | 88.6 | 0.1 | 0.121x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 123.4 | 123.1 | 123.8 | 0.3 | 0.169x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 123.4 | 123.2 | 123.8 | 0.2 | 0.169x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 123.7 | 123.3 | 124.9 | 0.6 | 0.170x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 123.8 | 123.4 | 132.9 | 3.7 | 0.170x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 284.0 | 270.3 | 285.5 | 6.0 | 0.389x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 298.1 | 276.3 | 306.6 | 10.4 | 0.409x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 725.5 | 720.4 | 747.6 | 9.1 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 729.4 | 719.6 | 738.8 | 6.0 | 1.000x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 84.4 | 83.9 | 91.8 | 2.8 | 0.116x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 89.1 | 84.6 | 89.3 | 1.8 | 0.122x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 115.3 | 115.0 | 117.5 | 0.9 | 0.158x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 115.3 | 115.2 | 117.7 | 0.9 | 0.158x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 115.3 | 115.2 | 115.4 | 0.1 | 0.158x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 115.5 | 115.0 | 115.8 | 0.3 | 0.158x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 288.9 | 267.9 | 337.4 | 24.7 | 0.396x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 296.2 | 293.8 | 320.4 | 10.5 | 0.406x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 729.3 | 721.5 | 750.9 | 8.6 | 1.000x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 38.1 | 37.6 | 38.2 | 0.2 | 0.085x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.1 | 149.6 | 150.6 | 0.3 | 0.334x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 150.3 | 149.7 | 152.2 | 0.9 | 0.334x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 150.4 | 149.6 | 151.6 | 0.7 | 0.335x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 150.4 | 149.5 | 155.8 | 2.3 | 0.335x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 253.7 | 236.2 | 259.7 | 8.3 | 0.564x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 282.9 | 254.2 | 287.4 | 11.9 | 0.629x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 449.5 | 442.4 | 468.7 | 6.9 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 451.2 | 445.6 | 461.3 | 4.5 | 1.004x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 41.7 | 40.7 | 41.9 | 0.4 | 0.093x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 71.6 | 70.3 | 78.8 | 2.6 | 0.160x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 142.2 | 142.1 | 142.6 | 0.2 | 0.317x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.5 | 142.0 | 142.7 | 0.3 | 0.318x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 142.9 | 142.2 | 159.0 | 6.5 | 0.319x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 143.8 | 142.7 | 144.1 | 0.5 | 0.321x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 272.3 | 253.4 | 279.8 | 10.0 | 0.607x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 290.2 | 257.3 | 299.4 | 14.8 | 0.647x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 448.6 | 445.2 | 485.8 | 11.7 | 1.000x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 86.7 | 86.5 | 96.9 | 4.1 | 0.137x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 150.1 | 149.9 | 150.8 | 0.3 | 0.237x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 150.3 | 150.1 | 153.2 | 1.2 | 0.237x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 150.3 | 149.8 | 159.5 | 3.7 | 0.237x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 150.8 | 150.0 | 153.5 | 1.2 | 0.238x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 273.5 | 267.8 | 292.8 | 8.7 | 0.432x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 295.7 | 272.9 | 311.4 | 12.4 | 0.467x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 631.8 | 626.1 | 648.7 | 6.0 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 633.1 | 627.1 | 642.6 | 4.6 | 1.000x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 62.9 | 62.8 | 63.2 | 0.1 | 0.099x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 82.0 | 81.4 | 93.4 | 3.7 | 0.129x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 142.2 | 142.0 | 142.9 | 0.3 | 0.224x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 142.5 | 141.9 | 142.8 | 0.3 | 0.224x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 142.5 | 142.5 | 149.6 | 2.8 | 0.224x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 143.4 | 142.2 | 144.6 | 0.9 | 0.226x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 277.8 | 271.8 | 297.5 | 9.3 | 0.437x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 283.6 | 272.4 | 305.9 | 12.1 | 0.446x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 636.0 | 627.4 | 661.3 | 9.2 | 1.000x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 34.8 | 34.8 | 35.5 | 0.3 | 0.117x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 43.7 | 43.6 | 43.8 | 0.1 | 0.146x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 43.7 | 43.7 | 44.2 | 0.2 | 0.147x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 44.0 | 43.7 | 48.5 | 1.8 | 0.147x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 44.0 | 43.7 | 44.1 | 0.2 | 0.148x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 250.1 | 247.6 | 254.3 | 2.2 | 0.839x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 287.6 | 262.7 | 295.1 | 11.0 | 0.964x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 297.6 | 289.7 | 309.9 | 4.8 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 298.3 | 294.7 | 310.1 | 4.3 | 1.000x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 37.7 | 37.7 | 38.5 | 0.3 | 0.035x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 37.8 | 37.7 | 37.9 | 0.1 | 0.035x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 37.8 | 37.8 | 38.0 | 0.1 | 0.035x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 37.8 | 37.5 | 37.8 | 0.1 | 0.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 68.7 | 67.3 | 79.4 | 4.3 | 0.064x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 255.6 | 253.2 | 257.8 | 1.7 | 0.238x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 483.4 | 457.8 | 508.2 | 16.1 | 0.451x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 503.9 | 490.8 | 526.6 | 12.2 | 0.470x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,072.5 | 1,060.5 | 1,111.8 | 12.9 | 1.000x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 35.0 | 35.0 | 35.1 | 0.1 | 0.118x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 89.4 | 89.1 | 90.3 | 0.4 | 0.301x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 89.5 | 89.1 | 89.5 | 0.2 | 0.301x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 89.6 | 89.2 | 94.0 | 1.8 | 0.301x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 89.7 | 89.5 | 89.8 | 0.1 | 0.302x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 252.3 | 246.0 | 253.2 | 2.7 | 0.848x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.5 | 254.2 | 294.7 | 13.9 | 0.953x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 297.0 | 289.8 | 309.8 | 6.1 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 297.5 | 293.7 | 302.1 | 2.8 | 1.000x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.6 | 69.3 | 78.7 | 3.1 | 0.066x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 83.1 | 82.9 | 83.2 | 0.1 | 0.078x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 83.2 | 83.0 | 83.4 | 0.1 | 0.078x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 83.2 | 83.1 | 83.3 | 0.1 | 0.078x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 83.3 | 83.1 | 83.7 | 0.2 | 0.078x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 534.0 | 530.3 | 548.8 | 7.0 | 0.499x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 760.1 | 724.7 | 767.9 | 15.3 | 0.710x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 847.1 | 838.8 | 955.4 | 44.4 | 0.791x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,070.7 | 1,058.7 | 1,103.5 | 12.2 | 1.000x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 34.8 | 34.6 | 35.1 | 0.2 | 0.117x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 43.5 | 43.4 | 43.9 | 0.2 | 0.146x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 43.7 | 43.6 | 44.1 | 0.2 | 0.147x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 43.8 | 43.7 | 43.9 | 0.1 | 0.147x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 44.0 | 43.4 | 48.1 | 1.7 | 0.148x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 250.6 | 245.5 | 257.7 | 4.2 | 0.841x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 286.8 | 257.5 | 294.0 | 12.9 | 0.962x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 295.4 | 291.8 | 323.5 | 10.6 | 0.991x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 298.1 | 294.1 | 318.8 | 6.7 | 1.000x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 37.3 | 37.3 | 37.5 | 0.1 | 0.035x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 37.5 | 37.3 | 37.9 | 0.2 | 0.035x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 37.5 | 37.5 | 38.1 | 0.2 | 0.035x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 37.6 | 37.6 | 38.7 | 0.4 | 0.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 68.6 | 67.4 | 78.1 | 3.6 | 0.064x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 263.6 | 255.6 | 269.9 | 5.4 | 0.247x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 475.0 | 458.7 | 491.9 | 11.3 | 0.445x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 526.2 | 521.4 | 550.1 | 11.0 | 0.493x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,068.3 | 1,057.2 | 1,103.3 | 12.4 | 1.000x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 35.0 | 34.8 | 35.1 | 0.1 | 0.118x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 59.9 | 59.7 | 60.0 | 0.1 | 0.202x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 59.9 | 59.6 | 64.8 | 2.0 | 0.202x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 59.9 | 59.9 | 60.0 | 0.0 | 0.202x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 60.0 | 59.8 | 60.1 | 0.1 | 0.202x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 251.7 | 243.7 | 257.7 | 4.9 | 0.848x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 286.4 | 256.7 | 291.3 | 12.7 | 0.965x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 296.3 | 290.7 | 367.2 | 22.5 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 296.8 | 293.3 | 302.3 | 2.8 | 1.000x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 53.4 | 53.2 | 53.7 | 0.2 | 0.050x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 53.6 | 53.2 | 53.9 | 0.3 | 0.050x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 53.9 | 53.6 | 54.3 | 0.2 | 0.050x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 54.0 | 53.7 | 54.0 | 0.1 | 0.050x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.3 | 69.0 | 79.2 | 3.0 | 0.066x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 328.7 | 327.7 | 329.9 | 0.8 | 0.307x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 550.3 | 531.3 | 571.4 | 14.6 | 0.515x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 608.0 | 589.8 | 632.5 | 17.4 | 0.568x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,069.5 | 1,056.0 | 1,114.7 | 17.2 | 1.000x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 48.7 | 47.0 | 51.5 | 1.8 | 0.137x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.5 | 50.3 | 50.7 | 0.2 | 0.141x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 50.6 | 49.9 | 54.7 | 1.7 | 0.142x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 50.7 | 50.4 | 51.1 | 0.3 | 0.142x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 50.9 | 50.5 | 51.5 | 0.4 | 0.142x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 263.2 | 259.9 | 270.9 | 4.3 | 0.737x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.1 | 258.2 | 294.1 | 12.4 | 0.793x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 356.7 | 352.5 | 395.8 | 12.0 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 356.9 | 353.4 | 362.2 | 3.1 | 1.000x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 43.9 | 43.7 | 45.2 | 0.6 | 0.034x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 43.9 | 43.9 | 44.8 | 0.3 | 0.034x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 44.0 | 43.7 | 44.3 | 0.2 | 0.034x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.2 | 43.9 | 44.4 | 0.2 | 0.034x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 72.0 | 70.8 | 80.4 | 2.8 | 0.055x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 387.9 | 380.5 | 394.2 | 4.8 | 0.297x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 612.3 | 586.6 | 617.3 | 11.4 | 0.469x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 620.3 | 607.5 | 632.2 | 8.7 | 0.475x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,305.9 | 1,296.5 | 1,347.5 | 14.8 | 1.000x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 44.0 | 43.7 | 48.4 | 1.8 | 0.140x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 50.3 | 50.1 | 51.4 | 0.5 | 0.160x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 50.4 | 50.0 | 51.5 | 0.5 | 0.161x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 50.6 | 49.8 | 54.3 | 1.6 | 0.161x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.6 | 50.0 | 51.0 | 0.3 | 0.161x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 261.2 | 251.1 | 268.8 | 6.1 | 0.832x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 288.5 | 255.6 | 302.2 | 16.0 | 0.919x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 312.5 | 308.3 | 354.4 | 13.2 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 313.9 | 310.3 | 317.4 | 1.9 | 1.000x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 43.7 | 43.7 | 44.4 | 0.3 | 0.038x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 43.9 | 43.9 | 44.2 | 0.1 | 0.039x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.2 | 44.0 | 44.3 | 0.1 | 0.039x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.3 | 43.9 | 44.9 | 0.4 | 0.039x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.8 | 69.5 | 79.5 | 3.1 | 0.062x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 363.2 | 359.8 | 364.3 | 1.7 | 0.319x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 584.1 | 559.1 | 595.3 | 13.7 | 0.514x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 602.4 | 575.9 | 624.2 | 15.9 | 0.530x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,137.3 | 1,128.3 | 1,171.0 | 11.3 | 1.000x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 26.6 | 0.2 | 0.045x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 36.8 | 36.5 | 39.9 | 1.3 | 0.064x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 36.8 | 36.7 | 37.3 | 0.2 | 0.064x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 37.0 | 36.9 | 37.5 | 0.2 | 0.064x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 37.2 | 37.0 | 37.4 | 0.1 | 0.064x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 246.8 | 237.7 | 251.2 | 5.1 | 0.426x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 285.3 | 259.0 | 295.8 | 12.9 | 0.493x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 576.3 | 571.0 | 618.7 | 13.3 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 579.0 | 570.3 | 590.4 | 5.4 | 1.000x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 30.9 | 30.9 | 31.4 | 0.2 | 0.014x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.2 | 31.2 | 31.3 | 0.0 | 0.014x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 31.3 | 31.2 | 31.3 | 0.1 | 0.014x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 31.7 | 31.0 | 32.0 | 0.4 | 0.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 97.7 | 97.2 | 103.0 | 1.7 | 0.045x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 177.2 | 173.5 | 182.1 | 2.9 | 0.082x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 401.6 | 381.9 | 416.5 | 11.6 | 0.185x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 425.2 | 383.3 | 431.7 | 18.1 | 0.196x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 2,173.4 | 2,161.7 | 2,236.2 | 25.2 | 1.000x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 50.2 | 49.9 | 50.5 | 0.2 | 0.063x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 50.4 | 50.2 | 59.0 | 3.4 | 0.063x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.5 | 50.3 | 51.3 | 0.4 | 0.063x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 50.5 | 50.2 | 50.6 | 0.2 | 0.063x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 116.5 | 116.3 | 117.0 | 0.3 | 0.146x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 318.9 | 317.5 | 339.0 | 8.7 | 0.400x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 356.4 | 322.0 | 382.4 | 21.6 | 0.447x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 794.5 | 783.9 | 846.5 | 21.1 | 0.996x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 798.1 | 778.6 | 810.2 | 9.4 | 1.000x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 43.9 | 43.7 | 45.8 | 0.8 | 0.015x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 44.0 | 43.3 | 45.2 | 0.6 | 0.015x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.0 | 43.9 | 44.2 | 0.1 | 0.015x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.3 | 43.9 | 44.4 | 0.2 | 0.015x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 133.6 | 131.3 | 137.2 | 1.5 | 0.044x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 700.3 | 697.1 | 702.0 | 1.6 | 0.232x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 911.3 | 895.7 | 921.0 | 8.8 | 0.302x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 920.7 | 895.3 | 945.9 | 21.0 | 0.305x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,014.2 | 2,974.3 | 3,093.8 | 39.1 | 1.000x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 26.7 | 0.3 | 0.126x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 53.1 | 53.0 | 53.4 | 0.2 | 0.256x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 53.1 | 52.8 | 53.4 | 0.3 | 0.256x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 53.1 | 52.7 | 61.0 | 3.2 | 0.256x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.4 | 53.2 | 53.6 | 0.2 | 0.258x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 206.2 | 203.1 | 221.7 | 5.2 | 0.996x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 207.1 | 203.1 | 211.5 | 2.7 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 248.7 | 235.1 | 256.0 | 7.8 | 1.201x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 286.3 | 257.3 | 291.7 | 12.3 | 1.383x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 47.3 | 47.3 | 48.6 | 0.5 | 0.064x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 47.6 | 47.3 | 48.2 | 0.3 | 0.065x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.8 | 47.7 | 47.9 | 0.1 | 0.065x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 48.0 | 47.8 | 48.3 | 0.2 | 0.065x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 66.7 | 64.2 | 76.8 | 3.8 | 0.091x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 239.5 | 237.8 | 240.8 | 1.0 | 0.325x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 444.2 | 439.9 | 469.2 | 11.2 | 0.604x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 475.1 | 453.5 | 498.2 | 16.4 | 0.646x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 735.7 | 718.0 | 778.1 | 15.4 | 1.000x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 39.7 | 39.6 | 41.0 | 0.5 | 0.117x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 40.1 | 39.9 | 40.7 | 0.4 | 0.118x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.4 | 40.2 | 40.5 | 0.1 | 0.119x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 40.6 | 40.3 | 40.8 | 0.2 | 0.120x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 40.7 | 40.4 | 48.0 | 2.9 | 0.120x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 254.6 | 249.2 | 271.7 | 8.7 | 0.749x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 280.4 | 240.7 | 300.4 | 20.5 | 0.825x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 337.2 | 334.3 | 364.7 | 8.7 | 0.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 339.7 | 335.3 | 340.9 | 1.7 | 1.000x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 34.6 | 34.5 | 34.9 | 0.2 | 0.028x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 34.7 | 34.6 | 34.9 | 0.1 | 0.029x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 34.9 | 34.7 | 35.8 | 0.4 | 0.029x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 35.0 | 34.5 | 35.1 | 0.2 | 0.029x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.1 | 67.3 | 81.2 | 4.1 | 0.058x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 294.0 | 293.2 | 298.6 | 2.0 | 0.242x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 502.1 | 501.0 | 531.2 | 11.4 | 0.413x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 529.9 | 526.0 | 559.9 | 12.6 | 0.436x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,216.3 | 1,203.2 | 1,245.2 | 13.9 | 1.000x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 53.1 | 53.0 | 55.3 | 0.9 | 0.108x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 53.3 | 52.9 | 62.1 | 3.6 | 0.108x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.3 | 52.9 | 53.4 | 0.2 | 0.108x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 53.5 | 52.9 | 53.6 | 0.3 | 0.109x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 74.2 | 73.8 | 74.4 | 0.2 | 0.151x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 297.1 | 288.1 | 301.4 | 5.1 | 0.603x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 307.6 | 275.6 | 320.7 | 15.5 | 0.624x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 492.6 | 483.0 | 504.1 | 6.6 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 494.2 | 482.2 | 703.4 | 63.0 | 1.003x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 47.5 | 47.3 | 51.0 | 1.4 | 0.026x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.6 | 47.6 | 47.8 | 0.1 | 0.026x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 47.6 | 47.4 | 48.4 | 0.4 | 0.026x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 48.0 | 47.7 | 48.1 | 0.1 | 0.026x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 94.5 | 90.4 | 99.9 | 2.7 | 0.052x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 590.4 | 575.6 | 602.1 | 8.9 | 0.325x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 685.6 | 660.8 | 726.2 | 21.7 | 0.377x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 814.1 | 787.5 | 828.0 | 14.2 | 0.448x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,818.5 | 1,800.6 | 1,884.5 | 24.9 | 1.000x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 28.1 | 0.8 | 0.127x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.5 | 110.4 | 121.6 | 4.4 | 0.539x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.7 | 110.6 | 111.1 | 0.2 | 0.540x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.7 | 110.6 | 111.6 | 0.4 | 0.540x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 110.9 | 110.6 | 119.6 | 3.5 | 0.541x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 204.8 | 198.5 | 213.0 | 4.0 | 0.999x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 205.1 | 200.8 | 209.8 | 3.0 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 253.8 | 247.8 | 271.2 | 8.0 | 1.238x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 291.8 | 255.0 | 298.5 | 15.8 | 1.423x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 105.4 | 105.1 | 106.1 | 0.4 | 0.112x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 105.6 | 105.4 | 106.0 | 0.2 | 0.112x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 105.6 | 105.4 | 108.4 | 1.1 | 0.112x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 105.9 | 105.2 | 111.0 | 2.2 | 0.112x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 106.5 | 104.9 | 113.9 | 2.6 | 0.113x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 109.3 | 105.5 | 110.1 | 1.7 | 0.116x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 334.7 | 325.4 | 350.9 | 10.0 | 0.355x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 351.5 | 330.7 | 374.7 | 15.3 | 0.373x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 943.3 | 927.1 | 989.2 | 16.6 | 1.000x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 25.2 | 25.2 | 25.3 | 0.0 | 0.732x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 34.1 | 33.7 | 40.9 | 2.0 | 0.990x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 34.5 | 34.3 | 38.6 | 1.6 | 1.000x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 46.8 | 46.4 | 46.9 | 0.2 | 1.357x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 46.8 | 46.7 | 47.0 | 0.1 | 1.359x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 46.9 | 46.9 | 48.4 | 0.6 | 1.361x |
| 7 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 47.1 | 46.8 | 48.0 | 0.4 | 1.366x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 241.6 | 228.7 | 254.6 | 10.4 | 7.010x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 244.9 | 230.2 | 263.9 | 12.2 | 7.106x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.1 | 34.9 | 40.7 | 1.7 | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 39.1 | 36.3 | 49.0 | 3.8 | 1.114x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 40.3 | 40.1 | 40.7 | 0.2 | 1.149x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 40.4 | 40.0 | 43.0 | 1.1 | 1.152x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 40.6 | 40.5 | 40.7 | 0.1 | 1.157x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 40.9 | 40.7 | 46.9 | 2.4 | 1.164x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 200.5 | 199.3 | 200.8 | 0.5 | 5.711x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 411.8 | 409.0 | 438.4 | 11.2 | 11.732x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 457.2 | 442.8 | 481.3 | 13.3 | 13.025x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 16.5 | 16.3 | 18.7 | 0.9 | 0.566x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 29.1 | 28.9 | 31.2 | 0.7 | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 29.3 | 29.1 | 29.7 | 0.1 | 1.006x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 34.3 | 34.2 | 34.6 | 0.2 | 1.176x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 34.3 | 33.9 | 35.1 | 0.4 | 1.177x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 34.3 | 33.8 | 34.5 | 0.3 | 1.178x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 34.5 | 34.2 | 39.2 | 1.9 | 1.185x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 253.3 | 237.1 | 269.9 | 11.1 | 8.695x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 261.3 | 246.8 | 263.0 | 7.3 | 8.969x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 29.2 | 29.2 | 29.5 | 0.1 | 0.798x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 29.4 | 29.3 | 30.2 | 0.3 | 0.803x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 29.5 | 29.5 | 29.6 | 0.0 | 0.806x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 29.6 | 29.4 | 30.4 | 0.4 | 0.808x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 36.6 | 35.8 | 42.0 | 1.7 | 1.000x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 41.0 | 36.6 | 50.1 | 3.7 | 1.121x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 144.1 | 143.2 | 144.9 | 0.6 | 3.937x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 357.9 | 344.4 | 373.4 | 9.6 | 9.779x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 370.8 | 358.4 | 446.5 | 31.7 | 10.131x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 17.3 | 17.3 | 17.5 | 0.1 | 0.084x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 17.4 | 17.3 | 18.9 | 0.6 | 0.084x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 17.7 | 17.5 | 17.7 | 0.1 | 0.085x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 17.7 | 17.6 | 18.5 | 0.3 | 0.085x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 18.7 | 18.7 | 19.2 | 0.2 | 0.090x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 207.5 | 205.3 | 213.5 | 2.2 | 1.000x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 207.6 | 204.1 | 212.0 | 2.4 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 249.2 | 215.6 | 268.9 | 17.5 | 1.200x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 264.2 | 240.2 | 277.2 | 13.6 | 1.273x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 12.5 | 12.5 | 13.1 | 0.2 | 0.058x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 12.7 | 12.4 | 13.0 | 0.2 | 0.059x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 12.7 | 12.6 | 13.0 | 0.1 | 0.059x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 12.7 | 12.6 | 14.9 | 0.9 | 0.059x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 53.2 | 51.9 | 60.9 | 3.1 | 0.246x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 64.3 | 63.6 | 64.7 | 0.4 | 0.297x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 216.5 | 214.4 | 225.0 | 3.0 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 279.6 | 273.8 | 291.2 | 7.6 | 1.292x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 312.8 | 289.0 | 334.9 | 16.3 | 1.445x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 23.5 | 23.4 | 24.7 | 0.6 | 0.152x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 130.2 | 130.1 | 130.5 | 0.2 | 0.840x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 130.2 | 130.0 | 138.9 | 3.5 | 0.840x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 130.4 | 130.1 | 130.6 | 0.2 | 0.842x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 130.5 | 130.4 | 138.5 | 3.2 | 0.842x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 152.7 | 149.0 | 162.1 | 3.3 | 0.985x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 155.0 | 151.7 | 163.9 | 3.5 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 238.7 | 235.8 | 250.7 | 5.5 | 1.540x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 264.7 | 253.3 | 270.5 | 6.2 | 1.708x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 102.6 | 98.2 | 108.7 | 3.3 | 0.096x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 124.3 | 124.0 | 124.4 | 0.2 | 0.116x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 124.5 | 124.3 | 125.4 | 0.4 | 0.116x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 124.6 | 124.6 | 124.7 | 0.0 | 0.116x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 124.9 | 124.7 | 125.2 | 0.2 | 0.116x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 150.7 | 147.5 | 151.6 | 1.7 | 0.141x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 369.0 | 351.6 | 393.5 | 13.7 | 0.344x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 369.9 | 352.9 | 378.6 | 9.2 | 0.345x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,072.4 | 1,061.3 | 1,121.2 | 16.4 | 1.000x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 16.4 | 16.3 | 18.4 | 0.8 | 0.561x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 29.2 | 28.9 | 30.9 | 0.6 | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 29.5 | 29.1 | 33.3 | 1.2 | 1.010x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 111.9 | 111.1 | 112.2 | 0.4 | 3.831x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 112.2 | 111.4 | 120.4 | 3.4 | 3.840x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 112.4 | 112.0 | 112.7 | 0.3 | 3.846x |
| 7 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 112.5 | 112.0 | 112.8 | 0.3 | 3.852x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 255.2 | 226.4 | 265.4 | 13.5 | 8.734x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 256.3 | 241.4 | 285.9 | 14.6 | 8.771x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 73.0 | 71.6 | 75.9 | 1.5 | 0.135x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 79.2 | 77.4 | 87.7 | 3.5 | 0.146x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 107.2 | 106.7 | 110.9 | 1.5 | 0.198x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 107.3 | 106.9 | 107.7 | 0.3 | 0.198x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 107.4 | 107.1 | 108.5 | 0.5 | 0.198x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 107.5 | 107.1 | 107.7 | 0.2 | 0.198x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 286.0 | 283.1 | 310.0 | 9.8 | 0.527x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 298.4 | 269.2 | 309.6 | 13.4 | 0.550x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 542.4 | 532.3 | 552.2 | 5.7 | 1.000x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 23.5 | 23.3 | 25.0 | 0.6 | 0.154x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 49.8 | 49.7 | 50.6 | 0.3 | 0.325x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 49.8 | 49.7 | 51.2 | 0.6 | 0.325x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.0 | 49.7 | 51.1 | 0.5 | 0.326x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 50.2 | 50.2 | 51.3 | 0.4 | 0.328x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 152.7 | 149.5 | 159.9 | 3.1 | 0.998x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 153.1 | 149.9 | 159.9 | 3.1 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 242.1 | 232.1 | 249.7 | 6.0 | 1.582x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 265.5 | 252.3 | 278.9 | 9.9 | 1.734x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 43.9 | 43.7 | 45.0 | 0.4 | 0.087x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 44.0 | 43.9 | 45.3 | 0.5 | 0.087x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.1 | 43.9 | 44.5 | 0.2 | 0.087x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.2 | 44.1 | 44.8 | 0.3 | 0.087x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 65.3 | 62.7 | 76.4 | 4.1 | 0.129x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 225.5 | 224.9 | 226.9 | 0.8 | 0.444x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 424.9 | 420.4 | 448.7 | 10.4 | 0.837x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 467.0 | 435.7 | 472.2 | 13.2 | 0.920x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 507.4 | 493.9 | 526.3 | 8.9 | 1.000x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 36.5 | 36.3 | 36.7 | 0.1 | 0.077x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 36.6 | 36.2 | 38.9 | 1.0 | 0.077x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 36.8 | 36.5 | 36.9 | 0.1 | 0.078x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 36.8 | 36.7 | 36.9 | 0.1 | 0.078x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 52.2 | 51.9 | 52.5 | 0.2 | 0.110x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 270.8 | 258.1 | 280.6 | 8.0 | 0.572x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 292.4 | 257.5 | 298.7 | 14.9 | 0.617x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 472.2 | 462.6 | 489.5 | 8.3 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 473.5 | 467.0 | 501.2 | 9.2 | 1.000x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 31.1 | 31.0 | 31.7 | 0.3 | 0.018x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 31.1 | 31.1 | 32.8 | 0.7 | 0.018x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 31.1 | 30.9 | 31.4 | 0.2 | 0.018x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.1 | 31.1 | 31.2 | 0.0 | 0.018x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 87.3 | 84.8 | 95.3 | 3.5 | 0.050x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 348.1 | 347.1 | 349.7 | 0.8 | 0.199x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 545.0 | 523.4 | 549.8 | 9.5 | 0.312x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 570.1 | 543.7 | 582.1 | 13.6 | 0.327x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,745.0 | 1,725.1 | 1,801.8 | 19.8 | 1.000x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.0 | 26.0 | 26.2 | 0.1 | 0.033x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 39.8 | 39.7 | 40.3 | 0.2 | 0.050x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 40.1 | 39.8 | 40.4 | 0.2 | 0.051x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.4 | 39.8 | 40.7 | 0.3 | 0.051x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 40.6 | 39.6 | 45.9 | 2.3 | 0.051x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 242.6 | 233.3 | 258.5 | 8.5 | 0.306x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 285.4 | 256.3 | 291.7 | 12.6 | 0.360x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 788.3 | 779.1 | 841.1 | 16.6 | 0.995x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 792.1 | 777.6 | 805.3 | 7.3 | 1.000x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.4 | 34.3 | 35.0 | 0.2 | 0.011x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 34.4 | 34.3 | 34.8 | 0.2 | 0.011x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 34.4 | 34.3 | 35.3 | 0.4 | 0.011x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 34.5 | 34.3 | 35.2 | 0.3 | 0.011x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 120.2 | 118.0 | 127.8 | 2.6 | 0.040x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 185.1 | 183.0 | 187.5 | 1.5 | 0.061x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 411.5 | 385.9 | 414.6 | 12.5 | 0.136x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 414.7 | 400.7 | 418.1 | 6.3 | 0.137x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 3,031.2 | 3,014.9 | 3,077.8 | 19.4 | 1.000x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 18.8 | 18.6 | 18.9 | 0.1 | 0.063x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 22.2 | 22.1 | 22.4 | 0.1 | 0.075x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 22.3 | 22.3 | 24.2 | 0.8 | 0.075x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 22.4 | 22.3 | 22.7 | 0.1 | 0.075x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 22.5 | 22.2 | 22.8 | 0.2 | 0.075x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 244.1 | 222.3 | 259.1 | 13.3 | 0.820x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 272.5 | 236.7 | 284.6 | 16.7 | 0.915x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 295.8 | 292.6 | 313.6 | 5.7 | 0.994x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 297.6 | 293.8 | 335.8 | 11.8 | 1.000x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 17.9 | 17.8 | 18.8 | 0.3 | 0.022x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 18.1 | 17.9 | 18.7 | 0.3 | 0.022x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 18.2 | 18.2 | 18.3 | 0.1 | 0.023x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 18.3 | 18.2 | 19.0 | 0.3 | 0.023x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 63.7 | 60.5 | 70.6 | 3.4 | 0.079x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 90.3 | 89.4 | 94.2 | 1.6 | 0.112x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 321.2 | 257.1 | 343.9 | 30.7 | 0.397x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 322.3 | 286.3 | 336.8 | 16.9 | 0.398x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 809.6 | 802.4 | 845.3 | 11.8 | 1.000x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 22.3 | 22.1 | 22.5 | 0.1 | 0.154x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 126.6 | 126.5 | 127.1 | 0.2 | 0.872x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 126.8 | 126.4 | 127.8 | 0.5 | 0.874x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 127.0 | 126.4 | 135.9 | 3.6 | 0.875x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 127.1 | 127.0 | 128.4 | 0.6 | 0.876x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 144.1 | 141.2 | 161.5 | 5.5 | 0.993x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 145.1 | 142.2 | 150.7 | 2.3 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 242.4 | 231.9 | 255.3 | 8.6 | 1.671x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 273.4 | 254.4 | 280.0 | 8.7 | 1.884x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 98.5 | 97.1 | 111.0 | 4.2 | 0.096x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 121.2 | 120.8 | 125.5 | 1.8 | 0.118x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 121.5 | 121.0 | 122.1 | 0.4 | 0.118x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 121.6 | 121.5 | 122.7 | 0.5 | 0.118x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 121.6 | 121.6 | 123.8 | 0.8 | 0.118x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 129.5 | 128.1 | 148.4 | 7.7 | 0.126x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 351.0 | 328.4 | 356.8 | 10.2 | 0.341x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 353.7 | 334.7 | 359.6 | 11.2 | 0.344x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,027.9 | 1,018.4 | 1,071.1 | 14.7 | 1.000x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 41.8 | 40.3 | 43.0 | 1.0 | 0.138x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 100.6 | 100.3 | 101.2 | 0.3 | 0.333x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 100.9 | 100.7 | 102.1 | 0.5 | 0.334x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 101.2 | 100.8 | 101.6 | 0.3 | 0.335x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 102.0 | 100.7 | 110.0 | 3.5 | 0.338x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 257.1 | 248.6 | 270.2 | 7.1 | 0.851x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 288.3 | 252.3 | 293.4 | 14.9 | 0.954x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 301.1 | 297.8 | 325.1 | 7.4 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 302.1 | 297.7 | 316.8 | 5.4 | 1.000x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 95.2 | 94.9 | 96.0 | 0.4 | 0.058x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 95.2 | 94.8 | 95.4 | 0.2 | 0.058x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 95.6 | 95.5 | 95.7 | 0.1 | 0.058x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 95.7 | 95.5 | 96.3 | 0.3 | 0.058x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 105.1 | 103.5 | 120.1 | 4.9 | 0.064x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 304.1 | 302.4 | 305.6 | 1.1 | 0.186x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 457.2 | 440.6 | 487.9 | 18.8 | 0.279x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 506.4 | 495.2 | 517.4 | 7.3 | 0.309x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,636.5 | 1,628.4 | 1,675.9 | 13.5 | 1.000x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 22.3 | 22.2 | 23.7 | 0.6 | 0.155x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 126.6 | 126.5 | 127.0 | 0.2 | 0.880x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 127.0 | 126.6 | 127.4 | 0.3 | 0.883x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 127.0 | 126.9 | 134.9 | 3.1 | 0.883x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 127.2 | 126.5 | 135.6 | 3.4 | 0.884x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 143.1 | 140.8 | 158.9 | 5.3 | 0.995x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 143.8 | 140.2 | 149.7 | 2.9 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 239.5 | 232.4 | 254.4 | 8.1 | 1.665x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 271.1 | 253.9 | 279.5 | 8.8 | 1.885x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 98.8 | 97.5 | 119.7 | 6.5 | 0.097x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 121.1 | 120.9 | 124.9 | 1.5 | 0.118x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 121.2 | 121.1 | 122.3 | 0.5 | 0.118x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 121.7 | 121.4 | 122.3 | 0.3 | 0.119x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 121.7 | 121.4 | 122.2 | 0.3 | 0.119x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 128.3 | 127.9 | 129.5 | 0.6 | 0.125x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 343.1 | 336.8 | 355.8 | 7.3 | 0.335x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 350.5 | 329.6 | 356.8 | 9.7 | 0.343x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,022.8 | 1,009.5 | 1,058.3 | 13.4 | 1.000x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.2 | 26.0 | 27.1 | 0.4 | 0.088x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 37.2 | 37.1 | 37.4 | 0.1 | 0.125x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 37.3 | 37.2 | 37.5 | 0.1 | 0.125x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 37.6 | 37.4 | 40.6 | 1.2 | 0.126x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 37.7 | 37.4 | 39.9 | 0.9 | 0.126x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 243.8 | 233.8 | 250.5 | 6.2 | 0.817x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 287.7 | 258.6 | 297.0 | 13.2 | 0.964x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 296.0 | 291.7 | 313.1 | 6.9 | 0.992x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 298.5 | 295.8 | 313.1 | 4.8 | 1.000x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 31.3 | 31.2 | 32.6 | 0.5 | 0.029x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 31.5 | 31.4 | 31.6 | 0.1 | 0.029x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 31.5 | 31.5 | 33.0 | 0.6 | 0.029x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 31.6 | 31.5 | 31.6 | 0.0 | 0.029x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 69.8 | 67.3 | 79.0 | 3.7 | 0.065x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 176.7 | 174.0 | 178.3 | 1.6 | 0.164x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 404.9 | 393.9 | 445.4 | 17.7 | 0.375x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 406.3 | 383.3 | 410.5 | 11.4 | 0.377x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,078.4 | 1,065.9 | 1,113.1 | 12.6 | 1.000x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.2 | 26.1 | 27.2 | 0.4 | 0.089x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 28.2 | 27.8 | 28.3 | 0.2 | 0.095x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 28.2 | 28.1 | 30.0 | 0.7 | 0.095x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 28.3 | 27.9 | 28.7 | 0.2 | 0.096x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 28.4 | 28.2 | 29.9 | 0.6 | 0.096x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 245.3 | 234.8 | 251.4 | 6.2 | 0.829x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 288.2 | 255.0 | 303.5 | 16.3 | 0.974x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 295.4 | 292.4 | 312.2 | 5.6 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 296.0 | 292.5 | 301.4 | 2.6 | 1.000x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 21.3 | 21.0 | 21.6 | 0.2 | 0.020x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 21.3 | 21.1 | 22.7 | 0.6 | 0.020x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.3 | 21.3 | 21.4 | 0.1 | 0.020x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.4 | 21.3 | 21.6 | 0.1 | 0.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 68.7 | 65.8 | 75.7 | 3.2 | 0.064x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 166.8 | 164.9 | 169.1 | 1.5 | 0.156x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 394.7 | 389.4 | 404.9 | 5.1 | 0.370x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 400.8 | 375.0 | 414.4 | 15.0 | 0.376x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,066.8 | 1,049.2 | 1,096.1 | 12.9 | 1.000x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 26.5 | 0.2 | 0.088x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 28.0 | 27.9 | 28.1 | 0.1 | 0.095x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 28.1 | 28.1 | 28.2 | 0.0 | 0.095x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 28.2 | 27.8 | 28.6 | 0.3 | 0.095x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 28.2 | 28.0 | 30.4 | 0.9 | 0.095x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 247.3 | 233.7 | 253.9 | 7.2 | 0.834x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 286.8 | 255.7 | 287.5 | 12.4 | 0.967x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 294.5 | 291.8 | 313.9 | 6.1 | 0.993x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 296.6 | 291.4 | 301.7 | 3.1 | 1.000x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 21.2 | 21.0 | 21.5 | 0.2 | 0.020x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.3 | 21.3 | 21.4 | 0.0 | 0.020x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 21.3 | 21.1 | 21.6 | 0.2 | 0.020x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.3 | 21.3 | 21.8 | 0.2 | 0.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 69.1 | 64.9 | 76.8 | 3.6 | 0.065x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 170.3 | 165.5 | 170.5 | 2.0 | 0.160x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 393.8 | 377.9 | 405.3 | 9.4 | 0.370x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 397.3 | 379.0 | 438.2 | 22.9 | 0.374x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,063.4 | 1,056.9 | 1,090.2 | 9.8 | 1.000x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.2 | 26.1 | 26.6 | 0.2 | 0.088x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 28.1 | 27.8 | 29.7 | 0.7 | 0.094x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 28.1 | 27.9 | 31.8 | 1.5 | 0.094x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 28.2 | 28.0 | 30.6 | 1.0 | 0.095x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 28.3 | 27.9 | 29.0 | 0.3 | 0.095x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 249.5 | 234.4 | 254.8 | 7.6 | 0.839x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.3 | 256.5 | 286.7 | 11.3 | 0.953x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 294.4 | 293.2 | 312.7 | 5.6 | 0.990x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 297.4 | 291.1 | 301.2 | 3.3 | 1.000x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 21.2 | 21.0 | 23.3 | 0.9 | 0.020x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 21.2 | 21.2 | 21.3 | 0.0 | 0.020x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 21.3 | 21.3 | 21.4 | 0.0 | 0.020x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 21.4 | 21.3 | 22.1 | 0.3 | 0.020x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 69.0 | 65.3 | 82.9 | 5.5 | 0.065x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 168.9 | 165.6 | 170.5 | 1.7 | 0.159x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 398.3 | 385.5 | 412.1 | 9.5 | 0.374x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 405.1 | 361.3 | 433.9 | 25.9 | 0.381x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,063.5 | 1,051.7 | 1,136.5 | 24.5 | 1.000x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.2 | 26.0 | 27.7 | 0.6 | 0.088x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 30.9 | 30.7 | 32.4 | 0.6 | 0.104x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 31.0 | 30.7 | 49.6 | 7.5 | 0.104x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 31.0 | 30.8 | 32.3 | 0.6 | 0.104x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 31.2 | 30.5 | 32.0 | 0.5 | 0.105x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 251.2 | 237.2 | 258.0 | 8.5 | 0.844x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.6 | 253.3 | 286.7 | 12.3 | 0.953x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 294.4 | 291.9 | 310.9 | 5.2 | 0.989x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 297.7 | 291.2 | 303.3 | 4.1 | 1.000x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 25.4 | 25.3 | 28.2 | 1.1 | 0.024x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 25.4 | 25.3 | 25.6 | 0.1 | 0.024x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 25.5 | 25.4 | 25.9 | 0.2 | 0.024x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 25.5 | 25.4 | 29.6 | 1.6 | 0.024x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 68.7 | 65.1 | 76.8 | 3.5 | 0.064x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 158.4 | 156.7 | 165.1 | 3.0 | 0.148x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 386.8 | 379.2 | 398.3 | 6.5 | 0.363x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 397.3 | 355.8 | 409.9 | 20.5 | 0.373x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,066.5 | 1,049.0 | 1,094.4 | 11.0 | 1.000x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 7,695.9 | 7,688.4 | 7,744.5 | 20.4 | 0.778x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 7,871.4 | 7,859.3 | 7,894.1 | 13.3 | 0.796x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 7,918.3 | 7,863.2 | 8,002.2 | 48.2 | 0.801x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 9,859.0 | 9,826.6 | 10,000.1 | 47.6 | 0.997x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 9,888.6 | 9,816.3 | 10,328.7 | 144.5 | 1.000x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 67,167.6 | 67,062.7 | 67,293.4 | 73.8 | 6.792x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 67,275.3 | 67,088.8 | 67,324.8 | 85.1 | 6.803x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 67,298.3 | 67,249.2 | 67,361.6 | 38.9 | 6.806x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 67,491.2 | 67,374.7 | 67,996.4 | 226.6 | 6.825x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 5,971.4 | 5,913.7 | 6,151.8 | 86.0 | 0.082x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 6,145.7 | 6,081.6 | 6,201.2 | 44.7 | 0.084x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 6,675.3 | 6,669.3 | 6,695.3 | 9.0 | 0.091x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 26,277.1 | 26,265.4 | 26,325.1 | 21.1 | 0.360x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 26,314.0 | 26,265.1 | 26,510.9 | 88.6 | 0.361x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 26,316.1 | 26,297.5 | 26,343.4 | 15.2 | 0.361x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 26,352.1 | 26,306.2 | 26,422.6 | 39.2 | 0.361x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 72,926.8 | 72,674.5 | 78,811.0 | 1,785.4 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 72,974.5 | 72,670.3 | 74,077.2 | 409.3 | 1.000x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 13,749.4 | 13,740.5 | 13,818.2 | 29.1 | 0.086x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 13,907.4 | 13,872.5 | 14,000.9 | 44.2 | 0.087x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 26,064.0 | 26,020.4 | 26,117.0 | 35.4 | 0.163x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 33,616.7 | 33,597.9 | 33,723.0 | 50.2 | 0.210x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 33,631.4 | 33,583.3 | 33,679.3 | 37.8 | 0.211x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 33,713.1 | 33,688.7 | 33,802.2 | 42.9 | 0.211x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 33,735.5 | 33,683.9 | 33,776.5 | 39.3 | 0.211x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 159,209.6 | 158,732.5 | 161,709.6 | 993.4 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 159,765.7 | 158,786.1 | 162,249.9 | 910.6 | 1.000x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 7,664.6 | 7,656.8 | 7,691.1 | 11.9 | 0.811x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 7,818.9 | 7,785.7 | 7,841.9 | 20.4 | 0.827x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 7,867.9 | 7,833.5 | 7,936.9 | 34.1 | 0.832x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 9,441.1 | 9,419.2 | 9,538.3 | 38.9 | 0.999x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 9,455.0 | 9,423.7 | 9,717.2 | 81.9 | 1.000x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 33,346.9 | 33,334.7 | 33,420.5 | 31.5 | 3.527x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 33,371.9 | 33,315.3 | 33,444.8 | 50.0 | 3.530x |
| 8 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 33,480.3 | 33,462.8 | 33,575.0 | 42.0 | 3.541x |
| 9 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 33,536.1 | 33,522.2 | 33,827.7 | 117.7 | 3.547x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 5,391.2 | 5,373.8 | 5,452.7 | 27.2 | 0.120x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 6,158.0 | 6,137.2 | 6,577.2 | 189.1 | 0.137x |
| 3 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 6,305.0 | 6,296.9 | 6,414.4 | 44.7 | 0.141x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 13,151.7 | 13,147.6 | 13,180.8 | 12.5 | 0.294x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13,152.0 | 13,140.2 | 13,198.9 | 20.9 | 0.294x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 13,196.0 | 13,179.0 | 13,238.8 | 20.3 | 0.295x |
| 7 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 13,197.4 | 13,174.8 | 13,210.4 | 12.5 | 0.295x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 44,659.5 | 44,550.6 | 45,315.0 | 241.1 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 44,787.5 | 44,638.6 | 45,021.3 | 126.5 | 1.000x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 43.7 | 43.7 | 44.6 | 0.3 | 0.138x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 224.8 | 206.7 | 269.3 | 24.6 | 0.708x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 245.4 | 238.7 | 281.9 | 15.9 | 0.772x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 317.8 | 311.4 | 338.8 | 7.0 | 1.000x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 318.8 | 315.8 | 333.2 | 6.2 | 1.003x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 1,684.5 | 1,681.3 | 1,686.7 | 1.9 | 5.301x |
| 7 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 1,685.3 | 1,684.7 | 1,688.6 | 1.4 | 5.303x |
| 8 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 1,686.2 | 1,682.8 | 1,700.4 | 6.2 | 5.306x |
| 9 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 1,690.2 | 1,683.4 | 1,702.9 | 6.3 | 5.319x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 6,877.5 | 6,857.1 | 6,937.4 | 29.1 | 0.062x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 7,041.6 | 7,024.9 | 7,114.8 | 32.0 | 0.064x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 13,122.7 | 13,112.7 | 13,128.9 | 5.8 | 0.119x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 25,194.9 | 25,181.8 | 25,365.2 | 68.7 | 0.228x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 25,206.9 | 25,191.1 | 25,271.8 | 29.2 | 0.228x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 25,279.6 | 25,276.9 | 25,357.2 | 31.2 | 0.228x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 25,351.7 | 25,280.8 | 25,394.7 | 42.0 | 0.229x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 110,340.1 | 109,344.7 | 111,522.2 | 708.7 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 110,690.5 | 110,001.7 | 115,677.4 | 1,580.8 | 1.000x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 10,640.7 | 10,624.5 | 10,649.9 | 10.8 | 0.112x |
| 2 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 10,799.0 | 10,772.3 | 10,869.6 | 34.6 | 0.113x |
| 3 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 11,644.1 | 11,605.0 | 12,777.2 | 455.9 | 0.122x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 26,906.7 | 26,885.4 | 26,925.1 | 14.4 | 0.282x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 26,981.9 | 26,874.9 | 27,098.2 | 89.6 | 0.283x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 27,033.2 | 27,014.2 | 27,185.9 | 70.3 | 0.284x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 27,036.7 | 26,989.2 | 27,561.3 | 212.5 | 0.284x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 95,243.3 | 94,870.7 | 97,338.8 | 665.6 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 95,324.1 | 94,988.7 | 95,877.6 | 282.0 | 1.000x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 16.4 | 16.3 | 19.5 | 1.3 | 0.562x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 29.1 | 28.9 | 30.0 | 0.4 | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 29.4 | 29.1 | 29.6 | 0.1 | 1.010x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 41.3 | 41.2 | 41.4 | 0.1 | 1.419x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 41.3 | 41.2 | 41.8 | 0.2 | 1.420x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 41.5 | 41.1 | 41.7 | 0.2 | 1.425x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 41.6 | 41.1 | 41.7 | 0.2 | 1.430x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 209.5 | 204.8 | 228.4 | 9.6 | 7.201x |
| 9 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 226.1 | 178.6 | 244.2 | 23.5 | 7.769x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 33.7 | 33.7 | 36.2 | 1.0 | 0.059x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 33.8 | 33.5 | 34.7 | 0.4 | 0.060x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 33.9 | 33.4 | 37.0 | 1.3 | 0.060x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 34.6 | 33.7 | 42.2 | 3.1 | 0.061x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 63.4 | 61.0 | 71.7 | 3.2 | 0.112x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 230.0 | 228.5 | 233.7 | 1.7 | 0.405x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 454.9 | 444.0 | 473.6 | 10.8 | 0.802x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 460.4 | 434.4 | 469.0 | 13.9 | 0.812x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 567.2 | 554.6 | 591.0 | 9.1 | 1.000x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 74.6 | 74.6 | 74.8 | 0.1 | 0.113x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 117.2 | 117.1 | 117.4 | 0.1 | 0.177x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 117.2 | 117.1 | 117.3 | 0.1 | 0.177x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 117.2 | 116.6 | 117.6 | 0.4 | 0.177x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 118.6 | 117.4 | 135.5 | 7.1 | 0.179x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 271.1 | 250.8 | 281.1 | 10.8 | 0.410x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 275.5 | 269.2 | 316.5 | 19.6 | 0.417x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 660.1 | 651.3 | 666.3 | 4.8 | 0.998x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 661.2 | 650.8 | 670.8 | 5.0 | 1.000x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 80.4 | 80.3 | 80.8 | 0.2 | 0.121x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 82.6 | 81.1 | 91.6 | 3.5 | 0.125x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 109.9 | 109.6 | 115.7 | 2.4 | 0.166x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 109.9 | 109.6 | 110.2 | 0.2 | 0.166x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 110.0 | 109.7 | 115.2 | 2.1 | 0.166x |
| 6 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 111.5 | 109.7 | 114.7 | 1.8 | 0.168x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 295.4 | 286.8 | 298.9 | 4.8 | 0.446x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 313.8 | 295.5 | 326.8 | 10.6 | 0.474x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 662.3 | 653.2 | 672.3 | 5.6 | 1.000x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 77.7 | 77.7 | 79.6 | 0.8 | 0.121x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.3 | 109.8 | 111.0 | 0.4 | 0.172x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.5 | 110.5 | 110.8 | 0.1 | 0.172x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.6 | 110.1 | 110.8 | 0.2 | 0.172x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 110.8 | 110.2 | 120.0 | 3.8 | 0.173x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 279.4 | 271.6 | 296.7 | 9.2 | 0.435x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 284.0 | 275.8 | 292.6 | 5.8 | 0.443x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 641.8 | 634.4 | 661.2 | 8.3 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 645.6 | 631.4 | 656.9 | 8.2 | 1.006x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 81.9 | 80.9 | 90.9 | 3.7 | 0.128x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 90.0 | 89.8 | 90.1 | 0.1 | 0.140x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.2 | 102.9 | 103.3 | 0.1 | 0.161x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.2 | 102.3 | 104.6 | 0.7 | 0.161x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.3 | 103.0 | 103.9 | 0.3 | 0.161x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.4 | 102.8 | 103.7 | 0.3 | 0.161x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 286.9 | 254.3 | 299.4 | 15.3 | 0.447x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 291.4 | 285.0 | 320.7 | 12.9 | 0.454x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 641.4 | 626.3 | 650.0 | 6.9 | 1.000x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 20.8 | 20.6 | 21.0 | 0.1 | 0.050x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 39.9 | 39.7 | 40.9 | 0.5 | 0.096x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 40.1 | 39.9 | 40.4 | 0.2 | 0.097x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 40.2 | 39.8 | 40.4 | 0.2 | 0.097x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 40.4 | 39.8 | 49.6 | 3.7 | 0.098x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 258.6 | 221.8 | 261.8 | 14.8 | 0.624x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 261.1 | 241.1 | 273.7 | 11.0 | 0.630x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 413.2 | 408.8 | 430.8 | 6.7 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 414.4 | 407.5 | 432.5 | 6.6 | 1.000x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 26.2 | 25.5 | 27.1 | 0.5 | 0.063x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 32.6 | 32.4 | 32.9 | 0.2 | 0.078x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 32.6 | 32.4 | 34.4 | 0.7 | 0.078x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 32.6 | 32.4 | 32.7 | 0.1 | 0.078x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 32.7 | 32.4 | 33.5 | 0.4 | 0.078x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 62.2 | 54.1 | 74.7 | 5.5 | 0.149x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 262.8 | 257.4 | 282.5 | 8.8 | 0.630x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 264.5 | 248.6 | 271.5 | 7.7 | 0.634x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 416.9 | 411.8 | 442.5 | 8.2 | 1.000x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 27.2 | 0.4 | 0.125x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 53.2 | 52.9 | 53.6 | 0.2 | 0.254x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 53.3 | 53.2 | 53.5 | 0.1 | 0.254x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.4 | 53.2 | 53.4 | 0.1 | 0.255x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 54.1 | 53.5 | 54.4 | 0.4 | 0.258x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 207.9 | 205.8 | 223.2 | 5.5 | 0.992x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 209.4 | 208.0 | 222.5 | 4.4 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 244.5 | 224.4 | 261.5 | 12.1 | 1.167x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.0 | 241.7 | 299.4 | 19.2 | 1.351x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 47.0 | 47.0 | 48.3 | 0.5 | 0.065x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.2 | 47.2 | 47.4 | 0.1 | 0.065x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 47.2 | 47.1 | 47.4 | 0.1 | 0.065x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.4 | 47.1 | 47.8 | 0.2 | 0.065x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 66.7 | 65.4 | 84.9 | 6.1 | 0.092x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 236.5 | 235.7 | 241.4 | 2.1 | 0.325x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 455.5 | 442.6 | 469.0 | 9.7 | 0.626x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 455.8 | 441.9 | 478.7 | 12.1 | 0.627x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 727.5 | 716.7 | 770.4 | 14.0 | 1.000x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 44.7 | 44.2 | 46.1 | 0.7 | 0.082x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 90.7 | 90.3 | 90.8 | 0.2 | 0.167x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 90.9 | 90.7 | 91.2 | 0.1 | 0.167x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 91.0 | 90.7 | 94.0 | 1.2 | 0.168x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 91.0 | 90.6 | 100.7 | 3.9 | 0.168x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 262.9 | 251.6 | 292.8 | 14.5 | 0.484x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 287.6 | 247.3 | 292.2 | 16.4 | 0.529x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 542.4 | 536.1 | 578.9 | 13.0 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 543.2 | 541.1 | 561.1 | 7.2 | 1.000x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 51.3 | 51.0 | 52.1 | 0.4 | 0.094x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 76.7 | 74.0 | 83.9 | 3.3 | 0.141x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 82.9 | 82.7 | 83.4 | 0.3 | 0.152x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 83.4 | 83.3 | 84.0 | 0.3 | 0.153x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 83.4 | 83.2 | 84.3 | 0.4 | 0.153x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 83.8 | 82.7 | 84.7 | 0.8 | 0.154x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 273.0 | 262.6 | 284.5 | 6.9 | 0.501x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 282.8 | 268.4 | 289.3 | 7.8 | 0.519x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 544.9 | 539.0 | 553.3 | 4.2 | 1.000x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 58.4 | 57.8 | 60.6 | 1.0 | 0.104x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 201.9 | 201.6 | 202.4 | 0.3 | 0.360x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 202.2 | 201.0 | 202.7 | 0.6 | 0.360x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 202.6 | 202.4 | 203.6 | 0.4 | 0.361x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 204.5 | 202.7 | 213.3 | 4.7 | 0.364x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 271.8 | 269.9 | 276.6 | 2.4 | 0.484x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 278.7 | 244.0 | 288.8 | 16.4 | 0.497x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 561.0 | 558.9 | 571.1 | 3.6 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 561.6 | 555.6 | 580.0 | 8.4 | 1.001x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 65.4 | 65.2 | 67.6 | 0.9 | 0.116x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 91.4 | 88.4 | 101.4 | 4.1 | 0.163x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 194.4 | 194.2 | 195.1 | 0.3 | 0.346x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 194.7 | 194.2 | 194.9 | 0.3 | 0.346x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 200.6 | 200.3 | 202.2 | 0.8 | 0.357x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 201.1 | 200.6 | 202.4 | 0.6 | 0.358x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 281.7 | 272.8 | 295.4 | 7.4 | 0.501x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 286.9 | 265.0 | 293.8 | 10.4 | 0.510x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 562.3 | 556.7 | 575.2 | 5.7 | 1.000x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 67.1 | 66.9 | 68.0 | 0.4 | 0.056x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 166.0 | 165.8 | 166.9 | 0.4 | 0.139x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 166.1 | 165.8 | 166.4 | 0.2 | 0.139x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 166.2 | 166.1 | 168.9 | 1.0 | 0.139x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 166.3 | 166.0 | 174.8 | 3.4 | 0.139x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 300.0 | 285.2 | 306.2 | 7.4 | 0.251x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 386.8 | 324.0 | 394.8 | 26.0 | 0.324x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 1,193.2 | 1,181.4 | 1,241.6 | 16.9 | 1.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,193.7 | 1,173.4 | 1,213.3 | 11.8 | 1.000x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 153.6 | 153.1 | 154.8 | 0.6 | 0.088x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 160.6 | 160.5 | 162.4 | 0.7 | 0.092x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 160.8 | 160.4 | 161.4 | 0.4 | 0.093x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 160.8 | 160.7 | 162.1 | 0.5 | 0.093x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 160.8 | 160.5 | 162.3 | 0.6 | 0.093x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 172.0 | 168.1 | 198.0 | 8.7 | 0.099x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 368.4 | 350.2 | 380.0 | 11.0 | 0.212x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 424.0 | 400.5 | 426.5 | 10.6 | 0.244x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,736.9 | 1,729.4 | 1,772.7 | 14.8 | 1.000x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 26.1 | 26.0 | 26.9 | 0.3 | 0.087x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 40.2 | 40.1 | 40.5 | 0.1 | 0.134x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 40.2 | 39.5 | 41.0 | 0.5 | 0.134x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 40.3 | 40.2 | 44.9 | 1.9 | 0.134x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 40.5 | 40.4 | 40.7 | 0.1 | 0.135x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 246.7 | 231.9 | 248.2 | 6.1 | 0.823x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 285.9 | 242.5 | 291.5 | 17.9 | 0.954x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 298.9 | 292.3 | 318.4 | 7.9 | 0.997x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 299.7 | 295.8 | 321.4 | 7.0 | 1.000x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 34.5 | 34.3 | 35.0 | 0.2 | 0.032x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 34.5 | 34.3 | 35.6 | 0.5 | 0.032x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 34.5 | 34.5 | 34.6 | 0.1 | 0.032x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 34.6 | 34.4 | 34.7 | 0.1 | 0.032x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 70.2 | 67.4 | 76.6 | 3.0 | 0.065x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 190.0 | 188.8 | 190.7 | 0.6 | 0.177x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 406.4 | 385.4 | 426.1 | 13.6 | 0.379x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 420.2 | 411.0 | 458.6 | 17.6 | 0.392x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,073.2 | 1,054.5 | 1,116.6 | 15.4 | 1.000x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 35.1 | 35.0 | 35.1 | 0.0 | 0.117x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 53.3 | 53.1 | 54.9 | 0.7 | 0.178x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 53.5 | 52.9 | 58.6 | 2.1 | 0.178x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 53.5 | 53.1 | 53.6 | 0.2 | 0.178x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 53.6 | 53.5 | 53.7 | 0.1 | 0.179x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 253.0 | 236.4 | 253.9 | 6.7 | 0.844x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 285.3 | 247.8 | 291.0 | 16.0 | 0.952x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 296.3 | 295.0 | 417.3 | 36.1 | 0.989x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 299.6 | 292.9 | 335.8 | 13.0 | 1.000x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 47.1 | 46.9 | 48.7 | 0.7 | 0.044x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 47.3 | 46.9 | 47.8 | 0.4 | 0.044x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 47.5 | 47.4 | 48.0 | 0.2 | 0.044x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 47.5 | 47.3 | 48.0 | 0.3 | 0.045x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 71.8 | 69.5 | 77.8 | 2.5 | 0.067x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 303.6 | 301.5 | 304.6 | 1.2 | 0.284x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 531.2 | 504.6 | 550.2 | 16.9 | 0.498x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 578.4 | 546.6 | 597.8 | 18.7 | 0.542x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,067.7 | 1,058.4 | 1,103.4 | 12.8 | 1.000x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 88.4 | 88.3 | 90.1 | 0.7 | 0.139x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.5 | 110.3 | 111.0 | 0.2 | 0.173x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.6 | 110.2 | 110.9 | 0.3 | 0.174x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.6 | 110.1 | 110.9 | 0.3 | 0.174x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 111.2 | 110.6 | 119.9 | 3.6 | 0.175x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 280.6 | 270.4 | 286.7 | 6.1 | 0.441x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 292.4 | 271.6 | 297.6 | 9.0 | 0.459x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 637.0 | 629.3 | 650.5 | 6.7 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 639.0 | 630.7 | 767.2 | 39.0 | 1.003x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 69.2 | 68.9 | 69.6 | 0.2 | 0.108x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 88.3 | 87.2 | 93.7 | 1.9 | 0.138x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 102.7 | 102.5 | 103.8 | 0.4 | 0.161x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.2 | 102.9 | 103.3 | 0.2 | 0.161x |
| 5 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.2 | 103.1 | 103.5 | 0.2 | 0.161x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.4 | 103.2 | 104.6 | 0.5 | 0.162x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 278.8 | 265.6 | 290.1 | 9.9 | 0.436x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 292.0 | 281.4 | 303.0 | 7.7 | 0.457x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 639.0 | 628.1 | 651.5 | 6.8 | 1.000x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 88.6 | 88.2 | 89.2 | 0.4 | 0.140x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.5 | 110.4 | 110.7 | 0.1 | 0.174x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.6 | 110.5 | 111.5 | 0.4 | 0.175x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.7 | 110.5 | 111.4 | 0.3 | 0.175x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 111.2 | 110.4 | 119.6 | 3.5 | 0.176x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 277.5 | 267.7 | 282.2 | 5.0 | 0.438x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 292.4 | 270.6 | 298.9 | 10.4 | 0.462x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 632.8 | 628.2 | 660.1 | 10.1 | 0.999x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 633.2 | 625.3 | 654.0 | 8.0 | 1.000x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 69.2 | 69.1 | 69.3 | 0.1 | 0.109x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 88.2 | 87.3 | 92.1 | 1.3 | 0.139x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 102.9 | 102.7 | 105.6 | 1.1 | 0.162x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.2 | 102.2 | 103.6 | 0.5 | 0.162x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.4 | 103.1 | 103.7 | 0.2 | 0.162x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.4 | 103.2 | 103.7 | 0.2 | 0.162x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 280.7 | 265.6 | 290.5 | 8.9 | 0.441x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 293.8 | 277.7 | 303.6 | 9.1 | 0.461x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 636.7 | 629.0 | 647.1 | 5.0 | 1.000x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 87.3 | 86.5 | 88.4 | 0.6 | 0.124x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.4 | 109.4 | 110.9 | 0.5 | 0.157x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.6 | 110.5 | 111.2 | 0.3 | 0.157x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.9 | 110.5 | 111.5 | 0.3 | 0.158x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 110.9 | 110.5 | 119.6 | 3.5 | 0.158x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 275.0 | 269.5 | 287.8 | 6.4 | 0.391x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 298.0 | 272.1 | 300.6 | 10.6 | 0.424x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 703.2 | 695.5 | 721.9 | 7.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 707.2 | 693.3 | 854.4 | 45.6 | 1.006x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 62.8 | 62.3 | 69.7 | 2.8 | 0.090x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 88.9 | 88.3 | 91.8 | 1.0 | 0.127x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.0 | 102.8 | 103.3 | 0.2 | 0.147x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.3 | 103.1 | 103.4 | 0.1 | 0.148x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.4 | 102.7 | 103.8 | 0.4 | 0.148x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.4 | 103.1 | 104.0 | 0.3 | 0.148x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 286.5 | 249.0 | 320.6 | 27.0 | 0.409x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 291.4 | 273.9 | 310.4 | 12.3 | 0.416x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 699.8 | 693.9 | 720.0 | 6.9 | 1.000x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 74.0 | 73.8 | 74.1 | 0.1 | 0.102x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.5 | 110.3 | 133.8 | 9.3 | 0.152x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 110.8 | 110.4 | 111.1 | 0.2 | 0.153x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 110.9 | 110.8 | 117.2 | 2.5 | 0.153x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 111.1 | 110.7 | 115.1 | 1.8 | 0.153x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 271.0 | 267.3 | 273.5 | 2.4 | 0.374x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 289.1 | 268.1 | 297.4 | 10.2 | 0.399x |
| 8 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 724.6 | 712.5 | 768.0 | 15.4 | 1.000x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 724.8 | 714.6 | 747.6 | 8.8 | 1.000x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 64.7 | 60.0 | 72.1 | 4.2 | 0.089x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 84.7 | 83.1 | 89.1 | 1.8 | 0.117x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.2 | 103.0 | 103.6 | 0.2 | 0.142x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.2 | 103.1 | 103.3 | 0.1 | 0.142x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.3 | 103.2 | 121.5 | 7.2 | 0.142x |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.4 | 103.3 | 104.4 | 0.4 | 0.142x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 277.5 | 263.8 | 296.3 | 11.2 | 0.382x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 284.6 | 239.8 | 321.1 | 29.3 | 0.392x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 726.7 | 716.7 | 773.2 | 15.2 | 1.000x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 73.9 | 73.8 | 74.0 | 0.1 | 0.102x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 110.4 | 109.7 | 111.9 | 0.7 | 0.153x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 110.5 | 109.8 | 111.1 | 0.5 | 0.153x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 110.6 | 110.3 | 114.9 | 1.7 | 0.153x |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 111.0 | 110.3 | 111.9 | 0.5 | 0.154x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 270.8 | 267.2 | 281.1 | 4.8 | 0.375x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 283.5 | 263.9 | 309.9 | 17.0 | 0.392x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 722.4 | 717.5 | 746.1 | 9.2 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 723.2 | 711.7 | 764.6 | 15.1 | 1.001x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 64.9 | 62.1 | 67.9 | 2.2 | 0.089x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 84.5 | 83.1 | 88.5 | 1.7 | 0.116x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 103.0 | 102.6 | 103.1 | 0.2 | 0.142x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 103.1 | 102.6 | 103.8 | 0.4 | 0.142x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 103.3 | 103.1 | 104.4 | 0.4 | 0.142x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 103.3 | 102.9 | 104.0 | 0.4 | 0.142x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 285.7 | 268.5 | 306.5 | 13.4 | 0.393x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 297.0 | 249.2 | 320.4 | 24.9 | 0.408x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 727.6 | 718.8 | 748.0 | 8.3 | 1.000x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 46.8 | 46.6 | 47.5 | 0.3 | 0.133x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 50.4 | 50.0 | 54.8 | 1.8 | 0.143x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 50.4 | 50.1 | 51.5 | 0.5 | 0.143x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 50.5 | 49.7 | 54.9 | 1.9 | 0.144x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 50.5 | 50.2 | 51.0 | 0.2 | 0.144x |
| 6 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 265.9 | 261.8 | 273.7 | 4.2 | 0.756x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 284.1 | 254.5 | 287.4 | 12.3 | 0.808x |
| 8 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 351.7 | 348.5 | 374.4 | 7.4 | 1.000x |
| 9 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 355.5 | 347.6 | 388.0 | 12.3 | 1.011x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 43.9 | 43.7 | 44.4 | 0.3 | 0.034x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 44.0 | 43.9 | 44.2 | 0.1 | 0.034x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 44.1 | 44.0 | 44.4 | 0.1 | 0.034x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 44.4 | 43.7 | 46.1 | 0.8 | 0.035x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 71.7 | 70.3 | 80.6 | 3.3 | 0.056x |
| 6 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 378.5 | 377.2 | 379.4 | 0.8 | 0.296x |
| 7 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 598.9 | 590.0 | 600.5 | 3.9 | 0.468x |
| 8 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 611.2 | 603.0 | 638.0 | 12.5 | 0.478x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 1,279.5 | 1,266.8 | 1,315.6 | 13.2 | 1.000x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 11.9 | 11.8 | 12.3 | 0.2 | 0.408x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 12.1 | 11.9 | 12.1 | 0.1 | 0.412x |
| 3 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 12.5 | 12.4 | 12.6 | 0.1 | 0.426x |
| 4 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13.3 | 12.1 | 15.6 | 1.4 | 0.454x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 15.6 | 15.5 | 16.8 | 0.5 | 0.533x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 29.0 | 28.9 | 34.2 | 1.6 | 0.993x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 29.2 | 29.0 | 29.5 | 0.1 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 247.4 | 224.7 | 268.2 | 13.8 | 8.462x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 262.5 | 250.8 | 272.2 | 7.2 | 8.978x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 4.6 | 4.5 | 5.3 | 0.3 | 0.150x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 4.8 | 4.7 | 5.1 | 0.1 | 0.158x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 4.8 | 4.7 | 5.0 | 0.1 | 0.159x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 4.9 | 4.4 | 5.5 | 0.4 | 0.159x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 17.2 | 17.1 | 18.9 | 0.7 | 0.563x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 30.5 | 30.1 | 31.0 | 0.4 | 1.000x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 37.7 | 36.6 | 52.3 | 4.7 | 1.237x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 209.2 | 204.4 | 235.5 | 11.5 | 6.861x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 247.9 | 239.0 | 271.2 | 12.3 | 8.132x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 13.0 | 12.7 | 15.4 | 1.0 | 0.439x |
| 2 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 13.3 | 13.0 | 14.1 | 0.4 | 0.447x |
| 3 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 13.5 | 12.8 | 14.8 | 0.7 | 0.454x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 14.2 | 13.3 | 17.6 | 1.6 | 0.478x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 16.4 | 16.3 | 18.7 | 0.9 | 0.553x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 29.6 | 29.3 | 31.5 | 0.7 | 0.996x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 29.7 | 29.0 | 30.8 | 0.6 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 248.7 | 229.0 | 268.5 | 12.5 | 8.380x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 263.1 | 251.1 | 271.3 | 6.9 | 8.865x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 5.1 | 5.1 | 6.8 | 0.7 | 0.163x |
| 2 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 5.1 | 5.0 | 6.2 | 0.4 | 0.165x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 5.6 | 5.4 | 6.0 | 0.2 | 0.180x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 5.6 | 5.6 | 6.2 | 0.2 | 0.180x |
| 5 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 24.0 | 23.9 | 26.9 | 1.1 | 0.771x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 31.1 | 31.0 | 34.9 | 1.1 | 1.000x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 40.1 | 37.5 | 48.7 | 3.1 | 1.288x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 245.4 | 217.0 | 261.2 | 16.5 | 7.880x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 261.6 | 239.0 | 298.0 | 22.9 | 8.401x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 21.6 | 21.5 | 22.6 | 0.4 | 0.589x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 35.7 | 34.6 | 38.1 | 1.1 | 0.976x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 36.6 | 34.8 | 38.7 | 1.0 | 1.000x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 138.0 | 137.6 | 138.2 | 0.2 | 3.769x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 138.1 | 137.9 | 138.2 | 0.1 | 3.771x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 138.1 | 138.0 | 138.2 | 0.1 | 3.773x |
| 7 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 138.5 | 138.2 | 139.1 | 0.4 | 3.784x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 244.7 | 240.3 | 248.0 | 2.5 | 6.685x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 272.3 | 257.7 | 282.2 | 7.8 | 7.439x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.6 | 35.4 | 43.4 | 2.3 | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 41.5 | 39.9 | 50.7 | 3.1 | 1.166x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 132.0 | 131.8 | 132.6 | 0.3 | 3.710x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 132.1 | 132.0 | 134.3 | 1.0 | 3.714x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 132.2 | 132.1 | 132.5 | 0.1 | 3.718x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 132.3 | 132.2 | 132.8 | 0.2 | 3.719x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 616.6 | 613.7 | 630.9 | 6.1 | 17.335x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 839.0 | 809.0 | 845.9 | 13.6 | 23.588x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 863.7 | 841.5 | 868.4 | 12.1 | 24.283x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_692c2e8_vm-in-caps-simdna` | `whole-subject` | 23.1 | 22.9 | 24.4 | 0.6 | 0.655x |
| 2 | `pcrec_692c2e8_auto-nocaps-simdna` | `whole-subject` | 30.2 | 29.7 | 31.4 | 0.5 | 0.858x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `whole-subject` | 30.3 | 30.1 | 31.5 | 0.5 | 0.861x |
| 4 | `pcrec_8da6120_auto-nocaps-simdna` | `whole-subject` | 30.3 | 30.1 | 31.3 | 0.4 | 0.862x |
| 5 | `pcrec_8da6120_auto-caps-simdna` | `whole-subject` | 30.4 | 30.2 | 30.5 | 0.1 | 0.863x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 34.7 | 33.6 | 37.1 | 1.0 | 0.987x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.2 | 34.2 | 38.4 | 1.4 | 1.000x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `whole-subject` | 237.2 | 225.7 | 246.4 | 6.7 | 6.736x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `whole-subject` | 260.4 | 233.4 | 264.2 | 11.5 | 7.395x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 24.9 | 24.9 | 27.0 | 0.8 | 0.711x |
| 2 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 25.0 | 24.9 | 26.6 | 0.6 | 0.714x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 25.2 | 25.2 | 26.1 | 0.4 | 0.720x |
| 4 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 25.2 | 25.2 | 25.4 | 0.1 | 0.721x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 35.0 | 34.8 | 42.1 | 2.1 | 1.000x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 39.8 | 38.4 | 50.5 | 3.5 | 1.136x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 125.0 | 124.2 | 126.9 | 0.9 | 3.571x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 328.6 | 325.1 | 353.0 | 10.5 | 9.387x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 353.9 | 350.0 | 375.6 | 9.4 | 10.109x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 3,697,867.3 | 3,619,893.5 | 3,962,741.4 | 86,596.2 | 0.128x |
| 2 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 5,514,810.0 | 5,497,894.8 | 5,886,715.0 | 151,500.9 | 0.191x |
| 3 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 6,542,380.1 | 6,533,295.3 | 6,549,917.4 | 5,888.6 | 0.227x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 6,546,199.3 | 6,535,898.5 | 6,599,885.0 | 23,271.6 | 0.227x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 6,546,520.9 | 6,535,742.9 | 6,597,911.3 | 22,726.1 | 0.227x |
| 6 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 6,553,414.3 | 6,536,042.1 | 6,570,095.1 | 12,053.2 | 0.227x |
| 7 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 12,112,463.0 | 11,459,356.0 | 13,238,110.3 | 652,907.4 | 0.420x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 12,594,527.0 | 11,540,583.2 | 12,999,718.2 | 513,274.6 | 0.437x |
| 9 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 28,846,216.7 | 28,708,957.9 | 29,162,079.1 | 149,462.8 | 1.000x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio |
|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 17,779.9 | 17,704.4 | 28,635.8 | 3,248.7 | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 2,569,259.8 | 2,533,967.4 | 2,586,428.6 | 17,035.5 | 144.503x |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 3,420,686.1 | 3,418,064.7 | 3,422,532.7 | 1,492.9 | 192.390x |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 3,428,525.6 | 3,418,886.9 | 3,463,530.5 | 15,999.0 | 192.831x |
| 5 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 3,431,061.7 | 3,418,017.7 | 3,463,327.2 | 17,059.5 | 192.974x |
| 6 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 3,433,874.3 | 3,419,820.9 | 3,458,171.2 | 14,923.8 | 193.132x |
| 7 | `pcrec_692c2e8_vm-in-caps-simdna` | `plain` | 16,029,994.2 | 15,803,482.8 | 16,746,954.0 | 323,159.8 | 901.579x |
| 8 | `pcrec_692c2e8_vm-caps-simdna` | `plain` | 16,153,819.5 | 15,986,018.8 | 16,494,018.2 | 181,111.1 | 908.543x |
| 9 | `pcrec_8da6120_vm-caps-simdna` | `plain` | 16,968,804.0 | 16,819,943.0 | 17,133,175.0 | 99,216.8 | 954.380x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.1)

| rank | testee | form | median ns/call | min | max | stddev | ratio | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | `plain` | 17,785.8 | 17,727.8 | 22,237.2 | 1,318.8 | 1.000x | 10 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | `plain` | 2,830,193.0 | 2,821,643.6 | 2,842,780.3 | 5,488.0 | 159.127x | 10 | 100% |
| 3 | `pcrec_692c2e8_auto-caps-simdna` | `plain` | 3,417,759.4 | 3,414,384.1 | 3,420,838.7 | 2,304.4 | 192.163x | 5 | 100% |
| 4 | `pcrec_8da6120_auto-caps-simdna` | `plain` | 3,422,799.6 | 3,414,990.9 | 3,436,319.7 | 8,063.5 | 192.446x | 5 | 100% |
| 5 | `pcrec_8da6120_auto-nocaps-simdna` | `plain` | 3,424,102.3 | 3,415,649.6 | 3,511,766.2 | 35,973.8 | 192.519x | 5 | 100% |
| 6 | `pcrec_692c2e8_auto-nocaps-simdna` | `plain` | 3,431,051.7 | 3,417,933.7 | 3,456,455.2 | 13,313.4 | 192.910x | 5 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | form | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-058` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-059` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-061` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-063` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `s-064` | `match-compliance` | `whole-subject` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 10 | 0% | 0 | 0 | timed-out=10 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_auto-nocaps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_692c2e8_vm-in-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |
| `orig` | `t-c-long-atom-run` | `large-subject-throughput` | `plain` | `pcrec_8da6120_vm-caps-simdna` | 5 | 0% | 5 | 0 | gave-up=5 |

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

