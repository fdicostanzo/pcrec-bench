# pcrec-bench report

reporter: v26 (2026-10-13)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, since=2026-10-12T00:00:00Z, until=2026-10-13T23:59:59Z, testee=libpcre2_10.46_jit-caps-simdna, testee=libpcre2_10.46_interp-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 2.27% (`libpcre2_10.46_jit-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20261013T114535Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20261013T114535Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20261013T113318Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20261013T113318Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.8
- grain: set (sum of per-subject ns/call over the whole subject set, reduced over trials; a set cell is excluded if ANY subject in it fails)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x regime, SET grain: sum over the subject set; best median first)

### `factored` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | n subjects | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 404,433,533.7 | 77.1396 | 402,608,474.4 | 408,031,242.3 | 2,057,771.9 | 1.000x | 1.000x | 5 | 100% |

#### `factored` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 50,961,503.9 | 48.6007 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,869.7 | 0.0180 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,664.3 | 0.0178 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 353,473,455.7 | 337.0986 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,664.5 | 0.0178 |

### `factored` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,427,455.3 | 1,419,977.0 | 1,462,149.9 | 15,514.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,428,257.3 | 1,420,244.4 | 1,437,741.5 | 6,526.2 | 1.001x | 1.001x |

### `factored` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 15,251.6 | 15,228.9 | 15,265.2 | 12.8 | 0.116x | 1.000x | 77 | 198.1 | 42.6 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 131,621.1 | 131,193.1 | 168,643.3 | 14,699.5 | 1.000x | 8.630x | 77 | 1,709.4 | 91.2 | 100% |

### `floor` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best | set composition |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,892,625.7 | 0.3610 | 1,877,046.8 | 1,937,575.7 | 21,492.3 | 0.499x | 1.000x | **dominated**: `t-a-valid-addrs` is 90.1% of this set |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,791,549.5 | 0.7232 | 3,781,040.5 | 4,589,218.4 | 339,627.5 | 1.000x | 2.003x | **dominated**: `t-a-valid-addrs` is 96.7% of this set |

_**dominated**: for the flagged testee(s), one subject is more than 90 % of the set total, so the `vs baseline` / `vs best` ratios on those rows are ratios of that ONE subject wearing the set's name. The set number is still the set's; the per-subject rows below carry the other reading, and they can point the opposite way -- pcrec I-7 §1 measured a set ratio of 3.15x slower that was 7.7x slower on one subject and 144x FASTER on the other two._

#### `floor` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 1,705,178.5 | 1.6262 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 3,666,197.7 | 3.4964 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,309.1 | 0.0375 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,749.9 | 0.0169 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,251.9 | 0.0374 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,732.3 | 0.0169 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 69,668.6 | 0.0664 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 72,064.7 | 0.0687 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 39,659.9 | 0.0378 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,728.9 | 0.0169 |

### `floor` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,580.2 | 2,560.8 | 2,606.0 | 19.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 2,580.6 | 2,565.9 | 2,588.9 | 7.8 | 1.000x | 1.000x |

### `floor` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp (floor control — per-call overhead, not a ranking of engines)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 3,280.5 | 3,261.2 | 3,423.6 | 64.1 | 0.467x | 1.000x | 77 | 42.6 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 7,022.7 | 6,930.4 | 7,267.6 | 117.4 | 1.000x | 2.141x | 77 | 91.2 | 100% |

### `orig` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | ns/byte | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 18,168,002.4 | 3.4653 | 18,100,024.6 | 18,363,541.6 | 93,000.9 | 0.149x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 122,147,725.5 | 23.2978 | 121,871,542.6 | 145,036,623.6 | 9,020,029.0 | 1.000x | 6.723x |

#### `orig` / `large-subject-throughput` per-subject (email-specimen@0.2)

| subject | bytes | testee | median ns/call | ns/byte |
|---|---|---|---|---|
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,715,144.1 | 3.5430 |
| `t-a-valid-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 28,906,360.6 | 27.5673 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,544,231.2 | 2.4264 |
| `t-b-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,000.7 | 0.0172 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 2,818,144.0 | 2.6876 |
| `t-c-long-atom-run` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 17,952.5 | 0.0171 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 5,960,488.6 | 5.6844 |
| `t-d-prose-sparse-addrs` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 93,187,403.6 | 88.8704 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_jit-caps-simdna` | 3,156,052.2 | 3.0098 |
| `t-e-prose-no-at` | 1,048,576 | `libpcre2_10.46_interp-caps-simdna` | 18,018.3 | 0.0172 |

### `orig` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 532,667.3 | 531,523.6 | 542,220.8 | 4,209.4 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 537,439.0 | 533,693.4 | 553,885.0 | 7,058.0 | 1.000x | 1.009x |

### `orig` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best | n subjects | per-subject mean ns | floor ns | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 6,349.9 | 6,323.8 | 6,505.3 | 65.3 | 0.096x | 1.000x | 77 | 82.5 | 42.6 | 100% |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 66,244.9 | 65,755.0 | 66,669.6 | 330.3 | 1.000x | 10.432x | 77 | 860.3 | 91.2 | 100% |

## Excluded from ranking (expectation-failing cells)

| pattern | regime | testee | n subjects | pass-rate | gave-up | wrong | failing subjects (reason) |
|---|---|---|---|---|---|---|---|
| `factored` | `large-subject-throughput` | `libpcre2_10.46_jit-caps-simdna` | 5 | 80% | 0 | 0 | `t-c-long-atom-run` (timed-out) |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

_0 hits: no included YES-class config's median beats any pcrec `auto-nocaps` row's median in this report's roster._

## Compile cost (by execution-model class; never pooled across classes)

### `eager-jit`

| pattern | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `libpcre2_10.46_jit-caps-simdna` | 73,858.0 | 65,090.0 | 155,501.0 | 33,398.3 | 5 | 951 | 0.452 (max is trial 1) | compiled=5 |
| `floor` | `libpcre2_10.46_jit-caps-simdna` | 6,310.0 | 5,001.0 | 54,070.0 | 19,166.2 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `libpcre2_10.46_jit-caps-simdna` | 59,620.0 | 54,641.0 | 182,099.0 | 49,089.4 | 5 | 1,609 | 0.823 (max is trial 1) | compiled=5 |

### `interpretive`

| pattern | testee | median total_ns | min | max | stddev | n costed | artifact bytes | jitter | outcomes |
|---|---|---|---|---|---|---|---|---|---|
| `factored` | `libpcre2_10.46_interp-caps-simdna` | 14,710.0 | 13,070.0 | 43,870.0 | 11,773.1 | 5 | 951 | timer-floor (max is trial 1) | compiled=5 |
| `floor` | `libpcre2_10.46_interp-caps-simdna` | 360.0 | 320.0 | 15,080.0 | 5,879.5 | 5 | 161 | timer-floor (max is trial 1) | compiled=5 |
| `orig` | `libpcre2_10.46_interp-caps-simdna` | 13,530.0 | 12,140.0 | 46,840.0 | 13,409.0 | 5 | 1,609 | timer-floor (max is trial 1) | compiled=5 |

