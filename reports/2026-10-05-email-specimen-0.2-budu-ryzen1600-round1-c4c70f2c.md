# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, testee=pcrec_c4c70f2c_auto-caps-simdna, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (11 record(s) matching this query)
- records included: 4
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_c4c70f2c_auto-caps-simdna__budu-ryzen1600__20261005T120545Z` (store/records/email-specimen@0.2/pcrec_c4c70f2c_auto-caps-simdna/email-specimen@0.2__pcrec_c4c70f2c_auto-caps-simdna__budu-ryzen1600__20261005T120545Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__budu-ryzen1600__20260920T164034Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- superseded: 7 record(s) (OD-B15; --all-records lists them)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.4, 1.6, 1.7
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 4 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 7,027,725.3 | 1.3404 | 7,023,766.6 | 7,034,094.7 | 3,513.8 | 0.014x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 70.952x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,809,902.9 | 3.6334 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,713.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,681.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,165,282.1 | 3.0186 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,694.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,249.0 | 73,235.8 | 73,408.0 | 64.5 | 0.040x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.050x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.225x |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 3,901.1 | 3,898.8 | 3,907.9 | 3.4 | 0.028x | 1.000x | 77 | 50.7 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 3.917x | 77 | 198.4 | 44.2 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 35.359x | 77 | 1,791.4 | 95.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 698,959.8 | 0.1333 | 698,670.0 | 699,702.9 | 349.2 | 0.188x | 1.000x | spread |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.743x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.307x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 614,634.8 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,710.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,699.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 31,175.4 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,682.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 891.9 | 891.1 | 918.0 | 10.3 | 0.347x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 2.880x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 2.888x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 1,325.0 | 1,322.9 | 1,588.4 | 105.4 | 0.179x | 1.000x | 77 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 2.567x | 77 | 44.2 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 5.576x | 77 | 95.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 7,054,261.4 | 1.3455 | 7,042,288.9 | 7,055,106.3 | 4,853.3 | 0.057x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 2.578x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 17.392x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,773,251.9 | 3.5985 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,700.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,671.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,228,103.5 | 3.0786 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,723.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,138.0 | 73,132.6 | 73,141.6 | 3.2 | 0.136x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 7.305x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 7.347x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 3,710.4 | 3,707.6 | 3,715.6 | 2.7 | 0.056x | 1.000x | 77 | 48.2 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.659x | 77 | 80.0 | 44.2 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 17.725x | 77 | 854.1 | 95.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 1.000x | 1.000x |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 1.000x | 1.000x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 1.000x | 1.000x | 77 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 1.000x | 1.000x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 1.000x | 1.000x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 1.000x | 1.000x | 77 | 162.6 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 7,027,725.3 | 1.3404 | 7,023,766.6 | 7,034,094.7 | 3,513.8 | 0.014x | 1.000x | 5 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 70.952x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,809,902.9 | 3.6334 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,713.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,681.4 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,165,282.1 | 3.0186 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,694.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,249.0 | 73,235.8 | 73,408.0 | 64.5 | 0.040x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.050x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.225x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 3,901.1 | 3,898.8 | 3,907.9 | 3.4 | 0.028x | 1.000x | 77 | 50.7 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 3.917x | 77 | 198.4 | 44.2 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 35.359x | 77 | 1,791.4 | 95.9 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 698,959.8 | 0.1333 | 698,670.0 | 699,702.9 | 349.2 | 0.188x | 1.000x | spread |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 0.229x | 1.217x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.743x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.307x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 614,634.8 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,710.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,699.5 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 31,175.4 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,682.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 0.231x | 1.000x |
| 2 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 891.9 | 891.1 | 918.0 | 10.3 | 0.347x | 1.506x |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 4.337x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 4.348x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 1,325.0 | 1,322.9 | 1,588.4 | 105.4 | 0.179x | 1.000x | 77 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 2.567x | 77 | 44.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 0.689x | 3.841x | 77 | 66.1 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 5.576x | 77 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 7,054,261.4 | 1.3455 | 7,042,288.9 | 7,055,106.3 | 4,853.3 | 0.057x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 0.113x | 1.972x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 2.578x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 17.392x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,773,251.9 | 3.5985 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,700.8 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,671.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 3,228,103.5 | 3.0786 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_c4c70f2c_auto-caps-simdna` | 17,723.9 | 0.0169 |
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
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,138.0 | 73,132.6 | 73,141.6 | 3.2 | 0.136x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 0.226x | 1.658x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 7.305x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 7.347x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_c4c70f2c_auto-caps-simdna` | measured | `plain` | same program | 3,710.4 | 3,707.6 | 3,715.6 | 2.7 | 0.056x | 1.000x | 77 | 48.2 | 17.2 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.659x | 77 | 80.0 | 44.2 | 100% |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 0.190x | 3.374x | 77 | 162.6 | 66.1 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 17.725x | 77 | 854.1 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_c4c70f2c_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_c4c70f2c_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_c4c70f2c_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_c4c70f2c_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=range, edges=1 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_c4c70f2c_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_c4c70f2c_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_c4c70f2c_auto-caps-simdna` | 186,275,251.0 | 173,528,255.0 | 195,441,631.0 | 7,084,412.9 | 5 | 48,968 | 84,896 | 16,202 | 0.038 | compiled=5 | 8,915,057.0 | 175,060,824.0 | 194,712.0 |
| `factored` | `whole-subject` | `pcrec_c4c70f2c_auto-caps-simdna` | 196,401,716.0 | 187,123,207.0 | 219,135,792.0 | 11,480,654.6 | 5 | 49,104 | 97,107 | 18,118 | 0.058 | compiled=5 | 11,180,579.0 | 185,108,236.0 | 103,639.0 |
| `floor` | `plain` | `pcrec_c4c70f2c_auto-caps-simdna` | 154,904,079.0 | 152,839,208.0 | 160,355,537.0 | 2,628,966.7 | 5 | 28,400 | 20,396 | 15,399 | 0.017 | compiled=5 | 2,028,330.0 | 151,562,450.0 | 199,571.0 |
| `floor` | `whole-subject` | `pcrec_c4c70f2c_auto-caps-simdna` | 169,353,905.0 | 163,036,961.0 | 179,895,329.0 | 6,715,069.5 | 5 | 28,544 | 23,324 | 18,001 | 0.040 | compiled=5 | 1,970,480.0 | 167,198,613.0 | 109,032.0 |
| `orig` | `plain` | `pcrec_c4c70f2c_auto-caps-simdna` | 178,808,492.0 | 161,967,038.0 | 185,107,617.0 | 8,583,697.6 | 5 | 48,928 | 84,469 | 15,942 | 0.048 | compiled=5 | 8,474,153.0 | 170,132,427.0 | 113,390.0 |
| `orig` | `whole-subject` | `pcrec_c4c70f2c_auto-caps-simdna` | 190,966,186.0 | 182,751,034.0 | 207,217,170.0 | 8,845,660.1 | 5 | 49,072 | 96,680 | 17,858 | 0.046 (max is trial 1) | compiled=5 | 10,367,064.0 | 180,513,602.0 | 204,251.0 |

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

