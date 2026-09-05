# pcrec-bench report

reporter: v13 (2026-09-03)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-09-02T02:40:00Z, until=2026-09-05T04:10:00Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_288d505_auto-caps-simdna, testee=pcrec_1989c62_auto-caps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 8.2% (`pcrec_1989c62_auto-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (../../store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (../../store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z` (../../store/records/email-specimen@0.2/pcrec_1989c62_auto-caps-simdna/email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_288d505_auto-caps-simdna__budu-ryzen1600__20260905T040524Z` (../../store/records/email-specimen@0.2/pcrec_288d505_auto-caps-simdna/email-specimen@0.2__pcrec_288d505_auto-caps-simdna__budu-ryzen1600__20260905T040524Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.5
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 4 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 13,683,591.1 | 2.6099 | 13,677,516.1 | 13,704,448.8 | 10,134.3 | 0.027x | 1.000x | - | 5 | 100% |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 13,691,593.4 | 2.6115 | 13,658,025.6 | 13,706,128.5 | 18,570.3 | 0.027x | 1.001x | unchanged (within spread) | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 36.440x | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,584,231.2 | 3.4182 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,588,166.2 | 3.4219 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,879,469.6 | 1.7924 |
| `t-b-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 1,875,059.9 | 1.7882 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,875,293.9 | 1.7884 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 1,875,907.4 | 1.7890 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,190,860.9 | 3.0430 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,181,424.3 | 3.0340 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,157,983.1 | 3.0117 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,152,336.1 | 3.0063 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,588,166.2 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -9,436.6 ns (now 3,181,424.3 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,254.9 | 73,239.0 | 73,364.9 | 45.3 | 0.040x | 1.000x | unchanged (within spread) |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,257.3 | 73,236.9 | 73,355.6 | 43.1 | 0.040x | 1.000x | - |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.048x | - |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.223x | - |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,066.3 ns, 10,252 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,660.3 | 3,657.9 | 3,665.5 | 2.8 | 0.027x | 1.000x | unchanged (within spread) | 77 | 47.5 | 17.6 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,664.3 | 3,662.4 | 3,677.2 | 5.4 | 0.027x | 1.001x | - | 77 | 47.6 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.175x | - | 77 | 198.4 | 44.2 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 37.685x | - | 77 | 1,791.4 | 95.9 | 100% |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `s-004`, 123.7 ns, 33 B; largest Δ: `s-082`, -1.0 ns (now 5.4 ns), 1 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 710,846.8 | 0.1356 | 710,609.8 | 711,393.9 | 265.4 | 0.192x | 1.000x | spread | unchanged (within spread) |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 710,901.6 | 0.1356 | 710,333.3 | 711,068.1 | 307.0 | 0.192x | 1.000x | spread | - |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.697x | **dominated**: `t-a-valid-addrs` is 90.2% of this set | - |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.218x | **dominated**: `t-a-valid-addrs` is 96.7% of this set | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 626,935.4 | 0.5979 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 627,124.2 | 0.5981 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 17,699.5 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,686.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 17,696.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,628.6 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 30,893.6 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 30,829.4 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 17,643.5 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,634.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 626,935.4 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 856.8 | 856.5 | 877.2 | 8.2 | 0.334x | 1.000x | unchanged (within spread) |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 874.0 | 862.7 | 892.4 | 10.2 | 0.340x | 1.020x | - |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 2.998x | - |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 3.006x | - |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `s-082`, 12.4 ns, 1 B; largest Δ: `s-081`, -0.4 ns (now 10.2 ns), 0 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 1,356.6 | 1,350.1 | 1,364.9 | 5.1 | 0.184x | 1.000x | unchanged (within spread) | 77 | 17.6 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 1,359.9 | 1,351.5 | 1,378.8 | 9.3 | 0.184x | 1.002x | - | 77 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 2.507x | - | 77 | 44.2 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 5.446x | - | 77 | 95.9 | 100% |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `s-043`, 19.8 ns, 22 B; largest Δ: `s-084`, -1.2 ns (now 8.7 ns), 10 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 13,578,816.8 | 2.5900 | 13,567,353.8 | 13,595,411.6 | 9,073.4 | 0.111x | 1.000x | - |
| 2 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 13,579,853.5 | 2.5902 | 13,562,922.8 | 13,584,016.4 | 7,661.1 | 0.111x | 1.000x | unchanged (within spread) |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.339x | - |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 9.035x | - |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,576,575.8 | 3.4109 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,582,953.6 | 3.4170 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,892,471.5 | 1.8048 |
| `t-b-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 1,893,311.9 | 1.8056 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,875,730.8 | 1.7888 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 1,874,805.3 | 1.7880 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,137,862.7 | 2.9925 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,126,954.3 | 2.9821 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,093,057.1 | 2.9498 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_288d505_auto-caps-simdna` | 3,101,972.4 | 2.9583 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,582,953.6 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -10,908.4 ns (now 3,126,954.3 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,146.4 | 73,130.2 | 73,154.0 | 8.2 | 0.136x | 1.000x | faster ×1.00 |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,181.3 | 73,167.7 | 73,196.5 | 9.3 | 0.136x | 1.000x | - |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 7.304x | - |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 7.346x | - |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `s-057`, 19,061.9 ns, 10,252 B; largest Δ: `s-060`, -13.5 ns (now 19,037.6 ns), 10,240 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_288d505_auto-caps-simdna` | measured | `plain` | same program | 3,516.3 | 3,514.2 | 3,523.5 | 3.2 | 0.053x | 1.000x | unchanged (within spread) | 77 | 45.7 | 17.6 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured | `plain` | same program | 3,529.5 | 3,518.5 | 3,545.8 | 9.3 | 0.054x | 1.004x | - | 77 | 45.8 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.751x | - | 77 | 80.0 | 44.2 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.704x | - | 77 | 854.1 | 95.9 | 100% |

- Δ detail: `pcrec_288d505_auto-caps-simdna` vs previous `pcrec_1989c62_auto-caps-simdna`: worst now: `s-004`, 120.1 ns, 33 B; largest Δ: `s-082`, -1.2 ns (now 5.3 ns), 1 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_1989c62_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_288d505_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 164,915,127.0 | 156,981,861.0 | 182,641,919.0 | 8,625,738.7 | 5 | 43,344 | 82,314 | 13,620 | 0.052 | compiled=5 | 21,246,982.0 | 147,074,564.0 | 190,671.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 173,581,817.0 | 166,130,205.0 | 183,948,586.0 | 6,720,513.4 | 5 | 47,584 | 94,525 | 15,536 | 0.039 | compiled=5 | 12,067,839.0 | 161,425,557.0 | 109,531.0 |
| `factored` | `plain` | `pcrec_288d505_auto-caps-simdna` | 158,778,616.0 | 158,398,844.0 | 179,484,234.0 | 8,701,313.4 | 5 | 47,728 | 82,424 | 13,730 | 0.055 (max is trial 1) | compiled=5 | 9,906,122.0 | 148,792,303.0 | 112,661.0 |
| `factored` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 178,193,008.0 | 171,097,333.0 | 180,329,800.0 | 3,444,464.3 | 5 | 47,872 | 94,635 | 15,646 | 0.019 | compiled=5 | 12,137,206.0 | 165,947,621.0 | 103,491.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 138,937,769.0 | 130,915,322.0 | 149,545,609.0 | 6,514,661.1 | 5 | 22,832 | 17,965 | 12,968 | 0.047 | compiled=5 | 1,809,261.0 | 137,082,487.0 | 189,661.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 149,982,771.0 | 145,127,543.0 | 155,552,133.0 | 3,491,085.5 | 5 | 22,968 | 20,308 | 14,985 | 0.023 | compiled=5 | 1,692,279.0 | 148,114,051.0 | 96,651.0 |
| `floor` | `plain` | `pcrec_288d505_auto-caps-simdna` | 140,190,810.0 | 135,797,732.0 | 147,058,772.0 | 4,141,120.9 | 5 | 27,216 | 18,075 | 13,078 | 0.030 | compiled=5 | 1,658,620.0 | 138,230,527.0 | 105,440.0 |
| `floor` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 155,838,228.0 | 143,964,803.0 | 157,904,771.0 | 5,742,878.0 | 5 | 27,352 | 20,418 | 15,095 | 0.037 | compiled=5 | 1,693,591.0 | 154,040,776.0 | 107,020.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 156,626,339.0 | 152,463,315.0 | 162,571,233.0 | 3,827,137.0 | 5 | 43,304 | 81,907 | 13,380 | 0.024 | compiled=5 | 9,352,623.0 | 147,153,485.0 | 107,731.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 169,897,296.0 | 158,601,931.0 | 180,453,986.0 | 7,594,084.9 | 5 | 47,544 | 94,118 | 15,296 | 0.045 (max is trial 1) | compiled=5 | 11,432,616.0 | 150,413,164.0 | 196,642.0 |
| `orig` | `plain` | `pcrec_288d505_auto-caps-simdna` | 155,010,061.0 | 143,823,141.0 | 173,840,701.0 | 9,875,501.6 | 5 | 47,688 | 82,017 | 13,490 | 0.064 | compiled=5 | 9,649,731.0 | 145,232,460.0 | 111,091.0 |
| `orig` | `whole-subject` | `pcrec_288d505_auto-caps-simdna` | 178,467,200.0 | 164,943,363.0 | 181,739,570.0 | 7,158,180.3 | 5 | 47,832 | 94,228 | 15,406 | 0.040 (max is trial 1) | compiled=5 | 11,517,913.0 | 158,921,187.0 | 105,001.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 70,150.0 | 64,051.0 | 167,201.0 | 39,050.5 | 5 | 951 | 0.557 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,351.0 | 5,120.0 | 51,820.0 | 18,281.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 59,880.0 | 54,300.0 | 175,181.0 | 46,340.9 | 5 | 1,609 | 0.774 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,450.0 | 13,070.0 | 50,681.0 | 14,528.5 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,470.0 | 6,041.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 33,290.0 | 30,010.0 | 102,420.0 | 27,822.1 | 5 | 1,609 | 0.836 (max is trial 1) | compiled=5 |

