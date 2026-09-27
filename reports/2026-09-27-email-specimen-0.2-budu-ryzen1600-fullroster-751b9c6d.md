# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, testee=pcrec_751b9c6d_auto-caps-simdna, testee=pcrec_751b9c6d_auto-nocaps-simdna, testee=pcrec_751b9c6d_vm-caps-simdna, testee=pcrec_751b9c6d_vm-in-caps-simdna, testee=libpcre2_10.46_interp-caps-simdna, testee=libpcre2_10.46_jit-caps-simdna, testee=rust_1.13.1_default-caps-simdna
- record source: store/index.tsv (14 record(s) matching this query)
- records included: 7
- worst other-core busy: 10.81% (`rust_1.13.1_default-caps-simdna` / `orig` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20260902T075326Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260902T080213Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T091338Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_auto-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_auto-caps-simdna__budu-ryzen1600__20260927T091338Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_auto-nocaps-simdna__budu-ryzen1600__20260927T091920Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_auto-nocaps-simdna/email-specimen@0.2__pcrec_751b9c6d_auto-nocaps-simdna__budu-ryzen1600__20260927T091920Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T092525Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_vm-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_vm-caps-simdna__budu-ryzen1600__20260927T092525Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 496 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_751b9c6d_vm-in-caps-simdna__budu-ryzen1600__20260927T093420Z` (store/records/email-specimen@0.2/pcrec_751b9c6d_vm-in-caps-simdna/email-specimen@0.2__pcrec_751b9c6d_vm-in-caps-simdna__budu-ryzen1600__20260927T093420Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
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
- status rule: v1.4 X13 (pre-flight + trial agreement) on 7 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,018,630.0 | 1.3387 | 7,014,772.2 | 7,022,962.4 | 2,908.8 | 0.014x | 1.000x | 5 | 100% |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 111,373,789.5 | 21.2429 | 110,827,104.7 | 112,207,349.1 | 486,165.0 | 0.223x | 15.868x | 5 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 112,681,436.2 | 21.4923 | 111,572,780.4 | 113,150,910.4 | 640,462.1 | 0.226x | 16.055x | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 71.044x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,789,127.8 | 3.6136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 12,276,737.1 | 11.7080 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 12,472,845.9 | 11.8950 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,720.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 18,037.4 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 18,007.9 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,706.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,925.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,871.4 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,174,406.5 | 3.0273 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 99,158,013.9 | 94.5645 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 99,749,318.3 | 95.1284 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,690.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,963.3 | 0.0171 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,998.8 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,245.2 | 73,241.5 | 73,251.5 | 3.3 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460,693.1 | 454,617.7 | 461,859.2 | 3,205.5 | 0.251x | 6.290x | 85 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.052x | 85 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.226x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,940.5 | 3,935.9 | 3,944.4 | 2.9 | 0.029x | 1.000x | 77 | 51.2 | 17.1 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 3.878x | 77 | 198.4 | 44.2 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 34,899.4 | 34,419.4 | 35,025.6 | 218.4 | 0.253x | 8.857x | 77 | 453.2 | 15.1 | 100% |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 35,172.7 | 34,596.0 | 35,567.8 | 343.0 | 0.255x | 8.926x | 77 | 456.8 | 15.9 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 35.004x | 77 | 1,791.4 | 95.9 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 698,825.3 | 0.1333 | 698,590.0 | 922,007.7 | 89,268.2 | 0.188x | 1.000x | spread |
| 2 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,685,511.1 | 0.3215 | 1,685,101.9 | 1,692,377.6 | 2,767.2 | 0.454x | 2.412x | spread |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,692,678.3 | 0.3229 | 1,691,646.9 | 1,695,117.4 | 1,346.8 | 0.456x | 2.422x | spread |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.744x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.308x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 614,704.1 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 977,723.2 | 0.9324 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 984,134.5 | 0.9385 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,705.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,743.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,706.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,722.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,696.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 31,022.2 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 654,782.9 | 0.6244 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 655,085.0 | 0.6247 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,691.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,699.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,696.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 529.4 | 529.3 | 530.5 | 0.5 | 0.206x | 1.000x |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 559.2 | 557.8 | 561.2 | 1.2 | 0.218x | 1.056x |
| 3 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 833.9 | 823.7 | 848.7 | 8.4 | 0.325x | 1.575x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 4.852x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 4.864x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,160.6 | 1,158.8 | 1,164.6 | 2.0 | 0.157x | 1.000x | 77 | 15.1 | 100% |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,227.3 | 1,224.2 | 1,228.9 | 1.5 | 0.166x | 1.057x | 77 | 15.9 | 100% |
| 3 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 1,320.4 | 1,319.9 | 1,323.1 | 1.2 | 0.179x | 1.138x | 77 | 17.1 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 2.931x | 77 | 44.2 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 6.365x | 77 | 95.9 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,053,755.3 | 1.3454 | 7,048,184.0 | 7,194,846.7 | 56,986.4 | 0.057x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 2.578x |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 22,840,316.3 | 4.3564 | 22,758,079.6 | 23,117,623.4 | 122,729.8 | 0.186x | 3.238x |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 23,621,686.4 | 4.5055 | 23,337,194.8 | 23,931,857.4 | 206,785.4 | 0.193x | 3.349x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 17.394x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,774,303.0 | 3.5995 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 5,236,612.5 | 4.9940 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 5,963,203.3 | 5.6870 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,732.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,723.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,698.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,681.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,726.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,221,893.2 | 3.0726 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,585,066.0 | 16.7704 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,609,664.6 | 16.7939 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,719.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,693.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,716.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61,998.6 | 61,887.2 | 62,467.7 | 212.1 | 0.115x | 1.000x |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,876.5 | 62,830.5 | 66,758.3 | 1,542.8 | 0.117x | 1.014x |
| 3 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,131.7 | 73,120.8 | 73,136.1 | 5.5 | 0.136x | 1.180x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.618x |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.667x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,704.0 | 3,701.2 | 3,799.8 | 38.6 | 0.056x | 1.000x | 77 | 48.1 | 17.1 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.662x | 77 | 80.0 | 44.2 | 100% |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 8,596.0 | 8,554.5 | 8,800.2 | 89.6 | 0.131x | 2.321x | 77 | 111.6 | 15.9 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 9,421.3 | 9,367.8 | 9,446.5 | 28.0 | 0.143x | 2.544x | 77 | 122.4 | 15.1 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 17.756x | 77 | 854.1 | 95.9 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,417.6 | 1.3444 | 7,045,136.7 | 7,053,866.5 | 2,825.0 | 1.000x | 1.000x |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,773,966.2 | 3.5991 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.5 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.9 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,221,634.0 | 3.0724 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,679.6 | 0.0169 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,150.7 | 73,133.3 | 73,179.6 | 16.8 | 1.000x | 1.000x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,702.6 | 3,697.4 | 3,708.4 | 3.6 | 1.000x | 1.000x | 77 | 48.1 | 17.1 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 698,579.8 | 0.1332 | 698,448.6 | 699,266.1 | 299.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 1.217x | 1.217x |

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 614,501.1 | 0.5860 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.3 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,651.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 31,143.0 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,722.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 828.4 | 825.0 | 842.2 | 7.1 | 1.399x | 1.399x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 1,319.7 | 1,317.7 | 1,329.1 | 4.2 | 1.000x | 1.000x | 77 | 17.1 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 3.856x | 3.856x | 77 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,489.6 | 1.3444 | 7,040,718.7 | 7,053,433.2 | 5,019.7 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 1.974x | 1.974x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,775,381.2 | 3.6005 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,690.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,219,745.6 | 3.0706 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,670.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,137.5 | 73,127.5 | 73,141.1 | 5.0 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 1.658x | 1.658x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_751b9c6d_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,703.1 | 3,701.2 | 3,705.6 | 1.6 | 1.000x | 1.000x | 77 | 48.1 | 17.1 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 3.381x | 3.381x | 77 | 162.6 | 66.1 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,018,630.0 | 1.3387 | 7,014,772.2 | 7,022,962.4 | 2,908.8 | 0.014x | 1.000x | 5 | 100% |
| 2 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,417.6 | 1.3444 | 7,045,136.7 | 7,053,866.5 | 2,825.0 | 0.014x | 1.004x | 5 | 100% |
| 3 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 111,373,789.5 | 21.2429 | 110,827,104.7 | 112,207,349.1 | 486,165.0 | 0.223x | 15.868x | 5 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 112,681,436.2 | 21.4923 | 111,572,780.4 | 113,150,910.4 | 640,462.1 | 0.226x | 16.055x | 5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 498,628,352.6 | 95.1058 | 498,099,435.6 | 504,091,413.0 | 2,369,758.7 | 1.000x | 71.044x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,789,127.8 | 3.6136 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,773,966.2 | 3.5991 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 12,276,737.1 | 11.7080 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 12,472,845.9 | 11.8950 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 51,615,885.8 | 49.2247 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,720.7 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.5 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 18,037.4 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 18,007.9 | 0.0172 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,798.8 | 0.0179 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,706.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,925.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,871.4 | 0.0170 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,761.9 | 0.0179 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,174,406.5 | 3.0273 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,221,634.0 | 3.0724 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 99,158,013.9 | 94.5645 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 99,749,318.3 | 95.1284 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 447,267,822.4 | 426.5478 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,690.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,679.6 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,963.3 | 0.0171 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,998.8 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,846.0 | 0.0180 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,150.7 | 73,133.3 | 73,179.6 | 16.8 | 0.040x | 1.000x | 85 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,245.2 | 73,241.5 | 73,251.5 | 3.3 | 0.040x | 1.001x | 85 | 100% |
| 3 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 460,693.1 | 454,617.7 | 461,859.2 | 3,205.5 | 0.251x | 6.298x | 85 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,834,922.8 | 1,824,112.8 | 1,872,579.8 | 19,292.9 | 1.000x | 25.084x | 85 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,847,682.0 | 1,822,401.3 | 1,871,729.4 | 18,328.2 | 1.007x | 25.259x | 85 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,702.6 | 3,697.4 | 3,708.4 | 3.6 | 0.027x | 1.000x | 77 | 48.1 | 17.1 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,940.5 | 3,935.9 | 3,944.4 | 2.9 | 0.029x | 1.064x | 77 | 51.2 | 17.1 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 15,280.0 | 15,216.5 | 15,328.3 | 45.2 | 0.111x | 4.127x | 77 | 198.4 | 44.2 | 100% |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 34,899.4 | 34,419.4 | 35,025.6 | 218.4 | 0.253x | 9.426x | 77 | 453.2 | 15.1 | 100% |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 35,172.7 | 34,596.0 | 35,567.8 | 343.0 | 0.255x | 9.499x | 77 | 456.8 | 15.9 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 137,936.2 | 137,773.3 | 138,235.8 | 186.6 | 1.000x | 37.254x | 77 | 1,791.4 | 95.9 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 698,579.8 | 0.1332 | 698,448.6 | 699,266.1 | 299.9 | 0.188x | 1.000x | spread |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 698,825.3 | 0.1333 | 698,590.0 | 922,007.7 | 89,268.2 | 0.188x | 1.000x | spread |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 850,311.8 | 0.1622 | 849,617.6 | 850,818.6 | 446.9 | 0.229x | 1.217x | spread |
| 4 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,685,511.1 | 0.3215 | 1,685,101.9 | 1,692,377.6 | 2,767.2 | 0.454x | 2.413x | spread |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,692,678.3 | 0.3229 | 1,691,646.9 | 1,695,117.4 | 1,346.8 | 0.456x | 2.423x | spread |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,917,329.2 | 0.3657 | 1,858,784.8 | 1,924,547.9 | 27,662.3 | 0.517x | 2.745x | **dominated**: `t-a-valid-addrs` is 90.2% of this set |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 3,709,245.8 | 0.7075 | 3,685,407.6 | 3,766,448.0 | 36,562.9 | 1.000x | 5.310x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 614,501.1 | 0.5860 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 614,704.1 | 0.5862 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 761,325.9 | 0.7261 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 977,723.2 | 0.9324 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 984,134.5 | 0.9385 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,728,929.7 | 1.6488 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,585,463.7 | 3.4194 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,664.3 | 0.0168 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,705.6 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 17,933.5 | 0.0171 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,743.1 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,706.9 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,676.1 | 0.0378 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,720.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,651.4 | 0.0168 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,722.7 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,076.5 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,696.3 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,337.4 | 0.0375 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 31,143.0 | 0.0297 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 31,022.2 | 0.0296 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 34,679.3 | 0.0331 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 654,782.9 | 0.6244 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 655,085.0 | 0.6247 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,317.0 | 0.0661 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 70,617.0 | 0.0673 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,722.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,691.3 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 18,053.0 | 0.0172 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,699.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,696.1 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,612.0 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,747.4 | 0.0169 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 529.4 | 529.3 | 530.5 | 0.5 | 0.206x | 1.000x |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 559.2 | 557.8 | 561.2 | 1.2 | 0.218x | 1.056x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 592.4 | 592.0 | 593.4 | 0.5 | 0.231x | 1.119x |
| 4 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 828.4 | 825.0 | 842.2 | 7.1 | 0.322x | 1.565x |
| 5 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 833.9 | 823.7 | 848.7 | 8.4 | 0.325x | 1.575x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,568.8 | 2,562.5 | 2,575.4 | 4.2 | 1.000x | 4.852x |
| 7 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,575.4 | 2,573.2 | 2,585.0 | 4.4 | 1.003x | 4.864x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 1,160.6 | 1,158.8 | 1,164.6 | 2.0 | 0.157x | 1.000x | 77 | 15.1 | 100% |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 1,227.3 | 1,224.2 | 1,228.9 | 1.5 | 0.166x | 1.057x | 77 | 15.9 | 100% |
| 3 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 1,319.7 | 1,317.7 | 1,329.1 | 4.2 | 0.179x | 1.137x | 77 | 17.1 | 100% |
| 4 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 1,320.4 | 1,319.9 | 1,323.1 | 1.2 | 0.179x | 1.138x | 77 | 17.1 | 100% |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 3,401.2 | 3,360.2 | 3,449.3 | 28.3 | 0.460x | 2.931x | 77 | 44.2 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 5,089.3 | 5,083.2 | 5,171.0 | 36.2 | 0.689x | 4.385x | 77 | 66.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 7,387.8 | 7,265.9 | 7,539.5 | 94.8 | 1.000x | 6.365x | 77 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 7,048,489.6 | 1.3444 | 7,040,718.7 | 7,053,433.2 | 5,019.7 | 0.057x | 1.000x |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 7,053,755.3 | 1.3454 | 7,048,184.0 | 7,194,846.7 | 56,986.4 | 0.057x | 1.001x |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 13,914,223.0 | 2.6539 | 13,897,291.2 | 13,962,598.9 | 24,297.0 | 0.113x | 1.974x |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 18,187,186.2 | 3.4689 | 18,144,884.1 | 18,264,896.8 | 40,459.4 | 0.148x | 2.580x |
| 5 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 22,840,316.3 | 4.3564 | 22,758,079.6 | 23,117,623.4 | 122,729.8 | 0.186x | 3.240x |
| 6 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 23,621,686.4 | 4.5055 | 23,337,194.8 | 23,931,857.4 | 206,785.4 | 0.193x | 3.351x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 122,689,562.2 | 23.4012 | 122,478,185.0 | 129,024,141.5 | 2,561,512.1 | 1.000x | 17.407x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,775,381.2 | 3.6005 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,774,303.0 | 3.5995 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 6,366,900.5 | 6.0719 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,700,507.0 | 3.5291 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 5,236,612.5 | 4.9940 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 5,963,203.3 | 5.6870 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,638,016.7 | 27.3113 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,672.0 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,732.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,865,231.4 | 1.7788 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,559,712.1 | 2.4411 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,697.4 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,723.3 | 0.0169 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,983.0 | 0.0171 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,690.8 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,698.2 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,868,705.8 | 1.7821 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,428.0 | 2.6879 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,681.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,726.1 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,933.2 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 3,219,745.6 | 3.0706 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 3,221,893.2 | 3.0726 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,942,459.5 | 1.8525 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,966,791.7 | 5.6904 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,585,066.0 | 16.7704 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,609,664.6 | 16.7939 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,901,018.6 | 89.5510 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-nocaps-simdna` | 17,670.8 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_auto-caps-simdna` | 17,719.7 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,869,164.2 | 1.7826 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,159,050.0 | 3.0127 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-caps-simdna` | 17,693.5 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_751b9c6d_vm-in-caps-simdna` | 17,716.9 | 0.0169 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,971.3 | 0.0171 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `whole-subject` | separate artifact | 61,998.6 | 61,887.2 | 62,467.7 | 212.1 | 0.115x | 1.000x |
| 2 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 62,876.5 | 62,830.5 | 66,758.3 | 1,542.8 | 0.117x | 1.014x |
| 3 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 73,131.7 | 73,120.8 | 73,136.1 | 5.5 | 0.136x | 1.180x |
| 4 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 73,137.5 | 73,127.5 | 73,141.1 | 5.0 | 0.136x | 1.180x |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 121,264.2 | 121,191.1 | 121,553.8 | 130.9 | 0.226x | 1.956x |
| 6 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 534,278.2 | 532,144.6 | 539,692.4 | 2,817.0 | 0.994x | 8.618x |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 537,363.1 | 533,855.5 | 540,123.7 | 2,234.5 | 1.000x | 8.667x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_751b9c6d_auto-nocaps-simdna` | measured | `plain` | same program | 3,703.1 | 3,701.2 | 3,705.6 | 1.6 | 0.056x | 1.000x | 77 | 48.1 | 17.1 | 100% |
| 2 | `pcrec_751b9c6d_auto-caps-simdna` | measured | `plain` | same program | 3,704.0 | 3,701.2 | 3,799.8 | 38.6 | 0.056x | 1.000x | 77 | 48.1 | 17.1 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,156.7 | 6,142.2 | 6,684.1 | 210.4 | 0.094x | 1.663x | 77 | 80.0 | 44.2 | 100% |
| 4 | `pcrec_751b9c6d_vm-caps-simdna` | measured | `plain` | same program | 8,596.0 | 8,554.5 | 8,800.2 | 89.6 | 0.131x | 2.321x | 77 | 111.6 | 15.9 | 100% |
| 5 | `pcrec_751b9c6d_vm-in-caps-simdna` | measured | `plain` | same program | 9,421.3 | 9,367.8 | 9,446.5 | 28.0 | 0.143x | 2.544x | 77 | 122.4 | 15.1 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 12,519.9 | 12,498.8 | 13,271.2 | 298.2 | 0.190x | 3.381x | 77 | 162.6 | 66.1 | 100% |
| 7 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 65,768.1 | 65,571.9 | 66,171.5 | 218.5 | 1.000x | 17.760x | 77 | 854.1 | 95.9 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**8 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `pcrec_751b9c6d_auto-nocaps-simdna` | 7,048,417.6 | `pcrec_751b9c6d_auto-caps-simdna` | 7,018,630.0 | 0.996x | clears IQR only: gap 0.42%; IQR 0.06% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 828.4 | `pcrec_751b9c6d_vm-caps-simdna` | 559.2 | 0.675x | clears IQR only: gap 32.50%; IQR 1.55% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 828.4 | `pcrec_751b9c6d_vm-in-caps-simdna` | 529.4 | 0.639x | clears IQR only: gap 36.09%; IQR 1.55% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_751b9c6d_auto-nocaps-simdna` | 1,319.7 | `pcrec_751b9c6d_vm-caps-simdna` | 1,227.3 | 0.930x | clears IQR only: gap 7.00%; IQR 0.26% (clears); no null band (no cross-pin pair in this report) |
| `floor` | `short-subject-search` | `pcrec_751b9c6d_auto-nocaps-simdna` | 1,319.7 | `pcrec_751b9c6d_vm-in-caps-simdna` | 1,160.6 | 0.879x | clears IQR only: gap 12.06%; IQR 0.26% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_auto-caps-simdna` | 73,131.7 | 1.000x | within IQR: gap 0.01%; IQR 0.01% (within); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_vm-caps-simdna` | 62,876.5 | 0.860x | clears IQR only: gap 14.03%; IQR 0.23% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_751b9c6d_auto-nocaps-simdna` | 73,137.5 | `pcrec_751b9c6d_vm-in-caps-simdna` | 61,998.6 | 0.848x | clears IQR only: gap 15.23%; IQR 0.22% (clears); no null band (no cross-pin pair in this report) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_751b9c6d_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class-bounded table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_751b9c6d_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,546 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,654 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,839 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
- `pcrec_751b9c6d_vm-in-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=_in, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 28,949 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=32768/131072 (caller-provided), frame=24
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
| `factored` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 176,165,338.0 | 169,951,885.0 | 196,473,115.0 | 10,135,069.5 | 5 | 48,352 | 83,886 | 15,192 | 0.058 | compiled=5 | 12,853,278.0 | 161,116,428.0 | 196,921.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 185,721,738.0 | 173,410,853.0 | 190,569,704.0 | 6,034,344.4 | 5 | 48,496 | 96,097 | 17,108 | 0.032 | compiled=5 | 13,036,999.0 | 172,772,170.0 | 123,491.0 |
| `factored` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 168,937,809.0 | 163,870,263.0 | 177,438,115.0 | 4,591,805.3 | 5 | 48,352 | 83,703 | 15,005 | 0.027 | compiled=5 | 12,637,407.0 | 155,611,830.0 | 197,511.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 185,504,757.0 | 168,100,154.0 | 208,858,921.0 | 14,070,465.5 | 5 | 48,496 | 95,914 | 16,921 | 0.076 (max is trial 1) | compiled=5 | 13,058,369.0 | 172,213,227.0 | 108,331.0 |
| `factored` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 576,139,717.0 | 569,680,273.0 | 586,426,511.0 | 5,370,233.7 | 5 | 44,264 | 60,302 | 58,694 | 0.009 | compiled=5 | 2,397,543.0 | 573,555,424.0 | 127,010.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 578,346,268.0 | 568,374,987.0 | 595,478,368.0 | 10,527,133.0 | 5 | 44,264 | 60,418 | 58,810 | 0.018 | compiled=5 | 2,480,624.0 | 575,769,775.0 | 198,041.0 |
| `factored` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 584,225,110.0 | 576,541,099.0 | 590,554,034.0 | 4,707,838.2 | 5 | 44,264 | 60,302 | 58,694 | 0.008 | compiled=5 | 2,720,684.0 | 578,623,870.0 | 206,042.0 |
| `factored` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 587,832,999.0 | 572,366,057.0 | 592,267,772.0 | 7,146,849.0 | 5 | 44,264 | 60,418 | 58,810 | 0.012 | compiled=5 | 2,492,624.0 | 585,122,764.0 | 217,611.0 |
| `floor` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 155,608,989.0 | 144,033,349.0 | 158,410,945.0 | 5,606,026.0 | 5 | 27,792 | 19,406 | 14,409 | 0.036 | compiled=5 | 2,043,281.0 | 153,692,710.0 | 118,701.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 163,951,553.0 | 154,908,956.0 | 165,616,893.0 | 4,627,729.4 | 5 | 27,936 | 21,861 | 16,538 | 0.028 | compiled=5 | 1,831,690.0 | 162,031,913.0 | 118,251.0 |
| `floor` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 150,936,946.0 | 143,526,446.0 | 159,092,858.0 | 5,218,235.7 | 5 | 27,792 | 19,406 | 14,409 | 0.035 | compiled=5 | 2,048,871.0 | 148,998,255.0 | 210,272.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 165,490,831.0 | 155,222,089.0 | 171,165,671.0 | 5,627,958.9 | 5 | 27,936 | 21,861 | 16,538 | 0.034 (max is trial 1) | compiled=5 | 1,855,280.0 | 162,441,446.0 | 196,152.0 |
| `floor` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 142,192,828.0 | 136,093,417.0 | 148,688,534.0 | 4,406,135.0 | 5 | 23,304 | 19,133 | 19,133 | 0.031 | compiled=5 | 1,558,598.0 | 140,525,230.0 | 107,781.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 141,420,036.0 | 139,478,215.0 | 148,944,085.0 | 3,712,058.1 | 5 | 23,304 | 19,356 | 19,356 | 0.026 | compiled=5 | 1,576,759.0 | 138,298,569.0 | 204,191.0 |
| `floor` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 147,429,877.0 | 137,109,183.0 | 149,116,775.0 | 5,452,278.7 | 5 | 23,304 | 19,133 | 19,133 | 0.037 | compiled=5 | 1,706,989.0 | 145,745,158.0 | 107,761.0 |
| `floor` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 141,711,338.0 | 139,209,483.0 | 152,721,425.0 | 5,374,774.0 | 5 | 23,304 | 19,356 | 19,356 | 0.038 | compiled=5 | 1,593,108.0 | 139,920,498.0 | 197,881.0 |
| `orig` | `plain` | `pcrec_751b9c6d_auto-caps-simdna` | 170,948,340.0 | 162,246,404.0 | 176,646,581.0 | 5,434,696.4 | 5 | 48,320 | 83,479 | 14,952 | 0.032 | compiled=5 | 10,201,704.0 | 157,190,908.0 | 200,461.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_auto-caps-simdna` | 184,587,183.0 | 175,857,756.0 | 202,110,285.0 | 9,283,126.6 | 5 | 48,456 | 95,690 | 16,868 | 0.050 | compiled=5 | 12,547,796.0 | 171,134,501.0 | 200,881.0 |
| `orig` | `plain` | `pcrec_751b9c6d_auto-nocaps-simdna` | 173,343,853.0 | 164,964,798.0 | 195,040,547.0 | 10,999,416.8 | 5 | 48,320 | 83,479 | 14,952 | 0.063 (max is trial 1) | compiled=5 | 10,212,413.0 | 162,901,409.0 | 194,831.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_auto-nocaps-simdna` | 185,316,116.0 | 183,678,096.0 | 197,207,167.0 | 5,033,881.3 | 5 | 48,456 | 95,690 | 16,868 | 0.027 (max is trial 1) | compiled=5 | 13,009,958.0 | 171,621,184.0 | 107,491.0 |
| `orig` | `plain` | `pcrec_751b9c6d_vm-caps-simdna` | 451,346,230.0 | 445,656,879.0 | 468,099,107.0 | 7,745,808.2 | 5 | 35,992 | 49,131 | 47,690 | 0.017 | compiled=5 | 2,144,891.0 | 449,001,527.0 | 116,940.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_vm-caps-simdna` | 446,200,222.0 | 441,234,595.0 | 465,314,273.0 | 8,474,990.7 | 5 | 35,992 | 49,249 | 47,808 | 0.019 | compiled=5 | 2,121,691.0 | 443,974,881.0 | 104,941.0 |
| `orig` | `plain` | `pcrec_751b9c6d_vm-in-caps-simdna` | 440,170,060.0 | 432,054,367.0 | 452,054,323.0 | 7,025,957.5 | 5 | 35,992 | 49,131 | 47,690 | 0.016 | compiled=5 | 2,130,671.0 | 437,934,009.0 | 204,081.0 |
| `orig` | `whole-subject` | `pcrec_751b9c6d_vm-in-caps-simdna` | 439,169,464.0 | 434,068,269.0 | 460,292,136.0 | 10,513,387.1 | 5 | 35,992 | 49,249 | 47,808 | 0.024 | compiled=5 | 2,171,241.0 | 436,819,872.0 | 200,181.0 |

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

