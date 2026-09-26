# pcrec-bench report

reporter: v24 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, until=2026-09-21T03:25:41Z, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=pcrec_d34c9131_auto-caps-simdna, testee=pcrec_1989c62_auto-nocaps-simdna, testee=pcrec_1989c62_vm-caps-simdna, testee=pcrec_1989c62_vm-in-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (14 record(s) matching this query)
- records included: 7
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z` (store/records/email-specimen@0.2/pcrec_1989c62_auto-nocaps-simdna/email-specimen@0.2__pcrec_1989c62_auto-nocaps-simdna__budu-ryzen1600__20260902T081837Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-caps-simdna__budu-ryzen1600__20260902T082347Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 490 rows; 11 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z` (store/records/email-specimen@0.2/pcrec_1989c62_vm-in-caps-simdna/email-specimen@0.2__pcrec_1989c62_vm-in-caps-simdna__budu-ryzen1600__20260902T082959Z.jsonl) — agreement: agree (0 of 8 groups; 0 of 495 rows; 6 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z` (store/records/email-specimen@0.2/pcrec_d34c9131_auto-caps-simdna/email-specimen@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__20260906T190251Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.5, 1.6
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
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,676,206.1 | 2.6085 | 13,658,410.5 | 13,740,603.5 | 31,219.0 | 0.027x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 36.460x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,586,692.1 | 3.4205 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,347.2 | 1.7885 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,174.1 | 1.7883 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,192,965.9 | 3.0450 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,152,957.6 | 3.0069 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,303.5 | 73,290.6 | 73,322.0 | 11.5 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 461,165.2 | 455,738.7 | 466,627.4 | 3,547.8 | 0.251x | 6.291x | 85 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.032x | 85 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.206x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,662.4 | 3,660.4 | 3,669.2 | 3.1 | 0.027x | 1.000x | 77 | 47.6 | 17.4 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.172x | 77 | 198.4 | 44.2 | 100% |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 53,848.7 | 53,614.7 | 54,626.5 | 355.7 | 0.390x | 14.703x | 77 | 699.3 | 13.7 | 100% |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 53,902.2 | 53,519.5 | 54,707.0 | 391.5 | 0.391x | 14.718x | 77 | 700.0 | 13.6 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 37.663x | 77 | 1,791.4 | 95.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 713,690.6 | 0.1361 | 711,392.5 | 714,486.3 | 1,256.0 | 0.192x | 1.000x | spread |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,832,899.2 | 0.3496 | 1,831,518.1 | 1,847,785.7 | 7,649.4 | 0.494x | 2.568x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.686x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,920,640.2 | 0.3663 | 1,905,569.9 | 1,965,206.8 | 22,635.0 | 0.518x | 2.691x | spread |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.197x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 628,059.0 | 0.5990 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 581,707.3 | 0.5548 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 658,242.3 | 0.6277 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,667.6 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,113.4 | 0.2957 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,324.2 | 0.2959 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,117.0 | 0.2958 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,392.8 | 0.2960 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 30,949.2 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 320,961.8 | 0.3061 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 322,506.7 | 0.3076 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,671.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,051.9 | 0.2957 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,488.9 | 0.2961 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 432.9 | 431.7 | 434.5 | 1.0 | 0.169x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 516.6 | 516.4 | 517.7 | 0.5 | 0.201x | 1.193x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 870.5 | 858.7 | 887.1 | 10.0 | 0.339x | 2.011x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 5.934x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 5.950x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,045.1 | 1,043.2 | 1,047.9 | 1.6 | 0.141x | 1.000x | 77 | 13.6 | 100% |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,057.6 | 1,054.3 | 1,058.3 | 1.4 | 0.143x | 1.012x | 77 | 13.7 | 100% |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,338.1 | 1,337.9 | 1,348.7 | 4.3 | 0.181x | 1.280x | 77 | 17.4 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 3.254x | 77 | 44.2 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 7.069x | 77 | 95.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,596,186.2 | 2.5933 | 13,552,434.1 | 13,627,695.7 | 29,055.1 | 0.111x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.338x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 9.024x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,578,393.8 | 3.4126 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,885,944.5 | 1.7986 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,874,971.6 | 1.7881 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,154,491.2 | 3.0084 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,095,320.2 | 2.9519 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,176.3 | 62,132.6 | 62,239.1 | 35.5 | 0.116x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,809.0 | 62,698.2 | 63,185.7 | 168.0 | 0.117x | 1.010x |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,208.6 | 73,199.3 | 73,292.6 | 34.9 | 0.136x | 1.177x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.593x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.643x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,527.0 | 3,524.4 | 3,541.1 | 5.9 | 0.054x | 1.000x | 77 | 45.8 | 17.4 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.746x | 77 | 80.0 | 44.2 | 100% |
| 3 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12,384.0 | 12,336.7 | 12,419.3 | 32.6 | 0.188x | 3.511x | 77 | 160.8 | 13.7 | 100% |
| 4 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 12,893.3 | 12,802.8 | 13,527.0 | 269.1 | 0.196x | 3.656x | 77 | 167.4 | 13.6 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.647x | 77 | 854.1 | 95.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 13,583,640.9 | 2.5909 | 13,563,234.4 | 13,588,319.8 | 9,475.1 | 1.000x | 1.000x |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,581,417.1 | 3.4155 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,881,379.0 | 1.7942 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,877,090.2 | 1.7901 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,149,477.5 | 3.0036 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,092,666.6 | 2.9494 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,179.2 | 73,161.2 | 73,330.5 | 63.1 | 1.000x | 1.000x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,524.4 | 3,519.8 | 3,602.1 | 31.7 | 1.000x | 1.000x | 77 | 45.8 | 17.6 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 711,171.0 | 0.1356 | 710,981.1 | 1,145,934.8 | 173,418.1 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 1.196x | 1.196x |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 627,246.0 | 0.5982 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,662.8 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,621.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 30,896.9 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,645.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 875.7 | 860.0 | 884.2 | 7.9 | 1.478x | 1.478x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,353.0 | 1,352.2 | 1,372.9 | 8.0 | 1.000x | 1.000x | 77 | 17.6 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 3.761x | 3.761x | 77 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 13,580,774.2 | 2.5903 | 13,566,989.8 | 13,601,866.2 | 13,405.5 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 1.025x | 1.025x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,584,125.0 | 3.4181 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,888,192.1 | 1.8007 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,875,429.5 | 1.7885 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,137,544.3 | 2.9922 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,094,784.0 | 2.9514 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,171.4 | 73,144.9 | 73,224.4 | 27.8 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 1.657x | 1.657x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_1989c62_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,523.5 | 3,523.4 | 3,529.5 | 2.3 | 1.000x | 1.000x | 77 | 45.8 | 17.6 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 3.553x | 3.553x | 77 | 162.6 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 13,583,640.9 | 2.5909 | 13,563,234.4 | 13,588,319.8 | 9,475.1 | 0.027x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,676,206.1 | 2.6085 | 13,658,410.5 | 13,740,603.5 | 31,219.0 | 0.027x | 1.007x | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 36.708x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,581,417.1 | 3.4155 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,586,692.1 | 3.4205 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,881,379.0 | 1.7942 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,347.2 | 1.7885 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,877,090.2 | 1.7901 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,875,174.1 | 1.7883 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,149,477.5 | 3.0036 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,192,965.9 | 3.0450 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,092,666.6 | 2.9494 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,152,957.6 | 3.0069 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,179.2 | 73,161.2 | 73,330.5 | 63.1 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,303.5 | 73,290.6 | 73,322.0 | 11.5 | 0.040x | 1.002x | 85 | 100% |
| 3 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 461,165.2 | 455,738.7 | 466,627.4 | 3,547.8 | 0.251x | 6.302x | 85 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.074x | 85 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.249x | 85 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,524.4 | 3,519.8 | 3,602.1 | 31.7 | 0.026x | 1.000x | 77 | 45.8 | 17.6 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,662.4 | 3,660.4 | 3,669.2 | 3.1 | 0.027x | 1.039x | 77 | 47.6 | 17.4 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.335x | 77 | 198.4 | 44.2 | 100% |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 53,848.7 | 53,614.7 | 54,626.5 | 355.7 | 0.390x | 15.279x | 77 | 699.3 | 13.7 | 100% |
| 5 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 53,902.2 | 53,519.5 | 54,707.0 | 391.5 | 0.391x | 15.294x | 77 | 700.0 | 13.6 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 39.138x | 77 | 1,791.4 | 95.9 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 711,171.0 | 0.1356 | 710,981.1 | 1,145,934.8 | 173,418.1 | 0.192x | 1.000x | spread |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 713,690.6 | 0.1361 | 711,392.5 | 714,486.3 | 1,256.0 | 0.192x | 1.004x | spread |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 0.229x | 1.196x | spread |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,832,899.2 | 0.3496 | 1,831,518.1 | 1,847,785.7 | 7,649.4 | 0.494x | 2.577x | spread |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.696x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,920,640.2 | 0.3663 | 1,905,569.9 | 1,965,206.8 | 22,635.0 | 0.518x | 2.701x | spread |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.216x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 627,246.0 | 0.5982 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 628,059.0 | 0.5990 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 581,707.3 | 0.5548 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 658,242.3 | 0.6277 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,662.8 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,667.6 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,113.4 | 0.2957 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,324.2 | 0.2959 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,621.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,649.3 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,117.0 | 0.2958 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,392.8 | 0.2960 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 30,896.9 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 30,949.2 | 0.0295 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 320,961.8 | 0.3061 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 322,506.7 | 0.3076 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 17,645.2 | 0.0168 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 17,671.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-caps-simdna` | 310,051.9 | 0.2957 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_vm-in-caps-simdna` | 310,488.9 | 0.2961 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 432.9 | 431.7 | 434.5 | 1.0 | 0.169x | 1.000x |
| 2 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 516.6 | 516.4 | 517.7 | 0.5 | 0.201x | 1.193x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 0.231x | 1.368x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 870.5 | 858.7 | 887.1 | 10.0 | 0.339x | 2.011x |
| 5 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 875.7 | 860.0 | 884.2 | 7.9 | 0.341x | 2.023x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 5.934x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 5.950x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 1,045.1 | 1,043.2 | 1,047.9 | 1.6 | 0.141x | 1.000x | 77 | 13.6 | 100% |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 1,057.6 | 1,054.3 | 1,058.3 | 1.4 | 0.143x | 1.012x | 77 | 13.7 | 100% |
| 3 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 1,338.1 | 1,337.9 | 1,348.7 | 4.3 | 0.181x | 1.280x | 77 | 17.4 | 100% |
| 4 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 1,353.0 | 1,352.2 | 1,372.9 | 8.0 | 0.183x | 1.295x | 77 | 17.6 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 3.254x | 77 | 44.2 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 0.689x | 4.870x | 77 | 66.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 7.069x | 77 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 13,580,774.2 | 2.5903 | 13,566,989.8 | 13,601,866.2 | 13,405.5 | 0.111x | 1.000x | 5 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 13,596,186.2 | 2.5933 | 13,552,434.1 | 13,627,695.7 | 29,055.1 | 0.111x | 1.001x | 5 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 0.113x | 1.025x | 5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 1.339x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 9.034x | 5 | 100% |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,584,125.0 | 3.4181 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,578,393.8 | 3.4126 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,888,192.1 | 1.8007 |
| `t-b-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,885,944.5 | 1.7986 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 1,875,429.5 | 1.7885 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 1,874,971.6 | 1.7881 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,137,544.3 | 2.9922 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,154,491.2 | 3.0084 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_1989c62_auto-nocaps-simdna` | 3,094,784.0 | 2.9514 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_d34c9131_auto-caps-simdna` | 3,095,320.2 | 2.9519 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 62,176.3 | 62,132.6 | 62,239.1 | 35.5 | 0.116x | 1.000x |
| 2 | `pcrec_1989c62_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,809.0 | 62,698.2 | 63,185.7 | 168.0 | 0.117x | 1.010x |
| 3 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,171.4 | 73,144.9 | 73,224.4 | 27.8 | 0.136x | 1.177x |
| 4 | `pcrec_d34c9131_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,208.6 | 73,199.3 | 73,292.6 | 34.9 | 0.136x | 1.177x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 0.226x | 1.950x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.593x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.643x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_1989c62_auto-nocaps-simdna` | measured | `plain` | same program | 3,523.5 | 3,523.4 | 3,529.5 | 2.3 | 0.054x | 1.000x | 77 | 45.8 | 17.6 | 100% |
| 2 | `pcrec_d34c9131_auto-caps-simdna` | measured | `plain` | same program | 3,527.0 | 3,524.4 | 3,541.1 | 5.9 | 0.054x | 1.001x | 77 | 45.8 | 17.4 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.747x | 77 | 80.0 | 44.2 | 100% |
| 4 | `pcrec_1989c62_vm-caps-simdna` | measured | `plain` | same program | 12,384.0 | 12,336.7 | 12,419.3 | 32.6 | 0.188x | 3.515x | 77 | 160.8 | 13.7 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 0.190x | 3.553x | 77 | 162.6 | 66.1 | 100% |
| 6 | `pcrec_1989c62_vm-in-caps-simdna` | measured | `plain` | same program | 12,893.3 | 12,802.8 | 13,527.0 | 269.1 | 0.196x | 3.659x | 77 | 167.4 | 13.6 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 18.665x | 77 | 854.1 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -2:PCREC_ERR_STEPS×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |
| `orig` | `large-subject-throughput` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 5 | 80% | -4:PCREC_ERR_WORK×1 (smallest: t-c-long-atom-run, 1,048,576 B) | 0 | `t-c-long-atom-run` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**6 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `floor` | `match-compliance` | `pcrec_1989c62_auto-nocaps-simdna` | 875.7 | `pcrec_1989c62_vm-caps-simdna` | 432.9 | 0.494x | clears IQR only: gap 50.57%; IQR 0.13% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `match-compliance` | `pcrec_1989c62_auto-nocaps-simdna` | 875.7 | `pcrec_1989c62_vm-in-caps-simdna` | 516.6 | 0.590x | clears IQR only: gap 41.01%; IQR 0.13% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_1989c62_auto-nocaps-simdna` | 1,353.0 | `pcrec_1989c62_vm-caps-simdna` | 1,057.6 | 0.782x | clears IQR only: gap 21.84%; IQR 0.07% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_1989c62_auto-nocaps-simdna` | 1,353.0 | `pcrec_1989c62_vm-in-caps-simdna` | 1,045.1 | 0.772x | clears IQR only: gap 22.76%; IQR 0.12% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_1989c62_auto-nocaps-simdna` | 73,171.4 | `pcrec_1989c62_vm-caps-simdna` | 62,809.0 | 0.858x | clears IQR only: gap 14.16%; IQR 0.16% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_1989c62_auto-nocaps-simdna` | 73,171.4 | `pcrec_1989c62_vm-in-caps-simdna` | 62,176.3 | 0.850x | clears IQR only: gap 15.03%; IQR 0.04% (clears); no null band (no cross-pin pair in this report) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

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
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_d34c9131_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 151,621,570.0 | 150,070,112.0 | 160,325,170.0 | 3,773,314.3 | 5 | 47,440 | 82,131 | 13,433 | 0.025 | compiled=5 | 10,169,728.0 | 140,530,217.0 | 114,060.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,328,764.0 | 154,959,980.0 | 186,417,630.0 | 10,113,724.8 | 5 | 47,584 | 94,342 | 15,349 | 0.059 (max is trial 1) | compiled=5 | 12,979,624.0 | 158,353,199.0 | 192,941.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 557,601,392.0 | 549,327,714.0 | 569,843,521.0 | 7,315,769.4 | 5 | 39,248 | 58,359 | 56,805 | 0.013 | compiled=5 | 2,524,514.0 | 554,883,877.0 | 193,001.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 565,207,216.0 | 558,228,695.0 | 571,057,819.0 | 4,268,779.8 | 5 | 39,248 | 58,475 | 56,921 | 0.008 | compiled=5 | 2,169,652.0 | 561,344,614.0 | 200,541.0 |
| `factored` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 557,938,347.0 | 546,318,699.0 | 563,311,338.0 | 6,106,183.7 | 5 | 39,248 | 58,359 | 56,805 | 0.011 | compiled=5 | 2,326,253.0 | 555,627,603.0 | 108,241.0 |
| `factored` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 561,136,606.0 | 549,125,744.0 | 565,607,772.0 | 5,693,701.3 | 5 | 39,248 | 58,475 | 56,921 | 0.010 | compiled=5 | 2,209,483.0 | 558,601,840.0 | 106,210.0 |
| `factored` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 164,584,146.0 | 163,200,287.0 | 172,326,812.0 | 3,438,404.2 | 5 | 48,128 | 82,455 | 13,761 | 0.021 | compiled=5 | 9,866,191.0 | 154,496,783.0 | 194,071.0 |
| `factored` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 183,590,851.0 | 175,932,235.0 | 194,146,927.0 | 6,021,076.8 | 5 | 48,264 | 94,666 | 15,677 | 0.033 | compiled=5 | 12,225,066.0 | 171,279,445.0 | 198,781.0 |
| `floor` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 139,949,224.0 | 130,838,550.0 | 142,838,561.0 | 4,676,626.4 | 5 | 22,832 | 17,965 | 12,968 | 0.033 | compiled=5 | 1,653,409.0 | 136,240,052.0 | 109,170.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 148,273,931.0 | 141,076,649.0 | 152,803,577.0 | 4,745,842.6 | 5 | 22,968 | 20,308 | 14,985 | 0.032 | compiled=5 | 1,822,371.0 | 146,451,511.0 | 183,361.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 128,967,530.0 | 124,322,624.0 | 137,012,847.0 | 4,823,380.7 | 5 | 22,376 | 17,258 | 17,258 | 0.037 | compiled=5 | 1,429,138.0 | 127,548,612.0 | 182,731.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 137,382,550.0 | 121,509,347.0 | 142,162,417.0 | 7,505,540.6 | 5 | 22,376 | 17,369 | 17,369 | 0.055 | compiled=5 | 1,457,899.0 | 135,826,510.0 | 98,900.0 |
| `floor` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 136,759,498.0 | 133,740,580.0 | 137,964,826.0 | 1,824,242.0 | 5 | 22,376 | 17,258 | 17,258 | 0.013 | compiled=5 | 1,467,469.0 | 135,122,328.0 | 196,311.0 |
| `floor` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 136,344,905.0 | 128,201,518.0 | 141,820,418.0 | 5,034,770.1 | 5 | 22,376 | 17,369 | 17,369 | 0.037 | compiled=5 | 1,755,101.0 | 133,278,078.0 | 190,831.0 |
| `floor` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 146,925,846.0 | 134,069,456.0 | 156,562,775.0 | 7,227,152.4 | 5 | 27,608 | 18,106 | 13,109 | 0.049 | compiled=5 | 1,805,321.0 | 144,978,534.0 | 192,931.0 |
| `floor` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 158,953,769.0 | 153,090,875.0 | 161,812,987.0 | 3,417,763.5 | 5 | 27,752 | 20,449 | 15,126 | 0.022 | compiled=5 | 1,819,561.0 | 155,299,577.0 | 213,442.0 |
| `orig` | `plain` | `pcrec_1989c62_auto-nocaps-simdna` | 155,645,893.0 | 148,604,192.0 | 161,597,979.0 | 5,318,300.2 | 5 | 43,304 | 81,907 | 13,380 | 0.034 | compiled=5 | 9,623,285.0 | 139,588,191.0 | 112,860.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_auto-nocaps-simdna` | 171,558,255.0 | 168,392,047.0 | 174,796,025.0 | 2,301,945.8 | 5 | 47,544 | 94,118 | 15,296 | 0.013 | compiled=5 | 11,420,075.0 | 157,236,173.0 | 193,971.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-caps-simdna` | 432,550,604.0 | 423,790,122.0 | 432,981,428.0 | 3,557,204.4 | 5 | 30,976 | 47,188 | 45,801 | 0.008 | compiled=5 | 1,953,732.0 | 430,495,102.0 | 115,240.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-caps-simdna` | 432,168,521.0 | 409,864,175.0 | 439,547,864.0 | 11,267,008.2 | 5 | 30,976 | 47,306 | 45,919 | 0.026 | compiled=5 | 1,929,061.0 | 430,050,959.0 | 192,691.0 |
| `orig` | `plain` | `pcrec_1989c62_vm-in-caps-simdna` | 437,531,255.0 | 432,370,325.0 | 447,960,387.0 | 5,531,367.4 | 5 | 30,976 | 47,188 | 45,801 | 0.013 | compiled=5 | 2,042,772.0 | 433,210,960.0 | 188,701.0 |
| `orig` | `whole-subject` | `pcrec_1989c62_vm-in-caps-simdna` | 429,579,968.0 | 421,616,232.0 | 432,505,467.0 | 3,830,835.1 | 5 | 30,976 | 47,306 | 45,919 | 0.009 | compiled=5 | 2,052,033.0 | 427,185,674.0 | 197,772.0 |
| `orig` | `plain` | `pcrec_d34c9131_auto-caps-simdna` | 166,883,659.0 | 162,455,282.0 | 173,020,587.0 | 4,309,592.0 | 5 | 48,088 | 82,048 | 13,521 | 0.026 | compiled=5 | 9,496,359.0 | 154,801,744.0 | 195,231.0 |
| `orig` | `whole-subject` | `pcrec_d34c9131_auto-caps-simdna` | 178,790,732.0 | 164,688,805.0 | 180,042,050.0 | 5,996,848.9 | 5 | 48,224 | 94,259 | 15,437 | 0.034 (max is trial 1) | compiled=5 | 11,568,361.0 | 159,379,703.0 | 108,781.0 |

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

