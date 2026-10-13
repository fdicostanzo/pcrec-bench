# pcrec-bench report

reporter: v26 (2026-10-13)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, since=2026-10-12T00:00:00Z, testee=libpcre2_10.46_jit-caps-simdna, testee=libpcre2_10.46_interp-caps-simdna
- record source: store/index.tsv (2 record(s) matching this query)
- records included: 2
- worst other-core busy: 2.27% (`libpcre2_10.46_jit-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20261013T114535Z` (store/records/email-specimen@0.2/libpcre2_10.46_interp-caps-simdna/email-specimen@0.2__libpcre2_10.46_interp-caps-simdna__budu-ryzen1600__20261013T114535Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20261013T113318Z` (store/records/email-specimen@0.2/libpcre2_10.46_jit-caps-simdna/email-specimen@0.2__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20261013T113318Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 500 rows; 1 unjudged (1 all-timed-out); k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.8
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 2 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 876.3 | 867.7 | 884.2 | 6.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 876.5 | 863.7 | 891.3 | 9.5 | 1.000x | 1.000x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 150.4 | 150.1 | 151.1 | 0.4 | 0.172x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 872.9 | 867.3 | 1,144.8 | 108.5 | 1.000x | 5.805x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,178.9 | 1,166.4 | 1,195.7 | 10.8 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,179.8 | 1,165.8 | 1,195.6 | 10.2 | 1.000x | 1.001x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 165.0 | 164.5 | 167.9 | 1.3 | 0.141x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,172.7 | 1,167.5 | 1,728.0 | 222.0 | 1.000x | 7.107x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 761.0 | 758.2 | 788.5 | 11.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 762.2 | 759.4 | 767.3 | 2.6 | 1.002x | 1.002x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 122.3 | 120.9 | 123.9 | 1.2 | 0.160x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 762.9 | 760.0 | 1,055.4 | 117.3 | 1.000x | 6.238x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,193.3 | 1,170.6 | 1,212.3 | 13.7 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,194.3 | 1,187.3 | 1,216.5 | 10.8 | 1.000x | 1.001x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 177.8 | 176.5 | 179.5 | 1.0 | 0.148x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,198.0 | 1,184.7 | 1,751.2 | 221.7 | 1.000x | 6.740x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 884.9 | 875.8 | 892.8 | 5.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 890.2 | 886.9 | 892.7 | 2.3 | 1.006x | 1.006x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 161.8 | 161.5 | 163.0 | 0.6 | 0.183x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 886.7 | 882.5 | 1,183.8 | 119.0 | 1.000x | 5.479x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 764.0 | 752.7 | 779.6 | 9.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 765.1 | 749.7 | 781.9 | 10.5 | 1.001x | 1.001x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 121.8 | 120.2 | 124.1 | 1.5 | 0.160x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 762.7 | 746.3 | 1,058.5 | 120.6 | 1.000x | 6.260x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,357.6 | 1,354.6 | 1,378.0 | 8.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,364.6 | 1,341.6 | 1,389.4 | 16.1 | 1.005x | 1.005x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 161.1 | 158.6 | 163.6 | 1.7 | 0.118x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,364.9 | 1,345.8 | 1,954.0 | 237.8 | 1.000x | 8.474x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 961.1 | 956.6 | 965.7 | 3.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 961.7 | 942.2 | 973.4 | 10.2 | 1.001x | 1.001x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 166.2 | 160.5 | 168.6 | 2.9 | 0.172x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 964.2 | 950.2 | 987.3 | 13.0 | 1.000x | 5.803x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 874.6 | 857.7 | 878.3 | 7.7 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 884.8 | 868.1 | 902.6 | 11.0 | 1.000x | 1.012x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 157.3 | 155.5 | 159.7 | 1.4 | 0.179x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 880.3 | 863.3 | 929.0 | 22.5 | 1.000x | 5.597x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 862.5 | 858.1 | 873.1 | 6.0 | 0.983x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 877.8 | 860.8 | 880.7 | 7.3 | 1.000x | 1.018x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 147.0 | 140.7 | 148.2 | 2.7 | 0.168x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 873.3 | 863.6 | 1,223.9 | 141.5 | 1.000x | 5.941x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 725.5 | 720.1 | 726.4 | 2.7 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 726.9 | 721.8 | 735.4 | 4.6 | 1.000x | 1.002x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 115.0 | 114.5 | 117.7 | 1.2 | 0.159x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 724.8 | 723.4 | 976.2 | 100.6 | 1.000x | 6.301x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 604.5 | 597.7 | 608.4 | 3.9 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 613.7 | 597.5 | 625.7 | 11.0 | 1.000x | 1.015x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 429.8 | 427.3 | 430.9 | 1.2 | 0.102x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 4,208.9 | 4,145.5 | 5,083.6 | 361.7 | 1.000x | 9.793x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,082.1 | 1,078.3 | 1,098.0 | 6.9 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,091.9 | 1,071.5 | 1,115.9 | 16.3 | 1.000x | 1.009x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 171.4 | 171.2 | 172.5 | 0.5 | 0.156x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,098.2 | 1,084.7 | 1,116.6 | 10.3 | 1.000x | 6.408x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,083.9 | 1,077.2 | 1,092.6 | 5.0 | 0.987x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,098.3 | 1,069.0 | 1,115.8 | 17.0 | 1.000x | 1.013x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 171.5 | 171.0 | 172.4 | 0.5 | 0.156x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,097.8 | 1,079.6 | 1,126.2 | 15.7 | 1.000x | 6.400x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 866.1 | 860.2 | 883.2 | 7.8 | 0.989x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 875.8 | 863.5 | 885.4 | 7.5 | 1.000x | 1.011x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 152.2 | 151.1 | 152.8 | 0.5 | 0.172x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 882.9 | 862.6 | 1,183.0 | 122.7 | 1.000x | 5.802x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,039.4 | 1,031.6 | 1,055.4 | 9.0 | 0.984x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,056.1 | 1,026.7 | 1,070.2 | 17.1 | 1.000x | 1.016x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 165.3 | 164.5 | 166.7 | 0.9 | 0.156x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,058.8 | 1,047.0 | 1,673.6 | 247.4 | 1.000x | 6.406x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 359.1 | 354.9 | 363.0 | 3.0 | 0.983x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 365.5 | 357.4 | 371.4 | 5.2 | 1.000x | 1.018x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 253.2 | 251.6 | 254.5 | 1.1 | 0.112x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,263.3 | 2,226.8 | 3,917.5 | 666.5 | 1.000x | 8.938x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,079.6 | 1,062.4 | 1,088.6 | 9.3 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,083.6 | 1,073.7 | 1,106.6 | 12.0 | 1.000x | 1.004x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 171.8 | 171.3 | 173.6 | 0.8 | 0.156x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,101.7 | 1,069.1 | 1,722.7 | 252.7 | 1.000x | 6.412x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,040.6 | 1,030.1 | 1,060.3 | 10.6 | 0.983x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,058.5 | 1,027.9 | 1,077.6 | 19.3 | 1.000x | 1.017x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 164.8 | 162.1 | 167.0 | 2.0 | 0.156x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,054.2 | 1,047.4 | 1,672.3 | 247.8 | 1.000x | 6.397x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 383.8 | 380.5 | 392.5 | 4.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 387.5 | 381.0 | 394.7 | 5.1 | 1.009x | 1.009x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 254.4 | 249.7 | 258.7 | 3.5 | 0.106x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,396.3 | 2,365.9 | 4,111.3 | 687.5 | 1.000x | 9.420x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,105.4 | 1,099.5 | 1,112.7 | 4.4 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,116.6 | 1,092.8 | 1,132.8 | 14.7 | 1.000x | 1.010x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 174.6 | 174.0 | 175.5 | 0.6 | 0.157x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,112.9 | 1,092.7 | 1,538.7 | 171.3 | 1.000x | 6.374x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,147.8 | 1,144.7 | 1,164.6 | 7.1 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,165.0 | 1,143.6 | 1,195.5 | 16.7 | 1.000x | 1.015x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 124.5 | 123.9 | 125.6 | 0.6 | 0.106x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,170.0 | 1,154.3 | 1,187.3 | 10.8 | 1.000x | 9.400x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 662.6 | 654.6 | 674.9 | 6.5 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 672.9 | 659.9 | 685.3 | 8.7 | 1.000x | 1.016x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 99.7 | 99.3 | 101.8 | 0.9 | 0.147x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 679.8 | 665.7 | 1,173.5 | 199.4 | 1.000x | 6.817x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,131.4 | 1,123.6 | 1,145.8 | 8.3 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,145.3 | 1,134.3 | 1,164.3 | 11.4 | 1.000x | 1.012x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 111.9 | 110.7 | 114.0 | 1.1 | 0.097x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,148.0 | 1,139.3 | 1,572.5 | 169.6 | 1.000x | 10.258x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,153.8 | 1,143.0 | 1,161.9 | 7.1 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,163.7 | 1,154.9 | 1,193.7 | 13.9 | 1.000x | 1.009x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 123.4 | 122.4 | 124.1 | 0.6 | 0.105x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,175.3 | 1,159.3 | 1,561.4 | 157.3 | 1.000x | 9.523x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,141.8 | 1,129.2 | 1,151.4 | 8.2 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,155.8 | 1,136.0 | 1,182.8 | 16.3 | 1.000x | 1.012x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 110.8 | 109.6 | 111.6 | 0.7 | 0.095x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,165.5 | 1,149.9 | 1,546.4 | 154.8 | 1.000x | 10.521x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 661.8 | 650.3 | 674.3 | 7.7 | 0.983x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 672.9 | 656.3 | 685.6 | 9.4 | 1.000x | 1.017x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 100.9 | 99.4 | 101.6 | 0.7 | 0.150x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 674.4 | 669.3 | 1,197.8 | 209.5 | 1.000x | 6.687x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,075.1 | 1,062.2 | 1,086.2 | 7.9 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,085.1 | 1,070.3 | 1,109.6 | 13.8 | 1.000x | 1.009x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 106.7 | 106.3 | 108.2 | 0.7 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,093.7 | 1,081.6 | 1,485.6 | 158.7 | 1.000x | 10.251x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 690.4 | 684.5 | 699.9 | 5.2 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 691.4 | 686.8 | 704.0 | 6.0 | 1.000x | 1.001x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 220.8 | 218.2 | 226.9 | 3.6 | 0.089x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,489.1 | 2,479.0 | 3,410.7 | 366.0 | 1.000x | 11.273x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 686.9 | 686.0 | 704.6 | 7.1 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 690.6 | 686.1 | 703.7 | 6.0 | 1.000x | 1.005x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 238.2 | 232.7 | 239.3 | 2.4 | 0.096x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,487.2 | 2,464.5 | 3,404.8 | 366.6 | 1.000x | 10.443x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 689.4 | 682.3 | 706.0 | 8.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 690.6 | 687.0 | 703.0 | 5.5 | 1.002x | 1.002x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 221.2 | 218.9 | 224.9 | 2.2 | 0.088x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,499.8 | 2,461.5 | 3,397.3 | 363.6 | 1.000x | 11.299x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 689.6 | 688.2 | 705.5 | 6.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 689.9 | 686.1 | 699.8 | 5.4 | 1.000x | 1.000x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 233.6 | 232.3 | 236.4 | 1.5 | 0.094x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,487.8 | 2,471.6 | 3,388.4 | 358.8 | 1.000x | 10.650x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 843.2 | 833.7 | 846.0 | 4.4 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 851.5 | 836.1 | 861.9 | 10.1 | 1.000x | 1.010x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 308.3 | 306.1 | 313.4 | 2.8 | 0.099x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,099.0 | 3,077.9 | 3,475.6 | 152.0 | 1.000x | 10.052x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 782.6 | 780.1 | 802.7 | 8.3 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 794.8 | 778.3 | 825.5 | 17.3 | 1.000x | 1.016x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 310.3 | 306.2 | 316.5 | 4.3 | 0.109x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,840.0 | 2,814.2 | 2,883.9 | 25.2 | 1.000x | 9.152x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,172.8 | 1,162.5 | 1,183.9 | 7.1 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,182.2 | 1,176.9 | 1,225.1 | 18.3 | 1.000x | 1.008x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 394.7 | 391.5 | 397.1 | 2.4 | 0.087x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 4,522.0 | 4,433.2 | 4,550.7 | 44.4 | 1.000x | 11.457x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,497.5 | 1,481.8 | 1,508.2 | 9.6 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,509.3 | 1,492.6 | 1,546.7 | 17.9 | 1.000x | 1.008x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 477.7 | 474.6 | 479.6 | 1.9 | 0.082x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 5,793.4 | 5,709.1 | 5,894.3 | 62.3 | 1.000x | 12.129x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 534.7 | 533.1 | 542.7 | 3.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 535.7 | 527.9 | 540.7 | 4.4 | 1.002x | 1.002x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 186.5 | 181.5 | 187.5 | 2.5 | 0.100x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,856.1 | 1,846.1 | 1,896.7 | 18.7 | 1.000x | 9.954x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 773.5 | 769.5 | 785.1 | 6.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 774.3 | 768.9 | 777.6 | 3.1 | 1.001x | 1.001x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 280.6 | 279.1 | 283.3 | 1.5 | 0.100x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,807.9 | 2,802.7 | 2,897.9 | 37.8 | 1.000x | 10.008x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 939.2 | 938.7 | 946.1 | 2.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 943.6 | 937.0 | 953.7 | 5.5 | 1.005x | 1.005x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 573.0 | 570.7 | 575.5 | 1.7 | 0.164x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,495.5 | 3,454.2 | 3,605.7 | 53.8 | 1.000x | 6.100x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 378.3 | 371.5 | 393.2 | 7.5 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 380.5 | 374.8 | 388.5 | 5.1 | 1.000x | 1.006x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 202.9 | 202.1 | 204.4 | 0.8 | 0.129x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,568.0 | 1,548.7 | 1,718.1 | 61.4 | 1.000x | 7.729x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 34.3 | 33.6 | 35.0 | 0.5 | 0.949x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 36.1 | 34.1 | 37.4 | 1.2 | 1.000x | 1.054x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 35.1 | 35.0 | 35.4 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 41.3 | 39.9 | 42.3 | 0.8 | 1.177x | 1.177x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 160.3 | 158.8 | 167.2 | 3.5 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 162.3 | 160.2 | 163.2 | 1.1 | 1.000x | 1.012x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 51.0 | 51.0 | 51.5 | 0.2 | 0.284x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 179.8 | 178.8 | 191.7 | 4.8 | 1.000x | 3.523x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 516.0 | 508.7 | 521.9 | 4.2 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 517.8 | 516.2 | 524.3 | 2.9 | 1.000x | 1.004x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 85.7 | 84.6 | 85.9 | 0.5 | 0.163x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 525.6 | 515.8 | 541.2 | 8.6 | 1.000x | 6.129x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 462.8 | 460.0 | 469.8 | 3.3 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 466.3 | 457.6 | 468.3 | 4.1 | 1.000x | 1.008x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 291.0 | 285.1 | 294.8 | 3.8 | 0.115x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,526.1 | 2,499.3 | 2,592.2 | 34.7 | 1.000x | 8.682x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 161.3 | 160.7 | 165.3 | 1.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 162.1 | 159.7 | 167.6 | 2.9 | 1.005x | 1.005x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 160.3 | 159.2 | 162.5 | 1.1 | 0.155x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,035.8 | 1,020.9 | 1,058.7 | 13.8 | 1.000x | 6.461x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 463.4 | 454.3 | 468.5 | 4.6 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 465.0 | 457.1 | 467.7 | 3.8 | 1.000x | 1.003x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 189.2 | 188.1 | 190.2 | 0.7 | 0.110x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,716.3 | 1,702.7 | 1,761.7 | 23.1 | 1.000x | 9.069x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 934.3 | 927.7 | 936.6 | 3.0 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 935.0 | 921.2 | 946.4 | 8.4 | 1.000x | 1.001x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 540.3 | 533.2 | 544.5 | 3.7 | 0.157x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,435.3 | 3,384.1 | 3,543.4 | 55.2 | 1.000x | 6.358x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,521.2 | 1,512.8 | 1,535.5 | 7.9 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,532.4 | 1,520.3 | 1,576.7 | 20.2 | 1.000x | 1.007x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 473.1 | 468.1 | 482.3 | 4.7 | 0.080x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 5,883.2 | 5,834.2 | 6,006.9 | 58.1 | 1.000x | 12.436x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 688.4 | 682.2 | 698.4 | 5.6 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 694.2 | 688.2 | 713.3 | 9.5 | 1.000x | 1.008x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 192.9 | 189.0 | 196.0 | 2.8 | 0.104x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,853.4 | 1,829.4 | 1,886.4 | 23.4 | 1.000x | 9.609x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 434.0 | 425.6 | 439.7 | 5.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 434.9 | 431.4 | 437.8 | 2.1 | 1.002x | 1.002x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 267.2 | 266.4 | 268.3 | 0.6 | 0.116x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,302.4 | 2,271.9 | 2,558.9 | 107.7 | 1.000x | 8.616x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 694.8 | 692.8 | 700.8 | 2.9 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 699.2 | 691.3 | 702.2 | 3.9 | 1.000x | 1.006x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 399.0 | 392.7 | 415.5 | 8.1 | 0.117x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,424.6 | 3,410.4 | 4,930.5 | 600.2 | 1.000x | 8.583x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 429.8 | 428.5 | 435.3 | 2.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 433.1 | 427.6 | 434.1 | 2.5 | 1.008x | 1.008x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 272.4 | 267.8 | 274.6 | 2.7 | 0.119x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,281.9 | 2,270.9 | 3,548.7 | 501.9 | 1.000x | 8.377x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 686.8 | 680.0 | 698.1 | 7.2 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 690.4 | 684.1 | 712.3 | 10.3 | 1.000x | 1.005x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 224.3 | 223.3 | 228.3 | 2.0 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,484.6 | 2,480.6 | 3,380.8 | 352.8 | 1.000x | 11.079x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 686.2 | 681.2 | 695.4 | 5.5 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 691.5 | 686.2 | 711.4 | 10.0 | 1.000x | 1.008x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 224.3 | 218.8 | 226.5 | 2.9 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,482.1 | 2,469.7 | 3,375.6 | 353.7 | 1.000x | 11.066x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 684.2 | 682.6 | 704.3 | 9.1 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 688.0 | 686.0 | 712.6 | 11.4 | 1.000x | 1.006x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 226.3 | 219.6 | 228.4 | 3.0 | 0.091x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,490.1 | 2,467.2 | 3,385.4 | 356.0 | 1.000x | 11.002x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 686.9 | 680.9 | 699.9 | 8.0 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 688.8 | 686.1 | 715.0 | 11.2 | 1.000x | 1.003x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 218.5 | 217.1 | 225.4 | 3.1 | 0.088x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,483.6 | 2,473.5 | 3,378.4 | 353.5 | 1.000x | 11.367x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 685.7 | 679.7 | 698.3 | 7.5 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 689.9 | 686.0 | 707.6 | 8.7 | 1.000x | 1.006x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 219.1 | 216.3 | 225.6 | 3.1 | 0.088x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,488.4 | 2,468.8 | 3,377.0 | 353.8 | 1.000x | 11.355x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 10,156.5 | 10,120.1 | 12,474.6 | 929.8 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 10,183.9 | 10,130.1 | 10,860.3 | 275.1 | 1.000x | 1.003x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 115,306.6 | 114,897.7 | 120,362.5 | 2,042.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 115,552.6 | 115,363.7 | 117,259.9 | 705.8 | 1.002x | 1.002x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 272,202.4 | 267,040.2 | 272,704.4 | 2,440.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 272,279.1 | 266,822.6 | 275,193.0 | 3,361.9 | 1.000x | 1.000x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 548,785.1 | 547,008.6 | 553,358.3 | 2,126.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 548,838.3 | 546,223.5 | 569,291.3 | 8,497.9 | 1.000x | 1.000x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71,512.2 | 71,139.2 | 72,509.9 | 587.8 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 71,852.6 | 71,370.8 | 73,405.6 | 748.4 | 1.000x | 1.005x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 788.6 | 783.4 | 794.9 | 4.8 | 0.983x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 802.0 | 783.3 | 805.8 | 9.6 | 1.000x | 1.017x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 200,547.8 | 200,171.9 | 203,973.4 | 1,626.2 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 200,982.0 | 199,905.2 | 201,638.8 | 615.2 | 1.000x | 1.002x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 146,283.7 | 144,440.2 | 149,615.7 | 1,866.7 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 146,915.8 | 144,441.9 | 151,197.6 | 2,364.9 | 1.000x | 1.004x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 164.1 | 162.6 | 167.8 | 2.1 | 0.982x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 167.1 | 164.9 | 169.5 | 1.8 | 1.000x | 1.018x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 145.0 | 144.1 | 145.5 | 0.5 | 0.097x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,496.9 | 1,479.1 | 2,139.4 | 259.3 | 1.000x | 10.322x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,055.0 | 1,050.7 | 1,058.7 | 2.8 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,065.0 | 1,055.1 | 1,073.8 | 6.0 | 1.000x | 1.010x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 162.9 | 162.4 | 166.5 | 1.5 | 0.153x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,062.1 | 1,043.4 | 1,682.4 | 250.5 | 1.000x | 6.519x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,020.2 | 1,012.0 | 1,031.5 | 7.5 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,024.5 | 1,019.0 | 1,034.3 | 5.3 | 1.000x | 1.004x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 157.0 | 150.2 | 159.3 | 3.1 | 0.154x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,022.8 | 1,013.8 | 1,471.8 | 181.1 | 1.000x | 6.513x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 703.3 | 701.1 | 710.4 | 3.2 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 705.5 | 697.9 | 714.1 | 5.2 | 1.000x | 1.003x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 104.5 | 101.7 | 107.0 | 1.7 | 0.149x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 700.5 | 699.3 | 937.2 | 94.3 | 1.000x | 6.704x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 538.9 | 533.2 | 558.0 | 9.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 540.2 | 537.5 | 554.8 | 6.3 | 1.002x | 1.002x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 202.4 | 187.6 | 205.9 | 6.4 | 0.100x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,017.8 | 1,988.4 | 2,976.5 | 386.5 | 1.000x | 9.968x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 872.0 | 859.9 | 882.1 | 8.7 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 874.4 | 868.4 | 880.3 | 3.8 | 1.000x | 1.003x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 147.2 | 145.8 | 147.4 | 0.6 | 0.167x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 878.8 | 859.9 | 1,229.8 | 143.0 | 1.000x | 5.970x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 882.0 | 880.3 | 895.2 | 5.5 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 887.5 | 886.2 | 904.1 | 6.6 | 1.000x | 1.006x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 160.2 | 159.2 | 160.4 | 0.5 | 0.181x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 885.5 | 871.7 | 1,245.6 | 144.9 | 1.000x | 5.528x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 2,105.8 | 2,098.4 | 2,118.4 | 6.6 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,115.4 | 2,090.7 | 2,128.5 | 12.5 | 1.000x | 1.005x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 396.5 | 394.5 | 398.5 | 1.4 | 0.131x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,037.7 | 3,002.0 | 5,754.8 | 1,089.8 | 1.000x | 7.661x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 697.1 | 691.5 | 699.8 | 2.9 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 702.1 | 691.6 | 712.6 | 8.4 | 1.000x | 1.007x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 224.2 | 220.3 | 226.5 | 2.3 | 0.090x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,498.4 | 2,466.6 | 3,390.0 | 358.6 | 1.000x | 11.142x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 696.2 | 690.5 | 714.9 | 10.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 696.4 | 686.7 | 700.1 | 4.8 | 1.000x | 1.000x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 236.4 | 234.0 | 240.3 | 2.1 | 0.095x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,489.6 | 2,473.2 | 2,767.4 | 112.0 | 1.000x | 10.529x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,037.4 | 1,026.6 | 1,044.4 | 6.8 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,050.4 | 1,036.6 | 1,063.1 | 8.9 | 1.000x | 1.012x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 120.9 | 120.8 | 122.1 | 0.5 | 0.116x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,045.1 | 1,030.2 | 1,414.9 | 149.8 | 1.000x | 8.643x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,031.6 | 1,027.4 | 1,043.2 | 5.7 | 0.982x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,050.0 | 1,043.1 | 1,057.4 | 4.5 | 1.000x | 1.018x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 120.9 | 120.4 | 121.9 | 0.5 | 0.116x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,042.1 | 1,037.6 | 1,525.1 | 193.6 | 1.000x | 8.619x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,146.4 | 1,142.3 | 1,169.8 | 10.0 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,157.8 | 1,153.8 | 1,178.3 | 8.9 | 1.000x | 1.010x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 113.6 | 112.2 | 113.7 | 0.7 | 0.098x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,157.8 | 1,154.2 | 1,612.4 | 182.3 | 1.000x | 10.192x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,092.6 | 1,081.2 | 1,110.7 | 9.5 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,093.3 | 1,083.5 | 1,111.5 | 9.2 | 1.000x | 1.001x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 111.8 | 111.0 | 112.8 | 0.7 | 0.102x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,093.3 | 1,085.0 | 1,582.9 | 195.9 | 1.000x | 9.780x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,087.8 | 1,080.7 | 1,105.7 | 9.4 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,092.9 | 1,083.0 | 1,113.3 | 10.1 | 1.000x | 1.005x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 111.9 | 110.8 | 112.6 | 0.7 | 0.102x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,095.3 | 1,086.6 | 1,582.1 | 195.8 | 1.000x | 9.791x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 820.5 | 818.6 | 825.7 | 3.0 | 0.987x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 831.7 | 824.4 | 847.5 | 8.8 | 1.000x | 1.014x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 310.4 | 306.5 | 313.8 | 2.4 | 0.103x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,017.5 | 2,993.6 | 4,278.2 | 505.3 | 1.000x | 9.721x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.4 | 30.3 | 31.4 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 30.6 | 30.3 | 30.9 | 0.2 | 1.007x | 1.007x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.5 | 30.4 | 31.0 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 40.8 | 39.3 | 44.3 | 1.7 | 1.334x | 1.334x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.3 | 30.3 | 30.7 | 0.2 | 1.000x | 1.000x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.4 | 30.4 | 30.7 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39.9 | 39.2 | 44.1 | 1.8 | 1.312x | 1.312x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 34.6 | 33.8 | 37.7 | 1.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 35.0 | 34.3 | 35.9 | 0.5 | 1.013x | 1.013x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 35.9 | 35.5 | 36.3 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39.8 | 39.1 | 41.8 | 1.0 | 1.111x | 1.111x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 34.9 | 33.6 | 35.8 | 0.7 | 0.989x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 35.3 | 34.7 | 37.1 | 0.9 | 1.000x | 1.011x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 35.2 | 35.1 | 35.3 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 40.4 | 39.6 | 42.3 | 0.9 | 1.150x | 1.150x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 7,144,380.3 | 7,068,696.3 | 9,792,021.3 | 1,063,141.9 | 0.140x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 50,961,503.9 | 50,823,704.7 | 51,735,890.5 | 348,644.2 | 1.000x | 7.133x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 18,869.7 | 18,682.8 | 18,996.0 | 121.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 17,671,349.3 | 17,597,822.7 | 17,678,909.7 | 38,057.8 | 936.494x | 936.494x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best | n | pass-rate |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 18,664.3 | 18,447.2 | 18,715.8 | 94.7 | 1.000x | 1.000x | 5 | 100% |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42,670,154.0 | 42,640,594.0 | 42,678,507.3 | 13,569.9 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 353,473,455.7 | 351,728,585.6 | 356,574,004.8 | 1,749,820.7 | 1.000x | 8.284x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 18,664.5 | 18,615.1 | 18,697.4 | 26.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 22,543,060.3 | 22,506,927.0 | 22,553,727.3 | 18,070.7 | 1207.805x | 1207.805x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.9 | 29.1 | 0.1 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.9 | 29.5 | 0.3 | 1.000x | 1.001x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 42.6 | 44.3 | 0.6 | 0.453x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.4 | 93.8 | 99.2 | 2.2 | 1.000x | 2.209x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.9 | 29.3 | 0.2 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.7 | 29.8 | 0.5 | 1.000x | 1.006x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.0 | 42.2 | 45.0 | 1.0 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 93.5 | 95.5 | 0.8 | 1.000x | 2.189x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 28.9 | 0.1 | 0.986x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.8 | 29.8 | 0.4 | 1.000x | 1.014x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 41.7 | 44.9 | 1.1 | 0.452x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.0 | 93.1 | 95.6 | 1.0 | 1.000x | 2.212x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.2 | 0.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.4 | 0.2 | 1.000x | 1.007x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.3 | 42.4 | 44.8 | 0.8 | 0.440x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 98.4 | 97.1 | 103.7 | 2.4 | 1.000x | 2.271x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 28.9 | 0.1 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.4 | 0.2 | 1.000x | 1.003x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.7 | 42.2 | 46.0 | 1.3 | 0.467x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.7 | 92.0 | 96.2 | 1.4 | 1.000x | 2.144x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.1 | 0.2 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 29.6 | 0.4 | 1.000x | 1.005x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 42.1 | 44.6 | 0.9 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 93.0 | 96.7 | 1.4 | 1.000x | 2.180x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.6 | 29.0 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 28.5 | 29.2 | 0.2 | 1.008x | 1.008x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.9 | 42.2 | 44.9 | 1.1 | 0.468x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 93.1 | 95.6 | 0.9 | 1.000x | 2.135x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.4 | 29.3 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.5 | 29.2 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.3 | 40.9 | 44.7 | 1.3 | 0.463x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.7 | 93.4 | 95.8 | 1.1 | 1.000x | 2.162x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.2 | 28.8 | 29.6 | 0.3 | 1.012x | 1.012x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.7 | 42.2 | 44.4 | 0.7 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.3 | 93.1 | 97.3 | 1.7 | 1.000x | 2.179x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.5 | 29.5 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 28.9 | 29.2 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 42.3 | 44.8 | 0.9 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.0 | 93.1 | 95.9 | 1.0 | 1.000x | 2.180x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.4 | 0.2 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.4 | 29.8 | 0.5 | 1.000x | 1.008x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 42.5 | 44.7 | 0.8 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.6 | 93.1 | 99.0 | 2.0 | 1.000x | 2.190x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.2 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.7 | 29.6 | 0.3 | 1.000x | 1.006x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 42.2 | 44.7 | 0.9 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.5 | 93.7 | 96.2 | 1.0 | 1.000x | 2.201x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.8 | 29.2 | 0.1 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 29.2 | 0.2 | 1.000x | 1.006x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.3 | 42.5 | 45.1 | 1.0 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.8 | 93.0 | 95.8 | 1.1 | 1.000x | 2.189x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.5 | 29.5 | 0.3 | 1.000x | 1.007x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 42.4 | 45.1 | 1.0 | 0.458x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 93.0 | 98.5 | 2.0 | 1.000x | 2.184x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.2 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 29.5 | 0.3 | 1.000x | 1.000x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.3 | 44.5 | 0.8 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.3 | 93.0 | 96.2 | 1.1 | 1.000x | 2.173x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.3 | 29.0 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 29.0 | 29.3 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.8 | 42.3 | 44.9 | 1.0 | 0.455x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 93.1 | 101.3 | 3.0 | 1.000x | 2.196x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.5 | 29.1 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.2 | 28.7 | 29.2 | 0.2 | 1.006x | 1.006x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.7 | 42.2 | 44.5 | 0.8 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 93.2 | 102.4 | 3.5 | 1.000x | 2.202x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 28.9 | 29.2 | 0.1 | 1.010x | 1.010x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.1 | 42.2 | 44.6 | 1.0 | 0.470x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 93.1 | 96.3 | 1.1 | 1.000x | 2.128x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.2 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.2 | 0.2 | 1.004x | 1.004x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.5 | 41.8 | 44.3 | 0.9 | 0.462x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 93.9 | 101.7 | 3.0 | 1.000x | 2.165x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.6 | 28.5 | 29.3 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.1 | 0.1 | 1.008x | 1.008x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.8 | 42.1 | 45.0 | 1.1 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.4 | 93.0 | 100.2 | 2.6 | 1.000x | 2.205x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.4 | 29.8 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.0 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 42.4 | 44.9 | 0.9 | 0.455x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.7 | 93.0 | 100.3 | 2.6 | 1.000x | 2.198x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 29.0 | 0.1 | 0.981x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.4 | 28.8 | 29.7 | 0.4 | 1.000x | 1.020x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.3 | 42.0 | 44.4 | 0.8 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 92.9 | 95.4 | 1.0 | 1.000x | 2.173x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.7 | 29.6 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.6 | 29.0 | 0.2 | 1.000x | 1.000x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.8 | 44.8 | 0.7 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.3 | 94.2 | 99.7 | 2.1 | 1.000x | 2.172x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.6 | 29.2 | 0.2 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.4 | 0.2 | 1.000x | 1.002x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.2 | 42.2 | 46.0 | 1.4 | 0.468x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.4 | 93.5 | 99.8 | 2.3 | 1.000x | 2.137x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 28.9 | 0.1 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.6 | 29.5 | 0.3 | 1.000x | 1.009x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 42.1 | 44.8 | 1.1 | 0.456x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 92.7 | 99.8 | 2.5 | 1.000x | 2.195x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.5 | 29.4 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.3 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.8 | 42.2 | 45.0 | 1.1 | 0.464x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.5 | 93.0 | 103.6 | 3.9 | 1.000x | 2.156x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 29.1 | 0.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.6 | 0.3 | 1.000x | 1.007x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.7 | 42.3 | 44.9 | 0.9 | 0.465x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 93.2 | 103.8 | 3.9 | 1.000x | 2.148x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.7 | 29.9 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.0 | 0.1 | 1.005x | 1.005x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.7 | 42.1 | 44.7 | 1.0 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.6 | 92.8 | 101.5 | 3.2 | 1.000x | 2.189x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.0 | 0.1 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.6 | 29.7 | 0.4 | 1.000x | 1.008x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 41.8 | 44.6 | 1.1 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.9 | 92.8 | 99.7 | 2.5 | 1.000x | 2.202x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.0 | 0.1 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 29.8 | 0.4 | 1.000x | 1.006x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.7 | 41.6 | 47.4 | 2.0 | 0.479x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.4 | 92.7 | 100.4 | 2.8 | 1.000x | 2.088x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.6 | 29.1 | 0.2 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.6 | 0.3 | 1.000x | 1.003x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 42.5 | 44.9 | 1.0 | 0.461x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.7 | 92.8 | 97.1 | 1.8 | 1.000x | 2.169x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.6 | 29.8 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.1 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.7 | 41.7 | 44.6 | 1.0 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.2 | 92.8 | 102.2 | 3.3 | 1.000x | 2.179x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.2 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.7 | 29.6 | 0.3 | 1.000x | 1.001x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 42.9 | 44.5 | 0.7 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 92.7 | 104.2 | 4.2 | 1.000x | 2.187x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.5 | 29.2 | 0.2 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.1 | 0.1 | 1.000x | 1.003x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.3 | 45.3 | 1.2 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.3 | 92.9 | 103.9 | 4.0 | 1.000x | 2.174x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 29.4 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 28.7 | 29.3 | 0.2 | 1.001x | 1.001x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 42.2 | 44.7 | 0.9 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 93.0 | 98.2 | 1.8 | 1.000x | 2.190x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.1 | 0.1 | 0.989x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.5 | 29.7 | 0.5 | 1.000x | 1.011x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 41.5 | 48.9 | 2.5 | 0.462x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.6 | 92.9 | 96.3 | 1.3 | 1.000x | 2.164x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.1 | 0.1 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.4 | 29.6 | 0.4 | 1.000x | 1.002x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 41.9 | 44.9 | 1.0 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 92.8 | 95.7 | 1.0 | 1.000x | 2.176x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.1 | 0.1 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.3 | 29.6 | 0.4 | 1.000x | 1.007x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.7 | 42.1 | 45.1 | 1.2 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 92.8 | 95.7 | 1.1 | 1.000x | 2.205x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.4 | 0.3 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.3 | 29.4 | 0.4 | 1.000x | 1.002x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.0 | 42.0 | 48.0 | 2.1 | 0.470x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.7 | 92.8 | 95.7 | 1.0 | 1.000x | 2.128x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.6 | 0.3 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.3 | 29.5 | 0.4 | 1.000x | 1.005x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 42.0 | 44.0 | 0.8 | 0.453x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 93.3 | 98.5 | 1.8 | 1.000x | 2.206x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.0 | 0.1 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.5 | 29.4 | 0.3 | 1.000x | 1.009x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 33.1 | 33.1 | 33.1 | 0.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 36.4 | 35.4 | 39.1 | 1.3 | 1.101x | 1.101x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 82.5 | 82.4 | 83.6 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 83.0 | 82.2 | 86.0 | 1.6 | 1.006x | 1.006x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.5 | 42.5 | 44.7 | 0.8 | 0.453x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.9 | 94.4 | 99.1 | 1.7 | 1.000x | 2.208x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.2 | 0.1 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.8 | 29.9 | 0.4 | 1.000x | 1.003x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 41.8 | 44.9 | 1.1 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.5 | 93.6 | 98.4 | 1.7 | 1.000x | 2.177x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.1 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 29.1 | 29.5 | 0.2 | 1.000x | 1.009x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 41.2 | 44.6 | 1.2 | 0.461x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 92.8 | 101.2 | 3.0 | 1.000x | 2.171x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.3 | 0.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.4 | 29.3 | 0.3 | 1.000x | 1.007x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.4 | 41.4 | 48.7 | 2.7 | 0.451x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 92.9 | 95.7 | 0.9 | 1.000x | 2.218x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.1 | 28.9 | 29.2 | 0.1 | 0.989x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.4 | 28.9 | 29.6 | 0.3 | 1.000x | 1.011x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.5 | 42.8 | 44.8 | 0.7 | 0.453x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.9 | 92.7 | 96.7 | 1.5 | 1.000x | 2.205x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.7 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.2 | 0.1 | 1.007x | 1.007x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.5 | 44.9 | 0.9 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.0 | 92.7 | 99.3 | 2.3 | 1.000x | 2.190x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 28.9 | 0.0 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.7 | 29.4 | 0.2 | 1.000x | 1.004x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 41.8 | 44.5 | 1.0 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 92.8 | 98.1 | 1.9 | 1.000x | 2.203x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.3 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.6 | 0.3 | 1.004x | 1.004x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 41.8 | 44.0 | 0.8 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.7 | 93.0 | 95.9 | 1.0 | 1.000x | 2.187x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.6 | 29.1 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.2 | 1.006x | 1.006x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 41.3 | 43.9 | 1.1 | 0.463x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 93.0 | 96.1 | 1.3 | 1.000x | 2.160x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.4 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.2 | 0.2 | 1.006x | 1.006x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.7 | 41.4 | 44.1 | 1.1 | 0.450x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.0 | 93.0 | 97.9 | 1.7 | 1.000x | 2.224x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.2 | 0.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.7 | 29.3 | 0.2 | 1.000x | 1.007x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.5 | 41.4 | 44.4 | 1.2 | 0.453x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 92.9 | 96.6 | 1.3 | 1.000x | 2.210x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.0 | 0.1 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.8 | 29.9 | 0.4 | 1.000x | 1.001x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 42.2 | 44.9 | 1.2 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 92.8 | 97.3 | 1.6 | 1.000x | 2.188x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 28.9 | 0.1 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.4 | 0.2 | 1.000x | 1.006x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.1 | 41.7 | 45.0 | 1.2 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 92.8 | 96.6 | 1.3 | 1.000x | 2.180x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.1 | 0.1 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.5 | 29.2 | 0.2 | 1.000x | 1.003x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.5 | 42.4 | 44.8 | 0.8 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 93.0 | 95.5 | 1.0 | 1.000x | 2.187x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.6 | 29.7 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.2 | 0.2 | 1.007x | 1.007x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.0 | 42.5 | 44.4 | 0.7 | 0.464x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.8 | 93.0 | 97.0 | 1.3 | 1.000x | 2.155x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.7 | 29.1 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.2 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 43.0 | 44.6 | 0.6 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.8 | 92.9 | 95.1 | 0.9 | 1.000x | 2.175x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.2 | 0.2 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.8 | 29.5 | 0.2 | 1.000x | 1.001x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.8 | 29.8 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.7 | 29.2 | 0.2 | 1.001x | 1.001x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.4 | 29.4 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.2 | 0.2 | 1.000x | 1.000x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.4 | 29.6 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.1 | 0.1 | 1.003x | 1.003x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.8 | 29.2 | 0.2 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.5 | 29.6 | 0.4 | 1.000x | 1.012x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.8 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 29.1 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.4 | 29.8 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.6 | 29.1 | 0.2 | 1.002x | 1.002x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.0 | 0.1 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.5 | 29.4 | 0.4 | 1.000x | 1.012x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.2 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.0 | 0.1 | 1.001x | 1.001x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.2 | 41.2 | 44.9 | 1.3 | 0.462x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.5 | 92.9 | 96.5 | 1.4 | 1.000x | 2.162x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.8 | 28.7 | 29.8 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.4 | 0.2 | 1.003x | 1.003x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.8 | 42.3 | 44.7 | 0.9 | 0.461x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 93.0 | 95.6 | 1.0 | 1.000x | 2.169x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.7 | 28.7 | 29.5 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.8 | 29.5 | 0.2 | 1.005x | 1.005x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.4 | 42.2 | 44.7 | 1.0 | 0.444x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.6 | 92.7 | 96.3 | 1.4 | 1.000x | 2.253x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.7 | 28.4 | 29.5 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.8 | 29.2 | 0.2 | 1.007x | 1.007x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.5 | 41.5 | 44.7 | 1.4 | 0.451x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 92.7 | 96.3 | 1.3 | 1.000x | 2.217x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.1 | 0.1 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.5 | 29.3 | 0.3 | 1.000x | 1.002x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.7 | 41.7 | 44.7 | 1.1 | 0.454x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.1 | 92.9 | 96.4 | 1.4 | 1.000x | 2.205x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.4 | 29.2 | 0.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.1 | 0.1 | 1.000x | 1.000x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.0 | 42.6 | 44.7 | 1.0 | 0.451x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.3 | 92.8 | 97.3 | 1.6 | 1.000x | 2.218x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 29.2 | 0.2 | 0.989x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.3 | 29.4 | 0.4 | 1.000x | 1.011x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.2 | 42.5 | 45.6 | 1.0 | 0.469x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.2 | 92.7 | 96.3 | 1.3 | 1.000x | 2.132x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.6 | 29.2 | 0.2 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.4 | 29.8 | 0.5 | 1.000x | 1.016x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 42.2 | 44.7 | 0.9 | 0.465x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.6 | 93.0 | 96.7 | 1.5 | 1.000x | 2.149x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.2 | 0.2 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.4 | 29.8 | 0.5 | 1.000x | 1.010x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 42.8 | 44.8 | 0.7 | 0.466x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.5 | 92.8 | 96.6 | 1.4 | 1.000x | 2.145x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.9 | 30.0 | 0.4 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.5 | 29.8 | 0.4 | 1.000x | 1.002x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.7 | 44.8 | 0.9 | 0.460x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.3 | 93.0 | 95.6 | 1.0 | 1.000x | 2.174x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 31.1 | 0.9 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.9 | 29.8 | 0.4 | 1.000x | 1.001x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44.4 | 42.4 | 46.3 | 1.5 | 0.473x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 93.1 | 97.3 | 1.5 | 1.000x | 2.113x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.6 | 30.0 | 0.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 30.1 | 0.5 | 1.001x | 1.001x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.0 | 41.8 | 44.9 | 1.3 | 0.442x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 92.7 | 95.7 | 1.0 | 1.000x | 2.263x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.7 | 29.2 | 0.2 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.6 | 29.3 | 0.2 | 1.000x | 1.005x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.7 | 41.8 | 44.9 | 1.1 | 0.464x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.0 | 92.7 | 95.5 | 0.9 | 1.000x | 2.154x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.7 | 29.7 | 0.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.5 | 29.7 | 0.4 | 1.000x | 1.000x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 42.9 | 41.8 | 50.6 | 3.2 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93.8 | 93.0 | 95.6 | 1.0 | 1.000x | 2.188x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.9 | 28.9 | 29.1 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.8 | 29.6 | 0.3 | 1.002x | 1.002x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.4 | 42.4 | 44.0 | 0.6 | 0.457x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.9 | 92.8 | 96.2 | 1.3 | 1.000x | 2.188x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.0 | 28.9 | 29.2 | 0.1 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.1 | 28.4 | 29.8 | 0.4 | 1.000x | 1.003x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.6 | 42.3 | 44.7 | 0.8 | 0.459x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 94.9 | 92.8 | 95.6 | 1.2 | 1.000x | 2.178x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.5 | 28.5 | 28.5 | 0.0 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28.6 | 28.2 | 28.7 | 0.2 | 1.000x | 1.005x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 32.5 | 32.5 | 32.5 | 0.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39.7 | 38.7 | 40.8 | 0.8 | 1.224x | 1.224x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 90.8 | 90.1 | 97.0 | 2.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 93.4 | 90.7 | 96.8 | 2.5 | 1.030x | 1.030x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 43.0 | 41.8 | 44.8 | 1.0 | 0.452x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 95.1 | 94.5 | 97.6 | 1.3 | 1.000x | 2.214x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.8 | 28.8 | 29.0 | 0.1 | 0.987x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.4 | 29.3 | 0.4 | 1.000x | 1.013x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 34.0 | 33.5 | 34.1 | 0.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 36.6 | 35.6 | 38.9 | 1.2 | 1.077x | 1.077x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.7 | 28.9 | 0.1 | 0.987x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.2 | 28.4 | 29.8 | 0.6 | 1.000x | 1.013x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 33.1 | 33.1 | 33.4 | 0.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 36.7 | 35.4 | 41.9 | 2.5 | 1.109x | 1.109x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,705,178.5 | 1,689,415.8 | 1,748,940.8 | 21,221.7 | 0.465x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,666,197.7 | 3,657,355.8 | 4,463,987.2 | 338,970.6 | 1.000x | 2.150x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 17,749.9 | 17,741.5 | 17,821.0 | 30.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39,309.1 | 39,107.2 | 40,035.3 | 333.7 | 2.215x | 2.215x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 17,732.3 | 17,711.2 | 18,546.1 | 327.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39,251.9 | 39,110.2 | 39,792.7 | 238.3 | 2.214x | 2.214x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 69,668.6 | 69,477.4 | 70,839.3 | 511.6 | 0.967x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 72,064.7 | 70,402.5 | 76,104.9 | 1,882.7 | 1.000x | 1.034x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 17,728.9 | 17,705.4 | 17,810.4 | 37.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 39,659.9 | 39,167.2 | 39,833.5 | 238.2 | 2.237x | 2.237x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 552.5 | 543.0 | 561.9 | 6.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 554.9 | 547.0 | 567.9 | 6.7 | 1.004x | 1.004x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 79.1 | 77.8 | 79.3 | 0.6 | 0.143x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 551.3 | 548.2 | 556.0 | 2.8 | 1.000x | 6.973x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 760.2 | 754.8 | 767.9 | 5.3 | 0.998x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 761.9 | 757.0 | 773.6 | 5.5 | 1.000x | 1.002x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 92.2 | 91.8 | 94.2 | 1.0 | 0.121x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 762.0 | 757.1 | 771.9 | 6.5 | 1.000x | 8.269x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 484.8 | 479.1 | 493.6 | 5.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 485.5 | 481.5 | 523.3 | 15.4 | 1.001x | 1.001x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 65.0 | 64.6 | 66.0 | 0.5 | 0.134x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 487.0 | 484.0 | 494.9 | 3.9 | 1.000x | 7.488x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 766.6 | 763.5 | 772.3 | 3.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 770.2 | 760.6 | 774.4 | 4.8 | 1.005x | 1.005x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 100.9 | 100.1 | 102.4 | 0.9 | 0.132x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 766.5 | 755.1 | 770.6 | 5.5 | 1.000x | 7.595x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 561.0 | 552.7 | 570.5 | 6.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 565.6 | 556.8 | 571.5 | 4.9 | 1.008x | 1.008x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 92.6 | 91.6 | 93.8 | 0.8 | 0.164x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 565.9 | 555.0 | 567.8 | 4.8 | 1.000x | 6.111x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 484.8 | 479.7 | 492.4 | 4.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 489.5 | 480.0 | 512.6 | 11.9 | 1.010x | 1.010x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 65.3 | 62.9 | 66.6 | 1.3 | 0.134x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 486.7 | 476.5 | 487.8 | 4.5 | 1.000x | 7.456x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 791.9 | 783.9 | 819.0 | 12.2 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 795.3 | 777.4 | 845.0 | 23.3 | 1.000x | 1.004x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 85.0 | 84.0 | 85.6 | 0.6 | 0.107x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 797.3 | 777.4 | 800.6 | 8.4 | 1.000x | 9.382x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 621.5 | 616.8 | 634.3 | 6.0 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 624.0 | 614.8 | 698.9 | 31.1 | 1.000x | 1.004x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 93.1 | 91.6 | 94.8 | 1.2 | 0.152x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 612.6 | 601.5 | 624.0 | 7.3 | 1.000x | 6.583x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 548.8 | 544.3 | 569.0 | 8.6 | 0.997x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 550.3 | 542.1 | 617.6 | 28.2 | 1.000x | 1.003x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 81.3 | 79.5 | 81.7 | 0.8 | 0.148x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 548.5 | 532.7 | 553.5 | 7.5 | 1.000x | 6.742x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 542.3 | 539.3 | 560.7 | 8.1 | 0.992x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 546.7 | 537.6 | 615.4 | 28.9 | 1.000x | 1.008x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 76.6 | 75.5 | 77.7 | 0.9 | 0.142x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 541.5 | 533.7 | 545.8 | 4.2 | 1.000x | 7.067x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 436.3 | 434.2 | 459.9 | 9.5 | 0.984x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 443.1 | 420.7 | 474.9 | 20.4 | 1.000x | 1.016x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 70.3 | 68.5 | 72.6 | 1.3 | 0.162x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 435.4 | 430.9 | 444.3 | 4.5 | 1.000x | 6.190x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 352.2 | 347.5 | 360.8 | 5.3 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 353.8 | 341.9 | 366.0 | 9.3 | 1.000x | 1.004x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 141.3 | 136.5 | 147.3 | 3.8 | 0.080x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,770.2 | 1,745.3 | 1,776.9 | 11.1 | 1.000x | 12.525x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 684.0 | 679.0 | 701.2 | 8.8 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 688.2 | 675.0 | 750.9 | 27.4 | 1.000x | 1.006x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 101.4 | 100.9 | 104.5 | 1.4 | 0.148x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 686.0 | 678.9 | 698.8 | 7.0 | 1.000x | 6.764x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 687.8 | 681.7 | 749.5 | 25.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 692.3 | 682.1 | 706.0 | 7.7 | 1.007x | 1.007x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 102.1 | 100.7 | 103.5 | 0.9 | 0.148x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 690.9 | 682.8 | 695.9 | 4.6 | 1.000x | 6.767x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 546.1 | 534.5 | 553.3 | 6.1 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 552.9 | 538.0 | 610.1 | 26.7 | 1.000x | 1.012x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 95.3 | 92.5 | 98.2 | 2.1 | 0.174x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 546.5 | 536.8 | 552.9 | 5.2 | 1.000x | 5.736x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 664.0 | 658.7 | 672.5 | 5.0 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 667.1 | 659.2 | 737.4 | 29.6 | 1.000x | 1.005x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 99.7 | 98.2 | 104.2 | 2.0 | 0.149x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 668.8 | 663.7 | 669.9 | 2.2 | 1.000x | 6.706x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 194.0 | 182.2 | 203.7 | 7.6 | 0.994x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 195.1 | 183.4 | 205.6 | 8.3 | 1.000x | 1.006x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 111.6 | 106.2 | 114.6 | 2.7 | 0.101x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,101.8 | 1,087.9 | 1,107.1 | 6.7 | 1.000x | 9.871x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 683.8 | 674.0 | 687.5 | 5.7 | 0.986x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 693.5 | 674.5 | 755.2 | 29.6 | 1.000x | 1.014x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 101.5 | 100.0 | 105.2 | 1.8 | 0.148x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 685.5 | 672.6 | 691.9 | 6.8 | 1.000x | 6.757x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 662.5 | 649.0 | 738.4 | 33.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 666.5 | 656.3 | 674.1 | 6.3 | 1.006x | 1.006x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 100.7 | 98.9 | 101.5 | 0.9 | 0.150x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 669.7 | 657.0 | 676.6 | 6.5 | 1.000x | 6.651x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 196.1 | 192.7 | 202.4 | 3.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 201.6 | 189.3 | 215.8 | 8.6 | 1.028x | 1.028x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 111.8 | 108.2 | 115.8 | 2.7 | 0.101x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,101.6 | 1,087.3 | 1,106.3 | 6.5 | 1.000x | 9.856x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 693.1 | 680.4 | 764.3 | 31.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 697.8 | 677.8 | 699.6 | 9.2 | 1.007x | 1.007x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 102.3 | 100.2 | 104.5 | 1.5 | 0.146x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 702.0 | 693.2 | 705.5 | 5.1 | 1.000x | 6.863x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 720.4 | 712.1 | 780.4 | 24.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 723.4 | 716.8 | 739.0 | 8.5 | 1.004x | 1.004x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 76.3 | 76.0 | 78.7 | 1.0 | 0.106x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 719.6 | 718.4 | 725.3 | 2.9 | 1.000x | 9.429x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 454.2 | 453.0 | 458.9 | 2.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 460.8 | 450.1 | 471.5 | 7.4 | 1.014x | 1.014x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 63.0 | 61.6 | 65.0 | 1.1 | 0.136x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 463.5 | 454.8 | 469.4 | 5.9 | 1.000x | 7.353x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 684.3 | 672.1 | 713.0 | 14.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 688.8 | 682.0 | 701.4 | 7.2 | 1.007x | 1.007x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 74.0 | 73.7 | 75.8 | 0.8 | 0.109x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 677.6 | 674.6 | 686.6 | 4.3 | 1.000x | 9.158x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 723.3 | 712.8 | 745.8 | 11.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 731.7 | 725.2 | 745.8 | 7.9 | 1.012x | 1.012x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 85.0 | 84.8 | 86.6 | 0.7 | 0.118x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 720.2 | 719.8 | 732.9 | 5.0 | 1.000x | 8.477x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 742.3 | 733.2 | 748.9 | 5.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 749.2 | 732.9 | 769.8 | 12.5 | 1.009x | 1.009x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 78.0 | 78.0 | 79.2 | 0.5 | 0.106x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 738.9 | 729.1 | 748.7 | 6.7 | 1.000x | 9.467x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 452.4 | 449.0 | 455.7 | 2.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 454.3 | 449.7 | 476.6 | 9.6 | 1.004x | 1.004x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 63.5 | 62.1 | 64.7 | 0.9 | 0.139x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 458.2 | 451.4 | 462.2 | 3.7 | 1.000x | 7.218x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 643.4 | 631.5 | 648.2 | 6.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 650.2 | 639.7 | 664.8 | 8.1 | 1.011x | 1.011x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 72.2 | 70.5 | 74.0 | 1.2 | 0.112x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 643.3 | 634.6 | 648.7 | 5.0 | 1.000x | 8.912x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 300.4 | 295.0 | 313.6 | 7.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 302.0 | 297.3 | 317.6 | 6.9 | 1.005x | 1.005x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 68.8 | 66.9 | 69.4 | 0.9 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,069.8 | 1,066.3 | 1,073.9 | 2.6 | 1.000x | 15.542x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 301.0 | 296.0 | 313.2 | 6.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 301.9 | 297.4 | 315.7 | 6.1 | 1.003x | 1.003x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71.3 | 70.4 | 74.4 | 1.6 | 0.067x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,069.2 | 1,062.9 | 1,074.7 | 3.8 | 1.000x | 14.986x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 301.4 | 294.2 | 310.8 | 6.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 302.9 | 296.2 | 315.2 | 6.3 | 1.005x | 1.005x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 69.2 | 67.0 | 69.3 | 0.9 | 0.065x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,068.0 | 1,057.3 | 1,070.8 | 4.9 | 1.000x | 15.442x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 302.7 | 297.2 | 318.9 | 7.4 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 303.8 | 294.9 | 313.1 | 6.9 | 1.000x | 1.004x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71.9 | 69.5 | 74.3 | 1.8 | 0.067x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,066.8 | 1,059.1 | 1,078.3 | 6.6 | 1.000x | 14.846x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 359.2 | 352.0 | 369.2 | 6.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 361.6 | 357.8 | 382.4 | 9.0 | 1.006x | 1.006x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71.7 | 70.0 | 71.9 | 0.7 | 0.055x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,302.2 | 1,300.3 | 1,314.0 | 5.8 | 1.000x | 18.170x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 315.0 | 310.1 | 327.9 | 6.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 319.7 | 314.7 | 338.5 | 8.5 | 1.015x | 1.015x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 70.7 | 68.4 | 71.2 | 1.0 | 0.062x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,140.1 | 1,129.8 | 1,150.4 | 7.6 | 1.000x | 16.130x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 578.3 | 568.7 | 628.9 | 22.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 580.7 | 580.0 | 598.9 | 7.2 | 1.004x | 1.004x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 84.7 | 82.5 | 85.2 | 1.0 | 0.039x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 2,176.6 | 2,151.1 | 2,225.0 | 27.0 | 1.000x | 25.697x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 786.6 | 782.1 | 799.0 | 7.3 | 0.990x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 794.2 | 769.5 | 859.7 | 32.0 | 1.000x | 1.010x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 119.8 | 119.4 | 121.3 | 0.7 | 0.040x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,000.9 | 2,984.3 | 3,055.7 | 25.9 | 1.000x | 25.056x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 206.5 | 202.1 | 209.4 | 2.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 206.8 | 203.2 | 219.9 | 5.9 | 1.001x | 1.001x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 68.1 | 64.5 | 69.7 | 2.0 | 0.094x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 725.6 | 707.8 | 738.6 | 10.9 | 1.000x | 10.652x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 343.9 | 333.1 | 350.6 | 6.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 344.1 | 337.9 | 346.9 | 3.4 | 1.001x | 1.001x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 78.0 | 77.7 | 82.5 | 1.8 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,224.5 | 1,199.4 | 1,242.5 | 14.1 | 1.000x | 15.699x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 493.4 | 491.6 | 503.9 | 4.4 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 495.3 | 488.6 | 502.1 | 5.1 | 1.000x | 1.004x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 95.3 | 94.2 | 98.7 | 1.5 | 0.051x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,857.5 | 1,844.8 | 1,872.2 | 10.5 | 1.000x | 19.481x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 203.8 | 203.1 | 222.8 | 7.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 210.1 | 201.4 | 224.4 | 7.5 | 1.031x | 1.031x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 126.8 | 126.4 | 127.8 | 0.5 | 0.135x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 942.5 | 928.3 | 962.0 | 12.5 | 1.000x | 7.432x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 34.5 | 34.0 | 37.0 | 1.1 | 0.959x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 36.0 | 34.2 | 38.4 | 1.5 | 1.000x | 1.043x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 37.5 | 37.1 | 47.0 | 3.8 | 0.800x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 46.9 | 46.6 | 46.9 | 0.1 | 1.000x | 1.249x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.5 | 29.4 | 30.1 | 0.3 | 0.964x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.6 | 30.2 | 31.9 | 0.6 | 1.000x | 1.037x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 38.5 | 36.9 | 47.5 | 3.8 | 0.806x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 47.8 | 47.5 | 47.8 | 0.1 | 1.000x | 1.241x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 207.7 | 204.1 | 218.1 | 4.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 212.5 | 201.9 | 216.8 | 5.3 | 1.023x | 1.023x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 52.6 | 50.3 | 54.2 | 1.3 | 0.251x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 209.2 | 206.9 | 216.1 | 3.7 | 1.000x | 3.980x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 150.9 | 148.0 | 161.5 | 4.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 154.8 | 150.4 | 166.9 | 5.6 | 1.026x | 1.026x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 133.2 | 133.0 | 134.0 | 0.4 | 0.126x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,056.5 | 1,046.8 | 1,066.3 | 7.0 | 1.000x | 7.932x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.6 | 29.5 | 30.6 | 0.4 | 0.980x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.2 | 29.4 | 30.6 | 0.4 | 1.000x | 1.020x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 79.2 | 77.6 | 80.9 | 1.1 | 0.144x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 550.2 | 532.0 | 561.3 | 10.2 | 1.000x | 6.943x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 150.8 | 150.5 | 160.1 | 3.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 155.6 | 150.3 | 167.4 | 5.9 | 1.031x | 1.031x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 66.6 | 64.7 | 68.2 | 1.3 | 0.133x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 499.5 | 496.2 | 510.9 | 5.4 | 1.000x | 7.496x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 475.5 | 468.3 | 553.0 | 31.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 480.6 | 467.8 | 488.7 | 7.1 | 1.011x | 1.011x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 85.6 | 84.4 | 86.1 | 0.6 | 0.048x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,785.1 | 1,720.7 | 1,790.6 | 31.5 | 1.000x | 20.860x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 786.2 | 773.9 | 872.8 | 36.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 806.2 | 789.5 | 816.1 | 10.1 | 1.025x | 1.025x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 106.9 | 105.7 | 108.6 | 1.0 | 0.035x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 3,049.9 | 3,008.3 | 3,068.6 | 21.8 | 1.000x | 28.541x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 299.9 | 293.5 | 309.9 | 5.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 303.9 | 295.8 | 320.5 | 8.7 | 1.013x | 1.013x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 62.0 | 61.0 | 62.6 | 0.6 | 0.077x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 808.1 | 804.7 | 818.2 | 5.2 | 1.000x | 13.027x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 143.2 | 140.5 | 148.9 | 2.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 145.6 | 141.0 | 157.3 | 6.0 | 1.017x | 1.017x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 128.2 | 127.2 | 130.9 | 1.4 | 0.125x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,026.2 | 1,021.6 | 1,034.2 | 4.2 | 1.000x | 8.006x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 301.7 | 298.8 | 326.3 | 10.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 308.5 | 300.7 | 315.4 | 5.8 | 1.022x | 1.022x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 122.6 | 121.8 | 126.2 | 1.6 | 0.076x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,603.6 | 1,595.2 | 1,620.6 | 8.7 | 1.000x | 13.078x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 141.7 | 141.1 | 157.3 | 6.2 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 142.3 | 140.0 | 149.3 | 3.2 | 1.000x | 1.004x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 129.3 | 127.6 | 132.1 | 1.8 | 0.127x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,014.2 | 1,003.2 | 1,031.7 | 10.3 | 1.000x | 7.844x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 299.5 | 294.9 | 307.6 | 4.7 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 308.5 | 295.7 | 318.3 | 7.8 | 1.030x | 1.030x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 69.0 | 66.5 | 69.5 | 1.1 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,069.5 | 1,054.5 | 1,085.8 | 10.5 | 1.000x | 15.510x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 299.6 | 295.4 | 310.4 | 5.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 306.0 | 295.3 | 317.7 | 8.4 | 1.021x | 1.021x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 67.6 | 65.4 | 68.3 | 1.0 | 0.063x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,067.3 | 1,051.8 | 1,081.1 | 10.9 | 1.000x | 15.791x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 300.8 | 291.8 | 308.0 | 6.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 306.3 | 295.0 | 320.1 | 8.5 | 1.018x | 1.018x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 67.5 | 64.9 | 67.8 | 1.1 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,061.9 | 1,051.0 | 1,081.5 | 11.4 | 1.000x | 15.736x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 297.6 | 293.7 | 310.0 | 6.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 303.4 | 295.0 | 320.6 | 9.0 | 1.020x | 1.020x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 67.7 | 64.8 | 70.4 | 1.8 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,065.6 | 1,054.2 | 1,087.5 | 11.5 | 1.000x | 15.743x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 298.9 | 293.6 | 310.6 | 6.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 303.5 | 296.8 | 320.1 | 8.0 | 1.016x | 1.016x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 67.7 | 66.2 | 71.6 | 1.9 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,065.6 | 1,053.5 | 1,095.6 | 14.1 | 1.000x | 15.741x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 9,808.3 | 9,780.1 | 10,079.7 | 109.6 | 0.895x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 10,958.3 | 9,796.5 | 12,718.8 | 1,281.3 | 1.000x | 1.117x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 71,275.5 | 70,573.0 | 71,468.3 | 366.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 71,280.3 | 69,192.5 | 71,567.2 | 904.2 | 1.000x | 1.000x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 161,503.1 | 157,855.1 | 163,948.2 | 2,388.5 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 163,430.8 | 157,640.6 | 164,133.4 | 2,409.0 | 1.000x | 1.012x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 9,408.2 | 9,396.7 | 9,434.7 | 13.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 9,409.0 | 9,404.5 | 9,418.1 | 4.8 | 1.000x | 1.000x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 44,442.0 | 44,351.4 | 45,582.0 | 524.5 | 0.984x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 45,152.2 | 44,379.3 | 49,393.7 | 1,865.7 | 1.000x | 1.016x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 317.3 | 314.2 | 331.0 | 7.3 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 317.6 | 315.1 | 322.4 | 2.8 | 1.001x | 1.001x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 110,223.2 | 109,304.4 | 113,521.8 | 1,479.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 110,682.2 | 108,741.5 | 111,437.4 | 894.3 | 1.004x | 1.004x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 94,259.4 | 94,233.9 | 97,636.5 | 1,350.4 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 94,286.7 | 94,218.9 | 96,166.8 | 760.9 | 1.000x | 1.000x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.4 | 29.2 | 29.6 | 0.2 | 0.979x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.0 | 29.0 | 30.9 | 0.7 | 1.000x | 1.022x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 61.8 | 60.4 | 62.8 | 0.8 | 0.113x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 547.8 | 538.3 | 556.3 | 6.4 | 1.000x | 8.857x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 656.5 | 654.2 | 673.5 | 7.2 | 0.996x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 659.4 | 658.8 | 741.2 | 32.1 | 1.000x | 1.004x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 101.3 | 99.0 | 104.0 | 2.0 | 0.149x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 679.9 | 663.8 | 685.2 | 7.3 | 1.000x | 6.714x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 635.5 | 629.9 | 651.8 | 7.4 | 0.991x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 641.0 | 631.3 | 724.3 | 35.0 | 1.000x | 1.009x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 82.3 | 82.0 | 84.7 | 1.0 | 0.129x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 638.1 | 623.0 | 644.6 | 7.9 | 1.000x | 7.753x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 409.8 | 407.8 | 452.4 | 16.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 412.0 | 406.3 | 415.8 | 3.1 | 1.005x | 1.005x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 61.1 | 60.7 | 63.2 | 1.0 | 0.147x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 415.3 | 409.2 | 419.0 | 4.0 | 1.000x | 6.797x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 205.0 | 203.4 | 207.4 | 1.4 | 0.985x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 208.2 | 203.5 | 211.7 | 3.2 | 1.000x | 1.016x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 67.9 | 66.5 | 70.1 | 1.4 | 0.095x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 715.2 | 712.3 | 723.0 | 3.7 | 1.000x | 10.539x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 536.7 | 528.4 | 544.5 | 5.7 | 0.988x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 543.1 | 532.5 | 623.8 | 34.2 | 1.000x | 1.012x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 76.5 | 76.2 | 78.4 | 0.8 | 0.141x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 542.8 | 531.5 | 549.2 | 6.4 | 1.000x | 7.094x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 555.7 | 549.6 | 558.5 | 3.2 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 556.1 | 548.0 | 637.6 | 33.7 | 1.000x | 1.001x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 91.7 | 91.4 | 93.2 | 0.7 | 0.163x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 562.9 | 550.4 | 579.1 | 10.3 | 1.000x | 6.137x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,218.4 | 1,183.1 | 1,268.7 | 30.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 1,221.5 | 1,193.7 | 1,245.2 | 18.6 | 1.002x | 1.002x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 211.0 | 209.9 | 219.1 | 3.4 | 0.120x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,754.7 | 1,725.7 | 1,778.5 | 18.6 | 1.000x | 8.317x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 299.7 | 296.5 | 306.5 | 3.4 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 301.8 | 297.4 | 316.7 | 6.7 | 1.000x | 1.007x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 69.0 | 66.6 | 69.3 | 1.0 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,070.1 | 1,056.6 | 1,077.1 | 7.1 | 1.000x | 15.514x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 300.0 | 293.8 | 313.9 | 6.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 302.1 | 294.8 | 308.6 | 4.8 | 1.007x | 1.007x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71.4 | 70.4 | 74.5 | 1.6 | 0.067x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,071.4 | 1,058.4 | 1,082.8 | 8.1 | 1.000x | 15.013x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 641.1 | 635.1 | 655.4 | 7.2 | 0.995x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 644.3 | 635.3 | 694.7 | 21.7 | 1.000x | 1.005x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 74.0 | 72.6 | 75.5 | 1.0 | 0.115x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 641.9 | 637.6 | 667.2 | 10.5 | 1.000x | 8.676x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 639.1 | 632.3 | 699.9 | 25.6 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 640.6 | 636.2 | 656.2 | 7.2 | 1.002x | 1.002x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 74.1 | 72.4 | 75.3 | 1.0 | 0.116x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 641.8 | 639.1 | 651.3 | 4.2 | 1.000x | 8.656x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 705.9 | 697.1 | 763.8 | 24.2 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 711.2 | 700.2 | 717.2 | 6.0 | 1.007x | 1.007x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 75.0 | 74.0 | 78.6 | 1.6 | 0.105x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 711.4 | 708.5 | 719.3 | 3.9 | 1.000x | 9.485x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 728.0 | 722.8 | 787.0 | 24.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 734.6 | 728.3 | 742.1 | 4.4 | 1.009x | 1.009x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 78.3 | 78.2 | 81.9 | 1.4 | 0.107x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 733.7 | 721.5 | 739.1 | 6.5 | 1.000x | 9.366x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 730.3 | 722.6 | 790.6 | 25.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 732.5 | 720.5 | 738.0 | 5.9 | 1.003x | 1.003x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 78.3 | 78.2 | 81.5 | 1.3 | 0.107x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 734.4 | 720.7 | 738.2 | 6.5 | 1.000x | 9.381x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 350.6 | 346.2 | 370.4 | 8.8 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 354.2 | 347.0 | 360.5 | 4.3 | 1.010x | 1.010x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 71.9 | 69.4 | 72.2 | 1.0 | 0.056x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 1,278.0 | 1,270.0 | 1,284.7 | 5.6 | 1.000x | 17.763x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 28.9 | 28.9 | 29.1 | 0.1 | 0.999x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 29.0 | 28.9 | 29.0 | 0.0 | 1.000x | 1.001x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.4 | 30.1 | 32.8 | 1.0 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 38.1 | 37.9 | 43.7 | 2.2 | 1.253x | 1.253x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 29.7 | 29.2 | 30.0 | 0.3 | 0.963x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 30.8 | 29.6 | 30.8 | 0.5 | 1.000x | 1.038x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 38.0 | 36.3 | 44.3 | 2.9 | 0.945x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 40.2 | 40.1 | 40.2 | 0.0 | 1.000x | 1.058x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 34.9 | 34.5 | 37.8 | 1.2 | 0.993x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 35.1 | 35.1 | 40.5 | 2.3 | 1.000x | 1.007x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 39.7 | 38.9 | 47.0 | 3.0 | 0.814x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 48.7 | 48.7 | 49.2 | 0.2 | 1.000x | 1.228x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 34.2 | 34.2 | 38.4 | 1.9 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 35.4 | 34.0 | 37.3 | 1.2 | 1.034x | 1.034x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 37.6 | 36.6 | 47.0 | 3.9 | 0.803x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 46.8 | 46.6 | 47.2 | 0.2 | 1.000x | 1.245x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 3,715,144.1 | 3,631,246.1 | 3,855,549.2 | 80,371.2 | 0.129x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 28,906,360.6 | 28,662,484.0 | 44,085,760.6 | 6,020,762.5 | 1.000x | 7.781x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 18,000.7 | 17,971.7 | 18,040.7 | 26.1 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 2,544,231.2 | 2,520,143.0 | 2,574,082.6 | 22,659.1 | 141.341x | 141.341x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 17,952.5 | 17,860.8 | 18,016.6 | 56.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 2,818,144.0 | 2,816,992.8 | 2,821,169.7 | 1,416.7 | 156.977x | 156.977x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_jit-caps-simdna` | measured | 5,960,488.6 | 5,959,187.3 | 5,964,918.6 | 2,187.2 | 0.064x | 1.000x |
| 2 | `libpcre2_10.46_interp-caps-simdna` | measured | 93,187,403.6 | 93,155,028.3 | 100,896,857.9 | 3,004,935.9 | 1.000x | 15.634x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: libpcre2_10.46_interp-caps-simdna (interp, present in this group)
| rank | testee | status | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|
| 1 | `libpcre2_10.46_interp-caps-simdna` | measured | 18,018.3 | 17,976.1 | 18,034.9 | 25.5 | 1.000x | 1.000x |
| 2 | `libpcre2_10.46_jit-caps-simdna` | measured | 3,156,052.2 | 3,155,215.9 | 3,168,053.4 | 4,936.6 | 175.158x | 175.158x |

## Excluded from ranking (expectation-failing cells)

| pattern | subject | regime | testee | n | pass-rate | gave-up | wrong | outcomes |
|---|---|---|---|---|---|---|---|---|
| `factored` | `t-c-long-atom-run` | `large-subject-throughput` | `libpcre2_10.46_jit-caps-simdna` | 5 | 0% | 0 | 0 | timed-out=5 |

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

