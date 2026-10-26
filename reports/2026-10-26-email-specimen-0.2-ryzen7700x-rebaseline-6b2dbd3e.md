# pcrec-bench report

reporter: v28 (2026-10-25)

## Query

- filters: subbench=email-specimen, version=0.2, machine=ryzen7700x, since=2026-10-19T03:50:00Z, until=2026-10-20T11:00:00Z
- record source: store/index.tsv (6 record(s) matching this query)
- records included: 6
- worst other-core busy: 0.83% (`pcrec_6b2dbd3e_auto-nocaps-simdna` / `orig` / `short-subject-search`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__ryzen7700x__20261019T045428Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__ryzen7700x__20261019T045428Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261019T044203Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__ryzen7700x__20261019T044203Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261019T041908Z` (store/records/email-specimen@0.2/pcrec_6b2dbd3e_auto-caps-simdna/email-specimen@0.2__pcrec_6b2dbd3e_auto-caps-simdna__ryzen7700x__20261019T041908Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_6b2dbd3e_auto-nocaps-simdna__ryzen7700x__20261019T042608Z` (store/records/email-specimen@0.2/pcrec_6b2dbd3e_auto-nocaps-simdna/email-specimen@0.2__pcrec_6b2dbd3e_auto-nocaps-simdna__ryzen7700x__20261019T042608Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_6b2dbd3e_vm-caps-simdna__ryzen7700x__20261019T043303Z` (store/records/email-specimen@0.2/pcrec_6b2dbd3e_vm-caps-simdna/email-specimen@0.2__pcrec_6b2dbd3e_vm-caps-simdna__ryzen7700x__20261019T043303Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 496 rows; 5 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__rust_1.13.1_default-caps-simdna__ryzen7700x__20261019T050314Z` (store/records/email-specimen@0.2/rust_1.13.1_default-caps-simdna/email-specimen@0.2__rust_1.13.1_default-caps-simdna__ryzen7700x__20261019T050314Z.jsonl) — agreement: agree (0 of 6 groups; 0 of 334 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): ryzen7700x
- schema version(s): 1.8
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 6 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

_[B82] (inbox I-99, Frank's ruling -- a D119 addendum): this report's roster spans BOTH capture classes, so the two views below are the HEADLINE -- "If an engine is run non-capturing on a pattern, then we can't compare that to a capturing engine run -- they are almost completely different things with different objectives." No cell in either view compares across classes; the third, MIXED table further down restates today's single-roster ranking and is never the headline._

## Ranking -- CAPTURING engines only, caps vs caps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,172,962.9 | 0.7959 | 4,170,693.0 | 4,177,091.9 | 2,212.2 | 0.033x | 1.000x | spread | 5 | 100% |
| 2 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 40,728,867.3 | 7.7684 | 40,706,059.4 | 40,795,948.9 | 35,209.8 | 0.318x | 9.760x | **dominated**: `t-d-prose-sparse-addrs` is 90.4% of this set | 5 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 127,935,452.7 | 24.4018 | 126,345,623.2 | 129,093,528.1 | 994,305.6 | 1.000x | 30.658x | spread | 5 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,219,389.0 | 2.1166 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 3,906,556.3 | 3.7256 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 14,372,170.3 | 13.7064 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,464.2 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,704.2 | 0.0073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,940.4 | 0.0076 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,396.2 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,623.5 | 0.0073 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,021.4 | 0.0076 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,930,586.8 | 1.8412 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 36,805,542.9 | 35.1005 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 113,588,453.7 | 108.3264 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,358.3 | 0.0070 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,706.7 | 0.0073 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,952.9 | 0.0076 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,498.4 | 43,460.7 | 43,520.6 | 19.3 | 0.068x | 1.000x | 85 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636,977.8 | 630,479.6 | 652,446.7 | 7,319.9 | 0.998x | 14.644x | 85 | 100% |
| 3 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638,141.3 | 628,861.9 | 650,705.5 | 7,335.8 | 1.000x | 14.670x | 85 | 100% |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,032.9 | 2,030.4 | 2,062.4 | 12.1 | 0.053x | 1.000x | 77 | 26.4 | 6.5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,248.8 | 6,157.7 | 6,437.9 | 108.8 | 0.163x | 3.074x | 77 | 81.2 | 22.9 | 100% |
| 3 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 11,294.7 | 11,280.5 | 11,326.7 | 18.5 | 0.295x | 5.556x | 77 | 146.7 | 6.5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 38,244.2 | 38,075.6 | 39,798.7 | 640.9 | 1.000x | 18.813x | 77 | 496.7 | 32.2 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 342,416.3 | 0.0653 | 341,670.3 | 342,587.4 | 340.8 | 0.259x | 1.000x | spread |
| 2 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 605,603.7 | 0.1155 | 605,117.0 | 605,919.9 | 292.4 | 0.458x | 1.769x | spread |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 966,758.0 | 0.1844 | 916,013.4 | 1,010,244.0 | 32,096.6 | 0.731x | 2.823x | spread |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,322,564.3 | 0.2523 | 1,313,511.7 | 1,545,421.3 | 88,822.6 | 1.000x | 3.862x | **dominated**: `t-a-valid-addrs` is 96.5% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 307,638.8 | 0.2934 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 368,243.6 | 0.3512 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 857,441.4 | 0.8177 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,276,226.6 | 1.2171 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,505.7 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,466.6 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,734.1 | 0.0236 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,610.5 | 0.0073 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,574.9 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,483.9 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,697.7 | 0.0236 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,629.9 | 0.0073 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12,327.1 | 0.0118 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 215,069.6 | 0.2051 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 35,299.2 | 0.0337 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 23,618.7 | 0.0225 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,404.2 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,440.4 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,781.6 | 0.0236 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,647.2 | 0.0073 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.6 | 263.4 | 264.0 | 0.2 | 0.209x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 377.6 | 377.6 | 382.1 | 1.8 | 0.299x | 1.433x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,261.3 | 1,231.7 | 1,265.6 | 14.9 | 0.999x | 4.786x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,262.4 | 1,231.8 | 1,290.0 | 21.1 | 1.000x | 4.790x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 502.7 | 502.3 | 507.3 | 1.9 | 0.203x | 1.000x | 77 | 6.5 | 100% |
| 2 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 503.7 | 503.0 | 510.1 | 2.7 | 0.203x | 1.002x | 77 | 6.5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,765.2 | 1,710.6 | 2,173.8 | 169.9 | 0.712x | 3.511x | 77 | 22.9 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,480.0 | 2,476.3 | 2,486.4 | 3.3 | 1.000x | 4.933x | 77 | 32.2 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,159,394.4 | 0.7933 | 4,157,391.2 | 4,163,492.6 | 2,107.2 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,623,267.3 | 1.4540 | 7,612,695.2 | 7,729,306.1 | 43,487.4 | 0.179x | 1.833x |
| 3 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 9,581,146.5 | 1.8275 | 9,378,244.1 | 9,884,647.9 | 183,672.3 | 0.225x | 2.303x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 42,509,219.7 | 8.1080 | 42,259,092.4 | 43,408,983.4 | 403,077.6 | 1.000x | 10.220x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,206,631.1 | 2.1044 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,624,195.4 | 1.5490 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 1,800,930.9 | 1.7175 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,711,154.2 | 8.3076 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,409.5 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 981,030.1 | 0.9356 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,619.9 | 0.0073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,751.1 | 0.0074 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,439.5 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,067,616.3 | 1.0182 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,555.9 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,644.1 | 0.0073 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,930,578.2 | 1.8411 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,610,268.9 | 2.4893 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,734,261.1 | 7.3760 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 33,848,578.7 | 32.2805 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,455.4 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,351,378.9 | 1.2888 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,581.0 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,657.4 | 0.0073 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32,841.5 | 32,814.1 | 32,958.3 | 58.8 | 0.148x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,422.5 | 43,405.3 | 43,482.8 | 34.7 | 0.195x | 1.322x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220,983.1 | 220,069.6 | 226,027.8 | 2,258.6 | 0.995x | 6.729x |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 222,125.7 | 215,597.1 | 224,620.7 | 3,189.3 | 1.000x | 6.764x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,019.3 | 2,014.9 | 2,022.9 | 2.7 | 0.097x | 1.000x | 77 | 26.2 | 6.5 | 100% |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,699.3 | 2,671.1 | 2,844.9 | 61.5 | 0.129x | 1.337x | 77 | 35.1 | 22.9 | 100% |
| 3 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 3,265.0 | 3,244.3 | 3,278.3 | 11.4 | 0.156x | 1.617x | 77 | 42.4 | 6.5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,881.2 | 20,467.8 | 21,063.5 | 230.9 | 1.000x | 10.341x | 77 | 271.2 | 32.2 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_6b2dbd3e_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |

## Ranking -- NON-CAPTURING engines only, nocaps vs nocaps (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 4,161,789.4 | 0.7938 | 4,159,904.7 | 4,163,307.8 | 1,170.0 | 1.000x | 1.000x |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 2,206,325.7 | 2.1041 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,404.3 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,493.5 | 0.0071 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 1,931,715.8 | 1.8422 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,491.0 | 0.0071 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43,400.8 | 43,395.8 | 43,441.5 | 17.0 | 1.000x | 1.000x |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 2,018.5 | 2,016.8 | 2,019.9 | 1.1 | 1.000x | 1.000x | 77 | 26.2 | 6.5 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 341,554.4 | 0.0651 | 341,371.8 | 341,945.8 | 200.2 | 1.000x | 1.000x | spread |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 439,305.3 | 0.0838 | 438,787.9 | 439,649.6 | 292.2 | 1.286x | 1.286x | **dominated**: `t-a-valid-addrs` is 91.6% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 306,981.5 | 0.2928 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 402,532.8 | 0.3839 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,517.9 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,600.6 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,438.3 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,635.4 | 0.0073 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 12,104.8 | 0.0115 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 13,970.7 | 0.0133 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,487.5 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,566.6 | 0.0072 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: rust_1.13.1_default-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 372.4 | 372.0 | 373.0 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 386.0 | 377.5 | 402.0 | 8.5 | 1.036x | 1.036x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 502.6 | 502.4 | 504.9 | 0.9 | 1.000x | 1.000x | 77 | 6.5 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,527.7 | 2,519.3 | 2,537.3 | 7.0 | 5.029x | 5.029x | 77 | 32.8 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 4,159,595.3 | 0.7934 | 4,157,947.8 | 4,162,171.7 | 1,362.9 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 8,253,740.5 | 1.5743 | 8,249,690.2 | 8,313,403.6 | 24,147.6 | 1.984x | 1.984x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 2,206,333.9 | 2.1041 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 3,544,081.1 | 3.3799 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,449.3 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,169,458.9 | 1.1153 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,538.4 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,165,492.7 | 1.1115 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 1,930,491.1 | 1.8411 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,204,440.2 | 1.1486 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,513.9 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,169,613.1 | 1.1154 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43,397.4 | 43,388.4 | 43,502.4 | 42.1 | 1.000x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 75,500.9 | 75,487.7 | 75,519.4 | 11.2 | 1.740x | 1.740x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_6b2dbd3e_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 2,017.7 | 2,014.0 | 2,021.3 | 2.5 | 1.000x | 1.000x | 77 | 26.2 | 6.5 | 100% |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 6,208.6 | 6,187.2 | 6,728.7 | 207.6 | 3.077x | 3.077x | 77 | 80.6 | 32.8 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Ranking -- MIXED CLASSES, never compare across cells (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 4,161,789.4 | 0.7938 | 4,159,904.7 | 4,163,307.8 | 1,170.0 | 0.033x | 1.000x | spread | 5 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,172,962.9 | 0.7959 | 4,170,693.0 | 4,177,091.9 | 2,212.2 | 0.033x | 1.003x | spread | 5 | 100% |
| 3 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 40,728,867.3 | 7.7684 | 40,706,059.4 | 40,795,948.9 | 35,209.8 | 0.318x | 9.786x | **dominated**: `t-d-prose-sparse-addrs` is 90.4% of this set | 5 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 127,935,452.7 | 24.4018 | 126,345,623.2 | 129,093,528.1 | 994,305.6 | 1.000x | 30.740x | spread | 5 | 100% |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 2,206,325.7 | 2.1041 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,219,389.0 | 2.1166 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 3,906,556.3 | 3.7256 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 14,372,170.3 | 13.7064 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,404.3 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,464.2 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,704.2 | 0.0073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,940.4 | 0.0076 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,493.5 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,396.2 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,623.5 | 0.0073 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,021.4 | 0.0076 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 1,931,715.8 | 1.8422 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,930,586.8 | 1.8412 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 36,805,542.9 | 35.1005 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 113,588,453.7 | 108.3264 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,491.0 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,358.3 | 0.0070 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,706.7 | 0.0073 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,952.9 | 0.0076 |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43,400.8 | 43,395.8 | 43,441.5 | 17.0 | 0.068x | 1.000x | 85 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,498.4 | 43,460.7 | 43,520.6 | 19.3 | 0.068x | 1.002x | 85 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 636,977.8 | 630,479.6 | 652,446.7 | 7,319.9 | 0.998x | 14.677x | 85 | 100% |
| 4 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 638,141.3 | 628,861.9 | 650,705.5 | 7,335.8 | 1.000x | 14.703x | 85 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 2,018.5 | 2,016.8 | 2,019.9 | 1.1 | 0.053x | 1.000x | 77 | 26.2 | 6.5 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,032.9 | 2,030.4 | 2,062.4 | 12.1 | 0.053x | 1.007x | 77 | 26.4 | 6.5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 6,248.8 | 6,157.7 | 6,437.9 | 108.8 | 0.163x | 3.096x | 77 | 81.2 | 22.9 | 100% |
| 4 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 11,294.7 | 11,280.5 | 11,326.7 | 18.5 | 0.295x | 5.596x | 77 | 146.7 | 6.5 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 38,244.2 | 38,075.6 | 39,798.7 | 640.9 | 1.000x | 18.947x | 77 | 496.7 | 32.2 | 100% |

- not ranked: `rust_1.13.1_default-caps-simdna` — did-not-compile (regex build failed [Syntax]: regex parse error:\n    (?:(?<atom>[a-z0-9!#$%&'*+/=?^_`{|}~-]+)){0}(?:(?<qchar>[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])){0}(?:(?<label>[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)){0}(?:(?<octet>25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){0}(?:(?&atom)(?:\\.(?&atom))*|"(?:(?&qchar))*")@(?:(?:(?&label)\\.)+(?&label)|\\[(?:(?:(?&octet))\\.){3}(?:(?&octet)|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\n                                                                                                                                                                                                                                                            ^\nerror: unrecognized flag)

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 341,554.4 | 0.0651 | 341,371.8 | 341,945.8 | 200.2 | 0.258x | 1.000x | spread |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 342,416.3 | 0.0653 | 341,670.3 | 342,587.4 | 340.8 | 0.259x | 1.003x | spread |
| 3 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 439,305.3 | 0.0838 | 438,787.9 | 439,649.6 | 292.2 | 0.332x | 1.286x | **dominated**: `t-a-valid-addrs` is 91.6% of this set |
| 4 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 605,603.7 | 0.1155 | 605,117.0 | 605,919.9 | 292.4 | 0.458x | 1.773x | spread |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 966,758.0 | 0.1844 | 916,013.4 | 1,010,244.0 | 32,096.6 | 0.731x | 2.830x | spread |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,322,564.3 | 0.2523 | 1,313,511.7 | 1,545,421.3 | 88,822.6 | 1.000x | 3.872x | **dominated**: `t-a-valid-addrs` is 96.5% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 306,981.5 | 0.2928 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 307,638.8 | 0.2934 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 402,532.8 | 0.3839 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 368,243.6 | 0.3512 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 857,441.4 | 0.8177 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 1,276,226.6 | 1.2171 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,517.9 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,505.7 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,600.6 | 0.0072 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,466.6 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,734.1 | 0.0236 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,610.5 | 0.0073 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,438.3 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,574.9 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,635.4 | 0.0073 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,483.9 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,697.7 | 0.0236 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,629.9 | 0.0073 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 12,104.8 | 0.0115 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 12,327.1 | 0.0118 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 13,970.7 | 0.0133 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 215,069.6 | 0.2051 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 35,299.2 | 0.0337 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 23,618.7 | 0.0225 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,487.5 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,404.2 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 7,566.6 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,440.4 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 24,781.6 | 0.0236 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,647.2 | 0.0073 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 263.6 | 263.4 | 264.0 | 0.2 | 0.209x | 1.000x |
| 2 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 372.4 | 372.0 | 373.0 | 0.4 | 0.295x | 1.413x |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 377.6 | 377.6 | 382.1 | 1.8 | 0.299x | 1.433x |
| 4 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 386.0 | 377.5 | 402.0 | 8.5 | 0.306x | 1.464x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,261.3 | 1,231.7 | 1,265.6 | 14.9 | 0.999x | 4.786x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 1,262.4 | 1,231.8 | 1,290.0 | 21.1 | 1.000x | 4.790x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 502.6 | 502.4 | 504.9 | 0.9 | 0.203x | 1.000x | 77 | 6.5 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 502.7 | 502.3 | 507.3 | 1.9 | 0.203x | 1.000x | 77 | 6.5 | 100% |
| 3 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 503.7 | 503.0 | 510.1 | 2.7 | 0.203x | 1.002x | 77 | 6.5 | 100% |
| 4 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 1,765.2 | 1,710.6 | 2,173.8 | 169.9 | 0.712x | 3.512x | 77 | 22.9 | 100% |
| 5 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 2,480.0 | 2,476.3 | 2,486.4 | 3.3 | 1.000x | 4.934x | 77 | 32.2 | 100% |
| 6 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 2,527.7 | 2,519.3 | 2,537.3 | 7.0 | 1.019x | 5.029x | 77 | 32.8 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 4,159,394.4 | 0.7933 | 4,157,391.2 | 4,163,492.6 | 2,107.2 | 0.098x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 4,159,595.3 | 0.7934 | 4,157,947.8 | 4,162,171.7 | 1,362.9 | 0.098x | 1.000x |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 7,623,267.3 | 1.4540 | 7,612,695.2 | 7,729,306.1 | 43,487.4 | 0.179x | 1.833x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 8,253,740.5 | 1.5743 | 8,249,690.2 | 8,313,403.6 | 24,147.6 | 0.194x | 1.984x |
| 5 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 9,581,146.5 | 1.8275 | 9,378,244.1 | 9,884,647.9 | 183,672.3 | 0.225x | 2.303x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 42,509,219.7 | 8.1080 | 42,259,092.4 | 43,408,983.4 | 403,077.6 | 1.000x | 10.220x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 2,206,631.1 | 2.1044 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 2,206,333.9 | 2.1041 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,624,195.4 | 1.5490 |
| `t-a-valid-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 3,544,081.1 | 3.3799 |
| `t-a-valid-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 1,800,930.9 | 1.7175 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 8,711,154.2 | 8.3076 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,409.5 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,449.3 | 0.0071 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 981,030.1 | 0.9356 |
| `t-b-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,169,458.9 | 1.1153 |
| `t-b-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,619.9 | 0.0073 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,751.1 | 0.0074 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,439.5 | 0.0071 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,538.4 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,067,616.3 | 1.0182 |
| `t-c-long-atom-run` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,165,492.7 | 1.1115 |
| `t-c-long-atom-run` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,555.9 | 0.0072 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,644.1 | 0.0073 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 1,930,578.2 | 1.8411 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 1,930,491.1 | 1.8411 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,610,268.9 | 2.4893 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,204,440.2 | 1.1486 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,734,261.1 | 7.3760 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 33,848,578.7 | 32.2805 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-caps-simdna` | 7,455.4 | 0.0071 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 7,513.9 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,351,378.9 | 1.2888 |
| `t-e-prose-no-at` | 1,048,576 | `rust_1.13.1_default-caps-simdna` | 1,169,613.1 | 1.1154 |
| `t-e-prose-no-at` | 1,048,576 | `pcrec_6b2dbd3e_vm-caps-simdna` | 7,581.0 | 0.0072 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 7,657.4 | 0.0073 |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
_rows compare different programs answering the same regime; rank order is real, the ratio between forms is a regime artifact until an end-anchored entry exists (pcrec [OS-4])._

| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `whole-subject` | separate artifact | 32,841.5 | 32,814.1 | 32,958.3 | 58.8 | 0.148x | 1.000x |
| 2 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `whole-subject` | separate artifact | 43,397.4 | 43,388.4 | 43,502.4 | 42.1 | 0.195x | 1.321x |
| 3 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `whole-subject` | separate artifact | 43,422.5 | 43,405.3 | 43,482.8 | 34.7 | 0.195x | 1.322x |
| 4 | `rust_1.13.1_default-caps-simdna` | measured | `whole-subject` | separate artifact | 75,500.9 | 75,487.7 | 75,519.4 | 11.2 | 0.340x | 2.299x |
| 5 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 220,983.1 | 220,069.6 | 226,027.8 | 2,258.6 | 0.995x | 6.729x |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 222,125.7 | 215,597.1 | 224,620.7 | 3,189.3 | 1.000x | 6.764x |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | form | fact | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_6b2dbd3e_auto-nocaps-simdna` | measured | `plain` | same program | 2,017.7 | 2,014.0 | 2,021.3 | 2.5 | 0.097x | 1.000x | 77 | 26.2 | 6.5 | 100% |
| 2 | `pcrec_6b2dbd3e_auto-caps-simdna` | measured | `plain` | same program | 2,019.3 | 2,014.9 | 2,022.9 | 2.7 | 0.097x | 1.001x | 77 | 26.2 | 6.5 | 100% |
| 3 | `libpcre2_10.46_jit-caps-simdna` | measured | `plain` | same program | 2,699.3 | 2,671.1 | 2,844.9 | 61.5 | 0.129x | 1.338x | 77 | 35.1 | 22.9 | 100% |
| 4 | `pcrec_6b2dbd3e_vm-caps-simdna` | measured | `plain` | same program | 3,265.0 | 3,244.3 | 3,278.3 | 11.4 | 0.156x | 1.618x | 77 | 42.4 | 6.5 | 100% |
| 5 | `rust_1.13.1_default-caps-simdna` | measured | `plain` | same program | 6,208.6 | 6,187.2 | 6,728.7 | 207.6 | 0.297x | 3.077x | 77 | 80.6 | 32.8 | 100% |
| 6 | `libpcre2_10.46_interp-caps-simdna` | measured | `plain` | same program | 20,881.2 | 20,467.8 | 21,063.5 | 230.9 | 1.000x | 10.349x | 77 | 271.2 | 32.2 | 100% |

- `rust_1.13.1_default-caps-simdna` is classified `no` for the capture-class views despite its own id token: the timed loop is find_at-driven (no per-match capture assignment) with exactly ONE captures_at call on the FIRST match per timed call, for verification only -- a DECLARED fixed per-call cost, never a per-match capture assignment (src/main.rs:255-266); the config's own `captures=on` (its id says `-caps-`) names the engine's capability, not this run's behaviour (I-99 (rust-default QUESTION) / I-100 RULING (2): retires once rust-find (NO) / rust-captures (YES) land as separate configs)

## Excluded from ranking (expectation-failing cells)

| pattern | regime | form | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |
| `factored` | `match-compliance` | `whole-subject` | `pcrec_6b2dbd3e_vm-caps-simdna` | 85 | 94% | -3:PCREC_ERR_FRAMES×5 (smallest: s-061, 2,008 B) | 0 | `s-058` (gave-up), `s-059` (gave-up), `s-061` (gave-up), `s-063` (gave-up), `s-064` (gave-up) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**4 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `floor` | `match-compliance` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 386.0 | `pcrec_6b2dbd3e_auto-caps-simdna` | 377.6 | 0.978x | within IQR: gap 2.16%; IQR 2.55% (within); no null band (no cross-pin pair in this report) |
| `floor` | `match-compliance` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 386.0 | `pcrec_6b2dbd3e_vm-caps-simdna` | 263.6 | 0.683x | clears IQR only: gap 31.71%; IQR 2.55% (clears); no null band (no cross-pin pair in this report) |
| `orig` | `large-subject-throughput` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 4,159,595.3 | `pcrec_6b2dbd3e_auto-caps-simdna` | 4,159,394.4 | 1.000x | within IQR: gap 0.00%; IQR 0.03% (within); no null band (no cross-pin pair in this report) |
| `orig` | `match-compliance` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 43,397.4 | `pcrec_6b2dbd3e_vm-caps-simdna` | 32,841.5 | 0.757x | clears IQR only: gap 24.32%; IQR 0.24% (clears); no null band (no cross-pin pair in this report) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_6b2dbd3e_vm-caps-simdna` / `factored` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 39,958 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_vm-caps-simdna` / `factored` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 40,066 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=54/81 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_vm-caps-simdna` / `floor` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 236 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_6b2dbd3e_vm-caps-simdna` / `floor` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=1, islands=0, shape=forward (prog: 339 B), clsfolds=0, rungs=-, K=8/default, caps=500,000/1,000,000, fast tier=1/1 == stamped default (single tier), buffers=1/1 (stamped default), frame=24
- `pcrec_6b2dbd3e_vm-caps-simdna` / `orig` / `plain`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 29,251 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
- `pcrec_6b2dbd3e_vm-caps-simdna` / `orig` / `whole-subject`: engine=vm, sel=forced, entry=plain entry, vm_prefilter=none, dfa: no DFA scan (rx_info.scan NULL: not a hybrid), edges=0 (match: 0), frameless=0, islands=0, shape=plain (prog: 29,361 B), clsfolds=0, rungs=PCREC_VM_RUNG_CURSOR|PCREC_VM_RUNG_FRAMES_BOUNDED|PCREC_VM_RUNG_FRAMES_UNBOUNDED, K=8/default, caps=500,000/1,000,000, fast tier=61/92 fast, escalates to 2048/3072, buffers=2048/3072 (stamped default), frame=24
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - K = pcrec's `RX_UNROLL_K`/`_WHY`: the VM counter rung's unroll factor and who chose it (default / option / denied / size-model / size-model-declined / cap-rescue / capacity-declined -- limits.md 8); caps = the EFFECTIVE `RX_MAX_EMIT_CODE_BYTES`/`RX_MAX_EMIT_BYTES` the artifact was built under (raise-only; 500,000/1,000,000 by default). VM artifacts only: a DFA artifact has no counter rung and stamps no code cap.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
    - frameless = pcrec's `RX_VM_FRAMELESS` ([OPT-VMFL], abi 16+): `1` iff this VM program emits NO push site and no linked call, so its fail label carries no pop-and-resume dispatch; `0` otherwise. VM artifacts only, hybrids included -- a DIFFERENT scope from `start=`, though the two stamps arrived at one abi. It is NOT `buffers=`'s resume-frame CAPACITY and the two can disagree: the capacity is what the artifact was SIZED for, this is what its program CONTAINS. `0` is a real, recorded value.
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.
    - islands = pcrec's `RX_VM_ALT_ISLANDS` ([ENG-ISL] STEP 1, abi 18+): how many of this VM program's flat alternations were lowered as an ALTERNATION ISLAND -- a trie dispatch over the alternatives' literal bytes -- instead of vm_alt's serial resume chain (one frame per untried branch). Selected per alternation on its LANGUAGE (a finite literal set), so a COUNT; a caseless, prefix-bearing-under-four-words or over-budget alternation is declined as a selection outcome. This is what removes the branch-ORDER effect (altwide srt-256 vs w-256) at the source; `-fno-alt-island` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.
    - shape = pcrec's `RX_VM_ENTRY_SHAPE` with `RX_VM_PROGRAM_BYTES` in the parenthetical ([CC-DIFF] STEP 2, abi 22+): the entry-chain rung the emitter TOOK for the six entries -- `plain` (one body, six framed entries), `shared` (one out-of-line body behind three forwarding entries), `forward` (three bodies in the three `_in` entries, no canary anywhere), `inline` (six bodies) -- and the program size AUTO compared against VM_INLINE_CHAIN_MAX_BYTES (4,096 B) to choose it: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal (the program writes its storage); a FRAMED program (`frameless=0`) is `plain` whatever the size. ANSWER-IDENTICAL across every value -- only the scaffolding above the first label moves -- so a COST and SIZE fact; the number is what makes the token checkable. `prog: N B` is the VM PROGRAM REGION with its COMMENTS INCLUDED (the raw length of the emitter's program buffer; the island trie writes a per-node comment), NOT the `code bytes` columns' quantity -- those and `--max-emit-code-bytes` count the whole .c+.h with every comment EXCLUDED -- so the program stamp can exceed the code bytes (w-256: 305,686 vs 292,043) and neither is wrong; for cap reasoning use the code bytes (pcrec I-50 1).
    - clsfolds = pcrec's `RX_VM_CLS_FOLDS` ([FORM-CHAR] STEP 1, abi 23+): how many of this VM program's class-pool entries take the ASCII-FOLD membership test -- a two-member set differing only in bit 0x20, both letters (what `(?i)` makes of a letter at parse time), tested as `(byte | 0x20) == lower` with NO 32-byte bitmap table emitted for it. Chosen per pool class, so a COUNT; a set that is not exactly two members, not a 0x20 pair, or a 0x20 pair of non-letters keeps its bitmap. A SIZE fact (one table per fold class gone, plus the test text), never an answer one: the fold compare and the bitmap read are the same predicate over the pair's two bytes. VM route only -- an `auto` row that selected the DFA prints no clause even on a `(?i)` pattern; `-fno-cls-fold` is the sibling that reads `0` at the same pin. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 78,408,732.0 | 77,852,616.0 | 78,837,014.0 | 360,463.3 | 5 | 49,472 | 85,071 | 16,377 | 0.005 | compiled=5 | 4,329,205.0 | 73,897,334.0 | 51,426.0 |
| `factored` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 72,512,194.0 | 71,908,852.0 | 73,051,176.0 | 392,585.5 | 5 | 37,040 | 42,326 | 16,649 | 0.005 (max is trial 1) | compiled=5 | 3,745,199.0 | 68,692,084.0 | 51,477.0 |
| `factored` | `plain` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 75,967,261.0 | 75,431,844.0 | 76,562,907.0 | 435,970.8 | 5 | 49,472 | 84,868 | 16,170 | 0.006 | compiled=5 | 4,084,310.0 | 72,012,907.0 | 50,425.0 |
| `factored` | `whole-subject` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 71,411,013.0 | 70,451,906.0 | 71,898,061.0 | 551,341.8 | 5 | 37,040 | 42,143 | 16,462 | 0.008 | compiled=5 | 3,701,037.0 | 67,579,620.0 | 42,781.0 |
| `factored` | `plain` | `pcrec_6b2dbd3e_vm-caps-simdna` | 238,610,165.0 | 238,452,307.0 | 239,697,704.0 | 557,386.2 | 5 | 45,384 | 61,983 | 60,375 | 0.002 | compiled=5 | 1,961,927.0 | 236,625,133.0 | 52,569.0 |
| `factored` | `whole-subject` | `pcrec_6b2dbd3e_vm-caps-simdna` | 239,446,341.0 | 238,773,072.0 | 240,088,371.0 | 436,852.4 | 5 | 45,384 | 62,099 | 60,491 | 0.002 | compiled=5 | 2,112,462.0 | 237,238,560.0 | 51,988.0 |
| `floor` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 64,711,033.0 | 64,508,323.0 | 65,438,738.0 | 348,011.3 | 5 | 28,768 | 17,888 | 14,557 | 0.005 (max is trial 1) | compiled=5 | 1,085,127.0 | 63,555,724.0 | 52,559.0 |
| `floor` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 66,425,471.0 | 65,844,389.0 | 67,712,426.0 | 648,855.9 | 5 | 28,808 | 19,474 | 15,916 | 0.010 | compiled=5 | 950,063.0 | 65,446,583.0 | 53,320.0 |
| `floor` | `plain` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 65,546,768.0 | 64,747,302.0 | 65,933,116.0 | 396,855.6 | 5 | 28,768 | 17,888 | 14,557 | 0.006 (max is trial 1) | compiled=5 | 1,028,970.0 | 64,521,956.0 | 53,010.0 |
| `floor` | `whole-subject` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 66,673,633.0 | 66,070,074.0 | 67,870,068.0 | 718,791.4 | 5 | 28,808 | 19,474 | 15,916 | 0.011 (max is trial 1) | compiled=5 | 1,040,171.0 | 65,579,620.0 | 52,770.0 |
| `floor` | `plain` | `pcrec_6b2dbd3e_vm-caps-simdna` | 65,953,840.0 | 65,832,612.0 | 67,439,932.0 | 706,548.1 | 5 | 28,552 | 22,213 | 20,745 | 0.011 (max is trial 1) | compiled=5 | 1,070,187.0 | 64,972,861.0 | 49,393.0 |
| `floor` | `whole-subject` | `pcrec_6b2dbd3e_vm-caps-simdna` | 68,223,189.0 | 67,494,454.0 | 69,344,250.0 | 648,177.9 | 5 | 28,552 | 22,436 | 20,968 | 0.010 (max is trial 1) | compiled=5 | 996,338.0 | 67,240,927.0 | 48,751.0 |
| `orig` | `plain` | `pcrec_6b2dbd3e_auto-caps-simdna` | 76,080,872.0 | 75,089,731.0 | 76,218,470.0 | 436,249.8 | 5 | 49,440 | 84,644 | 16,117 | 0.006 | compiled=5 | 3,980,942.0 | 72,019,810.0 | 53,280.0 |
| `orig` | `whole-subject` | `pcrec_6b2dbd3e_auto-caps-simdna` | 69,899,380.0 | 69,563,199.0 | 71,347,579.0 | 692,669.4 | 5 | 32,904 | 41,919 | 16,409 | 0.010 (max is trial 1) | compiled=5 | 3,544,192.0 | 66,298,952.0 | 47,018.0 |
| `orig` | `plain` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 76,129,018.0 | 74,714,201.0 | 76,630,453.0 | 703,317.4 | 5 | 49,440 | 84,644 | 16,117 | 0.009 | compiled=5 | 4,039,135.0 | 71,772,074.0 | 47,169.0 |
| `orig` | `whole-subject` | `pcrec_6b2dbd3e_auto-nocaps-simdna` | 70,632,275.0 | 70,058,133.0 | 71,199,885.0 | 364,080.8 | 5 | 32,904 | 41,919 | 16,409 | 0.005 | compiled=5 | 3,636,746.0 | 66,761,648.0 | 52,268.0 |
| `orig` | `plain` | `pcrec_6b2dbd3e_vm-caps-simdna` | 193,423,395.0 | 192,241,128.0 | 193,513,016.0 | 485,422.9 | 5 | 41,248 | 52,623 | 49,714 | 0.003 | compiled=5 | 1,847,792.0 | 191,529,466.0 | 50,224.0 |
| `orig` | `whole-subject` | `pcrec_6b2dbd3e_vm-caps-simdna` | 191,218,571.0 | 190,278,658.0 | 191,663,480.0 | 471,495.8 | 5 | 37,152 | 52,741 | 49,832 | 0.002 | compiled=5 | 1,833,195.0 | 189,332,326.0 | 51,187.0 |

### `eager-jit`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 37,161.0 | 22,423.0 | 99,577.0 | 28,243.2 | 5 | 951 | 0.760 (max is trial 1) | compiled=5 |
| `factored` | `plain` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `factored` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | - | - | - | - | 0 | - |  | did-not-compile=1 |
| `floor` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 2,103.0 | 1,663.0 | 26,980.0 | 9,911.2 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `rust_1.13.1_default-caps-simdna` | 1,834.0 | 851.0 | 99,257.0 | 39,074.3 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 5,079.0 | 3,737.0 | 108,705.0 | 41,368.8 | 5 | - | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_jit-caps-simdna` | 19,817.0 | 16,601.0 | 95,570.0 | 30,265.5 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `rust_1.13.1_default-caps-simdna` | 70,733.0 | 65,232.0 | 262,836.0 | 75,760.0 | 5 | - | 1.071 (max is trial 1) | compiled=5 |
| `orig` | `whole-subject` | `rust_1.13.1_default-caps-simdna` | 71,504.0 | 63,460.0 | 226,657.0 | 62,076.4 | 5 | - | 0.868 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,029.0 | 3,977.0 | 26,069.0 | 8,453.9 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 261.0 | 180.0 | 11,301.0 | 4,417.9 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `plain` | `libpcre2_10.46_interp-caps-simdna` | 5,150.0 | 4,048.0 | 27,031.0 | 8,837.9 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

