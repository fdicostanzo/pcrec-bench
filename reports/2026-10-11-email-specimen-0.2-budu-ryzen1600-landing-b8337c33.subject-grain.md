# pcrec-bench report

reporter: v25 (2026-09-26)

## Query

- filters: subbench=email-specimen, version=0.2, machine=budu-ryzen1600, since=2026-10-11T00:00:00Z, testee=pcrec_7388f1c0_auto-caps-simdna, testee=pcrec_7388f1c0_auto-nocaps-simdna, testee=pcrec_b8337c33_auto-caps-simdna, testee=pcrec_b8337c33_auto-nocaps-simdna
- record source: store/index.tsv (4 record(s) matching this query)
- records included: 4
- worst other-core busy: 23.68% (`pcrec_7388f1c0_auto-caps-simdna` / `floor` / `large-subject-throughput`)
    - `email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261011T054009Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-caps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-caps-simdna__budu-ryzen1600__20261011T054009Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials); after: occ 20.85%
    - `email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261011T055746Z` (store/records/email-specimen@0.2/pcrec_7388f1c0_auto-nocaps-simdna/email-specimen@0.2__pcrec_7388f1c0_auto-nocaps-simdna__budu-ryzen1600__20261011T055746Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261011T054614Z` (store/records/email-specimen@0.2/pcrec_b8337c33_auto-caps-simdna/email-specimen@0.2__pcrec_b8337c33_auto-caps-simdna__budu-ryzen1600__20261011T054614Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
    - `email-specimen@0.2__pcrec_b8337c33_auto-nocaps-simdna__budu-ryzen1600__20261011T055209Z` (store/records/email-specimen@0.2/pcrec_b8337c33_auto-nocaps-simdna/email-specimen@0.2__pcrec_b8337c33_auto-nocaps-simdna__budu-ryzen1600__20261011T055209Z.jsonl) — agreement: agree (0 of 9 groups; 0 of 501 rows; 0 unjudged; k=1.5, 2/3; 5 trials)
- sub-bench version(s): email-specimen@0.2
- machine(s): budu-ryzen1600
- schema version(s): 1.7
- grain: subject (per pattern x subject x regime; the drill-down)
- reduction: median/min/max/stddev (population) over per-trial `elapsed_ns / iterations`; lazy-JIT compile cost is DERIVED as first-match-row-minus-steady-state (lowest `seq` timed row for the pattern, minus the median of every other timed row), one value per (pattern, testee), never pooled with another execution-model class's compile cost
- `form`: this report includes a `whole-subject` artifact beside `plain` for at least one cell (schema v1.1: a testee with no end-anchored mode compiles and times a SEPARATE artifact for match-compliance, e.g. `(?:pattern)\z`, where another testee reaches the same regime via runtime flags on its ordinary artifact) -- shown as a per-row COLUMN, not a split: both forms answer the same regime and RANK TOGETHER in one table (`form` is a key only for compile-cost rows, where a whole-subject artifact is genuinely a separate compile with its own cost); `fact` restates it as 'same program' / 'separate artifact' (R4)
- status policy (OD-B14): a ranking row whose record `status` is not `measured` is excluded from ranking by default, listed under its table as `not ranked: <testee> -- <status> (<status_detail excerpt>)`; `--include-unmeasured` ranks it instead, with `status` shown
- trial-agreement policy (schema v1.4, rule v1.4-group, X31-X33): a record's five trials must agree to within k=1.5 on every group of its rows — one slow trial of five tolerated; two, or one fast, is a disagreeing row; a group disagrees at >= 2 disagreeing rows reaching a third of it (d_min=2, c=3); a record with a disagreeing group, or with fewer than five odd trials, is `inconclusive-spread` and unranked like `inconclusive-load`; the after-run load/occupancy samples are provenance (v1.4 X13), shown under --include-provenance
- status rule: v1.4 X13 (pre-flight + trial agreement) on 4 record(s)
- tier policy (R3, schema v1.2 `tier`, absent = `pinned`): a `scratch`-tier row is excluded from ranking by default, listed as `scratch: <testee>`; `--include-scratch` ranks it instead, with a `tier` column
- duplicate-record policy (OD-B15, amended 2026-08-25): the NEWEST MEASURED record per (subbench@version, testee_id, machine) ranks by default -- a newer record that is NOT measured does not supersede a measured one of the same testee and version (listed as "newer, not measured" instead); only when no record in the group is measured does the newest record overall stand (itself unranked per the status policy above, unless --include-unmeasured). `--all-records` shows every record as its own row, its testee id suffixed `@<timestamp>`

## Null-control band (D119 bar; [B79], inbox I-93 block B / I-104)

_Computed at SET grain only (the D119 bar is a set-grain statement, as R8's `Δ vs previous version` is); this subject-grain render carries no band -- render the same query at `--grain set`._

_[B85] (KB-28, a D119/[B82] follow-up): this report's roster spans BOTH capture classes, but at SUBJECT grain the class-pure views are NOT rendered as separate sections -- three passes over the same per-subject rows is a real-size hazard (107 MB on the AFTER groups this fix responded to). The single table below carries a `capture class` column instead (`yes`/`no`/`undeclared`, from `pcrecbench.capture_class`); a `--grain set` render of the same query still gets the two class-pure headline views._

## Ranking (per pattern x subject x regime; best median first)

### `factored` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.6 | 32.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.8 | 32.7 | 32.9 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.9 | 35.8 | 0.3 | 1.071x | 1.071x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.8 | 35.5 | 0.3 | 1.072x | 1.072x |

### `factored` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.5 | 63.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.7 | 63.5 | 63.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.3 | 68.5 | 0.1 | 1.076x | 1.076x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.4 | 68.6 | 0.1 | 1.077x | 1.077x |

### `factored` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.4 | 40.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.5 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.3 | 43.2 | 43.4 | 0.1 | 1.071x | 1.071x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.3 | 43.2 | 43.8 | 0.2 | 1.071x | 1.071x |

### `factored` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.9 | 82.9 | 83.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.9 | 82.8 | 83.0 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 86.2 | 86.1 | 86.2 | 0.1 | 1.040x | 1.040x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 86.4 | 86.0 | 86.4 | 0.1 | 1.042x | 1.042x |

### `factored` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.4 | 18.3 | 18.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.9 | 21.1 | 0.1 | 1.142x | 1.142x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.0 | 20.9 | 21.0 | 0.0 | 1.145x | 1.145x |

### `factored` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.7 | 30.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 28.9 | 30.2 | 0.5 | 1.012x | 1.012x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 32.2 | 32.1 | 32.2 | 0.0 | 1.111x | 1.111x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 32.8 | 32.2 | 32.9 | 0.3 | 1.132x | 1.132x |

### `factored` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.7 | 43.6 | 43.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.8 | 43.4 | 43.8 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.7 | 46.4 | 46.9 | 0.2 | 1.068x | 1.068x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.7 | 46.7 | 46.8 | 0.1 | 1.069x | 1.069x |

### `factored` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 89.8 | 89.5 | 90.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 90.1 | 89.7 | 90.7 | 0.3 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 93.5 | 93.4 | 93.9 | 0.2 | 1.041x | 1.041x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 93.6 | 93.1 | 93.9 | 0.3 | 1.042x | 1.042x |

### `factored` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.4 | 61.1 | 61.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.6 | 61.4 | 61.9 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 65.2 | 65.1 | 65.4 | 0.1 | 1.063x | 1.063x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 65.2 | 65.0 | 65.3 | 0.1 | 1.063x | 1.063x |

### `factored` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 124.9 | 124.8 | 125.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.2 | 125.0 | 125.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 129.0 | 128.8 | 129.3 | 0.2 | 1.033x | 1.033x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 129.1 | 128.7 | 129.1 | 0.2 | 1.033x | 1.033x |

### `factored` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.3 | 18.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.4 | 18.3 | 18.4 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.8 | 20.9 | 0.0 | 1.138x | 1.138x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.9 | 20.9 | 21.0 | 0.0 | 1.140x | 1.140x |

### `factored` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.8 | 28.7 | 29.8 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.9 | 28.7 | 29.7 | 0.3 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 32.5 | 32.2 | 33.2 | 0.3 | 1.130x | 1.130x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 32.9 | 32.2 | 33.5 | 0.5 | 1.146x | 1.146x |

### `factored` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.3 | 33.3 | 33.5 | 0.1 | 1.068x | 1.068x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.3 | 33.2 | 33.5 | 0.1 | 1.070x | 1.070x |

### `factored` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.1 | 60.1 | 60.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.2 | 60.1 | 60.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 64.2 | 64.2 | 64.4 | 0.1 | 1.068x | 1.068x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 64.3 | 64.2 | 64.4 | 0.1 | 1.069x | 1.069x |

### `factored` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.9 | 46.8 | 47.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.9 | 46.7 | 47.4 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 50.3 | 49.6 | 50.5 | 0.3 | 1.073x | 1.073x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 50.4 | 50.2 | 50.6 | 0.1 | 1.075x | 1.075x |

### `factored` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.7 | 95.7 | 96.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.8 | 95.5 | 96.0 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 100.7 | 100.5 | 100.8 | 0.1 | 1.052x | 1.052x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 100.8 | 100.6 | 101.0 | 0.1 | 1.053x | 1.053x |

### `factored` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 36.9 | 37.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 37.0 | 37.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 39.5 | 39.4 | 39.7 | 0.1 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 39.7 | 39.5 | 39.7 | 0.1 | 1.071x | 1.071x |

### `factored` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.4 | 74.2 | 74.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.6 | 74.3 | 74.7 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 78.5 | 78.4 | 78.7 | 0.1 | 1.055x | 1.055x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 78.5 | 78.4 | 78.7 | 0.1 | 1.056x | 1.056x |

### `factored` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.0 | 0.0 | 1.077x | 1.077x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.5 | 0.2 | 1.078x | 1.078x |

### `factored` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.4 | 56.3 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.1 | 56.6 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.6 | 60.6 | 60.7 | 0.1 | 1.074x | 1.074x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.5 | 61.0 | 0.2 | 1.075x | 1.075x |

### `factored` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.4 | 0.2 | 1.079x | 1.079x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.1 | 31.9 | 32.2 | 0.1 | 1.080x | 1.080x |

### `factored` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.3 | 56.8 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.6 | 61.1 | 0.2 | 1.073x | 1.073x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.8 | 60.7 | 61.2 | 0.2 | 1.075x | 1.075x |

### `factored` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.9 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.9 | 12.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.2 | 0.1 | 1.008x | 1.008x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.012x | 1.012x |

### `factored` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.8 | 37.7 | 38.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 37.9 | 37.6 | 38.2 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 37.9 | 37.8 | 38.1 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 38.0 | 37.8 | 38.1 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.0 | 37.8 | 38.4 | 0.2 | 1.070x | 1.070x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.3 | 37.9 | 38.4 | 0.2 | 1.079x | 1.079x |

### `factored` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.4 | 71.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.5 | 72.2 | 0.6 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.2 | 75.4 | 0.1 | 1.064x | 1.064x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.1 | 75.4 | 0.1 | 1.065x | 1.065x |

### `factored` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.5 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.8 | 37.4 | 38.1 | 0.3 | 1.065x | 1.065x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.0 | 37.5 | 38.2 | 0.3 | 1.069x | 1.069x |

### `factored` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 71.6 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 71.1 | 71.0 | 71.2 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.2 | 75.4 | 0.1 | 1.064x | 1.064x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.0 | 75.4 | 0.2 | 1.065x | 1.065x |

### `factored` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 30.4 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.8 | 29.7 | 29.9 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 32.0 | 32.2 | 0.1 | 1.079x | 1.079x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.1 | 31.9 | 32.2 | 0.1 | 1.080x | 1.080x |

### `factored` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.2 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.5 | 56.6 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.6 | 60.5 | 60.7 | 0.1 | 1.072x | 1.072x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.5 | 60.8 | 0.1 | 1.074x | 1.074x |

### `factored` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.8 | 34.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.4 | 36.6 | 0.1 | 1.071x | 1.071x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.2 | 37.1 | 0.3 | 1.071x | 1.071x |

### `factored` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 67.0 | 67.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 66.9 | 67.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.1 | 72.2 | 0.0 | 1.076x | 1.076x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.1 | 72.2 | 0.1 | 1.076x | 1.076x |

### `factored` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 9.4 | 9.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 9.4 | 9.5 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 9.8 | 9.8 | 0.0 | 1.034x | 1.034x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 9.8 | 9.8 | 0.0 | 1.034x | 1.034x |

### `factored` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.1 | 29.0 | 29.5 | 0.2 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 29.0 | 29.8 | 0.3 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.0 | 29.5 | 0.2 | 1.012x | 1.012x |

### `factored` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.8 | 37.6 | 38.2 | 0.3 | 1.063x | 1.063x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.9 | 37.5 | 38.2 | 0.2 | 1.067x | 1.067x |

### `factored` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.3 | 71.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.4 | 71.4 | 0.4 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.3 | 75.4 | 0.1 | 1.065x | 1.065x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.4 | 75.2 | 75.5 | 0.1 | 1.066x | 1.066x |

### `factored` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 34.0 | 34.1 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.4 | 36.3 | 36.5 | 0.1 | 1.074x | 1.074x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.5 | 36.3 | 37.0 | 0.2 | 1.076x | 1.076x |

### `factored` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 67.0 | 67.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 67.0 | 67.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.1 | 72.3 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.1 | 72.1 | 72.4 | 0.1 | 1.077x | 1.077x |

### `factored` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.7 | 9.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.7 | 10.1 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.5 | 0.1 | 1.051x | 1.051x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.0 | 0.3 | 1.054x | 1.054x |

### `factored` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.9 | 30.7 | 31.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.9 | 30.7 | 30.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.9 | 30.6 | 31.4 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 31.0 | 30.5 | 31.4 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.6 | 38.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.8 | 38.7 | 38.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.4 | 41.3 | 41.8 | 0.2 | 1.068x | 1.068x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.4 | 41.2 | 41.6 | 0.1 | 1.069x | 1.069x |

### `factored` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.7 | 77.7 | 77.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.8 | 77.7 | 77.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 82.0 | 81.9 | 82.0 | 0.0 | 1.055x | 1.055x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 82.0 | 82.0 | 82.1 | 0.0 | 1.056x | 1.056x |

### `factored` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.8 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.8 | 29.7 | 30.0 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.8 | 32.4 | 0.2 | 1.075x | 1.075x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.1 | 31.8 | 32.4 | 0.2 | 1.076x | 1.076x |

### `factored` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.5 | 56.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.6 | 60.5 | 60.7 | 0.1 | 1.073x | 1.073x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.8 | 60.5 | 61.2 | 0.2 | 1.076x | 1.076x |

### `factored` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.1 | 41.9 | 42.2 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.7 | 44.6 | 44.9 | 0.1 | 1.068x | 1.068x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.1 | 0.2 | 1.069x | 1.069x |

### `factored` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 85.0 | 85.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.2 | 84.9 | 85.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 90.1 | 89.9 | 90.2 | 0.1 | 1.060x | 1.060x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.2 | 90.0 | 90.3 | 0.1 | 1.061x | 1.061x |

### `factored` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.6 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.4 | 37.9 | 0.2 | 1.058x | 1.058x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.6 | 37.5 | 38.3 | 0.4 | 1.060x | 1.060x |

### `factored` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.6 | 70.5 | 70.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.6 | 70.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.1 | 75.4 | 0.1 | 1.066x | 1.066x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.2 | 75.4 | 0.1 | 1.067x | 1.067x |

### `factored` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.9 | 31.9 | 32.7 | 0.3 | 1.074x | 1.074x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.0 | 31.9 | 32.1 | 0.1 | 1.075x | 1.075x |

### `factored` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.3 | 56.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.5 | 60.3 | 61.0 | 0.2 | 1.071x | 1.071x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.7 | 60.5 | 61.2 | 0.3 | 1.075x | 1.075x |

### `factored` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.2 | 35.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.8 | 37.6 | 38.3 | 0.3 | 1.063x | 1.063x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.9 | 37.4 | 38.6 | 0.5 | 1.068x | 1.068x |

### `factored` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.6 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.6 | 70.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.0 | 75.4 | 0.1 | 1.065x | 1.065x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.3 | 75.4 | 0.0 | 1.065x | 1.065x |

### `factored` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.8 | 42.1 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.7 | 44.6 | 45.0 | 0.1 | 1.067x | 1.067x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.1 | 0.1 | 1.070x | 1.070x |

### `factored` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.1 | 85.0 | 85.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.2 | 84.8 | 85.2 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 90.0 | 89.6 | 90.2 | 0.2 | 1.057x | 1.057x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.2 | 90.0 | 90.2 | 0.1 | 1.060x | 1.060x |

### `factored` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.7 | 41.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.9 | 42.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.8 | 44.6 | 45.1 | 0.2 | 1.069x | 1.069x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 44.9 | 44.9 | 46.1 | 0.5 | 1.072x | 1.072x |

### `factored` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.9 | 85.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.1 | 85.1 | 85.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.0 | 89.8 | 90.3 | 0.2 | 1.059x | 1.059x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 90.2 | 89.7 | 90.3 | 0.3 | 1.062x | 1.062x |

### `factored` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 1.011x | 1.011x |

### `factored` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.0 | 24.9 | 25.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.0 | 24.9 | 25.5 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.1 | 25.0 | 25.3 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 25.0 | 25.2 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.009x | 1.009x |

### `factored` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.7 | 49.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 48.8 | 48.8 | 48.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.9 | 48.7 | 49.1 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 48.9 | 48.9 | 49.2 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.1 | 25.0 | 25.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 25.2 | 25.1 | 25.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.2 | 25.0 | 25.6 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.2 | 25.1 | 25.3 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 33.2 | 33.1 | 34.2 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.3 | 33.0 | 34.1 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.3 | 33.1 | 33.9 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 33.3 | 33.1 | 33.5 | 0.2 | 1.002x | 1.002x |

### `factored` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.3 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.1 | 1.001x | 1.001x |

### `factored` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.2 | 29.1 | 29.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.2 | 30.1 | 0.3 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.2 | 29.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.2 | 29.6 | 0.1 | 1.007x | 1.007x |

### `factored` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.1 | 29.0 | 29.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.2 | 29.1 | 29.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.1 | 30.0 | 0.3 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.2 | 30.3 | 0.4 | 1.009x | 1.009x |

### `factored` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.4 | 20.3 | 20.4 | 0.0 | 1.004x | 1.004x |

### `factored` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.4 | 21.4 | 21.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.5 | 21.4 | 21.6 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 21.5 | 21.4 | 21.7 | 0.1 | 1.007x | 1.007x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.6 | 21.4 | 21.8 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 22.9 | 23.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.2 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.2 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.0 | 28.0 | 28.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.2 | 28.2 | 28.3 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.4 | 28.2 | 28.7 | 0.1 | 1.014x | 1.014x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.5 | 27.9 | 29.0 | 0.4 | 1.017x | 1.017x |

### `factored` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.7 | 11.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.3 | 0.2 | 1.024x | 1.024x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.026x | 1.026x |

### `factored` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.7 | 29.2 | 30.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.6 | 30.1 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.8 | 29.4 | 30.3 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.1 | 29.8 | 30.3 | 0.2 | 1.010x | 1.010x |

### `factored` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.7 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 1.003x | 1.003x |

### `factored` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.5 | 23.3 | 23.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.8 | 23.4 | 24.0 | 0.2 | 1.010x | 1.010x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.8 | 23.3 | 23.9 | 0.2 | 1.010x | 1.010x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 24.2 | 23.8 | 24.5 | 0.2 | 1.030x | 1.030x |

### `factored` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.8 | 0.3 | 1.005x | 1.005x |

### `factored` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.6 | 29.2 | 29.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.7 | 29.3 | 30.3 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.9 | 29.8 | 30.4 | 0.2 | 1.010x | 1.010x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.6 | 30.3 | 0.3 | 1.010x | 1.010x |

### `factored` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.9 | 9.8 | 10.0 | 0.1 | 1.009x | 1.009x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.6 | 0.1 | 1.053x | 1.053x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.4 | 0.1 | 1.054x | 1.054x |

### `factored` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.5 | 63.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.7 | 63.5 | 63.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.6 | 68.5 | 68.9 | 0.1 | 1.079x | 1.079x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.7 | 68.5 | 68.9 | 0.1 | 1.080x | 1.080x |

### `factored` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.2 | 26.1 | 26.4 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.2 | 26.2 | 26.4 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 7.4 | 8.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 7.4 | 7.4 | 8.4 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.4 | 7.4 | 7.9 | 0.2 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.6 | 7.4 | 8.9 | 0.6 | 1.032x | 1.032x |

### `factored` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 10.6 | 0.7 | 1.064x | 1.064x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 8.6 | 10.3 | 0.6 | 1.064x | 1.064x |

### `factored` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.7 | 21.5 | 21.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.1 | 21.7 | 22.1 | 0.2 | 1.017x | 1.017x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 22.1 | 21.9 | 22.4 | 0.2 | 1.022x | 1.022x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.3 | 21.8 | 22.8 | 0.4 | 1.027x | 1.027x |

### `factored` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.3 | 12.1 | 12.4 | 0.1 | 1.013x | 1.013x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.6 | 0.0 | 1.028x | 1.028x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.6 | 12.5 | 12.7 | 0.1 | 1.039x | 1.039x |

### `factored` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.2 | 13.9 | 14.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.4 | 14.2 | 14.6 | 0.1 | 1.018x | 1.018x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 14.8 | 14.1 | 15.2 | 0.4 | 1.044x | 1.044x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 14.9 | 14.2 | 15.2 | 0.4 | 1.055x | 1.055x |

### `factored` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.8 | 11.9 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.021x | 1.021x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.024x | 1.024x |

### `factored` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.5 | 75.3 | 75.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.7 | 75.3 | 75.8 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 79.8 | 79.2 | 80.0 | 0.3 | 1.057x | 1.057x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 80.0 | 79.7 | 80.1 | 0.1 | 1.060x | 1.060x |

### `factored` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 9.5 | 0.4 | 1.062x | 1.062x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 10.6 | 0.7 | 1.064x | 1.064x |

### `factored` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.4 | 65.3 | 65.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.6 | 65.2 | 65.6 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.3 | 70.3 | 70.5 | 0.1 | 1.075x | 1.075x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 70.4 | 70.3 | 70.6 | 0.1 | 1.076x | 1.076x |

### `factored` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.9 | 12.0 | 0.1 | 1.007x | 1.007x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.1 | 0.1 | 1.019x | 1.019x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.2 | 0.2 | 1.024x | 1.024x |

### `factored` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.5 | 28.1 | 28.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.6 | 28.5 | 29.2 | 0.3 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.6 | 28.3 | 28.9 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.5 | 29.1 | 0.2 | 1.014x | 1.014x |

### `factored` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.8 | 21.8 | 22.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 1.006x | 1.006x |

### `factored` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.5 | 21.4 | 21.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 21.5 | 21.4 | 22.1 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.7 | 21.5 | 22.0 | 0.2 | 1.008x | 1.008x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.8 | 21.5 | 22.1 | 0.2 | 1.017x | 1.017x |

### `factored` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.2 | 0.0 | 1.003x | 1.003x |

### `factored` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.9 | 22.8 | 23.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 22.9 | 22.8 | 23.2 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.0 | 22.8 | 23.3 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.1 | 22.9 | 23.3 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.006x | 1.006x |

### `factored` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 15.0 | 14.9 | 15.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 15.0 | 14.9 | 15.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.1 | 15.4 | 0.1 | 1.022x | 1.022x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.5 | 15.3 | 16.2 | 0.3 | 1.033x | 1.033x |

### `factored` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.8 | 10.5 | 10.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.8 | 10.4 | 10.9 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.2 | 11.1 | 11.3 | 0.1 | 1.044x | 1.044x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.2 | 11.0 | 11.3 | 0.1 | 1.045x | 1.045x |

### `factored` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.0 | 72.7 | 73.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.0 | 73.0 | 73.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.4 | 77.2 | 77.5 | 0.1 | 1.060x | 1.060x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.5 | 77.9 | 0.1 | 1.064x | 1.064x |

### `factored` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.6 | 14.7 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.7 | 0.1 | 1.005x | 1.005x |

### `factored` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 58.0 | 57.9 | 58.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 58.1 | 57.9 | 58.3 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 62.7 | 62.4 | 63.0 | 0.2 | 1.082x | 1.082x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 62.8 | 62.4 | 62.9 | 0.2 | 1.083x | 1.083x |

### `factored` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.7 | 10.6 | 10.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.5 | 11.0 | 0.2 | 1.022x | 1.022x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.0 | 10.7 | 11.2 | 0.2 | 1.029x | 1.029x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.2 | 10.5 | 11.3 | 0.3 | 1.047x | 1.047x |

### `factored` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.1 | 73.0 | 73.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.2 | 73.2 | 73.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.4 | 77.4 | 77.5 | 0.0 | 1.059x | 1.059x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 77.6 | 77.4 | 77.7 | 0.1 | 1.061x | 1.061x |

### `factored` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 1.004x | 1.004x |

### `factored` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 22.5 | 22.4 | 23.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.7 | 22.7 | 23.0 | 0.1 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.0 | 22.6 | 23.4 | 0.3 | 1.021x | 1.021x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.1 | 22.9 | 23.3 | 0.2 | 1.026x | 1.026x |

### `factored` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.008x | 1.008x |

### `factored` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.9 | 17.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17.0 | 16.7 | 17.7 | 0.4 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.3 | 17.2 | 17.8 | 0.2 | 1.021x | 1.021x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.4 | 17.1 | 18.7 | 0.6 | 1.027x | 1.027x |

### `factored` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.006x | 1.006x |

### `factored` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.8 | 17.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 16.8 | 17.7 | 0.3 | 1.009x | 1.009x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 16.7 | 17.9 | 0.4 | 1.010x | 1.010x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 16.6 | 17.4 | 0.3 | 1.015x | 1.015x |

### `factored` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 1.007x | 1.007x |

### `factored` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 16.8 | 16.5 | 17.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 16.8 | 16.6 | 16.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 16.8 | 17.2 | 0.2 | 1.021x | 1.021x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.2 | 16.9 | 17.4 | 0.2 | 1.024x | 1.024x |

### `factored` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.4 | 13.2 | 13.4 | 0.1 | 1.010x | 1.010x |

### `factored` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 19.1 | 19.0 | 19.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 19.3 | 19.1 | 19.4 | 0.1 | 1.009x | 1.009x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.3 | 19.2 | 19.5 | 0.1 | 1.013x | 1.013x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.6 | 19.1 | 19.8 | 0.3 | 1.026x | 1.026x |

### `factored` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,063.6 | 19,063.5 | 19,064.2 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,071.1 | 19,069.9 | 19,072.8 | 1.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,071.6 | 19,070.1 | 19,145.1 | 29.4 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,072.8 | 19,069.4 | 19,075.0 | 2.1 | 1.000x | 1.000x |

### `factored` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,462.7 | 7,461.6 | 7,465.4 | 1.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,463.1 | 7,462.5 | 7,465.1 | 1.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,464.2 | 7,463.8 | 7,467.2 | 1.2 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,464.6 | 7,462.5 | 7,466.5 | 1.6 | 1.000x | 1.000x |

### `factored` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,548.8 | 9,548.4 | 9,549.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,551.3 | 9,550.8 | 9,552.0 | 0.4 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,552.7 | 9,550.2 | 9,555.1 | 1.8 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,552.8 | 9,551.9 | 9,555.2 | 1.1 | 1.000x | 1.000x |

### `factored` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,036.3 | 19,035.9 | 19,038.3 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,045.2 | 19,043.5 | 19,046.5 | 1.3 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,047.1 | 19,041.6 | 19,053.1 | 3.7 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,048.6 | 19,047.1 | 19,052.8 | 2.0 | 1.001x | 1.001x |

### `factored` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,739.1 | 3,738.4 | 3,741.6 | 1.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,739.3 | 3,738.0 | 3,740.2 | 0.7 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,739.6 | 3,738.3 | 3,741.1 | 0.9 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,740.5 | 3,739.7 | 3,744.1 | 1.7 | 1.000x | 1.000x |

### `factored` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.3 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.8 | 0.3 | 1.004x | 1.004x |

### `factored` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,785.6 | 4,785.2 | 4,787.6 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,787.3 | 4,786.5 | 4,790.0 | 1.4 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,787.5 | 4,785.3 | 4,787.6 | 1.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,788.1 | 4,782.6 | 4,789.6 | 2.5 | 1.001x | 1.001x |

### `factored` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,645.4 | 7,644.8 | 7,645.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,646.3 | 7,645.7 | 7,647.9 | 0.9 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,648.3 | 7,648.0 | 7,648.7 | 0.3 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,648.8 | 7,648.0 | 7,651.4 | 1.2 | 1.000x | 1.000x |

### `factored` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.6 | 8.6 | 9.5 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.041x | 1.041x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.0 | 0.0 | 1.041x | 1.041x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.4 | 8.6 | 9.9 | 0.5 | 1.104x | 1.104x |

### `factored` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.9 | 23.9 | 24.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.0 | 23.9 | 25.1 | 0.4 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 24.5 | 23.7 | 24.7 | 0.3 | 1.021x | 1.021x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.7 | 24.5 | 25.3 | 0.3 | 1.031x | 1.031x |

### `factored` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.1 | 33.8 | 34.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.1 | 34.0 | 34.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.7 | 36.3 | 38.2 | 0.7 | 1.078x | 1.078x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.8 | 36.3 | 37.2 | 0.3 | 1.082x | 1.082x |

### `factored` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 67.0 | 67.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.2 | 67.0 | 67.7 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.2 | 72.1 | 72.3 | 0.1 | 1.076x | 1.076x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 72.2 | 72.1 | 72.3 | 0.1 | 1.077x | 1.077x |

### `factored` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.8 | 34.7 | 35.3 | 0.2 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.6 | 35.1 | 0.2 | 1.068x | 1.068x |

### `factored` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.4 | 63.5 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.4 | 0.1 | 1.078x | 1.078x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.1 | 68.8 | 0.2 | 1.079x | 1.079x |

### `factored` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.8 | 16.7 | 17.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.8 | 16.8 | 17.0 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.5 | 19.4 | 19.5 | 0.0 | 1.159x | 1.159x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.5 | 19.4 | 19.6 | 0.1 | 1.162x | 1.162x |

### `factored` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.9 | 25.8 | 26.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 26.2 | 25.9 | 26.9 | 0.3 | 1.010x | 1.010x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.7 | 28.6 | 29.9 | 0.6 | 1.108x | 1.108x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.8 | 28.7 | 29.0 | 0.1 | 1.112x | 1.112x |

### `factored` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.8 | 11.7 | 11.8 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.030x | 1.030x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.3 | 0.1 | 1.033x | 1.033x |

### `factored` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.2 | 30.1 | 30.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.3 | 30.1 | 30.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.3 | 30.1 | 30.6 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.4 | 30.1 | 30.5 | 0.2 | 1.004x | 1.004x |

### `factored` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.2 | 28.2 | 28.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.3 | 28.2 | 28.3 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 30.5 | 30.5 | 30.6 | 0.0 | 1.082x | 1.082x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 30.8 | 30.6 | 30.8 | 0.1 | 1.090x | 1.090x |

### `factored` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.8 | 52.8 | 53.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.9 | 52.8 | 54.4 | 0.6 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 57.7 | 57.6 | 57.8 | 0.1 | 1.092x | 1.092x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 57.9 | 57.0 | 57.9 | 0.4 | 1.095x | 1.095x |

### `factored` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.2 | 56.1 | 56.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.3 | 56.3 | 56.5 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 59.8 | 59.7 | 60.1 | 0.2 | 1.064x | 1.064x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 59.9 | 59.7 | 67.7 | 3.1 | 1.067x | 1.067x |

### `factored` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.6 | 114.3 | 115.0 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.7 | 114.5 | 115.1 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 118.5 | 118.4 | 118.7 | 0.1 | 1.034x | 1.034x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 118.5 | 118.3 | 118.8 | 0.1 | 1.034x | 1.034x |

### `factored` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.0 | 42.9 | 43.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.0 | 42.8 | 43.3 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.0 | 43.0 | 43.7 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.4 | 0.1 | 1.002x | 1.002x |

### `factored` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 94.0 | 93.9 | 94.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 94.3 | 93.9 | 95.0 | 0.4 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 99.0 | 98.9 | 99.2 | 0.1 | 1.054x | 1.054x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 99.2 | 98.9 | 99.3 | 0.1 | 1.055x | 1.055x |

### `factored` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.0 | 1.006x | 1.006x |

### `factored` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.2 | 23.2 | 23.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.2 | 23.1 | 23.5 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.3 | 23.1 | 24.0 | 0.3 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.3 | 23.1 | 23.6 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.7 | 30.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.8 | 30.5 | 0.3 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.9 | 29.7 | 30.4 | 0.2 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.9 | 30.3 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.6 | 32.7 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.8 | 35.1 | 0.1 | 1.074x | 1.074x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.2 | 34.8 | 35.4 | 0.2 | 1.080x | 1.080x |

### `factored` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.3 | 64.7 | 0.5 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.2 | 68.0 | 68.3 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.8 | 0.2 | 1.079x | 1.079x |

### `factored` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.6 | 34.3 | 0.7 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.7 | 34.7 | 35.1 | 0.2 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.0 | 34.7 | 35.3 | 0.2 | 1.075x | 1.075x |

### `factored` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.9 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.4 | 0.1 | 1.077x | 1.077x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.8 | 0.3 | 1.078x | 1.078x |

### `factored` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.5 | 32.8 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.8 | 34.7 | 34.9 | 0.1 | 1.068x | 1.068x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.7 | 35.2 | 0.2 | 1.070x | 1.070x |

### `factored` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.0 | 68.5 | 0.2 | 1.078x | 1.078x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.4 | 68.1 | 68.5 | 0.1 | 1.078x | 1.078x |

### `factored` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.8 | 35.0 | 0.1 | 1.071x | 1.071x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.5 | 35.1 | 0.2 | 1.073x | 1.073x |

### `factored` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.2 | 63.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.6 | 0.2 | 1.078x | 1.078x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 68.1 | 68.4 | 0.1 | 1.078x | 1.078x |

### `factored` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.7 | 34.6 | 34.9 | 0.1 | 1.066x | 1.066x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.9 | 34.6 | 35.0 | 0.1 | 1.070x | 1.070x |

### `factored` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 64.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.3 | 64.0 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 68.3 | 67.9 | 68.8 | 0.3 | 1.077x | 1.077x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 68.6 | 68.1 | 68.7 | 0.2 | 1.082x | 1.082x |

### `factored` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.0 | 1.004x | 1.004x |

### `factored` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.1 | 29.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.3 | 29.6 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.2 | 30.0 | 0.3 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.1 | 29.6 | 0.2 | 1.005x | 1.005x |

### `factored` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.4 | 11.8 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 9.7 | 10.4 | 0.2 | 1.023x | 1.023x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.1 | 9.7 | 11.4 | 0.6 | 1.028x | 1.028x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.2 | 9.8 | 11.4 | 0.6 | 1.038x | 1.038x |

### `factored` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 4.0 | 3.9 | 4.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.2 | 0.0 | 1.044x | 1.044x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.2 | 0.0 | 1.046x | 1.046x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 5.0 | 3.9 | 5.0 | 0.6 | 1.266x | 1.266x |

### `factored` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.1 | 0.5 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 9.4 | 10.6 | 0.5 | 1.064x | 1.064x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.5 | 8.6 | 10.1 | 0.5 | 1.064x | 1.064x |

### `factored` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 8.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.3 | 8.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.3 | 8.4 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.4 | 8.3 | 9.1 | 0.3 | 1.014x | 1.014x |

### `factored` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.7 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.026x | 1.026x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.4 | 0.1 | 1.032x | 1.032x |

### `factored` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.0 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.0 | 0.0 | 1.001x | 1.001x |

### `factored` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.2 | 19.2 | 19.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.4 | 0.1 | 1.004x | 1.004x |

### `factored` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.6 | 7.4 | 8.3 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.7 | 7.4 | 8.6 | 0.5 | 1.024x | 1.024x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 7.8 | 7.4 | 9.3 | 0.6 | 1.030x | 1.030x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.7 | 7.4 | 9.7 | 0.9 | 1.146x | 1.146x |

### `factored` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,783,423.4 | 3,782,817.8 | 3,787,644.6 | 1,933.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,784,653.7 | 3,782,848.8 | 3,792,979.4 | 3,769.9 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,805,462.8 | 3,804,656.7 | 3,806,180.6 | 629.8 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 3,807,136.4 | 3,806,158.3 | 3,808,283.6 | 776.9 | 1.006x | 1.006x |

### `factored` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,677.9 | 17,648.1 | 17,700.0 | 16.8 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,678.9 | 17,667.4 | 17,692.1 | 8.8 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,720.0 | 17,704.3 | 17,789.6 | 31.6 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,745.9 | 17,727.2 | 17,787.9 | 21.2 | 1.004x | 1.004x |

### `factored` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,689.5 | 17,672.0 | 17,716.2 | 15.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,698.6 | 17,685.3 | 17,801.4 | 42.5 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,703.1 | 17,674.6 | 17,716.5 | 14.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,722.6 | 17,691.8 | 17,751.8 | 21.9 | 1.002x | 1.002x |

### `factored` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 3,162,106.4 | 3,161,351.7 | 3,166,186.6 | 1,920.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,162,541.5 | 3,157,672.8 | 3,169,898.0 | 4,359.5 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,219,462.6 | 3,217,766.5 | 3,222,646.3 | 1,638.8 | 1.018x | 1.018x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,221,767.3 | 3,218,829.3 | 3,227,671.6 | 2,919.0 | 1.019x | 1.019x |

### `factored` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,683.5 | 17,659.4 | 17,926.3 | 100.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,689.1 | 17,671.2 | 17,702.6 | 10.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,716.3 | 17,691.7 | 17,721.0 | 11.3 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,732.0 | 17,703.5 | 17,810.1 | 38.8 | 1.003x | 1.003x |

### `floor` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.003x | 1.003x |

### `floor` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.3 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.362x | 1.362x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.8 | 17.7 | 17.8 | 0.0 | 1.365x | 1.365x |

### `floor` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.4 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 15.0 | 0.8 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.1 | 1.361x | 1.361x |

### `floor` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 15.6 | 1.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 1.359x | 1.359x |

### `floor` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.4 | 13.3 | 13.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.5 | 13.4 | 13.5 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 18.2 | 18.2 | 18.2 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 18.2 | 18.2 | 18.4 | 0.1 | 1.359x | 1.359x |

### `floor` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.4 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.1 | 13.0 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.349x | 1.349x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.351x | 1.351x |

### `floor` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.6 | 0.4 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.361x | 1.361x |

### `floor` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 12.9 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.1 | 0.0 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.3 | 1.361x | 1.361x |

### `floor` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.2 | 0.1 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.2 | 0.1 | 1.012x | 1.012x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.363x | 1.363x |

### `floor` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.9 | 0.3 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.4 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 14.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |

### `floor` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.5 | 17.8 | 0.1 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.358x | 1.358x |

### `floor` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.1 | 13.0 | 13.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.353x | 1.353x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.354x | 1.354x |

### `floor` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.9 | 0.3 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |

### `floor` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.9 | 0.3 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.8 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.2 | 13.0 | 13.8 | 0.3 | 1.013x | 1.013x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.5 | 17.7 | 0.1 | 1.354x | 1.354x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.360x | 1.360x |

### `floor` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.354x | 1.354x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |

### `floor` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.1 | 0.1 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.5 | 18.5 | 0.4 | 1.360x | 1.360x |

### `floor` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.360x | 1.360x |

### `floor` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.1 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.8 | 0.0 | 1.364x | 1.364x |

### `floor` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.5 | 0.3 | 1.361x | 1.361x |

### `floor` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.362x | 1.362x |

### `floor` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.9 | 0.1 | 1.364x | 1.364x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.365x | 1.365x |

### `floor` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 18.6 | 0.4 | 1.363x | 1.363x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.364x | 1.364x |

### `floor` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.1 | 0.2 | 1.361x | 1.361x |

### `floor` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.8 | 0.1 | 1.360x | 1.360x |

### `floor` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.364x | 1.364x |

### `floor` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.9 | 8.9 | 9.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.9 | 8.9 | 9.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.9 | 8.9 | 9.5 | 0.3 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 9.2 | 9.0 | 10.3 | 0.5 | 1.039x | 1.039x |

### `floor` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.2 | 9.2 | 9.2 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.2 | 9.2 | 10.0 | 0.3 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.3 | 9.1 | 10.0 | 0.3 | 1.014x | 1.014x |

### `floor` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.2 | 13.0 | 13.8 | 0.3 | 1.018x | 1.018x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.9 | 17.0 | 0.0 | 1.301x | 1.301x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.9 | 16.9 | 0.0 | 1.303x | 1.303x |

### `floor` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 12.6 | 12.5 | 12.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 12.6 | 12.6 | 12.6 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.5 | 17.4 | 17.5 | 0.0 | 1.390x | 1.390x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.5 | 17.5 | 18.4 | 0.4 | 1.390x | 1.390x |

### `floor` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.5 | 0.4 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.363x | 1.363x |

### `floor` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 18.3 | 0.2 | 1.363x | 1.363x |

### `floor` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.361x | 1.361x |

### `floor` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.356x | 1.356x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |

### `floor` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.362x | 1.362x |

### `floor` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.362x | 1.362x |

### `floor` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.362x | 1.362x |

### `floor` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.8 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 14.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.9 | 0.1 | 1.359x | 1.359x |

### `floor` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.4 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.362x | 1.362x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 18.1 | 0.2 | 1.363x | 1.363x |

### `floor` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.002x | 1.002x |

### `floor` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |

### `floor` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.8 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.7 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 18.2 | 0.2 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.360x | 1.360x |

### `floor` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.359x | 1.359x |

### `floor` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.0 | 1.361x | 1.361x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.361x | 1.361x |

### `floor` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.8 | 0.3 | 1.010x | 1.010x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |

### `floor` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.9 | 0.4 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 18.4 | 0.3 | 1.361x | 1.361x |

### `floor` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.1 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.2 | 13.0 | 13.5 | 0.2 | 1.007x | 1.007x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.349x | 1.349x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 19.0 | 0.5 | 1.354x | 1.354x |

### `floor` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.5 | 17.7 | 0.1 | 1.359x | 1.359x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.8 | 0.1 | 1.359x | 1.359x |

### `floor` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.2 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.4 | 17.7 | 0.1 | 1.358x | 1.358x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.1 | 13.0 | 13.3 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.1 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.360x | 1.360x |

### `floor` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.360x | 1.360x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.7 | 17.7 | 17.7 | 0.0 | 1.362x | 1.362x |

### `floor` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 11.6 | 1.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 13.0 | 13.0 | 13.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.6 | 17.6 | 17.7 | 0.0 | 1.357x | 1.357x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.7 | 17.6 | 17.7 | 0.0 | 1.358x | 1.358x |

### `floor` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.0 | 9.9 | 10.4 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.1 | 10.0 | 11.1 | 0.4 | 1.011x | 1.011x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.0 | 11.0 | 0.4 | 1.024x | 1.024x |

### `floor` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 6.2 | 6.2 | 6.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 6.4 | 6.2 | 7.2 | 0.4 | 1.032x | 1.032x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 6.5 | 6.5 | 6.5 | 0.0 | 1.047x | 1.047x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 6.5 | 6.5 | 6.7 | 0.1 | 1.047x | 1.047x |

### `floor` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.0 | 13.0 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.0 | 13.0 | 14.6 | 0.6 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.1 | 13.0 | 13.1 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.1 | 13.0 | 14.2 | 0.5 | 1.005x | 1.005x |

### `floor` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 12.6 | 12.5 | 12.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 12.6 | 12.6 | 12.7 | 0.0 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.0 | 16.9 | 17.1 | 0.1 | 1.355x | 1.355x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.2 | 17.1 | 17.8 | 0.3 | 1.367x | 1.367x |

### `floor` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.1 | 0.5 | 1.007x | 1.007x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.0 | 8.9 | 9.7 | 0.4 | 1.012x | 1.012x |

### `floor` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.6 | 9.5 | 9.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.8 | 9.5 | 10.5 | 0.3 | 1.016x | 1.016x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 10.3 | 9.5 | 10.4 | 0.4 | 1.076x | 1.076x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 10.5 | 9.7 | 11.2 | 0.5 | 1.091x | 1.091x |

### `floor` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.7 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 8.9 | 0.0 | 1.001x | 1.001x |

### `floor` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.1 | 8.9 | 9.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 9.2 | 8.9 | 10.8 | 0.7 | 1.012x | 1.012x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.2 | 8.9 | 10.5 | 0.7 | 1.012x | 1.012x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 9.2 | 9.1 | 9.4 | 0.1 | 1.015x | 1.015x |

### `floor` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 576,391.5 | 576,340.9 | 576,773.1 | 188.8 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 576,758.3 | 576,477.6 | 577,392.8 | 305.3 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 614,889.3 | 614,528.8 | 629,657.6 | 5,833.8 | 1.067x | 1.067x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 614,985.7 | 614,740.1 | 615,331.7 | 208.4 | 1.067x | 1.067x |

### `floor` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,669.3 | 17,646.1 | 17,731.1 | 30.5 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,713.3 | 17,689.8 | 17,748.7 | 20.5 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,728.5 | 17,699.4 | 17,751.2 | 18.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,737.2 | 17,707.4 | 17,773.1 | 24.6 | 1.004x | 1.004x |

### `floor` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,681.5 | 17,652.1 | 17,698.7 | 16.8 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,700.9 | 17,698.8 | 17,717.3 | 6.8 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,710.2 | 17,686.8 | 17,723.2 | 13.7 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,713.4 | 17,707.3 | 17,817.3 | 41.8 | 1.002x | 1.002x |

### `floor` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30,309.3 | 30,264.1 | 30,344.5 | 25.8 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30,472.3 | 30,333.4 | 30,514.3 | 67.6 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30,963.8 | 30,933.8 | 31,106.2 | 64.1 | 1.022x | 1.022x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 31,117.9 | 31,107.7 | 31,272.1 | 63.4 | 1.027x | 1.027x |

### `floor` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,689.1 | 17,679.6 | 17,711.6 | 11.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,700.6 | 17,663.6 | 17,733.8 | 25.4 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,722.6 | 17,687.5 | 17,755.5 | 22.2 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,737.8 | 17,670.2 | 17,774.1 | 35.0 | 1.003x | 1.003x |

### `orig` / `s-000` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.6 | 33.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.6 | 32.9 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.7 | 32.5 | 32.7 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.7 | 32.7 | 32.9 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-000` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.4 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.4 | 63.6 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.6 | 63.3 | 63.7 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.6 | 63.4 | 64.1 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-001` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 40.3 | 40.3 | 40.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 40.3 | 40.1 | 40.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.3 | 40.5 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 40.4 | 40.4 | 40.4 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-001` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.8 | 82.8 | 82.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 82.9 | 82.4 | 83.1 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 82.9 | 82.8 | 96.3 | 5.4 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 82.9 | 82.8 | 83.0 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-002` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.3 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.4 | 18.3 | 18.4 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.5 | 18.4 | 18.5 | 0.0 | 1.009x | 1.009x |

### `orig` / `s-002` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.8 | 29.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.7 | 34.9 | 2.4 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.0 | 28.9 | 30.0 | 0.4 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.8 | 29.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-003` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.6 | 43.4 | 43.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.7 | 43.5 | 44.1 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.8 | 43.5 | 43.9 | 0.2 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.8 | 43.6 | 43.8 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-003` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 89.8 | 89.6 | 90.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 89.9 | 89.8 | 90.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 90.0 | 89.7 | 90.1 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 90.0 | 89.6 | 90.5 | 0.3 | 1.002x | 1.002x |

### `orig` / `s-004` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 61.4 | 60.9 | 62.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 61.4 | 61.3 | 61.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.4 | 61.1 | 61.5 | 0.2 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 61.5 | 61.2 | 61.7 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-004` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.0 | 124.9 | 125.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 125.1 | 124.7 | 125.1 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 125.1 | 125.0 | 125.4 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 125.1 | 124.8 | 125.3 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-005` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.2 | 18.4 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 18.3 | 18.1 | 18.9 | 0.3 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 18.4 | 18.3 | 18.5 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-005` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.7 | 29.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.0 | 28.9 | 29.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.8 | 29.5 | 0.3 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.0 | 28.7 | 29.4 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-006` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.1 | 31.1 | 31.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.1 | 31.1 | 31.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 31.2 | 31.0 | 31.2 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 31.2 | 31.1 | 31.2 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-006` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.2 | 59.7 | 60.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 60.2 | 59.9 | 60.8 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 60.2 | 60.1 | 60.2 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 60.3 | 60.2 | 60.3 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-007` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.7 | 46.6 | 46.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 46.8 | 46.7 | 47.2 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.8 | 46.7 | 46.9 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 46.9 | 46.8 | 47.1 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-007` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.3 | 95.3 | 96.1 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 95.3 | 95.0 | 96.6 | 0.6 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 95.6 | 95.3 | 96.2 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 96.0 | 95.2 | 97.4 | 0.8 | 1.007x | 1.007x |

### `orig` / `s-008` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 36.9 | 36.8 | 37.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 37.0 | 36.9 | 37.1 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 37.0 | 37.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 37.0 | 37.0 | 37.2 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-008` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 74.3 | 74.1 | 74.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.4 | 74.3 | 75.1 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 74.5 | 74.4 | 75.0 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 74.5 | 74.3 | 74.9 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-009` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-009` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.4 | 56.3 | 56.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.4 | 56.4 | 57.1 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.4 | 56.9 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 56.6 | 56.5 | 56.8 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-010` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.9 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-010` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.0 | 56.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.4 | 56.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.5 | 64.9 | 3.3 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.6 | 56.4 | 56.7 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-011` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.3 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.2 | 0.1 | 1.009x | 1.009x |

### `orig` / `s-011` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.8 | 37.6 | 37.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 37.8 | 37.8 | 38.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 37.8 | 37.8 | 37.9 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 38.0 | 37.8 | 38.2 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-012` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.6 | 0.0 | 1.001x | 1.001x |

### `orig` / `s-012` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.6 | 70.5 | 70.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.7 | 70.6 | 70.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.3 | 71.0 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 70.9 | 70.7 | 70.9 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-013` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.8 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.6 | 35.3 | 35.6 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.8 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-013` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.5 | 70.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.7 | 71.2 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.8 | 71.1 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 70.9 | 70.8 | 71.0 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-014` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.8 | 29.6 | 29.8 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.8 | 29.7 | 29.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.8 | 29.6 | 29.9 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-014` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.6 | 56.5 | 56.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.7 | 56.4 | 63.0 | 2.5 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 56.7 | 56.5 | 56.9 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 57.0 | 56.5 | 58.2 | 0.6 | 1.006x | 1.006x |

### `orig` / `s-015` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.9 | 33.9 | 34.1 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 34.0 | 34.1 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-015` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.9 | 68.1 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.1 | 66.9 | 67.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.3 | 67.0 | 68.4 | 0.5 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.5 | 66.9 | 75.4 | 3.2 | 1.008x | 1.008x |

### `orig` / `s-016` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 9.7 | 9.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.8 | 9.7 | 10.5 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 9.8 | 11.1 | 0.5 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.8 | 9.8 | 10.8 | 0.4 | 1.004x | 1.004x |

### `orig` / `s-016` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.8 | 29.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.1 | 28.9 | 29.2 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 28.9 | 29.3 | 0.2 | 1.011x | 1.011x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 28.8 | 29.7 | 0.3 | 1.012x | 1.012x |

### `orig` / `s-017` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.4 | 35.2 | 35.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.4 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.5 | 35.7 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.7 | 35.5 | 36.2 | 0.3 | 1.007x | 1.007x |

### `orig` / `s-017` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.7 | 70.6 | 70.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 71.0 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.8 | 71.0 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.6 | 71.0 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-018` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.8 | 33.8 | 33.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.0 | 33.8 | 34.7 | 0.3 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-018` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.9 | 67.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.9 | 67.7 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 67.0 | 67.4 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.1 | 67.1 | 68.5 | 0.6 | 1.001x | 1.001x |

### `orig` / `s-019` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.2 | 10.1 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 1.012x | 1.012x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.4 | 10.3 | 10.4 | 0.0 | 1.013x | 1.013x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.5 | 10.3 | 11.5 | 0.4 | 1.023x | 1.023x |

### `orig` / `s-019` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.7 | 30.5 | 31.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.8 | 30.6 | 30.9 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.8 | 30.7 | 31.2 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.8 | 30.7 | 30.9 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-020` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.6 | 38.3 | 38.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 38.7 | 38.6 | 38.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.7 | 38.6 | 38.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 38.8 | 38.7 | 38.9 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-020` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 77.6 | 77.5 | 77.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 77.7 | 77.6 | 77.8 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.7 | 77.7 | 77.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 77.8 | 77.6 | 77.9 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-021` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.7 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.8 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-021` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.5 | 56.5 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.4 | 56.9 | 0.2 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 56.7 | 56.5 | 57.2 | 0.3 | 1.003x | 1.003x |

### `orig` / `s-022` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.8 | 41.7 | 41.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.9 | 42.2 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.7 | 42.1 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 42.0 | 41.9 | 42.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-022` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 84.8 | 84.4 | 85.0 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 84.8 | 84.8 | 84.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.8 | 85.0 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 85.0 | 84.8 | 85.2 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-023` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.4 | 35.4 | 35.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.2 | 35.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.3 | 35.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.7 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-023` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 72.1 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.8 | 70.4 | 71.1 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.6 | 71.1 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 71.1 | 70.8 | 72.1 | 0.5 | 1.005x | 1.005x |

### `orig` / `s-024` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.7 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 29.6 | 29.6 | 29.8 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.6 | 29.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 29.7 | 29.7 | 29.9 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-024` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 56.5 | 56.4 | 56.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.5 | 56.3 | 56.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 56.6 | 56.5 | 56.7 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 56.7 | 56.5 | 57.0 | 0.2 | 1.002x | 1.002x |

### `orig` / `s-025` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.5 | 35.4 | 35.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 35.6 | 35.4 | 35.6 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-025` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.6 | 70.5 | 70.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.5 | 71.0 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 70.8 | 70.7 | 70.9 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 70.9 | 70.5 | 70.9 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-026` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 41.9 | 41.9 | 42.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 42.0 | 41.8 | 42.1 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 42.0 | 41.6 | 42.2 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.8 | 42.1 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-026` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 84.8 | 84.8 | 84.9 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 85.0 | 84.9 | 85.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.8 | 86.0 | 0.5 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.1 | 84.9 | 85.2 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-027` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.8 | 41.8 | 42.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 41.9 | 41.8 | 42.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.8 | 42.1 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 42.0 | 41.8 | 42.2 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-027` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 84.8 | 84.7 | 85.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.8 | 85.6 | 0.3 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 85.0 | 84.9 | 85.5 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 85.1 | 84.8 | 85.1 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-028` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.9 | 0.3 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.009x | 1.009x |

### `orig` / `s-028` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.0 | 24.9 | 25.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 25.0 | 25.0 | 25.7 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.0 | 25.0 | 25.1 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.2 | 25.0 | 25.3 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-029` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.5 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.008x | 1.008x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.0 | 1.009x | 1.009x |

### `orig` / `s-029` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 48.7 | 48.7 | 49.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 48.8 | 48.7 | 49.3 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 49.0 | 48.7 | 49.2 | 0.2 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 49.0 | 48.6 | 49.2 | 0.3 | 1.006x | 1.006x |

### `orig` / `s-030` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-030` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 25.1 | 25.1 | 25.7 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.1 | 25.0 | 25.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.1 | 25.1 | 25.4 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 25.4 | 25.1 | 25.6 | 0.2 | 1.009x | 1.009x |

### `orig` / `s-031` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |

### `orig` / `s-031` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.2 | 33.0 | 33.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 33.2 | 33.1 | 33.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 33.3 | 33.2 | 34.1 | 0.3 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 33.3 | 33.1 | 33.9 | 0.3 | 1.004x | 1.004x |

### `orig` / `s-032` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.3 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-032` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.2 | 29.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.3 | 29.3 | 29.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.4 | 29.1 | 29.7 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.5 | 29.3 | 29.7 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-033` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.1 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.006x | 1.006x |

### `orig` / `s-033` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.0 | 29.0 | 29.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 29.0 | 30.1 | 0.4 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.2 | 29.1 | 29.4 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.2 | 29.0 | 29.6 | 0.2 | 1.008x | 1.008x |

### `orig` / `s-034` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.1 | 20.1 | 20.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 20.2 | 20.1 | 20.3 | 0.0 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.2 | 20.2 | 20.3 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 20.3 | 20.2 | 20.4 | 0.0 | 1.009x | 1.009x |

### `orig` / `s-034` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.4 | 21.4 | 22.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.4 | 21.4 | 21.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 21.4 | 21.4 | 21.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.6 | 21.4 | 21.7 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-035` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 22.9 | 23.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.3 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.2 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-035` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.0 | 27.9 | 28.7 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.1 | 27.8 | 28.6 | 0.3 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.3 | 27.9 | 28.7 | 0.3 | 1.010x | 1.010x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.3 | 28.2 | 28.4 | 0.1 | 1.011x | 1.011x |

### `orig` / `s-036` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.1 | 11.9 | 12.1 | 0.1 | 1.011x | 1.011x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.1 | 12.2 | 0.0 | 1.015x | 1.015x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.2 | 12.0 | 12.2 | 0.1 | 1.016x | 1.016x |

### `orig` / `s-036` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.4 | 29.3 | 29.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.5 | 29.3 | 29.6 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.4 | 29.9 | 0.2 | 1.007x | 1.007x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.0 | 29.6 | 30.1 | 0.2 | 1.020x | 1.020x |

### `orig` / `s-037` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.5 | 14.4 | 14.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.5 | 14.5 | 14.7 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 1.010x | 1.010x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.5 | 14.8 | 0.1 | 1.012x | 1.012x |

### `orig` / `s-037` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.6 | 23.4 | 24.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.6 | 23.5 | 23.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.8 | 23.5 | 24.3 | 0.3 | 1.009x | 1.009x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 24.2 | 23.9 | 24.4 | 0.2 | 1.026x | 1.026x |

### `orig` / `s-038` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.3 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.1 | 23.1 | 23.2 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-038` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.4 | 29.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.6 | 29.3 | 29.8 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.0 | 29.2 | 30.1 | 0.4 | 1.013x | 1.013x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.1 | 30.0 | 30.5 | 0.2 | 1.019x | 1.019x |

### `orig` / `s-039` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.0 | 10.3 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.3 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.1 | 10.4 | 0.1 | 1.008x | 1.008x |

### `orig` / `s-039` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.4 | 63.3 | 64.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.5 | 63.3 | 63.6 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.5 | 63.3 | 64.0 | 0.3 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.7 | 63.3 | 65.3 | 0.7 | 1.003x | 1.003x |

### `orig` / `s-040` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 26.1 | 26.1 | 26.2 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 26.2 | 26.0 | 26.5 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-040` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 7.5 | 7.4 | 9.3 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.6 | 7.4 | 8.6 | 0.5 | 1.139x | 1.139x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.7 | 7.4 | 8.8 | 0.5 | 1.147x | 1.147x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.7 | 8.6 | 9.5 | 0.3 | 1.151x | 1.151x |

### `orig` / `s-041` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.8 | 10.0 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.4 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.3 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.9 | 11.8 | 1.1 | 1.099x | 1.099x |

### `orig` / `s-041` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.6 | 21.5 | 22.1 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.9 | 21.7 | 22.1 | 0.1 | 1.013x | 1.013x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.9 | 21.8 | 22.2 | 0.1 | 1.016x | 1.016x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 22.3 | 22.1 | 22.8 | 0.2 | 1.033x | 1.033x |

### `orig` / `s-042` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.4 | 12.2 | 12.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.5 | 12.4 | 12.5 | 0.0 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.6 | 12.0 | 12.6 | 0.2 | 1.014x | 1.014x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.6 | 12.2 | 12.7 | 0.2 | 1.015x | 1.015x |

### `orig` / `s-042` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 14.3 | 14.1 | 15.2 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.3 | 14.2 | 15.1 | 0.4 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 14.4 | 14.1 | 14.8 | 0.2 | 1.011x | 1.011x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 14.5 | 14.3 | 15.5 | 0.5 | 1.013x | 1.013x |

### `orig` / `s-043` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.8 | 12.0 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.7 | 12.9 | 0.4 | 1.004x | 1.004x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.012x | 1.012x |

### `orig` / `s-043` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.1 | 75.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 75.3 | 75.2 | 75.9 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.4 | 75.3 | 75.7 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 75.6 | 75.3 | 75.8 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-044` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.8 | 10.3 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.0 | 0.5 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.0 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.4 | 1.008x | 1.008x |

### `orig` / `s-044` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 65.3 | 65.2 | 65.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.3 | 65.2 | 65.6 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 65.3 | 65.1 | 66.0 | 0.3 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 65.4 | 65.3 | 65.6 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-045` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 12.0 | 12.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 12.0 | 12.1 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 11.8 | 12.8 | 0.3 | 1.010x | 1.010x |

### `orig` / `s-045` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.4 | 28.4 | 28.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 28.5 | 28.3 | 28.8 | 0.2 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 28.6 | 28.5 | 28.8 | 0.1 | 1.007x | 1.007x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 28.9 | 28.4 | 29.2 | 0.3 | 1.015x | 1.015x |

### `orig` / `s-046` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.8 | 21.7 | 21.9 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 21.9 | 21.7 | 21.9 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 21.9 | 21.8 | 21.9 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-046` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.6 | 21.5 | 21.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 21.7 | 21.5 | 21.8 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 21.8 | 21.5 | 22.0 | 0.2 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 21.8 | 21.4 | 22.2 | 0.3 | 1.008x | 1.008x |

### `orig` / `s-047` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.1 | 23.0 | 23.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.4 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 23.2 | 23.1 | 23.3 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-047` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.1 | 22.9 | 23.4 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.2 | 22.9 | 23.7 | 0.2 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.4 | 22.9 | 23.9 | 0.3 | 1.011x | 1.011x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.4 | 23.0 | 23.6 | 0.2 | 1.014x | 1.014x |

### `orig` / `s-048` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.3 | 13.4 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-048` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 15.3 | 15.3 | 15.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 15.4 | 15.4 | 16.0 | 0.2 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.1 | 15.6 | 0.2 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 15.4 | 15.2 | 15.8 | 0.2 | 1.004x | 1.004x |

### `orig` / `s-049` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.8 | 10.7 | 11.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.9 | 10.7 | 11.3 | 0.3 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.0 | 10.5 | 11.3 | 0.3 | 1.011x | 1.011x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.1 | 10.8 | 11.2 | 0.1 | 1.020x | 1.020x |

### `orig` / `s-049` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 72.7 | 72.5 | 73.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.9 | 72.7 | 73.0 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 73.1 | 72.7 | 73.2 | 0.2 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.1 | 72.8 | 73.2 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-050` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.6 | 14.5 | 14.7 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.8 | 0.1 | 1.007x | 1.007x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 14.7 | 14.6 | 14.7 | 0.0 | 1.008x | 1.008x |

### `orig` / `s-050` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 57.9 | 57.9 | 67.3 | 3.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 57.9 | 57.8 | 58.2 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 58.0 | 57.9 | 58.1 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 58.6 | 58.0 | 59.2 | 0.5 | 1.013x | 1.013x |

### `orig` / `s-051` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.9 | 10.6 | 11.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.1 | 10.9 | 11.3 | 0.2 | 1.021x | 1.021x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.2 | 10.6 | 11.2 | 0.3 | 1.030x | 1.030x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 11.3 | 11.0 | 11.3 | 0.1 | 1.034x | 1.034x |

### `orig` / `s-051` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 72.9 | 72.8 | 73.1 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 72.9 | 72.8 | 73.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 73.2 | 72.8 | 73.8 | 0.4 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 73.3 | 72.9 | 73.4 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-052` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-052` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 22.6 | 22.4 | 23.1 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.6 | 22.6 | 22.9 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 22.8 | 22.5 | 22.8 | 0.1 | 1.007x | 1.007x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.0 | 22.7 | 23.0 | 0.1 | 1.015x | 1.015x |

### `orig` / `s-053` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.8 | 0.2 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-053` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.1 | 17.0 | 17.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.2 | 17.0 | 17.3 | 0.1 | 1.006x | 1.006x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.1 | 17.3 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.2 | 17.3 | 0.1 | 1.011x | 1.011x |

### `orig` / `s-054` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.1 | 13.3 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-054` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 16.9 | 16.8 | 17.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.8 | 17.2 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.2 | 17.0 | 17.4 | 0.1 | 1.018x | 1.018x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17.2 | 17.1 | 17.3 | 0.1 | 1.019x | 1.019x |

### `orig` / `s-055` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.5 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.0 | 1.007x | 1.007x |

### `orig` / `s-055` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 16.9 | 16.8 | 17.2 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17.0 | 16.7 | 17.2 | 0.2 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17.0 | 16.8 | 17.2 | 0.2 | 1.010x | 1.010x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17.4 | 17.0 | 17.7 | 0.2 | 1.035x | 1.035x |

### `orig` / `s-056` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.3 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-056` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 19.2 | 19.1 | 19.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.3 | 19.0 | 19.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 19.3 | 19.2 | 19.3 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 19.3 | 19.0 | 19.9 | 0.3 | 1.005x | 1.005x |

### `orig` / `s-057` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,062.4 | 19,060.0 | 19,100.1 | 15.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,067.5 | 19,063.1 | 19,073.0 | 3.7 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,071.2 | 19,069.1 | 19,077.8 | 3.4 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,072.7 | 19,070.7 | 19,076.1 | 2.3 | 1.001x | 1.001x |

### `orig` / `s-058` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,459.5 | 7,459.3 | 7,459.8 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,462.5 | 7,459.3 | 7,519.6 | 23.2 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,462.8 | 7,461.8 | 7,464.7 | 1.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,464.0 | 7,462.2 | 7,465.5 | 1.3 | 1.001x | 1.001x |

### `orig` / `s-059` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,546.5 | 9,546.2 | 9,551.0 | 2.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9,549.0 | 9,547.6 | 9,553.4 | 2.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,551.0 | 9,549.5 | 9,552.8 | 1.2 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9,553.0 | 9,550.2 | 9,553.7 | 1.4 | 1.001x | 1.001x |

### `orig` / `s-060` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,036.3 | 19,035.4 | 19,036.9 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19,039.2 | 19,038.4 | 19,044.5 | 2.8 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,044.0 | 19,041.3 | 19,049.8 | 3.3 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19,045.1 | 19,043.3 | 19,048.9 | 2.0 | 1.000x | 1.000x |

### `orig` / `s-061` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,737.6 | 3,737.2 | 3,738.4 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 3,738.3 | 3,736.5 | 3,738.9 | 0.9 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,738.4 | 3,736.9 | 3,739.3 | 0.9 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 3,738.9 | 3,736.5 | 3,739.7 | 1.1 | 1.000x | 1.000x |

### `orig` / `s-062` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.1 | 16.4 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.2 | 16.3 | 0.0 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.3 | 16.1 | 16.4 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-063` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,782.2 | 4,780.7 | 4,783.6 | 1.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 4,784.9 | 4,783.6 | 4,786.0 | 0.8 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,786.0 | 4,783.7 | 4,786.8 | 1.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 4,786.4 | 4,785.0 | 4,787.5 | 0.9 | 1.001x | 1.001x |

### `orig` / `s-064` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,643.7 | 7,642.6 | 7,645.3 | 0.9 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,646.3 | 7,645.6 | 7,647.4 | 0.6 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 7,646.5 | 7,644.1 | 7,776.4 | 52.1 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 7,646.8 | 7,645.7 | 7,648.6 | 1.1 | 1.000x | 1.000x |

### `orig` / `s-065` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 8.9 | 8.9 | 9.8 | 0.4 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.5 | 0.6 | 1.006x | 1.006x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.0 | 8.9 | 9.8 | 0.3 | 1.018x | 1.018x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.9 | 10.1 | 0.4 | 1.098x | 1.098x |

### `orig` / `s-065` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.0 | 23.8 | 25.0 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 24.1 | 23.8 | 24.6 | 0.3 | 1.005x | 1.005x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 24.1 | 23.9 | 24.6 | 0.3 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 24.6 | 24.0 | 26.4 | 0.9 | 1.024x | 1.024x |

### `orig` / `s-066` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 33.9 | 33.8 | 34.3 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.0 | 33.9 | 34.1 | 0.1 | 1.004x | 1.004x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 34.1 | 34.0 | 34.2 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 34.2 | 33.8 | 34.2 | 0.2 | 1.009x | 1.009x |

### `orig` / `s-066` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 66.9 | 67.0 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.9 | 67.4 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 67.0 | 66.8 | 71.6 | 1.8 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 67.0 | 67.0 | 67.2 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-067` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.4 | 32.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.6 | 32.7 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-067` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-068` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.8 | 16.7 | 16.8 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.8 | 16.6 | 17.0 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.9 | 16.7 | 16.9 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.9 | 16.8 | 17.1 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-068` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.9 | 25.9 | 26.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 25.9 | 25.8 | 26.5 | 0.3 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 26.0 | 25.8 | 26.2 | 0.1 | 1.004x | 1.004x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 26.0 | 25.9 | 26.8 | 0.4 | 1.005x | 1.005x |

### `orig` / `s-069` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 11.9 | 11.9 | 13.6 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.0 | 11.9 | 12.1 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 12.0 | 11.8 | 12.2 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 12.1 | 12.0 | 12.2 | 0.1 | 1.014x | 1.014x |

### `orig` / `s-069` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.1 | 30.0 | 30.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.2 | 30.0 | 30.6 | 0.2 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 30.3 | 30.1 | 30.6 | 0.2 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 30.4 | 30.4 | 30.8 | 0.1 | 1.012x | 1.012x |

### `orig` / `s-070` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.2 | 28.2 | 28.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 28.2 | 28.1 | 28.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 28.3 | 28.1 | 28.3 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 28.3 | 28.3 | 28.5 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-070` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 52.8 | 52.7 | 53.9 | 0.5 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.9 | 52.7 | 53.6 | 0.3 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 52.9 | 52.8 | 55.7 | 1.2 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 53.6 | 52.8 | 54.4 | 0.6 | 1.015x | 1.015x |

### `orig` / `s-071` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 56.2 | 56.1 | 56.5 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.3 | 56.1 | 56.5 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 56.5 | 56.2 | 56.5 | 0.1 | 1.005x | 1.005x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 56.5 | 56.1 | 56.5 | 0.2 | 1.005x | 1.005x |

### `orig` / `s-071` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.4 | 114.1 | 114.6 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 114.5 | 114.2 | 115.0 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 114.6 | 114.4 | 115.5 | 0.4 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 114.8 | 114.4 | 115.1 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-072` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.2 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.5 | 0.2 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 43.1 | 43.0 | 43.1 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 43.2 | 42.9 | 43.5 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-072` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 93.8 | 93.8 | 94.6 | 0.3 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 93.9 | 93.7 | 94.0 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 94.0 | 93.7 | 94.3 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 94.0 | 93.8 | 94.2 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-073` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.1 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.3 | 13.2 | 13.4 | 0.1 | 1.007x | 1.007x |

### `orig` / `s-073` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 23.2 | 23.1 | 23.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.3 | 23.2 | 23.8 | 0.2 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 23.3 | 23.2 | 23.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 23.3 | 23.1 | 23.7 | 0.2 | 1.003x | 1.003x |

### `orig` / `s-074` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 13.2 | 13.2 | 13.3 | 0.0 | 1.004x | 1.004x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 13.3 | 13.1 | 13.4 | 0.1 | 1.004x | 1.004x |

### `orig` / `s-074` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.7 | 29.8 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.8 | 29.8 | 30.0 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.9 | 29.8 | 30.2 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 30.2 | 29.8 | 30.3 | 0.2 | 1.014x | 1.014x |

### `orig` / `s-075` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.6 | 32.7 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-075` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.1 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.3 | 0.0 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 63.5 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-076` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.3 | 32.9 | 0.2 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.6 | 32.6 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.8 | 0.1 | 1.002x | 1.002x |

### `orig` / `s-076` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.1 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.5 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.3 | 63.4 | 0.0 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.2 | 64.8 | 0.6 | 1.001x | 1.001x |

### `orig` / `s-077` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.5 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.002x | 1.002x |

### `orig` / `s-077` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 64.8 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.1 | 63.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 66.9 | 1.4 | 1.001x | 1.001x |

### `orig` / `s-078` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.5 | 32.5 | 32.6 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.003x | 1.003x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.7 | 32.5 | 32.8 | 0.1 | 1.005x | 1.005x |

### `orig` / `s-078` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.2 | 63.2 | 63.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.4 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.3 | 63.5 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.4 | 63.3 | 72.3 | 3.6 | 1.003x | 1.003x |

### `orig` / `s-079` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.6 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 32.6 | 32.4 | 32.6 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 32.6 | 32.5 | 32.7 | 0.1 | 1.001x | 1.001x |

### `orig` / `s-079` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 71.6 | 3.4 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.3 | 0.0 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 63.3 | 63.2 | 63.6 | 0.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 63.3 | 63.2 | 63.6 | 0.2 | 1.001x | 1.001x |

### `orig` / `s-080` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.1 | 16.0 | 16.2 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.1 | 16.1 | 16.2 | 0.1 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 16.2 | 16.0 | 16.2 | 0.1 | 1.003x | 1.003x |

### `orig` / `s-080` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 29.3 | 29.1 | 29.5 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 29.5 | 29.2 | 29.6 | 0.2 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 29.3 | 29.7 | 0.1 | 1.006x | 1.006x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 29.5 | 29.2 | 29.6 | 0.1 | 1.006x | 1.006x |

### `orig` / `s-081` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.0 | 9.5 | 11.4 | 0.7 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.1 | 9.9 | 10.2 | 0.1 | 1.002x | 1.002x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.1 | 9.6 | 10.1 | 0.2 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.0 | 11.5 | 0.6 | 1.028x | 1.028x |

### `orig` / `s-081` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 4.1 | 4.1 | 4.1 | 0.0 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.2 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 4.1 | 4.1 | 4.2 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-082` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 8.9 | 8.9 | 10.9 | 0.8 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 9.1 | 8.9 | 10.4 | 0.6 | 1.017x | 1.017x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.9 | 10.9 | 0.8 | 1.089x | 1.089x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 9.7 | 8.9 | 11.2 | 0.9 | 1.091x | 1.091x |

### `orig` / `s-082` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.3 | 8.3 | 8.4 | 0.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.4 | 8.3 | 8.9 | 0.2 | 1.008x | 1.008x |
| 3 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.4 | 8.3 | 8.5 | 0.1 | 1.012x | 1.012x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 9.0 | 8.3 | 9.5 | 0.4 | 1.085x | 1.085x |

### `orig` / `s-083` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.5 | 0.1 | 1.005x | 1.005x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 10.3 | 10.2 | 10.4 | 0.1 | 1.009x | 1.009x |
| 4 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 10.4 | 10.3 | 11.9 | 0.7 | 1.010x | 1.010x |

### `orig` / `s-083` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.0 | 8.0 | 8.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.6 | 0.3 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.0 | 8.0 | 8.1 | 0.0 | 1.003x | 1.003x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.3 | 8.0 | 8.3 | 0.1 | 1.038x | 1.038x |

### `orig` / `s-084` / `match-compliance` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- matches: n/s (the record carries no expected-answer field for its common `matched-as-expected` rows -- KB-2, docs/dev/known_issues.md)

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.3 | 0.1 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `whole-subject` | separate artifact | 19.2 | 19.0 | 19.3 | 0.1 | 1.000x | 1.000x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.2 | 19.1 | 19.4 | 0.1 | 1.000x | 1.000x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `whole-subject` | separate artifact | 19.3 | 19.2 | 19.3 | 0.0 | 1.003x | 1.003x |

### `orig` / `s-084` / `short-subject-search` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-nocaps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 7.8 | 7.4 | 8.7 | 0.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 8.2 | 7.4 | 8.7 | 0.6 | 1.060x | 1.060x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 8.6 | 7.4 | 8.7 | 0.5 | 1.103x | 1.103x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 8.7 | 8.6 | 9.6 | 0.4 | 1.123x | 1.123x |

### `orig` / `t-a-valid-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,781,204.7 | 3,780,041.5 | 3,783,702.8 | 1,212.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 3,782,965.9 | 3,781,957.9 | 3,783,216.9 | 457.4 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,784,037.5 | 3,782,834.1 | 3,784,901.9 | 736.2 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,786,407.2 | 3,784,205.5 | 3,791,572.1 | 2,617.2 | 1.001x | 1.001x |

### `orig` / `t-b-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,685.7 | 17,671.1 | 17,725.5 | 20.7 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,715.8 | 17,683.5 | 17,734.7 | 18.7 | 1.002x | 1.002x |
| 3 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,780.8 | 17,764.4 | 17,848.2 | 30.0 | 1.005x | 1.005x |
| 4 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,793.3 | 17,765.0 | 18,016.4 | 93.0 | 1.006x | 1.006x |

### `orig` / `t-c-long-atom-run` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_b8337c33_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,680.9 | 17,661.2 | 17,689.1 | 10.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,682.7 | 17,651.6 | 17,710.7 | 18.8 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,709.5 | 17,695.1 | 17,732.2 | 13.4 | 1.002x | 1.002x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,746.6 | 17,728.5 | 17,866.2 | 50.4 | 1.004x | 1.004x |

### `orig` / `t-d-prose-sparse-addrs` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 3,218,037.1 | 3,212,711.1 | 3,228,166.5 | 5,132.6 | 1.000x | 1.000x |
| 2 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,222,623.3 | 3,218,310.5 | 3,225,473.6 | 2,461.6 | 1.001x | 1.001x |
| 3 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 3,223,524.5 | 3,221,334.7 | 3,224,549.8 | 1,365.9 | 1.002x | 1.002x |
| 4 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 3,224,086.7 | 3,217,923.5 | 3,243,318.6 | 8,889.1 | 1.002x | 1.002x |

### `orig` / `t-e-prose-no-at` / `large-subject-throughput` (email-specimen@0.2) — baseline: libpcre2 engine_mode=interp

- baseline: pcrec_7388f1c0_auto-caps-simdna (row-best fallback -- interp absent from this group)
| rank | testee | status | capture class | form | fact | median ns/call | min | max | stddev | vs baseline | vs best |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `pcrec_7388f1c0_auto-caps-simdna` | measured | yes | `plain` | same program | 17,689.6 | 17,668.0 | 17,773.1 | 37.0 | 1.000x | 1.000x |
| 2 | `pcrec_b8337c33_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,693.9 | 17,653.4 | 17,746.8 | 31.6 | 1.000x | 1.000x |
| 3 | `pcrec_b8337c33_auto-caps-simdna` | measured | yes | `plain` | same program | 17,704.7 | 17,681.3 | 17,731.8 | 17.1 | 1.001x | 1.001x |
| 4 | `pcrec_7388f1c0_auto-nocaps-simdna` | measured | no | `plain` | same program | 17,739.4 | 17,684.7 | 17,863.9 | 62.9 | 1.003x | 1.003x |

## Standing cross-class query (inbox I-101; Frank's own anomaly check -- a QUERY, never a ranking; every hit below is a finding on pcrec's side by definition)

**597 hit(s)** -- each is a finding on pcrec's side by definition (I-101):

| pattern | regime | pcrec auto-nocaps testee | auto-nocaps ns/call | competitor testee | competitor ns/call | ratio (competitor / auto-nocaps) | clears IQR / null band |
|---|---|---|---|---|---|---|---|
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.988x | no verdict: gap 1.16%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.0 | `pcrec_b8337c33_auto-caps-simdna` | 11.9 | 0.992x | no verdict: gap 0.83%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 38.0 | `pcrec_7388f1c0_auto-caps-simdna` | 37.9 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.8 | `pcrec_7388f1c0_auto-caps-simdna` | 9.5 | 0.967x | no verdict: gap 3.31%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 9.8 | `pcrec_b8337c33_auto-caps-simdna` | 9.5 | 0.967x | no verdict: gap 3.30%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.1 | `pcrec_b8337c33_auto-caps-simdna` | 28.9 | 0.994x | no verdict: gap 0.57%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.4 | `pcrec_7388f1c0_auto-caps-simdna` | 9.9 | 0.953x | no verdict: gap 4.66%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.4 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.951x | no verdict: gap 4.87%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 30.9 | `pcrec_b8337c33_auto-caps-simdna` | 30.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.0 | `pcrec_7388f1c0_auto-caps-simdna` | 25.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 48.9 | `pcrec_7388f1c0_auto-caps-simdna` | 48.8 | 0.997x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 48.9 | `pcrec_b8337c33_auto-caps-simdna` | 48.7 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.2 | `pcrec_7388f1c0_auto-caps-simdna` | 25.1 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 25.2 | `pcrec_b8337c33_auto-caps-simdna` | 25.2 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.75%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 33.3 | `pcrec_b8337c33_auto-caps-simdna` | 33.2 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.1 | `pcrec_7388f1c0_auto-caps-simdna` | 16.1 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.2 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.3 | `pcrec_7388f1c0_auto-caps-simdna` | 29.3 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.4 | `pcrec_b8337c33_auto-caps-simdna` | 29.2 | 0.993x | no verdict: gap 0.68%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.1 | 0.992x | no verdict: gap 0.83%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.4 | `pcrec_b8337c33_auto-caps-simdna` | 29.2 | 0.992x | no verdict: gap 0.80%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 20.3 | `pcrec_7388f1c0_auto-caps-simdna` | 20.3 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 20.4 | `pcrec_b8337c33_auto-caps-simdna` | 20.3 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.5 | `pcrec_7388f1c0_auto-caps-simdna` | 21.4 | 0.995x | no verdict: gap 0.50%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 21.6 | `pcrec_b8337c33_auto-caps-simdna` | 21.5 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.2 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.997x | no verdict: gap 0.30%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.2 | `pcrec_b8337c33_auto-caps-simdna` | 23.1 | 0.995x | no verdict: gap 0.45%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 28.4 | `pcrec_b8337c33_auto-caps-simdna` | 28.0 | 0.986x | no verdict: gap 1.41%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.977x | no verdict: gap 2.30%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 11.8 | 0.977x | no verdict: gap 2.33%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.8 | `pcrec_7388f1c0_auto-caps-simdna` | 29.7 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 30.1 | `pcrec_b8337c33_auto-caps-simdna` | 29.8 | 0.990x | no verdict: gap 0.95%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 14.7 | `pcrec_b8337c33_auto-caps-simdna` | 14.6 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.2 | `pcrec_b8337c33_auto-caps-simdna` | 23.1 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.9 | `pcrec_b8337c33_auto-caps-simdna` | 29.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.4 | `pcrec_7388f1c0_auto-caps-simdna` | 9.8 | 0.950x | no verdict: gap 5.03%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.4 | `pcrec_b8337c33_auto-caps-simdna` | 9.9 | 0.958x | no verdict: gap 4.23%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 26.2 | `pcrec_7388f1c0_auto-caps-simdna` | 26.2 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7.4 | `pcrec_7388f1c0_auto-caps-simdna` | 7.4 | 0.995x | no verdict: gap 0.54%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 7.6 | `pcrec_b8337c33_auto-caps-simdna` | 7.4 | 0.969x | no verdict: gap 3.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 22.1 | `pcrec_7388f1c0_auto-caps-simdna` | 21.7 | 0.983x | no verdict: gap 1.71%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 22.3 | `pcrec_b8337c33_auto-caps-simdna` | 22.1 | 0.995x | no verdict: gap 0.48%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.6 | `pcrec_7388f1c0_auto-caps-simdna` | 12.2 | 0.962x | no verdict: gap 3.78%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.5 | `pcrec_b8337c33_auto-caps-simdna` | 12.3 | 0.985x | no verdict: gap 1.48%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.0 | `pcrec_7388f1c0_auto-caps-simdna` | 11.8 | 0.979x | no verdict: gap 2.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 11.8 | 0.979x | no verdict: gap 2.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.977x | no verdict: gap 2.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 11.9 | 0.988x | no verdict: gap 1.23%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 28.6 | `pcrec_7388f1c0_auto-caps-simdna` | 28.5 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.8 | `pcrec_7388f1c0_auto-caps-simdna` | 21.5 | 0.983x | no verdict: gap 1.68%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 21.7 | `pcrec_b8337c33_auto-caps-simdna` | 21.5 | 0.995x | no verdict: gap 0.52%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.1 | `pcrec_b8337c33_auto-caps-simdna` | 23.0 | 0.994x | no verdict: gap 0.62%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 15.4 | `pcrec_7388f1c0_auto-caps-simdna` | 15.0 | 0.979x | no verdict: gap 2.14%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 15.5 | `pcrec_b8337c33_auto-caps-simdna` | 15.0 | 0.970x | no verdict: gap 3.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.2 | `pcrec_7388f1c0_auto-caps-simdna` | 10.8 | 0.957x | no verdict: gap 4.35%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 11.2 | `pcrec_b8337c33_auto-caps-simdna` | 10.8 | 0.961x | no verdict: gap 3.87%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 14.7 | `pcrec_7388f1c0_auto-caps-simdna` | 14.6 | 0.997x | no verdict: gap 0.30%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 14.6 | `pcrec_b8337c33_auto-caps-simdna` | 14.6 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.0 | `pcrec_7388f1c0_auto-caps-simdna` | 10.7 | 0.972x | no verdict: gap 2.82%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 11.2 | `pcrec_b8337c33_auto-caps-simdna` | 10.9 | 0.977x | no verdict: gap 2.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.3 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.0 | `pcrec_7388f1c0_auto-caps-simdna` | 22.5 | 0.979x | no verdict: gap 2.09%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.3 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.76%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.4 | `pcrec_7388f1c0_auto-caps-simdna` | 16.9 | 0.973x | no verdict: gap 2.65%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 17.3 | `pcrec_b8337c33_auto-caps-simdna` | 17.0 | 0.981x | no verdict: gap 1.93%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.3 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 17.1 | `pcrec_b8337c33_auto-caps-simdna` | 16.9 | 0.990x | no verdict: gap 0.99%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.3 | 0.997x | no verdict: gap 0.30%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.8 | 0.976x | no verdict: gap 2.37%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 17.1 | `pcrec_b8337c33_auto-caps-simdna` | 16.8 | 0.980x | no verdict: gap 1.99%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.3 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.4 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.990x | no verdict: gap 1.02%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19.6 | `pcrec_7388f1c0_auto-caps-simdna` | 19.3 | 0.984x | no verdict: gap 1.62%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 19.3 | `pcrec_b8337c33_auto-caps-simdna` | 19.1 | 0.987x | no verdict: gap 1.31%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19,071.6 | `pcrec_7388f1c0_auto-caps-simdna` | 19,063.6 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19,072.8 | `pcrec_b8337c33_auto-caps-simdna` | 19,071.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,463.1 | `pcrec_7388f1c0_auto-caps-simdna` | 7,462.7 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 7,464.6 | `pcrec_b8337c33_auto-caps-simdna` | 7,464.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9,551.3 | `pcrec_7388f1c0_auto-caps-simdna` | 9,548.8 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19,048.6 | `pcrec_7388f1c0_auto-caps-simdna` | 19,036.3 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19,047.1 | `pcrec_b8337c33_auto-caps-simdna` | 19,045.2 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,739.3 | `pcrec_7388f1c0_auto-caps-simdna` | 3,739.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.2 | 0.996x | no verdict: gap 0.39%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.2 | `pcrec_b8337c33_auto-caps-simdna` | 16.2 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 4,787.5 | `pcrec_b8337c33_auto-caps-simdna` | 4,787.3 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,648.8 | `pcrec_7388f1c0_auto-caps-simdna` | 7,645.4 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.6 | 0.960x | no verdict: gap 3.97%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 24.7 | `pcrec_7388f1c0_auto-caps-simdna` | 24.5 | 0.991x | no verdict: gap 0.94%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 24.0 | `pcrec_b8337c33_auto-caps-simdna` | 23.9 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.2 | `pcrec_7388f1c0_auto-caps-simdna` | 11.8 | 0.969x | no verdict: gap 3.10%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 11.8 | 0.971x | no verdict: gap 2.89%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 30.4 | `pcrec_7388f1c0_auto-caps-simdna` | 30.3 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 30.3 | `pcrec_b8337c33_auto-caps-simdna` | 30.2 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 43.1 | `pcrec_7388f1c0_auto-caps-simdna` | 43.0 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 43.0 | `pcrec_b8337c33_auto-caps-simdna` | 43.0 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.43%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.3 | `pcrec_b8337c33_auto-caps-simdna` | 23.2 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.9 | `pcrec_7388f1c0_auto-caps-simdna` | 29.8 | 0.995x | no verdict: gap 0.54%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.1 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.2 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.996x | no verdict: gap 0.40%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.2 | `pcrec_7388f1c0_auto-caps-simdna` | 9.8 | 0.963x | no verdict: gap 3.69%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4.1 | `pcrec_7388f1c0_auto-caps-simdna` | 4.0 | 0.958x | no verdict: gap 4.24%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.4 | `pcrec_7388f1c0_auto-caps-simdna` | 8.3 | 0.987x | no verdict: gap 1.34%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.3 | `pcrec_b8337c33_auto-caps-simdna` | 8.3 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.4 | `pcrec_7388f1c0_auto-caps-simdna` | 10.0 | 0.969x | no verdict: gap 3.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.3 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.976x | no verdict: gap 2.42%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.0 | `pcrec_7388f1c0_auto-caps-simdna` | 8.0 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.0 | `pcrec_b8337c33_auto-caps-simdna` | 8.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19.2 | `pcrec_7388f1c0_auto-caps-simdna` | 19.2 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19.2 | `pcrec_b8337c33_auto-caps-simdna` | 19.2 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7.7 | `pcrec_7388f1c0_auto-caps-simdna` | 7.6 | 0.976x | no verdict: gap 2.38%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.7 | `pcrec_b8337c33_auto-caps-simdna` | 7.8 | 0.899x | no verdict: gap 10.13%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,745.9 | `pcrec_7388f1c0_auto-caps-simdna` | 17,678.9 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,720.0 | `pcrec_b8337c33_auto-caps-simdna` | 17,677.9 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,698.6 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.5 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,722.6 | `pcrec_b8337c33_auto-caps-simdna` | 17,703.1 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,221,767.3 | `pcrec_7388f1c0_auto-caps-simdna` | 3,162,541.5 | 0.982x | no verdict: gap 1.84%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 3,219,462.6 | `pcrec_b8337c33_auto-caps-simdna` | 3,162,106.4 | 0.982x | no verdict: gap 1.78%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,716.3 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `factored` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,732.0 | `pcrec_b8337c33_auto-caps-simdna` | 17,683.5 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.8 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.995x | no verdict: gap 0.53%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.1 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.994x | no verdict: gap 0.60%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.992x | no verdict: gap 0.79%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.988x | no verdict: gap 1.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.997x | no verdict: gap 0.35%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.6 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.1 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.993x | no verdict: gap 0.73%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.993x | no verdict: gap 0.66%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.987x | no verdict: gap 1.27%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.993x | no verdict: gap 0.72%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.996x | no verdict: gap 0.40%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.6 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.9 | `pcrec_7388f1c0_auto-caps-simdna` | 16.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.982x | no verdict: gap 1.75%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.6 | `pcrec_b8337c33_auto-caps-simdna` | 12.6 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.991x | no verdict: gap 0.95%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.1 | 0.993x | no verdict: gap 0.67%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.995x | no verdict: gap 0.52%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.1 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.996x | no verdict: gap 0.45%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.7 | `pcrec_7388f1c0_auto-caps-simdna` | 17.7 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.0 | `pcrec_b8337c33_auto-caps-simdna` | 13.0 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 6.5 | `pcrec_b8337c33_auto-caps-simdna` | 6.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.1 | `pcrec_7388f1c0_auto-caps-simdna` | 13.0 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.2 | `pcrec_7388f1c0_auto-caps-simdna` | 17.0 | 0.991x | no verdict: gap 0.85%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.6 | `pcrec_b8337c33_auto-caps-simdna` | 12.6 | 0.995x | no verdict: gap 0.51%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 614,985.7 | `pcrec_7388f1c0_auto-caps-simdna` | 614,889.3 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 576,758.3 | `pcrec_b8337c33_auto-caps-simdna` | 576,391.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,737.2 | `pcrec_7388f1c0_auto-caps-simdna` | 17,669.3 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 31,117.9 | `pcrec_7388f1c0_auto-caps-simdna` | 30,963.8 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 30,472.3 | `pcrec_b8337c33_auto-caps-simdna` | 30,309.3 | 0.995x | no verdict: gap 0.53%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,722.6 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.1 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `floor` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,737.8 | `pcrec_b8337c33_auto-caps-simdna` | 17,700.6 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.6 | `pcrec_7388f1c0_auto-caps-simdna` | 63.4 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 40.4 | `pcrec_7388f1c0_auto-caps-simdna` | 40.3 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 40.4 | `pcrec_b8337c33_auto-caps-simdna` | 40.3 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 18.5 | `pcrec_7388f1c0_auto-caps-simdna` | 18.3 | 0.992x | no verdict: gap 0.81%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 18.4 | `pcrec_b8337c33_auto-caps-simdna` | 18.3 | 0.996x | no verdict: gap 0.45%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.0 | `pcrec_7388f1c0_auto-caps-simdna` | 28.9 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 43.8 | `pcrec_7388f1c0_auto-caps-simdna` | 43.7 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 43.8 | `pcrec_b8337c33_auto-caps-simdna` | 43.6 | 0.995x | no verdict: gap 0.55%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 90.0 | `pcrec_7388f1c0_auto-caps-simdna` | 90.0 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 61.5 | `pcrec_7388f1c0_auto-caps-simdna` | 61.4 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 61.4 | `pcrec_b8337c33_auto-caps-simdna` | 61.4 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 18.4 | `pcrec_b8337c33_auto-caps-simdna` | 18.3 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.0 | `pcrec_7388f1c0_auto-caps-simdna` | 29.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.0 | `pcrec_b8337c33_auto-caps-simdna` | 28.9 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 31.2 | `pcrec_7388f1c0_auto-caps-simdna` | 31.1 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 46.9 | `pcrec_7388f1c0_auto-caps-simdna` | 46.8 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 46.8 | `pcrec_b8337c33_auto-caps-simdna` | 46.7 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 37.0 | `pcrec_7388f1c0_auto-caps-simdna` | 36.9 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 37.0 | `pcrec_b8337c33_auto-caps-simdna` | 37.0 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 74.4 | `pcrec_7388f1c0_auto-caps-simdna` | 74.3 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 74.5 | `pcrec_b8337c33_auto-caps-simdna` | 74.5 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.7 | `pcrec_b8337c33_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.19%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.6 | `pcrec_7388f1c0_auto-caps-simdna` | 56.4 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.6 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.7 | `pcrec_b8337c33_auto-caps-simdna` | 29.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.6 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 56.6 | `pcrec_b8337c33_auto-caps-simdna` | 56.5 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.2 | `pcrec_7388f1c0_auto-caps-simdna` | 12.1 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 12.0 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.5 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 35.5 | `pcrec_b8337c33_auto-caps-simdna` | 35.5 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 70.9 | `pcrec_7388f1c0_auto-caps-simdna` | 70.7 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.6 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 35.6 | `pcrec_b8337c33_auto-caps-simdna` | 35.5 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.8 | `pcrec_7388f1c0_auto-caps-simdna` | 29.7 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 57.0 | `pcrec_7388f1c0_auto-caps-simdna` | 56.6 | 0.994x | no verdict: gap 0.64%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 34.0 | `pcrec_7388f1c0_auto-caps-simdna` | 33.9 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 34.0 | `pcrec_b8337c33_auto-caps-simdna` | 33.9 | 0.997x | no verdict: gap 0.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 67.3 | `pcrec_7388f1c0_auto-caps-simdna` | 67.1 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 67.5 | `pcrec_b8337c33_auto-caps-simdna` | 67.0 | 0.992x | no verdict: gap 0.77%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.8 | `pcrec_7388f1c0_auto-caps-simdna` | 9.8 | 0.997x | no verdict: gap 0.30%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 9.8 | `pcrec_b8337c33_auto-caps-simdna` | 9.7 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.2 | `pcrec_7388f1c0_auto-caps-simdna` | 29.1 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.2 | `pcrec_b8337c33_auto-caps-simdna` | 28.9 | 0.989x | no verdict: gap 1.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.4 | 0.996x | no verdict: gap 0.43%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 35.7 | `pcrec_b8337c33_auto-caps-simdna` | 35.4 | 0.993x | no verdict: gap 0.73%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 70.9 | `pcrec_7388f1c0_auto-caps-simdna` | 70.8 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 34.0 | `pcrec_7388f1c0_auto-caps-simdna` | 34.0 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 34.0 | `pcrec_b8337c33_auto-caps-simdna` | 33.8 | 0.995x | no verdict: gap 0.50%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 67.0 | `pcrec_7388f1c0_auto-caps-simdna` | 67.0 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 67.1 | `pcrec_b8337c33_auto-caps-simdna` | 67.0 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 10.5 | `pcrec_7388f1c0_auto-caps-simdna` | 10.2 | 0.978x | no verdict: gap 2.23%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.4 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 38.8 | `pcrec_7388f1c0_auto-caps-simdna` | 38.6 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 38.7 | `pcrec_b8337c33_auto-caps-simdna` | 38.7 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 77.8 | `pcrec_7388f1c0_auto-caps-simdna` | 77.6 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 77.7 | `pcrec_b8337c33_auto-caps-simdna` | 77.7 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.7 | `pcrec_b8337c33_auto-caps-simdna` | 29.6 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.5 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 42.0 | `pcrec_b8337c33_auto-caps-simdna` | 41.8 | 0.996x | no verdict: gap 0.39%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 85.0 | `pcrec_7388f1c0_auto-caps-simdna` | 84.8 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.5 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 70.9 | `pcrec_7388f1c0_auto-caps-simdna` | 70.8 | 0.997x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.7 | `pcrec_7388f1c0_auto-caps-simdna` | 29.6 | 0.997x | no verdict: gap 0.27%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.7 | `pcrec_b8337c33_auto-caps-simdna` | 29.6 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 56.7 | `pcrec_7388f1c0_auto-caps-simdna` | 56.5 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 35.6 | `pcrec_7388f1c0_auto-caps-simdna` | 35.5 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 35.5 | `pcrec_b8337c33_auto-caps-simdna` | 35.5 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 70.9 | `pcrec_b8337c33_auto-caps-simdna` | 70.8 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 42.0 | `pcrec_b8337c33_auto-caps-simdna` | 42.0 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 85.0 | `pcrec_7388f1c0_auto-caps-simdna` | 84.8 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 85.1 | `pcrec_b8337c33_auto-caps-simdna` | 85.0 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 42.0 | `pcrec_7388f1c0_auto-caps-simdna` | 41.8 | 0.996x | no verdict: gap 0.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 42.0 | `pcrec_b8337c33_auto-caps-simdna` | 41.9 | 0.998x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 85.0 | `pcrec_7388f1c0_auto-caps-simdna` | 84.8 | 0.997x | no verdict: gap 0.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.3 | 1.000x | no verdict: gap 0.01%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.991x | no verdict: gap 0.86%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.2 | `pcrec_7388f1c0_auto-caps-simdna` | 25.0 | 0.994x | no verdict: gap 0.58%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.994x | no verdict: gap 0.65%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.992x | no verdict: gap 0.76%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 49.0 | `pcrec_7388f1c0_auto-caps-simdna` | 48.7 | 0.995x | no verdict: gap 0.48%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 49.0 | `pcrec_b8337c33_auto-caps-simdna` | 48.8 | 0.995x | no verdict: gap 0.50%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 25.1 | `pcrec_7388f1c0_auto-caps-simdna` | 25.1 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.1 | `pcrec_7388f1c0_auto-caps-simdna` | 16.1 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.2 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.998x | no verdict: gap 0.21%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.1 | 0.994x | no verdict: gap 0.57%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.1 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.2 | `pcrec_7388f1c0_auto-caps-simdna` | 29.0 | 0.995x | no verdict: gap 0.52%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 20.2 | `pcrec_7388f1c0_auto-caps-simdna` | 20.1 | 0.995x | no verdict: gap 0.54%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 20.3 | `pcrec_b8337c33_auto-caps-simdna` | 20.2 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.4 | `pcrec_7388f1c0_auto-caps-simdna` | 21.4 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 21.6 | `pcrec_b8337c33_auto-caps-simdna` | 21.4 | 0.993x | no verdict: gap 0.70%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.1 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.1 | `pcrec_b8337c33_auto-caps-simdna` | 23.1 | 0.997x | no verdict: gap 0.26%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 28.3 | `pcrec_7388f1c0_auto-caps-simdna` | 28.3 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 28.1 | `pcrec_b8337c33_auto-caps-simdna` | 28.0 | 0.997x | no verdict: gap 0.34%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 12.1 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.2 | `pcrec_b8337c33_auto-caps-simdna` | 12.0 | 0.984x | no verdict: gap 1.62%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 14.7 | `pcrec_7388f1c0_auto-caps-simdna` | 14.5 | 0.991x | no verdict: gap 0.95%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 14.7 | `pcrec_b8337c33_auto-caps-simdna` | 14.5 | 0.988x | no verdict: gap 1.23%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.8 | `pcrec_7388f1c0_auto-caps-simdna` | 23.6 | 0.992x | no verdict: gap 0.75%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.1 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.1 | `pcrec_b8337c33_auto-caps-simdna` | 23.1 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.3 | `pcrec_b8337c33_auto-caps-simdna` | 10.3 | 0.995x | no verdict: gap 0.47%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.5 | `pcrec_7388f1c0_auto-caps-simdna` | 63.4 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 63.7 | `pcrec_b8337c33_auto-caps-simdna` | 63.5 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 26.1 | `pcrec_b8337c33_auto-caps-simdna` | 26.1 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.6 | `pcrec_7388f1c0_auto-caps-simdna` | 7.5 | 0.878x | no verdict: gap 12.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.993x | no verdict: gap 0.74%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.9 | `pcrec_7388f1c0_auto-caps-simdna` | 21.9 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 14.5 | `pcrec_7388f1c0_auto-caps-simdna` | 14.3 | 0.987x | no verdict: gap 1.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.9 | 0.988x | no verdict: gap 1.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.0 | `pcrec_b8337c33_auto-caps-simdna` | 12.0 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 75.4 | `pcrec_7388f1c0_auto-caps-simdna` | 75.3 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 75.6 | `pcrec_b8337c33_auto-caps-simdna` | 75.3 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.9 | `pcrec_7388f1c0_auto-caps-simdna` | 8.9 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.9 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.992x | no verdict: gap 0.76%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 65.3 | `pcrec_7388f1c0_auto-caps-simdna` | 65.3 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 12.1 | `pcrec_7388f1c0_auto-caps-simdna` | 12.0 | 0.992x | no verdict: gap 0.84%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.0 | `pcrec_b8337c33_auto-caps-simdna` | 12.0 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 21.9 | `pcrec_7388f1c0_auto-caps-simdna` | 21.8 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.2 | `pcrec_b8337c33_auto-caps-simdna` | 23.1 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.4 | `pcrec_7388f1c0_auto-caps-simdna` | 23.1 | 0.989x | no verdict: gap 1.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.998x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 15.4 | `pcrec_7388f1c0_auto-caps-simdna` | 15.3 | 0.996x | no verdict: gap 0.38%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 15.4 | `pcrec_b8337c33_auto-caps-simdna` | 15.4 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.1 | `pcrec_7388f1c0_auto-caps-simdna` | 11.0 | 0.992x | no verdict: gap 0.83%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.9 | `pcrec_b8337c33_auto-caps-simdna` | 10.8 | 0.992x | no verdict: gap 0.81%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 73.1 | `pcrec_7388f1c0_auto-caps-simdna` | 72.9 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 14.7 | `pcrec_b8337c33_auto-caps-simdna` | 14.6 | 0.993x | no verdict: gap 0.65%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 57.9 | `pcrec_7388f1c0_auto-caps-simdna` | 57.9 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 58.6 | `pcrec_b8337c33_auto-caps-simdna` | 58.0 | 0.989x | no verdict: gap 1.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 11.1 | `pcrec_7388f1c0_auto-caps-simdna` | 10.9 | 0.980x | no verdict: gap 2.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 11.3 | `pcrec_b8337c33_auto-caps-simdna` | 11.2 | 0.997x | no verdict: gap 0.35%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 73.2 | `pcrec_7388f1c0_auto-caps-simdna` | 72.9 | 0.996x | no verdict: gap 0.37%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.997x | no verdict: gap 0.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 22.8 | `pcrec_b8337c33_auto-caps-simdna` | 22.6 | 0.993x | no verdict: gap 0.72%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.997x | no verdict: gap 0.29%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.9 | 0.982x | no verdict: gap 1.79%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.994x | no verdict: gap 0.63%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.3 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 0.996x | no verdict: gap 0.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.997x | no verdict: gap 0.32%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 19.3 | `pcrec_b8337c33_auto-caps-simdna` | 19.2 | 0.995x | no verdict: gap 0.46%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19,072.7 | `pcrec_7388f1c0_auto-caps-simdna` | 19,062.4 | 0.999x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19,071.2 | `pcrec_b8337c33_auto-caps-simdna` | 19,067.5 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,464.0 | `pcrec_7388f1c0_auto-caps-simdna` | 7,459.5 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 7,462.8 | `pcrec_b8337c33_auto-caps-simdna` | 7,462.5 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9,553.0 | `pcrec_7388f1c0_auto-caps-simdna` | 9,546.5 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 9,551.0 | `pcrec_b8337c33_auto-caps-simdna` | 9,549.0 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19,044.0 | `pcrec_7388f1c0_auto-caps-simdna` | 19,036.3 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19,045.1 | `pcrec_b8337c33_auto-caps-simdna` | 19,039.2 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,738.9 | `pcrec_7388f1c0_auto-caps-simdna` | 3,737.6 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 3,738.4 | `pcrec_b8337c33_auto-caps-simdna` | 3,738.3 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.2 | `pcrec_7388f1c0_auto-caps-simdna` | 16.2 | 0.996x | no verdict: gap 0.40%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.3 | `pcrec_b8337c33_auto-caps-simdna` | 16.2 | 0.994x | no verdict: gap 0.65%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4,786.0 | `pcrec_7388f1c0_auto-caps-simdna` | 4,782.2 | 0.999x | no verdict: gap 0.08%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 4,786.4 | `pcrec_b8337c33_auto-caps-simdna` | 4,784.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 7,646.3 | `pcrec_7388f1c0_auto-caps-simdna` | 7,643.7 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 7,646.8 | `pcrec_b8337c33_auto-caps-simdna` | 7,646.5 | 1.000x | no verdict: gap 0.00%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 9.0 | `pcrec_b8337c33_auto-caps-simdna` | 8.9 | 0.982x | no verdict: gap 1.76%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 24.6 | `pcrec_b8337c33_auto-caps-simdna` | 24.1 | 0.981x | no verdict: gap 1.89%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 34.1 | `pcrec_7388f1c0_auto-caps-simdna` | 33.9 | 0.994x | no verdict: gap 0.59%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 67.0 | `pcrec_7388f1c0_auto-caps-simdna` | 67.0 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 32.7 | `pcrec_b8337c33_auto-caps-simdna` | 32.5 | 0.996x | no verdict: gap 0.42%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 16.9 | `pcrec_7388f1c0_auto-caps-simdna` | 16.8 | 0.994x | no verdict: gap 0.58%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.9 | `pcrec_b8337c33_auto-caps-simdna` | 16.8 | 0.997x | no verdict: gap 0.30%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 12.1 | `pcrec_b8337c33_auto-caps-simdna` | 11.9 | 0.986x | no verdict: gap 1.41%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 28.3 | `pcrec_7388f1c0_auto-caps-simdna` | 28.3 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 52.9 | `pcrec_7388f1c0_auto-caps-simdna` | 52.8 | 0.999x | no verdict: gap 0.15%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 56.3 | `pcrec_b8337c33_auto-caps-simdna` | 56.2 | 0.998x | no verdict: gap 0.18%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 13.2 | `pcrec_7388f1c0_auto-caps-simdna` | 13.2 | 1.000x | no verdict: gap 0.04%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.3 | `pcrec_b8337c33_auto-caps-simdna` | 13.3 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 23.3 | `pcrec_7388f1c0_auto-caps-simdna` | 23.2 | 0.999x | no verdict: gap 0.06%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 23.3 | `pcrec_b8337c33_auto-caps-simdna` | 23.3 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 13.2 | `pcrec_b8337c33_auto-caps-simdna` | 13.2 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.9 | `pcrec_7388f1c0_auto-caps-simdna` | 29.8 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 30.2 | `pcrec_b8337c33_auto-caps-simdna` | 29.8 | 0.989x | no verdict: gap 1.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 32.6 | `pcrec_b8337c33_auto-caps-simdna` | 32.5 | 0.997x | no verdict: gap 0.31%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.4 | `pcrec_7388f1c0_auto-caps-simdna` | 63.3 | 0.998x | no verdict: gap 0.20%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.6 | 0.999x | no verdict: gap 0.10%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 32.6 | `pcrec_b8337c33_auto-caps-simdna` | 32.5 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.4 | `pcrec_7388f1c0_auto-caps-simdna` | 63.3 | 0.999x | no verdict: gap 0.13%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.5 | 0.998x | no verdict: gap 0.22%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 32.6 | `pcrec_b8337c33_auto-caps-simdna` | 32.5 | 0.998x | no verdict: gap 0.17%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 63.3 | `pcrec_b8337c33_auto-caps-simdna` | 63.3 | 1.000x | no verdict: gap 0.05%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.6 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 32.7 | `pcrec_b8337c33_auto-caps-simdna` | 32.5 | 0.995x | no verdict: gap 0.49%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 63.3 | `pcrec_7388f1c0_auto-caps-simdna` | 63.2 | 0.998x | no verdict: gap 0.23%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 63.4 | `pcrec_b8337c33_auto-caps-simdna` | 63.3 | 0.999x | no verdict: gap 0.11%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 32.6 | `pcrec_7388f1c0_auto-caps-simdna` | 32.6 | 0.999x | no verdict: gap 0.07%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 16.2 | `pcrec_b8337c33_auto-caps-simdna` | 16.1 | 0.999x | no verdict: gap 0.12%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 29.5 | `pcrec_7388f1c0_auto-caps-simdna` | 29.3 | 0.994x | no verdict: gap 0.56%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 29.5 | `pcrec_b8337c33_auto-caps-simdna` | 29.5 | 0.999x | no verdict: gap 0.09%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 10.1 | `pcrec_b8337c33_auto-caps-simdna` | 10.0 | 0.998x | no verdict: gap 0.24%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 4.1 | `pcrec_7388f1c0_auto-caps-simdna` | 4.1 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 4.1 | `pcrec_b8337c33_auto-caps-simdna` | 4.1 | 0.997x | no verdict: gap 0.25%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 9.0 | `pcrec_7388f1c0_auto-caps-simdna` | 8.4 | 0.933x | no verdict: gap 6.70%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_7388f1c0_auto-nocaps-simdna` | 8.0 | `pcrec_7388f1c0_auto-caps-simdna` | 8.0 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_7388f1c0_auto-nocaps-simdna` | 19.2 | `pcrec_7388f1c0_auto-caps-simdna` | 19.2 | 1.000x | no verdict: gap 0.02%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `match-compliance` | `pcrec_b8337c33_auto-nocaps-simdna` | 19.3 | `pcrec_b8337c33_auto-caps-simdna` | 19.2 | 0.997x | no verdict: gap 0.33%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `short-subject-search` | `pcrec_b8337c33_auto-nocaps-simdna` | 8.7 | `pcrec_b8337c33_auto-caps-simdna` | 8.6 | 0.982x | no verdict: gap 1.82%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,786,407.2 | `pcrec_7388f1c0_auto-caps-simdna` | 3,781,204.7 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 3,784,037.5 | `pcrec_b8337c33_auto-caps-simdna` | 3,782,965.9 | 1.000x | no verdict: gap 0.03%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,780.8 | `pcrec_7388f1c0_auto-caps-simdna` | 17,685.7 | 0.995x | no verdict: gap 0.54%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,793.3 | `pcrec_b8337c33_auto-caps-simdna` | 17,715.8 | 0.996x | no verdict: gap 0.44%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,746.6 | `pcrec_7388f1c0_auto-caps-simdna` | 17,682.7 | 0.996x | no verdict: gap 0.36%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_b8337c33_auto-nocaps-simdna` | 17,709.5 | `pcrec_b8337c33_auto-caps-simdna` | 17,680.9 | 0.998x | no verdict: gap 0.16%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 3,222,623.3 | `pcrec_7388f1c0_auto-caps-simdna` | 3,218,037.1 | 0.999x | no verdict: gap 0.14%; IQR n/a at subject grain; no null band (set grain only) |
| `orig` | `large-subject-throughput` | `pcrec_7388f1c0_auto-nocaps-simdna` | 17,739.4 | `pcrec_7388f1c0_auto-caps-simdna` | 17,689.6 | 0.997x | no verdict: gap 0.28%; IQR n/a at subject grain; no null band (set grain only) |

## Compile cost (by execution-model class; never pooled across classes)

### `compiled-aot`

- `pcrec_7388f1c0_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_7388f1c0_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-caps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `factored` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `factored` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `floor` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=memchr table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=end-minus-width, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `floor` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `orig` / `plain`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=unanchored prefilter=byte-class table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
- `pcrec_b8337c33_auto-nocaps-simdna` / `orig` / `whole-subject`: engine=dfa, sel=selected, entry=plain entry, vm_prefilter=-, dfa: scan=rev-end prefilter=none table=premultiplied offsets=none, edge=none, edges=0 (match: 0), start=reverse-pass, folds=0, match=unwrapped, rungs=-, fast tier=n/a (DFA: no tier), buffers=0 (DFA), frame=0 (DFA)
    - sel = pcrec's `RX_ENGINE_SEL`; `DFA fallback tripped` = sel not in (selected, forced), and NOTHING else -- since pcrec 263b013 ([LIM-1] / [OPT-4.1]) every fallback has its own token (`overflowed-dfa`, `overflowed-prefilter`, `collapsed-prefilter`, `declined-nullable`, `size-cap-retry`), the size-cap rescue included; at pcrec 96e44c2 that rescue stamped `sel=selected` and only its `lang=count-collapsed (size cap retry, ...)` clause says so.
    - edge = pcrec's `RX_DFA_SCAN_EDGE` ([OPT-5] STEP 1, abi 13+), how a DFA scan tests a SCAN EDGE's byte class: `range` = a contiguous run (subtract-and-compare against two immediates); `bitmap` = a non-contiguous class (a 256-byte membership read); `mixed` = one artifact whose machines took both forms; `none` = no collapsible run (an attempt/empty scan, or -fno-scan-edge).
    - edges = pcrec's `scan_edges` ([B32]): how many [OPT-5] SCAN EDGES this artifact's SEARCH-side machines carry (`rx_search`/`rx_prefilter`), the per-scan-iteration compare-count covariate `edge`'s single shape token cannot separate (I-33: the cost is one compare per edge per iteration); the `(match: M)` parenthetical, when carried, is the SAME count on the anchored `rx_match` machine, kept apart because the measured [OPT-EDGE] regression is search-band only. `0` is a real, recorded value.
    - start = pcrec's `RX_DFA_START` ([OPT-5] STEP 2, abi 16+), how the SEARCH entry recovers the match START: `pinned` = the forward machine's start state accepts unconditionally, so the match provably begins at `search_from` and THE ARTIFACT CARRIES NO REVERSE MACHINE at all (no reverse tables, accessor block or scan loop); `reverse-pass` = it carries one and walks it backwards from the match end. The two forms are ANSWER-IDENTICAL by contract -- `caps[0][0]`'s absolute offsets and the zero-length-match convention hold under both -- so this explains a row's SIZE and pass count, never its answer.
      - start=end-minus-width: every match is one fixed byte width W, so the start is the verified end minus W; NO reverse machine (abi 74, [START-LANDING])
    - folds = pcrec's `RX_DFA_UNIFORM_FOLDS` ([CC-DIFF] STEP 1, abi 17+): how many of this artifact's DFA tables (two per machine it contains -- forward always, reverse unless `start=pinned`, anchored under `match=unwrapped`; so 0..6) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `table=` keeps naming the encoding that was SELECTED, so `premultiplied` beside `folds=4` is an artifact carrying NO transition table at all -- a SIZE fact, never an answer one. `0` is a real, recorded value.

| pattern | form | testee | median total_ns | min | max | stddev | n costed | artifact bytes | emit bytes | code bytes | jitter | outcomes | emit-c ns | gcc ns | load ns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `factored` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 183,364,750.0 | 183,169,307.0 | 195,276,771.0 | 4,758,516.4 | 5 | 49,472 | 85,071 | 16,377 | 0.026 (max is trial 1) | compiled=5 | 9,485,779.0 | 173,662,847.0 | 221,130.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 178,806,804.0 | 172,689,703.0 | 187,691,044.0 | 6,452,235.3 | 5 | 37,040 | 42,326 | 16,649 | 0.036 | compiled=5 | 9,580,703.0 | 163,914,435.0 | 104,492.0 |
| `factored` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 180,362,043.0 | 179,151,257.0 | 191,095,150.0 | 4,622,010.6 | 5 | 49,472 | 84,868 | 16,170 | 0.026 (max is trial 1) | compiled=5 | 9,519,133.0 | 170,781,742.0 | 101,849.0 |
| `factored` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 182,921,516.0 | 176,804,644.0 | 195,038,624.0 | 7,408,307.9 | 5 | 37,040 | 42,143 | 16,462 | 0.040 | compiled=5 | 11,574,223.0 | 168,974,192.0 | 187,501.0 |
| `factored` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 212,941,107.0 | 190,569,548.0 | 220,192,927.0 | 12,562,001.7 | 5 | 49,472 | 85,071 | 16,377 | 0.059 (max is trial 1) | compiled=5 | 20,469,919.0 | 184,779,176.0 | 170,721.0 |
| `factored` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 173,326,956.0 | 172,159,429.0 | 191,772,975.0 | 7,466,710.7 | 5 | 37,040 | 42,326 | 16,649 | 0.043 (max is trial 1) | compiled=5 | 9,484,881.0 | 163,650,874.0 | 190,611.0 |
| `factored` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 178,865,825.0 | 178,528,114.0 | 197,356,525.0 | 7,561,763.1 | 5 | 49,472 | 84,868 | 16,170 | 0.042 | compiled=5 | 9,734,283.0 | 168,847,711.0 | 185,351.0 |
| `factored` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 172,855,484.0 | 169,225,045.0 | 185,951,632.0 | 6,589,063.4 | 5 | 37,040 | 42,143 | 16,462 | 0.038 | compiled=5 | 9,566,162.0 | 160,340,495.0 | 194,781.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 170,410,710.0 | 159,328,642.0 | 172,537,731.0 | 4,681,503.0 | 5 | 28,912 | 20,571 | 15,574 | 0.027 (max is trial 1) | compiled=5 | 2,203,342.0 | 167,694,325.0 | 105,822.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 160,104,955.0 | 155,466,821.0 | 172,009,567.0 | 5,785,265.1 | 5 | 28,808 | 19,474 | 15,916 | 0.036 (max is trial 1) | compiled=5 | 2,072,261.0 | 157,862,122.0 | 182,231.0 |
| `floor` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,718,038.0 | 157,746,712.0 | 169,966,727.0 | 4,395,334.5 | 5 | 28,912 | 20,571 | 15,574 | 0.026 | compiled=5 | 2,187,802.0 | 164,433,436.0 | 98,450.0 |
| `floor` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 166,959,222.0 | 160,255,104.0 | 168,755,031.0 | 3,588,272.0 | 5 | 28,808 | 19,474 | 15,916 | 0.021 | compiled=5 | 2,076,193.0 | 164,792,188.0 | 105,320.0 |
| `floor` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 163,842,254.0 | 158,834,258.0 | 169,532,206.0 | 3,656,715.2 | 5 | 28,768 | 17,888 | 14,557 | 0.022 | compiled=5 | 2,159,611.0 | 161,576,962.0 | 107,590.0 |
| `floor` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 164,567,540.0 | 158,942,109.0 | 168,981,751.0 | 3,274,019.5 | 5 | 28,808 | 19,474 | 15,916 | 0.020 | compiled=5 | 2,087,561.0 | 162,379,287.0 | 202,301.0 |
| `floor` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 160,812,067.0 | 153,906,159.0 | 165,340,862.0 | 3,678,380.7 | 5 | 28,768 | 17,888 | 14,557 | 0.023 | compiled=5 | 2,148,771.0 | 158,276,344.0 | 185,191.0 |
| `floor` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 169,634,056.0 | 162,871,298.0 | 172,958,303.0 | 3,507,701.0 | 5 | 28,808 | 19,474 | 15,916 | 0.021 | compiled=5 | 2,081,211.0 | 164,870,830.0 | 204,111.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-caps-simdna` | 182,954,393.0 | 178,691,073.0 | 190,871,808.0 | 4,569,826.4 | 5 | 49,440 | 84,644 | 16,117 | 0.025 | compiled=5 | 9,077,639.0 | 169,604,234.0 | 120,169.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-caps-simdna` | 174,538,901.0 | 173,513,145.0 | 177,638,087.0 | 1,417,535.9 | 5 | 32,904 | 41,919 | 16,409 | 0.008 (max is trial 1) | compiled=5 | 8,801,677.0 | 165,062,550.0 | 188,581.0 |
| `orig` | `plain` | `pcrec_7388f1c0_auto-nocaps-simdna` | 189,011,509.0 | 167,988,099.0 | 201,753,867.0 | 11,160,035.5 | 5 | 49,440 | 84,644 | 16,117 | 0.059 | compiled=5 | 9,155,119.0 | 172,079,120.0 | 103,900.0 |
| `orig` | `whole-subject` | `pcrec_7388f1c0_auto-nocaps-simdna` | 177,383,977.0 | 167,952,017.0 | 178,377,491.0 | 4,689,219.7 | 5 | 32,904 | 41,919 | 16,409 | 0.026 | compiled=5 | 8,791,647.0 | 159,103,649.0 | 100,500.0 |
| `orig` | `plain` | `pcrec_b8337c33_auto-caps-simdna` | 188,982,029.0 | 179,142,686.0 | 192,938,429.0 | 4,591,232.2 | 5 | 49,440 | 84,644 | 16,117 | 0.024 (max is trial 1) | compiled=5 | 10,521,636.0 | 170,299,529.0 | 194,311.0 |
| `orig` | `whole-subject` | `pcrec_b8337c33_auto-caps-simdna` | 175,038,255.0 | 168,213,757.0 | 178,014,081.0 | 3,662,283.4 | 5 | 32,904 | 41,919 | 16,409 | 0.021 | compiled=5 | 8,801,987.0 | 166,042,626.0 | 184,800.0 |
| `orig` | `plain` | `pcrec_b8337c33_auto-nocaps-simdna` | 188,146,249.0 | 178,986,966.0 | 217,998,886.0 | 14,085,930.2 | 5 | 49,440 | 84,644 | 16,117 | 0.075 | compiled=5 | 9,258,171.0 | 178,611,674.0 | 208,572.0 |
| `orig` | `whole-subject` | `pcrec_b8337c33_auto-nocaps-simdna` | 177,609,097.0 | 167,674,894.0 | 185,866,384.0 | 6,017,568.9 | 5 | 32,904 | 41,919 | 16,409 | 0.034 | compiled=5 | 8,825,699.0 | 165,175,871.0 | 96,901.0 |

