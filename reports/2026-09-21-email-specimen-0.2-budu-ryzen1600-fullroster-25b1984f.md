# pcrec-bench report

reporter: v24 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-09-21T14:30:16Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_25b1984f_auto-caps-simdna, testee=pcrec_25b1984f_auto-nocaps-simdna, testee=pcrec_25b1984f_vm-caps-simdna, testee=pcrec_25b1984f_vm-in-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (14 record(s) matching this query)
- records included: 7
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-caps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-caps-simdna__budu-ryzen1600__20260921T065926Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z` (store/records/email-specimen@0.2/pcrec_25b1984f_auto-nocaps-simdna/email-specimen@0.2__pcrec_25b1984f_auto-nocaps-simdna__budu-ryzen1600__20260921T070439Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-caps-simdna__budu-ryzen1600__20260921T070947Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z` (store/records/email-specimen@0.2/pcrec_25b1984f_vm-in-caps-simdna/email-specimen@0.2__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__20260921T071628Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.6
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 7 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,255,555.6 | 2.7190 | 14,236,565.6 | 14,364,717.5 | 46,979.9 | 0.029x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 34.978x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,287.4 | 3.9513 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,632.0 | 1.7887 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,876,063.9 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,195,106.6 | 3.0471 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,151,717.6 | 3.0057 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,325.7 | 73,269.7 | 73,444.6 | 66.8 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 457,848.2 | 455,596.2 | 489,129.2 | 12,830.0 | 0.250x | 6.244x | 85 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.024x | 85 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.198x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,670.8 | 3,668.1 | 3,681.0 | 5.0 | 0.027x | 1.000x | 77 | 47.7 | 17.7 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.163x | 77 | 198.4 | 44.2 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 54,452.0 | 54,248.9 | 56,967.5 | 1,019.2 | 0.395x | 14.834x | 77 | 707.2 | 13.6 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 54,809.4 | 53,700.0 | 55,505.3 | 584.0 | 0.397x | 14.931x | 77 | 711.8 | 12.5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 37.576x | 77 | 1,791.4 | 95.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 971,431.9 | 0.1853 | 966,721.2 | 983,955.1 | 6,153.0 | 0.262x | 1.000x | **dominated**: `t-a-valid-addrs` is 91.1% of this set |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 1.974x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,319,613.0 | 0.6332 | 3,307,904.0 | 3,351,862.1 | 14,745.7 | 0.895x | 3.417x | spread |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,351,449.5 | 0.6392 | 3,340,220.9 | 3,389,538.2 | 17,693.1 | 0.904x | 3.450x | spread |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 3.818x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 881,323.3 | 0.8405 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 817,493.5 | 0.7796 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 855,355.9 | 0.8157 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,701.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,919.4 | 0.5922 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,441.9 | 0.5917 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,683.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,386.8 | 0.5916 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,408.6 | 0.5917 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 33,341.7 | 0.0318 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 632,526.5 | 0.6032 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 630,340.5 | 0.6011 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,686.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,430.1 | 0.5917 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,977.6 | 0.5922 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.6 | 484.2 | 487.9 | 1.3 | 0.189x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 505.8 | 505.7 | 507.1 | 0.5 | 0.197x | 1.042x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 882.2 | 858.7 | 896.2 | 13.5 | 0.343x | 1.817x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 5.290x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 5.304x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 961.4 | 954.9 | 967.1 | 4.0 | 0.130x | 1.000x | 77 | 12.5 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,043.4 | 1,039.8 | 1,045.4 | 1.8 | 0.141x | 1.085x | 77 | 13.6 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,364.3 | 1,362.9 | 1,367.5 | 1.5 | 0.185x | 1.419x | 77 | 17.7 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 3.538x | 77 | 44.2 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 7.684x | 77 | 95.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,131,365.5 | 2.6953 | 14,105,993.7 | 14,195,054.8 | 31,617.7 | 0.115x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.287x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 8.682x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,067.6 | 3.9511 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,886,626.1 | 1.7992 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,434.8 | 1.7886 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,132,783.4 | 2.9877 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,083,466.1 | 2.9406 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,071.9 | 62,030.4 | 62,228.5 | 74.3 | 0.116x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,899.6 | 62,741.4 | 62,971.2 | 84.0 | 0.117x | 1.013x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,231.8 | 73,200.7 | 73,340.4 | 51.8 | 0.136x | 1.180x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.607x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.657x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,522.1 | 3,518.8 | 3,594.9 | 29.6 | 0.054x | 1.000x | 77 | 45.7 | 17.7 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.748x | 77 | 80.0 | 44.2 | 100% |
| 3 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,764.0 | 12,666.2 | 12,851.3 | 65.7 | 0.194x | 3.624x | 77 | 165.8 | 13.6 | 100% |
| 4 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,831.4 | 12,810.0 | 12,886.0 | 27.0 | 0.195x | 3.643x | 77 | 166.6 | 12.5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.673x | 77 | 854.1 | 95.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,136,501.8 | 2.6963 | 14,121,185.8 | 14,178,147.4 | 19,152.4 | 1.000x | 1.000x |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,140,798.8 | 3.9490 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,881,351.0 | 1.7942 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,875,092.7 | 1.7882 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,142,816.5 | 2.9972 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,098,133.9 | 2.9546 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,250.8 | 73,186.0 | 73,340.5 | 49.3 | 1.000x | 1.000x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.3 | 3,518.7 | 3,564.8 | 16.9 | 1.000x | 1.000x | 77 | 45.8 | 17.8 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 1.000x | 1.000x | spread |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 967,321.1 | 0.1845 | 966,348.4 | 973,089.8 | 2,487.4 | 1.138x | 1.138x | **dominated**: `t-a-valid-addrs` is 91.1% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 880,810.7 | 0.8400 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,761.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,695.8 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 33,253.8 | 0.0317 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,679.2 | 0.0169 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 874.7 | 864.8 | 887.5 | 7.5 | 1.477x | 1.477x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,370.4 | 1,367.6 | 1,374.0 | 2.2 | 1.000x | 1.000x | 77 | 17.8 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 3.714x | 3.714x | 77 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 1.000x | 1.000x |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,138,384.1 | 2.6967 | 14,117,417.0 | 14,178,994.4 | 22,669.4 | 1.016x | 1.016x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,145,504.2 | 3.9535 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,888,425.7 | 1.8009 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,874,718.0 | 1.7879 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,137,025.9 | 2.9917 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,094,842.2 | 2.9515 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,267.0 | 73,211.0 | 73,343.4 | 53.1 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 1.655x | 1.655x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_25b1984f_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.6 | 3,521.7 | 3,548.6 | 12.1 | 1.000x | 1.000x | 77 | 45.8 | 17.8 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 3.551x | 3.551x | 77 | 162.6 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,136,501.8 | 2.6963 | 14,121,185.8 | 14,178,147.4 | 19,152.4 | 0.028x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,255,555.6 | 2.7190 | 14,236,565.6 | 14,364,717.5 | 46,979.9 | 0.029x | 1.008x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 35.272x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,140,798.8 | 3.9490 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,287.4 | 3.9513 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,881,351.0 | 1.7942 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,632.0 | 1.7887 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,875,092.7 | 1.7882 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,876,063.9 | 1.7892 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,142,816.5 | 2.9972 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,195,106.6 | 3.0471 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,098,133.9 | 2.9546 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,151,717.6 | 3.0057 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,250.8 | 73,186.0 | 73,340.5 | 49.3 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,325.7 | 73,269.7 | 73,444.6 | 66.8 | 0.040x | 1.001x | 85 | 100% |
| 3 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 457,848.2 | 455,596.2 | 489,129.2 | 12,830.0 | 0.250x | 6.250x | 85 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.050x | 85 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.224x | 85 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.3 | 3,518.7 | 3,564.8 | 16.9 | 0.026x | 1.000x | 77 | 45.8 | 17.8 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,670.8 | 3,668.1 | 3,681.0 | 5.0 | 0.027x | 1.041x | 77 | 47.7 | 17.7 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.334x | 77 | 198.4 | 44.2 | 100% |
| 4 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 54,452.0 | 54,248.9 | 56,967.5 | 1,019.2 | 0.395x | 15.446x | 77 | 707.2 | 13.6 | 100% |
| 5 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 54,809.4 | 53,700.0 | 55,505.3 | 584.0 | 0.397x | 15.548x | 77 | 711.8 | 12.5 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 39.128x | 77 | 1,791.4 | 95.9 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 0.229x | 1.000x | spread |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 967,321.1 | 0.1845 | 966,348.4 | 973,089.8 | 2,487.4 | 0.261x | 1.138x | **dominated**: `t-a-valid-addrs` is 91.1% of this set |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 971,431.9 | 0.1853 | 966,721.2 | 983,955.1 | 6,153.0 | 0.262x | 1.142x | **dominated**: `t-a-valid-addrs` is 91.1% of this set |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.255x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 3,319,613.0 | 0.6332 | 3,307,904.0 | 3,351,862.1 | 14,745.7 | 0.895x | 3.904x | spread |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 3,351,449.5 | 0.6392 | 3,340,220.9 | 3,389,538.2 | 17,693.1 | 0.904x | 3.941x | spread |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 4.362x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 880,810.7 | 0.8400 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 881,323.3 | 0.8405 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 817,493.5 | 0.7796 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 855,355.9 | 0.8157 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,761.2 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,701.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,919.4 | 0.5922 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,441.9 | 0.5917 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,695.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,683.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,386.8 | 0.5916 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,408.6 | 0.5917 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 33,253.8 | 0.0317 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 33,341.7 | 0.0318 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 632,526.5 | 0.6032 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 630,340.5 | 0.6011 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 17,679.2 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 17,686.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-caps-simdna` | 620,430.1 | 0.5917 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_vm-in-caps-simdna` | 620,977.6 | 0.5922 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 485.6 | 484.2 | 487.9 | 1.3 | 0.189x | 1.000x |
| 2 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 505.8 | 505.7 | 507.1 | 0.5 | 0.197x | 1.042x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 0.231x | 1.220x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 874.7 | 864.8 | 887.5 | 7.5 | 0.341x | 1.801x |
| 5 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 882.2 | 858.7 | 896.2 | 13.5 | 0.343x | 1.817x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 5.290x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 5.304x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 961.4 | 954.9 | 967.1 | 4.0 | 0.130x | 1.000x | 77 | 12.5 | 100% |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 1,043.4 | 1,039.8 | 1,045.4 | 1.8 | 0.141x | 1.085x | 77 | 13.6 | 100% |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 1,364.3 | 1,362.9 | 1,367.5 | 1.5 | 0.185x | 1.419x | 77 | 17.7 | 100% |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 1,370.4 | 1,367.6 | 1,374.0 | 2.2 | 0.185x | 1.425x | 77 | 17.8 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 3.538x | 77 | 44.2 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 0.689x | 5.293x | 77 | 66.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 7.684x | 77 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 0.113x | 1.000x | 5 | 100% |
| 2 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 14,131,365.5 | 2.6953 | 14,105,993.7 | 14,195,054.8 | 31,617.7 | 0.115x | 1.016x | 5 | 100% |
| 3 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 14,138,384.1 | 2.6967 | 14,117,417.0 | 14,178,994.4 | 22,669.4 | 0.115x | 1.016x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.307x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 8.818x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 4,143,067.6 | 3.9511 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 4,145,504.2 | 3.9535 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,886,626.1 | 1.7992 |
| `t-b-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,888,425.7 | 1.8009 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 1,875,434.8 | 1.7886 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 1,874,718.0 | 1.7879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,132,783.4 | 2.9877 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,137,025.9 | 2.9917 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-caps-simdna` | 3,083,466.1 | 2.9406 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_25b1984f_auto-nocaps-simdna` | 3,094,842.2 | 2.9515 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,071.9 | 62,030.4 | 62,228.5 | 74.3 | 0.116x | 1.000x |
| 2 | `pcrec_25b1984f_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,899.6 | 62,741.4 | 62,971.2 | 84.0 | 0.117x | 1.013x |
| 3 | `pcrec_25b1984f_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,231.8 | 73,200.7 | 73,340.4 | 51.8 | 0.136x | 1.180x |
| 4 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,267.0 | 73,211.0 | 73,343.4 | 53.1 | 0.136x | 1.180x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 0.226x | 1.954x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.607x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.657x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_25b1984f_auto-caps-simdna` | measured | `plain` | same program | 3,522.1 | 3,518.8 | 3,594.9 | 29.6 | 0.054x | 1.000x | 77 | 45.7 | 17.7 | 100% |
| 2 | `pcrec_25b1984f_auto-nocaps-simdna` | measured | `plain` | same program | 3,525.6 | 3,521.7 | 3,548.6 | 12.1 | 0.054x | 1.001x | 77 | 45.8 | 17.8 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.748x | 77 | 80.0 | 44.2 | 100% |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 0.190x | 3.555x | 77 | 162.6 | 66.1 | 100% |
| 5 | `pcrec_25b1984f_vm-caps-simdna` | measured | `plain` | same program | 12,764.0 | 12,666.2 | 12,851.3 | 65.7 | 0.194x | 3.624x | 77 | 165.8 | 13.6 | 100% |
| 6 | `pcrec_25b1984f_vm-in-caps-simdna` | measured | `plain` | same program | 12,831.4 | 12,810.0 | 12,886.0 | 27.0 | 0.195x | 3.643x | 77 | 166.6 | 12.5 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.673x | 77 | 854.1 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**10 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `floor` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 874.7 | `pcrec_25b1984f_vm-caps-simdna` | 485.6 | 0.555x | clears IQR only: gap 44.49%; IQR 0.74% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 874.7 | `pcrec_25b1984f_vm-in-caps-simdna` | 505.8 | 0.578x | clears IQR only: gap 42.18%; IQR 0.74% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_auto-caps-simdna` | 1,364.3 | 0.996x | clears IQR only: gap 0.44%; IQR 0.22% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_vm-caps-simdna` | 1,043.4 | 0.761x | clears IQR only: gap 23.86%; IQR 0.22% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 1,370.4 | `pcrec_25b1984f_vm-in-caps-simdna` | 961.4 | 0.702x | clears IQR only: gap 29.84%; IQR 0.22% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `large-subject-throughput` | `pcrec_25b1984f_auto-nocaps-simdna` | 14,138,384.1 | `pcrec_25b1984f_auto-caps-simdna` | 14,131,365.5 | 1.000x | within IQR: gap 0.05%; IQR 0.25% (within); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_auto-caps-simdna` | 73,231.8 | 1.000x | within IQR: gap 0.05%; IQR 0.14% (within); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_vm-caps-simdna` | 62,899.6 | 0.858x | clears IQR only: gap 14.15%; IQR 0.16% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_25b1984f_auto-nocaps-simdna` | 73,267.0 | `pcrec_25b1984f_vm-in-caps-simdna` | 62,071.9 | 0.847x | clears IQR only: gap 15.28%; IQR 0.14% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `short-subject-search` | `pcrec_25b1984f_auto-nocaps-simdna` | 3,525.6 | `pcrec_25b1984f_auto-caps-simdna` | 3,522.1 | 0.999x | within IQR: gap 0.10%; IQR 0.70% (within); no null band (no cross-pin pair in this report) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_25b1984f_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,526,814.0 | 164,766,687.0 | 181,490,745.0 | 6,338,789.0 | 5 | 48,128 | 82,643 | 13,949 | 0.037 (max is trial 1) | compiled=5 | 10,395,046.0 | 160,879,176.0 | 189,471.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 186,029,821.0 | 170,466,739.0 | 206,000,837.0 | 11,357,854.9 | 5 | 48,264 | 94,854 | 15,865 | 0.061 | compiled=5 | 12,996,749.0 | 172,858,711.0 | 174,361.0 |
| `factored` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 168,681,429.0 | 156,403,863.0 | 181,503,177.0 | 8,812,007.3 | 5 | 48,128 | 82,460 | 13,762 | 0.052 (max is trial 1) | compiled=5 | 10,525,176.0 | 156,384,723.0 | 189,021.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 181,271,647.0 | 178,884,604.0 | 182,453,363.0 | 1,282,469.9 | 5 | 48,264 | 94,671 | 15,678 | 0.007 (max is trial 1) | compiled=5 | 12,978,020.0 | 166,770,179.0 | 110,180.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 571,637,701.0 | 557,575,008.0 | 575,374,422.0 | 6,300,976.6 | 5 | 39,936 | 58,762 | 57,208 | 0.011 | compiled=5 | 2,270,593.0 | 566,253,219.0 | 193,121.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 566,462,271.0 | 562,968,250.0 | 594,057,801.0 | 12,339,418.7 | 5 | 39,936 | 58,878 | 57,324 | 0.022 | compiled=5 | 4,766,337.0 | 561,527,712.0 | 92,481.0 |
| `factored` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,406,753.0 | 560,698,170.0 | 588,568,428.0 | 9,061,480.9 | 5 | 39,936 | 58,762 | 57,208 | 0.016 | compiled=5 | 2,286,311.0 | 570,885,651.0 | 195,401.0 |
| `factored` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 573,429,854.0 | 568,076,198.0 | 577,436,234.0 | 3,411,473.3 | 5 | 39,936 | 58,878 | 57,324 | 0.006 | compiled=5 | 2,301,011.0 | 571,018,422.0 | 110,421.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 150,392,660.0 | 141,045,572.0 | 152,132,871.0 | 3,925,733.9 | 5 | 27,608 | 18,294 | 13,297 | 0.026 | compiled=5 | 1,681,089.0 | 148,544,911.0 | 113,721.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 159,682,441.0 | 152,028,068.0 | 176,186,068.0 | 8,194,139.2 | 5 | 27,752 | 20,637 | 15,314 | 0.051 | compiled=5 | 1,710,609.0 | 155,587,679.0 | 187,651.0 |
| `floor` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 147,937,338.0 | 140,196,106.0 | 153,161,896.0 | 4,472,283.5 | 5 | 27,608 | 18,294 | 13,297 | 0.030 | compiled=5 | 1,665,219.0 | 146,008,117.0 | 98,841.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 159,648,271.0 | 149,105,894.0 | 164,562,937.0 | 5,277,252.6 | 5 | 27,752 | 20,637 | 15,314 | 0.033 | compiled=5 | 1,797,069.0 | 157,121,978.0 | 187,311.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 134,754,625.0 | 125,109,458.0 | 141,177,793.0 | 6,732,611.9 | 5 | 23,072 | 17,837 | 17,837 | 0.050 | compiled=5 | 1,447,328.0 | 133,138,416.0 | 107,971.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 137,947,814.0 | 128,667,100.0 | 144,615,432.0 | 5,824,084.4 | 5 | 23,072 | 17,948 | 17,948 | 0.042 | compiled=5 | 1,440,808.0 | 136,275,634.0 | 105,560.0 |
| `floor` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 136,660,116.0 | 131,490,790.0 | 142,668,874.0 | 4,334,978.6 | 5 | 23,072 | 17,837 | 17,837 | 0.032 | compiled=5 | 1,643,548.0 | 133,541,640.0 | 192,511.0 |
| `floor` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 133,836,271.0 | 129,480,890.0 | 139,214,469.0 | 4,000,255.9 | 5 | 23,072 | 17,948 | 17,948 | 0.030 (max is trial 1) | compiled=5 | 1,446,067.0 | 132,247,174.0 | 187,101.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-caps-simdna` | 173,309,253.0 | 165,686,853.0 | 178,341,950.0 | 4,878,175.1 | 5 | 48,088 | 82,236 | 13,709 | 0.028 | compiled=5 | 9,909,873.0 | 156,121,711.0 | 185,431.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-caps-simdna` | 183,255,716.0 | 172,385,108.0 | 186,693,395.0 | 4,956,690.6 | 5 | 48,224 | 94,447 | 15,625 | 0.027 (max is trial 1) | compiled=5 | 12,300,625.0 | 167,948,045.0 | 116,710.0 |
| `orig` | `plain` | `pcrec_25b1984f_auto-nocaps-simdna` | 179,676,289.0 | 159,232,408.0 | 190,602,777.0 | 12,059,362.9 | 5 | 48,088 | 82,236 | 13,709 | 0.067 (max is trial 1) | compiled=5 | 12,042,185.0 | 166,726,229.0 | 186,401.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_auto-nocaps-simdna` | 180,355,242.0 | 172,212,788.0 | 196,159,277.0 | 7,844,183.0 | 5 | 48,224 | 94,447 | 15,625 | 0.043 (max is trial 1) | compiled=5 | 12,109,145.0 | 166,968,820.0 | 190,301.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-caps-simdna` | 446,696,252.0 | 442,685,129.0 | 449,710,861.0 | 2,531,966.7 | 5 | 35,760 | 47,591 | 46,204 | 0.006 (max is trial 1) | compiled=5 | 3,780,542.0 | 442,800,800.0 | 190,731.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-caps-simdna` | 439,876,962.0 | 429,616,723.0 | 446,978,854.0 | 5,741,717.6 | 5 | 35,760 | 47,709 | 46,322 | 0.013 (max is trial 1) | compiled=5 | 2,021,122.0 | 437,670,750.0 | 105,661.0 |
| `orig` | `plain` | `pcrec_25b1984f_vm-in-caps-simdna` | 439,646,101.0 | 432,618,487.0 | 448,206,325.0 | 5,990,601.0 | 5 | 35,760 | 47,591 | 46,204 | 0.014 | compiled=5 | 2,315,571.0 | 435,607,032.0 | 109,971.0 |
| `orig` | `whole-subject` | `pcrec_25b1984f_vm-in-caps-simdna` | 438,950,479.0 | 438,450,046.0 | 441,788,012.0 | 1,181,345.0 | 5 | 35,760 | 47,709 | 46,322 | 0.003 | compiled=5 | 2,027,140.0 | 436,816,828.0 | 109,560.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 70,150.0 | 64,051.0 | 167,201.0 | 39,050.5 | 5 | 951 | 0.557 (max is trial 1) | compiled=5 |
| `factored` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `factored` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 6,351.0 | 5,120.0 | 51,820.0 | 18,281.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `rust_1.13.1_default-caps-simdna` | 3,950.0 | 1,680.0 | 176,891.0 | 69,576.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 11,350.0 | 8,290.0 | 204,572.0 | 76,971.9 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 59,880.0 | 54,300.0 | 175,181.0 | 46,340.9 | 5 | 1,609 | 0.774 (max is trial 1) | compiled=5 |
| `orig` | `plain` | `rust_1.13.1_default-caps-simdna` | 409,433.0 | 376,542.0 | 954,257.0 | 220,856.8 | 5 | - | 0.539 (max is trial 1) | compiled=5 |
| `orig` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 141,981.0 | 119,361.0 | 388,192.0 | 102,003.0 | 5 | - | 0.718 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 14,450.0 | 13,070.0 | 50,681.0 | 14,528.5 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 310.0 | 15,470.0 | 6,041.3 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 33,290.0 | 30,010.0 | 102,420.0 | 27,822.1 | 5 | 1,609 | 0.836 (max is trial 1) | compiled=5 |

