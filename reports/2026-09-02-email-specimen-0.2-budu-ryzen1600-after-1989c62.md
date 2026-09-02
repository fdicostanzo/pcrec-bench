# pcrec-bench report

reporter: v11 (2026-09-01)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-09-03T00:00:00Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_1989c62_auto-caps-simdna, testee=pcrec_1989c62_auto-nocaps-simdna, testee=pcrec_1989c62_vm-caps-simdna, testee=pcrec_1989c62_vm-in-caps-simdna, testee=pcrec_96e44c2_auto-caps-simdna, testee=pcrec_96e44c2_auto-nocaps-simdna, testee=pcrec_96e44c2_vm-caps-simdna, testee=pcrec_96e44c2_vm-in-caps-simdna
- record source: store/index.tsv (111 candidate file(s))
- records included: 10
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-caps-simdna/email-specimen@0.2__pcrec_1989c62_auto-caps-simdna__budu-ryzen1600__20260902T081329Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-nocaps-simdna/email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-in-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-caps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-nocaps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-in-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z.jsonl) — agreement: n/a (v1.3)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3, 1.4
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 4 record(s); v1.4 X13 (pre-flight + trial agreement) on 6 record(s) — MIXED: every ranking row's status cell carries the record's schema version (`measured@1.3` / `measured@1.4`)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 13,583,640.9 | 2.5909 | 13,563,234.4 | 13,588,319.8 | 9,475.1 | 0.027x | 1.000x | unchanged (within spread) | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 13,595,834.2 | 2.5932 | 13,569,312.4 | 13,731,462.8 | 60,163.9 | 0.027x | 1.001x | - | 5 | 100% |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 13,683,591.1 | 2.6099 | 13,677,516.1 | 13,704,448.8 | 10,134.3 | 0.027x | 1.007x | unchanged (within spread) | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 13,704,256.6 | 2.6139 | 13,685,839.0 | 13,749,076.2 | 21,250.8 | 0.027x | 1.009x | - | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 36.708x | - | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,581,417.1 | 3.4155 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,581,485.2 | 3.4156 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,584,231.2 | 3.4182 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,588,937.2 | 3.4227 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,881,379.0 | 1.7942 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,891,541.7 | 1.8039 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,879,469.6 | 1.7924 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,877,627.3 | 1.7906 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,877,090.2 | 1.7901 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,878,044.0 | 1.7910 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,875,293.9 | 1.7884 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,184.2 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,149,477.5 | 3.0036 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,137,206.7 | 2.9919 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,190,860.9 | 3.0430 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,198,130.0 | 3.0500 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,092,666.6 | 2.9494 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,099,418.9 | 2.9558 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,157,983.1 | 3.0117 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,166,592.9 | 3.0199 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,581,417.1 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, +12,270.8 ns (now 3,149,477.5 ns), 1,048,576 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `t-a-valid-addrs`, 3,584,231.2 ns, 1,048,576 B; largest Δ: `t-e-prose-no-at`, -8,609.8 ns (now 3,157,983.1 ns), 1,048,576 B

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73,179.2 | 73,161.2 | 73,330.5 | 63.1 | 0.040x | 1.000x | unchanged (within spread) | 85 | 100% |
| 2 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73,257.3 | 73,236.9 | 73,355.6 | 43.1 | 0.040x | 1.001x | faster ×1.00 | 85 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73,301.0 | 73,260.7 | 73,340.4 | 25.4 | 0.040x | 1.002x | - | 85 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73,383.3 | 73,375.9 | 73,385.8 | 3.3 | 0.040x | 1.003x | - | 85 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 461,165.2 | 455,738.7 | 466,627.4 | 3,547.8 | 0.251x | 6.302x | unchanged (within spread) | 85 | 100% |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 462,186.8 | 461,060.9 | 465,355.0 | 1,465.4 | 0.252x | 6.316x | - | 85 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.074x | - | 85 | 100% |
| 8 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.249x | - | 85 | 100% |

- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-057`, 19,070.0 ns, 10,252 B; largest Δ: `s-060`, -31.5 ns (now 19,047.2 ns), 10,240 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `s-057`, 19,073.4 ns, 10,252 B; largest Δ: `s-060`, -34.5 ns (now 19,043.2 ns), 10,240 B
- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now: `s-060`, 194,185.2 ns, 10,240 B; largest Δ: `s-063`, -482.2 ns (now 99,310.0 ns), 5,135 B

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,524.4 | 3,519.8 | 3,602.1 | 31.7 | 0.026x | 1.000x | unchanged (within spread) | 77 | 45.8 | 17.6 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,527.2 | 3,525.6 | 3,536.6 | 4.0 | 0.026x | 1.001x | - | 77 | 45.8 | 17.3 | 100% |
| 3 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,664.3 | 3,662.4 | 3,677.2 | 5.4 | 0.027x | 1.040x | unchanged (within spread) | 77 | 47.6 | 17.7 | 100% |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,667.3 | 3,661.1 | 3,671.7 | 3.6 | 0.027x | 1.041x | - | 77 | 47.6 | 17.2 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.335x | - | 77 | 198.4 | 44.2 | 100% |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 53,848.7 | 53,614.7 | 54,626.5 | 355.7 | 0.390x | 15.279x | unchanged (within spread) | 77 | 699.3 | 13.7 | 100% |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 53,902.2 | 53,519.5 | 54,707.0 | 391.5 | 0.391x | 15.294x | unchanged (within spread) | 77 | 700.0 | 13.6 | 100% |
| 8 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 53,906.8 | 53,710.9 | 54,238.1 | 182.2 | 0.391x | 15.295x | - | 77 | 700.1 | 31.4 | 100% |
| 9 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 54,069.3 | 53,491.4 | 54,216.1 | 257.6 | 0.392x | 15.341x | - | 77 | 702.2 | 31.7 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 39.138x | - | 77 | 1,791.4 | 95.9 | 100% |

- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-004`, 120.1 ns, 33 B; largest Δ: `s-082`, +1.2 ns (now 6.5 ns), 1 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `s-004`, 123.9 ns, 33 B; largest Δ: `s-082`, +0.9 ns (now 6.4 ns), 1 B
- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now: `s-029`, 3,261.6 ns, 28 B; largest Δ: `s-031`, +121.9 ns (now 1,511.0 ns), 19 B
- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now: `s-029`, 3,274.2 ns, 28 B; largest Δ: `s-040`, -138.9 ns (now 1,703.9 ns), 15 B

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 710,901.6 | 0.1356 | 710,333.3 | 711,068.1 | 307.0 | 0.192x | 1.000x | spread | unchanged (within spread) |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 711,171.0 | 0.1356 | 710,981.1 | 1,145,934.8 | 173,418.1 | 0.192x | 1.000x | spread | unchanged (within spread) |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 713,176.7 | 0.1360 | 711,858.4 | 719,884.4 | 2,872.0 | 0.192x | 1.003x | spread | - |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 713,484.5 | 0.1361 | 711,877.5 | 714,765.8 | 1,046.9 | 0.192x | 1.004x | spread | - |
| 5 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,832,899.2 | 0.3496 | 1,831,518.1 | 1,847,785.7 | 7,649.4 | 0.494x | 2.578x | spread | faster ×8.91 |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.697x | **dominated**: `t-a-valid-addrs` is 90.2% of this set | - |
| 7 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,920,640.2 | 0.3663 | 1,905,569.9 | 1,965,206.8 | 22,635.0 | 0.518x | 2.702x | spread | faster ×8.52 |
| 8 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.218x | **dominated**: `t-a-valid-addrs` is 96.7% of this set | - |
| 9 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 16,325,112.9 | 3.1138 | 15,821,062.7 | 16,573,878.5 | 308,141.1 | 4.401x | 22.964x | spread | - |
| 10 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 16,371,986.6 | 3.1227 | 16,299,110.1 | 16,640,133.5 | 120,554.5 | 4.414x | 23.030x | spread | - |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 627,124.2 | 0.5981 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 627,246.0 | 0.5982 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 628,684.2 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 628,731.1 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 581,707.3 | 0.5548 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 658,242.3 | 0.6277 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,923,994.5 | 3.7422 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 4,012,120.3 | 3.8263 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,686.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,662.8 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,669.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,732.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,113.4 | 0.2957 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,324.2 | 0.2959 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,076,750.8 | 2.9342 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,047,388.0 | 2.9062 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,628.6 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,621.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,697.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,117.0 | 0.2958 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,392.8 | 0.2960 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,799,563.2 | 2.6699 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 2,791,699.8 | 2.6624 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 30,829.4 | 0.0294 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 30,896.9 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 30,981.7 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 30,939.0 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 320,961.8 | 0.3061 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 322,506.7 | 0.3076 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,337,656.4 | 3.1830 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,368,779.2 | 3.2127 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 17,634.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,645.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,695.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,051.9 | 0.2957 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,488.9 | 0.2961 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,941,908.1 | 2.8056 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,407,572.1 | 3.2497 |

- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 627,124.2 ns, 1,048,576 B
- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 627,246.0 ns, 1,048,576 B
- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 581,707.3 ns, 1,048,576 B
- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 658,242.3 ns, 1,048,576 B

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 432.9 | 431.7 | 434.5 | 1.0 | 0.169x | 1.000x | faster ×1.58 |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 516.6 | 516.4 | 517.7 | 0.5 | 0.201x | 1.193x | faster ×1.51 |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 685.4 | 685.0 | 686.2 | 0.4 | 0.267x | 1.583x | - |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 782.6 | 781.7 | 786.7 | 1.8 | 0.305x | 1.808x | - |
| 5 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 831.4 | 827.5 | 835.1 | 3.0 | 0.324x | 1.921x | - |
| 6 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 834.1 | 827.3 | 839.7 | 4.1 | 0.325x | 1.927x | - |
| 7 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 874.0 | 862.7 | 892.4 | 10.2 | 0.340x | 2.019x | slower ×1.05 |
| 8 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 875.7 | 860.0 | 884.2 | 7.9 | 0.341x | 2.023x | slower ×1.05 |
| 9 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 5.934x | - |
| 10 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 5.950x | - |

- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now: `s-082`, 8.9 ns, 1 B; largest Δ: `s-041`, -4.5 ns (now 5.6 ns), 12 B
- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now: `s-082`, 8.1 ns, 1 B; largest Δ: `s-027`, -3.2 ns (now 6.1 ns), 22 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `s-082`, 12.4 ns, 1 B; largest Δ: `s-083`, +0.7 ns (now 10.4 ns), 43 B
- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-082`, 12.4 ns, 1 B; largest Δ: `s-016`, +0.6 ns (now 10.3 ns), 17 B

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 1,045.1 | 1,043.2 | 1,047.9 | 1.6 | 0.141x | 1.000x | faster ×2.33 | 77 | 13.6 | 100% |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 1,057.6 | 1,054.3 | 1,058.3 | 1.4 | 0.143x | 1.012x | faster ×2.29 | 77 | 13.7 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 1,327.8 | 1,326.3 | 1,330.6 | 1.6 | 0.180x | 1.270x | - | 77 | 17.2 | 100% |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 1,329.7 | 1,328.5 | 1,346.0 | 6.7 | 0.180x | 1.272x | - | 77 | 17.3 | 100% |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 1,353.0 | 1,352.2 | 1,372.9 | 8.0 | 0.183x | 1.295x | slower ×1.02 | 77 | 17.6 | 100% |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 1,359.9 | 1,351.5 | 1,378.8 | 9.3 | 0.184x | 1.301x | slower ×1.02 | 77 | 17.7 | 100% |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 2,418.7 | 2,413.7 | 2,422.0 | 2.7 | 0.327x | 2.314x | - | 77 | 31.4 | 100% |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 2,438.3 | 2,435.6 | 2,451.1 | 5.7 | 0.330x | 2.333x | - | 77 | 31.7 | 100% |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 3.254x | - | 77 | 44.2 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 7.069x | - | 77 | 95.9 | 100% |

- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now (also the largest Δ): `s-083`, 28.8 ns, 43 B
- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now (also the largest Δ): `s-083`, 34.4 ns, 43 B
- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-000`, 18.9 ns, 16 B; largest Δ: `s-083`, +1.3 ns (now 10.6 ns), 43 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `s-043`, 19.2 ns, 22 B; largest Δ: `s-084`, +1.3 ns (now 9.9 ns), 10 B

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 13,578,816.8 | 2.5900 | 13,567,353.8 | 13,595,411.6 | 9,073.4 | 0.111x | 1.000x | unchanged (within spread) | 5 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 13,580,774.2 | 2.5903 | 13,566,989.8 | 13,601,866.2 | 13,405.5 | 0.111x | 1.000x | faster ×1.00 | 5 | 100% |
| 3 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 13,607,713.5 | 2.5955 | 13,575,535.2 | 13,632,111.1 | 21,217.8 | 0.111x | 1.002x | - | 5 | 100% |
| 4 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 13,625,779.9 | 2.5989 | 13,583,858.4 | 13,632,604.3 | 20,133.9 | 0.111x | 1.003x | - | 5 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.339x | - | 5 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 9.035x | - | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,576,575.8 | 3.4109 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,584,125.0 | 3.4181 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,583,848.6 | 3.4178 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,587,388.5 | 3.4212 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,892,471.5 | 1.8048 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,888,192.1 | 1.8007 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,887,163.0 | 1.7997 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,886,284.8 | 1.7989 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 1,875,730.8 | 1.7888 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,875,429.5 | 1.7885 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,250.4 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,875,774.8 | 1.7889 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,137,862.7 | 2.9925 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,137,544.3 | 2.9922 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,135,589.7 | 2.9903 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,148,674.1 | 3.0028 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-caps-simdna` | 3,093,057.1 | 2.9498 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,094,784.0 | 2.9514 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,095,070.0 | 2.9517 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,097,595.6 | 2.9541 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now (also the largest Δ): `t-a-valid-addrs`, 3,576,575.8 ns, 1,048,576 B
- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `t-a-valid-addrs`, 3,584,125.0 ns, 1,048,576 B; largest Δ: `t-d-prose-sparse-addrs`, -11,129.8 ns (now 3,137,544.3 ns), 1,048,576 B

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 62,176.3 | 62,132.6 | 62,239.1 | 35.5 | 0.116x | 1.000x | unchanged (within spread) |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 62,301.2 | 62,260.8 | 63,740.2 | 578.8 | 0.116x | 1.002x | - |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 62,809.0 | 62,698.2 | 63,185.7 | 168.0 | 0.117x | 1.010x | unchanged (within spread) |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 62,982.0 | 62,964.9 | 63,086.2 | 44.3 | 0.117x | 1.013x | - |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73,171.4 | 73,144.9 | 73,224.4 | 27.8 | 0.136x | 1.177x | unchanged (within spread) |
| 6 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `whole-subject` | separate artifact | 73,181.3 | 73,167.7 | 73,196.5 | 9.3 | 0.136x | 1.177x | unchanged (within spread) |
| 7 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73,249.7 | 73,230.2 | 73,332.7 | 40.2 | 0.136x | 1.178x | - |
| 8 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `whole-subject` | separate artifact | 73,272.4 | 73,248.6 | 73,457.8 | 78.3 | 0.136x | 1.178x | - |
| 9 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.593x | - |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.643x | - |

- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now: `s-059`, 13,701.6 ns, 5,134 B; largest Δ: `s-057`, -29.0 ns (now 7,668.9 ns), 10,252 B
- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now: `s-059`, 13,706.2 ns, 5,134 B; largest Δ: `s-064`, -77.7 ns (now 10,582.4 ns), 4,110 B
- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-057`, 19,068.7 ns, 10,252 B; largest Δ: `s-060`, -29.2 ns (now 19,044.4 ns), 10,240 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now (also the largest Δ): `s-057`, 19,073.6 ns, 10,252 B

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | Δ vs previous version | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured@1.3 | `plain` | same program | 3,523.0 | 3,519.3 | 4,256.5 | 293.9 | 0.054x | 1.000x | - | 77 | 45.8 | 17.2 | 100% |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured@1.4 | `plain` | same program | 3,523.5 | 3,523.4 | 3,529.5 | 2.3 | 0.054x | 1.000x | unchanged (within spread) | 77 | 45.8 | 17.6 | 100% |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured@1.3 | `plain` | same program | 3,526.4 | 3,524.9 | 3,553.6 | 11.2 | 0.054x | 1.001x | - | 77 | 45.8 | 17.3 | 100% |
| 4 | `pcrec_1989c62_auto-caps-simdna` | measured@1.4 | `plain` | same program | 3,529.5 | 3,518.5 | 3,545.8 | 9.3 | 0.054x | 1.002x | unchanged (within spread) | 77 | 45.8 | 17.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured@1.4 | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.748x | - | 77 | 80.0 | 44.2 | 100% |
| 6 | `pcrec_1989c62_vm-caps-simdna` | measured@1.4 | `plain` | same program | 12,384.0 | 12,336.7 | 12,419.3 | 32.6 | 0.188x | 3.515x | faster ×1.01 | 77 | 160.8 | 13.7 | 100% |
| 7 | `pcrec_96e44c2_vm-caps-simdna` | measured@1.3 | `plain` | same program | 12,522.3 | 12,458.7 | 12,533.6 | 27.3 | 0.190x | 3.554x | - | 77 | 162.6 | 31.4 | 100% |
| 8 | `pcrec_96e44c2_vm-in-caps-simdna` | measured@1.3 | `plain` | same program | 12,826.9 | 12,818.1 | 12,870.4 | 19.0 | 0.195x | 3.641x | - | 77 | 166.6 | 31.7 | 100% |
| 9 | `pcrec_1989c62_vm-in-caps-simdna` | measured@1.4 | `plain` | same program | 12,893.3 | 12,802.8 | 13,527.0 | 269.1 | 0.196x | 3.660x | unchanged (within spread) | 77 | 167.4 | 13.6 | 100% |
| 10 | `libpcre2_10.46_interp-caps-simdna` | measured@1.4 | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.668x | - | 77 | 854.1 | 95.9 | 100% |

- Δ detail: `pcrec_1989c62_auto-nocaps-simdna` vs previous `pcrec_96e44c2_auto-nocaps-simdna`: worst now: `s-004`, 120.4 ns, 33 B; largest Δ: `s-082`, +1.4 ns (now 6.5 ns), 1 B
- Δ detail: `pcrec_1989c62_auto-caps-simdna` vs previous `pcrec_96e44c2_auto-caps-simdna`: worst now: `s-004`, 120.4 ns, 33 B; largest Δ: `s-069`, -1.3 ns (now 27.0 ns), 17 B
- Δ detail: `pcrec_1989c62_vm-caps-simdna` vs previous `pcrec_96e44c2_vm-caps-simdna`: worst now: `s-035`, 714.5 ns, 16 B; largest Δ: `s-038`, -22.6 ns (now 577.9 ns), 17 B
- Δ detail: `pcrec_1989c62_vm-in-caps-simdna` vs previous `pcrec_96e44c2_vm-in-caps-simdna`: worst now: `s-035`, 703.6 ns, 16 B; largest Δ: `s-077`, -31.9 ns (now 62.2 ns), 16 B

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_1989c62_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_1989c62_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_1989c62_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
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
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 164,915,127.0 | 156,981,861.0 | 182,641,919.0 | 8,625,738.7 | 5 | 43,344 | 82,314 | 13,620 | 0.052 | compiled=5 | 21,246,982.0 | 147,074,564.0 | 190,671.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 173,581,817.0 | 166,130,205.0 | 183,948,586.0 | 6,720,513.4 | 5 | 47,584 | 94,525 | 15,536 | 0.039 | compiled=5 | 12,067,839.0 | 161,425,557.0 | 109,531.0 |
| `factored` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 151,621,570.0 | 150,070,112.0 | 160,325,170.0 | 3,773,314.3 | 5 | 47,440 | 82,131 | 13,433 | 0.025 | compiled=5 | 10,169,728.0 | 140,530,217.0 | 114,060.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,328,764.0 | 154,959,980.0 | 186,417,630.0 | 10,113,724.8 | 5 | 47,584 | 94,342 | 15,349 | 0.059 (max is trial 1) | compiled=5 | 12,979,624.0 | 158,353,199.0 | 192,941.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 557,601,392.0 | 549,327,714.0 | 569,843,521.0 | 7,315,769.4 | 5 | 39,248 | 58,359 | 56,805 | 0.013 | compiled=5 | 2,524,514.0 | 554,883,877.0 | 193,001.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 565,207,216.0 | 558,228,695.0 | 571,057,819.0 | 4,268,779.8 | 5 | 39,248 | 58,475 | 56,921 | 0.008 | compiled=5 | 2,169,652.0 | 561,344,614.0 | 200,541.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 557,938,347.0 | 546,318,699.0 | 563,311,338.0 | 6,106,183.7 | 5 | 39,248 | 58,359 | 56,805 | 0.011 | compiled=5 | 2,326,253.0 | 555,627,603.0 | 108,241.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 561,136,606.0 | 549,125,744.0 | 565,607,772.0 | 5,693,701.3 | 5 | 39,248 | 58,475 | 56,921 | 0.010 | compiled=5 | 2,209,483.0 | 558,601,840.0 | 106,210.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 161,367,376.0 | 160,364,191.0 | 168,045,206.0 | 2,768,245.7 | 5 | 43,224 | 82,080 | 13,386 | 0.017 | compiled=5 | 9,593,116.0 | 150,683,764.0 | 199,961.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 173,642,569.0 | 162,000,350.0 | 195,343,764.0 | 11,832,867.7 | 5 | 47,464 | 94,291 | 15,302 | 0.068 (max is trial 1) | compiled=5 | 17,795,364.0 | 160,135,889.0 | 196,911.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 156,332,757.0 | 146,742,271.0 | 169,572,655.0 | 8,313,785.5 | 5 | 43,224 | 81,897 | 13,199 | 0.053 | compiled=5 | 9,544,566.0 | 146,686,991.0 | 187,602.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 169,353,324.0 | 158,336,598.0 | 175,847,071.0 | 6,277,917.7 | 5 | 47,464 | 94,108 | 15,115 | 0.037 | compiled=5 | 11,953,990.0 | 157,465,023.0 | 179,471.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 560,952,030.0 | 552,401,499.0 | 574,504,699.0 | 7,800,620.7 | 5 | 39,128 | 58,254 | 56,700 | 0.014 | compiled=5 | 2,163,513.0 | 558,645,066.0 | 198,721.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 561,262,931.0 | 553,920,967.0 | 566,432,401.0 | 4,509,880.6 | 5 | 39,128 | 58,370 | 56,816 | 0.008 | compiled=5 | 2,579,045.0 | 557,399,298.0 | 90,240.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 549,464,481.0 | 548,090,774.0 | 552,673,581.0 | 1,655,066.8 | 5 | 39,128 | 58,254 | 56,700 | 0.003 (max is trial 1) | compiled=5 | 2,182,383.0 | 545,859,350.0 | 188,261.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 568,066,400.0 | 554,524,271.0 | 569,803,801.0 | 5,749,619.0 | 5 | 39,128 | 58,370 | 56,816 | 0.010 | compiled=5 | 2,302,993.0 | 565,593,376.0 | 100,111.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 138,937,769.0 | 130,915,322.0 | 149,545,609.0 | 6,514,661.1 | 5 | 22,832 | 17,965 | 12,968 | 0.047 | compiled=5 | 1,809,261.0 | 137,082,487.0 | 189,661.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 149,982,771.0 | 145,127,543.0 | 155,552,133.0 | 3,491,085.5 | 5 | 22,968 | 20,308 | 14,985 | 0.023 | compiled=5 | 1,692,279.0 | 148,114,051.0 | 96,651.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 139,949,224.0 | 130,838,550.0 | 142,838,561.0 | 4,676,626.4 | 5 | 22,832 | 17,965 | 12,968 | 0.033 | compiled=5 | 1,653,409.0 | 136,240,052.0 | 109,170.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 148,273,931.0 | 141,076,649.0 | 152,803,577.0 | 4,745,842.6 | 5 | 22,968 | 20,308 | 14,985 | 0.032 | compiled=5 | 1,822,371.0 | 146,451,511.0 | 183,361.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 128,967,530.0 | 124,322,624.0 | 137,012,847.0 | 4,823,380.7 | 5 | 22,376 | 17,258 | 17,258 | 0.037 | compiled=5 | 1,429,138.0 | 127,548,612.0 | 182,731.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 137,382,550.0 | 121,509,347.0 | 142,162,417.0 | 7,505,540.6 | 5 | 22,376 | 17,369 | 17,369 | 0.055 | compiled=5 | 1,457,899.0 | 135,826,510.0 | 98,900.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 136,759,498.0 | 133,740,580.0 | 137,964,826.0 | 1,824,242.0 | 5 | 22,376 | 17,258 | 17,258 | 0.013 | compiled=5 | 1,467,469.0 | 135,122,328.0 | 196,311.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 136,344,905.0 | 128,201,518.0 | 141,820,418.0 | 5,034,770.1 | 5 | 22,376 | 17,369 | 17,369 | 0.037 | compiled=5 | 1,755,101.0 | 133,278,078.0 | 190,831.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 133,986,396.0 | 129,174,899.0 | 142,126,773.0 | 4,614,847.4 | 5 | 22,712 | 17,731 | 12,734 | 0.034 | compiled=5 | 1,734,020.0 | 132,040,485.0 | 188,771.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 147,942,328.0 | 144,005,944.0 | 154,591,887.0 | 3,790,768.5 | 5 | 22,856 | 20,074 | 14,751 | 0.026 | compiled=5 | 1,672,159.0 | 145,940,916.0 | 99,891.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 131,184,190.0 | 124,625,080.0 | 138,781,244.0 | 5,533,696.7 | 5 | 22,712 | 17,731 | 12,734 | 0.042 | compiled=5 | 1,680,810.0 | 129,391,839.0 | 117,511.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 149,578,517.0 | 143,713,063.0 | 151,059,906.0 | 2,757,231.6 | 5 | 22,856 | 20,074 | 14,751 | 0.018 | compiled=5 | 1,678,290.0 | 147,514,265.0 | 102,211.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 144,984,105.0 | 140,000,455.0 | 155,450,617.0 | 5,526,755.8 | 5 | 22,344 | 17,660 | 17,660 | 0.038 | compiled=5 | 1,620,700.0 | 143,173,954.0 | 186,041.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 149,400,661.0 | 140,726,940.0 | 152,597,870.0 | 4,214,821.7 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 1,528,869.0 | 147,835,302.0 | 106,611.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 143,038,783.0 | 142,028,867.0 | 152,074,138.0 | 3,847,908.1 | 5 | 22,344 | 17,660 | 17,660 | 0.027 | compiled=5 | 1,451,489.0 | 140,558,609.0 | 190,721.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 149,887,504.0 | 141,599,525.0 | 152,215,158.0 | 4,185,187.6 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 2,899,487.0 | 146,859,346.0 | 187,241.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-caps-simdna` | 156,626,339.0 | 152,463,315.0 | 162,571,233.0 | 3,827,137.0 | 5 | 43,304 | 81,907 | 13,380 | 0.024 | compiled=5 | 9,352,623.0 | 147,153,485.0 | 107,731.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-caps-simdna` | 169,897,296.0 | 158,601,931.0 | 180,453,986.0 | 7,594,084.9 | 5 | 47,544 | 94,118 | 15,296 | 0.045 (max is trial 1) | compiled=5 | 11,432,616.0 | 150,413,164.0 | 196,642.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 155,645,893.0 | 148,604,192.0 | 161,597,979.0 | 5,318,300.2 | 5 | 43,304 | 81,907 | 13,380 | 0.034 | compiled=5 | 9,623,285.0 | 139,588,191.0 | 112,860.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,558,255.0 | 168,392,047.0 | 174,796,025.0 | 2,301,945.8 | 5 | 47,544 | 94,118 | 15,296 | 0.013 | compiled=5 | 11,420,075.0 | 157,236,173.0 | 193,971.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 432,550,604.0 | 423,790,122.0 | 432,981,428.0 | 3,557,204.4 | 5 | 30,976 | 47,188 | 45,801 | 0.008 | compiled=5 | 1,953,732.0 | 430,495,102.0 | 115,240.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 432,168,521.0 | 409,864,175.0 | 439,547,864.0 | 11,267,008.2 | 5 | 30,976 | 47,306 | 45,919 | 0.026 | compiled=5 | 1,929,061.0 | 430,050,959.0 | 192,691.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 437,531,255.0 | 432,370,325.0 | 447,960,387.0 | 5,531,367.4 | 5 | 30,976 | 47,188 | 45,801 | 0.013 | compiled=5 | 2,042,772.0 | 433,210,960.0 | 188,701.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 429,579,968.0 | 421,616,232.0 | 432,505,467.0 | 3,830,835.1 | 5 | 30,976 | 47,306 | 45,919 | 0.009 | compiled=5 | 2,052,033.0 | 427,185,674.0 | 197,772.0 |
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
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 70,150.0 | 64,051.0 | 167,201.0 | 39,050.5 | 5 | 951 | 0.557 (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,351.0 | 5,120.0 | 51,820.0 | 18,281.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 59,880.0 | 54,300.0 | 175,181.0 | 46,340.9 | 5 | 1,609 | 0.774 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,450.0 | 13,070.0 | 50,681.0 | 14,528.5 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,470.0 | 6,041.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 33,290.0 | 30,010.0 | 102,420.0 | 27,822.1 | 5 | 1,609 | 0.836 (max is trial 1) | compiled=5 |

