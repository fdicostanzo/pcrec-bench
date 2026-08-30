# pcrec-bench report

reporter: v9 (2026-08-30)

## Query

- filters: subbench=email-specimen, version=0.2, since=2026-08-30T11:00:00Z
- record source: store/index.tsv (68 candidate file(s))
- records included: 6
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260830T131028Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T131859Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-caps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-caps-simdna__budu-ryzen1600__20260830T132955Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z` (store/records/email-specimen@0.2/pcrec_96e44c2_auto-nocaps-simdna/email-specimen@0.2__pcrec_96e44c2_auto-nocaps-simdna__budu-ryzen1600__20260830T133503Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-caps-simdna__budu-ryzen1600__20260830T134000Z.jsonl) — agreement: n/a (v1.3)
    - `email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z` (store/records/email-specimen@0.2/pcrec_96e44c2_vm-in-caps-simdna/email-specimen@0.2__pcrec_96e44c2_vm-in-caps-simdna__budu-ryzen1600__20260830T134650Z.jsonl) — agreement: n/a (v1.3)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.3
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.1-1.3 X13 (both samples quiet) on 6 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 13,595,834.2 | 2.5932 | 13,569,312.4 | 13,731,462.8 | 60,163.9 | 0.027x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 13,704,256.6 | 2.6139 | 13,685,839.0 | 13,749,076.2 | 21,250.8 | 0.027x | 1.008x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 499,942,662.6 | 95.3565 | 498,365,862.4 | 527,409,710.5 | 11,071,765.4 | 1.000x | 36.772x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,581,485.2 | 3.4156 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,588,937.2 | 3.4227 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,692,993.8 | 49.2983 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,891,541.7 | 1.8039 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,877,627.3 | 1.7906 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,417.0 | 0.0185 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,878,044.0 | 1.7910 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,184.2 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,842.9 | 0.0180 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,137,206.7 | 2.9919 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,198,130.0 | 3.0500 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 448,191,962.3 | 427.4292 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,099,418.9 | 2.9558 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,166,592.9 | 3.0199 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 19,569.1 | 0.0187 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,301.0 | 73,260.7 | 73,340.4 | 25.4 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,383.3 | 73,375.9 | 73,385.8 | 3.3 | 0.040x | 1.001x | 85 | 100% |
| 3 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 462,186.8 | 461,060.9 | 465,355.0 | 1,465.4 | 0.252x | 6.305x | 85 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,827,818.2 | 1,823,644.9 | 1,854,085.7 | 13,115.1 | 0.998x | 24.936x | 85 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,831,243.6 | 1,823,541.1 | 1,855,218.0 | 10,904.9 | 1.000x | 24.983x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,527.2 | 3,525.6 | 3,536.6 | 4.0 | 0.026x | 1.000x | 77 | 45.8 | 17.3 | 100% |
| 2 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,667.3 | 3,661.1 | 3,671.7 | 3.6 | 0.027x | 1.040x | 77 | 47.6 | 17.2 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,276.8 | 15,232.8 | 15,352.6 | 44.0 | 0.111x | 4.331x | 77 | 198.4 | 48.5 | 100% |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 53,906.8 | 53,710.9 | 54,238.1 | 182.2 | 0.391x | 15.283x | 77 | 700.1 | 31.4 | 100% |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 54,069.3 | 53,491.4 | 54,216.1 | 257.6 | 0.392x | 15.329x | 77 | 702.2 | 31.7 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,939.8 | 137,769.6 | 138,305.3 | 207.8 | 1.000x | 39.108x | 77 | 1,791.4 | 96.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 713,176.7 | 0.1360 | 711,858.4 | 719,884.4 | 2,872.0 | 0.193x | 1.000x | spread |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 713,484.5 | 0.1361 | 711,877.5 | 714,765.8 | 1,046.9 | 0.194x | 1.000x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,015,740.1 | 0.3845 | 1,880,816.0 | 2,092,105.9 | 79,225.2 | 0.547x | 2.826x | **dominated**: `t-a-valid-addrs` is 90.6% of this set |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,686,660.4 | 0.7032 | 3,674,751.8 | 3,726,701.6 | 20,583.2 | 1.000x | 5.169x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |
| 5 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 16,325,112.9 | 3.1138 | 15,821,062.7 | 16,573,878.5 | 308,141.1 | 4.428x | 22.891x | spread |
| 6 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 16,371,986.6 | 3.1227 | 16,299,110.1 | 16,640,133.5 | 120,554.5 | 4.441x | 22.956x | spread |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 628,684.2 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 628,731.1 | 0.5996 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,825,442.7 | 1.7409 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,563,281.1 | 3.3982 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,923,994.5 | 3.7422 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 4,012,120.3 | 3.8263 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,669.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,732.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,399.9 | 0.0376 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,809.6 | 0.0170 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,076,750.8 | 2.9342 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,047,388.0 | 2.9062 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,697.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,807.9 | 0.0380 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,798.9 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,799,563.2 | 2.6699 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 2,791,699.8 | 2.6624 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 30,981.7 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 30,939.0 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,985.7 | 0.0667 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,122.5 | 0.0669 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 3,337,656.4 | 3.1830 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,368,779.2 | 3.2127 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 17,695.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 17,734.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 40,399.3 | 0.0385 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,756.0 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-caps-simdna` | 2,941,908.1 | 2.8056 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_vm-in-caps-simdna` | 3,407,572.1 | 3.2497 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 685.4 | 685.0 | 686.2 | 0.4 | 0.266x | 1.000x |
| 2 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 782.6 | 781.7 | 786.7 | 1.8 | 0.303x | 1.142x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 831.4 | 827.5 | 835.1 | 3.0 | 0.322x | 1.213x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 834.1 | 827.3 | 839.7 | 4.1 | 0.323x | 1.217x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,579.4 | 2,569.9 | 3,062.9 | 194.7 | 1.000x | 3.763x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,580.2 | 2,574.8 | 2,606.9 | 11.5 | 1.000x | 3.765x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 1,327.8 | 1,326.3 | 1,330.6 | 1.6 | 0.178x | 1.000x | 77 | 17.2 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 1,329.7 | 1,328.5 | 1,346.0 | 6.7 | 0.178x | 1.001x | 77 | 17.3 | 100% |
| 3 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 2,418.7 | 2,413.7 | 2,422.0 | 2.7 | 0.324x | 1.822x | 77 | 31.4 | 100% |
| 4 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 2,438.3 | 2,435.6 | 2,451.1 | 5.7 | 0.327x | 1.836x | 77 | 31.7 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,733.5 | 3,398.3 | 4,226.3 | 302.0 | 0.500x | 2.812x | 77 | 48.5 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,462.0 | 7,347.7 | 7,607.0 | 93.6 | 1.000x | 5.620x | 77 | 96.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 13,607,713.5 | 2.5955 | 13,575,535.2 | 13,632,111.1 | 21,217.8 | 0.111x | 1.000x | 5 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 13,625,779.9 | 2.5989 | 13,583,858.4 | 13,632,604.3 | 20,133.9 | 0.111x | 1.001x | 5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,232,940.2 | 3.4777 | 18,157,667.8 | 18,459,450.8 | 117,430.0 | 0.149x | 1.340x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,773,449.3 | 23.4172 | 122,444,857.7 | 123,619,068.6 | 427,456.4 | 1.000x | 9.022x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,583,848.6 | 3.4178 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,587,388.5 | 3.4212 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,696,994.6 | 3.5257 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,821,951.8 | 27.4868 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,887,163.0 | 1.7997 |
| `t-b-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,886,284.8 | 1.7989 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,546,837.8 | 2.4289 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,092.5 | 0.0173 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 1,876,250.4 | 1.7893 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 1,875,774.8 | 1.7889 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,820,671.8 | 2.6900 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,005.5 | 0.0172 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,135,589.7 | 2.9903 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,148,674.1 | 3.0028 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,974,673.2 | 5.6979 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,897,422.0 | 89.5476 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-caps-simdna` | 3,095,070.0 | 2.9517 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_96e44c2_auto-nocaps-simdna` | 3,097,595.6 | 2.9541 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,166,813.3 | 3.0201 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,121.3 | 0.0173 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,301.2 | 62,260.8 | 63,740.2 | 578.8 | 0.117x | 1.000x |
| 2 | `pcrec_96e44c2_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,982.0 | 62,964.9 | 63,086.2 | 44.3 | 0.118x | 1.011x |
| 3 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,249.7 | 73,230.2 | 73,332.7 | 40.2 | 0.137x | 1.176x |
| 4 | `pcrec_96e44c2_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,272.4 | 73,248.6 | 73,457.8 | 78.3 | 0.137x | 1.176x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 533,938.1 | 533,459.3 | 534,573.8 | 431.6 | 1.000x | 8.570x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,007.8 | 533,632.1 | 535,269.5 | 601.9 | 1.000x | 8.571x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_96e44c2_auto-caps-simdna` | measured | `plain` | same program | 3,523.0 | 3,519.3 | 4,256.5 | 293.9 | 0.054x | 1.000x | 77 | 45.8 | 17.2 | 100% |
| 2 | `pcrec_96e44c2_auto-nocaps-simdna` | measured | `plain` | same program | 3,526.4 | 3,524.9 | 3,553.6 | 11.2 | 0.054x | 1.001x | 77 | 45.8 | 17.3 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,144.2 | 6,121.5 | 6,233.4 | 42.1 | 0.093x | 1.744x | 77 | 79.8 | 48.5 | 100% |
| 4 | `pcrec_96e44c2_vm-caps-simdna` | measured | `plain` | same program | 12,522.3 | 12,458.7 | 12,533.6 | 27.3 | 0.190x | 3.554x | 77 | 162.6 | 31.4 | 100% |
| 5 | `pcrec_96e44c2_vm-in-caps-simdna` | measured | `plain` | same program | 12,826.9 | 12,818.1 | 12,870.4 | 19.0 | 0.195x | 3.641x | 77 | 166.6 | 31.7 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,845.8 | 65,550.6 | 67,991.3 | 905.8 | 1.000x | 18.690x | 77 | 855.1 | 96.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
| `factored` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 161,367,376.0 | 160,364,191.0 | 168,045,206.0 | 2,768,245.7 | 5 | 43,224 | 82,080 | 13,386 | 0.017 | compiled=5 | 9,593,116.0 | 150,683,764.0 | 199,961.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 173,642,569.0 | 162,000,350.0 | 195,343,764.0 | 11,832,867.7 | 5 | 47,464 | 94,291 | 15,302 | 0.068 (max is trial 1) | compiled=5 | 17,795,364.0 | 160,135,889.0 | 196,911.0 |
| `factored` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 156,332,757.0 | 146,742,271.0 | 169,572,655.0 | 8,313,785.5 | 5 | 43,224 | 81,897 | 13,199 | 0.053 | compiled=5 | 9,544,566.0 | 146,686,991.0 | 187,602.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 169,353,324.0 | 158,336,598.0 | 175,847,071.0 | 6,277,917.7 | 5 | 47,464 | 94,108 | 15,115 | 0.037 | compiled=5 | 11,953,990.0 | 157,465,023.0 | 179,471.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 560,952,030.0 | 552,401,499.0 | 574,504,699.0 | 7,800,620.7 | 5 | 39,128 | 58,254 | 56,700 | 0.014 | compiled=5 | 2,163,513.0 | 558,645,066.0 | 198,721.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 561,262,931.0 | 553,920,967.0 | 566,432,401.0 | 4,509,880.6 | 5 | 39,128 | 58,370 | 56,816 | 0.008 | compiled=5 | 2,579,045.0 | 557,399,298.0 | 90,240.0 |
| `factored` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 549,464,481.0 | 548,090,774.0 | 552,673,581.0 | 1,655,066.8 | 5 | 39,128 | 58,254 | 56,700 | 0.003 (max is trial 1) | compiled=5 | 2,182,383.0 | 545,859,350.0 | 188,261.0 |
| `factored` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 568,066,400.0 | 554,524,271.0 | 569,803,801.0 | 5,749,619.0 | 5 | 39,128 | 58,370 | 56,816 | 0.010 | compiled=5 | 2,302,993.0 | 565,593,376.0 | 100,111.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-caps-simdna` | 133,986,396.0 | 129,174,899.0 | 142,126,773.0 | 4,614,847.4 | 5 | 22,712 | 17,731 | 12,734 | 0.034 | compiled=5 | 1,734,020.0 | 132,040,485.0 | 188,771.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-caps-simdna` | 147,942,328.0 | 144,005,944.0 | 154,591,887.0 | 3,790,768.5 | 5 | 22,856 | 20,074 | 14,751 | 0.026 | compiled=5 | 1,672,159.0 | 145,940,916.0 | 99,891.0 |
| `floor` | `plain` | `pcrec_96e44c2_auto-nocaps-simdna` | 131,184,190.0 | 124,625,080.0 | 138,781,244.0 | 5,533,696.7 | 5 | 22,712 | 17,731 | 12,734 | 0.042 | compiled=5 | 1,680,810.0 | 129,391,839.0 | 117,511.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_auto-nocaps-simdna` | 149,578,517.0 | 143,713,063.0 | 151,059,906.0 | 2,757,231.6 | 5 | 22,856 | 20,074 | 14,751 | 0.018 | compiled=5 | 1,678,290.0 | 147,514,265.0 | 102,211.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-caps-simdna` | 144,984,105.0 | 140,000,455.0 | 155,450,617.0 | 5,526,755.8 | 5 | 22,344 | 17,660 | 17,660 | 0.038 | compiled=5 | 1,620,700.0 | 143,173,954.0 | 186,041.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-caps-simdna` | 149,400,661.0 | 140,726,940.0 | 152,597,870.0 | 4,214,821.7 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 1,528,869.0 | 147,835,302.0 | 106,611.0 |
| `floor` | `plain` | `pcrec_96e44c2_vm-in-caps-simdna` | 143,038,783.0 | 142,028,867.0 | 152,074,138.0 | 3,847,908.1 | 5 | 22,344 | 17,660 | 17,660 | 0.027 | compiled=5 | 1,451,489.0 | 140,558,609.0 | 190,721.0 |
| `floor` | `whole-subject` | `pcrec_96e44c2_vm-in-caps-simdna` | 149,887,504.0 | 141,599,525.0 | 152,215,158.0 | 4,185,187.6 | 5 | 22,344 | 17,771 | 17,771 | 0.028 | compiled=5 | 2,899,487.0 | 146,859,346.0 | 187,241.0 |
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

