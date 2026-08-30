# pcrec-bench report

reporter: v8 (2026-08-30)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-08-29T00:00:00Z, until=2026-08-30T15:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 10
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z.jsonl)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-caps-simdna/email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-nocaps-simdna/email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-in-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z.jsonl)
    - `email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-caps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z.jsonl)
    - `email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-nocaps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z.jsonl)
    - `email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z.jsonl)
    - `email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-in-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z.jsonl)
- superseded: 4 record(s) (OD-B15; --all-records lists them)
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

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 13,595,834.2 | 2.5932 | 13,569,312.4 | 13,731,462.8 | 60,163.9 | 0.027x | 1.000x | unchanged (within spread) | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 13,609,367.8 | 2.5958 | 13,584,177.0 | 13,626,756.8 | 16,249.9 | 0.027x | 1.001x | - | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 13,704,256.6 | 2.6139 | 13,685,839.0 | 13,749,076.2 | 21,250.8 | 0.027x | 1.008x | unchanged (within spread) | 5 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 13,720,312.1 | 2.6169 | 13,702,290.7 | 13,724,828.9 | 9,334.1 | 0.027x | 1.009x | - | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 499,942,662.6 | 95.3565 | 498,365,862.4 | 527,409,710.5 | 11,071,765.4 | 1.000x | 36.772x | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,581,485.2 | 3.4156 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,585,869.9 | 3.4198 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,588,937.2 | 3.4227 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,592,664.3 | 3.4262 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,692,993.8 | 49.2983 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,891,541.7 | 1.8039 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,891,036.2 | 1.8034 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,877,627.3 | 1.7906 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,260.8 | 1.7903 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,417.0 | 0.0185 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,878,044.0 | 1.7910 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,877,691.4 | 1.7907 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,184.2 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,576.4 | 1.7906 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,842.9 | 0.0180 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,137,206.7 | 2.9919 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,141,066.7 | 2.9956 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,198,130.0 | 3.0500 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,208,442.6 | 3.0598 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 448,191,962.3 | 427.4292 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,099,418.9 | 2.9558 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,101,481.2 | 2.9578 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,166,592.9 | 3.0199 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,163,082.9 | 3.0166 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,569.1 | 0.0187 |

- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,581,485.2 ns, 1,048,576 B
- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,588,937.2 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -10,312.6 ns (now 3,198,130.0 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,286.4 | 73,249.2 | 73,401.2 | 51.9 | 0.040x | 1.000x | - | 85 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,301.0 | 73,260.7 | 73,340.4 | 25.4 | 0.040x | 1.000x | unchanged (within spread) | 85 | 100% |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,371.5 | 73,350.7 | 73,435.9 | 29.6 | 0.040x | 1.001x | - | 85 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,383.3 | 73,375.9 | 73,385.8 | 3.3 | 0.040x | 1.001x | unchanged (within spread) | 85 | 100% |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 462,186.8 | 461,060.9 | 465,355.0 | 1,465.4 | 0.252x | 6.307x | unchanged (within spread) | 85 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 464,104.4 | 460,234.7 | 464,676.6 | 1,802.9 | 0.253x | 6.333x | - | 85 | 100% |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,827,818.2 | 1,823,644.9 | 1,854,085.7 | 13,115.1 | 0.998x | 24.941x | - | 85 | 100% |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,831,243.6 | 1,823,541.1 | 1,855,218.0 | 10,904.9 | 1.000x | 24.987x | - | 85 | 100% |

- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-057`, 19,097.9 ns, 10,252 B; largest Δ: `s-063`, -16.7 ns (now 4,794.5 ns), 5,135 B
- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,106.5 ns, 10,252 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-060`, 194,217.0 ns, 10,240 B; largest Δ: `s-063`, -1,165.2 ns (now 99,792.2 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,527.2 | 3,525.6 | 3,536.6 | 4.0 | 0.026x | 1.000x | unchanged (within spread) | 77 | 45.8 | 17.3 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,534.4 | 3,528.3 | 3,543.8 | 5.5 | 0.026x | 1.002x | - | 77 | 45.9 | 17.7 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,667.3 | 3,661.1 | 3,671.7 | 3.6 | 0.027x | 1.040x | unchanged (within spread) | 77 | 47.6 | 17.2 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,682.0 | 3,666.7 | 3,697.8 | 10.2 | 0.027x | 1.044x | - | 77 | 47.8 | 17.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,276.8 | 15,232.8 | 15,352.6 | 44.0 | 0.111x | 4.331x | - | 77 | 198.4 | 48.5 | 100% |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 53,715.6 | 53,553.6 | 54,209.1 | 222.1 | 0.389x | 15.229x | - | 77 | 697.6 | 31.7 | 100% |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 53,872.8 | 53,373.3 | 54,711.3 | 450.2 | 0.391x | 15.274x | - | 77 | 699.6 | 32.0 | 100% |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 53,906.8 | 53,710.9 | 54,238.1 | 182.2 | 0.391x | 15.283x | unchanged (within spread) | 77 | 700.1 | 31.4 | 100% |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 54,069.3 | 53,491.4 | 54,216.1 | 257.6 | 0.392x | 15.329x | unchanged (within spread) | 77 | 702.2 | 31.7 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,939.8 | 137,769.6 | 138,305.3 | 207.8 | 1.000x | 39.108x | - | 77 | 1,791.4 | 96.9 | 100% |

- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-004`, 120.7 ns, 33 B; largest Δ: `s-042`, -2.0 ns (now 12.0 ns), 5 B
- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `s-004`, 123.8 ns, 33 B; largest Δ: `s-023`, -1.0 ns (now 69.0 ns), 18 B
- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `s-029`, 3,229.2 ns, 28 B; largest Δ: `s-038`, +72.1 ns (now 2,866.9 ns), 17 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-029`, 3,232.3 ns, 28 B; largest Δ: `s-041`, +90.3 ns (now 1,054.4 ns), 12 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 712,225.7 | 0.1358 | 711,585.6 | 712,766.2 | 433.2 | 0.193x | 1.000x | spread | - |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 712,540.3 | 0.1359 | 711,293.3 | 714,401.3 | 1,071.1 | 0.193x | 1.000x | spread | - |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 713,176.7 | 0.1360 | 711,858.4 | 719,884.4 | 2,872.0 | 0.193x | 1.001x | spread | unchanged (within spread) |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 713,484.5 | 0.1361 | 711,877.5 | 714,765.8 | 1,046.9 | 0.194x | 1.002x | spread | unchanged (within spread) |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,015,740.1 | 0.3845 | 1,880,816.0 | 2,092,105.9 | 79,225.2 | 0.547x | 2.830x | **dominated**: `t-a-valid-addrs` is 90.6% of this set | - |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,686,660.4 | 0.7032 | 3,674,751.8 | 3,726,701.6 | 20,583.2 | 1.000x | 5.176x | **dominated**: `t-a-valid-addrs` is 96.7% of this set | - |
| 7 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16,289,983.3 | 3.1071 | 16,020,151.8 | 16,947,474.1 | 313,043.2 | 4.419x | 22.872x | spread | - |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16,325,112.9 | 3.1138 | 15,821,062.7 | 16,573,878.5 | 308,141.1 | 4.428x | 22.921x | spread | unchanged (within spread) |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 16,371,986.6 | 3.1227 | 16,299,110.1 | 16,640,133.5 | 120,554.5 | 4.441x | 22.987x | spread | unchanged (within spread) |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16,919,060.9 | 3.2271 | 16,526,827.9 | 17,367,674.8 | 285,219.8 | 4.589x | 23.755x | spread | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 628,374.4 | 0.5993 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 628,359.3 | 0.5993 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 628,684.2 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 628,731.1 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,825,442.7 | 1.7409 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,563,281.1 | 3.3982 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 4,021,540.8 | 3.8352 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,923,994.5 | 3.7422 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 4,012,120.3 | 3.8263 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,943,119.2 | 3.7605 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,692.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,675.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,669.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,732.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,399.9 | 0.0376 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,809.6 | 0.0170 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 2,857,535.9 | 2.7252 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,076,750.8 | 2.9342 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,047,388.0 | 2.9062 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,409,032.7 | 3.2511 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,662.8 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,679.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,697.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,807.9 | 0.0380 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,798.9 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 2,799,047.8 | 2.6694 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,799,563.2 | 2.6699 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 2,791,699.8 | 2.6624 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 2,811,404.5 | 2.6812 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 30,857.2 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 30,868.6 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 30,981.7 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 30,939.0 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,985.7 | 0.0667 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,122.5 | 0.0669 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 3,378,161.3 | 3.2217 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,337,656.4 | 3.1830 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,368,779.2 | 3.2127 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,359,601.7 | 3.2040 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,711.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,700.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,695.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 40,399.3 | 0.0385 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,756.0 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 3,210,584.2 | 3.0619 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,941,908.1 | 2.8056 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,407,572.1 | 3.2497 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,411,499.4 | 3.2535 |

- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 628,684.2 ns, 1,048,576 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 628,731.1 ns, 1,048,576 B
- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `t-a-valid-addrs`, 3,923,994.5 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -469,591.3 ns (now 2,941,908.1 ns), 1,048,576 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `t-a-valid-addrs`, 4,012,120.3 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, +196,988.0 ns (now 3,407,572.1 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 612.3 | 611.1 | 613.7 | 0.9 | 0.237x | 1.000x | - |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 685.4 | 685.0 | 686.2 | 0.4 | 0.266x | 1.119x | slower ×1.12 |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 782.6 | 781.7 | 786.7 | 1.8 | 0.303x | 1.278x | unchanged (within spread) |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 783.3 | 782.0 | 785.0 | 1.2 | 0.304x | 1.279x | - |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 831.4 | 827.5 | 835.1 | 3.0 | 0.322x | 1.358x | faster ×1.04 |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 834.1 | 827.3 | 839.7 | 4.1 | 0.323x | 1.362x | faster ×1.04 |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 865.5 | 861.6 | 872.7 | 3.8 | 0.335x | 1.414x | - |
| 8 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 869.2 | 860.7 | 879.7 | 7.0 | 0.337x | 1.420x | - |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,579.4 | 2,569.9 | 3,062.9 | 194.7 | 1.000x | 4.213x | - |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,580.2 | 2,574.8 | 2,606.9 | 11.5 | 1.000x | 4.214x | - |

- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `s-082`, 11.5 ns, 1 B; largest Δ: `s-078`, +0.9 ns (now 8.0 ns), 16 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-082`, 10.9 ns, 1 B; largest Δ: `s-012`, -0.1 ns (now 9.2 ns), 18 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-082`, 12.6 ns, 1 B; largest Δ: `s-016`, -0.5 ns (now 9.6 ns), 17 B
- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `s-082`, 12.5 ns, 1 B; largest Δ: `s-041`, -0.7 ns (now 10.0 ns), 12 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,327.8 | 1,326.3 | 1,330.6 | 1.6 | 0.178x | 1.000x | faster ×1.03 | 77 | 17.2 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,329.7 | 1,328.5 | 1,346.0 | 6.7 | 0.178x | 1.001x | faster ×1.02 | 77 | 17.3 | 100% |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,362.2 | 1,361.1 | 1,374.4 | 5.0 | 0.183x | 1.026x | - | 77 | 17.7 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,366.4 | 1,360.5 | 1,382.1 | 7.8 | 0.183x | 1.029x | - | 77 | 17.7 | 100% |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,418.7 | 2,413.7 | 2,422.0 | 2.7 | 0.324x | 1.822x | faster ×1.01 | 77 | 31.4 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,438.3 | 2,435.6 | 2,451.1 | 5.7 | 0.327x | 1.836x | faster ×1.01 | 77 | 31.7 | 100% |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,440.6 | 2,431.1 | 2,447.9 | 7.2 | 0.327x | 1.838x | - | 77 | 31.7 | 100% |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,466.5 | 2,459.9 | 2,487.0 | 10.4 | 0.331x | 1.858x | - | 77 | 32.0 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,733.5 | 3,398.3 | 4,226.3 | 302.0 | 0.500x | 2.812x | - | 77 | 48.5 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,462.0 | 7,347.7 | 7,607.0 | 93.6 | 1.000x | 5.620x | - | 77 | 96.9 | 100% |

- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `s-004`, 18.3 ns, 33 B; largest Δ: `s-081`, -1.6 ns (now 5.0 ns), 0 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-004`, 18.3 ns, 33 B; largest Δ: `s-081`, -1.7 ns (now 5.1 ns), 0 B
- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `s-083`, 137.4 ns, 43 B; largest Δ: `s-040`, -2.3 ns (now 59.9 ns), 15 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-083`, 137.8 ns, 43 B; largest Δ: `s-040`, -4.3 ns (now 60.4 ns), 15 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 13,586,898.8 | 2.5915 | 13,567,348.6 | 13,609,391.2 | 15,307.1 | 0.111x | 1.000x | - | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 13,591,290.1 | 2.5923 | 13,571,707.0 | 13,689,336.5 | 45,361.0 | 0.111x | 1.000x | - | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 13,607,713.5 | 2.5955 | 13,575,535.2 | 13,632,111.1 | 21,217.8 | 0.111x | 1.002x | unchanged (within spread) | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 13,625,779.9 | 2.5989 | 13,583,858.4 | 13,632,604.3 | 20,133.9 | 0.111x | 1.003x | unchanged (within spread) | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,232,940.2 | 3.4777 | 18,157,667.8 | 18,459,450.8 | 117,430.0 | 0.149x | 1.342x | - | 5 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,773,449.3 | 23.4172 | 122,444,857.7 | 123,619,068.6 | 427,456.4 | 1.000x | 9.036x | - | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,583,346.1 | 3.4173 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,582,024.1 | 3.4161 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,583,848.6 | 3.4178 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,587,388.5 | 3.4212 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,696,994.6 | 3.5257 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,821,951.8 | 27.4868 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,890,919.6 | 1.8033 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,892,116.2 | 1.8045 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,887,163.0 | 1.7997 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,886,284.8 | 1.7989 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,546,837.8 | 2.4289 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,092.5 | 0.0173 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,410.1 | 1.7904 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,878,493.8 | 1.7915 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,250.4 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,875,774.8 | 1.7889 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,820,671.8 | 2.6900 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,005.5 | 0.0172 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,145,599.7 | 2.9999 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,140,389.6 | 2.9949 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,135,589.7 | 2.9903 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,148,674.1 | 3.0028 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,974,673.2 | 5.6979 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,897,422.0 | 89.5476 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,094,151.3 | 2.9508 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,091,404.0 | 2.9482 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,095,070.0 | 2.9517 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,097,595.6 | 2.9541 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,166,813.3 | 3.0201 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,121.3 | 0.0173 |

- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,583,848.6 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -10,010.0 ns (now 3,135,589.7 ns), 1,048,576 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,587,388.5 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +8,284.5 ns (now 3,148,674.1 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,301.2 | 62,260.8 | 63,740.2 | 578.8 | 0.117x | 1.000x | unchanged (within spread) |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,713.6 | 62,618.4 | 62,834.9 | 72.6 | 0.117x | 1.007x | - |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,982.0 | 62,964.9 | 63,086.2 | 44.3 | 0.118x | 1.011x | unchanged (within spread) |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63,023.4 | 62,788.1 | 63,372.5 | 188.3 | 0.118x | 1.012x | - |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,249.7 | 73,230.2 | 73,332.7 | 40.2 | 0.137x | 1.176x | unchanged (within spread) |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,272.4 | 73,248.6 | 73,457.8 | 78.3 | 0.137x | 1.176x | unchanged (within spread) |
| 7 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,306.7 | 73,279.6 | 73,348.2 | 22.3 | 0.137x | 1.177x | - |
| 8 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,309.9 | 73,302.2 | 73,529.6 | 101.5 | 0.137x | 1.177x | - |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 533,938.1 | 533,459.3 | 534,573.8 | 431.6 | 1.000x | 8.570x | - |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,007.8 | 533,632.1 | 535,269.5 | 601.9 | 1.000x | 8.571x | - |

- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-059`, 13,729.4 ns, 5,134 B; largest Δ: `s-058`, -105.1 ns (now 5,917.4 ns), 4,011 B
- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `s-059`, 13,728.3 ns, 5,134 B; largest Δ: `s-064`, +58.6 ns (now 10,660.1 ns), 4,110 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-057`, 19,092.5 ns, 10,252 B; largest Δ: `s-060`, -34.2 ns (now 19,073.6 ns), 10,240 B
- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,105.8 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,523.0 | 3,519.3 | 4,256.5 | 293.9 | 0.054x | 1.000x | unchanged (within spread) | 77 | 45.8 | 17.2 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,526.4 | 3,524.9 | 3,553.6 | 11.2 | 0.054x | 1.001x | unchanged (within spread) | 77 | 45.8 | 17.3 | 100% |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,531.7 | 3,527.9 | 3,555.3 | 11.5 | 0.054x | 1.002x | - | 77 | 45.9 | 17.7 | 100% |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,534.8 | 3,528.8 | 3,546.3 | 6.6 | 0.054x | 1.003x | - | 77 | 45.9 | 17.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,144.2 | 6,121.5 | 6,233.4 | 42.1 | 0.093x | 1.744x | - | 77 | 79.8 | 48.5 | 100% |
| 6 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 12,522.3 | 12,458.7 | 12,533.6 | 27.3 | 0.190x | 3.554x | faster ×1.02 | 77 | 162.6 | 31.4 | 100% |
| 7 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 12,819.6 | 12,759.2 | 12,876.4 | 42.4 | 0.195x | 3.639x | - | 77 | 166.5 | 31.7 | 100% |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 12,826.9 | 12,818.1 | 12,870.4 | 19.0 | 0.195x | 3.641x | faster ×1.02 | 77 | 166.6 | 31.7 | 100% |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 13,146.2 | 13,106.0 | 13,170.9 | 23.2 | 0.200x | 3.732x | - | 77 | 170.7 | 32.0 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,845.8 | 65,550.6 | 67,991.3 | 905.8 | 1.000x | 18.690x | - | 77 | 855.1 | 96.9 | 100% |

- Δ detail: `pcrec_96e44c2_auto-caps-simdna` vs previous `pcrec_36d5963_auto-caps-simdna`: worst now: `s-004`, 120.4 ns, 33 B; largest Δ: `s-081`, -1.4 ns (now 4.5 ns), 0 B
- Δ detail: `pcrec_96e44c2_auto-nocaps-simdna` vs previous `pcrec_36d5963_auto-nocaps-simdna`: worst now: `s-004`, 120.4 ns, 33 B; largest Δ: `s-082`, -1.4 ns (now 5.1 ns), 1 B
- Δ detail: `pcrec_96e44c2_vm-caps-simdna` vs previous `pcrec_36d5963_vm-caps-simdna`: worst now: `s-035`, 693.7 ns, 16 B; largest Δ: `s-075`, -19.0 ns (now 68.5 ns), 16 B
- Δ detail: `pcrec_96e44c2_vm-in-caps-simdna` vs previous `pcrec_36d5963_vm-in-caps-simdna`: worst now: `s-035`, 702.9 ns, 16 B; largest Δ: `s-004`, -25.2 ns (now 67.8 ns), 33 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_36d5963_auto-caps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_36d5963_vm-caps-simdna` / `factored` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `floor` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `orig` / `plain`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_36d5963_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_96e44c2_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_96e44c2_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced) -- the three tokens that share one `dfa overflowed` RX_ENGINE_WHY and differ in what survived -- OR a `lang=count-collapsed (size cap retry, ...)`: the size-cap rescue stamps sel=selected (measured at pcrec 96e44c2), so it is bucketed on its why prefix and marked `size-cap rescue` until pcrec's [LIM-1] gives it a token (inbox I-19 (3)).
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 163,173,581.0 | 148,043,728.0 | 165,355,524.0 | 6,230,940.4 | 5 | 43,000 | - | - | 0.038 | compiled=5 | 9,712,969.0 | 151,485,660.0 | 186,221.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 172,018,683.0 | 169,330,388.0 | 187,531,128.0 | 6,850,899.9 | 5 | 47,240 | - | - | 0.040 (max is trial 1) | compiled=5 | 11,935,272.0 | 160,085,781.0 | 190,281.0 |
| `factored` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 158,379,641.0 | 144,622,938.0 | 160,943,538.0 | 6,230,002.9 | 5 | 43,000 | - | - | 0.039 (max is trial 1) | compiled=5 | 9,574,438.0 | 140,183,871.0 | 190,981.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,254,961.0 | 156,661,801.0 | 182,598,618.0 | 9,464,812.7 | 5 | 47,240 | - | - | 0.058 (max is trial 1) | compiled=5 | 11,943,713.0 | 151,211,278.0 | 192,071.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 567,703,383.0 | 559,754,886.0 | 571,675,245.0 | 4,062,965.4 | 5 | 34,816 | - | - | 0.007 | compiled=5 | 2,253,513.0 | 564,927,396.0 | 125,381.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 559,242,744.0 | 556,895,190.0 | 570,217,336.0 | 4,711,477.0 | 5 | 34,816 | - | - | 0.008 | compiled=5 | 2,213,983.0 | 556,877,430.0 | 212,661.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 555,700,975.0 | 548,732,151.0 | 561,291,690.0 | 5,165,541.3 | 5 | 34,816 | - | - | 0.009 | compiled=5 | 2,286,274.0 | 553,427,801.0 | 190,972.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 551,792,261.0 | 547,407,994.0 | 564,315,969.0 | 6,285,963.3 | 5 | 34,816 | - | - | 0.011 | compiled=5 | 2,263,684.0 | 548,875,712.0 | 118,861.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 161,367,376.0 | 160,364,191.0 | 168,045,206.0 | 2,768,245.7 | 5 | 43,224 | 82,080 | 13,386 | 0.017 | compiled=5 | 9,593,116.0 | 150,683,764.0 | 199,961.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 173,642,569.0 | 162,000,350.0 | 195,343,764.0 | 11,832,867.7 | 5 | 47,464 | 94,291 | 15,302 | 0.068 (max is trial 1) | compiled=5 | 17,795,364.0 | 160,135,889.0 | 196,911.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 156,332,757.0 | 146,742,271.0 | 169,572,655.0 | 8,313,785.5 | 5 | 43,224 | 81,897 | 13,199 | 0.053 | compiled=5 | 9,544,566.0 | 146,686,991.0 | 187,602.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 169,353,324.0 | 158,336,598.0 | 175,847,071.0 | 6,277,917.7 | 5 | 47,464 | 94,108 | 15,115 | 0.037 | compiled=5 | 11,953,990.0 | 157,465,023.0 | 179,471.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 560,952,030.0 | 552,401,499.0 | 574,504,699.0 | 7,800,620.7 | 5 | 39,128 | 58,254 | 56,700 | 0.014 | compiled=5 | 2,163,513.0 | 558,645,066.0 | 198,721.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 561,262,931.0 | 553,920,967.0 | 566,432,401.0 | 4,509,880.6 | 5 | 39,128 | 58,370 | 56,816 | 0.008 | compiled=5 | 2,579,045.0 | 557,399,298.0 | 90,240.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 549,464,481.0 | 548,090,774.0 | 552,673,581.0 | 1,655,066.8 | 5 | 39,128 | 58,254 | 56,700 | 0.003 (max is trial 1) | compiled=5 | 2,182,383.0 | 545,859,350.0 | 188,261.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 568,066,400.0 | 554,524,271.0 | 569,803,801.0 | 5,749,619.0 | 5 | 39,128 | 58,370 | 56,816 | 0.010 | compiled=5 | 2,302,993.0 | 565,593,376.0 | 100,111.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 137,975,417.0 | 130,154,820.0 | 142,913,866.0 | 4,140,189.2 | 5 | 22,488 | - | - | 0.030 | compiled=5 | 3,055,408.0 | 135,445,562.0 | 190,461.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 144,611,468.0 | 133,599,301.0 | 149,537,718.0 | 6,141,196.3 | 5 | 22,632 | - | - | 0.042 | compiled=5 | 1,661,280.0 | 142,664,806.0 | 196,431.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 137,161,193.0 | 131,844,181.0 | 140,083,190.0 | 2,832,113.2 | 5 | 22,488 | - | - | 0.021 (max is trial 1) | compiled=5 | 1,624,910.0 | 133,667,721.0 | 187,942.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 146,188,127.0 | 137,551,574.0 | 148,622,902.0 | 3,782,109.1 | 5 | 22,632 | - | - | 0.026 | compiled=5 | 1,755,770.0 | 142,880,468.0 | 105,240.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 149,341,986.0 | 137,028,735.0 | 150,343,371.0 | 4,944,844.8 | 5 | 22,120 | - | - | 0.033 | compiled=5 | 1,696,930.0 | 147,530,796.0 | 176,811.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 146,819,080.0 | 139,205,948.0 | 153,194,038.0 | 4,814,096.7 | 5 | 22,120 | - | - | 0.033 | compiled=5 | 1,431,778.0 | 145,203,761.0 | 187,691.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 143,224,196.0 | 133,623,356.0 | 149,166,282.0 | 5,314,418.2 | 5 | 22,120 | - | - | 0.037 | compiled=5 | 1,870,712.0 | 141,694,146.0 | 108,651.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 139,422,771.0 | 137,041,307.0 | 155,827,535.0 | 7,167,340.5 | 5 | 22,120 | - | - | 0.051 | compiled=5 | 2,750,817.0 | 137,806,721.0 | 199,131.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 133,986,396.0 | 129,174,899.0 | 142,126,773.0 | 4,614,847.4 | 5 | 22,712 | 17,731 | 12,734 | 0.034 | compiled=5 | 1,734,020.0 | 132,040,485.0 | 188,771.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 147,942,328.0 | 144,005,944.0 | 154,591,887.0 | 3,790,768.5 | 5 | 22,856 | 20,074 | 14,751 | 0.026 | compiled=5 | 1,672,159.0 | 145,940,916.0 | 99,891.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 131,184,190.0 | 124,625,080.0 | 138,781,244.0 | 5,533,696.7 | 5 | 22,712 | 17,731 | 12,734 | 0.042 | compiled=5 | 1,680,810.0 | 129,391,839.0 | 117,511.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 149,578,517.0 | 143,713,063.0 | 151,059,906.0 | 2,757,231.6 | 5 | 22,856 | 20,074 | 14,751 | 0.018 | compiled=5 | 1,678,290.0 | 147,514,265.0 | 102,211.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 144,984,105.0 | 140,000,455.0 | 155,450,617.0 | 5,526,755.8 | 5 | 22,344 | 17,660 | 17,660 | 0.038 | compiled=5 | 1,620,700.0 | 143,173,954.0 | 186,041.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 149,400,661.0 | 140,726,940.0 | 152,597,870.0 | 4,214,821.7 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 1,528,869.0 | 147,835,302.0 | 106,611.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 143,038,783.0 | 142,028,867.0 | 152,074,138.0 | 3,847,908.1 | 5 | 22,344 | 17,660 | 17,660 | 0.027 | compiled=5 | 1,451,489.0 | 140,558,609.0 | 190,721.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 149,887,504.0 | 141,599,525.0 | 152,215,158.0 | 4,185,187.6 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 2,899,487.0 | 146,859,346.0 | 187,241.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 160,234,903.0 | 142,502,585.0 | 170,930,038.0 | 9,452,596.4 | 5 | 42,960 | - | - | 0.059 (max is trial 1) | compiled=5 | 9,209,996.0 | 144,087,044.0 | 215,871.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 166,290,610.0 | 163,930,325.0 | 182,586,678.0 | 6,746,131.3 | 5 | 47,200 | - | - | 0.041 | compiled=5 | 11,352,189.0 | 154,132,576.0 | 207,132.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 152,456,135.0 | 144,069,245.0 | 174,208,458.0 | 10,143,322.1 | 5 | 42,960 | - | - | 0.067 | compiled=5 | 9,225,456.0 | 143,266,640.0 | 102,641.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,517,013.0 | 155,667,265.0 | 165,485,665.0 | 4,206,358.8 | 5 | 47,200 | - | - | 0.026 | compiled=5 | 11,363,629.0 | 151,287,019.0 | 199,952.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 429,171,779.0 | 423,947,059.0 | 447,217,713.0 | 8,229,989.8 | 5 | 30,632 | - | - | 0.019 (max is trial 1) | compiled=5 | 1,931,061.0 | 427,170,727.0 | 194,501.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 435,901,317.0 | 424,067,939.0 | 452,243,691.0 | 11,235,002.5 | 5 | 30,632 | - | - | 0.026 | compiled=5 | 2,212,242.0 | 431,366,691.0 | 196,301.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 430,350,492.0 | 428,462,499.0 | 435,167,061.0 | 2,401,459.0 | 5 | 30,632 | - | - | 0.006 (max is trial 1) | compiled=5 | 2,006,842.0 | 428,298,358.0 | 184,621.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 429,422,065.0 | 424,291,654.0 | 437,092,543.0 | 4,553,396.7 | 5 | 30,632 | - | - | 0.011 | compiled=5 | 4,000,955.0 | 425,227,189.0 | 186,951.0 |
| `orig` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 155,909,854.0 | 148,124,119.0 | 161,865,359.0 | 4,560,674.0 | 5 | 43,184 | 81,673 | 13,146 | 0.029 (max is trial 1) | compiled=5 | 9,193,534.0 | 145,299,572.0 | 112,481.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 166,269,755.0 | 157,823,085.0 | 187,526,990.0 | 11,174,706.0 | 5 | 47,424 | 93,884 | 15,062 | 0.067 | compiled=5 | 11,325,736.0 | 154,860,548.0 | 190,591.0 |
| `orig` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 158,494,010.0 | 153,283,090.0 | 159,820,747.0 | 2,292,895.1 | 5 | 43,184 | 81,673 | 13,146 | 0.014 | compiled=5 | 15,270,279.0 | 143,030,149.0 | 193,582.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 170,588,431.0 | 165,958,083.0 | 174,447,733.0 | 3,451,250.8 | 5 | 47,424 | 93,884 | 15,062 | 0.020 | compiled=5 | 11,299,856.0 | 155,813,914.0 | 176,731.0 |
| `orig` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 432,252,700.0 | 428,192,665.0 | 440,587,819.0 | 4,944,494.4 | 5 | 30,856 | 47,083 | 45,696 | 0.011 (max is trial 1) | compiled=5 | 1,940,911.0 | 430,240,938.0 | 183,021.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 439,477,152.0 | 427,270,060.0 | 440,660,949.0 | 5,186,906.2 | 5 | 30,856 | 47,201 | 45,814 | 0.012 | compiled=5 | 3,999,074.0 | 435,747,821.0 | 201,951.0 |
| `orig` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 432,276,781.0 | 422,582,502.0 | 440,401,109.0 | 6,161,203.2 | 5 | 30,856 | 47,083 | 45,696 | 0.014 | compiled=5 | 1,970,322.0 | 430,082,787.0 | 108,371.0 |
| `orig` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 418,893,331.0 | 418,489,718.0 | 421,067,724.0 | 1,080,686.2 | 5 | 30,856 | 47,201 | 45,814 | 0.003 | compiled=5 | 2,167,223.0 | 416,497,917.0 | 186,551.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 69,970.0 | 63,740.0 | 158,851.0 | 35,898.1 | 5 | 951 | 0.513 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,320.0 | 4,940.0 | 55,180.0 | 19,635.4 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 61,501.0 | 54,730.0 | 185,332.0 | 49,645.3 | 5 | 1,609 | 0.807 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,880.0 | 12,990.0 | 43,700.0 | 11,712.6 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 370.0 | 310.0 | 15,581.0 | 6,081.7 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,400.0 | 12,240.0 | 56,820.0 | 17,389.8 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

