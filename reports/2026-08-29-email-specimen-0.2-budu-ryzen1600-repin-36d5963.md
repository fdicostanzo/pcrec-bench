# pcrec-bench report

reporter: v8 (2026-08-30)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-08-30T11:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 10
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260829T203945Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260829T203945Z.jsonl)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260829T190658Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260829T190658Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-caps-simdna__budu-ryzen1600__20260828T142809Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_auto-nocaps-simdna/email-specimen@0.2__pcrec_35e1ab1_auto-nocaps-simdna__budu-ryzen1600__20260828T143259Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-caps-simdna__budu-ryzen1600__20260828T143810Z.jsonl)
    - `email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z` (store/records/email-specimen@0.2/pcrec_35e1ab1_vm-in-caps-simdna/email-specimen@0.2__pcrec_35e1ab1_vm-in-caps-simdna__budu-ryzen1600__20260828T144426Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-caps-simdna/email-specimen@0.2__pcrec_36d5963_auto-caps-simdna__budu-ryzen1600__20260829T191837Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z` (store/records/email-specimen@0.2/pcrec_36d5963_auto-nocaps-simdna/email-specimen@0.2__pcrec_36d5963_auto-nocaps-simdna__budu-ryzen1600__20260829T192412Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-caps-simdna__budu-ryzen1600__20260829T204855Z.jsonl)
    - `email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z` (store/records/email-specimen@0.2/pcrec_36d5963_vm-in-caps-simdna/email-specimen@0.2__pcrec_36d5963_vm-in-caps-simdna__budu-ryzen1600__20260829T193713Z.jsonl)
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
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 13,593,900.0 | 2.5928 | 13,556,964.8 | 13,728,371.4 | 59,896.2 | 0.027x | 1.000x | - | 5 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 13,609,367.8 | 2.5958 | 13,584,177.0 | 13,626,756.8 | 16,249.9 | 0.027x | 1.001x | unchanged (within spread) | 5 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 13,684,627.4 | 2.6101 | 13,638,732.1 | 13,864,401.6 | 78,198.4 | 0.027x | 1.007x | - | 5 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 13,720,312.1 | 2.6169 | 13,702,290.7 | 13,724,828.9 | 9,334.1 | 0.027x | 1.009x | unchanged (within spread) | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 501,589,741.8 | 95.6707 | 498,587,872.4 | 536,142,175.1 | 14,113,850.4 | 1.000x | 36.898x | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,578,231.1 | 3.4125 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,585,869.9 | 3.4198 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,591,987.4 | 3.4256 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,592,664.3 | 3.4262 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,904,436.8 | 49.4999 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,890,786.8 | 1.8032 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,891,036.2 | 1.8034 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,877,191.1 | 1.7902 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,260.8 | 1.7903 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,840.6 | 0.0180 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,876,102.3 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,877,691.4 | 1.7907 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,875,979.8 | 1.7891 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,576.4 | 1.7906 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,719.6 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,143,556.6 | 2.9979 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,141,066.7 | 2.9956 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,194,847.5 | 3.0468 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,208,442.6 | 3.0598 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 450,017,052.5 | 429.1697 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,098,348.9 | 2.9548 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,101,481.2 | 2.9578 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,146,368.5 | 3.0006 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,163,082.9 | 3.0166 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,062.9 | 0.0182 |

- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,585,869.9 ns, 1,048,576 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,592,664.3 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, +16,714.4 ns (now 3,163,082.9 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,286.4 | 73,249.2 | 73,401.2 | 51.9 | 0.040x | 1.000x | faster ×1.83 | 85 | 100% |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,371.5 | 73,350.7 | 73,435.9 | 29.6 | 0.040x | 1.001x | faster ×1.77 | 85 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 130,228.4 | 130,199.9 | 130,355.6 | 55.7 | 0.071x | 1.777x | - | 85 | 100% |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 133,944.5 | 133,867.9 | 134,190.9 | 110.3 | 0.073x | 1.828x | - | 85 | 100% |
| 5 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 456,277.5 | 454,029.4 | 463,699.5 | 3,715.3 | 0.250x | 6.226x | - | 85 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 464,104.4 | 460,234.7 | 464,676.6 | 1,802.9 | 0.254x | 6.333x | slower ×1.02 | 85 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,827,130.5 | 1,822,010.4 | 1,867,078.8 | 17,513.4 | 1.000x | 24.931x | - | 85 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,854,580.4 | 1,827,848.8 | 1,869,229.8 | 13,830.8 | 1.015x | 25.306x | - | 85 | 100% |

- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now (also the largest Δ): `s-057`, 19,097.4 ns, 10,252 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,088.8 ns, 10,252 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `s-060`, 194,410.1 ns, 10,240 B; largest Δ: `s-063`, +5,558.3 ns (now 100,957.4 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,528.7 | 3,525.8 | 3,539.3 | 5.0 | 0.026x | 1.000x | - | 77 | 45.8 | 17.7 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,534.4 | 3,528.3 | 3,543.8 | 5.5 | 0.026x | 1.002x | unchanged (within spread) | 77 | 45.9 | 17.7 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,666.5 | 3,665.8 | 3,669.9 | 1.5 | 0.027x | 1.039x | - | 77 | 47.6 | 17.7 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,682.0 | 3,666.7 | 3,697.8 | 10.2 | 0.027x | 1.043x | unchanged (within spread) | 77 | 47.8 | 17.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,316.2 | 15,254.1 | 16,001.0 | 291.5 | 0.111x | 4.341x | - | 77 | 198.9 | 45.1 | 100% |
| 6 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 53,715.6 | 53,553.6 | 54,209.1 | 222.1 | 0.389x | 15.223x | unchanged (within spread) | 77 | 697.6 | 31.7 | 100% |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 53,852.7 | 53,636.1 | 54,444.3 | 320.9 | 0.390x | 15.261x | - | 77 | 699.4 | 32.6 | 100% |
| 8 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 53,872.8 | 53,373.3 | 54,711.3 | 450.2 | 0.391x | 15.267x | unchanged (within spread) | 77 | 699.6 | 32.0 | 100% |
| 9 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 54,151.3 | 53,905.1 | 54,258.7 | 119.1 | 0.393x | 15.346x | - | 77 | 703.3 | 32.9 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,942.8 | 137,557.4 | 138,150.5 | 231.2 | 1.000x | 39.092x | - | 77 | 1,791.5 | 98.6 | 100% |

- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `s-004`, 120.5 ns, 33 B; largest Δ: `s-042`, +1.4 ns (now 13.9 ns), 5 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now: `s-004`, 123.9 ns, 33 B; largest Δ: `s-022`, +1.0 ns (now 84.1 ns), 22 B
- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `s-029`, 3,290.1 ns, 28 B; largest Δ: `s-030`, +76.7 ns (now 905.8 ns), 14 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `s-029`, 3,209.7 ns, 28 B; largest Δ: `s-028`, -144.7 ns (now 933.1 ns), 14 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 711,403.3 | 0.1357 | 710,834.2 | 714,069.7 | 1,159.6 | 0.192x | 1.000x | spread | - |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 712,225.7 | 0.1358 | 711,585.6 | 712,766.2 | 433.2 | 0.192x | 1.001x | spread | unchanged (within spread) |
| 3 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 712,540.3 | 0.1359 | 711,293.3 | 714,401.3 | 1,071.1 | 0.192x | 1.002x | spread | unchanged (within spread) |
| 4 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 712,658.0 | 0.1359 | 711,305.9 | 713,849.5 | 824.2 | 0.192x | 1.002x | spread | - |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,890,737.3 | 0.3606 | 1,861,252.5 | 1,924,941.4 | 24,099.7 | 0.510x | 2.658x | **dominated**: `t-a-valid-addrs` is 90.0% of this set | - |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,705,152.2 | 0.7067 | 3,678,320.7 | 3,781,904.3 | 36,721.5 | 1.000x | 5.208x | **dominated**: `t-a-valid-addrs` is 96.7% of this set | - |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 15,694,249.9 | 2.9934 | 15,644,181.0 | 16,112,979.1 | 173,516.2 | 4.236x | 22.061x | spread | - |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 15,827,138.2 | 3.0188 | 15,789,874.1 | 15,846,666.6 | 18,853.1 | 4.272x | 22.248x | spread | - |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 16,289,983.3 | 3.1071 | 16,020,151.8 | 16,947,474.1 | 313,043.2 | 4.397x | 22.898x | spread | unchanged (within spread) |
| 10 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 16,919,060.9 | 3.2271 | 16,526,827.9 | 17,367,674.8 | 285,219.8 | 4.566x | 23.783x | spread | slower ×1.08 |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 627,186.7 | 0.5981 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 628,374.4 | 0.5993 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 628,359.3 | 0.5993 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 628,561.1 | 0.5994 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,702,577.5 | 1.6237 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,580,885.0 | 3.4150 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 3,908,618.9 | 3.7275 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 4,074,182.9 | 3.8854 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 4,021,540.8 | 3.8352 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,943,119.2 | 3.7605 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,705.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,692.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,675.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,720.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,329.9 | 0.0375 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,808.9 | 0.0170 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,793,280.9 | 2.6639 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,790,208.5 | 2.6610 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 2,857,535.9 | 2.7252 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,409,032.7 | 3.2511 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,705.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,662.8 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,679.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,715.6 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,953.9 | 0.0381 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,791.6 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,790,950.1 | 2.6617 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,790,569.1 | 2.6613 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 2,799,047.8 | 2.6694 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 2,811,404.5 | 2.6812 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 30,813.1 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 30,857.2 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 30,868.6 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 30,873.3 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,364.2 | 0.0662 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,450.4 | 0.0672 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 3,345,865.5 | 3.1909 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 3,371,357.6 | 3.2152 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 3,378,161.3 | 3.2217 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,359,601.7 | 3.2040 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 17,686.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 17,711.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 17,700.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 17,687.2 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,673.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,829.2 | 0.0170 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-caps-simdna` | 2,823,491.0 | 2.6927 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_vm-in-caps-simdna` | 2,793,313.5 | 2.6639 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_vm-in-caps-simdna` | 3,210,584.2 | 3.0619 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_vm-caps-simdna` | 3,411,499.4 | 3.2535 |

- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 628,374.4 ns, 1,048,576 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 628,359.3 ns, 1,048,576 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `t-a-valid-addrs`, 4,021,540.8 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, +417,270.7 ns (now 3,210,584.2 ns), 1,048,576 B
- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `t-a-valid-addrs`, 3,943,119.2 ns, 1,048,576 B; largest Δ: `t-b-no-at`, +615,751.9 ns (now 3,409,032.7 ns), 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 612.3 | 611.1 | 613.7 | 0.9 | 0.238x | 1.000x | faster ×1.03 |
| 2 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 633.6 | 633.3 | 633.8 | 0.2 | 0.246x | 1.035x | - |
| 3 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 781.4 | 780.9 | 792.2 | 4.4 | 0.303x | 1.276x | - |
| 4 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 783.3 | 782.0 | 785.0 | 1.2 | 0.304x | 1.279x | unchanged (within spread) |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 865.5 | 861.6 | 872.7 | 3.8 | 0.336x | 1.414x | faster ×2.72 |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 869.2 | 860.7 | 879.7 | 7.0 | 0.337x | 1.420x | faster ×2.70 |
| 7 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 2,349.0 | 2,343.3 | 2,356.5 | 4.6 | 0.911x | 3.837x | - |
| 8 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 2,353.4 | 2,346.9 | 2,360.2 | 5.3 | 0.913x | 3.844x | - |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,577.7 | 2,574.6 | 2,598.8 | 9.5 | 1.000x | 4.210x | - |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,584.5 | 2,577.7 | 2,737.7 | 62.2 | 1.003x | 4.221x | - |

- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `s-082`, 11.0 ns, 1 B; largest Δ: `s-041`, +0.9 ns (now 9.2 ns), 12 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `s-082`, 10.8 ns, 1 B; largest Δ: `s-017`, -0.1 ns (now 9.2 ns), 18 B
- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `s-082`, 12.4 ns, 1 B; largest Δ: `s-057`, -149.8 ns (now 10.2 ns), 10,252 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now: `s-082`, 12.5 ns, 1 B; largest Δ: `s-057`, -150.0 ns (now 10.1 ns), 10,252 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 1,361.4 | 1,360.0 | 1,361.5 | 0.6 | 0.179x | 1.000x | - | 77 | 17.7 | 100% |
| 2 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 1,362.2 | 1,361.1 | 1,374.4 | 5.0 | 0.179x | 1.001x | unchanged (within spread) | 77 | 17.7 | 100% |
| 3 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 1,365.8 | 1,364.0 | 1,384.5 | 7.7 | 0.180x | 1.003x | - | 77 | 17.7 | 100% |
| 4 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 1,366.4 | 1,360.5 | 1,382.1 | 7.8 | 0.180x | 1.004x | unchanged (within spread) | 77 | 17.7 | 100% |
| 5 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 2,440.6 | 2,431.1 | 2,447.9 | 7.2 | 0.322x | 1.793x | unchanged (within spread) | 77 | 31.7 | 100% |
| 6 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 2,466.5 | 2,459.9 | 2,487.0 | 10.4 | 0.325x | 1.812x | faster ×1.03 | 77 | 32.0 | 100% |
| 7 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 2,508.1 | 2,484.5 | 2,736.2 | 113.9 | 0.330x | 1.842x | - | 77 | 32.6 | 100% |
| 8 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 2,530.6 | 2,529.2 | 2,579.4 | 19.4 | 0.333x | 1.859x | - | 77 | 32.9 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,469.0 | 3,370.0 | 3,553.3 | 64.6 | 0.457x | 2.548x | - | 77 | 45.1 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,589.8 | 7,471.2 | 7,808.9 | 117.6 | 1.000x | 5.575x | - | 77 | 98.6 | 100% |

- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `s-000`, 18.6 ns, 16 B; largest Δ: `s-083`, -0.6 ns (now 9.5 ns), 43 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now (also the largest Δ): `s-043`, 18.7 ns, 22 B
- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `s-083`, 136.7 ns, 43 B; largest Δ: `s-084`, -3.9 ns (now 46.0 ns), 10 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now (also the largest Δ): `s-083`, 139.6 ns, 43 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 13,586,691.1 | 2.5915 | 13,528,810.2 | 13,661,164.5 | 48,476.7 | 0.110x | 1.000x | - | 5 | 100% |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 13,586,898.8 | 2.5915 | 13,567,348.6 | 13,609,391.2 | 15,307.1 | 0.110x | 1.000x | unchanged (within spread) | 5 | 100% |
| 3 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 13,591,290.1 | 2.5923 | 13,571,707.0 | 13,689,336.5 | 45,361.0 | 0.110x | 1.000x | unchanged (within spread) | 5 | 100% |
| 4 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 13,609,551.7 | 2.5958 | 13,584,614.0 | 13,613,088.3 | 10,455.9 | 0.110x | 1.002x | - | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,220,243.6 | 3.4752 | 18,181,812.7 | 19,016,218.5 | 319,595.3 | 0.147x | 1.341x | - | 5 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 123,868,558.9 | 23.6261 | 122,840,836.5 | 125,511,976.9 | 969,778.5 | 1.000x | 9.117x | - | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,579,415.8 | 3.4136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,583,346.1 | 3.4173 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,582,024.1 | 3.4161 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,584,658.7 | 3.4186 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,704,618.8 | 3.5330 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,917,610.5 | 27.5780 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,888,829.9 | 1.8013 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,890,919.6 | 1.8033 |
| `t-b-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,892,116.2 | 1.8045 |
| `t-b-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,895,118.8 | 1.8073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,542,172.6 | 2.4244 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,007.3 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 1,876,578.1 | 1.7896 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 1,877,410.1 | 1.7904 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 1,878,493.8 | 1.7915 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 1,878,612.2 | 1.7916 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,820,397.6 | 2.6897 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,981.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,133,275.5 | 2.9881 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,145,599.7 | 2.9999 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,140,389.6 | 2.9949 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,138,982.6 | 2.9936 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,968,396.9 | 5.6919 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 94,897,024.5 | 90.5009 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-nocaps-simdna` | 3,113,753.6 | 2.9695 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-caps-simdna` | 3,094,151.3 | 2.9508 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_36d5963_auto-nocaps-simdna` | 3,091,404.0 | 2.9482 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_35e1ab1_auto-caps-simdna` | 3,106,092.4 | 2.9622 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,157,766.2 | 3.0115 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,063.1 | 0.0172 |

- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,583,346.1 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -11,941.0 ns (now 3,094,151.3 ns), 1,048,576 B
- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,582,024.1 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -22,349.6 ns (now 3,091,404.0 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,129.7 | 62,020.5 | 62,288.3 | 94.6 | 0.116x | 1.000x | - |
| 2 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,713.6 | 62,618.4 | 62,834.9 | 72.6 | 0.117x | 1.009x | slower ×1.01 |
| 3 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,804.9 | 62,698.9 | 62,947.0 | 91.8 | 0.117x | 1.011x | - |
| 4 | `pcrec_36d5963_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 63,023.4 | 62,788.1 | 63,372.5 | 188.3 | 0.118x | 1.014x | unchanged (within spread) |
| 5 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,306.7 | 73,279.6 | 73,348.2 | 22.3 | 0.137x | 1.180x | faster ×1.82 |
| 6 | `pcrec_36d5963_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,309.9 | 73,302.2 | 73,529.6 | 101.5 | 0.137x | 1.180x | faster ×1.83 |
| 7 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 133,784.0 | 133,732.1 | 133,983.3 | 94.1 | 0.250x | 2.153x | - |
| 8 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 133,799.6 | 133,717.0 | 133,825.2 | 36.9 | 0.250x | 2.154x | - |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 535,094.0 | 533,955.6 | 547,752.4 | 5,279.6 | 1.000x | 8.613x | - |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 535,304.5 | 534,347.4 | 535,987.6 | 555.2 | 1.000x | 8.616x | - |

- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `s-059`, 13,749.7 ns, 5,134 B; largest Δ: `s-064`, +70.1 ns (now 10,658.7 ns), 4,110 B
- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `s-059`, 13,721.9 ns, 5,134 B; largest Δ: `s-058`, +57.4 ns (now 6,329.1 ns), 4,011 B
- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `s-060`, 19,107.8 ns, 10,240 B; largest Δ: `s-057`, -19,112.5 ns (now 19,097.0 ns), 10,252 B
- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,097.0 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_35e1ab1_auto-nocaps-simdna` | measured | `plain` | same program | 3,527.1 | 3,524.7 | 3,550.2 | 9.7 | 0.053x | 1.000x | - | 77 | 45.8 | 17.7 | 100% |
| 2 | `pcrec_36d5963_auto-caps-simdna` | measured | `plain` | same program | 3,531.7 | 3,527.9 | 3,555.3 | 11.5 | 0.054x | 1.001x | unchanged (within spread) | 77 | 45.9 | 17.7 | 100% |
| 3 | `pcrec_35e1ab1_auto-caps-simdna` | measured | `plain` | same program | 3,533.0 | 3,523.9 | 3,533.4 | 4.1 | 0.054x | 1.002x | - | 77 | 45.9 | 17.7 | 100% |
| 4 | `pcrec_36d5963_auto-nocaps-simdna` | measured | `plain` | same program | 3,534.8 | 3,528.8 | 3,546.3 | 6.6 | 0.054x | 1.002x | unchanged (within spread) | 77 | 45.9 | 17.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,127.6 | 6,102.7 | 6,710.4 | 243.6 | 0.093x | 1.737x | - | 77 | 79.6 | 45.1 | 100% |
| 6 | `pcrec_35e1ab1_vm-caps-simdna` | measured | `plain` | same program | 12,517.8 | 12,422.0 | 12,657.3 | 82.6 | 0.190x | 3.549x | - | 77 | 162.6 | 32.6 | 100% |
| 7 | `pcrec_35e1ab1_vm-in-caps-simdna` | measured | `plain` | same program | 12,632.4 | 12,600.2 | 12,687.0 | 33.7 | 0.191x | 3.582x | - | 77 | 164.1 | 32.9 | 100% |
| 8 | `pcrec_36d5963_vm-caps-simdna` | measured | `plain` | same program | 12,819.6 | 12,759.2 | 12,876.4 | 42.4 | 0.194x | 3.635x | slower ×1.02 | 77 | 166.5 | 31.7 | 100% |
| 9 | `pcrec_36d5963_vm-in-caps-simdna` | measured | `plain` | same program | 13,146.2 | 13,106.0 | 13,170.9 | 23.2 | 0.199x | 3.727x | slower ×1.04 | 77 | 170.7 | 32.0 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 66,004.3 | 65,709.2 | 66,147.6 | 149.3 | 1.000x | 18.713x | - | 77 | 857.2 | 98.6 | 100% |

- Δ detail: `pcrec_36d5963_auto-caps-simdna` vs previous `pcrec_35e1ab1_auto-caps-simdna`: worst now: `s-004`, 120.4 ns, 33 B; largest Δ: `s-017`, +0.7 ns (now 66.2 ns), 18 B
- Δ detail: `pcrec_36d5963_auto-nocaps-simdna` vs previous `pcrec_35e1ab1_auto-nocaps-simdna`: worst now: `s-004`, 120.2 ns, 33 B; largest Δ: `s-041`, +0.9 ns (now 19.9 ns), 12 B
- Δ detail: `pcrec_36d5963_vm-caps-simdna` vs previous `pcrec_35e1ab1_vm-caps-simdna`: worst now: `s-035`, 696.9 ns, 16 B; largest Δ: `s-009`, +16.7 ns (now 67.6 ns), 14 B
- Δ detail: `pcrec_36d5963_vm-in-caps-simdna` vs previous `pcrec_35e1ab1_vm-in-caps-simdna`: worst now: `s-035`, 716.9 ns, 16 B; largest Δ: `s-004`, +24.2 ns (now 93.0 ns), 33 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

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
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.

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
| `factored` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 163,173,581.0 | 148,043,728.0 | 165,355,524.0 | 6,230,940.4 | 5 | 43,000 | 0.038 | compiled=5 | 9,712,969.0 | 151,485,660.0 | 186,221.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 172,018,683.0 | 169,330,388.0 | 187,531,128.0 | 6,850,899.9 | 5 | 47,240 | 0.040 (max is trial 1) | compiled=5 | 11,935,272.0 | 160,085,781.0 | 190,281.0 |
| `factored` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 158,379,641.0 | 144,622,938.0 | 160,943,538.0 | 6,230,002.9 | 5 | 43,000 | 0.039 (max is trial 1) | compiled=5 | 9,574,438.0 | 140,183,871.0 | 190,981.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,254,961.0 | 156,661,801.0 | 182,598,618.0 | 9,464,812.7 | 5 | 47,240 | 0.058 (max is trial 1) | compiled=5 | 11,943,713.0 | 151,211,278.0 | 192,071.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 567,703,383.0 | 559,754,886.0 | 571,675,245.0 | 4,062,965.4 | 5 | 34,816 | 0.007 | compiled=5 | 2,253,513.0 | 564,927,396.0 | 125,381.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 559,242,744.0 | 556,895,190.0 | 570,217,336.0 | 4,711,477.0 | 5 | 34,816 | 0.008 | compiled=5 | 2,213,983.0 | 556,877,430.0 | 212,661.0 |
| `factored` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 555,700,975.0 | 548,732,151.0 | 561,291,690.0 | 5,165,541.3 | 5 | 34,816 | 0.009 | compiled=5 | 2,286,274.0 | 553,427,801.0 | 190,972.0 |
| `factored` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 551,792,261.0 | 547,407,994.0 | 564,315,969.0 | 6,285,963.3 | 5 | 34,816 | 0.011 | compiled=5 | 2,263,684.0 | 548,875,712.0 | 118,861.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 128,124,003.0 | 121,815,237.0 | 132,250,058.0 | 3,741,734.5 | 5 | 17,816 | 0.029 | compiled=5 | 1,563,309.0 | 126,608,855.0 | 112,481.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 136,601,994.0 | 125,250,527.0 | 138,196,622.0 | 6,006,842.3 | 5 | 17,904 | 0.044 (max is trial 1) | compiled=5 | 1,463,518.0 | 134,997,154.0 | 200,402.0 |
| `floor` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 125,053,645.0 | 118,093,685.0 | 130,520,689.0 | 4,812,299.8 | 5 | 17,816 | 0.038 (max is trial 1) | compiled=5 | 1,404,458.0 | 123,415,805.0 | 99,061.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 135,198,375.0 | 124,770,805.0 | 136,922,336.0 | 4,667,899.5 | 5 | 17,904 | 0.035 | compiled=5 | 1,432,719.0 | 132,068,647.0 | 199,521.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 143,839,405.0 | 133,489,685.0 | 145,996,357.0 | 4,499,436.2 | 5 | 17,600 | 0.031 | compiled=5 | 1,470,958.0 | 142,085,106.0 | 104,780.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 131,485,234.0 | 130,493,468.0 | 152,939,310.0 | 9,269,487.4 | 5 | 17,600 | 0.070 | compiled=5 | 1,303,697.0 | 130,010,745.0 | 190,152.0 |
| `floor` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 143,130,173.0 | 127,595,569.0 | 148,446,484.0 | 7,271,673.7 | 5 | 17,600 | 0.051 (max is trial 1) | compiled=5 | 1,367,788.0 | 141,680,644.0 | 107,271.0 |
| `floor` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 136,645,873.0 | 127,325,307.0 | 145,517,016.0 | 6,966,108.5 | 5 | 17,600 | 0.051 | compiled=5 | 1,317,248.0 | 135,247,565.0 | 93,341.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 137,975,417.0 | 130,154,820.0 | 142,913,866.0 | 4,140,189.2 | 5 | 22,488 | 0.030 | compiled=5 | 3,055,408.0 | 135,445,562.0 | 190,461.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 144,611,468.0 | 133,599,301.0 | 149,537,718.0 | 6,141,196.3 | 5 | 22,632 | 0.042 | compiled=5 | 1,661,280.0 | 142,664,806.0 | 196,431.0 |
| `floor` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 137,161,193.0 | 131,844,181.0 | 140,083,190.0 | 2,832,113.2 | 5 | 22,488 | 0.021 (max is trial 1) | compiled=5 | 1,624,910.0 | 133,667,721.0 | 187,942.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 146,188,127.0 | 137,551,574.0 | 148,622,902.0 | 3,782,109.1 | 5 | 22,632 | 0.026 | compiled=5 | 1,755,770.0 | 142,880,468.0 | 105,240.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 149,341,986.0 | 137,028,735.0 | 150,343,371.0 | 4,944,844.8 | 5 | 22,120 | 0.033 | compiled=5 | 1,696,930.0 | 147,530,796.0 | 176,811.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 146,819,080.0 | 139,205,948.0 | 153,194,038.0 | 4,814,096.7 | 5 | 22,120 | 0.033 | compiled=5 | 1,431,778.0 | 145,203,761.0 | 187,691.0 |
| `floor` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 143,224,196.0 | 133,623,356.0 | 149,166,282.0 | 5,314,418.2 | 5 | 22,120 | 0.037 | compiled=5 | 1,870,712.0 | 141,694,146.0 | 108,651.0 |
| `floor` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 139,422,771.0 | 137,041,307.0 | 155,827,535.0 | 7,167,340.5 | 5 | 22,120 | 0.051 | compiled=5 | 2,750,817.0 | 137,806,721.0 | 199,131.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-caps-simdna` | 143,041,582.0 | 133,638,077.0 | 152,605,977.0 | 7,423,117.4 | 5 | 38,288 | 0.052 | compiled=5 | 8,399,070.0 | 133,049,073.0 | 97,811.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-caps-simdna` | 161,003,156.0 | 144,668,771.0 | 174,001,693.0 | 9,821,090.4 | 5 | 38,376 | 0.061 | compiled=5 | 18,044,156.0 | 141,891,755.0 | 186,281.0 |
| `orig` | `plain` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,731,375.0 | 133,116,513.0 | 154,306,767.0 | 7,366,531.2 | 5 | 38,288 | 0.050 | compiled=5 | 8,303,388.0 | 134,495,101.0 | 190,511.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_auto-nocaps-simdna` | 148,766,935.0 | 141,953,955.0 | 157,360,185.0 | 5,601,770.9 | 5 | 38,376 | 0.038 (max is trial 1) | compiled=5 | 10,395,781.0 | 138,189,823.0 | 191,472.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-caps-simdna` | 425,700,355.0 | 418,138,020.0 | 433,200,719.0 | 5,739,473.7 | 5 | 26,112 | 0.013 | compiled=5 | 3,573,812.0 | 423,604,592.0 | 98,321.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-caps-simdna` | 418,219,710.0 | 416,284,479.0 | 424,829,349.0 | 3,247,138.2 | 5 | 26,112 | 0.008 | compiled=5 | 1,887,041.0 | 416,182,378.0 | 101,761.0 |
| `orig` | `plain` | `pcrec_35e1ab1_vm-in-caps-simdna` | 426,965,172.0 | 417,563,868.0 | 436,633,782.0 | 6,421,511.5 | 5 | 26,112 | 0.015 | compiled=5 | 3,456,131.0 | 422,794,938.0 | 94,571.0 |
| `orig` | `whole-subject` | `pcrec_35e1ab1_vm-in-caps-simdna` | 416,505,570.0 | 410,439,183.0 | 436,855,013.0 | 9,723,201.5 | 5 | 26,112 | 0.023 (max is trial 1) | compiled=5 | 3,768,522.0 | 414,571,809.0 | 91,591.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-caps-simdna` | 160,234,903.0 | 142,502,585.0 | 170,930,038.0 | 9,452,596.4 | 5 | 42,960 | 0.059 (max is trial 1) | compiled=5 | 9,209,996.0 | 144,087,044.0 | 215,871.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-caps-simdna` | 166,290,610.0 | 163,930,325.0 | 182,586,678.0 | 6,746,131.3 | 5 | 47,200 | 0.041 | compiled=5 | 11,352,189.0 | 154,132,576.0 | 207,132.0 |
| `orig` | `plain` | `pcrec_36d5963_auto-nocaps-simdna` | 152,456,135.0 | 144,069,245.0 | 174,208,458.0 | 10,143,322.1 | 5 | 42,960 | 0.067 | compiled=5 | 9,225,456.0 | 143,266,640.0 | 102,641.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_auto-nocaps-simdna` | 163,517,013.0 | 155,667,265.0 | 165,485,665.0 | 4,206,358.8 | 5 | 47,200 | 0.026 | compiled=5 | 11,363,629.0 | 151,287,019.0 | 199,952.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-caps-simdna` | 429,171,779.0 | 423,947,059.0 | 447,217,713.0 | 8,229,989.8 | 5 | 30,632 | 0.019 (max is trial 1) | compiled=5 | 1,931,061.0 | 427,170,727.0 | 194,501.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-caps-simdna` | 435,901,317.0 | 424,067,939.0 | 452,243,691.0 | 11,235,002.5 | 5 | 30,632 | 0.026 | compiled=5 | 2,212,242.0 | 431,366,691.0 | 196,301.0 |
| `orig` | `plain` | `pcrec_36d5963_vm-in-caps-simdna` | 430,350,492.0 | 428,462,499.0 | 435,167,061.0 | 2,401,459.0 | 5 | 30,632 | 0.006 (max is trial 1) | compiled=5 | 2,006,842.0 | 428,298,358.0 | 184,621.0 |
| `orig` | `whole-subject` | `pcrec_36d5963_vm-in-caps-simdna` | 429,422,065.0 | 424,291,654.0 | 437,092,543.0 | 4,553,396.7 | 5 | 30,632 | 0.011 | compiled=5 | 4,000,955.0 | 425,227,189.0 | 186,951.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 79,241.0 | 65,550.0 | 161,422.0 | 35,427.1 | 5 | 951 | 0.447 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,180.0 | 4,820.0 | 57,130.0 | 20,468.0 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 148,601.0 | 139,231.0 | 367,712.0 | 87,829.9 | 5 | 1,609 | 0.591 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,540.0 | 13,051.0 | 45,860.0 | 12,622.0 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,270.0 | 5,961.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 13,430.0 | 12,301.0 | 43,590.0 | 12,093.7 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

