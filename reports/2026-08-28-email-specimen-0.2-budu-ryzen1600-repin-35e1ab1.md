# pcrec-bench report

reporter: v6 (2026-08-28)

## Query

- filters: subbench=email-specimen, version=0.2
- record source: store/index.tsv (26 candidate file(s))
- records included: 6
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260828T145051Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260828T145051Z.jsonl)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260828T141718Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260828T141718Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-nocaps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-in-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z.jsonl)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 13,593,900.0 | 2.5928 | 13,556,964.8 | 13,728,371.4 | 59,896.2 | 0.027x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 13,684,627.4 | 2.6101 | 13,638,732.1 | 13,864,401.6 | 78,198.4 | 0.027x | 1.007x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 501,204,604.4 | 95.5972 | 498,857,639.0 | 504,528,853.9 | 1,816,122.3 | 1.000x | 36.870x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,578,231.1 | 3.4125 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,591,987.4 | 3.4256 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,651,471.6 | 49.2587 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,890,786.8 | 1.8032 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,877,191.1 | 1.7902 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,035.0 | 0.0182 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,876,102.3 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,875,979.8 | 1.7891 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,766.5 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,143,556.6 | 2.9979 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,194,847.5 | 3.0468 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 449,517,489.8 | 428.6933 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,098,348.9 | 2.9548 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,146,368.5 | 3.0006 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,000.4 | 0.0181 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130,228.4 | 130,199.9 | 130,355.6 | 55.7 | 0.071x | 1.000x | 85 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 133,944.5 | 133,867.9 | 134,190.9 | 110.3 | 0.073x | 1.029x | 85 | 100% |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 456,277.5 | 454,029.4 | 463,699.5 | 3,715.3 | 0.250x | 3.504x | 85 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,825,025.0 | 1,815,613.3 | 1,867,137.1 | 20,348.5 | 1.000x | 14.014x | 85 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,852,787.7 | 1,824,863.0 | 1,854,982.2 | 13,705.0 | 1.015x | 14.227x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,528.7 | 3,525.8 | 3,539.3 | 5.0 | 0.026x | 1.000x | 77 | 45.8 | 17.7 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,666.5 | 3,665.8 | 3,669.9 | 1.5 | 0.027x | 1.039x | 77 | 47.6 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,290.9 | 15,257.2 | 15,566.4 | 127.7 | 0.111x | 4.333x | 77 | 198.6 | 44.2 | 100% |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 53,852.7 | 53,636.1 | 54,444.3 | 320.9 | 0.391x | 15.261x | 77 | 699.4 | 32.6 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54,151.3 | 53,905.1 | 54,258.7 | 119.1 | 0.393x | 15.346x | 77 | 703.3 | 32.9 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,828.5 | 137,490.3 | 138,452.9 | 336.3 | 1.000x | 39.060x | 77 | 1,790.0 | 96.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 711,403.3 | 0.1357 | 710,834.2 | 714,069.7 | 1,159.6 | 0.192x | 1.000x | spread |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 712,658.0 | 0.1359 | 711,305.9 | 713,849.5 | 824.2 | 0.192x | 1.002x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,895,312.2 | 0.3615 | 1,861,172.0 | 1,988,350.5 | 45,725.8 | 0.510x | 2.664x | **dominated**: `t-a-valid-addrs` is 90.1% of this set |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,714,520.4 | 0.7085 | 3,670,703.3 | 3,746,187.1 | 28,012.6 | 1.000x | 5.221x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |
| 5 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 15,694,249.9 | 2.9934 | 15,644,181.0 | 16,112,979.1 | 173,516.2 | 4.225x | 22.061x | spread |
| 6 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 15,827,138.2 | 3.0188 | 15,789,874.1 | 15,846,666.6 | 18,853.1 | 4.261x | 22.248x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 627,186.7 | 0.5981 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 628,561.1 | 0.5994 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,707,833.8 | 1.6287 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,590,816.7 | 3.4245 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 3,908,618.9 | 3.7275 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 4,074,182.9 | 3.8854 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,705.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,720.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,218.5 | 0.0374 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,761.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,793,280.9 | 2.6639 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,790,208.5 | 2.6610 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,705.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,715.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,429.5 | 0.0376 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,774.7 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,790,950.1 | 2.6617 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,790,569.1 | 2.6613 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 30,813.1 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 30,873.3 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,063.3 | 0.0659 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,023.5 | 0.0668 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 3,345,865.5 | 3.1909 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 3,371,357.6 | 3.2152 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,686.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,687.2 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,876.5 | 0.0380 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,730.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,823,491.0 | 2.6927 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,793,313.5 | 2.6639 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 633.6 | 633.3 | 633.8 | 0.2 | 0.246x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 781.4 | 780.9 | 792.2 | 4.4 | 0.303x | 1.233x |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,349.0 | 2,343.3 | 2,356.5 | 4.6 | 0.912x | 3.707x |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 2,353.4 | 2,346.9 | 2,360.2 | 5.3 | 0.914x | 3.714x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,573.1 | 2,568.1 | 2,585.2 | 5.7 | 0.999x | 4.061x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,575.9 | 2,572.7 | 2,597.2 | 9.0 | 1.000x | 4.065x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,361.4 | 1,360.0 | 1,361.5 | 0.6 | 0.182x | 1.000x | 77 | 17.7 | 100% |
| 2 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,365.8 | 1,364.0 | 1,384.5 | 7.7 | 0.183x | 1.003x | 77 | 17.7 | 100% |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,508.1 | 2,484.5 | 2,736.2 | 113.9 | 0.336x | 1.842x | 77 | 32.6 | 100% |
| 4 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,530.6 | 2,529.2 | 2,579.4 | 19.4 | 0.339x | 1.859x | 77 | 32.9 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,406.3 | 3,362.7 | 3,478.7 | 41.8 | 0.457x | 2.502x | 77 | 44.2 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,460.7 | 7,271.5 | 7,603.6 | 106.6 | 1.000x | 5.480x | 77 | 96.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 13,586,691.1 | 2.5915 | 13,528,810.2 | 13,661,164.5 | 48,476.7 | 0.111x | 1.000x | 5 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 13,609,551.7 | 2.5958 | 13,584,614.0 | 13,613,088.3 | 10,455.9 | 0.111x | 1.002x | 5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,200,581.7 | 3.4715 | 18,143,115.8 | 18,245,427.0 | 38,971.3 | 0.148x | 1.340x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,619,648.3 | 23.3878 | 122,492,083.3 | 128,349,586.4 | 2,241,432.7 | 1.000x | 9.025x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,579,415.8 | 3.4136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,584,658.7 | 3.4186 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,684,690.7 | 3.5140 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,694,695.4 | 27.3654 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,888,829.9 | 1.8013 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,895,118.8 | 1.8073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,563,984.5 | 2.4452 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,985.3 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,876,578.1 | 1.7896 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,878,612.2 | 1.7916 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,819,271.7 | 2.6887 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,957.3 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,133,275.5 | 2.9881 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,138,982.6 | 2.9936 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,411.6 | 5.6900 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,875,420.9 | 89.5266 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,113,753.6 | 2.9695 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,106,092.4 | 2.9622 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,157,856.9 | 3.0116 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,076.5 | 0.0172 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,129.7 | 62,020.5 | 62,288.3 | 94.6 | 0.116x | 1.000x |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,804.9 | 62,698.9 | 62,947.0 | 91.8 | 0.117x | 1.011x |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 133,784.0 | 133,732.1 | 133,983.3 | 94.1 | 0.250x | 2.153x |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 133,799.6 | 133,717.0 | 133,825.2 | 36.9 | 0.250x | 2.154x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,774.2 | 533,692.2 | 536,160.3 | 931.4 | 0.999x | 8.607x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535,288.3 | 533,762.5 | 536,917.9 | 1,116.9 | 1.000x | 8.616x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,527.1 | 3,524.7 | 3,550.2 | 9.7 | 0.054x | 1.000x | 77 | 45.8 | 17.7 | 100% |
| 2 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,533.0 | 3,523.9 | 3,533.4 | 4.1 | 0.054x | 1.002x | 77 | 45.9 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,110.7 | 6,105.2 | 6,285.2 | 73.4 | 0.093x | 1.732x | 77 | 79.4 | 44.2 | 100% |
| 4 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 12,517.8 | 12,422.0 | 12,657.3 | 82.6 | 0.190x | 3.549x | 77 | 162.6 | 32.6 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 12,632.4 | 12,600.2 | 12,687.0 | 33.7 | 0.192x | 3.582x | 77 | 164.1 | 32.9 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,802.9 | 65,577.6 | 68,398.8 | 1,065.5 | 1.000x | 18.656x | 77 | 854.6 | 96.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_35e1ab1_auto-caps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_35e1ab1_vm-caps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `floor` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `orig` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_35e1ab1_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 141,464,363.0 | 130,784,800.0 | 181,033,514.0 | 18,383,356.4 | 5 | 38,328 | 0.130 | compiled=5 | 8,618,961.0 | 132,755,341.0 | 109,411.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 158,500,382.0 | 149,923,522.0 | 177,325,533.0 | 10,534,750.7 | 5 | 38,416 | 0.066 | compiled=5 | 11,273,977.0 | 145,619,447.0 | 97,171.0 |
| `factored` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 140,463,715.0 | 136,195,132.0 | 148,699,214.0 | 4,110,299.8 | 5 | 38,328 | 0.029 | compiled=5 | 8,726,391.0 | 130,714,848.0 | 98,790.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 155,116,653.0 | 150,699,867.0 | 173,544,091.0 | 8,260,812.8 | 5 | 38,416 | 0.053 | compiled=5 | 10,988,664.0 | 141,275,411.0 | 179,141.0 |
| `factored` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 547,577,831.0 | 546,223,373.0 | 553,227,145.0 | 2,667,457.8 | 5 | 30,288 | 0.005 | compiled=5 | 2,069,092.0 | 545,419,478.0 | 186,391.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 551,471,633.0 | 547,201,459.0 | 555,134,585.0 | 2,807,182.1 | 5 | 30,288 | 0.005 (max is trial 1) | compiled=5 | 2,077,272.0 | 549,215,960.0 | 102,721.0 |
| `factored` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 550,174,265.0 | 542,143,397.0 | 558,601,396.0 | 5,346,769.4 | 5 | 30,288 | 0.010 | compiled=5 | 2,064,322.0 | 546,000,761.0 | 108,470.0 |
| `factored` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 552,115,297.0 | 548,172,073.0 | 552,589,780.0 | 1,880,987.6 | 5 | 30,288 | 0.003 (max is trial 1) | compiled=5 | 2,070,633.0 | 549,936,604.0 | 188,061.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 128,124,003.0 | 121,815,237.0 | 132,250,058.0 | 3,741,734.5 | 5 | 17,816 | 0.029 | compiled=5 | 1,563,309.0 | 126,608,855.0 | 112,481.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 136,601,994.0 | 125,250,527.0 | 138,196,622.0 | 6,006,842.3 | 5 | 17,904 | 0.044 (max is trial 1) | compiled=5 | 1,463,518.0 | 134,997,154.0 | 200,402.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 125,053,645.0 | 118,093,685.0 | 130,520,689.0 | 4,812,299.8 | 5 | 17,816 | 0.038 (max is trial 1) | compiled=5 | 1,404,458.0 | 123,415,805.0 | 99,061.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 135,198,375.0 | 124,770,805.0 | 136,922,336.0 | 4,667,899.5 | 5 | 17,904 | 0.035 | compiled=5 | 1,432,719.0 | 132,068,647.0 | 199,521.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 143,839,405.0 | 133,489,685.0 | 145,996,357.0 | 4,499,436.2 | 5 | 17,600 | 0.031 | compiled=5 | 1,470,958.0 | 142,085,106.0 | 104,780.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 131,485,234.0 | 130,493,468.0 | 152,939,310.0 | 9,269,487.4 | 5 | 17,600 | 0.070 | compiled=5 | 1,303,697.0 | 130,010,745.0 | 190,152.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 143,130,173.0 | 127,595,569.0 | 148,446,484.0 | 7,271,673.7 | 5 | 17,600 | 0.051 (max is trial 1) | compiled=5 | 1,367,788.0 | 141,680,644.0 | 107,271.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 136,645,873.0 | 127,325,307.0 | 145,517,016.0 | 6,966,108.5 | 5 | 17,600 | 0.051 | compiled=5 | 1,317,248.0 | 135,247,565.0 | 93,341.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 143,041,582.0 | 133,638,077.0 | 152,605,977.0 | 7,423,117.4 | 5 | 38,288 | 0.052 | compiled=5 | 8,399,070.0 | 133,049,073.0 | 97,811.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 161,003,156.0 | 144,668,771.0 | 174,001,693.0 | 9,821,090.4 | 5 | 38,376 | 0.061 | compiled=5 | 18,044,156.0 | 141,891,755.0 | 186,281.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,731,375.0 | 133,116,513.0 | 154,306,767.0 | 7,366,531.2 | 5 | 38,288 | 0.050 | compiled=5 | 8,303,388.0 | 134,495,101.0 | 190,511.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,766,935.0 | 141,953,955.0 | 157,360,185.0 | 5,601,770.9 | 5 | 38,376 | 0.038 (max is trial 1) | compiled=5 | 10,395,781.0 | 138,189,823.0 | 191,472.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 425,700,355.0 | 418,138,020.0 | 433,200,719.0 | 5,739,473.7 | 5 | 26,112 | 0.013 | compiled=5 | 3,573,812.0 | 423,604,592.0 | 98,321.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 418,219,710.0 | 416,284,479.0 | 424,829,349.0 | 3,247,138.2 | 5 | 26,112 | 0.008 | compiled=5 | 1,887,041.0 | 416,182,378.0 | 101,761.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 426,965,172.0 | 417,563,868.0 | 436,633,782.0 | 6,421,511.5 | 5 | 26,112 | 0.015 | compiled=5 | 3,456,131.0 | 422,794,938.0 | 94,571.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 416,505,570.0 | 410,439,183.0 | 436,855,013.0 | 9,723,201.5 | 5 | 26,112 | 0.023 (max is trial 1) | compiled=5 | 3,768,522.0 | 414,571,809.0 | 91,591.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 77,221.0 | 63,801.0 | 158,901.0 | 34,563.5 | 5 | 951 | 0.448 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,280.0 | 4,990.0 | 51,650.0 | 18,235.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 66,930.0 | 54,590.0 | 163,171.0 | 40,903.4 | 5 | 1,609 | 0.611 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,840.0 | 12,990.0 | 48,891.0 | 13,770.9 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 320.0 | 14,730.0 | 5,748.1 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,870.0 | 12,390.0 | 44,650.0 | 12,443.2 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

